"""Fogacin's mutant experiment must not grade an intact deposited locus."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = spec_from_file_location("fogacin_scope_seed", ROOT / "scripts/seed_from_sources.py")
SEED = module_from_spec(SPEC)
SPEC.loader.exec_module(SEED)
IDENTIFIER = "naturalproductmech:mibig-a4fac30c3f"


@pytest.fixture
def inputs():
    sources = [r for r in SEED.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in {"BGC0000248", "BGC0002021"}]
    decision, = [r for r in SEED.read_tsv(SEED.MIBIG_LOCUS_EVIDENCE_OVERRIDES)
                 if r["minted_identifier"] == IDENTIFIER]
    return {"mibig_compounds": sources, "mibig_locus_evidence_overrides": [decision]}


def test_only_exact_fogacin_grade_changes_with_context_preserved(inputs):
    original = deepcopy(inputs)
    before = {d["identifier"]: d for d in SEED.build_records(
        {"mibig_compounds": inputs["mibig_compounds"]})}
    after = {d["identifier"]: d for d in SEED.build_records(inputs)}
    assert set(before) == set(after)
    assert len(after) >= 3
    for identifier, doc in after.items():
        if identifier != IDENTIFIER:
            assert doc == before[identifier]
    doc = after[IDENTIFIER]
    assert doc["chemical_structure"] == before[IDENTIFIER]["chemical_structure"]
    assert doc["biosynthesis_origin"] == before[IDENTIFIER]["biosynthesis_origin"] == "NATURAL_PRODUCT"
    producer, = doc["producer_organisms"]
    cluster, = doc["biosynthetic_gene_clusters"]
    assert producer["evidence_basis"] == "SOURCE_ASSERTION"
    assert cluster["link_evidence_basis"] == "CLUSTER_UNSTATED"
    assert "locus_evidence_methods" not in cluster
    assert cluster["genome_accession"] == "genbank:JAKQYH010000014.1"
    assert (cluster["locus_from"], cluster["locus_to"]) == (94867, 120787)
    assert producer["taxon_id"] == cluster["organism_taxon_id"] == "NCBITaxon:29301"
    for field in ("producer_organisms", "biosynthetic_gene_clusters"):
        evidence = doc[field][0]["evidence"]
        assert evidence[0] == before[IDENTIFIER][field][0]["evidence"][0]
        assert evidence[0]["reference"] == "PMID:10206788"
        qualification, = evidence[1:]
        assert qualification["reference"] == "PMID:37989784"
        assert qualification["evidence_type"] == "CURATOR_INFERENCE"
        assert all(term in qualification["notes"] for term in (
            "ncnN deletion", "S. albus", "intact deposited", "Heterologous expression"))
    assert inputs == original
    assert producer["evidence"] is not cluster["evidence"]


@pytest.mark.parametrize("field", SEED.MIBIG_WITHDRAWAL_CONTEXT)
def test_fogacin_withdrawal_rejects_each_pinned_context_drift(inputs, field):
    source, = [r for r in inputs["mibig_compounds"]
               if r["mibig_accession"] == "BGC0000248" and r["compound_index"] == "2"]
    source[field] += " changed"
    with pytest.raises(ValueError, match="source context changed"):
        SEED.build_records(inputs)
