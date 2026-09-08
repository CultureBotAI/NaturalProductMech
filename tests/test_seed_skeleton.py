"""The seeder's rules, tested at M1 while they are still cheap to change.

The harmonizer itself is M2. What is testable now is everything that decides
whether the harmonizer can be trusted: identity minting, the producer-evidence
grading, the filing tie-break, and the safety rails.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("seed_from_sources",
                                              REPO_ROOT / "scripts" / "seed_from_sources.py")
seed = importlib.util.module_from_spec(spec)
sys.modules["seed_from_sources"] = seed
spec.loader.exec_module(seed)


def test_minting_ignores_the_label():
    """A minted CURIE is the key curation decisions are written against, so an
    upstream label correction must not move it."""
    a = seed.mint_identifier("MIBIG", "BGC0000055")
    b = seed.mint_identifier("MIBIG", "BGC0000055")
    assert a == b
    assert a != seed.mint_identifier("MIBIG", "BGC0000056")
    assert a != seed.mint_identifier("CHEBI", "BGC0000055")
    assert a.startswith("naturalproductmech:mibig-")


def test_producer_evidence_map_covers_the_mibig_vocabulary():
    mapping = seed.load_producer_evidence_map()
    assert mapping["Knock-out studies"] == "BGC_CHARACTERIZED"
    assert mapping["Heterologous expression"] == "BGC_CHARACTERIZED"
    assert mapping["Gene expression correlated with compound production"] == "BGC_CORRELATED"
    assert mapping["Correlation of genomic and metabolomic data"] == "BGC_CORRELATED"
    assert mapping["Homology-based prediction"] == "NOT_PRODUCER_GRADE"


def test_homology_prediction_is_not_a_producer_claim():
    mapping = seed.load_producer_evidence_map()
    assert seed.grade_producer_evidence(["Homology-based prediction"], mapping) is None


def test_the_strongest_basis_wins_when_a_locus_has_several():
    mapping = seed.load_producer_evidence_map()
    methods = ["Correlation of genomic and metabolomic data", "Knock-out studies"]
    assert seed.grade_producer_evidence(methods, mapping) == "BGC_CHARACTERIZED"


def test_correlation_alone_stays_correlational():
    """The finding behind issue #3: this must not silently become CHARACTERIZED."""
    mapping = seed.load_producer_evidence_map()
    methods = ["Gene expression correlated with compound production"]
    assert seed.grade_producer_evidence(methods, mapping) == "BGC_CORRELATED"


def test_an_unknown_evidence_method_fails_closed():
    """A vocabulary that grew upstream should be looked at, not admitted."""
    mapping = seed.load_producer_evidence_map()
    assert seed.grade_producer_evidence(["Vibes"], mapping) is None


def test_one_pathway_files_the_record():
    assert seed.choose_pathway(["Polyketides"]) == "POLYKETIDES"
    assert seed.choose_pathway(["Shikimates and Phenylpropanoids"]) == \
        "SHIKIMATES_AND_PHENYLPROPANOIDS"


def test_several_pathways_file_unclassified_rather_than_picking_by_order():
    """Issue #4. Picking the first array element is how a corpus ends up
    asserting a classification nothing decided."""
    assert seed.choose_pathway(["Polyketides", "Terpenoids"]) == "UNCLASSIFIED"
    assert seed.choose_pathway([]) == "UNCLASSIFIED"


def test_an_unrecognised_pathway_label_is_unclassified_not_a_new_directory():
    assert seed.choose_pathway(["Something New"]) == "UNCLASSIFIED"


def test_every_pathway_enum_value_has_a_directory():
    """A schema value with no directory would crash the first record that used it."""
    import yaml
    schema = yaml.safe_load(
        (REPO_ROOT / "src" / "naturalproductmech" / "schema" / "naturalproductmech.yaml")
        .read_text(encoding="utf-8"))
    values = set(schema["enums"]["NPPathwayEnum"]["permissible_values"])
    assert values == set(seed.PATHWAY_DIRS)


def test_prune_is_refused_on_a_partial_run(monkeypatch, capsys):
    """--prune with --only would delete records the run never built."""
    monkeypatch.setattr(sys, "argv", ["seed", "--apply", "--prune", "--only", "CHEBI:42355"])
    assert seed.main() == 2
    assert "refusing --prune" in capsys.readouterr().err


def test_an_empty_data_raw_seeds_nothing_and_says_so(capsys):
    """The M1 state is reported honestly rather than as a success or a crash."""
    assert seed.build_records({}) == []


def test_inventories_present_without_a_harmonizer_is_a_loud_failure():
    """Fail closed: silently writing nothing when inventories exist would look
    identical to a clean run."""
    with pytest.raises(NotImplementedError):
        seed.build_records({"mibig_compounds": [{"a": "b"}]})
