# Scientific review of echinocandin B

- Review: 20261027T164530Z-echinocandin-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T16:43:07.722934Z
- Finished UTC: 2026-10-27T16:45:30.898482Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Echinocandin B has internally consistent retained encodings and historical abstract-level isolation support. Taxon/strain correspondence, the tentative historical formula and Streptomyces deacylation citation remain source-applicability limits, without an established corrective finding.

## Scope And Provenance

Bounded source and representation review of echinocandin B using retained owner/raw rows and supplemental sibling assertion, saved encoding diagnostics, the historical isolation abstract and later cluster/deacylation titles. Tentative historical formula, native occurrence and substrate biotransformation remain separate questions.

Selection: One exact owner record: data/natural_products/amino_acids_and_peptides/echinocandin-b.yaml (CHEBI:315018); retained source assertions, saved diagnostics and inspected own-source material are assessed at their individual evidence scopes.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:315018 | data/natural_products/amino_acids_and_peptides/echinocandin-b.yaml | generated | echinocandin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | CHEBI:315018 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | CHEBI:315018 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | CHEBI:315018 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:315018 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:315018 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | CHEBI:315018 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved encoding consistency | passed | True | CHEBI:315018 | Saved RDKit2026.03.5 results regenerate FAUOJMHVEYMQQG-HVYQDZECSA-N from both retained encodings, with formula C52H81N7O16, 1 fragment and net formal charge 0. This supports internal encoding consistency only, not experimental natural identity. Both owner encodings and retained CHEBI:315018 alternate SMILES regenerate the same full key/formula. No unspecified tetrahedral center is reported; five InChI C(-O)=N flags are imidic contexts. Internal O16 encoding agreement does not adjudicate the historical tentative O18 report or natural material. |
| Historical structure and taxon correspondence | unavailable | True | CHEBI:315018 | The 1974 formula is explicitly tentative; O18 versus retained O16 does not establish a wrong current structure. A32204, NRRL8112 and the LOTUS A. spinulosporus label are not equated without exact evidence. |
| Streptomyces occurrence applicability | unavailable | True | CHEBI:315018 | The title raises a substrate-versus-occurrence question, but methods/material evidence is unavailable. No claim that Streptomyces cannot produce echinocandin B, or that the stored occurrence is false, is established. |
| Current chemical, taxon and source authority applicability | unavailable | True | CHEBI:315018 | No current chemical, protein, taxon, sequence or database-authority query was made. Retained names, groundings and accessions are not newly verified authority facts. |

## Scientific And Domain Assessments

### Internal chemical encoding

representation: supported. Targets: CHEBI:315018.

Saved RDKit2026.03.5 results regenerate FAUOJMHVEYMQQG-HVYQDZECSA-N from both retained encodings, with formula C52H81N7O16, 1 fragment and net formal charge 0. This supports internal encoding consistency only, not experimental natural identity.

### Encoded stereo and chemical-form boundary

representation: supported. Targets: CHEBI:315018.

Both owner encodings and retained CHEBI:315018 alternate SMILES regenerate the same full key/formula. No unspecified tetrahedral center is reported; five InChI C(-O)=N flags are imidic contexts. Internal O16 encoding agreement does not adjudicate the historical tentative O18 report or natural material.

### Historical named-component isolation

evidence: supported. Targets: CHEBI:315018.

The own abstract directly reports isolation/separation of echinocandin B and anti-yeast activity in its stated historical material context. Exact current structure and taxonomy remain separate.

### Tentative historical molecular formula

representation: unknown. Targets: CHEBI:315018.

C52H81N7O18 is labelled tentative in the historical abstract, while retained/computed encodings use C52H81N7O16. This documented difference calls for primary/authority reconciliation, not an automatic replacement or wrong-structure finding.

### Isolate and genomic evidence scope

provenance: unknown. Targets: CHEBI:315018.

The 1974 reference is retained at COMPOUND_BIOACTIVITY level; it does not establish KT806042.1. The 2016 title is relevant but does not validate the whole locus or current fungal synonymy. CLUSTER_UNSTATED remains unchanged.

### Biotransformation versus occurrence

provenance: unknown. Targets: CHEBI:315018.

Whether the Streptomyces study used supplied substrate or also demonstrated native occurrence is unresolved. The title alone is insufficient to adjudicate the LOTUS organism association.

