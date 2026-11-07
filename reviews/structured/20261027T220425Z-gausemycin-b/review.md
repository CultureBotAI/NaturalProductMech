# Scientific review of gausemycin B

- Review: 20261027T220425Z-gausemycin-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T22:00:57.436139Z
- Finished UTC: 2026-10-27T22:04:25.381156Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Gausemycin B has a distinct, internally consistent C87H121ClN18O29 encoding and six unresolved carbon stereocentres. Its own abstract supports named A/B isolation and shared biological context; exact B-specific structure, strain/locus and quantitative mechanism claims remain limited. The model-derived RiPPs-Lasso label is separate from the MIBiG NRPS/SACCHARIDE source classes.

## Scope And Provenance

Bounded assessment of the original gausemycin B owner and exact retained source rows, saved chemical encoding consistency, own PubMed title/abstract/identifiers and the precise source-access limits.

Selection: One exact record selected in canonical repository path order from the unreviewed population; this observation assesses only its declared partial scientific scope.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-d010e4d4d2 | data/natural_products/amino_acids_and_peptides/gausemycin-b.yaml | generated | gausemycin B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-d010e4d4d2 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-d010e4d4d2 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-d010e4d4d2 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-d010e4d4d2 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-d010e4d4d2 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | naturalproductmech:mibig-d010e4d4d2 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved two-encoding consistency | passed | True | naturalproductmech:mibig-d010e4d4d2 | The saved SMILES and Standard InChI produce declared full key ZSGBYOOWDWUSGB-ULKWOHBESA-N, formula C87H121ClN18O29, one fragment, net charge zero and the same normalized Standard InChI. Each representation has 12 specified and 6 unspecified tetrahedral carbon centres, with 2 specified double bonds. The 15 additional unspecified double-bond flags in the parsed InChI are C(-O)=N forms, not missing C=C assignments. This establishes internal encoding consistency only. |
| Whole original owner and exact retained source joins | passed | True | naturalproductmech:mibig-d010e4d4d2 | The whole original gausemycin B owner, seven retained arrays containing 3 rows, and two empty supplemental arrays were read. Exact producer, locus and occurrence assertions, structure literals and curation history are retained. No bioactivity annotation, molecular target, pathway or causal graph occurs in this saved owner. |
| Own PubMed identity and supplied abstract | passed | True | naturalproductmech:mibig-d010e4d4d2 | The matched article owns PMID 34009717; its own ArticleIdList identifies 10.1002/anie.202104528. The complete supplied abstract was read. Reference-list identifiers and family names are not used as exact congener aliases. |
| Exact natural structure and stereochemistry | unavailable | True | naturalproductmech:mibig-d010e4d4d2 | Six carbon stereocentres remain unspecified in each retained encoding. The abstract does not independently establish all exact A/B atom assignments, the individual side-chain state or the NPA cross-reference mapping. |
| Exact stock, locus, occurrence and assay applicability | unavailable | True | naturalproductmech:mibig-d010e4d4d2 | The retained S. kanamyceticus/MZ394730.1 source assertion is not explicitly linked in the abstract to INA-Ac-5812; exact locus experiments and individual quantitative bioactivity remain unverified. |

## Scientific And Domain Assessments

### Internal chemical consistency

representation: supported. Targets: naturalproductmech:mibig-d010e4d4d2.

The saved SMILES and Standard InChI produce declared full key ZSGBYOOWDWUSGB-ULKWOHBESA-N, formula C87H121ClN18O29, one fragment, net charge zero and the same normalized Standard InChI. Each representation has 12 specified and 6 unspecified tetrahedral carbon centres, with 2 specified double bonds. The 15 additional unspecified double-bond flags in the parsed InChI are C(-O)=N forms, not missing C=C assignments. This establishes internal encoding consistency only.

### A/B distinction and abstract applicability

identity: unknown. Targets: naturalproductmech:mibig-d010e4d4d2.

gausemycin B is retained as MIBiG BGC0002430 version 3 compound 2, with NPA033085 as an unverified cross-reference. A and B have different full keys and formulas; B adds C3H5NO relative to A and the stored ornithine-side-chain fragment differs. The abstract names both isolated compounds but summarizes several structural features collectively. Its N-acylation wording is not sufficient to call the stored A free-side-chain amine or the B acyl appendage erroneous.

