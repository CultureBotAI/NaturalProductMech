# Bacilysin: scoped resolution of nonexact cross-references

- Review: 20261013T143632Z-bacilysin-2-xref-resolution
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T14:21:23.894966Z
- Finished UTC: 2026-10-13T14:36:32.930846Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolve the two nonexact external equivalence links only. Preserve historical source assertions, unresolved chemistry and all campaign coverage.

## Scope And Provenance

One exact owner, bounded predecessor F1 disposition. Campaign remains3115 owners/243 components,18 partially reviewed owners and zero completed scientific reviews.

Selection: Explicit issue911 and predecessor finding; not a new population sample.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 115e3c962ac60ff68abc8f0748769ee20a9cfd57.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5044e5068f | data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml | generated | bacilysin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| seed-dry | passed | True | naturalproductmech:mibig-5044e5068f | Actual command result retained with times and exact log hash. |
| canary | passed | True | naturalproductmech:mibig-5044e5068f | Actual command result retained with times and exact log hash. |
| focused | passed | True | naturalproductmech:mibig-5044e5068f | 55 focused xref and historical-archive tests passed. |
| strict | passed | True | naturalproductmech:mibig-5044e5068f | Actual command result retained with times and exact log hash. |
| scope-audit | passed | True | naturalproductmech:mibig-5044e5068f | Actual command result retained with times and exact log hash. |
| render | passed | True | naturalproductmech:mibig-5044e5068f | Actual command result retained with times and exact log hash. |
| docs-stats | failed | False | naturalproductmech:mibig-5044e5068f | Initial check reported stale generated discussion counts; docs-stats-write regenerated them. |
| docs-stats-write | passed | True | naturalproductmech:mibig-5044e5068f | Actual command result retained with times and exact log hash. |
| qc | failed | False | naturalproductmech:mibig-5044e5068f | Initial sandbox-only QC stopped at pinned governance DNS; superseded by qc-final. |
| qc-network | failed | False | naturalproductmech:mibig-5044e5068f | QC read the stale README while generation was running; superseded after generation completed. |
| qc-final | passed | True | naturalproductmech:mibig-5044e5068f | Full authoritative QC passed after generation completed; exact output retained. |
| Whole-record primary chemistry and experiment verification | unavailable | True | naturalproductmech:mibig-5044e5068f | Inherited full-text/stereochemistry/occurrence gaps remain. No blocked source was retried; whole-record scientific completion and native status promotion are not justified. |

## Scientific And Domain Assessments

### Exact chemical equivalence at supported stereo resolution

grounding: supported. Targets: naturalproductmech:mibig-5044e5068f.

Withholding both links removes the confirmed overstatement without guessing an authority or filling unknown stereocenters.

### Maintained inputs and bounded generated changes

provenance: supported. Targets: naturalproductmech:mibig-5044e5068f.

Source-row pins, original assertions and historical/current NPAtlas differences remain auditable; unrelated scientific claims, records, components and old reviews are unchanged.

### Primary experimental and exact-isolate identity support

completeness: unknown. Targets: naturalproductmech:mibig-5044e5068f.

Whole-record primary support remains partial. The1993 reassignment, source stereo disagreement and occurrence claims were not newly adjudicated by this xref remediation.

## Findings

### F1: Both imported xrefs exceed exact chemical equivalence

major / resolved / confirmed; issue key: bacilysin-BGC0000888-nonexact-pubchem-npatlas-xrefs.

PubChem160175 encodes the different JJOS anhydride connectivity. NPAtlasNPA015870 has XFOU connectivity but keyNWQN with two additional stereo assignments, not owner keyPCPU. Both are asserted as exact xrefs by the generated owner, contrary to the exact-equivalence contract. Neither formula agreement nor a shared compound name is sufficient. NPAtlas historical version1 and its embedded ClassyFire payload do match the owner, but the unversioned xref points to a current version2 structure with a different key; retain this historical context in any qualification.

