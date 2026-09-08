#!/usr/bin/env python3
"""Resolve the organism names other sources leave unresolved.

    just extract-taxonomy-dry
    just extract-taxonomy
    just extract-taxonomy --offline

Why this source exists
----------------------
``Occurrence.taxon_id`` is required, because a name-only organism is a name-only
join. Three adopted sources name organisms the corpus could not resolve and
whose rows were therefore dropped: 1,146 ChEBI origins with a non-numeric
species accession, 804 LOTUS triples whose organism has no NCBI id in the LOTUS
metadata, and 95 CyanoMetDB rows whose ``Genus species`` the corpus had not
already seen. That is roughly two thousand cited occurrences discarded over a
missing identifier rather than missing evidence.

NCBI Taxonomy is the authority those identifiers come from, and it is public
domain: "Information that is created by or for the US government on this site is
within the public domain. Public domain information on the National Library of
Medicine (NLM) Web pages may be freely distributed and copied."

What it emits, and what it deliberately does not
------------------------------------------------
A committed ``taxon_names.tsv`` mapping organism NAME to NCBI taxid, restricted
to the names the adopted sources actually use. The full ``names.dmp`` is about
250 MB and most of it names organisms this corpus will never mention; committing
it would put an inventory in ``data/raw/`` that nothing reads.

**No genus fallback.** A row naming ``Genus species`` whose species NCBI does not
know is left unresolved rather than written under the genus, because an
identifier and a label denoting different things is the defect
``test_taxon_labels_stay_consistent_for_an_id`` exists to catch. Adopting a
taxonomy source raises how many names resolve; it does not lower the bar for
what counts as resolved.

**Scientific names and synonyms only.** ``names.dmp`` carries several name
classes; ``includes``, ``in-part`` and ``blast name`` are deliberately excluded
because they are not assertions that the name denotes that taxon.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import sys
import tarfile
import time
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "taxon_names.tsv"

ARCHIVE = "taxdump.tar.gz"
URL = f"https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/{ARCHIVE}"

#: Name classes that assert the name denotes the taxon. `includes`, `in-part`
#: and `blast name` do not — they group or approximate — so a match on one of
#: those would resolve a name to a taxon nobody claimed it was.
USABLE_NAME_CLASSES = {"scientific name", "synonym", "equivalent name",
                       "genbank synonym", "genbank anamorph", "anamorph"}

COLUMNS = ["organism_name", "taxon_id", "name_class", "requested_by"]


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
    with urllib.request.urlopen(request) as response, destination.open("wb") as out:  # noqa: S310
        while chunk := response.read(1 << 20):
            out.write(chunk)
    return destination


def names_wanted() -> dict[str, set[str]]:
    """Organism names the adopted sources leave unresolved, by source.

    Read from the cached upstream files rather than from the committed
    inventories, so this extractor does not depend on the others having run —
    the rows it needs to resolve are precisely the ones they dropped.
    """
    wanted: dict[str, set[str]] = {}

    cyano = DOWNLOAD_DIR / "CyanoMetDB_V03_2024.csv"
    if cyano.exists():
        names = set()
        with cyano.open(newline="", encoding="utf-8", errors="replace") as fh:
            for row in csv.DictReader(fh):
                label = f"{(row.get('Genus') or '').strip()} {(row.get('Species') or '').strip()}"
                label = " ".join(label.split())
                if label:
                    names.add(label)
        wanted["cyanometdb"] = names

    origins = DOWNLOAD_DIR / "compound_origins.tsv.gz"
    if origins.exists():
        names = set()
        with gzip.open(origins, "rt", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                accession = (row.get("species_accession") or "").strip()
                species = (row.get("species_text") or "").strip()
                if species and not accession.isdigit():
                    names.add(species)
        wanted["chebi_origins"] = names

    lotus = DOWNLOAD_DIR / "260413_frozen.csv.gz"
    lotus_meta = DOWNLOAD_DIR / "260413_frozen_metadata.csv.gz"
    if lotus.exists() and lotus_meta.exists():
        csv.field_size_limit(1 << 24)
        # Only the organisms LOTUS itself cannot resolve. Requesting every
        # LOTUS name would fill this inventory with 34,000 rows the LOTUS
        # extractor never consults, which is the opposite of what an inventory
        # named "the names other sources leave unresolved" should hold.
        resolved_qids: set[str] = set()
        with gzip.open(lotus_meta, "rt", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh):
                ncbi = (row.get("organism_taxonomy_ncbiid") or "").strip()
                qid = (row.get("organism_wikidata") or "").strip()
                if qid and ncbi and ncbi.replace(".0", "").isdigit():
                    resolved_qids.add(qid)
        names = set()
        with gzip.open(lotus, "rt", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh):
                name = (row.get("organism_name") or "").strip()
                qid = (row.get("organism_wikidata") or "").strip()
                if name and qid not in resolved_qids:
                    names.add(name)
        wanted["lotus"] = names

    return wanted


def resolve(archive: Path, wanted: set[str]) -> tuple[dict[str, tuple[str, str]], Counter]:
    """Name -> (taxid, name_class), for the wanted names only.

    A scientific name wins over a synonym when both match, so a name that is one
    taxon's accepted name and another's synonym resolves to the accepted one.
    """
    counts: Counter[str] = Counter()
    lowered = {name.lower(): name for name in wanted}
    found: dict[str, tuple[str, str]] = {}

    with tarfile.open(archive, "r:gz") as tar:
        member = tar.extractfile("names.dmp")
        if member is None:
            raise SystemExit("names.dmp missing from the taxdump archive")
        for raw in member:
            line = raw.decode("utf-8", "replace")
            parts = [p.strip() for p in line.split("\t|")]
            if len(parts) < 4:
                continue
            taxid, name, _unique, name_class = parts[0], parts[1], parts[2], parts[3].rstrip("\t|\n")
            counts["names_dmp_rows"] += 1
            if name_class not in USABLE_NAME_CLASSES:
                continue
            original = lowered.get(name.lower())
            if original is None:
                continue
            existing = found.get(original)
            if existing is None or (name_class == "scientific name"
                                    and existing[1] != "scientific name"):
                found[original] = (taxid, name_class)
    counts["resolved"] = len(found)
    return found, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    wanted_by_source = names_wanted()
    if not wanted_by_source:
        raise SystemExit("no cached source files to collect names from")
    wanted = set().union(*wanted_by_source.values())

    print("names to resolve, by source:", file=sys.stderr)
    for source, names in sorted(wanted_by_source.items()):
        print(f"  {source:<16} {len(names):>7}", file=sys.stderr)
    print(f"  {'distinct total':<16} {len(wanted):>7}", file=sys.stderr)

    archive = download(offline=args.offline)
    found, counts = resolve(archive, wanted)

    print(f"\nnames.dmp rows read : {counts['names_dmp_rows']}", file=sys.stderr)
    print(f"resolved            : {len(found)} of {len(wanted)} "
          f"({100 * len(found) // max(len(wanted), 1)}%)", file=sys.stderr)
    by_class = Counter(name_class for _, name_class in found.values())
    for name_class, count in by_class.most_common():
        print(f"    {name_class:<24} {count:>7}", file=sys.stderr)
    for source, names in sorted(wanted_by_source.items()):
        gained = len(names & set(found))
        print(f"  would resolve for {source:<16} {gained:>7} of {len(names)}", file=sys.stderr)

    if args.dry_run:
        print("\ndry run: nothing written", file=sys.stderr)
        return 0

    rows = []
    for name, (taxid, name_class) in sorted(found.items()):
        requested = ",".join(sorted(s for s, names in wanted_by_source.items() if name in names))
        rows.append({
            "organism_name": name,
            "taxon_id": f"NCBITaxon:{taxid}",
            "name_class": name_class,
            "requested_by": requested,
        })

    inventory = RAW_DIR / INVENTORY_NAME
    inventory.parent.mkdir(parents=True, exist_ok=True)
    with inventory.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    manifest["retrieved_on"] = time.strftime("%Y-%m-%d")
    manifest.setdefault("upstream", {})[ARCHIVE] = {
        "url": URL, "sha256": sha256_of(archive), "bytes": archive.stat().st_size,
    }
    manifest.setdefault("inventories", {})[INVENTORY_NAME] = {
        "rows": len(rows), "bytes": inventory.stat().st_size, "sha256": sha256_of(inventory),
        "source": "NCBI Taxonomy taxdump, names.dmp (public domain)",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"\nwrote {inventory.relative_to(REPO_ROOT)} ({len(rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
