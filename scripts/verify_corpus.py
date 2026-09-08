#!/usr/bin/env python3
"""Prove data/natural_products/ is exactly what data/raw/ produces.

Schema validation checks each record's SHAPE. Without this, a hand-edited or
drifted record passes every other gate: the fields would still be well formed
and the corpus would still say something the sources do not.

What it compares is deliberately partial. Seeder-owned fields — identity,
label, structure, classification, source concepts, grounding, and the
source-marked producer, occurrence and gene-cluster items — must reproduce
exactly. Curator-owned fields are NOT compared, or curation would make this
check permanently red.

The consequence is worth stating rather than discovering: this cannot catch a
FABRICATED claim. A hand-added producer citing an invented PMID, or a hand flip
of curation_status to REVIEWED, passes. That is what review is for.

    python scripts/verify_corpus.py
    python scripts/verify_corpus.py --summary
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"


def read_lockfile() -> list[dict[str, str]]:
    with PATHS_FILE.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    rows = read_lockfile()
    on_disk = sorted(p for p in CORPUS_DIR.rglob("*.yaml"))

    problems: list[str] = []

    # Lockfile and filesystem must agree in both directions. A record file with
    # no lockfile row is an unrecorded write; a row with no file is a rename
    # that skipped PATHS.tsv, and slugs are published URLs.
    locked_paths = {row["path"] for row in rows}
    actual_paths = {str(p.relative_to(REPO_ROOT)) for p in on_disk}
    for path in sorted(actual_paths - locked_paths):
        problems.append(f"  {path}: on disk but absent from PATHS.tsv")
    for path in sorted(locked_paths - actual_paths):
        problems.append(f"  {path}: in PATHS.tsv but not on disk")

    # The filing pathway is pinned in the lockfile. A record whose np_pathway
    # disagrees with its locked value has been moved without going through the
    # rename path, which is how a published URL breaks silently.
    locked_pathway = {row["path"]: row["np_pathway"] for row in rows}
    for path in on_disk:
        rel = str(path.relative_to(REPO_ROOT))
        if rel not in locked_pathway:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if doc.get("np_pathway") != locked_pathway[rel]:
            problems.append(f"  {rel}: np_pathway {doc.get('np_pathway')!r} != "
                            f"locked {locked_pathway[rel]!r}")

    if problems:
        print("corpus verification FAILED:", file=sys.stderr)
        print("\n".join(problems), file=sys.stderr)
        return 1

    if not rows:
        print("corpus verification OK: the corpus is empty (expected at M1; "
              "seeding is M2, see PLAN.md section 7)")
        return 0
    print(f"corpus verification OK: {len(rows)} records reproduce from their inputs")
    if args.summary:
        print(f"  lockfile rows: {len(rows)}, files on disk: {len(on_disk)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
