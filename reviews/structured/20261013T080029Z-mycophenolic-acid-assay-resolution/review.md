# Mycophenolic acid: scoped assay finding resolution

- Review: 20261013T080029Z-mycophenolic-acid-assay-resolution
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T08:00:27.009296Z
- Finished UTC: 2026-10-13T08:00:29.106406Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

F1 and F2 resolved against the regenerated owner, maintained transforms and tests. This is a scoped disposition, not a completed scientific review of the compound or its mechanisms.

## Scope And Provenance

CHEBI:168396 assay-import remediation only. Full campaign remains 3115 owners, now 243 components after storage-only migration; eight unique owners partially assessed, zero complete, 3107 unassessed.

Selection: Reassess the exact target and both predecessors from 20261013T073122Z-mycophenolic-acid.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 988766b35bae770331e9ec46018158654a88b4b7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:168396 | data/natural_products/polyketides/mycophenolic-acid.yaml | generated | mycophenolic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | CHEBI:168396 | All native QC gates passed on the remediated tree before this successor was saved. |
| Canonical inspection | passed | True | CHEBI:168396 | Reinspected current owner and maintained implementation inputs; no old hashes were silently updated. |
| Remaining whole-record scientific checks | skipped | True | CHEBI:168396 | Primary papers, current BGC status, all occurrence citations, pinned chemistry, all xrefs, sequence/construct boundaries and every graph edge remain incompletely assessed. Inherited access stops retained. |
| Final archive regressions | passed | True | CHEBI:168396 | 22 tests passed after the checkpoint-state correction and its final regression assertions. |

## Scientific And Domain Assessments

### Outcome, endpoint and classification preservation

quantity: supported. Targets: CHEBI:168396.

Both original defects are fixed at the maintained seeder and verified on all retained mycophenolic-acid observations; source values and evidence remain intact.

### Numeric results with outcome calls

representation: supported. Targets: CHEBI:168396.

Renderer regression #880 was found in the adversarial pass and fixed; numeric, zero, call-only and measurement-only tests pass.

### Scientific review completeness

completeness: unknown. Targets: CHEBI:168396.

Earlier unverified identity equivalences, primary/source-currentness and mechanism checks are not resolved by assay-import fixes.

## Findings

### F1: AID1650 cytotoxicity counterscreen is labelled antiviral

major / resolved / confirmed; issue key: pubchem-AID1650-cytotoxicity-labelled-antiviral.

The seeder matches anti-viral before cytotoxicity in the assay title. The official protocol measures mock-infected Vero E6 viability; the 4.61 uM value is CC50, not antiviral potency. This finding does not deny antiviral activity supported by other assays or the sibling link.

Disposition: The maintained seeder and guarded regenerated owner satisfy the scoped acceptance checks. Focused negative-case regressions and full QC passed; no scientific status promotion or resolution of unrelated source uncertainty.

### F2: Quantitative assay observations lose source outcome and endpoint context

major / resolved / confirmed; issue key: pubchem-quantitative-outcome-endpoint-loss.

All 25 retained numeric observations omit source outcome: 11 Active, 13 Inconclusive, 1 Inactive. Twenty-four omit measurement_type, losing names such as CC50 and Potency. AID624296 retains 0.3663 uM without its Inactive outcome; seven Inconclusive rows carry CYTOTOXIC. Numeric values alone must not become positive activity support. The extractor retains these fields; the loss is in the seeder. Inconclusive is not intermediate susceptibility, and Potency must not be guessed to mean IC50.

Disposition: The maintained seeder and guarded regenerated owner satisfy the scoped acceptance checks. Focused negative-case regressions and full QC passed; no scientific status promotion or resolution of unrelated source uncertainty.

## Recommended Actions And Acceptance Checks

### complete-source-review

Continue the incomplete exact-source scientific review and preserve all inherited access stops. Save a new immutable observation for any further finding or disposition.

