"""Keep lomaiviticin identity conflicts separate from locus attribution fixes."""

import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'reviews/evidence/20261014-lomaiviticin'
SLUGS = ('lomaiviticin-c-2', 'lomaiviticin-c', 'lomaiviticin-d-2', 'lomaiviticin-d')
SPEC = spec_from_file_location('lomaiviticin_seed', ROOT / 'scripts/seed_from_sources.py')
SEED = module_from_spec(SPEC)
SPEC.loader.exec_module(SEED)


def record(slug):
    return yaml.safe_load((ROOT / 'data/natural_products/polyketides' / f'{slug}.yaml').read_text())


@pytest.mark.parametrize('slug', SLUGS)
def test_identity_history_and_supported_graph_edges_are_preserved(slug):
    doc = record(slug)
    before = yaml.safe_load((PACKET / f'{slug}-before.yaml').read_text())
    for field in ('identifier', 'chemical_structure', 'np_pathway', 'np_classification',
                  'source_concepts', 'biosynthesis_origin', 'curation_status'):
        assert doc[field] == before[field]
    assert doc['curation_status'] == 'SEEDED'
    assert doc['curation_history'][:len(before['curation_history'])] == before['curation_history']
    assert doc['curation_history'][-1]['action'] == 'RECORD_CURATED'
    assert doc['curation_history'][-1]['llm_assisted'] is True
    graph, = doc['causal_graphs']
    old_graph, = before['causal_graphs']
    assert graph['nodes'] == old_graph['nodes']
    assert graph['edges'][:-1] == old_graph['edges'][:-1]
    assert 'Exact-product identity remains disputed' in graph['edges'][-1]['notes']
    assert 'Exact-product identity remains disputed' in doc['biosynthetic_pathway'][0]['notes']
    discussion, = [d for d in doc['discussions']
                   if d['discussion_id'] == 'curator-lomaiviticin-identity-conflict']
    assert discussion['status'] == 'OPEN'
    assert discussion['evidence']
    if doc['label'] == 'lomaiviticin D':
        assert 'not automatically' in graph['edges'][-1]['notes']


@pytest.mark.parametrize('slug', ('lomaiviticin-c', 'lomaiviticin-d-2'))
def test_pacifica_locus_is_not_graded_by_other_strains(slug):
    doc = record(slug)
    producer, = doc['producer_organisms']
    cluster, = doc['biosynthetic_gene_clusters']
    assert producer['evidence_basis'] == 'SOURCE_ASSERTION'
    assert cluster['link_evidence_basis'] == 'CLUSTER_UNSTATED'
    assert 'locus_evidence_methods' not in cluster
    assert cluster['genome_accession'] == 'genbank:KF731828.1'
    assert producer['taxon_id'] == cluster['organism_taxon_id'] == 'NCBITaxon:351187'
    assert cluster['evidence'][0]['reference'] == 'https://www.ncbi.nlm.nih.gov/nuccore/KF731828.1'
    for claim in (producer, cluster):
        assert claim['evidence'][0]['evidence_type'] == 'DATABASE_ASSERTION'
        assert any('DPJ-0019' in e.get('notes', '') and e['evidence_type'] == 'CURATOR_INFERENCE'
                   for e in claim['evidence'])
        assert 'PMID:23649992' not in {e['reference'] for e in claim['evidence']}
    if slug == 'lomaiviticin-c':
        assert producer['strain'] == 'DPJ-0016'
        assert producer['evidence'][0]['reference'] == 'DOI:10.1016/j.tet.2014.03.009'
    else:
        assert 'strain' not in producer
        assert producer['evidence'][0]['reference'].endswith('/BGC0000240.5/')
        discussion, = [d for d in doc['discussions']
                       if d['discussion_id'] == 'curator-lomaiviticin-d-producer-strain']
        assert discussion['status'] == 'OPEN'
        assert 'not proof of nonproduction' in discussion['rationale']


@pytest.mark.parametrize('slug', ('lomaiviticin-c-2', 'lomaiviticin-d'))
def test_cnb440_experimental_provenance_is_not_withdrawn(slug):
    doc = record(slug)
    before = yaml.safe_load((PACKET / f'{slug}-before.yaml').read_text())
    for field in ('producer_organisms', 'biosynthetic_gene_clusters'):
        assert doc[field] == before[field]


def test_only_the_two_reviewed_mibig_rows_change():
    rows = [r for r in SEED.read_tsv(ROOT / 'data/raw/mibig_compounds.tsv')
            if r['mibig_accession'] in ('BGC0000240', 'BGC0000241')]
    inputs = {'mibig_compounds': rows}
    before = {d['identifier']: d for d in SEED.build_records(inputs)}
    for key, filename in (
        ('mibig_locus_evidence_overrides', 'mibig_locus_evidence_overrides.tsv'),
        ('mibig_claim_references', 'mibig_claim_references.tsv'),
        ('mibig_producer_strains', 'mibig_producer_strains.tsv'),
    ):
        inputs[key] = [r for r in SEED.read_tsv(ROOT / 'curation' / filename)
                       if r['source_id'].split(':')[0] == 'BGC0000240']
    original = deepcopy(inputs)
    after = {d['identifier']: d for d in SEED.build_records(inputs)}
    assert inputs == original
    assert set(before) == set(after)
    changed = {key for key in before if before[key] != after[key]}
    assert changed == {'naturalproductmech:mibig-5a11cea583', 'naturalproductmech:mibig-ba6ee9b824'}


@pytest.mark.parametrize('identifier', (
    'naturalproductmech:mibig-5a11cea583', 'naturalproductmech:mibig-ba6ee9b824',
))
@pytest.mark.parametrize('field', SEED.MIBIG_WITHDRAWAL_CONTEXT)
def test_each_withdrawal_pin_rejects_source_drift(identifier, field):
    decisions = [r for r in SEED.read_tsv(SEED.MIBIG_LOCUS_EVIDENCE_OVERRIDES)
                 if r['minted_identifier'] == identifier]
    overrides = SEED.load_mibig_locus_evidence_overrides(decisions)
    row, = [r for r in SEED.read_tsv(ROOT / 'data/raw/mibig_compounds.tsv')
            if SEED.mint_identifier('MIBIG', r['mibig_accession'] + ':' + r['compound_index']) == identifier]
    row[field] += ' changed'
    with pytest.raises(ValueError, match='source context changed'):
        SEED.apply_mibig_locus_evidence_override(row, overrides)


def test_evidence_hashes_historical_owners_and_strain_deposits():
    manifest = json.loads((PACKET / 'manifest.json').read_text())
    for name, digest in manifest['files'].items():
        assert hashlib.sha256((PACKET / name).read_bytes()).hexdigest() == digest
    for name, receipt in manifest['retrievals'].items():
        assert receipt['sha256'] == manifest['files'][name]
    for name, owner in manifest['owners'].items():
        original = subprocess.check_output(
            ['git', 'show', f"{owner['git_revision']}:{owner['path']}"], cwd=ROOT)
        assert (PACKET / name).read_bytes() == original
    strains = {}
    for sequence in ET.parse(PACKET / 'pacifica-loci.xml').getroot():
        quals = sequence.findall(
            "./GBSeq_feature-table/GBFeature[GBFeature_key='source']/GBFeature_quals/GBQualifier")
        strains[sequence.findtext('GBSeq_accession-version')] = [
            q.findtext('GBQualifier_value') for q in quals
            if q.findtext('GBQualifier_name') == 'strain']
    assert strains == {'KF731828.1': ['DPJ-0016'], 'KF515737.1': ['DPJ-0019']}
