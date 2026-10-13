"""Gentamicin fixes retain chemistry, source tiers and unresolved product scope."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_gentamicin", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


def test_pinned_decisions_affect_only_the_reviewed_fields():
    sources = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in ("BGC0000696", "BGC0001603")]
    keys = {r["standard_inchi_key"] for r in sources}
    inputs = {"mibig_compounds": sources,
              "pubchem_bioassay": [r for r in seed.read_tsv(ROOT / "data/raw/pubchem_bioassay.tsv")
                                   if r["standard_inchi_key"] in keys]}
    before = seed.build_records(inputs)
    for name in ("mibig_xref_exclusions", "mibig_producer_strains", "pubchem_bioassay_exclusions"):
        inputs[name] = [r for r in seed.read_tsv(ROOT / "curation" / (name + ".tsv"))
                        if r.get("source_id", "").split(":")[0] in ("BGC0000696", "BGC0001603")
                        or r.get("standard_inchi_key") in keys]
    assert len(inputs["mibig_producer_strains"]) == 2
    for decision in inputs["mibig_producer_strains"]:
        row, = [r for r in sources if r["mibig_accession"] == decision["source_id"].split(":")[0]]
        assert row_digest(row) == decision["expected_source_row_sha256"]
    after = seed.build_records(inputs)
    for old, new in zip(before, after, strict=True):
        producer, = new["producer_organisms"]
        bgc = producer["biosynthetic_gene_cluster"]
        assert producer.pop("strain") == ("DSM 43036" if bgc.endswith("0696") else "ATCC 15835")
        assert producer["evidence"].pop()["evidence_type"] == "CURATOR_INFERENCE"
        if bgc.endswith("0696"):
            assert new["xrefs"] == ["npatlas:NPA09026"]
            new["xrefs"].append("pubchem:72396")
            assert "bioactivities" not in new
            new["bioactivities"] = old["bioactivities"]
            assert {d["discussion_id"] for d in new.pop("discussions")} == {
                "source-xref-exclusion-BGC0000696-1-pubchem-72396", "source-bioassay-exclusion-72396-1195"}
        assert old == new


def test_current_owners_preserve_identity_and_open_questions():
    for slug, key, strain in (
        ("gentamicin", "BDTQHFBWYNCGHN-CUYCKOLISA-N", "DSM 43036"),
        ("gentamicin-2", "HFLKNINDVFJPQT-UHFFFAOYSA-N", "ATCC 15835"),
    ):
        doc = yaml.safe_load((ROOT / f"data/natural_products/carbohydrates/{slug}.yaml").read_text())
        assert doc["chemical_structure"]["standard_inchi_key"] == key
        assert doc["curation_status"] == "SEEDED"
        assert doc["producer_organisms"][0]["strain"] == strain
        assert doc["producer_organisms"][0]["evidence_basis"] == "SOURCE_ASSERTION"
        assert doc["biosynthetic_gene_clusters"][0]["link_evidence_basis"] == "CLUSTER_UNSTATED"
        assert "bioactivities" not in doc
        assert doc.get("xrefs", []) == (["npatlas:NPA09026"] if slug == "gentamicin" else [])
        discussion, = [d for d in doc["discussions"]
                       if d["discussion_id"] == "curator-gentamicin-exact-product-assignment"]
        assert discussion["status"] == "OPEN" and len(discussion["evidence"]) == 4
        same = {"chemical_structure": deepcopy(doc["chemical_structure"])}
        seed.carry_curator_owned_fields(same, doc)
        assert same["discussions"] == [discussion]
        different = {"chemical_structure": {"standard_inchi_key": "OTHER"}}
        seed.carry_curator_owned_fields(different, doc)
        assert "discussions" not in different
