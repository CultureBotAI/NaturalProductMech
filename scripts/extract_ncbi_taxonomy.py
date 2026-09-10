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

Merged identifiers (#63)
------------------------
Two sources supply numeric taxids directly — MIBiG at submission time, LOTUS
from Wikidata — and NCBI retires ids into others as taxa are merged. A first
run of the id-label gate found 42 such ids in the corpus, 118 rows of them
from LOTUS: still denoting the organism, since NCBI keeps the redirect, but
joining to nothing current. ``merged.dmp`` from the same taxdump says where
each went, so this extractor also emits ``taxon_merged.tsv`` — old id to
current id, restricted to ids the adopted sources actually use — and the
seeder rewrites through it at write time, keeping the source's id in the
inventory as provenance and saying on the claim that it was rewritten.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
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
MERGED_INVENTORY_NAME = "taxon_merged.tsv"
NON_ORGANISM_INVENTORY_NAME = "taxon_non_organism.tsv"

#: Nodes that are structurally not an organism: the root, the rank above the
#: domains, and NCBI's two catch-alls for sequences it has not placed.
STRUCTURAL_NON_ORGANISM = {
    "1": "root of the taxonomy",
    "131567": "the rank above the domains, not a taxon anyone isolates from",
    "12908": "NCBI's bin for unclassified sequences",
    "32644": "NCBI's bin for unidentified organisms",
}

#: Subtrees whose members are communities or unplaced sequences rather than
#: organisms. Everything under them is excluded, so a metagenome this corpus
#: has not seen yet is caught without being listed.
NON_ORGANISM_SUBTREES = {
    "12908": "under unclassified sequences",
    "408169": "under metagenomes — a community, not an organism",
}

#: Generic environmental bins: real nodes, but ones that many unrelated
#: organisms share. NCBI places them directly under a domain via an
#: `environmental samples` wrapper, so no lineage rule distinguishes them from
#: a specific uncultured clone — `uncultured bacterium AR_456` sits in exactly
#: the same place and DOES denote one lineage. What separates them is that a
#: join on a bin is meaningless: 36 producer claims in this corpus point at
#: 77133, and treating that as an organism asserts that one bacterium makes 36
#: unrelated compounds (#68).
GENERIC_BINS = {
    "77133": "uncultured bacterium — shared by every unplaced bacterium",
    "155900": "uncultured organism — shared by every unplaced organism",
}

ARCHIVE = "taxdump.tar.gz"
URL = f"https://ftp.ncbi.nlm.nih.gov/pub/taxonomy/{ARCHIVE}"

#: Name classes that assert the name denotes the taxon. `includes`, `in-part`
#: and `blast name` do not — they group or approximate — so a match on one of
#: those would resolve a name to a taxon nobody claimed it was.
USABLE_NAME_CLASSES = {"scientific name", "synonym", "equivalent name",
                       "genbank synonym", "genbank anamorph", "anamorph"}

COLUMNS = ["organism_name", "taxon_id", "name_class", "requested_by"]
MERGED_COLUMNS = ["old_taxon_id", "new_taxon_id", "requested_by"]
NON_ORGANISM_COLUMNS = ["taxon_id", "scientific_name", "reason", "requested_by"]


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

    # BindingDB names the organism whose protein was assayed, and the seeder
    # had nowhere to resolve it: molecular_targets carried a taxon_label and no
    # taxon_id on all 123 targets, which is the name-only join the occurrence
    # rule forbids (#67). Read from the committed inventory rather than the
    # upstream zip, because that extractor has already done the filtering.
    bindingdb = RAW_DIR / "bindingdb_targets.tsv"
    if bindingdb.exists():
        names = set()
        with bindingdb.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                organism = " ".join((row.get("target_organism") or "").split())
                if organism:
                    names.add(organism)
        wanted["bindingdb"] = names

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


def ids_wanted() -> dict[str, set[str]]:
    """Numeric taxids the adopted sources supply directly, by source.

    Read from the cached upstream files, like ``names_wanted``: the ids to
    check for currency are precisely the ones that arrived already numeric.
    """
    wanted: dict[str, set[str]] = {}

    for mibig in sorted(DOWNLOAD_DIR.glob("mibig_json_*.tar.gz")):
        ids = set()
        with tarfile.open(mibig, "r:gz") as tar:
            for member in tar:
                if not member.isfile() or not member.name.endswith(".json"):
                    continue
                handle = tar.extractfile(member)
                if handle is None:
                    continue
                taxid = (json.load(handle).get("taxonomy") or {}).get("ncbiTaxId")
                if taxid:
                    ids.add(str(taxid))
        wanted["mibig"] = ids
        break

    lotus_meta = DOWNLOAD_DIR / "260413_frozen_metadata.csv.gz"
    if lotus_meta.exists():
        ids = set()
        with gzip.open(lotus_meta, "rt", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh):
                ncbi = (row.get("organism_taxonomy_ncbiid") or "").strip().replace(".0", "")
                if ncbi.isdigit():
                    ids.add(ncbi)
        wanted["lotus"] = ids

    origins = DOWNLOAD_DIR / "compound_origins.tsv.gz"
    if origins.exists():
        ids = set()
        with gzip.open(origins, "rt", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                accession = (row.get("species_accession") or "").strip()
                if accession.isdigit():
                    ids.add(accession)
        wanted["chebi_origins"] = ids

    return wanted


def non_organism(archive: Path, wanted: set[str]) -> dict[str, tuple[str, str]]:
    """Wanted taxids that do not denote a single organism -> (name, reason).

    Three ways in, in order of how much of the taxonomy they cover: a
    structural node, a member of a non-organism subtree, or one of the two
    generic bins. A producer claim on any of them names no organism, which is
    a claim the corpus cannot make (#62, #68).
    """
    parents: dict[str, str] = {}
    with tarfile.open(archive, "r:gz") as tar:
        nodes = tar.extractfile("nodes.dmp")
        if nodes is None:
            raise SystemExit("nodes.dmp missing from the taxdump archive")
        for raw in nodes:
            parts = [p.strip() for p in raw.decode("utf-8", "replace").split("\t|")]
            if len(parts) >= 2:
                parents[parts[0]] = parts[1]

    def lineage(taxid: str) -> list[str]:
        chain, seen = [], set()
        while taxid and taxid not in seen and taxid != "1":
            seen.add(taxid)
            chain.append(taxid)
            taxid = parents.get(taxid, "")
        return chain

    found: dict[str, tuple[str, str]] = {}
    for taxid in wanted:
        if taxid in STRUCTURAL_NON_ORGANISM:
            found[taxid] = ("", STRUCTURAL_NON_ORGANISM[taxid])
            continue
        if taxid in GENERIC_BINS:
            found[taxid] = ("", GENERIC_BINS[taxid])
            continue
        for ancestor in lineage(taxid)[1:]:
            if ancestor in NON_ORGANISM_SUBTREES:
                found[taxid] = ("", NON_ORGANISM_SUBTREES[ancestor])
                break

    if found:
        with tarfile.open(archive, "r:gz") as tar:
            member = tar.extractfile("names.dmp")
            if member is not None:
                for raw in member:
                    parts = [p.strip() for p in raw.decode("utf-8", "replace").split("\t|")]
                    if (len(parts) > 3 and parts[0] in found
                            and parts[3].rstrip("\t|\n") == "scientific name"):
                        found[parts[0]] = (parts[1], found[parts[0]][1])
    return found


def merged(archive: Path, wanted: set[str]) -> dict[str, str]:
    """Old taxid -> current taxid, for the wanted ids that NCBI has merged."""
    found: dict[str, str] = {}
    with tarfile.open(archive, "r:gz") as tar:
        member = tar.extractfile("merged.dmp")
        if member is None:
            raise SystemExit("merged.dmp missing from the taxdump archive")
        for raw in member:
            parts = [p.strip() for p in raw.decode("utf-8", "replace").split("\t|")]
            if len(parts) >= 2 and parts[0] in wanted:
                found[parts[0]] = parts[1]
    return found


def resolve(archive: Path, wanted: set[str]) -> tuple[dict[str, tuple[str, str]], Counter]:
    """Name -> (taxid, name_class), for the wanted names only.

    A scientific name wins over a synonym when both match, so a name that is one
    taxon's accepted name and another's synonym resolves to the accepted one.
    """
    counts: Counter[str] = Counter()
    # Sorted, not a set comprehension: ChEBI supplies the same organism under
    # two casings (`Geodia barretti` and `Geodia Barretti`), and a dict built
    # by iterating a set keeps whichever it saw last — a choice Python's
    # randomised string hashing makes differently each process. That made this
    # inventory reproduce differently roughly every other run (#74).
    lowered: dict[str, str] = {}
    for name in sorted(wanted):
        lowered.setdefault(name.lower(), name)
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

    ids_by_source = ids_wanted()
    ids_all = set().union(*ids_by_source.values()) if ids_by_source else set()
    merges = merged(archive, ids_all)
    bins = non_organism(archive, ids_all)
    print("\nnumeric taxids supplied directly, by source:", file=sys.stderr)
    for source, ids in sorted(ids_by_source.items()):
        gone = len(ids & set(merges))
        print(f"  {source:<16} {len(ids):>7}   merged by NCBI: {gone}", file=sys.stderr)
    print(f"  {'distinct merged':<16} {len(merges):>7}", file=sys.stderr)
    print(f"\ntaxa that do not denote a single organism: {len(bins)}", file=sys.stderr)
    for taxid, (name, reason) in sorted(bins.items(), key=lambda kv: int(kv[0])):
        print(f"  NCBITaxon:{taxid:<10} {name[:34]:<36} {reason}", file=sys.stderr)

    print(f"\nnames.dmp rows read : {counts['names_dmp_rows']}", file=sys.stderr)
    print(f"resolved            : {len(found)} of {len(wanted)} "
          f"({100 * len(found) // max(len(wanted), 1)}%)", file=sys.stderr)
    by_class = Counter(name_class for _, name_class in found.values())
    for name_class, count in by_class.most_common():
        print(f"    {name_class:<24} {count:>7}", file=sys.stderr)
    for source, names in sorted(wanted_by_source.items()):
        gained = len(names & set(found))
        print(f"  would resolve for {source:<16} {gained:>7} of {len(names)}", file=sys.stderr)

    # The residue is a curation queue, not an extractor counter. 202 ChEBI
    # names alone are superseded botanical basionyms — Biota orientalis is now
    # Platycladus orientalis — which a curator can resolve one line at a time,
    # and the highest-count names are worth several occurrences each (#36).
    unresolved_path = REPO_ROOT / "curation" / "unresolved_taxa.tsv"
    unresolved = sorted(
        (name, ",".join(sorted(s for s, names in wanted_by_source.items() if name in names)))
        for name in wanted - set(found)
    )

    if args.dry_run:
        print(f"\n{len(unresolved)} names would remain unresolved", file=sys.stderr)
        print("dry run: nothing written", file=sys.stderr)
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

    merged_rows = [{
        "old_taxon_id": f"NCBITaxon:{old}",
        "new_taxon_id": f"NCBITaxon:{new}",
        "requested_by": ",".join(sorted(s for s, ids in ids_by_source.items() if old in ids)),
    } for old, new in sorted(merges.items(), key=lambda kv: int(kv[0]))]
    bin_rows = [{
        "taxon_id": f"NCBITaxon:{taxid}",
        "scientific_name": name,
        "reason": reason,
        "requested_by": ",".join(sorted(s for s, ids in ids_by_source.items() if taxid in ids)),
    } for taxid, (name, reason) in sorted(bins.items(), key=lambda kv: int(kv[0]))]
    bin_inventory = RAW_DIR / NON_ORGANISM_INVENTORY_NAME
    with bin_inventory.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=NON_ORGANISM_COLUMNS,
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(bin_rows)

    merged_inventory = RAW_DIR / MERGED_INVENTORY_NAME
    with merged_inventory.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=MERGED_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(merged_rows)

    with unresolved_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["organism_name", "requested_by"],
                                delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({"organism_name": n, "requested_by": s} for n, s in unresolved)
    print(f"wrote {unresolved_path.relative_to(REPO_ROOT)} "
          f"({len(unresolved)} names still unresolved)", file=sys.stderr)

    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}
    manifest["retrieved_on"] = time.strftime("%Y-%m-%d")
    manifest.setdefault("upstream", {})[ARCHIVE] = {
        "url": URL, "sha256": sha256_of(archive), "bytes": archive.stat().st_size,
    }
    manifest.setdefault("inventories", {})[INVENTORY_NAME] = {
        "rows": len(rows), "bytes": inventory.stat().st_size, "sha256": sha256_of(inventory),
        "source": "NCBI Taxonomy taxdump, names.dmp (public domain)",
    }
    manifest["inventories"][NON_ORGANISM_INVENTORY_NAME] = {
        "rows": len(bin_rows), "bytes": bin_inventory.stat().st_size,
        "sha256": sha256_of(bin_inventory),
        "source": "NCBI Taxonomy taxdump, nodes.dmp + names.dmp (public domain)",
    }
    manifest["inventories"][MERGED_INVENTORY_NAME] = {
        "rows": len(merged_rows), "bytes": merged_inventory.stat().st_size,
        "sha256": sha256_of(merged_inventory),
        "source": "NCBI Taxonomy taxdump, merged.dmp (public domain)",
    }
    print(f"wrote {merged_inventory.relative_to(REPO_ROOT)} ({len(merged_rows)} rows)",
          file=sys.stderr)
    print(f"wrote {bin_inventory.relative_to(REPO_ROOT)} ({len(bin_rows)} rows)", file=sys.stderr)
    MANIFEST_PATH.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"\nwrote {inventory.relative_to(REPO_ROOT)} ({len(rows)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
