#!/usr/bin/env python3
"""Extract CyanoMetDB isolation reports as occurrences.

    just extract-cyanometdb-dry
    just extract-cyanometdb
    just extract-cyanometdb --offline

Occurrences, not producers
--------------------------
CyanoMetDB records where a cyanobacterial metabolite was isolated from: a genus,
a species, often a strain designation, sometimes a named bloom or lake. That is
an isolation report, and an isolation report is an ``occurrence``.

It is tempting to read a strain designation as production by an axenic culture,
which would be a producer claim. It is not: a strain designation says the
compound was found in material from that strain, not that anyone demonstrated
the strain makes it, and CyanoMetDB's own ``Field_sample`` column shows how
often the material was a bloom rather than a culture at all. The research report
flagged the same thing — producer attribution here is "often to a genus or a
bloom sample rather than an axenic strain".

Taxon resolution is the binding constraint
------------------------------------------
CyanoMetDB carries no NCBI taxonomy identifiers, and ``Occurrence.taxon_id`` is
required, because a name-only organism is a name-only join. Rather than adopt a
taxonomy source for one input, names are resolved against taxa the corpus has
ALREADY resolved through MIBiG and LOTUS.

That resolution is species-level only. A row naming ``Genus species`` whose
genus alone is known would get a genus taxid under a species label — an
identifier and a label denoting different things, which is the defect
``test_taxon_labels_stay_consistent_for_an_id`` exists to catch. Those rows are
counted and dropped rather than approximated.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
import time
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "cyanometdb_occurrences.tsv"

RECORD = "13854577"
SOURCE_FILE = "CyanoMetDB_V03_2024.csv"
URL = f"https://zenodo.org/records/{RECORD}/files/{SOURCE_FILE}?download=1"

#: CyanoMetDB's header spells the InChIKey column with a lowercase L.
#: Reading it by the correct spelling silently yields nothing.
INCHIKEY_COLUMN = "InChlKey"

COLUMNS = [
    "standard_inchi_key", "compound_name", "taxon_id", "taxon_label",
    "strain", "field_sample", "nmr_used", "reference",
]


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(*, offline: bool) -> Path:
    destination = DOWNLOAD_DIR / SOURCE_FILE
    if destination.exists():
        return destination
    if offline:
        raise SystemExit(f"missing {destination} and --offline was given")
    destination.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {URL}", file=sys.stderr)
    request = urllib.request.Request(  # noqa: S310
        URL, headers={"User-Agent": "NaturalProductMech/0.1 (+https://github.com/CultureBotAI)"})
    with urllib.request.urlopen(request) as response, destination.open("wb") as out:  # noqa: S310
        while chunk := response.read(1 << 20):
            out.write(chunk)
    return destination


def corpus_keys() -> set[str]:
    path = RAW_DIR / "mibig_compounds.tsv"
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as fh:
        return {row["standard_inchi_key"] for row in csv.DictReader(fh, delimiter="\t")}


def resolved_genera(known: dict[str, str]) -> set[str]:
    """Genus names the corpus can resolve, for counting only.

    Deliberately NOT used to resolve a row: a genus match under a species label
    would put an identifier and a label that denote different things on one
    occurrence. It exists so the two rejection reasons can be told apart —
    "only the genus is known" is a different gap from "nothing is known", and
    the first is what adopting a taxonomy source would close.

    Hoisted out of the row loop, where it was rebuilt over all resolved names
    on every unresolved row (#32).
    """
    return {name.split()[0] for name in known}


def resolved_taxa() -> dict[str, str]:
    """Organism name -> NCBI taxid, from taxa the corpus already resolved.

    Species-level only, deliberately. Adding a genus fallback would let a row
    naming a species be written under a genus identifier.
    """
    known: dict[str, str] = {}
    for name, label_col, id_col in (
        ("lotus_occurrences.tsv", "organism_name", "taxon_id"),
        ("mibig_compounds.tsv", "taxon_label", "taxon_id"),
    ):
        path = RAW_DIR / name
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                label = (row[label_col] or "").strip()
                if label and row[id_col]:
                    known.setdefault(label.lower(), row[id_col])
    return known


def first_reference(row: dict[str, str]) -> str:
    pmid = (row.get("PubMedID_No1") or "").strip()
    if pmid.isdigit():
        return f"PMID:{pmid}"
    doi = (row.get("DOI_No1") or "").strip()
    return f"DOI:{doi}" if doi else ""


def extract(path: Path, keys: set[str], known: dict[str, str]) -> tuple[list[dict], Counter]:
    counts: Counter[str] = Counter()
    rows: list[dict] = []
    genera = resolved_genera(known)
    with path.open(newline="", encoding="utf-8", errors="replace") as fh:
        for row in csv.DictReader(fh):
            counts["rows_total"] += 1
            key = (row.get(INCHIKEY_COLUMN) or "").strip()
            if key not in keys:
                continue
            counts["rows_for_corpus_structures"] += 1

            genus = (row.get("Genus") or "").strip()
            species = (row.get("Species") or "").strip()
            label = f"{genus} {species}".strip()
            taxid = known.get(label.lower())
            if not taxid:
                # Counted separately because the two say different things: one
                # is an organism nothing has resolved, the other is one only a
                # genus is known for, and approximating the second would put a
                # genus id under a species label.
                if genus and genus.split("/")[0].lower() in genera:
                    counts["rejected_genus_level_only"] += 1
                else:
                    counts["rejected_unresolvable_taxon"] += 1
                continue

            reference = first_reference(row)
            if not reference:
                counts["rejected_no_citation"] += 1
                continue

            rows.append({
                "standard_inchi_key": key,
                "compound_name": " ".join((row.get("CompoundName") or "").split()),
                "taxon_id": f"NCBITaxon:{taxid}" if not taxid.startswith("NCBITaxon:") else taxid,
                "taxon_label": label,
                "strain": " ".join((row.get("Strain") or "").split()),
                "field_sample": " ".join((row.get("Field_sample") or "").split()),
                "nmr_used": (row.get("NMR_used") or "").strip(),
                "reference": reference,
            })
            counts["kept"] += 1
    rows.sort(key=lambda r: (r["standard_inchi_key"], r["taxon_id"], r["reference"]))
    return rows, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    keys = corpus_keys()
    if not keys:
        raise SystemExit("no corpus structures yet; run the MIBiG extractor first")

    path = download(offline=args.offline)
    known = resolved_taxa()
    rows, counts = extract(path, keys, known)

    print("\nCyanoMetDB:", file=sys.stderr)
    for key in sorted(counts):
        print(f"  {key:<40} {counts[key]:>7}", file=sys.stderr)
    print(f"\n  taxa already resolved by the corpus : {len(known)}", file=sys.stderr)
    print(f"  occurrences kept                    : {len(rows)}", file=sys.stderr)
    print(f"  structures covered                  : "
          f"{len({r['standard_inchi_key'] for r in rows})}", file=sys.stderr)

    if args.dry_run:
        print("\ndry run: nothing written", file=sys.stderr)
        return 0

    inventory = RAW_DIR / INVENTORY_NAME
    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    manifest["retrieved_on"] = time.strftime("%Y-%m-%d")
    manifest.setdefault("upstream", {})[SOURCE_FILE] = {
        "url": URL, "doi": f"10.5281/zenodo.{RECORD}",
        "sha256": sha256_of(path), "bytes": path.stat().st_size,
    }
    manifest.setdefault("inventories", {})[INVENTORY_NAME] = {
        "rows": len(rows), "bytes": inventory.stat().st_size, "sha256": sha256_of(inventory),
        "source": f"CyanoMetDB v03, Zenodo {RECORD} (CC BY 4.0)",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"\nwrote {inventory.relative_to(REPO_ROOT)} ({len(rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
