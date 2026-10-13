# heme D1: identity and claim-level scientific review (mibig:BGC0000905)

- Review: 20261013T054205Z-heme-d1-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T05:22:02.577750Z
- Finished UTC: 2026-10-13T05:42:05.581388Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed blocker: the heme D1-labelled structure is iron-free. Full owner assessed, but current source, primary biosynthesis, xref and pinned chemistry checks remain incomplete. One blocker, no corpus edits.

## Scope And Provenance

One complete owner and every referenced graph component. Part of the full 3115-owner, 242-component campaign; this report is not a sampled corpus verdict.

Selection: Exact path and minted identifier from the saved ignored-inclusive campaign frontier, continuing in its selected order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e9a4cab937b614e80cf1a90d2bc98fabb80a5bc5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-9f05c51ff7 | data/natural_products/alkaloids/heme-d1-2.yaml | generated | heme D1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| inspect | passed | True | naturalproductmech:mibig-9f05c51ff7 | Canonical target/base/input capture succeeded before assessment. |
| strict | passed | True | naturalproductmech:mibig-9f05c51ff7 | Validating 1 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/src/naturalproductmech/schema/naturalproductmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/npmech-record-reviews-next-PKCU4Z/heme-d1-2-strict.tsv |
| corpus | passed | True | naturalproductmech:mibig-9f05c51ff7 | lockfile integrity OK: 3115 records, each filed where PATHS.tsv pins it<br>  lockfile rows: 3115, files on disk: 3115 |
| reproduction | passed | True | naturalproductmech:mibig-9f05c51ff7 | molecular targets whose assay organism did not resolve: 5 (1 distinct: Human…)<br>producer claims withheld — taxon names no single organism: 42 (NCBITaxon:77133 36, NCBITaxon:12908 3, NCBITaxon:1163772 2, NCBITaxon:155900 1)<br>taxon ids rewritten through taxon_merged.tsv: 161 (ChEBI 8, LOTUS 147, MIBiG 6)<br>corpus reproduction OK: 3115 records are byte-identical to what the seeder builds from data/raw/ |
| provenance | passed | True | naturalproductmech:mibig-9f05c51ff7 | provenance OK: 15 inventories, 0 upstream files, retrieved 2026-10-07 |
| labels | passed | True | naturalproductmech:mibig-9f05c51ff7 | id↔label correspondence summary:<br>          OK_CANONICAL: 13434<br>            OK_SYNONYM: 646<br>          OK_EXCEPTION: 35<br>              MISMATCH: 499<br>    SKIPPED_NO_ADAPTER: 4649<br><br>Wrote 499 flagged pairs to /private/tmp/npmech-record-reviews-next-PKCU4Z/labels.tsv |
| queue | passed | True | naturalproductmech:mibig-9f05c51ff7 | Native curation queue regenerated without changing corpus status: {"producer-evidence": 2289, "biosynthesis": 1194, "structure-disagreement": 5, "name-disagreement": 68, "unnamed-producer": 39, "shared-structure": 208, "needs-a-name": 18, "occurrence-only": 12, "pathway-ambiguous": 620, "unresolved-taxa": 3329, "stereo-incomplete": 1124, "record-review": 25}. This queue is not scientific review coverage. |
| full-qc-baseline | skipped | False | naturalproductmech:mibig-9f05c51ff7 | Full QC was not rerun for these read-only observations. Historical full QC at e66f934111777c4ebfe69475d0520c0cfa074785 passed 554 tests with 3 skips. All 3115 owners, 242 components and captured baseline source inputs were rehashed unchanged; fresh corpus, reproduction, provenance and per-owner strict checks are recorded separately. |
| pinned-chemistry | unavailable | True | naturalproductmech:mibig-9f05c51ff7 | The repository environment has no rdkit module. No new pinned RDKit 2026.3.5 SMILES/InChI/key calculation was performed. A successful older-toolkit auxiliary calculation is recorded separately, not substituted for the pinned native check. |
| current-sources | unavailable | True | naturalproductmech:mibig-9f05c51ff7 | Current MIBiG/PubChem and required primary-source checks could not be completed; per-source failures and retained access stops are recorded in evidence and limitations. |
| imodulondb | not_applicable | False | naturalproductmech:mibig-9f05c51ff7 | No transcriptomic dataset, expression module or regulator claim is asserted here. Protein identity is checked with cached structured UniProt/GenBank where present; absence of an iModulonDB check is not negative biological evidence. |
| aux-chemistry | passed | False | naturalproductmech:mibig-9f05c51ff7 | Older RDKit core operations parsed this SMILES and reproduced its exact Standard InChI and key. Missing NumPy import diagnostics were emitted; successful core operations alone are reported. Does not satisfy the unavailable pinned 2026.3.5 check. |

## Scientific And Domain Assessments

### Auxiliary chemical serialization check

consistency: supported. Targets: naturalproductmech:mibig-9f05c51ff7.

RDKit 2024.03.5 reproduces the saved InChI and InChIKey. Iron atom count is 0; tetrahedral centres: [[12, "R"], [19, "R"]]. This proves only limited internal serialization consistency, not correct biological identity or pinned-toolkit equivalence.

### Computed filing, asserted BGC class, biological origin and taxonomy axes

consistency: supported. Targets: naturalproductmech:mibig-9f05c51ff7.

Filing and model version match the exact-key NPClassifier row. The BGC class is retained separately. NATURAL_PRODUCT is imported biological-origin context, not a claim that a recombinant assay used a native production system. Producer taxon groups do not substitute for exact taxon/strain identifiers.

### Maintained correction ownership

ownership: supported. Targets: naturalproductmech:mibig-9f05c51ff7.

Seed-owned identity, taxonomy and source assertions must be fixed upstream or through an implemented tested correction path; generated owner/page patches would not be durable. Curated pathway/component changes require guarded writers and history. No changes were made.

