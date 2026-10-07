"""Exact-source structure adjudication must not transfer old-key claims."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from naturalproductmech.curate.structure_corrections import (
    apply_structure_corrections,
    row_digest,
)
from naturalproductmech.validation.write_validated import validate_natural_product

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("seed_correction_tests", ROOT / "scripts/seed_from_sources.py")
seed = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seed)
OLD = "OGUMLESFFBGVOO-VJDLAWOBSA-N"
NEW = "GQKXCBCSVYJUMI-WACKOAQBSA-N"


@pytest.fixture
def inputs():
    source, = [row for row in seed.read_tsv(ROOT / "data/raw/mibig_compounds.tsv")
               if row["mibig_accession"] == "BGC0000024"]
    target, = [row for row in seed.read_tsv(ROOT / "data/raw/chebi_structures.tsv")
               if row["chebi_id"] == "CHEBI:80024"]
    correction, = seed.read_tsv(seed.MIBIG_STRUCTURE_CORRECTIONS)
    return [source], [correction], [target]


def test_correction_preserves_raw_rows_and_provenance(inputs):
    before = copy.deepcopy(inputs)
    source, = apply_structure_corrections(*inputs)
    assert inputs == before
    assert source["standard_inchi_key"] == NEW
    assert source["smiles"] == inputs[2][0]["smiles"]
    assert source["database_ids"] == ""
    assert source["structure_source_id"] == "CHEBI:80024"
    assert OLD in source["structure_correction_note"]
    assert "pubchem:6436188|chemspider:5029106" in source["structure_correction_note"]
    for field in ("taxon_id", "genome_accession", "locus_evidence_methods", "entry_version"):
        assert source[field] == inputs[0][0][field]
    assert row_digest(dict(reversed(list(inputs[0][0].items())))) == row_digest(inputs[0][0])


@pytest.mark.parametrize("table", [0, 2])
def test_all_source_and_target_fields_are_pinned(inputs, table):
    for field in inputs[table][0]:
        changed = copy.deepcopy(inputs)
        changed[table][0][field] += " changed"
        with pytest.raises(ValueError):
            apply_structure_corrections(*changed)


@pytest.mark.parametrize("table,count", [(0, 0), (0, 2), (2, 0), (2, 2)])
def test_missing_or_duplicate_source_target_rejected(inputs, table, count):
    inputs[table][:] = inputs[table] * count
    with pytest.raises(ValueError, match="exactly one"):
        apply_structure_corrections(*inputs)


@pytest.mark.parametrize("field", [
    "action", "source_id", "expected_source_row_sha256", "target_chebi_id",
    "expected_target_row_sha256", "standard_inchi", "stereo_complete",
    "reference", "curator", "date", "rationale",
])
@pytest.mark.parametrize("value", [None, "", " "])
def test_incomplete_decision_rejected(inputs, field, value):
    inputs[1][0][field] = value
    with pytest.raises(ValueError):
        apply_structure_corrections(*inputs)


@pytest.mark.parametrize("field,value", [
    ("action", "REPLACE"), ("reference", "uncited"), ("reference", "https://"),
    ("date", "2026-02-30"), ("date", "20261007"), ("stereo_complete", "True"),
    ("standard_inchi", "InChI=invalid"), ("expected_source_row_sha256", "x" * 64),
])
def test_malformed_decision_rejected(inputs, field, value):
    inputs[1][0][field] = value
    with pytest.raises(ValueError):
        apply_structure_corrections(*inputs)


def test_duplicate_decisions_rejected(inputs):
    inputs[1].append(copy.deepcopy(inputs[1][0]))
    with pytest.raises(ValueError, match="duplicate structure"):
        apply_structure_corrections(*inputs)


@pytest.mark.parametrize("key", [OLD, NEW])
def test_occupied_source_or_destination_not_merged(inputs, key):
    inputs[0].append({**inputs[0][0], "compound_index": "2", "standard_inchi_key": key})
    with pytest.raises(ValueError, match="distinct owners"):
        apply_structure_corrections(*inputs)


def test_chebi_collision_rejected(inputs):
    inputs[2].append({**inputs[2][0], "chebi_id": "CHEBI:999999"})
    with pytest.raises(ValueError, match="distinct owners"):
        apply_structure_corrections(*inputs)


def test_corrected_seed_joins_only_corrected_key(inputs):
    inventories = seed.read_inventories()
    inventories["mibig_compounds"] = inputs[0]
    inventories.pop("mibig_locus_evidence_overrides")
    doc, = seed.build_records(inventories)
    assert doc["identifier"] == "CHEBI:80024"
    assert doc["chemical_structure"]["structure_source"] == "CHEBI"
    assert doc["chemical_structure"]["standard_inchi_key"] == NEW
    assert "xrefs" not in doc
    assert not any(o["source"] == "LOTUS" for o in doc.get("occurrences", []))
    assert any(link["corpus"] == "AntibioticMech" and link["identifier"] == "CHEBI:80024"
               for link in doc["related_records"])
    assert all(len(link['source_version']) == 40 for link in doc['related_records'])
    assert all(o['evidence'][0]['reference'].startswith(('https://', 'DOI:', 'PMID:'))
               for o in doc.get('occurrences', []))
    assert doc["source_concepts"][0]["minted_identifier"] == "naturalproductmech:mibig-a7a97dab7f"
    assert len(doc["source_concepts"]) == 2
    for claim in doc["producer_organisms"] + doc["biosynthetic_gene_clusters"]:
        assert claim["evidence"][0]["evidence_type"] == "DATABASE_ASSERTION"
        assert claim["evidence"][1]["evidence_type"] == "CURATOR_INFERENCE"
        assert claim["evidence"][1]["reference"] == "DOI:10.1021/ja102751h"
    assert doc["discussions"][0]["status"] == "RESOLVED"
    assert not validate_natural_product({k: v for k, v in doc.items() if not k.startswith('_')})


def test_no_correction_is_an_identity_operation(inputs):
    rows, _, chebi = inputs
    assert apply_structure_corrections(rows, [], chebi) == rows


def test_seed_refuses_identity_overwrite_before_any_writes(tmp_path, monkeypatch):
    monkeypatch.setattr(seed, "CORPUS_DIR", tmp_path)
    directory = tmp_path / "polyketides"
    directory.mkdir()
    path = directory / "existing.yaml"
    path.write_text(yaml.safe_dump({"chemical_structure": {"standard_inchi_key": OLD}}))
    before = path.read_bytes()
    first = {"identifier": "new", "np_pathway": "POLYKETIDES", "_slug": "new",
             "chemical_structure": {"standard_inchi_key": NEW}}
    second = {**first, "identifier": "existing", "_slug": "existing"}
    monkeypatch.setattr(seed, "write_validated_natural_product",
                        lambda *args: pytest.fail("no writes allowed before complete preflight"))
    with pytest.raises(ValueError, match="explicit curation migration"):
        seed.write_records([first, second])
    assert path.read_bytes() == before


def test_ordinary_carry_does_not_migrate_chemistry():
    payload = {"chemical_structure": {"standard_inchi_key": NEW}}
    old = {"chemical_structure": {"standard_inchi_key": OLD},
           "causal_graphs": ["not transferable"], "curation_history": ["old"]}
    seed.carry_curator_owned_fields(payload, old)
    assert "causal_graphs" not in payload and "curation_history" not in payload


def test_new_path_does_not_bypass_explicit_owner_migration(tmp_path, monkeypatch):
    monkeypatch.setattr(seed, "CORPUS_DIR", tmp_path)
    old_path = tmp_path / "old.yaml"
    old_path.write_text(yaml.safe_dump({"chemical_structure": {"standard_inchi_key": OLD}}))
    doc = {"identifier": "CHEBI:80024", "np_pathway": "POLYKETIDES", "_slug": "new",
           "_previous_standard_inchi_key": OLD,
           "chemical_structure": {"standard_inchi_key": NEW}}
    monkeypatch.setattr(seed, "write_validated_natural_product", lambda *args: pytest.fail("write"))
    with pytest.raises(ValueError, match="old structure owner remains"):
        seed.write_records([doc])


def test_classifier_uses_corrected_structure_and_rejects_missing_source(monkeypatch, tmp_path, inputs):
    spec = importlib.util.spec_from_file_location('classifier_correction_tests',
                                                ROOT / 'scripts/extract_npclassifier.py')
    classifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(classifier)
    wanted = classifier.structures_needing_classification()
    assert NEW in wanted and OLD not in wanted
    assert wanted[NEW] == inputs[2][0]['smiles']
    monkeypatch.setattr(classifier, 'MIBIG_INVENTORY', tmp_path / 'missing.tsv')
    with pytest.raises(ValueError, match='exactly one'):
        classifier.structures_needing_classification()


def test_aureothin_migration_preserves_original_aurf_and_history():
    doc = yaml.safe_load((ROOT / 'data/natural_products/polyketides/aureothin.yaml').read_text())
    assert doc['identifier'] == 'CHEBI:80024'
    # Prefixes allow later curation without weakening the migration's preservation contract.
    expected = {
        'causal_graphs': (1, '6cfe06b5b0f0a449aec6e5c0a49d4594014e9a148a9b6d2a95a2b6780c4f1f88'),
        'biosynthetic_pathway': (1, '54b71c7713e81d3a396f46b45c44353269585ce1d3eb3b31df6d5c71970d11aa'),
        'curation_history': (3, '16a8634bb47bfaf271b5cd8d1d4da1fe5950f9e79339a899bd6ff79dbc0e401c'),
    }
    for field, (count, digest) in expected.items():
        value = json.dumps(doc[field][:count], sort_keys=True, separators=(',', ':'))
        assert hashlib.sha256(value.encode()).hexdigest() == digest
