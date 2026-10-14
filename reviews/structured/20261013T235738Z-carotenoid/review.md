# Carotenoid exact-owner review: carotenoid

- Review: 20261013T235738Z-carotenoid
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T23:47:59.159483Z
- Finished UTC: 2026-10-13T23:57:38.059572Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed identity blocker and independent major cluster-class leak.

## Scope And Provenance

Entire exact owner and resolved mechanism at the immutable base.

Selection: Next exact owner in the 3115-record campaign; same-name sibling is reviewed separately.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 1131b6f7dbb5550da182effa1b396ab790bc42c6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-0f4777d2a4 | data/natural_products/polyketides/carotenoid.yaml | generated | carotenoid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| carotenoid-inspect | passed | True | naturalproductmech:mibig-0f4777d2a4 | Canonical input inspection before assessment. |
| strict | passed | True | naturalproductmech:mibig-0f4777d2a4 | Both exact owners pass closed-schema validation with zero errors. |
| chemistry | passed | True | naturalproductmech:mibig-0f4777d2a4 | Pinned graph roundtrip, registry comparison and structured source checks passed. |
| labels | passed | True | naturalproductmech:mibig-0f4777d2a4 | Full label gate passes with 499 nonblocking warnings and 4649 adapter skips; no primary-identity guarantee. |
| Exact-base full QC | passed | True | naturalproductmech:mibig-0f4777d2a4 | Applies only to the reviewed 1131b6f7 base, not subsequent branch edits. |
| All claim-specific primary structures and experiments | unavailable | True | naturalproductmech:mibig-0f4777d2a4 | Incomplete primary/figure/supplement adjudication; partial review. PMC2879347 XML returned HTTP500 and NPA013316 HTTP403; neither is scientific negative evidence. |

## Scientific And Domain Assessments

### One exact compound versus class-level source concepts

identity: concern. Targets: naturalproductmech:mibig-0f4777d2a4.

F1 is a confirmed identity conflict. A valid key and exact registry match cannot validate mismatched biological joins or a generic class as one individual product.

### Chemical graph and stereochemical resolution

consistency: supported. Targets: naturalproductmech:mibig-0f4777d2a4.

All thirteen tetrahedral centers are assigned; stereo_complete:true agrees with this encoding.

### Exact xrefs and minted identity

grounding: unknown. Targets: naturalproductmech:mibig-0f4777d2a4.

PubChem is an exact graph match and pinned ChEBI has no exact key. NPAtlas NPA013316 remains unverified after403; no xref exclusion is justified from that denial.

### Computed filing and asserted BGC classes

representation: concern. Targets: naturalproductmech:mibig-0f4777d2a4.

The filing and NPClassifier version reproduce pinned classification; origin is a separate source assertion. F2 is false per-cluster PKS attribution, not an error in computed polyketide filing of the encoded anthracycline.

### Native organisms, taxonomy and engineered expression

scope: concern. Targets: naturalproductmech:mibig-0f4777d2a4.

MIBiG supplies SOURCE_ASSERTION; locus methods remain CLUSTER_UNSTATED, not upgraded to experimental proof. Taxon IDs resolve, but exact-product support is compromised by F1. Deposit strain propagation and experimental context require later adjudication.

### Structure-organism-reference triples

evidence: concern. Targets: naturalproductmech:mibig-0f4777d2a4.

LOTUS joins remain cited database assertions distinct from production. The abstract-level product conflicts mean exact-structure occurrence support cannot be accepted wholesale. All occurrence full texts, including bibliography-only transfers, remain unadjudicated.

### Exact version, organism and locus support

evidence: concern. Targets: naturalproductmech:mibig-0f4777d2a4.

Versioned source entries and deposited accessions resolve, but generic product labels and conflicting primary products prevent exact-compound sign-off. No cluster method upgrade is inferred from gene annotations.

### Activities, targets, mechanisms and datasets

graph: not_applicable. Targets: naturalproductmech:mibig-0f4777d2a4.

No assay, activity summary, target, clinical assertion, pathway, inline graph, graph reference or dataset is asserted. Missing optional content is not a defect. Do not copy family-level activity or expression-module data onto the uncertain product.

