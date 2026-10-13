# 2-methylisoborneol: exact-structure and source-support review (BGC0000657)

- Review: 20261013T044353Z-2-methylisoborneol-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T04:25:19Z
- Finished UTC: 2026-10-13T04:43:53.433441Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

A confirmed constitutional identity error survives deterministic validation. The full owner was read and existing claims assessed; unavailable source verification prevents a completed review. One blocker and one provisional major evidence-tier finding.

## Scope And Provenance

One exact record, including the full owner and graph-reference check. This is one observation in an exhaustive 3115-record campaign, not a sample-based corpus verdict.

Selection: Exact path and minted identifier from the ignored-inclusive population inventory; prioritized for same-name/different-constitution risk.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e66f934111777c4ebfe69475d0520c0cfa074785.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-0ed362dd75 | data/natural_products/alkaloids/2-methylisoborneol-2.yaml | generated | 2-methylisoborneol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| second-inspect | passed | True | naturalproductmech:mibig-0ed362dd75 | Canonical target and context hash capture succeeded before assessment. |
| second-strict | passed | True | naturalproductmech:mibig-0ed362dd75 | Closed-schema validation passed for this exact owner, including graph-reference resolution. |
| complete-view | passed | True | naturalproductmech:mibig-0ed362dd75 | The native read_natural_product reader resolves the complete owner view; both selected records have zero graphs and zero component references. |
| qc | passed | True | naturalproductmech:mibig-0ed362dd75 | Full-corpus QC: lint, governed-file sync, documentation, provenance, source queue, tests, strict schema, page freshness, offline reproduction, corpus integrity and report. |
| labels | passed | True | naturalproductmech:mibig-0ed362dd75 | Full-corpus configured ontology/label check. Minted identifiers and database namespaces remain adapter-skipped; this is not chemical identity proof. |
| review-baseline | passed | True | naturalproductmech:mibig-0ed362dd75 | Baseline shared checker found zero structured reviews, including hidden/ignored review paths. Zero is missing coverage, not a pass. |
| review-queue | passed | True | naturalproductmech:mibig-0ed362dd75 | The native exhaustive queue was generated for prioritization; it is not scientific coverage. |
| second-ignored-inclusive-search | passed | True | naturalproductmech:mibig-0ed362dd75 | Ignored-inclusive identifier/label/slug search; no inference from Git-aware search alone. |
| Name versus exact structure | failed | True | naturalproductmech:mibig-0ed362dd75 | The named natural product and the stored molecular constitution disagree; see F1. |
| Live source and identifier verification | unavailable | True | naturalproductmech:mibig-0ed362dd75 | MIBiG BGC0000657, PubChem CID9237955 property lookup, and HQ830028.1 were inaccessible. Their current contents were not inferred from the seeded YAML. |
| Structured expression-module applicability | not_applicable | False | naturalproductmech:mibig-0ed362dd75 | No iModulon, regulator, gene-level expression dataset or protein example is asserted in this target. Local MIBiG source rows were checked; expression modules cannot resolve the chemical identity conflict. |
| Auxiliary chemical serialization consistency | passed | False | naturalproductmech:mibig-0ed362dd75 | Cached RDKit 2024.03.5 reproduces the stored InChI and InChIKey; this is not the project-pinned 2026.3.5 extractor and is not a native gate. |

## Scientific And Domain Assessments

### Exact named chemical form

identity: concern. Targets: naturalproductmech:mibig-0ed362dd75.

F1: the molecular constitution does not match the label or its cited biological context. Minting avoids a false ChEBI link but does not repair the name/structure conflict.

### SMILES, InChI, key and stereochemical encoding

consistency: supported. Targets: naturalproductmech:mibig-0ed362dd75.

The stored serializations agree in the auxiliary calculation, with no undefined tetrahedral centers detected. No formula/charge/mass values are asserted in this YAML. Experimental identity remains refuted by F1.

### Cross-references, parents, congeners and same-name neighbors

grounding: unknown. Targets: naturalproductmech:mibig-0ed362dd75.

The sole xref pubchem:9237955 could not be resolved. The other same-name owner has an unspecified-stereo key; it is not automatically equivalent to ChEBI's stereospecific entry.

### Computed filing versus asserted BGC class and origin

consistency: supported. Targets: naturalproductmech:mibig-0ed362dd75.

ALKALOIDS matches the pinned NPClassifier row for the stored input; the source BGC class remains a separate assertion. The filing mechanism is faithful, but NATURAL_PRODUCT membership is scientifically compromised by F1.

