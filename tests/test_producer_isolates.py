"""Literal deposit isolates are pinned context, not inferred cultured strains."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

from naturalproductmech.curate.producer_strains import (
    load_producer_isolates,
    qualify_producer_isolate,
)
from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_isolates", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


@pytest.fixture
def inputs():
    source, = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] == "BGC0000174"]
    decision, = [r for r in seed.read_tsv(seed.MIBIG_PRODUCER_ISOLATES)
                 if r["source_id"] == "BGC0000174:1"]
    return {"mibig_compounds": [source], "mibig_producer_isolates": [decision]}


def test_isolate_only_changes_scoped_producer_notes_and_evidence(inputs):
    original = deepcopy(inputs)
    source = inputs["mibig_compounds"][0]
    inputs["mibig_compounds"].append({**source, "mibig_accession": "BGC0000206"})
    before, = seed.build_records({"mibig_compounds": inputs["mibig_compounds"]})
    after, = seed.build_records(inputs)
    producer = after["producer_organisms"][0]
    assert "strain" not in producer
    assert producer["notes"].endswith(" Deposited isolate: DEEP.")
    producer["notes"] = producer["notes"].removesuffix(" Deposited isolate: DEEP.")
    evidence = producer["evidence"].pop()
    assert evidence["reference"].endswith("/DQ889941.1")
    assert evidence["evidence_type"] == "CURATOR_INFERENCE"
    assert original["mibig_producer_isolates"][0]["expected_source_row_sha256"] in evidence["notes"]
    assert before == after
    inputs["mibig_compounds"].pop()
    assert inputs == original


def test_notes_without_existing_text_and_independent_strain_are_preserved(inputs):
    decision = inputs["mibig_producer_isolates"][0]
    producer = {"evidence": [], "strain": "separately sourced strain"}
    qualify_producer_isolate(producer, decision)
    assert producer["notes"] == "Deposited isolate: DEEP."
    assert producer["strain"] == "separately sourced strain"


def test_every_source_field_is_pinned(inputs):
    source = inputs["mibig_compounds"][0]
    for field in source:
        changed = {**source, field: source[field] + " changed"}
        with pytest.raises(ValueError, match="source drift|exactly one source row"):
            load_producer_isolates([changed], inputs["mibig_producer_isolates"])


@pytest.mark.parametrize("value", [None, "", " "])
def test_every_decision_field_is_required(inputs, value):
    decision = inputs["mibig_producer_isolates"][0]
    for field in decision:
        with pytest.raises(ValueError):
            load_producer_isolates(inputs["mibig_compounds"], [{**decision, field: value}])
        missing = {k: v for k, v in decision.items() if k != field}
        with pytest.raises(ValueError):
            load_producer_isolates(inputs["mibig_compounds"], [missing])


@pytest.mark.parametrize("field,value", [
    ("reference", "uncited"), ("reference", "http://example.org"),
    ("reference", "https://"), ("reference", "https://example.org/a b"),
    ("date", "2026-02-30"), ("date", "20261013"),
    ("source_id", "BGC0000174"), ("expected_source_row_sha256", "BAD"),
])
def test_malformed_decision_rejected(inputs, field, value):
    inputs["mibig_producer_isolates"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("table,count", [
    ("mibig_compounds", 0), ("mibig_compounds", 2), ("mibig_producer_isolates", 2),
])
def test_missing_and_duplicate_rows_rejected(inputs, table, count):
    inputs[table] *= count
    with pytest.raises(ValueError):
        seed.build_records(inputs)


def test_strain_field_cannot_masquerade_as_isolate(inputs):
    decision = inputs["mibig_producer_isolates"][0]
    decision["strain"] = decision.pop("isolate")
    with pytest.raises(ValueError, match="exact fields"):
        seed.build_records(inputs)


def test_unknown_field_rejected(inputs):
    inputs["mibig_producer_isolates"][0]["evidence_basis"] = "BGC_CHARACTERIZED"
    with pytest.raises(ValueError, match="exact fields"):
        seed.build_records(inputs)


@pytest.mark.parametrize("field,value", [("taxon_id", ""), ("standard_inchi_key", "")])
def test_qualification_must_reach_a_producer(inputs, field, value):
    source = inputs["mibig_compounds"][0]
    source[field] = value
    inputs["mibig_producer_isolates"][0]["expected_source_row_sha256"] = row_digest(source)
    with pytest.raises(ValueError, match="unnamed producer|did not reach a producer"):
        seed.build_records(inputs)


def test_isolate_needs_reassessment_after_structure_correction(inputs, monkeypatch):
    monkeypatch.setattr(seed, "apply_structure_corrections", lambda rows, *_: [
        {**row, "structure_correction_note": "Reassigned structure",
         "structure_correction_reference": "PMID:1"} for row in rows
    ])
    with pytest.raises(ValueError, match="isolate context needs review"):
        seed.build_records(inputs)


def test_withheld_nonorganism_producer_rejects_qualification(inputs):
    inputs["taxon_non_organism"] = [{"taxon_id": "NCBITaxon:62101", "reason": "test bin"}]
    with pytest.raises(ValueError, match="did not reach a producer"):
        seed.build_records(inputs)


def test_no_isolate_decisions_is_identity(inputs):
    assert load_producer_isolates(inputs["mibig_compounds"], []) == {}
