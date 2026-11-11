# Coelichelin: consistent free ligand and qualified database-proposed pathway

- Review: 20261027T114857Z-coelichelin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T11:14:19.111415Z
- Finished UTC: 2026-10-27T11:48:57.742338Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Local encodings consistently describe uncomplexed coelichelin, and the SCO0492 graph preserves its limited database-proposed scope. Nature/RSC metadata are bibliography only; the genome abstract cannot verify exact product function or occurrence applicability.

## Scope And Provenance

Original whole local owner/raw snapshot, actual reconciliation, local chemistry consistency and selected own metadata only. Primary material and current authorities remain unverified.

Selection: One resolved record selected in canonical path order from the unreviewed corpus. Complete retained local owner/source arrays were read; scientific claim verification is partial.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:80049 | data/natural_products/amino_acids_and_peptides/coelichelin.yaml | generated | coelichelin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | CHEBI:80049 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | CHEBI:80049 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | CHEBI:80049 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:80049 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:80049 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | CHEBI:80049 | The exact selected owner passed the documented strict validator; this is a configured consistency result. |
| Exact material and primary claim verification | unavailable | True | CHEBI:80049 | Own metadata/abstracts do not supply full primary material, figures and supplements needed for exact compound/strain/function attribution. |
| Current identity authority verification | unavailable | True | CHEBI:80049 | Local consistency was assessed; current chemical/protein/organism authorities and experimental natural stereochemistry were not verified. |

## Scientific And Domain Assessments

### Uncomplexed ligand identity

consistency: supported. Targets: CHEBI:80049.

Owner/MIBiG/retained ChEBI forms agree at full-key/formula level. The free ligand is not a ferric/gallium complex; no metal-complex property or experimental stereochemical validation follows.

### Qualified SCO0492 participation

graph: supported. Targets: CHEBI:80049.

The edge is database-proposed participation; Q9RK14/CAB53322.1 is a reference sequence, not an inspected assay construct. Retain exclusions of exact substrates, module order/iteration, release and stereoselectivity. No Cch alias or experimental upgrade.

### Producer/BGC evidence grade

evidence: unknown. Targets: CHEBI:80049.

BGC0000325 retains SOURCE_ASSERTION and CLUSTER_UNSTATED, empty locus methods, questionable quality and unknown completeness. The genome abstract supplies organism/sequence context, not compound-specific function.

### Occurrence and citation limits

scope: unknown. Targets: CHEBI:80049.

Fifteen LOTUS rows and1 ChEBI origin remain occurrence assertions. Title-only records cannot verify all species/material placements. Explicit owner PMID21342472 remains uninspected; raw bare21342472 is not independently namespace-verified.

### Blank assay sentinel

scope: supported. Targets: CHEBI:80049.

The extra PubChem row has no AID, outcome or measurement: it is not an assay. No pure-compound potency, metal-complex activity or absence of biological activity follows.

### Computed peptide classification

provenance: supported. Targets: CHEBI:80049.

