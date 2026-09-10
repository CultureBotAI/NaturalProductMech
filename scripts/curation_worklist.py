#!/usr/bin/env python3
"""The curation backlog, by queue, ranked — computed from the committed tree.

    just worklist
    just worklist --queue pathway-drift
    just review-queue --limit 0 --tsv curation/record_review_queue.tsv

Every queue is derived, never stored. A row leaves a queue when the thing that
put it there changes, so nothing has to be marked done and nothing goes stale;
that is also why this is a report rather than a file under `curation/`.

Ranking is by how much a curator's decision would settle, not by how easy the
row is. A producer claim resting on a database assertion alone outranks a
stereo flag, because the first is a claim about the world and the second is a
note about an identifier.

`pathway-drift` is the queue issue #2 asked for and #43 tracked. The pin —
`np_pathway` locked per record in `PATHS.tsv` — is enforced by
`just verify-corpus`. What was missing is the other half: noticing when a NEWER
classifier inventory disagrees with the pin. It does not move the record.
Slugs are published URLs, so a move is a curator's decision with `RETIRED.tsv`
reserving the old slug, and this is the list that decision is made from.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from collections.abc import Callable
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
RAW_DIR = REPO_ROOT / "data" / "raw"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"

#: Producer bases that assert the organism was shown to make the compound.
#: Imported rather than restated: `naturalproductmech.grading` owns this, and a
#: second copy would drift (#19).
sys.path.insert(0, str(REPO_ROOT / "src"))
from naturalproductmech.grading import CAUSAL_BASES  # noqa: E402

COLUMNS = ["queue", "rank", "identifier", "label", "path", "detail"]

_SEEDER = None


def seeder():
    """The seeder module, loaded once. Imported for its rules rather than
    reimplemented — `choose_pathway` decides what a classifier label means,
    and two answers to that would queue records nothing is wrong with."""
    global _SEEDER
    if _SEEDER is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "seed_from_sources", REPO_ROOT / "scripts" / "seed_from_sources.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules["seed_from_sources"] = module
        spec.loader.exec_module(module)
        _SEEDER = module
    return _SEEDER


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_records() -> list[tuple[Path, dict[str, Any]]]:
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("identifier"):
            out.append((path, doc))
    return out


def _row(queue: str, rank: int, path: Path, doc: dict[str, Any], detail: str) -> dict[str, str]:
    return {
        "queue": queue,
        "rank": str(rank),
        "identifier": doc["identifier"],
        "label": doc.get("label", ""),
        "path": str(path.relative_to(REPO_ROOT)),
        "detail": detail,
    }


# -- queues ---------------------------------------------------------------

def queue_pathway_drift(records, _discussions) -> list[dict[str, str]]:
    """Records whose pinned filing pathway disagrees with the current
    classifier inventory. The answer to #2 that #43 was still waiting for."""
    inventory = {r["standard_inchi_key"]: r for r in read_tsv(RAW_DIR / "npclassifier.tsv")}
    if not inventory:
        return []
    locked = {r["identifier"]: r["np_pathway"] for r in read_tsv(PATHS_FILE)}
    rows = []
    for path, doc in records:
        key = (doc.get("chemical_structure") or {}).get("standard_inchi_key")
        current = inventory.get(key)
        pinned = locked.get(doc["identifier"])
        if not current or not pinned:
            continue
        results = [x for x in (current.get("pathway_results") or "").split("|") if x]
        # One result is a filing decision; several or none is ambiguity, which
        # is the other queue's business rather than drift.
        if len(results) != 1:
            continue
        # The seeder's own function, not a second copy of the mapping: a
        # worklist that disagreed with the seeder about what a label means
        # would queue records nothing is wrong with.
        computed = seeder().choose_pathway(results)
        if computed != "UNCLASSIFIED" and computed != pinned:
            rows.append(_row("pathway-drift", 0, path, doc,
                             f"pinned {pinned}, {current.get('model_version') or 'the current model'} "
                             f"says {computed} ({results[0]!r})"))
    return rows


def queue_pathway_ambiguous(records, _discussions) -> list[dict[str, str]]:
    """Filed UNCLASSIFIED because the classifier returned several pathways or
    none. `PLAN.md` §3.4: the filing value is single, so a curator files it."""
    rows = []
    inventory = {r["standard_inchi_key"]: r for r in read_tsv(RAW_DIR / "npclassifier.tsv")}
    for path, doc in records:
        if doc.get("np_pathway") != "UNCLASSIFIED":
            continue
        key = (doc.get("chemical_structure") or {}).get("standard_inchi_key")
        results = [x for x in ((inventory.get(key) or {}).get("pathway_results") or "").split("|") if x]
        detail = (f"classifier returned {len(results)}: {', '.join(results)}"
                  if results else "classifier returned nothing")
        rows.append(_row("pathway-ambiguous", len(results), path, doc, detail))
    return rows


def queue_producer_evidence(records, _discussions) -> list[dict[str, str]]:
    """Every producer claim rests on a database assertion alone. The corpus's
    central claim at its weakest grade, so it ranks above everything else."""
    rows = []
    for path, doc in records:
        producers = doc.get("producer_organisms") or []
        if not producers:
            continue
        if any(p.get("evidence_basis") in CAUSAL_BASES for p in producers):
            continue
        bases = sorted({p.get("evidence_basis") or "none" for p in producers})
        rows.append(_row("producer-evidence", len(producers), path, doc,
                         f"{len(producers)} producer claim(s), none causal: {', '.join(bases)}"))
    return rows


