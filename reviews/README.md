# Saved Scientific Reviews

The authoritative observations are immutable YAML/Markdown pairs under
[`structured/`](structured/). They follow [the shared contract](../docs/record-reviews.md).
They do not change records, native curation status or source inventories.

## First Campaign Checkpoint

At corpus base `e66f934111777c4ebfe69475d0520c0cfa074785`, the ignored-inclusive
inventory contains **3,115 records and 242 referenced graph components**.
Two records have partial scientific assessments; **zero have completed
assessments in this campaign and 3,113 remain unassessed**. Deterministic checks
are not scientific coverage. The full-corpus review is still in progress.

| Exact Owner | Observation | Open Scientific Follow-Up |
| --- | --- | --- |
| `naturalproductmech:mibig-1e0dcc87ee` | [Markdown](structured/20261013T044353Z-mycophenolic-acid-2/review.md), [YAML](structured/20261013T044353Z-mycophenolic-acid-2/review.yaml) | [#868: identity](https://github.com/CultureBotAI/NaturalProductMech/issues/868) |
| `naturalproductmech:mibig-0ed362dd75` | [Markdown](structured/20261013T044353Z-2-methylisoborneol-2/review.md), [YAML](structured/20261013T044353Z-2-methylisoborneol-2/review.yaml) | [#724: identity](https://github.com/CultureBotAI/NaturalProductMech/issues/724), [#869: evidence grade](https://github.com/CultureBotAI/NaturalProductMech/issues/869) |

Both observations have `completion: partial` and `verdict: needs_curation`:
two confirmed identity blockers and one provisional major evidence concern.
Unavailable live-source verification prevents completed reviews. The occupied
mycophenolic-acid destination and unresolved 2-MIB stereochemistry prevent a
safe automatic correction. Publishing these reports does not resolve those
scientific issues or authorize transferring claims between structures.

## Durable Evidence

The [evidence manifest](evidence/20261013-first-two-records/manifest.json) maps
historical `/private/tmp/npmech-all-record-reviews-pU8b8GXS/` references to
repository-relative archived files with SHA-256 hashes. Original report bytes
remain unchanged. Follow the manifest mapping, not the original machine paths.

- [QC log](evidence/20261013-first-two-records/artifacts/qc.log.txt): 554 tests
  passed, 3 skipped; full native QC passed on the unchanged corpus.
- [Label report](evidence/20261013-first-two-records/artifacts/labels.log.txt):
  the reporting command exited 0 with **499 mismatches** and 4,649
  adapter-skipped checks. This is not an all-labels-clean result.
- [Auxiliary chemistry](evidence/20261013-first-two-records/artifacts/chemistry-auxiliary.json):
  cached RDKit 2024.03.5, explicitly not the project-pinned 2026.3.5 extractor.
- [Population](evidence/20261013-first-two-records/artifacts/population.json)
  and [checkpoint](evidence/20261013-first-two-records/artifacts/review-campaign-checkpoint.json):
  every owner/component hash, partial observations and the exhaustive remaining
  list. Same-name prioritization is a lead, not a finding.

Command receipts retain actual times, results and failures, including the initial
missing-target inspection and rejected draft formatting. Archived scripts have
`.py.txt` suffixes and are inert historical evidence, not portable executables or
instructions to replay exclusive captures/savers. `.log.txt` files are byte-for-byte
log copies. Archive-local Git attributes preserve original line endings and
output whitespace. Caches and unsaved YAML drafts are excluded explicitly.

The checkpoint predates this publication: its branch, `no_github_mutations` and
local-path metadata describe capture time, not current release status. Its
inherited access-stop pointer refers to an earlier local protein campaign;
that earlier campaign is not bundled or needed to verify these observations.
Unavailable sources remain unverified; no inaccessible paper text is archived.

`tests/test_review_evidence_archive.py` checks archive integrity, local-reference
coverage, receipt hashes, immutable report hashes and the historical corpus
population without reading the original temporary directory. Preserve these
files as a historical snapshot; add a later checkpoint rather than rewriting it.

Publication defect [#867](https://github.com/CultureBotAI/NaturalProductMech/issues/867)
is addressed by this archive and its checks. It is distinct from the open
scientific corrections above.
