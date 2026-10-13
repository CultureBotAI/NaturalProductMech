# Capsular product scientific review: Actinobacillus

- Review: 20261013T210902Z-capsular-polysaccharide
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T20:50:38Z
- Finished UTC: 2026-10-13T21:09:02.235470Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One identity blocker and one minor deposited-context finding; primary access gaps prevent full assessment.

## Scope And Provenance

One exact capsule owner and all attached components (none).

Selection: Next exact owner in the exhaustive 3115-owner campaign checkpoint; no cohort extrapolation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b87e2fa3e2acc7896755a7c4eaa09d48fe0159e8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-241ecc69e8 | data/natural_products/unclassified/capsular-polysaccharide.yaml | generated | capsular polysaccharide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict | passed | True | naturalproductmech:mibig-241ecc69e8 | Actual execution 2026-10-13T20:52:51.224787Z through 2026-10-13T20:52:54.565972Z; exit 0. This deterministic check is not scientific certification. |
| labels | passed | True | naturalproductmech:mibig-241ecc69e8 | Actual execution 2026-10-13T20:53:32.890779Z through 2026-10-13T20:55:10.121917Z; exit 0. Label check retains 499 warnings and 4649 adapter skips; not all identifier classes remotely resolved. |
| corpus | passed | True | naturalproductmech:mibig-241ecc69e8 | Actual execution 2026-10-13T20:57:14.235892Z through 2026-10-13T20:58:21.232339Z; exit 0. This deterministic check is not scientific certification. |
| chemistry-pinned | passed | True | naturalproductmech:mibig-241ecc69e8 | Actual execution 2026-10-13T20:56:30.571312Z through 2026-10-13T20:56:32.114784Z; exit 0. This deterministic check is not scientific certification. |
| local-search | passed | True | naturalproductmech:mibig-241ecc69e8 | Actual execution 2026-10-13T20:56:31.792599Z through 2026-10-13T20:56:31.865683Z; exit 0. This deterministic check is not scientific certification. |
| Exact-product primary evidence and LOTUS origin trace | unavailable | True | naturalproductmech:mibig-241ecc69e8 | The cited primary full text and applicable Wikidata origin endpoints encountered HTTP403/access challenges. Abstracts and database payloads do not resolve exact-product identity; no bypass attempted. |
| Structured expression dataset applicability search | passed | False | naturalproductmech:mibig-241ecc69e8 | Installed sibling kg-microbe-sources imodulondb datasets ran successfully; no covered target organism dataset. Not negative biological evidence. Earlier missing runner/dependency attempts failed and were superseded. |
| Exact-base historical native QC | passed | True | naturalproductmech:mibig-241ecc69e8 | Historical merge-group run 38464138422 on b87e2fa3 passed native QC and reproduction (786 passed, 4 skipped). All current domain input hashes matched that base at capture; not a fresh full QC run for these review bundles. |

## Scientific And Domain Assessments

### Exact product versus capsule/serotype concept

identity: concern. Targets: naturalproductmech:mibig-241ecc69e8.

Three serotype 12/6/7 loci share one finite type-7-labelled graph. Its n-propoxy substituent, geminal ring diol and phosphate monoester require adjudication against capsule chemistry. The accessible 2024 study describes a glycosylglycerol-phosphate polymer backbone, not this finite graph, and its AP76 enzyme context is not the imported isolate 72-14676. A. lignieresii occurrence support remains unknown because the cited full paper is inaccessible; absence from its abstract is not refutation. Registry names/MeSH associations are name-based and are not independent chemical certification. Exact PubChem graph agreement is verified; deleting its xref alone would not repair the biological assignment. The confirmed defect is unsupported exact-product assignment across the recorded contexts, not an experimentally established replacement structure.

### Internal chemical encoding and exact registry xref

representation: supported. Targets: naturalproductmech:mibig-241ecc69e8.

RDKit 2026.03.5 reproduces stored Standard InChI and key and matches PubChem. Formula C15H29O16P; 9 assigned and 0 undefined centers; stereo_complete flag is computationally consistent. Finite graph, not a variable-degree polymer; this does not validate its biological assignment. Keep the exact PubChem xref; it is not a mismatching-key case.

n-propoxy-on-ring, geminal-ring-diol and phosphate-monoester SMARTS matches are persisted with atom indices. Their biological assignment remains unresolved; no replacement graph inferred.

### Minted identity and exact joins

grounding: supported. Targets: naturalproductmech:mibig-241ecc69e8.

MINTED rationale agrees with pinned exact-key inventory joins. Broader capsule ontology terms cannot serve as exact structure replacements.

### Computed filing, asserted class, taxonomy and origin facets

consistency: supported. Targets: naturalproductmech:mibig-241ecc69e8.