### Blank assay sentinel and linked antifungal class

evidence: unknown. Targets: CHEBI:315018.

The blank-AID row is not an assay result. The exact-key sibling ANTIFUNGAL assertion is retained with its original provenance, not a newly inspected endpoint or molecular mechanism. Broad historical anti-yeast support does not create a quantitative assay.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI679-LOCAL | /private/tmp/npm-review-work/shared-next-batch068-tentative/tentative-owner-source-inventory-001.json; /entries/8/owner_document; /entries/8/rows; /entries/8/supplemental_retained_rows | context_only | Seven retained rows include one blank-AID PubChem sentinel, not an assay observation. One supplemental exact-key AntibioticMech row supports the pinned sibling link and ANTIFUNGAL summary only. MIBiG BGC0001371/KT806042.1 remains SOURCE_ASSERTION/CLUSTER_UNSTATED; three LOTUS fungal/genus occurrences are separate. |
| SCI679-CHEM | /private/tmp/npm-review-work/shared-next-batch068-tentative/source-science-preparation/native-tentative68-local-chemical-consistency-and-neighbors-001.json; /records/8 | supports | Saved RDKit2026.03.5 results regenerate FAUOJMHVEYMQQG-HVYQDZECSA-N from both retained encodings, with formula C52H81N7O16, 1 fragment and net formal charge 0. This supports internal encoding consistency only, not experimental natural identity. |
| SCI679-NEIGHBORS | /private/tmp/npm-review-work/shared-next-batch068-tentative/source-science-preparation/native-tentative68-chemical-neighbor-interpretation-own-postwrite-001.json; /records/8 | supports | Both owner encodings and retained CHEBI:315018 alternate SMILES regenerate the same full key/formula. No unspecified tetrahedral center is reported; five InChI C(-O)=N flags are imidic contexts. Internal O16 encoding agreement does not adjudicate the historical tentative O18 report or natural material. |
| SCI679-HISTORICAL | DOI:10.1002/hlca.19740570818; /message/DOI; /message/title; /message/abstract; saved body /private/tmp/npm-review-work/shared-next-batch068-tentative/literature-preparation/public-metadata-crossref-001/doi-4e5218e46e01.json | supports | The own historical abstract reports an echinocandin complex from A. nidulans var. echinulatus A32204, separation of component B, anti-yeast activity and a tentative C52H81N7O18 formula. It describes spectra and hydrolysis products but does not provide those data here. |
| SCI679-CLUSTER-TITLE | DOI:10.1186/s12864-016-2885-x; /message/DOI; /message/title; /message/abstract (not supplied); saved body /private/tmp/npm-review-work/shared-next-batch068-tentative/literature-preparation/public-metadata-crossref-001/doi-61164e24c700.json | partial | The own title names an echinocandin B cluster in A. nidulans NRRL8112 and reassembly of Ecd/Hty subclusters from A. pachycristatus NRRL11440. No abstract was supplied; exact genomic boundaries and current taxonomy remain unverified. |
| SCI679-DEACYLATION | DOI:10.1007/s13205-019-1946-7; /message/DOI; /message/title; /message/abstract (not supplied); saved body /private/tmp/npm-review-work/shared-next-batch068-tentative/literature-preparation/public-metadata-crossref-001/doi-e36aa6f78768.json | partial | The own title describes deacylation of echinocandin B by Streptomyces to produce the echinocandin B nucleus. No abstract was supplied. Substrate biotransformation, product nucleus and native compound occurrence must remain separate. |

## Limits And Additional Notes

