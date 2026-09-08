#!/usr/bin/env python3
"""Extract ChEBI identity and occurrence assertions into committed inventories.

    just extract-chebi-dry     # free: counts and rejections, writes nothing
    just extract-chebi         # write both inventories
    just extract-chebi --offline

Two inventories, because ChEBI answers two different questions for this corpus.

``chebi_structures.tsv`` — **identity**. Every 3-star ChEBI entry with a default
structure and a Standard InChIKey. This is what turns a minted record into a
grounded one: a MIBiG structure whose key matches a ChEBI entry gets ChEBI's
CURIE, name and definition, and stops being keyed on a hash of an accession.

``chebi_origins.tsv`` — **occurrences**. ChEBI's own ``compound_origins`` table
records where a compound was found: a species with an NCBI taxonomy accession,
often a tissue or component, sometimes a strain, and a citation. That is an
occurrence in this corpus's sense and never a producer claim — ChEBI is
recording that the compound was detected in the organism, not that the organism
biosynthesizes it. The distinction is the whole point of the schema, so the
seeder writes these to ``occurrences`` and nothing promotes them.

Star ratings
------------
Only 3-star entries are read. ChEBI's 2-star entries are automatically imported
rather than manually curated, and an automatic import is exactly where an
unreviewed assertion enters a corpus that claims to be evidence-backed. Lowering
this is a curation decision, not a tuning knob.
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
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
PLANNED_CONF_PATH = REPO_ROOT / "conf" / "sources.planned.yaml"
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"

BASE = "https://ftp.ebi.ac.uk/pub/databases/chebi/flat_files/"
FILES = ("compounds.tsv.gz", "structures.tsv.gz", "compound_origins.tsv.gz")

# The Standard InChI is deliberately NOT carried. Grounding joins on the
# InChIKey and the structure itself comes from the source that supplied it, so
# the full InChI would add ~10 MB to a committed inventory for a column nothing
# reads. The SMILES stays: a later milestone may want to compare ChEBI's own
# depiction against the seeded one.
STRUCTURE_COLUMNS = [
    "chebi_id", "name", "definition", "stars", "standard_inchi_key", "smiles",
]
ORIGIN_COLUMNS = [
    "chebi_id", "species_text", "species_accession", "component_text",
    "strain_text", "source_accession", "comments",
]

MIN_STARS = 3


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_conf() -> dict:
    for path in (CONF_PATH, PLANNED_CONF_PATH):
        conf = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if "chebi" in conf:
            return conf["chebi"]
    raise SystemExit("no chebi section in conf/sources.yaml or conf/sources.planned.yaml")


def download(name: str, *, offline: bool) -> Path:
    destination = DOWNLOAD_DIR / name
    if destination.exists():
        return destination
    if offline:
        raise SystemExit(f"missing {destination} and --offline was given")
    destination.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {BASE}{name}", file=sys.stderr)
    with urllib.request.urlopen(BASE + name) as response, destination.open("wb") as out:  # noqa: S310
        while chunk := response.read(1 << 20):
            out.write(chunk)
    return destination


def read_rows(path: Path):
    """ChEBI's flat files embed molfiles with raw newlines and quotes, so the
    csv module is given a large field limit and QUOTE_MINIMAL handling."""
    csv.field_size_limit(1 << 24)
    with gzip.open(path, "rt", encoding="utf-8", errors="replace", newline="") as fh:
        yield from csv.DictReader(fh, delimiter="\t")


def extract_compounds(path: Path) -> tuple[dict[str, dict[str, str]], Counter]:
    counts: Counter[str] = Counter()
    compounds: dict[str, dict[str, str]] = {}
    for row in read_rows(path):
        counts["compounds_total"] += 1
        # ChEBI's status vocabulary (status.tsv): 1 CHECKED, 3 OK, 9 SUBMITTED.
        # SUBMITTED entries are unreviewed and are the majority of the file;
        # admitting them would be the automatic-import problem the star filter
        # exists to avoid, arriving through a different door.
        if row.get("status_id") not in ("1", "3"):
            counts["rejected_status_submitted"] += 1
            continue
        stars = (row.get("stars") or "0").strip()
        if not stars.isdigit() or int(stars) < MIN_STARS:
            counts[f"rejected_stars_{stars}"] += 1
            continue
        compounds[row["id"]] = {
            "name": (row.get("name") or "").strip(),
            "definition": (row.get("definition") or "").strip().strip('"'),
            "stars": stars,
        }
        counts["compounds_kept"] += 1
    return compounds, counts


def extract_structures(path: Path, compounds: dict[str, dict[str, str]]) -> tuple[list[dict], Counter]:
    counts: Counter[str] = Counter()
    best: dict[str, dict[str, str]] = {}
    for row in read_rows(path):
        counts["structure_rows"] += 1
        cid = row.get("compound_id")
        if cid not in compounds:
            continue
        key = (row.get("standard_inchi_key") or "").strip()
        if not key:
            continue
        # ChEBI marks one structure per compound as the default. Anything else
        # is an alternative depiction, and grounding on one would key a record
        # to a structure ChEBI itself does not consider canonical.
        is_default = (row.get("default_structure") or "").strip().lower()
        if is_default not in ("true", "y", "t", "1"):
            counts["skipped_non_default_structure"] += 1
            continue
        best[cid] = {
            "chebi_id": f"CHEBI:{cid}",
            "name": compounds[cid]["name"],
            "definition": compounds[cid]["definition"],
            "stars": compounds[cid]["stars"],
            "standard_inchi_key": key,
            "smiles": (row.get("smiles") or "").strip(),
        }
        counts["structures_kept"] += 1
    return sorted(best.values(), key=lambda r: int(r["chebi_id"].split(":")[1])), counts


def extract_origins(path: Path, compounds: dict[str, dict[str, str]]) -> tuple[list[dict], Counter]:
    counts: Counter[str] = Counter()
    rows: list[dict] = []
    for row in read_rows(path):
        counts["origin_rows"] += 1
        cid = row.get("compound_id")
        if cid not in compounds:
            counts["rejected_compound_not_kept"] += 1
            continue
        species = (row.get("species_text") or "").strip()
        if not species:
            counts["rejected_no_species"] += 1
            continue
        # A citation is required. An occurrence with nobody to attribute it to
        # is not an occurrence this corpus can carry: `Occurrence.evidence` is
        # a required field precisely so this cannot slip through.
        source = (row.get("source_accession") or "").strip()
        if not source:
            counts["rejected_no_citation"] += 1
            continue
        # A resolvable taxon is required, not merely a species name. The schema
        # makes Occurrence.taxon_id mandatory for this reason: a name-only
        # organism is a name-only join, which is a curation project rather than
        # an extraction, and it would not survive the guarded write path
        # anyway — it did not, which is how this rule got written down.
        accession = (row.get("species_accession") or "").strip()
        if not accession.isdigit():
            counts["rejected_species_not_resolvable"] += 1
            continue
        rows.append({
            "chebi_id": f"CHEBI:{cid}",
            "species_text": species,
            "species_accession": accession,
            "component_text": (row.get("component_text") or "").strip(),
            "strain_text": (row.get("strain_text") or "").strip(),
            "source_accession": source,
            "comments": " ".join((row.get("comments") or "").split()),
        })
        counts["origins_kept"] += 1
    rows.sort(key=lambda r: (int(r["chebi_id"].split(":")[1]), r["species_text"], r["source_accession"]))
    return rows, counts


def write_tsv(path: Path, columns: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, delimiter="\t",
                                lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(downloads: dict[str, Path], inventories: dict[str, tuple[Path, int]]) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    for name, path in downloads.items():
        manifest.setdefault("upstream", {})[name] = {
            "url": BASE + name,
            "sha256": sha256_of(path),
            "bytes": path.stat().st_size,
        }
    for name, (path, rows) in inventories.items():
        manifest.setdefault("inventories", {})[name] = {
            "rows": rows,
            "bytes": path.stat().st_size,
            "sha256": sha256_of(path),
            "source": f"ChEBI flat files, {MIN_STARS}-star entries",
        }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()

    paths = {name: download(name, offline=args.offline) for name in FILES}

    compounds, c_counts = extract_compounds(paths["compounds.tsv.gz"])
    structures, s_counts = extract_structures(paths["structures.tsv.gz"], compounds)
    origins, o_counts = extract_origins(paths["compound_origins.tsv.gz"], compounds)

    for label, counts in (("compounds", c_counts), ("structures", s_counts), ("origins", o_counts)):
        print(f"\nChEBI {label}:", file=sys.stderr)
        for key in sorted(counts):
            print(f"  {key:<40} {counts[key]:>8}", file=sys.stderr)

    keys = {row["standard_inchi_key"] for row in structures}
    with_taxid = sum(1 for row in origins if row["species_accession"].isdigit())
    print(f"\n  grounding inventory: {len(structures)} entries, "
          f"{len(keys)} unique InChIKeys", file=sys.stderr)
    print(f"  occurrence inventory: {len(origins)} rows, "
          f"{with_taxid} with a numeric species accession", file=sys.stderr)

    if args.dry_run:
        print("\ndry run: nothing written", file=sys.stderr)
        return 0

    structures_path = RAW_DIR / "chebi_structures.tsv"
    origins_path = RAW_DIR / "chebi_origins.tsv"
    write_tsv(structures_path, STRUCTURE_COLUMNS, structures)
    write_tsv(origins_path, ORIGIN_COLUMNS, origins)
    update_manifest(paths, {
        structures_path.name: (structures_path, len(structures)),
        origins_path.name: (origins_path, len(origins)),
    })
    print(f"\nwrote {structures_path.name} ({len(structures)} rows) and "
          f"{origins_path.name} ({len(origins)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
