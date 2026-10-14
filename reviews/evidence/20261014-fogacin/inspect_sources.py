"""Replay the bounded fogacin chemistry and inventory audit offline."""

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

BASE = "12e9c505e12ba17920a7c95964fd1c35e3e057d3"
PACK = Path(__file__).resolve().parent


def checked(data: bytes, expected: str) -> bytes:
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("Evidence input hash mismatch")
    return data


def scan(text: str, values: set[str], column: str = "standard_inchi_key") -> dict:
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    if column not in (reader.fieldnames or []):
        raise ValueError(f"Inventory is missing required column {column}")
    rows = list(reader)
    return {"rows_scanned": len(rows), "join_column": column,
            "join_values": sorted(values),
            "matches": [{"row_number": i + 2, "row": row}
                        for i, row in enumerate(rows) if row[column] in values]}


def replay(repo: Path) -> dict:
    from rdkit import Chem, rdBase
    from rdkit.Chem import rdMolDescriptors

    if rdBase.rdkitVersion != "2026.03.5":
        raise ValueError(f"Expected RDKit2026.03.5, got {rdBase.rdkitVersion}")
    manifest = json.loads((PACK / "replay-inputs.json").read_text())
    if manifest["base"] != BASE:
        raise ValueError("Unexpected review base")

    def native(path):
        data = subprocess.check_output(["git", "-C", str(repo), "show", f"{BASE}:{path}"])
        return checked(data, manifest["git_inputs"][path]).decode()

    def captured(name):
        return checked((PACK / "inputs" / name).read_bytes(), manifest["captured_inputs"][name])

    out = {"rdkit": rdBase.rdkitVersion, "chemistry": {}, "inventories": {}}
    keys = set()
    for slug, version in (("fogacin", "5"), ("fogacin-2", "3")):
        doc = yaml.safe_load(native(f"data/natural_products/polyketides/{slug}.yaml"))
        structure = doc["chemical_structure"]
        mol = Chem.MolFromSmiles(structure["smiles"])
        if mol is None:
            raise ValueError(f"Invalid molecule: {slug}")
        data = {"formula": rdMolDescriptors.CalcMolFormula(mol),
                "charge": Chem.GetFormalCharge(mol), "inchi": Chem.MolToInchi(mol),
                "key": Chem.MolToInchiKey(mol),
                "centers": Chem.FindMolChiralCenters(mol, includeUnassigned=True)}
        if data["inchi"] != structure["standard_inchi"] or data["key"] != structure["standard_inchi_key"]:
            raise ValueError(f"Chemical round-trip mismatch: {slug}")
        if structure["stereo_complete"] != all(c[1] != "?" for c in data["centers"]):
            raise ValueError(f"Stereochemical completeness mismatch: {slug}")
        accession = structure["structure_source_id"].split(":")[1]
        mibig = json.loads(captured(f"{accession}.{version}.json"))
        matches = [i + 1 for i, c in enumerate(mibig["compounds"])
                   if c.get("structure", c.get("chem_struct")) == structure["smiles"]]
        if len(matches) != 1:
            raise ValueError(f"Expected one exact MIBiG compound member: {slug}")
        data["mibig_compound_index"] = matches[0]
        keys.add(data["key"])
        out["chemistry"][slug] = data

    chebi = scan(native("data/raw/chebi_structures.tsv"), keys)
    out["inventories"]["chebi_structures"] = chebi
    chebi_ids = {m["row"]["chebi_id"] for m in chebi["matches"]}
    out["inventories"]["chebi_origins"] = scan(
        native("data/raw/chebi_origins.tsv"), chebi_ids, "chebi_id")
    for name in ("mibig_compounds", "lotus_occurrences", "npclassifier",
                 "antibioticmech_inchikeys", "pubchem_bioassay"):
        out["inventories"][name] = scan(native(f"data/raw/{name}.tsv"), keys)
    out["taxonomy"] = [
        {"taxon_id": t.findtext("TaxId"), "name": t.findtext("ScientificName"),
         "rank": t.findtext("Rank"), "lineage": t.findtext("Lineage")}
        for t in ET.fromstring(captured("taxonomy.xml")).findall("Taxon")]
    out["sequences"] = {}
    for name in ("AP012319.1-region.xml", "JAKQYH010000014.1-region.xml"):
        out["sequences"][name] = [
            {"accession": s.findtext("GBSeq_accession-version"),
             "definition": s.findtext("GBSeq_definition"), "length": s.findtext("GBSeq_length"),
             "features": [{"key": f.findtext("GBFeature_key"),
                           "location": f.findtext("GBFeature_location"),
                           "qualifiers": [(q.findtext("GBQualifier_name"), q.findtext("GBQualifier_value"))
                                          for q in f.findall("GBFeature_quals/GBQualifier")
                                          if q.findtext("GBQualifier_name") != "translation"]}
                          for f in s.findall("GBSeq_feature-table/GBFeature")
                          if f.findtext("GBFeature_key") in ("source", "CDS")]}
            for s in ET.fromstring(captured(name)).findall("GBSeq")]
    out["pubchem"] = json.loads(captured("pubchem-11493248.json"))["PropertyTable"]["Properties"]
    if out["pubchem"][0]["InChIKey"] != out["chemistry"]["fogacin-2"]["key"]:
        raise ValueError("PubChem cross-reference mismatch")
    out["wikidata"] = []
    for qid in ("Q25834569", "Q1144013"):
        entity = json.loads(captured(f"wikidata-{qid}.json"))["entities"][qid]
        out["wikidata"].append({"id": qid, "label": entity["labels"]["en"]["value"],
                                "ncbi_taxon_ids": [c["mainsnak"]["datavalue"]["value"]
                                                   for c in entity["claims"].get("P685", [])]})
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=PACK.parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = replay(args.repo)
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(f"Replayed both fogacin owners at {BASE}")
