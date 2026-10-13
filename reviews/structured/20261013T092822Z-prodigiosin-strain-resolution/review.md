# prodigiosin (CHEBI:82758): scoped producer strain resolution

- Review: 20261013T092822Z-prodigiosin-strain-resolution
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T09:28:02.763862Z
- Finished UTC: 2026-10-13T09:28:22.631075Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolve only F2 and GitHub #887; the original major occurrence finding remains open. No completed scientific review is claimed.

## Scope And Provenance

Producer strain provenance only; 3115-owner campaign remains active, ten owners partial and zero complete.

Selection: Exact F2 follow-up from 20261013T085654Z-prodigiosin.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95b25be273d45a087df8d1262303713a2a2d8c17.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:82758 | data/natural_products/alkaloids/prodigiosin.yaml | generated | prodigiosin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| final-focus | failed | False | CHEBI:82758 | Initial renderer deduplication regression; fixed and superseded by the passing retry. |
| final-focus-retry | passed | True | CHEBI:82758 | Recorded native check; exact output and timing retained in the archive. |
| qc-remediation | failed | False | CHEBI:82758 | Isolated structure-correction fixture retained unrelated qualification rows; fixed without weakening production checks and superseded by qc-final. |
| qc-final | passed | True | CHEBI:82758 | Recorded native check; exact output and timing retained in the archive. |
| fixture-focus | passed | True | CHEBI:82758 | Recorded native check; exact output and timing retained in the archive. |
| render-final | passed | True | CHEBI:82758 | Recorded native check; exact output and timing retained in the archive. |
| archive-tests | passed | True | CHEBI:82758 | Recorded native check; exact output and timing retained in the archive. |

## Scientific And Domain Assessments

### Explicit strain scope and retained source assertion

evidence: supported. Targets: CHEBI:82758.

The generated producer has the source-supported strain, unchanged taxon/grade and original database evidence plus attributed curator interpretation.

### Whole-record scientific review

completeness: unknown. Targets: CHEBI:82758.

F1, chemical equivalence and access-limited occurrence checks are not resolved by adding strain context.

## Findings

### F2: Characterized producer claim omits strain S4059

minor / resolved / confirmed; issue key: prodigiosin-s4059-strain-provenance.

The BGC_CHARACTERIZED producer row gives P. rubra but no strain or strain-specific notes. Its cited study and genome are S4059-specific. Preserve that scope without changing the supported knockout grade or inventing a strain taxon identifier.

Disposition: The pinned maintained qualification now supplies the missing strain and separate curator evidence. Guarded regeneration, exhaustive unchanged-field audit, focused regressions and native QC pass. No identity, taxon, grade, occurrence or status changes; no whole-record sign-off.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://journals.asm.org/doi/10.1128/spectrum.01171-21; Results: BGC verification; Materials and Methods: culture, genome, deletion | supports | Results and methods identify S4059: in-frame pigC deletion abolishes the prodigiosin LC-MS signal. Culture/strain and CP045429 context support the native knockout grade, not species-wide generality. Residual extract activity is not a pure-compound assay. |
| previous | reviews/structured/20261013T085654Z-prodigiosin/review.yaml | supports | Immutable original observation; this successor resolves only F2. |
| owner | data/natural_products/alkaloids/prodigiosin.yaml | supports | Complete current owner read; explicit strains and separate evidence retained without broadening scope. |
| maintained-input | curation/mibig_producer_strains.tsv | supports | Complete raw-row pins and inspected source citations; no raw inventory mutation. |
| audit | reviews/evidence/20261013-prodigiosin-remediation/remediation-audit.json | supports | Ignored-inclusive audit of all 3115 owners and 243 components; only the two intended owners change. |
| validation | reviews/evidence/20261013-prodigiosin-remediation/qc-final.log | supports | Fresh full gate passed on the final implementation, including renderer and isolated fixture fixes. |

## Limits And Additional Notes

