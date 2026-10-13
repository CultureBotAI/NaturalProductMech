"""Nonexact xrefs are withheld only through drift-guarded, attributed decisions."""

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

from naturalproductmech.curate.structure_corrections import row_digest
from naturalproductmech.curate.xref_exclusions import load_xref_exclusions
from naturalproductmech.validation.write_validated import validate_natural_product

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("seed_xref_tests", ROOT / "scripts/seed_from_sources.py")
seed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seed)


@pytest.fixture
def inputs():
    rows = [row for row in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
            if row["mibig_accession"] in ("BGC0000467", "BGC0001055", "BGC0002570")]
    return {"mibig_compounds": rows,
            "mibig_xref_exclusions": [
                d for d in seed.read_tsv(seed.MIBIG_XREF_EXCLUSIONS)
                if d["source_id"] == "BGC0000467:1"]}


def test_exact_owner_only_and_raw_source_preserved(inputs):
    original = deepcopy(inputs)
    baseline = seed.build_records({"mibig_compounds": inputs["mibig_compounds"]})
    after = seed.build_records(inputs)
    assert original == inputs
    before_by_id = {d["identifier"]: d for d in baseline}
    after_by_id = {d["identifier"]: d for d in after}
    sibling = "naturalproductmech:mibig-66a349ed2d"
    assert after_by_id[sibling] == before_by_id[sibling]
    owner = after_by_id["naturalproductmech:mibig-5395461679"]
    assert owner["xrefs"] == ["npatlas:NPA015861"]
    discussion = owner["discussions"].pop(0)
    assert discussion["status"] == "RESOLVED"
    assert "BGC0000467:1" in discussion["resolution_note"]
    assert "pubchem:5462519" in discussion["resolution_note"]
    assert inputs["mibig_xref_exclusions"][0]["expected_source_row_sha256"] in discussion["resolution_note"]
    owner["xrefs"].append("pubchem:5462519")
    assert after_by_id == before_by_id


def test_complete_row_drift_rejected(inputs):
    source = inputs["mibig_compounds"][0]
    assert source["mibig_accession"] == "BGC0000467"
    for field in source:
        changed = deepcopy(inputs)
        changed["mibig_compounds"][0][field] += " changed"
        with pytest.raises(ValueError):
            seed.build_records(changed)