### Taxon identifiers, named strain and broad lineage facet

grounding: supported. Targets: naturalproductmech:mibig-0ed362dd75.

NCBITaxon:1002505 matches Pseudanabaena sp. dqh15 in the pinned taxonomy; CYANOBACTERIAL matches its lineage row. This checks taxon identity, not the claimed chemical product.

### Producer versus locus claim, source version and grade

evidence: concern. Targets: naturalproductmech:mibig-0ed362dd75.

Version-5 BGC_CORRELATED/CLUSTER_CORRELATED faithfully reproduce the imported method. F2 questions whether the attached evidence supports expression-production correlation; it is not a claim that correlation implies native necessity.

### Occurrence versus biosynthesis and exact compound support

evidence: not_applicable. Targets: naturalproductmech:mibig-0ed362dd75.

No occurrence objects are asserted; no occurrence-to-producer promotion is introduced by this review.

### Pathway, all graphs, targets, activities and bioactivity summary

completeness: not_applicable. Targets: naturalproductmech:mibig-0ed362dd75.

The complete raw owner contains no pathway, inline graph, graph references, molecular target, bioactivity observation or activity-summary assertion. Optional empty slots are not findings; mechanism expansion must wait for exact identity.

### Datasets, cross-corpus links, clinical status and discussions

completeness: not_applicable. Targets: naturalproductmech:mibig-0ed362dd75.

No dataset, related-record link, clinical-status claim or discussion is asserted. Genome metadata belongs to the BGC object and is assessed separately. No bibliography or clinical inference is manufactured.

### Generated ownership, status and audit trail

provenance: supported. Targets: naturalproductmech:mibig-0ed362dd75.

Both events are seed-from-sources events and native status remains SEEDED. Reproduction/strict/history coverage in QC establishes structural provenance, not literature review. This report changes neither history nor status.

## Findings

### F1: The structure is not the natural product named by the record

blocker / open / confirmed; issue key: mibig-BGC0000657-compound-1-wrong-constitution.

The stored MBPWQYMDPQWNIL-RYUDHWBXSA-N (C15H16BrN3O4S) is a chemically different constitution from the named compound. The committed MIBiG row already contains the mismatch. A generated record can be byte-reproducible while denoting the wrong molecule. Producer, BGC and natural-origin claims must not be transferred across the identity conflict.

### F2: The cited study does not establish the imported expression-production correlation

major / open / provisional; issue key: mibig-BGC0000657-expression-production-evidence.

The inspected methods/results measure transcripts under light treatments, not matched product abundance. Thus the cited experiment does not establish the imported correlation method. This concern remains provisional pending the complete live entry and any additional supporting evidence.

## Recommended Actions And Acceptance Checks

### A1

Resolve the upstream compound identity and audit every attached claim. Correct or withhold the bad maintained source assertion through an implemented, tested route; do not hand-edit generated YAML or use reserved decisions.tsv. Resolve the intended stereochemical form and PubChem xref independently before selecting a destination. Do not equate the existing unspecified-stereo owner with the stereospecific ChEBI entry by label alone.

- Inspected primary/authority evidence establishes one exact compound form and every retained source claim matches it.
- Regression tests cover this accession and reject name-only merging or transfer of old-key occurrences, assays, graphs or history.
- Run the documented seed dry run and one-record canary before authorized guarded changes; then strict validation, verify-corpus, verify-reproduction, label checks and full QC pass.
- Keep the wrong and intended structures distinct until an explicitly audited migration accounts for every affected owner and published slug.

### A2

Check the complete locus evidence for matched production/transcript data. If unsupported, apply an appropriately pinned evidence-method correction through the implemented override path; preserve the distinction between production, predicted locus assignment, and direct function.

