"""Keep the proposed compound 3 identity and source isolate explicitly scoped."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / "data/natural_products/amino_acids_and_peptides/compound-3.yaml"
KEY = "RHGNLLJMHSJJRX-UHFFFAOYSA-N"
DISCUSSION = "curator-compound3-proposed-structure"
spec = spec_from_file_location("seed_compound3_test", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


def test_compound3_strain_decision_is_exact_and_preserves_imported_claims():
    rows = seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
    source, = [r for r in rows if r["mibig_accession"] == "BGC0002321"
               and r["compound_index"] == "4"]
    decision, = [r for r in seed.read_tsv(ROOT / "curation/mibig_producer_strains.tsv")
                 if r["source_id"] == "BGC0002321:4"]
    assert decision["expected_source_row_sha256"] == row_digest(source)
    assert source["standard_inchi_key"] == KEY
    assert source["genome_accession"] == "CP034458.1"
    before, = seed.build_records({"mibig_compounds": [source]})
    after, = seed.build_records({"mibig_compounds": [source],
                                "mibig_producer_strains": [decision]})
    producer, = after["producer_organisms"]
    assert producer.pop("strain") == "APC1.2 (CCOS978)"
    evidence = producer["evidence"].pop()
    assert evidence["reference"] == "PMID:31081214"
    assert evidence["evidence_type"] == "CURATOR_INFERENCE"
    assert before == after


def test_compound3_qualification_is_cited_and_survives_same_key_reseed():
    doc = yaml.safe_load(OWNER.read_text())
    assert doc["identifier"] == "naturalproductmech:mibig-0dd7b68dcd"
    assert doc["chemical_structure"]["standard_inchi_key"] == KEY
    assert doc["chemical_structure"]["stereo_complete"] is False
    assert doc["curation_status"] == "SEEDED"
    assert doc["producer_organisms"][0]["evidence_basis"] == "BGC_CORRELATED"
    assert doc["producer_organisms"][0]["strain"] == "APC1.2 (CCOS978)"
    assert doc["biosynthetic_gene_clusters"][0]["link_evidence_basis"] == "CLUSTER_CORRELATED"
    discussion, = [d for d in doc["discussions"] if d["discussion_id"] == DISCUSSION]
    assert discussion["status"] == "OPEN"
    assert "proposed, not definitively elucidated" in discussion["prompt"]
    assert "constitutional uncertainty" in discussion["rationale"]
    assert discussion["evidence"][0]["reference"] == "PMID:31081214"
    assert discussion["evidence"][0]["evidence_source"] == "full_text"
    assert not doc.get("bioactivities")
    payload = {"chemical_structure": deepcopy(doc["chemical_structure"])}
    seed.carry_curator_owned_fields(payload, doc)
    assert payload["discussions"] == [discussion]
    different = {"chemical_structure": {"standard_inchi_key": "DIFFERENT"}}
    seed.carry_curator_owned_fields(different, doc)
    assert "discussions" not in different
