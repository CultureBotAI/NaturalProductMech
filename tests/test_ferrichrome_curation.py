"""Exact-form fixes must not migrate chemistry or erase unresolved identity."""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

from naturalproductmech.curate.structure_corrections import row_digest

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_ferrichrome_test", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)


def test_xref_exclusion_is_exact_and_does_not_change_other_claims():
    source, = [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if r["mibig_accession"] == "BGC0000900" and r["compound_index"] == "1"]
    decision, = [r for r in seed.read_tsv(ROOT / "curation/mibig_xref_exclusions.tsv")
                 if r["source_id"] == "BGC0000900:1"]
    assert decision["expected_source_row_sha256"] == row_digest(source)
    assert decision["xref"] == "pubchem:644246"
    before, = seed.build_records({"mibig_compounds": [source]})
    after, = seed.build_records({"mibig_compounds": [source], "mibig_xref_exclusions": [decision]})
    assert before["xrefs"] == ["pubchem:90658043", "pubchem:644246"]
    assert after["xrefs"] == ["pubchem:90658043"]
    before.pop("xrefs")
    after.pop("xrefs")
    discussion, = after.pop("discussions")
    assert discussion["discussion_id"].startswith("source-xref-exclusion-")
    assert "644246" in discussion["prompt"]
    assert before == after


def test_qualifications_preserve_exact_owners_and_carry_only_on_same_key():
    for slug, key, discussion_id, xrefs in [
        ("ferrichrome-2", "ZZDYFKJSJLUQON-UFYCRDLUSA-N",
         "curator-ferrichrome-constitution-conflict", ["pubchem:90658043"]),
        ("ferrichrome", "GGUNGDGGXMHBMJ-HCMAANCNSA-N",
         "curator-ferrichrome-55fe-attribution", ["pubchem:644246"]),
    ]:
        doc = yaml.safe_load((ROOT / f"data/natural_products/amino_acids_and_peptides/{slug}.yaml")
                             .read_text())
        assert doc["chemical_structure"]["standard_inchi_key"] == key
        assert doc["curation_status"] == "SEEDED"
        assert doc["producer_organisms"][0]["evidence_basis"] == "SOURCE_ASSERTION"
        assert doc["biosynthetic_gene_clusters"][0]["link_evidence_basis"] == "CLUSTER_UNSTATED"
        assert doc["xrefs"] == xrefs
        discussion, = [d for d in doc["discussions"] if d["discussion_id"] == discussion_id]
        assert discussion["status"] == "OPEN"
        assert len(discussion["evidence"]) >= 4
        assert all(e["reference"] for e in discussion["evidence"])
        payload = {"chemical_structure": deepcopy(doc["chemical_structure"])}
        seed.carry_curator_owned_fields(payload, doc)
        assert payload["discussions"] == [discussion]
        different = {"chemical_structure": {"standard_inchi_key": "DIFFERENT"}}
        seed.carry_curator_owned_fields(different, doc)
        assert "discussions" not in different
        if slug == "ferrichrome":
            assert "[55Fe+3]" in doc["chemical_structure"]["smiles"]
            assert doc["chemical_structure"]["stereo_complete"] is False
            assert "HTTP403" in discussion["rationale"]
        else:
            assert "constitutional conflict" in discussion["rationale"]
