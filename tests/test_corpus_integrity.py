"""Corpus-wide invariants that per-record validation cannot see.

These pass trivially on an empty corpus, which is the M1 state. They are
written now, before there are records, because every one of them describes a
way the corpus could become wrong the moment M2 seeds it.
"""

from __future__ import annotations

import csv
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
PATHS_FILE = CORPUS_DIR / "PATHS.tsv"
RETIRED_FILE = CORPUS_DIR / "RETIRED.tsv"

PATHS_COLUMNS = ["identifier", "np_pathway", "slug", "path"]
RETIRED_COLUMNS = ["slug", "retired_on", "identifier", "reason"]


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def test_lockfile_has_the_expected_columns():
    columns, _ = read_tsv(PATHS_FILE)
    assert columns == PATHS_COLUMNS


def test_retired_ledger_has_the_expected_columns():
    columns, _ = read_tsv(RETIRED_FILE)
    assert columns == RETIRED_COLUMNS


def test_every_record_on_disk_is_in_the_lockfile(record_paths):
    _, rows = read_tsv(PATHS_FILE)
    locked = {row["path"] for row in rows}
    actual = {str(p.relative_to(REPO_ROOT)) for p in record_paths}
    assert actual - locked == set(), "record written without a lockfile row"


def test_no_two_records_share_a_slug():
    _, rows = read_tsv(PATHS_FILE)
    duplicates = [slug for slug, n in Counter(r["slug"] for r in rows).items() if n > 1]
    assert not duplicates, f"slugs are published URLs: {duplicates}"


def test_no_live_record_reuses_a_retired_slug():
    """A retired slug stays reserved, or an old URL silently starts resolving to
    a different compound."""
    _, live = read_tsv(PATHS_FILE)
    _, retired = read_tsv(RETIRED_FILE)
    clash = {r["slug"] for r in live} & {r["slug"] for r in retired}
    assert not clash, f"live records reuse retired slugs: {sorted(clash)}"


def test_identifiers_are_unique(records):
    duplicates = [i for i, n in Counter(r["identifier"] for r in records).items() if n > 1]
    assert not duplicates, f"duplicate identifiers: {duplicates}"


def test_a_surviving_inchikey_collision_is_flagged(records):
    """Merging on InChIKey is the product, but not every collision may be merged.

    ChEBI keeps a compound and its zwitterion as separate entries with the same
    Standard InChIKey; merging them would overrule the people who own the
    identifiers. Two MINTED concepts sharing a structure mean an upstream
    cross-reference is wrong and the seeder cannot tell which, so both stay.
    Tautomer pairs collide for a third reason.

    So the rule is not "never collide". It is that a collision which survives
    must be VISIBLE: each record carries a discussion naming its twin. A test
    forbidding all collisions would force a merge the domain does not allow —
    see issue #8.
    """
    by_key = {}
    for record in records:
        key = (record.get("chemical_structure") or {}).get("standard_inchi_key")
        if key:
            by_key.setdefault(key, []).append(record)

    unflagged = []
    for key, group in by_key.items():
        if len(group) < 2:
            continue
        for record in group:
            if not record.get("discussions"):
                unflagged.append((key, record["identifier"]))
    assert not unflagged, (
        f"InChIKey collisions surviving without a discussion naming the twin: {unflagged}"
    )


def test_a_minted_record_never_duplicates_a_grounded_structure(records):
    """A minted identity over a structure ChEBI already grounds is a failure of
    resolution, not a curation choice."""
    grounded = {r["chemical_structure"]["standard_inchi_key"]
                for r in records if r.get("grounding_status") == "EXACT"
                and r.get("chemical_structure", {}).get("standard_inchi_key")}
    offenders = [r["identifier"] for r in records
                 if r.get("grounding_status") == "MINTED"
                 and r.get("chemical_structure", {}).get("standard_inchi_key") in grounded]
    assert not offenders, f"minted records duplicating a grounded structure: {offenders}"


def test_no_producer_claim_lacks_evidence(records):
    offenders = [
        (r["identifier"], p.get("taxon_label"))
        for r in records for p in r.get("producer_organisms") or []
        if not p.get("evidence")
    ]
    assert not offenders, f"uncited production claims: {offenders}"


def test_no_occurrence_lacks_evidence(records):
    offenders = [
        (r["identifier"], o.get("taxon_label"))
        for r in records for o in r.get("occurrences") or []
        if not o.get("evidence")
    ]
    assert not offenders, f"uncited occurrences: {offenders}"


def test_every_bioactivity_summary_value_is_backed(records):
    """The one backing rule, from PLAN.md 3.5. A summary value with nothing
    behind it is the field's whole failure mode."""
    offenders = []
    for r in records:
        summary = r.get("bioactivity_summary") or []
        if not summary:
            continue
        backed = bool(r.get("bioactivities") or r.get("molecular_targets")
                      or r.get("related_records") or r.get("evidence"))
        if not backed:
            offenders.append(r["identifier"])
    assert not offenders, f"bioactivity_summary with no backing: {offenders}"


def test_every_measured_value_carries_units(records):
    """A value without units is not a measurement."""
    offenders = [
        (r["identifier"], b.get("assay"))
        for r in records for b in r.get("bioactivities") or []
        if b.get("value") is not None and not b.get("units")
    ]
    assert not offenders, f"values without units: {offenders}"


