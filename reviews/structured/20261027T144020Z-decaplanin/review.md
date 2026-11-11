# Scientific review of decaplanin

- Review: 20261027T144020Z-decaplanin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T14:38:54.456650Z
- Finished UTC: 2026-10-27T14:40:20.997372Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The decaplanina abstract directly supports decaplanin production by DSM44594T; the regifaucium taxonomy abstract does not resolve that separate compound association. Two source entries retain an open shared-structure discussion. Local encodings agree while leaving 23 tetrahedral carbon sites unassigned; exact natural structure, both locus mappings and current taxonomy remain unresolved.

## Scope And Provenance

Complete retained owner and source-row reading, local encoding checks, and bounded scientific interpretation of inspected publication metadata and supplied abstracts.

Selection: One resolved record in canonical path order from the unreviewed corpus; actual official intake reconciled to retained evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-de067fa3d6 | data/natural_products/amino_acids_and_peptides/decaplanin.yaml | generated | decaplanin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-de067fa3d6 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-de067fa3d6 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-de067fa3d6 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-de067fa3d6 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-de067fa3d6 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | naturalproductmech:mibig-de067fa3d6 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved local encoding and stereo consistency | passed | True | naturalproductmech:mibig-de067fa3d6 | Saved RDKit 2026.03.5 results regenerate SJSZMXQSCZCGFO-UHFFFAOYSA-N from both retained encodings, with formula C72H86ClN9O28, one fragment and formal charge zero. Both encodings contain 23 unassigned tetrahedral carbon sites, consistent with the retained stereo_complete=false. This establishes encoding consistency, not natural absolute configuration. Seven additional unspecified double-bond observations in the parsed InChI representation have saved C(-O)=N neighbor environments. They are not seven additional missing natural C=C configurations; the distinct unassigned tetrahedral carbon sites remain unresolved. |
| Own PMID/DOI identity and original metadata scope | passed | True | naturalproductmech:mibig-de067fa3d6 | Own ArticleIdList verifies PMID14742486/DOI10.1099/ijs.0.02586-0 and PMID17978218/DOI10.1099/ijs.0.64974-0. The four owner citation placements represent two papers; original access and later reading clocks are retained separately. |
| Exact material, shared structure and current authority | unavailable | True | naturalproductmech:mibig-de067fa3d6 | No full primary/SI or current structure/taxon authority check establishes the exact natural stereoisomer or resolves the existing BGC0001459/BGC0001460 shared-structure discussion. |
| Exact locus and regifaucium compound applicability | unavailable | True | naturalproductmech:mibig-de067fa3d6 | Neither abstract establishes the retained genome accession/coordinate claims. Compound-specific support for the regifaucium association remains unresolved; its kigamicin title does not alone demonstrate misattribution. |

## Scientific And Domain Assessments

### Internal structure encoding

representation: supported. Targets: naturalproductmech:mibig-de067fa3d6.

Saved RDKit 2026.03.5 results regenerate SJSZMXQSCZCGFO-UHFFFAOYSA-N from both retained encodings, with formula C72H86ClN9O28, one fragment and formal charge zero. Both encodings contain 23 unassigned tetrahedral carbon sites, consistent with the retained stereo_complete=false. This establishes encoding consistency, not natural absolute configuration.

### Named producer and strain context

evidence: supported. Targets: naturalproductmech:mibig-de067fa3d6.

PMID14742486 explicitly describes DSM44594T producing decaplanin and states its type-strain aliases. This supports the named producer/material context of the second MIBiG entry and the species-level LOTUS occurrence; it does not verify either retained taxon identifier or exact locus.

### Separate regifaucium compound claim

evidence: unknown. Targets: naturalproductmech:mibig-de067fa3d6.

PMID17978218 supplies a kigamicin-producing A. regifaucium taxonomy context and no decaplanin assertion in its abstract. Exact compound support must be resolved from appropriate primary material or retained entry provenance; neither a wrong citation nor a negative species-production claim follows from this omission.

### Two distinct retained loci and source grades

provenance: unknown. Targets: naturalproductmech:mibig-de067fa3d6.