ChEBI says tetrapeptide; NPClassifier supplies a computed Tripeptides label. Preserve asserted-versus-computed provenance; this alone establishes no molecular-graph or identity defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-LOCAL | /private/tmp/npm-review-work/shared-next-batch063-tentative/tentative-owner-source-inventory-001.json; /entries/6/owner_document and /entries/6/rows | supports | Whole owner and seven retained sets contain20 rows; six official sets contain19. One extra PubChem row has blank AID and no measurement. The owner has one two-node/one-edge SCO0492 graph explicitly limited to database-proposed participation. |
| E-CHEM | /private/tmp/npm-review-work/shared-next-batch063-tentative/source-science-preparation/root-tentative63-local-chemical-consistency-001.json; /records/6; scope addendum /private/tmp/npm-review-work/shared-next-batch063-tentative/source-science-preparation/root-tentative63-chemical-computation-reading-and-tautomer-scope-001.json | supports | SMILES, Standard InChI and retained ChEBI alternative reproduce ZPJLQAOTGYKOBJ-OVYGPGRDSA-N and C21H39N7O11. This represents the uncomplexed ligand. InChI tautomeric double-bond flags alone do not establish a missing natural stereochemical assignment. |
| E-NATURE-BIB | DOI:10.1038/nchembio731; /message in /private/tmp/npm-review-work/shared-next-batch063/literature-preparation/public-metadata-001/metadata-d4127cb837b8.json | context_only | Own bibliography identifies a S. coelicolor genome-mining natural-product paper; current Crossref supplies no abstract. Historical subscription-preview notes are not newly inspected experiments. |
| E-RSC-BIB | DOI:10.1039/b801016a; /message in /private/tmp/npm-review-work/shared-next-batch063/literature-preparation/public-metadata-001/metadata-8daf522b6ecc.json | context_only | Own bibliography identifies ornithine hydroxylation during coelichelin biosynthesis; current Crossref supplies no abstract. Historical abstract-only landing-page notes are not a new abstract or primary-body read. |
| E-GENOME | PMID:12000953; ./PubmedArticle[2]/MedlineCitation/Article, own PMID12000953 in /private/tmp/npm-review-work/shared-next-batch032/review-support/public-002/primary-pubmed.xml | context_only | The retained S. coelicolor A3(2) genome abstract describes known/predicted secondary-metabolite clusters. It does not establish exact coelichelin product, SCO0492 function, substrates, module order or experimental methods. Original October22 HTTP and October27 local-read clocks remain separate. |

## Limits And Additional Notes

- Nature/RSC current bodies are bibliography only; historical preview/abstract notes are not new primary inspections. No figures, supplements or assay constructs were verified.
- The genome abstract does not verify exact coelichelin/SCO0492 function. Current UniProt/ENA/chemical authorities and old curated sequence claims were not reverified.
- Free ligand, ferric/gallium complexes, occurrence assertions and blank sentinel remain distinct. Empty findings mean no corrective defect established in this partial scope.
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
- The entire local owner and retained source rows were read. Full-owner scientific verification remains false; scientific_review denotes only the bounded interpretation explicitly described in evidence and assessments.
- Original local source reading, HTTP retrieval and local computation times are retained separately in the cited evidence and authoring provenance. Earlier readings are reused; the start/finish fields bound the actual review intake and final adjudication.
- No scientific record, maintained input or native curation status was changed. Empty findings mean no corrective defect was established in this partial scope.

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
review_id: 20261027T114857Z-coelichelin
title: 'Coelichelin: consistent free ligand and qualified database-proposed pathway'
started_at: '2026-10-27T11:14:19.111415Z'
finished_at: '2026-10-27T11:48:57.742338Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Local encodings consistently describe uncomplexed coelichelin, and the SCO0492
  graph preserves its limited database-proposed scope. Nature/RSC metadata are bibliography
  only; the genome abstract cannot verify exact product function or occurrence applicability.
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
  - path: data/natural_products/amino_acids_and_peptides/coelichelin.yaml
    sha256: d86da6d63d2400cc3edd706c10cf1350b9fb9d5042d583231c485a4aa2e07c31
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
- target_id: CHEBI:80049
  path: data/natural_products/amino_acids_and_peptides/coelichelin.yaml
  label: coelichelin
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
    path: data/natural_products/amino_acids_and_peptides/coelichelin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
scope:
  description: Original whole local owner/raw snapshot, actual reconciliation, local
    chemistry consistency and selected own metadata only. Primary material and current
    authorities remain unverified.
  selection: One resolved record selected in canonical path order from the unreviewed
    corpus. Complete retained local owner/source arrays were read; scientific claim
    verification is partial.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:80049
  exclusions:
  - target: Full primary material and current external authorities
    reason: Available evidence is limited to the cited own metadata/abstracts and
      local source/representation checks; exact unresolved claims remain listed below.
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
    Reused for batch063 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch063. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:80049
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
    Reused for batch063 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch063. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:80049
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
    Reused for batch063 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch063. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:80049
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
    Reused for batch063 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch063. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:80049
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
    Reused for batch063 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch063. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:80049
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The exact selected owner passed the documented strict validator; this is
    a configured consistency result.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/coelichelin.yaml
    --out /private/tmp/npm-review-work/627/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual target intake execution finished 2026-10-27T11:14:20.457996Z.
    Original receipt: /private/tmp/npm-review-work/627/strict-receipt.json.'
  target_ids:
  - CHEBI:80049
