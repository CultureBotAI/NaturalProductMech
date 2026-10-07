#!/usr/bin/env python3
"""Extract reviewed product-to-pathway joins at an explicit PathwayMech commit.

Uses committed MIBiG product rows or ChEBI structures to establish the product
identity. A product link never asserts that all producer taxa use the linked
organism-specific pathway. No network requests or working-tree sibling reads.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import subprocess
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
COLUMNS = ["standard_inchi_key", "identifier", "label", "basis", "corpus_commit"]
INVENTORY_NAME = "pathwaymech_products.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_pathway(checkout: Path, commit: str, name: str) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        raise ValueError("PathwayMech pin must be a full commit hash")
    if not name.startswith("data/pathways/") or ".." in Path(name).parts:
        raise ValueError(f"not a PathwayMech record path: {name}")
    result = subprocess.run(
        ["git", "-C", str(checkout), "show", f"{commit}:{name}"],
        capture_output=True, check=True, text=True,
    )
    doc = yaml.safe_load(result.stdout)
    if not isinstance(doc, dict):
        raise ValueError(f"not a pathway record: {name}")
    return doc


def product_rows(recipe: dict, doc: dict, mibig: list[dict], chebi: list[dict],
                 commit: str) -> list[dict[str, str]]:
    """Match only reviewed exact product identities, with evidence in the basis."""
    identifier = recipe["identifier"]
    if doc.get("id") != identifier:
        raise ValueError(f"expected {identifier}, found {doc.get('id')}")
    taxa = {item["id"] for item in doc.get("taxa", [])}
    scope = "; ".join(sorted(taxa)) or "unspecified taxon"
    matches: set[tuple[str, str]] = set()
    if recipe["join"] == "SAME_MIBIG_PRODUCT":
        for cluster in doc.get("gene_clusters", []):
            if cluster.get("id") != identifier:
                continue
            accession = identifier.split(":", 1)[1]
            for row in mibig:
                if (row["mibig_accession"] == accession
                        and row.get("entry_status") == "active"
                        and row["compound_name"] in cluster.get("products", [])
                        and row.get("taxon_id") in taxa):
                    basis = (f"SAME_MIBIG_PRODUCT: {identifier}, product {row['compound_name']}; "
                             f"same source taxon {row['taxon_id']}. "
                             "This links the product to its cluster, not to every producer.")
                    matches.add((row["standard_inchi_key"], basis))
    elif recipe["join"] == "SAME_TERMINAL_PRODUCT_INCHIKEY":
        product = recipe["product"]
        edges = doc.get("mechanistic_edges", [])
        produced = any(e.get("predicate") == "produces" and e.get("object") == product
                       for e in edges)
        consumed = any(e.get("predicate") == "consumes" and e.get("subject") == product
                       for e in edges)
        if not produced or consumed:
            raise ValueError(f"{product} is not a terminal product of {identifier}")
        keys = {r["standard_inchi_key"] for r in chebi if r["chebi_id"] == product}
        if len(keys) != 1 or not next(iter(keys)):
            raise ValueError(f"{product} must have one pinned ChEBI structure")
        basis = (f"SAME_TERMINAL_PRODUCT_INCHIKEY: {product} in the pinned ChEBI inventory; "
                 f"pathway taxon {scope}. Product identity only; no assertion that this "
                 "record's other producer taxa use this pathway.")
        matches.add((next(iter(keys)), basis))
    else:
        raise ValueError(f"unknown pathway join {recipe['join']}")
    if not matches:
        raise ValueError(f"no supported products for {identifier}")
    return [{"standard_inchi_key": key, "identifier": identifier,
             "label": doc["label"], "basis": basis, "corpus_commit": commit}
            for key, basis in sorted(matches)]


def extract(checkout: Path, root: Path = REPO_ROOT) -> list[dict[str, str]]:
    pins = yaml.safe_load((root / "conf/sibling_pins.yaml").read_text())
    commit = pins["pathwaymech"]["commit"]
    recipes = yaml.safe_load((root / "conf/pathwaymech_links.yaml").read_text())["pathways"]
    mibig = read_tsv(root / "data/raw/mibig_compounds.tsv")
    chebi = read_tsv(root / "data/raw/chebi_structures.tsv")
    rows = []
    for recipe in recipes:
        doc = read_pathway(checkout, commit, recipe["file"])
        rows.extend(product_rows(recipe, doc, mibig, chebi, commit))
    return sorted(rows, key=lambda row: (row["standard_inchi_key"], row["identifier"]))


def render(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--check", action="store_true", help="compare to the committed inventory")
    args = parser.parse_args()
    payload = render(extract(args.checkout))
    inventory = REPO_ROOT / "data/raw" / INVENTORY_NAME
    if args.check:
        if not inventory.exists() or inventory.read_text() != payload:
            print("PathwayMech inventory differs from the pinned source")
            return 1
        print("PathwayMech inventory reproduces from the pinned source")
    elif args.dry_run:
        print(payload, end="")
    else:
        inventory.write_text(payload, encoding="utf-8")
        path = REPO_ROOT / "data/raw/MANIFEST.yaml"
        manifest = yaml.safe_load(path.read_text())
        pin = yaml.safe_load((REPO_ROOT / "conf/sibling_pins.yaml").read_text())["pathwaymech"]
        manifest["inventories"][INVENTORY_NAME] = {
            "rows": len(payload.splitlines()) - 1,
            "bytes": len(payload.encode()),
            "sha256": hashlib.sha256(payload.encode()).hexdigest(),
            "source": (f"CultureBotAI/PathwayMech at {pin['commit']}; "
                       "pinned local ChEBI and MIBiG inventories"),
            "retrieved_on": date.today().isoformat(),
        }
        path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True))
        print(f"wrote {inventory.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
