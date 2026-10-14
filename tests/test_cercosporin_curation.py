"""Cercosporin qualifications do not silently settle identity or engineering."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("slug,key", [
    ("cercosporin", "DGAZLNHJYDOWLG-QWRGUYRKSA-N"),
    ("cercosporin-2", "MXLWQNCWIIZUQT-GHMZBOCLSA-N"),
])
def test_exact_cercosporin_identity_remains_qualified(slug, key):
    doc = yaml.safe_load((ROOT / "data/natural_products/polyketides" / f"{slug}.yaml").read_text())
    assert doc["chemical_structure"]["standard_inchi_key"] == key
    assert doc["curation_status"] == "SEEDED"
    assert doc["biosynthesis_origin"] == "NATURAL_PRODUCT"
    assert doc["producer_organisms"][0]["evidence_basis"] == "SOURCE_ASSERTION"
    assert doc["biosynthetic_gene_clusters"][0]["link_evidence_basis"] == "CLUSTER_UNSTATED"
    identity, = [d for d in doc["discussions"] if d["discussion_id"] == "curator-cercosporin-exact-identity"]
    assert identity["status"] == "OPEN"
    assert any(e["reference"].endswith("/issues/955") for e in identity["evidence"])
    if slug == "cercosporin-2":
        context, = [d for d in doc["discussions"]
                    if d["discussion_id"] == "curator-cercosporin-zeina-complementation"]
        assert context["status"] == "OPEN"
        assert {"PMID:28535078", "https://www.ncbi.nlm.nih.gov/nuccore/KY656140.1"} <= {
            e["reference"] for e in context["evidence"]
        }
        assert doc["occurrences"][0]["evidence"][0]["reference"] == "DOI:10.1094/MPMI-03-17-0054-R"
        for field in ("producer_organisms", "biosynthetic_gene_clusters"):
            assert doc[field][0]["evidence"][0]["reference"] == "PMID:28535078"
            assert "complemented" in doc[field][0]["evidence"][-1]["notes"]
