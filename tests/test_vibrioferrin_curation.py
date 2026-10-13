"""Vibrioferrin remediation must preserve identity boundaries and source scope."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_vibrioferrin_test", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


def test_exact_strain_rows_and_xref_exclusion_change_only_reviewed_claims():
    sources = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in {"BGC0000946", "BGC0000947"}]
    strains = [r for r in seed.read_tsv(seed.MIBIG_PRODUCER_STRAINS)
               if r["source_id"] in {"BGC0000946:1", "BGC0000947:1"}]
    xrefs = [r for r in seed.read_tsv(seed.MIBIG_XREF_EXCLUSIONS) if r["source_id"] == "BGC0000946:1"]
    assert len(sources) == 2 and len(strains) == 2 and len(xrefs) == 1
    before = seed.build_records({"mibig_compounds": sources})
    after = seed.build_records({"mibig_compounds": sources, "mibig_producer_strains": strains,
                                "mibig_xref_exclusions": xrefs})
    for old, new in zip(before, after, strict=True):
        producer, = new["producer_organisms"]
        is_wp1 = producer["biosynthetic_gene_cluster"] == "mibig:BGC0000946"
        assert producer.pop("strain") == ("WP1" if is_wp1 else "MVPO1")
        evidence = producer["evidence"].pop()
        assert evidence["evidence_type"] == "CURATOR_INFERENCE"
        assert ("AQ 3354" if is_wp1 else "MVP01 (zero)") in evidence["notes"]
        if is_wp1:
            assert "xrefs" not in new
            new["xrefs"] = old["xrefs"]
            discussion, = new.pop("discussions")
            assert discussion["status"] == "RESOLVED" and "#929" in discussion["resolution_note"]
        else:
            assert new["xrefs"] == ["pubchem:197680"]
        assert old == new


def test_open_qualifications_and_references_survive_only_same_key_reseeding():
    for slug, key, did in [
        ("vibrioferrin-2", "FPHRKFJYHKRDFJ-LWYCVJHGSA-N", "constitution"),
        ("vibrioferrin", "IGQXNKDXMPSELX-BIAKFKOBSA-N", "indirect-origin"),
    ]:
        path = ROOT / "data/natural_products/amino_acids_and_peptides" / (slug + ".yaml")
        doc = yaml.safe_load(path.read_text())
        assert doc["chemical_structure"]["standard_inchi_key"] == key
        assert doc["chemical_structure"]["stereo_complete"] is False
        assert doc["curation_status"] == "SEEDED"
        assert all(p["evidence_basis"] == "SOURCE_ASSERTION" for p in doc["producer_organisms"])
        assert all(c["link_evidence_basis"] == "CLUSTER_UNSTATED" for c in doc["biosynthetic_gene_clusters"])
        discussion, = [d for d in doc["discussions"]
                       if d["discussion_id"] == "curator-vibrioferrin-" + did]
        assert discussion["status"] == "OPEN" and len(discussion["evidence"]) >= 3
        same = {"chemical_structure": deepcopy(doc["chemical_structure"])}
        seed.carry_curator_owned_fields(same, doc)
        assert same["discussions"] == [discussion]
        different = {"chemical_structure": {"standard_inchi_key": "OTHER"}}
        seed.carry_curator_owned_fields(different, doc)
        assert "discussions" not in different
        if slug == "vibrioferrin":
            assert doc["xrefs"] == ["npatlas:NPA024673"]
            assert doc["producer_organisms"][0]["strain"] == "WP1"
            assert "strain" not in doc["producer_organisms"][1]
            for claim in (doc["producer_organisms"][1], doc["biosynthetic_gene_clusters"][1]):
                assert claim["evidence"][0]["reference"] == "PMID:26452553"
                assert claim["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
            occurrence, = [o for o in doc["occurrences"] if o["taxon_id"] == "NCBITaxon:663"]
            assert occurrence["evidence"][0]["reference"] == "PMID:22146715"
        else:
            assert doc["xrefs"] == ["pubchem:197680"]
            assert doc["producer_organisms"][0]["strain"] == "MVPO1"
            assert len(doc["occurrences"]) == 7
