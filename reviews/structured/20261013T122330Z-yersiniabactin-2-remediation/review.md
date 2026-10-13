# yersiniabactin-2: bounded xref and strain dispositions

- Review: 20261013T122330Z-yersiniabactin-2-remediation
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T12:07:36.505415Z
- Finished UTC: 2026-10-13T12:23:30.002328Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Resolve supported provenance defects only; preserve access-limited science and the full campaign denominator.

## Scope And Provenance

Scoped successor for one exact owner. Campaign remains3115 owners/243 components,14 partial owners and zero completed scientific reviews.

Selection: Explicit predecessor findings from the yersiniabactin PR; not a population sample.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8b5a3ebf476c27b21d49a89d7e5684cef41a367d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-66a349ed2d | data/natural_products/alkaloids/yersiniabactin-2.yaml | generated | yersiniabactin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| qc | failed | False | naturalproductmech:mibig-66a349ed2d | Initial QC correctly rejected stale generated README discussion statistics; regenerated and superseded by qc-final. |
| docs-stats | passed | True | naturalproductmech:mibig-66a349ed2d | Actual command result retained with timing and exact log hash in the remediation evidence archive. |
| focused | passed | True | naturalproductmech:mibig-66a349ed2d | Actual command result retained with timing and exact log hash in the remediation evidence archive. |
| scope-audit | passed | True | naturalproductmech:mibig-66a349ed2d | Actual command result retained with timing and exact log hash in the remediation evidence archive. |
| reseed-hold | passed | True | naturalproductmech:mibig-66a349ed2d | Actual command result retained with timing and exact log hash in the remediation evidence archive. |
| render | passed | True | naturalproductmech:mibig-66a349ed2d | Actual command result retained with timing and exact log hash in the remediation evidence archive. |
| qc-final | passed | True | naturalproductmech:mibig-66a349ed2d | Actual command result retained with timing and exact log hash in the remediation evidence archive. |
| Initial focused fixture check | failed | False | naturalproductmech:mibig-66a349ed2d | Initial run:338 passed and1 failed because the synthetic replacement fixture marked unrelated rows without replacement-reference metadata. Scoped the fixture to its actual target; final focused run passed342 tests. |
| Whole-record primary experiment and isolate-form verification | unavailable | True | naturalproductmech:mibig-66a349ed2d | Inherited primary-source access limitations remain. No restricted source was retried; no whole-record sign-off or native REVIEWED promotion. |

## Scientific And Domain Assessments

### Supported scoped corrections

evidence: supported. Targets: naturalproductmech:mibig-66a349ed2d.

Exact source strain context is now retained. The unspecified owner no longer asserts nonexact PubChem equivalence; the sibling retains its valid xref. Imported scientific claims and identity remain unchanged.

### Whole-record scientific completeness

completeness: unknown. Targets: naturalproductmech:mibig-66a349ed2d.

Incomplete primary experimental and isolated-form verification remains. The E.coli occurrence question is not resolved by strain qualification or by adding a discussion.

## Findings

### F1: Producer assertion drops the available A0 34/86 strain

minor / resolved / confirmed; issue key: yersiniabactin-BGC0001055-producer-strain.

The species-level taxon562 producer has neither strain nor a strain qualifier. AM236324.1 and the cited paper identify A0 34/86. Preserve this context without changing the taxon or upgrading the source-assertion evidence.

Disposition: Exact-source-pinned correction is emitted through the guarded seeder; focused regressions and native QC pass. Original source assertion/provenance, both chemical identities and native status remain. This resolves only the named defect, not whole-record scientific completeness.

### F2: E.coli occurrence needs direct chemical-detection support

major / open / provisional; issue key: yersiniabactin-lotus-ecoli-genomic-citation.

The occurrence claims that this structure was found in E.coli, but its DOI is a comparative-genomics paper whose inspected abstract reports genes rather than metabolite detection. This is a provisional evidence gap, not proof that the complete paper contains no chemical experiment, nor proof of nonproduction. The new curator discussion records this limitation without deleting the LOTUS assertion. GitHub #902 remains open.