### Generated boundaries, history and status

ownership: supported. Targets: naturalproductmech:mibig-0f4777d2a4.

Three seed events and SEEDED status are preserved at the reviewed base. Source owners are known; record-only rewrites and silent status promotion are prohibited.

## Findings

### F1: Cosmomycin B structure is labeled carotenoid and joined to Algoriphagus

blocker / open / confirmed; issue key: carotenoid-cosmomycin-identity-conflict.

The stored anthracycline and exact CID156935 match cosmomycin B. BGC0000650 and the Algoriphagus LOTUS assertion cite a flexixanthin study, not cosmomycin B. This is a demonstrated identity/scope conflict; exact replacement and BGC0000214 congener support still require primary adjudication.

### F2: BGC0000650 inherits PKS from a different cluster

major / open / confirmed; issue key: mibig-cluster-class-union-leak.

The record-level class union is copied onto the second cluster. The pinned and official BGC0000650v3 class is terpene only. The resulting extra PKS assertion is an independent generator defect.

## Recommended Actions And Acceptance Checks

### A1

Track #952; add an explicit cited unresolved curator discussion, then obtain exact primary structures and implement reviewed source correction/withholding with source pins. Re-audit all affected biological joins. Preserve exact registry xrefs and unresolved stereochemistry; no guessed replacement.

- Each source concept has exact primary compound/experiment support or explicit maintained withholding.
- LOTUS occurrences are independently re-audited; no old-key claim transfer.
- Native/engineered and deposit strain context remain explicit; strict/reproduction/QC pass; linked successor review adjudicates the finding.

### A2

Fix #951 using a per-row class list while retaining the owner union; regenerate only actual changes and audit the full blast radius.

- Disjoint, hybrid, duplicate, empty and unmapped class tests pass in both canonical accession orders.
- Every changed cluster equals its own pinned mapped classes; no other source fields or component content change.
- Canary, strict, reproduction and full QC pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| owner | data/natural_products/polyketides/carotenoid.yaml; Exact owner at the recorded base, before publication fixes | supports | Complete raw owner, all nested assertions and history read; read_natural_product resolved the entire mechanism. No graph references are present. |
| chemistry | /private/tmp/npmech-carotenoid-review-QbnJL2/source-inspection.json; chemistry section; script and execution receipt retained | supports | Pinned RDKit 2026.03.5 reproduces full InChI/key and C40H53NO14; 13 tetrahedral centers assigned, neutral charge. This checks graph encoding, not experimental determination. |
| registry | https://pubchem.ncbi.nlm.nih.gov/compound/156935; PUG REST properties and synonyms payloads; original fetch receipts in /private/tmp/npmech-carotenoid-review-wTUdYJ | supports | The xref agrees with the full encoded InChI and key. Synonym response names Cosmomycin B; related names do not independently validate production. |
| mibig | https://mibig.secondarymetabolites.org/repository/; source-inspection.json mibig section; exact source URLs and payload hashes in capture.json | supports | Exact BGC0000214v5 and BGC0000650v3 are active and both encode MYQIMJTUIOIEOX-LVWNLLCFSA-N. The former names cosmomycin B/PKS, the latter carotenoid/terpene. Taxon IDs, sequence accessions, legacy references and empty locus-method lists were compared to the pinned raw inventory and owner. Source quality is not scientific proof. |
| primary | PMID:16625353; Full corresponding PubMed title/abstract and article identifiers, not full paper or supplement | refutes | The Algoriphagus study abstract identifies native flexixanthin and beta-carotene from CrtYcd expression in E. coli, not the stored anthracycline. PMID16810496 concerns cosmomycin glycosyltransferases but the abstract does not settle the exact B congener/locus assignment. |
| inventories | data/raw/mibig_compounds.tsv; source-inspection.json inventories; complete TSV scans, including all rows | supports | Structured exact-key scans find no pinned ChEBI or AntibioticMech match for either owner. NPClassifier and LOTUS rows match the seeded joins. Both BioAssay rows are no-data sentinels, not activity observations. |
| context | https://www.ncbi.nlm.nih.gov/nuccore/; source-inspection.json sequences/taxonomy; original XML payloads and fetch receipts | context_only | All eighteen versioned GenBank source qualifiers and twenty-five taxonomy records were parsed. Deposits distinguish strain, organism and cloning context. IDs resolve; current preferred names can differ from source labels. Detailed strain propagation and synonym review are incomplete. |
| adapter | /private/tmp/npmech-carotenoid-review-QbnJL2/imodulondb-crt.log; Dataset inventory and crt search outputs | context_only | The structured adapter returned nine crt-related genes and no iModulon hits for the covered C. glutamicum dataset263. No module summary applies; expression-gene context does not establish exact compound identity or the MJ233 deposit strain. |
| local-search | /private/tmp/npmech-carotenoid-review-QbnJL2/local-search.log; Recorded rg command and complete log | supports | Ignored/hidden-inclusive search located current source owners and historical diagnostics. No prior canonical review of either owner exists among the 56 hash-checked predecessor observations. |
| rules | docs/CURATION.md; Current maintained boundaries and native REVIEWED gate | supports | Generated fields require maintained inputs. decisions.tsv is reserved and not consumed. Exact product identity, producer scope and compound-specific BGC support are required before REVIEWED. |
| ci | https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38485037460; Merge-group QC log and receipt retained in /private/tmp/npmech-bryostatin-publish-xDdyDA | supports | Full QC succeeded on the exact immutable base reviewed here, including corpus strict/history/reference/provenance and reproduction gates. Reused commit-bound evidence, not a fresh local run or scientific sign-off. |
| class-leak | scripts/seed_from_sources.py; Base lines1006-1124; regression-confirmed.log; test covers both accession orders, hybrid/duplicate/empty/unmapped cases | refutes | At the reviewed base the row loop accumulates the owner class union and copies it onto subsequent clusters. BGC0000650 therefore inherits PKS from BGC0000214 although the pinned and official source classes contain only terpene. Six of eight adversarial regression cases fail before the fix. |

