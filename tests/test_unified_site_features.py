"""The fleet's unified website features, held on this site's pages.

Each test is driven by an input on which the old page and the fixed page
differ: a link that used to 404, a reference that used to be text, a section
that used to be absent. Tests over committed pages rely on `render --check`
in the gate to keep pages/ current.
"""
from __future__ import annotations

import html
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
from markupsafe import escape

from tests.test_render_pages import REPO_ROOT
from tests.test_render_pages import render_pages as site

PAGES = REPO_ROOT / "pages"


def between(text: str, start: str, end: str) -> str:
    begin = text.index(start)
    return text[begin:text.index(end, begin + len(start))]


def hrefs(fragment: str) -> list[str]:
    return [html.unescape(href) for href in re.findall(r'href="([^"]*)"', fragment)]


def view(doc: dict, rel: str = "alkaloids/example.yaml") -> dict:
    return site.build_record(site.CORPUS_DIR / rel, doc)


def render_record(record: dict, **context) -> str:
    return site.template_environment().get_template("record.html").render(
        r=record, root="../", **context)


def page(rel: str) -> str:
    return (PAGES / rel).read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def loaded():
    """Every record as the renderer reads it; loaded once, it is the slow part."""
    return site.load_records()


@pytest.fixture(scope="module")
def corpus(loaded):
    """Every record and its view, as `just render` builds them."""
    return [(path, doc, site.build_record(path, doc)) for path, doc in loaded]


def committed_record_pages():
    return sorted(p for p in PAGES.glob("*/*.html") if p.name != "index.html")


# ---------------------------------------------------------------------------
# cross_mech_links: every sibling link uses a route verified live (#986, #987)
# ---------------------------------------------------------------------------

#: claw's verified sibling route table (2026-10-25), search and record routes.
VERIFIED_ROUTES = (
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon%3A",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/PathwayMech/pages/records/",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
) + tuple(f"https://culturebotai.github.io/AntibioticMech/pages/{directory}/"
          for directory in sorted(set(site.ANTIBIOTICMECH_CLASS_DIRS.values())))
SIBLING = re.compile(r"https://culturebotai\.github\.io/(?!NaturalProductMech/|mechs/)[^\"'\s<>]+")


def test_every_sibling_url_on_a_committed_page_uses_a_verified_route():
    unverified = {}
    for path in [*committed_record_pages(), *PAGES.glob("*.html"), *PAGES.glob("*/index.html")]:
        for url in SIBLING.findall(path.read_text(encoding="utf-8")):
            url = html.unescape(url)
            if not url.startswith(VERIFIED_ROUTES):
                unverified.setdefault(url, path.relative_to(PAGES).as_posix())
    assert not unverified, sorted(unverified.items())[:10]


def test_antibioticmech_unspecified_class_links_its_directory_not_a_lowercased_name(monkeypatch):
    rows = {"CHEBI:41977": [{"identifier": "CHEBI:41977", "standard_inchi_key": "KEY",
                             "antimicrobial_class": "ANTIMICROBIAL_UNSPECIFIED",
                             "slug": "daunorubicin", "corpus_commit": "74f6cc8"}],
            "CHEBI:2": [{"identifier": "CHEBI:2", "standard_inchi_key": "KEY",
                         "antimicrobial_class": "SOMETHING_NEW", "slug": "two",
                         "corpus_commit": "74f6cc8"}]}
    monkeypatch.setattr(site, "antibiotic_routes", lambda: rows)
    link = {"corpus": "AntibioticMech", "identifier": "CHEBI:41977", "source_version": "74f6cc8",
            "relation": "SAME_STRUCTURE", "basis": "SAME_INCHIKEY"}
    assert site.related_link(link, {"standard_inchi_key": "KEY"})["url"] == (
        "https://culturebotai.github.io/AntibioticMech/pages/unspecified/daunorubicin.html")
    # A class with no known directory is left unlinked rather than guessed.
    assert "url" not in site.related_link({**link, "identifier": "CHEBI:2"},
                                          {"standard_inchi_key": "KEY"})