- check_id: C-PRIMARY-SCOPE
  name: Exact material and primary claim verification
  status: unavailable
  required: true
  summary: Own metadata/abstracts do not supply full primary material, figures and
    supplements needed for exact compound/strain/function attribution.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-NATURE-BIB
  - E-RSC-BIB
  - E-GENOME
- check_id: C-AUTHORITY-SCOPE
  name: Current identity authority verification
  status: unavailable
  required: true
  summary: Local consistency was assessed; current chemical/protein/organism authorities
    and experimental natural stereochemistry were not verified.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
  - E-CHEM
evidence:
- evidence_id: E-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch063-tentative/tentative-owner-source-inventory-001.json
  locator: /entries/6/owner_document and /entries/6/rows
  accessed_at: '2026-10-27T10:19:57.540835Z'
  snapshot_sha256: 0c08e787a64f4c41a491ec047e16a6187eb7d4fe517516bb00536ac322f87fc8
  support: supports
  summary: Whole owner and seven retained sets contain20 rows; six official sets contain19.
    One extra PubChem row has blank AID and no measurement. The owner has one two-node/one-edge
    SCO0492 graph explicitly limited to database-proposed participation.
- evidence_id: E-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch063-tentative/source-science-preparation/root-tentative63-local-chemical-consistency-001.json
  locator: /records/6; scope addendum /private/tmp/npm-review-work/shared-next-batch063-tentative/source-science-preparation/root-tentative63-chemical-computation-reading-and-tautomer-scope-001.json
  accessed_at: '2026-10-27T10:51:33.569411Z'
  snapshot_sha256: 25c46d465e6c3c9b924bb2faa3905a61ca2259abc288a1bab7360952c31c9881
  support: supports
  summary: SMILES, Standard InChI and retained ChEBI alternative reproduce ZPJLQAOTGYKOBJ-OVYGPGRDSA-N
    and C21H39N7O11. This represents the uncomplexed ligand. InChI tautomeric double-bond
    flags alone do not establish a missing natural stereochemical assignment.
- evidence_id: E-NATURE-BIB
  kind: database
  reference: DOI:10.1038/nchembio731
  locator: /message in /private/tmp/npm-review-work/shared-next-batch063/literature-preparation/public-metadata-001/metadata-d4127cb837b8.json
  accessed_at: '2026-10-27T11:40:11.530190Z'
  snapshot_sha256: acdf2e7dea2ddbb498db34688fa6524054709c14b2df7acdde04d7c4e96baaac
  support: context_only
  summary: Own bibliography identifies a S. coelicolor genome-mining natural-product
    paper; current Crossref supplies no abstract. Historical subscription-preview
    notes are not newly inspected experiments.
- evidence_id: E-RSC-BIB
  kind: database
  reference: DOI:10.1039/b801016a
  locator: /message in /private/tmp/npm-review-work/shared-next-batch063/literature-preparation/public-metadata-001/metadata-8daf522b6ecc.json
  accessed_at: '2026-10-27T11:40:11.530190Z'
  snapshot_sha256: e277275db2d65958e158e988f82c3c473928f2ca98c10d731f1fcf8f2495306e
  support: context_only
  summary: Own bibliography identifies ornithine hydroxylation during coelichelin
    biosynthesis; current Crossref supplies no abstract. Historical abstract-only
    landing-page notes are not a new abstract or primary-body read.
