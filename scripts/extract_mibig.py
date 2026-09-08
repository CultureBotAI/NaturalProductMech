#!/usr/bin/env python3
"""Extract MIBiG compound, producer and gene-cluster assertions into an inventory.

The official archive is cached under ``downloads/`` and is never committed. The
emitted TSV is an offline input to ``seed_from_sources.py``.

    just extract-mibig-dry      # free: counts and rejections, writes nothing
    just extract-mibig          # write data/raw/mibig_compounds.tsv
    just extract-mibig --offline

What this gates on, and what it deliberately does not
-----------------------------------------------------
Three MIBiG fields look like quality signals and are not. Verified against the
4.0 release by counting, not by reading about them:

* ``quality`` reads ``questionable`` for 2,710 of 3,013 entries. The MIBiG 4.0
  paper says the label marks legacy-FORMAT entries awaiting re-curation and
  "does not address the quality of the underlying literature". Gating on it
  would discard 90% of the database.
* The changelog reviewer id is the ``AAAA…`` placeholder in 2,988 of 3,013
  entries. AntibioticMech gates on a non-placeholder reviewer, which is why its
  committed inventory holds 24 entries; carried over here that gate would admit
  25 of 3,013 (AntibioticMech#203).
* ``completeness`` is ``unknown`` for 2,132 entries.

What IS a signal is per-locus: ``loci[].evidence[].method`` is a controlled
vocabulary describing how the cluster–compound link was established, and
``conf/producer_evidence.tsv`` grades it. Heterologous expression, knockouts,
enzymatic assays and in-vitro expression are ``BGC_CHARACTERIZED``; the two
correlation methods are ``BGC_CORRELATED``; homology-based prediction is not
producer-grade at all and its entries are reported rather than emitted.

The other gate is ``status``: the dump ships retired and pending entries
alongside active ones.

Structures
----------
MIBiG stores SMILES and **never an InChI or InChIKey** — there is no such field
anywhere in the 4.0 JSON. Standard InChIKeys are generated here with RDKit, so
this extractor is the only place in the pipeline that needs it, and the
committed TSV is what everything downstream reads.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import tarfile
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from naturalproductmech.grading import (  # noqa: E402
    grade_production,
    load_producer_evidence_map,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
PRODUCER_EVIDENCE_PATH = REPO_ROOT / "conf" / "producer_evidence.tsv"
RAW_DIR = REPO_ROOT / "data" / "raw"
DOWNLOAD_DIR = REPO_ROOT / "downloads"
MANIFEST_PATH = RAW_DIR / "MANIFEST.yaml"
INVENTORY_NAME = "mibig_compounds.tsv"

COLUMNS = [
    "mibig_accession",
    "entry_version",
    "entry_status",
    "entry_quality",
    "entry_completeness",
    "compound_name",
    "compound_index",
    "smiles",
    "standard_inchi",
    "standard_inchi_key",
    "stereo_complete",
    "compound_classes",
    "database_ids",
    "taxon_id",
    "taxon_label",
    "bgc_classes",
    "bgc_subclasses",
    "genome_accession",
    "locus_from",
    "locus_to",
    "locus_evidence_methods",
    "producer_evidence_basis",
    "primary_reference",
    "reference_basis",
]

def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_conf() -> dict:
    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8"))
    return conf["mibig"]




def download(url: str, destination: Path, *, offline: bool) -> Path:
    if destination.exists():
        return destination
    if offline:
        raise SystemExit(f"missing {destination} and --offline was given")
    destination.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {url}", file=sys.stderr)
    with urllib.request.urlopen(url) as response, destination.open("wb") as out:  # noqa: S310
        out.write(response.read())
    return destination


def archive_entries(path: Path):
    """Yield one parsed JSON entry per member of the release tarball."""
    with tarfile.open(path, "r:gz") as archive:
        for member in archive:
            if not member.isfile() or not member.name.endswith(".json"):
                continue
            handle = archive.extractfile(member)
            if handle is None:
                continue
            yield json.load(handle)


def structure_fields(smiles: str) -> tuple[dict[str, str], str | None]:
    """Standard InChI, InChIKey and a stereo-completeness flag from a SMILES.

    Returns ``({}, reason)`` when RDKit cannot parse or key the structure, so a
    bad SMILES is counted and reported rather than silently dropped.
    """
    from rdkit import Chem, RDLogger
    from rdkit.Chem import inchi

    RDLogger.DisableLog("rdApp.*")
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {}, "unparseable_smiles"
    try:
        standard_inchi = inchi.MolToInchi(mol)
    except Exception:  # noqa: BLE001 - RDKit raises a bare Exception here
        return {}, "inchi_failed"
    if not standard_inchi:
        return {}, "inchi_empty"
    key = inchi.InchiToInchiKey(standard_inchi)
    if not key:
        return {}, "inchikey_failed"

    # An undefined stereocentre is recorded, never invented. Natural products
    # are where stereochemistry is most often assigned years after isolation.
    unassigned = Chem.FindMolChiralCenters(mol, includeUnassigned=True, useLegacyImplementation=False)
    stereo_complete = not any(tag == "?" for _, tag in unassigned)
    return {
        "standard_inchi": standard_inchi,
        "standard_inchi_key": key,
        "stereo_complete": "true" if stereo_complete else "false",
    }, None


def normalize_reference(value) -> str:
    """MIBiG references arrive as `pubmed:123`, `doi:10.x/y` or a bare string."""
    if isinstance(value, dict):
        value = value.get("reference") or value.get("value") or ""
    text = str(value).strip()
    prefix, separator, local = text.partition(":")
    if separator and prefix.lower() == "pubmed":
        return f"PMID:{local}"
    if separator and prefix.lower() == "doi":
        return f"DOI:{local}"
    return text


def primary_reference(entry: dict, compound: dict) -> tuple[str, str]:
    """The best reference for a compound, and WHICH LEVEL it came from.

    MIBiG puts references in several places and they do not mean the same
    thing, so the level travels with the citation rather than being flattened
    away. A curator reading a seeded record has to be able to tell a
    compound-specific structure report from the entry's general reference.

    Priority, best first:

    * ``compounds[].evidence[].references`` — the report that established this
      structure (NMR, MS, X-ray, total synthesis).
    * ``compounds[].bioactivities[].references`` — compound-specific, but about
      what it does rather than what it is.
    * ``legacy_references`` — entry level. Present on every active entry, and
      the right citation for the cluster–organism claim rather than the
      structure.
    """
    for item in compound.get("evidence") or []:
        for value in (item.get("references") or []) if isinstance(item, dict) else []:
            reference = normalize_reference(value)
            if reference:
                return reference, "COMPOUND_EVIDENCE"
    for item in compound.get("bioactivities") or []:
        for value in (item.get("references") or []) if isinstance(item, dict) else []:
            reference = normalize_reference(value)
            if reference:
                return reference, "COMPOUND_BIOACTIVITY"
    for value in entry.get("legacy_references") or []:
        reference = normalize_reference(value)
        if reference:
            return reference, "ENTRY"
    return "", ""


def locus_evidence_methods(entry: dict) -> list[str]:
    methods: list[str] = []
    for locus in entry.get("loci") or []:
        for item in locus.get("evidence") or []:
            method = item.get("method") if isinstance(item, dict) else item
            if method and method not in methods:
                methods.append(str(method))
    return methods




def compound_class_labels(compound: dict) -> str:
    labels = []
    for item in compound.get("classes") or []:
        # MIBiG's compound classes appear both as objects and as bare strings,
        # which is schema drift inside one release rather than two vocabularies.
        label = (item.get("class") or item.get("name")) if isinstance(item, dict) else item
        if label:
            labels.append(str(label))
    return "|".join(labels)


def database_ids(compound: dict) -> str:
    ids = [str(x) for x in (compound.get("databaseIds") or []) if x]
    return "|".join(ids)


def biosynthesis_classes(entry: dict) -> tuple[str, str]:
    classes, subclasses = [], []
    for item in (entry.get("biosynthesis") or {}).get("classes") or []:
        if not isinstance(item, dict):
            continue
        if item.get("class"):
            classes.append(str(item["class"]))
        if item.get("subclass"):
            subclasses.append(str(item["subclass"]))
    return "|".join(classes), "|".join(subclasses)


def first_locus(entry: dict) -> dict:
    loci = entry.get("loci") or []
    return loci[0] if loci else {}


def extract(path: Path, conf: dict, evidence_map: dict[str, str]) -> tuple[list[dict], Counter]:
    counts: Counter[str] = Counter()
    rows: list[dict] = []
    allowed_status = set(conf.get("status_allowed") or ["active"])

    for entry in archive_entries(path):
        counts["entries_total"] += 1
        status = entry.get("status")
        counts[f"status_{status}"] += 1
        if status not in allowed_status:
            counts["rejected_status"] += 1
            continue
        counts["entries_active"] += 1

        taxonomy = entry.get("taxonomy") or {}
        taxon_id = taxonomy.get("ncbiTaxId")
        taxon_label = str(taxonomy.get("name") or "").strip()

        methods = locus_evidence_methods(entry)
        basis = grade_production(methods, evidence_map)
        counts[f"producer_basis_{basis or 'none'}"] += 1

        bgc_classes, bgc_subclasses = biosynthesis_classes(entry)
        locus = first_locus(entry)
        location = locus.get("location") or {}

        for index, compound in enumerate(entry.get("compounds") or [], start=1):
            counts["compounds_total"] += 1
            smiles = str(compound.get("structure") or "").strip()
            if not smiles:
                counts["rejected_no_structure"] += 1
                continue
            structure, error = structure_fields(smiles)
            if error:
                counts[f"rejected_{error}"] += 1
                continue
            if not taxon_id:
                counts["rejected_no_taxon"] += 1
                continue
            reference, reference_basis = primary_reference(entry, compound)
            if not reference:
                counts["rejected_no_reference"] += 1
                continue
            counts[f"reference_from_{reference_basis.lower()}"] += 1

            rows.append({
                "mibig_accession": entry["accession"],
                "entry_version": str(entry.get("version") or ""),
                "entry_status": str(status or ""),
                "entry_quality": str(entry.get("quality") or ""),
                "entry_completeness": str(entry.get("completeness") or ""),
                "compound_name": " ".join(str(compound.get("name") or "").split()),
                "compound_index": str(index),
                "smiles": smiles,
                **structure,
                "compound_classes": compound_class_labels(compound),
                "database_ids": database_ids(compound),
                "taxon_id": f"NCBITaxon:{taxon_id}",
                "taxon_label": taxon_label,
                "bgc_classes": bgc_classes,
                "bgc_subclasses": bgc_subclasses,
                "genome_accession": str(locus.get("accession") or ""),
                "locus_from": str(location.get("from") or ""),
                "locus_to": str(location.get("to") or ""),
                "locus_evidence_methods": "|".join(methods),
                "producer_evidence_basis": basis or "",
                "primary_reference": reference,
                "reference_basis": reference_basis,
            })
            counts["inventory_rows"] += 1

    rows.sort(key=lambda row: (row["mibig_accession"], int(row["compound_index"])))
    return rows, counts


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_manifest(conf: dict, archive: Path, inventory: Path, rows: int) -> None:
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    manifest.setdefault("upstream", {})[archive.name] = {
        "url": conf["archive_url"],
        "version": str(conf.get("version") or ""),
        "sha256": sha256_of(archive),
        "bytes": archive.stat().st_size,
    }
    manifest.setdefault("inventories", {})[inventory.name] = {
        "rows": rows,
        "bytes": inventory.stat().st_size,
        "sha256": sha256_of(inventory),
        "source": f"MIBiG {conf.get('version')} active entries",
    }
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")


def report(counts: Counter, rows: list[dict]) -> None:
    print("MIBiG extraction:", file=sys.stderr)
    for key in sorted(counts):
        print(f"  {key:<40} {counts[key]:>6}", file=sys.stderr)
    if not rows:
        return
    keys = {row["standard_inchi_key"] for row in rows}
    by_basis = Counter(row["producer_evidence_basis"] or "none" for row in rows)
    print(f"\n  rows: {len(rows)}, unique InChIKeys: {len(keys)}", file=sys.stderr)
    print("  producer grade of the emitted rows:", file=sys.stderr)
    for basis, count in by_basis.most_common():
        print(f"    {basis:<38} {count:>6}", file=sys.stderr)
    incomplete = sum(1 for row in rows if row["stereo_complete"] == "false")
    print(f"  structures with undefined stereocentres: {incomplete}", file=sys.stderr)
    collisions = Counter(row["standard_inchi_key"] for row in rows)
    repeated = {k: n for k, n in collisions.items() if n > 1}
    print(f"  InChIKeys appearing on more than one row: {len(repeated)}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="report counts and write nothing")
    parser.add_argument("--offline", action="store_true",
                        help="never download; require the cached archive")
    parser.add_argument("--archive", type=Path, help="use this archive instead of the cache")
    args = parser.parse_args()

    conf = load_conf()
    evidence_map = load_producer_evidence_map()
    archive = args.archive or (DOWNLOAD_DIR / conf["archive_name"])
    archive = download(conf["archive_url"], archive, offline=args.offline)

    rows, counts = extract(archive, conf, evidence_map)
    report(counts, rows)

    if args.dry_run:
        print("\ndry run: nothing written", file=sys.stderr)
        return 0

    inventory = RAW_DIR / INVENTORY_NAME
    write_tsv(inventory, rows)
    update_manifest(conf, archive, inventory, len(rows))
    print(f"\nwrote {inventory.relative_to(REPO_ROOT)} ({len(rows)} rows) "
          f"and updated {MANIFEST_PATH.name}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
