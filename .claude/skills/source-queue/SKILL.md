---
name: source-queue
description: Triage and maintain NaturalProductMech's prioritized data-source queue in curation/source_queue.tsv — rank candidate sources by the corpus gap they close, verify licence, structure completeness and producer-versus-occurrence semantics before adoption, and fold in deep-research findings. Use when asked what data source to add next, when evaluating a specific source, or after a research report lands; do not use as permission to extract, seed, or adopt a source.
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Triage the data-source queue

`curation/source_queue.tsv` is the ranked list of data sources this corpus might
adopt. This skill keeps it honest and answers "what should we add next?" with
evidence rather than enthusiasm.

Adapted from AntibioticMech's `source-queue`. The ranking rule and the licence
gate are the same. What is different is the natural-product source landscape:
it is dominated by aggregators that relabel each other's content, by
non-commercial licences, and by occurrence data that is easy to mistake for
production data.

## Read these first

- `curation/source_queue.tsv` — the queue itself.
- `research/2026-09-07-natural-product-data-sources.md` — the verified
  landscape, with confidence labels and refuted claims. Do not re-derive what
  it already settled; do re-check anything it marked UNVERIFIED.
- `just report` — which fields are actually empty, corpus-wide. A source that
  closes a full column beats one that improves a column already at 90%.
  (Until the corpus exists, `PLAN.md` §5 is the stand-in.)
- `PLAN.md` §2 / `docs/HARMONIZATION.md` — the scope decision and the identity
  model. A source outside scope is a rejection, not a low priority.
- `conf/sources.yaml` — what the pipeline reads today.
- `NEXT_TASKS.md` — the work already committed to.

## The ranking rule

Rank by **what the corpus cannot currently assert**, not by how well known the
source is. In order:

1. **Does it close a stated gap?** Check against `just report`, not intuition.
   The gaps this corpus was built to fill, in priority order:
   `producer_organisms` with biosynthesis-grade evidence,
   `biosynthetic_gene_clusters`, `occurrences` with a reference,
   `bioactivities` with assay context, `molecular_targets`,
   `biosynthetic_pathway`, `causal_graphs`. Structures alone close nothing:
   a record is admitted by an origin assertion, and a structure database with
   no organism or reference cannot introduce records here.
2. **Can we redistribute it?** A source we cannot redistribute is
   `use: CURATE_ONLY` or `REFERENCE` at best — it can inform a curator, and it
   must never be seeded. This is a hard gate, not a weighting.

   The corpus's record content is **CC BY 4.0** (`LICENSE-DATA`), inherited
   from the fleet decision in AntibioticMech #27; the code is CC0. Judge a
   candidate against that:

   - **CC0 / public domain** — acceptable. Wikidata (and therefore LOTUS's
     Wikidata deposition), PubChem, US federal data.
   - **CC BY** — acceptable. Add the source to `ATTRIBUTION.md` when adopting.
   - **CC BY-SA** — refused for seeding. Share-alike would propagate to the
     whole corpus. `CURATE_ONLY` at best. ChEMBL is the prominent case.
   - **NonCommercial** — refused. NPAtlas is CC BY-NC; excellent content, cannot
     be seeded.
   - **Proprietary or bespoke terms** — refused unless the terms explicitly permit
     redistribution and modification. Dictionary of Natural Products, MarinLit,
     AntiBase, NAPRALERT.
   - **Aggregate relabelling** — a database that says "our collection is CC0"
     while incorporating rows from CC BY-NC or proprietary sources has not
     changed those rows' terms. COCONUT and NP-KG both need per-source
     provenance before any row is seedable. Record which upstream a row came
     from, and treat the dataset-level label as a claim to verify, not a
     licence.

   Record what the licence says, not what it would take to make it work.
3. **Does it say who makes it, or only where it was found?** This is the
   natural-product-specific gate. A source asserting `compound → taxon` must
   be classified as producer-grade (MIBiG: characterized BGC) or
   occurrence-grade (LOTUS: isolated from / detected in). An occurrence source
   fills `occurrences`; it never fills `producer_organisms`, however large it
   is. Write which field it fills into `closes_gap`.