- Partial scoped disposition, not a whole-record pass. The native SEEDED status and all occurrence claims remain unchanged.
- The major occurrence finding F1 remains open; a newer scoped passing observation does not close it.
- All inherited access stops and exact pinned chemistry limitations remain. No primary full text was retrieved around an access restriction.
- The same assistant implemented and reviewed these changes; this is self-review, not an independent reviewer.
- Inspected and saved in a detached durable-main-base worktree populated with the exact remediated bytes. Working-tree hashes attest those bytes, not their existence in the base commit.
- Initial full QC failed on an isolated test fixture. Its receipt is retained; a fresh full QC run and focused retries validate the final implementation. The archive-lineage regression added afterward requires a focused check and final-head CI. Protected PR and merge-queue CI must cover the final committed head.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T092822Z-prodigiosin-strain-resolution
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'prodigiosin (CHEBI:82758): scoped producer strain resolution'
started_at: '2026-10-13T09:28:02.763862Z'
finished_at: '2026-10-13T09:28:22.631075Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread as prior repository work; direct source-checking
    pass, not an independent human or agent review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: 'Resolve only F2 and GitHub #887; the original major occurrence finding remains
  open. No completed scientific review is claimed.'
source:
  git_revision: 95b25be273d45a087df8d1262303713a2a2d8c17
  state: working_tree
  inputs:
  - path: curation/mibig_producer_strains.tsv
    sha256: 13341e78333d6efbb8a0331a675aa076d13a5830af8d5f860f743022a6c6268a
    role: context
  - path: data/natural_products/alkaloids/prodigiosin-2.yaml
    sha256: 9804386ec88d5cbe761543bc454c1830eb3bbae176d709a000063b752f777486
    role: context
  - path: data/natural_products/alkaloids/prodigiosin.yaml
    sha256: 730433d43289c7a4e119822bf7519b25934348a2d50b62fd3d661ab83880bc93
    role: target
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: docs/CURATION.md
    sha256: 4b9e28dde3917c1f6a45c5c4a1443459dc80504c06cf63198783d37c88e50f80
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/.gitattributes
    sha256: 45fb6649fd891d590100736ba94acef426f23223920447c41da4a7d7f276217b
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/README.md
    sha256: 15eb253f47e6ae3caa9a420b8740199bc68bfbeeecadd7e60276b0c25db150a3
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/archive-tests.log
    sha256: 453aa3c08a5b0a5f5985281c93ca147087548bbbb8e446b186caf5b5d62c88b4
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/archive-tests.receipt.json
    sha256: 35b83f16ff7e833512b9af058a9f3c796f0c5de6504747e21349bfd3ce9855f5
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/final-focus-retry.log
    sha256: d15d6250a9935c6a0975074735e92455d7a95525e86d46f85039a5082fe1bd03
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/final-focus-retry.receipt.json
    sha256: 55b16b18453063f98ad225645779536a22969613d8b4013d3863154034e128fd
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/final-focus.log
    sha256: fd6a8055a740616c32e877375c7b940db4ca3b592d8f121bb8dfe0095fd19aa0
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/final-focus.receipt.json
    sha256: c53419692cb7c6af2ac3949f6d910a585f28a42f5501828481976d70c7d6e856
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/fixture-focus.log
    sha256: 3f18797fb34dbe828cbf9b1137efb3077d76a4dd88d816fbf95eabd2e2317df7
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/fixture-focus.receipt.json
    sha256: b81bd6b65ddc928335f83e07757c242aba10893f053b7fa9b80bdb78c030f64c
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/qc-final.log
    sha256: 5ad4dc0ee80126b1ff8134931843d9f304f01755e65480019d341c070ad266a4
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/qc-final.receipt.json
    sha256: 0ae18ddb952d2ef3aec93207dfc8ce5b925ee3a9ffaac146c4c1786a09d0150e
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/qc-remediation.log
    sha256: e5a6ee004206ce6cc143262f9497fb9e1e6125a37fed7f46f64b431df3db0885
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/qc-remediation.receipt.json
    sha256: 0f990e03e3ec87225441292c34596b09318cffa9d549096d217ecf4d2dd5ac01
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/remediation-audit.json
    sha256: 9592413667d43ad3580d906305552cc1628714cfc9a86e39ad7397ae15610e94
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/render-final.log
    sha256: 96a7374ab88d05f746d0133d0e9616c26f64f2a7eef370554d01ce8cf29138ac
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/render-final.receipt.json
    sha256: 72c3af2db2799efbddcfcc4f4a0a8c8e4e0d1d4bec57f3debe8a06bc2d164e76
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/render-strains.log
    sha256: 96a7374ab88d05f746d0133d0e9616c26f64f2a7eef370554d01ce8cf29138ac
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/render-strains.receipt.json
    sha256: fb58c71e401dc9df10fc7c6f35b1be90b540797a9b0f57defc81fcfaf667911e
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/render.log
    sha256: 96a7374ab88d05f746d0133d0e9616c26f64f2a7eef370554d01ce8cf29138ac
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/render.receipt.json
    sha256: 8e9f3a529095396ac49be86cebcaf8d18cf97441affd1e560771972fc6df095e
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/seed-canary.log
    sha256: bbd00ba915502c98a556fa7a72234eced33bd5687b03fa1868ad4d00152a0179
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/seed-canary.receipt.json
    sha256: 4c7b12b7751b67dd1559b5a625bed0ffd0ded3bc0116be1dca7d16532ecb62c9
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/seed-dry.log
    sha256: 3f035b21edd80119c58f2c51f84fa17f4f80f58823cfdcdf5752c0916250f60d
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/seed-dry.receipt.json
    sha256: d3d244bea9450d3a99cfc3438b549f53e0fd8838d7616cb267f1b908e27a459d
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/seed-second.log
    sha256: bbd00ba915502c98a556fa7a72234eced33bd5687b03fa1868ad4d00152a0179
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/seed-second.receipt.json
    sha256: f6f8319f4beb7aa505f49d98f9af204dd7a9eb156d30bcc7191f41c82ef4988e
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/strain-focus.log
    sha256: a7c244571a0cf185e2784e5fd37216c8e30f55e6dff9db02d2142f05e57296fb
    role: context
  - path: reviews/evidence/20261013-prodigiosin-remediation/strain-focus.receipt.json
    sha256: 3762598af6fa9dd2f04b2477b425d974ff863aea44b5df80b7a3acc33197b41b
    role: context
  - path: reviews/structured/20261013T044353Z-2-methylisoborneol-2/review.yaml
    sha256: fa1713d6f819fb9ce372d3975f846b471e54fc071c401aef611be24ad9a4348d
    role: context
  - path: reviews/structured/20261013T044353Z-mycophenolic-acid-2/review.yaml
    sha256: 5a4aff125ca2a5b14dc05f7a49519813ed90187a987b3841d7a26bbc68c41cf5
    role: context
  - path: reviews/structured/20261013T054205Z-2-methylisoborneol/review.yaml
    sha256: d651c6bdfaa95004ba5ab85dc00cd31b876b9f8a743d2fbf3c59716384d2b1e1
    role: context
  - path: reviews/structured/20261013T054205Z-heme-d1-2/review.yaml
    sha256: 6366328e4e0c2b54e6940baf66b7235737dce7853947ee4f71747720a4b3cfbb
    role: context
  - path: reviews/structured/20261013T054205Z-heme-d1/review.yaml
    sha256: a20c71701b017a6a7ffa57afab6df3c3057bd8aa0d54fa818d54274549f32f89
    role: context
  - path: reviews/structured/20261013T064409Z-indigoidine-2/review.yaml
    sha256: 2211c24a7b789b64669465925131f151e6100e1649e0628c25229d42bd8e1cf3
    role: context
  - path: reviews/structured/20261013T064413Z-indigoidine/review.yaml
    sha256: a6817941b6d7065d286b92088625d03dded1a72791c58efdfce759e36949d4fe
    role: context
  - path: reviews/structured/20261013T073122Z-mycophenolic-acid/review.yaml
    sha256: 0b4aa0627b9555b3fa74b89ddbdc397d630635dbdd6b9fbe8270c0c82a2b354f
    role: context
  - path: reviews/structured/20261013T080029Z-mycophenolic-acid-assay-resolution/review.yaml
    sha256: eca9cab0bb4a603dcbe369db647621a0a08538fb4ed9e6d03786fdafe1b81f14
    role: context
  - path: reviews/structured/20261013T085546Z-prodigiosin-2/review.yaml
    sha256: ca8c8c46bc85832d2013831a0ef5b525a0c81af30addb2e7f0ffc8c62df9701d
    role: context
  - path: reviews/structured/20261013T085654Z-prodigiosin/review.yaml
    sha256: 84c50c31c70c7e18e3373644626ac8b3e1d8b95efd0e4d6dd887aca8de89c323
    role: context
  - path: scripts/render_pages.py
    sha256: bd3f7cd49488ad718377efe96dbd3c5efc5a287b3df403669c36f484d085619e
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 1b9616ed25b5dd7b8053109beea665dd178ea73055ece551ba69e9cc63bff7a7
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/templates/record.html
    sha256: 6c7cb3f03f23d23726bfa35c7f6809fdbd84dcc46f38ea71a95c899ef990f9c1
    role: context
  - path: tests/test_prodigiosin_review_archive.py
    sha256: 7785fce144cc1cb15039c071b1bb10e984fb67b60335a14b759977ff91c75479
    role: context
  - path: tests/test_producer_strains.py
    sha256: 17002ef1640464777f1925d12d842ed83c9098aad6de724ae0ea236ecccc4ff3
    role: context
  - path: tests/test_render_pages.py
    sha256: c294d3f879b917963c22347a52fffb9b7c2bee110164c2fbcd48e35ad1e3e951
    role: context
  - path: tests/test_seed_skeleton.py
    sha256: 2ea004a23633b197a239e90d7a5702dbe7970849012b63c1b7726c822c6eff03
    role: context
  - path: tests/test_structure_corrections.py
    sha256: fa71433ed59d9b0758ef621eeb269567326ab2e800458fe4437e859e3aa6be5e
    role: context