### Named A/B isolation context

evidence: supported. Targets: naturalproductmech:mibig-d010e4d4d2.

The own abstract explicitly names gausemycins A and B as isolated major components from Streptomyces sp. INA-Ac-5812. This supports the named-product context for gausemycin B, with exact atom assignments and species/stock mapping still limited.

### Producer versus locus and genus occurrence

provenance: unknown. Targets: naturalproductmech:mibig-d010e4d4d2.

The retained producer is Streptomyces kanamyceticus (NCBITaxon:1967), graded SOURCE_ASSERTION; the MZ394730.1/BGC0002430 link remains CLUSTER_UNSTATED. The raw entry quality is questionable, completeness unknown, with no locus coordinates or evidence methods. LOTUS separately reports a Streptomyces genus occurrence (NCBITaxon:1883). The own ArticleIdList proves the DOI 10.1002/anie.202104528 citation identity, but does not prove the exact species/strain/locus relationship.

### Source classes versus model predictions

representation: supported. Targets: naturalproductmech:mibig-d010e4d4d2.

The NRPS/SACCHARIDE labels are retained MIBiG source classes. Cyclic peptides, RiPPs-Lasso peptides and glycoside status are NPClassifier predictions; the lasso prediction is not experimental RiPP biosynthesis evidence. The supplied abstract independently provides broad cyclic lipoglycopeptide context only.

### Individual potency and molecular mechanism

quantity: unknown. Targets: naturalproductmech:mibig-d010e4d4d2.

The abstract reports activity and mechanistic observations for gausemycins collectively, without a B-specific quantitative endpoint or direct molecular target in the supplied text. No individual potency, pore mechanism or cell-wall target is transferred into gausemycin B; the original owner has no such annotation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI732-LOCAL | /private/tmp/npm-review-work/shared-next-batch074-tentative/tentative-owner-source-inventory-001.json; /entries/1/owner_document; /entries/1/rows; /entries/1/row_guards; /entries/1/supplemental_retained_rows; sibling owner_document/chemical_structure entries 0,1 | context_only | The whole original gausemycin B owner, seven retained arrays containing 3 rows, and two empty supplemental arrays were read. Exact producer, locus and occurrence assertions, structure literals and curation history are retained. No bioactivity annotation, molecular target, pathway or causal graph occurs in this saved owner. |
| SCI732-CHEM | /private/tmp/npm-review-work/shared-next-batch074-tentative/source-science-preparation/root-tentative74-local-chemical-consistency-and-neighbors-001.json; /records/1/comparisons; /records/1/smiles/computed; /records/1/inchi/computed; /records/1/inchi/unspecified_neighbors; original record clock 2026-10-27T20:34:06.989346Z to 2026-10-27T20:34:06.992567Z | supports | The saved SMILES and Standard InChI produce declared full key ZSGBYOOWDWUSGB-ULKWOHBESA-N, formula C87H121ClN18O29, one fragment, net charge zero and the same normalized Standard InChI. Each representation has 12 specified and 6 unspecified tetrahedral carbon centres, with 2 specified double bonds. The 15 additional unspecified double-bond flags in the parsed InChI are C(-O)=N forms, not missing C=C assignments. This establishes internal encoding consistency only. |
| SCI732-ABSTRACT | /private/tmp/npm-review-work/shared-next-batch074-tentative/literature-preparation/public-metadata-pubmed-001/pmid-34009717.xml; ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract; ./PubmedArticle/PubmedData/ArticleIdList (own article only) | partial | The own PMID 34009717 abstract reports isolation and structure elucidation of named gausemycins A and B from Streptomyces sp. INA-Ac-5812. It describes shared lipoglycopeptide features and Gram-positive activity, slight calcium dependence, no low-concentration pore formation and no detectable cell-wall precursor accumulation. Individual quantitative potency, a direct molecular target, the complete per-congener natural configuration and the exact retained strain/genome mapping are not established by this abstract. |

## Limits And Additional Notes