BGC0001459/LOBU02000007.1:259653–327583 and BGC0001460/AOHO01000074.1:276857–343203 retain SOURCE_ASSERTION and CLUSTER_UNSTATED with blank method fields. Abstract producer support does not verify these coordinates or justify silently changing either grade.

### Open shared-structure question

representation: unknown. Targets: naturalproductmech:mibig-de067fa3d6.

The two MIBiG rows store the same stereochemically incomplete structure and the owner explicitly retains an OPEN shared-structure discussion. Internal full-key agreement does not establish that both biological source entries describe one exact natural stereoisomer.

### Production, occurrence and publication independence

provenance: supported. Targets: naturalproductmech:mibig-de067fa3d6.

Own metadata proves each PMID aliases the corresponding LOTUS DOI. Preserve producer and occurrence distinctions, strain/species scope and the two-paper count. Taxon equivalence is not inferred from shared names.

### Retained glycopeptide classification

representation: supported. Targets: naturalproductmech:mibig-de067fa3d6.

The local NPClassifier glycoside and Vancomycins-and-Teicoplanins filing is compatible with the own abstract describing decaplanin as a glycopeptide antibiotic. This is broad classification support, not exact connectivity or stereochemical verification.

### Assay, target and graph coverage

completeness: unknown. Targets: naturalproductmech:mibig-de067fa3d6.

The empty-AID PubChem row is a no-assay-data sentinel. The owner has no quantitative bioactivity, molecular target, pathway step or causal graph; these local absences establish neither inactivity nor global absence of such evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI654-LOCAL | /private/tmp/npm-review-work/shared-next-batch066-tentative/tentative-owner-source-inventory-001.json; /entries/3/owner_document; /entries/3/rows; /entries/3/supplemental_retained_rows | context_only | The retained decaplanin owner joins two MIBiG entries, two LOTUS occurrences, one NPClassifier row and one empty-AID PubChem sentinel; the other retained and both supplemental arrays are empty. These local rows do not independently verify natural material or current authority identities. |
| SCI654-CHEM | /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-local-chemical-consistency-001.json; /records/3 | supports | Saved RDKit 2026.03.5 results regenerate SJSZMXQSCZCGFO-UHFFFAOYSA-N from both retained encodings, with formula C72H86ClN9O28, one fragment and formal charge zero. Both encodings contain 23 unassigned tetrahedral carbon sites, consistent with the retained stereo_complete=false. This establishes encoding consistency, not natural absolute configuration. |
| SCI654-NEIGHBORS | /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-saved-stereo-neighbor-inspection-001.json; /records/3 | supports | Seven additional unspecified double-bond observations in the parsed InChI representation have saved C(-O)=N neighbor environments. They are not seven additional missing natural C=C configurations; the distinct unassigned tetrahedral carbon sites remain unresolved. |
| SCI654-DECAPLANINA | PMID:14742486; ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList; cached body /private/tmp/npm-review-work/shared-next-batch066-tentative/literature-preparation/public-metadata-001/pmid-14742486.xml | supports | The supplied own abstract explicitly identifies decaplanin-producing DSM44594T and the type-strain equivalence FH1845T=DSM44594T=NRRL B-24209T. This supports the named compound/producer context without verifying the retained molecular key or AOHO01000074.1 locus. Metadata/abstract only; no primary full text or reference-list evidence. |
| SCI654-REGIFAUCIUM | PMID:17978218; ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList; cached body /private/tmp/npm-review-work/shared-next-batch066-tentative/literature-preparation/public-metadata-pubmed-002/pmid-17978218.xml | context_only | The own title concerns A. regifaucium producing kigamicins and the supplied abstract reports its taxonomy. It does not name decaplanin. This does not corroborate the retained compound claim at abstract tier, but omission alone establishes neither a wrong citation nor inability of the species to produce decaplanin. Metadata/abstract only; no primary full text or reference-list evidence. |

## Limits And Additional Notes

