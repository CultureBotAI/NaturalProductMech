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
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from naturalproductmech.curate.curation_event import record_curation_event  # noqa: E402
from naturalproductmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_natural_product,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
RETIRED_FILE = CORPUS_DIR / "RETIRED.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
PRODUCER_EVIDENCE_PATH = REPO_ROOT / "conf" / "producer_evidence.tsv"

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

NOT_PRODUCER_GRADE = "NOT_PRODUCER_GRADE"


def mint_identifier(source: str, source_id: str) -> str:
    """Content-hashed CURIE for one source concept.

    Hashes (source, source_id) and never the label: an upstream label
    correction must not move the key `curation/decisions.tsv` rows are written
    against.
    """
    digest = hashlib.sha256(f"{source}\x00{source_id}".encode()).hexdigest()[:10]
    return f"naturalproductmech:{source.lower()}-{digest}"


def load_producer_evidence_map(path: Path = PRODUCER_EVIDENCE_PATH) -> dict[str, str]:
    """MIBiG locus-evidence method -> `evidence_basis`, from the committed TSV.

    In the config rather than in this file so the grading can be argued with.
    A method absent from the map is not silently treated as producer-grade;
    `grade_producer_evidence` refuses it.
    """
    with path.open(newline="", encoding="utf-8") as fh:
        return {row["mibig_method"]: row["evidence_basis"] for row in csv.DictReader(fh, delimiter="\t")}


def grade_producer_evidence(methods: list[str], evidence_map: dict[str, str]) -> str | None:
    """Best `evidence_basis` supported by a locus's evidence methods.

    Returns None when nothing in `methods` is producer-grade, which sends the
    claim to the worklist rather than into `producer_organisms`. An unknown
    method is treated as not producer-grade: a vocabulary that grew upstream
    should fail closed and be looked at, not admitted by default.
    """
    best: str | None = None
    for method in methods:
        basis = evidence_map.get(method)
        if basis is None or basis == NOT_PRODUCER_GRADE:
            continue
        if basis == "BGC_CHARACTERIZED":
            return basis
        best = best or basis
    return best


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


def build_records(inventories: dict[str, list[dict[str, str]]]) -> list[dict[str, Any]]:
    """Harmonize inventories into records.

    M2 implements this over the MIBiG, ChEBI, LOTUS, PubChem and NPClassifier
    inventories. It returns an empty list until those exist, so `just seed`
    reports an empty plan rather than pretending to have one.
    """
    if not inventories:
        return []
    raise NotImplementedError(
        "No harmonizer yet: the extractors that produce data/raw/ are M2 "
        "(PLAN.md section 7). Inventories are present, so this is a real gap "
        f"rather than the empty M1 state: {sorted(inventories)}"
    )


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
        print(f"producer-evidence grades loaded: "
              f"{sorted(set(load_producer_evidence_map().values()))}")
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
