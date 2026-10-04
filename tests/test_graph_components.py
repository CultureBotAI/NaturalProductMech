"""Components must preserve biology and fail closed across corpus consumers."""

import importlib.util
import sys
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from naturalproductmech.curate.curation_event import record_curation_event
from naturalproductmech.graph_components import (
    GraphComponentError,
    audit_graph_components,
    component_path,
    read_natural_product,
    resolve_graphs,
    write_validated_graph_bundle,
)
from naturalproductmech.validation.write_validated import (
    ValidationFailedError,
    emit_natural_product_yaml,
    write_validated_natural_product,
)

ROOT = Path(__file__).resolve().parents[1]


def script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def event(doc, changes="Test component curation"):
    record_curation_event(
        doc, curator="test", action="RECORD_CURATED", changes=changes, timestamp="2026-10-04T00:00:00Z"
    )


@pytest.fixture
def bundle(tmp_path, minimal_record):
    path = tmp_path / "data/natural_products/polyketides/test.yaml"
    owner = deepcopy(minimal_record)
    owner["causal_graph_refs"] = ["test-graph"]
    graph = {
        "graph_id": "test-graph",
        "scope": "BIOSYNTHESIS",
        "description": "Partial pathway",
        "nodes": [
            {"node_id": "enzyme", "label": "enzyme", "identifier": "NCBIProtein:AAA00001.1"},
            {"node_id": "product", "label": owner["label"]},
        ],
        "edges": [
            {
                "subject": "enzyme",
                "predicate": "affects",
                "object": "product",
                "notes": "Genetic evidence, not purified catalysis.",
                "evidence": [
                    {
                        "reference": "https://example.org/primary",
                        "evidence_type": "PRIMARY_EXPERIMENT",
                        "snippet": "example",
                    }
                ],
            }
        ],
    }
    doc = {
        "record_id": owner["identifier"],
        "standard_inchi_key": owner["chemical_structure"]["standard_inchi_key"],
        "graph": graph,
    }
    event(owner)
    event(doc)
    return path, owner, doc


def test_roundtrip_preserves_graphs_and_rejects_flattened_writes(bundle):
    path, owner, doc = bundle
    write_validated_graph_bundle(owner, path, [doc])
    graph_path = component_path(owner, path, "test-graph")
    original = (path.read_bytes(), graph_path.read_bytes())
    view = read_natural_product(path)
    assert view["causal_graphs"] == [doc["graph"]]
    assert view["causal_graph_refs"] == owner["causal_graph_refs"]
    assert "causal_graphs" not in owner
    assert audit_graph_components(path.parent.parent) == [graph_path]
    write_validated_graph_bundle(owner, path, [doc])
    assert original == (path.read_bytes(), graph_path.read_bytes())
    with pytest.raises(GraphComponentError, match="duplicate graph"):
        write_validated_natural_product(view, path)
    assert original == (path.read_bytes(), graph_path.read_bytes())


@pytest.mark.parametrize(
    "change",
    [
        "wrong_owner",
        "wrong_key",
        "wrong_id",
        "unknown_field",
        "no_history",
        "duplicate_node",
        "missing_node",
        "dangling_edge",
        "empty_evidence",
        "blank_reference",
        "oversize",
    ],
)
def test_invalid_component_never_writes(bundle, change):
    path, owner, doc = bundle
    if change == "wrong_owner":
        doc["record_id"] = "CHEBI:1"
    elif change == "wrong_key":
        doc["standard_inchi_key"] = "AAAAAAAAAAAAAA-BBBBBBBBBB-C"
    elif change == "wrong_id":
        doc["graph"]["graph_id"] = "wrong"
    elif change == "unknown_field":
        doc["graph"]["protein"] = "unknown"
    elif change == "no_history":
        doc["curation_history"] = []
    elif change == "duplicate_node":
        doc["graph"]["nodes"].append(doc["graph"]["nodes"][0])
    elif change == "missing_node":
        doc["graph"]["nodes"][0]["node_id"] = ""
    elif change == "dangling_edge":
        doc["graph"]["edges"][0]["subject"] = "absent"
    elif change == "empty_evidence":
        doc["graph"]["edges"][0]["evidence"] = []
    elif change == "blank_reference":
        doc["graph"]["edges"][0]["evidence"][0]["reference"] = " "
    elif change == "oversize":
        doc["graph"]["description"] = "x" * (64 * 1024)
    with pytest.raises((GraphComponentError, ValidationFailedError)):
        write_validated_graph_bundle(owner, path, [doc])
    assert not list(path.parents[3].rglob("*.yaml"))


@pytest.mark.parametrize("ref", ["../escape", "/absolute", "a/b", "a\\b", "..", "", "a.yaml", "a" * 201])
def test_unsafe_reference(bundle, ref):
    path, owner, _ = bundle
    owner["causal_graph_refs"] = [ref]
    with pytest.raises(GraphComponentError, match="unsafe"):
        resolve_graphs(owner, path)


def test_missing_duplicate_and_orphan_references(bundle):
    path, owner, doc = bundle
    with pytest.raises(GraphComponentError, match="cannot read"):
        write_validated_natural_product(owner, path)
    owner["causal_graph_refs"].append("test-graph")
    with pytest.raises(GraphComponentError, match="duplicate"):
        resolve_graphs(owner, path)
    owner["causal_graph_refs"].pop()
    write_validated_graph_bundle(owner, path, [doc])
    extra = component_path(owner, path, "orphan")
    extra.write_text(emit_natural_product_yaml(doc))
    with pytest.raises(GraphComponentError, match="unreferenced"):
        audit_graph_components(path.parent.parent)