Filing UNCLASSIFIED follows the pinned NPClassifier output; SACCHARIDE remains an asserted BGC class. NATURAL_PRODUCT is source-asserted, not predicted. OTHER_BACTERIAL taxonomy is separate from natural/engineered origin. This is metadata consistency, not validation of the disputed graph assignment.

### Producer and locus evidence scope

provenance: concern. Targets: naturalproductmech:mibig-241ecc69e8.

3 deposited strain/isolate qualifiers are missing from explicit producer context. SOURCE_ASSERTION and CLUSTER_UNSTATED correctly reflect empty MIBiG method lists; no characterization upgrade justified.

### Occurrence versus production and publication independence

evidence: unknown. Targets: naturalproductmech:mibig-241ecc69e8.

LOTUS occurrences remain DATABASE_ASSERTION, never promoted to production. Their DOI is the same publication as the PMID on the MIBiG entries, not independent evidence. Exact structure and Wikidata provenance remain unresolved. A. lignieresii support is unknown, not disproved by absence from the abstract.

### Graphs, pathway, activities, targets, clinical status and sibling links

completeness: not_applicable. Targets: naturalproductmech:mibig-241ecc69e8.

Full owner has no graph components, curated mechanism, assay, molecular target, clinical status or related sibling link. These optional absences are not fabricated defects; clinical/genotype studies are not pure-compound bioactivity assays.

### Generated boundaries and scientific status

ownership: supported. Targets: naturalproductmech:mibig-241ecc69e8.

SEEDED remains appropriate. Existing shared-structure discussion is OPEN; no REVIEWED promotion. Generated changes belong in implemented curation tables or source transforms, not reserved unconsumed decisions.tsv.

## Findings

### F1: Exact capsule-product assignment is unsupported across deposited serotypes

blocker / open / confirmed; issue key: capsular-polysaccharide-exact-product-assignment.

Three serotype 12/6/7 loci share one finite type-7-labelled graph. Its n-propoxy substituent, geminal ring diol and phosphate monoester require adjudication against capsule chemistry. The accessible 2024 study describes a glycosylglycerol-phosphate polymer backbone, not this finite graph, and its AP76 enzyme context is not the imported isolate 72-14676. A. lignieresii occurrence support remains unknown because the cited full paper is inaccessible; absence from its abstract is not refutation. Registry names/MeSH associations are name-based and are not independent chemical certification. Exact PubChem graph agreement is verified; deleting its xref alone would not repair the biological assignment. The confirmed defect is unsupported exact-product assignment across the recorded contexts, not an experimentally established replacement structure.

### F2: Deposited strain and serotype qualifications are missing

minor / open / confirmed; issue key: capsular-polysaccharide-deposited-strain-context.

3 source qualifiers are available but not explicitly carried into producer strain/evidence context. Femo is already in the taxon label; isolate 72-14676 must not become WF83 or AP76.

## Recommended Actions And Acceptance Checks

### A1

Preserve an OPEN identity qualification, then adjudicate exact locus-to-product and occurrence assignments from accessible primary chemistry before migration; do not rename all entries to the registry serotype.

- Per-source structure and polymer/form boundary justified by inspected primary chemistry.
- Use a supported maintained migration/exclusion path, preserve provenance, and pass strict validation, reproduction and full QC.

### A2

Add complete-row-pinned strain qualifications with versioned GenBank references and serotype rationale; no taxon or evidence-grade changes.

