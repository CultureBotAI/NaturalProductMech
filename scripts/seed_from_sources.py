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

# PubChem's activity names to the schema's measurement vocabulary. An
# unmapped name keeps its value and units without claiming a type, rather
# than being coerced into the nearest one.
# Assay-name patterns that name an activity class unambiguously. Deliberately
# narrow: an unset class is honest, a guessed one is "computed presented as
# asserted" in a new place (#39).
ACTIVITY_CLASS_PATTERNS = [
    (re.compile(r"antibacterial|anti-bacterial|\bE\. ?coli\b|staphylococc|"
                r"antibiotic", re.I), "ANTIBACTERIAL"),
    (re.compile(r"antifungal|anti-fungal|candida|aspergillus", re.I), "ANTIFUNGAL"),
    (re.compile(r"antivir|anti-viral|hiv|influenza", re.I), "ANTIVIRAL"),
    (re.compile(r"antimalarial|plasmodium|trypanosom|leishman", re.I), "ANTIPARASITIC"),
    (re.compile(r"cytotox|tumor|tumour|cancer|nci-?60|growth inhibition|"
                r"antiproliferat", re.I), "CYTOTOXIC"),
    (re.compile(r"mutagen|carcinogen|ccris|genotox", re.I), "TOXIN"),
    (re.compile(r"inhibitors? of|inhibition of|\bIC50\b|\bKi\b|binding", re.I),
     "ENZYME_INHIBITOR"),
]


# AntibioticMech's filing class to this corpus's activity vocabulary. The
# mapping is deliberately lossless in both directions that matter: an
# unspecified antimicrobial stays unspecified rather than becoming
# antibacterial, and a mycobacterial claim keeps its own value rather than
# being widened. Anything unmapped is dropped rather than guessed.
SIBLING_ACTIVITY_CLASSES = {
    "ANTIBACTERIAL": "ANTIBACTERIAL",
    "ANTIFUNGAL": "ANTIFUNGAL",
    "ANTIMYCOBACTERIAL": "ANTIMYCOBACTERIAL",
    "ANTIVIRAL": "ANTIVIRAL",
    "ANTIPROTOZOAL": "ANTIPARASITIC",
    "ANTIMICROBIAL_UNSPECIFIED": "ANTIMICROBIAL_UNSPECIFIED",
}


def classify_activity(assay_name: str) -> str | None:
    """A BioactivityClassEnum value when the assay name says one plainly."""
    for pattern, label in ACTIVITY_CLASS_PATTERNS:
        if pattern.search(assay_name or ""):
            return label
    return None


MEASUREMENT_TYPES = {
    "IC50": "IC50", "EC50": "EC50", "KI": "KI", "KD": "KD",
    "MIC": "MIC", "GI50": "GI50", "AC50": "EC50",
}

# Only cross-references whose prefix this corpus declares are carried through.
DB_ID_RE = re.compile(r"^(npatlas|pubchem|chembl|chebi|cyanometdb|lotus):[A-Za-z0-9._-]+$")

# How many occurrences reach a record. The INVENTORY keeps all of them, so
# nothing is lost and the corpus still reproduces; this bounds what a curator
# has to read. Without it lupeol carried 925 occurrences in a 397 KB file,
# while the median record has one — and `curate-yaml-record` instructs a
# curator to read the entire YAML (#28).
MAX_OCCURRENCES_PER_RECORD = 25

# The same reasoning as occurrences, and the distribution is worse: one
# structure carries 960 assay rows while the median carries 11. The inventory
# keeps them all; a record keeps the ones a curator can read.
MAX_BIOACTIVITIES_PER_RECORD = 25

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


# A chemical name extends its parent with punctuation far more often than with
# a space: `tirucalla-7,24-dien-3β-ol`, `spirangien A1`, `xiamycin A`. Matching
# only on a space left the vague name winning, which is the defect #16 fixed
# for one delimiter and #22 found for the rest.
EXTENSION_CHARS = (" ", "-", ",", "(")


def _extends(longer: str, shorter: str) -> bool:
    """True when `longer` is `shorter` plus a specifying suffix."""
    a, b = longer.lower(), shorter.lower()
    return a != b and a.startswith(b) and a[len(b):len(b) + 1] in EXTENSION_CHARS


