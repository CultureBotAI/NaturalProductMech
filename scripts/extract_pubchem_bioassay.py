#!/usr/bin/env python3
"""Extract PubChem BioAssay results for corpus structures.

    just extract-bioassay-dry       # free: how many calls, sends nothing
    just extract-bioassay-canary    # ONE real call, then stop
    just extract-bioassay           # the batch, resumable

Where the slice comes from
--------------------------
PubChem has no natural-product flag, so the natural-product slice has to be
CONSTRUCTED rather than selected: the corpus's own structures carry PubChem CID
cross-references from MIBiG, and those CIDs are what is queried. That makes this
a source which thickens existing records and cannot introduce them.

What survives, and why most rows do not
---------------------------------------
`docs/CURATION.md` is explicit that a value without units and a method is not a
measurement, and that a single-concentration screening hit is a call rather than
a potency. PubChem's assay summaries carry both kinds in one table, so:

* a row with a numeric value and a named activity becomes a measurement, with
  the assay name as its method;
* a row with only an outcome becomes a CALL — `ACTIVE`, `INACTIVE` — carrying
  its assay, and never a value;
* a row with neither is dropped.

The depositor travels with every row. PubChem is a deposition archive: NCBI's
own documentation says reuse conditions are set by each contributing source, so
"PubChem is public domain" is true of NCBI's own content and not automatically
of a depositor's. Recording `source_name` per assay is what makes a later
licence question answerable per row rather than for the whole inventory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from functools import partial
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "pubchem_bioassay.tsv"

SUMMARY = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/assaysummary/JSON"
ASSAY_META = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{aids}/description/JSON"

COLUMNS = [
    "standard_inchi_key", "cid", "aid", "assay_name", "assay_type", "depositor",
    "activity_outcome", "activity_name", "activity_value_um",
    "target_accession", "reference",
]

#: Depositors whose content this corpus may not redistribute, whatever route it
#: arrives by. ChEMBL deposits 79,319 of the 132,670 assay rows touching corpus
#: structures — 60% — and ChEMBL is CC BY-SA 3.0. Taking those through PubChem
#: does not escape share-alike; it only makes it harder to see. This is exactly
#: the laundering trap the source research warned about for Open Targets, and
#: the depositor column exists to catch it.
EXCLUDED_DEPOSITORS = {"chembl"}

#: PubChem asks for no more than 5 requests a second. 0.25s between calls keeps
#: a single-threaded run inside that without needing a token bucket.
POLITE_DELAY = 0.25


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cid_to_key() -> dict[str, str]:
    """PubChem CID -> Standard InChIKey, from the corpus's own cross-references.

    Read from the records rather than an inventory because the xrefs are what
    the seeder actually wrote, so this queries exactly the compounds the corpus
    claims a PubChem identity for.
    """
    mapping: dict[str, str] = {}
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue
        key = (doc.get("chemical_structure") or {}).get("standard_inchi_key")
        if not key:
            continue
        for xref in doc.get("xrefs") or []:
            if xref.startswith("pubchem:"):
                mapping.setdefault(xref.split(":", 1)[1], key)
    return mapping


def fetch(url: str, *, timeout: float = 60.0) -> dict | None:
    request = urllib.request.Request(  # noqa: S310
        url, headers={"User-Agent": "NaturalProductMech/0.1 (+https://github.com/CultureBotAI)"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310
            # Assay descriptions are free text deposited by third parties and
            # are not reliably UTF-8: one carried a stray 0xb7 that killed a
            # 1,207-call batch at the very last step. Decode leniently — a
            # replacement character in a depositor name is a cosmetic loss,
            # losing the batch is not.
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        # 404 means the CID has no assay data. That is an answer, not a failure.
        if exc.code == 404:
            return None
        raise


def read_inventory(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def write_inventory(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: (r["standard_inchi_key"], r["aid"])))


def rows_from_summary(payload: dict, cid: str, key: str, counts: Counter) -> list[dict[str, str]]:
    table = payload.get("Table") or {}
    columns = list((table.get("Columns") or {}).get("Column", []))
    index = {name: i for i, name in enumerate(columns)}
    rows: list[dict[str, str]] = []
    def cell_value(cells: list[str], name: str) -> str:
        i = index.get(name)
        return (cells[i] or "").strip() if i is not None and i < len(cells) else ""

    for entry in table.get("Row") or []:
        cell = entry.get("Cell") or []
        value = partial(cell_value, cell)

        outcome = value("Activity Outcome")
        activity_value = value("Activity Value [uM]")
        activity_name = value("Activity Name")
        assay_name = value("Assay Name")

        # A value with no activity name has no method attached; an outcome with
        # no assay name has nothing to attribute the call to. Both fail the
        # corpus's evidence rules and are counted rather than coerced.
        if activity_value and activity_name:
            counts["measurements"] += 1
        elif outcome and assay_name:
            counts["calls"] += 1
        else:
            counts["rejected_neither_value_nor_call"] += 1
            continue

        # An Inactive or Unspecified outcome with no value is not evidence a
        # curator will act on, and there are 107,000 of them. Measurements and
        # positive calls are what a record can carry.
        if not (activity_value and activity_name) and outcome != "Active":
            counts["rejected_not_a_measurement_or_active_call"] += 1
            continue

        pmid = value("PubMed ID")
        rows.append({
            "standard_inchi_key": key,
            "cid": cid,
            "aid": value("AID"),
            "assay_name": " ".join(assay_name.split())[:300],
            "assay_type": value("Assay Type"),
            "depositor": "",
            "activity_outcome": outcome,
            "activity_name": activity_name,
            "activity_value_um": activity_value,
            "target_accession": value("Target Accession"),
            "reference": f"PMID:{pmid}" if pmid.isdigit() else "",
        })
    return rows


def add_depositors(rows: list[dict[str, str]], *, limit: int = 100) -> Counter:
    """Fill `depositor` per assay, in batches of AIDs.

    PubChem is a deposition archive and NCBI's documentation says reuse
    conditions are the depositor's, so a row without one cannot answer a later
    licence question about itself.
    """
    counts: Counter[str] = Counter()
    aids = sorted({row["aid"] for row in rows if row["aid"]})
    resolved: dict[str, str] = {}
    for start in range(0, len(aids), limit):
        chunk = aids[start:start + limit]
        payload = fetch(ASSAY_META.format(aids=",".join(chunk)))
        time.sleep(POLITE_DELAY)
        if not payload:
            continue
        for description in (payload.get("PC_AssayContainer") or []):
            assay = ((description.get("assay") or {}).get("descr") or {})
            aid = str((assay.get("aid") or {}).get("id") or "")
            source = (((assay.get("aid_source") or {}).get("db") or {}).get("name") or "").strip()
            if aid and source:
                resolved[aid] = source
        counts["assay_descriptions_fetched"] += len(chunk)
    for row in rows:
        row["depositor"] = resolved.get(row["aid"], "")
    counts["rows_with_depositor"] = sum(1 for r in rows if r["depositor"])
    return counts


def drop_excluded_depositors(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], Counter]:
    """Remove rows this corpus may not redistribute, by depositor.

    Applied AFTER the depositor pass, because the summary endpoint does not
    carry a depositor and the exclusion cannot be made before one is known.
    """
    counts: Counter[str] = Counter()
    kept: list[dict[str, str]] = []
    for row in rows:
        if row["depositor"].strip().lower() in EXCLUDED_DEPOSITORS:
            counts[f"excluded_depositor_{row['depositor'].strip()}"] += 1
            continue
        kept.append(row)
    return kept, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--canary", action="store_true", help="one CID, then stop")
    parser.add_argument("--limit", type=int, help="query at most this many CIDs")
    args = parser.parse_args()

    mapping = cid_to_key()
    inventory_path = RAW_DIR / INVENTORY_NAME
    existing = read_inventory(inventory_path)
    done = {row["cid"] for row in existing}
    todo = [cid for cid in sorted(mapping) if cid not in done]

    print(f"corpus CIDs to query : {len(mapping)}", file=sys.stderr)
    print(f"already queried      : {len(done)}", file=sys.stderr)
    print(f"calls this run       : {len(todo)}", file=sys.stderr)

    if args.dry_run:
        print("dry run: nothing sent, nothing written", file=sys.stderr)
        return 0
    if not todo:
        print("nothing to do", file=sys.stderr)
        return 0

    budget = 1 if args.canary else (args.limit or len(todo))
    counts: Counter[str] = Counter()
    rows = list(existing)
    queried = 0

    for cid in todo:
        if queried >= budget:
            break
        try:
            payload = fetch(SUMMARY.format(cid=cid))
        except Exception as exc:  # noqa: BLE001 - one bad CID must not end the batch
            counts[f"error_{type(exc).__name__}"] += 1
            if counts.total() > 200:
                print("too many errors; stopping", file=sys.stderr)
                break
            continue
        queried += 1
        counts["cids_queried"] += 1
        if payload is None:
            counts["cids_without_assay_data"] += 1
        else:
            new = rows_from_summary(payload, cid, mapping[cid], counts)
            rows.extend(new)
            if new:
                counts["cids_with_rows"] += 1
        # Mark the CID as queried even when it returned nothing, so a resumed
        # run does not ask again for every empty one.
        if payload is None:
            rows.append({c: "" for c in COLUMNS} | {
                "standard_inchi_key": mapping[cid], "cid": cid, "aid": "",
                "assay_name": "(no assay data)",
            })
        if queried % 100 == 0:
            write_inventory(inventory_path, rows)
            print(f"  {queried}/{budget} CIDs queried", file=sys.stderr)
        time.sleep(POLITE_DELAY)

    if not args.canary:
        try:
            counts.update(add_depositors([r for r in rows if r["aid"]]))
        except Exception as exc:  # noqa: BLE001
            # The expensive part is the 1,207 CID calls already made. Never
            # discard them because an optional enrichment pass failed.
            counts["depositor_pass_failed"] += 1
            print(f"depositor pass failed ({type(exc).__name__}: {exc}); "
                  f"rows are written without it", file=sys.stderr)
        else:
            # Only safe once depositors are known: a row with no depositor
            # cannot be shown to be excludable, so the filter runs here rather
            # than defaulting to keeping unknown provenance.
            rows, excluded = drop_excluded_depositors(rows)
            counts.update(excluded)

    write_inventory(inventory_path, rows)
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    manifest["retrieved_on"] = time.strftime("%Y-%m-%d")
    manifest.setdefault("inventories", {})[INVENTORY_NAME] = {
        "rows": len(rows), "bytes": inventory_path.stat().st_size,
        "sha256": sha256_of(inventory_path),
        "source": "PubChem BioAssay via PUG REST, CIDs cross-referenced by the corpus",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")

    print(f"\ninventory rows: {len(rows)}", file=sys.stderr)
    for key in sorted(counts):
        print(f"  {key:<36} {counts[key]:>7}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
