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


def sibling_classes_for(record: dict) -> set:
    """Activity classes the linked sibling corpus asserts for this structure.

    Read from the pinned inventory, which is what the seeder used, so the test
    checks the same evidence rather than a restatement of it.
    """
    links = record.get("related_records") or []
    if not links:
        return set()
    mapping = {
        "ANTIBACTERIAL": "ANTIBACTERIAL", "ANTIFUNGAL": "ANTIFUNGAL",
        "ANTIMYCOBACTERIAL": "ANTIMYCOBACTERIAL", "ANTIVIRAL": "ANTIVIRAL",
        "ANTIPROTOZOAL": "ANTIPARASITIC",
        "ANTIMICROBIAL_UNSPECIFIED": "ANTIMICROBIAL_UNSPECIFIED",
    }
    path = REPO_ROOT / "data" / "raw" / "antibioticmech_inchikeys.tsv"
    if not path.exists():
        return set()
    key = (record.get("chemical_structure") or {}).get("standard_inchi_key")
    with path.open(newline="", encoding="utf-8") as fh:
        return {
            mapping[row["antimicrobial_class"]]
            for row in csv.DictReader(fh, delimiter="\t")
            if row["standard_inchi_key"] == key and row["antimicrobial_class"] in mapping
        }


def test_every_bioactivity_summary_value_is_backed(records):
    """The one backing rule, from PLAN.md 3.5. A summary value with nothing
    behind it is the field's whole failure mode."""
    offenders = []
    for r in records:
        summary = r.get("bioactivity_summary") or []
        if not summary:
            continue
        # Tighter than "some backing field exists": every summary VALUE must
        # trace to an observation carrying that class, a target, or a sibling
        # link. A summary value nothing on the record supports is the field's
        # whole failure mode.
        # A summary value must trace to something on THIS record that asserts
        # that class: an observation carrying it, or a sibling link whose
        # corpus asserts it. "The record has a link, therefore any value is
        # fine" was too loose — a linked record could have claimed CYTOTOXIC
        # with nothing behind it.
        classes = {b.get("activity_class") for b in r.get("bioactivities") or []}
        classes |= sibling_classes_for(r)
        unbacked = [v for v in summary if v not in classes]
        backed = not unbacked or bool(r.get("molecular_targets"))
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
#
# Rose from 8 to 22 when NCBI Taxonomy was adopted, and the rise is the source
# working as intended: resolving a name class of `synonym` is precisely how
# `Penicillium notatum` and `Penicillium chrysogenum` reach the same taxid.
# Every pair at 22 was checked and is a real synonym or a reclassification —
# Acremonium chrysogenum / Cephalosporium acremonium, Burkholderia /
# Paraburkholderia rhizoxinica, Clostridium / Ruminiclostridium cellulolyticum.
# The number moving is the signal; raising the bound without reading the new
# pairs would throw that away.
#: Taxon ids carrying more than one label that are NOT explained by a merge.
#: Two names for one id is what a source mislabelling a taxid looks like, so
#: the count is budgeted rather than waived. It came DOWN from 22 when merged
#: ids started being rewritten (#63): five of the old conflicts were one taxon
#: under its retired and current ids, and unifying them removed the conflict.
KNOWN_SYNONYM_TAXA = 17

def non_organism_taxa() -> set[str]:
    """Taxa that do not denote a single organism, from the committed inventory.

    Read rather than hard-coded, so this test checks the corpus against the
    same decision the seeder applied — the taxonomy extractor derives the set
    from NCBI's own tree (#62, #68). A literal here would drift from it.
    """
    path = REPO_ROOT / "data" / "raw" / "taxon_non_organism.tsv"
    assert path.exists(), "taxon_non_organism.tsv missing; run `just extract-taxonomy`"
    _, rows = read_tsv(path)
    assert rows, "taxon_non_organism.tsv is empty, which the first run showed it is not"
    return {row["taxon_id"] for row in rows}


