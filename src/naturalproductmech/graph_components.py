"""Exact-owner graph components and a read-only, complete mechanism view.

Mutation callers load raw YAML. Analysis callers use ``read_natural_product``;
its expanded view retains refs so a guarded writer rejects accidental flattening.
"""

from __future__ import annotations

import re
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from naturalproductmech.validation.write_validated import (
    ValidationFailedError,
    emit_natural_product_yaml,
    validate_natural_product,
)

MAX_ARTIFACT_BYTES = 64 * 1024
GRAPH_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,199}\Z")
INCHI_KEY = re.compile(r"[A-Z]{14}-[A-Z]{10}-[A-Z]\Z")


class GraphComponentError(ValueError):
    """A mechanism is incomplete, ambiguously owned, or unsafe to read/write."""


def check_size(content: str | bytes, path: Path) -> None:
    size = len(content.encode("utf-8") if isinstance(content, str) else content)
    if size > MAX_ARTIFACT_BYTES:
        raise GraphComponentError(f"{path}: {size} bytes exceeds 64-KiB artifact limit")


def graph_root(record_path: Path) -> Path:
    if record_path.parent.parent.name != "natural_products":
        raise GraphComponentError(f"noncanonical owner path: {record_path}")
    return record_path.parent.parent.parent / "causal_graphs"


def _no_symlinks(path: Path, stop: Path) -> None:
    for part in (path, *path.parents):
        if part.is_symlink():
            raise GraphComponentError(f"symlink is not a graph artifact path: {part}")
        if part == stop:
            break


def component_path(owner: dict, record_path: Path, graph_id: str) -> Path:
    key = (owner.get("chemical_structure") or {}).get("standard_inchi_key")
    if not isinstance(key, str) or not INCHI_KEY.fullmatch(key):
        raise GraphComponentError("graph owner requires a Standard InChIKey")
    if not isinstance(graph_id, str) or not GRAPH_ID.fullmatch(graph_id):
        raise GraphComponentError(f"unsafe graph reference: {graph_id!r}")
    root = graph_root(record_path)
    path = root / key / f"{graph_id}.yaml"
    _no_symlinks(path, root.parent)
    _no_symlinks(record_path, root.parent)
    return path


def validate_graphs(graphs: list[dict]) -> None:
    """Topology checks that LinkML's object shape alone cannot express."""
    seen = set()
    for graph in graphs:
        graph_id = graph.get("graph_id")
        if not isinstance(graph_id, str) or not graph_id.strip() or graph_id in seen:
            raise GraphComponentError(f"missing or duplicate graph ID: {graph_id!r}")
        seen.add(graph_id)
        nodes = [n.get("node_id") for n in graph.get("nodes") or []]
        if any(not isinstance(n, str) or not n.strip() for n in nodes) or len(nodes) != len(set(nodes)):
            raise GraphComponentError(f"{graph_id}: missing or duplicate node ID")
        for edge in graph.get("edges") or []:
            if edge.get("subject") not in nodes or edge.get("object") not in nodes:
                raise GraphComponentError(f"{graph_id}: dangling edge {edge!r}")
            if not edge.get("evidence") or any(
                not isinstance(e.get("reference"), str) or not e["reference"].strip()
                for e in edge["evidence"]
            ):
                raise GraphComponentError(f"{graph_id}: uncited edge")


def validate_component(doc: dict, owner: dict, path: Path, graph_id: str) -> None:
    errors = validate_natural_product(doc, target_class="CausalGraphDocument")
    if errors:
        raise ValidationFailedError(path, errors)
    if (
        doc["record_id"] != owner["identifier"]
        or doc["standard_inchi_key"] != owner["chemical_structure"]["standard_inchi_key"]
        or doc["graph"]["graph_id"] != graph_id
    ):
        raise GraphComponentError(f"{path}: graph ownership or ID mismatch")
    if not doc.get("curation_history"):
        raise GraphComponentError(f"{path}: component needs a curation event")
    validate_graphs([doc["graph"]])
    check_size(emit_natural_product_yaml(doc), path)


def resolve_graphs(owner: dict, record_path: Path, *, staged: dict[str, dict] | None = None) -> dict:
    """Return a deep-copied view with every graph; never silently skip a ref."""
    refs = owner.get("causal_graph_refs")
    if refs is None:
        refs = []
    if not isinstance(refs, list) or any(not isinstance(r, str) for r in refs):
        raise GraphComponentError("causal_graph_refs must be a list of graph IDs")
    if len(refs) != len({r.casefold() for r in refs}):
        raise GraphComponentError("duplicate graph reference")
    graphs = deepcopy(owner.get("causal_graphs") or [])
    for ref in refs:
        path = component_path(owner, record_path, ref)
        if staged is not None and ref in staged:
            doc = staged[ref]
        else:
            try:
                content = path.read_bytes()
            except OSError as exc:
                raise GraphComponentError(f"cannot read component {path}: {exc}") from exc
            check_size(content, path)
            doc = yaml.safe_load(content)
        validate_component(doc, owner, path, ref)
        graphs.append(deepcopy(doc["graph"]))
    validate_graphs(graphs)
    result = deepcopy(owner)
    if refs:
        result["causal_graphs"] = graphs
    return result