def choose_label(names: list[str], authoritative: str | None = None) -> tuple[str, list[str]]:
    """The record's label, and every other source name as a synonym.

    Chosen separately from the lead row, because the lead row is picked by
    producer-evidence strength and has nothing to say about naming.

    Three rules, in order:

    1. **Specificity wins.** Drop any candidate that another candidate extends:
       `erythromycin` loses to `erythromycin A`, and `tirucalla` loses to
       `tirucalla-7,24-dien-3β-ol`. The record is one structure and the bare
       name is the family.
    2. **The identity authority wins.** Among what survives, prefer
       `authoritative` — ChEBI's name, for a record grounded to a ChEBI term.
       Without this, a deterministic sort chose MIBiG's `β-carotein` over
       ChEBI's `β-carotene` because `i` sorts before `n` (#22).
    3. **Deterministic case.** Otherwise collapse case variants and sort, so
       `Aflatoxin B1` and `aflatoxin B1` do not depend on entry order.

    Every discarded name is returned as a synonym rather than thrown away.
    """
    unique = sorted({n.strip() for n in names if n and n.strip()})
    if not unique:
        return "", []

    specific = [
        name for name in unique
        if not any(_extends(other, name) for other in unique)
    ]
    candidates = specific or unique

    if authoritative and authoritative.strip() in candidates:
        label = authoritative.strip()
    else:
        by_lower: dict[str, list[str]] = defaultdict(list)
        for name in candidates:
            by_lower[name.lower()].append(name)
        label = sorted(by_lower[sorted(by_lower)[0]])[0]

    return label, [name for name in unique if name != label]


# Typographic variants that are not disagreements: a Unicode minus against a
# hyphen, a Greek Tau against a Latin T, and a leading stereo or positional
# descriptor. Each produced false controversies (#24).
# Applied AFTER lowercasing, so the Greek letters here are the lowercase
# codepoints: an uppercase Tau has already become a lowercase tau by then, and
# mapping only the uppercase form silently did nothing.
_NAME_NOISE = str.maketrans({
    "\u2212": "-", "\u2013": "-", "\u2014": "-",
    "\u03c4": "t", "\u03b1": "a", "\u03b2": "b", "\u03b3": "g",
})
# Only descriptors that do NOT change which compound is meant: optical
# rotation, absolute configuration, cis/trans. A Greek letter or a numeric
# locant is NOT stripped — alpha-amyrin and beta-amyrin are different
# compounds, and two sources disagreeing about that on one InChIKey is
# precisely the upstream error this check exists to surface.
_LEADING_DESCRIPTOR = re.compile(
    r"^(\([+\-\u2212\u00b1]\)-|\([0-9rszeRSZE'`,\- ]+\)-|[+\-\u2212\u00b1]-|cis-|trans-|rel-)+",
    re.IGNORECASE,
)


def _name_core(value: str) -> str:
    """A name reduced to what a disagreement would have to be about."""
    text = value.strip().lower().translate(_NAME_NOISE)
    text = " ".join(text.split())
    return _LEADING_DESCRIPTOR.sub("", text) or text


