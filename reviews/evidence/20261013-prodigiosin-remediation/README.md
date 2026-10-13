# Prodigiosin Strain Remediation

PR #883 corrects only the producer strain omissions tracked in #885 and #887:
ATCC 39006, ATCC 274 and S4059. A complete-source-row-pinned curation input feeds
the guarded seeder. Database evidence remains separate from the curator's
interpretation; taxon IDs and producer/BGC evidence grades are unchanged.

`remediation-audit.json` checks every owner and component, including ignored
files: exactly two owners change, 3,113 remain byte-identical, and all 243
components are unchanged. Each changed owner adds only strain, curator evidence
and one seed event. Identity, occurrences, BGCs, scientific status and prior
history are preserved.

Issue #888 was found in the rendered output: the producer table hid strain
context. The template now exposes the strain and its evidence details; reference
labels are deduplicated without collapsing source evidence. Focused tests cover
absent/present strains, escaped content and source immutability. An initial
deduplication-test failure and its passing retry are retained.

The original reviews and their baseline archive are immutable. Separate
successors resolve only F2 in each review, not the whole compound. Occurrence
issues #884 and #886 remain open, as do exact-chemistry and access-limited checks.
No native REVIEWED status is assigned.

Issue #889 fixes an isolated structure-correction test fixture that retained
unrelated strain qualifications after narrowing its source inventory. The
production missing-target rejection remains strict. The initial full QC failure
and a fresh full-gate retry are retained, alongside focused test receipts.

Receipts retain actual commands, times, exits and log hashes. The detached
worktree used for successor inspection is based on the durable main ancestor,
with exact remediated input bytes, so squash merge cannot discard the review base.
