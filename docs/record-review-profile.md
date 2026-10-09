# NaturalProductMech review profile

New record reviews follow [the shared contract](record-reviews.md), with
authoritative YAML and derived Markdown under
`reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/`. Historical ad hoc reports remain
historical evidence and need no migration. `conf/record_review.yaml` lists the
active routes and local rubrics.

## Routes and output

- `.claude/skills/review-yaml-record/SKILL.md`: one resolved record.
- `.claude/skills/review-yaml-category/SKILL.md`: a coherent category with
  explicit lump/split/retain/defer decisions; sampled coverage keeps its method,
  denominator, inspected members and limitations. Explicit batches use `kind: batch`.
- `.claude/skills/curate-yaml-record/SKILL.md`: the audit-only route uses the
  same output contract and retains the native scientific checklist.

Run from the repository root using its own Python environment (LinkML,
linkml-runtime, jsonschema and PyYAML; pytest in the dev extra):

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just review-validate /tmp/completed-review.yaml
just review-save /tmp/completed-review.yaml
just review-check
```

Use session-unique temporary inputs and add `--input <path>` to inspect for each
additional rubric/schema/source/overlay used. Retain the captured Git revision
and hashes. Checks record actual commands and exit codes, never invented
success. New observations are immutable; link both saved files in the final
response. Missing dependencies or required checks are an explicit blocked output
step or partial assessment, not permission to save unvalidated prose.

## Native questions and ownership

Review `data/natural_products/` for exact structure/stereochemistry, asserted
origin, producers versus occurrences, BGC activity/version and evidence basis,
computed filing pathway versus asserted classification, pure-compound activity,
and biosynthetic/causal support. Use `docs/CURATION.md`,
`docs/HARMONIZATION.md`, and the local checklist. Retain taxon/strain,
stereochemical resolution, source version and evidence tier as dimensions.

Read the owner AND every `causal_graph_refs` component under
`data/causal_graphs/<StandardInChIKey>/`; `read_natural_product` provides the
complete read-only mechanism. Hash the inspected components as context inputs.
Seeded facts belong to committed inventories, extractors/seeder and implemented
curation tables documented in `docs/CURATION.md`. `curation/decisions.tsv` is
reserved and is not consumed by the current seeder: do not recommend it as an
effective fix. Curator claims/components use the validated record/bundle writer
and their own curation events. Generated pages are not an owner.

REVIEWED still requires exact identity, internally consistent structure at the
supported stereochemical resolution, correct filing/classification, and checked
origin, occurrences and active compound-specific clusters. BGC_CORRELATED must
not become BGC_CHARACTERIZED without the requisite evidence. A saved review
does not promote native status or append history.

## Native checks and queue

```bash
just validate-strict <record-path> --out /tmp/naturalproductmech-record-validation.tsv
just verify-corpus --summary
just verify-reproduction
just review-queue --tsv /tmp/naturalproductmech-review-queue.tsv
just qc
```

`scripts/curation_worklist.py --review-records` computes a pending-record
checkpoint; its deterministic diagnostics and publication search output remain
inputs. They do not establish scientific review. Inspect the selected claims
and save the final assessment through the shared validator/saver. Keep the
population denominator and uninspected remainder for sampled cohorts.

## Validation and ownership of the contract

`schema/record_review.yaml`, `scripts/record_review.py`,
`docs/record-reviews.md`, and `tests/test_record_review_contract.py` are copied
byte-identically from CLAW. Canonical marked skill regions are rendered with
the native sections preserved. Edit the shared contract upstream and re-adopt;
the local profile, rubrics and scientific status gates remain repository-owned.
`just review-check` validates retained bundles and runs the profile/roundtrip
contract tests. The existing PR and merge-group quality workflow also runs the
contract test alongside its unchanged native checks. Zero structured reviews
means missing coverage, not a scientific pass. The new path is Git-visible
without opening ignored legacy report directories.

CI fetches full history and sets `RECORD_REVIEW_BASE` from the trusted PR base,
merge-group base, or push-before SHA. It requires that commit to exist before
running the canonical test, which rejects changes or deletions to previously
saved bundles. Local `just review-check` defaults to HEAD; set
`RECORD_REVIEW_BASE=<base-commit>` when checking a branch's committed changes.
There is no automatic CI fallback to an already modified HEAD.
