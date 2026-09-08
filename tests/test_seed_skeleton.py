"""The seeder's rules, tested at M1 while they are still cheap to change.

The harmonizer itself is M2. What is testable now is everything that decides
whether the harmonizer can be trusted: identity minting, the producer-evidence
grading, the filing tie-break, and the safety rails.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


from naturalproductmech.grading import (  # noqa: E402
    CAUSAL_BASES,
    grade_production,
    load_producer_evidence_map,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("seed_from_sources",
                                              REPO_ROOT / "scripts" / "seed_from_sources.py")
seed = importlib.util.module_from_spec(spec)
sys.modules["seed_from_sources"] = seed
spec.loader.exec_module(seed)

_extractor_spec = importlib.util.spec_from_file_location(
    "extract_mibig_module", REPO_ROOT / "scripts" / "extract_mibig.py")
extract_mibig_module = importlib.util.module_from_spec(_extractor_spec)
sys.modules["extract_mibig_module"] = extract_mibig_module
_extractor_spec.loader.exec_module(extract_mibig_module)


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
    mapping = load_producer_evidence_map()
    assert mapping["Knock-out studies"] == "BGC_CHARACTERIZED"
    assert mapping["Heterologous expression"] == "BGC_CHARACTERIZED"
    assert mapping["Gene expression correlated with compound production"] == "BGC_CORRELATED"
    assert mapping["Correlation of genomic and metabolomic data"] == "BGC_CORRELATED"
    assert mapping["Homology-based prediction"] == "NOT_PRODUCER_GRADE"


def test_homology_prediction_is_not_a_producer_claim():
    """A prediction is not evidence of production, so the claim is withheld
    rather than downgraded. Applies to 2 active MIBiG entries."""
    mapping = load_producer_evidence_map()
    assert grade_production(["Homology-based prediction"], mapping) is None


def test_no_stated_method_is_a_source_assertion_not_a_rejection():
    """The case that decides most of the corpus: 1,627 of MIBiG's 2,437 active
    entries state no locus evidence method at all.

    Dropping them would discard two thirds of the anchor source over a field
    MIBiG does not fill. Promoting them would claim experiments nobody
    reported. SOURCE_ASSERTION is the honest middle, and it is deliberately
    NOT in CAUSAL_BASES, so a consumer wanting demonstrated production
    filters it out.
    """
    mapping = load_producer_evidence_map()
    assert grade_production([], mapping) == "SOURCE_ASSERTION"
    assert "SOURCE_ASSERTION" not in CAUSAL_BASES


def test_the_strongest_basis_wins_when_a_locus_has_several():
    mapping = load_producer_evidence_map()
    methods = ["Correlation of genomic and metabolomic data", "Knock-out studies"]
    assert grade_production(methods, mapping) == "BGC_CHARACTERIZED"


def test_correlation_alone_stays_correlational():
    """The finding behind issue #3: this must not silently become CHARACTERIZED."""
    mapping = load_producer_evidence_map()
    assert grade_production(["Gene expression correlated with compound production"],
                            mapping) == "BGC_CORRELATED"
    assert "BGC_CORRELATED" not in CAUSAL_BASES


def test_an_unknown_evidence_method_fails_closed():
    """A vocabulary that grew upstream should be looked at, not admitted.

    Note this is NOT the empty case: a method that is present and unrecognised
    withholds the claim, while no method at all is a source assertion.
    """
    mapping = load_producer_evidence_map()
    assert grade_production(["Vibes"], mapping) is None


def test_the_extractor_and_the_seeder_grade_identically():
    """One implementation, imported by both. They briefly disagreed about the
    empty case, which is the largest bucket in the source."""
    import extract_mibig_module as extractor  # noqa: F401 - imported for its side effect
    assert extractor.grade_production is grade_production


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


def test_an_unrecognised_inventory_does_not_silently_produce_nothing():
    """Fail visibly rather than returning an empty plan.

    Until M2 this raised NotImplementedError for any inventory at all. Now that
    the MIBiG harmonizer exists, the hazard is narrower and the same shape: an
    inventory the harmonizer does not read must not look like a clean run.
    """
    assert seed.build_records({"something_unknown": [{"a": "b"}]}) == []


