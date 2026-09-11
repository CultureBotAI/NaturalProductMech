#!/usr/bin/env python3
"""Text-embed every AntibioticRecord into a dense vector with a LOCAL model.

WHAT THIS EMBEDS, AND WHAT IT DOES NOT. These records are chemical structures,
but this is a *text* embedding: it captures what the corpus SAYS about a
compound — its name, class, structural family, definition, mechanism and the
roles its sources assert — not its chemistry. Two structural analogues with
different annotations land far apart; two unrelated scaffolds described the same
way land together. That is the right tool for "find records that talk about the
same thing" and the wrong one for "find similar molecules". A chemical map needs
fingerprints or a molecular language model, and is a separate artifact.

FIELDS DELIBERATELY EXCLUDED, with reasons — the include/exclude list is the
substance of a text embedding, so it is written down rather than implied:

  smiles / standard_inchi / standard_inchi_key
      A sentence embedder tokenizes these as gibberish of a length that would
      dominate every document. They carry the chemistry this model cannot read;
      that is what the structure map is for.
  producer notes / occurrence evidence notes
      Near-identical by design across thousands of records: one producer note
      states the locus evidence in the same sentence 233 times in a 400-record
      sample, and one LOTUS sentence appears 894 times. Including either would
      manufacture an enormous false cluster of "records seeded the same way".
      The VALUES they describe — the evidence basis, the source — are included.
  strain / detection_context / genome_accession / locus coordinates
      Collection numbers and coordinates: opaque per token, separating nothing.
  curation_status / grounding_status / source_version
      Facts about our process, not about the compound.

Output (data/embeddings/, vectors gitignored — large and rebuildable):
  vectors.f16.npy   float16 [N, dim], L2-normalized, row i <-> ids[i]
  ids.json          the N record identifiers, in row order
  meta.json         {model, dim, count, normalized, text_mode}

  just embed                          # whole corpus (~2,900 records, seconds)
  python3 scripts/embed_records.py --limit 20 --model BAAI/bge-large-en-v1.5
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
OUT = REPO_ROOT / "data" / "embeddings"

# Fields whose presence in a document would be noise or leakage. Named here so
# the audit is one list rather than an argument reconstructed from the code.
EXCLUDED = (
    # Chemistry a sentence embedder reads as gibberish, at a length that would
    # dominate every document.
    "smiles", "standard_inchi", "standard_inchi_key",
    # Facts about our process, not about the compound.
    "curation_status", "grounding_status", "source_version",
    # The boilerplate trap, and it is worse in this corpus than in the sibling
    # that documented it. A producer's `notes` states the locus evidence in the
    # same sentence on thousands of records ("Locus evidence: none stated. That
    # evidence grades the LOCUS as ..."), and an occurrence's evidence `notes`
    # carries one LOTUS sentence 894 times in a 400-record sample. Either would
    # manufacture one enormous cluster of "records seeded the same way" and
    # drown every real signal. The VALUES those notes describe — the evidence
    # basis, the source — are short enough to say directly and are included.
    "notes",
    # From producer_organisms and occurrences: the species goes in, these do
    # not. A strain designation is a collection number and a cluster accession
    # an identifier; both are opaque per token and would separate nothing.
    "strain", "biosynthetic_gene_cluster", "detection_context",
    # Locus coordinates are numbers with no semantic content for a text model.
    "locus_from", "locus_to", "genome_accession",
)


def pick_synonyms(entries: list[dict], limit: int = 6) -> list[str]:
    """The record's synonyms, shortest first.

    Deliberately simpler than the sibling this was ported from, and the reason
    is a measurement rather than taste. There, synonyms were 42% of all corpus
    tokens, ran to 828 characters and hid full systematic names, so they needed
    ranking by `synonym_type` and a length filter on the residue. This corpus
    holds 162 synonyms in total, every one RELATED_SYNONYM, the longest 51
    characters and the median 12. There is no long tail to cut, so cutting one
    would be machinery guarding a problem that is not here.
    """
    values = [str(e["value"]) for e in entries if e.get("value")]
    return sorted(dict.fromkeys(values), key=lambda v: (len(v), v))[:limit]


def humanize(value: str) -> str:
    """AMINO_ACIDS_AND_PEPTIDES -> 'amino acids and peptides'."""
    return (value or "").replace("_", " ").lower()


def build_document(record: dict) -> str:
    """One document per record, ordered MOST DISCRIMINATIVE FIRST.

    The model's window is 512 tokens, so order decides what survives if a
    document grows past it. The short fields that actually separate one natural
    product from another — what kind of molecule it is, what it does, and above
    all WHICH ORGANISM MAKES IT — go first. The ChEBI definition, then
    synonyms, then identifiers go last: verbose, weakly semantic per token, and
    the right things for truncation to take first.

    Producers and occurrences are both included and are LABELLED DIFFERENTLY,
    because the distinction is the point of this corpus. "produced by" and
    "found in" are different claims, and a text model that saw one merged list
    would place a record whose only link to an organism is an isolation report
    beside one with a characterized gene cluster.
    """
    parts: list[str] = [str(record.get("label") or record.get("identifier"))]

    # What kind of molecule. np_pathway is NPClassifier's and therefore
    # computed; it is included as a description, which is all a text embedding
    # can treat it as anyway.
    pathway = humanize(record.get("np_pathway", ""))
    if pathway and pathway != "unclassified":
        parts.append(f"{pathway} natural product")
    classes = [str(c) for c in (record.get("compound_classes") or []) if c]
    if classes:
        parts.append(", ".join(classes[:4]))
    bgc = [humanize(str(c)) for c in (record.get("bgc_class") or []) if c]
    if bgc:
        parts.append("gene cluster class: " + ", ".join(bgc[:4]))

    # What it does. The summary is the curated roll-up; the assay names beneath
    # it are long and repetitive, so only the summary goes in.
    activity = [humanize(str(a)) for a in (record.get("bioactivity_summary") or []) if a]
    if activity:
        parts.append("activity: " + ", ".join(activity[:6]))

    # The organism that makes it, with the strength of the claim. Species only:
    # a strain designation is a collection number that separates nothing.
    producers = dict.fromkeys(
        str(p.get("taxon_label")) for p in (record.get("producer_organisms") or [])
        if p.get("taxon_label"))
    if producers:
        parts.append("produced by " + ", ".join(list(producers)[:4]))
    bases = dict.fromkeys(
        humanize(str(p.get("evidence_basis"))) for p in (record.get("producer_organisms") or [])
        if p.get("evidence_basis"))
    if bases:
        parts.append("producer evidence: " + ", ".join(list(bases)[:3]))

    # Where it was FOUND, which is a weaker claim and is said as one.
    found_in = dict.fromkeys(
        str(o.get("taxon_label")) for o in (record.get("occurrences") or [])
        if o.get("taxon_label"))
    found_in = [name for name in found_in if name not in producers]
    if found_in:
        parts.append("found in " + ", ".join(found_in[:6]))

    targets = [str(t.get("target_label")) for t in (record.get("molecular_targets") or [])
               if t.get("target_label")]
    if targets:
        parts.append("targets: " + ", ".join(dict.fromkeys(targets))[:200])

    if record.get("definition"):
        parts.append(str(record["definition"]))

    synonyms = pick_synonyms(record.get("synonyms") or [])
    if synonyms:
        parts.append("also known as " + ", ".join(synonyms[:6]))

    # Identifiers are opaque one at a time, but their SHARED tokens cluster
    # records from one MIBiG entry or one ChEBI subtree, which is real
    # structure rather than noise. Last: weakest signal per token.
    ground = [str(record.get("identifier"))]
    ground += [str(x) for x in (record.get("xrefs") or [])]
    ground += [str(c.get("accession")) for c in (record.get("biosynthetic_gene_clusters") or [])
               if c.get("accession")]
    ground = list(dict.fromkeys(g for g in ground if g))[:12]
    parts.append("identifiers: " + ", ".join(ground))

    # Strip a trailing period before joining: ChEBI definitions end with one and
    # the join would otherwise produce ".." mid-document.
    return ". ".join(p.rstrip().rstrip(".") for p in parts if p and p.strip())


def corpus_fingerprint(docs: list[str]) -> str:
    """A hash of the embedded DOCUMENTS, not of the record files.

    Vectors and the map derive from these strings, so this is what decides
    whether a committed map still describes the corpus. It is recomputed by
    `tests/test_embeddings.py` in pure python — no torch — which is the only
    reason staleness is detectable in CI at all. A corpus edit that does not
    change any embedded field (a curation_status flip, say) correctly leaves it
    alone; one that changes a definition or a mechanism does not.
    """
    return hashlib.sha256("\x1f".join(docs).encode("utf-8")).hexdigest()[:16]


def load_corpus() -> tuple[list[str], list[str], list[dict]]:
    """(ids, documents, light metadata) in a stable identifier order."""
    rows = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict) or not record.get("identifier"):
            continue
        rows.append(record)
    rows.sort(key=lambda r: str(r["identifier"]))
    ids = [str(r["identifier"]) for r in rows]
    docs = [build_document(r) for r in rows]
    meta = [{"id": str(r["identifier"]), "label": r.get("label"),
             "class": r.get("np_pathway"),
             "producers": [p.get("taxon_label") for p in
                           (r.get("producer_organisms") or [])][:3]} for r in rows]
    return ids, docs, meta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default="BAAI/bge-large-en-v1.5")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--limit", type=int, default=0, help="embed only the first N (canary)")
    ap.add_argument("--device", default=None, help="mps|cpu|cuda (auto if unset)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the documents that WOULD be embedded and stop")
    args = ap.parse_args()

    ids, docs, meta = load_corpus()
    if not ids:
        print("no records found under data/natural_products/", file=sys.stderr)
        return 2
    if args.limit:
        ids, docs, meta = ids[:args.limit], docs[:args.limit], meta[:args.limit]

    if args.dry_run:
        print(f"{len(ids):,} records would be embedded with {args.model}\n")
        for i, d in zip(ids[:3], docs[:3], strict=True):
            print(f"--- {i} ---\n{d}\n")
        lengths = [len(d) for d in docs]
        print(f"document chars: min {min(lengths)}  median "
              f"{sorted(lengths)[len(lengths) // 2]}  max {max(lengths)}")
        print("\n--dry-run: nothing written.")
        return 0

    import numpy as np
    import torch
    from sentence_transformers import SentenceTransformer

    device = args.device or ("mps" if torch.backends.mps.is_available()
                             else "cuda" if torch.cuda.is_available() else "cpu")
    print(f"{len(ids):,} records -> embedding with {args.model} on {device}")
    model = SentenceTransformer(args.model, device=device)
    vectors = model.encode(docs, batch_size=args.batch, convert_to_numpy=True,
                           normalize_embeddings=True, show_progress_bar=True)

    OUT.mkdir(parents=True, exist_ok=True)
    np.save(OUT / "vectors.f16.npy", vectors.astype(np.float16))
    (OUT / "ids.json").write_text(json.dumps(ids), encoding="utf-8")
    (OUT / "records.json").write_text(json.dumps(meta), encoding="utf-8")
    (OUT / "meta.json").write_text(json.dumps({
        "model": args.model, "dim": int(vectors.shape[1]), "count": len(ids),
        "normalized": True, "excluded_fields": list(EXCLUDED),
        "corpus_fingerprint": corpus_fingerprint(docs),
    }, indent=2), encoding="utf-8")
    print(f"wrote {vectors.shape[0]:,} x {vectors.shape[1]} vectors to "
          f"{OUT.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
