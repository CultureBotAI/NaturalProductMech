"""Unit tests for curated literature-backed ChEBI compound seeding and ecological_roles carry-forward."""

from __future__ import annotations

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from naturalproductmech.curate.curated_compounds import load_curated_compounds  # noqa: E402
from naturalproductmech.curate.structure_corrections import row_digest  # noqa: E402
from naturalproductmech.validation.write_validated import canonicalize_top_level_keys  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "seed_from_sources", REPO_ROOT / "scripts" / "seed_from_sources.py"
)
seed = importlib.util.module_from_spec(spec)
sys.modules["seed_from_sources"] = seed
spec.loader.exec_module(seed)


CHEBI_ROW = {
    "chebi_id": "CHEBI:50439",
    "name": "desferrioxamine G",
    "definition": "A hydroxamate siderophore.",
    "stars": "3",
    "standard_inchi_key": "MIVGUYBAQIHKPJ-UHFFFAOYSA-N",
    "smiles": "NCCCCC(O)=O",
}

CURATED_ROW = {
    "chebi_id": "CHEBI:50439",
    "expected_chebi_row_sha256": row_digest(CHEBI_ROW),
    "standard_inchi": (
        "InChI=1S/C27H50N6O10/c28-16-4-1-7-19-31(41)24(36)12-10-22(34)29-17-5-2-8-20-"
        "32(42)25(37)13-11-23(35)30-18-6-3-9-21-33(43)26(38)14-15-27(39)40/"
        "h41-43H,1-21,28H2,(H,29,34)(H,30,35)(H,39,40)"
    ),
    "standard_inchi_key": "MIVGUYBAQIHKPJ-UHFFFAOYSA-N",
    "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1902",
    "taxon_label": "Streptomyces coelicolor",
    "strain": "M145",
    "producer_evidence_basis": "BGC_CHARACTERIZED",
    "mibig_accession": "BGC0000940",
    "reference": "PMID:15919996",
    "evidence_type": "PRIMARY_EXPERIMENT",
    "snippet": "Streptomyces coelicolor produces a mixture of desferrioxamines B and G1.",
    "notes": "In-frame deletion of desA-desD abolishes desferrioxamine G1 and B production.",
    "curator": "test-curator",
    "date": "2026-10-30",
}


def test_load_curated_compounds_accepts_valid_row():
    grouped = load_curated_compounds([CURATED_ROW], [CHEBI_ROW], [])
    assert list(grouped) == ["MIVGUYBAQIHKPJ-UHFFFAOYSA-N"]
    assert len(grouped["MIVGUYBAQIHKPJ-UHFFFAOYSA-N"]) == 1


def test_load_curated_compounds_rejects_chebi_digest_drift():
    bad = {**CURATED_ROW, "expected_chebi_row_sha256": "0" * 64}
    with pytest.raises(ValueError, match="ChEBI row digest drift"):
        load_curated_compounds([bad], [CHEBI_ROW], [])


def test_load_curated_compounds_rejects_already_occupied_mibig_key():
    mibig = [{"standard_inchi_key": "MIVGUYBAQIHKPJ-UHFFFAOYSA-N"}]
    with pytest.raises(ValueError, match="already owned by MIBiG"):
        load_curated_compounds([CURATED_ROW], [CHEBI_ROW], mibig)


def test_load_curated_compounds_rejects_ambiguous_chebi_key():
    second_chebi = {**CHEBI_ROW, "chebi_id": "CHEBI:99999"}
    with pytest.raises(ValueError, match="shared by multiple ChEBI entries"):
        load_curated_compounds([CURATED_ROW], [CHEBI_ROW, second_chebi], [])


def test_build_records_emits_curated_compound_and_carries_ecological_roles():
    records = seed.build_records({
        "chebi_structures": [CHEBI_ROW],
        "curated_compounds": [CURATED_ROW],
        "taxon_groups": [{"taxon_id": "NCBITaxon:1902", "taxon_group": "ACTINOBACTERIAL"}],
        "npclassifier": [{
            "standard_inchi_key": "MIVGUYBAQIHKPJ-UHFFFAOYSA-N",
            "smiles": CHEBI_ROW["smiles"],
            "pathway_results": "Alkaloids",
            "superclass_results": "",
            "class_results": "",
            "is_glycoside": "false",
            "model_version": "npclassifier.gnps2.org@2026-09-09",
        }],
    })
    assert len(records) == 1
    doc = records[0]
    assert doc["identifier"] == "CHEBI:50439"
    assert doc["grounding_status"] == "EXACT"
    assert doc["np_pathway"] == "ALKALOIDS"
    assert doc["producer_taxon_groups"] == ["ACTINOBACTERIAL"]
    producer = doc["producer_organisms"][0]
    assert producer["taxon_id"] == "NCBITaxon:1902"
    assert producer["strain"] == "M145"
    assert producer["evidence_basis"] == "BGC_CHARACTERIZED"
    assert producer["biosynthetic_gene_cluster"] == "mibig:BGC0000940"
    assert producer["source"] == "CURATOR"

    existing = deepcopy(doc)
    existing["ecological_roles"] = ["CHEBI:26672"]
    existing["curation_status"] = "REVIEWED"
    rebuilt = deepcopy(doc)
    seed.carry_curator_owned_fields(rebuilt, existing)
    assert rebuilt["ecological_roles"] == ["CHEBI:26672"]
    assert rebuilt["curation_status"] == "REVIEWED"

    ordered = canonicalize_top_level_keys(rebuilt)
    keys = list(ordered.keys())
    assert "ecological_roles" in keys
    assert keys.index("curation_status") < keys.index("ecological_roles")