- Full primary text/SI and current taxon/structure/sequence authorities were not inspected.
- The retained 23 unassigned tetrahedral carbon sites remain unresolved; parsed InChI C(-O)=N flags are a separate representational observation.
- The existing shared-structure discussion and exact regifaucium compound/locus applicability remain open; no corrective finding is inferred from abstract omission alone.
- The current official intake reproduces the retained owner and six official source arrays. Additional PubChem and supplemental arrays retain their original local-reading scope. Baseline and ROOT decisions are bound separately; saved two-encoding computation and official intake SMILES computation remain distinct.
- Configured consistency only; independent scientific claim support and unrestricted remote authority refresh are not implied.
- Fresh QC attempt001 failed on public canonical-artifact DNS retrieval after lint and before downstream tests. Its actual exit1/log/input capture/root observation remain pinned; the selected successful canonical QC attempt002 is separately timed. No individual-review validation failure or counter reset is claimed.
- 499non-blocking identifier-label warnings,35configured exceptions and4898no-adapter skips remain unverified within this gate.
- The QC test suite reported four skipped tests and two dependency deprecation warnings; this pass does not assert skipped checks ran.
- Canonical reproduction retains five unresolved assay-organism annotations,42 withheld nonsingle-organism producer claims and161 configured taxon-ID rewrites.
- This QC is a configured consistency gate, not an independent primary-source biological or stereochemical verification.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions and no-adapter pairs; a successful command does not convert these into verified scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population was checked; external caches and generated bytecode are not asserted to be independently byte-pinned.
- The whole local owner and retained source rows were read. Full-owner scientific verification remains false; scientific_review denotes the bounded scientific interpretation in this report.
- Original owner/source reading, two-encoding computation, neighbor inspection, HTTP retrieval and later metadata reading retain separate clocks. Official intake separately computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. No corrective finding was established within the inspected evidence; exact-source limitations remain explicit.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/NaturalProductMech
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
review_id: 20261027T144020Z-decaplanin
title: Scientific review of decaplanin
started_at: '2026-10-27T14:38:54.456650Z'
finished_at: '2026-10-27T14:40:20.997372Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The decaplanina abstract directly supports decaplanin production by DSM44594T;
  the regifaucium taxonomy abstract does not resolve that separate compound association.
  Two source entries retain an open shared-structure discussion. Local encodings agree
  while leaving 23 tetrahedral carbon sites unassigned; exact natural structure, both
  locus mappings and current taxonomy remain unresolved.
source:
  git_revision: 14373517042b407747272446f79953ae86d51fa4
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
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
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/amino_acids_and_peptides/decaplanin.yaml
    sha256: 52615d26305121f4ccc32de32e963ef3f5cf495b09fa226a0d521fef215d1d23
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: data/raw/cyanometdb_occurrences.tsv
    sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
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
    sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: naturalproductmech:mibig-de067fa3d6
  path: data/natural_products/amino_acids_and_peptides/decaplanin.yaml
  label: decaplanin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: MIBiG source identity, producer and locus
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: LOTUS occurrence triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: CyanoMetDB exact-structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/amino_acids_and_peptides/decaplanin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
scope:
  description: Complete retained owner and source-row reading, local encoding checks,
    and bounded scientific interpretation of inspected publication metadata and supplied
    abstracts.
  selection: One resolved record in canonical path order from the unreviewed corpus;
    actual official intake reconciled to retained evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-de067fa3d6
  exclusions:
  - target: Full primary material and current external authorities
    reason: Exact claims requiring full article/SI, current taxonomy, chemical or
      sequence authorities remain unverified.
