"""Strain repair and identity warnings must not silently migrate chemistry."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_myxochromide_test", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


def test_exact_strain_rows_change_only_producer_qualifiers():
    sources = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] in {"BGC0001425", "BGC0001426", "BGC0001427", "BGC0001428"}]
    decisions = [r for r in seed.read_tsv(ROOT / "curation/mibig_producer_strains.tsv")
                 if r["source_id"] in {"BGC0001426:1", "BGC0001427:1", "BGC0001428:1"}]
    expected = {"BGC0001426": "DK897", "BGC0001427": "A47", "BGC0001428": "Mx48"}
    assert len(sources) == 4 and len(decisions) == 3
    for decision in decisions:
        source, = [r for r in sources if r["mibig_accession"] + ":1" == decision["source_id"]]
        assert row_digest(source) == decision["expected_source_row_sha256"]
    before, = seed.build_records({"mibig_compounds": sources})
    after, = seed.build_records({"mibig_compounds": sources, "mibig_producer_strains": decisions})
    for producer in after["producer_organisms"]:
        accession = producer["biosynthetic_gene_cluster"].split(":")[1]
        if accession not in expected:
            assert "strain" not in producer
            continue
        assert producer.pop("strain") == expected[accession]
        evidence = producer["evidence"].pop()
        assert evidence["evidence_type"] == "CURATOR_INFERENCE"
        assert "#924" in evidence["notes"]
    assert before == after


def test_open_qualifications_keep_distinct_owners_and_same_key_carry_forward():
    for relative, key, did, grades in [
        ("amino_acids_and_peptides/myxochromide-a", "NDLATPRQLJTXJX-OBQOMHFNSA-N",
         "curator-myxochromide-a-core-identity", ["BGC_CHARACTERIZED"] + ["SOURCE_ASSERTION"] * 3),
        ("unclassified/myxochromide-a-2", "TXEVVKPQBOIUHV-DHXUWNHESA-N",
         "curator-myxochromide-a-hw1-proline", ["SOURCE_ASSERTION"]),
    ]:
        doc = yaml.safe_load((ROOT / "data/natural_products" / (relative + ".yaml")).read_text())
        assert doc["chemical_structure"]["standard_inchi_key"] == key
        assert doc["curation_status"] == "SEEDED"
        assert [p["evidence_basis"] for p in doc["producer_organisms"]] == grades
        discussion, = [d for d in doc["discussions"] if d["discussion_id"] == did]
        assert discussion["status"] == "OPEN" and "HTTP403" in discussion["rationale"]
        assert len(discussion["evidence"]) >= 4
        same = {"chemical_structure": deepcopy(doc["chemical_structure"])}
        seed.carry_curator_owned_fields(same, doc)
        assert same["discussions"] == [discussion]
        different = {"chemical_structure": {"standard_inchi_key": "OTHER"}}
        seed.carry_curator_owned_fields(different, doc)
        assert "discussions" not in different
        if relative.endswith("-2"):
            assert doc["chemical_structure"]["stereo_complete"] is False
            assert doc["np_pathway"] == "UNCLASSIFIED"
            assert doc["xrefs"] == ["npatlas:NPA017265"]
        else:
            assert [p.get("strain") for p in doc["producer_organisms"]] == [None, "DK897", "A47", "Mx48"]
