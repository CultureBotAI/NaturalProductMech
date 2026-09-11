#!/usr/bin/env python3
"""Render the browsable site under pages/ from the committed corpus.

    just render
    just render-check

The site is committed, like the corpus and the inventories, so a reader gets
what CI rendered rather than what their toolchain happens to produce. That also
means it can go stale against the corpus exactly as a record could go stale
against `data/raw/`, which is what `--check` is for: it renders to a temporary
directory and fails if `pages/` differs.

What the pages are FOR
----------------------
The corpus exists to keep a producer claim and an occurrence apart, so every
page that can show the distinction shows it. A record page gives producers
their evidence basis and occurrences their citation, in separate sections, and
says on each what the claim does and does not assert. A pathway page counts
causal against asserted producer claims per record, because that ratio is the
honest summary of how much of this corpus is demonstrated.

The filing pathway is NPClassifier's and therefore computed, so the record page
says which model version decided it rather than presenting it as an assertion.
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "src" / "naturalproductmech" / "templates"
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
PAGES_DIR = REPO_ROOT / "pages"
CHEMICAL_MAP_ARTIFACT = REPO_ROOT / "data" / "embeddings" / "chemical-structure-map.json"

PATHWAY_TITLES = {
    "ALKALOIDS": "Alkaloids",
    "AMINO_ACIDS_AND_PEPTIDES": "Amino acids and peptides",
    "CARBOHYDRATES": "Carbohydrates",
    "FATTY_ACIDS": "Fatty acids",
    "POLYKETIDES": "Polyketides",
    "SHIKIMATES_AND_PHENYLPROPANOIDS": "Shikimates and phenylpropanoids",
    "TERPENOIDS": "Terpenoids",
    "UNCLASSIFIED": "Unclassified",
}
PATHWAY_BLURBS = {
    "UNCLASSIFIED": "The classifier returned several pathways or none, so the "
                    "filing decision was left open rather than resolved by array order.",
}

#: Fields the index reports coverage for, in the order `just report` uses.
COVERAGE_FIELDS = [
    "producer_organisms", "occurrences", "biosynthetic_gene_clusters",
    "biosynthetic_pathway", "bioactivities", "bioactivity_summary",
    "molecular_targets", "causal_graphs", "related_records", "discussions",
]

sys.path.insert(0, str(REPO_ROOT / "src"))
from naturalproductmech.grading import CAUSAL_BASES  # noqa: E402


def corpus_commit() -> str:
    """The commit the corpus was rendered from, or a marker when unknown.

    Not embedded in a page: a commit id would make every page differ on every
    commit, and `--check` would then be a test of the git history rather than
    of the site. It is printed, for whoever runs the render.
    """
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def load_records() -> list[tuple[Path, dict[str, Any]]]:
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("identifier"):
            out.append((path, doc))
    return out


def slug_of(path: Path) -> str:
    return path.stem


def measurement(item: dict[str, Any]) -> str:
    value, units = item.get("measurement_value"), item.get("measurement_units")
    kind = item.get("measurement_type") or ""
    if value is None:
        return kind
    return f"{kind} {value:g} {units or ''}".strip()


def first_reference(item: dict[str, Any]) -> str:
    for evidence in item.get("evidence") or []:
        if evidence.get("reference"):
            return evidence["reference"]
    return ""


def build_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    producers = []
    for p in doc.get("producer_organisms") or []:
        producers.append({**p, "causal": p.get("evidence_basis") in CAUSAL_BASES,
                          "evidence": p.get("evidence") or []})
    occurrences = []
    for o in doc.get("occurrences") or []:
        occurrences.append({**o, "reference": first_reference(o)})
    clusters = []
    for c in doc.get("biosynthetic_gene_clusters") or []:
        clusters.append({**c, "demonstrated": c.get("link_evidence_basis") == "CLUSTER_DEMONSTRATED"})
    targets = []
    for t in doc.get("molecular_targets") or []:
        targets.append({**t, "measurement": measurement(t), "reference": first_reference(t)})
    bioactivities = []
    for b in doc.get("bioactivities") or []:
        result = b.get("call") or measurement({
            "measurement_type": b.get("measurement_type"),
            "measurement_value": b.get("value"),
            "measurement_units": b.get("units"),
        })
        bioactivities.append({"assay": b.get("assay", ""), "result": result,
                              "reference": first_reference(b)})
    steps = []
    for s in doc.get("biosynthetic_pathway") or []:
        steps.append({**s, "reference": first_reference(s)})
    graphs = []
    for g in doc.get("causal_graphs") or []:
        labels = {n.get("node_id"): n.get("label", n.get("node_id", ""))
                  for n in g.get("nodes") or []}
        edges = [{**e,
                  "subject_label": labels.get(e.get("subject"), e.get("subject", "")),
                  "object_label": labels.get(e.get("object"), e.get("object", "")),
                  "reference": first_reference(e)}
                 for e in g.get("edges") or []]
        graphs.append({**g, "edges": edges})

    return {
        "label": doc.get("label", ""),
        "identifier": doc["identifier"],
        "slug": slug_of(path),
        "definition": doc.get("definition"),
        "grounding_status": doc.get("grounding_status", ""),
        "curation_status": doc.get("curation_status", ""),
        "bioactivity_summary": doc.get("bioactivity_summary") or [],
        "structure": doc.get("chemical_structure") or {},
        "xrefs": doc.get("xrefs") or [],
        "pathway_title": PATHWAY_TITLES.get(doc.get("np_pathway", ""), doc.get("np_pathway", "")),
        "classification": doc.get("np_classification"),
        "bgc_class": doc.get("bgc_class") or [],
        "producers": producers,
        "occurrences": occurrences,
        # The record caps what it carries; say so rather than implying the
        # inventories hold no more (#28).
        "occurrences_capped": None,
        "clusters": clusters,
        "targets": targets,
        "bioactivities": bioactivities[:25],
        "bioactivity_total": len(bioactivities),
        "related": doc.get("related_records") or [],
        "discussions": [d for d in doc.get("discussions") or []
                        if (d.get("status") or "OPEN") == "OPEN"],
        "pathway_steps": steps,
        "graphs": graphs,
        "source_concepts": doc.get("source_concepts") or [],
        "record_path": str(path.relative_to(REPO_ROOT)),
        "causal": sum(1 for p in producers if p["causal"]),
        "weak": sum(1 for p in producers if not p["causal"]),
        "n_occurrences": len(occurrences),
        "n_clusters": len(clusters),
    }


def load_chemical_map(record_ids: set[str]) -> dict[str, Any] | None:
    """The committed structure-map artifact, or None when it has not been built.

    Checked against the live corpus rather than trusted: an artifact naming a
    different record set would draw a map of a corpus that no longer exists,
    and the page gives no hint that anything is stale. Absent is fine and the
    map page is skipped — `just chemical-map` is a separate, heavier step than
    `just render`.
    """
    if not CHEMICAL_MAP_ARTIFACT.exists():
        return None
    artifact = json.loads(CHEMICAL_MAP_ARTIFACT.read_text(encoding="utf-8"))
    rows = artifact.get("records")
    if not isinstance(rows, list):
        raise SystemExit(f"{CHEMICAL_MAP_ARTIFACT}: records must be a list")
    map_ids = {row.get("identifier") for row in rows if isinstance(row, dict)}
    if map_ids != record_ids or len(rows) != len(record_ids):
        raise SystemExit(
            f"{CHEMICAL_MAP_ARTIFACT.relative_to(REPO_ROOT)} names a different record "
            f"set than the corpus ({len(rows)} vs {len(record_ids)}); "
            f"regenerate with `just chemical-map`"
        )
    return artifact


def build(out_dir: Path) -> tuple[int, int]:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)),
                      autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    records = load_records()
    by_pathway: dict[str, list[dict[str, Any]]] = {}
    coverage: Counter[str] = Counter()
    producer_claims = causal_claims = occurrence_records = 0

    for path, doc in records:
        built = build_record(path, doc)
        by_pathway.setdefault(doc.get("np_pathway", "UNCLASSIFIED"), []).append(built)
        for field in COVERAGE_FIELDS:
            if doc.get(field):
                coverage[field] += 1
        producer_claims += len(built["producers"])
        causal_claims += built["causal"]
        occurrence_records += 1 if built["occurrences"] else 0

    pathways = []
    for key in PATHWAY_TITLES:
        items = sorted(by_pathway.get(key, []), key=lambda r: (r["label"].lower(), r["identifier"]))
        if not items:
            continue
        pathways.append({
            "key": key, "slug": key.lower(), "title": PATHWAY_TITLES[key],
            "blurb": PATHWAY_BLURBS.get(key, ""), "count": len(items), "records": items,
        })

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    shutil.copyfile(TEMPLATES_DIR / "style.css", out_dir / "style.css")

    # conf/sources.yaml is a mapping of source key -> config at the top level,
    # alongside a couple of non-source settings. Counting its keys blindly
    # would report `producer_scope` as a data source.
    sources_path = REPO_ROOT / "conf" / "sources.yaml"
    source_count = 0
    if sources_path.exists():
        conf = yaml.safe_load(sources_path.read_text(encoding="utf-8")) or {}
        source_count = sum(1 for value in conf.values()
                           if isinstance(value, dict) and "license" in value)

    (out_dir / "index.html").write_text(env.get_template("index.html").render(
        root="", total=len(records), source_count=source_count, pathways=pathways,
        coverage=[(f, coverage.get(f, 0)) for f in COVERAGE_FIELDS],
        generated_on=retrieved_on(),
        stats={"producer_claims": producer_claims, "causal": causal_claims,
               "occurrence_records": occurrence_records},
    ), encoding="utf-8")
    (out_dir / "browse.html").write_text(env.get_template("browse.html").render(
        root="", total=len(records), pathways=pathways), encoding="utf-8")
    (out_dir / "404.html").write_text(env.get_template("not_found.html").render(
        root=""), encoding="utf-8")

    # The structure map, when its artifact has been built. Skipped rather than
    # half-drawn: `just chemical-map` needs RDKit and UMAP, which `just render`
    # does not, so a checkout that has never run it still renders a whole site.
    chemical_map = load_chemical_map({doc["identifier"] for _, doc in records})
    if chemical_map is not None:
        (out_dir / "chemical-map.html").write_text(
            env.get_template("chemical_map.html").render(
                root="", quality=chemical_map["quality"],
                model_version=chemical_map["model_version"],
                total=len(records)),
            encoding="utf-8")
        shutil.copyfile(TEMPLATES_DIR / "chemical_map.js", out_dir / "chemical-map.js")
        (out_dir / "data").mkdir(exist_ok=True)
        shutil.copyfile(CHEMICAL_MAP_ARTIFACT,
                        out_dir / "data" / "chemical-structure-map.json")

    record_template = env.get_template("record.html")
    pathway_template = env.get_template("pathway.html")
    written = 0
    for pathway in pathways:
        directory = out_dir / pathway["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(
            pathway_template.render(root="../", pathway=pathway), encoding="utf-8")
        for record in pathway["records"]:
            (directory / f"{record['slug']}.html").write_text(
                record_template.render(root="../", r=record), encoding="utf-8")
            written += 1
    return written, len(pathways)


def retrieved_on() -> str:
    """The manifest's retrieval date — the corpus's own notion of 'when'.

    Deliberately not today's date: a page that says when it was rendered
    differs on every render and would make `--check` fail for no reason.
    """
    manifest = REPO_ROOT / "data" / "raw" / "MANIFEST.yaml"
    if manifest.exists():
        value = (yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}).get("retrieved_on")
        if value:
            return f"from sources retrieved {value}"
    return "from the committed inventories"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--check", action="store_true",
                        help="render to a temporary directory and fail if pages/ differs")
    args = parser.parse_args(argv)

    if not args.check:
        written, pathways = build(args.out)
        print(f"rendered {written} record pages across {pathways} pathways "
              f"-> {args.out.relative_to(REPO_ROOT)} (corpus at {corpus_commit()})")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        expected = Path(tmp) / "pages"
        build(expected)
        if not args.out.exists():
            print("pages/ is not rendered; run `just render`", file=sys.stderr)
            return 1
        differences = _diff(expected, args.out)
        if differences:
            print("pages/ is out of step with the corpus:", file=sys.stderr)
            for line in differences[:20]:
                print(f"  {line}", file=sys.stderr)
            if len(differences) > 20:
                print(f"  … and {len(differences) - 20} more", file=sys.stderr)
            print("\nRun `just render` and commit the result.", file=sys.stderr)
            return 1
    print("pages/ is in step with the corpus")
    return 0


def _diff(expected: Path, actual: Path) -> list[str]:
    want = {p.relative_to(expected) for p in expected.rglob("*") if p.is_file()}
    have = {p.relative_to(actual) for p in actual.rglob("*") if p.is_file()}
    out = [f"{p}: expected but not committed" for p in sorted(want - have)]
    out += [f"{p}: committed but not rendered" for p in sorted(have - want)]
    for rel in sorted(want & have):
        if not filecmp.cmp(expected / rel, actual / rel, shallow=False):
            out.append(f"{rel}: differs")
    return out


if __name__ == "__main__":
    raise SystemExit(main())
