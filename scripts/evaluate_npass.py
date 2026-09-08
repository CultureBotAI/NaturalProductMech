#!/usr/bin/env python3
"""Measure what NPASS would add, without redistributing any of it.

    just evaluate-npass

An EVALUATOR, not an extractor. NPASS states no licence on any page checked —
homepage, about page, download page — and this corpus's record content is
CC BY 4.0, so `scripts/check_source_queue.py` refuses adoption under unverified
terms. That gate stays shut until someone resolves the licence.

What proceeds meanwhile is the work that does not require redistributing
anything: how many corpus records would gain a bioactivity or a target, whether
the join is by structure or by name, and what the data would look like once it
arrived. Counts are facts ABOUT the data, not the data, so this writes a report
to `research/` and never an inventory to `data/raw/`.

Doing it now rather than after a grant means the licence answer arrives to a
decision that is already made: adopt, or do not, on evidence.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"

STRUCTURES = DOWNLOAD_DIR / "NPASS3.0_naturalproducts_structure.txt"
SPECIES_PAIRS = DOWNLOAD_DIR / "NPASS3.0_naturalproducts_species_pair.txt"
ACTIVITIES = DOWNLOAD_DIR / "NPASS3.0_activities.txt"


def corpus_keys() -> set[str]:
    with (RAW_DIR / "mibig_compounds.tsv").open(newline="", encoding="utf-8") as fh:
        return {row["standard_inchi_key"] for row in csv.DictReader(fh, delimiter="\t")}


def read_tsv(path: Path):
    csv.field_size_limit(1 << 24)
    with path.open(newline="", encoding="utf-8", errors="replace") as fh:
        yield from csv.DictReader(fh, delimiter="\t")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    for path in (STRUCTURES, SPECIES_PAIRS, ACTIVITIES):
        if not path.exists():
            raise SystemExit(f"missing {path}; fetch NPASS into downloads/ first")

    keys = corpus_keys()

    # np_id -> InChIKey, for the structures this corpus actually holds. NPASS is
    # natively InChIKey-keyed, which is what makes it joinable at all: most of
    # the bioactivity landscape is name-keyed and would be a curation project.
    np_to_key: dict[str, str] = {}
    total_structures = 0
    for row in read_tsv(STRUCTURES):
        total_structures += 1
        key = (row.get("InChIKey") or "").strip()
        if key in keys:
            np_to_key[row["np_id"]] = key

    activity_counts: Counter[str] = Counter()
    activity_types: Counter[str] = Counter()
    with_units = with_target = with_assay_organism = 0
    activity_structures: set[str] = set()
    for row in read_tsv(ACTIVITIES):
        np_id = row.get("np_id")
        if np_id not in np_to_key:
            continue
        activity_counts["rows"] += 1
        activity_structures.add(np_to_key[np_id])
        activity_types[(row.get("activity_type") or "").strip() or "(blank)"] += 1
        if (row.get("activity_units") or "").strip():
            with_units += 1
        if (row.get("target_id") or "").strip():
            with_target += 1
        if (row.get("assay_organism") or "").strip():
            with_assay_organism += 1

    pair_rows = 0
    pair_structures: set[str] = set()
    pairs_with_reference = 0
    for row in read_tsv(SPECIES_PAIRS):
        np_id = row.get("np_id")
        if np_id not in np_to_key:
            continue
        pair_rows += 1
        pair_structures.add(np_to_key[np_id])
        if (row.get("ref_id") or "").strip():
            pairs_with_reference += 1

    print(f"NPASS structures in the release        : {total_structures}")
    print(f"corpus structures                      : {len(keys)}")
    print(f"joined by exact Standard InChIKey      : {len(np_to_key)}")
    print()
    print(f"activity rows for corpus structures    : {activity_counts['rows']}")
    print(f"  distinct structures with an activity : {len(activity_structures)}")
    print(f"  rows carrying units                  : {with_units}")
    print(f"  rows carrying a target id            : {with_target}")
    print(f"  rows carrying an assay organism      : {with_assay_organism}")
    print("  most common activity types:")
    for name, count in activity_types.most_common(8):
        print(f"    {name[:38]:<40} {count:>7}")
    print()
    print(f"species-pair rows for corpus structures: {pair_rows}")
    print(f"  distinct structures                  : {len(pair_structures)}")
    print(f"  rows carrying a reference            : {pairs_with_reference}")
    print()
    print("NOT WRITTEN. NPASS states no licence on any page checked, so nothing")
    print("from it enters data/raw/ or the corpus. These are counts about the")
    print("data, not the data; the gate opens only if the terms are resolved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