## Recommended Actions And Acceptance Checks

### A2

With authorized article access, locate the exact E.coli isolation/detection result or adjudicate the LOTUS occurrence as unsupported. Do not remove it solely from abstract silence. If correction is needed, implement a tested source-row-pinned extraction/overlay path; reserved decisions.tsv cannot do this.

- Inspect the complete cited paper or user-supplied source without bypassing access restrictions.
- Evidence must identify compound form, A0 34/86 and a chemical detection experiment rather than gene presence.
- Any later row exclusion preserves provenance and passes exact-key occurrence, reproduction and full QC regressions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| previous | reviews/structured/20261013T115040Z-yersiniabactin-2/review.yaml | supports | Immutable historical findings and full-text limitations retained; this successor is scoped remediation, not a new whole-record review. |
| owner | data/natural_products/alkaloids/yersiniabactin-2.yaml | supports | Complete regenerated owner, history and all fields inspected after canonical capture. No graph components are referenced. Chemistry, taxonomy, grades, occurrences and SEEDED status are unchanged. |
| strain-table | curation/mibig_producer_strains.tsv | supports | Exact untouched source rows are SHA256-pinned; source-specific strain qualifications add separate curator evidence only. |
| xref-table | curation/mibig_xref_exclusions.tsv | supports | BGC0000467:1 PubChem5462519 exclusion is source-row-pinned; raw assertion and attribution survive in a table-owned discussion. The sibling xref remains. |
| audit | reviews/evidence/20261013-yersiniabactin-remediation/scope-audit.json | supports | Ignored-inclusive audit covers 3115 owners and243 components; only the two intended owners change, with an exact allowed-field comparison. Raw inventories and PATHS.tsv are unchanged. |
| validation | reviews/evidence/20261013-yersiniabactin-remediation/qc-final.log | supports | Fresh complete native QC after regenerating README statistics; deterministic success is not whole-record scientific sign-off. |
| AM236324.1.embl | reviews/evidence/20261013-yersiniabactin/artifacts/AM236324.1.embl.gz | supports | Inspected exact source feature identifies taxon562 and strain A0 34/86; genomic context is not chemical-detection evidence. |

## Limits And Additional Notes

- Partial scoped disposition, not a whole-record or whole-corpus pass. All inherited access restrictions remain.
- Only three supported defects are resolved across these two successors; GitHub #902 stays open. Records remain SEEDED.
- Inspected in an isolated worktree at durable main8b5a3ebf, populated with byte-identical remediated inputs. Working-tree hashes are attestations, not a claim the remediated bytes existed in the base commit.
- Original review files and historical campaign checkpoint are immutable; no unassessed owner was removed from the campaign.
- Fresh full QC covers the implementation and historical archive. Final successor pairs require their own canonical check and final-head CI.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T122330Z-yersiniabactin-2-remediation
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'yersiniabactin-2: bounded xref and strain dispositions'
started_at: '2026-10-13T12:07:36.505415Z'
finished_at: '2026-10-13T12:23:30.002328Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant implemented and adversarially rechecked the changes;
    not an independent reviewer.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Resolve supported provenance defects only; preserve access-limited science
  and the full campaign denominator.