def queue_occurrence_only(records, _discussions) -> list[dict[str, str]]:
    """Cited occurrences and no producer at all. A candidate for a producer
    claim if a source can be found, and never by promoting the occurrence."""
    rows = []
    for path, doc in records:
        occurrences = doc.get("occurrences") or []
        if occurrences and not (doc.get("producer_organisms") or []):
            rows.append(_row("occurrence-only", len(occurrences), path, doc,
                             f"{len(occurrences)} cited occurrence(s), no producer claim"))
    return rows


def queue_biosynthesis(records, _discussions) -> list[dict[str, str]]:
    """M6's work, ranked by how much evidence is already waiting: a
    characterized cluster with a causal producer and no pathway written."""
    rows = []
    for path, doc in records:
        if doc.get("biosynthetic_pathway"):
            continue
        clusters = doc.get("biosynthetic_gene_clusters") or []
        demonstrated = sum(1 for c in clusters
                           if c.get("link_evidence_basis") == "CLUSTER_DEMONSTRATED")
        causal = sum(1 for p in doc.get("producer_organisms") or []
                     if p.get("evidence_basis") in CAUSAL_BASES)
        if not demonstrated and not causal:
            continue
        rows.append(_row("biosynthesis", demonstrated * 2 + causal, path, doc,
                         f"{demonstrated} demonstrated cluster link(s), {causal} causal "
                         f"producer claim(s), no biosynthetic_pathway"))
    return rows


def queue_stereo_incomplete(records, _discussions) -> list[dict[str, str]]:
    """The InChIKey does not pin the stereochemistry, so two records could
    describe different compounds."""
    rows = []
    for path, doc in records:
        structure = doc.get("chemical_structure") or {}
        if structure.get("stereo_complete") is False:
            rows.append(_row("stereo-incomplete", 0, path, doc,
                             f"{structure.get('standard_inchi_key', '')} has undefined stereocentres"))
    return rows


def queue_unresolved_taxa(_records, _discussions) -> list[dict[str, str]]:
    """Organism names no adopted source could resolve. Not record-shaped: one
    row per NAME, because resolving one settles every record that cites it."""
    rows = []
    for entry in read_tsv(REPO_ROOT / "curation" / "unresolved_taxa.tsv"):
        rows.append({
            "queue": "unresolved-taxa", "rank": "0",
            "identifier": "", "label": entry.get("organism_name", ""),
            "path": "curation/unresolved_taxa.tsv",
            "detail": f"named by {entry.get('requested_by', '')}",
        })
    return rows


def discussion_queue(discussion_id: str, name: str) -> Callable:
    """A queue per open discussion the seeder raises. The record already says
    what needs deciding; this is only how a curator finds them all."""
    def build(records, _discussions) -> list[dict[str, str]]:
        rows = []
        for path, doc in records:
            for discussion in doc.get("discussions") or []:
                if (discussion.get("discussion_id") == discussion_id
                        and (discussion.get("status") or "OPEN") == "OPEN"):
                    rows.append(_row(name, 0, path, doc,
                                     " ".join((discussion.get("prompt") or "").split())[:160]))
        return rows
    return build


QUEUES: dict[str, Callable] = {
    "producer-evidence": queue_producer_evidence,
    "biosynthesis": queue_biosynthesis,
    "pathway-drift": queue_pathway_drift,
    "structure-disagreement": discussion_queue("structure-disagreement", "structure-disagreement"),
    "name-disagreement": discussion_queue("name-disagreement", "name-disagreement"),
    "unnamed-producer": discussion_queue("unnamed-producer", "unnamed-producer"),
    "shared-structure": discussion_queue("shared-structure", "shared-structure"),
    "needs-a-name": discussion_queue("needs-a-name", "needs-a-name"),
    "occurrence-only": queue_occurrence_only,
    "pathway-ambiguous": queue_pathway_ambiguous,
    "unresolved-taxa": queue_unresolved_taxa,
    "stereo-incomplete": queue_stereo_incomplete,
}

#: Queue order IS the ranking between queues, most consequential first: a
#: claim about the world before a claim about an identifier.
QUEUE_ORDER = list(QUEUES)


def build(queue: str | None) -> list[dict[str, str]]:
    records = load_records()
    rows: list[dict[str, str]] = []
    for name in QUEUE_ORDER:
        if queue and name != queue:
            continue
        produced = QUEUES[name](records, None)
        produced.sort(key=lambda r: (-int(r["rank"]), r["label"], r["identifier"]))
        rows.extend(produced)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", choices=sorted(QUEUES),
                        help="one queue instead of all of them")
    parser.add_argument("--limit", type=int, default=10,
                        help="rows shown per queue; 0 for all")
    parser.add_argument("--tsv", type=Path, help="write every row to this TSV as well")
    args = parser.parse_args()

    rows = build(args.queue)
    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        print(f"wrote {args.tsv} ({len(rows)} rows)", file=sys.stderr)

    counts = Counter(r["queue"] for r in rows)
    if not rows:
        print("nothing queued." if args.queue else "the corpus has no open curation work.")
        return 0

    for name in QUEUE_ORDER:
        if name not in counts:
            continue
        print(f"\n{name}  ({counts[name]})")
        shown = [r for r in rows if r["queue"] == name]
        for row in (shown if args.limit == 0 else shown[:args.limit]):
            title = row["label"] or row["identifier"]
            print(f"  {title[:42]:<44} {row['detail'][:88]}")
        if args.limit and len(shown) > args.limit:
            print(f"  … {len(shown) - args.limit} more")

    print(f"\n{len(rows)} rows across {len(counts)} queue(s). "
          f"Queue order is the ranking: a claim about the world before a claim "
          f"about an identifier.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
