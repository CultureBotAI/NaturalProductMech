"""Check the bounded numbered-product audit, not experimental identity."""

import hashlib
import json
from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "reviews/evidence/20261014-numbered-products"
SPEC = spec_from_file_location("numbered_replay", PACK / "replay.py")
REPLAY = module_from_spec(SPEC)
SPEC.loader.exec_module(REPLAY)


def test_manifest_retains_exact_payload_bytes():
    manifest = json.loads((PACK / "manifest.json").read_text())
    assert manifest["base"] == REPLAY.BASE
    assert len(manifest["git_inputs"]) == 15
    assert not any("__pycache__" in name or name.endswith(".pyc") for name in manifest["files"])
    for name, digest in manifest["files"].items():
        assert hashlib.sha256((PACK / name).read_bytes()).hexdigest() == digest
    with pytest.raises(ValueError, match="hash mismatch"):
        REPLAY.checked_bytes(b"changed", "0" * 64)


@pytest.mark.parametrize("column", ["chebi_id", "standard_inchi_key"])
def test_inventory_requires_join_column_even_if_empty(column):
    with pytest.raises(ValueError, match="Missing join column"):
        REPLAY.scan("wrong_column\n", set(), column)


def test_origin_join_is_exact_and_uses_chebi_ids():
    text = "chebi_id\tspecies\nCHEBI:1\tA\nCHEBI:2\tB\n"
    assert REPLAY.scan(text, {"CHEBI:2"}, "chebi_id")["matches"] == [
        {"chebi_id": "CHEBI:2", "species": "B"}
    ]
    assert REPLAY.scan(text, set(), "chebi_id")["matches"] == []


def test_replay_retains_all_four_distinct_members_and_original_calculations():
    original = json.loads((PACK / "source-analysis.json").read_text())
    result = json.loads((PACK / "replay-result.json").read_text())
    assert "abstracts" not in original
    assert result["rdkit"] == original["rdkit"] == "2026.03.5"
    assert len(result["records"]) == len({r["key"] for r in result["records"]}) == 4
    assert [r["source_id"] for r in result["records"]] == [
        "BGC0002290:7", "BGC0002162:6", "BGC0002162:3", "BGC0002290:9"
    ]
    assert [r["charge"] for r in result["records"]] == [0, 1, 1, 0]
    for before, after in zip(original["records"], result["records"], strict=True):
        for key in ("path", "key", "formula", "charge", "exact_mass", "centers", "ring_sizes"):
            assert before[key] == after[key]
    for name, actual in result["inventories"].items():
        for key in ("rows_scanned", "join_field", "matches"):
            assert actual[key] == original["inventories"][name][key]


@pytest.mark.parametrize("index", ["0", "-1", "1", "99"])
def test_source_member_rejects_wrong_or_out_of_bounds_index(index):
    original = json.loads((PACK / "source-analysis.json").read_text())["records"][0]
    row = deepcopy(original["raw_row"])
    member = original["source_compound"]
    doc = {"label": member["name"], "chemical_structure": {"smiles": member["structure"]}}
    source = json.loads((PACK / "inputs/BGC0002290.2.json").read_text())
    assert REPLAY.source_member(source, row, doc) == member
    row["compound_index"] = index
    with pytest.raises(ValueError, match="Compound index|member mismatch"):
        REPLAY.source_member(source, row, doc)


def test_saved_reviews_keep_scope_verdict_and_scientific_limits_separate():
    index = json.loads((PACK / "review-index.json").read_text())
    assert len(index) == 4
    for item in index:
        review = yaml.safe_load((ROOT / item["yaml"]).read_text())
        assert review["source"]["git_revision"] == REPLAY.BASE
        assert review["scope"]["population_size"] == 1
        assert review["completion"] == "partial"
        assert len(review["targets"]) == 1
        if review["verdict"] == "seed_only":
            assert review["scientific_review"] is False
            assert review["findings"] == []
        else:
            assert review["verdict"] == "needs_curation"
            assert review["scientific_review"] is True
            finding, = review["findings"]
            assert (finding["severity"], finding["certainty"], finding["status"]) == (
                "major", "provisional", "open"
            )