targets:
- target_id: CHEBI:82758
  path: data/natural_products/alkaloids/prodigiosin.yaml
  label: prodigiosin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported exact chemical, producer and BGC assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Imported organism-reference triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Imported ChEBI identity and definition
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Imported ChEBI occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned same-structure sibling inventory
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Harmonization and generated record emission
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Occurrence source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Cluster source extraction
scope:
  description: Producer strain provenance only; 3115-owner campaign remains active,
    ten owners partial and zero complete.
  selection: Exact F2 follow-up from 20261013T085654Z-prodigiosin.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:82758
checks:
- check_id: final-focus
  name: final-focus
  required: false
  status: failed
  exit_code: 1
  command: .venv/bin/python -m pytest -q tests/test_producer_strains.py tests/test_seed_skeleton.py
    tests/test_render_pages.py tests/test_prodigiosin_review_archive.py
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Initial renderer deduplication regression; fixed and superseded by the
    passing retry.
- check_id: final-focus-retry
  name: final-focus-retry
  required: true
  status: passed
  exit_code: 0
  command: .venv/bin/python -m pytest -q tests/test_producer_strains.py tests/test_seed_skeleton.py
    tests/test_render_pages.py tests/test_prodigiosin_review_archive.py
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Recorded native check; exact output and timing retained in the archive.
- check_id: qc-remediation
  name: qc-remediation
  required: false
  status: failed
  exit_code: 1
  command: env UV_CACHE_DIR=/private/tmp/npmech-prodigiosin-review-m1Ai8z/uv-cache
    just qc
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Isolated structure-correction fixture retained unrelated qualification
    rows; fixed without weakening production checks and superseded by qc-final.