### Native status and complete audit trail

provenance: supported. Targets: naturalproductmech:mibig-9f05c51ff7.

Status remains SEEDED. Existing history describes seeding. This review neither appends history nor promotes scientific status. Validation and reproduction do not establish biological truth.

### Optional activity, targets, clinical, datasets and cross-corpus claims

completeness: not_applicable. Targets: naturalproductmech:mibig-9f05c51ff7.

Full owner/resolved view has no assertions in: bioactivities, bioactivity_summary, molecular_targets, related_records, clinical_status, datasets. Their absence is not a required-field defect; no extract-level result, assay spectrum, clinical status or sibling identity is inferred.

### Chemical entity, label and metal state

identity: concern. Targets: naturalproductmech:mibig-9f05c51ff7.

The SMILES has no Fe atom and the InChI formula layer is C34H32N4O10 with /p-2. It cannot denote the iron chelate named heme D1. This is a constitutional conflict, independent of toolkit recalculation. The exact intended corrected structure is not resolved.

### SMILES/InChI/InChIKey and stereochemical resolution

representation: unknown. Targets: naturalproductmech:mibig-9f05c51ff7.

Two ring stereocentres and alkene geometry are encoded, consistent with the source stereo_complete flag, but they do not repair the absent metal. No independent pinned-toolkit recomputation was available.

### Minted identity, PubChem xrefs and similarly named owners

grounding: unknown. Targets: naturalproductmech:mibig-9f05c51ff7.

No exact key exists in the committed eligible ChEBI inventory. PubChem 6438545 and 53356663 equivalence could not be checked. The other heme d1 owner shares CID6438545 but differs in metal and stereochemical encoding; this is a reason to audit the xref, not permission to merge or a verified PubChem contradiction.

### Exact producer, genome accession and BGC link evidence

evidence: unknown. Targets: naturalproductmech:mibig-9f05c51ff7.

BGC0000905 preserves the committed version, taxon and genome EU052681.1. Empty locus method/coordinates are reported without upgrading SOURCE_ASSERTION or CLUSTER_UNSTATED. Entry-level PMID:17906152 is marked DATABASE_ASSERTION, not a newly read experiment. Current entry status, genome record and direct biosynthetic support remain unverified.

### Producer taxon and name

nomenclature: supported. Targets: naturalproductmech:mibig-9f05c51ff7.

NCBITaxon:28064 uses the source name Heliobacillus mobilis; the pinned taxonomy lists Heliobacterium mobile and explicitly retains Heliobacillus mobilis as a synonym. This is not a wrong-taxon finding.

### Occurrences, pathway, graphs and discussions

completeness: not_applicable. Targets: naturalproductmech:mibig-9f05c51ff7.

Complete owner and resolved view contain no occurrences, biosynthetic steps, causal graphs or graph references. No missing graph is inferred: a complete mechanism is a curation goal, not a review prerequisite. The iron-free identity concern is separately recorded where applicable.

## Findings

### F1: Heme D1 label is attached to an iron-free tetrapyrrole

blocker / open / confirmed; issue key: bgc0000905-heme-d1-missing-iron.

Both maintained MIBiG inventory and generated owner omit Fe entirely: SMILES contains only C/N/O/H and the Standard InChI formula has no Fe component. A heme is an iron chelate. This is not merely a metal-coordinate bond representation difference, and validation/reproduction do not detect the semantic conflict. The observation does not establish the correct PubChem CID, exact ferroheme form, replacement label or producer evidence.

## Recommended Actions And Acceptance Checks

### resolve-heme-identity

Resolve the intended biological product and exact metal/stereo/protonation state from inspectable primary or authoritative compound evidence. Correct the maintained source transformation, or use the narrow ChEBI correction only after proving eligibility and an unoccupied target. Do not just insert Fe into SMILES, rename the generated owner, or merge with BGC0000906 by shared label/CID.

- Exact compound evidence supports label, iron state, stereochemistry, protonation and every retained xref.
- Pinned RDKit chemistry is mutually consistent; correction row digests and occupied-destination checks pass.
- Re-audit producer/BGC claims rather than transferring them by name. Canary and guarded migration if needed; verify-reproduction, verify-corpus, strict validation, provenance, generated-page and QC gates pass.

### complete-source-review

Complete this exact owner review when authorized inspectable source material is available; preserve access stops and do not substitute search snippets or the similarly named sibling.