- All deposited qualifiers match source; isolate remains labelled as isolate.
- Canary, scoped reseeding, invariant regression tests and byte-identical reproduction pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-owner | data/natural_products/unclassified/capsular-polysaccharide.yaml; b87e2fa3e2acc7896755a7c4eaa09d48fe0159e8 | supports | Entire owner read, with all source concepts, producer/cluster/occurrence claims, history and discussions; no attached graph components. |
| E-mibig | https://mibig.secondarymetabolites.org/; mibig array; accession/version selectors in E-matrix | partial | Inspected exact-version MIBiG payloads for BGC0000751:1 version 3, BGC0000752:1 version 3, BGC0000753:1 version 3. All active, generic capsule label, empty compound and locus-method evidence. These support a database assertion, not experimentally established exact-product equivalence. |
| E-genbank | https://www.ncbi.nlm.nih.gov/nuccore/; GBSeq accession-version; source feature strain/isolate, serotype and db_xref qualifiers | supports | AY496881.1: 8329, serotype 12; AY534316.1: Femo, serotype 6; AY534317.1: isolate 72-14676, serotype 7 |
| E-matrix | reviews/evidence/20261013-capsular/manifest.json; matrix.json | supports | Exact-source mapping, complete raw-row SHA256 pins and deposited context; no taxon or product inference. |
| E-taxonomy | https://www.ncbi.nlm.nih.gov/taxonomy | supports | Six source taxon IDs resolve with the retained labels/ranks: 573 species, 574 subspecies, 1311 species, 715 species, 720 species, 754256 strain. No species-to-strain remapping inferred. |
| E-pubchem | https://pubchem.ncbi.nlm.nih.gov/compound/195740; RecordTitle and MeSH/Synonyms; no identity inferred from names alone | context_only | Names and Identifiers record title associates this graph with type 7; MeSH names explicitly use name-based association, not chemical equivalence certification. |
| E-chemistry | reviews/evidence/20261013-capsular/manifest.json; data/natural_products/unclassified/capsular-polysaccharide.yaml | supports | RDKit 2026.03.5 reproduces stored Standard InChI and key and matches PubChem. Formula C15H29O16P; 9 assigned and 0 undefined centers; stereo_complete flag is computationally consistent. Finite graph, not a variable-degree polymer; this does not validate its biological assignment. |
| E-literature | PMID:18215476; Europe PMC result id 18215476 | partial | Three serotype 12/6/7 loci share one finite type-7-labelled graph. Its n-propoxy substituent, geminal ring diol and phosphate monoester require adjudication against capsule chemistry. The accessible 2024 study describes a glycosylglycerol-phosphate polymer backbone, not this finite graph, and its AP76 enzyme context is not the imported isolate 72-14676. A. lignieresii occurrence support remains unknown because the cited full paper is inaccessible; absence from its abstract is not refutation. Metadata and abstract only for this cited paper; full text was denied and was not retrieved through an alternate route. |
| E-sources | data/raw/mibig_compounds.tsv | supports | Structured full-inventory joins retain imported rows, LOTUS references and NPClassifier pin. No exact-key ChEBI grounding row or sibling link; 21 capsule-context ChEBI rows are not exact identity candidates. Initial name-only Chebi-origin zero was not exhaustive; exact-ID context origins were separately checked. |
| E-search | reviews/evidence/20261013-capsular/manifest.json | context_only | Ignored-inclusive local search found the three owners and queue/lock references, not additional matching maintained corrections or components in the declared scope. |
| E-primary-backbone | DOI:10.1038/s41589-024-01664-8; PMC11666461 Sec6 and cloning methods | partial | Full text Results Cps7D polymerization and cloning methods inspected. Cps7D builds a galactosylglycerol-phosphate backbone; Cps7A/C experiments include AP76, not imported isolate 72-14676. This does not certify the complete modified native capsule or upgrade the imported loci. |
| E-check-strict | reviews/evidence/20261013-capsular/manifest.json; strict.log | supports | Actual execution 2026-10-13T20:52:51.224787Z through 2026-10-13T20:52:54.565972Z; exit 0. This deterministic check is not scientific certification. |
| E-check-labels | reviews/evidence/20261013-capsular/manifest.json; labels.log | supports | Actual execution 2026-10-13T20:53:32.890779Z through 2026-10-13T20:55:10.121917Z; exit 0. Label check retains 499 warnings and 4649 adapter skips; not all identifier classes remotely resolved. |
| E-check-corpus | reviews/evidence/20261013-capsular/manifest.json; corpus.log | supports | Actual execution 2026-10-13T20:57:14.235892Z through 2026-10-13T20:58:21.232339Z; exit 0. This deterministic check is not scientific certification. |
| E-check-chemistry-pinned | reviews/evidence/20261013-capsular/manifest.json; chemistry-pinned.log | supports | Actual execution 2026-10-13T20:56:30.571312Z through 2026-10-13T20:56:32.114784Z; exit 0. This deterministic check is not scientific certification. |
| E-check-local-search | reviews/evidence/20261013-capsular/manifest.json; local-search.log | supports | Actual execution 2026-10-13T20:56:31.792599Z through 2026-10-13T20:56:31.865683Z; exit 0. This deterministic check is not scientific certification. |

## Limits And Additional Notes

- The three cited primary full texts encountered HTTP403; applicable Wikidata organism endpoints also denied access. Later structural leads with access challenges were not pursued through alternate routes.
- Default Python lacked RDKit; uv chemistry-extra resolution lacked an Intel Mac wheel. Exact pinned RDKit 2026.03.5 in an existing environment succeeded. Earlier CLI dependency failures were superseded by the installed sibling runner.
- PubChem naming is not exact-product proof. No replacement structure, all-serotype equivalence, experimental strain equivalence or complete native polymer modification set established.
- Deterministic QC is not a completed scientific review. Full campaign remains incomplete; this assesses historical base b87e2fa3 before curation.
- Evidence manifest retains source captures, derived chemistry, source matrix and execution receipts; publication metadata/full article content is reference-only where redistribution is not established.
- Prior GBS type II lead discarded: current registry label is type V.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T210902Z-capsular-polysaccharide
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Capsular product scientific review: Actinobacillus'
started_at: '2026-10-13T20:50:38Z'
finished_at: '2026-10-13T21:09:02.235470Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same assistant conducting the campaign and follow-up; not independent
    human sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