## Limits And Additional Notes

- Primary full texts, structural figures and supplements were not fully adjudicated; this is not complete scientific sign-off.
- PMC2879347 XML returned HTTP500. NPA013316 returned HTTP403 and was not retried through an alternate route.
- 2019 PDF retrieval is not counted as complete inspection. Older occurrence references and bibliography-only transfers remain unverified.
- Taxonomy IDs and deposit qualifiers were inspected, but all historical names/strain propagation are not fully adjudicated.
- Base QC is reused commit-bound evidence; subsequent branch fixes require fresh QC. Label warnings/skips remain as disclosed.
- Absence searches include ignored/hidden files within declared roots, excluding compressed contents; no universal literature-absence claim.
- This observation deliberately assesses base1131b6f7 before the separately authorized publication fixes.
- Exact PubChem matches are not proposed for exclusion. Optional missing graphs/assays are not findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T235738Z-carotenoid
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Carotenoid exact-owner review: carotenoid'
started_at: '2026-10-13T23:47:59.159483Z'
finished_at: '2026-10-13T23:57:38.059572Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant conducting the corpus campaign; not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
native_verdict: SEEDED retained; exact-product sign-off blocked
scientific_review: true
summary: Confirmed identity blocker and independent major cluster-class leak.
source:
  git_revision: 1131b6f7dbb5550da182effa1b396ab790bc42c6
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: CLAUDE.md
    sha256: 49e2ab03c7e82013e9d68356de2c9965c9f8517a3408a44124076f4ca1b529cd
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
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f3f808ad1e58d79947aa82ecf1272e465cfbef57e5a4cd646731af23bb48ce75
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: a1eb14fec4a7cee0c2fc25c43091e75af24ae62c44c4f7659ed7aedf0e6a0e6c
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 6f879bb9f2c9be6b6e8de8c013dbaebe09075b7e106790ea303a17006761ea11
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: f61d7ba85ffd21837cd2b625f83c4681c4663e72503466b40eba3f4ab0204bc1
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 18b61c1e5a69112c99cea1373791cd1ec571b7084bfd9198ab68fa551f5d531a
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/polyketides/carotenoid.yaml
    sha256: 52dbab7761e857b68d74ec6ca681e8aa15e6c8679ad157f16a511feec914256f
    role: target
  - path: data/natural_products/terpenoids/carotenoid-2.yaml
    sha256: 450aedab428d79b5a5e9de7f483bed4bd622c750813173641200fcf86f0e2ecd
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 373f049029be3db137e062ff5f872a2400a9d5b423f3e108ea44ebde2f8dcc7d
    role: context
  - path: data/raw/antibioticmech_inchikeys.tsv
    sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
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
    sha256: 7b9b9f78f5b14aea9fabb163bbaa9e842920a7e9b07deac8f98c97666e9e23fc
    role: context
  - path: data/raw/pubchem_bioassay.tsv
    sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
    role: context
  - path: docs/CURATION.md
    sha256: 3ab166b341e5f3f1eaaee1b2af2485ac575c1a1eab1570bbf1d8d2d3ba76e53e
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
  - path: scripts/extract_lotus.py
    sha256: 8a8c524f60f85d2bb54412ca055a6a45e0d37ec5f4584d8d70be454b8f664290
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/extract_pubchem_bioassay.py
    sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 09a5881dfc8eda563a6c688741e667b53298e5f23a8f482e7adb440a2fa68c1c
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: a8b8834788b4714cf1cb0d1cc410d5c2f88112a32ad8621c8e043f0a4bc38a9d
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
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
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
targets:
- target_id: naturalproductmech:mibig-0f4777d2a4
  path: data/natural_products/polyketides/carotenoid.yaml
  label: carotenoid
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
    role: Implemented complete-row-pinned PubChem and NPAtlas exclusions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Imported compound-specific assay observations
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: BioAssay extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_isolates.tsv
    role: Implemented pinned isolate context