- Inspect the cited PMID and the exact versioned MIBiG/genome assertions.
- Verify each PubChem xref at metal, stereochemical and protonation resolution.
- Run the pinned chemical consistency calculation and save a successor review with finding lineage where relevant.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| aux-chemistry | RDKit 2024.03.5 core molecule/InChI API | partial | Auxiliary reparse of this exact owner SMILES with MolFromSmiles, MolToInchi, InchiToInchiKey, iron atom count and FindMolChiralCenters(includeUnassigned=True): {"identifier": "naturalproductmech:mibig-9f05c51ff7", "iron_atoms": 0, "calculated_inchi": "InChI=1S/C34H32N4O10/c1-15-17(5-7-27(39)40)21-10-22-18(6-8-28(41)42)16(2)20(36-22)11-25-33(3,13-29(43)44)32(48)24(38-25)12-26-34(4,14-30(45)46)31(47)23(37-26)9-19(15)35-21/h6,8-12H,5,7,13-14H2,1-4H3,(H6,35,36,37,38,39,40,41,42,43,44,45,46,47,48)/p-2/b8-6+/t33-,34-/m1/s1", "calculated_key": "RNPKTIINQWKWOQ-YWYZNWELSA-L", "inchi_matches": true, "key_matches": true, "chiral_centers": [[12, "R"], [19, "R"]]}. Auxiliary RDKit 2024.03.5 only, not the pinned 2026.3.5 native chemistry environment. Import emits missing-NumPy diagnostics; only successful core molecule/InChI operations are reported. |
| owner | data/natural_products/alkaloids/heme-d1-2.yaml | supports | Complete YAML owner read, including source concepts, all evidence objects, optional fields and full curation history; SHA-256 4baf05f6ad90f876641397ecc16421800288608d19eff1c1d383346910c9e48e. 0 referenced graph components also read in full. |
| inventory | data/raw/mibig_compounds.tsv | partial | Exact compound rows inspected from the committed inventory: [{"mibig_accession": "BGC0000905", "entry_version": "5", "entry_status": "active", "entry_quality": "questionable", "entry_completeness": "unknown", "compound_name": "heme D1", "compound_index": "1", "smiles": "CC1=C(C2=CC3=C(C(=C([N-]3)C=C4[C@@](C(=O)C(=N4)C=C5[C@@](C(=O)C(=N5)C=C1[N-]2)(C)CC(=O)O)(C)CC(=O)O)C)/C=C/C(=O)O)CCC(=O)O", "standard_inchi": "InChI=1S/C34H32N4O10/c1-15-17(5-7-27(39)40)21-10-22-18(6-8-28(41)42)16(2)20(36-22)11-25-33(3,13-29(43)44)32(48)24(38-25)12-26-34(4,14-30(45)46)31(47)23(37-26)9-19(15)35-21/h6,8-12H,5,7,13-14H2,1-4H3,(H6,35,36,37,38,39,40,41,42,43,44,45,46,47,48)/p-2/b8-6+/t33-,34-/m1/s1", "standard_inchi_key": "RNPKTIINQWKWOQ-YWYZNWELSA-L", "stereo_complete": "true", "compound_classes": "", "database_ids": "pubchem:6438545&#124;pubchem:53356663", "taxon_id": "NCBITaxon:28064", "taxon_label": "Heliobacillus mobilis", "bgc_classes": "other", "bgc_subclasses": "other", "genome_accession": "EU052681.1", "locus_from": "", "locus_to": "", "locus_evidence_methods": "", "producer_evidence_basis": "SOURCE_ASSERTION", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "primary_reference": "PMID:17906152", "reference_basis": "ENTRY"}]. This proves the seeded database assertion, not current live status or primary experimental support. |
| taxonomy | data/raw/corpus_taxa.obo | partial | Parsed exact taxon terms and synonyms with pronto 2.7.3; compared taxonomy-group rows: [{"taxon_id": "NCBITaxon:28064", "record_labels": ["Heliobacillus mobilis"], "cached_name": "Heliobacterium mobile", "cached_synonyms": ["Heliobacillus mobilis"], "groups": ["OTHER_BACTERIAL"]}]. Pinned snapshot, not a fresh NCBI taxonomy release. |
| classification | data/raw/npclassifier.tsv | supports | Exact-key row: [{"standard_inchi_key": "RNPKTIINQWKWOQ-YWYZNWELSA-L", "smiles": "CC1=C(C2=CC3=C(C(=C([N-]3)C=C4[C@@](C(=O)C(=N4)C=C5[C@@](C(=O)C(=N5)C=C1[N-]2)(C)CC(=O)O)(C)CC(=O)O)C)/C=C/C(=O)O)CCC(=O)O", "pathway_results": "Alkaloids", "superclass_results": "", "class_results": "", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07"}]. Computed filing provenance only; BGC class and origin are separate source assertions. |
| chebi-local | data/raw/chebi_structures.tsv | partial | Whole committed inventory exact-key search: []; connectivity-only candidates: []. No exact default-structure match in this inventory. A connectivity match is not exact stereochemical/protonation identity. |
| ownership | docs/CURATION.md | supports | Read maintained-input boundaries. REPLACE_WITH_CHEBI is a narrow pinned-row structure correction, rejects occupied destinations and does not merge records. Locus overrides alter method grading, not chemistry or organism identity. The reserved decisions.tsv has no consumer. Applicable rows in both implemented correction tables: {"mibig_structure_corrections": [], "mibig_locus_evidence_overrides": []}. |
| historical-qc | reviews/evidence/20261013-first-two-records/artifacts/qc.log.txt | context_only | Historical baseline only: complete QC succeeded before the prior reports were published. The current capture and subsequent local-source audit revalidated every campaign owner/component hash and captured baseline input. No new full-QC run is claimed. |
| heme-authority | https://www.ebi.ac.uk/chebi/CHEBI:30413; Definition and outgoing ontology relations | refutes | ChEBI defines heme by an iron-chelating tetrapyrrole and places it under iron coordination entities. This is class-level identity evidence only, not an exact replacement structure or organism claim. |
| ferroheme-d1-authority | https://www.ebi.ac.uk/chebi/CHEBI:60549; Definition, formula, SMILES, InChI, InChIKey and conjugate-acid/base relation | partial | Inspected ferroheme d1(4-) entry: C34H26FeN4O10, charge -4, InChIKey YTCKFKAUGWIMPJ-FSQDTXDGSA-H; explicit stereochemistry and conjugate-base relation to CHEBI:61147. It is not an exact xref for either reviewed owner. Timestamp records reinspection of the retained web result, not a second retrieval. |
| access-limits | https://pubmed.ncbi.nlm.nih.gov/17906152/ | unknown | Search returned bibliographic leads, but direct source opening returned a browser/reCAPTCHA challenge on 2026-10-13. No primary source text was accepted. MIBiG BGC0000905 and PubChem PUG for CIDs 6438545/53356663 returned tool access errors. CHEBI:61147 also returned a tool access error; local pinned inventory and independently accessible CHEBI:60549 are distinguished. No stopped paper was retried or fetched through an alternate route. Timestamp records result reinspection. |

## Limits And Additional Notes

- Partial scientific assessment, not a scientific pass. Required source and exact-chemistry checks remain unavailable; no native status promotion.
- The full campaign remains 3115 owner records plus 242 referenced graph components. This report covers one owner, not the unassessed remainder.
- Cached inventories and sequence records establish only their pinned assertions. Live currentness and experimental support are not inferred from validation or database quality/review labels.
- Review-only scope: no corpus mutation, history event, generated page, GitHub issue, PR or publication was performed.
- PMID:17906152 browser challenge; exact MIBiG entry and cited PubChem structures unavailable. GenBank accession currentness was not independently verified. No conclusion about absence of experiments is drawn from access failure.
- Guidance conflict resolved in favor of CLAUDE.md and the active profile: the checklist mentions decisions.tsv, but that reserved file is not consumed. Do not use it as an effective correction path.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T054205Z-heme-d1-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'heme D1: identity and claim-level scientific review (mibig:BGC0000905)'
started_at: '2026-10-13T05:22:02.577750Z'
finished_at: '2026-10-13T05:42:05.581388Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant/thread previously curated this repository. No
    independent reviewer is claimed; owners and components were not changed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
scientific_review: true
verdict: needs_curation
summary: 'Confirmed blocker: the heme D1-labelled structure is iron-free. Full owner
  assessed, but current source, primary biosynthesis, xref and pinned chemistry checks
  remain incomplete. One blocker, no corpus edits.'
source:
  git_revision: e9a4cab937b614e80cf1a90d2bc98fabb80a5bc5
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
  - path: data/natural_products/alkaloids/heme-d1-2.yaml
    sha256: 4baf05f6ad90f876641397ecc16421800288608d19eff1c1d383346910c9e48e
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
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
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
  - path: justfile
    sha256: 4f9057e3e54656dd46f2ded4d3a8f0804acad348d2605d436405e1fcfb6af550
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
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: naturalproductmech:mibig-9f05c51ff7
  path: data/natural_products/alkaloids/heme-d1-2.yaml
  label: heme D1
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported compound, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Structure-organism-reference occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Source harmonization and generated owner emission
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented narrow structure correction input
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Implemented source-method correction input
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/heme-d1-2.yaml
    role: Curator-owned pathway, graph references, discussions and audit history
scope:
  description: One complete owner and every referenced graph component. Part of the
    full 3115-owner, 242-component campaign; this report is not a sampled corpus verdict.
  selection: Exact path and minted identifier from the saved ignored-inclusive campaign
    frontier, continuing in its selected order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-9f05c51ff7
checks:
- check_id: inspect
  name: inspect
  status: passed
  required: true
  summary: Canonical target/base/input capture succeeded before assessment.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/record_review.py inspect --targets /private/tmp/npmech-record-reviews-next-PKCU4Z/heme-d1-2-targets.json
    --input CLAUDE.md --input justfile --input docs/record-review-profile.md --input
    docs/record-reviews.md --input .claude/skills/review-yaml-record/SKILL.md --input
    .claude/skills/curate-yaml-record/references/review-checklist.md --input docs/CURATION.md
    --input docs/HARMONIZATION.md --input conf/record_review.yaml --input schema/record_review.yaml
    --input src/naturalproductmech/schema/naturalproductmech.yaml --input conf/producer_evidence.tsv
    --input conf/id_label_targets.yaml --input data/raw/MANIFEST.yaml --input data/raw/mibig_compounds.tsv
    --input data/raw/lotus_occurrences.tsv --input data/raw/chebi_structures.tsv --input
    data/raw/corpus_taxa.obo --input data/raw/taxon_groups.tsv --input data/raw/taxon_merged.tsv
    --input data/raw/npclassifier.tsv --input data/natural_products/PATHS.tsv --input
    curation/mibig_structure_corrections.tsv --input curation/mibig_locus_evidence_overrides.tsv
    --input scripts/extract_mibig.py --input scripts/extract_lotus.py --input scripts/seed_from_sources.py
    --input src/naturalproductmech/graph_components.py
  exit_code: 0
  scope_note: Run 2026-10-13T05:21:59.606288Z to 2026-10-13T05:22:02.568800Z; output
    SHA-256 c09f41d9476aa2059713233792e438a6b47ba3a36ce3a464d0c300b8594b1718
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: "Validating 1 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/src/naturalproductmech/schema/naturalproductmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/npmech-record-reviews-next-PKCU4Z/heme-d1-2-strict.tsv"
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python3
    scripts/validate_strict.py data/natural_products/alkaloids/heme-d1-2.yaml --out
    /private/tmp/npmech-record-reviews-next-PKCU4Z/heme-d1-2-strict.tsv
  exit_code: 0
  scope_note: Run 2026-10-13T05:22:02.579163Z to 2026-10-13T05:22:06.692986Z; output
    SHA-256 f8455d320cde8664df801dfc2c0911cbd5b4204b7833f09a7e93a071f01ba6aa
- check_id: corpus
  name: corpus
  status: passed
  required: true
  summary: "lockfile integrity OK: 3115 records, each filed where PATHS.tsv pins it\n\
    \  lockfile rows: 3115, files on disk: 3115"
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python
    scripts/verify_corpus.py --summary
  exit_code: 0
  scope_note: Actual fresh run from 2026-10-13T05:33:54.158149Z to 2026-10-13T05:35:23.137082Z;
    output SHA-256 f41149d35ddb3ab65a8fe2fdf8bfd6242ff6753e740c3482f9ed0f0bb7122b50.
    Results retained here, not dependent on the temporary log. Deterministic check,
    not scientific sign-off.
- check_id: reproduction
  name: reproduction
  status: passed
  required: true
  summary: 'molecular targets whose assay organism did not resolve: 5 (1 distinct:
    Human…)

    producer claims withheld — taxon names no single organism: 42 (NCBITaxon:77133
    36, NCBITaxon:12908 3, NCBITaxon:1163772 2, NCBITaxon:155900 1)

    taxon ids rewritten through taxon_merged.tsv: 161 (ChEBI 8, LOTUS 147, MIBiG 6)

    corpus reproduction OK: 3115 records are byte-identical to what the seeder builds
    from data/raw/'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python
    scripts/check_reproduction.py
  exit_code: 0
  scope_note: Actual fresh run from 2026-10-13T05:35:23.137928Z to 2026-10-13T05:37:53.396103Z;
    output SHA-256 d76e0bdd701f4e95ea43c705242db68502c2e347cf60baf2321fa70034472fcd.
    Results retained here, not dependent on the temporary log. Deterministic check,
    not scientific sign-off.
- check_id: provenance
  name: provenance
  status: passed
  required: true
  summary: 'provenance OK: 15 inventories, 0 upstream files, retrieved 2026-10-07'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python
    scripts/check_provenance.py
  exit_code: 0
  scope_note: Actual fresh run from 2026-10-13T05:37:53.397792Z to 2026-10-13T05:37:54.044163Z;
    output SHA-256 edfd9b0adb518e4962a19be934e3364eb2a3d8527de0159322af10d2ddf6a252.
    Results retained here, not dependent on the temporary log. Deterministic check,
    not scientific sign-off.
- check_id: labels
  name: labels
  status: passed
  required: true
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 13434\n    \
    \        OK_SYNONYM: 646\n          OK_EXCEPTION: 35\n              MISMATCH:\
    \ 499\n    SKIPPED_NO_ADAPTER: 4649\n\nWrote 499 flagged pairs to /private/tmp/npmech-record-reviews-next-PKCU4Z/labels.tsv"
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python
    scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report
    /private/tmp/npmech-record-reviews-next-PKCU4Z/labels.tsv
  exit_code: 0
  scope_note: Actual fresh run from 2026-10-13T05:37:54.045148Z to 2026-10-13T05:39:55.736120Z;
    output SHA-256 803d0d84664eb9a85ed2e3c0060b95139dbdfaf29150ccb78f95589b37bb531d.
    Results retained here, not dependent on the temporary log. Reporting mode is non-blocking;
    exit zero does not mean all labels match. Unsupported adapters remain skipped.
- check_id: queue
  name: queue
  status: passed
  required: true
  summary: 'Native curation queue regenerated without changing corpus status: {"producer-evidence":
    2289, "biosynthesis": 1194, "structure-disagreement": 5, "name-disagreement":
    68, "unnamed-producer": 39, "shared-structure": 208, "needs-a-name": 18, "occurrence-only":
    12, "pathway-ambiguous": 620, "unresolved-taxa": 3329, "stereo-incomplete": 1124,
    "record-review": 25}. This queue is not scientific review coverage.'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/bin/python
    scripts/curation_worklist.py --review-records --limit 0 --tsv /private/tmp/npmech-record-reviews-next-PKCU4Z/review-queue.tsv
  exit_code: 0
  scope_note: Actual fresh run from 2026-10-13T05:39:55.737055Z to 2026-10-13T05:40:47.760630Z;
    output SHA-256 854e4142b7742735c1b6f82dd04f6a0c8ecf61c68fe4527f59e509e88bbd175b.
    Results retained here, not dependent on the temporary log. Deterministic check,
    not scientific sign-off.