- The 1974 own abstract and two later own titles were inspected; full primary methods/materials, strain taxonomy and complete structural evidence remain unavailable.
- The supplemental sibling link and imported assay sentinel are not promoted to new experimental verification.
- Internal encoding agreement does not establish the exact natural stereoisomer, source-material identity or current authority correctness.
- Full-owner scientific verification remains false. Original local-reading, saved-computation, source-access and own-field reading clocks stay separate. Actual intake reconciliation verifies reproduction of the whole owner and six official arrays only; it adds no primary evidence or current authority verification.
- Configured consistency only; independent scientific claim support and unrestricted remote authority refresh are not implied.
- FailedQC001 is retained for an explicit separate network-enabled retry; no artifact will be overwritten.
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
- No scientific record, maintained input or native curation status was changed. Any findings and actions record ROOT-adopted proposed work; exact-source limitations and unavailable checks remain explicit.

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
review_id: 20261027T164530Z-echinocandin-b
title: Scientific review of echinocandin B
started_at: '2026-10-27T16:43:07.722934Z'
finished_at: '2026-10-27T16:45:30.898482Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Echinocandin B has internally consistent retained encodings and historical
  abstract-level isolation support. Taxon/strain correspondence, the tentative historical
  formula and Streptomyces deacylation citation remain source-applicability limits,
  without an established corrective finding.
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
  - path: data/natural_products/amino_acids_and_peptides/echinocandin-b.yaml
    sha256: 41d07f70bdcd4957247c79d97002e1f5a0e368007a98b6df75bdb8ce26a9c8fb
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
- target_id: CHEBI:315018
  path: data/natural_products/amino_acids_and_peptides/echinocandin-b.yaml
  label: echinocandin B
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
scope:
  description: Bounded source and representation review of echinocandin B using retained
    owner/raw rows and supplemental sibling assertion, saved encoding diagnostics,
    the historical isolation abstract and later cluster/deacylation titles. Tentative
    historical formula, native occurrence and substrate biotransformation remain separate
    questions.
  selection: 'One exact owner record: data/natural_products/amino_acids_and_peptides/echinocandin-b.yaml
    (CHEBI:315018); retained source assertions, saved diagnostics and inspected own-source
    material are assessed at their individual evidence scopes.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:315018
  exclusions:
  - reason: Historical O18 is tentative, taxon/strain correspondence remains unresolved
      and the deacylation title alone does not establish native parent occurrence.
    target: Current fungal taxonomy, historical material and native Streptomyces occurrence
  - reason: The blank-AID row and imported ANTIFUNGAL sibling assertion do not establish
      a newly inspected quantitative endpoint or molecular mechanism.
    target: New assay or mechanism from a sentinel/sibling link
  - reason: No current chemical, protein, taxon or sequence authority query was made;
      saved encoding agreement and inspected source excerpts do not establish complete
      natural identity.
    target: Current external authorities and full-owner scientific verification
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
    Reused for batch068 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch068. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:315018
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
    Reused for batch068 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch068. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:315018
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
    Reused for batch068 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch068. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:315018
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
    Reused for batch068 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch068. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:315018
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
    Reused for batch068 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch068. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:315018
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/echinocandin-b.yaml
    --out /private/tmp/npm-review-work/679/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T16:43:09.057895Z. Original
    receipt: /private/tmp/npm-review-work/679/strict-receipt.json.'
  target_ids:
  - CHEBI:315018
- check_id: SCI679-ENCODING
  name: Saved encoding consistency
  status: passed
  required: true
  summary: Saved RDKit2026.03.5 results regenerate FAUOJMHVEYMQQG-HVYQDZECSA-N from
    both retained encodings, with formula C52H81N7O16, 1 fragment and net formal charge
    0. This supports internal encoding consistency only, not experimental natural
    identity. Both owner encodings and retained CHEBI:315018 alternate SMILES regenerate
    the same full key/formula. No unspecified tetrahedral center is reported; five
    InChI C(-O)=N flags are imidic contexts. Internal O16 encoding agreement does
    not adjudicate the historical tentative O18 report or natural material.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-CHEM
  - SCI679-NEIGHBORS
- check_id: SCI679-HISTORICAL-IDENTITY
  name: Historical structure and taxon correspondence
  status: unavailable
  required: true
  summary: The 1974 formula is explicitly tentative; O18 versus retained O16 does
    not establish a wrong current structure. A32204, NRRL8112 and the LOTUS A. spinulosporus
    label are not equated without exact evidence.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-CHEM
  - SCI679-HISTORICAL
  - SCI679-CLUSTER-TITLE
- check_id: SCI679-STREPTOMYCES
  name: Streptomyces occurrence applicability
  status: unavailable
  required: true
  summary: The title raises a substrate-versus-occurrence question, but methods/material
    evidence is unavailable. No claim that Streptomyces cannot produce echinocandin
    B, or that the stored occurrence is false, is established.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-DEACYLATION
- check_id: SCI679-AUTHORITIES
  name: Current chemical, taxon and source authority applicability
  status: unavailable
  required: true
  summary: No current chemical, protein, taxon, sequence or database-authority query
    was made. Retained names, groundings and accessions are not newly verified authority
    facts.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-CHEM
