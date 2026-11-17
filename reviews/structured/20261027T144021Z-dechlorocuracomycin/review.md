# Scientific review of dechlorocuracomycin

- Review: 20261027T144021Z-dechlorocuracomycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T14:38:56.829821Z
- Finished UTC: 2026-10-27T14:40:21.039653Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The own AJOC abstract supports dechlorocuracomycin isolated from S. noursei NBRC15452T and proposed comparative biosynthesis. The stored ATCC11455 producer strain and exact CP011533.1 locus remain separately unverified. Both local encodings agree while retaining two unassigned carbon stereocentres. The earlier curacomycin occurrence concern belongs to a different congener/source claim and is not assigned to this owner.

## Scope And Provenance

Complete retained owner and source-row reading, local encoding checks, and bounded scientific interpretation of inspected publication metadata and supplied abstracts.

Selection: One resolved record in canonical path order from the unreviewed corpus; actual official intake reconciled to retained evidence.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-31c4f73017 | data/natural_products/amino_acids_and_peptides/dechlorocuracomycin.yaml | generated | dechlorocuracomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-31c4f73017 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-31c4f73017 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-31c4f73017 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-31c4f73017 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-31c4f73017 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | naturalproductmech:mibig-31c4f73017 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved local encoding and incomplete stereo | passed | True | naturalproductmech:mibig-31c4f73017 | Saved RDKit 2026.03.5 results regenerate OMJIEOKXBASSMV-IFENFBHBSA-N from both retained encodings, with formula C37H57N9O8, one fragment and formal charge zero. Both encodings contain 2 unassigned tetrahedral carbon sites, consistent with the retained stereo_complete=false. This establishes encoding consistency, not natural absolute configuration. Seven additional unspecified double-bond observations in the parsed InChI representation have saved C(-O)=N neighbor environments. They are not seven additional missing natural C=C configurations; the distinct unassigned tetrahedral carbon sites remain unresolved. |
| Own DOI and congener-resolved abstract | passed | True | naturalproductmech:mibig-31c4f73017 | The own Crossref abstract explicitly pairs dechlorocuracomycin (compound2) with S. noursei NBRC15452T and curacomycin (compound1) with S. curacoi NBRC12761T. It reports MS/NMR structure work and describes proposed clusters and comparative gene-function interpretation, not a stated knockout or heterologous-production experiment. |
| Exact strain equivalence and locus evidence | unavailable | True | naturalproductmech:mibig-31c4f73017 | ATCC11455 in the retained producer claim and NBRC15452T in the abstract have not been checked for equivalence or conflict. The abstract does not independently verify CP011533.1:2863457–2909713/BGC0001569 or an experimental locus method. |
| Exact natural structure and current authority | unavailable | True | naturalproductmech:mibig-31c4f73017 | Full primary/SI, absolute configurations at both unknown carbon sites and current structure/taxon/strain authority records were not verified. |

## Scientific And Domain Assessments

### Internal encoding and explicit incomplete stereo

representation: supported. Targets: naturalproductmech:mibig-31c4f73017.

Saved RDKit 2026.03.5 results regenerate OMJIEOKXBASSMV-IFENFBHBSA-N from both retained encodings, with formula C37H57N9O8, one fragment and formal charge zero. Both encodings contain 2 unassigned tetrahedral carbon sites, consistent with the retained stereo_complete=false. This establishes encoding consistency, not natural absolute configuration. Seven additional unspecified double-bond observations in the parsed InChI representation have saved C(-O)=N neighbor environments. They are not seven additional missing natural C=C configurations; the distinct unassigned tetrahedral carbon sites remain unresolved.

### Exact congener and species pairing at abstract tier

evidence: supported. Targets: naturalproductmech:mibig-31c4f73017.

The abstract identifies compound2 as dechlorocuracomycin isolated from S. noursei NBRC15452T, respectively paired apart from compound1 curacomycin. This supports the present species-level LOTUS occurrence, without resolving the stored producer-strain identifier.

### Producer strain versus occurrence species

provenance: unknown. Targets: naturalproductmech:mibig-31c4f73017.

The MIBiG producer is S. noursei ATCC11455 and the LOTUS occurrence is species-level S. noursei. The abstract uses NBRC15452T. No current strain authority was consulted, so equivalence and conflict are both unestablished.

### Proposed comparative biosynthesis versus experimental proof

evidence: unknown. Targets: naturalproductmech:mibig-31c4f73017.

The abstract calls both clusters proposed and infers functions by comparison. Keep SOURCE_ASSERTION/CLUSTER_UNSTATED and the blank experimental-method field distinct from a verified knockout, complementation or heterologous-production result; exact genome coordinates remain unverified.

### One paper and congener-specific interpretation