source:
  git_revision: 8b5a3ebf476c27b21d49a89d7e5684cef41a367d
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: conf/record_review.yaml
    sha256: e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 8762b6c3e9b048d64965049aad4addbaefdf76e817f6043e42301c68e301c25a
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: 7f2c7a379c0ccf72311ae69c49d5f68c65b56768fd4c785ce9ef47ee7d1bf7b2
    role: context
  - path: data/natural_products/alkaloids/yersiniabactin-2.yaml
    sha256: 501b4d7def902f0e3762cff08463cfe34dc72c397f1069520b298844ba6bddbd
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
    sha256: 73a0fd94ffd5d283f3e12bdd291a4906b61257c99bd78e18165c941c4583e5d4
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
  - path: reviews/evidence/20261013-yersiniabactin-remediation/README.md
    sha256: 53647ee74304ee80790dad579840b71b7ca2a8ed7b8599c0c8625f05936e87c4
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/add-hold.log
    sha256: 7ec772d3eacd8cafaf2ef3e9298238c405bc6b763cef97c6664efb875896bcc5
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/add-hold.receipt.json
    sha256: bdfc34fa40f139fea3ea33812dd81bc6fac27ec4b733d48a4b22a4282561909e
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/add_hold.py.txt
    sha256: cafe879d197b12d9bf8fa3c016f8cc890b4b5d8ec152f430171f66619af6aa29
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/audit.py.txt
    sha256: ad1a265e5d81d3d68f76e31c4a53756b6afe4b4d5ad2a4129d9140857d382185
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/capture_successors.py.txt
    sha256: 86c69915ddec0fcbcb44b74e3955b00e237d2e9a0c9fbfbee65731dd67b6c419
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/docs-stats.log
    sha256: 658ee65842023f89e2a79628d38b67cf05f0706355ac5505e3c930d751b6619c
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/docs-stats.receipt.json
    sha256: 77543fee78c020d51c89366ac2a3eb6e5ab2704512cf5d8fd20421311d31ef4c
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/focused.log
    sha256: 94aeaf51a6ee85e1271c06786e4d08625e736e25b259dd77c7857ae53da286ae
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/focused.receipt.json
    sha256: fa8bf480ea3bae4a6a4357f50d02e698d6f81e367ab6018bc2b635d954179dee
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/manifest.json
    sha256: 2ce309e369fffaca4aafabfe6693ba25627354a1eab8eef1f22cc3ddf86aeafe
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/prepare_successors.py.txt
    sha256: cced98991957d1df4b9f7e1287447b4f951236a7dee66f9658a805d11cc1325c
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/qc-final.log
    sha256: e2f7633602ce2bbab6f66425717fd73ba471ff1b073bdb298c638fc1ffa2431d
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/qc-final.receipt.json
    sha256: 8785bbfa355fe161024613535ed4346d5764bf228f70db79bd1111e71e53dd94
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/qc.log
    sha256: d37d262a25c5733586f19babed4d60abb407a46d1ce6f7ccd7d71ca236dd390d
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/qc.receipt.json
    sha256: 773678384620ea3c6f39790b423d33920990f7552641d0e015d35afdad512b2f
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/render.log
    sha256: 4b1347fe48eea4e17e145a12701ca0820fb28f93e027050d8f8e755e57f3a967
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/render.receipt.json
    sha256: e1143fbbde4aab341610a4589bba3975a361e5642eb1fe7ef171f69e3689dee7
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/reseed-hold.log
    sha256: 67e92562fe50792bab3f0f4aac51f3fb0afa9d85dd044b9cfbde8fbb6bdc6d39
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/reseed-hold.receipt.json
    sha256: 710976273c37975b291be718735497e426a75abebb5514c87f3770c3ee8ce998
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/run_check.py.txt
    sha256: a21156898f286b32be0861f548896214ac3f3fa6824a6793a81e52d4c26f4c97
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/scope-audit.json
    sha256: a8a24569daf74a06a0d64a4fdd32f4d50f8ae8f88e97fc7469ed1cbaf28172a4
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/scope-audit.log
    sha256: dc272c41527fa9a6cbfd375dd9ef84c39db24850f9e67199b3337fdc7d4c47c6
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/scope-audit.receipt.json
    sha256: cc9e84d7930515584c07652d0cfcae133c16fe7f8520fb6f8743176fd73d19b8
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/yersiniabactin-2-owner.yaml
    sha256: 501b4d7def902f0e3762cff08463cfe34dc72c397f1069520b298844ba6bddbd
    role: context
  - path: reviews/evidence/20261013-yersiniabactin-remediation/yersiniabactin-owner.yaml
    sha256: ddd8892b0ef1668a9ab46e295e1f34a02315fd035b5533781bfae357aa56564e
    role: context
  - path: reviews/evidence/20261013-yersiniabactin/artifacts/AM236324.1.embl.gz
    sha256: 8ce87778e0673e66b25ed7ca1d0e433197e49e8ac209c197a6d248083e21aefa
    role: context
  - path: reviews/evidence/20261013-yersiniabactin/manifest.json
    sha256: dc352207327db5f155e89d83d914259bc4e1985cbf5b6cd4a70d5615e77435ed
    role: context
  - path: reviews/structured/20261013T115040Z-yersiniabactin-2/review.yaml
    sha256: 0abc8cf956e27fa04f8b99ab57350325520b0ef832eb13a41a2fadfddea7438b
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
  - path: scripts/seed_from_sources.py
    sha256: 8d82d7633e0492e9fe16011f6e5af6f8024f573e80c8a24176b65e2941478b71
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: a8b8834788b4714cf1cb0d1cc410d5c2f88112a32ad8621c8e043f0a4bc38a9d
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: ea8720cae8461b30fad3a64e32211de965a6a0d6b1ec3c3d9f3db27ab904282a
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: tests/test_xref_exclusions.py
    sha256: 2ef227846542ebf4b619e39dc7f0903f1c0113a3a3e12559f989d3574282e24c
    role: context
  - path: tests/test_yersiniabactin_review_archive.py
    sha256: e3ff0c03add194950d1d591f3f15e37a02008dc6b4dc0be9c0938d1596df1111
    role: context
