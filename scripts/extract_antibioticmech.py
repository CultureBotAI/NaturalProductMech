#!/usr/bin/env python3
"""Pin AntibioticMech's structures so this corpus can link to them offline.

    just extract-antibioticmech-dry
    just extract-antibioticmech --checkout ../AntibioticMech

Two corpora in the fleet key on the same thing — a Standard InChIKey — so a
compound can be in both. When it is, the mechanism content belongs to
AntibioticMech and this corpus links rather than duplicating: no antimicrobial
targets, no resistance determinants, no MIC spectra written here.

The link has to reproduce offline like everything else, so it is not a live
lookup against a sibling checkout. This writes a committed inventory pinned to
one AntibioticMech commit. When that corpus moves, the pin is advanced in a
pull request and the diff shows exactly which links changed — which is the
point. A silent divergence between two corpora that claim to describe the same
structures is the failure this exists to prevent.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "antibioticmech_inchikeys.tsv"
DEFAULT_CHECKOUT = REPO_ROOT.parent / "AntibioticMech"

COLUMNS = ["standard_inchi_key", "identifier", "label", "slug", "corpus_commit"]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def corpus_commit(checkout: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def read_sibling(checkout: Path, commit: str) -> list[dict[str, str]]:
    corpus = checkout / "data" / "antibiotics"
    if not corpus.is_dir():
        raise SystemExit(f"no AntibioticMech corpus at {corpus}")
    rows: list[dict[str, str]] = []
    for path in sorted(corpus.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or "identifier" not in doc:
            continue
        key = (doc.get("chemical_structure") or {}).get("standard_inchi_key")
        if not key:
            continue
        rows.append({
            "standard_inchi_key": key,
            "identifier": doc["identifier"],
            "label": doc.get("label") or "",
            "slug": path.stem,
            "corpus_commit": commit,
        })
    rows.sort(key=lambda r: (r["standard_inchi_key"], r["identifier"]))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=DEFAULT_CHECKOUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    commit = corpus_commit(args.checkout)
    rows = read_sibling(args.checkout, commit)
    keys = {row["standard_inchi_key"] for row in rows}

    ours: set[str] = set()
    mibig = RAW_DIR / "mibig_compounds.tsv"
    if mibig.exists():
        with mibig.open(newline="", encoding="utf-8") as fh:
            ours = {row["standard_inchi_key"] for row in csv.DictReader(fh, delimiter="\t")}

    print(f"AntibioticMech at {commit[:12]}: {len(rows)} records, "
          f"{len(keys)} unique InChIKeys", file=sys.stderr)
    print(f"structures shared with this corpus: {len(keys & ours)}", file=sys.stderr)

    if args.dry_run:
        print("dry run: nothing written", file=sys.stderr)
        return 0

    inventory = RAW_DIR / INVENTORY_NAME
    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    manifest.setdefault("inventories", {})[INVENTORY_NAME] = {
        "rows": len(rows),
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": f"CultureBotAI/AntibioticMech at {commit}",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"wrote {inventory.relative_to(REPO_ROOT)} ({len(rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