- Verify the remaining primary, chemical, strain, construct, xref, occurrence and BGC claims at their exact scope before any whole-record scientific pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| previous | reviews/structured/20261013T073122Z-mycophenolic-acid/review.yaml | supports | Original partial observation remains byte-identical. This successor resolves only F1/F2, not all scientific checks. |
| owner | data/natural_products/polyketides/mycophenolic-acid.yaml | supports | All 25 retained numeric observations now carry outcomes: 11 ACTIVE, 13 NOT_DETERMINED with source Inconclusive, one INACTIVE. CC50/Potency retain exact source names with OTHER. AID1650 is CYTOTOXIC; inactive and inconclusive rows cannot carry positive activity classes. ANTIVIRAL summary remains independently backed by the sibling link. |
| seeder | scripts/seed_from_sources.py | supports | Verified AID1650 title-specific classification, ambiguous-title abstention, outcome preservation, OTHER endpoint fallback, and ACTIVE-only class/summary support. |
| renderer | scripts/render_pages.py | supports | Result cells retain measurement and outcome together; expanded source fields preserve exact endpoint/outcome notes. |
| regeneration | reviews/evidence/20261013-mycophenolic-remediation/regeneration-audit.json | supports | Historical comparison of all 3115 owners: 116 changed. Assay values, units, order/cap, evidence references and chemical identities preserved. The 242 existing graph components are byte-identical; one final inline staurosporine graph was moved without changing resolved graph content or order, yielding 243 components. Existing history is preserved and guarded mutations append events. |
| qc | reviews/evidence/20261013-mycophenolic-remediation/qc.log | supports | Actual full native QC log and matching receipt. Tests, strict schema, graph ownership, provenance, source queue, generated site, reproduction, corpus and documentation checks passed; deterministic success is not scientific completeness. |
| archive-final | reviews/evidence/20261013-mycophenolic-remediation/archive-final-v2.log | supports | The subsequent checkpoint metadata correction and strengthened state assertions passed all 22 archive tests. This focused rerun covers the final test/metadata edits made after the full-QC test phase. |

## Limits And Additional Notes

- Partial scoped disposition only; the native SEEDED status remains unchanged.
- Self-review by the same assistant/thread, not independent review.
- The original eight-owner campaign checkpoint predates remediation and retains historical hashes/findings. This successor closes only the two linked finding heads; no unassessed owner becomes reviewed.
- The 242-to-243 component change is storage-only, not a new natural product, mechanism or reviewed owner.
- Inspected and saved from a detached main-base worktree populated with the exact remediated input bytes. Source state is an explicit working-tree attestation at the durable main ancestor, not a claim that those input bytes existed in that commit; this avoids depending on discarded feature-branch commits after squash merge.
- Previously stopped primary papers and aliases were not retried; all prior scientific access limits remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T080029Z-mycophenolic-acid-assay-resolution
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Mycophenolic acid: scoped assay finding resolution'
started_at: '2026-10-13T08:00:27.009296Z'
finished_at: '2026-10-13T08:00:29.106406Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread that previously curated this repository;
    a separate adversarial pass, not an independent reviewer.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: F1 and F2 resolved against the regenerated owner, maintained transforms and
  tests. This is a scoped disposition, not a completed scientific review of the compound
  or its mechanisms.
source:
  git_revision: 988766b35bae770331e9ec46018158654a88b4b7
  state: working_tree
  inputs:
  - path: data/natural_products/polyketides/mycophenolic-acid.yaml
    sha256: 8005e7693de3eb281ef2cfbaccc0f3f9b7ea19f7ee661f9dcd703fc805a30aaf
    role: target
  - path: docs/CURATION.md
    sha256: 21ad646576ece0cb33a7a6746c22382c71b60f6ae991a422a537b8454c1216fb
    role: context
  - path: reviews/evidence/20261013-mycophenolic-remediation/archive-final-v2.log
    sha256: 77ff04ecf2098356591ec7c8070be3c80443607dd1f0d196a695082f4325ea40
    role: context
  - path: reviews/evidence/20261013-mycophenolic-remediation/qc.log
    sha256: ad16e9406f79e59e47f36fdbd47b625b9c88714329de7b715bb0fe3aba0fda47
    role: context
  - path: reviews/evidence/20261013-mycophenolic-remediation/qc.receipt.json
    sha256: e038ed422072c6ddf97cdc1b9a69cdd042dfca26044cd5e53d214ac81f64e6b9
    role: context
  - path: reviews/evidence/20261013-mycophenolic-remediation/regeneration-audit.json
    sha256: 2626d59ff897ce19676fb5fd0d9aef869a36d0ca7e5d99521fddbff842914cad
    role: context
  - path: reviews/structured/20261013T073122Z-mycophenolic-acid/review.yaml
    sha256: 0b4aa0627b9555b3fa74b89ddbdc397d630635dbdd6b9fbe8270c0c82a2b354f
    role: context
  - path: scripts/render_pages.py
    sha256: fa675a391845df3c6177a3e4e03c8f7d8d27779d07d6d78a6133257cd16ee0c5
    role: context
  - path: scripts/seed_from_sources.py
    sha256: a3129e6f597cd56fde18ce815c431e78d8ba7a174c9d07cfc643855ef4b98e17
    role: context
  - path: tests/test_corpus_integrity.py
    sha256: d5a9a5f6ac3864a37c35ca31282ba8e95ee5836bf31d2f41246d72901e1c64f2
    role: context
  - path: tests/test_render_pages.py
    sha256: 7c95d8fcc92fd1de20a9d03b6ab0d4297d2b4fcb6f22bb9a4dcd62df3f43f11a
    role: context
  - path: tests/test_review_evidence_archive.py
    sha256: 737b0654fda5dba5b4574b0260a4e3f7a0f732909b4e38ba1ded6326ff7edea0
    role: context
  - path: tests/test_seed_skeleton.py
    sha256: 0b5b83bfc4220637a88dcb9d685fe6ba347087a14fdbca8deeb27a37f44f3b00
    role: context
