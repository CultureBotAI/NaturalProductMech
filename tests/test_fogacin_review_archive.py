"""The fogacin evidence pack remains inspectable without its research workspace."""

import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "reviews/evidence/20261014-fogacin"
SPEC = importlib.util.spec_from_file_location("fogacin_replay", PACK / "inspect_sources.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_archived_and_historical_inputs_match_hashes():
    manifest = json.loads((PACK / "replay-inputs.json").read_text())
    assert manifest["base"] == MODULE.BASE
    assert len(manifest["captured_inputs"]) == 8
    assert len(manifest["git_inputs"]) == 9
    for name, digest in manifest["captured_inputs"].items():
        assert hashlib.sha256((PACK / "inputs" / name).read_bytes()).hexdigest() == digest
    for name, digest in manifest["git_inputs"].items():
        data = subprocess.check_output(["git", "show", f"{MODULE.BASE}:{name}"], cwd=ROOT)
        assert hashlib.sha256(data).hexdigest() == digest
    with pytest.raises(ValueError, match="hash mismatch"):
        MODULE.checked(b"changed", "0" * 64)


@pytest.mark.parametrize("column", ["standard_inchi_key", "chebi_id"])
def test_missing_join_column_fails_closed(column):
    with pytest.raises(ValueError, match=column):
        MODULE.scan("other\nvalue\n", {"KEY"}, column)


def test_exact_origin_join_and_empty_join():
    text = "chebi_id\tlabel\nCHEBI:1\tone\nCHEBI:2\ttwo\n"
    assert MODULE.scan(text, {"CHEBI:2"}, "chebi_id")["matches"] == [
        {"row_number": 3, "row": {"chebi_id": "CHEBI:2", "label": "two"}}]
    assert not MODULE.scan(text, set(), "chebi_id")["matches"]


def test_fogacin_forms_and_negative_assay_sentinel_are_not_conflated():
    result = json.loads((PACK / "source-inspection.json").read_text())
    assert result["chemistry"]["fogacin"]["formula"] == "C16H16O6"
    assert result["chemistry"]["fogacin-2"]["formula"] == "C16H18O6"
    assert result["chemistry"]["fogacin"]["key"] != result["chemistry"]["fogacin-2"]["key"]
    assert len(result["inventories"]["lotus_occurrences"]["matches"]) == 2
    assay, = result["inventories"]["pubchem_bioassay"]["matches"]
    assert assay["row"]["assay_name"] == "(no assay data)" and not assay["row"]["aid"]
    assert result["inventories"]["chebi_origins"]["join_column"] == "chebi_id"
    assert result["inventories"]["chebi_origins"]["join_values"] == []
