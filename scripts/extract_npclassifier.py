#!/usr/bin/env python3
"""Classify corpus structures with NPClassifier into a committed inventory.

    just extract-npclassifier-dry            # free: how many calls, nothing sent
    just extract-npclassifier-canary         # ONE real call, then stop
    just extract-npclassifier                # the batch, resumable

Why this runs at extraction time and not at seed time
-----------------------------------------------------
``np_pathway`` is the filing decision, so it determines a record's directory
and its published URL. Computing it during seeding would put a network call
inside a pipeline whose whole point is that it runs offline from ``data/raw/``,
and would make the filing depend on whatever the service returned that day.

So the classification is a committed inventory keyed by Standard InChIKey, with
the model version recorded, exactly like every other input. A newer model is a
visible diff in a pull request, and `PATHS.tsv` pins each record's pathway so
even an accepted change moves records only when a curator says so.

Resumability
------------
The batch writes after every chunk and skips keys already in the inventory, so
an interrupted run costs the chunk in flight and nothing else. That matters
because this is thousands of calls against a public service.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
MIBIG_INVENTORY = RAW_DIR / "mibig_compounds.tsv"
INVENTORY_NAME = "npclassifier.tsv"

API = "https://npclassifier.gnps2.org/classify"
COLUMNS = [
    "standard_inchi_key",
    "smiles",
    "pathway_results",
    "superclass_results",
    "class_results",
    "is_glycoside",
    "model_version",
]

# The service publishes no version endpoint, so the inventory records the date
# the classification was taken alongside this label. A model change that the
# service does not announce would show up as a diff in the committed pathways,
# which is the observable we actually have.
MODEL_LABEL = "npclassifier.gnps2.org"


def structures_needing_classification() -> dict[str, str]:
    """Standard InChIKey -> one SMILES, from every committed structure source."""
    wanted: dict[str, str] = {}
    if MIBIG_INVENTORY.exists():
        with MIBIG_INVENTORY.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                key, smiles = row["standard_inchi_key"], row["smiles"]
                if key and smiles:
                    wanted.setdefault(key, smiles)
    return wanted


def read_inventory(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {row["standard_inchi_key"]: row for row in csv.DictReader(fh, delimiter="\t")}


def write_inventory(path: Path, rows: dict[str, dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for key in sorted(rows):
            writer.writerow(rows[key])


def classify(smiles: str, *, timeout: float = 30.0) -> dict:
    url = f"{API}?{urllib.parse.urlencode({'smiles': smiles})}"
    with urllib.request.urlopen(url, timeout=timeout) as response:  # noqa: S310
        return json.loads(response.read())


def row_from_result(key: str, smiles: str, result: dict, today: str) -> dict[str, str]:
    return {
        "standard_inchi_key": key,
        "smiles": smiles,
        # Every returned label is kept. Only the FILING decision has to be
        # single, and choose_pathway() in the seeder makes that call.
        "pathway_results": "|".join(result.get("pathway_results") or []),
        "superclass_results": "|".join(result.get("superclass_results") or []),
        "class_results": "|".join(result.get("class_results") or []),
        "is_glycoside": "true" if result.get("isglycoside") else "false",
        "model_version": f"{MODEL_LABEL}@{today}",
    }


def update_manifest(inventory: Path, rows: int) -> None:
    import hashlib

    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}

    # The one piece of provenance that cannot be recovered later: a sha256
    # says WHAT was fetched, nothing says WHEN. ChEBI replaces its flat files
    # in place, so for those the date is the only handle on the release (#29).
    manifest["retrieved_on"] = time.strftime("%Y-%m-%d")
    digest = hashlib.sha256(inventory.read_bytes()).hexdigest()
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": rows,
        "bytes": inventory.stat().st_size,
        "sha256": digest,
        "source": f"NPClassifier via {API}",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="count the work, send nothing")
    parser.add_argument("--canary", action="store_true", help="one real call, then stop")
    parser.add_argument("--limit", type=int, help="classify at most this many structures")
    parser.add_argument("--sleep", type=float, default=0.05,
                        help="seconds between calls (be kind to a public service)")
    args = parser.parse_args()

    today = time.strftime("%Y-%m-%d")
    inventory_path = RAW_DIR / INVENTORY_NAME
    have = read_inventory(inventory_path)
    wanted = structures_needing_classification()
    todo = {k: v for k, v in wanted.items() if k not in have}

    print(f"structures in the committed sources: {len(wanted)}", file=sys.stderr)
    print(f"already classified:                  {len(have)}", file=sys.stderr)
    print(f"calls this run would make:           {len(todo)}", file=sys.stderr)

    if args.dry_run:
        sample = next(iter(todo.items()), None)
        if sample:
            print(f"first call would be {sample[0]} -> {API}?smiles=...", file=sys.stderr)
        print("dry run: nothing sent, nothing written", file=sys.stderr)
        return 0

    if not todo:
        print("nothing to do", file=sys.stderr)
        return 0

    budget = 1 if args.canary else (args.limit or len(todo))
    done = 0
    failures: Counter[str] = Counter()

    for key, smiles in todo.items():
        if done >= budget:
            break
        try:
            result = classify(smiles)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            failures[type(exc).__name__] += 1
            # One bad structure must not end a batch of thousands.
            if failures.total() > 50:
                print("too many failures; stopping", file=sys.stderr)
                break
            continue
        have[key] = row_from_result(key, smiles, result, today)
        done += 1
        if done % 200 == 0:
            write_inventory(inventory_path, have)
            print(f"  {done}/{budget} classified", file=sys.stderr)
        time.sleep(args.sleep)

    write_inventory(inventory_path, have)
    update_manifest(inventory_path, len(have))

    pathways = Counter()
    multi = 0
    for row in have.values():
        results = [x for x in row["pathway_results"].split("|") if x]
        if len(results) == 1:
            pathways[results[0]] += 1
        else:
            multi += 1
            pathways["<multi or none>"] += 1
    print(f"\nclassified {done} this run; inventory now {len(have)} rows", file=sys.stderr)
    if failures:
        print(f"failures: {dict(failures)}", file=sys.stderr)
    print("pathway distribution:", file=sys.stderr)
    for pathway, count in pathways.most_common():
        print(f"  {pathway:<40} {count:>6}", file=sys.stderr)
    if multi:
        print(f"\n{multi} structures returned several pathways or none. Those file "
              f"UNCLASSIFIED and queue for a curator rather than being resolved "
              f"by array order.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