- Inspect any additional cited source before treating the imported method as supported.
- Test the resulting producer and cluster grades separately; never upgrade homology to native characterization.
- After any separately authorized correction, append proper curation provenance and pass strict validation, reproduction and full QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/natural_products/alkaloids/2-methylisoborneol-2.yaml; Entire owner YAML, all fields and both curation events | supports | Exact minted record read in full. No inline graphs or component references. This evidence establishes what is asserted, not whether the science is correct. |
| source-rows | data/raw/mibig_compounds.tsv; BGC0000657, compound_index=1; joined classification, taxonomy and filing rows | supports | Complete parsed source rows and applicable maintained correction tables were inspected. Chemistry and source grades reproduce the imported snapshot; no correction/override row targets this accession. Local extract: /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-local-source-rows.json |
| chemistry | /private/tmp/npmech-all-record-reviews-pU8b8GXS/chemistry-auxiliary.json; data/natural_products/alkaloids/2-methylisoborneol-2.yaml | supports | Auxiliary RDKit 2024.03.5 calculated formula C15H16BrN3O4S, exact stored InChI/Key, and 0 undefined tetrahedral centers. Internal consistency does not authenticate the label. |
| chebi | https://www.ebi.ac.uk/chebi/CHEBI:61987; Name, definition, formula, SMILES, InChI and InChIKey | refutes | 2-Methylisoborneol is C11H20O, key LFYXNXGVLGKVCJ-FBIMIBRVSA-N for the specified stereoisomer. The stored C15H16BrN3O4S is a different constitution; neither unspecified stereochemistry nor protonation explains it. |
| local-search | CultureBotAI/NaturalProductMech@e66f934111777c4ebfe69475d0520c0cfa074785; Full worktree file-content search plus structured source-table selectors | context_only | The same label has another structure owner. Only its locator/key was inspected for collision handling; the other owner is not counted as reviewed. |
| ownership | docs/CURATION.md; MIBiG structure corrections; locus-evidence overrides; generated versus curator ownership | supports | Fixes belong in implemented maintained inputs and tested source transforms, never generated pages or direct owner YAML edits. decisions.tsv is reserved, not consumed. The narrow structure-correction table rejects occupied destinations. |
| qc | /private/tmp/npmech-all-record-reviews-pU8b8GXS/qc.log; Complete current-run log | supports | Native deterministic checks passed on the unchanged corpus. The scientific identity defect survives them. |
| labels | /private/tmp/npmech-all-record-reviews-pU8b8GXS/labels.log; Full configured ontology/label results and warning report | context_only | The minted identity is intentionally not ontology-resolved. Successful configured correspondence checks do not validate its compound name. |
| access-limits | https://mibig.secondarymetabolites.org/repository/BGC0000657/; Direct official URL checks through web tool | unknown | Direct BGC0000657, PubChem CID9237955 property endpoint and NCBI HQ830028.1 requests returned Internal Error; no source content was inferred. |
| pubmed | https://pubmed.ncbi.nlm.nih.gov/21490938/; Bibliographic identity and DOI link | supports | PMID21490938 resolves to Wang et al. 2011 and DOI10.1371/journal.pone.0018665. |
| paper | https://doi.org/10.1371/journal.pone.0018665; Results: isolation and GC-MS, light response; Discussion; Materials and Methods | partial | The paper identifies ordinary 2-MIB in dqh15 against a standard, assigns HQ830028 to its operon, and measures light-dependent transcripts. It does not present paired product measurements for that expression series; direct gene-function experiments are explicitly absent. |

## Limits And Additional Notes

- Required source-currentness checks are unavailable as detailed above; partial completion is deliberate and no scientific pass is claimed.
- The project-pinned RDKit 2026.3.5 was unavailable locally/offline. The explicitly versioned 2024.03.5 calculation is auxiliary only, not a replacement native gate.
- All 3115 records remain in the campaign. The other 3114 records are outside this single-record review; referenced same-name neighbors are not counted as scientifically reviewed.
- No paid providers, source retries, record corrections, status promotions, GitHub issues or other publication actions were performed. Findings/actions are proposed curation, not completed fixes.
- The original zero-review baseline and the population hashes are retained in /private/tmp/npmech-all-record-reviews-pU8b8GXS. Existing ad hoc or generated review-queue content is not structured scientific review.
- All native checks ran against base e66f934111777c4ebfe69475d0520c0cfa074785; external evidence was inspected on 2026-10-13.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T044353Z-2-methylisoborneol-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: '2-methylisoborneol: exact-structure and source-support review (BGC0000657)'
started_at: '2026-10-13T04:25:19Z'
finished_at: '2026-10-13T04:43:53.433441Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread previously curated this repository; no
    claim of independent review. These two source-owned target records were not changed
    during this review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: A confirmed constitutional identity error survives deterministic validation.
  The full owner was read and existing claims assessed; unavailable source verification
  prevents a completed review. One blocker and one provisional major evidence-tier
  finding.
