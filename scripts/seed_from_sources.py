#!/usr/bin/env python3
"""Harmonize the committed inventories into one NaturalProductRecord per structure.

**M1 skeleton.** The identity model, the write path and the safety rails are
implemented and tested here; the extractors that produce `data/raw/` are M2, so
with no inventories on disk this reports an empty plan and writes nothing. That
is the intended state, not a stub to be quietly replaced: the rules below are
the contract M2's extractors have to satisfy.

    just seed                       # dry run: per-pathway counts, nothing written
    just seed-canary CHEBI:42355    # write exactly one record and validate it
    just seed-apply                 # write the whole corpus

Identity
--------
A record is ONE chemical structure. Resolution, in order:

1. A source concept whose ChEBI entry has a default structure grounds to that
   ChEBI CURIE (`grounding_status: EXACT`).
2. Otherwise the concept keeps a content-hashed
   `naturalproductmech:<source>-<hash>` CURIE (`grounding_status: MINTED`).
   The hash covers (source, source_id) and never the label, so an upstream
   label correction does not move the key that curation decisions are written
   against.
3. Concepts resolving to the same Standard InChIKey merge into one record
   carrying every source concept. That merge is the product.

A concept with no structure is NOT written: without an InChIKey there is
nothing to assert identity on, and a name is not a structure. MIBiG ships
SMILES and never an InChIKey, so keys are generated locally with the pinned
RDKit; 1,042 of its 5,443 compound records have no structure at all.

Origin
------
`producer_organisms` and `occurrences` are separate fields with separate
evidence bars, and **the seeder never promotes one to the other**. A MIBiG
locus grades a producer claim through `conf/producer_evidence.tsv`; a LOTUS
triple is an occurrence, whatever taxon it names.

Filing
------
`np_pathway` comes from the committed NPClassifier inventory, not a live call.
A multi-label or empty result files UNCLASSIFIED and queues the record rather
than resolving to a winner by array order — see PLAN.md 3.4.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from naturalproductmech.curate.curation_event import record_curation_event  # noqa: E402
from naturalproductmech.grading import load_evidence_map  # noqa: E402
from naturalproductmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_natural_product,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"

# MIBiG's cluster vocabulary -> the schema enum. Six values in 4.0; `alkaloid`
# was removed when compound classification was split from cluster
# classification. An unmapped value is dropped rather than guessed.
BGC_CLASS_MAP = {
    "PKS": "PKS",
    "NRPS": "NRPS",
    "ribosomal": "RIBOSOMAL",
    "terpene": "TERPENE",
    "saccharide": "SACCHARIDE",
    "other": "OTHER",
}

# Only cross-references whose prefix this corpus declares are carried through.
DB_ID_RE = re.compile(r"^(npatlas|pubchem|chembl|chebi|cyanometdb|lotus):[A-Za-z0-9._-]+$")

# One directory per NPClassifier pathway. UNCLASSIFIED is a real bucket, not an
# error state: it is where a multi-label result lands until a curator files it.
PATHWAY_DIRS = {
    "ALKALOIDS": "alkaloids",
    "AMINO_ACIDS_AND_PEPTIDES": "amino_acids_and_peptides",
    "CARBOHYDRATES": "carbohydrates",
    "FATTY_ACIDS": "fatty_acids",
    "POLYKETIDES": "polyketides",
    "SHIKIMATES_AND_PHENYLPROPANOIDS": "shikimates_and_phenylpropanoids",
    "TERPENOIDS": "terpenoids",
    "UNCLASSIFIED": "unclassified",
}

def mint_identifier(source: str, source_id: str) -> str:
    """Content-hashed CURIE for one source concept.

    Hashes (source, source_id) and never the label: an upstream label
    correction must not move the key `curation/decisions.tsv` rows are written
    against.
    """
    digest = hashlib.sha256(f"{source}\x00{source_id}".encode()).hexdigest()[:10]
    return f"naturalproductmech:{source.lower()}-{digest}"


def choose_pathway(pathway_results: list[str]) -> str:
    """The filing pathway, from NPClassifier's result array.

    One result files the record. Several or none files it UNCLASSIFIED, because
    picking by array order is how a corpus ends up asserting a classification
    nothing decided — AntibioticMech leaves its structural class empty for the
    same reason. Every returned label is still kept in `np_classification`.
    """
    if len(pathway_results) == 1:
        value = pathway_results[0].strip().upper().replace(" ", "_").replace("-", "_")
        return value if value in PATHWAY_DIRS else "UNCLASSIFIED"
    return "UNCLASSIFIED"


# Keys the seeder uses internally and strips before writing. A record's YAML
# must contain only schema fields, and closed validation would reject the rest.
INTERNAL_PREFIX = "_"


def record_path(pathway: str, slug: str) -> Path:
    """Where a record lives. The directory IS the filing decision."""
    return CORPUS_DIR / PATHWAY_DIRS.get(pathway, "unclassified") / f"{slug}.yaml"


def read_inventories() -> dict[str, list[dict[str, str]]]:
    """Every committed inventory in data/raw/, keyed by file stem.

    Empty at M1. The pipeline reads only this directory and never the network,
    which is what makes `just verify-corpus` and the offline test suite mean
    anything.
    """
    inventories: dict[str, list[dict[str, str]]] = {}
    for path in sorted(RAW_DIR.glob("*.tsv")):
        with path.open(newline="", encoding="utf-8") as fh:
            inventories[path.stem] = list(csv.DictReader(fh, delimiter="\t"))
    return inventories


def slugify(label: str, identifier: str) -> str:
    """A filesystem- and URL-safe slug for a record.

    Falls back to the identifier when a label slugifies to nothing, which
    happens for compounds named only with brackets or Greek letters. A slug is
    a published URL, so it is assigned once and locked in PATHS.tsv.
    """
    text = unicodedata.normalize("NFKD", label.lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    slug = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if not slug:
        slug = re.sub(r"[^a-z0-9]+", "-", identifier.lower()).strip("-")
    return slug[:80]


# A name from a paper's own numbering, not a compound name. Narrow on purpose:
# anything broader starts flagging real names such as "A-74528" or "BAA".
PAPER_INTERNAL_NAME = re.compile(r"(?i)^(compound|metabolite|unnamed|unknown)?\s*\d+[a-z]?$")


def choose_label(names: list[str]) -> tuple[str, list[str]]:
    """The record's label, and every other source name as a synonym.

    Chosen separately from the lead row, because the lead row is picked by
    producer-evidence strength and has nothing to say about naming. Without
    this, three records took a bare family name over the specific congener —
    `xiamycin` over `xiamycin A` — which labels one structure with what is
    really a class. Erythromycin came out right only because the accession
    tie-break happened to favour the better row (#16).

    Two rules, in order:

    1. **Specificity wins.** Drop any candidate that another candidate has as a
       prefix: `erythromycin` loses to `erythromycin A`, because the record is
       one structure and the bare name is the family.
    2. **Deterministic case.** Among names equal but for case, prefer the one
       that is not all-lowercase-by-accident, then sort. `Aflatoxin B1` and
       `aflatoxin B1` must not depend on entry order.

    Every discarded name is returned as a synonym rather than thrown away.
    """
    unique = sorted({n.strip() for n in names if n and n.strip()})
    if not unique:
        return "", []

    # Rule 1: a name another name extends is the less specific one.
    specific = [
        name for name in unique
        if not any(other.lower() != name.lower() and other.lower().startswith(name.lower() + " ")
                   for other in unique)
    ]
    candidates = specific or unique

    # Rule 2: collapse case variants deterministically.
    by_lower: dict[str, list[str]] = defaultdict(list)
    for name in candidates:
        by_lower[name.lower()].append(name)
    best_key = sorted(by_lower)[0]
    label = sorted(by_lower[best_key])[0]

    synonyms = [name for name in unique if name != label]
    return label, synonyms


def mibig_evidence(row: dict[str, str]) -> list[dict[str, str]]:
    """Claim-level evidence for one MIBiG row.

    Always a DATABASE_ASSERTION, whatever the reference points at. The corpus
    relays what MIBiG asserts; nobody here has read the paper, and
    docs/CURATION.md is explicit that a database assertion does not become the
    primary report merely because the database cites one. The level the
    citation came from travels in the note, so a curator can tell a
    compound-specific structure report from the entry's general reference.

    Returns a fresh list per call. Sharing one object between the producer and
    the gene cluster made PyYAML emit anchors and aliases, which no reader of a
    record should have to resolve.
    """
    level = row["reference_basis"].lower().replace("_", " ")
    return [{
        "reference": row["primary_reference"],
        "evidence_type": "DATABASE_ASSERTION",
        "notes": (f"MIBiG {row['mibig_accession']} entry version "
                  f"{row['entry_version']}; citation taken from the {level} level"),
    }]


def group_by_structure(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    """Group source rows by Standard InChIKey. That merge is the product."""
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = row.get("standard_inchi_key")
        if key:
            grouped[key].append(row)
    return grouped


def build_records(inventories: dict[str, list[dict[str, str]]]) -> list[dict[str, Any]]:
    """Harmonize the committed inventories into one record per structure.

    M2 covers MIBiG plus the NPClassifier filing inventory. ChEBI grounding,
    LOTUS occurrences and PubChem structures join here in later milestones; the
    shape below is what they slot into.

    Every record produced is MINTED, because MIBiG carries no ChEBI
    cross-reference for most compounds and this milestone does not yet read
    ChEBI. Grounding those is exactly what the next milestone is for, and
    `just worklist` will rank them.
    """
    mibig_rows = inventories.get("mibig_compounds") or []
    if not mibig_rows:
        return []

    classification = {
        row["standard_inchi_key"]: row
        for row in inventories.get("npclassifier") or []
    }

    records: list[dict[str, Any]] = []
    for key, rows in sorted(group_by_structure(mibig_rows).items()):
        # Prefer the row with the strongest producer evidence as the record's
        # spokesman for label and structure: same structure either way, but a
        # characterized entry is the better-curated one.
        rows = sorted(rows, key=lambda r: (
            0 if r["producer_evidence_basis"] == "BGC_CHARACTERIZED" else
            1 if r["producer_evidence_basis"] == "BGC_CORRELATED" else 2,
            r["mibig_accession"],
        ))
        lead = rows[0]
        label, synonyms = choose_label([r["compound_name"] for r in rows])
        label = label or key
        identifier = mint_identifier("MIBIG", lead["mibig_accession"] + ":" + lead["compound_index"])

        classified = classification.get(key)
        pathway_results = [
            x for x in (classified["pathway_results"].split("|") if classified else []) if x
        ]
        pathway = choose_pathway(pathway_results)

        doc: dict[str, Any] = {
            "identifier": identifier,
            "label": label,
            "chemical_structure": {
                "smiles": lead["smiles"],
                "standard_inchi": lead["standard_inchi"],
                "standard_inchi_key": key,
                "stereo_complete": lead["stereo_complete"] == "true",
                "structure_source": "MIBIG",
                "structure_source_id": f"mibig:{lead['mibig_accession']}",
            },
            "np_pathway": pathway,
        }
        if synonyms:
            doc["synonyms"] = [{"value": value, "synonym_type": "RELATED_SYNONYM",
                                "source": "mibig:" + lead["mibig_accession"]}
                               for value in synonyms]

        if classified:
            doc["np_classification"] = {
                "tool": "NPClassifier",
                "tool_version": classified["model_version"],
                "pathway_results": pathway_results,
                "superclass_results": [x for x in classified["superclass_results"].split("|") if x],
                "class_results": [x for x in classified["class_results"].split("|") if x],
                "is_glycoside": classified["is_glycoside"] == "true",
            }

        bgc_classes, compound_classes, xrefs = [], [], []
        producers: list[dict[str, Any]] = []
        clusters: list[dict[str, Any]] = []
        source_concepts: list[dict[str, Any]] = []

        for row in rows:
            accession = row["mibig_accession"]
            source_concepts.append({
                "source": "MIBIG",
                "source_id": accession,
                "source_label": row["compound_name"] or label,
                "source_version": row["entry_version"],
                "minted_identifier": mint_identifier(
                    "MIBIG", accession + ":" + row["compound_index"]),
            })

            for value in row["bgc_classes"].split("|"):
                mapped = BGC_CLASS_MAP.get(value.strip())
                if mapped and mapped not in bgc_classes:
                    bgc_classes.append(mapped)
            for value in row["compound_classes"].split("|"):
                if value and value not in compound_classes:
                    compound_classes.append(value)
            for value in row["database_ids"].split("|"):
                if value and value not in xrefs and DB_ID_RE.match(value):
                    xrefs.append(value)

            # Unconditional, and that is the point: MIBiG asserting a
            # compound-organism pair IS an assertion of production. What varies
            # is how well supported it is, which is what evidence_basis says.
            # grade_production has no withholding case for the same reason —
            # the one that used to exist, homology-based prediction, now lands
            # on the CLUSTER grade where it belongs (#20).
            producers.append({
                "taxon_id": row["taxon_id"],
                "taxon_label": row["taxon_label"],
                "evidence_basis": row["producer_evidence_basis"],
                "biosynthetic_gene_cluster": f"mibig:{accession}",
                "source": "MIBIG",
                "source_version": row["entry_version"],
                "notes": (
                    f"Locus evidence: {row['locus_evidence_methods'] or 'none stated'}. "
                    f"That evidence grades the LOCUS as "
                    f"{row.get('cluster_link_evidence_basis', 'CLUSTER_UNSTATED')}; this "
                    f"field grades the taxon claim, which is a different question."
                ),
                "evidence": mibig_evidence(row),
            })

            cluster: dict[str, Any] = {
                "accession": f"mibig:{accession}",
                "entry_version": row["entry_version"],
                "entry_status": row["entry_status"],
                "organism_taxon_id": row["taxon_id"],
                "organism_label": row["taxon_label"],
                "evidence": mibig_evidence(row),
            }
            if row["genome_accession"]:
                cluster["genome_accession"] = f"genbank:{row['genome_accession']}"
            for field, column in (("locus_from", "locus_from"), ("locus_to", "locus_to")):
                if row[column] and row[column].isdigit() and int(row[column]) > 0:
                    cluster[field] = int(row[column])
            if bgc_classes:
                cluster["bgc_class"] = list(bgc_classes)
            methods = [m for m in row["locus_evidence_methods"].split("|") if m]
            if methods:
                cluster["locus_evidence_methods"] = methods
            if row.get("cluster_link_evidence_basis"):
                cluster["link_evidence_basis"] = row["cluster_link_evidence_basis"]
            clusters.append(cluster)

        if bgc_classes:
            doc["bgc_class"] = bgc_classes
        if compound_classes:
            doc["compound_classes"] = compound_classes
        if xrefs:
            doc["xrefs"] = xrefs
        if producers:
            doc["producer_organisms"] = producers
        if clusters:
            doc["biosynthetic_gene_clusters"] = clusters

        doc["source_concepts"] = source_concepts
        doc["grounding_status"] = "MINTED"
        doc["grounding_notes"] = (
            "Minted from MIBiG. ChEBI grounding is a later milestone; most MIBiG "
            "compounds carry no ChEBI cross-reference."
        )
        doc["curation_status"] = "SEEDED"

        discussions: list[dict[str, Any]] = []

        # A paper-internal label identifies a structure only relative to one
        # paper's numbering. The name is not invented here — MIBiG's is kept —
        # but the record says it needs one, so it lands on the worklist rather
        # than being found by someone browsing (#17).
        if PAPER_INTERNAL_NAME.match(label):
            discussions.append({
                "discussion_id": "needs-a-name",
                "kind": "CURATION_TODO",
                "status": "OPEN",
                "prompt": (
                    f"This record is labelled {label!r}, which is a label from the "
                    f"cited paper's own numbering rather than a compound name. "
                    f"Resolve a name from the literature or a structure registry."
                ),
            })

        # A collision that survives must be visible, not silent.
        if len(rows) > 1 and len({r["mibig_accession"] for r in rows}) > 1:
            discussions.append({
                "discussion_id": "shared-structure",
                "kind": "CURATION_TODO",
                "status": "OPEN",
                "prompt": (
                    "This structure is reported by more than one MIBiG entry: "
                    + ", ".join(sorted({r["mibig_accession"] for r in rows}))
                    + ". Confirm they describe the same compound rather than an "
                    "upstream cross-reference error."
                ),
            })

        if discussions:
            doc["discussions"] = discussions

        doc["_slug"] = slugify(label, identifier)
        records.append(doc)

    # Slugs are published URLs and must be unique. A clash is resolved
    # deterministically rather than by whichever record was built first.
    seen: Counter[str] = Counter()
    for doc in sorted(records, key=lambda d: d["identifier"]):
        base = doc["_slug"]
        seen[base] += 1
        if seen[base] > 1:
            doc["_slug"] = f"{base}-{seen[base]}"
    return records


def write_records(records: list[dict[str, Any]], *, only: str | None = None,
                  limit: int | None = None) -> int:
    written = 0
    rows: list[dict[str, str]] = []
    for doc in records:
        if only and doc["identifier"] != only:
            continue
        if limit is not None and written >= limit:
            break
        slug = doc["_slug"]
        pathway = doc["np_pathway"]
        path = record_path(pathway, slug)
        payload = {k: v for k, v in doc.items() if not k.startswith(INTERNAL_PREFIX)}
        record_curation_event(
            payload,
            curator="seed_from_sources",
            action="SEEDED_FROM_SOURCES",
            changes="Seeded from the committed inventories in data/raw/.",
        )
        try:
            write_validated_natural_product(payload, path)
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            raise
        rows.append({
            "identifier": doc["identifier"],
            "np_pathway": pathway,
            "slug": slug,
            "path": str(path.relative_to(REPO_ROOT)),
        })
        written += 1
    # A partial run must not rewrite the whole lockfile: it would drop every
    # record the run did not touch. `--prune` is already refused on a partial
    # run for the same reason.
    if rows and only is None and limit is None:
        write_lockfile(rows)
    elif rows:
        print(f"partial run: wrote {len(rows)} record(s) but left PATHS.tsv alone",
              file=sys.stderr)
    return written


def write_lockfile(rows: list[dict[str, str]]) -> None:
    """PATHS.tsv locks identifier, filing pathway and slug together.

    The pathway lives here, not only in the record, because it is the pin that
    stops a later NPClassifier release moving a published URL. A disagreement
    between this file and the current inventory is a `pathway-drift` worklist
    entry for a curator, never an automatic move.
    """
    columns = ["identifier", "np_pathway", "slug", "path"]
    with PATHS_FILE.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["identifier"]))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write records (default: dry run)")
    parser.add_argument("--only", help="seed exactly one identifier — the canary")
    parser.add_argument("--limit", type=int, help="stop after this many records")
    parser.add_argument("--prune", action="store_true",
                        help="delete records the run did not rebuild")
    args = parser.parse_args()

    # A partial run must never prune: --prune with --only or --limit would
    # delete records the run never built.
    if args.prune and (args.only or args.limit):
        print("refusing --prune on a partial run (--only/--limit)", file=sys.stderr)
        return 2

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    budget = conf.get("record_budget")
    inventories = read_inventories()
    records = build_records(inventories)

    if budget and len(records) > budget:
        print(f"refusing to seed {len(records)} records over the budget of {budget} "
              f"in conf/sources.yaml — widening scope is a recorded decision",
              file=sys.stderr)
        return 2

    if not records:
        print("no inventories in data/raw/, so nothing to seed.")
        print("This is the expected M1 state: the extractors are M2 (PLAN.md section 7).")
        loaded = load_evidence_map()
        print(f"evidence methods loaded: {len(loaded)}; producer grades "
              f"{sorted({v['producer_basis'] for v in loaded.values() if v['producer_basis']})}; "
              f"cluster grades {sorted({v['cluster_basis'] for v in loaded.values()})}")
        return 0

    counts = Counter(doc["np_pathway"] for doc in records)
    for pathway, count in sorted(counts.items()):
        print(f"  {pathway:<34} {count:>6}")

    if not args.apply:
        print(f"dry run: {len(records)} records would be written")
        return 0

    written = write_records(records, only=args.only, limit=args.limit)
    print(f"wrote {written} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