def test_the_four_pathwaymech_records_named_on_record_pages_are_links(corpus):
    linked = {}
    for _path, doc, record in corpus:
        for link in record["related"]:
            if link["corpus"] == "PathwayMech":
                linked[doc["identifier"]] = link.get("url")
    assert len(linked) == 4
    assert set(linked.values()) == {
        "https://culturebotai.github.io/PathwayMech/pages/records/MIBiG_BGC0002072.html",
        "https://culturebotai.github.io/PathwayMech/pages/records/MetaCyc_P101-PWY.html"}
    # The link needs the pinned row for this exact structure.
    link = {"corpus": "PathwayMech", "identifier": "MIBiG:BGC0002072",
            "source_version": "aa305727458c44ab05614901334540e2c87a9f3a"}
    assert "url" not in site.related_link(link, {"standard_inchi_key": "NOT-THE-PRODUCT"})


def test_explore_links_ask_each_sibling_only_what_it_can_answer():
    producers = [{"taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor"},
                 {"taxon_id": "NCBITaxon:1902", "taxon_label": "Streptomyces coelicolor"},
                 {"taxon_id": None, "taxon_label": "unnamed host"}]
    clusters = [{"accession": "mibig:BGC0002072"}, {"accession": "mibig:BGC0002072"}]
    exact = {"identifier": "CHEBI:42", "label": "x",
             "chemical_structure": {"standard_inchi_key": "AAA-BBB-N"}}
    urls = [link["url"] for link in site.sibling_links(exact, producers, clusters)]
    assert urls == [
        "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=AAA-BBB-N",
        "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=CHEBI%3A42",
        "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon%3A1902",
        "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=BGC0002072",
    ]
    minted = {**exact, "identifier": "naturalproductmech:mibig-0123456789"}
    assert not any("MediaIngredientMech" in link["url"]
                   for link in site.sibling_links(minted, producers, clusters))


# ---------------------------------------------------------------------------
# term_links: a displayed identifier opens where it can be looked up
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("curie, url", [
    ("CHEBI:338412", "http://purl.obolibrary.org/obo/CHEBI_338412"),
    ("NCBITaxon:47917", "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=47917"),
    ("mibig:BGC0002002", "https://mibig.secondarymetabolites.org/go/BGC0002002"),
    ("MIBIG:BGC0000223.5", "https://mibig.secondarymetabolites.org/go/BGC0000223.5"),
    ("genbank:NZ_CP011254.1", "https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP011254.1"),
    ("NCBI_Nuccore:AUSV01000133.1", "https://www.ncbi.nlm.nih.gov/nuccore/AUSV01000133.1"),
    ("NCBIProtein:WP_011030045.1", "https://www.ncbi.nlm.nih.gov/protein/WP_011030045.1"),
    ("npatlas:NPA04901", "https://www.npatlas.org/explore/compounds/NPA04901"),
    ("pubchem:44607162", "https://pubchem.ncbi.nlm.nih.gov/compound/44607162"),
    ("pubchem.aid:624296", "https://pubchem.ncbi.nlm.nih.gov/bioassay/624296"),
    ("chembl:CHEMBL1403281", "https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1403281"),
    ("lotus:Q105246007", "https://www.wikidata.org/wiki/Q105246007"),
    ("UniProtKB:Q9I0Q0", "https://www.uniprot.org/uniprotkb/Q9I0Q0/entry"),
    ("RHEA:37871", "https://www.rhea-db.org/rhea/37871"),
    ("EC:1.14.13.248", "https://enzyme.expasy.org/EC/1.14.13.248"),
    ("GO:1900796", "https://www.ebi.ac.uk/QuickGO/term/GO:1900796"),
    ("PDB:2WK1", "https://www.rcsb.org/structure/2WK1"),
    ("ComplexPortal:CPX-2010", "https://www.ebi.ac.uk/complexportal/complex/CPX-2010"),
    ("PMID:28373542", "https://pubmed.ncbi.nlm.nih.gov/28373542/"),
    ("DOI:10.1016/0005-2744(70)90044-4", "https://doi.org/10.1016/0005-2744%2870%2990044-4"),
    ("url:https://pubmed.ncbi.nlm.nih.gov/327539/", "https://pubmed.ncbi.nlm.nih.gov/327539/"),
    ("https://example.org/a?b=1", "https://example.org/a?b=1"),
    # Any other registered-looking prefix falls back to bioregistry.
    ("patent:JP2003125779A", "https://bioregistry.io/patent:JP2003125779A"),
    # No page exists for these; a link would be a dead end.
    ("cyanometdb:CyanoMetDB_1565", None),
    ("naturalproductmech:mibig-1155c4085f", None),
    ("antibioticmech:aro-34c0642a61", None),
    ("CHEBI:not-a-number", None),
    ("DOI:10.1/too-short", None),
    ("ISBN: 9789401773218", None),
    ("https://user:secret@example.org/x", None),
])
def test_identifier_routes(curie, url):
    assert site.curie_url(curie) == url