source:
  git_revision: e66f934111777c4ebfe69475d0520c0cfa074785
  state: working_tree
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
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 0b2e8b991c926f9a67a3094964b0335dd1cd347fbf548674fa273db8fac3a4b2
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/alkaloids/2-methylisoborneol-2.yaml
    sha256: 182ccce74f0fc70c82431c5c3820232a9dd066be625033d9ceaa47b302d83393
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: 373f049029be3db137e062ff5f872a2400a9d5b423f3e108ea44ebde2f8dcc7d
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
  - path: data/raw/taxon_groups.tsv
    sha256: f73f228d57d79a1d85a1441efa6829917b1ffecac08cb7bdd4fc855046255f8f
    role: context
  - path: docs/CURATION.md
    sha256: 3b979068592adbb0611de95927ca31eaabb5fb5d791aa09973e3b1e8d5a19011
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 30c7007e57806c245674ce922e0f8c485b1a8a12a9f9fb95850ba6ee4f8cddc2
    role: context
  - path: docs/record-review-profile.md
    sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
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
    sha256: 2da30b7ccf4b9543ecbe02eb0c8662e51a82c0745aa45be28afbf8ceb38fc1be
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One exact record, including the full owner and graph-reference check.
    This is one observation in an exhaustive 3115-record campaign, not a sample-based
    corpus verdict.
  selection: Exact path and minted identifier from the ignored-inclusive population
    inventory; prioritized for same-name/different-constitution risk.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-0ed362dd75
targets:
- target_id: naturalproductmech:mibig-0ed362dd75
  path: data/natural_products/alkaloids/2-methylisoborneol-2.yaml
  label: 2-methylisoborneol
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported source chemistry and cluster claims
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Structure-key harmonization and source grading
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Potential guarded correction route only after structure identity is established
checks:
- check_id: second-inspect
  name: second-inspect
  status: passed
  required: true
  summary: Canonical target and context hash capture succeeded before assessment.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/record_review.py inspect --targets /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-targets.json
    --input CLAUDE.md --input docs/record-review-profile.md --input docs/record-reviews.md
    --input .claude/skills/review-yaml-record/SKILL.md --input .claude/skills/curate-yaml-record/references/review-checklist.md
    --input docs/CURATION.md --input docs/HARMONIZATION.md --input conf/record_review.yaml
    --input schema/record_review.yaml --input src/naturalproductmech/schema/naturalproductmech.yaml
    --input conf/producer_evidence.tsv --input conf/id_label_targets.yaml --input
    data/raw/MANIFEST.yaml --input data/raw/mibig_compounds.tsv --input data/raw/lotus_occurrences.tsv
    --input data/raw/chebi_structures.tsv --input data/raw/corpus_taxa.obo --input
    data/raw/npclassifier.tsv --input data/natural_products/PATHS.tsv --input curation/mibig_structure_corrections.tsv
    --input curation/mibig_locus_evidence_overrides.tsv --input scripts/extract_mibig.py
    --input scripts/extract_lotus.py --input scripts/seed_from_sources.py --input
    data/raw/taxon_groups.tsv
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-inspect.log;
    SHA-256 54bfd1f87a2b73fc045ceab621b2aab86c948e2b4c503582da229be3c897fec8'
- check_id: second-strict
  name: second-strict
  status: passed
  required: true
  summary: Closed-schema validation passed for this exact owner, including graph-reference
    resolution.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/validate_strict.py data/natural_products/alkaloids/2-methylisoborneol-2.yaml
    --out /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-strict.tsv
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-strict.log;
    SHA-256 5c02fe348e33ea2502bdf1dabfd2ccfd7aeef4901c85a068be2ab328fdb8ded3'
- check_id: complete-view
  name: complete-view
  status: passed
  required: true
  summary: The native read_natural_product reader resolves the complete owner view;
    both selected records have zero graphs and zero component references.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    /private/tmp/npmech-all-record-reviews-pU8b8GXS/complete_view.py
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/complete-view.log;
    SHA-256 14911c364922912e663e97731aa3f0b68bfd741bb3a182fbc21caa89eacbd467'
- check_id: qc
  name: qc
  status: passed
  required: true
  summary: 'Full-corpus QC: lint, governed-file sync, documentation, provenance, source
    queue, tests, strict schema, page freshness, offline reproduction, corpus integrity
    and report.'
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/run_qc.py
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/qc.log;
    SHA-256 0c04323074ee7b0b9bf526e53dcd1c8f4208f74f2053e31a464070abb10df41e'
