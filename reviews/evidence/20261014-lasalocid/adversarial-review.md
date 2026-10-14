# Adversarial PR Review

Reviewed PR #974 head `b74978c16` against
`64c095104e5352fb88ad3177c47995ccfd4275d5` on 2026-10-14 UTC.
This is a separate adversarial pass by the implementing assistant, not an
independent reviewer or scientific peer review.

## Findings And Dispositions

- Major #971: missing AB449340 strain-conflict representation. The guarded
  curator update now preserves both inspected assertions in an OPEN discussion.
  Closing this representation issue must not imply that the source disagreement
  is resolved.
- Major #972: wrong-locus primary citation on BGC0001648. The exact-row-pinned
  correction separates FXJ1.172 production evidence from the KT591188 deposit.
  The old reference remains in raw source data and explicitly contextualized
  correction notes. No experimental evidence tier is upgraded.
- Minor #973: missing FXJ1.172 strain qualifier. The pinned qualification adds
  the literal strain without replacing NCBITaxon:1931 with 710705.

No additional actionable defect was found in the published change scope.

## Adversarial Checks

- Read the two complete owners and maintained decision paths; checked the
  generated diffs and HTML evidence presentation. The 2009 citation remains
  only as correction context on the producer/locus, not primary support.
- Rechecked raw GenBank strain literals and the 2011 primary results. Primary
  analytical identification is not claimed to establish absolute stereochemistry.
- Tested snapshot hashes and binding to the exact two historical Git owners.
- The focused suite passed 203 tests, including source drift, citation routing
  and producer qualifiers. Strict validation passed for both owners.
- Delta audit confirmed 3,113 unrelated owners, 243 graph components, 75 prior
  review bundles, raw sources and PATHS.tsv unchanged. Chemistry, occurrence
  evidence and scientific statuses on these two owners are also unchanged.
- Initial test-command path errors and a test's whitespace-normalized strain
  expectation were corrected; the raw source data were never changed to fit a test.

Full local QC, the final immutable-review contract check, and GitHub required
checks remain publication gates. Their actual outcomes are recorded separately,
not presumed here. Complete primary source closure remains outside this bounded
fix and both successor reviews must stay partial.

## Validation Follow-Up

GitHub run `38511099497` subsequently passed the full authoritative QC for the
reviewed `b74978c161025dc63f8f959233541aefd321707a` head. Its metadata and log are
retained in `ci-qc.log`. The redundant slow local QC was stopped only after that
pass; its termination is retained in `correction-checks.json` and is not counted
as a successful local run. The final successor-review commit still requires its
own PR and merge-queue checks before merging.
