"""Regression for exact-compound, source-pinned MIBiG evidence withdrawal."""

import copy
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("seed_withdrawal_tests", ROOT / "scripts/seed_from_sources.py")
seed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seed)

IDENTIFIER = "naturalproductmech:mibig-d02aa1e8bc"
REFERENCE = "https://mibig.secondarymetabolites.org/repository/BGC0000892.4/index.html"
METHODS = "Knock-out studies|Gene expression correlated with compound production"


@pytest.fixture
def source():
    row, = [row for row in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
            if row["mibig_accession"] == "BGC0000892"]
    return row


@pytest.fixture
def withdrawal():
    row, = [row for row in seed.read_tsv(seed.MIBIG_LOCUS_EVIDENCE_OVERRIDES)
            if row["minted_identifier"] == IDENTIFIER]
    return row


def build(rows, withdrawal):
    return seed.build_records({
        "mibig_compounds": rows,
        "mibig_locus_evidence_overrides": [withdrawal],
    })


def test_pinned_caryoynencin_source_and_qualification(source, withdrawal):
    assert withdrawal["action"] == "WITHDRAW"
    assert withdrawal["reference"] == REFERENCE
    assert source["entry_version"] == "4"
    assert source["compound_index"] == "1"
    assert source["taxon_id"] == "NCBITaxon:999541"
    assert source["genome_accession"] == "CP002599.1"
    assert (source["locus_from"], source["locus_to"]) == ("2260844", "2274030")
    assert source["standard_inchi_key"] == "GOOGOKNSXZDSND-QDCWQMMGSA-N"
    assert source["locus_evidence_methods"] == METHODS
    assert source["producer_evidence_basis"] == "BGC_CHARACTERIZED"
    assert source["cluster_link_evidence_basis"] == "CLUSTER_DEMONSTRATED"
    assert all(value in withdrawal["rationale"] for value in (
        "DSM50341", "KJ815051-KJ815060", "BSR3", "CP002599.1"))
    before = copy.deepcopy(source)
    doc, = build([source], withdrawal)
    assert source == before
    assert doc["identifier"] == IDENTIFIER
    assert doc["chemical_structure"]["stereo_complete"] is False
    producer, = doc["producer_organisms"]
    cluster, = doc["biosynthetic_gene_clusters"]
    assert producer["taxon_id"] == cluster["organism_taxon_id"] == "NCBITaxon:999541"
    assert producer["taxon_label"] == cluster["organism_label"] == "Burkholderia gladioli BSR3"
    assert cluster["genome_accession"] == "genbank:CP002599.1"
    assert (cluster["locus_from"], cluster["locus_to"]) == (2260844, 2274030)
    assert producer["evidence_basis"] == "SOURCE_ASSERTION"
    assert cluster["link_evidence_basis"] == "CLUSTER_UNSTATED"
    assert "locus_evidence_methods" not in cluster
    assert "none stated" not in producer["notes"] and METHODS in producer["notes"]
    for claim in (producer, cluster):
        original, qualification = claim["evidence"]
        assert original == seed.mibig_evidence(source)[0]
        assert qualification["reference"] == REFERENCE
        assert qualification["evidence_type"] == "CURATOR_INFERENCE"
        assert METHODS in qualification["notes"]
        assert withdrawal["rationale"] in qualification["notes"]
    assert producer["evidence"] is not cluster["evidence"]
    producer["evidence"][1]["notes"] = "mutated"
    assert cluster["evidence"][1]["notes"] != "mutated"


def test_withdrawal_does_not_change_same_cluster_sibling(source, withdrawal):
    sibling = {**source, "compound_index": "2", "compound_name": "other compound",
               "standard_inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"}
    untouched = seed.build_records({"mibig_compounds": [sibling]})[0]
    records = build([source, sibling], withdrawal)
    assert next(doc for doc in records if doc["identifier"] == untouched["identifier"]) == untouched


def test_withdrawal_applies_before_lead_selection(source, withdrawal):
    alternative = {**source, "mibig_accession": "BGC9999999", "compound_name": "other source"}
    doc, = build([source, alternative], withdrawal)
    assert doc["identifier"] == seed.mint_identifier("MIBIG", "BGC9999999:1")
    assert doc["chemical_structure"]["structure_source_id"] == "mibig:BGC9999999"


