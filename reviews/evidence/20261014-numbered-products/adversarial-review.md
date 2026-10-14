# Adversarial Review

Bounded review of this publication against durable base
`22ced0a503edd1d04628f7cfbdbb14ee1d03047c`, 2026-10-14 UTC. This is a
separate adversarial pass by the implementing assistant, not independent
human review. The exact final commit and CI results are recorded on the PR.

## Findings And Dispositions

- Provisional major [#982](https://github.com/CultureBotAI/NaturalProductMech/issues/982):
  compound 6's charged encoding lacks a verified exact-product experiment.
  OPEN. The SI's ent-6 depiction is contextual, not an established stereochemical
  crosswalk. Do not substitute a neutral product or claim the record disproved.
- Provisional major [#983](https://github.com/CultureBotAI/NaturalProductMech/issues/983):
  compound 8's charged encoding and unresolved stereocenters need exact primary
  mapping. OPEN. Locus-level expression and database NMR annotations do not
  independently demonstrate this precise material.
- Publication defect [#984](https://github.com/CultureBotAI/NaturalProductMech/issues/984):
  rejected drafts used the campaign denominator in a one-record review and
  combined seed-only verdicts with scientific sign-off. A later preflight also
  rejected YAML aliases. The final author uses population one, false scientific
  sign-off for seed-only observations and alias-free emission. No rejected draft
  was ever saved as a canonical bundle, and no shared validator was weakened.
  Temporary evidence dependencies are addressed by a pinned packet and an
  offline replay tested from outside the research workspace.
  A manifest refresh initially included an ignored Python bytecode cache;
  it is excluded explicitly and guarded by a regression assertion so CI does
  not depend on an uncommitted, platform-specific file.

No additional actionable defect was found in the bounded publication scope.
The BGC0002290 pair remains seed-only because preparation and exact biological
origin cannot be settled from accessible abstracts. That gap is not normalized
as a confirmed contradiction. All four observations remain partial.

## Challenges Applied

- Re-read all four complete owners, source member indices, exact keys, stored
  charges, history, separate producer/locus grades and computed classifications.
  The schema defines the locus link in relation to the compound, supporting
  an exact-product question without confusing it with native-organism production.
- Confirmed four distinct keys and one-based source indices. Equal generic
  labels and shared BGCs do not authorize owner merging or name invention.
- Rechecked the SI's methods and proposed-mechanism caption. Do not imply all
  50 SI pages or raw spectra were reanalysed. A 2018 main-page recheck failed
  at an inaccessible identity-provider redirect; no alternate retrieval followed.
- The official JCM catalogue equates JCM1740 and NRRL181. Interpreting literal
  SI JMC1740 as a transposition is an inference, not a new strain-mismatch finding.
- Preserved source assertions and uncertainty: no computed class is promoted
  to experimental fact; no natural/engineered status or native taxon is changed.
- Replayed all nine local inventory joins with pinned chemistry. ChEBI origin
  matching is through ChEBI IDs; empty and malformed join inputs are tested.
  Wrong or out-of-bounds compound indices fail closed.
- The ignored-inclusive filesystem delta audit confirms all 3,115 owners,
  243 graph components and 174 files in the 87 prior canonical pairs are unchanged.
  New evidence excludes full articles, copied abstracts and the SI PDF.
- Checks retain actual timestamps, failed setup attempts and rejected drafts.
  A late redundant draft-generation preflight hit an existing output-index
  filename; it did not overwrite the index or any canonical review.

Local corpus QC is baseline validation of unchanged scientific inputs, not a
claim that later publication files were collected by that original test run.
Focused packet tests and canonical review checks cover the additions. Exact-head
PR and merge-group checks remain mandatory before merge; their success cannot
close the two scientific findings or promote native records.