scope:
  description: Entire exact owner and resolved mechanism at the immutable base.
  selection: Next exact owner in the 3115-record campaign; same-name sibling is reviewed
    separately.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  exclusions:
  - target: Other 3114 owners
    reason: Outside this one-owner observation, not omitted from campaign accounting.
checks:
- check_id: carotenoid-inspect
  name: carotenoid-inspect
  status: passed
  required: true
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/npmech-carotenoid-review-QbnJL2/carotenoid-targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/review-yaml-record/SKILL.md --input CLAUDE.md --input conf/id_label_targets.yaml
    --input conf/producer_evidence.tsv --input conf/record_review.yaml --input curation/decisions.tsv
    --input curation/mibig_claim_references.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input curation/mibig_producer_isolates.tsv --input curation/mibig_producer_strains.tsv
    --input curation/mibig_structure_corrections.tsv --input curation/mibig_xref_exclusions.tsv
    --input curation/pubchem_bioassay_exclusions.tsv --input data/natural_products/PATHS.tsv
    --input data/natural_products/polyketides/carotenoid.yaml --input data/natural_products/terpenoids/carotenoid-2.yaml
    --input data/raw/MANIFEST.yaml --input data/raw/antibioticmech_inchikeys.tsv --input
    data/raw/chebi_origins.tsv --input data/raw/chebi_structures.tsv --input data/raw/corpus_taxa.obo
    --input data/raw/lotus_occurrences.tsv --input data/raw/mibig_compounds.tsv --input
    data/raw/npclassifier.tsv --input data/raw/pubchem_bioassay.tsv --input docs/CURATION.md
    --input docs/HARMONIZATION.md --input docs/record-review-profile.md --input docs/record-reviews.md
    --input justfile --input pyproject.toml --input schema/record_review.yaml --input
    scripts/extract_lotus.py --input scripts/extract_mibig.py --input scripts/extract_pubchem_bioassay.py
    --input scripts/record_review.py --input scripts/run_qc.py --input scripts/seed_from_sources.py
    --input src/naturalproductmech/curate/bioassay_exclusions.py --input src/naturalproductmech/curate/producer_strains.py
    --input src/naturalproductmech/curate/structure_corrections.py --input src/naturalproductmech/curate/xref_exclusions.py
    --input src/naturalproductmech/graph_components.py --input src/naturalproductmech/schema/history.yaml
    --input src/naturalproductmech/schema/mech_shared.yaml --input src/naturalproductmech/schema/naturalproductmech.yaml
    --input uv.lock
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  summary: Canonical input inspection before assessment.
  scope_note: Actual execution 2026-10-13T23:47:59.178437Z..2026-10-13T23:48:01.280141Z;
    /private/tmp/npmech-carotenoid-review-QbnJL2/carotenoid-inspect.json; SHA256 7442b59e4ba1dc15e7ebdc94314e01715ab00e8b3535edddf7f29da006d7872b