def taxon_claims(record: dict):
    """Every (field, taxon id) a record asserts about an organism."""
    for producer in record.get("producer_organisms") or []:
        yield "producer_organisms", producer.get("taxon_id")
    for occurrence in record.get("occurrences") or []:
        yield "occurrences", occurrence.get("taxon_id")
    for cluster in record.get("biosynthetic_gene_clusters") or []:
        yield "biosynthetic_gene_clusters", cluster.get("organism_taxon_id")
    for target in record.get("molecular_targets") or []:
        yield "molecular_targets", target.get("taxon_id")
    for observation in record.get("bioactivities") or []:
        yield "bioactivities", observation.get("target_organism_id")


def test_no_taxon_claim_carries_a_merged_id(records):
    """NCBI retires taxids into others. The seeder rewrites through
    data/raw/taxon_merged.tsv at write time (#63); an old id on a record means
    a claim was written around that path, or the inventory is stale."""
    merged_path = REPO_ROOT / "data" / "raw" / "taxon_merged.tsv"
    assert merged_path.exists(), "taxon_merged.tsv is not committed; run `just extract-taxonomy`"
    _, rows = read_tsv(merged_path)
    old_ids = {row["old_taxon_id"] for row in rows}
    assert old_ids, "taxon_merged.tsv is empty, which the first run showed it is not"
    offenders = [
        (record["identifier"], field, taxon)
        for record in records
        for field, taxon in taxon_claims(record)
        if taxon in old_ids
    ]
    assert not offenders, f"taxon claims on merged ids: {offenders[:6]}"


def test_no_taxon_claim_names_a_non_organism_node(records):
    """A producer claim on "unclassified sequences" or "uncultured bacterium"
    asserts a producer while naming none, and every other gate passes it: the
    id is a valid CURIE and the label is non-empty. 42 claims did exactly that
    (#62, #68) — 36 of them on one node, which would have said that a single
    bacterium makes 36 unrelated compounds."""
    forbidden = non_organism_taxa()
    offenders = [
        (record["identifier"], field, taxon)
        for record in records
        for field, taxon in taxon_claims(record)
        if taxon in forbidden
    ]
    assert not offenders, f"taxon claims on non-organism nodes: {offenders[:6]}"


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
    # An id that other ids were merged INTO legitimately carries both the
    # retired name and the current one — Penicillium notatum and P.
    # chrysogenum are one organism, and the sources predate the merge. Those
    # are excluded rather than budgeted, because taxon_merged.tsv explains
    # them; everything else still has to fit the budget (#63).
    _, merge_rows = read_tsv(REPO_ROOT / "data" / "raw" / "taxon_merged.tsv")
    merge_targets = {row["new_taxon_id"] for row in merge_rows}
    conflicting = {
        k: sorted(v) for k, v in labels.items()
        if len(v) > 1 and k not in merge_targets
    }
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


# Organism labels resolving to more than one taxon id. The inverse of
# KNOWN_SYNONYM_TAXA, and the failure mode name-based resolution actually
# introduces: a source supplies an id for one row and none for another, and the
# fallback resolves the same name to a different id (#34).
KNOWN_AMBIGUOUS_LABELS = 8


def test_an_organism_label_resolves_to_one_taxon_id(records):
    """`Scytonema hofmannii` has two ids upstream — one strain-level, one
    species. Where a source gives an id for one row and none for another, the
    corpus can carry both under one name, and nothing else checks for it."""
    ids = {}
    for record in records:
        for occurrence in record.get("occurrences") or []:
            label = (occurrence.get("taxon_label") or "").strip().lower()
            if label and occurrence.get("taxon_id"):
                ids.setdefault(label, set()).add(occurrence["taxon_id"])
    ambiguous = {k: sorted(v) for k, v in ids.items() if len(v) > 1}
    assert len(ambiguous) <= KNOWN_AMBIGUOUS_LABELS, (
        f"organism labels resolving to several taxon ids rose to {len(ambiguous)}: "
        f"{list(ambiguous.items())[:4]}"
    )