def test_term_link_opens_own_records_first_and_never_links_nowhere():
    env = site.template_environment()
    template = env.from_string("{{ value|term_link }}")
    record = {"identifier": "CHEBI:1", "record_path": "data/natural_products/alkaloids/one.yaml"}
    own = {"CHEBI:1": "alkaloids/one.html", "CHEBI:2": "polyketides/two.html",
           "naturalproductmech:mibig-0000000003": "unclassified/three.html"}
    context = {"r": record, "own_pages": own, "root": "../"}
    # Another of this corpus's records opens its page, not ChEBI.
    assert template.render(value="CHEBI:2", **context) == (
        '<a href="../polyketides/two.html">CHEBI:2</a>')
    # The page's own identity opens what the page is built from.
    assert template.render(value="CHEBI:1", **context) == (
        '<a href="http://purl.obolibrary.org/obo/CHEBI_1">CHEBI:1</a>')
    minted = {"identifier": "naturalproductmech:mibig-0000000003",
              "record_path": "data/natural_products/unclassified/three.yaml"}
    assert template.render(value=minted["identifier"], r=minted, own_pages=own, root="../") == (
        '<a href="https://github.com/CultureBotAI/NaturalProductMech/blob/main/'
        'data/natural_products/unclassified/three.yaml">naturalproductmech:mibig-0000000003</a>')
    assert template.render(value="cyanometdb:CyanoMetDB_1 <b>", **context) == (
        "cyanometdb:CyanoMetDB_1 &lt;b&gt;")
    assert template.render(value=None, **context) == ""


def displayed_identifiers(doc):
    """Every identifier a record page shows as an identifier."""
    yield doc["identifier"]
    yield from doc.get("xrefs") or []
    for p in doc.get("producer_organisms") or []:
        yield from (p.get("taxon_id"), p.get("biosynthetic_gene_cluster"))
    for o in doc.get("occurrences") or []:
        yield o.get("taxon_id")
    for c in doc.get("biosynthetic_gene_clusters") or []:
        yield from (c.get("accession"), c.get("organism_taxon_id"), c.get("genome_accession"))
    for s in doc.get("biosynthetic_pathway") or []:
        yield from (s.get("enzyme_id"), s.get("reaction_id"))
        yield from site.pathway_endpoints(s, "substrate", "substrates")
        yield from site.pathway_endpoints(s, "product", "products")
    for t in doc.get("molecular_targets") or []:
        yield from t.get("protein_examples") or []
        yield t.get("taxon_id")
    for b in doc.get("bioactivities") or []:
        yield b.get("target_enzyme")


#: MIBiG's placeholder for a sequence it holds itself: GenBank has no record of it.
MIBIG_SEQUENCE_PLACEHOLDER = re.compile(r"genbank:MIBIG\.BGC[0-9]+(?:\.[0-9]+)?")


def test_every_identifier_the_corpus_displays_resolves_or_is_deliberately_text(corpus):
    """The route shapes match this corpus: no known-prefix identifier falls
    through to text because its pattern was written for some other corpus."""
    own = {doc["identifier"] for _path, doc, _record in corpus}
    unresolved = {}
    for path, doc, _record in corpus:
        for value in filter(None, displayed_identifiers(doc)):
            prefix = value.split(":", 1)[0]
            if (value in own or site.curie_url(value) or prefix in site.UNRESOLVABLE
                    or MIBIG_SEQUENCE_PLACEHOLDER.fullmatch(value)):
                continue
            unresolved.setdefault(value, path.name)
    assert not unresolved, sorted(unresolved.items())[:10]
    assert site.curie_url("genbank:MIBIG.BGC0001325.1") is None


