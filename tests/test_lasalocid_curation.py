"""Lasalocid provenance fixes must not silently adjudicate product identity."""

import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load((ROOT / 'data/natural_products/polyketides' / f'{slug}.yaml').read_text())


@pytest.mark.parametrize('slug,key,stereo', [
    ('lasalocid', 'BBMULGJBVDDDNI-OWKLGTHSSA-N', True),
    ('lasalocid-2', 'RDHDUYAKDYQPEW-UHFFFAOYSA-M', False),
])
def test_identity_and_evidence_tiers_are_not_promoted(slug, key, stereo):
    doc = record(slug)
    assert doc['chemical_structure']['standard_inchi_key'] == key
    assert doc['chemical_structure']['stereo_complete'] is stereo
    assert doc['curation_status'] == 'SEEDED'
    assert doc['biosynthesis_origin'] == 'NATURAL_PRODUCT'
    assert {p['evidence_basis'] for p in doc['producer_organisms']} == {'SOURCE_ASSERTION'}
    assert {c['link_evidence_basis'] for c in doc['biosynthetic_gene_clusters']} == {'CLUSTER_UNSTATED'}


def test_fxj_producer_and_locus_references_are_separate():
    doc = record('lasalocid')
    producer, = doc['producer_organisms']
    cluster, = doc['biosynthetic_gene_clusters']
    assert producer['strain'] == 'FXJ1.172'
    assert producer['taxon_id'] == cluster['organism_taxon_id'] == 'NCBITaxon:1931'
    assert producer['evidence'][0]['reference'] == 'DOI:10.1128/AEM.02915-10'
    assert cluster['evidence'][0]['reference'] == 'https://www.ncbi.nlm.nih.gov/nuccore/KT591188.1'
    assert cluster['genome_accession'] == 'genbank:KT591188.1'
    for claim in (producer, cluster):
        assert claim['evidence'][0]['evidence_type'] == 'DATABASE_ASSERTION'
        assert 'PMID:19129623' not in {e['reference'] for e in claim['evidence']}
        assert any(e.get('evidence_type') == 'CURATOR_INFERENCE'
                   and 'Original imported citation PMID:19129623' in e.get('notes', '')
                   for e in claim['evidence'])
    assert any(e['reference'] == 'DOI:10.1271/BBB.80631'
               for occurrence in doc['occurrences'] for e in occurrence['evidence'])


def test_conflicting_salt_strain_assertions_stay_unresolved():
    doc = record('lasalocid-2')
    discussion, = [d for d in doc['discussions']
                   if d['discussion_id'] == 'curator-lasalocid-ab449340-strain-conflict']
    assert discussion['status'] == 'OPEN'
    for qualifier in ('ATCC31180', 'ATCC35851', 'NRRL3382R'):
        assert qualifier in discussion['rationale']
    assert {e['reference'] for e in discussion['evidence']} == {
        'https://www.ncbi.nlm.nih.gov/nuccore/AB449340.1',
        'https://www.ncbi.nlm.nih.gov/nuccore/FM173265.1',
        'DOI:10.1271/bbb.80631',
    }
    assert all('strain' not in p for p in doc['producer_organisms'])
    assert {p['evidence'][0]['reference'] for p in doc['producer_organisms']} == {
        'PMID:18710235', 'PMID:19025863',
    }


def test_portable_sources_match_receipts_and_historical_owners():
    evidence = ROOT / 'reviews/evidence/20261014-lasalocid'
    manifest = json.loads((evidence / 'manifest.json').read_text())
    base = '64c095104e5352fb88ad3177c47995ccfd4275d5'
    assert manifest['base'] == base
    assert manifest['owners'] == {
        f'{slug}-before.yaml': {
            'git_revision': base,
            'path': f'data/natural_products/polyketides/{slug}.yaml',
        } for slug in ('lasalocid', 'lasalocid-2')
    }
    for name, digest in manifest['files'].items():
        assert hashlib.sha256((evidence / name).read_bytes()).hexdigest() == digest
    for name, receipt in manifest['retrievals'].items():
        assert receipt['sha256'] == manifest['files'][name]
    for name, owner in manifest['owners'].items():
        original = subprocess.check_output(
            ['git', 'show', f"{owner['git_revision']}:{owner['path']}"], cwd=ROOT,
        )
        assert (evidence / name).read_bytes() == original
    strains = {}
    for sequence in ET.parse(evidence / 'genbank.xml').getroot():
        qualifiers = sequence.findall(
            "./GBSeq_feature-table/GBFeature[GBFeature_key='source']/GBFeature_quals/GBQualifier",
        )
        strains[sequence.findtext('GBSeq_accession-version')] = [
            q.findtext('GBQualifier_value') for q in qualifiers
            if q.findtext('GBQualifier_name') == 'strain'
        ]
    assert strains == {'AB449340.1': ['ATCC 31180'], 'FM173265.1': ['NRRL 3382R'],
                       'KT591188.1': ['FXJ1.172']}