@pytest.mark.parametrize("field", [
    "source_id", "expected_source_row_sha256", "xref", "reference", "curator", "date", "rationale",
])
@pytest.mark.parametrize("value", [None, "", " "])
def test_incomplete_decisions_fail(inputs, field, value):
    inputs["mibig_xref_exclusions"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("field,value", [
    ("source_id", "BGC0000467"), ("xref", "pubchem:0"), ("xref", "CHEBI:1"),
    ("xref", "pubchem:123"), ("reference", "https://"), ("reference", "uncited"),
    ("xref", "npatlas:NPA15870"), ("xref", "npatlas:npa015870"),
    ("xref", "NPAtlas:NPA015870"), ("xref", "npatlas:NPA015870.1"),
    ("date", "2026-02-30"), ("date", "20261013"), ("date", "2026-10-13 "),
    ("expected_source_row_sha256", "z" * 64), ("unexpected", "field"),
])
def test_malformed_decisions_fail(inputs, field, value):
    inputs["mibig_xref_exclusions"][0][field] = value
    with pytest.raises(ValueError):
        seed.build_records(inputs)


@pytest.mark.parametrize("count", [0, 2])
def test_target_must_be_unique(inputs, count):
    source = inputs["mibig_compounds"][0]
    inputs["mibig_compounds"] = [source] * count
    with pytest.raises(ValueError, match="exactly one"):
        seed.build_records(inputs)


def test_duplicate_decisions_fail(inputs):
    inputs["mibig_xref_exclusions"] *= 2
    with pytest.raises(ValueError, match="duplicate"):
        seed.build_records(inputs)


def test_structure_replacement_needs_new_adjudication(inputs, monkeypatch):
    monkeypatch.setattr(seed, "apply_structure_corrections", lambda rows, *_: [
        {**row, "structure_correction_note": "replaced"}
        if row["mibig_accession"] == "BGC0000467" else row for row in rows
    ])
    with pytest.raises(ValueError, match="need review after structure correction"):
        seed.build_records(inputs)


def test_reintroduced_assertion_cannot_silently_resolve(inputs):
    inputs["mibig_compounds"][2]["database_ids"] += "|pubchem:5462519"
    with pytest.raises(ValueError, match="reintroduced"):
        seed.build_records(inputs)


def test_exclusion_must_reach_emitted_owner(inputs):
    source = inputs["mibig_compounds"][0]
    source["standard_inchi_key"] = ""
    inputs["mibig_xref_exclusions"][0]["expected_source_row_sha256"] = row_digest(source)
    with pytest.raises(ValueError, match="did not reach a record"):
        seed.build_records(inputs)


def test_table_owned_adjudication_not_overwritten(inputs):
    owner = next(d for d in seed.build_records(inputs)
                 if d["identifier"] == "naturalproductmech:mibig-5395461679")
    stale = deepcopy(owner)
    stale["discussions"][0].update(status="OPEN", resolution_note="stale answer", evidence=[])
    expected = deepcopy(owner["discussions"])
    seed.carry_curator_owned_fields(owner, stale)
    assert owner["discussions"] == expected
    payload = {k: v for k, v in owner.items() if not k.startswith("_")}
    assert validate_natural_product(payload) == []


def test_multiple_xrefs_have_independent_decisions(inputs):
    row = inputs["mibig_compounds"][0]
    row["database_ids"] += "|pubchem:1"
    first = inputs["mibig_xref_exclusions"][0]
    first["expected_source_row_sha256"] = row_digest(row)
    inputs["mibig_xref_exclusions"].append({**first, "xref": "pubchem:1"})
    loaded = load_xref_exclusions(inputs["mibig_compounds"], inputs["mibig_xref_exclusions"])
    assert len(loaded["BGC0000467:1"]) == 2
    owner = next(d for d in seed.build_records(inputs)
                 if d["identifier"] == "naturalproductmech:mibig-5395461679")
    assert owner["xrefs"] == ["npatlas:NPA015861"]
    assert len({d["discussion_id"] for d in owner["discussions"]}) == 3


@pytest.fixture
def bacilysin_inputs():
    return {
        "mibig_compounds": [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
                            if r["mibig_accession"] in ("BGC0000888", "BGC0001184")],
        "mibig_xref_exclusions": [d for d in seed.read_tsv(seed.MIBIG_XREF_EXCLUSIONS)
                                  if d["source_id"] == "BGC0000888:1"],
    }


def test_bacilysin_withholds_only_two_nonexact_xrefs(bacilysin_inputs):
    original = deepcopy(bacilysin_inputs)
    baseline = seed.build_records({"mibig_compounds": bacilysin_inputs["mibig_compounds"]})
    after = seed.build_records(bacilysin_inputs)
    owner = next(d for d in after if d["identifier"] == "naturalproductmech:mibig-5044e5068f")
    assert "xrefs" not in owner
    discussions = owner.pop("discussions")
    assert len(discussions) == 2
    assert len({d["discussion_id"] for d in discussions}) == 2
    assert all(d["status"] == "RESOLVED" for d in discussions)
    atlas = next(d for d in discussions if "npatlas" in d["discussion_id"])
    assert "historical version 1" in atlas["resolution_note"]
    assert "stereo disagreement is unresolved" in atlas["resolution_note"]
    owner["xrefs"] = ["npatlas:NPA015870", "pubchem:160175"]
    assert after == baseline
    assert original == bacilysin_inputs


@pytest.mark.parametrize("failure", ["drift", "missing", "duplicate", "reintroduced"])
def test_npatlas_exclusions_fail_closed(bacilysin_inputs, failure):
    rows = bacilysin_inputs["mibig_compounds"]
    source = next(r for r in rows if r["mibig_accession"] == "BGC0000888")
    if failure == "drift":
        source["entry_version"] = "99"
    elif failure == "missing":
        bacilysin_inputs["mibig_compounds"].remove(source)
    elif failure == "duplicate":
        bacilysin_inputs["mibig_xref_exclusions"].append(
            deepcopy(bacilysin_inputs["mibig_xref_exclusions"][-1]))
    else:
        rows.append({**source, "mibig_accession": "BGC9999999", "database_ids": "npatlas:NPA015870"})
    with pytest.raises(ValueError):
        seed.build_records(bacilysin_inputs)


def test_yersiniabactin_strain_decisions_preserve_other_claims(inputs):
    decisions = [d for d in seed.read_tsv(seed.MIBIG_PRODUCER_STRAINS)
                 if d["source_id"] in ("BGC0001055:1", "BGC0000467:1")]
    assert len(decisions) == 2
    baseline = seed.build_records(inputs)
    after = seed.build_records({**inputs, "mibig_producer_strains": decisions})
    expected = {"mibig:BGC0001055": "A0 34/86", "mibig:BGC0000467": "WA-314 (sub_strain WA-C)"}
    seen = set()
    for owner in after:
        for producer in owner["producer_organisms"]:
            bgc = producer["biosynthetic_gene_cluster"]
            if bgc in expected:
                assert producer.pop("strain") == expected[bgc]
                assert producer["evidence"].pop()["evidence_type"] == "CURATOR_INFERENCE"
                seen.add(bgc)
    assert seen == set(expected)
    assert after == baseline