provenance: supported. Targets: naturalproductmech:mibig-31c4f73017.

The MIBiG producer/locus and LOTUS occurrence use the same own DOI. Their different citation placements do not supply independent papers. The abstract pairing for dechlorocuracomycin must be read on its own terms; no curacomycin-specific occurrence finding or assay is transferred here.

### Comparative antimicrobial statement

evidence: unknown. Targets: naturalproductmech:mibig-31c4f73017.

The abstract describes a chlorine-dependent comparison, but supplies no exact assay endpoint, value or target here. It does not establish universal inactivity of dechlorocuracomycin, and the retained owner asserts no measured potency or activity.

### Local target and pathway coverage

completeness: unknown. Targets: naturalproductmech:mibig-31c4f73017.

The complete owner has no bioactivity annotations, molecular targets, pathway steps or causal graphs; exact-key PubChem and both supplemental arrays are empty. This is local scope only, not evidence that no published activity or mechanistic information exists.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI655-LOCAL | /private/tmp/npm-review-work/shared-next-batch066-tentative/tentative-owner-source-inventory-001.json; /entries/4/owner_document; /entries/4/rows; /entries/4/supplemental_retained_rows | context_only | The retained dechlorocuracomycin owner joins one MIBiG compound, one LOTUS occurrence and one NPClassifier row; other retained and both supplemental arrays are empty. Producer strain and species-level occurrence are distinct assertions. These local rows do not independently verify natural material or current authority identities. |
| SCI655-CHEM | /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-local-chemical-consistency-001.json; /records/4 | supports | Saved RDKit 2026.03.5 results regenerate OMJIEOKXBASSMV-IFENFBHBSA-N from both retained encodings, with formula C37H57N9O8, one fragment and formal charge zero. Both encodings contain 2 unassigned tetrahedral carbon sites, consistent with the retained stereo_complete=false. This establishes encoding consistency, not natural absolute configuration. |
| SCI655-NEIGHBORS | /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-saved-stereo-neighbor-inspection-001.json; /records/4 | supports | Seven additional unspecified double-bond observations in the parsed InChI representation have saved C(-O)=N neighbor environments. They are not seven additional missing natural C=C configurations; the distinct unassigned tetrahedral carbon sites remain unresolved. |
| SCI655-ABSTRACT | DOI:10.1002/ajoc.201700433; /message/DOI; /message/title; /message/abstract; cached body /private/tmp/npm-review-work/shared-next-batch064-tentative/literature-preparation/public-metadata-001/curacomycin-crossref.json | supports | The own Crossref abstract explicitly pairs dechlorocuracomycin (compound2) with S. noursei NBRC15452T and curacomycin (compound1) with S. curacoi NBRC12761T. It reports MS/NMR structure work and describes proposed clusters and comparative gene-function interpretation, not a stated knockout or heterologous-production experiment. This is own abstract metadata, not full primary/SI. |

## Limits And Additional Notes

- Full primary text/SI and current chemical/taxon/strain/sequence authorities were not inspected.
- Two retained tetrahedral carbon configurations remain unassigned; the separate InChI C(-O)=N flags do not determine natural configurations.
- ATCC11455 versus NBRC15452T and the exact retained locus need independent reconciliation; neither synonymy nor a contradiction is asserted.
- No batch64 finding, congener-specific assay or universal inactivity claim is transferred.
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
review_id: 20261027T144021Z-dechlorocuracomycin
title: Scientific review of dechlorocuracomycin
started_at: '2026-10-27T14:38:56.829821Z'
finished_at: '2026-10-27T14:40:21.039653Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The own AJOC abstract supports dechlorocuracomycin isolated from S. noursei
  NBRC15452T and proposed comparative biosynthesis. The stored ATCC11455 producer
  strain and exact CP011533.1 locus remain separately unverified. Both local encodings
  agree while retaining two unassigned carbon stereocentres. The earlier curacomycin
  occurrence concern belongs to a different congener/source claim and is not assigned
  to this owner.
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
  - path: data/natural_products/amino_acids_and_peptides/dechlorocuracomycin.yaml
    sha256: 5398388f02b306d9204081a36f08883341979c9bcb6416fa492de1e24687c56b
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
- target_id: naturalproductmech:mibig-31c4f73017
  path: data/natural_products/amino_acids_and_peptides/dechlorocuracomycin.yaml
  label: dechlorocuracomycin
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
  description: Complete retained owner and source-row reading, local encoding checks,
    and bounded scientific interpretation of inspected publication metadata and supplied
    abstracts.
  selection: One resolved record in canonical path order from the unreviewed corpus;
    actual official intake reconciled to retained evidence.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-31c4f73017
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
  - naturalproductmech:mibig-31c4f73017
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
  - naturalproductmech:mibig-31c4f73017
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
  - naturalproductmech:mibig-31c4f73017
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
  - naturalproductmech:mibig-31c4f73017
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
  - naturalproductmech:mibig-31c4f73017
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/dechlorocuracomycin.yaml
    --out /private/tmp/npm-review-work/655/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T14:38:58.176086Z. Original
    receipt: /private/tmp/npm-review-work/655/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-31c4f73017