def test_a_committed_record_page_links_its_identifiers():
    anisomycin = page("alkaloids/anisomycin.html")
    header = between(anisomycin, "<h1>", "</p>")
    assert "http://purl.obolibrary.org/obo/CHEBI_338412" in hrefs(header)
    producers = between(anisomycin, "<h2>Producer organisms", "</table>")
    assert any(h.startswith("https://www.ncbi.nlm.nih.gov/Taxonomy/") for h in hrefs(producers))
    assert "https://mibig.secondarymetabolites.org/go/BGC0001510" in hrefs(producers)
    clusters = between(anisomycin, 'id="gene-clusters"', "</table>")
    assert any(h.startswith("https://www.ncbi.nlm.nih.gov/nuccore/") for h in hrefs(clusters))
    assert 'href="#"' not in anisomycin


# ---------------------------------------------------------------------------
# evidence: references are followable wherever record content shows them
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("text, links", [
    ("with ECO:0000269 PMID:11697907.", [("https://pubmed.ncbi.nlm.nih.gov/11697907/",
                                          "PMID:11697907")]),
    ("see doi:10.1038/nrmicro.2016.94).", [("https://doi.org/10.1038/nrmicro.2016.94",
                                            "doi:10.1038/nrmicro.2016.94")]),
    ("(10.1016/0005-2744(70)90044-4)", [("https://doi.org/10.1016/0005-2744%2870%2990044-4",
                                         "10.1016/0005-2744(70)90044-4")]),
    ("full text PMC94635.html", [("https://pmc.ncbi.nlm.nih.gov/articles/PMC94635/",
                                  "PMC94635")]),
    ("at https://example.org/a?b=1&c=2, then", [("https://example.org/a?b=1&amp;c=2",
                                                 "https://example.org/a?b=1&amp;c=2")]),
    ("javascript:alert(1) and PMID:x", []),
    ("https://user:secret@example.org/x", []),
    # Markup around a citation ends the token instead of joining it (CultureBotAI/TraitMech#2022).
    ("[10.1038/x](https://doi.org/10.1038/x)", [
        ("https://doi.org/10.1038/x", "10.1038/x"),
        ("https://doi.org/10.1038/x", "https://doi.org/10.1038/x")]),
    ("**10.1099/y**", [("https://doi.org/10.1099/y", "10.1099/y")]),
    ("`10.1146/z`", [("https://doi.org/10.1146/z", "10.1146/z")]),
    ("see **https://example.org/b**; and https://example.org/c:", [
        ("https://example.org/b", "https://example.org/b"),
        ("https://example.org/c", "https://example.org/c")]),
    # Scanning resumes after a trimmed token, so the second citation is found.
    ("(https://example.org/a)-(https://example.org/b)", [
        ("https://example.org/a", "https://example.org/a"),
        ("https://example.org/b", "https://example.org/b")]),
    ('https://example.org/"><script>x</script>', [("https://example.org/", "https://example.org/")]),
])
def test_autolink_links_only_citation_tokens_and_keeps_the_text(text, links):
    rendered = str(site.autolink(text))
    assert re.findall(r'<a href="([^"]*)">([^<]*)</a>', rendered) == links
    assert "<script>" not in rendered
    assert html.unescape(re.sub(r"<[^>]+>", "", rendered)) == text


@pytest.mark.parametrize("reference, url", [
    ("PMID:28373542", "https://pubmed.ncbi.nlm.nih.gov/28373542/"),
    ("DOI:10.1038/JA.2009.92", "https://doi.org/10.1038/JA.2009.92"),
    ("pubchem.aid:624296", "https://pubchem.ncbi.nlm.nih.gov/bioassay/624296"),
    ("url:https://pubmed.ncbi.nlm.nih.gov/327539/", "https://pubmed.ncbi.nlm.nih.gov/327539/"),
    ("Geigy Scientific Tables, doi:10.1002/abcd.1", "https://doi.org/10.1002/abcd.1"),
    ("ISBN: 9789401773218", None),
])
def test_a_whole_reference_opens_its_source(reference, url):
    rendered = str(site.reference_link(reference))
    assert hrefs(rendered) == ([url] if url else [])
    assert html.unescape(re.sub(r"<[^>]+>", "", rendered)) == reference