- The complete owner and retained local source arrays were read literally; full-owner scientific verification and current chemical, taxonomic, sequence or NPA authority verification were not performed.
- Both retained encodings leave six tetrahedral carbon centres unspecified. Formula/key agreement does not establish a complete natural stereoisomer or physiological microspecies.
- Only the supplied PubMed title, abstract and own identifiers were inspected for the cited study; primary figures, methods and supplements remain unavailable in this evidence set.
- INA-Ac-5812 is not explicitly mapped in the supplied abstract to the retained S. kanamyceticus taxon and MZ394730.1 locus. Entry-level citation placement does not supply congener-specific experimental locus proof.
- Shared structural and mechanistic abstract language is not an individual quantitative activity or molecular-target assertion, and does not by itself resolve the different A/B side-chain encodings.
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
review_id: 20261027T220425Z-gausemycin-b
title: Scientific review of gausemycin B
started_at: '2026-10-27T22:00:57.436139Z'
finished_at: '2026-10-27T22:04:25.381156Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Gausemycin B has a distinct, internally consistent C87H121ClN18O29 encoding
  and six unresolved carbon stereocentres. Its own abstract supports named A/B isolation
  and shared biological context; exact B-specific structure, strain/locus and quantitative
  mechanism claims remain limited. The model-derived RiPPs-Lasso label is separate
  from the MIBiG NRPS/SACCHARIDE source classes.
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
  - path: data/natural_products/amino_acids_and_peptides/gausemycin-b.yaml
    sha256: 4154bb3dc3a19f3bb40134924f519e57796bd410d5c56915e3027abecadc1206
    role: target
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
- target_id: naturalproductmech:mibig-d010e4d4d2
  path: data/natural_products/amino_acids_and_peptides/gausemycin-b.yaml
  label: gausemycin B
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
  description: Bounded assessment of the original gausemycin B owner and exact retained
    source rows, saved chemical encoding consistency, own PubMed title/abstract/identifiers
    and the precise source-access limits.
  selection: One exact record selected in canonical repository path order from the
    unreviewed population; this observation assesses only its declared partial scientific
    scope.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-d010e4d4d2
  exclusions:
  - target: Full-owner scientific verification
    reason: Not independently verified within the stated source access and scientific
      scope; corresponding checks or assessments remain unavailable or unknown.
  - target: Complete primary methods, figures, spectra and supplements
    reason: Not independently verified within the stated source access and scientific
      scope; corresponding checks or assessments remain unavailable or unknown.
  - target: Current chemical, taxonomic, sequence and cross-reference authority verification
    reason: Not independently verified within the stated source access and scientific
      scope; corresponding checks or assessments remain unavailable or unknown.
  - target: Uninspected exact-congener natural configuration, stock/locus experiment
      and quantitative assay transfer
    reason: Not independently verified within the stated source access and scientific
      scope; corresponding checks or assessments remain unavailable or unknown.
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
    Reused for batch074 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch074. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
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
    Reused for batch074 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch074. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
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
    Reused for batch074 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch074. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
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
    Reused for batch074 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch074. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
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
    Reused for batch074 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch074. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/gausemycin-b.yaml
    --out /private/tmp/npm-review-work/732/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T22:00:58.805548Z. Original
    receipt: /private/tmp/npm-review-work/732/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- check_id: SCI732-ENCODINGS
  name: Saved two-encoding consistency
  status: passed
  required: true
  summary: The saved SMILES and Standard InChI produce declared full key ZSGBYOOWDWUSGB-ULKWOHBESA-N,
    formula C87H121ClN18O29, one fragment, net charge zero and the same normalized
    Standard InChI. Each representation has 12 specified and 6 unspecified tetrahedral
    carbon centres, with 2 specified double bonds. The 15 additional unspecified double-bond
    flags in the parsed InChI are C(-O)=N forms, not missing C=C assignments. This
    establishes internal encoding consistency only.
  evidence_ids:
  - SCI732-CHEM
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- check_id: SCI732-LOCAL-JOINS
  name: Whole original owner and exact retained source joins
  status: passed
  required: true
  summary: The whole original gausemycin B owner, seven retained arrays containing
    3 rows, and two empty supplemental arrays were read. Exact producer, locus and
    occurrence assertions, structure literals and curation history are retained. No
    bioactivity annotation, molecular target, pathway or causal graph occurs in this
    saved owner.
  evidence_ids:
  - SCI732-LOCAL
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- check_id: SCI732-OWN-ARTICLE
  name: Own PubMed identity and supplied abstract
  status: passed
  required: true
  summary: The matched article owns PMID 34009717; its own ArticleIdList identifies
    10.1002/anie.202104528. The complete supplied abstract was read. Reference-list
    identifiers and family names are not used as exact congener aliases.
  evidence_ids:
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- check_id: SCI732-NATURAL-IDENTITY
  name: Exact natural structure and stereochemistry
  status: unavailable
  required: true
  summary: Six carbon stereocentres remain unspecified in each retained encoding.
    The abstract does not independently establish all exact A/B atom assignments,
    the individual side-chain state or the NPA cross-reference mapping.
  evidence_ids:
  - SCI732-LOCAL
  - SCI732-CHEM
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- check_id: SCI732-EXPERIMENT-APPLICABILITY
  name: Exact stock, locus, occurrence and assay applicability
  status: unavailable
  required: true
  summary: The retained S. kanamyceticus/MZ394730.1 source assertion is not explicitly
    linked in the abstract to INA-Ac-5812; exact locus experiments and individual
    quantitative bioactivity remain unverified.
  evidence_ids:
  - SCI732-LOCAL
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
evidence:
- evidence_id: SCI732-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch074-tentative/tentative-owner-source-inventory-001.json
  accessed_at: '2026-10-27T20:32:40.640683Z'
  locator: /entries/1/owner_document; /entries/1/rows; /entries/1/row_guards; /entries/1/supplemental_retained_rows;
    sibling owner_document/chemical_structure entries 0,1
  snapshot_sha256: f16d8ad06743d4ce16187336c67cc9b27c42bc26b8d83a75d8205b92ee407e7e
  support: context_only
  summary: The whole original gausemycin B owner, seven retained arrays containing
    3 rows, and two empty supplemental arrays were read. Exact producer, locus and
    occurrence assertions, structure literals and curation history are retained. No
    bioactivity annotation, molecular target, pathway or causal graph occurs in this
    saved owner.
