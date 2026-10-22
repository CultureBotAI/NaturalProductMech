"""LOTUS exclusions are exact-triple decisions, not taxon-wide filters."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

from naturalproductmech.curate.lotus_exclusions import load_lotus_exclusions, lotus_key
from naturalproductmech.curate.structure_corrections import row_digest
from naturalproductmech.validation.write_validated import validate_natural_product

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_lotus_exclusions", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)
KEY = "QTQAWLPCGQOSGP-KSRBKZBZSA-N"


@pytest.fixture
def inputs():
    return {
        "mibig_compounds": [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
                            if r["mibig_accession"] in ("BGC0000066", "BGC0000067")],
        "lotus_occurrences": [r for r in seed.read_tsv(ROOT / "data/raw/lotus_occurrences.tsv")
                              if r["standard_inchi_key"] == KEY],
        "lotus_occurrence_exclusions": [
            r for r in seed.read_tsv(ROOT / "curation/lotus_occurrence_exclusions.tsv")
            if r["standard_inchi_key"] == KEY
        ],
        "taxon_groups": seed.read_tsv(ROOT / "data/raw/taxon_groups.tsv"),
    }


def test_exact_triple_only_and_facets_recomputed(inputs):
    raw = inputs["lotus_occurrences"][0]
    original = deepcopy(inputs)
    baseline = seed.build_records({k: v for k, v in inputs.items() if k != "lotus_occurrence_exclusions"})
    after = seed.build_records(inputs)
    assert inputs == original
    for old, new in zip(baseline, after, strict=True):
        if new["chemical_structure"]["standard_inchi_key"] != KEY:
            assert new == old
            continue
        assert old["occurrence_taxon_groups"] == ["ACTINOBACTERIAL", "FUNGAL"]
        assert new["occurrence_taxon_groups"] == ["ACTINOBACTERIAL"]
        assert len(new["occurrences"]) == 3
        discussion, = new.pop("discussions")
        assert discussion["status"] == "RESOLVED"
        assert row_digest(raw) in discussion["resolution_note"]
        old["occurrences"].pop(0)
        old["occurrence_taxon_groups"].remove("FUNGAL")
        assert old == new


def test_other_doi_taxon_or_structure_not_excluded(inputs):
    raw = inputs["lotus_occurrences"][0]
    other_key = inputs["mibig_compounds"][0]["standard_inchi_key"]
    inputs["lotus_occurrences"] += [dict(raw, reference_doi="10.1000/other"),
        dict(raw, taxon_id="NCBITaxon:1912", organism_name="Streptomyces hygroscopicus"),
        dict(raw, standard_inchi_key=other_key)]
    after = seed.build_records(inputs)
    owner = next(d for d in after if d["chemical_structure"]["standard_inchi_key"] == KEY)
    assert len(owner["occurrences"]) == 5
    assert "FUNGAL" in owner["occurrence_taxon_groups"]
    sibling = next(d for d in after if d["chemical_structure"]["standard_inchi_key"] == other_key)
    assert len(sibling["occurrences"]) == 1


def test_stale_answer_cannot_override_and_sole_occurrence_removed(inputs):
    inputs["lotus_occurrences"] = inputs["lotus_occurrences"][:1]
    owner = next(d for d in seed.build_records(inputs)
                 if d["chemical_structure"]["standard_inchi_key"] == KEY)
    assert "occurrences" not in owner and "occurrence_taxon_groups" not in owner
    stale = deepcopy(owner)
    stale["discussions"][0].update(status="OPEN", resolution_note="stale", evidence=[])
    expected = deepcopy(owner)
    seed.carry_curator_owned_fields(owner, stale)
    assert owner == expected
    assert validate_natural_product({k: v for k, v in owner.items() if not k.startswith("_")}) == []


def test_every_source_field_is_pinned(inputs):
    for field in inputs["lotus_occurrences"][0]:
        changed = deepcopy(inputs)
        changed["lotus_occurrences"][0][field] += " changed"
        with pytest.raises(ValueError):
            seed.build_records(changed)


@pytest.mark.parametrize("field", ["standard_inchi_key", "taxon_id", "reference_doi",
    "expected_source_row_sha256", "reference", "curator", "date", "rationale"])
@pytest.mark.parametrize("value", [None, "", " "])
def test_missing_attribution_rejected(inputs, field, value):
    inputs["lotus_occurrence_exclusions"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("field,value", [
    ("standard_inchi_key", "invalid"), ("taxon_id", "NCBITaxon:0"),
    ("reference_doi", "not-doi"), ("date", "20261014"), ("date", "2026-02-30"),
    ("reference", "https://"), ("reference", "http://example.org"),
    ("expected_source_row_sha256", "z" * 64), ("extra", "field")])
def test_malformed_decision_rejected(inputs, field, value):
    inputs["lotus_occurrence_exclusions"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("count", [0, 2])
def test_unique_source_required(inputs, count):
    inputs["lotus_occurrences"] = inputs["lotus_occurrences"][:1] * count
    with pytest.raises(ValueError, match="exactly one source row"):
        seed.build_records(inputs)


def test_duplicate_decision_rejected(inputs):
    inputs["lotus_occurrence_exclusions"] *= 2
    with pytest.raises(ValueError, match="duplicate"):
        seed.build_records(inputs)


@pytest.mark.parametrize("empty", [True, False])
def test_decision_must_reach_owner(inputs, empty):
    inputs["mibig_compounds"] = [] if empty else inputs["mibig_compounds"][:1]
    with pytest.raises(ValueError, match="did not reach a record"):
        seed.build_records(inputs)


def test_loader_does_not_mutate_sources_or_decisions(inputs):
    before = deepcopy(inputs)
    loaded = load_lotus_exclusions(inputs["lotus_occurrences"], inputs["lotus_occurrence_exclusions"])
    assert list(loaded) == [lotus_key(inputs["lotus_occurrences"][0])]
    next(iter(loaded.values()))["rationale"] = "different"
    assert inputs == before


def test_committed_desosamine_narbonensis_exclusion_removes_sole_occurrence():
    des_key = "ZOYWWAGVGBSJDL-UHFFFAOYSA-N"
    subset = {
        "mibig_compounds": [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
                            if r["mibig_accession"] == "BGC0000899"],
        "lotus_occurrences": [r for r in seed.read_tsv(ROOT / "data/raw/lotus_occurrences.tsv")
                              if r["standard_inchi_key"] == des_key],
        "lotus_occurrence_exclusions": [
            r for r in seed.read_tsv(ROOT / "curation/lotus_occurrence_exclusions.tsv")
            if r["standard_inchi_key"] == des_key
        ],
        "taxon_groups": seed.read_tsv(ROOT / "data/raw/taxon_groups.tsv"),
    }
    before, = seed.build_records({k: v for k, v in subset.items() if k != "lotus_occurrence_exclusions"})
    after, = seed.build_records(subset)
    assert before["occurrence_taxon_groups"] == ["ACTINOBACTERIAL"]
    assert len(before["occurrences"]) == 1
    assert "occurrences" not in after and "occurrence_taxon_groups" not in after
    discussion, = after["discussions"]
    digest = row_digest(subset["lotus_occurrences"][0])
    assert discussion["discussion_id"] == f"source-lotus-exclusion-{digest}"
    assert discussion["status"] == "RESOLVED"
    assert digest in discussion["resolution_note"]

