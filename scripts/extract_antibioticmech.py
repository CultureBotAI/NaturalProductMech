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
import time
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "antibioticmech_inchikeys.tsv"
DEFAULT_CHECKOUT = REPO_ROOT.parent / "AntibioticMech"
PINS_PATH = REPO_ROOT / "conf" / "sibling_pins.yaml"
PIN_KEY = "antibioticmech"

COLUMNS = ["standard_inchi_key", "identifier", "label", "antimicrobial_class",
           "slug", "corpus_commit"]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checkout_head(checkout: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def pinned_commit() -> str:
    pins = yaml.safe_load(PINS_PATH.read_text(encoding="utf-8")) or {}
    commit = ((pins.get(PIN_KEY) or {}).get("commit") or "").strip()
    if not commit:
        raise SystemExit(f"no {PIN_KEY} commit pinned in {PINS_PATH}")
    return commit


def resolve_commit(checkout: Path, *, advance: bool) -> str:
    """The commit to read the sibling at.

    Reading the checkout's HEAD made the pin an OBSERVATION: re-running the
    extractor for an unrelated reason silently moved it, and with it the link
    set (#41). The pin is an input now, and moving it takes --advance-pin.
    """
    head = checkout_head(checkout)
    if advance:
        pins = yaml.safe_load(PINS_PATH.read_text(encoding="utf-8")) or {}
        pins.setdefault(PIN_KEY, {})["commit"] = head
        PINS_PATH.write_text(yaml.safe_dump(pins, sort_keys=False), encoding="utf-8")
        print(f"advanced the {PIN_KEY} pin to {head[:12]}", file=sys.stderr)
        return head

    commit = pinned_commit()
    if commit != head:
        print(f"sibling checkout is at {head[:12]}, reading the pinned "
              f"{commit[:12]} instead", file=sys.stderr)
        result = subprocess.run(
            ["git", "-C", str(checkout), "cat-file", "-e", f"{commit}^{{commit}}"],
            capture_output=True, text=True, check=False,
        )
        if result.returncode:
            raise SystemExit(
                f"the pinned commit {commit} is not in {checkout}. Fetch it, or "
                f"advance the pin deliberately with --advance-pin."
            )
    return commit


def read_sibling(checkout: Path, commit: str) -> list[dict[str, str]]:
    """Records as they were AT THE PINNED COMMIT, not in the working tree.

    Reading the tree would make the inventory depend on whatever the sibling
    checkout has staged, uncommitted or checked out, which is the same class of
    problem as reading its HEAD.
    """
    # -z, and NOT `.split()`. Without it git quote-escapes any path containing
    # a non-ASCII byte, so `α-gurjunene.yaml` comes back as
    # "data/.../\316\261-gurjunene.yaml" — trailing quote included — and a
    # `.endswith(".yaml")` filter drops it. That silently lost 85 of 2,920
    # sibling records, every one of them a compound with a Greek letter in its
    # name, which in natural-product chemistry is not a rare corner.
    listing = subprocess.run(
        ["git", "-C", str(checkout), "ls-tree", "-r", "-z", "--name-only", commit,
         "--", "data/antibiotics"],
        capture_output=True, check=True,
    ).stdout.decode("utf-8").split("\0")
    rows: list[dict[str, str]] = []
    for name in sorted(n for n in listing if n.endswith(".yaml")):
        blob = subprocess.run(
            ["git", "-C", str(checkout), "show", f"{commit}:{name}"],
            capture_output=True, check=True,
        ).stdout.decode("utf-8")
        doc = yaml.safe_load(blob)
        if not isinstance(doc, dict) or "identifier" not in doc:
            continue
        key = (doc.get("chemical_structure") or {}).get("standard_inchi_key")
        if not key:
            continue
        rows.append({
            "standard_inchi_key": key,
            "identifier": doc["identifier"],
            "label": doc.get("label") or "",
            # The sibling's filing class. Carried so this corpus can say a
            # shared compound is antibacterial WITHOUT copying the mechanism
            # that establishes it — PLAN.md 4.1, and the backing rule in 3.5
            # that accepts a sibling link.
            "antimicrobial_class": doc.get("antimicrobial_class") or "",
            "slug": Path(name).stem,
            "corpus_commit": commit,
        })
    rows.sort(key=lambda r: (r["standard_inchi_key"], r["identifier"]))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=DEFAULT_CHECKOUT)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--advance-pin", action="store_true",
                        help="move the pin to the checkout's HEAD, deliberately")
    args = parser.parse_args()

    commit = resolve_commit(args.checkout, advance=args.advance_pin)
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
    shared_classes = Counter(
        row["antimicrobial_class"] for row in rows if row["standard_inchi_key"] in ours)
    for name, count in shared_classes.most_common():
        print(f"    {name or '(none)':<28} {count:>5}", file=sys.stderr)

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

    # The one piece of provenance that cannot be recovered later: a sha256
    # says WHAT was fetched, nothing says WHEN. ChEBI replaces its flat files
    # in place, so for those the date is the only handle on the release (#29).
    manifest["retrieved_on"] = time.strftime("%Y-%m-%d")
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