native_verdict: SEEDED retained; exact identity not adjudicated
summary: One identity blocker and one minor deposited-context finding; primary access
  gaps prevent full assessment.
source:
  git_revision: b87e2fa3e2acc7896755a7c4eaa09d48fe0159e8
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
  - path: curation/mibig_producer_strains.tsv
    sha256: 3188b61104388bf7725540c7e29f83f65ae3a0b458710c6e42de6a0c4bff215e
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: ac01b66bb97bc2c4e16558227fed641e28daa3c5926a09e213e98c38a09856a2
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
    sha256: a6f7cdde7a670bbeee6a415ae8c3c62c45850cf4b9b4e4c07f8522850ce80845
    role: context
  - path: data/natural_products/carbohydrates/capsular-polysaccharide-3.yaml
    sha256: fa2ccc203ee86f2f2cbffb12ee9d0a3743d716e36adc23ba2e5cfabe4125833a
    role: context
  - path: data/natural_products/unclassified/capsular-polysaccharide.yaml
    sha256: 5e72568abadd03108ff5a45f1fdad9f6886190396e2844b71a6fab02e7215545
    role: target
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
    sha256: aba5606d7e5e7c2887e66294655db26a10e853a42893d71aab8f015dc9b91c71
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 21fd298fb528f1179286125bc3d12f36ae72ca6c1e0f783cf94dcace2648f292
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: 6026ddca19f0989d499b1681f7724fbab23918de8d3957750b49bbfe1a9c0bff
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
scope:
  description: One exact capsule owner and all attached components (none).
  selection: Next exact owner in the exhaustive 3115-owner campaign checkpoint; no
    cohort extrapolation.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-241ecc69e8
  exclusions:
  - target: Other 3114 owners and their components
    reason: Not assessed in this observation.
targets:
- target_id: naturalproductmech:mibig-241ecc69e8
  path: data/natural_products/unclassified/capsular-polysaccharide.yaml
  label: capsular polysaccharide
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
    path: curation/mibig_claim_references.tsv
    role: Implemented pinned claim-specific citation routing
checks:
- check_id: C-strict
  name: strict
  status: passed
  required: true
  summary: Actual execution 2026-10-13T20:52:51.224787Z through 2026-10-13T20:52:54.565972Z;
    exit 0. This deterministic check is not scientific certification.
  command: just validate-strict data/natural_products/carbohydrates/capsular-polysaccharide-2.yaml
    data/natural_products/carbohydrates/capsular-polysaccharide-3.yaml data/natural_products/unclassified/capsular-polysaccharide.yaml
    --out /private/tmp/npmech-capsular-resume-6vn9Sp/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-check-strict
- check_id: C-labels
  name: labels
  status: passed
  required: true
  summary: Actual execution 2026-10-13T20:53:32.890779Z through 2026-10-13T20:55:10.121917Z;
    exit 0. Label check retains 499 warnings and 4649 adapter skips; not all identifier
    classes remotely resolved.
  command: just validate-products
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-check-labels
- check_id: C-corpus
  name: corpus
  status: passed
  required: true
  summary: Actual execution 2026-10-13T20:57:14.235892Z through 2026-10-13T20:58:21.232339Z;
    exit 0. This deterministic check is not scientific certification.
  command: just verify-corpus --summary
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-check-corpus
- check_id: C-chemistry-pinned
  name: chemistry-pinned
  status: passed
  required: true
  summary: Actual execution 2026-10-13T20:56:30.571312Z through 2026-10-13T20:56:32.114784Z;
    exit 0. This deterministic check is not scientific certification.
  command: env RDBASE=/private/tmp/npmech-rdkit-2026.03.5/share/RDKit PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/NaturalProductMech/.venv/lib/python3.13/site-packages
    /private/tmp/npmech-rdkit-2026.03.5/bin/python /private/tmp/npmech-capsular-resume-6vn9Sp/chemistry.py
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-check-chemistry-pinned
- check_id: C-local-search
  name: local-search
  status: passed
  required: true
  summary: Actual execution 2026-10-13T20:56:31.792599Z through 2026-10-13T20:56:31.865683Z;
    exit 0. This deterministic check is not scientific certification.
  command: rg --no-ignore --hidden -l -i -e 'ODLPTSAMUCYJMF|NOVHANKYCIGDMV|FJTWZGAJWZJDEU|mibig-6a3f1200b4|mibig-ffbecb0bfb|mibig-241ecc69e8|capsular.?polysaccharide|BGC00007(28|29|30|31|33|40|41|42|43|44|45|46|47|48|51|52|53)'
    data/natural_products data/causal_graphs curation src scripts .claude
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-check-local-search
- check_id: C-primary
  name: Exact-product primary evidence and LOTUS origin trace
  status: unavailable
  required: true
  summary: The cited primary full text and applicable Wikidata origin endpoints encountered
    HTTP403/access challenges. Abstracts and database payloads do not resolve exact-product
    identity; no bypass attempted.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-literature
