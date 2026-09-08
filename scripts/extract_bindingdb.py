#!/usr/bin/env python3
"""Extract BindingDB's own-curated affinities as molecular targets.

    just extract-bindingdb-dry
    just extract-bindingdb
    just extract-bindingdb --offline

The licence is the whole reason this reads one specific file
---------------------------------------------------------------
BindingDB's terms state that data imported from ChEMBL keeps ChEMBL's CC BY-SA
3.0, while data curated by BindingDB staff is CC BY 3.0. Share-alike cannot be
seeded into this corpus, so only BindingDB's own curation is usable — and
BindingDB packages it separately, in ``BindingDB_BindingDB_Articles``.

**The filename is not the filter.** 429 rows inside that file are labelled
``ChEMBL`` in ``Curation/DataSource`` and are therefore share-alike. The
extractor filters on that column, not on which file the rows came in.

What a row becomes
------------------
A ``MolecularTarget`` with a measurement, a UniProt accession, the target's
source organism, and the PubMed citation. BindingDB records pH and temperature
per measurement, which almost nothing else in the landscape does, so they are
kept in the note rather than discarded.

An affinity value can carry a relational operator inside the numeric cell —
``>10000`` — so values are parsed rather than cast, and a qualifier travels with
the number instead of being flattened into it.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "bindingdb_targets.tsv"

RELEASE = "202609"
ARCHIVE = f"BindingDB_BindingDB_Articles_{RELEASE}_tsv.zip"
# The direct path. The SDFdownload.jsp link the download page renders is an
# interstitial that returns an HTML page, which a naive fetcher happily saves
# under a .zip name — see the content-type guard below.
URL = f"https://www.bindingdb.org/rwd/bind/downloads/{ARCHIVE}"

#: The only provenance this corpus may seed. Everything else in the file — 429
#: rows at this release — is ChEMBL-derived and share-alike.
CURATED_BY_BINDINGDB = "Curated from the literature by BindingDB"

#: Affinity columns, in the order a curator would prefer them: a dissociation
#: constant before a functional one, because Kd and Ki describe binding while
#: IC50 and EC50 depend on assay conditions.
MEASUREMENTS = [
    ("Kd (nM)", "KD"),
    ("Ki (nM)", "KI"),
    ("IC50 (nM)", "IC50"),
    ("EC50 (nM)", "EC50"),
]

COLUMNS = [
    "standard_inchi_key", "target_name", "target_organism", "uniprot",
    "measurement_type", "measurement_value_nm", "measurement_qualifier",
    "ph", "temperature_c", "reference", "curation_source",
]

_VALUE = re.compile(r"^\s*([<>~]?)\s*([0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?)\s*$")
_QUALIFIER = {"": "EQUAL", ">": "GREATER_THAN", "<": "LESS_THAN", "~": "APPROXIMATELY"}


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(*, offline: bool) -> Path:
    destination = DOWNLOAD_DIR / ARCHIVE
    if destination.exists():
        return destination
    if offline:
        raise SystemExit(f"missing {destination} and --offline was given")
    destination.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {URL}", file=sys.stderr)
    request = urllib.request.Request(  # noqa: S310
        URL, headers={"User-Agent": "NaturalProductMech/0.1 (+https://github.com/CultureBotAI)"})
    with urllib.request.urlopen(request) as response:  # noqa: S310
        # Fail loudly rather than saving an interstitial. BindingDB's rendered
        # download links go through a JSP that returns HTML with a 200, and a
        # fetcher that trusts the filename writes that HTML to a .zip and the
        # error surfaces later as a corrupt archive.
        content_type = response.headers.get("Content-Type", "")
        if "html" in content_type.lower():
            raise SystemExit(
                f"{URL} returned {content_type!r}, not an archive. The direct "
                f"download path has probably moved again."
            )
        with destination.open("wb") as out:
            while chunk := response.read(1 << 20):
                out.write(chunk)
    if not zipfile.is_zipfile(destination):
        destination.unlink()
        raise SystemExit(f"{URL} did not return a zip archive; removed the partial file")
    return destination


def corpus_keys() -> set[str]:
    path = RAW_DIR / "mibig_compounds.tsv"
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as fh:
        return {row["standard_inchi_key"] for row in csv.DictReader(fh, delimiter="\t")}


def parse_value(raw: str) -> tuple[float, str] | None:
    """A BindingDB affinity, with its relational operator kept as a qualifier.

    The operator lives inside the numeric cell upstream, so a naive float()
    either raises or, worse, silently drops the sign that says the measurement
    is a bound rather than a value.
    """
    match = _VALUE.match(raw or "")
    if not match:
        return None
    return float(match.group(2)), _QUALIFIER[match.group(1)]


def extract(path: Path, keys: set[str]) -> tuple[list[dict], Counter]:
    counts: Counter[str] = Counter()
    rows: list[dict] = []
    with zipfile.ZipFile(path) as archive:
        name = next(n for n in archive.namelist() if n.endswith(".tsv"))
        with archive.open(name) as handle:
            text = (line.decode("utf-8", "replace") for line in handle)
            reader = csv.DictReader(text, delimiter="\t")
            for row in reader:
                counts["rows_total"] += 1
                source = (row.get("Curation/DataSource") or "").strip()
                counts[f"curation_{source or 'blank'}"] += 1
                if source != CURATED_BY_BINDINGDB:
                    counts["rejected_not_bindingdb_curated"] += 1
                    continue
                key = (row.get("Ligand InChI Key") or "").strip()
                if key not in keys:
                    continue
                counts["rows_for_corpus_structures"] += 1

                measurement = None
                for column, kind in MEASUREMENTS:
                    parsed = parse_value(row.get(column) or "")
                    if parsed:
                        measurement = (kind, parsed[0], parsed[1])
                        break
                if not measurement:
                    counts["rejected_no_parseable_value"] += 1
                    continue

                pmid = (row.get("PMID") or "").strip()
                doi = (row.get("Article DOI") or "").strip()
                if pmid.isdigit():
                    reference = f"PMID:{pmid}"
                elif doi:
                    reference = f"DOI:{doi}"
                else:
                    counts["rejected_no_citation"] += 1
                    continue

                rows.append({
                    "standard_inchi_key": key,
                    "target_name": " ".join((row.get("Target Name") or "").split()),
                    "target_organism": " ".join(
                        (row.get("Target Source Organism According to Curator or DataSource")
                         or "").split()),
                    "uniprot": (row.get("UniProt (SwissProt) Primary ID of Target Chain 1")
                                or "").strip(),
                    "measurement_type": measurement[0],
                    "measurement_value_nm": f"{measurement[1]:g}",
                    "measurement_qualifier": measurement[2],
                    "ph": (row.get("pH") or "").strip(),
                    "temperature_c": (row.get("Temp (C)") or "").strip(),
                    "reference": reference,
                    "curation_source": source,
                })
                counts["kept"] += 1
    rows.sort(key=lambda r: (r["standard_inchi_key"], r["target_name"], r["reference"]))
    return rows, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    keys = corpus_keys()
    if not keys:
        raise SystemExit("no corpus structures yet; run the MIBiG extractor first")

    archive = download(offline=args.offline)
    rows, counts = extract(archive, keys)

    print("\nBindingDB:", file=sys.stderr)
    for key in sorted(counts):
        print(f"  {key:<48} {counts[key]:>8}", file=sys.stderr)
    structures = {r["standard_inchi_key"] for r in rows}
    with_uniprot = sum(1 for r in rows if r["uniprot"])
    print(f"\n  targets kept              : {len(rows)}", file=sys.stderr)
    print(f"  corpus structures covered : {len(structures)}", file=sys.stderr)
    print(f"  rows with a UniProt id    : {with_uniprot}", file=sys.stderr)

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
    manifest.setdefault("upstream", {})[ARCHIVE] = {
        "url": URL, "sha256": sha256_of(archive), "bytes": archive.stat().st_size,
    }
    manifest.setdefault("inventories", {})[INVENTORY_NAME] = {
        "rows": len(rows), "bytes": inventory.stat().st_size, "sha256": sha256_of(inventory),
        "source": f"BindingDB {RELEASE}, own-curated articles only (CC BY 3.0)",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"\nwrote {inventory.relative_to(REPO_ROOT)} ({len(rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