- check_id: strict
  name: strict
  status: passed
  required: true
  command: just validate-strict data/natural_products/polyketides/carotenoid.yaml
    data/natural_products/terpenoids/carotenoid-2.yaml --out /private/tmp/npmech-carotenoid-review-QbnJL2/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  summary: Both exact owners pass closed-schema validation with zero errors.
  scope_note: Actual execution 2026-10-13T23:48:14.193809Z..2026-10-13T23:48:17.929234Z;
    /private/tmp/npmech-carotenoid-review-QbnJL2/strict.log; SHA256 f8bf701d3bc1efcc1b1f54df95d092855f78c67a846e071b1b421e0ecd0b977c
- check_id: chemistry
  name: chemistry
  status: passed
  required: true
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-carotenoid-review-QbnJL2/inspect_sources.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  summary: Pinned graph roundtrip, registry comparison and structured source checks
    passed.
  scope_note: Actual execution 2026-10-13T23:54:09.608824Z..2026-10-13T23:54:12.203795Z;
    /private/tmp/npmech-carotenoid-review-QbnJL2/chemistry.log; SHA256 94b4415817c6c8b4bfe636933a7d8d2a714294e2858481f8f540d5b1b7df9015
- check_id: labels
  name: labels
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  summary: Full label gate passes with 499 nonblocking warnings and 4649 adapter skips;
    no primary-identity guarantee.
  scope_note: Actual execution 2026-10-13T23:48:15.267179Z..2026-10-13T23:50:05.652164Z;
    /private/tmp/npmech-carotenoid-review-QbnJL2/labels.log; SHA256 19a4f6cca7894851de23ee2062f52d29b32def53c7b4f59edbc6c45ec4ce9828
- check_id: base-qc
  name: Exact-base full QC
  status: passed
  required: true
  command: just qc (reused successful exact-base CI execution)
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - ci
  summary: Applies only to the reviewed 1131b6f7 base, not subsequent branch edits.
- check_id: primary-closure
  name: All claim-specific primary structures and experiments
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  summary: Incomplete primary/figure/supplement adjudication; partial review. PMC2879347
    XML returned HTTP500 and NPA013316 HTTP403; neither is scientific negative evidence.
evidence:
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/polyketides/carotenoid.yaml
  summary: Complete raw owner, all nested assertions and history read; read_natural_product
    resolved the entire mechanism. No graph references are present.
  locator: Exact owner at the recorded base, before publication fixes
  accessed_at: '2026-10-13T23:57:38.042472Z'
  support: supports
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-carotenoid-review-QbnJL2/source-inspection.json
  summary: Pinned RDKit 2026.03.5 reproduces full InChI/key and C40H53NO14; 13 tetrahedral
    centers assigned, neutral charge. This checks graph encoding, not experimental
    determination.
  locator: chemistry section; script and execution receipt retained
  accessed_at: '2026-10-13T23:57:38.042566Z'
  support: supports
  snapshot_sha256: c24fb775db91ba76b5838f42853e0da623735eea2215129135dd43accabee6b0
- evidence_id: registry
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/156935
  summary: The xref agrees with the full encoded InChI and key. Synonym response names
    Cosmomycin B; related names do not independently validate production.
  locator: PUG REST properties and synonyms payloads; original fetch receipts in /private/tmp/npmech-carotenoid-review-wTUdYJ
  accessed_at: '2026-10-13T23:57:38.042838Z'
  support: supports
  snapshot_sha256: 0fec32ec555e23e6775094907b4de26d17af3f893bbb8a8231bebfa3967c2a7e
