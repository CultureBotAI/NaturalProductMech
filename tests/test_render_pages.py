from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "render_pages",
    REPO_ROOT / "scripts" / "render_pages.py",
)
assert _spec and _spec.loader
render_pages = importlib.util.module_from_spec(_spec)
sys.modules["render_pages"] = render_pages
_spec.loader.exec_module(render_pages)


def test_causal_graph_rendering_preserves_every_edge_reference():
    record = render_pages.build_record(
        REPO_ROOT / "data" / "natural_products" / "carbohydrates" / "tubercidin.yaml",
        {
            "identifier": "CHEBI:1",
            "np_pathway": "CARBOHYDRATES",
            "causal_graphs": [
                {
                    "scope": "BIOACTIVITY",
                    "nodes": [
                        {"node_id": "compound", "label": "compound"},
                        {"node_id": "target", "label": "target"},
                    ],
                    "edges": [
                        {
                            "subject": "compound",
                            "predicate": "binds",
                            "object": "target",
                            "notes": "Binding is structural; cytotoxicity is downstream.",
                            "evidence": [
                                {"reference": "DOI:10.1/primary"},
                                {"reference": "DOI:10.2/structure"},
                            ],
                        },
                    ],
                },
            ],
        },
    )

    assert record["graphs"][0]["edges"][0]["references"] == [
        "DOI:10.1/primary",
        "DOI:10.2/structure",
    ]

    env = Environment(
        loader=FileSystemLoader(str(render_pages.TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    rendered = env.get_template("record.html").render(r=record)

    assert "DOI:10.1/primary<br>DOI:10.2/structure" in rendered
    assert "Binding is structural; cytotoxicity is downstream." in rendered


def test_pathway_step_without_grounded_compounds_renders_as_ungrounded():
    record = render_pages.build_record(
        REPO_ROOT / "data" / "natural_products" / "carbohydrates" / "coformycin.yaml",
        {
            "identifier": "CHEBI:16213",
            "np_pathway": "CARBOHYDRATES",
            "biosynthetic_pathway": [
                {
                    "step_number": 1,
                    "enzyme_label": "CofB",
                    "evidence": [{"reference": "DOI:10.1073/pnas.2000111117"}],
                },
            ],
        },
    )

    env = Environment(
        loader=FileSystemLoader(str(render_pages.TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    rendered = env.get_template("record.html").render(r=record)

    assert "ungrounded &rarr; ungrounded" in rendered


def test_pathway_step_without_step_number_renders_as_entry():
    record = render_pages.build_record(
        REPO_ROOT / "data" / "natural_products" / "carbohydrates" / "coformycin.yaml",
        {
            "identifier": "CHEBI:16213",
            "np_pathway": "CARBOHYDRATES",
            "biosynthetic_pathway": [
                {
                    "enzyme_label": "CofB",
                    "notes": "Exact chemistry is unresolved.",
                    "evidence": [{"reference": "DOI:10.1073/pnas.2000111117"}],
                },
            ],
        },
    )

    env = Environment(
        loader=FileSystemLoader(str(render_pages.TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    rendered = env.get_template("record.html").render(r=record)

    assert "<tr><th>#</th>" in rendered
    assert "<td>1</td>" in rendered
    assert "Entry 1: Exact chemistry is unresolved." in rendered
    assert "Step : Exact chemistry is unresolved." not in rendered