4. **Does it carry complete structures where it needs to?** A record is one
   chemical structure. A source that names compounds without structures
   (antiSMASH-DB predictions, many spectral libraries, most ethnopharmacology
   databases at the herb level) can still supply evidence keyed to compounds
   we already have, but it cannot introduce records. Note also stereochemistry:
   a source that flattens stereo cannot be the structure authority for a
   record.
5. **Is it asserted or computed?** NPClassifier, ClassyFire, NP-likeness and
   antiSMASH products are computed. They can populate a computed field with a
   tool-and-version provenance marker; they cannot admit a record and cannot
   be presented as a source assertion.
6. **Bulk access over API.** `data/raw/` is committed and the pipeline runs
   offline; a source that can only be scraped or queried per-compound imposes a
   networked step. Wikidata SPARQL is acceptable because LOTUS also ships a
   versioned bulk dump; record which one the extractor reads.
7. **Effort, last.** A tractable source that closes nothing still closes nothing.

Two sources that close the same gap: adopt one, measure what it actually added,
then decide about the second. MIBiG and LOTUS both claim compound–organism
pairs; they fill different fields, so both may be adopted — but the second is
still measured against the first.

## Verifying a source before it moves to ADOPTED

`redistribution` starts `UNVERIFIED` and must be checked against the source's own
licence page — not a summary, not a memory, not another database's claim about
it, and not the research report's summary of it unless the report quotes the
page. Record the date in `verified_on`. `scripts/check_source_queue.py` refuses
an ADOPTED row whose terms are unverified, and refuses a `SEED` adoption under
`RESTRICTED`, `SHARE_ALIKE` or `NON_COMMERCIAL` terms.

Also establish, and write into `rationale`:

- **Coverage against this corpus**, not in the abstract: how many of our
  records would actually gain a field. "700,000 structures" is not an answer;
  "of our N Phase-A records, M have an exact InChIKey match" is.
- **Identifier joinability** — does it carry Standard InChIKeys, SMILES from
  which one can be computed, ChEBI ids, Wikidata QIDs, NCBI Taxonomy ids?
  Name-only joining is a curation project, not an extraction. Taxon names
  without ids are a second name-only join.
- **Update cadence and versioning** — a source with no release identity cannot
  be recorded in `data/raw/MANIFEST.yaml`, which every committed inventory needs.
- **Known data-quality traps.** The ones this domain is known for: extracts
  recorded as constituents; occurrence presented as production; the host
  recorded as the producer of a symbiont's compound; stereochemistry lost on
  aggregation; class-level compound names in BGC entries ("a polyketide");
  unreviewed auto-generated entries presented identically to reviewed ones;
  text-mined organism pairs with no locatable reference; activity values on
  mixtures attributed to one constituent.
- **Whether an already-adopted source closes it.** Before adding a dependency,
  check what the sources already in `conf/sources.yaml` assert and are being
  discarded. ChEBI carries specialized-metabolite roles and citations; MIBiG
  carries bioactivity labels that the first release deliberately ignores.

  When the answer is yes, the work is **not** a new queue row: a new use of an
  adopted source is not a new source, and `check_source_queue.py` will refuse
  an ADOPTED row that `conf/sources.yaml` does not read as a source in its own
  right. Record the new capability in the existing source's rationale instead.

A licence that cannot be reached is a result too. Record the attempt, the URLs
tried and what blocked them, so the next pass does not repeat a failed fetch.

## Folding in a research report

When a deep-research report on sources lands, do not paste it into the queue.
For each source it covers: add or update the row, move `redistribution` off
`UNVERIFIED` only where the report cites the licence page itself, and put the
report's specific finding in `rationale`. A claim the report could not verify
stays `UNVERIFIED` in the queue — the report's own confidence labels carry over.

## What this skill does not do

It does not extract, seed, or adopt. Moving a source to ADOPTED means the
extractor reads it, `data/raw/` carries its inventory with a manifest entry,
`ATTRIBUTION.md` names it, and `just qc` passes — that is a pull request, with
the canary discipline in `CLAUDE.md`, not a row edit. Editing the row to say
ADOPTED without that work makes `check_source_queue.py` fail, which is the
intended behaviour.

## Output

Report: the top three candidates with the gap each closes, which field
(producer or occurrence) it is allowed to fill, and what is unverified about
it; anything whose status should change and why; and any source in the queue
that the corpus has outgrown. If the queue is already accurate, say so — a
short honest answer beats a reshuffle.