- check_id: qc-final
  name: qc-final
  required: true
  status: passed
  exit_code: 0
  command: env UV_CACHE_DIR=/private/tmp/npmech-prodigiosin-review-m1Ai8z/uv-cache
    just qc
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Recorded native check; exact output and timing retained in the archive.
- check_id: fixture-focus
  name: fixture-focus
  required: true
  status: passed
  exit_code: 0
  command: .venv/bin/python -m pytest -q tests/test_producer_strains.py tests/test_structure_corrections.py
    tests/test_render_pages.py
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Recorded native check; exact output and timing retained in the archive.
- check_id: render-final
  name: render-final
  required: true
  status: passed
  exit_code: 0
  command: .venv/bin/python scripts/render_pages.py
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Recorded native check; exact output and timing retained in the archive.
- check_id: archive-tests
  name: archive-tests
  required: true
  status: passed
  exit_code: 0
  command: .venv/bin/python -m pytest -q tests/test_prodigiosin_review_archive.py
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - validation
  summary: Recorded native check; exact output and timing retained in the archive.
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/spectrum.01171-21
  accessed_at: '2026-10-13T08:56:54.385812Z'
  support: supports
  summary: 'Results and methods identify S4059: in-frame pigC deletion abolishes the
    prodigiosin LC-MS signal. Culture/strain and CP045429 context support the native
    knockout grade, not species-wide generality. Residual extract activity is not
    a pure-compound assay.'
  locator: 'Results: BGC verification; Materials and Methods: culture, genome, deletion'
- evidence_id: previous
  kind: record_content
  reference: reviews/structured/20261013T085654Z-prodigiosin/review.yaml
  accessed_at: '2026-10-13T09:28:22.630568Z'
  snapshot_sha256: 84c50c31c70c7e18e3373644626ac8b3e1d8b95efd0e4d6dd887aca8de89c323
  support: supports
  summary: Immutable original observation; this successor resolves only F2.
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/alkaloids/prodigiosin.yaml
  accessed_at: '2026-10-13T09:28:22.630743Z'
  snapshot_sha256: 730433d43289c7a4e119822bf7519b25934348a2d50b62fd3d661ab83880bc93
  support: supports
  summary: Complete current owner read; explicit strains and separate evidence retained
    without broadening scope.