checks:
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its
    pinned path.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-verify-corpus-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.783967Z;
    finished 2026-10-25T22:37:16.453216Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-corpus.log.
    Reused for batch066 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch066. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: Fresh canonical reproduction gate passed:all3116 records byte-identical
    to source seeding; source warnings remain retained.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-verify-reproduction-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.784055Z;
    finished 2026-10-25T22:37:31.682209Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/verify-reproduction.log.
    Reused for batch066 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch066. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: Fresh deterministic review queue completed:8922 rows across12 queues. Queue
    output is not scientific-review coverage.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-review-queue-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just review-queue --tsv /private/tmp/npm-review-queue-batch-036-fresh14373517-001.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.781802Z;
    finished 2026-10-25T22:37:08.229737Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/review-queue.log.
    Reused for batch066 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch066. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking
    mismatches and4898no-adapter skips remain explicit.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-validate-products-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-001 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:36:55.784040Z;
    finished 2026-10-25T22:37:32.251879Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-001/validate-products.log.
    Reused for batch066 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch066. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: Canonical just qc completed with actual terminal exit0:1024 tests passed,4
    skipped,2 dependency warnings;3116 records passed closed schema validation, site
    freshness, byte reproduction and lockfile integrity.22 governed artifacts and15
    raw inventories passed. Prior DNS failed001 remains preserved.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=14373517042b407747272446f79953ae86d51fa4
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-036-fresh14373517-baseline-qc-attempt-002
    PYTHONDONTWRITEBYTECODE=1 just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only fresh-20261025-002 execution on 14373517042b407747272446f79953ae86d51fa4
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-25T22:40:55.179857Z;
    finished 2026-10-25T22:46:28.974296Z. Exact original receipt: /private/tmp/npm-native-checks/batch-036/fresh-20261025-002/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-036/fresh-20261025-002/qc.log.
    Reused for batch066 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch066. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/decaplanin.yaml
    --out /private/tmp/npm-review-work/654/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T14:38:55.800033Z. Original
    receipt: /private/tmp/npm-review-work/654/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
- check_id: SCI654-ENCODING
  name: Saved local encoding and stereo consistency
  status: passed
  required: true
  summary: Saved RDKit 2026.03.5 results regenerate SJSZMXQSCZCGFO-UHFFFAOYSA-N from
    both retained encodings, with formula C72H86ClN9O28, one fragment and formal charge
    zero. Both encodings contain 23 unassigned tetrahedral carbon sites, consistent
    with the retained stereo_complete=false. This establishes encoding consistency,
    not natural absolute configuration. Seven additional unspecified double-bond observations
    in the parsed InChI representation have saved C(-O)=N neighbor environments. They
    are not seven additional missing natural C=C configurations; the distinct unassigned
    tetrahedral carbon sites remain unresolved.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-CHEM
  - SCI654-NEIGHBORS
- check_id: SCI654-OWN-IDS
  name: Own PMID/DOI identity and original metadata scope
  status: passed
  required: true
  summary: Own ArticleIdList verifies PMID14742486/DOI10.1099/ijs.0.02586-0 and PMID17978218/DOI10.1099/ijs.0.64974-0.
    The four owner citation placements represent two papers; original access and later
    reading clocks are retained separately.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-DECAPLANINA
  - SCI654-REGIFAUCIUM
- check_id: SCI654-EXACT-MATERIAL
  name: Exact material, shared structure and current authority
  status: unavailable
  required: true
  summary: No full primary/SI or current structure/taxon authority check establishes
    the exact natural stereoisomer or resolves the existing BGC0001459/BGC0001460
    shared-structure discussion.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-CHEM
  - SCI654-DECAPLANINA
  - SCI654-REGIFAUCIUM
- check_id: SCI654-LOCUS
  name: Exact locus and regifaucium compound applicability
  status: unavailable
  required: true
  summary: Neither abstract establishes the retained genome accession/coordinate claims.
    Compound-specific support for the regifaucium association remains unresolved;
    its kigamicin title does not alone demonstrate misattribution.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-DECAPLANINA
  - SCI654-REGIFAUCIUM
evidence:
- evidence_id: SCI654-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch066-tentative/tentative-owner-source-inventory-001.json
  locator: /entries/3/owner_document; /entries/3/rows; /entries/3/supplemental_retained_rows
  accessed_at: '2026-10-27T13:34:04.199112Z'
  snapshot_sha256: efcd8406650fc62eb769ecc575be2ac134e643c8b39c3a750558229786855677
  support: context_only
  summary: The retained decaplanin owner joins two MIBiG entries, two LOTUS occurrences,
    one NPClassifier row and one empty-AID PubChem sentinel; the other retained and
    both supplemental arrays are empty. These local rows do not independently verify
    natural material or current authority identities.
- evidence_id: SCI654-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-local-chemical-consistency-001.json
  locator: /records/3
  accessed_at: '2026-10-27T13:34:17.199424Z'
  snapshot_sha256: 827c0d7bb3ba949b11e8d7cf986fc122b208a34ab2f3e4ba0ff5bbc008a12c6c
  support: supports
  summary: Saved RDKit 2026.03.5 results regenerate SJSZMXQSCZCGFO-UHFFFAOYSA-N from
    both retained encodings, with formula C72H86ClN9O28, one fragment and formal charge
    zero. Both encodings contain 23 unassigned tetrahedral carbon sites, consistent
    with the retained stereo_complete=false. This establishes encoding consistency,
    not natural absolute configuration.
