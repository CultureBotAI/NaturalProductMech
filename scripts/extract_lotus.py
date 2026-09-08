#!/usr/bin/env python3
"""Extract LOTUS structure-organism-reference triples as occurrences.

    just extract-lotus-dry     # free once cached: counts, writes nothing
    just extract-lotus
    just extract-lotus --offline

What LOTUS is, and what it is not
---------------------------------
Every LOTUS row is a (structure, organism, reference) triple: this compound was
reported in this organism, in this paper. That is an **occurrence** and never a
producer claim. An occurrence may reflect biosynthesis, symbiosis, diet, uptake,
contamination or a degradation product, and LOTUS does not say which — so these
rows fill ``occurrences`` and nothing promotes them to ``producer_organisms``.

That distinction is why the corpus has two fields, and LOTUS is the source that
makes it load-bearing: it is far larger than every producer source combined.

Scope
-----
``producer_scope`` in ``conf/sources.yaml`` filters PRODUCERS, not occurrences
(PLAN.md 2.4). A cited isolation report is evidence about a compound the corpus
already holds, and dropping it because the host is a plant would discard
evidence rather than narrow scope. So no taxon filter is applied here; what
bounds the work is the corpus itself, since only structures already present can
gain an occurrence.

The route decides the licence
-----------------------------
LOTUS is distributed through Wikidata, whose main-namespace structured data is
CC0, and as frozen exports on Zenodo, which are tagged CC BY 4.0. This reads the
Zenodo export, because a committed inventory needs a release identity to record
in ``data/raw/MANIFEST.yaml`` and a SPARQL query has none. So the terms that
apply here are CC BY 4.0, and ``ATTRIBUTION.md`` says so.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import sys
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "lotus_occurrences.tsv"

RECORD = "19360665"
BASE = f"https://zenodo.org/records/{RECORD}/files/"
TRIPLES = "260413_frozen.csv.gz"
METADATA = "260413_frozen_metadata.csv.gz"

COLUMNS = [
    "standard_inchi_key", "organism_name", "taxon_id", "organism_wikidata",
    "reference_doi", "structure_wikidata",
]


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(name: str, *, offline: bool) -> Path:
    destination = DOWNLOAD_DIR / name
    if destination.exists():
        return destination
    if offline:
        raise SystemExit(f"missing {destination} and --offline was given")
    destination.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {BASE}{name}", file=sys.stderr)
    request = urllib.request.Request(  # noqa: S310
        BASE + name + "?download=1",
        headers={"User-Agent": "NaturalProductMech/0.1 (+https://github.com/CultureBotAI)"},
    )
    with urllib.request.urlopen(request) as response, destination.open("wb") as out:  # noqa: S310
        while chunk := response.read(1 << 20):
            out.write(chunk)
    return destination


def corpus_keys() -> set[str]:
    """Structures the corpus already holds. LOTUS can add occurrences to those
    and nothing else: it is an occurrence source, not an admission source."""
    keys: set[str] = set()
    for name in ("mibig_compounds.tsv",):
        path = RAW_DIR / name
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            keys |= {row["standard_inchi_key"] for row in csv.DictReader(fh, delimiter="\t")}
    return keys


def read_csv_gz(path: Path):
    csv.field_size_limit(1 << 24)
    with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as fh:
        yield from csv.DictReader(fh)


def extract_triples(path: Path, keys: set[str]) -> tuple[list[dict], Counter, set[str]]:
    counts: Counter[str] = Counter()
    rows: list[dict] = []
    organisms: set[str] = set()
    seen: set[tuple[str, str, str]] = set()
    for row in read_csv_gz(path):
        counts["triples_total"] += 1
        key = (row.get("structure_inchikey") or "").strip()
        if key not in keys:
            continue
        counts["triples_for_corpus_structures"] += 1
        doi = (row.get("reference_doi") or "").strip()
        if not doi:
            # Occurrence.evidence is required. An uncited occurrence is not an
            # occurrence this corpus can carry.
            counts["rejected_no_reference"] += 1
            continue
        organism = (row.get("organism_name") or "").strip()
        qid = (row.get("organism_wikidata") or "").strip()
        if not organism:
            counts["rejected_no_organism"] += 1
            continue
        signature = (key, qid or organism, doi)
        if signature in seen:
            counts["rejected_duplicate"] += 1
            continue
        seen.add(signature)
        organisms.add(qid)
        rows.append({
            "standard_inchi_key": key,
            "organism_name": organism,
            "taxon_id": "",
            "organism_wikidata": qid,
            "reference_doi": doi,
            "structure_wikidata": (row.get("structure_wikidata") or "").strip(),
        })
    return rows, counts, organisms


def resolve_taxids(path: Path, organisms: set[str]) -> dict[str, str]:
    """Wikidata QID -> NCBI taxonomy id, for the organisms actually matched.

    The metadata table is 90 MB compressed and mostly about structures this
    corpus will never hold, so it is streamed and only the needed organisms are
    kept.
    """
    taxids: dict[str, str] = {}
    for row in read_csv_gz(path):
        qid = (row.get("organism_wikidata") or "").strip()
        if not qid or qid in taxids or qid not in organisms:
            continue
        ncbi = (row.get("organism_taxonomy_ncbiid") or "").strip()
        if ncbi and ncbi.replace(".0", "").isdigit():
            taxids[qid] = ncbi.replace(".0", "")
    return taxids


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(downloads: dict[str, Path], inventory: Path, rows: int) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    for name, path in downloads.items():
        manifest.setdefault("upstream", {})[name] = {
            "url": BASE + name,
            "doi": f"10.5281/zenodo.{RECORD}",
            "sha256": sha256_of(path),
            "bytes": path.stat().st_size,
        }
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": rows,
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": f"LOTUS frozen export, Zenodo {RECORD} (CC BY 4.0)",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    keys = corpus_keys()
    if not keys:
        raise SystemExit("no corpus structures yet; run the MIBiG extractor first")

    paths = {name: download(name, offline=args.offline) for name in (TRIPLES, METADATA)}
    rows, counts, organisms = extract_triples(paths[TRIPLES], keys)

    print("\nLOTUS triples:", file=sys.stderr)
    for key in sorted(counts):
        print(f"  {key:<40} {counts[key]:>8}", file=sys.stderr)

    taxids = resolve_taxids(paths[METADATA], organisms) if rows else {}
    kept: list[dict] = []
    unresolved = 0
    for row in rows:
        taxid = taxids.get(row["organism_wikidata"])
        if not taxid:
            # Occurrence.taxon_id is required: a name-only organism is a
            # name-only join, which is a curation project rather than an
            # extraction. Same rule the ChEBI origins follow.
            unresolved += 1
            continue
        row["taxon_id"] = f"NCBITaxon:{taxid}"
        kept.append(row)
    kept.sort(key=lambda r: (r["standard_inchi_key"], r["taxon_id"], r["reference_doi"]))

    structures = {r["standard_inchi_key"] for r in kept}
    print(f"\n  organisms needing a taxid : {len(organisms)}", file=sys.stderr)
    print(f"  resolved to an NCBI taxid : {len(taxids)}", file=sys.stderr)
    print(f"  rows dropped, unresolvable: {unresolved}", file=sys.stderr)
    print(f"  occurrences kept          : {len(kept)}", file=sys.stderr)
    print(f"  corpus structures covered : {len(structures)} of {len(keys)}", file=sys.stderr)

    if args.dry_run:
        print("\ndry run: nothing written", file=sys.stderr)
        return 0

    inventory = RAW_DIR / INVENTORY_NAME
    write_tsv(inventory, kept)
    update_manifest(paths, inventory, len(kept))
    print(f"\nwrote {inventory.relative_to(REPO_ROOT)} ({len(kept)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