def test_references_link_in_every_part_of_a_record_page():
    ev = [{"reference": "PMID:101"}]
    doc = {
        "identifier": "CHEBI:1", "label": "x", "np_pathway": "ALKALOIDS",
        "definition": "Defined in PMID:102.",
        "grounding_notes": "Reviewed against doi:10.1000/ground.",
        "producer_organisms": [{"taxon_id": "NCBITaxon:2", "taxon_label": "t",
                                "evidence_basis": "BGC_CHARACTERIZED", "evidence": ev}],
        "occurrences": [{"taxon_id": "NCBITaxon:3", "taxon_label": "o",
                         "evidence": [{"reference": "PMID:103"}]}],
        "biosynthetic_pathway": [{"step_number": 1, "enzyme_label": "E",
                                  "notes": "Proposed in PMID:104.",
                                  "evidence": [{"reference": "DOI:10.1000/step"}]}],
        "causal_graphs": [{"scope": "BIOSYNTHESIS", "description": "From PMID:105.",
                           "nodes": [{"node_id": "a", "label": "a"}, {"node_id": "b", "label": "b"}],
                           "edges": [{"subject": "a", "predicate": "p", "object": "b",
                                      "notes": "See PMID:106.",
                                      "evidence": [{"reference": "PMID:107"}]}]}],
        "molecular_targets": [{"target_label": "T", "notes": "Measured in PMID:108.",
                               "evidence": [{"reference": "PMID:109"}]}],
        "bioactivities": [{"assay": "A", "evidence": [{"reference": "pubchem.aid:110"}]}],
        "discussions": [{"discussion_id": "q", "status": "OPEN", "prompt": "Does PMID:111 apply?"}],
        "curation_history": [{"timestamp": "2026-10-01T00:00:00Z", "curator": "c",
                              "action": "RECORD_CURATED", "changes": "Fixed per PMID:112"}],
    }
    rendered = render_record(view(doc))
    expected = {
        between(rendered, "<h1>", "<h2>Structure"): ["https://pubmed.ncbi.nlm.nih.gov/102/",
                                                     "https://doi.org/10.1000/ground"],
        between(rendered, "<h2>Producer organisms", "</table>"): ["https://pubmed.ncbi.nlm.nih.gov/101/"],
        between(rendered, 'id="occurrences"', "</table>"): ["https://pubmed.ncbi.nlm.nih.gov/103/"],
        between(rendered, "<h2>Biosynthesis", "<h2>Mechanism"): ["https://doi.org/10.1000/step",
                                                                "https://pubmed.ncbi.nlm.nih.gov/104/"],
        between(rendered, "<h2>Causal graph", "Every edge carries"): [
            "https://pubmed.ncbi.nlm.nih.gov/105/", "https://pubmed.ncbi.nlm.nih.gov/106/",
            "https://pubmed.ncbi.nlm.nih.gov/107/"],
        between(rendered, "<h2>Molecular targets", "</table>"): [
            "https://pubmed.ncbi.nlm.nih.gov/108/", "https://pubmed.ncbi.nlm.nih.gov/109/"],
        between(rendered, "<h2>Bioactivities", "</table>"): [
            "https://pubchem.ncbi.nlm.nih.gov/bioassay/110"],
        between(rendered, "<h2>Open questions", 'id="curation-history"'): [
            "https://pubmed.ncbi.nlm.nih.gov/111/"],
        between(rendered, 'id="curation-history"', "<h2>Provenance"): [
            "https://pubmed.ncbi.nlm.nih.gov/112/"],
    }
    for section, urls in expected.items():
        for url in urls:
            assert url in hrefs(section), (url, section[:60])


_ANCHOR = re.compile(r"<a\b[^>]*>.*?</a>", re.S)
_TAG = re.compile(r"<[^>]+>")
_REFERENCE_TEXT = re.compile(r"\bPMID:\s?[0-9]+|(?<![\w./])10\.[0-9]{4,9}/[^\s<]+|https?://\S+", re.I)


def test_no_committed_record_page_shows_a_reference_as_plain_text():
    plain = {}
    for path in committed_record_pages():
        main = between(path.read_text(encoding="utf-8"), "<main", "</main>")
        found = _REFERENCE_TEXT.findall(html.unescape(_TAG.sub(" ", _ANCHOR.sub(" ", main))))
        if found:
            plain[path.relative_to(PAGES).as_posix()] = found[:3]
    assert not plain, sorted(plain.items())[:10]
    anisomycin = page("alkaloids/anisomycin.html")
    assert "https://pubmed.ncbi.nlm.nih.gov/28373542/" in hrefs(anisomycin)


# ---------------------------------------------------------------------------
# curation_history: every record page lists its dated, attributed events
# ---------------------------------------------------------------------------

