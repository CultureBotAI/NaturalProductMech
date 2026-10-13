# Evidence grade, citation wording and producer strain: vibriobactin

- Review: 20261013T110552Z-vibriobactin-findings-resolution
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T11:05:50.409875Z
- Finished UTC: 2026-10-13T11:05:52.341721Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Resolve the three saved findings through guarded regeneration; retain partial scientific status and all primary-access limitations.

## Scope And Provenance

Exact-owner scoped successor only; campaign remains3115 owners,12 partial,0 complete and3103 unassessed.

Selection: Explicit follow-up to 20261013T102720Z-vibriobactin
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9e5163ca9689a98df9af76f1ccb38fe0df72594c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:9973 | data/natural_products/alkaloids/vibriobactin.yaml | generated | vibriobactin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused-tests | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| archive-tests | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| seed-dry | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| seed-canary | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| seed-apply | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| scope-audit | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| render | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| docs-stats | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| labels | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |
| qc | passed | True | CHEBI:9973 | Executed successfully; exact command, UTC timing and output hash retained in the remediation archive. |

## Scientific And Domain Assessments

### Evidence grade, citation wording and producer strain

scope: supported. Targets: CHEBI:9973.

The locus is CLUSTER_UNSTATED; original database evidence and excluded methods survive. Lou15 strain is explicit, while taxon and SOURCE_ASSERTION grade remain. Occurrence notes no longer infer independent publications.

### Whole-record scientific completeness

completeness: unknown. Targets: CHEBI:9973.

Uninspected primary material and exact experimental scope remain unresolved.

## Findings

### F1: Transport complementation is graded as demonstrated biosynthesis

major / resolved / confirmed; issue key: vibriobactin-bgc2494-transport-as-biosynthesis.

BGC0002494 imports Heterologous expression from the 1999 transport study. Its supported phenotype is siderophore utilization, not biosynthetic production by the locus. CLUSTER_DEMONSTRATED therefore overstates this evidence. This does not refute VibD/VibH participation or native production.

Disposition: Maintained-input correction, focused regressions, generated-field audit and full native QC establish this scoped fix. No whole-record scientific sign-off.

### F2: The producer and occurrence cite the same publication

minor / resolved / confirmed; issue key: vibriobactin-same-publication-corroboration.

The occurrence DOI and producer PMID:10601218 are the same publication, explicitly aliased by MIBiG. The generated note incorrectly claims a different citation and independent corroboration. Two database assertions are not two experiments.

Disposition: Maintained-input correction, focused regressions, generated-field audit and full native QC establish this scoped fix. No whole-record scientific sign-off.

### F3: Producer assertion omits the available Lou15 strain qualifier

minor / resolved / confirmed; issue key: vibriobactin-lou15-producer-strain.

The producer row is species NCBITaxon:666 without strain, while its exact U52150.2 source deposit specifies Lou15 (El Tor). The graph already preserves this source distinction. Carry the strain into the producer assertion without changing taxon identity or SOURCE_ASSERTION grade.

Disposition: Maintained-input correction, focused regressions, generated-field audit and full native QC establish this scoped fix. No whole-record scientific sign-off.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| previous | reviews/structured/20261013T102720Z-vibriobactin/review.yaml | supports | Immutable predecessor remains unchanged; its unassessed scientific scope is not retired. |
| owner | data/natural_products/alkaloids/vibriobactin.yaml | supports | Complete owner read; chemistry, graph content and native status retained. Only the declared remediation scope is assessed. |
| audit | reviews/evidence/20261013-vibriobactin-remediation/scope-audit.json | supports | Ignored-inclusive all-owner comparison: 3115 owners,243 components;732 corrected owners, with no chemistry, graph, status or population changes. |
| checks | reviews/evidence/20261013-vibriobactin-remediation/qc.receipt.json | supports | Full native QC and companion receipts/logs are durable in this directory. |
| archive | reviews/evidence/20261013-vibriobactin/manifest.json | supports | Checksum mapping retains historical native deposits, public structured sources, failed checks and campaign population. |
| primary | https://journals.asm.org/doi/10.1128/jb.181.24.7588-7596.1999; Results on heterologous transport complementation; Table 1 and Table 3. | supports | Inspected transport experiment and strain context support the narrow correction; not a whole-record biosynthesis validation. |
| strain | curation/mibig_producer_strains.tsv | supports | Complete source-row pin scopes the Lou15 qualification to BGC0002494:1. |
| withdrawal | curation/mibig_locus_evidence_overrides.tsv | supports | Exact raw context, including empty bounds, withdraws the inapplicable method while preserving source provenance. |