- evidence_id: E-GENOME
  kind: primary_source
  reference: PMID:12000953
  locator: ./PubmedArticle[2]/MedlineCitation/Article, own PMID12000953 in /private/tmp/npm-review-work/shared-next-batch032/review-support/public-002/primary-pubmed.xml
  accessed_at: '2026-10-27T10:40:16.143444Z'
  snapshot_sha256: 18e163b12774c629142741de48e96ff227ed60100fff3f6a2e80853bdf11f610
  support: context_only
  summary: The retained S. coelicolor A3(2) genome abstract describes known/predicted
    secondary-metabolite clusters. It does not establish exact coelichelin product,
    SCO0492 function, substrates, module order or experimental methods. Original October22
    HTTP and October27 local-read clocks remain separate.
assessments:
- assessment_id: A-IDENTITY
  area: consistency
  topic: Uncomplexed ligand identity
  outcome: supported
  summary: Owner/MIBiG/retained ChEBI forms agree at full-key/formula level. The free
    ligand is not a ferric/gallium complex; no metal-complex property or experimental
    stereochemical validation follows.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
  - E-CHEM
- assessment_id: A-GRAPH
  area: graph
  topic: Qualified SCO0492 participation
  outcome: supported
  summary: The edge is database-proposed participation; Q9RK14/CAB53322.1 is a reference
    sequence, not an inspected assay construct. Retain exclusions of exact substrates,
    module order/iteration, release and stereoselectivity. No Cch alias or experimental
    upgrade.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
  - E-NATURE-BIB
  - E-RSC-BIB
- assessment_id: A-PRODUCER
  area: evidence
  topic: Producer/BGC evidence grade
  outcome: unknown
  summary: BGC0000325 retains SOURCE_ASSERTION and CLUSTER_UNSTATED, empty locus methods,
    questionable quality and unknown completeness. The genome abstract supplies organism/sequence
    context, not compound-specific function.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
  - E-GENOME
- assessment_id: A-OCCURRENCE
  area: scope
  topic: Occurrence and citation limits
  outcome: unknown
  summary: Fifteen LOTUS rows and1 ChEBI origin remain occurrence assertions. Title-only
    records cannot verify all species/material placements. Explicit owner PMID21342472
    remains uninspected; raw bare21342472 is not independently namespace-verified.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
  - E-NATURE-BIB
  - E-RSC-BIB
  - E-GENOME
- assessment_id: A-ACTIVITY
  area: scope
  topic: Blank assay sentinel
  outcome: supported
  summary: 'The extra PubChem row has no AID, outcome or measurement: it is not an
    assay. No pure-compound potency, metal-complex activity or absence of biological
    activity follows.'
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
- assessment_id: A-FILING
  area: provenance
  topic: Computed peptide classification
  outcome: supported
  summary: ChEBI says tetrapeptide; NPClassifier supplies a computed Tripeptides label.
    Preserve asserted-versus-computed provenance; this alone establishes no molecular-graph
    or identity defect.
  target_ids:
  - CHEBI:80049
  evidence_ids:
  - E-LOCAL
  - E-CHEM
findings: []
actions: []
limitations:
- Nature/RSC current bodies are bibliography only; historical preview/abstract notes
  are not new primary inspections. No figures, supplements or assay constructs were
  verified.
- The genome abstract does not verify exact coelichelin/SCO0492 function. Current
  UniProt/ENA/chemical authorities and old curated sequence claims were not reverified.
- Free ligand, ferric/gallium complexes, occurrence assertions and blank sentinel
  remain distinct. Empty findings mean no corrective defect established in this partial
  scope.
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
- The entire local owner and retained source rows were read. Full-owner scientific
  verification remains false; scientific_review denotes only the bounded interpretation
  explicitly described in evidence and assessments.
- Original local source reading, HTTP retrieval and local computation times are retained
  separately in the cited evidence and authoring provenance. Earlier readings are
  reused; the start/finish fields bound the actual review intake and final adjudication.
- No scientific record, maintained input or native curation status was changed. Empty
  findings mean no corrective defect was established in this partial scope.
```
