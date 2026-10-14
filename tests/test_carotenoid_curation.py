"""Classification repair must not masquerade as exact-product adjudication."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("path,key,cid,discussion_id,producer_count", [
    ("polyketides/carotenoid", "MYQIMJTUIOIEOX-LVWNLLCFSA-N", 156935,
     "curator-carotenoid-cosmomycin-identity-conflict", 2),
    ("terpenoids/carotenoid-2", "MQXYWDPDLKUSFB-HOOXQTDMSA-N", 446841,
     "curator-carotenoid-generic-class-structure-collapse", 16),
])
def test_identity_conflicts_remain_open(path, key, cid, discussion_id, producer_count):
    doc = yaml.safe_load((ROOT / "data/natural_products" / (path + ".yaml")).read_text())
    assert doc["chemical_structure"]["standard_inchi_key"] == key
    assert f"pubchem:{cid}" in doc["xrefs"]
    assert doc["curation_status"] == "SEEDED"
    assert len(doc["producer_organisms"]) == producer_count
    assert all(p["evidence_basis"] == "SOURCE_ASSERTION" for p in doc["producer_organisms"])
    assert all(c["link_evidence_basis"] == "CLUSTER_UNSTATED"
               for c in doc["biosynthetic_gene_clusters"])
    discussion, = [d for d in doc["discussions"] if d["discussion_id"] == discussion_id]
    assert discussion["status"] == "OPEN"
    assert discussion["kind"] == "CONTROVERSY"
    assert any(e["reference"].endswith("/issues/952") for e in discussion["evidence"])
    assert any(e["reference"].startswith("PMID:") for e in discussion["evidence"])