## Limits And Additional Notes

- The 1997 and 1984 primary texts remain access-stopped; prior protein-method and exact experimental-form limits remain. No full scientific completion is claimed.
- Inspected a detached worktree at durable main base9e5163ca populated with identical reviewed bytes; working-tree input hashes are an attestation, not a claim those changes existed in the base.
- Full QC executed in the publication worktree before these immutable successors; canonical validation and final-head CI must cover the newly saved observations.
- No additional owner is counted as reviewed and no native status is promoted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T110552Z-vibriobactin-findings-resolution
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Evidence grade, citation wording and producer strain: vibriobactin'
started_at: '2026-10-13T11:05:50.409875Z'
finished_at: '2026-10-13T11:05:52.341721Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant implements and saves this scoped disposition;
    separate read-only agent adversarial review is documented on PR894.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Resolve the three saved findings through guarded regeneration; retain partial
  scientific status and all primary-access limitations.
source:
  git_revision: 9e5163ca9689a98df9af76f1ccb38fe0df72594c
  state: working_tree
  inputs:
  - path: README.md
    sha256: 6a00cbeb07cf3bdcb8fac4aeb1738a9383d4a4a66869ca9853ed8bfa188e50b4
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: f075713522db63c54eb4054b539cf421b42feb6375a2736e7386e8d7abeeea32
    role: context
  - path: data/natural_products/alkaloids/vibriobactin.yaml
    sha256: 1b3c9b40cab9e76264c8f9be622883225af34069a0e4c8b49ff27a0ce537c183
    role: target
  - path: data/raw/antibioticmech_inchikeys.tsv
    sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
    role: context
  - path: data/raw/chebi_origins.tsv
    sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
    role: context
  - path: data/raw/chebi_structures.tsv
    sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
    role: context
  - path: data/raw/lotus_occurrences.tsv
    sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
    role: context
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: data/raw/npclassifier.tsv
    sha256: 7b9b9f78f5b14aea9fabb163bbaa9e842920a7e9b07deac8f98c97666e9e23fc
    role: context
  - path: docs/CURATION.md
    sha256: e0b1b524d1dfdb16f2c100ab3794f3e69e2740d7352060f04b82d5f7020e76b4
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
  - path: reviews/evidence/20261013-vibriobactin-remediation/README.md
    sha256: c4692f4095488c422049f97cb330d78004c90b52ad24173afa969f473d4297eb
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/archive-tests.log
    sha256: af3fec7180585a3d9522aa65703e1cdccd11a69a8b858ff2dfa9ea3b136142b9
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/archive-tests.receipt.json
    sha256: 3b8d6b5e3516dfa48826c8d67dff1195b6ee5752b7d3108708cfabce63d8f436
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/audit_scope.py.txt
    sha256: f41329840a46c1659eeef7df65493bd869db218683dfd01f5f31f0d559d88280
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/docs-stats.log
    sha256: 658ee65842023f89e2a79628d38b67cf05f0706355ac5505e3c930d751b6619c
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/docs-stats.receipt.json
    sha256: fc54be354c3c047e68a731266a4813659582db5a756e60b585d6c382eac9c89f
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/focused-tests.log
    sha256: 919f9c6d6e23c5a73bf54f1a4916ca7108cd0edc4e9cbf9b85e90e8300fd50d2
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/focused-tests.receipt.json
    sha256: a35a72e7c2e0c0c248c2dda74d295927e4b97b53fd33a46d694532c34cd620df
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/labels.log
    sha256: 556ef5804e095767472c0aa8a542d5bff7e332470383a992e6b260103034414b
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/labels.receipt.json
    sha256: dd230c74e6f2c2b53858ca4d6e7893bf6d2ac095a099f8d5af5c04cc64edad3a
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/prepare_successors.py.txt
    sha256: da930e2a1d8d61f4c58fd19de0ea4a01134083d17fa6566c50b3b6e584be0571
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/qc.log
    sha256: 3367c866e4689b0527556a6e47817dcb009b6164aaddea6feada4c929cd25528
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/qc.receipt.json
    sha256: b25a7d8e0f361ff6e9d33c3b25cd9baab458cb1507f7b316ed964de32321741a
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/render.log
    sha256: d9035101f2746e4f553e61414a9c1b5d4310dcc6bd9fdca32d2706fa89a886d1
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/render.receipt.json
    sha256: 7b45481303fcad40856b254a9b6debdec71d357beb2dbd6918ea336bc88727ca
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/run_check.py.txt
    sha256: 296c1f36fac8dc53a10e21dabaaa5128c2e81803f6f6d5c046718210b840db44
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/scope-audit.json
    sha256: 450f29c12cdde3d52ae2aeaf336ce49a7e06aba6b7a529434f20cd18656a54c9
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/scope-audit.log
    sha256: 22a550667602f054e2723752dbfdea2759b1a3eb181154561a4bfa9c41b9eb90
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/scope-audit.receipt.json
    sha256: ff89a340e265ebfd92a7e567d79668bc2b43b478511161714844c8ed8b432cff
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/seed-apply.log
    sha256: fd45814ae86c719dba1ca7816d1496da86b7c4cfc439d3f9c787c571141367ff
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/seed-apply.receipt.json
    sha256: 0016ddcc3b97bb3680643a1735e28ee0abb0852724f58cf0224a66e6a961e26a
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/seed-canary.log
    sha256: bbd00ba915502c98a556fa7a72234eced33bd5687b03fa1868ad4d00152a0179
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/seed-canary.receipt.json
    sha256: ce51941aac83c24cf5d77db74442779c3aed8dbeb75fd4a56de892382ce08c02
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/seed-dry.log
    sha256: 3f035b21edd80119c58f2c51f84fa17f4f80f58823cfdcdf5752c0916250f60d
    role: context
  - path: reviews/evidence/20261013-vibriobactin-remediation/seed-dry.receipt.json
    sha256: 75e54dac1abbab4e77a2a7ec228dec19ab20a6c53454e01ac27efc8259f4a141
    role: context
  - path: reviews/evidence/20261013-vibriobactin/artifacts/npmech-acetylaszonalenin-20261010-MSlYJu/AE003852.embl.gz
    sha256: 9cc7688ae804e8d477e0fe4cb9535eb8d275162bdac6c058de7059522e248149
    role: context
  - path: reviews/evidence/20261013-vibriobactin/manifest.json
    sha256: 135bf299792609cd54a5b3a3996edbdd545a90a49a4378970db7917870a944b7
    role: context
  - path: reviews/structured/20261013T102719Z-vibriobactin-2/review.yaml
    sha256: cbef9fc2e7041eb8d6bb7f89190b4075d765db085599ca6408fec2069c6a7309
    role: context
  - path: reviews/structured/20261013T102720Z-vibriobactin/review.yaml
    sha256: b63d7d92f1fc1e7bd9c776bacd561adadad0469b4fc5b017ffe2771f68310a96
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_lotus.py
    sha256: 8a8c524f60f85d2bb54412ca055a6a45e0d37ec5f4584d8d70be454b8f664290
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/np_report.py
    sha256: ba83e6d5865b1cb7fe2d976e9815990aed6d912fe481fd9d5cbda5b02258e399
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 4daf8b2b5864b55c9d8d50a85572bbd71d6b1d8223e492a8961479c497d026ea
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
    role: context
  - path: tests/test_corpus_integrity.py
    sha256: 4573cee6b6d03b60430cf067125744eba0665771825ae82abd0e762f4be2ba90
    role: context
  - path: tests/test_mibig_locus_evidence_overrides.py
    sha256: 9177b5bd24f6e47cc4743857179217d9e0d4add9560b2ce3faefaebe53ba09a0
    role: context
  - path: tests/test_np_report.py
    sha256: 1f281854edea4be20a63157ab9e125e95092c5c1ae509b2adde78c2f04e9afa4
    role: context
  - path: tests/test_seed_skeleton.py
    sha256: 671f48ceef83b27d4c745de21d4175334ac0f78a2af08bae5ff0941a93b79ce9
    role: context
  - path: tests/test_vibriobactin_review_archive.py
    sha256: 4694172f33f6d4e7207640026529f44f0352d2e27714b514e55ab59a3d6258fd
    role: context
