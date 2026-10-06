"""Presentation regressions for site audit #573–#583."""
from __future__ import annotations

from copy import deepcopy

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from tests.test_render_pages import REPO_ROOT
from tests.test_render_pages import render_pages as site


def render(name, **context):
    env = Environment(loader=FileSystemLoader(site.TEMPLATES_DIR),
                      autoescape=select_autoescape(["html"]))
    return env.get_template(name).render(**context)


def record(doc):
    return site.build_record(REPO_ROOT / 'data/natural_products/alkaloids/example.yaml', doc)


def test_bioactivity_dedup_requires_full_source_equality():
    first = {'assay': 'assay', 'value': 1.2, 'units': 'uM',
             'evidence': [{'reference': 'PMID:1'}]}
    target = {**deepcopy(first), 'target_enzyme': 'UniProtKB:P00519'}
    condition = {**deepcopy(first), 'notes': 'different condition'}
    result = record({'identifier': 'CHEBI:1', 'bioactivities': [first, deepcopy(first), target, condition]})
    assert result['bioactivity_total'] == 3
    assert result['bioactivity_duplicates'] == 1
    assert [b['source'] for b in result['bioactivities']] == [first, target, condition]
    html = render('record.html', r=result)
    assert 'Not recorded' in html and 'UniProtKB:P00519' in html
    assert 'different condition' in html


def test_staurosporine_pairs_keep_their_different_target_scope():
    path = REPO_ROOT / 'data/natural_products/alkaloids/staurosporine-2.yaml'
    doc = yaml.safe_load(path.read_text())
    built = site.build_record(path, doc)
    for aid in (1963315, 1963316, 1963317):
        matches = [b for b in built['bioactivities'] if b['reference'] == f'pubchem.aid:{aid}']
        assert len(matches) == 2
        assert {b['target'] for b in matches} == {'Not recorded', 'UniProtKB:P00519'}
    assert 'not independent replications' in render('record.html', r=built)


def test_review_note_and_status_explanation_keep_mapping_uncertain():
    doc = {'identifier': 'CHEBI:1', 'grounding_status': 'REVIEW_NEEDED',
           'grounding_notes': 'CHEBI:62219 or CHEBI:75306 <unresolved>', 'curation_status': 'SEEDED'}
    html = render('record.html', r=record(doc))
    assert 'CHEBI:62219 or CHEBI:75306 &lt;unresolved&gt;' in html
    assert 'does not imply that no later curation occurred' in html
    assert 'not independently verified human review' in html


def test_related_links_require_pinned_identity_and_preserve_relationship(monkeypatch):
    row = {'identifier': 'CHEBI:1', 'standard_inchi_key': 'KEY', 'corpus_commit': 'abc123',
           'antimicrobial_class': 'ANTIVIRAL', 'slug': 'compound'}
    monkeypatch.setattr(site, 'antibiotic_routes', lambda: {'CHEBI:1': [row]})
    link = {'corpus': 'AntibioticMech', 'identifier': 'CHEBI:1', 'source_version': 'abc',
            'relation': 'SAME_STRUCTURE', 'basis': 'SAME_INCHIKEY'}
    result = site.related_link(link, {'standard_inchi_key': 'KEY'})
    assert result['url'].endswith('/AntibioticMech/pages/antiviral/compound.html')
    assert result['relation'] == link['relation']
    assert 'url' not in site.related_link(link, {'standard_inchi_key': 'DIFFERENT'})
    assert 'url' not in site.related_link({**link, 'source_version': 'zzz'}, {'standard_inchi_key': 'KEY'})


def test_search_aliases_include_structure_and_source_identifiers_without_mutation():
    doc = {'identifier': 'CHEBI:1', 'xrefs': ['pubchem.compound:123'],
           'chemical_structure': {'standard_inchi_key': 'KEY'},
           'source_concepts': [{'source_id': 'mibig:BGC1'}]}
    original = deepcopy(doc)
    assert site.search_identifiers(doc) == ['CHEBI:1', 'KEY', 'pubchem.compound:123', 'mibig:BGC1']
    assert doc == original


def test_pathway_lists_use_counts_and_links_instead_of_dictionary_strings():
    r = record({'identifier': 'CHEBI:1', 'label': 'example',
                'occurrences': [{'taxon_label': 'Taxon', 'evidence': [{'reference': 'PMID:1'}]}],
                'biosynthetic_gene_clusters': [{'accession': 'BGC0001'}]})
    html = render('pathway.html', pathway={'title': 'Alkaloids', 'count': 1, 'records': [r]})
    assert '1 cited occurrence' in html and 'example.html#occurrences' in html
    assert '1 gene cluster' in html and 'example.html#gene-clusters' in html
    assert "{'" not in html
    empty = render('pathway.html', pathway={'records': [record({'identifier': 'CHEBI:2'})]})
    assert 'None cited' in empty and 'None recorded' in empty


def test_duplicate_labels_are_disambiguated_without_merging_records():
    records = [record({'identifier': f'CHEBI:{n}', 'label': 'same'}) for n in (1, 2)]
    for n, r in enumerate(records):
        r.update(duplicate_label=True, slug=f'compound-{n}')
    html = render('browse.html', total=2, pathways=[{'slug': 'alkaloids', 'records': records}])
    assert html.count('class="mono"') == 2
    assert 'compound-0.html' in html and 'compound-1.html' in html


def test_404_links_are_absolute_for_arbitrary_missing_routes():
    html = render('not_found.html', root=site.SITE_BASE)
    assert f'href="{site.SITE_BASE}browse.html"' in html


def test_all_record_grounding_notes_are_retained_in_the_view():
    count = 0
    for path in site.CORPUS_DIR.rglob('*.yaml'):
        doc = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
        if doc.get('grounding_notes'):
            built = site.build_record(path, doc)
            assert built['grounding_note'] == doc['grounding_notes']
            assert 'Grounding review:' in render('record.html', r=built)
            count += 1
    assert count > 0
