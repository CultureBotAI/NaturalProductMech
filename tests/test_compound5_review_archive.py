"""Regression checks for the bounded compound-5 evidence, not scientific approval."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

PACK = Path(__file__).resolve().parents[1] / "reviews/evidence/20261014-compound5"
SPEC = importlib.util.spec_from_file_location("compound5_replay", PACK / "inspect_sources.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_origin_join_uses_chebi_identity():
    text = "chebi_id\tspecies_text\nCHEBI:1\tFungus A\nCHEBI:2\tFungus B\n"
    result = MODULE.scan_inventory(text, {"KEY"}, {"CHEBI:2"}, origins=True)
    assert result["rows_scanned"] == 2
    assert result["join_column"] == "chebi_id"
    assert result["matches"] == [
        {
            "row_number": 3,
            "row": {
                "chebi_id": "CHEBI:2",
                "species_text": "Fungus B",
            },
        }
    ]
    assert not MODULE.scan_inventory(text, {"KEY"}, set(), origins=True)["matches"]


@pytest.mark.parametrize("origins,column", [(True, "chebi_id"), (False, "standard_inchi_key")])
def test_missing_join_column_fails_closed(origins, column):
    with pytest.raises(ValueError, match=column):
        MODULE.scan_inventory("wrong_column\nvalue\n", {"KEY"}, set(), origins=origins)


def test_exact_key_scan_does_not_match_nearby_structure():
    text = "standard_inchi_key\tlabel\nKEY-A\tone\nKEY-B\ttwo\n"
    result = MODULE.scan_inventory(text, {"KEY-B"}, set())
    assert [match["row"]["label"] for match in result["matches"]] == ["two"]


def test_retained_inputs_match_manifest():
    manifest = json.loads((PACK / "replay-inputs.json").read_text())
    assert manifest["base"] == MODULE.BASE
    assert len(manifest["captured_inputs"]) == 5
    assert len(manifest["git_inputs"]) == 9
    for name, digest in manifest["captured_inputs"].items():
        assert hashlib.sha256((PACK / "inputs" / name).read_bytes()).hexdigest() == digest
    with pytest.raises(ValueError, match="hash mismatch"):
        MODULE.checked_bytes(b"changed", "0" * 64)


def test_corrected_result_changes_only_join_metadata():
    original = json.loads((PACK / "source-inspection.json").read_text())
    corrected = json.loads((PACK / "source-inspection-corrected.json").read_text())
    for key in ("rdkit", "chemistry", "taxonomy", "sequences"):
        assert corrected[key] == original[key]
    for name, result in corrected["inventories"].items():
        assert result["matches"] == original["inventories"][name]["matches"]
        assert result["rows_scanned"] == original["inventories"][name]["rows_scanned"]
    assert corrected["inventories"]["chebi_origins"]["join_column"] == "chebi_id"
    assert corrected["inventories"]["chebi_origins"]["join_values"] == []