- check_id: full-qc-baseline
  name: full-qc-baseline
  status: skipped
  required: false
  summary: Full QC was not rerun for these read-only observations. Historical full
    QC at e66f934111777c4ebfe69475d0520c0cfa074785 passed 554 tests with 3 skips.
    All 3115 owners, 242 components and captured baseline source inputs were rehashed
    unchanged; fresh corpus, reproduction, provenance and per-owner strict checks
    are recorded separately.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - historical-qc
- check_id: pinned-chemistry
  name: pinned-chemistry
  status: unavailable
  required: true
  summary: The repository environment has no rdkit module. No new pinned RDKit 2026.3.5
    SMILES/InChI/key calculation was performed. A successful older-toolkit auxiliary
    calculation is recorded separately, not substituted for the pinned native check.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: .venv/bin/python -c 'import rdkit; print(rdkit.__version__)'
  scope_note: The displayed availability probe exited 1 with ModuleNotFoundError.
    The requested pinned chemical calculation itself was not executed.
- check_id: current-sources
  name: current-sources
  status: unavailable
  required: true
  summary: Current MIBiG/PubChem and required primary-source checks could not be completed;
    per-source failures and retained access stops are recorded in evidence and limitations.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - access-limits
- check_id: imodulondb
  name: imodulondb
  status: not_applicable
  required: false
  summary: No transcriptomic dataset, expression module or regulator claim is asserted
    here. Protein identity is checked with cached structured UniProt/GenBank where
    present; absence of an iModulonDB check is not negative biological evidence.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