def read_natural_product(path: Path) -> dict[str, Any]:
    """Read the complete mechanism. Use raw YAML instead when mutating a record."""
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise GraphComponentError(f"{path}: expected a record mapping")
    return resolve_graphs(doc, path)


def validate_component_file(path: Path) -> None:
    """Validate a directly selected component against its actual referencing owner."""
    if path.parent.parent.name != "causal_graphs":
        raise GraphComponentError(f"noncanonical component path: {path}")
    _no_symlinks(path, path.parent.parent.parent)
    corpus = path.parent.parent.parent / "natural_products"
    matches = []
    for record_path in sorted(corpus.rglob("*.yaml")):
        owner = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        key = (owner.get("chemical_structure") or {}).get("standard_inchi_key")
        if key == path.parent.name and path.stem in (owner.get("causal_graph_refs") or []):
            matches.append((record_path, owner))
    if len(matches) != 1:
        raise GraphComponentError(f"{path}: expected exactly one referencing owner")
    record_path, owner = matches[0]
    if component_path(owner, record_path, path.stem).absolute() != path.absolute():
        raise GraphComponentError(f"noncanonical component path: {path}")
    resolve_graphs(owner, record_path)


def prevent_detached_components(owner: dict, record_path: Path) -> None:
    """A normal owner write cannot silently orphan an existing component."""
    if not record_path.exists():
        return
    previous = yaml.safe_load(record_path.read_text(encoding="utf-8"))
    old_refs = set(previous.get("causal_graph_refs") or [])
    if old_refs - set(owner.get("causal_graph_refs") or []):
        raise GraphComponentError("detaching a component requires an explicit removal migration")
    if old_refs and (
        previous["identifier"] != owner["identifier"]
        or previous["chemical_structure"]["standard_inchi_key"]
        != owner["chemical_structure"]["standard_inchi_key"]
    ):
        raise GraphComponentError("changing component ownership requires an explicit migration")


def audit_graph_components(corpus_dir: Path) -> list[Path]:
    """Validate all owners and components, including unreferenced artifacts."""
    expected: set[Path] = set()
    for record_path in sorted(corpus_dir.rglob("*.yaml")):
        owner = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        resolve_graphs(owner, record_path)
        for ref in owner.get("causal_graph_refs") or []:
            path = component_path(owner, record_path, ref)
            if path in expected:
                raise GraphComponentError(f"multiple owners reference {path}")
            expected.add(path)
    root = corpus_dir.parent / "causal_graphs"
    _no_symlinks(root, root.parent)
    if root.exists() and not root.is_dir():
        raise GraphComponentError(f"component root is not a directory: {root}")
    actual = set()
    for path in sorted(root.rglob("*")):
        _no_symlinks(path, root.parent)
        if path.is_file():
            actual.add(path)
    if actual != expected:
        raise GraphComponentError(
            f"component inventory mismatch: unreferenced={sorted(actual - expected)}, "
            f"missing={sorted(expected - actual)}"
        )
    return sorted(expected)


def _require_event(doc: dict, path: Path) -> None:
    previous = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    if previous == doc:
        return
    old_history = previous.get("curation_history") or []
    history = doc.get("curation_history") or []
    if len(history) <= len(old_history) or history[: len(old_history)] != old_history:
        raise GraphComponentError(f"{path}: mutation requires an appended curation event")


def write_validated_graph_bundle(owner: dict, record_path: Path, components: list[dict]) -> None:
    """Preflight the entire change, then write components and their owner.

    Every changed artifact needs an appended record_curation_event. Unchanged
    components may be omitted. No implicit deletion. Runtime failures roll back;
    interruption/power loss requires inspection and a full component audit.
    """
    from naturalproductmech.validation.write_validated import write_validated_natural_product

    errors = validate_natural_product(owner)
    if errors:
        raise ValidationFailedError(record_path, errors)
    staged = {}
    for doc in components:
        errors = validate_natural_product(doc, target_class="CausalGraphDocument")
        if errors:
            raise ValidationFailedError(None, errors)
        ref = doc["graph"]["graph_id"]
        if ref in staged or ref not in (owner.get("causal_graph_refs") or []):
            raise GraphComponentError(f"duplicate or unreferenced staged component: {ref}")
        staged[ref] = doc
    resolve_graphs(owner, record_path, staged=staged)
    prevent_detached_components(owner, record_path)
    check_size(emit_natural_product_yaml(owner), record_path)
    writes = [(component_path(owner, record_path, ref), doc) for ref, doc in staged.items()]
    writes.append((record_path, owner))
    for path, doc in writes:
        _require_event(doc, path)
    backups = {path: path.read_bytes() if path.exists() else None for path, _ in writes}
    try:
        for path, doc in writes:
            target_class = "NaturalProductRecord" if path == record_path else "CausalGraphDocument"
            write_validated_natural_product(doc, path, target_class=target_class)
    except Exception:
        for path, content in backups.items():
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(content)
        raise
