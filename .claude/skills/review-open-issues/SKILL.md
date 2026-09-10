---
name: review-open-issues
description: Sweep and triage the full open-issue queue for NaturalProductMech. Fetches every open issue, checks each against the committed corpus, the inventories, the schema and the code, flags duplicates and stale figures, and assigns a priority tier (P0 something wrong that every gate passes, P1 real-but-schedulable, P2 low-severity/process/doc, P3 backlog). Produces a short ranked report; only writes to GitHub when asked. Use when the user asks to review issues, prioritize the backlog, or triage, or after a review pass files a batch of new issues.
tools: Bash, Read
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review and prioritize open issues

Adapted from AntibioticMech's `review-open-issues`, which took its method from
PFASCommunityAgents and the KG-Microbe Mech repos. The full-queue sweep, the
evidence-over-vibes rule and the read-only default are theirs. What a check
consists of is specific to this repository: a generated corpus of natural
product structures, the inventories it reproduces from, and the origin claims
it carries.

## Overview

**Purpose**: an honest, current ranking of the whole open-issue queue.

**When NOT to use**: for choosing the next data source — that is the
`source-queue` skill — or for `NEXT_TASKS.md` upkeep. This skill ranks; it does
not implement fixes.

## What makes this repo different

**1. Almost every claim is checkable on a bare clone, so check it.**
The repository commits its evidence: the inventories in `data/raw/`, every
record YAML under `data/natural_products/`, the generated site in `pages/` (once #53 lands),
the slug lockfile and the retired-slug ledger, and the pinned AntibioticMech
InChIKey inventory. An issue asserting something about a record, a producer, a
BGC, a slug or a count can be answered by reading the file. The exception is
`downloads/`, the raw ChEBI, MIBiG and LOTUS releases, which is gitignored:
an issue about *extraction* semantics may need a re-extraction without
`--offline`, and that is a network fetch worth saying out loud.

**2. A green gate is not evidence the code is right.**
This is the fleet's defining failure mode and the one that sets P0. In
AntibioticMech, nineteen defects were found in one review pass while `just qc`
was green, because the corpus faithfully reproduced computations that were
wrong. Expect the same here. Run the gates, then check the *claim*
independently of them.

**3. The domain has a signature silent error: occurrence written as
production.** A record whose `producer_organisms` carries a taxon that the
cited source only *isolated the compound from* is wrong in a way no schema
check sees. So is a sponge recorded as the producer of its symbiont's
polyketide, a plant recorded as the producer of an endophyte's alkaloid, or a
producer claim resting on a gene cluster supported only by homology
prediction. Every issue touching `producer_organisms`, `occurrences` or
`biosynthetic_gene_clusters` is checked against the cited source's own words,
not against the field's presence.

A close relative of it: **a source field that does not mean what its name
says.** MIBiG's `quality: questionable` marks a legacy-format entry, not
doubtful science, and its reviewer id is a placeholder in almost every entry.
An issue proposing to gate on either is proposing to discard most of the
database or all of it. Check what the field's own documentation says before
agreeing with an issue about it.

**4. Computed classification masquerading as assertion is the second one.**
An NPClassifier pathway or an NP-likeness score written into a field without
its tool-and-version marker, or used to *admit* a record, is P0. The filing
class is allowed to be computed; the record must say so.

**5. Figures drift fast, and issues quote figures.**
Re-derive every count, class breakdown and coverage percentage before repeating
it, and say so when a title has drifted. Phase widening (`producer_scope`) can
move the corpus by thousands in one PR.

**6. Some issues are blocked on someone who is not us.**
- **Owner decision** — scope widening to plants (`PLAN.md` §2.4), which
  licence-aggregating sources to trust, which label a record carries.
- **Upstream terms** — NPAtlas's NonCommercial licence, COCONUT's per-source
  terms, ChEMBL's share-alike. A waiver, not a patch.
- **Upstream data** — a MIBiG entry naming a class rather than a compound, a
  LOTUS occurrence citing a reference that does not contain the compound, two
  Wikidata items for one structure. Flagged with a `CURATION_TODO` discussion;
  the fix belongs to the provider.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
queue_file="${TMPDIR:-/tmp}/naturalproductmech-open-issues.json"
gh issue list --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], (.labels|map(.name)|join(",")), .title] | @tsv' "$queue_file"
jq length "$queue_file"
```

`--limit` silently caps with no warning. Print `jq length` and state whether
coverage was complete. Read from the saved JSON rather than the TSV overview:
bodies and comments carry the evidence.

### Step 2 — Establish what is true right now

Once, before checking any corpus-shaped issue:

```bash
just qc                 # every gate: lint, docs, provenance, source queue,
                        # tests, validation, reproduction, generated site