- check_id: aux-chemistry
  name: aux-chemistry
  status: passed
  required: false
  summary: Older RDKit core operations parsed this SMILES and reproduced its exact
    Standard InChI and key. Missing NumPy import diagnostics were emitted; successful
    core operations alone are reported. Does not satisfy the unavailable pinned 2026.3.5
    check.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  command: env PYENV_VERSION=3.12.11 PYTHONPATH=/Users/marcin/.cache/uv/archive-v0/emAjwJ0D1JTZTu-QXHtug
    python3.12 /private/tmp/npmech-record-reviews-next-PKCU4Z/aux_chemistry.py
  exit_code: 0
  evidence_ids:
  - aux-chemistry
evidence:
- evidence_id: aux-chemistry
  kind: validation
  reference: RDKit 2024.03.5 core molecule/InChI API
  accessed_at: '2026-10-13T05:41:06.911891Z'
  support: partial
  summary: 'Auxiliary reparse of this exact owner SMILES with MolFromSmiles, MolToInchi,
    InchiToInchiKey, iron atom count and FindMolChiralCenters(includeUnassigned=True):
    {"identifier": "naturalproductmech:mibig-9f05c51ff7", "iron_atoms": 0, "calculated_inchi":
    "InChI=1S/C34H32N4O10/c1-15-17(5-7-27(39)40)21-10-22-18(6-8-28(41)42)16(2)20(36-22)11-25-33(3,13-29(43)44)32(48)24(38-25)12-26-34(4,14-30(45)46)31(47)23(37-26)9-19(15)35-21/h6,8-12H,5,7,13-14H2,1-4H3,(H6,35,36,37,38,39,40,41,42,43,44,45,46,47,48)/p-2/b8-6+/t33-,34-/m1/s1",
    "calculated_key": "RNPKTIINQWKWOQ-YWYZNWELSA-L", "inchi_matches": true, "key_matches":
    true, "chiral_centers": [[12, "R"], [19, "R"]]}. Auxiliary RDKit 2024.03.5 only,
    not the pinned 2026.3.5 native chemistry environment. Import emits missing-NumPy
    diagnostics; only successful core molecule/InChI operations are reported.'