def test_case_colliding_refs_and_detachment_are_rejected(bundle):
    path, owner, doc = bundle
    owner["causal_graph_refs"].append("TEST-graph")
    with pytest.raises(GraphComponentError, match="duplicate"):
        resolve_graphs(owner, path)
    owner["causal_graph_refs"].pop()
    write_validated_graph_bundle(owner, path, [doc])
    owner.pop("causal_graph_refs")
    event(owner)
    with pytest.raises(GraphComponentError, match="detaching"):
        write_validated_natural_product(owner, path)


@pytest.mark.parametrize("refs", [False, 0, {}, "", [1]])
def test_malformed_reference_container_cannot_silently_hide_graphs(bundle, refs):
    path, owner, _ = bundle
    owner["causal_graph_refs"] = refs
    with pytest.raises(GraphComponentError, match="must be a list"):
        resolve_graphs(owner, path)


def test_component_root_must_be_a_directory(tmp_path):
    (tmp_path / "causal_graphs").write_text("not a component directory")
    with pytest.raises(GraphComponentError, match="not a directory"):
        audit_graph_components(tmp_path / "natural_products")


def test_component_only_changes_trigger_main_label_checks():
    from fnmatch import fnmatchcase

    workflow = yaml.safe_load((ROOT / ".github/workflows/label-correspondence.yaml").read_text())
    triggers = workflow.get("on", workflow.get(True))
    path = "data/causal_graphs/AAAAAAAAAAAAAA-BBBBBBBBBB-C/graph.yaml"
    assert any(fnmatchcase(path, pattern) for pattern in triggers["push"]["paths"])


@pytest.mark.parametrize("level", ["root", "directory", "file"])
def test_symlink_components_are_rejected(bundle, tmp_path, level):
    path, owner, _ = bundle
    target = tmp_path / "elsewhere"
    target.mkdir()
    graph_path = component_path(owner, path, "test-graph")
    link = {"file": graph_path, "directory": graph_path.parent, "root": graph_path.parent.parent}[level]
    link.parent.mkdir(parents=True, exist_ok=True)
    link.symlink_to(target, target_is_directory=True)
    with pytest.raises(GraphComponentError, match="symlink"):
        resolve_graphs(owner, path)


def test_changed_component_requires_append_only_history(bundle):
    path, owner, doc = bundle
    write_validated_graph_bundle(owner, path, [doc])
    doc["graph"]["description"] = "Revised interpretation"
    with pytest.raises(GraphComponentError, match="appended curation event"):
        write_validated_graph_bundle(owner, path, [doc])
    event(doc)
    write_validated_graph_bundle(owner, path, [doc])
    assert read_natural_product(path)["causal_graphs"][0] == doc["graph"]


def test_write_failure_restores_all_artifacts(bundle, monkeypatch):
    path, owner, doc = bundle
    from naturalproductmech.validation import write_validated

    real_write = write_validated.write_validated_natural_product

    def fail_owner(document, target, **kwargs):
        if target == path:
            raise OSError("test disk failure")
        real_write(document, target, **kwargs)

    monkeypatch.setattr(write_validated, "write_validated_natural_product", fail_owner)
    with pytest.raises(OSError, match="test disk failure"):
        write_validated_graph_bundle(owner, path, [doc])
    assert not list(path.parents[3].rglob("*.yaml"))


def test_reseed_preserves_refs_component_bytes_and_raw_view(bundle):
    path, owner, doc = bundle
    write_validated_graph_bundle(owner, path, [doc])
    graph_path = component_path(owner, path, "test-graph")
    before = graph_path.read_bytes()
    seed = script("seed_from_sources")
    payload = {k: v for k, v in owner.items() if k not in ("causal_graph_refs", "curation_history")}
    seed.carry_existing_curator_owned_fields(payload, path)
    assert emit_natural_product_yaml(payload) == path.read_text()
    write_validated_natural_product(payload, path)
    assert "causal_graphs" not in seed.read_record(path)
    assert graph_path.read_bytes() == before
    payload["chemical_structure"] = {"standard_inchi_key": "AAAAAAAAAAAAAA-BBBBBBBBBB-C"}
    payload.pop("causal_graph_refs")
    seed.carry_curator_owned_fields(payload, owner)
    assert "causal_graph_refs" not in payload


def test_consumers_see_complete_mechanism_and_labels(bundle, monkeypatch):
    path, owner, doc = bundle
    write_validated_graph_bundle(owner, path, [doc])
    corpus = path.parent.parent
    report = script("np_report")
    assert report.summarize(report.load_records(corpus))["field_coverage"]["causal_graphs"] == 1
    for name in ("render_pages", "curation_worklist"):
        consumer = script(name)
        monkeypatch.setattr(consumer, "CORPUS_DIR", corpus)
        assert consumer.load_records()[0][1]["causal_graphs"] == [doc["graph"]]
    labels = script("validate_id_label_correspondence")
    cfg = labels.load_config(ROOT / "conf/id_label_targets.yaml")
    target = next(t for t in cfg["targets"] if t["name"] == "graph_component_nodes")
    matches = list(path.parents[3].glob(target["glob"]))
    assert len(matches) == 1
    pairs = list(labels.iter_yaml(matches[0], target["pairs"]))
    assert any(p[1:3] == ("NCBIProtein:AAA00001.1", "enzyme") for p in pairs)
    strict = script("validate_strict")
    assert strict.validate_one(path) == []
    assert strict.validate_one(matches[0]) == []
    matches[0].unlink()
    assert strict.validate_one(path)[0]["category"] == "graph_integrity"


def test_committed_components_are_complete_reviewable_and_canonical():
    for path in audit_graph_components(ROOT / "data/natural_products"):
        doc = yaml.safe_load(path.read_text())
        assert emit_natural_product_yaml(doc).encode() == path.read_bytes()