just report             # live per-class counts and field coverage
just worklist           # the curation backlog by queue
git log --oneline -8    # what has landed since the issues were filed
```

**If `just qc` fails, say so before ranking anything.** Every corpus-derived
verdict is then provisional and must be reported as such.

**If `just qc` passes, do not treat that as agreement with any issue's claim.**

Then classify each issue's evidence:

- **Checkable from the committed tree** — a record, a producer claim, a BGC
  accession, a slug, a count, a schema rule, a test. Measure it.
- **Needs an upstream fetch** — extraction semantics against a ChEBI, MIBiG or
  LOTUS release not in `downloads/`. Say so, and say whether you fetched.
- **Needs the cited source** — a producer/occurrence claim can only be
  verified by reading the reference. Say whether you read it.
- **Code-only** — read the code and ignore the corpus.
- **Blocked on a person or a provider** — see point 6; do not rank as actionable.

### Step 3 — Group and dedupe

Group by shared root cause, same script, or near-identical failure scenario.
The families to expect, most of them inherited from AntibioticMech's history:

- **Something wrong that every gate passes.** Occurrence seeded as production;
  computed class presented as asserted; an unreviewed MIBiG entry admitted;
  roles silently dropped; a cross-corpus link pointing at a retired slug.
- **Silent loss of curator work.** A re-seed that discards curated fields
  because a record moved directory when its filing class changed.
- **A claim the code does not deliver.** A documented invariant with no
  enforcement; a scope statement `conf/sources.yaml` contradicts; a drifted
  figure.
- **A safety rail that is not one.** A canary that exits 0 having written
  nothing; a size budget that is not enforced; a destructive flag without a
  guard.
- **Identity and provenance limits.** InChIKey collisions on macrocycles and
  glycosides; `stereo_complete` false on a record presented as fully defined;
  minted-versus-grounded resolution; retired slugs.
- **Licence.** A row seeded from an upstream whose terms were never verified
  per source; attribution missing from `ATTRIBUTION.md`.

### Step 4 — Check each issue against current reality

- **Already fixed?** `git fetch origin`, then
  `git log --oneline origin/main --perl-regexp --grep "#<N>\b"`. The `\b` is
  required. Also check the working branch; scaffold work may live off `main`.
- **Closed by a merged PR?**
  `gh issue view <N> --json closedByPullRequestsReferences`, then check
  `mergedAt`. `Closes #A and #B` only auto-closes `#A`.
- **Still reproducible?** Prefer a command over a reading:
  ```bash
  # does a record's producer claim carry biosynthesis-grade evidence?
  python3 -c "import yaml;d=yaml.safe_load(open('data/natural_products/polyketide/erythromycin-a.yaml'));print([(p['taxon_id'],p.get('evidence_basis')) for p in d.get('producer_organisms',[])])"
  # is a MIBiG entry in the inventory reviewed?
  awk -F'\t' '$1=="BGC0000055"{print $3,$4,$5}' data/raw/mibig_compounds.tsv
  # has a figure in a title drifted?
  just report | head -12
  # does the AntibioticMech link still resolve?
  grep -F "<InChIKey>" data/raw/antibioticmech_inchikeys.tsv
  ```
- **Title still true?** Re-derive before repeating.

### Step 5 — Assign priority

- **P0 — something wrong that the gates do not catch.** A producer claim the
  cited source does not make; a computed class admitted as an assertion; a
  redistribution claim the licence page contradicts; a path that silently
  destroys curated work. Invisible wrongness: `just qc` green and the corpus
  still saying something untrue.
- **P1 — real, schedulable.** A crash, a destructive flag, a gap in a gate.
- **P2 — low-severity, process, or doc.** Drift, cleanups, stale references.
- **P3 — backlog.** Real, not scheduled, kept as a record.

Orthogonal to severity: **blocked-on-owner**, **blocked-upstream**. Use P0
sparingly; if more than ~10% land P0, recalibrate. This repository starts with
only GitHub's default labels. Creating priority labels is a write action;
propose it, do not assume it.

### Step 6 — Present the report

- Ranked list, P0 first, one line per issue or group, number and a one-sentence
  why.
- Separate "fixed in code" from "blocked on a decision" from "still open and
  actionable".
- List issues recommended for closing, each with evidence: a commit, a PR, a
  command and its output. Never "this looks done".
- Recommend a top 2–3 to act on next, with reasoning.
- State how many issues were reviewed and whether coverage was complete.
- Say which verdicts were re-derived from the current corpus, which required
  reading a cited source, and which were not checked.

### Step 7 — Act only when asked

Read-only by default. A general "yes, go ahead" is not blanket approval for an
unattended close loop.

- **Closing**: confirm the evidence first, then
  `gh issue close <N> --comment "<evidence>"`, one at a time.
- **Relabelling** is lower risk but still a write; batch it and say what changed.
- **Retitling** when a figure has drifted is worth doing; the comment should say
  what the number was and why it moved.

## Conventions this skill enforces

- Full-queue coverage, not first-page sampling. State the count.
- Re-derive every figure.
- Evidence over vibes: every CLOSE, STALE or duplicate recommendation cites a
  commit, a PR, or a command and its output.
- A green gate is not a verdict on a claim. Check the claim.
- Occurrence is not production. Check the source's words.
- Computed is not asserted. Check the provenance marker.
- Unknown stays unknown.
- P0 means silently wrong, not loudly broken.
- Read-only by default.

## Notes and limitations

- Keep `comments` in Step 1's `--json` list.
- Merging and closing stay the user's call; prior approval of one is not
  approval of the next.
- No @-mentions in comments without explicit per-mention authorization
  (standing rule).
- This skill ranks; it does not merge, push, or edit files under review.

## Related

- `just qc`, `just report`, `just worklist`.
- `curation/source_queue.tsv` and the `source-queue` skill — for issues that are
  really "should we adopt source X?".
- `PLAN.md`, `docs/HARMONIZATION.md`, `docs/CURATION.md` — the invariants an
  issue may be alleging a violation of.
- `NEXT_TASKS.md` — owed work.