targets:
- target_id: CHEBI:9973
  path: data/natural_products/alkaloids/vibriobactin.yaml
  label: vibriobactin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and BGC assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Imported exact structure-organism-reference triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: ChEBI identity and definition
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: ChEBI occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned exact-structure sibling joins
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated source harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: LOTUS occurrence extraction
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/vibriobactin.yaml
    role: Curator-owned inline graph; use validated writer, not seeder edits
scope:
  description: Exact-owner scoped successor only; campaign remains3115 owners,12 partial,0
    complete and3103 unassessed.
  selection: Explicit follow-up to 20261013T102720Z-vibriobactin
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:9973
checks:
- check_id: focused-tests
  name: focused-tests
  required: true
  status: passed
  command: .venv/bin/python -m pytest -q tests/test_seed_skeleton.py tests/test_mibig_locus_evidence_overrides.py
    tests/test_np_report.py
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: archive-tests
  name: archive-tests
  required: true
  status: passed
  command: .venv/bin/python -m pytest -q tests/test_vibriobactin_review_archive.py
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: seed-dry
  name: seed-dry
  required: true
  status: passed
  command: .venv/bin/python scripts/seed_from_sources.py
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: seed-canary
  name: seed-canary
  required: true
  status: passed
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only CHEBI:9973
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: seed-apply
  name: seed-apply
  required: true
  status: passed
  command: .venv/bin/python scripts/seed_from_sources.py --apply
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: scope-audit
  name: scope-audit
  required: true
  status: passed
  command: .venv/bin/python /private/tmp/npmech-vibriobactin-publish-ZQxmpQoV/audit_scope.py
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: render
  name: render
  required: true
  status: passed
  command: .venv/bin/python scripts/render_pages.py
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: docs-stats
  name: docs-stats
  required: true
  status: passed
  command: .venv/bin/python scripts/check_docs.py --write
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: labels
  name: labels
  required: true
  status: passed
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
- check_id: qc
  name: qc
  required: true
  status: passed
  command: env RECORD_REVIEW_BASE=9e5163ca9689a98df9af76f1ccb38fe0df72594c .venv/bin/python
    scripts/run_qc.py
  exit_code: 0
  evidence_ids:
  - checks
  summary: Executed successfully; exact command, UTC timing and output hash retained
    in the remediation archive.
  target_ids:
  - CHEBI:9973