targets:
- target_id: naturalproductmech:mibig-66a349ed2d
  path: data/natural_products/alkaloids/yersiniabactin-2.yaml
  label: yersiniabactin
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
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Maintained scoped remediation input
scope:
  description: Scoped successor for one exact owner. Campaign remains3115 owners/243
    components,14 partial owners and zero completed scientific reviews.
  selection: Explicit predecessor findings from the yersiniabactin PR; not a population
    sample.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-66a349ed2d
checks:
- check_id: qc
  name: qc
  status: failed
  required: false
  command: just qc
  exit_code: 1
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Initial QC correctly rejected stale generated README discussion statistics;
    regenerated and superseded by qc-final.
- check_id: docs-stats
  name: docs-stats
  status: passed
  required: true
  command: .venv/bin/python scripts/check_docs.py --write
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Actual command result retained with timing and exact log hash in the remediation
    evidence archive.
- check_id: focused
  name: focused
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_xref_exclusions.py tests/test_structure_corrections.py
    tests/test_seed_skeleton.py tests/test_mibig_locus_evidence_overrides.py tests/test_yersiniabactin_review_archive.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Actual command result retained with timing and exact log hash in the remediation
    evidence archive.
- check_id: scope-audit
  name: scope-audit
  status: passed
  required: true
  command: .venv/bin/python /private/tmp/npmech-yersiniabactin-pr-NHM4I6/audit.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Actual command result retained with timing and exact log hash in the remediation
    evidence archive.
- check_id: reseed-hold
  name: reseed-hold
  status: passed
  required: true
  command: .venv/bin/python scripts/seed_from_sources.py --apply --only naturalproductmech:mibig-66a349ed2d
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Actual command result retained with timing and exact log hash in the remediation
    evidence archive.
- check_id: render
  name: render
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Actual command result retained with timing and exact log hash in the remediation
    evidence archive.
- check_id: qc-final
  name: qc-final
  status: passed
  required: true
  command: just qc
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - validation
  summary: Actual command result retained with timing and exact log hash in the remediation
    evidence archive.
- check_id: initial-focused-fixture
  name: Initial focused fixture check
  status: failed
  required: false
  exit_code: 1
  command: .venv/bin/python -m pytest -q tests/test_xref_exclusions.py tests/test_structure_corrections.py
    tests/test_seed_skeleton.py tests/test_mibig_locus_evidence_overrides.py
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  summary: Initial run:338 passed and1 failed because the synthetic replacement fixture
    marked unrelated rows without replacement-reference metadata. Scoped the fixture
    to its actual target; final focused run passed342 tests.
