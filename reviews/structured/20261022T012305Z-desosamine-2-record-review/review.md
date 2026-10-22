# Desosamine (CHEBI:32540, desosamine-2.yaml): post-split record review

- Review: 20261022T012305Z-desosamine-2-record-review
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-22T01:12:00.000000Z
- Finished UTC: 2026-10-22T01:23:05.000000Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete single-record scientific review of data/natural_products/carbohydrates/desosamine-2.yaml (CHEBI:32540, D-desosamine), created in Cycle 1 Stage 1 via SPLIT_SHARED_WITH_CHEBI on MIBiG BGC0000898:1. Confirms exact 3-star ChEBI chemical identity (VTJCSBJRQLZNHE-CSMHCCOUSA-N), clean removal of upstream methymycin xrefs (pubchem:5282034&#124;npatlas:NPA01238), and valid CARBOHYDRATES filing. Identifies missing ATCC 15439 producer strain qualification (F-DES2-001) for Stage 5 remediation and documents the upstream open-chain vs cyclic desosamine and AF079762.1 deposit-grading boundary (F-DES2-002).

## Scope And Provenance

Complete single-record scientific review of CHEBI:32540 (data/natural_products/carbohydrates/desosamine-2.yaml) across identity, structure correction provenance, classification, producer organism, biosynthetic gene cluster, and curation history.

Selection: Newly added/split natural product owner record from Cycle 1 Stage 1 (BGC0000898:1 split from methymycin.yaml onto 3-star CHEBI:32540).
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:32540 | data/natural_products/carbohydrates/desosamine-2.yaml | generated | desosamine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native source inspection (desosamine-2.yaml) | passed | True | CHEBI:32540 | Captured exact Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf and verified SHA256 digest for data/natural_products/carbohydrates/desosamine-2.yaml. |
| Strict schema and semantic validation | passed | True | CHEBI:32540 | desosamine-2.yaml passed strict LinkML validation with 0 ERROR rows. |
| Full-corpus lockfile and filing verification | passed | True | CHEBI:32540 | Confirmed CHEBI:32540 is filed at data/natural_products/carbohydrates/desosamine-2.yaml in exact agreement with data/natural_products/PATHS.tsv. |
| Full-corpus ontology ID-label correspondence | passed | True | CHEBI:32540 | CHEBI:32540 (desosamine) and NCBITaxon:54571 (Streptomyces venezuelae) resolve to canonical ontology labels. |

## Scientific And Domain Assessments

### Exact ChEBI grounding and SPLIT_SHARED_WITH_CHEBI provenance

identity: supported. Targets: CHEBI:32540.

CHEBI:32540 accurately represents stereochemically complete D-desosamine (VTJCSBJRQLZNHE-CSMHCCOUSA-N) split from BGC0000898:1, with contaminated methymycin xrefs removed and full CURATOR_INFERENCE provenance recorded on both producer and BGC claims.

### Missing ATCC 15439 strain qualifier on NCBITaxon:54571 producer claim

completeness: concern. Targets: CHEBI:32540.

producer_organisms[0] records NCBITaxon:54571 (Streptomyces venezuelae) without strain ATCC 15439 because BGC0000898:1 is not yet listed in curation/mibig_producer_strains.tsv.

### Open-chain ChEBI structure vs cyclic BGC0000899 desosamine and AF079762.1 locus grading

representation: concern. Targets: CHEBI:32540.

CHEBI:32540 uses ChEBI 3-star open-chain aldehyde form whereas BGC0000899:1 (desosamine.yaml) uses an ungrounded stereo-incomplete cyclic form; BGC0000898 (AF079762.1) remains CLUSTER_UNSTATED due to upstream MIBiG deposit splitting from BGC0000094 (AF079138.1).

## Findings

### F-DES2-001: Missing ATCC 15439 producer strain qualification on CHEBI:32540 (desosamine-2.yaml)

major / open / confirmed; issue key: pik-des-atcc15439-producer-strain-missing.

producer_organisms[0] on desosamine-2.yaml (seeded from BGC0000898:1) omits strain ATCC 15439 despite explicit attribution in PMID:9770448 (DOI:10.1073/pnas.95.21.12111) and GenBank AF079762.1. Add BGC0000898:1 (along with sibling pik/des rows) to curation/mibig_producer_strains.tsv.

### F-DES2-002: Open-chain vs cyclic desosamine tautomeric separation and AF079762.1 deposit grading boundary

minor / open / confirmed; issue key: desosamine-cyclic-open-chain-and-bgc0000898-locus-split.

CHEBI:32540 encodes open-chain D-desosamine aldehyde (VTJCSBJRQLZNHE-CSMHCCOUSA-N) while BGC0000899:1 (desosamine.yaml) encodes stereo-incomplete cyclic desosamine (ZOYWWAGVGBSJDL-UHFFFAOYSA-N), and BGC0000898 (AF079762.1) is graded CLUSTER_UNSTATED separately from BGC0000094 (AF079138.1).

## Recommended Actions And Acceptance Checks

### qualify-bgc0000898-1-atcc15439

Add BGC0000898:1 (expected_source_row_sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae, strain ATCC 15439, reference DOI:10.1073/pnas.95.21.12111) to curation/mibig_producer_strains.tsv and re-seed desosamine-2.yaml.

- Confirm producer_organisms[0].strain == ATCC 15439 in data/natural_products/carbohydrates/desosamine-2.yaml after running scripts/seed_from_sources.py.
- Confirm strict validation and verify_corpus pass with 0 errors.

### retain-open-chain-chebi-32540-boundary

Retain CHEBI:32540 as a separate exact-structure owner from naturalproductmech:mibig-bc0da8b0f6 and preserve deposit-scoped BGC0000898 grading.

- Do not merge CHEBI:32540 with stereo-incomplete ZOYWWAGVGBSJDL-UHFFFAOYSA-N.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner-yaml | data/natural_products/carbohydrates/desosamine-2.yaml; Full YAML record at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf | supports | Identifier CHEBI:32540, grounding_status EXACT, curation_status SEEDED, Standard InChIKey VTJCSBJRQLZNHE-CSMHCCOUSA-N, np_pathway CARBOHYDRATES, one producer NCBITaxon:54571 (SOURCE_ASSERTION), one BGC mibig:BGC0000898 (AF079762.1, CLUSTER_UNSTATED), and explicit CURATOR_INFERENCE structure-correction notes. |
| chebi-32540 | data/raw/chebi_structures.tsv; CHEBI:32540 row (sha256 7561e3031fa23d8968b38d0bc0fbffdf04b9386bf5ab88c4b00308f413f47da8) | supports | 3-star ChEBI entry CHEBI:32540 (desosamine) defines SMILES [H]C([H])([C@@]([H])(C)O)[C@]([H])(N(C)C)[C@@]([H])(O)C=O and Standard InChIKey VTJCSBJRQLZNHE-CSMHCCOUSA-N (stereo_complete=true). |
| mibig-bgc0000898-1 | data/raw/mibig_compounds.tsv; BGC0000898:1 row (sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae) and curation/mibig_structure_corrections.tsv | supports | Raw row BGC0000898:1 is labeled desosamine in S. venezuelae (NCBITaxon:54571, AF079762.1, PMID:9770448) but carried methymycin SMILES HUKYPYXOBINMND-HYUJHOPRSA-N and xrefs pubchem:5282034&#124;npatlas:NPA01238; SPLIT_SHARED_WITH_CHEBI replaces the structure with CHEBI:32540 and strips the contaminated xrefs. |
| pnas-1998 | DOI:10.1073/pnas.95.21.12111; Xue et al., Proc. Natl. Acad. Sci. U.S.A. 1998;95(21):12111-12116 (PMID:9770448) | supports | Establishes that the desI-desVIII TDP-D-desosamine biosynthetic locus in AF079762.1 / AF079138.1 originates from Streptomyces venezuelae strain ATCC 15439. |

## Limits And Additional Notes

- Stage 4 review is read-only on scientific records; ATCC 15439 producer strain qualification is queued for Stage 5 grouped remediation.
- Open-chain vs cyclic desosamine unification is bounded by upstream 3-star ChEBI coverage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012305Z-desosamine-2-record-review
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Desosamine (CHEBI:32540, desosamine-2.yaml): post-split record review'
started_at: '2026-10-22T01:12:00.000000Z'
finished_at: '2026-10-22T01:23:05.000000Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Same cycle campaign agent auditing the newly split CHEBI:32540
    owner record in Stage 4; not an external human review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: SEEDED retained; SPLIT_SHARED_WITH_CHEBI grounding verified; ATCC
  15439 producer strain qualification queued for Stage 5
scientific_review: true
summary: Complete single-record scientific review of data/natural_products/carbohydrates/desosamine-2.yaml
  (CHEBI:32540, D-desosamine), created in Cycle 1 Stage 1 via SPLIT_SHARED_WITH_CHEBI
  on MIBiG BGC0000898:1. Confirms exact 3-star ChEBI chemical identity (VTJCSBJRQLZNHE-CSMHCCOUSA-N),
  clean removal of upstream methymycin xrefs (pubchem:5282034|npatlas:NPA01238), and
  valid CARBOHYDRATES filing. Identifies missing ATCC 15439 producer strain qualification
  (F-DES2-001) for Stage 5 remediation and documents the upstream open-chain vs cyclic
  desosamine and AF079762.1 deposit-grading boundary (F-DES2-002).
source:
  git_revision: f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 645746a86769610457ad445361746d6d5ccccdd29ddf29fc1ff256d419ff70de
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: CLAUDE.md
    sha256: c783814c18591ea92aaa628fde98e6b0dbf1f59d45d240fe349682eec753e63f
    role: context
  - path: conf/id_label_targets.yaml
    sha256: 24235903e0e8df5793a30e92c551082c71c1c67739ea4e3b5fb0f68853a805e6
    role: context
  - path: conf/producer_evidence.tsv
    sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
    role: context
  - path: conf/record_review.yaml
    sha256: e53c74aea54cae75daeacf22c1acea16a8edd1c123d469845f2a291047e0e8e8
    role: context
  - path: conf/sibling_pins.yaml
    sha256: 39a1d007ee65ba546567e8a34b7a309f75270b872809e1f783fe1fcee55866f2
    role: context
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: 4bc422b93002508b0abb86e0fa0afa49aff88745b5b0dd3bcbf351a68725d766
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f87a4fa580dede966366bece28ccfb6542bdec4a0f810e40cdfc719811407a05
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: b27c2e61e696a285c38bc88c852dbbdc6c06fec8c4584343f2b9146462eea6cf
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/carbohydrates/desosamine-2.yaml
    sha256: e9aa2c5f8c764bac920477fda25577f8352012d088382090ec452c9d747c2f26
    role: target
  - path: data/natural_products/carbohydrates/desosamine.yaml
    sha256: 054f874a6fb55098958357acfab7ecc78bcb597cfb04cf5437e9d74d29702c4d
    role: context
  - path: data/natural_products/polyketides/methymycin.yaml
    sha256: 7c19ea9d7cedee074008cf7bed76bdf2f76abf41d8a659507778b26948b416ee
    role: context
  - path: data/natural_products/polyketides/narbomycin.yaml
    sha256: b112dcc3d151dca470cae5bf9f4528892052edae5707ccc2e3c5a88d224f84de
    role: context
  - path: data/natural_products/polyketides/neomethymycin.yaml
    sha256: fc676329e89ea3bbd693300d380a8c11a231e476c51628f50bd9bb8b382ea1ef
    role: context
  - path: data/natural_products/polyketides/pikromycin.yaml
    sha256: f64b4aaadd9a388a8dc4066f2fe15f052ad6a82bf4fc84884907db82d6d940b1
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
    role: context
  - path: data/raw/antibioticmech_inchikeys.tsv
    sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
    role: context
  - path: data/raw/bindingdb_targets.tsv
    sha256: 3cff45281c35a8b14d4d7784bc4b7af80e8e27779a5667a0292f0d9b022a22c1
    role: context
  - path: data/raw/chebi_origins.tsv
    sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
    role: context
  - path: data/raw/chebi_structures.tsv
    sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
    role: context
  - path: data/raw/corpus_taxa.obo
    sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
    role: context
  - path: data/raw/lotus_occurrences.tsv
    sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
    role: context
  - path: data/raw/mibig_compounds.tsv
    sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
    role: context
  - path: data/raw/npclassifier.tsv
    sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: docs/CURATION.md
    sha256: 6873daace2f9e2225ef3d6830e993ac8cf8d01cec66b779fa5829309d77b3eaf
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
  - path: justfile
    sha256: 4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550
    role: context
  - path: pyproject.toml
    sha256: 02505a46585e870eac7333f31a6773df51465ef13969d4d490fbc0247931d85c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curation_worklist.py
    sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_strict.py
    sha256: e9b844d10fb7d2889521677716098da5883c7fd7d3c887a5cb600b87bbca0c21
    role: context
  - path: scripts/verify_corpus.py
    sha256: 3e79d6e18e43010a84e2ef7857625655185796d447ee12979a94cd836d756b60
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/naturalproductmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: CHEBI:32540
  path: data/natural_products/carbohydrates/desosamine-2.yaml
  label: desosamine
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/carbohydrates/desosamine-2.yaml
    role: Generated natural product owner record
scope:
  description: Complete single-record scientific review of CHEBI:32540 (data/natural_products/carbohydrates/desosamine-2.yaml)
    across identity, structure correction provenance, classification, producer organism,
    biosynthetic gene cluster, and curation history.
  selection: Newly added/split natural product owner record from Cycle 1 Stage 1 (BGC0000898:1
    split from methymycin.yaml onto 3-star CHEBI:32540).
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:32540
  exclusions:
  - target: Remaining 3,115 natural product owner records and 246 standalone causal
      graph components in the frozen 3,362-file corpus inventory
    reason: Single-record review denominator is strictly 1; sibling pik/des cohort
      records are covered in 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort.
checks:
- check_id: inspect-record
  name: Native source inspection (desosamine-2.yaml)
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py inspect --targets /tmp/stage4_targets_record.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - owner-yaml
  summary: Captured exact Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf and verified
    SHA256 digest for data/natural_products/carbohydrates/desosamine-2.yaml.
  scope_note: 2026-10-22T01:22:07.276591Z..2026-10-22T01:22:09.464545Z; output SHA256
    a4f5bca566b6f360c00349f8025ff671582d61a9fd14a43512d08611ebaf2086
- check_id: strict-cohort
  name: Strict schema and semantic validation
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --workers 1 --out /tmp/strict_cohort.tsv
    data/natural_products/carbohydrates/desosamine-2.yaml data/natural_products/carbohydrates/desosamine.yaml
    data/natural_products/polyketides/methymycin.yaml data/natural_products/polyketides/pikromycin.yaml
    data/natural_products/polyketides/neomethymycin.yaml data/natural_products/polyketides/narbomycin.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - owner-yaml
  summary: desosamine-2.yaml passed strict LinkML validation with 0 ERROR rows.
  scope_note: 2026-10-22T01:17:46.004235Z..2026-10-22T01:17:50.285016Z; output SHA256
    dfc2c19d17b3a607f326a6094a754bd80c103487f7676f8acb78d3edccf66785
- check_id: verify-corpus
  name: Full-corpus lockfile and filing verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - owner-yaml
  summary: Confirmed CHEBI:32540 is filed at data/natural_products/carbohydrates/desosamine-2.yaml
    in exact agreement with data/natural_products/PATHS.tsv.
  scope_note: 2026-10-22T01:12:31.470813Z..2026-10-22T01:14:13.653446Z; output SHA256
    c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e
- check_id: validate-id-labels
  name: Full-corpus ontology ID-label correspondence
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/id_label_correspondence.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - chebi-32540
  - mibig-bgc0000898-1
  summary: CHEBI:32540 (desosamine) and NCBITaxon:54571 (Streptomyces venezuelae)
    resolve to canonical ontology labels.
  scope_note: 2026-10-22T01:18:32.625871Z..2026-10-22T01:20:33.968758Z; output SHA256
    c859dad0c7a6023dd517b77fdcb98bb923c85cef6d72bd3ccf600babbb9bc41e
evidence:
- evidence_id: owner-yaml
  kind: record_content
  reference: data/natural_products/carbohydrates/desosamine-2.yaml
  locator: Full YAML record at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
  accessed_at: '2026-10-22T01:22:09.464545Z'
  support: supports
  snapshot_sha256: e9aa2c5f8c764bac920477fda25577f8352012d088382090ec452c9d747c2f26
  summary: Identifier CHEBI:32540, grounding_status EXACT, curation_status SEEDED,
    Standard InChIKey VTJCSBJRQLZNHE-CSMHCCOUSA-N, np_pathway CARBOHYDRATES, one producer
    NCBITaxon:54571 (SOURCE_ASSERTION), one BGC mibig:BGC0000898 (AF079762.1, CLUSTER_UNSTATED),
    and explicit CURATOR_INFERENCE structure-correction notes.
- evidence_id: chebi-32540
  kind: database
  reference: data/raw/chebi_structures.tsv
  locator: CHEBI:32540 row (sha256 7561e3031fa23d8968b38d0bc0fbffdf04b9386bf5ab88c4b00308f413f47da8)
  accessed_at: '2026-10-22T01:13:23.000000Z'
  support: supports
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
  summary: 3-star ChEBI entry CHEBI:32540 (desosamine) defines SMILES [H]C([H])([C@@]([H])(C)O)[C@]([H])(N(C)C)[C@@]([H])(O)C=O
    and Standard InChIKey VTJCSBJRQLZNHE-CSMHCCOUSA-N (stereo_complete=true).
- evidence_id: mibig-bgc0000898-1
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0000898:1 row (sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae)
    and curation/mibig_structure_corrections.tsv
  accessed_at: '2026-10-22T01:13:23.000000Z'
  support: supports
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
  summary: Raw row BGC0000898:1 is labeled desosamine in S. venezuelae (NCBITaxon:54571,
    AF079762.1, PMID:9770448) but carried methymycin SMILES HUKYPYXOBINMND-HYUJHOPRSA-N
    and xrefs pubchem:5282034|npatlas:NPA01238; SPLIT_SHARED_WITH_CHEBI replaces the
    structure with CHEBI:32540 and strips the contaminated xrefs.
- evidence_id: pnas-1998
  kind: primary_source
  reference: DOI:10.1073/pnas.95.21.12111
  locator: Xue et al., Proc. Natl. Acad. Sci. U.S.A. 1998;95(21):12111-12116 (PMID:9770448)
  accessed_at: '2026-10-22T01:12:00.000000Z'
  support: supports
  summary: Establishes that the desI-desVIII TDP-D-desosamine biosynthetic locus in
    AF079762.1 / AF079138.1 originates from Streptomyces venezuelae strain ATCC 15439.
assessments:
- assessment_id: identity-and-grounding
  area: identity
  topic: Exact ChEBI grounding and SPLIT_SHARED_WITH_CHEBI provenance
  outcome: supported
  summary: CHEBI:32540 accurately represents stereochemically complete D-desosamine
    (VTJCSBJRQLZNHE-CSMHCCOUSA-N) split from BGC0000898:1, with contaminated methymycin
    xrefs removed and full CURATOR_INFERENCE provenance recorded on both producer
    and BGC claims.
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - owner-yaml
  - chebi-32540
  - mibig-bgc0000898-1
- assessment_id: producer-strain-completeness
  area: completeness
  topic: Missing ATCC 15439 strain qualifier on NCBITaxon:54571 producer claim
  outcome: concern
  summary: producer_organisms[0] records NCBITaxon:54571 (Streptomyces venezuelae)
    without strain ATCC 15439 because BGC0000898:1 is not yet listed in curation/mibig_producer_strains.tsv.
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - owner-yaml
  - mibig-bgc0000898-1
  - pnas-1998
- assessment_id: tautomer-and-deposit-boundary
  area: representation
  topic: Open-chain ChEBI structure vs cyclic BGC0000899 desosamine and AF079762.1
    locus grading
  outcome: concern
  summary: CHEBI:32540 uses ChEBI 3-star open-chain aldehyde form whereas BGC0000899:1
    (desosamine.yaml) uses an ungrounded stereo-incomplete cyclic form; BGC0000898
    (AF079762.1) remains CLUSTER_UNSTATED due to upstream MIBiG deposit splitting
    from BGC0000094 (AF079138.1).
  target_ids:
  - CHEBI:32540
  evidence_ids:
  - owner-yaml
  - chebi-32540
  - mibig-bgc0000898-1
  - pnas-1998
findings:
- finding_id: F-DES2-001
  issue_key: pik-des-atcc15439-producer-strain-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing ATCC 15439 producer strain qualification on CHEBI:32540 (desosamine-2.yaml)
  description: producer_organisms[0] on desosamine-2.yaml (seeded from BGC0000898:1)
    omits strain ATCC 15439 despite explicit attribution in PMID:9770448 (DOI:10.1073/pnas.95.21.12111)
    and GenBank AF079762.1. Add BGC0000898:1 (along with sibling pik/des rows) to
    curation/mibig_producer_strains.tsv.
  target_ids:
  - CHEBI:32540
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].evidence
  evidence_ids:
  - owner-yaml
  - mibig-bgc0000898-1
  - pnas-1998
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:producer-strain-qualification
  native_severity: major
  normalization_reason: Published producer strain ATCC 15439 is directly supported
    by the cited primary literature and supported by curation/mibig_producer_strains.tsv.
