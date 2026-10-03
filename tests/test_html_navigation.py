"""Navigation and literal complete-corpus browser input contracts."""
from html.parser import HTMLParser
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from scripts.render_pages import build_record

ROOT = Path(__file__).resolve().parents[1]


class Elements(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def test_browse_keeps_searchable_identifiers_synonyms_and_all_links():
    env = Environment(loader=FileSystemLoader(ROOT / "src/naturalproductmech/templates"),
                      autoescape=select_autoescape(["html"]))
    record = build_record(ROOT / "data/natural_products/alkaloids/example.yaml", {
        "identifier": "CHEBI:42", "label": '<script>alert("x")</script>',
        "synonyms": [{"value": "Rare alias"}], "np_pathway": "ALKALOIDS"})
    rendered = env.get_template("browse.html").render(root="", total=1, pathways=[{
        "title": "Alkaloids", "slug": "alkaloids", "count": 1, "records": [record]}])
    parsed = Elements()
    parsed.feed(rendered)
    search = next(attrs for tag, attrs in parsed.elements if tag == "li" and "data-search" in attrs)
    assert 'CHEBI:42 Rare alias Alkaloids' in search["data-search"]
    assert '<script>alert("x")</script>' in search["data-search"]
    assert '<script>alert("x")</script>' not in rendered
    assert any(attrs.get("href") == "alkaloids/example.html" for _, attrs in parsed.elements)
    assert any(tag == "input" and attrs.get("id") == "browse-query" for tag, attrs in parsed.elements)
    assert any(attrs.get("role") == "status" for _, attrs in parsed.elements)


def test_chemical_map_has_one_main_and_source_records_link_to_yaml():
    pages = ROOT / "pages"
    parsed = Elements()
    parsed.feed((pages / "chemical-map.html").read_text())
    assert sum(tag == "main" for tag, _ in parsed.elements) == 1
    assert any(attrs.get("href") == "https://culturebotai.github.io/mechs/" for _, attrs in parsed.elements)
    record = Elements()
    record.feed((pages / "alkaloids/anisomycin.html").read_text())
    expected = "https://github.com/CultureBotAI/NaturalProductMech/blob/main/data/natural_products/alkaloids/anisomycin.yaml"
    assert any(attrs.get("href") == expected for _, attrs in record.elements)