- check_id: C-imodulondb
  name: Structured expression dataset applicability search
  status: passed
  required: false
  summary: Installed sibling kg-microbe-sources imodulondb datasets ran successfully;
    no covered target organism dataset. Not negative biological evidence. Earlier
    missing runner/dependency attempts failed and were superseded.
  command: ../../culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
- check_id: C-prior-qc
  name: Exact-base historical native QC
  status: passed
  required: true
  summary: Historical merge-group run 38464138422 on b87e2fa3 passed native QC and
    reproduction (786 passed, 4 skipped). All current domain input hashes matched
    that base at capture; not a fresh full QC run for these review bundles.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  scope_note: https://github.com/CultureBotAI/NaturalProductMech/actions/runs/38464138422
evidence:
- evidence_id: E-owner
  kind: record_content
  reference: data/natural_products/unclassified/capsular-polysaccharide.yaml
  accessed_at: '2026-10-13T21:09:02.221897Z'
  support: supports
  summary: Entire owner read, with all source concepts, producer/cluster/occurrence
    claims, history and discussions; no attached graph components.
  snapshot_sha256: 5e72568abadd03108ff5a45f1fdad9f6886190396e2844b71a6fab02e7215545
  locator: b87e2fa3e2acc7896755a7c4eaa09d48fe0159e8
- evidence_id: E-mibig
  kind: database
  reference: https://mibig.secondarymetabolites.org/
  accessed_at: '2026-10-13T21:09:02.222242Z'
  support: partial
  summary: Inspected exact-version MIBiG payloads for BGC0000751:1 version 3, BGC0000752:1
    version 3, BGC0000753:1 version 3. All active, generic capsule label, empty compound
    and locus-method evidence. These support a database assertion, not experimentally
    established exact-product equivalence.
  snapshot_sha256: 438709a7cb49bf4c7523c49ea49c07c4b56c735d83845d0b3f3aee223e58ada5
  locator: mibig array; accession/version selectors in E-matrix
- evidence_id: E-genbank
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/
  accessed_at: '2026-10-13T19:48:10.386471Z'
  support: supports
  summary: 'AY496881.1: 8329, serotype 12; AY534316.1: Femo, serotype 6; AY534317.1:
    isolate 72-14676, serotype 7'
  snapshot_sha256: d48604e4364f1f43d70fe261e4ce7f52a45acb1bb7926d771aae79f1f261c54f
  locator: GBSeq accession-version; source feature strain/isolate, serotype and db_xref
    qualifiers
- evidence_id: E-matrix
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.227725Z'
  support: supports
  summary: Exact-source mapping, complete raw-row SHA256 pins and deposited context;
    no taxon or product inference.
  snapshot_sha256: 6f79ff99a15f8b25f3df3dc09b9993d6222933129d982e9dca01d9cf0727a83f
  locator: matrix.json
- evidence_id: E-taxonomy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/taxonomy
  accessed_at: '2026-10-13T19:48:09.343586Z'
  support: supports
  summary: 'Six source taxon IDs resolve with the retained labels/ranks: 573 species,
    574 subspecies, 1311 species, 715 species, 720 species, 754256 strain. No species-to-strain
    remapping inferred.'
  snapshot_sha256: 522e8722824406b9540f9cf7d523a21fdaaeecfe51a7d7aa52b78f58e4727cfb
- evidence_id: E-pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/compound/195740
  accessed_at: '2026-10-13T20:59:07.984929Z'
  support: context_only
  summary: Names and Identifiers record title associates this graph with type 7; MeSH
    names explicitly use name-based association, not chemical equivalence certification.
  snapshot_sha256: 26b43a0c143a34fb207b3f7114cadbad7e27ffcb7d90fa0a0937070267a06f22
  locator: RecordTitle and MeSH/Synonyms; no identity inferred from names alone