evidence:
- evidence_id: SCI679-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch068-tentative/tentative-owner-source-inventory-001.json
  locator: /entries/8/owner_document; /entries/8/rows; /entries/8/supplemental_retained_rows
  accessed_at: '2026-10-27T15:46:38.869152Z'
  snapshot_sha256: a82b42a6a2e5c8fb871d2f3c98a92fe8ea8defc2232239a546e8b7b04e39be93
  support: context_only
  summary: Seven retained rows include one blank-AID PubChem sentinel, not an assay
    observation. One supplemental exact-key AntibioticMech row supports the pinned
    sibling link and ANTIFUNGAL summary only. MIBiG BGC0001371/KT806042.1 remains
    SOURCE_ASSERTION/CLUSTER_UNSTATED; three LOTUS fungal/genus occurrences are separate.
- evidence_id: SCI679-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch068-tentative/source-science-preparation/native-tentative68-local-chemical-consistency-and-neighbors-001.json
  locator: /records/8
  accessed_at: '2026-10-27T15:37:22.840055Z'
  snapshot_sha256: 9edf8da64ee0aa2345523558cd637f65d11800039f7fc7f7712a1fff471b9abb
  support: supports
  summary: Saved RDKit2026.03.5 results regenerate FAUOJMHVEYMQQG-HVYQDZECSA-N from
    both retained encodings, with formula C52H81N7O16, 1 fragment and net formal charge
    0. This supports internal encoding consistency only, not experimental natural
    identity.
- evidence_id: SCI679-NEIGHBORS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch068-tentative/source-science-preparation/native-tentative68-chemical-neighbor-interpretation-own-postwrite-001.json
  locator: /records/8
  accessed_at: '2026-10-27T15:38:23.219966Z'
  snapshot_sha256: 3930bf022054ad0ef8016fcd35d382cc80574979054ec24aa5439264d641c829
  support: supports
  summary: Both owner encodings and retained CHEBI:315018 alternate SMILES regenerate
    the same full key/formula. No unspecified tetrahedral center is reported; five
    InChI C(-O)=N flags are imidic contexts. Internal O16 encoding agreement does
    not adjudicate the historical tentative O18 report or natural material.
- evidence_id: SCI679-HISTORICAL
  kind: primary_source
  reference: DOI:10.1002/hlca.19740570818
  locator: /message/DOI; /message/title; /message/abstract; saved body /private/tmp/npm-review-work/shared-next-batch068-tentative/literature-preparation/public-metadata-crossref-001/doi-4e5218e46e01.json
  accessed_at: '2026-10-27T16:16:17.976553Z'
  snapshot_sha256: fc5b5085cbad0ce38e9948d03363a8bb0c1aafee72c576057f31c6ba0e87ebd1
  support: supports
  summary: The own historical abstract reports an echinocandin complex from A. nidulans
    var. echinulatus A32204, separation of component B, anti-yeast activity and a
    tentative C52H81N7O18 formula. It describes spectra and hydrolysis products but
    does not provide those data here.
- evidence_id: SCI679-CLUSTER-TITLE
  kind: database
  reference: DOI:10.1186/s12864-016-2885-x
  locator: /message/DOI; /message/title; /message/abstract (not supplied); saved body
    /private/tmp/npm-review-work/shared-next-batch068-tentative/literature-preparation/public-metadata-crossref-001/doi-61164e24c700.json
  accessed_at: '2026-10-27T16:16:17.976553Z'
  snapshot_sha256: b5029ef84a354e106fd2e1733c665f4b69330537e23ac35d87ee590f74ee1635
  support: partial
  summary: The own title names an echinocandin B cluster in A. nidulans NRRL8112 and
    reassembly of Ecd/Hty subclusters from A. pachycristatus NRRL11440. No abstract
    was supplied; exact genomic boundaries and current taxonomy remain unverified.
- evidence_id: SCI679-DEACYLATION
  kind: database
  reference: DOI:10.1007/s13205-019-1946-7
  locator: /message/DOI; /message/title; /message/abstract (not supplied); saved body
    /private/tmp/npm-review-work/shared-next-batch068-tentative/literature-preparation/public-metadata-crossref-001/doi-e36aa6f78768.json
  accessed_at: '2026-10-27T16:16:17.976553Z'
  snapshot_sha256: 05b8c1772aff6cd514af950556a05d10d353d40fa682d759abf7adb4b3f26cc7
  support: partial
  summary: The own title describes deacylation of echinocandin B by Streptomyces to
    produce the echinocandin B nucleus. No abstract was supplied. Substrate biotransformation,
    product nucleus and native compound occurrence must remain separate.