- evidence_id: SCI654-NEIGHBORS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-saved-stereo-neighbor-inspection-001.json
  locator: /records/3
  accessed_at: '2026-10-27T13:36:21.405954Z'
  snapshot_sha256: 5de0e2f1788d42f2e02a0b435258acb8805b646d63c184037c0b702f3cf871c6
  support: supports
  summary: Seven additional unspecified double-bond observations in the parsed InChI
    representation have saved C(-O)=N neighbor environments. They are not seven additional
    missing natural C=C configurations; the distinct unassigned tetrahedral carbon
    sites remain unresolved.
- evidence_id: SCI654-DECAPLANINA
  kind: primary_source
  reference: PMID:14742486
  locator: ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle;
    ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList;
    cached body /private/tmp/npm-review-work/shared-next-batch066-tentative/literature-preparation/public-metadata-001/pmid-14742486.xml
  accessed_at: '2026-10-27T13:49:51.703181Z'
  snapshot_sha256: 3502d6908b20f56cb6329ab242d3018409e012a3dcf59f74d35d297c633db49e
  support: supports
  summary: The supplied own abstract explicitly identifies decaplanin-producing DSM44594T
    and the type-strain equivalence FH1845T=DSM44594T=NRRL B-24209T. This supports
    the named compound/producer context without verifying the retained molecular key
    or AOHO01000074.1 locus. Metadata/abstract only; no primary full text or reference-list
    evidence.
- evidence_id: SCI654-REGIFAUCIUM
  kind: primary_source
  reference: PMID:17978218
  locator: ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle;
    ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList;
    cached body /private/tmp/npm-review-work/shared-next-batch066-tentative/literature-preparation/public-metadata-pubmed-002/pmid-17978218.xml
  accessed_at: '2026-10-27T13:56:34.174358Z'
  snapshot_sha256: e938fdad70ec41bbc16c8a749d0fe8717fddea69651dff59c3da9ea2b827717a
  support: context_only
  summary: The own title concerns A. regifaucium producing kigamicins and the supplied
    abstract reports its taxonomy. It does not name decaplanin. This does not corroborate
    the retained compound claim at abstract tier, but omission alone establishes neither
    a wrong citation nor inability of the species to produce decaplanin. Metadata/abstract
    only; no primary full text or reference-list evidence.
assessments:
- assessment_id: SCI654-ENCODING
  area: representation
  topic: Internal structure encoding
  outcome: supported
  summary: Saved RDKit 2026.03.5 results regenerate SJSZMXQSCZCGFO-UHFFFAOYSA-N from
    both retained encodings, with formula C72H86ClN9O28, one fragment and formal charge
    zero. Both encodings contain 23 unassigned tetrahedral carbon sites, consistent
    with the retained stereo_complete=false. This establishes encoding consistency,
    not natural absolute configuration.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-CHEM
  - SCI654-NEIGHBORS
- assessment_id: SCI654-DECAPLANINA
  area: evidence
  topic: Named producer and strain context
  outcome: supported
  summary: PMID14742486 explicitly describes DSM44594T producing decaplanin and states
    its type-strain aliases. This supports the named producer/material context of
    the second MIBiG entry and the species-level LOTUS occurrence; it does not verify
    either retained taxon identifier or exact locus.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-DECAPLANINA
  - SCI654-LOCAL
- assessment_id: SCI654-REGIFAUCIUM
  area: evidence
  topic: Separate regifaucium compound claim
  outcome: unknown
  summary: PMID17978218 supplies a kigamicin-producing A. regifaucium taxonomy context
    and no decaplanin assertion in its abstract. Exact compound support must be resolved
    from appropriate primary material or retained entry provenance; neither a wrong
    citation nor a negative species-production claim follows from this omission.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-REGIFAUCIUM
  - SCI654-LOCAL
