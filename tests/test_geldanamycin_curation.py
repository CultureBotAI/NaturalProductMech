"""Geldanamycin corrections do not merge identities or move unsupported assays."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location("seed_geldanamycin", ROOT / "scripts/seed_from_sources.py")
seed = module_from_spec(spec)
spec.loader.exec_module(seed)
QS = "QSAMODLUYGNFJU-LEBIDKMGSA-N"
QTQ = "QTQAWLPCGQOSGP-KSRBKZBZSA-N"


def test_pinned_decisions_do_not_transfer_activity_or_change_source_claims():
    inputs = {"mibig_compounds": [r for r in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
                                 if r["mibig_accession"] in ("BGC0000066", "BGC0000067", "BGC0000068")]}
    for name in ("lotus_occurrences", "pubchem_bioassay"):
        inputs[name] = [r for r in seed.read_tsv(ROOT / f"data/raw/{name}.tsv")
                        if r["standard_inchi_key"] in (QS, QTQ)]
    baseline = seed.build_records(inputs)
    for name in ("mibig_xref_exclusions", "pubchem_bioassay_exclusions", "lotus_occurrence_exclusions"):
        inputs[name] = [r for r in seed.read_tsv(ROOT / f"curation/{name}.tsv")
                        if r.get("standard_inchi_key") in (QS, QTQ) or r.get("source_id") == "BGC0000066:1"]
    assert len(inputs["pubchem_bioassay_exclusions"]) == 14
    after = seed.build_records(inputs)
    for old, new in zip(baseline, after, strict=True):
        key = new["chemical_structure"]["standard_inchi_key"]
        if key == QS:
            assert old["xrefs"] == ["npatlas:NPA019914", "pubchem:5288382"]
            assert new["xrefs"] == ["npatlas:NPA019914"]
            assert len(old["bioactivities"]) == 14
            assert "bioactivities" not in new and "bioactivity_summary" not in new
            old["xrefs"].remove("pubchem:5288382")
            old.pop("bioactivities")
            old.pop("bioactivity_summary")
            assert len(new.pop("discussions")) == 15
        else:
            assert key == QTQ and "bioactivities" not in new
            old["occurrences"].pop(0)
            discussions = new.pop("discussions")
            assert len(discussions) == 2
            new["discussions"] = [d for d in discussions if d["discussion_id"] == "shared-structure"]
        assert new == old


def test_curated_graphs_and_unresolved_status_are_preserved():
    qs = yaml.safe_load((ROOT / "data/natural_products/polyketides/geldanamycin-2.yaml").read_text())
    qtq = yaml.safe_load((ROOT / "data/natural_products/polyketides/geldanamycin.yaml").read_text())
    for doc, key in ((qs, QS), (qtq, QTQ)):
        assert doc["chemical_structure"]["standard_inchi_key"] == key
        assert doc["curation_status"] == "SEEDED"
        assert all(p["evidence_basis"] == "SOURCE_ASSERTION" for p in doc["producer_organisms"])
        assert all(b["link_evidence_basis"] == "CLUSTER_UNSTATED" for b in doc["biosynthetic_gene_clusters"])
    assert "causal_graphs" not in qs
    assert "bioactivities" not in qs and "bioactivity_summary" not in qs
    assert qs["xrefs"] == ["npatlas:NPA019914"]
    discussion, = [d for d in qs["discussions"] if d["discussion_id"].startswith("curator-")]
    assert discussion["status"] == "OPEN" and "#968" in discussion["resolution_note"]
    assert qtq["occurrence_taxon_groups"] == ["ACTINOBACTERIAL"]
    assert len(qtq["occurrences"]) == 3
    graph, = qtq["causal_graphs"]
    assert graph["nodes"][1]["identifier"] == "UniProtKB:P07900"
    edge, = graph["edges"]
    assert edge["predicate"] == "binds"
    assert "positions 9-236" in edge["notes"] and "position 63" in edge["notes"]
    assert "engineered mutation" in edge["notes"]
    assert edge["evidence"][0]["evidence_type"] == "PRIMARY_EXPERIMENT"
    assert edge["evidence"][1]["evidence_type"] == "DATABASE_ASSERTION"