def test_history_is_newest_first_and_collapses_only_identical_reseeds():
    seed = {"curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
            "changes": "Seeded from the committed inventories in data/raw/."}
    doc = {"curation_history": [
        {**seed, "timestamp": "2026-09-10T05:54:08Z"},
        {**seed, "timestamp": "2026-09-25T03:02:25Z"},
        {"timestamp": "2026-09-28T11:33:44Z", "curator": "codex", "action": "RECORD_CURATED",
         "changes": "Added a graph.", "llm_assisted": True},
        {**seed, "timestamp": "2026-10-13T23:57:32Z", "changes": "Seeded from the tables."},
    ]}
    history = site.curation_history(doc)
    assert [(h["timestamp"], h["action"], h["count"]) for h in history] == [
        ("2026-10-13T23:57:32Z", "SEEDED_FROM_SOURCES", 1),
        ("2026-09-28T11:33:44Z", "RECORD_CURATED", 1),
        ("2026-09-25T03:02:25Z", "SEEDED_FROM_SOURCES", 2),
    ]
    assert history[2]["first"] == "2026-09-10T05:54:08Z"
    rendered = render_record(view({"identifier": "CHEBI:1", **doc}))
    section = between(rendered, 'id="curation-history"', "<h2>Provenance")
    assert section.count("<li>") == 3
    assert '<time datetime="2026-09-28T11:33:44Z">' in section
    assert "codex" in section and "LLM-assisted" in section
    assert "2 identical runs since 2026-09-10T05:54:08Z" in section


def test_every_committed_record_page_shows_its_curation_history(corpus):
    missing = []
    for path, doc, record in corpus:
        text = (PAGES / record["href"]).read_text(encoding="utf-8")
        section = between(text, 'id="curation-history"', "<h2>Provenance")
        events = len(doc.get("curation_history") or [])
        if not events or section.count("<li>") != len(record["history"]) or (
                f'<span class="tag">{events}</span>' not in section):
            missing.append(path.name)
    assert not missing, missing[:10]


# ---------------------------------------------------------------------------
# build_provenance: a dated corpus version, from the records, on every page
# ---------------------------------------------------------------------------

def test_corpus_as_of_is_the_latest_recorded_event_not_the_clock():
    def records(*stamps):
        return [(Path(f"{n}.yaml"), {"curation_history": [{"timestamp": s}]})
                for n, s in enumerate(stamps)]
    assert site.corpus_as_of(records("2026-10-23T22:53:34Z", "2026-09-01T00:00:00Z")) == (
        "2026-10-23 22:53 UTC")
    assert site.corpus_as_of(records("2026-09-01T00:00:00Z", "2026-10-23T22:53:34Z")) == (
        "2026-10-23 22:53 UTC")
    assert site.corpus_as_of(records("not a time")) == ""


def test_corpus_digest_moves_when_record_content_does():
    record = {"identifier": "CHEBI:1", "chemical_structure": {"standard_inchi_key": "KEY"},
              "occurrences": []}
    curated = {**record, "occurrences": [{"taxon_id": "NCBITaxon:2"}]}
    assert (site.corpus_digest([(Path("one.yaml"), record)])
            != site.corpus_digest([(Path("one.yaml"), curated)]))


def test_every_page_type_footer_states_the_corpus_date(loaded):
    stamp = site.corpus_as_of(loaded)
    assert re.fullmatch(r"20[0-9]{2}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2} UTC", stamp)
    pages = ["index.html", "browse.html", "schema.html", "404.html", "map.html",
             "chemical-map.html", "sequence-map.html", "alkaloids/index.html",
             "alkaloids/anisomycin.html"]
    for rel in pages:
        assert f"Corpus as of {stamp}." in between(page(rel), '<footer class="site">', "</footer>"), rel
    assert f"Corpus as of {stamp}." in (REPO_ROOT / "404.html").read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# schema_docs: readable documentation generated from the schema
# ---------------------------------------------------------------------------