- evidence_id: E-chemistry
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.230072Z'
  support: supports
  summary: RDKit 2026.03.5 reproduces stored Standard InChI and key and matches PubChem.
    Formula C15H29O16P; 9 assigned and 0 undefined centers; stereo_complete flag is
    computationally consistent. Finite graph, not a variable-degree polymer; this
    does not validate its biological assignment.
  snapshot_sha256: ced3910a68670247d484823025f55eb213ba7c071b2a499f28d008ac0ef00095
  locator: data/natural_products/unclassified/capsular-polysaccharide.yaml
- evidence_id: E-literature
  kind: primary_source
  reference: PMID:18215476
  accessed_at: '2026-10-13T19:47:09.197319Z'
  support: partial
  summary: Three serotype 12/6/7 loci share one finite type-7-labelled graph. Its
    n-propoxy substituent, geminal ring diol and phosphate monoester require adjudication
    against capsule chemistry. The accessible 2024 study describes a glycosylglycerol-phosphate
    polymer backbone, not this finite graph, and its AP76 enzyme context is not the
    imported isolate 72-14676. A. lignieresii occurrence support remains unknown because
    the cited full paper is inaccessible; absence from its abstract is not refutation.
    Metadata and abstract only for this cited paper; full text was denied and was
    not retrieved through an alternate route.
  snapshot_sha256: 1f6a507b2df32cd81f07fe2829af7f07f1a6c240dae48d0c218f55e359b373a1
  locator: Europe PMC result id 18215476
- evidence_id: E-sources
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  accessed_at: '2026-10-13T21:09:02.230634Z'
  support: supports
  summary: Structured full-inventory joins retain imported rows, LOTUS references
    and NPClassifier pin. No exact-key ChEBI grounding row or sibling link; 21 capsule-context
    ChEBI rows are not exact identity candidates. Initial name-only Chebi-origin zero
    was not exhaustive; exact-ID context origins were separately checked.
  snapshot_sha256: b0d0c361842a27518591244c10e8014e4b79e6921e2da0794d4d47b6a26c6a9f
- evidence_id: E-search
  kind: search
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.230861Z'
  support: context_only
  summary: Ignored-inclusive local search found the three owners and queue/lock references,
    not additional matching maintained corrections or components in the declared scope.
  snapshot_sha256: 8ab6707bbf6e19a34ee121578b068544e807c2083c7bff89c84b176d1c3c16a8
  search_scope: rg --no-ignore --hidden over data/natural_products, data/causal_graphs,
    curation, src, scripts and .claude using all three identifiers/keys, capsule label
    and 17 BGC IDs; raw inventory joins use CSV parsing separately.
- evidence_id: E-primary-backbone
  kind: primary_source
  reference: DOI:10.1038/s41589-024-01664-8
  accessed_at: '2026-10-13T20:55:39.286268Z'
  support: partial
  summary: Full text Results Cps7D polymerization and cloning methods inspected. Cps7D
    builds a galactosylglycerol-phosphate backbone; Cps7A/C experiments include AP76,
    not imported isolate 72-14676. This does not certify the complete modified native
    capsule or upgrade the imported loci.
  snapshot_sha256: 1d28fb544ee70cf57439b33ef1c2862c8fa741e402ab9fec5d08d0d0e453e840
  locator: PMC11666461 Sec6 and cloning methods
- evidence_id: E-check-strict
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.234239Z'
  support: supports
  summary: Actual execution 2026-10-13T20:52:51.224787Z through 2026-10-13T20:52:54.565972Z;
    exit 0. This deterministic check is not scientific certification.
  snapshot_sha256: e1c5b1bb8e23eff84b07920005909fba97d10a23e59b02d5fb7f2763dfd98fa3
  locator: strict.log
- evidence_id: E-check-labels
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.234507Z'
  support: supports
  summary: Actual execution 2026-10-13T20:53:32.890779Z through 2026-10-13T20:55:10.121917Z;
    exit 0. Label check retains 499 warnings and 4649 adapter skips; not all identifier
    classes remotely resolved.
  snapshot_sha256: 19a4f6cca7894851de23ee2062f52d29b32def53c7b4f59edbc6c45ec4ce9828
  locator: labels.log
- evidence_id: E-check-corpus
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.234767Z'
  support: supports
  summary: Actual execution 2026-10-13T20:57:14.235892Z through 2026-10-13T20:58:21.232339Z;
    exit 0. This deterministic check is not scientific certification.
  snapshot_sha256: 99919ecf8be13f6447470547d51601b47f57ec19836b0254cb62cbf94b505a1c
  locator: corpus.log
- evidence_id: E-check-chemistry-pinned
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.235083Z'
  support: supports
  summary: Actual execution 2026-10-13T20:56:30.571312Z through 2026-10-13T20:56:32.114784Z;
    exit 0. This deterministic check is not scientific certification.
  snapshot_sha256: 3c24e1c608c797f4ccc64b10093d02467884a1be85c818cc920338dc4840de24
  locator: chemistry-pinned.log
