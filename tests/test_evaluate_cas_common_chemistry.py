"""Unit tests for CAS Common Chemistry source queue gate and REVIEW_NEEDED evaluator."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from check_source_queue import QUEUE_PATH, UNSEEDABLE  # noqa: E402
from evaluate_cas_common_chemistry import (  # noqa: E402
    REDISTRIBUTION_CLASS,
    classify_chebi_charge_state,
    compute_smiles_net_charge,
    evaluate_review_needed_rows,
    has_formal_charge_smiles,
    is_zwitterionic_smiles,
    strip_inchikey_prefix,
    validate_output_path_is_outside_corpus,
)


def test_cas_common_chemistry_is_recorded_as_blocked_non_commercial_in_source_queue():
    assert REDISTRIBUTION_CLASS in UNSEEDABLE
    with QUEUE_PATH.open(newline="", encoding="utf-8") as fh:
        rows = {r["source_id"]: r for r in csv.DictReader(fh, delimiter="\t")}
    assert "cas-common-chemistry" in rows
    row = rows["cas-common-chemistry"]
    assert row["use"] == "CURATE_ONLY"
    assert row["redistribution"] == "NON_COMMERCIAL"
    assert row["status"] == "BLOCKED"
    assert row["verified_on"] == "2026-11-09"


def test_is_zwitterionic_smiles_distinguishes_neutral_and_zwitterion():
    assert is_zwitterionic_smiles("CC1=NCC(C(=O)O)N1") is False
    assert is_zwitterionic_smiles("CC1=NC[C@H](C(=O)[O-])[NH2+]1") is True
    assert is_zwitterionic_smiles("C[N@+](C)(C)CC(=O)[O-]") is True
    assert is_zwitterionic_smiles("[Ca+2].[O-]C(=O)CC(=O)[O-]") is True
    assert is_zwitterionic_smiles("NCCCC([NH3+])CC(=O)N[NH3+]") is False
    assert compute_smiles_net_charge("CC1=NC[C@H](C(=O)[O-])[NH2+]1") == 0
    assert compute_smiles_net_charge("NCCCC([NH3+])CC(=O)N[NH3+]") == 2
    assert compute_smiles_net_charge("O=C([O-])CC([O-])C(=O)[O-]") == -3
    assert has_formal_charge_smiles("CC1=NCC(C(=O)O)N1") is False
    assert has_formal_charge_smiles("NCCCC([NH3+])CC(=O)N") is True
    assert strip_inchikey_prefix("InChIKey=WNYADZVDBIBLJJ-UHFFFAOYSA-N") == (
        "WNYADZVDBIBLJJ-UHFFFAOYSA-N"
    )
    assert classify_chebi_charge_state(
        {"chebi_id": "CHEBI:27592", "name": "ectoine", "smiles": "CC1=NCC(C(=O)O)N1"}
    ) == "NEUTRAL"
    assert classify_chebi_charge_state(
        {
            "chebi_id": "CHEBI:58515",
            "name": "ectoine zwitterion",
            "smiles": "CC1=NC[C@H](C(=O)[O-])[NH2+]1",
        }
    ) == "ZWITTERION"
    assert classify_chebi_charge_state(
        {
            "chebi_id": "CHEBI:60821",
            "name": "streptothricin F(2+)",
            "smiles": "NCCCC([NH3+])CC(=O)N[NH3+]",
        }
    ) == "NET_CHARGED_ION"


def test_validate_output_path_refuses_corpus_and_raw_directories(tmp_path):
    (tmp_path / "data" / "raw").mkdir(parents=True)
    (tmp_path / "data" / "natural_products").mkdir(parents=True)
    (tmp_path / "research").mkdir(parents=True)

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "data" / "raw" / "cas.tsv", repo_root=tmp_path
        )

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_corpus(
            tmp_path / "data" / "natural_products" / "cas.tsv", repo_root=tmp_path
        )

    validate_output_path_is_outside_corpus(
        tmp_path / "research" / "cas_eval.tsv", repo_root=tmp_path
    )


def test_evaluate_review_needed_rows_selects_neutral_chebi_parent():
    cas_rows = [
        {
            "group": "naturalproduct_review_needed",
            "mech": "NaturalProductMech",
            "identifier": "npmech:MIBIG-BGC0000853-ectoine",
            "query_name": "ectoine",
            "cas_rn": "96702-03-3",
            "cas_name": "4-Pyrimidinecarboxylic acid, 1,4,5,6-tetrahydro-2-methyl-, (4S)-",
            "canonical_smiles": "CC1=NCC(C(=O)O)N1",
            "inchikey": "InChIKey=WNYADZVDBIBLJJ-UHFFFAOYSA-N",
        }
    ]
    review_needed_by_id = {
        "npmech:MIBIG-BGC0000853-ectoine": {
            "identifier": "npmech:MIBIG-BGC0000853-ectoine",
            "label": "ectoine",
            "grounding_status": "REVIEW_NEEDED",
            "chemical_structure": {
                "standard_inchi_key": "WNYADZVDBIBLJJ-UHFFFAOYSA-N",
            },
        }
    }
    chebi_by_ik = {
        "WNYADZVDBIBLJJ-UHFFFAOYSA-N": [
            {
                "chebi_id": "CHEBI:27592",
                "name": "ectoine",
                "smiles": "CC1=NCC(C(=O)O)N1",
            },
            {
                "chebi_id": "CHEBI:58515",
                "name": "ectoine zwitterion",
                "smiles": "CC1=NC[C@H](C(=O)[O-])[NH2+]1",
            },
        ]
    }

    evaluated = evaluate_review_needed_rows(cas_rows, review_needed_by_id, chebi_by_ik)
    assert len(evaluated) == 1
    row = evaluated[0]
    assert row["inchikey_agreement"] == "AGREES"
    assert row["cas_charge_state"] == "NEUTRAL"
    assert row["neutral_chebi_candidates"] == "CHEBI:27592"
    assert row["zwitterion_chebi_candidates"] == "CHEBI:58515"
    assert row["net_charged_chebi_candidates"] == ""
    assert row["cas_aligned_chebi_id"] == "CHEBI:27592"


def test_evaluate_review_needed_rows_separates_net_charged_ions_from_zwitterions():
    cas_rows = [
        {
            "group": "naturalproduct_review_needed",
            "mech": "NaturalProductMech",
            "identifier": "npmech:MIBIG-BGC0000432-streptothricin-f",
            "query_name": "streptothricin F",
            "cas_rn": "3808-42-2",
            "cas_name": "Streptothricin F",
            "canonical_smiles": "NCCCC(N)CC(=O)N",
            "inchikey": "InChIKey=ADKDFJJOGSGGBN-JLFKCYBCSA-N",
        }
    ]
    review_needed_by_id = {
        "npmech:MIBIG-BGC0000432-streptothricin-f": {
            "identifier": "npmech:MIBIG-BGC0000432-streptothricin-f",
            "label": "streptothricin F",
            "grounding_status": "REVIEW_NEEDED",
            "chemical_structure": {
                "standard_inchi_key": "ADKDFJJOGSGGBN-JLFKCYBCSA-N",
            },
        }
    }
    chebi_by_ik = {
        "ADKDFJJOGSGGBN-JLFKCYBCSA-N": [
            {
                "chebi_id": "CHEBI:60810",
                "name": "streptothricin F",
                "smiles": "NCCCC(N)CC(=O)N",
            },
            {
                "chebi_id": "CHEBI:60821",
                "name": "streptothricin F(2+)",
                "smiles": "NCCCC([NH3+])CC(=O)N[NH3+]",
            },
        ]
    }
    evaluated = evaluate_review_needed_rows(cas_rows, review_needed_by_id, chebi_by_ik)
    row = evaluated[0]
    assert row["neutral_chebi_candidates"] == "CHEBI:60810"
    assert row["zwitterion_chebi_candidates"] == ""
    assert row["net_charged_chebi_candidates"] == "CHEBI:60821"
    assert row["cas_aligned_chebi_id"] == "CHEBI:60810"