def test_schema_page_documents_every_class_slot_and_enum_value():
    from linkml_runtime.utils.schemaview import SchemaView

    schema_view = SchemaView(str(site.SCHEMA_PATH))
    text = page("schema.html")
    for name in schema_view.all_classes():
        assert f'id="class-{name}"' in text, name
        for slot in schema_view.class_induced_slots(name):
            assert f'id="class-{name}-{slot.name}"' in text, (name, slot.name)
    for name, enum in schema_view.all_enums().items():
        section = between(text, f'id="enum-{name}"', "</section>")
        for value in enum.permissible_values or {}:
            assert f'<dt class="mono">{escape(value)}' in section, (name, value)
    for rel in ["index.html", "alkaloids/anisomycin.html", "404.html"]:
        nav = between(page(rel), '<nav aria-label="Main navigation">', "</nav>")
        assert any(h.endswith("schema.html") for h in hrefs(nav)), rel
    downloads = between(page("index.html"), 'id="downloads"', '<p class="sub">Generated')
    assert "schema.html" in hrefs(downloads)


# ---------------------------------------------------------------------------
# skip_link: the first tab stop on every page type skips to the content
# ---------------------------------------------------------------------------

class FirstFocusable(HTMLParser):
    def __init__(self):
        super().__init__()
        self.first = None
        self.ids = {}
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids[attrs["id"]] = (tag, attrs)
        if tag == "body":
            self.in_body = True
        focusable = ((tag == "a" and "href" in attrs) or tag in {"button", "input", "select",
                                                                 "textarea", "summary"}
                     or attrs.get("tabindex", "-1") != "-1")
        if self.in_body and focusable and self.first is None:
            self.first = (tag, attrs)


@pytest.mark.parametrize("rel", ["index.html", "browse.html", "alkaloids/index.html",
                                 "alkaloids/anisomycin.html", "map.html", "chemical-map.html",
                                 "sequence-map.html", "schema.html", "404.html"])
def test_first_tab_stop_skips_to_main_content(rel):
    parsed = FirstFocusable()
    parsed.feed(page(rel))
    tag, attrs = parsed.first
    assert (tag, attrs.get("href"), attrs.get("class")) == ("a", "#main-content", "skip-link")
    assert parsed.ids["main-content"][0] == "main"


# ---------------------------------------------------------------------------
# feedback_route: every record page reports a problem with that record
# ---------------------------------------------------------------------------

def test_record_page_report_route_names_the_record_and_its_page():
    record = view({"identifier": "naturalproductmech:mibig-0123456789", "np_pathway": "POLYKETIDES"},
                  "polyketides/example.yaml")
    url = urlsplit(record["issue_url"])
    assert (url.netloc, url.path) == ("github.com", "/CultureBotAI/NaturalProductMech/issues/new")
    assert parse_qs(url.query) == {
        "title": ["Problem with naturalproductmech:mibig-0123456789"],
        "body": ["https://culturebotai.github.io/NaturalProductMech/pages/polyketides/example.html"]}
    for path in committed_record_pages()[:50]:
        actions = between(path.read_text(encoding="utf-8"), '<p class="record-actions">', "</p>")
        report = urlsplit(hrefs(actions)[0])
        assert parse_qs(report.query)["body"] == [
            site.SITE_BASE + path.relative_to(PAGES).as_posix()], path.name


# ---------------------------------------------------------------------------
# visual_alternative and text_map: every map has a table; the text map says
# what it leaves out
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rel, prefix", [("map.html", "corpus-map"), ("chemical-map.html", "map"),
                                         ("sequence-map.html", "seq")])
def test_every_map_has_a_lazily_filled_table_alternative(rel, prefix):
    text = page(rel)
    table = between(text, f'<details class="map-table" id="{prefix}-table">', "</details>")
    assert "<summary>View data as table</summary>" in table
    assert f'<tbody id="{prefix}-table-body"></tbody>' in table
    assert 'role="region" tabindex="0" aria-label="' in table
    script = text if rel != "chemical-map.html" else page("chemical-map.js")
    assert f'getElementById("{prefix}-table-body")' in script
    assert 'addEventListener("toggle", renderTable)' in script
    assert "<noscript>" in text


def test_text_map_names_every_record_it_leaves_out(loaded):
    import json

    artifact = json.loads((REPO_ROOT / "data/embeddings/corpus_map.json").read_text())
    records = {doc["identifier"]: site.record_href(doc, path) for path, doc in loaded}
    plotted = {point[3] for point in artifact["points"] if point[3] in records}
    coverage = between(page("map.html"), 'id="map-coverage"', "</p>")
    assert f"{len(plotted)} of the {len(records)} published records are plotted." in coverage
    missing = sorted(set(records) - plotted)
    assert missing, "the gap this test was written for has closed; keep the test, drop this line"
    for identifier in missing:
        assert identifier in coverage and records[identifier] in hrefs(coverage), identifier
    dropped = sum(1 for point in artifact["points"] if point[3] not in records)
    assert f"{dropped} point" in coverage