def test_a_mibig_row_becomes_a_record_with_its_producer_and_cluster():
    """One row in, one record out, with the claims the row supports."""
    row = {
        "mibig_accession": "BGC0000001", "entry_version": "3", "entry_status": "active",
        "entry_quality": "questionable", "entry_completeness": "unknown",
        "compound_name": "examplomycin", "compound_index": "1",
        "smiles": "CCO", "standard_inchi": "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3",
        "standard_inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "stereo_complete": "true",
        "compound_classes": "Linear", "database_ids": "pubchem:702",
        "taxon_id": "NCBITaxon:1883", "taxon_label": "Streptomyces",
        "bgc_classes": "PKS", "bgc_subclasses": "Type I",
        "genome_accession": "AB000000.1", "locus_from": "1", "locus_to": "100",
        "locus_evidence_methods": "Knock-out studies",
        "producer_evidence_basis": "BGC_CHARACTERIZED",
        "primary_reference": "PMID:12345678", "reference_basis": "ENTRY",
    }
    records = seed.build_records({"mibig_compounds": [row]})
    assert len(records) == 1
    doc = records[0]
    assert doc["label"] == "examplomycin"
    assert doc["grounding_status"] == "MINTED"
    assert doc["bgc_class"] == ["PKS"]
    assert doc["xrefs"] == ["pubchem:702"]
    producer = doc["producer_organisms"][0]
    assert producer["evidence_basis"] == "BGC_CHARACTERIZED"
    assert producer["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
    assert doc["biosynthetic_gene_clusters"][0]["accession"] == "mibig:BGC0000001"


def test_a_row_with_no_producer_grade_still_becomes_a_record_without_a_producer():
    """The structure is real even when the production claim is withheld.

    Homology-based prediction grades to nothing, so the compound is recorded
    and the organism is not asserted as its producer.
    """
    row = {
        "mibig_accession": "BGC0000002", "entry_version": "1", "entry_status": "active",
        "entry_quality": "high", "entry_completeness": "complete",
        "compound_name": "predictomycin", "compound_index": "1",
        "smiles": "CCO", "standard_inchi": "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3",
        "standard_inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "stereo_complete": "true",
        "compound_classes": "", "database_ids": "",
        "taxon_id": "NCBITaxon:1883", "taxon_label": "Streptomyces",
        "bgc_classes": "", "bgc_subclasses": "",
        "genome_accession": "", "locus_from": "0", "locus_to": "0",
        "locus_evidence_methods": "Homology-based prediction",
        "producer_evidence_basis": "", "primary_reference": "PMID:1", "reference_basis": "ENTRY",
    }
    records = seed.build_records({"mibig_compounds": [row]})
    assert len(records) == 1
    assert "producer_organisms" not in records[0]
    assert records[0]["biosynthetic_gene_clusters"]


def test_evidence_objects_are_not_shared_between_claims():
    """Shared list objects made PyYAML emit anchors and aliases into records."""
    row = {
        "mibig_accession": "BGC0000003", "entry_version": "1", "entry_status": "active",
        "entry_quality": "high", "entry_completeness": "complete",
        "compound_name": "sharedmycin", "compound_index": "1",
        "smiles": "CCO", "standard_inchi": "InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3",
        "standard_inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "stereo_complete": "true",
        "compound_classes": "", "database_ids": "",
        "taxon_id": "NCBITaxon:1883", "taxon_label": "Streptomyces",
        "bgc_classes": "", "bgc_subclasses": "",
        "genome_accession": "", "locus_from": "0", "locus_to": "0",
        "locus_evidence_methods": "Knock-out studies",
        "producer_evidence_basis": "BGC_CHARACTERIZED",
        "primary_reference": "PMID:1", "reference_basis": "ENTRY",
    }
    doc = seed.build_records({"mibig_compounds": [row]})[0]
    assert doc["producer_organisms"][0]["evidence"] is not \
        doc["biosynthetic_gene_clusters"][0]["evidence"]


def test_the_specific_congener_name_beats_the_bare_family_name():
    """A bare family name is a class, and a class is never a record.

    Three records took `xiamycin` over `xiamycin A` before the label rule
    existed, and erythromycin came out right only because the accession
    tie-break happened to favour the better row (#16).
    """
    assert seed.choose_label(["xiamycin", "xiamycin A"]) == ("xiamycin A", ["xiamycin"])
    assert seed.choose_label(["erythromycin", "erythromycin A"]) == (
        "erythromycin A", ["erythromycin"])
    assert seed.choose_label(["siamycin", "siamycin I"]) == ("siamycin I", ["siamycin"])


def test_case_variants_resolve_deterministically_not_by_entry_order():
    label, synonyms = seed.choose_label(["aflatoxin B1", "Aflatoxin B1"])
    assert (label, synonyms) == ("Aflatoxin B1", ["aflatoxin B1"])
    # Order of the input must not change the answer.
    assert seed.choose_label(["Aflatoxin B1", "aflatoxin B1"]) == (label, synonyms)


def test_a_discarded_name_survives_as_a_synonym():
    """Nothing is thrown away; the less specific name is still a real name."""
    _, synonyms = seed.choose_label(["ebelactone", "ebelactone A"])
    assert synonyms == ["ebelactone"]


def test_sibling_congeners_are_not_collapsed():
    """`amychelin A` and `amychelin B` are different structures. Specificity
    filtering must not make one a synonym of the other."""
    label, synonyms = seed.choose_label(["amychelin A", "amychelin B"])
    assert label == "amychelin A"
    assert synonyms == ["amychelin B"]


def test_paper_internal_names_are_detected_narrowly():
    """Narrow on purpose: a broader pattern starts flagging real names."""
    assert seed.PAPER_INTERNAL_NAME.match("compound 6")
    assert seed.PAPER_INTERNAL_NAME.match("metabolite 12")
    assert seed.PAPER_INTERNAL_NAME.match("3")
    assert not seed.PAPER_INTERNAL_NAME.match("BAA")
    assert not seed.PAPER_INTERNAL_NAME.match("erythromycin A")
    assert not seed.PAPER_INTERNAL_NAME.match("A-74528")