- evidence_id: mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/
  summary: Exact BGC0000214v5 and BGC0000650v3 are active and both encode MYQIMJTUIOIEOX-LVWNLLCFSA-N.
    The former names cosmomycin B/PKS, the latter carotenoid/terpene. Taxon IDs, sequence
    accessions, legacy references and empty locus-method lists were compared to the
    pinned raw inventory and owner. Source quality is not scientific proof.
  locator: source-inspection.json mibig section; exact source URLs and payload hashes
    in capture.json
  accessed_at: '2026-10-13T23:57:38.042941Z'
  support: supports
  snapshot_sha256: c24fb775db91ba76b5838f42853e0da623735eea2215129135dd43accabee6b0
- evidence_id: primary
  kind: primary_source
  reference: PMID:16625353
  summary: The Algoriphagus study abstract identifies native flexixanthin and beta-carotene
    from CrtYcd expression in E. coli, not the stored anthracycline. PMID16810496
    concerns cosmomycin glycosyltransferases but the abstract does not settle the
    exact B congener/locus assignment.
  locator: Full corresponding PubMed title/abstract and article identifiers, not full
    paper or supplement
  accessed_at: '2026-10-13T23:57:38.043134Z'
  support: refutes
  snapshot_sha256: 83509aa808bcdf8221f344de6e18b9b5e3de4cc3eeae71373360acf9339f9ed5
- evidence_id: inventories
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  summary: Structured exact-key scans find no pinned ChEBI or AntibioticMech match
    for either owner. NPClassifier and LOTUS rows match the seeded joins. Both BioAssay
    rows are no-data sentinels, not activity observations.
  locator: source-inspection.json inventories; complete TSV scans, including all rows
  accessed_at: '2026-10-13T23:57:38.043603Z'
  support: supports
  snapshot_sha256: c24fb775db91ba76b5838f42853e0da623735eea2215129135dd43accabee6b0
- evidence_id: context
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/
  summary: All eighteen versioned GenBank source qualifiers and twenty-five taxonomy
    records were parsed. Deposits distinguish strain, organism and cloning context.
    IDs resolve; current preferred names can differ from source labels. Detailed strain
    propagation and synonym review are incomplete.
  locator: source-inspection.json sequences/taxonomy; original XML payloads and fetch
    receipts
  accessed_at: '2026-10-13T23:57:38.043789Z'
  support: context_only
  snapshot_sha256: c24fb775db91ba76b5838f42853e0da623735eea2215129135dd43accabee6b0
- evidence_id: adapter
  kind: database
  reference: /private/tmp/npmech-carotenoid-review-QbnJL2/imodulondb-crt.log
  summary: The structured adapter returned nine crt-related genes and no iModulon
    hits for the covered C. glutamicum dataset263. No module summary applies; expression-gene
    context does not establish exact compound identity or the MJ233 deposit strain.
  locator: Dataset inventory and crt search outputs
  accessed_at: '2026-10-13T23:57:38.043989Z'
  support: context_only
  snapshot_sha256: b889f1c8d2828c1b2b7c80d2e79620e24ad8dd43c534750674868c7258bf117d
- evidence_id: local-search
  kind: search
  reference: /private/tmp/npmech-carotenoid-review-QbnJL2/local-search.log
  summary: Ignored/hidden-inclusive search located current source owners and historical
    diagnostics. No prior canonical review of either owner exists among the 56 hash-checked
    predecessor observations.
  locator: Recorded rg command and complete log
  accessed_at: '2026-10-13T23:57:38.044091Z'
  support: supports
  search_scope: data, curation, conf, reviews and .claude; labels, both key connectivity
    blocks and BGC0000650; ignored/hidden included, compressed .gz contents excluded
  snapshot_sha256: bb7dbed54556e4789a3f09bcb390a5a51a73f7b057455e344fff025020b194a4
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  summary: Generated fields require maintained inputs. decisions.tsv is reserved and
    not consumed. Exact product identity, producer scope and compound-specific BGC
    support are required before REVIEWED.
  locator: Current maintained boundaries and native REVIEWED gate
  accessed_at: '2026-10-13T23:57:38.058411Z'
  support: supports