- check_id: SCI655-ENCODING
  name: Saved local encoding and incomplete stereo
  status: passed
  required: true
  summary: Saved RDKit 2026.03.5 results regenerate OMJIEOKXBASSMV-IFENFBHBSA-N from
    both retained encodings, with formula C37H57N9O8, one fragment and formal charge
    zero. Both encodings contain 2 unassigned tetrahedral carbon sites, consistent
    with the retained stereo_complete=false. This establishes encoding consistency,
    not natural absolute configuration. Seven additional unspecified double-bond observations
    in the parsed InChI representation have saved C(-O)=N neighbor environments. They
    are not seven additional missing natural C=C configurations; the distinct unassigned
    tetrahedral carbon sites remain unresolved.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
  - SCI655-CHEM
  - SCI655-NEIGHBORS
- check_id: SCI655-OWN-ABSTRACT
  name: Own DOI and congener-resolved abstract
  status: passed
  required: true
  summary: The own Crossref abstract explicitly pairs dechlorocuracomycin (compound2)
    with S. noursei NBRC15452T and curacomycin (compound1) with S. curacoi NBRC12761T.
    It reports MS/NMR structure work and describes proposed clusters and comparative
    gene-function interpretation, not a stated knockout or heterologous-production
    experiment.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-ABSTRACT
- check_id: SCI655-EXACT-STRAIN-LOCUS
  name: Exact strain equivalence and locus evidence
  status: unavailable
  required: true
  summary: ATCC11455 in the retained producer claim and NBRC15452T in the abstract
    have not been checked for equivalence or conflict. The abstract does not independently
    verify CP011533.1:2863457–2909713/BGC0001569 or an experimental locus method.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
  - SCI655-ABSTRACT
- check_id: SCI655-EXACT-MATERIAL
  name: Exact natural structure and current authority
  status: unavailable
  required: true
  summary: Full primary/SI, absolute configurations at both unknown carbon sites and
    current structure/taxon/strain authority records were not verified.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
  - SCI655-CHEM
  - SCI655-ABSTRACT
evidence:
- evidence_id: SCI655-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch066-tentative/tentative-owner-source-inventory-001.json
  locator: /entries/4/owner_document; /entries/4/rows; /entries/4/supplemental_retained_rows
  accessed_at: '2026-10-27T13:34:04.199112Z'
  snapshot_sha256: efcd8406650fc62eb769ecc575be2ac134e643c8b39c3a750558229786855677
  support: context_only
  summary: The retained dechlorocuracomycin owner joins one MIBiG compound, one LOTUS
    occurrence and one NPClassifier row; other retained and both supplemental arrays
    are empty. Producer strain and species-level occurrence are distinct assertions.
    These local rows do not independently verify natural material or current authority
    identities.
- evidence_id: SCI655-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-local-chemical-consistency-001.json
  locator: /records/4
  accessed_at: '2026-10-27T13:34:17.199424Z'
  snapshot_sha256: 827c0d7bb3ba949b11e8d7cf986fc122b208a34ab2f3e4ba0ff5bbc008a12c6c
  support: supports
  summary: Saved RDKit 2026.03.5 results regenerate OMJIEOKXBASSMV-IFENFBHBSA-N from
    both retained encodings, with formula C37H57N9O8, one fragment and formal charge
    zero. Both encodings contain 2 unassigned tetrahedral carbon sites, consistent
    with the retained stereo_complete=false. This establishes encoding consistency,
    not natural absolute configuration.
- evidence_id: SCI655-NEIGHBORS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch066-tentative/source-science-preparation/root-tentative66-saved-stereo-neighbor-inspection-001.json
  locator: /records/4
  accessed_at: '2026-10-27T13:36:21.405954Z'
  snapshot_sha256: 5de0e2f1788d42f2e02a0b435258acb8805b646d63c184037c0b702f3cf871c6
  support: supports
  summary: Seven additional unspecified double-bond observations in the parsed InChI
    representation have saved C(-O)=N neighbor environments. They are not seven additional
    missing natural C=C configurations; the distinct unassigned tetrahedral carbon
    sites remain unresolved.