# ---------------------------------------------------------------------------
# curation_notice: how records are produced, in the repository's own words
# ---------------------------------------------------------------------------

def test_landing_says_how_records_are_produced_in_the_repositorys_words(loaded):
    readme = " ".join((REPO_ROOT / "README.md").read_text(encoding="utf-8").split())
    assert " ".join(site.PRODUCTION_QUOTE.split()) in readme
    landing = page("index.html")
    notice = between(landing, 'id="curation"', "<h2>What the corpus holds")
    quoted = html.unescape(re.sub(r"<[^>]+>", "", between(notice, "<blockquote", "</blockquote>")))
    assert " ".join(site.PRODUCTION_QUOTE.replace("`", "").split()) in " ".join(quoted.split())
    statuses = site.enum_values(site.schema_reference(), "CurationStatusEnum")
    counts = {}
    for _path, doc in loaded:
        counts[doc.get("curation_status")] = counts.get(doc.get("curation_status"), 0) + 1
    for status in statuses:
        row = (f'<tr><td class="mono">{status["text"]}</td><td>{counts.get(status["text"], 0)}</td>'
               f'<td>{escape(status["description"])}</td></tr>')
        assert row in notice, status["text"]
    # Never a claim of human review the records' history does not show.
    assert re.findall(r"[^.]*\bhuman\b[^.]*", html.unescape(re.sub(r"<[^>]+>", "", notice))) == [
        "\nThese are workflow decisions, not independently verified human review"]
    assert "seed_from_sources" in notice and "llm_assisted" in notice


def test_record_page_quotes_the_schema_meaning_of_its_status():
    meanings = {"SEEDED": "Written from the committed inventories; no curator sign-off yet."}
    rendered = render_record(view({"identifier": "CHEBI:1", "curation_status": "SEEDED"}),
                             status_meanings=meanings)
    legend = between(rendered, '<details class="status-legend">', "</details>")
    assert ("This record is <strong>SEEDED</strong>: “Written from the committed inventories; "
            "no curator sign-off yet.”") in legend
    assert "../schema.html#enum-CurationStatusEnum" in hrefs(legend)


# ---------------------------------------------------------------------------
# discussions: open questions carry their status
# ---------------------------------------------------------------------------

def test_open_questions_show_their_status():
    rendered = render_record(view({"identifier": "CHEBI:1", "discussions": [
        {"discussion_id": "curator-open", "kind": "CURATION_TODO", "status": "OPEN",
         "prompt": "Which producer?"},
        {"discussion_id": "settled", "status": "RESOLVED", "prompt": "Old question"}]}))
    section = between(rendered, "<h2>Open questions", 'id="curation-history"')
    assert '<strong>curator-open</strong> <span class="tag">OPEN</span>' in section
    assert "curation todo" in section and "settled" not in section


# ---------------------------------------------------------------------------
# responsive: nothing forces a phone-width page to scroll sideways
# ---------------------------------------------------------------------------

def test_sibling_tags_wrap_and_wide_tables_scroll_inside_named_regions():
    css = (site.TEMPLATES_DIR / "style.css").read_text(encoding="utf-8")
    rule = between(css, ".cross-mech-links a.tag {", "}")
    assert "white-space: normal;" in rule and "overflow-wrap: anywhere;" in rule
    # A bare 1fr column grows to its widest content: an opened table then
    # widens the page at 390 px instead of scrolling inside its region.
    assert not re.search(r"grid-template-columns:\s*1fr\b", css)
    for rel in ["index.html", "alkaloids/index.html", "alkaloids/anisomycin.html",
                "polyketides/daunorubicin.html", "schema.html", "map.html"]:
        text = page(rel)
        regions = re.findall(r'<div class="scroll"[^>]*>', text)
        assert regions, rel
        for region in regions:
            assert re.fullmatch(r'<div class="scroll" role="region" tabindex="0" aria-label="[^"]+">',
                                region), (rel, region)
        assert 'height="auto"' not in text, rel


def test_landing_search_promises_only_what_browse_searches():
    placeholder = re.search(r'class="hero-search".*?placeholder="([^"]*)"', page("index.html"), re.S)
    assert placeholder and "producer" not in placeholder.group(1).lower()