Disposition: Both nonexact xrefs are withheld through complete-row-pinned maintained decisions and regenerated discussions. Scope audit, focused regressions and full QC pass. This resolves only equivalence overstatement, not primary stereochemistry, occurrence evidence or the sibling identity blocker.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| previous | reviews/structured/20261013T140252Z-bacilysin-2/review.yaml; F1 and its chemistry/primary-evidence limitations | supports | Original confirmed nonexact-xref finding is preserved byte-identically. Only this finding is reassessed. |
| owner | data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml; Complete resolved owner plus raw YAML; xrefs, discussions and history | supports | The two exact-equivalence xrefs are withheld. Source assertions and historical/current NPAtlas context remain in two attributed discussions; identity, all other claims and SEEDED status are unchanged. |
| table | curation/mibig_xref_exclusions.tsv; Two BGC0000888:1 decisions | supports | Both decisions pin the complete original source row bb86b4afe26dc6155af06d704d3ea0fc7f50fc98a46fa25d4f590628419c89b7 and literal xrefs. The raw inventory is unchanged. |
| consumer | src/naturalproductmech/curate/xref_exclusions.py; Literal IDs and complete-source validation | supports | Only literal PubChem and six-digit NPAtlas IDs are supported; missing, duplicate, malformed and drifted decisions fail. Existing seeder checks prevent reintroduction and unapplied decisions. |
| chemistry | reviews/evidence/20261013-bacilysin/artifacts/chemistry.json.gz; Checksum-pinned compressed RDKit calculation from inspected source snapshots | supports | Owner XFOU-PCPU has peptide connectivity; PubChem160175 is the JJOS anhydride. NPAtlas current XFOU-NWQN adds two assigned centers. This justifies withholding equivalence without selecting a biological assignment. |
| history | reviews/evidence/20261013-bacilysin/artifacts/reassignment-chemistry.json.gz; Checksum-pinned historical/current NPAtlas representation comparison | supports | Historical version1 and embedded ClassyFire match the owner; current version2 differs. Database history is not an independent experimental assignment. |
| validation | reviews/evidence/20261013-bacilysin-remediation/manifest.json; Checksums, commands, times, exit codes and log links for every retained check | supports | Full native QC, focused regressions, strict target validation and exhaustive scope audit passed. Earlier uv-cache/DNS/stale-statistics failures are retained, not relabeled. |
| scope | reviews/evidence/20261013-bacilysin-remediation/artifacts/scope-audit.json.gz; Gitignore-independent owner/component enumeration and structured claim comparison | supports | All3115 owners and243 components remain; only this owner changed, limited to two xrefs, two discussions and one history event. All25 prior observations and raw inventories are unchanged. |
| reinspection | reviews/evidence/20261013-bacilysin-remediation/post-commit/reassessment.json; Post-commit canonical inspection and byte-identical source reassessment | supports | All19 captured input bytes and exact target metadata are identical after commit. Re-read current owner, decisions, consumer and retained chemistry/scope checks; the bounded xref disposition and all remaining scientific limitations are unchanged. |

## Limits And Additional Notes

- A scoped partial successor, not a whole-record or corpus scientific pass. All193 historical source-access limits remain.
- Current owner/source inputs were captured and checked in the working tree; hashes do not claim these changes existed at the base commit.
- The original25 observations remain immutable; this26th observation adds no newly assessed owner and completes no whole scientific review.
- The sibling anhydride identity blocker remains open as GitHub910; no replacement, owner merger, claim transfer or REVIEWED promotion.
- Fresh full QC covers implementation and the historical archive. Final successor contract checks and PR/merge-group CI follow separately.
- An unsaved draft was rejected after the implementation commit moved HEAD. Canonical reinspection and explicit reassessment proved all19 reviewed inputs byte-identical; the final source base is the recaptured commit, not a silent hash refresh.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T143632Z-bacilysin-2-xref-resolution
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Bacilysin: scoped resolution of nonexact cross-references'
started_at: '2026-10-13T14:21:23.894966Z'
finished_at: '2026-10-13T14:36:32.930846Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant implemented and adversarially checked the changes;
    not an independent reviewer.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Resolve the two nonexact external equivalence links only. Preserve historical
  source assertions, unresolved chemistry and all campaign coverage.