- check_id: primary-fulltext
  name: Whole-record primary experiment and isolate-form verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  summary: Inherited primary-source access limitations remain. No restricted source
    was retried; no whole-record sign-off or native REVIEWED promotion.
evidence:
- evidence_id: previous
  kind: record_content
  reference: reviews/structured/20261013T115040Z-yersiniabactin-2/review.yaml
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: 0abc8cf956e27fa04f8b99ab57350325520b0ef832eb13a41a2fadfddea7438b
  summary: Immutable historical findings and full-text limitations retained; this
    successor is scoped remediation, not a new whole-record review.
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/alkaloids/yersiniabactin-2.yaml
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: 501b4d7def902f0e3762cff08463cfe34dc72c397f1069520b298844ba6bddbd
  summary: Complete regenerated owner, history and all fields inspected after canonical
    capture. No graph components are referenced. Chemistry, taxonomy, grades, occurrences
    and SEEDED status are unchanged.
- evidence_id: strain-table
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: 8762b6c3e9b048d64965049aad4addbaefdf76e817f6043e42301c68e301c25a
  summary: Exact untouched source rows are SHA256-pinned; source-specific strain qualifications
    add separate curator evidence only.
- evidence_id: xref-table
  kind: record_content
  reference: curation/mibig_xref_exclusions.tsv
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: 7f2c7a379c0ccf72311ae69c49d5f68c65b56768fd4c785ce9ef47ee7d1bf7b2
  summary: BGC0000467:1 PubChem5462519 exclusion is source-row-pinned; raw assertion
    and attribution survive in a table-owned discussion. The sibling xref remains.
- evidence_id: audit
  kind: validation
  reference: reviews/evidence/20261013-yersiniabactin-remediation/scope-audit.json
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: a8a24569daf74a06a0d64a4fdd32f4d50f8ae8f88e97fc7469ed1cbaf28172a4
  summary: Ignored-inclusive audit covers 3115 owners and243 components; only the
    two intended owners change, with an exact allowed-field comparison. Raw inventories
    and PATHS.tsv are unchanged.
- evidence_id: validation
  kind: validation
  reference: reviews/evidence/20261013-yersiniabactin-remediation/qc-final.log
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: e2f7633602ce2bbab6f66425717fd73ba471ff1b073bdb298c638fc1ffa2431d
  summary: Fresh complete native QC after regenerating README statistics; deterministic
    success is not whole-record scientific sign-off.
- evidence_id: AM236324.1.embl
  kind: database
  reference: reviews/evidence/20261013-yersiniabactin/artifacts/AM236324.1.embl.gz
  accessed_at: '2026-10-13T12:23:29.999563Z'
  support: supports
  snapshot_sha256: 8ce87778e0673e66b25ed7ca1d0e433197e49e8ac209c197a6d248083e21aefa
  summary: Inspected exact source feature identifies taxon562 and strain A0 34/86;
    genomic context is not chemical-detection evidence.
assessments:
- assessment_id: remediation
  area: evidence
  topic: Supported scoped corrections
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - previous
  - owner
  - strain-table
  - xref-table
  - audit
  - validation
  - AM236324.1.embl
  summary: Exact source strain context is now retained. The unspecified owner no longer
    asserts nonexact PubChem equivalence; the sibling retains its valid xref. Imported
    scientific claims and identity remain unchanged.
- assessment_id: remaining
  area: completeness
  topic: Whole-record scientific completeness
  outcome: unknown
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  evidence_ids:
  - previous
  - owner
  summary: Incomplete primary experimental and isolated-form verification remains.
    The E.coli occurrence question is not resolved by strain qualification or by adding
    a discussion.