- evidence_id: owner
  kind: record_content
  reference: data/natural_products/alkaloids/heme-d1-2.yaml
  accessed_at: '2026-10-13T05:22:02.577750Z'
  support: supports
  summary: Complete YAML owner read, including source concepts, all evidence objects,
    optional fields and full curation history; SHA-256 4baf05f6ad90f876641397ecc16421800288608d19eff1c1d383346910c9e48e.
    0 referenced graph components also read in full.
  snapshot_sha256: 4baf05f6ad90f876641397ecc16421800288608d19eff1c1d383346910c9e48e
- evidence_id: inventory
  kind: database
  reference: data/raw/mibig_compounds.tsv
  accessed_at: '2026-10-13T05:32:54.791756Z'
  support: partial
  summary: 'Exact compound rows inspected from the committed inventory: [{"mibig_accession":
    "BGC0000905", "entry_version": "5", "entry_status": "active", "entry_quality":
    "questionable", "entry_completeness": "unknown", "compound_name": "heme D1", "compound_index":
    "1", "smiles": "CC1=C(C2=CC3=C(C(=C([N-]3)C=C4[C@@](C(=O)C(=N4)C=C5[C@@](C(=O)C(=N5)C=C1[N-]2)(C)CC(=O)O)(C)CC(=O)O)C)/C=C/C(=O)O)CCC(=O)O",
    "standard_inchi": "InChI=1S/C34H32N4O10/c1-15-17(5-7-27(39)40)21-10-22-18(6-8-28(41)42)16(2)20(36-22)11-25-33(3,13-29(43)44)32(48)24(38-25)12-26-34(4,14-30(45)46)31(47)23(37-26)9-19(15)35-21/h6,8-12H,5,7,13-14H2,1-4H3,(H6,35,36,37,38,39,40,41,42,43,44,45,46,47,48)/p-2/b8-6+/t33-,34-/m1/s1",
    "standard_inchi_key": "RNPKTIINQWKWOQ-YWYZNWELSA-L", "stereo_complete": "true",
    "compound_classes": "", "database_ids": "pubchem:6438545|pubchem:53356663", "taxon_id":
    "NCBITaxon:28064", "taxon_label": "Heliobacillus mobilis", "bgc_classes": "other",
    "bgc_subclasses": "other", "genome_accession": "EU052681.1", "locus_from": "",
    "locus_to": "", "locus_evidence_methods": "", "producer_evidence_basis": "SOURCE_ASSERTION",
    "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "primary_reference": "PMID:17906152",
    "reference_basis": "ENTRY"}]. This proves the seeded database assertion, not current
    live status or primary experimental support.'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: taxonomy
  kind: authority
  reference: data/raw/corpus_taxa.obo
  accessed_at: '2026-10-13T05:32:54.791756Z'
  support: partial
  summary: 'Parsed exact taxon terms and synonyms with pronto 2.7.3; compared taxonomy-group
    rows: [{"taxon_id": "NCBITaxon:28064", "record_labels": ["Heliobacillus mobilis"],
    "cached_name": "Heliobacterium mobile", "cached_synonyms": ["Heliobacillus mobilis"],
    "groups": ["OTHER_BACTERIAL"]}]. Pinned snapshot, not a fresh NCBI taxonomy release.'
  snapshot_sha256: 8a3e9c4840389ddc294df6e92cb6a9711f4381a57c5644bbcf54f8219b764cf9
- evidence_id: classification
  kind: database
  reference: data/raw/npclassifier.tsv
  accessed_at: '2026-10-13T05:32:54.791756Z'
  support: supports
  summary: 'Exact-key row: [{"standard_inchi_key": "RNPKTIINQWKWOQ-YWYZNWELSA-L",
    "smiles": "CC1=C(C2=CC3=C(C(=C([N-]3)C=C4[C@@](C(=O)C(=N4)C=C5[C@@](C(=O)C(=N5)C=C1[N-]2)(C)CC(=O)O)(C)CC(=O)O)C)/C=C/C(=O)O)CCC(=O)O",
    "pathway_results": "Alkaloids", "superclass_results": "", "class_results": "",
    "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07"}].
    Computed filing provenance only; BGC class and origin are separate source assertions.'
  snapshot_sha256: 7b9b9f78f5b14aea9fabb163bbaa9e842920a7e9b07deac8f98c97666e9e23fc
- evidence_id: chebi-local
  kind: authority
  reference: data/raw/chebi_structures.tsv
  accessed_at: '2026-10-13T05:32:54.791756Z'
  support: partial
  summary: 'Whole committed inventory exact-key search: []; connectivity-only candidates:
    []. No exact default-structure match in this inventory. A connectivity match is
    not exact stereochemical/protonation identity.'
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
  search_scope: All rows parsed with csv.DictReader, independent of ignore rules;
    exact and first-block InChIKey comparisons bounded to this committed ChEBI inventory,
    not all current ChEBI.