source:
  git_revision: 115e3c962ac60ff68abc8f0748769ee20a9cfd57
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: 21f15282d9684d75bd9146dd08087d257500ff1c0f4307d4612db8f95450c63f
    role: context
  - path: data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml
    sha256: ca47263447870a484802ba0af85f8e97e2df10aadb5c6591905a9a05305458bc
    role: target
  - path: data/raw/chebi_structures.tsv
    sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
    role: context
  - path: data/raw/lotus_occurrences.tsv
    sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
    role: context
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: docs/CURATION.md
    sha256: 245df036e09a00a2f92a5f78c70eadb210cef7d70046e8ee35377a9e636cd30b
    role: context
  - path: docs/HARMONIZATION.md
    sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
    role: context
  - path: docs/record-review-profile.md
    sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/evidence/20261013-bacilysin/artifacts/chemistry.json.gz
    sha256: d65984799d98453bc5367cd00feb10172f87756b94525a6ec63f4c359b856f50
    role: context
  - path: reviews/evidence/20261013-bacilysin/artifacts/reassignment-chemistry.json.gz
    sha256: c274cec28c0f5002a88ed4dc68fee2a4da27549ee8ccaea2c2e2cceb25e09f99
    role: context
  - path: reviews/evidence/20261013-bacilysin/manifest.json
    sha256: aa269cb5e20b1524cb14c9c2cf5f3b700c1b55ea0348f1b73402e4b5d0b30a8b
    role: context
  - path: reviews/structured/20261013T140252Z-bacilysin-2/review.yaml
    sha256: 67536a5182bf1a8f74e05462ff6bcc1b5d2f42576ee23c1af331dfc3c09e56e9
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: tests/test_bacilysin_review_archive.py
    sha256: f32e78b83b09e1a82b1c69a885719717e12b7eb4afb10b1ae6124fb1abe3116c
    role: context
  - path: tests/test_xref_exclusions.py
    sha256: 3f26bef1b535e782a8ef33b3133f7a9172b03cfb5188cddc3c8a2ff55899dc48
    role: context
targets:
- target_id: naturalproductmech:mibig-5044e5068f
  path: data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml
  label: bacilysin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Imported structure-organism-reference triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned ChEBI grounding inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Pinned ChEBI occurrence inventory
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned sibling exact-structure joins
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: LOTUS extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented exact-context method corrections
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented pinned strain qualifications
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Implemented exact-row-pinned PubChem xref exclusions
scope:
  description: One exact owner, bounded predecessor F1 disposition. Campaign remains3115
    owners/243 components,18 partially reviewed owners and zero completed scientific
    reviews.
  selection: Explicit issue911 and predecessor finding; not a new population sample.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5044e5068f
checks:
- check_id: seed-dry
  name: seed-dry
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Actual command result retained with times and exact log hash.
- check_id: canary
  name: canary
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only naturalproductmech:mibig-5044e5068f
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Actual command result retained with times and exact log hash.
- check_id: focused
  name: focused
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_xref_exclusions.py tests/test_bacilysin_review_archive.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: 55 focused xref and historical-archive tests passed.
- check_id: strict
  name: strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Actual command result retained with times and exact log hash.
- check_id: scope-audit
  name: scope-audit
  status: passed
  required: true
  command: .venv/bin/python /private/tmp/npmech-bacilysin-publication-CBDI29/scope_audit.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Actual command result retained with times and exact log hash.
- check_id: render
  name: render
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Actual command result retained with times and exact log hash.
- check_id: docs-stats
  name: docs-stats
  status: failed
  required: false
  command: .venv/bin/python scripts/check_docs.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Initial check reported stale generated discussion counts; docs-stats-write
    regenerated them.
- check_id: docs-stats-write
  name: docs-stats-write
  status: passed
  required: true
  command: .venv/bin/python scripts/check_docs.py --write
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Actual command result retained with times and exact log hash.
- check_id: qc
  name: qc
  status: failed
  required: false
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Initial sandbox-only QC stopped at pinned governance DNS; superseded by
    qc-final.
- check_id: qc-network
  name: qc-network
  status: failed
  required: false
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: QC read the stale README while generation was running; superseded after
    generation completed.
- check_id: qc-final
  name: qc-final
  status: passed
  required: true
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - validation
  summary: Full authoritative QC passed after generation completed; exact output retained.