- evidence_id: SCI655-ABSTRACT
  kind: primary_source
  reference: DOI:10.1002/ajoc.201700433
  locator: /message/DOI; /message/title; /message/abstract; cached body /private/tmp/npm-review-work/shared-next-batch064-tentative/literature-preparation/public-metadata-001/curacomycin-crossref.json
  accessed_at: '2026-10-27T12:26:57.311028Z'
  snapshot_sha256: 5e39bcad8fc39974d63f0163190dd224c658762d8311daa4bb715dbca4a90e28
  support: supports
  summary: The own Crossref abstract explicitly pairs dechlorocuracomycin (compound2)
    with S. noursei NBRC15452T and curacomycin (compound1) with S. curacoi NBRC12761T.
    It reports MS/NMR structure work and describes proposed clusters and comparative
    gene-function interpretation, not a stated knockout or heterologous-production
    experiment. This is own abstract metadata, not full primary/SI.
assessments:
- assessment_id: SCI655-ENCODING
  area: representation
  topic: Internal encoding and explicit incomplete stereo
  outcome: supported
  summary: Saved RDKit 2026.03.5 results regenerate OMJIEOKXBASSMV-IFENFBHBSA-N from
    both retained encodings, with formula C37H57N9O8, one fragment and formal charge
    zero. Both encodings contain 2 unassigned tetrahedral carbon sites, consistent
    with the retained stereo_complete=false. This establishes encoding consistency,
    not natural absolute configuration. Seven additional unspecified double-bond observations
    in the parsed InChI representation have saved C(-O)=N neighbor environments. They
    are not seven additional missing natural C=C configurations; the distinct unassigned
    tetrahedral carbon sites remain unresolved.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-CHEM
  - SCI655-NEIGHBORS
- assessment_id: SCI655-MATERIAL
  area: evidence
  topic: Exact congener and species pairing at abstract tier
  outcome: supported
  summary: The abstract identifies compound2 as dechlorocuracomycin isolated from
    S. noursei NBRC15452T, respectively paired apart from compound1 curacomycin. This
    supports the present species-level LOTUS occurrence, without resolving the stored
    producer-strain identifier.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-ABSTRACT
  - SCI655-LOCAL
- assessment_id: SCI655-STRAIN
  area: provenance
  topic: Producer strain versus occurrence species
  outcome: unknown
  summary: The MIBiG producer is S. noursei ATCC11455 and the LOTUS occurrence is
    species-level S. noursei. The abstract uses NBRC15452T. No current strain authority
    was consulted, so equivalence and conflict are both unestablished.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
  - SCI655-ABSTRACT
- assessment_id: SCI655-LOCUS
  area: evidence
  topic: Proposed comparative biosynthesis versus experimental proof
  outcome: unknown
  summary: The abstract calls both clusters proposed and infers functions by comparison.
    Keep SOURCE_ASSERTION/CLUSTER_UNSTATED and the blank experimental-method field
    distinct from a verified knockout, complementation or heterologous-production
    result; exact genome coordinates remain unverified.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
  - SCI655-ABSTRACT
- assessment_id: SCI655-PAPER-SCOPE
  area: provenance
  topic: One paper and congener-specific interpretation
  outcome: supported
  summary: The MIBiG producer/locus and LOTUS occurrence use the same own DOI. Their
    different citation placements do not supply independent papers. The abstract pairing
    for dechlorocuracomycin must be read on its own terms; no curacomycin-specific
    occurrence finding or assay is transferred here.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
  - SCI655-ABSTRACT
- assessment_id: SCI655-ACTIVITY
  area: evidence
  topic: Comparative antimicrobial statement
  outcome: unknown
  summary: The abstract describes a chlorine-dependent comparison, but supplies no
    exact assay endpoint, value or target here. It does not establish universal inactivity
    of dechlorocuracomycin, and the retained owner asserts no measured potency or
    activity.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-ABSTRACT
  - SCI655-LOCAL
- assessment_id: SCI655-COVERAGE
  area: completeness
  topic: Local target and pathway coverage
  outcome: unknown
  summary: The complete owner has no bioactivity annotations, molecular targets, pathway
    steps or causal graphs; exact-key PubChem and both supplemental arrays are empty.
    This is local scope only, not evidence that no published activity or mechanistic
    information exists.
  target_ids:
  - naturalproductmech:mibig-31c4f73017
  evidence_ids:
  - SCI655-LOCAL
findings: []
actions: []
limitations:
- Full primary text/SI and current chemical/taxon/strain/sequence authorities were
  not inspected.
- Two retained tetrahedral carbon configurations remain unassigned; the separate InChI
  C(-O)=N flags do not determine natural configurations.
- ATCC11455 versus NBRC15452T and the exact retained locus need independent reconciliation;
  neither synonymy nor a contradiction is asserted.
- No batch64 finding, congener-specific assay or universal inactivity claim is transferred.
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
