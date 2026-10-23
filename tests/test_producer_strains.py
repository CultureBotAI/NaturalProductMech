"""Strain qualifications are narrow, pinned, and never change evidence grades."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from naturalproductmech.curate.producer_strains import load_producer_strains, qualify_producer
from naturalproductmech.curate.structure_corrections import row_digest


@pytest.fixture
def source():
    return {"mibig_accession": "BGC0000258", "compound_index": "1",
            "entry_version": "3", "taxon_id": "NCBITaxon:616", "taxon_label": "Serratia sp.",
            "standard_inchi_key": "WKGQSEFBQTWRPT-UUPRNIFOSA-N", "empty": ""}


@pytest.fixture
def qualification(source):
    return {"source_id": "BGC0000258:1", "expected_source_row_sha256": row_digest(source),
            "strain": "ATCC 39006", "reference": "PMID:15528645", "curator": "codex",
            "date": "2026-10-13", "rationale": "Inspected source identifies this strain."}


def test_qualification_preserves_input_and_producer_assertion(source, qualification):
    original = deepcopy(source)
    loaded = load_producer_strains([source], [qualification])
    assert source == original
    producer = {"taxon_id": "NCBITaxon:616", "taxon_label": "Serratia sp.",
                "evidence_basis": "SOURCE_ASSERTION", "source": "MIBIG",
                "evidence": [{"reference": "PMID:15528645", "evidence_type": "DATABASE_ASSERTION"}]}
    before = deepcopy(producer)
    qualify_producer(producer, loaded["BGC0000258:1"])
    assert producer.pop("strain") == "ATCC 39006"
    extra = producer["evidence"].pop()
    assert extra["evidence_type"] == "CURATOR_INFERENCE"
    assert qualification["expected_source_row_sha256"] in extra["notes"]
    assert "codex" in extra["notes"]
    assert producer == before


@pytest.mark.parametrize("field,value", [
    ("entry_version", "4"), ("taxon_id", "NCBITaxon:615"),
    ("standard_inchi_key", "different"), ("empty", "new content"),
])
def test_source_drift_fails_closed(source, qualification, field, value):
    source[field] = value
    with pytest.raises(ValueError, match="source drift"):
        load_producer_strains([source], [qualification])


@pytest.mark.parametrize("field,value", [
    ("strain", " "), ("reference", "not a reference"), ("reference", "http://example.org/paper"),
    ("curator", ""), ("rationale", ""), ("date", "2026-02-30"), ("date", "20261013"),
    ("expected_source_row_sha256", "bad"), ("source_id", "BGC0000258"),
])
def test_invalid_qualification_rejected(source, qualification, field, value):
    qualification[field] = value
    with pytest.raises(ValueError):
        load_producer_strains([source], [qualification])


def test_missing_duplicate_and_unknown_fields_rejected(source, qualification):
    for rows in ([], [source, source], [{**source, "compound_index": "2"}]):
        with pytest.raises(ValueError, match="exactly one"):
            load_producer_strains(rows, [qualification])
    with pytest.raises(ValueError, match="duplicate"):
        load_producer_strains([source], [qualification, qualification])
    with pytest.raises(ValueError, match="exact fields"):
        load_producer_strains([source], [{**qualification, "evidence_basis": "BGC_CHARACTERIZED"}])
    assert load_producer_strains([source], []) == {}


def test_cannot_qualify_an_unnamed_producer(source, qualification):
    source["taxon_id"] = ""
    qualification["expected_source_row_sha256"] = row_digest(source)
    with pytest.raises(ValueError, match="unnamed producer"):
        load_producer_strains([source], [qualification])


@pytest.mark.parametrize("relpath,expected,curator_token", [
    ("alkaloids/prodigiosin", [("mibig:BGC0002675", "S4059", "BGC_CHARACTERIZED")], "codex"),
    ("alkaloids/prodigiosin-2", [("mibig:BGC0000258", "ATCC 39006", "SOURCE_ASSERTION"),
                                 ("mibig:BGC0000259", "ATCC 274", "SOURCE_ASSERTION")], "codex"),
    ("carbohydrates/desosamine-2", [("mibig:BGC0000898", "ATCC 15439", "SOURCE_ASSERTION")], "antigravity"),
    ("polyketides/methymycin", [("mibig:BGC0000094", "ATCC 15439", "SOURCE_ASSERTION")], "antigravity"),
    ("polyketides/neomethymycin", [("mibig:BGC0000898", "ATCC 15439", "SOURCE_ASSERTION")], "antigravity"),
    ("polyketides/narbomycin", [("mibig:BGC0000898", "ATCC 15439", "SOURCE_ASSERTION")], "antigravity"),
    ("polyketides/pikromycin", [("mibig:BGC0000898", "ATCC 15439", "SOURCE_ASSERTION")], "antigravity"),
    (
        "amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate",
        [("mibig:BGC0000405", "Wisconsin 54-1255", "SOURCE_ASSERTION")],
        "antigravity",
    ),
    (
        "amino_acids_and_peptides/isopenicillin-n",
        [("mibig:BGC0000405", "Wisconsin 54-1255", "SOURCE_ASSERTION")],
        "antigravity",
    ),
    (
        "amino_acids_and_peptides/benzylpenicillin-sodium",
        [
            ("mibig:BGC0000404", "AS-P-78", "SOURCE_ASSERTION"),
            ("mibig:BGC0000405", "Wisconsin 54-1255", "SOURCE_ASSERTION"),
        ],
        "antigravity",
    ),
])
def test_curated_strain_context_keeps_database_assertions(relpath, expected, curator_token):
    root = Path(__file__).resolve().parents[1]
    record = yaml.safe_load((root / f"data/natural_products/{relpath}.yaml").read_text())
    producers = {p["biosynthetic_gene_cluster"]: p for p in record["producer_organisms"]}
    for bgc, strain, grade in expected:
        producer = producers[bgc]
        assert producer["strain"] == strain
        assert producer["evidence_basis"] == grade
        assert producer["source"] == "MIBIG"
        assert producer["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
        assert producer["evidence"][-1]["evidence_type"] == "CURATOR_INFERENCE"
        assert curator_token in producer["evidence"][-1]["notes"]
    assert record["curation_status"] == "SEEDED"