- evidence_id: ownership
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-13T05:42:04.549762Z'
  support: supports
  summary: 'Read maintained-input boundaries. REPLACE_WITH_CHEBI is a narrow pinned-row
    structure correction, rejects occupied destinations and does not merge records.
    Locus overrides alter method grading, not chemistry or organism identity. The
    reserved decisions.tsv has no consumer. Applicable rows in both implemented correction
    tables: {"mibig_structure_corrections": [], "mibig_locus_evidence_overrides":
    []}.'
  snapshot_sha256: 3b979068592adbb0611de95927ca31eaabb5fb5d791aa09973e3b1e8d5a19011
  search_scope: All rows in both implemented curation tables parsed with csv, including
    ignored files; bounded absence of applicable corrections, not absence of evidence
    elsewhere.
- evidence_id: historical-qc
  kind: validation
  reference: reviews/evidence/20261013-first-two-records/artifacts/qc.log.txt
  accessed_at: '2026-10-13T05:42:04.549994Z'
  support: context_only
  summary: 'Historical baseline only: complete QC succeeded before the prior reports
    were published. The current capture and subsequent local-source audit revalidated
    every campaign owner/component hash and captured baseline input. No new full-QC
    run is claimed.'
  snapshot_sha256: 0c04323074ee7b0b9bf526e53dcd1c8f4208f74f2053e31a464070abb10df41e
- evidence_id: heme-authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:30413
  accessed_at: '2026-10-13T05:29:08Z'
  support: refutes
  summary: ChEBI defines heme by an iron-chelating tetrapyrrole and places it under
    iron coordination entities. This is class-level identity evidence only, not an
    exact replacement structure or organism claim.
  locator: Definition and outgoing ontology relations
- evidence_id: ferroheme-d1-authority
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:60549
  accessed_at: '2026-10-13T05:40:23Z'
  support: partial
  summary: 'Inspected ferroheme d1(4-) entry: C34H26FeN4O10, charge -4, InChIKey YTCKFKAUGWIMPJ-FSQDTXDGSA-H;
    explicit stereochemistry and conjugate-base relation to CHEBI:61147. It is not
    an exact xref for either reviewed owner. Timestamp records reinspection of the
    retained web result, not a second retrieval.'
  locator: Definition, formula, SMILES, InChI, InChIKey and conjugate-acid/base relation
- evidence_id: access-limits
  kind: search
  reference: https://pubmed.ncbi.nlm.nih.gov/17906152/
  accessed_at: '2026-10-13T05:40:23Z'
  support: unknown
  summary: Search returned bibliographic leads, but direct source opening returned
    a browser/reCAPTCHA challenge on 2026-10-13. No primary source text was accepted.
    MIBiG BGC0000905 and PubChem PUG for CIDs 6438545/53356663 returned tool access
    errors. CHEBI:61147 also returned a tool access error; local pinned inventory
    and independently accessible CHEBI:60549 are distinguished. No stopped paper was
    retried or fetched through an alternate route. Timestamp records result reinspection.
  search_scope: Exact PMID search and one PubMed open; exact MIBiG entry open; one
    PubChem property request for the two cited CIDs; exact ChEBI entries. Search snippets
    were leads, not proof of production or a negative claim about the paper.
assessments:
- assessment_id: serialization
  area: consistency
  topic: Auxiliary chemical serialization check
  outcome: supported
  summary: 'RDKit 2024.03.5 reproduces the saved InChI and InChIKey. Iron atom count
    is 0; tetrahedral centres: [[12, "R"], [19, "R"]]. This proves only limited internal
    serialization consistency, not correct biological identity or pinned-toolkit equivalence.'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - aux-chemistry
  - owner
- assessment_id: filing
  area: consistency
  topic: Computed filing, asserted BGC class, biological origin and taxonomy axes
  outcome: supported
  summary: Filing and model version match the exact-key NPClassifier row. The BGC
    class is retained separately. NATURAL_PRODUCT is imported biological-origin context,
    not a claim that a recombinant assay used a native production system. Producer
    taxon groups do not substitute for exact taxon/strain identifiers.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
  - classification
  - inventory
  - taxonomy
- assessment_id: generated-boundary
  area: ownership
  topic: Maintained correction ownership
  outcome: supported
  summary: Seed-owned identity, taxonomy and source assertions must be fixed upstream
    or through an implemented tested correction path; generated owner/page patches
    would not be durable. Curated pathway/component changes require guarded writers
    and history. No changes were made.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - ownership
- assessment_id: audit
  area: provenance
  topic: Native status and complete audit trail
  outcome: supported
  summary: Status remains SEEDED. Existing history describes seeding. This review
    neither appends history nor promotes scientific status. Validation and reproduction
    do not establish biological truth.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
  - historical-qc
- assessment_id: optional-claims
  area: completeness
  topic: Optional activity, targets, clinical, datasets and cross-corpus claims
  outcome: not_applicable
  summary: 'Full owner/resolved view has no assertions in: bioactivities, bioactivity_summary,
    molecular_targets, related_records, clinical_status, datasets. Their absence is
    not a required-field defect; no extract-level result, assay spectrum, clinical
    status or sibling identity is inferred.'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
- assessment_id: identity
  area: identity
  topic: Chemical entity, label and metal state
  outcome: concern
  summary: The SMILES has no Fe atom and the InChI formula layer is C34H32N4O10 with
    /p-2. It cannot denote the iron chelate named heme D1. This is a constitutional
    conflict, independent of toolkit recalculation. The exact intended corrected structure
    is not resolved.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
  - inventory
  - heme-authority
  - ferroheme-d1-authority
  - chebi-local
