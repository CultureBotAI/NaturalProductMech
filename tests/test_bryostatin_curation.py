"""Bryostatin context fixes must leave the unresolved exact-product scope explicit."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("slug,key,cid,accession,region", [
    ("bryostatin", "MJQUEDHRCUIRLF-YFQOKXJGSA-N", 25235992, "DQ889941.1", "bryABCDX"),
    ("bryostatin-2", "NJMZVUZEDLKEGZ-XMADZBCLSA-N", 6438934, "DQ889942.1", "bryPQRS"),
])
def test_current_owners_preserve_identity_and_open_scope(slug, key, cid, accession, region):
    from importlib.util import module_from_spec, spec_from_file_location

    spec = spec_from_file_location("seed_bryostatin", ROOT / "scripts/seed_from_sources.py")
    seed = module_from_spec(spec)
    spec.loader.exec_module(seed)
    doc = yaml.safe_load((ROOT / f"data/natural_products/polyketides/{slug}.yaml").read_text())
    assert doc["chemical_structure"]["standard_inchi_key"] == key
    assert doc["chemical_structure"]["stereo_complete"] is False
    assert doc["xrefs"] == [f"pubchem:{cid}"]
    assert doc["curation_status"] == "SEEDED"
    producer, = doc["producer_organisms"]
    assert "strain" not in producer and "Deposited isolate: DEEP." in producer["notes"]
    assert producer["taxon_id"] == "NCBITaxon:62101"
    assert producer["evidence_basis"] == "SOURCE_ASSERTION"
    assert producer["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
    assert producer["evidence"][-1]["reference"].endswith("/" + accession)
    assert producer["evidence"][-1]["evidence_type"] == "CURATOR_INFERENCE"
    cluster, = doc["biosynthetic_gene_clusters"]
    assert cluster["genome_accession"] == "genbank:" + accession
    assert cluster["link_evidence_basis"] == "CLUSTER_UNSTATED"
    discussion, = doc["discussions"]
    assert discussion["discussion_id"] == "curator-bryostatin-exact-congener-locus-scope"
    assert discussion["status"] == "OPEN"
    assert key in discussion["rationale"] and region in discussion["rationale"]
    assert len(discussion["evidence"]) == 3
    same = {"chemical_structure": deepcopy(doc["chemical_structure"])}
    seed.carry_curator_owned_fields(same, doc)
    assert same["discussions"] == [discussion]
    different = {"chemical_structure": {"standard_inchi_key": "OTHER"}}
    seed.carry_curator_owned_fields(different, doc)
    assert "discussions" not in different
