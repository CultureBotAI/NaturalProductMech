# Adversarial Self-Review

PR #969; reviewed initial head `f0e15e528b2845dc9220166d43ed88cf4ab66965`
and the subsequent local fix for #970. Reviewer: Codex, the same assistant that
implemented the changes. This is a separate adversarial pass, not independent
peer review or scientific sign-off.

## Finding

Minor provenance gap, #970: the evidence replay pinned source TSVs to the Git
base but checked owner snapshots only against their manifest. A standalone
replay did not independently bind those snapshots to the historical owner files.

Addressed with an explicit historical YAML comparison before replay. It rejects
any changed owner field and any external graph refs. Five tests cover valid
snapshots, changed label/chemistry/graph content, and incomplete graph resolution.
The hardened pinned-RDKit replay reproduces the retained audit exactly.

## Other Checks

- Source pins cover every parsed field; duplicate, missing, drifted or unemitted
  LOTUS decisions fail. Exclusion occurs before deduplication, capping and facets.
- Other taxa, citations and structures survive. Stale generated discussion
  answers cannot replace the table-owned adjudication.
- All 14 historical assay rows share the confirmed nonexact CID. Withholding
  them does not deny their experiments or transfer them to another owner.
- The QS graph is removed through a guarded writer/event; QTQ direct binding is
  retained with qualified construct mapping and a separate database citation.
- No owner merge, structure replacement, producer-grade upgrade, raw source
  rewrite, scientific-status promotion or earlier-review edit occurs.
- Exact delta audit preserves 3,113 unrelated owners, 243 components and all 71
  earlier review bundles. Focused correction tests: 213 passed. Replay tests: 5
  passed. See correction-checks.json and publication CI for complete gate results.

No additional actionable defect was found in this bounded pass. Primary product
identity, remaining source scope and any migration remain open in #968; the PR
does not claim to resolve them. The issue is not silently closed by deterministic
validation or by this self-review.