- evidence_id: E-check-local-search
  kind: validation
  reference: reviews/evidence/20261013-capsular/manifest.json
  accessed_at: '2026-10-13T21:09:02.235324Z'
  support: supports
  summary: Actual execution 2026-10-13T20:56:31.792599Z through 2026-10-13T20:56:31.865683Z;
    exit 0. This deterministic check is not scientific certification.
  snapshot_sha256: 8ab6707bbf6e19a34ee121578b068544e807c2083c7bff89c84b176d1c3c16a8
  locator: local-search.log
assessments:
- assessment_id: A-identity
  area: identity
  topic: Exact product versus capsule/serotype concept
  outcome: concern
  summary: Three serotype 12/6/7 loci share one finite type-7-labelled graph. Its
    n-propoxy substituent, geminal ring diol and phosphate monoester require adjudication
    against capsule chemistry. The accessible 2024 study describes a glycosylglycerol-phosphate
    polymer backbone, not this finite graph, and its AP76 enzyme context is not the
    imported isolate 72-14676. A. lignieresii occurrence support remains unknown because
    the cited full paper is inaccessible; absence from its abstract is not refutation.
    Registry names/MeSH associations are name-based and are not independent chemical
    certification. Exact PubChem graph agreement is verified; deleting its xref alone
    would not repair the biological assignment. The confirmed defect is unsupported
    exact-product assignment across the recorded contexts, not an experimentally established
    replacement structure.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-owner
  - E-mibig
  - E-genbank
  - E-pubchem
  - E-literature
- assessment_id: A-structure
  area: representation
  topic: Internal chemical encoding and exact registry xref
  outcome: supported
  summary: RDKit 2026.03.5 reproduces stored Standard InChI and key and matches PubChem.
    Formula C15H29O16P; 9 assigned and 0 undefined centers; stereo_complete flag is
    computationally consistent. Finite graph, not a variable-degree polymer; this
    does not validate its biological assignment. Keep the exact PubChem xref; it is
    not a mismatching-key case.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-chemistry
  - E-pubchem
  details: n-propoxy-on-ring, geminal-ring-diol and phosphate-monoester SMARTS matches
    are persisted with atom indices. Their biological assignment remains unresolved;
    no replacement graph inferred.
- assessment_id: A-grounding
  area: grounding
  topic: Minted identity and exact joins
  outcome: supported
  summary: MINTED rationale agrees with pinned exact-key inventory joins. Broader
    capsule ontology terms cannot serve as exact structure replacements.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-sources
- assessment_id: A-class
  area: consistency
  topic: Computed filing, asserted class, taxonomy and origin facets
  outcome: supported
  summary: Filing UNCLASSIFIED follows the pinned NPClassifier output; SACCHARIDE
    remains an asserted BGC class. NATURAL_PRODUCT is source-asserted, not predicted.
    OTHER_BACTERIAL taxonomy is separate from natural/engineered origin. This is metadata
    consistency, not validation of the disputed graph assignment.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-owner
  - E-sources
  - E-taxonomy
- assessment_id: A-producer
  area: provenance
  topic: Producer and locus evidence scope
  outcome: concern
  summary: 3 deposited strain/isolate qualifiers are missing from explicit producer
    context. SOURCE_ASSERTION and CLUSTER_UNSTATED correctly reflect empty MIBiG method
    lists; no characterization upgrade justified.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-owner
  - E-mibig
  - E-genbank
  dimensions:
  - name: deposited_context
    value: 'AY496881.1: 8329 / 12; AY534316.1: Femo / 6; AY534317.1: isolate 72-14676
      / 7'
    definition: Exact GenBank source strain/isolate and serotype qualifiers, not experimental
      proof of the assigned finite compound.
    evidence_ids:
    - E-genbank
- assessment_id: A-occurrence
  area: evidence
  topic: Occurrence versus production and publication independence
  outcome: unknown
  summary: LOTUS occurrences remain DATABASE_ASSERTION, never promoted to production.
    Their DOI is the same publication as the PMID on the MIBiG entries, not independent
    evidence. Exact structure and Wikidata provenance remain unresolved. A. lignieresii
    support is unknown, not disproved by absence from the abstract.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-owner
  - E-sources
  - E-literature
- assessment_id: A-optional
  area: completeness
  topic: Graphs, pathway, activities, targets, clinical status and sibling links
  outcome: not_applicable
  summary: Full owner has no graph components, curated mechanism, assay, molecular
    target, clinical status or related sibling link. These optional absences are not
    fabricated defects; clinical/genotype studies are not pure-compound bioactivity
    assays.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-owner
  - E-search
  - E-sources