- check_id: labels
  name: labels
  status: passed
  required: true
  summary: Full-corpus configured ontology/label check. Minted identifiers and database
    namespaces remain adapter-skipped; this is not chemical identity proof.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report
    /private/tmp/npmech-all-record-reviews-pU8b8GXS/label-drift.tsv
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/labels.log;
    SHA-256 edd91274291ef54f0e30dcb5fa1049518e6f3ca75ea78ed845a14e51edffa0a6'
- check_id: review-baseline
  name: review-baseline
  status: passed
  required: true
  summary: Baseline shared checker found zero structured reviews, including hidden/ignored
    review paths. Zero is missing coverage, not a pass.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/record_review.py check
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/review-baseline.log;
    SHA-256 250073413f94ddb0b15b3cb220f6cfae1d9cfebb38402955458f22bf06be5b27'
- check_id: review-queue
  name: review-queue
  status: passed
  required: true
  summary: The native exhaustive queue was generated for prioritization; it is not
    scientific coverage.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/curation_worklist.py --review-records --limit 0 --tsv /private/tmp/npmech-all-record-reviews-pU8b8GXS/review-queue.tsv
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/review-queue.log;
    SHA-256 ef1687cb23c1715d7c8e9b0000470e57e4a0b6c3d03fe675a61cab8d0adb9dce'
- check_id: second-ignored-inclusive-search
  name: second-ignored-inclusive-search
  status: passed
  required: true
  summary: Ignored-inclusive identifier/label/slug search; no inference from Git-aware
    search alone.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  command: rg --hidden --no-ignore -l -i 'MBPWQYMDPQWNIL|BGC0000657|naturalproductmech:mibig-0ed362dd75|2-methylisoborneol'
    . -g '!**/.git/**' -g '!**/.venv/**' -g '!**/__pycache__/**'
  exit_code: 0
  scope_note: 'Actual command log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-ignored-inclusive-search.log;
    SHA-256 eb6a048b66b78eac43b49027b687d431c104aa53330c1b63fe7a2a08766b015e'
- check_id: chemical-identity
  name: Name versus exact structure
  status: failed
  required: true
  summary: The named natural product and the stored molecular constitution disagree;
    see F1.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - chebi
- check_id: source-currentness
  name: Live source and identifier verification
  status: unavailable
  required: true
  summary: MIBiG BGC0000657, PubChem CID9237955 property lookup, and HQ830028.1 were
    inaccessible. Their current contents were not inferred from the seeded YAML.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - access-limits
- check_id: imodulondb
  name: Structured expression-module applicability
  status: not_applicable
  required: false
  summary: No iModulon, regulator, gene-level expression dataset or protein example
    is asserted in this target. Local MIBiG source rows were checked; expression modules
    cannot resolve the chemical identity conflict.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
- check_id: auxiliary-chemistry
  name: Auxiliary chemical serialization consistency
  status: passed
  required: false
  summary: Cached RDKit 2024.03.5 reproduces the stored InChI and InChIKey; this is
    not the project-pinned 2026.3.5 extractor and is not a native gate.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  exit_code: 0
  command: env PYTHONPATH=/Users/marcin/.cache/uv/archive-v0/L63k5B2U7AExer7XjnGMw/lib/python3.12/site-packages
    /Users/marcin/.local/share/uv/python/cpython-3.12.9-macos-x86_64-none/bin/python3.12
    /private/tmp/npmech-all-record-reviews-pU8b8GXS/chemistry_auxiliary.py
  evidence_ids:
  - chemistry
evidence:
- evidence_id: record
  kind: record_content
  reference: data/natural_products/alkaloids/2-methylisoborneol-2.yaml
  locator: Entire owner YAML, all fields and both curation events
  accessed_at: '2026-10-13T04:43:53.423401Z'
  support: supports
  summary: Exact minted record read in full. No inline graphs or component references.
    This evidence establishes what is asserted, not whether the science is correct.
  snapshot_sha256: 182ccce74f0fc70c82431c5c3820232a9dd066be625033d9ceaa47b302d83393
- evidence_id: source-rows
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0000657, compound_index=1; joined classification, taxonomy and filing
    rows
  accessed_at: '2026-10-13T04:43:53.432787Z'
  support: supports
  summary: 'Complete parsed source rows and applicable maintained correction tables
    were inspected. Chemistry and source grades reproduce the imported snapshot; no
    correction/override row targets this accession. Local extract: /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-local-source-rows.json'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: chemistry
  kind: validation
  reference: /private/tmp/npmech-all-record-reviews-pU8b8GXS/chemistry-auxiliary.json
  locator: data/natural_products/alkaloids/2-methylisoborneol-2.yaml
  accessed_at: '2026-10-13T04:43:53.432959Z'
  support: supports
  summary: Auxiliary RDKit 2024.03.5 calculated formula C15H16BrN3O4S, exact stored
    InChI/Key, and 0 undefined tetrahedral centers. Internal consistency does not
    authenticate the label.
  snapshot_sha256: ab9e4ee76552879f4b077c00fa2dd29ceda41421a982cad790650f84d1f38614