- assessment_id: stereo
  area: representation
  topic: SMILES/InChI/InChIKey and stereochemical resolution
  outcome: unknown
  summary: Two ring stereocentres and alkene geometry are encoded, consistent with
    the source stereo_complete flag, but they do not repair the absent metal. No independent
    pinned-toolkit recomputation was available.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
  - chebi-local
- assessment_id: equivalence
  area: grounding
  topic: Minted identity, PubChem xrefs and similarly named owners
  outcome: unknown
  summary: No exact key exists in the committed eligible ChEBI inventory. PubChem
    6438545 and 53356663 equivalence could not be checked. The other heme d1 owner
    shares CID6438545 but differs in metal and stereochemical encoding; this is a
    reason to audit the xref, not permission to merge or a verified PubChem contradiction.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
  - chebi-local
  - access-limits
- assessment_id: producer-bgc
  area: evidence
  topic: Exact producer, genome accession and BGC link evidence
  outcome: unknown
  summary: BGC0000905 preserves the committed version, taxon and genome EU052681.1.
    Empty locus method/coordinates are reported without upgrading SOURCE_ASSERTION
    or CLUSTER_UNSTATED. Entry-level PMID:17906152 is marked DATABASE_ASSERTION, not
    a newly read experiment. Current entry status, genome record and direct biosynthetic
    support remain unverified.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - inventory
  - owner
  - access-limits
- assessment_id: taxon
  area: nomenclature
  topic: Producer taxon and name
  outcome: supported
  summary: NCBITaxon:28064 uses the source name Heliobacillus mobilis; the pinned
    taxonomy lists Heliobacterium mobile and explicitly retains Heliobacillus mobilis
    as a synonym. This is not a wrong-taxon finding.
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - taxonomy
  - inventory
- assessment_id: absent-mechanism
  area: completeness
  topic: Occurrences, pathway, graphs and discussions
  outcome: not_applicable
  summary: 'Complete owner and resolved view contain no occurrences, biosynthetic
    steps, causal graphs or graph references. No missing graph is inferred: a complete
    mechanism is a curation goal, not a review prerequisite. The iron-free identity
    concern is separately recorded where applicable.'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  evidence_ids:
  - owner
findings:
- finding_id: F1
  issue_key: bgc0000905-heme-d1-missing-iron
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Heme D1 label is attached to an iron-free tetrapyrrole
  description: 'Both maintained MIBiG inventory and generated owner omit Fe entirely:
    SMILES contains only C/N/O/H and the Standard InChI formula has no Fe component.
    A heme is an iron chelate. This is not merely a metal-coordinate bond representation
    difference, and validation/reproduction do not detect the semantic conflict. The
    observation does not establish the correct PubChem CID, exact ferroheme form,
    replacement label or producer evidence.'
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  field_paths:
  - label
  - chemical_structure
  - source_concepts[0]
  evidence_ids:
  - owner
  - inventory
  - heme-authority
  - ferroheme-d1-authority
  rule_id: 'docs/HARMONIZATION.md: one individual structure; review-checklist: Identity/Structure'
  native_severity: blocker
  normalization_reason: Wrong constitution makes the record denote a different chemical
    entity from its label.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Raw BGC0000905 compound 1 assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Structure extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner and source-concept harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Only usable if an exact eligible, unoccupied ChEBI target is demonstrated
actions:
- action_id: resolve-heme-identity
  description: Resolve the intended biological product and exact metal/stereo/protonation
    state from inspectable primary or authoritative compound evidence. Correct the
    maintained source transformation, or use the narrow ChEBI correction only after
    proving eligibility and an unoccupied target. Do not just insert Fe into SMILES,
    rename the generated owner, or merge with BGC0000906 by shared label/CID.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Raw BGC0000905 compound 1 assertion
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Structure extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner and source-concept harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Only usable if an exact eligible, unoccupied ChEBI target is demonstrated
  acceptance_checks:
  - Exact compound evidence supports label, iron state, stereochemistry, protonation
    and every retained xref.
  - Pinned RDKit chemistry is mutually consistent; correction row digests and occupied-destination
    checks pass.
  - Re-audit producer/BGC claims rather than transferring them by name. Canary and
    guarded migration if needed; verify-reproduction, verify-corpus, strict validation,
    provenance, generated-page and QC gates pass.
  generator: scripts/seed_from_sources.py
- action_id: complete-source-review
  description: Complete this exact owner review when authorized inspectable source
    material is available; preserve access stops and do not substitute search snippets
    or the similarly named sibling.
  finding_ids: []
  target_ids:
  - naturalproductmech:mibig-9f05c51ff7
  ownership_note: Evidence collection only; any subsequent corpus curation requires
    separate authorization.
  acceptance_checks:
  - Inspect the cited PMID and the exact versioned MIBiG/genome assertions.
  - Verify each PubChem xref at metal, stereochemical and protonation resolution.
  - Run the pinned chemical consistency calculation and save a successor review with
    finding lineage where relevant.
limitations:
- Partial scientific assessment, not a scientific pass. Required source and exact-chemistry
  checks remain unavailable; no native status promotion.
- The full campaign remains 3115 owner records plus 242 referenced graph components.
  This report covers one owner, not the unassessed remainder.
- Cached inventories and sequence records establish only their pinned assertions.
  Live currentness and experimental support are not inferred from validation or database
  quality/review labels.
- 'Review-only scope: no corpus mutation, history event, generated page, GitHub issue,
  PR or publication was performed.'
- PMID:17906152 browser challenge; exact MIBiG entry and cited PubChem structures
  unavailable. GenBank accession currentness was not independently verified. No conclusion
  about absence of experiments is drawn from access failure.
notes:
- 'Guidance conflict resolved in favor of CLAUDE.md and the active profile: the checklist
  mentions decisions.tsv, but that reserved file is not consumed. Do not use it as
  an effective correction path.'
```