- evidence_id: ci
  kind: validation
  reference: https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38485037460
  summary: Full QC succeeded on the exact immutable base reviewed here, including
    corpus strict/history/reference/provenance and reproduction gates. Reused commit-bound
    evidence, not a fresh local run or scientific sign-off.
  locator: Merge-group QC log and receipt retained in /private/tmp/npmech-bryostatin-publish-xDdyDA
  accessed_at: '2026-10-13T23:57:38.058425Z'
  support: supports
  snapshot_sha256: e2f04917c8af9abfa3a2c6c8f6c855ce282039e436480323e21d9236305869ee
- evidence_id: class-leak
  kind: record_content
  reference: scripts/seed_from_sources.py
  summary: At the reviewed base the row loop accumulates the owner class union and
    copies it onto subsequent clusters. BGC0000650 therefore inherits PKS from BGC0000214
    although the pinned and official source classes contain only terpene. Six of eight
    adversarial regression cases fail before the fix.
  locator: Base lines1006-1124; regression-confirmed.log; test covers both accession
    orders, hybrid/duplicate/empty/unmapped cases
  accessed_at: '2026-10-13T23:57:38.058840Z'
  support: refutes
  snapshot_sha256: 271180269a626c6bd60b678c43c09aa4a7762cc85d97b2dc81580e37c4552bea
assessments:
- assessment_id: identity
  area: identity
  topic: One exact compound versus class-level source concepts
  outcome: concern
  summary: F1 is a confirmed identity conflict. A valid key and exact registry match
    cannot validate mismatched biological joins or a generic class as one individual
    product.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - chemistry
  - registry
  - mibig
  - primary
- assessment_id: encoding
  area: consistency
  topic: Chemical graph and stereochemical resolution
  outcome: supported
  summary: All thirteen tetrahedral centers are assigned; stereo_complete:true agrees
    with this encoding.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - chemistry
- assessment_id: grounding
  area: grounding
  topic: Exact xrefs and minted identity
  outcome: unknown
  summary: PubChem is an exact graph match and pinned ChEBI has no exact key. NPAtlas
    NPA013316 remains unverified after403; no xref exclusion is justified from that
    denial.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - registry
  - inventories
  - owner
- assessment_id: classification
  area: representation
  topic: Computed filing and asserted BGC classes
  outcome: concern
  summary: The filing and NPClassifier version reproduce pinned classification; origin
    is a separate source assertion. F2 is false per-cluster PKS attribution, not an
    error in computed polyketide filing of the encoded anthracycline.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - inventories
  - owner
  - mibig
- assessment_id: origin
  area: scope
  topic: Native organisms, taxonomy and engineered expression
  outcome: concern
  summary: MIBiG supplies SOURCE_ASSERTION; locus methods remain CLUSTER_UNSTATED,
    not upgraded to experimental proof. Taxon IDs resolve, but exact-product support
    is compromised by F1. Deposit strain propagation and experimental context require
    later adjudication.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - mibig
  - context
  - primary
- assessment_id: occurrence
  area: evidence
  topic: Structure-organism-reference triples
  outcome: concern
  summary: LOTUS joins remain cited database assertions distinct from production.
    The abstract-level product conflicts mean exact-structure occurrence support cannot
    be accepted wholesale. All occurrence full texts, including bibliography-only
    transfers, remain unadjudicated.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - inventories
  - primary
- assessment_id: clusters
  area: evidence
  topic: Exact version, organism and locus support
  outcome: concern
  summary: Versioned source entries and deposited accessions resolve, but generic
    product labels and conflicting primary products prevent exact-compound sign-off.
    No cluster method upgrade is inferred from gene annotations.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - mibig
  - context
  - primary
- assessment_id: optional
  area: graph
  topic: Activities, targets, mechanisms and datasets
  outcome: not_applicable
  summary: No assay, activity summary, target, clinical assertion, pathway, inline
    graph, graph reference or dataset is asserted. Missing optional content is not
    a defect. Do not copy family-level activity or expression-module data onto the
    uncertain product.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - inventories
  - adapter
- assessment_id: audit
  area: ownership
  topic: Generated boundaries, history and status
  outcome: supported
  summary: Three seed events and SEEDED status are preserved at the reviewed base.
    Source owners are known; record-only rewrites and silent status promotion are
    prohibited.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  evidence_ids:
  - owner
  - rules
  - ci