@pytest.mark.parametrize("field", seed.MIBIG_WITHDRAWAL_CONTEXT)
def test_withdrawal_fails_on_raw_context_drift(source, withdrawal, field):
    source[field] += " changed"
    with pytest.raises(ValueError, match="source context changed: " + field):
        build([source], withdrawal)


def test_withdrawal_checks_source_accession_even_if_key_matches(source, withdrawal):
    withdrawal["source_id"] = "BGC9999999"
    with pytest.raises(ValueError, match="source context changed: mibig_accession"):
        build([source], withdrawal)


@pytest.mark.parametrize("count", [0, 2])
def test_withdrawal_requires_one_target(source, withdrawal, count):
    with pytest.raises(ValueError, match="exactly one matching source row"):
        build([copy.deepcopy(source) for _ in range(count)], withdrawal)


@pytest.mark.parametrize("field", [
    "reference", "rationale", "curator", "date", "source", "source_id",
    *["expected_" + field for field in seed.MIBIG_WITHDRAWAL_CONTEXT],
])
@pytest.mark.parametrize("blank", ["", "  ", None])
def test_withdrawal_requires_citation_rationale_and_context(withdrawal, field, blank):
    withdrawal[field] = blank
    with pytest.raises(ValueError):
        seed.load_mibig_locus_evidence_overrides([withdrawal])


@pytest.mark.parametrize("action", ["", " ", "DROP", None])
def test_explicit_invalid_action_never_means_withdrawal(withdrawal, action):
    withdrawal["action"] = action
    with pytest.raises(ValueError, match="invalid MIBiG evidence action"):
        seed.load_mibig_locus_evidence_overrides([withdrawal])


@pytest.mark.parametrize("methods", ["Knock-out studies", " ", "|"])
def test_withdrawal_rejects_nonempty_replacement_methods(withdrawal, methods):
    withdrawal["locus_evidence_methods"] = methods
    with pytest.raises(ValueError):
        seed.load_mibig_locus_evidence_overrides([withdrawal])


@pytest.mark.parametrize("reference", [
    "uncited", "PMID:wrong", "DOI:wrong", "https://", "https://example.org/a b",
])
def test_withdrawal_rejects_unstable_citation(withdrawal, reference):
    withdrawal["reference"] = reference
    with pytest.raises(ValueError, match="stable DOI, PMID or HTTPS"):
        seed.load_mibig_locus_evidence_overrides([withdrawal])


@pytest.mark.parametrize("reference", ["DOI:10.1002/anie.201403344", "PMID:24898429", REFERENCE])
def test_withdrawal_accepts_supported_citation_forms(withdrawal, reference):
    withdrawal["reference"] = reference
    result = seed.load_mibig_locus_evidence_overrides([withdrawal])[IDENTIFIER]
    assert result["qualification_reference"] == reference


def test_withdrawal_rejects_unknown_expected_methods(withdrawal):
    withdrawal["expected_locus_evidence_methods"] = "Unrecognized method"
    with pytest.raises(ValueError, match="unknown expected source methods"):
        seed.load_mibig_locus_evidence_overrides([withdrawal])


def test_duplicate_override_is_rejected(withdrawal):
    with pytest.raises(ValueError, match="duplicate MIBiG locus evidence override"):
        seed.load_mibig_locus_evidence_overrides([withdrawal, withdrawal])


def test_all_eight_legacy_replacements_keep_their_previous_shape():
    rows = [row for row in seed.read_tsv(seed.MIBIG_LOCUS_EVIDENCE_OVERRIDES)
            if row["action"] == "REPLACE"]
    assert len(rows) == 8
    legacy = [{"minted_identifier": row["minted_identifier"],
               "locus_evidence_methods": row["locus_evidence_methods"]} for row in rows]
    actual = seed.load_mibig_locus_evidence_overrides(rows)
    assert actual == seed.load_mibig_locus_evidence_overrides(legacy)
    for override in actual.values():
        assert set(override) == {
            "locus_evidence_methods", "producer_evidence_basis", "cluster_link_evidence_basis"}


def test_missing_action_does_not_allow_empty_methods(withdrawal):
    del withdrawal["action"]
    with pytest.raises(ValueError, match="no methods"):
        seed.load_mibig_locus_evidence_overrides([withdrawal])