- check_id: primary-fulltext
  name: Whole-record primary chemistry and experiment verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  summary: Inherited full-text/stereochemistry/occurrence gaps remain. No blocked
    source was retried; whole-record scientific completion and native status promotion
    are not justified.
evidence:
- evidence_id: previous
  kind: record_content
  reference: reviews/structured/20261013T140252Z-bacilysin-2/review.yaml
  locator: F1 and its chemistry/primary-evidence limitations
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: Original confirmed nonexact-xref finding is preserved byte-identically.
    Only this finding is reassessed.
  snapshot_sha256: 67536a5182bf1a8f74e05462ff6bcc1b5d2f42576ee23c1af331dfc3c09e56e9
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/amino_acids_and_peptides/bacilysin-2.yaml
  locator: Complete resolved owner plus raw YAML; xrefs, discussions and history
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: The two exact-equivalence xrefs are withheld. Source assertions and historical/current
    NPAtlas context remain in two attributed discussions; identity, all other claims
    and SEEDED status are unchanged.
  snapshot_sha256: ca47263447870a484802ba0af85f8e97e2df10aadb5c6591905a9a05305458bc
- evidence_id: table
  kind: record_content
  reference: curation/mibig_xref_exclusions.tsv
  locator: Two BGC0000888:1 decisions
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: Both decisions pin the complete original source row bb86b4afe26dc6155af06d704d3ea0fc7f50fc98a46fa25d4f590628419c89b7
    and literal xrefs. The raw inventory is unchanged.
  snapshot_sha256: 21f15282d9684d75bd9146dd08087d257500ff1c0f4307d4612db8f95450c63f
- evidence_id: consumer
  kind: record_content
  reference: src/naturalproductmech/curate/xref_exclusions.py
  locator: Literal IDs and complete-source validation
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: Only literal PubChem and six-digit NPAtlas IDs are supported; missing,
    duplicate, malformed and drifted decisions fail. Existing seeder checks prevent
    reintroduction and unapplied decisions.
  snapshot_sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
- evidence_id: chemistry
  kind: validation
  reference: reviews/evidence/20261013-bacilysin/artifacts/chemistry.json.gz
  locator: Checksum-pinned compressed RDKit calculation from inspected source snapshots
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: Owner XFOU-PCPU has peptide connectivity; PubChem160175 is the JJOS anhydride.
    NPAtlas current XFOU-NWQN adds two assigned centers. This justifies withholding
    equivalence without selecting a biological assignment.
  snapshot_sha256: d65984799d98453bc5367cd00feb10172f87756b94525a6ec63f4c359b856f50
- evidence_id: history
  kind: validation
  reference: reviews/evidence/20261013-bacilysin/artifacts/reassignment-chemistry.json.gz
  locator: Checksum-pinned historical/current NPAtlas representation comparison
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: Historical version1 and embedded ClassyFire match the owner; current version2
    differs. Database history is not an independent experimental assignment.
  snapshot_sha256: c274cec28c0f5002a88ed4dc68fee2a4da27549ee8ccaea2c2e2cceb25e09f99
- evidence_id: validation
  kind: validation
  reference: reviews/evidence/20261013-bacilysin-remediation/manifest.json
  locator: Checksums, commands, times, exit codes and log links for every retained
    check
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: Full native QC, focused regressions, strict target validation and exhaustive
    scope audit passed. Earlier uv-cache/DNS/stale-statistics failures are retained,
    not relabeled.
  snapshot_sha256: 06e0db4290c1a8a1815f46b1fe95a71222745e4fef09baaacd9e16cafcba1755
- evidence_id: scope
  kind: validation
  reference: reviews/evidence/20261013-bacilysin-remediation/artifacts/scope-audit.json.gz
  locator: Gitignore-independent owner/component enumeration and structured claim
    comparison
  accessed_at: '2026-10-13T14:35:01.382075Z'
  support: supports
  summary: All3115 owners and243 components remain; only this owner changed, limited
    to two xrefs, two discussions and one history event. All25 prior observations
    and raw inventories are unchanged.
  snapshot_sha256: 1e3ebaa1019d5699f9e809c74610956d8e442b0651796b224016d4ec82b27db5