findings:
- finding_id: F1
  issue_key: yersiniabactin-BGC0001055-producer-strain
  category: scope
  severity: minor
  status: resolved
  certainty: confirmed
  title: Producer assertion drops the available A0 34/86 strain
  description: The species-level taxon562 producer has neither strain nor a strain
    qualifier. AM236324.1 and the cited paper identify A0 34/86. Preserve this context
    without changing the taxon or upgrading the source-assertion evidence.
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  field_paths:
  - producer_organisms[0].strain
  evidence_ids:
  - previous
  - owner
  - strain-table
  - xref-table
  - audit
  - validation
  - AM236324.1.embl
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
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Maintained scoped remediation input
  rule_id: review-checklist:Identity; Equivalence; Producer organisms; Occurrences;
    docs/CURATION.md:Evidence rules
  native_severity: minor
  normalization_reason: Material unsupported identity/evidence is major; bounded lost
    strain provenance is minor. Provisional findings require source adjudication before
    correction.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T115040Z-yersiniabactin-2
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/900
  disposition_reason: Exact-source-pinned correction is emitted through the guarded
    seeder; focused regressions and native QC pass. Original source assertion/provenance,
    both chemical identities and native status remain. This resolves only the named
    defect, not whole-record scientific completeness.
- finding_id: F2
  issue_key: yersiniabactin-lotus-ecoli-genomic-citation
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: E.coli occurrence needs direct chemical-detection support
  description: 'The occurrence claims that this structure was found in E.coli, but
    its DOI is a comparative-genomics paper whose inspected abstract reports genes
    rather than metabolite detection. This is a provisional evidence gap, not proof
    that the complete paper contains no chemical experiment, nor proof of nonproduction.
    The new curator discussion records this limitation without deleting the LOTUS
    assertion. GitHub #902 remains open.'
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  field_paths:
  - occurrences[3].evidence
  evidence_ids:
  - previous
  - owner
  - strain-table
  - xref-table
  - audit
  - validation
  - AM236324.1.embl
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
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: Maintained scoped remediation input
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Maintained scoped remediation input
  rule_id: review-checklist:Identity; Equivalence; Producer organisms; Occurrences;
    docs/CURATION.md:Evidence rules
  native_severity: major
  normalization_reason: Material unsupported identity/evidence is major; bounded lost
    strain provenance is minor. Provisional findings require source adjudication before
    correction.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T115040Z-yersiniabactin-2
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/902
actions:
- action_id: A2
  description: With authorized article access, locate the exact E.coli isolation/detection
    result or adjudicate the LOTUS occurrence as unsupported. Do not remove it solely
    from abstract silence. If correction is needed, implement a tested source-row-pinned
    extraction/overlay path; reserved decisions.tsv cannot do this.
  finding_ids:
  - F2
  target_ids:
  - naturalproductmech:mibig-66a349ed2d
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Exact imported occurrence row
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Occurrence extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Occurrence emission
  acceptance_checks:
  - Inspect the complete cited paper or user-supplied source without bypassing access
    restrictions.
  - Evidence must identify compound form, A0 34/86 and a chemical detection experiment
    rather than gene presence.
  - Any later row exclusion preserves provenance and passes exact-key occurrence,
    reproduction and full QC regressions.
limitations:
- Partial scoped disposition, not a whole-record or whole-corpus pass. All inherited
  access restrictions remain.
- 'Only three supported defects are resolved across these two successors; GitHub #902
  stays open. Records remain SEEDED.'
- Inspected in an isolated worktree at durable main8b5a3ebf, populated with byte-identical
  remediated inputs. Working-tree hashes are attestations, not a claim the remediated
  bytes existed in the base commit.
- Original review files and historical campaign checkpoint are immutable; no unassessed
  owner was removed from the campaign.
- Fresh full QC covers the implementation and historical archive. Final successor
  pairs require their own canonical check and final-head CI.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T115040Z-yersiniabactin-2
  relationship: Exact finding dispositions; remaining limitations retained
links:
- https://github.com/CultureBotAI/NaturalProductMech/pull/898
```
