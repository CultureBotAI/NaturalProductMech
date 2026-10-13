"""Deposited capsule context must not certify or silently migrate chemistry."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_capsular_test", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)

EXPECTED = {
    "BGC0000728": ("Kauffmann E5051", "AB289645.1", "K5"),
    "BGC0000729": ("NTUH-K9534", "AB289646.1", "K5"),
    "BGC0000730": ("889/50", "AB289647.1", "K20"),
    "BGC0000731": ("NTUH-KP13", "AB289648.1", "K20"),
    "BGC0000733": ("NTUH-KP35", "AB289650.1", "K54"),
    "BGC0000740": ("090", "AF332893.1", "Ia"),
    "BGC0000741": ("M781", "AF332896.1", "III"),
    "BGC0000742": ("SS1214", "AF332901.1", "VI"),
    "BGC0000743": ("Prague 118754", "AF332902.1", "VI"),
    "BGC0000744": ("SG99/143", "AF363055.1", "III"),
    "BGC0000745": ("GB00/031", "AF363056.1", "III"),
    "BGC0000746": ("GB00/017", "AF363057.1", "Ia"),
    "BGC0000747": ("FP6453", "AF363058.1", "Ia"),
    "BGC0000748": ("SG99/276", "AF363059.1", "Ia"),
    "BGC0000751": ("8329", "AY496881.1", "12"),
    "BGC0000752": ("Femo", "AY534316.1", "6"),
    "BGC0000753": ("isolate 72-14676", "AY534317.1", "7"),
}


def test_pinned_qualifications_change_only_deposited_producer_context():
    sources = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in EXPECTED]
    decisions = [r for r in seed.read_tsv(seed.MIBIG_PRODUCER_STRAINS)
                 if r["source_id"].split(":")[0] in EXPECTED]
    assert len(sources) == len(decisions) == 17
    for row in decisions:
        accession = row["source_id"].split(":")[0]
        source, = [r for r in sources if r["mibig_accession"] == accession]
        strain, genome, serotype = EXPECTED[accession]
        assert row_digest(source) == row["expected_source_row_sha256"]
        assert row["strain"] == strain
        assert row["reference"] == "https://www.ncbi.nlm.nih.gov/nuccore/" + genome
        assert "serotype " + serotype + "." in row["rationale"]
    before = seed.build_records({"mibig_compounds": sources})
    after = seed.build_records({"mibig_compounds": sources, "mibig_producer_strains": decisions})
    assert len(before) == len(after) == 3
    for old, new in zip(before, after, strict=True):
        for p in new["producer_organisms"]:
            accession = p["biosynthetic_gene_cluster"].split(":")[1]
            assert p.pop("strain") == EXPECTED[accession][0]
            evidence = p["evidence"].pop()
            assert evidence["evidence_type"] == "CURATOR_INFERENCE"
            assert "#938" in evidence["notes"] and "identity" in evidence["notes"]
        assert old == new


def test_identity_qualifications_survive_only_same_structure_reseeding():
    for relative, key, cid, stereo, count in [
        ("carbohydrates/capsular-polysaccharide-2", "ODLPTSAMUCYJMF-UHFFFAOYSA-N", 3083199, False, 5),
        ("carbohydrates/capsular-polysaccharide-3", "NOVHANKYCIGDMV-KSYJWRBWSA-N", 3083207, True, 9),
        ("unclassified/capsular-polysaccharide", "FJTWZGAJWZJDEU-SRTYELMFSA-N", 195740, True, 3),
    ]:
        doc = yaml.safe_load((ROOT / "data/natural_products" / (relative + ".yaml")).read_text())
        assert doc["chemical_structure"]["standard_inchi_key"] == key
        assert doc["chemical_structure"]["stereo_complete"] is stereo
        assert doc["xrefs"] == [f"pubchem:{cid}"]
        assert doc["curation_status"] == "SEEDED"
        assert len(doc["producer_organisms"]) == count
        for p in doc["producer_organisms"]:
            assert p["strain"] == EXPECTED[p["biosynthetic_gene_cluster"].split(":")[1]][0]
            assert p["evidence_basis"] == "SOURCE_ASSERTION"
            assert p["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
        assert all(c["link_evidence_basis"] == "CLUSTER_UNSTATED" for c in doc["biosynthetic_gene_clusters"])
        discussion, = [d for d in doc["discussions"]
                       if d["discussion_id"] == "curator-capsule-exact-product-assignment"]
        assert discussion["status"] == "OPEN" and len(discussion["evidence"]) >= count + 3
        same = {"chemical_structure": deepcopy(doc["chemical_structure"])}
        seed.carry_curator_owned_fields(same, doc)
        assert same["discussions"] == [discussion]
        different = {"chemical_structure": {"standard_inchi_key": "OTHER"}}
        seed.carry_curator_owned_fields(different, doc)
        assert "discussions" not in different
        if cid == 195740:
            assert doc["np_pathway"] == "UNCLASSIFIED"
            assert {o["taxon_id"] for o in doc["occurrences"]} == {"NCBITaxon:715", "NCBITaxon:720"}
            assert "AP76" in discussion["rationale"] and "unknown" in discussion["rationale"]