- evidence_id: SCI732-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch074-tentative/source-science-preparation/root-tentative74-local-chemical-consistency-and-neighbors-001.json
  accessed_at: '2026-10-27T20:36:45.687735Z'
  locator: /records/1/comparisons; /records/1/smiles/computed; /records/1/inchi/computed;
    /records/1/inchi/unspecified_neighbors; original record clock 2026-10-27T20:34:06.989346Z
    to 2026-10-27T20:34:06.992567Z
  snapshot_sha256: 9673400e8e1da030ce3d2e5d2fd24d4f4d3c344fd6b572ffdb06ca50a4515c78
  support: supports
  summary: The saved SMILES and Standard InChI produce declared full key ZSGBYOOWDWUSGB-ULKWOHBESA-N,
    formula C87H121ClN18O29, one fragment, net charge zero and the same normalized
    Standard InChI. Each representation has 12 specified and 6 unspecified tetrahedral
    carbon centres, with 2 specified double bonds. The 15 additional unspecified double-bond
    flags in the parsed InChI are C(-O)=N forms, not missing C=C assignments. This
    establishes internal encoding consistency only.
- evidence_id: SCI732-ABSTRACT
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch074-tentative/literature-preparation/public-metadata-pubmed-001/pmid-34009717.xml
  accessed_at: '2026-10-27T20:43:19.797243Z'
  locator: ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle;
    ./PubmedArticle/MedlineCitation/Article/Abstract; ./PubmedArticle/PubmedData/ArticleIdList
    (own article only)
  snapshot_sha256: 34fc9a94f8482098c355d337d4d56df6024d387198b2d9436ca5d20cbccc9e38
  support: partial
  summary: The own PMID 34009717 abstract reports isolation and structure elucidation
    of named gausemycins A and B from Streptomyces sp. INA-Ac-5812. It describes shared
    lipoglycopeptide features and Gram-positive activity, slight calcium dependence,
    no low-concentration pore formation and no detectable cell-wall precursor accumulation.
    Individual quantitative potency, a direct molecular target, the complete per-congener
    natural configuration and the exact retained strain/genome mapping are not established
    by this abstract.
