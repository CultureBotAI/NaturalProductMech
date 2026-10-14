"""Replay four exact-owner encoding/source joins, without experimental sign-off."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import subprocess
from pathlib import Path

import yaml

BASE = "22ced0a503edd1d04628f7cfbdbb14ee1d03047c"
PACK = Path(__file__).resolve().parent


def checked_bytes(data: bytes, expected: str) -> bytes:
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("Evidence input hash mismatch")
    return data


def scan(text: str, values: set[str], column: str) -> dict:
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    if column not in (reader.fieldnames or []):
        raise ValueError(f"Missing join column: {column}")
    rows = list(reader)
    return {
        "rows_scanned": len(rows),
        "join_field": column,
        "matches": [row for row in rows if row[column] in values],
    }


def source_member(source: dict, row: dict, doc: dict) -> dict:
    index = int(row["compound_index"])
    if index < 1 or index > len(source["compounds"]):
        raise ValueError("Compound index must be one-based and in bounds")
    member = source["compounds"][index - 1]
    structure = doc["chemical_structure"]
    if (member["name"], member["structure"]) != (doc["label"], structure["smiles"]):
        raise ValueError("Exact compound member mismatch")
    if str(source["version"]) != row["entry_version"] or source["status"] != row["entry_status"]:
        raise ValueError("Source version/status mismatch")
    if str(source["taxonomy"]["ncbiTaxId"]) != row["taxon_id"].split(":")[1]:
        raise ValueError("Source taxon mismatch")
    locus, = source["loci"]
    if (locus["accession"], str(locus["location"]["from"]), str(locus["location"]["to"])) != (
        row["genome_accession"], row["locus_from"], row["locus_to"]
    ):
        raise ValueError("Source locus mismatch")
    return member


def replay(repo: Path) -> dict:
    from rdkit import Chem, rdBase
    from rdkit.Chem import rdMolDescriptors

    if rdBase.rdkitVersion != "2026.03.5":
        raise ValueError("Replay requires pinned RDKit 2026.03.5")
    manifest = json.loads((PACK / "manifest.json").read_text())
    if manifest["base"] != BASE:
        raise ValueError("Unexpected historical base")

    def native(path):
        data = subprocess.check_output(["git", "-C", str(repo), "show", f"{BASE}:{path}"])
        return checked_bytes(data, manifest["git_inputs"][path]).decode()

    def captured(path):
        return checked_bytes((PACK / path).read_bytes(), manifest["files"][path])

    capture = json.loads(captured("capture.json"))
    docs = [(t["path"], yaml.safe_load(native(t["path"]))) for t in capture["targets"]]
    keys = {d["chemical_structure"]["standard_inchi_key"] for _, d in docs}
    if len(keys) != 4:
        raise ValueError("Expected four distinct exact structures")
    inventories = {}
    inventories["chebi_structures"] = scan(native("data/raw/chebi_structures.tsv"), keys,
                                            "standard_inchi_key")
    chebi_ids = {r["chebi_id"] for r in inventories["chebi_structures"]["matches"]}
    for name in ("chebi_origins", "mibig_compounds", "npclassifier", "lotus_occurrences",
                 "pubchem_bioassay", "bindingdb_targets", "antibioticmech_inchikeys",
                 "pathwaymech_products"):
        origins = name == "chebi_origins"
        inventories[name] = scan(native(f"data/raw/{name}.tsv"), chebi_ids if origins else keys,
                                 "chebi_id" if origins else "standard_inchi_key")
    results = []
    for path, doc in docs:
        structure = doc["chemical_structure"]
        mol = Chem.MolFromSmiles(structure["smiles"])
        if mol is None:
            raise ValueError(f"Invalid molecule: {path}")
        if (Chem.MolToInchi(mol), Chem.MolToInchiKey(mol)) != (
            structure["standard_inchi"], structure["standard_inchi_key"]
        ):
            raise ValueError(f"Chemical round-trip mismatch: {path}")
        centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True)
        if structure["stereo_complete"] != all(c[1] != "?" for c in centers):
            raise ValueError(f"Atom stereo completeness mismatch: {path}")
        row, = [r for r in inventories["mibig_compounds"]["matches"]
                if r["standard_inchi_key"] == structure["standard_inchi_key"]]
        source = json.loads(
            native("reviews/evidence/20261014-compound5/inputs/BGC0002162.3.json")
            if row["mibig_accession"] == "BGC0002162"
            else captured("inputs/BGC0002290.2.json")
        )
        source_member(source, row, doc)
        results.append({
            "path": path, "key": Chem.MolToInchiKey(mol),
            "formula": rdMolDescriptors.CalcMolFormula(mol), "charge": Chem.GetFormalCharge(mol),
            "exact_mass": rdMolDescriptors.CalcExactMolWt(mol), "centers": centers,
            "ring_sizes": sorted(len(r) for r in Chem.GetSymmSSSR(mol)),
            "source_id": row["mibig_accession"] + ":" + row["compound_index"],
        })
    return {"rdkit": rdBase.rdkitVersion, "records": results, "inventories": inventories}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=PACK.parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = replay(args.repo)
    with args.output.open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    print(f"Replayed four exact owners at {BASE}; wrote {args.output}")


if __name__ == "__main__":
    main()