assessments:
- assessment_id: SCI679-ENCODING
  area: representation
  topic: Internal chemical encoding
  outcome: supported
  summary: Saved RDKit2026.03.5 results regenerate FAUOJMHVEYMQQG-HVYQDZECSA-N from
    both retained encodings, with formula C52H81N7O16, 1 fragment and net formal charge
    0. This supports internal encoding consistency only, not experimental natural
    identity.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-CHEM
- assessment_id: SCI679-STEREO
  area: representation
  topic: Encoded stereo and chemical-form boundary
  outcome: supported
  summary: Both owner encodings and retained CHEBI:315018 alternate SMILES regenerate
    the same full key/formula. No unspecified tetrahedral center is reported; five
    InChI C(-O)=N flags are imidic contexts. Internal O16 encoding agreement does
    not adjudicate the historical tentative O18 report or natural material.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-CHEM
  - SCI679-NEIGHBORS
  - SCI679-LOCAL
- assessment_id: SCI679-ISOLATION
  area: evidence
  topic: Historical named-component isolation
  outcome: supported
  summary: The own abstract directly reports isolation/separation of echinocandin
    B and anti-yeast activity in its stated historical material context. Exact current
    structure and taxonomy remain separate.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-HISTORICAL
- assessment_id: SCI679-FORMULA
  area: representation
  topic: Tentative historical molecular formula
  outcome: unknown
  summary: C52H81N7O18 is labelled tentative in the historical abstract, while retained/computed
    encodings use C52H81N7O16. This documented difference calls for primary/authority
    reconciliation, not an automatic replacement or wrong-structure finding.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-CHEM
  - SCI679-HISTORICAL
- assessment_id: SCI679-TAXON-LOCUS
  area: provenance
  topic: Isolate and genomic evidence scope
  outcome: unknown
  summary: The 1974 reference is retained at COMPOUND_BIOACTIVITY level; it does not
    establish KT806042.1. The 2016 title is relevant but does not validate the whole
    locus or current fungal synonymy. CLUSTER_UNSTATED remains unchanged.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-HISTORICAL
  - SCI679-CLUSTER-TITLE
- assessment_id: SCI679-OCCURRENCE
  area: provenance
  topic: Biotransformation versus occurrence
  outcome: unknown
  summary: Whether the Streptomyces study used supplied substrate or also demonstrated
    native occurrence is unresolved. The title alone is insufficient to adjudicate
    the LOTUS organism association.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-DEACYLATION
- assessment_id: SCI679-ASSAY-SIBLING
  area: evidence
  topic: Blank assay sentinel and linked antifungal class
  outcome: unknown
  summary: The blank-AID row is not an assay result. The exact-key sibling ANTIFUNGAL
    assertion is retained with its original provenance, not a newly inspected endpoint
    or molecular mechanism. Broad historical anti-yeast support does not create a
    quantitative assay.
  target_ids:
  - CHEBI:315018
  evidence_ids:
  - SCI679-LOCAL
  - SCI679-HISTORICAL
findings: []
actions: []
limitations:
- The 1974 own abstract and two later own titles were inspected; full primary methods/materials,
  strain taxonomy and complete structural evidence remain unavailable.
- The supplemental sibling link and imported assay sentinel are not promoted to new
  experimental verification.
- Internal encoding agreement does not establish the exact natural stereoisomer, source-material
  identity or current authority correctness.
- Full-owner scientific verification remains false. Original local-reading, saved-computation,
  source-access and own-field reading clocks stay separate. Actual intake reconciliation
  verifies reproduction of the whole owner and six official arrays only; it adds no
  primary evidence or current authority verification.
- Configured consistency only; independent scientific claim support and unrestricted
  remote authority refresh are not implied.
- FailedQC001 is retained for an explicit separate network-enabled retry; no artifact
  will be overwritten.
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
- No scientific record, maintained input or native curation status was changed. Any
  findings and actions record ROOT-adopted proposed work; exact-source limitations
  and unavailable checks remain explicit.
```