- assessment_id: SCI654-LOCUS
  area: provenance
  topic: Two distinct retained loci and source grades
  outcome: unknown
  summary: BGC0001459/LOBU02000007.1:259653–327583 and BGC0001460/AOHO01000074.1:276857–343203
    retain SOURCE_ASSERTION and CLUSTER_UNSTATED with blank method fields. Abstract
    producer support does not verify these coordinates or justify silently changing
    either grade.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-DECAPLANINA
  - SCI654-REGIFAUCIUM
- assessment_id: SCI654-SHARED-STRUCTURE
  area: representation
  topic: Open shared-structure question
  outcome: unknown
  summary: The two MIBiG rows store the same stereochemically incomplete structure
    and the owner explicitly retains an OPEN shared-structure discussion. Internal
    full-key agreement does not establish that both biological source entries describe
    one exact natural stereoisomer.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-CHEM
- assessment_id: SCI654-PAPER-SCOPE
  area: provenance
  topic: Production, occurrence and publication independence
  outcome: supported
  summary: Own metadata proves each PMID aliases the corresponding LOTUS DOI. Preserve
    producer and occurrence distinctions, strain/species scope and the two-paper count.
    Taxon equivalence is not inferred from shared names.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-DECAPLANINA
  - SCI654-REGIFAUCIUM
- assessment_id: SCI654-CLASS
  area: representation
  topic: Retained glycopeptide classification
  outcome: supported
  summary: The local NPClassifier glycoside and Vancomycins-and-Teicoplanins filing
    is compatible with the own abstract describing decaplanin as a glycopeptide antibiotic.
    This is broad classification support, not exact connectivity or stereochemical
    verification.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
  - SCI654-DECAPLANINA
- assessment_id: SCI654-ACTIVITY
  area: completeness
  topic: Assay, target and graph coverage
  outcome: unknown
  summary: The empty-AID PubChem row is a no-assay-data sentinel. The owner has no
    quantitative bioactivity, molecular target, pathway step or causal graph; these
    local absences establish neither inactivity nor global absence of such evidence.
  target_ids:
  - naturalproductmech:mibig-de067fa3d6
  evidence_ids:
  - SCI654-LOCAL
findings: []
actions: []
limitations:
- Full primary text/SI and current taxon/structure/sequence authorities were not inspected.
- The retained 23 unassigned tetrahedral carbon sites remain unresolved; parsed InChI
  C(-O)=N flags are a separate representational observation.
- The existing shared-structure discussion and exact regifaucium compound/locus applicability
  remain open; no corrective finding is inferred from abstract omission alone.
- The current official intake reproduces the retained owner and six official source
  arrays. Additional PubChem and supplemental arrays retain their original local-reading
  scope. Baseline and ROOT decisions are bound separately; saved two-encoding computation
  and official intake SMILES computation remain distinct.
- Configured consistency only; independent scientific claim support and unrestricted
  remote authority refresh are not implied.
- Fresh QC attempt001 failed on public canonical-artifact DNS retrieval after lint
  and before downstream tests. Its actual exit1/log/input capture/root observation
  remain pinned; the selected successful canonical QC attempt002 is separately timed.
  No individual-review validation failure or counter reset is claimed.
- 499non-blocking identifier-label warnings,35configured exceptions and4898no-adapter
  skips remain unverified within this gate.
- The QC test suite reported four skipped tests and two dependency deprecation warnings;
  this pass does not assert skipped checks ran.
- Canonical reproduction retains five unresolved assay-organism annotations,42 withheld
  nonsingle-organism producer claims and161 configured taxon-ID rewrites.
- This QC is a configured consistency gate, not an independent primary-source biological
  or stereochemical verification.
- Native baseline gates establish configured consistency, not independent biological
  production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions
  and no-adapter pairs; a successful command does not convert these into verified
  scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command
  execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population
  was checked; external caches and generated bytecode are not asserted to be independently
  byte-pinned.
notes:
- The whole local owner and retained source rows were read. Full-owner scientific
  verification remains false; scientific_review denotes the bounded scientific interpretation
  in this report.
- Original owner/source reading, two-encoding computation, neighbor inspection, HTTP
  retrieval and later metadata reading retain separate clocks. Official intake separately
  computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. No
  corrective finding was established within the inspected evidence; exact-source limitations
  remain explicit.
```