- assessment_id: A-history
  area: ownership
  topic: Generated boundaries and scientific status
  outcome: supported
  summary: SEEDED remains appropriate. Existing shared-structure discussion is OPEN;
    no REVIEWED promotion. Generated changes belong in implemented curation tables
    or source transforms, not reserved unconsumed decisions.tsv.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  evidence_ids:
  - E-owner
findings:
- finding_id: F1
  issue_key: capsular-polysaccharide-exact-product-assignment
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Exact capsule-product assignment is unsupported across deposited serotypes
  description: Three serotype 12/6/7 loci share one finite type-7-labelled graph.
    Its n-propoxy substituent, geminal ring diol and phosphate monoester require adjudication
    against capsule chemistry. The accessible 2024 study describes a glycosylglycerol-phosphate
    polymer backbone, not this finite graph, and its AP76 enzyme context is not the
    imported isolate 72-14676. A. lignieresii occurrence support remains unknown because
    the cited full paper is inaccessible; absence from its abstract is not refutation.
    Registry names/MeSH associations are name-based and are not independent chemical
    certification. Exact PubChem graph agreement is verified; deleting its xref alone
    would not repair the biological assignment. The confirmed defect is unsupported
    exact-product assignment across the recorded contexts, not an experimentally established
    replacement structure.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  field_paths:
  - chemical_structure
  - producer_organisms
  - biosynthetic_gene_clusters
  evidence_ids:
  - E-mibig
  - E-genbank
  - E-pubchem
  - E-chemistry
  - E-literature
  - E-primary-backbone
  rule_id: 'CLAUDE.md: A record is a structure; review-checklist: Identity and Gene
    clusters'
  native_severity: blocker
  normalization_reason: The compound identity assigned to biological source claims
    is not established; a valid graph and generic capsule name do not prove equivalence.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/937
- finding_id: F2
  issue_key: capsular-polysaccharide-deposited-strain-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Deposited strain and serotype qualifications are missing
  description: 3 source qualifiers are available but not explicitly carried into producer
    strain/evidence context. Femo is already in the taxon label; isolate 72-14676
    must not become WF83 or AP76.
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  field_paths:
  - producer_organisms[].strain
  - producer_organisms[].evidence
  evidence_ids:
  - E-owner
  - E-genbank
  - E-matrix
  rule_id: 'review-checklist: Producer organisms'
  native_severity: minor
  normalization_reason: Bounded provenance repair that can be made without deciding
    chemical identity or evidence grade.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented pinned strain qualifications
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/938
actions:
- action_id: A1
  description: Preserve an OPEN identity qualification, then adjudicate exact locus-to-product
    and occurrence assignments from accessible primary chemistry before migration;
    do not rename all entries to the registry serotype.
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Imported chemical, producer and cluster assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated harmonization and grading
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Implemented pinned structure corrections
  acceptance_checks:
  - Per-source structure and polymer/form boundary justified by inspected primary
    chemistry.
  - Use a supported maintained migration/exclusion path, preserve provenance, and
    pass strict validation, reproduction and full QC.
  generator: scripts/seed_from_sources.py
- action_id: A2
  description: Add complete-row-pinned strain qualifications with versioned GenBank
    references and serotype rationale; no taxon or evidence-grade changes.
  finding_ids:
  - F2
  target_ids:
  - naturalproductmech:mibig-241ecc69e8
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Implemented pinned strain qualifications
  acceptance_checks:
  - All deposited qualifiers match source; isolate remains labelled as isolate.
  - Canary, scoped reseeding, invariant regression tests and byte-identical reproduction
    pass.
  generator: scripts/seed_from_sources.py
limitations:
- The three cited primary full texts encountered HTTP403; applicable Wikidata organism
  endpoints also denied access. Later structural leads with access challenges were
  not pursued through alternate routes.
- Default Python lacked RDKit; uv chemistry-extra resolution lacked an Intel Mac wheel.
  Exact pinned RDKit 2026.03.5 in an existing environment succeeded. Earlier CLI dependency
  failures were superseded by the installed sibling runner.
- PubChem naming is not exact-product proof. No replacement structure, all-serotype
  equivalence, experimental strain equivalence or complete native polymer modification
  set established.
- Deterministic QC is not a completed scientific review. Full campaign remains incomplete;
  this assesses historical base b87e2fa3 before curation.
notes:
- Evidence manifest retains source captures, derived chemistry, source matrix and
  execution receipts; publication metadata/full article content is reference-only
  where redistribution is not established.
- 'Prior GBS type II lead discarded: current registry label is type V.'
tags:
- capsular
- scientific-review
- partial
```