- finding_id: F-DES2-002
  issue_key: desosamine-cyclic-open-chain-and-bgc0000898-locus-split
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Open-chain vs cyclic desosamine tautomeric separation and AF079762.1 deposit
    grading boundary
  description: CHEBI:32540 encodes open-chain D-desosamine aldehyde (VTJCSBJRQLZNHE-CSMHCCOUSA-N)
    while BGC0000899:1 (desosamine.yaml) encodes stereo-incomplete cyclic desosamine
    (ZOYWWAGVGBSJDL-UHFFFAOYSA-N), and BGC0000898 (AF079762.1) is graded CLUSTER_UNSTATED
    separately from BGC0000094 (AF079138.1).
  target_ids:
  - CHEBI:32540
  field_paths:
  - chemical_structure.standard_inchi_key
  - chemical_structure.smiles
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  evidence_ids:
  - owner-yaml
  - chebi-32540
  - mibig-bgc0000898-1
  - pnas-1998
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:exact-structure-and-deposit-boundary
  native_severity: minor
  normalization_reason: Source-limited upstream representation boundary between ChEBI
    3-star open-chain structure and MIBiG deposit split.
actions:
- action_id: qualify-bgc0000898-1-atcc15439
  description: Add BGC0000898:1 (expected_source_row_sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae,
    strain ATCC 15439, reference DOI:10.1073/pnas.95.21.12111) to curation/mibig_producer_strains.tsv
    and re-seed desosamine-2.yaml.
  finding_ids:
  - F-DES2-001
  target_ids:
  - CHEBI:32540
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Confirm producer_organisms[0].strain == ATCC 15439 in data/natural_products/carbohydrates/desosamine-2.yaml
    after running scripts/seed_from_sources.py.
  - Confirm strict validation and verify_corpus pass with 0 errors.
- action_id: retain-open-chain-chebi-32540-boundary
  description: Retain CHEBI:32540 as a separate exact-structure owner from naturalproductmech:mibig-bc0da8b0f6
    and preserve deposit-scoped BGC0000898 grading.
  finding_ids:
  - F-DES2-002
  target_ids:
  - CHEBI:32540
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  acceptance_checks:
  - Do not merge CHEBI:32540 with stereo-incomplete ZOYWWAGVGBSJDL-UHFFFAOYSA-N.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
  relationship: Parent 6-record pik/des category cohort review covering BGC0000094,
    BGC0000898, and BGC0000899.
limitations:
- Stage 4 review is read-only on scientific records; ATCC 15439 producer strain qualification
  is queued for Stage 5 grouped remediation.
- Open-chain vs cyclic desosamine unification is bounded by upstream 3-star ChEBI
  coverage.
```
