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


ORIGINAL_AURF_COVERAGE = (
    'This is a single curated starter-unit N-oxygenation step; downstream PKS loading, '
    'extension, O-methylation, and tetrahydrofuran formation remain uncurated.'
)
CURATED_AURF_COVERAGE = (
    'This graph covers the starter-unit N-oxygenation step; downstream tailoring '
    'is represented separately where curated.'
)


def _assert_aureothin_preservation(doc):
    doc = copy.deepcopy(doc)
    assert doc['identifier'] == 'CHEBI:80024'
    # The migration preserved the whole graph. Later AurI curation changes only
    # its stale coverage note; normalize that audited exception, not biology.
    edge = doc['causal_graphs'][0]['edges'][1]
    if edge['notes'] == CURATED_AURF_COVERAGE:
        assert any(
            event.get('action') == 'RECORD_CURATED'
            and 'clarified only the old AurF coverage note' in event.get('changes', '')
            for event in doc['curation_history'][4:]
        ), 'The later coverage-note update needs its own curation event'
        edge['notes'] = ORIGINAL_AURF_COVERAGE
    # Retain the original digests: no other graph, pathway or history changes
    # can be hidden by updating a golden hash to match the current corpus.
    expected = {
        'causal_graphs': (1, '6cfe06b5b0f0a449aec6e5c0a49d4594014e9a148a9b6d2a95a2b6780c4f1f88'),
        'biosynthetic_pathway': (1, '54b71c7713e81d3a396f46b45c44353269585ce1d3eb3b31df6d5c71970d11aa'),
        'curation_history': (3, '16a8634bb47bfaf271b5cd8d1d4da1fe5950f9e79339a899bd6ff79dbc0e401c'),
    }
    for field, (count, digest) in expected.items():
        value = json.dumps(doc[field][:count], sort_keys=True, separators=(',', ':'))
        assert hashlib.sha256(value.encode()).hexdigest() == digest


def test_aureothin_migration_preserves_original_aurf_and_history():
    doc = yaml.safe_load((ROOT / 'data/natural_products/polyketides/aureothin.yaml').read_text())
    before = copy.deepcopy(doc)
    _assert_aureothin_preservation(doc)
    assert doc == before


def test_original_aurf_coverage_needs_no_later_curation_exception():
    doc = yaml.safe_load((ROOT / 'data/natural_products/polyketides/aureothin.yaml').read_text())
    doc['causal_graphs'][0]['edges'][1]['notes'] = ORIGINAL_AURF_COVERAGE
    doc['curation_history'] = doc['curation_history'][:4]
    _assert_aureothin_preservation(doc)


@pytest.mark.parametrize('changed', [
    'protein', 'predicate', 'evidence', 'coverage', 'pathway', 'history', 'audit',
])
def test_aurf_coverage_exception_does_not_hide_other_changes(changed):
    doc = yaml.safe_load((ROOT / 'data/natural_products/polyketides/aureothin.yaml').read_text())
    graph = doc['causal_graphs'][0]
    if changed == 'protein':
        graph['nodes'][1]['identifier'] = 'UniProtKB:Q70KH3'
    elif changed == 'predicate':
        graph['edges'][1]['predicate'] = 'inhibits'
    elif changed == 'evidence':
        graph['edges'][1]['evidence'][0]['evidence_type'] = 'CURATOR_INFERENCE'
    elif changed == 'coverage':
        graph['edges'][1]['notes'] = 'Unreviewed coverage claim.'
    elif changed == 'pathway':
        doc['biosynthetic_pathway'][0]['product'] = 'CHEBI:80024'
    elif changed == 'history':
        doc['curation_history'][0]['changes'] = 'Rewritten history.'
    else:
        graph['edges'][1]['notes'] = CURATED_AURF_COVERAGE
        doc['curation_history'] = doc['curation_history'][:4]
    with pytest.raises(AssertionError):
        _assert_aureothin_preservation(doc)


def test_table_owned_adjudication_is_not_overwritten_by_old_discussion():
    payload = {'chemical_structure': {'standard_inchi_key': NEW}, 'discussions': [{
        'discussion_id': 'source-structure-correction', 'resolution_note': 'new table decision',
        'evidence': [{'reference': 'DOI:10.1021/ja102751h'}],
    }]}
    expected = copy.deepcopy(payload['discussions'])
    old = copy.deepcopy(payload)
    old['discussions'][0]['resolution_note'] = 'superseded decision'
    old['discussions'][0]['evidence'] = [{'reference': 'old citation'}]
    seed.carry_curator_owned_fields(payload, old)
    assert payload['discussions'] == expected


def test_structure_and_locus_withdrawal_pin_the_same_raw_source(inputs):
    source = inputs[0][0]
    # WITHDRAW requires explicit coordinates; this synthetic source supplies them.
    source.update({'locus_from': '1', 'locus_to': '29132'})
    inputs[1][0]['expected_source_row_sha256'] = row_digest(source)
    withdrawal = {
        'minted_identifier': seed.mint_identifier('MIBIG', 'BGC0000024:1'),
        'source': 'MIBIG', 'source_id': 'BGC0000024', 'action': 'WITHDRAW',
        'locus_evidence_methods': '', 'reference': 'https://example.org/test-decision',
        'rationale': 'Synthetic test decision, not production curation.',
        'curator': 'test', 'date': '2026-10-07',
        **{'expected_' + field: source[field] for field in seed.MIBIG_WITHDRAWAL_CONTEXT},
    }
    doc, = seed.build_records({
        'mibig_compounds': inputs[0], 'chebi_structures': inputs[2],
        'mibig_structure_corrections': inputs[1], 'mibig_locus_evidence_overrides': [withdrawal],
    })
    assert doc['chemical_structure']['standard_inchi_key'] == NEW
    producer, = doc['producer_organisms']
    cluster, = doc['biosynthetic_gene_clusters']
    assert producer['evidence_basis'] == 'SOURCE_ASSERTION'
    assert cluster['link_evidence_basis'] == 'CLUSTER_UNSTATED'
    assert 'locus_evidence_methods' not in cluster
    for claim in (producer, cluster):
        assert [e['evidence_type'] for e in claim['evidence']] == [
            'DATABASE_ASSERTION', 'CURATOR_INFERENCE', 'CURATOR_INFERENCE']
        assert claim['evidence'][1]['reference'] == withdrawal['reference']
        assert claim['evidence'][2]['reference'] == inputs[1][0]['reference']


@pytest.mark.parametrize('limit', [-1, 0])
def test_nonpositive_write_limit_never_writes(tmp_path, monkeypatch, limit):
    monkeypatch.setattr(seed, 'CORPUS_DIR', tmp_path)
    monkeypatch.setattr(seed, 'write_validated_natural_product', lambda *args: pytest.fail('write'))
    docs = [{'identifier': f'CHEBI:{i}', 'np_pathway': 'POLYKETIDES', '_slug': str(i),
             'chemical_structure': {'standard_inchi_key': NEW}} for i in range(2)]
    assert seed.write_records(docs, limit=limit) == 0
