"""Product links preserve chemical identity, source taxon scope and seeder ownership."""

from __future__ import annotations

import copy
import os
import subprocess
from pathlib import Path

import pytest
import yaml

from naturalproductmech.validation.write_validated import validate_natural_product
from scripts import extract_pathwaymech as extract
from tests.test_seed_skeleton import MIBIG_ROW, seed

PIN = "a" * 40


def test_cluster_requires_exact_product_and_source_taxon():
    recipe = {"identifier": "MIBiG:BGC0000001", "join": "SAME_MIBIG_PRODUCT"}
    doc = {"id": recipe["identifier"], "label": "test cluster",
           "taxa": [{"id": "NCBITaxon:2"}],
           "gene_clusters": [{"id": recipe["identifier"], "products": ["product A"]}]}
    rows = [{"mibig_accession": "BGC0000001", "compound_name": name,
             "entry_status": "active", "taxon_id": taxon, "standard_inchi_key": key}
            for name, taxon, key in [("product A", "NCBITaxon:2", "exact"),
                                     ("product B", "NCBITaxon:2", "other-product"),
                                     ("product A", "NCBITaxon:3", "other-taxon")]]
    matches = extract.product_rows(recipe, doc, rows, [], PIN)
    assert [r["standard_inchi_key"] for r in matches] == ["exact"]
    assert "NCBITaxon:2" in matches[0]["basis"]


def test_terminal_product_requires_structure_and_does_not_join_an_intermediate():
    recipe = {"identifier": "MetaCyc:P", "join": "SAME_TERMINAL_PRODUCT_INCHIKEY",
              "product": "CHEBI:1"}
    doc = {"id": "MetaCyc:P", "label": "pathway", "taxa": [{"id": "NCBITaxon:1"}],
           "mechanistic_edges": [{"subject": "RHEA:1", "predicate": "produces",
                                  "object": "CHEBI:1"}]}
    chebi = [{"chebi_id": "CHEBI:1", "standard_inchi_key": "product-key"}]
    row = extract.product_rows(recipe, doc, [], chebi, PIN)[0]
    assert row["standard_inchi_key"] == "product-key"
    assert "Product identity only" in row["basis"]
    assert "NCBITaxon:1" in row["basis"]
    with pytest.raises(ValueError, match="pinned ChEBI structure"):
        extract.product_rows(recipe, doc, [], [], PIN)
    doc["mechanistic_edges"].append({"subject": "CHEBI:1", "predicate": "consumes",
                                     "object": "RHEA:2"})
    with pytest.raises(ValueError, match="not a terminal product"):
        extract.product_rows(recipe, doc, [], chebi, PIN)


def test_pin_reads_committed_pathway_not_uncommitted_worktree(tmp_path, monkeypatch):
    for key in list(os.environ):
        if key.startswith("GIT_"):
            monkeypatch.delenv(key)
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", os.devnull)
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")

    def git(*args):
        return subprocess.check_output(["git", "-C", str(tmp_path), *args], text=True).strip()

    git("init", "-q")
    path = tmp_path / "data/pathways/p.yaml"
    path.parent.mkdir(parents=True)
    path.write_text("id: MetaCyc:P\nlabel: pinned\n")
    git("add", ".")
    git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
        "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
    commit = git("rev-parse", "HEAD")
    path.write_text("id: MetaCyc:P\nlabel: uncommitted\n")
    assert extract.read_pathway(tmp_path, commit, "data/pathways/p.yaml")["label"] == "pinned"
    with pytest.raises(ValueError, match="full commit"):
        extract.read_pathway(tmp_path, "HEAD", "data/pathways/p.yaml")


def test_seeder_adds_product_link_without_promoting_producer_or_activity():
    inventories = {"mibig_compounds": [MIBIG_ROW]}
    baseline = seed.build_records(copy.deepcopy(inventories))[0]
    inventories["pathwaymech_products"] = [{
        "standard_inchi_key": MIBIG_ROW["standard_inchi_key"],
        "identifier": "MetaCyc:P", "basis": "Product identity only", "corpus_commit": PIN,
    }]
    actual = seed.build_records(inventories)[0]
    assert actual.pop("related_records") == [{
        "corpus": "PathwayMech", "identifier": "MetaCyc:P", "relation": "BIOSYNTHESIZED_BY",
        "basis": "Product identity only", "source_version": PIN,
    }]
    assert actual == baseline


def test_inventory_has_only_four_reviewed_products_at_the_configured_pin():
    root = Path(__file__).resolve().parents[1]
    rows = extract.read_tsv(root / "data/raw/pathwaymech_products.tsv")
    pin = yaml.safe_load((root / "conf/sibling_pins.yaml").read_text())["pathwaymech"]["commit"]
    assert len(rows) == 4
    assert {row["corpus_commit"] for row in rows} == {pin}
    assert {row["identifier"] for row in rows} == {"MIBiG:BGC0002072", "MetaCyc:P101-PWY"}


def test_domain_link_inherits_governed_shape_and_keeps_closed_relation_enum(schema):
    link = schema["classes"]["NaturalProductCrossCorpusLink"]
    assert link["is_a"] == "CrossCorpusLink"
    assert link["slot_usage"]["relation"]["range"] == "CrossCorpusRelationEnum"


def test_governed_link_still_requires_basis_and_rejects_unknown_relations(minimal_record):
    link = {"corpus": "PathwayMech", "identifier": "MetaCyc:P101-PWY",
            "relation": "BIOSYNTHESIZED_BY", "basis": "Product identity only",
            "source_version": PIN}
    minimal_record["related_records"] = [link]
    assert validate_natural_product(minimal_record) == []
    link["relation"] = "ANYTHING"
    assert validate_natural_product(minimal_record)
    link["relation"] = "SAME_STRUCTURE"
    del link["basis"]
    assert validate_natural_product(minimal_record)