assessments:
- assessment_id: SCI732-ENCODING
  area: representation
  topic: Internal chemical consistency
  outcome: supported
  summary: The saved SMILES and Standard InChI produce declared full key ZSGBYOOWDWUSGB-ULKWOHBESA-N,
    formula C87H121ClN18O29, one fragment, net charge zero and the same normalized
    Standard InChI. Each representation has 12 specified and 6 unspecified tetrahedral
    carbon centres, with 2 specified double bonds. The 15 additional unspecified double-bond
    flags in the parsed InChI are C(-O)=N forms, not missing C=C assignments. This
    establishes internal encoding consistency only.
  evidence_ids:
  - SCI732-CHEM
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- assessment_id: SCI732-CONGENER
  area: identity
  topic: A/B distinction and abstract applicability
  outcome: unknown
  summary: gausemycin B is retained as MIBiG BGC0002430 version 3 compound 2, with
    NPA033085 as an unverified cross-reference. A and B have different full keys and
    formulas; B adds C3H5NO relative to A and the stored ornithine-side-chain fragment
    differs. The abstract names both isolated compounds but summarizes several structural
    features collectively. Its N-acylation wording is not sufficient to call the stored
    A free-side-chain amine or the B acyl appendage erroneous.
  evidence_ids:
  - SCI732-LOCAL
  - SCI732-CHEM
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- assessment_id: SCI732-NAMED-PRODUCT
  area: evidence
  topic: Named A/B isolation context
  outcome: supported
  summary: The own abstract explicitly names gausemycins A and B as isolated major
    components from Streptomyces sp. INA-Ac-5812. This supports the named-product
    context for gausemycin B, with exact atom assignments and species/stock mapping
    still limited.
  evidence_ids:
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- assessment_id: SCI732-PRODUCER-LOCUS
  area: provenance
  topic: Producer versus locus and genus occurrence
  outcome: unknown
  summary: The retained producer is Streptomyces kanamyceticus (NCBITaxon:1967), graded
    SOURCE_ASSERTION; the MZ394730.1/BGC0002430 link remains CLUSTER_UNSTATED. The
    raw entry quality is questionable, completeness unknown, with no locus coordinates
    or evidence methods. LOTUS separately reports a Streptomyces genus occurrence
    (NCBITaxon:1883). The own ArticleIdList proves the DOI 10.1002/anie.202104528
    citation identity, but does not prove the exact species/strain/locus relationship.
  evidence_ids:
  - SCI732-LOCAL
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- assessment_id: SCI732-CLASSIFICATION
  area: representation
  topic: Source classes versus model predictions
  outcome: supported
  summary: The NRPS/SACCHARIDE labels are retained MIBiG source classes. Cyclic peptides,
    RiPPs-Lasso peptides and glycoside status are NPClassifier predictions; the lasso
    prediction is not experimental RiPP biosynthesis evidence. The supplied abstract
    independently provides broad cyclic lipoglycopeptide context only.
  evidence_ids:
  - SCI732-LOCAL
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
- assessment_id: SCI732-ACTIVITY
  area: quantity
  topic: Individual potency and molecular mechanism
  outcome: unknown
  summary: The abstract reports activity and mechanistic observations for gausemycins
    collectively, without a B-specific quantitative endpoint or direct molecular target
    in the supplied text. No individual potency, pore mechanism or cell-wall target
    is transferred into gausemycin B; the original owner has no such annotation.
  evidence_ids:
  - SCI732-LOCAL
  - SCI732-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-d010e4d4d2
findings: []
actions: []
limitations:
- The complete owner and retained local source arrays were read literally; full-owner
  scientific verification and current chemical, taxonomic, sequence or NPA authority
  verification were not performed.
- Both retained encodings leave six tetrahedral carbon centres unspecified. Formula/key
  agreement does not establish a complete natural stereoisomer or physiological microspecies.
- Only the supplied PubMed title, abstract and own identifiers were inspected for
  the cited study; primary figures, methods and supplements remain unavailable in
  this evidence set.
- INA-Ac-5812 is not explicitly mapped in the supplied abstract to the retained S.
  kanamyceticus taxon and MZ394730.1 locus. Entry-level citation placement does not
  supply congener-specific experimental locus proof.
- Shared structural and mechanistic abstract language is not an individual quantitative
  activity or molecular-target assertion, and does not by itself resolve the different
  A/B side-chain encodings.
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