findings:
- finding_id: F1
  issue_key: carotenoid-cosmomycin-identity-conflict
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Cosmomycin B structure is labeled carotenoid and joined to Algoriphagus
  description: The stored anthracycline and exact CID156935 match cosmomycin B. BGC0000650
    and the Algoriphagus LOTUS assertion cite a flexixanthin study, not cosmomycin
    B. This is a demonstrated identity/scope conflict; exact replacement and BGC0000214
    congener support still require primary adjudication.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  field_paths:
  - label
  - chemical_structure
  - source_concepts
  - producer_organisms
  - biosynthetic_gene_clusters
  - occurrences
  evidence_ids:
  - owner
  - chemistry
  - registry
  - mibig
  - primary
  rule_id: Individual structure, exact identity and compound-specific origin/BGC gates
  native_severity: blocker
  normalization_reason: The owner denotes an exact structure while material labels/biological
    claims concern different products.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source or generation owner; no direct generated patch
- finding_id: F2
  issue_key: mibig-cluster-class-union-leak
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: BGC0000650 inherits PKS from a different cluster
  description: The record-level class union is copied onto the second cluster. The
    pinned and official BGC0000650v3 class is terpene only. The resulting extra PKS
    assertion is an independent generator defect.
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  field_paths:
  - biosynthetic_gene_clusters[1].bgc_class
  evidence_ids:
  - class-leak
  - mibig
  - owner
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_seed_skeleton.py
    role: Maintained source or generation owner; no direct generated patch
  rule_id: Claim-local asserted classification
  native_severity: major
  normalization_reason: Systemic source-to-claim attribution error survives schema
    validation.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_lotus.py
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source or generation owner; no direct generated patch
  description: 'Track #952; add an explicit cited unresolved curator discussion, then
    obtain exact primary structures and implement reviewed source correction/withholding
    with source pins. Re-audit all affected biological joins. Preserve exact registry
    xrefs and unresolved stereochemistry; no guessed replacement.'
  acceptance_checks:
  - Each source concept has exact primary compound/experiment support or explicit
    maintained withholding.
  - LOTUS occurrences are independently re-audited; no old-key claim transfer.
  - Native/engineered and deposit strain context remain explicit; strict/reproduction/QC
    pass; linked successor review adjudicates the finding.
  generator: Maintained correction path plus guarded canary/re-emission; never direct
    generated patch
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - naturalproductmech:mibig-0f4777d2a4
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained source or generation owner; no direct generated patch
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_seed_skeleton.py
    role: Maintained source or generation owner; no direct generated patch
  description: 'Fix #951 using a per-row class list while retaining the owner union;
    regenerate only actual changes and audit the full blast radius.'
  acceptance_checks:
  - Disjoint, hybrid, duplicate, empty and unmapped class tests pass in both canonical
    accession orders.
  - Every changed cluster equals its own pinned mapped classes; no other source fields
    or component content change.
  - Canary, strict, reproduction and full QC pass.
  generator: scripts/seed_from_sources.py
limitations:
- Primary full texts, structural figures and supplements were not fully adjudicated;
  this is not complete scientific sign-off.
- PMC2879347 XML returned HTTP500. NPA013316 returned HTTP403 and was not retried
  through an alternate route.
- 2019 PDF retrieval is not counted as complete inspection. Older occurrence references
  and bibliography-only transfers remain unverified.
- Taxonomy IDs and deposit qualifiers were inspected, but all historical names/strain
  propagation are not fully adjudicated.
- Base QC is reused commit-bound evidence; subsequent branch fixes require fresh QC.
  Label warnings/skips remain as disclosed.
- Absence searches include ignored/hidden files within declared roots, excluding compressed
  contents; no universal literature-absence claim.
notes:
- This observation deliberately assesses base1131b6f7 before the separately authorized
  publication fixes.
- Exact PubChem matches are not proposed for exclusion. Optional missing graphs/assays
  are not findings.
tags:
- carotenoid
- exact-identity
- record-review-campaign
```
