from __future__ import annotations

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

import pytest
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


def shown(value):
    """A source value as a record page shows it: a URL links itself, the rest is text."""
    text = escape(value)
    return f'<a href="{text}">{text}</a>' if value.startswith("https://") else str(text)


@pytest.mark.parametrize("fields, expected", [
    ({"measurement_type": "IC50", "value": 2.5, "units": "uM", "call": "ACTIVE"},
     "IC50 2.5 uM; ACTIVE"),
    ({"measurement_type": "OTHER", "value": 0, "units": "uM", "call": "INACTIVE"},
     "OTHER 0 uM; INACTIVE"),
    ({"measurement_type": "OTHER", "value": 0.3663, "units": "uM", "call": "NOT_DETERMINED"},
     "OTHER 0.3663 uM; NOT_DETERMINED"),
    ({"call": "ACTIVE"}, "ACTIVE"),
    ({"measurement_type": "IC50", "value": 2.5, "units": "uM"}, "IC50 2.5 uM"),
])
def test_bioactivity_result_preserves_both_measurement_and_call(fields, expected):
    observation = {
        "assay": "Synthetic assay", **fields,
        "evidence": [{"reference": "pubchem.aid:1", "notes": "Source endpoint: Potency."}],
    }
    record = render_pages.build_record(REPO_ROOT / "data/natural_products/test.yaml", {
        "identifier": "CHEBI:1", "np_pathway": "POLYKETIDES",
        "bioactivities": [observation],
    })
    assert record["bioactivities"][0]["result"] == expected
    assert record["bioactivities"][0]["source"] == observation
    env = render_pages.template_environment()
    rendered = env.get_template("record.html").render(r=record)
    assert expected in rendered
    assert "Source endpoint: Potency." in rendered


def test_text_map_never_retags_an_obsolete_identity():
    artifact = {"n": 2, "points": [[1, 2, 0, "old", "a"], [3, 4, 0, "live", "b"]],
                "corpus_fingerprint": "original"}
    joined = render_pages.join_text_map(artifact, {"new": "a.html", "live": "b.html"})
    assert joined["points"] == [[3, 4, 0, "live", "b"]]
    assert joined["hrefs"] == {"live": "b.html"} and joined["n"] == 1
    assert joined["corpus_fingerprint"] == "original"
    assert artifact["n"] == len(artifact["points"]) == 2
    assert render_pages.join_text_map(artifact, {})["n"] == 0


@pytest.mark.parametrize("strain", [None, "S4059", '<script>alert("strain")</script>'])
def test_producer_strain_is_visible_and_evidence_is_retained(strain):
    producer = {
        "taxon_id": "NCBITaxon:43658", "taxon_label": "Pseudoalteromonas rubra",
        "evidence_basis": "BGC_CHARACTERIZED", "biosynthetic_gene_cluster": "mibig:BGC0002675",
        "evidence": [{"reference": "DOI:10.1/paper", "evidence_type": "DATABASE_ASSERTION"},
                     {"reference": "DOI:10.1/paper", "evidence_type": "CURATOR_INFERENCE",
                      "notes": "Exact strain context, not a species-wide experiment."}],
    }
    if strain is not None:
        producer["strain"] = strain
    original = deepcopy(producer)
    view = render_pages.build_record(REPO_ROOT / "data/natural_products/test.yaml", {
        "identifier": "CHEBI:1", "np_pathway": "ALKALOIDS", "producer_organisms": [producer],
    })
    assert producer == original
    assert view["producers"][0]["evidence"] == original["evidence"]
    assert view["producers"][0]["references"] == ["DOI:10.1/paper"]
    env = render_pages.template_environment()
    rendered = env.get_template("record.html").render(r=view)
    assert rendered.count('<span class="mono">DOI:10.1/paper</span>') == 1
    assert '<script>alert("strain")</script>' not in rendered
    if strain is None:
        assert "Strain:" not in rendered
    else:
        assert f"Strain: {escape(strain)}" in rendered
        assert "Exact strain context, not a species-wide experiment." in rendered


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

    env = render_pages.template_environment()
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
    env = render_pages.template_environment()
    rendered = env.get_template("record.html").render(r=view)
    assert graph["description"] in rendered
    assert graph["edges"][0]["notes"] in rendered
    # The citations sit beside the disclosure, not inside its <summary>, so a
    # reference link is never nested in the control that opens the detail.
    references = "<br>".join(shown(item["reference"]) for item in evidence)
    assert '<details class="graph-evidence">' in rendered
    assert (f'<span class="mono">{references}</span><details class="graph-evidence">'
            '<summary>Evidence detail</summary>') in rendered
    for item in evidence:
        for key, value in item.items():
            assert f"<dt>{key.replace('_', ' ')}</dt>" in rendered
            assert f"<dd>{shown(value)}</dd>" in rendered
    if detailed:
        assert "<script>" not in rendered
        assert rendered.index("PRIMARY_EXPERIMENT") < rendered.index("CURATOR_INFERENCE")
        assert rendered.index("CURATOR_INFERENCE") < rendered.index("DATABASE_ASSERTION")
        assert rendered.count("<dd>DOI:10.1/synthetic</dd>") == 2
    else:
        assert "<dt>evidence type</dt>" not in rendered
        assert "<dt>snippet</dt>" not in rendered
    assert {p: p.read_bytes() for p in tmp_path.rglob("*.yaml")} == before


@pytest.mark.parametrize("source", ["CURATOR", "BINDINGDB"])
@pytest.mark.parametrize("detailed", [False, True])
def test_target_qualifications_and_all_evidence_reach_html(source, detailed):
    evidence = [{"reference": "DOI:10.1/synthetic"}]
    if detailed:
        evidence[0].update(evidence_type="PRIMARY_EXPERIMENT",
                           notes="Abstract only; no strain-specific assay.",
                           snippet='Synthetic <quoted> evidence & context.')
        evidence.append({"reference": "https://example.org/structure?a=1&b=2",
                         "evidence_type": "DATABASE_ASSERTION",
                         "notes": "Processed tagged construct, not the precursor."})
    target = {"target_label": "Synthetic proteasome complex", "target_type": "PROTEIN_COMPLEX",
              "relation": "INHIBITS", "source": source,
              "protein_examples": ["UniProtKB:P12345"],
              "notes": 'Deliberate reference only <script>alert("test")</script>.',
              "evidence": evidence}
    doc = {"identifier": "CHEBI:1", "np_pathway": "POLYKETIDES", "molecular_targets": [target]}
    before = deepcopy(doc)
    view = render_pages.build_record(REPO_ROOT / "data/natural_products/polyketides/synthetic.yaml", doc)
    env = render_pages.template_environment()
    rendered = env.get_template("record.html").render(r=view)
    assert str(escape(target["notes"])) in rendered
    assert "PROTEIN_COMPLEX" in rendered and "INHIBITS" in rendered
    assert "UniProtKB:P12345" in rendered
    assert '<details class="graph-evidence target-evidence">' in rendered
    assert "<script>" not in rendered
    for item in evidence:
        for key, value in item.items():
            assert f"<dt>{key.replace('_', ' ')}</dt>" in rendered
            assert f"<dd>{shown(value)}</dd>" in rendered
    assert doc == before


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

    env = render_pages.template_environment()
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

    env = render_pages.template_environment()
    rendered = env.get_template("record.html").render(r=record)

    assert "<tr><th>#</th>" in rendered
    assert "<td>1</td>" in rendered
    assert "Entry 1: Exact chemistry is unresolved." in rendered
    assert "Step : Exact chemistry is unresolved." not in rendered