evidence:
- evidence_id: previous
  kind: prior_review
  reference: reviews/structured/20261013T102720Z-vibriobactin/review.yaml
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: b63d7d92f1fc1e7bd9c776bacd561adadad0469b4fc5b017ffe2771f68310a96
  summary: Immutable predecessor remains unchanged; its unassessed scientific scope
    is not retired.
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/alkaloids/vibriobactin.yaml
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: 1b3c9b40cab9e76264c8f9be622883225af34069a0e4c8b49ff27a0ce537c183
  summary: Complete owner read; chemistry, graph content and native status retained.
    Only the declared remediation scope is assessed.
- evidence_id: audit
  kind: validation
  reference: reviews/evidence/20261013-vibriobactin-remediation/scope-audit.json
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: 450f29c12cdde3d52ae2aeaf336ce49a7e06aba6b7a529434f20cd18656a54c9
  summary: 'Ignored-inclusive all-owner comparison: 3115 owners,243 components;732
    corrected owners, with no chemistry, graph, status or population changes.'
- evidence_id: checks
  kind: validation
  reference: reviews/evidence/20261013-vibriobactin-remediation/qc.receipt.json
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: b25a7d8e0f361ff6e9d33c3b25cd9baab458cb1507f7b316ed964de32321741a
  summary: Full native QC and companion receipts/logs are durable in this directory.
- evidence_id: archive
  kind: record_content
  reference: reviews/evidence/20261013-vibriobactin/manifest.json
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: 135bf299792609cd54a5b3a3996edbdd545a90a49a4378970db7917870a944b7
  summary: Checksum mapping retains historical native deposits, public structured
    sources, failed checks and campaign population.
- evidence_id: primary
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/jb.181.24.7588-7596.1999
  locator: Results on heterologous transport complementation; Table 1 and Table 3.
  accessed_at: '2026-10-13T10:14:03Z'
  support: supports
  summary: Inspected transport experiment and strain context support the narrow correction;
    not a whole-record biosynthesis validation.
- evidence_id: strain
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: f075713522db63c54eb4054b539cf421b42feb6375a2736e7386e8d7abeeea32
  summary: Complete source-row pin scopes the Lou15 qualification to BGC0002494:1.
- evidence_id: withdrawal
  kind: record_content
  reference: curation/mibig_locus_evidence_overrides.tsv
  accessed_at: '2026-10-13T11:05:52.339776Z'
  support: supports
  snapshot_sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
  summary: Exact raw context, including empty bounds, withdraws the inapplicable method
    while preserving source provenance.
assessments:
- assessment_id: scope
  area: scope
  topic: Evidence grade, citation wording and producer strain
  outcome: supported
  summary: The locus is CLUSTER_UNSTATED; original database evidence and excluded
    methods survive. Lou15 strain is explicit, while taxon and SOURCE_ASSERTION grade
    remain. Occurrence notes no longer infer independent publications.
  target_ids:
  - CHEBI:9973
  evidence_ids:
  - previous
  - owner
  - audit
  - checks
  - archive
  - primary
  - strain
  - withdrawal
