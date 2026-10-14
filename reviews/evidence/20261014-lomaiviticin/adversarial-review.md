# Adversarial PR Review

Reviewed PR #980 head `86a87f1d2` against
`7d6b4d16acc9a28e2b4c9de4244f205beb0da157` on 2026-10-14 UTC.
This is a separate adversarial pass by the implementing assistant, not an
independent reviewer or scientific peer review.

## Findings And Dispositions

- Blocker #975: both C owners retain superseded core connectivity and one also
  conflicts with the isolation mass. Still OPEN; no replacement structure was
  independently established. Native conflict representation is mitigation only.
- Major, provisional #976: D formula/connectivity conflict. Still OPEN; do not
  select either encoding or automatically transfer the A-C revision to D.
- Major #977: cross-strain experimental attribution. Corrected through exact-row
  source pins, method withdrawal, separate producer/locus citations, and a C-only
  DPJ-0016 qualifier. D production in DPJ-0016 remains an explicit gap, not a new
  asserted experiment. Deposited locus and assayed DPJ-0019 graph remain distinct.
- Minor #978: ephemeral verification payloads. Addressed by the portable packet,
  source receipts, hashes, historical owner snapshots and regression checks.
  Full article text is not republished or claimed portable.
- Major #979: missing native conflict representation. Addressed with OPEN
  discussions and qualified pathway/final-product edges through guarded writes.
  This does not resolve the chemical findings or promote native status.
- Publication defect #981: repository lint found one E501 line in the archived
  helper; initial GitHub QC also failed there (run 38518371572). A formatting-only
  wrap fixes it. The original helper and manifest bytes remain separately
  archived, so captured review hashes are not silently rewritten.

No additional actionable defect was found in this bounded change scope.

## Adversarial Checks

- Re-read the published file scope, exact source pins, full corrected owners,
  primary strain/deposition text and generated page differences. Raw MIBiG
  assertions and original citations are retained as provenance, not misrepresented
  as experimentally verified exact-product assignments.
- The minimal-source regression proves only the two reviewed BGC0000240 rows
  change; neighboring A/E and BGC0000241 claims are not implicitly curated.
  Every withdrawal context field rejects source drift.
- Existing supported scaffold/starter edges, graph node identities and protein
  identifiers remain unchanged. Only the exact-product interpretation is narrowed.
- Focused correction tests: 148 passed. Packet/native tests after the lint fix:
  24 passed. Repository-wide lint passed; strict validation passed for all four.
- Delta audit: 3,111 unrelated owners, 243 components, 79 prior bundles, raw
  inventories and PATHS.tsv unchanged. All four chemical structures, native
  statuses and pre-existing history entries are unchanged.
- Original corpus QC passed 954 tests with 3 skips, plus complete schema,
  reproduction, corpus, provenance and generated-page gates. This baseline is
  not counted as QC of the later corrections.
- Initial temporary schema, test-path and timestamp errors were rejected and
  retained in logs. They did not become saved review defects. Original reviews
  and four linked successor observations remain immutable and partial.

The full local review-contract check and exact-head PR/merge-queue checks remain
publication gates at the time of this report. Their actual results will be
recorded on the PR; a passing CI result cannot close #975 or #976. The queue uses
squash merging, so all saved review Git bases are the existing durable main
commit, not a transient branch commit.