- evidence_id: reinspection
  kind: validation
  reference: reviews/evidence/20261013-bacilysin-remediation/post-commit/reassessment.json
  locator: Post-commit canonical inspection and byte-identical source reassessment
  accessed_at: '2026-10-13T14:36:32.930846Z'
  support: supports
  snapshot_sha256: 727fc303a5a295ee5031003052ca864610fc4654030badede7e876b4ba9b5125
  summary: All19 captured input bytes and exact target metadata are identical after
    commit. Re-read current owner, decisions, consumer and retained chemistry/scope
    checks; the bounded xref disposition and all remaining scientific limitations
    are unchanged.
assessments:
- assessment_id: equivalence
  area: grounding
  topic: Exact chemical equivalence at supported stereo resolution
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - owner
  - table
  - consumer
  - chemistry
  - history
  summary: Withholding both links removes the confirmed overstatement without guessing
    an authority or filling unknown stereocenters.
- assessment_id: scope
  area: provenance
  topic: Maintained inputs and bounded generated changes
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - scope
  - validation
  - previous
  - reinspection
  summary: Source-row pins, original assertions and historical/current NPAtlas differences
    remain auditable; unrelated scientific claims, records, components and old reviews
    are unchanged.
- assessment_id: remaining
  area: completeness
  topic: Primary experimental and exact-isolate identity support
  outcome: unknown
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  evidence_ids:
  - previous
  - history
  summary: Whole-record primary support remains partial. The1993 reassignment, source
    stereo disagreement and occurrence claims were not newly adjudicated by this xref
    remediation.
findings:
- finding_id: F1
  issue_key: bacilysin-BGC0000888-nonexact-pubchem-npatlas-xrefs
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Both imported xrefs exceed exact chemical equivalence
  description: PubChem160175 encodes the different JJOS anhydride connectivity. NPAtlasNPA015870
    has XFOU connectivity but keyNWQN with two additional stereo assignments, not
    owner keyPCPU. Both are asserted as exact xrefs by the generated owner, contrary
    to the exact-equivalence contract. Neither formula agreement nor a shared compound
    name is sufficient. NPAtlas historical version1 and its embedded ClassyFire payload
    do match the owner, but the unversioned xref points to a current version2 structure
    with a different key; retain this historical context in any qualification.
  target_ids:
  - naturalproductmech:mibig-5044e5068f
  field_paths:
  - xrefs[0]
  - xrefs[1]
  evidence_ids:
  - previous
  - owner
  - table
  - consumer
  - chemistry
  - history
  - validation
  - scope
  - reinspection
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned original compound, producer and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Source extraction and provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source harmonization and generated record emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Complete-source-row-pinned exact-equivalence exclusions
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Validated literal PubChem and NPAtlas exclusion consumer
  rule_id: review-checklist:Equivalence; CLAUDE.md:an xref means the same structure
  native_severity: major
  normalization_reason: Wrong exact-equivalence grounding materially misidentifies
    the owner through external identifiers without establishing that its entire peptide
    connectivity is wrong.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T140252Z-bacilysin-2
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/911
  disposition_reason: Both nonexact xrefs are withheld through complete-row-pinned
    maintained decisions and regenerated discussions. Scope audit, focused regressions
    and full QC pass. This resolves only equivalence overstatement, not primary stereochemistry,
    occurrence evidence or the sibling identity blocker.
actions: []
limitations:
- A scoped partial successor, not a whole-record or corpus scientific pass. All193
  historical source-access limits remain.
- Current owner/source inputs were captured and checked in the working tree; hashes
  do not claim these changes existed at the base commit.
- The original25 observations remain immutable; this26th observation adds no newly
  assessed owner and completes no whole scientific review.
- The sibling anhydride identity blocker remains open as GitHub910; no replacement,
  owner merger, claim transfer or REVIEWED promotion.
- Fresh full QC covers implementation and the historical archive. Final successor
  contract checks and PR/merge-group CI follow separately.
- An unsaved draft was rejected after the implementation commit moved HEAD. Canonical
  reinspection and explicit reassessment proved all19 reviewed inputs byte-identical;
  the final source base is the recaptured commit, not a silent hash refresh.
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/908
- https://github.com/CultureBotAI/NaturalProductMech/issues/911
- https://github.com/CultureBotAI/NaturalProductMech/issues/910
```