def names_disagree(label: str, other: str) -> bool:
    """True when two names for one structure differ substantively.

    Case, whitespace and the discarded-synonym cases are not disagreements. A
    grounded record whose sources call it two genuinely different things is,
    because one of the two upstream records then has the wrong structure —
    `astaxanthin` and `(2R,3S,3'S)-2-hydroxyastaxanthin` share an InChIKey in
    the committed inventories and are not the same compound.
    """
    a, b = _name_core(label), _name_core(other)
    if a == b or not a or not b:
        return False
    return not (_extends(a, b) or _extends(b, a))


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
    `just worklist` (#52) will rank them.
    """
    mibig_rows = inventories.get("mibig_compounds") or []
    if not mibig_rows:
        return []

    classification = {
        row["standard_inchi_key"]: row
        for row in inventories.get("npclassifier") or []
    }

    # ChEBI, keyed by structure. A key matching more than one 3-star entry is
    # NOT a resolution failure: ChEBI keeps a compound and its zwitterion as
    # separate entries sharing an InChIKey, deliberately. Picking one would
    # overrule the people who own the identifiers, so the record stays minted
    # and says the identity needs adjudicating.
    chebi_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("chebi_structures") or []:
        chebi_by_key[row["standard_inchi_key"]].append(row)

    origins_by_chebi: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("chebi_origins") or []:
        origins_by_chebi[row["chebi_id"]].append(row)

    # LOTUS: structure-organism-reference triples. Occurrences, never
    # producers — LOTUS reports that a compound was found in an organism and
    # does not say whether the organism makes it.
    lotus_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("lotus_occurrences") or []:
        lotus_by_key[row["standard_inchi_key"]].append(row)

    # CyanoMetDB isolation reports. Occurrences, not producers: a strain
    # designation says the compound was FOUND in material from that strain, not
    # that anyone showed the strain makes it.
    cyano_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("cyanometdb_occurrences") or []:
        cyano_by_key[row["standard_inchi_key"]].append(row)

    # BindingDB's own-curated affinities. Only rows its Curation/DataSource
    # column marks as BindingDB's own reach this inventory; the ChEMBL-derived
    # rows in the same file are share-alike and were filtered at extraction.
    targets_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("bindingdb_targets") or []:
        targets_by_key[row["standard_inchi_key"]].append(row)

    # PubChem BioAssay, already filtered at extraction to measurements and
    # positive calls, with ChEMBL-deposited rows excluded on licence.
    assays_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("pubchem_bioassay") or []:
        if row.get("aid"):
            assays_by_key[row["standard_inchi_key"]].append(row)

    # The sibling corpus, pinned. A compound in both keeps its antimicrobial
    # mechanism there and is linked from here, never copied.
    sibling_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventories.get("antibioticmech_inchikeys") or []:
        sibling_by_key[row["standard_inchi_key"]].append(row)

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
        minted = mint_identifier("MIBIG", lead["mibig_accession"] + ":" + lead["compound_index"])

        chebi_matches = chebi_by_key.get(key) or []
        name_candidates = [r["compound_name"] for r in rows]
        authoritative = chebi_matches[0]["name"] if len(chebi_matches) == 1 else None
        if authoritative:
            name_candidates.append(authoritative)
        label, synonyms = choose_label(name_candidates, authoritative=authoritative)
        label = label or key

        if len(chebi_matches) == 1:
            identifier = chebi_matches[0]["chebi_id"]
            grounding = "EXACT"
            grounding_notes = ""
        elif len(chebi_matches) > 1:
            identifier = minted
            grounding = "REVIEW_NEEDED"
            grounding_notes = (
                "This structure matches more than one 3-star ChEBI entry: "
                + ", ".join(m["chebi_id"] for m in chebi_matches)
                + ". ChEBI keeps such entries separate on purpose — a compound and "
                "its zwitterion share an InChIKey — so the identity is not picked "
                "here. A curator decides which term this record is."
            )
        else:
            identifier = minted
            grounding = "MINTED"
            grounding_notes = (
                "No 3-star ChEBI entry shares this structure, so the record keeps a "
                "content-hashed identifier."
            )

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
        if len(chebi_matches) == 1 and chebi_matches[0]["definition"]:
            doc["definition"] = chebi_matches[0]["definition"]
            doc["definition_source"] = chebi_matches[0]["chebi_id"]
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

        for match in chebi_matches:
            source_concepts.append({
                "source": "CHEBI",
                "source_id": match["chebi_id"],
                "source_label": match["name"],
                "source_version": f"{match['stars']}-star",
                "minted_identifier": mint_identifier("CHEBI", match["chebi_id"]),
            })

        # ChEBI's compound_origins records where a compound was FOUND. That is
        # an occurrence and never a producer claim: ChEBI is not asserting that
        # the organism biosynthesizes it, and the seeder does not promote.
        occurrences: list[dict[str, Any]] = []
        for match in chebi_matches:
            for origin in origins_by_chebi.get(match["chebi_id"]) or []:
                occurrence: dict[str, Any] = {
                    "taxon_label": origin["species_text"],
                    "source": "CHEBI",
                    "evidence": [{
                        "reference": f"PMID:{origin['source_accession']}"
                        if origin["source_accession"].isdigit() else origin["source_accession"],
                        "evidence_type": "DATABASE_ASSERTION",
                        "notes": f"ChEBI compound origin for {match['chebi_id']}",
                    }],
                }
                if origin["species_accession"].isdigit():
                    occurrence["taxon_id"] = f"NCBITaxon:{origin['species_accession']}"
                    occurrence["taxon_source"] = "NCBITaxon"
                if origin["strain_text"]:
                    occurrence["detection_context"] = origin["strain_text"]
                context = " ".join(x for x in (origin["component_text"], origin["comments"]) if x)
                if context:
                    occurrence["notes"] = context[:400]
                occurrences.append(occurrence)
        for row in lotus_by_key.get(key) or []:
            occurrence = {
                "taxon_id": row["taxon_id"],
                "taxon_label": row["organism_name"],
                "taxon_source": "NCBITaxon",
                "source": "LOTUS",
                "evidence": [{
                    "reference": f"DOI:{row['reference_doi']}",
                    "evidence_type": "DATABASE_ASSERTION",
                    "notes": (
                        "LOTUS structure-organism-reference triple. LOTUS reports that "
                        "the compound was found in the organism; it does not assert that "
                        "the organism produces it."
                    ),
                }],
            }
            if row["organism_wikidata"]:
                occurrence["notes"] = f"Wikidata organism {row['organism_wikidata']}"
            occurrences.append(occurrence)

        for row in cyano_by_key.get(key) or []:
            occurrence: dict[str, Any] = {
                "taxon_id": row["taxon_id"],
                "taxon_label": row["taxon_label"],
                "taxon_source": "NCBITaxon",
                "source": "CYANOMETDB",
                "evidence": [{
                    "reference": row["reference"],
                    "evidence_type": "DATABASE_ASSERTION",
                    "notes": (
                        "CyanoMetDB isolation report, manually curated from the primary "
                        "literature"
                        + (f"; structure confirmed by {row['nmr_used']}" if row["nmr_used"] else "")
                        + "."
                    ),
                }],
            }
            context = " ".join(
                x for x in (
                    f"strain {row['strain']}" if row["strain"] else "",
                    row["field_sample"] if row["field_sample"] else "",
                ) if x
            )
            if context:
                occurrence["detection_context"] = context[:200]
            occurrences.append(occurrence)

        # De-duplicate on (taxon, reference). Two routes produce exact
        # duplicates: a REVIEW_NEEDED record pulling origins from several ChEBI
        # entries that share one, and ChEBI and LOTUS citing the same paper
        # (#26). The same taxon from two DIFFERENT references is not a
        # duplicate — it is two independent reports, which is more evidence.
        deduped: list[dict[str, Any]] = []
        seen_occurrence: set[tuple[str, str]] = set()
        for occurrence in occurrences:
            signature = (
                occurrence.get("taxon_id") or occurrence["taxon_label"],
                occurrence["evidence"][0]["reference"],
            )
            if signature in seen_occurrence:
                continue
            seen_occurrence.add(signature)
            deduped.append(occurrence)

        # A taxon that is also a producer is CORROBORATION, not redundancy: the
        # occurrence carries its own independent citation. Said on the record so
        # a reader does not mistake it for a failure to deduplicate (#27).
        producer_taxa = {p["taxon_id"] for p in producers}
        for occurrence in deduped:
            if occurrence.get("taxon_id") in producer_taxa:
                note = ("This taxon is also recorded as a producer, from a different source "
                        "and citation. The two corroborate each other rather than duplicating.")
                occurrence["notes"] = (
                    f"{occurrence['notes']} {note}" if occurrence.get("notes") else note
                )

        if deduped:
            # Prefer occurrences that ADD something: a taxon not already
            # asserted as a producer carries information the record does not
            # otherwise have. Ordering is otherwise stable so the cap is
            # deterministic rather than dependent on source order.
            deduped.sort(key=lambda o: (
                o.get("taxon_id") in producer_taxa,
                o.get("taxon_id") or "",
                o["evidence"][0]["reference"],
            ))
            omitted = len(deduped) - MAX_OCCURRENCES_PER_RECORD
            if omitted > 0:
                kept_occurrences = deduped[:MAX_OCCURRENCES_PER_RECORD]
                note = (
                    f"{omitted} further cited occurrences are recorded in "
                    f"data/raw/lotus_occurrences.tsv and data/raw/chebi_origins.tsv "
                    f"but not written here: a record carrying hundreds of them cannot "
                    f"be reviewed. The inventories are the complete record."
                )
                kept_occurrences[-1]["notes"] = (
                    f"{kept_occurrences[-1]['notes']} {note}"
                    if kept_occurrences[-1].get("notes") else note
                )
                deduped = kept_occurrences
            doc["occurrences"] = deduped

        summary_classes: set[str] = set()
        bioactivities: list[dict[str, Any]] = []
        for row in assays_by_key.get(key) or []:
            observation: dict[str, Any] = {
                "assay": row["assay_name"] or f"PubChem AID {row['aid']}",
                "evidence": [{
                    "reference": row["reference"] or f"pubchem.aid:{row['aid']}",
                    "evidence_type": "DATABASE_ASSERTION",
                    "notes": (
                        f"PubChem BioAssay AID {row['aid']}"
                        + (f", deposited by {row['depositor']}" if row["depositor"] else "")
                        + (f"; assay type {row['assay_type']}" if row["assay_type"] else "")
                        + "."
                    ),
                }],
            }
            if row["activity_value_um"] and row["activity_name"]:
                measurement = MEASUREMENT_TYPES.get(row["activity_name"].upper())
                if measurement:
                    observation["measurement_type"] = measurement
                observation["value"] = float(row["activity_value_um"])
                observation["units"] = "uM"
            else:
                # A single-concentration screening hit is a CALL, never a
                # potency — docs/CURATION.md is explicit about it.
                observation["call"] = "ACTIVE"
            if row["target_accession"]:
                observation["target_enzyme"] = f"UniProtKB:{row['target_accession']}"
            activity_class = classify_activity(row["assay_name"])
            if activity_class:
                observation["activity_class"] = activity_class
            bioactivities.append(observation)

        if bioactivities:
            # Measurements before bare calls: a number with units is worth more
            # to a curator than a hit, and the cap should not spend itself on
            # the latter.
            bioactivities.sort(key=lambda b: (0 if "value" in b else 1, b["assay"]))
            omitted = len(bioactivities) - MAX_BIOACTIVITIES_PER_RECORD
            if omitted > 0:
                bioactivities = bioactivities[:MAX_BIOACTIVITIES_PER_RECORD]
                bioactivities[-1]["notes"] = (
                    f"{omitted} further PubChem assay results are in "
                    f"data/raw/pubchem_bioassay.tsv but not written here."
                )
            doc["bioactivities"] = bioactivities

            # bioactivity_summary is derived and must never float: PLAN.md 3.5
            # accepts a bioactivities item as backing, and there are now
            # classified items to derive from. Only classes actually present on
            # a written observation are summarised.
            summary_classes.update(b["activity_class"] for b in bioactivities
                                   if b.get("activity_class"))

        targets: list[dict[str, Any]] = []
        for row in targets_by_key.get(key) or []:
            context = ", ".join(
                part for part in (
                    f"pH {row['ph']}" if row["ph"] else "",
                    f"{row['temperature_c']} C" if row["temperature_c"] else "",
                ) if part
            )
            target: dict[str, Any] = {
                "target_label": row["target_name"] or "unnamed target",
                "target_type": "PROTEIN",
                "relation": "BINDS",
                "measurement_type": row["measurement_type"],
                "measurement_value": float(row["measurement_value_nm"]),
                "measurement_units": "nM",
                "source": "BINDINGDB",
                "evidence": [{
                    "reference": row["reference"],
                    "evidence_type": "DATABASE_ASSERTION",
                    "notes": (
                        "BindingDB own-curated affinity"
                        + (f"; measured at {context}" if context else "")
                        + f"; qualifier {row['measurement_qualifier']}."
                    ),
                }],
            }
            if row["uniprot"]:
                # An organism-specific accession is an EXAMPLE of a target, not
                # a target identity — docs/CURATION.md is explicit about it.
                target["protein_examples"] = [f"UniProtKB:{row['uniprot']}"]
            if row["target_organism"]:
                target["taxon_label"] = row["target_organism"]
            targets.append(target)
        if targets:
            doc["molecular_targets"] = targets

        links = [{
            "corpus": "AntibioticMech",
            "identifier": sibling["identifier"],
            "relation": "SAME_STRUCTURE",
            "basis": "SAME_INCHIKEY",
            "source_version": sibling["corpus_commit"][:12],
        } for sibling in sibling_by_key.get(key) or []]
        if links:
            doc["related_records"] = links

        # A shared structure's antimicrobial class comes from the sibling that
        # owns that claim, and ONLY the class: no targets, no resistance
        # determinants, no MIC spectra. PLAN.md 4.1 says the corpora join
        # rather than duplicate, and 3.5 accepts a sibling link as backing for
        # exactly this. The alternative was leaving 205 shared compounds
        # unclassified while the fleet already knew what they do.
        for sibling in sibling_by_key.get(key) or []:
            mapped = SIBLING_ACTIVITY_CLASSES.get(sibling.get("antimicrobial_class", ""))
            if mapped:
                summary_classes.add(mapped)

        if summary_classes:
            doc["bioactivity_summary"] = sorted(summary_classes)

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
        doc["grounding_status"] = grounding
        if grounding_notes:
            doc["grounding_notes"] = grounding_notes
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

        # One structure, two sources calling it genuinely different things:
        # somebody's structure is wrong upstream, and no naming rule should
        # quietly decide which (#22).
        if authoritative:
            for other in {r["compound_name"] for r in rows if r["compound_name"]}:
                if names_disagree(label, other):
                    discussions.append({
                        "discussion_id": "name-disagreement",
                        "kind": "CONTROVERSY",
                        "status": "OPEN",
                        "prompt": (
                            f"ChEBI calls this structure {authoritative!r} and MIBiG calls "
                            f"it {other!r}. They share a Standard InChIKey, so if the two "
                            f"names denote different compounds then one upstream record has "
                            f"the wrong structure. Check which."
                        ),
                    })
                    break

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