targets:
- target_id: CHEBI:168396
  path: data/natural_products/polyketides/mycophenolic-acid.yaml
  label: mycophenolic acid
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported exact chemical, producer and BGC assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Imported ChEBI identity and definition
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Imported organism-reference triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Imported quantitative assay rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: Structured assay source extraction; classification is owned by the seeder
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/bindingdb_targets.tsv
    role: Target source inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned same-structure sibling link
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Harmonization and generated emission
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/mycophenolic-acid.yaml
    role: Curator-owned inline graphs/discussions/history through guarded writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/HPNSFSBZBAHARI-RUDMXATFSA-N/mycophenolic-acid-nrrl864-core-biosynthesis-reference.yaml
    role: Exact-owner graph component maintained through guarded bundle writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/HPNSFSBZBAHARI-RUDMXATFSA-N/mycophenolic-acid-ibt23078-core-biosynthesis-reference.yaml
    role: Exact-owner graph component maintained through guarded bundle writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/HPNSFSBZBAHARI-RUDMXATFSA-N/mycophenolic-acid-pb864-sidechain-reconstitution.yaml
    role: Exact-owner graph component maintained through guarded bundle writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/causal_graphs/HPNSFSBZBAHARI-RUDMXATFSA-N/mycophenolic-acid-mpah-prime-structural-reference.yaml
    role: Exact-owner graph component maintained through guarded bundle writer
scope:
  description: CHEBI:168396 assay-import remediation only. Full campaign remains 3115
    owners, now 243 components after storage-only migration; eight unique owners partially
    assessed, zero complete, 3107 unassessed.
  selection: Reassess the exact target and both predecessors from 20261013T073122Z-mycophenolic-acid.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:168396
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  target_ids:
  - CHEBI:168396
  evidence_ids:
  - qc
  summary: All native QC gates passed on the remediated tree before this successor
    was saved.
- check_id: canonical-inspect
  name: Canonical inspection
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python
    scripts/record_review.py inspect --targets /private/tmp/npmech-mpa-review-current-NPq2SH/targets.json
    --input scripts/seed_from_sources.py --input scripts/render_pages.py --input docs/CURATION.md
    --input tests/test_seed_skeleton.py --input tests/test_render_pages.py --input
    tests/test_corpus_integrity.py --input reviews/structured/20261013T073122Z-mycophenolic-acid/review.yaml
    --input reviews/evidence/20261013-mycophenolic-remediation/regeneration-audit.json
    --input reviews/evidence/20261013-mycophenolic-remediation/qc.log --input reviews/evidence/20261013-mycophenolic-remediation/qc.receipt.json
    --input tests/test_review_evidence_archive.py --input reviews/evidence/20261013-mycophenolic-remediation/archive-final-v2.log
  exit_code: 0
  target_ids:
  - CHEBI:168396
  evidence_ids:
  - owner
  summary: Reinspected current owner and maintained implementation inputs; no old
    hashes were silently updated.
- check_id: remaining-science
  name: Remaining whole-record scientific checks
  status: skipped
  required: true
  target_ids:
  - CHEBI:168396
  summary: Primary papers, current BGC status, all occurrence citations, pinned chemistry,
    all xrefs, sequence/construct boundaries and every graph edge remain incompletely
    assessed. Inherited access stops retained.