- evidence_id: chebi
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:61987
  locator: Name, definition, formula, SMILES, InChI and InChIKey
  accessed_at: '2026-10-13T04:43:53.432970Z'
  support: refutes
  summary: 2-Methylisoborneol is C11H20O, key LFYXNXGVLGKVCJ-FBIMIBRVSA-N for the
    specified stereoisomer. The stored C15H16BrN3O4S is a different constitution;
    neither unspecified stereochemistry nor protonation explains it.
- evidence_id: local-search
  kind: search
  reference: CultureBotAI/NaturalProductMech@e66f934111777c4ebfe69475d0520c0cfa074785
  locator: Full worktree file-content search plus structured source-table selectors
  accessed_at: '2026-10-13T04:43:53.432992Z'
  support: context_only
  summary: The same label has another structure owner. Only its locator/key was inspected
    for collision handling; the other owner is not counted as reviewed.
  search_scope: 'rg --hidden --no-ignore -l -i ''MBPWQYMDPQWNIL|BGC0000657|naturalproductmech:mibig-0ed362dd75|2-methylisoborneol''
    . -g ''!**/.git/**'' -g ''!**/.venv/**'' -g ''!**/__pycache__/**''. Hidden and
    ignored project content included; only .git internals, .venv dependencies and
    __pycache__ bytecode excluded. Source TSVs parsed in full for matching keys/accessions.
    Saved search log: /private/tmp/npmech-all-record-reviews-pU8b8GXS/second-ignored-inclusive-search.log'
- evidence_id: ownership
  kind: record_content
  reference: docs/CURATION.md
  locator: MIBiG structure corrections; locus-evidence overrides; generated versus
    curator ownership
  accessed_at: '2026-10-13T04:43:53.433170Z'
  support: supports
  summary: Fixes belong in implemented maintained inputs and tested source transforms,
    never generated pages or direct owner YAML edits. decisions.tsv is reserved, not
    consumed. The narrow structure-correction table rejects occupied destinations.
  snapshot_sha256: 3b979068592adbb0611de95927ca31eaabb5fb5d791aa09973e3b1e8d5a19011
- evidence_id: qc
  kind: validation
  reference: /private/tmp/npmech-all-record-reviews-pU8b8GXS/qc.log
  locator: Complete current-run log
  accessed_at: '2026-10-13T04:43:53.433295Z'
  support: supports
  summary: Native deterministic checks passed on the unchanged corpus. The scientific
    identity defect survives them.
  snapshot_sha256: 0c04323074ee7b0b9bf526e53dcd1c8f4208f74f2053e31a464070abb10df41e
- evidence_id: labels
  kind: validation
  reference: /private/tmp/npmech-all-record-reviews-pU8b8GXS/labels.log
  locator: Full configured ontology/label results and warning report
  accessed_at: '2026-10-13T04:43:53.433394Z'
  support: context_only
  summary: The minted identity is intentionally not ontology-resolved. Successful
    configured correspondence checks do not validate its compound name.
  snapshot_sha256: edd91274291ef54f0e30dcb5fa1049518e6f3ca75ea78ed845a14e51edffa0a6
- evidence_id: access-limits
  kind: search
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000657/
  locator: Direct official URL checks through web tool
  accessed_at: '2026-10-13T04:43:53.433404Z'
  support: unknown
  summary: Direct BGC0000657, PubChem CID9237955 property endpoint and NCBI HQ830028.1
    requests returned Internal Error; no source content was inferred.
  search_scope: One direct attempt per named resource on 2026-10-13. No retries or
    alternate copies. Inherited 162 scientific source stops and aliases were consulted
    before research; no stopped paper was reopened.
- evidence_id: pubmed
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/21490938/
  locator: Bibliographic identity and DOI link
  accessed_at: '2026-10-13T04:43:53.433408Z'
  support: supports
  summary: PMID21490938 resolves to Wang et al. 2011 and DOI10.1371/journal.pone.0018665.
- evidence_id: paper
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0018665
  locator: 'Results: isolation and GC-MS, light response; Discussion; Materials and
    Methods'
  accessed_at: '2026-10-13T04:43:53.433412Z'
  support: partial
  summary: The paper identifies ordinary 2-MIB in dqh15 against a standard, assigns
    HQ830028 to its operon, and measures light-dependent transcripts. It does not
    present paired product measurements for that expression series; direct gene-function
    experiments are explicitly absent.
  quote: although direct evidences from gene mutations or enzymatic experiments are
    still lacking.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact named chemical form
  outcome: concern
  summary: 'F1: the molecular constitution does not match the label or its cited biological
    context. Minting avoids a false ChEBI link but does not repair the name/structure
    conflict.'
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - chebi
  - source-rows
  - paper
- assessment_id: structure
  area: consistency
  topic: SMILES, InChI, key and stereochemical encoding
  outcome: supported
  summary: The stored serializations agree in the auxiliary calculation, with no undefined
    tetrahedral centers detected. No formula/charge/mass values are asserted in this
    YAML. Experimental identity remains refuted by F1.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - chemistry
- assessment_id: equivalence
  area: grounding
  topic: Cross-references, parents, congeners and same-name neighbors
  outcome: unknown
  summary: The sole xref pubchem:9237955 could not be resolved. The other same-name
    owner has an unspecified-stereo key; it is not automatically equivalent to ChEBI's
    stereospecific entry.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - local-search
  - chebi
- assessment_id: classification
  area: consistency
  topic: Computed filing versus asserted BGC class and origin
  outcome: supported
  summary: ALKALOIDS matches the pinned NPClassifier row for the stored input; the
    source BGC class remains a separate assertion. The filing mechanism is faithful,
    but NATURAL_PRODUCT membership is scientifically compromised by F1.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - source-rows
  - qc
- assessment_id: taxa
  area: grounding
  topic: Taxon identifiers, named strain and broad lineage facet
  outcome: supported
  summary: NCBITaxon:1002505 matches Pseudanabaena sp. dqh15 in the pinned taxonomy;
    CYANOBACTERIAL matches its lineage row. This checks taxon identity, not the claimed
    chemical product.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - source-rows
  - labels
- assessment_id: producer-cluster
  area: evidence
  topic: Producer versus locus claim, source version and grade
  outcome: concern
  summary: Version-5 BGC_CORRELATED/CLUSTER_CORRELATED faithfully reproduce the imported
    method. F2 questions whether the attached evidence supports expression-production
    correlation; it is not a claim that correlation implies native necessity.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - source-rows
  - record
  - paper
  - access-limits
  dimensions:
  - name: source_entry_version
    value: '5'
    definition: Version retained in the committed MIBiG compound row, not a claim
      about the current live database
    evidence_ids:
    - source-rows
- assessment_id: occurrence
  area: evidence
  topic: Occurrence versus biosynthesis and exact compound support
  outcome: not_applicable
  summary: No occurrence objects are asserted; no occurrence-to-producer promotion
    is introduced by this review.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
- assessment_id: mechanism-activity
  area: completeness
  topic: Pathway, all graphs, targets, activities and bioactivity summary
  outcome: not_applicable
  summary: The complete raw owner contains no pathway, inline graph, graph references,
    molecular target, bioactivity observation or activity-summary assertion. Optional
    empty slots are not findings; mechanism expansion must wait for exact identity.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
- assessment_id: other-claims
  area: completeness
  topic: Datasets, cross-corpus links, clinical status and discussions
  outcome: not_applicable
  summary: No dataset, related-record link, clinical-status claim or discussion is
    asserted. Genome metadata belongs to the BGC object and is assessed separately.
    No bibliography or clinical inference is manufactured.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
- assessment_id: history
  area: provenance
  topic: Generated ownership, status and audit trail
  outcome: supported
  summary: Both events are seed-from-sources events and native status remains SEEDED.
    Reproduction/strict/history coverage in QC establishes structural provenance,
    not literature review. This report changes neither history nor status.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  evidence_ids:
  - record
  - ownership
  - qc
findings:
- finding_id: F1
  issue_key: mibig-BGC0000657-compound-1-wrong-constitution
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The structure is not the natural product named by the record
  description: The stored MBPWQYMDPQWNIL-RYUDHWBXSA-N (C15H16BrN3O4S) is a chemically
    different constitution from the named compound. The committed MIBiG row already
    contains the mismatch. A generated record can be byte-reproducible while denoting
    the wrong molecule. Producer, BGC and natural-origin claims must not be transferred
    across the identity conflict.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  field_paths:
  - label
  - chemical_structure
  - biosynthesis_origin
  - producer_organisms
  - biosynthetic_gene_clusters
  - xrefs
  evidence_ids:
  - record
  - source-rows
  - chemistry
  - chebi
  - paper
  rule_id: review-checklist:Identity; docs/HARMONIZATION.md:The unit of the corpus
    is a structure
  native_severity: blocker
  normalization_reason: Wrong identity makes the record denote a different molecule,
    matching the shared blocker definition.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported source chemistry and cluster claims
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Structure-key harmonization and source grading
- finding_id: F2
  issue_key: mibig-BGC0000657-expression-production-evidence
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: The cited study does not establish the imported expression-production correlation
  description: The inspected methods/results measure transcripts under light treatments,
    not matched product abundance. Thus the cited experiment does not establish the
    imported correlation method. This concern remains provisional pending the complete
    live entry and any additional supporting evidence.
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  field_paths:
  - producer_organisms[0].evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  evidence_ids:
  - record
  - source-rows
  - paper
  rule_id: review-checklist:Producer organisms; Gene clusters
  native_severity: major
  normalization_reason: If confirmed, an unsupported evidence tier affects both producer
    and locus claims, independently of the wrong chemical identity.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented source-specific evidence correction with provenance checks
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported source chemistry and cluster claims
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Structure-key harmonization and source grading
actions:
- action_id: A1
  description: Resolve the upstream compound identity and audit every attached claim.
    Correct or withhold the bad maintained source assertion through an implemented,
    tested route; do not hand-edit generated YAML or use reserved decisions.tsv. Resolve
    the intended stereochemical form and PubChem xref independently before selecting
    a destination. Do not equate the existing unspecified-stereo owner with the stereospecific
    ChEBI entry by label alone.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported source chemistry and cluster claims
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Structure-key harmonization and source grading
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Potential guarded correction route only after structure identity is established
  generator: scripts/seed_from_sources.py via the documented guarded curation/migration
    workflow
  acceptance_checks:
  - Inspected primary/authority evidence establishes one exact compound form and every
    retained source claim matches it.
  - Regression tests cover this accession and reject name-only merging or transfer
    of old-key occurrences, assays, graphs or history.
  - Run the documented seed dry run and one-record canary before authorized guarded
    changes; then strict validation, verify-corpus, verify-reproduction, label checks
    and full QC pass.
  - Keep the wrong and intended structures distinct until an explicitly audited migration
    accounts for every affected owner and published slug.
- action_id: A2
  description: Check the complete locus evidence for matched production/transcript
    data. If unsupported, apply an appropriately pinned evidence-method correction
    through the implemented override path; preserve the distinction between production,
    predicted locus assignment, and direct function.
  finding_ids:
  - F2
  target_ids:
  - naturalproductmech:mibig-0ed362dd75
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented source-specific evidence correction with provenance checks
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported source chemistry and cluster claims
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: MIBiG source extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Structure-key harmonization and source grading
  depends_on:
  - A1
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Inspect any additional cited source before treating the imported method as supported.
  - Test the resulting producer and cluster grades separately; never upgrade homology
    to native characterization.
  - After any separately authorized correction, append proper curation provenance
    and pass strict validation, reproduction and full QC.
limitations:
- Required source-currentness checks are unavailable as detailed above; partial completion
  is deliberate and no scientific pass is claimed.
- The project-pinned RDKit 2026.3.5 was unavailable locally/offline. The explicitly
  versioned 2024.03.5 calculation is auxiliary only, not a replacement native gate.
- All 3115 records remain in the campaign. The other 3114 records are outside this
  single-record review; referenced same-name neighbors are not counted as scientifically
  reviewed.
- No paid providers, source retries, record corrections, status promotions, GitHub
  issues or other publication actions were performed. Findings/actions are proposed
  curation, not completed fixes.
notes:
- The original zero-review baseline and the population hashes are retained in /private/tmp/npmech-all-record-reviews-pU8b8GXS.
  Existing ad hoc or generated review-queue content is not structured scientific review.
- All native checks ran against base e66f934111777c4ebfe69475d0520c0cfa074785; external
  evidence was inspected on 2026-10-13.
tags:
- all-records-campaign
- identity-conflict
- source-owned
- partial-source-access
```
