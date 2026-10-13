"""Assay exclusions must be attributable, drift guarded and exact-row scoped."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

from naturalproductmech.curate.bioassay_exclusions import assay_key, load_bioassay_exclusions
from naturalproductmech.curate.structure_corrections import row_digest
from naturalproductmech.validation.write_validated import validate_natural_product

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_assay_exclusions", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)
KEY = "BDTQHFBWYNCGHN-CUYCKOLISA-N"


@pytest.fixture
def inputs():
    sources = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in ("BGC0000696", "BGC0001603")]
    assays = [r for r in seed.read_tsv(ROOT / "data/raw/pubchem_bioassay.tsv")
              if r["standard_inchi_key"] == KEY]
    assert len(assays) == 1
    decision = {k: assays[0][k] for k in ("standard_inchi_key", "cid", "aid")}
    decision.update(expected_source_row_sha256=row_digest(assays[0]),
                    reference="https://pubchem.ncbi.nlm.nih.gov/bioassay/1195",
                    curator="codex", date="2026-10-13",
                    rationale="Nonexact CID; dose metadata, not activity.")
    return {"mibig_compounds": sources, "pubchem_bioassay": assays,
            "pubchem_bioassay_exclusions": [decision]}


def test_exact_row_removed_but_other_assays_and_owners_unchanged(inputs):
    original = inputs["pubchem_bioassay"][0]
    other_key = inputs["mibig_compounds"][1]["standard_inchi_key"]
    inputs["pubchem_bioassay"] += [
        {**original, "aid": "999", "assay_name": "Experimental antibacterial inhibition",
         "activity_name": "IC50", "activity_value_um": "2"},
        {**original, "cid": "999"},
        {**original, "standard_inchi_key": other_key},
    ]
    pristine = deepcopy(inputs)
    baseline = seed.build_records({k: v for k, v in inputs.items() if k != "pubchem_bioassay_exclusions"})
    after = seed.build_records(inputs)
    assert inputs == pristine
    for old, new in zip(baseline, after, strict=True):
        if new["chemical_structure"]["standard_inchi_key"] != KEY:
            assert new == old
            continue
        assert len(new["bioactivities"]) == 2
        assert any(b.get("value") == 2 for b in new["bioactivities"])
        assert len(old["bioactivities"]) == 3
        assert new["bioactivity_summary"] == old["bioactivity_summary"]
        discussion, = new.pop("discussions")
        assert discussion["status"] == "RESOLVED"
        assert row_digest(original) in discussion["resolution_note"]
        assert "raw inventory is unchanged" in discussion["resolution_note"]
        old["bioactivities"].remove(next(b for b in old["bioactivities"] if "value" not in b))
        assert new == old


def test_sole_excluded_call_has_no_activity_or_summary(inputs):
    owner = next(d for d in seed.build_records(inputs)
                 if d["chemical_structure"]["standard_inchi_key"] == KEY)
    assert "bioactivities" not in owner and "bioactivity_summary" not in owner
    assert "pubchem:72396" in owner["xrefs"]  # xref and assay decisions are independent
    stale = deepcopy(owner)
    stale["discussions"][0].update(status="OPEN", resolution_note="stale answer", evidence=[])
    expected = deepcopy(owner["discussions"])
    seed.carry_curator_owned_fields(owner, stale)
    assert owner["discussions"] == expected
    assert validate_natural_product({k: v for k, v in owner.items() if not k.startswith("_")}) == []


def test_every_source_field_is_pinned(inputs):
    for field in inputs["pubchem_bioassay"][0]:
        changed = deepcopy(inputs)
        changed["pubchem_bioassay"][0][field] += " changed"
        with pytest.raises(ValueError):
            seed.build_records(changed)


@pytest.mark.parametrize("field", [
    "standard_inchi_key", "cid", "aid", "expected_source_row_sha256",
    "reference", "curator", "date", "rationale",
])
@pytest.mark.parametrize("value", [None, "", " "])
def test_incomplete_attribution_rejected(inputs, field, value):
    inputs["pubchem_bioassay_exclusions"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("field,value", [
    ("cid", "0"), ("cid", "01"), ("aid", "1195 "), ("aid", "1.0"),
    ("standard_inchi_key", "BDTQHFBWYNCGHN"), ("date", "20261013"),
    ("date", "2026-02-30"), ("reference", "http://example.org"),
    ("reference", "https://"), ("reference", "uncited"),
    ("expected_source_row_sha256", "z" * 64), ("extra", "field"),
])
def test_malformed_decisions_rejected(inputs, field, value):
    inputs["pubchem_bioassay_exclusions"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("count", [0, 2])
def test_missing_or_ambiguous_source_rejected(inputs, count):
    inputs["pubchem_bioassay"] *= count
    with pytest.raises(ValueError, match="exactly one source row"):
        seed.build_records(inputs)


def test_duplicate_decisions_rejected(inputs):
    inputs["pubchem_bioassay_exclusions"] *= 2
    with pytest.raises(ValueError, match="duplicate"):
        seed.build_records(inputs)


@pytest.mark.parametrize("empty", [True, False])
def test_decision_must_reach_emitted_owner(inputs, empty):
    inputs["mibig_compounds"] = [] if empty else [inputs["mibig_compounds"][1]]
    with pytest.raises(ValueError, match="did not reach a record"):
        seed.build_records(inputs)


def test_loader_copies_decisions_and_does_not_modify_sources(inputs):
    before = deepcopy(inputs)
    loaded = load_bioassay_exclusions(inputs["pubchem_bioassay"], inputs["pubchem_bioassay_exclusions"])
    assert list(loaded) == [assay_key(inputs["pubchem_bioassay"][0])]
    next(iter(loaded.values()))["rationale"] = "new"
    assert inputs == before