- evidence_id: maintained-input
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  accessed_at: '2026-10-13T09:28:22.630832Z'
  snapshot_sha256: 13341e78333d6efbb8a0331a675aa076d13a5830af8d5f860f743022a6c6268a
  support: supports
  summary: Complete raw-row pins and inspected source citations; no raw inventory
    mutation.
- evidence_id: audit
  kind: validation
  reference: reviews/evidence/20261013-prodigiosin-remediation/remediation-audit.json
  accessed_at: '2026-10-13T09:28:22.630908Z'
  snapshot_sha256: 9592413667d43ad3580d906305552cc1628714cfc9a86e39ad7397ae15610e94
  support: supports
  summary: Ignored-inclusive audit of all 3115 owners and 243 components; only the
    two intended owners change.
- evidence_id: validation
  kind: validation
  reference: reviews/evidence/20261013-prodigiosin-remediation/qc-final.log
  accessed_at: '2026-10-13T09:28:22.630984Z'
  snapshot_sha256: 5ad4dc0ee80126b1ff8134931843d9f304f01755e65480019d341c070ad266a4
  support: supports
  summary: Fresh full gate passed on the final implementation, including renderer
    and isolated fixture fixes.
assessments:
- assessment_id: strain
  area: evidence
  topic: Explicit strain scope and retained source assertion
  outcome: supported
  summary: The generated producer has the source-supported strain, unchanged taxon/grade
    and original database evidence plus attributed curator interpretation.
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - owner
  - primary
  - maintained-input
  - audit
  - validation
- assessment_id: completeness
  area: completeness
  topic: Whole-record scientific review
  outcome: unknown
  summary: F1, chemical equivalence and access-limited occurrence checks are not resolved
    by adding strain context.
  target_ids:
  - CHEBI:82758
  evidence_ids:
  - previous
findings:
- finding_id: F2
  issue_key: prodigiosin-s4059-strain-provenance
  category: scope
  severity: minor
  status: resolved
  certainty: confirmed
  title: Characterized producer claim omits strain S4059
  description: The BGC_CHARACTERIZED producer row gives P. rubra but no strain or
    strain-specific notes. Its cited study and genome are S4059-specific. Preserve
    that scope without changing the supported knockout grade or inventing a strain
    taxon identifier.
  target_ids:
  - CHEBI:82758
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].notes
  evidence_ids:
  - previous
  - owner
  - maintained-input
  - audit
  - validation
  - primary
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Source cluster and taxon context
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Cluster extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Seeded producer representation
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Exact raw-source-pinned strain qualifications
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Fail-closed qualification validator
  rule_id: 'Native checklist: exact compound and taxon, narrow evidence, producer
    strain where supplied'
  native_severity: minor
  normalization_reason: Bounded loss of source strain provenance; producer evidence
    grade is not falsely upgraded.
  disposition_reason: The pinned maintained qualification now supplies the missing
    strain and separate curator evidence. Guarded regeneration, exhaustive unchanged-field
    audit, focused regressions and native QC pass. No identity, taxon, grade, occurrence
    or status changes; no whole-record sign-off.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T085654Z-prodigiosin
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/887
actions: []
limitations:
- Partial scoped disposition, not a whole-record pass. The native SEEDED status and
  all occurrence claims remain unchanged.
- The major occurrence finding F1 remains open; a newer scoped passing observation
  does not close it.
- All inherited access stops and exact pinned chemistry limitations remain. No primary
  full text was retrieved around an access restriction.
- The same assistant implemented and reviewed these changes; this is self-review,
  not an independent reviewer.
- Inspected and saved in a detached durable-main-base worktree populated with the
  exact remediated bytes. Working-tree hashes attest those bytes, not their existence
  in the base commit.
- Initial full QC failed on an isolated test fixture. Its receipt is retained; a fresh
  full QC run and focused retries validate the final implementation. The archive-lineage
  regression added afterward requires a focused check and final-head CI. Protected
  PR and merge-queue CI must cover the final committed head.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T085654Z-prodigiosin
  relationship: Scoped F2 resolution only
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/883
- https://github.com/CultureBotAI/NaturalProductMech/issues/887
```