- check_id: archive-final
  name: Final archive regressions
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_review_evidence_archive.py
  exit_code: 0
  target_ids:
  - CHEBI:168396
  evidence_ids:
  - archive-final
  summary: 22 tests passed after the checkpoint-state correction and its final regression
    assertions.
evidence:
- evidence_id: previous
  kind: prior_review
  reference: reviews/structured/20261013T073122Z-mycophenolic-acid/review.yaml
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: Original partial observation remains byte-identical. This successor resolves
    only F1/F2, not all scientific checks.
  snapshot_sha256: 0b4aa0627b9555b3fa74b89ddbdc397d630635dbdd6b9fbe8270c0c82a2b354f
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/polyketides/mycophenolic-acid.yaml
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: 'All 25 retained numeric observations now carry outcomes: 11 ACTIVE, 13
    NOT_DETERMINED with source Inconclusive, one INACTIVE. CC50/Potency retain exact
    source names with OTHER. AID1650 is CYTOTOXIC; inactive and inconclusive rows
    cannot carry positive activity classes. ANTIVIRAL summary remains independently
    backed by the sibling link.'
  snapshot_sha256: 8005e7693de3eb281ef2cfbaccc0f3f9b7ea19f7ee661f9dcd703fc805a30aaf
- evidence_id: seeder
  kind: record_content
  reference: scripts/seed_from_sources.py
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: Verified AID1650 title-specific classification, ambiguous-title abstention,
    outcome preservation, OTHER endpoint fallback, and ACTIVE-only class/summary support.
  snapshot_sha256: a3129e6f597cd56fde18ce815c431e78d8ba7a174c9d07cfc643855ef4b98e17
- evidence_id: renderer
  kind: record_content
  reference: scripts/render_pages.py
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: Result cells retain measurement and outcome together; expanded source fields
    preserve exact endpoint/outcome notes.
  snapshot_sha256: fa675a391845df3c6177a3e4e03c8f7d8d27779d07d6d78a6133257cd16ee0c5
- evidence_id: regeneration
  kind: validation
  reference: reviews/evidence/20261013-mycophenolic-remediation/regeneration-audit.json
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: 'Historical comparison of all 3115 owners: 116 changed. Assay values, units,
    order/cap, evidence references and chemical identities preserved. The 242 existing
    graph components are byte-identical; one final inline staurosporine graph was
    moved without changing resolved graph content or order, yielding 243 components.
    Existing history is preserved and guarded mutations append events.'
  snapshot_sha256: 2626d59ff897ce19676fb5fd0d9aef869a36d0ca7e5d99521fddbff842914cad
- evidence_id: qc
  kind: validation
  reference: reviews/evidence/20261013-mycophenolic-remediation/qc.log
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: Actual full native QC log and matching receipt. Tests, strict schema, graph
    ownership, provenance, source queue, generated site, reproduction, corpus and
    documentation checks passed; deterministic success is not scientific completeness.
  snapshot_sha256: ad16e9406f79e59e47f36fdbd47b625b9c88714329de7b715bb0fe3aba0fda47
- evidence_id: archive-final
  kind: validation
  reference: reviews/evidence/20261013-mycophenolic-remediation/archive-final-v2.log
  accessed_at: '2026-10-13T08:00:29.106406Z'
  support: supports
  summary: The subsequent checkpoint metadata correction and strengthened state assertions
    passed all 22 archive tests. This focused rerun covers the final test/metadata
    edits made after the full-QC test phase.
  snapshot_sha256: 77ff04ecf2098356591ec7c8070be3c80443607dd1f0d196a695082f4325ea40
assessments:
- assessment_id: assays
  area: quantity
  topic: Outcome, endpoint and classification preservation
  outcome: supported
  summary: Both original defects are fixed at the maintained seeder and verified on
    all retained mycophenolic-acid observations; source values and evidence remain
    intact.
  target_ids:
  - CHEBI:168396
  evidence_ids:
  - previous
  - owner
  - seeder
  - regeneration
  - qc
- assessment_id: rendering
  area: representation
  topic: Numeric results with outcome calls
  outcome: supported
  summary: 'Renderer regression #880 was found in the adversarial pass and fixed;
    numeric, zero, call-only and measurement-only tests pass.'
  target_ids:
  - CHEBI:168396
  evidence_ids:
  - renderer
  - qc
