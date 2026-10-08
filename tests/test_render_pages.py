from __future__ import annotations

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import escape

from naturalproductmech.curate.curation_event import record_curation_event
from naturalproductmech.graph_components import write_validated_graph_bundle
from naturalproductmech.validation.write_validated import write_validated_natural_product

REPO_ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "render_pages",
    REPO_ROOT / "scripts" / "render_pages.py",
)
assert _spec and _spec.loader
render_pages = importlib.util.module_from_spec(_spec)
sys.modules["render_pages"] = render_pages
_spec.loader.exec_module(render_pages)


def test_text_map_never_retags_an_obsolete_identity():
    artifact = {"n": 2, "points": [[1, 2, 0, "old", "a"], [3, 4, 0, "live", "b"]],
                "corpus_fingerprint": "original"}
    joined = render_pages.join_text_map(artifact, {"new": "a.html", "live": "b.html"})
    assert joined["points"] == [[3, 4, 0, "live", "b"]]
    assert joined["hrefs"] == {"live": "b.html"} and joined["n"] == 1
    assert joined["corpus_fingerprint"] == "original"
    assert artifact["n"] == len(artifact["points"]) == 2
    assert render_pages.join_text_map(artifact, {})["n"] == 0


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


@pytest.mark.parametrize("storage", ["inline", "component"])
@pytest.mark.parametrize("detailed", [False, True])
def test_graph_evidence_details_reach_html_without_changing_sources(
    tmp_path, monkeypatch, minimal_record, storage, detailed,
):
    evidence = [{"reference": "DOI:10.1/synthetic"}]
    if detailed:
        evidence[0].update({
            "evidence_type": "PRIMARY_EXPERIMENT",
            "retrieved_on": "2026-10-08",
            "notes": 'Synthetic assay qualifier <script>alert("test")</script> & context.',
            "snippet": 'Synthetic exact "quotation" < 5 & > 1.',
        })
        evidence.extend([
            {"reference": "DOI:10.1/synthetic", "evidence_type": "CURATOR_INFERENCE",
             "notes": "Same citation, distinct inferred claim."},
            {"reference": "https://example.org/database?one=1&two=2", "evidence_type": "DATABASE_ASSERTION",
             "notes": "Database version 7, not a new experiment."},
        ])
    graph = {
        "graph_id": "synthetic-evidence", "scope": "BIOSYNTHESIS",
        "description": "Synthetic partial mechanism for presentation testing.",
        "nodes": [{"node_id": "a", "label": "precursor"}, {"node_id": "b", "label": "product"}],
        "edges": [{"subject": "a", "predicate": "affects", "object": "b",
                   "notes": "Synthetic edge-level qualification.", "evidence": evidence}],
    }
    owner = deepcopy(minimal_record)
    path = tmp_path / "data/natural_products/polyketides/synthetic.yaml"
    if storage == "inline":
        owner["causal_graphs"] = [graph]
    else:
        owner["causal_graph_refs"] = [graph["graph_id"]]
    record_curation_event(owner, curator="test", action="RECORD_CURATED", changes="Synthetic test")
    if storage == "inline":
        write_validated_natural_product(owner, path)
    else:
        component = {"record_id": owner["identifier"],
                     "standard_inchi_key": owner["chemical_structure"]["standard_inchi_key"],
                     "graph": graph}
        record_curation_event(component, curator="test", action="RECORD_CURATED", changes="Synthetic test")
        write_validated_graph_bundle(owner, path, [component])
    before = {p: p.read_bytes() for p in tmp_path.rglob("*.yaml")}
    monkeypatch.setattr(render_pages, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(render_pages, "CORPUS_DIR", path.parent.parent)
    (loaded_path, loaded), = render_pages.load_records()
    view = render_pages.build_record(loaded_path, loaded)
    assert view["graphs"][0]["edges"][0]["evidence"] == evidence
    env = Environment(loader=FileSystemLoader(str(render_pages.TEMPLATES_DIR)),
                      autoescape=select_autoescape(["html"]))
    rendered = env.get_template("record.html").render(r=view)
    assert graph["description"] in rendered
    assert graph["edges"][0]["notes"] in rendered
    references = "<br>".join(str(escape(item["reference"])) for item in evidence)
    assert '<details class="graph-evidence">' in rendered
    assert f'<summary class="mono">{references}</summary>' in rendered
    for item in evidence:
        for key, value in item.items():
            assert f"<dt>{key.replace('_', ' ')}</dt>" in rendered
            assert f"<dd>{escape(value)}</dd>" in rendered
    if detailed:
        assert "<script>" not in rendered
        assert rendered.index("PRIMARY_EXPERIMENT") < rendered.index("CURATOR_INFERENCE")
        assert rendered.index("CURATOR_INFERENCE") < rendered.index("DATABASE_ASSERTION")
        assert rendered.count("<dd>DOI:10.1/synthetic</dd>") == 2
    else:
        assert "<dt>evidence type</dt>" not in rendered
        assert "<dt>snippet</dt>" not in rendered
    assert {p: p.read_bytes() for p in tmp_path.rglob("*.yaml")} == before


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