def test_every_causal_edge_is_cited(records):
    offenders = [
        (r["identifier"], g.get("graph_id"), e.get("predicate"))
        for r in records for g in r.get("causal_graphs") or []
        for e in g.get("edges") or [] if not e.get("evidence")
    ]
    assert not offenders, f"uncited causal edges: {offenders}"


def test_causal_edges_only_reference_declared_nodes(records):
    offenders = []
    for r in records:
        for graph in r.get("causal_graphs") or []:
            declared = {n["node_id"] for n in graph.get("nodes") or []}
            for edge in graph.get("edges") or []:
                for slot in ("subject", "object"):
                    if edge.get(slot) not in declared:
                        offenders.append((r["identifier"], graph.get("graph_id"), edge.get(slot)))
    assert not offenders, f"edges referencing undeclared nodes: {offenders}"


def test_the_filing_pathway_matches_the_directory(records, record_paths):
    """The directory IS the filing decision; a record filed elsewhere breaks the
    site's browse axis and its own URL.

    PATHWAY_DIRS is read from the seeder rather than restated, so a new pathway
    cannot be added in one place and silently missed in the other."""
    spec = spec_from_file_location("seed", REPO_ROOT / "scripts" / "seed_from_sources.py")
    seed = module_from_spec(spec)
    spec.loader.exec_module(seed)

    offenders = []
    for path in record_paths:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if "np_pathway" not in doc:
            continue
        if seed.PATHWAY_DIRS.get(doc["np_pathway"]) != path.parent.name:
            offenders.append((str(path), doc["np_pathway"]))
    assert not offenders, f"records filed outside their pathway directory: {offenders}"


def test_no_record_carries_html_markup(records):
    """ChEBI writes chemical typography as HTML, and it reached labels and so
    published slugs — `aflatoxin B1` became `aflatoxin-b-small-sub-1-sub-small`
    (#24). Stripped at extraction; asserted here because the slug is a URL."""
    import re
    tag = re.compile(r"<[^>]+>")
    offenders = [
        (r["identifier"], field)
        for r in records for field in ("label", "definition")
        if tag.search(r.get(field) or "")
    ]
    assert not offenders, f"records carrying HTML markup: {offenders[:5]}"


def test_no_record_repeats_an_occurrence(records):
    """Same taxon, same citation, twice. Small at first — 10 of 10,041 — and it
    grows with every occurrence source, because CyanoMetDB and NPAtlas would
    both overlap LOTUS heavily (#26).

    Note what is NOT a duplicate: the same taxon from two different references
    is two independent reports, which is more evidence rather than less.
    """
    offenders = []
    for record in records:
        seen = Counter(
            (o.get("taxon_id") or o.get("taxon_label"), o["evidence"][0]["reference"])
            for o in record.get("occurrences") or []
        )
        offenders.extend(
            (record["identifier"], key) for key, n in seen.items() if n > 1
        )
    assert not offenders, f"repeated occurrences: {offenders[:5]}"


def test_a_taxon_in_both_fields_says_it_is_corroboration(records):
    """A producer that is also an occurrence looks like a failure to
    deduplicate and is the opposite: two claims, two citations, two sources
    (#27). The record has to say so, or a reader draws the wrong conclusion."""
    offenders = []
    for record in records:
        producers = {p.get("taxon_id") for p in record.get("producer_organisms") or []}
        for occurrence in record.get("occurrences") or []:
            if occurrence.get("taxon_id") in producers and \
                    "corroborate" not in (occurrence.get("notes") or ""):
                offenders.append((record["identifier"], occurrence.get("taxon_id")))
    assert not offenders, f"uncommented producer/occurrence overlap: {offenders[:5]}"


# Taxon ids that legitimately carry two labels: nomenclatural synonyms, where
# sources recorded the name their own reference used. Listed rather than
# allowed silently, so a genuine mislabelling — which looks identical — shows
# up as a change in this number instead of hiding among them (#30).
KNOWN_SYNONYM_TAXA = 8


def test_taxon_labels_stay_consistent_for_an_id(records):
    """The id is the identity and the label is decoration, so nothing breaks.
    But two names for one identifier is also exactly what a source mislabelling
    a taxid would look like, and there is otherwise nothing to tell them apart.
    """
    labels = {}
    for record in records:
        for occurrence in record.get("occurrences") or []:
            taxon = occurrence.get("taxon_id")
            if taxon:
                labels.setdefault(taxon, set()).add(occurrence["taxon_label"])
    conflicting = {k: sorted(v) for k, v in labels.items() if len(v) > 1}
    assert len(conflicting) <= KNOWN_SYNONYM_TAXA, (
        f"taxon ids carrying several labels rose to {len(conflicting)}: "
        f"{list(conflicting.items())[:4]}"
    )


def test_no_record_is_too_large_to_review(record_paths):
    """`curate-yaml-record` tells a curator to read the entire YAML. Lupeol
    carried 925 occurrences in a 397 KB file, which is not readable — the
    inventories keep every one of them, the record keeps a bounded subset
    and says how many it omitted (#28)."""
    oversized = [
        (str(path), path.stat().st_size // 1024)
        for path in record_paths if path.stat().st_size > 64 * 1024
    ]
    assert not oversized, f"records too large to review: {oversized[:5]}"