- assessment_id: whole-record
  area: completeness
  topic: Scientific review completeness
  outcome: unknown
  summary: Earlier unverified identity equivalences, primary/source-currentness and
    mechanism checks are not resolved by assay-import fixes.
  target_ids:
  - CHEBI:168396
  evidence_ids:
  - previous
findings:
- finding_id: F1
  issue_key: pubchem-AID1650-cytotoxicity-labelled-antiviral
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: AID1650 cytotoxicity counterscreen is labelled antiviral
  description: The seeder matches anti-viral before cytotoxicity in the assay title.
    The official protocol measures mock-infected Vero E6 viability; the 4.61 uM value
    is CC50, not antiviral potency. This finding does not deny antiviral activity
    supported by other assays or the sibling link.
  target_ids:
  - CHEBI:168396
  field_paths:
  - bioactivities[0].activity_class
  evidence_ids:
  - previous
  - owner
  - seeder
  - regeneration
  - qc
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated assay transformation and activity summary
  rule_id: 'docs/CURATION.md: narrow evidence, measurement context, backed activity
    summaries'
  native_severity: major
  normalization_reason: Systemic source transformation can misrepresent measured activity
    while schema and reproduction gates pass.
  disposition_reason: The maintained seeder and guarded regenerated owner satisfy
    the scoped acceptance checks. Focused negative-case regressions and full QC passed;
    no scientific status promotion or resolution of unrelated source uncertainty.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T073122Z-mycophenolic-acid
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/877
- finding_id: F2
  issue_key: pubchem-quantitative-outcome-endpoint-loss
  category: quantity
  severity: major
  status: resolved
  certainty: confirmed
  title: Quantitative assay observations lose source outcome and endpoint context
  description: 'All 25 retained numeric observations omit source outcome: 11 Active,
    13 Inconclusive, 1 Inactive. Twenty-four omit measurement_type, losing names such
    as CC50 and Potency. AID624296 retains 0.3663 uM without its Inactive outcome;
    seven Inconclusive rows carry CYTOTOXIC. Numeric values alone must not become
    positive activity support. The extractor retains these fields; the loss is in
    the seeder. Inconclusive is not intermediate susceptibility, and Potency must
    not be guessed to mean IC50.'
  target_ids:
  - CHEBI:168396
  field_paths:
  - bioactivities
  - bioactivity_summary
  evidence_ids:
  - previous
  - owner
  - seeder
  - regeneration
  - qc
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated assay transformation and activity summary
  rule_id: 'docs/CURATION.md: narrow evidence, measurement context, backed activity
    summaries'
  native_severity: major
  normalization_reason: Systemic source transformation can misrepresent measured activity
    while schema and reproduction gates pass.
  disposition_reason: The maintained seeder and guarded regenerated owner satisfy
    the scoped acceptance checks. Focused negative-case regressions and full QC passed;
    no scientific status promotion or resolution of unrelated source uncertainty.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T073122Z-mycophenolic-acid
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/878
actions:
- action_id: complete-source-review
  finding_ids: []
  target_ids:
  - CHEBI:168396
  description: Continue the incomplete exact-source scientific review and preserve
    all inherited access stops. Save a new immutable observation for any further finding
    or disposition.
  ownership_note: Read-only research; native maintained-owner rules govern any later
    authorized curation.
  acceptance_checks:
  - Verify the remaining primary, chemical, strain, construct, xref, occurrence and
    BGC claims at their exact scope before any whole-record scientific pass.
limitations:
- Partial scoped disposition only; the native SEEDED status remains unchanged.
- Self-review by the same assistant/thread, not independent review.
- The original eight-owner campaign checkpoint predates remediation and retains historical
  hashes/findings. This successor closes only the two linked finding heads; no unassessed
  owner becomes reviewed.
- The 242-to-243 component change is storage-only, not a new natural product, mechanism
  or reviewed owner.
- Inspected and saved from a detached main-base worktree populated with the exact
  remediated input bytes. Source state is an explicit working-tree attestation at
  the durable main ancestor, not a claim that those input bytes existed in that commit;
  this avoids depending on discarded feature-branch commits after squash merge.
- Previously stopped primary papers and aliases were not retried; all prior scientific
  access limits remain in force.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T073122Z-mycophenolic-acid
  relationship: Scoped resolution of F1/F2; preserves all other limitations
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/879
```