- assessment_id: completeness
  area: completeness
  topic: Whole-record scientific completeness
  outcome: unknown
  summary: Uninspected primary material and exact experimental scope remain unresolved.
  target_ids:
  - CHEBI:9973
  evidence_ids:
  - previous
findings:
- finding_id: F1
  issue_key: vibriobactin-bgc2494-transport-as-biosynthesis
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Transport complementation is graded as demonstrated biosynthesis
  description: BGC0002494 imports Heterologous expression from the 1999 transport
    study. Its supported phenotype is siderophore utilization, not biosynthetic production
    by the locus. CLUSTER_DEMONSTRATED therefore overstates this evidence. This does
    not refute VibD/VibH participation or native production.
  target_ids:
  - CHEBI:9973
  field_paths:
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - producer_organisms[0].notes
  evidence_ids:
  - previous
  - owner
  - audit
  - checks
  - archive
  - primary
  - strain
  - withdrawal
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented pinned source-method withdrawal
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Locus and producer grade harmonization
  rule_id: 'Native checklist: narrow claim-level evidence; Gene clusters; Producer
    organisms; Evidence standard'
  native_severity: major
  normalization_reason: Material evidence-tier inflation survives deterministic validation;
    normalized as major unsupported evidence.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T102720Z-vibriobactin
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/890
  disposition_reason: Maintained-input correction, focused regressions, generated-field
    audit and full native QC establish this scoped fix. No whole-record scientific
    sign-off.
- finding_id: F2
  issue_key: vibriobactin-same-publication-corroboration
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: The producer and occurrence cite the same publication
  description: The occurrence DOI and producer PMID:10601218 are the same publication,
    explicitly aliased by MIBiG. The generated note incorrectly claims a different
    citation and independent corroboration. Two database assertions are not two experiments.
  target_ids:
  - CHEBI:9973
  field_paths:
  - occurrences[0].notes
  evidence_ids:
  - previous
  - owner
  - audit
  - checks
  - archive
  - primary
  - strain
  - withdrawal
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated cross-source corroboration wording
  - repository: CultureBotAI/NaturalProductMech
    path: docs/HARMONIZATION.md
    role: Producer-versus-occurrence corroboration documentation
  rule_id: 'Native checklist: narrow claim-level evidence; Gene clusters; Producer
    organisms; Evidence standard'
  native_severity: minor
  normalization_reason: Non-blocking provenance wording; the underlying occurrence
    need not be removed.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T102720Z-vibriobactin
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/891
  disposition_reason: Maintained-input correction, focused regressions, generated-field
    audit and full native QC establish this scoped fix. No whole-record scientific
    sign-off.
- finding_id: F3
  issue_key: vibriobactin-lou15-producer-strain
  category: scope
  severity: minor
  status: resolved
  certainty: confirmed
  title: Producer assertion omits the available Lou15 strain qualifier
  description: The producer row is species NCBITaxon:666 without strain, while its
    exact U52150.2 source deposit specifies Lou15 (El Tor). The graph already preserves
    this source distinction. Carry the strain into the producer assertion without
    changing taxon identity or SOURCE_ASSERTION grade.
  target_ids:
  - CHEBI:9973
  field_paths:
  - producer_organisms[0].strain
  evidence_ids:
  - previous
  - owner
  - audit
  - checks
  - archive
  - primary
  - strain
  - withdrawal
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Complete-raw-row-pinned source strain qualification
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Producer claim generation
  rule_id: 'Native checklist: narrow claim-level evidence; Gene clusters; Producer
    organisms; Evidence standard'
  native_severity: minor
  normalization_reason: Bounded provenance loss; database producer evidence was not
    falsely promoted to experimental causality.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T102720Z-vibriobactin
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/892
  disposition_reason: Maintained-input correction, focused regressions, generated-field
    audit and full native QC establish this scoped fix. No whole-record scientific
    sign-off.
actions: []
limitations:
- The 1997 and 1984 primary texts remain access-stopped; prior protein-method and
  exact experimental-form limits remain. No full scientific completion is claimed.
- Inspected a detached worktree at durable main base9e5163ca populated with identical
  reviewed bytes; working-tree input hashes are an attestation, not a claim those
  changes existed in the base.
- Full QC executed in the publication worktree before these immutable successors;
  canonical validation and final-head CI must cover the newly saved observations.
- No additional owner is counted as reviewed and no native status is promoted.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T102720Z-vibriobactin
  relationship: Scoped successor; all earlier unassessed scientific scope remains
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/894
```
