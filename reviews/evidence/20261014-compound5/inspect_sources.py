"""Replay the bounded compound-5 source audit without a research workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

BASE = "487536b67c632b474b54bcc2ce32cf5c1097a7bd"
PACK = Path(__file__).resolve().parent


def scan_inventory(text: str, keys: set[str], chebi_ids: set[str], *, origins: bool = False) -> dict:
    """Origins have no InChIKey: join through matched ChEBI structure IDs."""
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    column = "chebi_id" if origins else "standard_inchi_key"
    if column not in (reader.fieldnames or []):
        raise ValueError(f"Inventory is missing required column {column}")
    rows = list(reader)
    values = chebi_ids if origins else keys
    return {
        "rows_scanned": len(rows),
        "join_column": column,
        "join_values": sorted(values),
        "matches": [{"row_number": i + 2, "row": row} for i, row in enumerate(rows) if row[column] in values],
    }


def checked_bytes(data: bytes, expected: str) -> bytes:
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("Evidence input hash mismatch")
    return data


def replay(repo: Path) -> dict:
    from rdkit import Chem, rdBase
    from rdkit.Chem import rdMolDescriptors

    if rdBase.rdkitVersion != "2026.03.5":
        raise ValueError(f"Expected pinned RDKit2026.03.5, got {rdBase.rdkitVersion}")
    manifest = json.loads((PACK / "replay-inputs.json").read_text())
    if manifest["base"] != BASE:
        raise ValueError("Unexpected review base")

    def native(path):
        data = subprocess.check_output(["git", "-C", str(repo), "show", f"{BASE}:{path}"])
        return checked_bytes(data, manifest["git_inputs"][path]).decode()

    def captured(name):
        return checked_bytes((PACK / "inputs" / name).read_bytes(), manifest["captured_inputs"][name])

    docs = {
        "compound-5": yaml.safe_load(native("data/natural_products/terpenoids/compound-5.yaml")),
        "compound-5-2": yaml.safe_load(native("data/natural_products/polyketides/compound-5-2.yaml")),
    }
    out = {"rdkit": rdBase.rdkitVersion, "chemistry": {}, "inventories": {}}
    keys = {d["chemical_structure"]["standard_inchi_key"] for d in docs.values()}
    for slug, doc in docs.items():
        structure = doc["chemical_structure"]
        mol = Chem.MolFromSmiles(structure["smiles"])
        if mol is None:
            raise ValueError(f"Invalid molecule: {slug}")
        data = {
            "formula": rdMolDescriptors.CalcMolFormula(mol),
            "charge": Chem.GetFormalCharge(mol),
            "inchi": Chem.MolToInchi(mol),
            "key": Chem.MolToInchiKey(mol),
            "centers": Chem.FindMolChiralCenters(mol, includeUnassigned=True),
            "double_bond_stereo": [
                str(b.GetStereo()) for b in mol.GetBonds() if b.GetBondType() == Chem.BondType.DOUBLE
            ],
        }
        if data["inchi"] != structure["standard_inchi"] or data["key"] != structure["standard_inchi_key"]:
            raise ValueError(f"Chemical round-trip mismatch: {slug}")
        if structure["stereo_complete"] != all(c[1] != "?" for c in data["centers"]):
            raise ValueError(f"Stereochemical completeness mismatch: {slug}")
        bgc = structure["structure_source_id"].split(":")[1]
        source = json.loads(captured(bgc + ".3.json"))
        matches = [
            i + 1
            for i, compound in enumerate(source["compounds"])
            if compound["structure"] == structure["smiles"]
        ]
        if len(matches) != 1:
            raise ValueError(f"Expected one exact compound member: {slug}")
        data["mibig_compound_index"] = matches[0]
        out["chemistry"][slug] = data

    chebi = scan_inventory(native("data/raw/chebi_structures.tsv"), keys, set())
    chebi_ids = {match["row"]["chebi_id"] for match in chebi["matches"]}
    out["inventories"]["chebi_structures"] = chebi
    for name in (
        "mibig_compounds",
        "lotus_occurrences",
        "chebi_origins",
        "npclassifier",
        "antibioticmech_inchikeys",
        "pubchem_bioassay",
    ):
        out["inventories"][name] = scan_inventory(
            native(f"data/raw/{name}.tsv"), keys, chebi_ids, origins=name == "chebi_origins"
        )
    out["taxonomy"] = [
        {
            "taxon_id": taxon.findtext("TaxId"),
            "name": taxon.findtext("ScientificName"),
            "rank": taxon.findtext("Rank"),
            "lineage": taxon.findtext("Lineage"),
            "other_names": [
                (n.tag, n.text) for n in taxon.findall("OtherNames/*") if n.text and n.text.strip()
            ],
        }
        for taxon in ET.fromstring(captured("taxonomy.xml")).findall("Taxon")
    ]
    out["sequences"] = {}
    for filename in ("CH445335.1-region.xml", "DS027698.1-region.xml"):
        records = []
        for seq in ET.fromstring(captured(filename)).findall("GBSeq"):
            features = []
            for feature in seq.findall("GBSeq_feature-table/GBFeature"):
                if feature.findtext("GBFeature_key") not in ("source", "CDS"):
                    continue
                qualifiers = [
                    (q.findtext("GBQualifier_name"), q.findtext("GBQualifier_value"))
                    for q in feature.findall("GBFeature_quals/GBQualifier")
                    if q.findtext("GBQualifier_name") != "translation"
                ]
                features.append(
                    {
                        "key": feature.findtext("GBFeature_key"),
                        "location": feature.findtext("GBFeature_location"),
                        "qualifiers": qualifiers,
                    }
                )
            records.append(
                {
                    "accession": seq.findtext("GBSeq_accession-version"),
                    "definition": seq.findtext("GBSeq_definition"),
                    "length": seq.findtext("GBSeq_length"),
                    "features": features,
                }
            )
        out["sequences"][filename] = records
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=PACK.parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = replay(args.repo)
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(f"Replayed both exact owners at {BASE}; wrote {args.output}")


if __name__ == "__main__":
    main()
