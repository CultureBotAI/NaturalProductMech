"""Claim citation corrections are source-pinned and do not grade experiments."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

from naturalproductmech.curate.claim_references import correct_claim_reference, load_claim_references
from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_reference_test", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


@pytest.fixture
def inputs():
    source, = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] == "BGC0002527"]
    decision, = [r for r in seed.read_tsv(seed.MIBIG_CLAIM_REFERENCES)
                 if r["source_id"] == "BGC0002527:1"]
    return {"mibig_compounds": [source], "mibig_claim_references": [decision]}


def test_only_exact_claim_citations_change_and_raw_rows_survive(inputs):
    original = deepcopy(inputs)
    before, = seed.build_records({"mibig_compounds": inputs["mibig_compounds"]})
    after, = seed.build_records(inputs)
    for field in ("producer_organisms", "biosynthetic_gene_clusters"):
        claim = after[field][0]
        assert claim["evidence"][0]["reference"] == "PMID:26452553"
        assert claim["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
        correction = claim["evidence"].pop()
        assert correction["evidence_type"] == "CURATOR_INFERENCE"
        assert "DOI:10.1021/ic9016883 (COMPOUND_BIOACTIVITY)" in correction["notes"]
        assert original["mibig_claim_references"][0]["expected_source_row_sha256"] in correction["notes"]
        claim["evidence"][0] = before[field][0]["evidence"][0]
    assert before == after and inputs == original


def test_producer_and_locus_can_use_distinct_reviewed_references(inputs):
    inputs["mibig_claim_references"][0]["producer_reference"] = "PMID:1"
    doc, = seed.build_records(inputs)
    assert doc["producer_organisms"][0]["evidence"][0]["reference"] == "PMID:1"
    assert doc["biosynthetic_gene_clusters"][0]["evidence"][0]["reference"] == "PMID:26452553"
    assert doc["producer_organisms"][0]["evidence"] is not doc["biosynthetic_gene_clusters"][0]["evidence"]


def test_every_raw_source_field_is_pinned(inputs):
    for field in inputs["mibig_compounds"][0]:
        changed = deepcopy(inputs)
        changed["mibig_compounds"][0][field] += " changed"
        with pytest.raises(ValueError):
            seed.build_records(changed)


@pytest.mark.parametrize("field,value", [
    ("source_id", "BGC0002527:0"), ("source_id", "BGC0002527"),
    ("expected_source_row_sha256", "g" * 64), ("producer_reference", "PMID:0"),
    ("locus_reference", "https://"), ("source_reference", "http://example.org"),
    ("source_reference", "https://example.org/has space"),
    ("curator", " codex"), ("rationale", ""), ("date", "2026-02-30"),
    ("date", "20261013"),
])
def test_invalid_decision_rejected(inputs, field, value):
    inputs["mibig_claim_references"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


def test_missing_extra_or_empty_fields_rejected(inputs):
    for field in inputs["mibig_claim_references"][0]:
        for value in (None, "", " "):
            changed = deepcopy(inputs)
            changed["mibig_claim_references"][0][field] = value
            with pytest.raises(ValueError):
                seed.build_records(changed)
        changed = deepcopy(inputs)
        del changed["mibig_claim_references"][0][field]
        with pytest.raises(ValueError):
            seed.build_records(changed)
    inputs["mibig_claim_references"][0]["evidence_basis"] = "BGC_CHARACTERIZED"
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("table,count", [
    ("mibig_compounds", 0), ("mibig_compounds", 2), ("mibig_claim_references", 2),
])
def test_missing_and_duplicate_targets_rejected(inputs, table, count):
    inputs[table] *= count
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("change", ["unnamed", "withheld", "unemitted", "structure"])
def test_decision_cannot_silently_disappear_or_cross_identity(inputs, change, monkeypatch):
    row = inputs["mibig_compounds"][0]
    if change == "unnamed":
        row["taxon_id"] = ""
    elif change == "withheld":
        inputs["taxon_non_organism"] = [{"taxon_id": row["taxon_id"], "reason": "test"}]
    elif change == "unemitted":
        row["standard_inchi_key"] = ""
    else:
        original = seed.apply_structure_corrections

        def corrected(*args):
            return [{**r, "structure_correction_note": "test",
                     "structure_correction_reference": "PMID:1"} for r in original(*args)]

        monkeypatch.setattr(seed, "apply_structure_corrections", corrected)
    inputs["mibig_claim_references"][0]["expected_source_row_sha256"] = row_digest(row)
    with pytest.raises(ValueError):
        seed.build_records(inputs)


def test_no_decisions_preserves_ordinary_source_routing(inputs):
    assert load_claim_references(inputs["mibig_compounds"], []) == {}
    doc, = seed.build_records({"mibig_compounds": inputs["mibig_compounds"]})
    assert doc["producer_organisms"][0]["evidence"][0]["reference"] == "DOI:10.1021/ic9016883"


def test_other_qualifications_are_not_overwritten(inputs):
    source = inputs["mibig_compounds"][0]
    evidence = {"reference": "PMID:1", "evidence_type": "CURATOR_INFERENCE", "notes": "Other decision."}
    claim = {"evidence": seed.mibig_evidence(source) + [deepcopy(evidence)]}
    correct_claim_reference(claim, source, inputs["mibig_claim_references"][0], field="locus_reference")
    assert claim["evidence"][1] == evidence and len(claim["evidence"]) == 3
    with pytest.raises(ValueError, match="unsupported"):
        correct_claim_reference(claim, source, inputs["mibig_claim_references"][0], field="unreviewed")


@pytest.mark.parametrize("accession,reference", [
    ("BGC0002527", "PMID:26452553"),
    ("BGC0001542", "PMID:28535078"),
])
def test_committed_citation_decisions_are_claim_local(accession, reference):
    sources = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in {accession, "BGC0001541"}]
    decision, = [r for r in seed.read_tsv(seed.MIBIG_CLAIM_REFERENCES)
                 if r["source_id"] == f"{accession}:1"]
    original_sources = deepcopy(sources)
    before = seed.build_records({"mibig_compounds": sources})
    after = seed.build_records({"mibig_compounds": sources,
                               "mibig_claim_references": [decision]})
    source, = [r for r in sources if r["mibig_accession"] == accession]
    for old, current in zip(before, after, strict=True):
        if old["chemical_structure"]["standard_inchi_key"] != source["standard_inchi_key"]:
            assert current == old
            continue
        assert (current["producer_organisms"][0]["evidence"]
                is not current["biosynthetic_gene_clusters"][0]["evidence"])
        for field in ("producer_organisms", "biosynthetic_gene_clusters"):
            evidence = current[field][0]["evidence"]
            assert evidence[0]["reference"] == reference
            assert evidence[0]["evidence_type"] == "DATABASE_ASSERTION"
            assert evidence[-1]["evidence_type"] == "CURATOR_INFERENCE"
            assert source["primary_reference"] in evidence[-1]["notes"]
            assert row_digest(source) in evidence[-1]["notes"]
            current[field][0]["evidence"] = old[field][0]["evidence"]
        assert current == old
    assert sources == original_sources
