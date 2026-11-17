# Scientific review of obafluorin

- Review: 20261029T064438Z-obafluorin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-29T06:15:50.442618Z
- Finished UTC: 2026-10-29T06:44:38.192461Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Obafluorin’s retained nitro spelling parses successfully and normalizes to charge-separated nitro. Its own abstract supports the reported producer and β-lactone biosynthetic context; exact natural stereochemistry and uninspected occurrence claims remain bounded.

## Scope And Provenance

Partial exact-owner interpretation of all named raw arrays, accepted actual intake, saved two-encoding diagnostics and the own publication evidence identified here.

Selection: One record selected in canonical path order from the actual batch92 remaining-record catalogue; all of this owner and its named local source rows were read.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-6dc8b75919 | data/natural_products/amino_acids_and_peptides/obafluorin.yaml | generated | obafluorin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-6dc8b75919 | Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-6dc8b75919 | Fresh reproduction gate passed:all3116 records are byte-identical to seeding from maintained inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-6dc8b75919 | Fresh deterministic review queue produced8922 rows across12 queues; this is not scientific review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-6dc8b75919 | Fresh configured identifier-label gate passed:13472 canonical,657 synonym and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-6dc8b75919 | Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency warnings;3116 closed-schema records have zero errors; site freshness, reproduction and lockfile checks passed, alongside22 governed artifacts and15 raw inventories. |
| Native strict target validation | passed | True | naturalproductmech:mibig-6dc8b75919 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Whole owner, raw arrays and actual intake fidelity | passed | True | naturalproductmech:mibig-6dc8b75919 | The complete owner, retained history and nine named source arrays match their raw-table rows. Accepted actual intake reproduces the owner and six official arrays with37 captured inputs. Empty arrays are scoped to the named tables and exact join keys. |
| Saved dual-encoding consistency | passed | True | naturalproductmech:mibig-6dc8b75919 | Both saved input encodings parsed and match the declared full key and formulaC17H14N2O7, net charge0 and1 component. Both canonical-SMILES equality flags are false and the complete atom map is empty; those differences are preserved without inferring a different natural compound. SMILES reports0 unspecified potential sites; InChI reports1. The retained flag is true and both tetrahedral sites are specified. Neutral nitro syntax normalizes successfully; the extra InChI potential site is C=N. |
| Own publication scope | passed | True | naturalproductmech:mibig-6dc8b75919 | The own abstract describes ObiF thioesterase-mediated β-lactone release and genetic/biochemical characterization of the obafluorin BGC in Pseudomonas fluorescens ATCC39502. It is abstract-level support, not a reading of complete methods, spectra or all occurrence citations. |
| Successful nitro sanitization | passed | True | naturalproductmech:mibig-6dc8b75919 | Both saved encodings match the declared full key and C17H14N2O7, with two specified tetrahedral sites. Original N(=O)=O sanitizes to [N+](=O)[O-]; this is not a malformed-SMILES defect. The one additional unspecified InChI potential double-bond environment is C15=N17, not a natural C=C assignment. Natural absolute configuration is not established by these computations. |

## Scientific And Domain Assessments

### Whole owner and source fidelity

provenance: supported. Targets: naturalproductmech:mibig-6dc8b75919.

The complete owner, retained history and nine named source arrays match their raw-table rows. Accepted actual intake reproduces the owner and six official arrays with37 captured inputs. Empty arrays are scoped to the named tables and exact join keys.

### Saved encodings and stereochemical limits

consistency: supported. Targets: naturalproductmech:mibig-6dc8b75919.

Both saved input encodings parsed and match the declared full key and formulaC17H14N2O7, net charge0 and1 component. Both canonical-SMILES equality flags are false and the complete atom map is empty; those differences are preserved without inferring a different natural compound. SMILES reports0 unspecified potential sites; InChI reports1. The retained flag is true and both tetrahedral sites are specified. Neutral nitro syntax normalizes successfully; the extra InChI potential site is C=N.

### Exact named-product correspondence

identity: unknown. Targets: naturalproductmech:mibig-6dc8b75919.

Both saved encodings match the declared full key and C17H14N2O7, with two specified tetrahedral sites. Original N(=O)=O sanitizes to [N+](=O)[O-]; this is not a malformed-SMILES defect. The one additional unspecified InChI potential double-bond environment is C15=N17, not a natural C=C assignment. Natural absolute configuration is not established by these computations.

### Producer, strain and cluster applicability

evidence: supported. Targets: naturalproductmech:mibig-6dc8b75919.

Own PMID28504677 describes genetic and biochemical characterization of the obafluorin BGC in Pseudomonas fluorescens ATCC39502 and the catalytic cysteine of ObiF’s thioesterase domain. This supports the reported producer/biosynthetic context and is compatible with retained BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED grades. The abstract does not verify KX931446.1 or every individual knockout experiment; its DataBank entries are PubChem substances, not that sequence accession.

### Structural class and filing

consistency: supported. Targets: naturalproductmech:mibig-6dc8b75919.

Amino-acids-and-peptides filing and the MIBiG NRPS assertion are compatible with the abstract’s NRPS β-lactone biosynthesis. Empty NPClassifier superclass/class lists are not evidence that the structure is malformed.

### Assay and target specificity

evidence: unknown. Targets: naturalproductmech:mibig-6dc8b75919.

The own abstract describes antibiotic obafluorin and a biosynthetic enzyme mechanism, not a compound-specific potency measurement. The single PubChem CID146354 row has a blank AID and literal no-assay-data sentinel; it is not an assay or evidence of inactivity. Named BindingDB and AntibioticMech arrays are empty.

### Graph and protein grounding scope

grounding: not_applicable. Targets: naturalproductmech:mibig-6dc8b75919.

No inline causal graph, molecular targets or pathway steps are asserted. The abstract provides an ObiF catalytic-domain lead, but no new protein identifier, mechanism graph or experimental detail is added here.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI916-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/obafluorin.yaml; whole owner: identity, chemistry, classifications, producer/locus/occurrence assertions and retained history | context_only | The whole owner was read and is byte-identical to the accepted current intake owner. Source assertions are not independent proof of natural identity. |
| SCI916-ROWS | /private/tmp/npm-review-work/shared-next-batch092-tentative/source-science-preparation/bgc-tentative92-owner-source-scientific-reconnaissance-DATA-001.json; /records/5/retained_rows, supplemental_rows and row_guards; complete exact-key named table joins | supports | All nine named retained and supplemental source arrays were matched to pinned raw tables and exact row positions, including empty arrays; 9 rows are retained. These joins establish local provenance and reproducibility, not external identity. |
| SCI916-INTAKE | /private/tmp/npm-review-work/shared-next-batch092/native-current92-intake-reconciliation-001.json; /records[order=916]: whole_owner_and_six_official_arrays_equal, original_clocks and37 source inputs | supports | Actual intake preserves the whole owner and six official arrays with37 original captured inputs. Strict validation passed; its original clocks and warning text are retained separately from the two-encoding diagnostic. |
| SCI916-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch092-tentative/source-science-preparation/review-support-tentative92-ten-owner-dual-encoding-results-001.json; /records/5: both original strings, parse clocks, full atoms/bonds, stereo_counts, comparisons and atom_correspondence | partial | Both saved input encodings parsed and match the declared full key and formulaC17H14N2O7, net charge0 and1 component. Both canonical-SMILES equality flags are false and the complete atom map is empty; those differences are preserved without inferring a different natural compound. SMILES reports0 unspecified potential sites; InChI reports1. The retained flag is true and both tetrahedral sites are specified. Neutral nitro syntax normalizes successfully; the extra InChI potential site is C=N. |
| SCI916-PMID | /private/tmp/npm-review-work/shared-next-batch092-tentative/literature-preparation/public-metadata-seven-PubMed-001/pmid-28504677.xml; ./PubmedArticle/MedlineCitation/Article/ArticleTitle and Abstract; own PubmedData/ArticleIdList and Article/DataBankList; references excluded | partial | The own abstract describes ObiF thioesterase-mediated β-lactone release and genetic/biochemical characterization of the obafluorin BGC in Pseudomonas fluorescens ATCC39502. It is abstract-level support, not a reading of complete methods, spectra or all occurrence citations. |
| SCI916-STEREO-METHOD | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; structure_fields: stereo_complete from FindMolChiralCenters(includeUnassigned=True) | context_only | The retained completeness flag concerns undefined tetrahedral centres; extra potential double-bond sites in a saved InChI representation are not an automatic schema violation. |

## Limits And Additional Notes

- Partial scientific coverage: own publication evidence is the saved title/abstract and explicitly identified metadata; uninspected full texts, figures, spectra, supplements and independent sequence/taxonomy authorities are not verified.
- Both canonical-SMILES differences and empty complete atom maps are retained. Eight combined diagnostic warnings remain unattributed to individual records; no chemistry was rerun.
- LOTUS occurrence and MIBiG producer/locus claims are separate; publication independence and uninspected cross-references are not assumed.
- The six distinct LOTUS occurrence citations were not read as primary articles. The different own DOI10.1038/nchembio.2374 and occurrence DOI10.1038/NCOMMS15935 are not alone a citation error.
- The blank-AID PubChem row is an availability sentinel, not negative activity evidence.
- Source seeding retains five unresolved assay-organism targets (one distinct Human label),42 withheld nonspecific producer claims and161 merged-taxonomy rewrites.
- Queue diagnostics rank deterministic curation questions and do not prove literature support or review completion.
- 499 configured nonblocking mismatches remain warnings;4898 pairs lacked an adapter.35 exception and657 synonym matches retain their configured scope; no fresh ontology authority retrieval is asserted.
- Four tests were skipped; two dependency deprecations concern LinkML dataclass and Pandas copy-on-write behavior. Source seeding warnings and configured gate boundaries are retained in the full log.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- Configured ontology caches and scientific/test skips retain their original scope; a new command execution is not a fresh retrieval of every authority.
- All tracked link objects are hashed as link-target bytes without dereferencing; canonical record source intake remains regular-file-only and uses the separately reviewed AGENTS.md context projection.
- The whole local owner and retained source rows were read. Full-owner scientific verification remains false; scientific_review denotes the bounded scientific interpretation in this report.
- Original owner/source reading, two-encoding computation, primary-text reading, HTTP retrieval and later metadata reading retain separate clocks. Official intake separately computed SMILES facts.
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
review_id: 20261029T064438Z-obafluorin
title: Scientific review of obafluorin
started_at: '2026-10-29T06:15:50.442618Z'
finished_at: '2026-10-29T06:44:38.192461Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Obafluorin’s retained nitro spelling parses successfully and normalizes to
  charge-separated nitro. Its own abstract supports the reported producer and β-lactone
  biosynthetic context; exact natural stereochemistry and uninspected occurrence claims
  remain bounded.
source:
  git_revision: ce6a5498df5be51116bd5e0c119023ee62bb5464
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: AGENTS.md
    sha256: 69e4037f8dc97d4b00bb7bb83b41ceca025f6ef578d5c0bf8086f3400becde0b
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
  - path: data/natural_products/amino_acids_and_peptides/obafluorin.yaml
    sha256: 9db703ad21ba8fcf8a9bc3b62c885a3282a1bd7b7aa6c42e7ecda1c87ae1f72d
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
- target_id: naturalproductmech:mibig-6dc8b75919
  path: data/natural_products/amino_acids_and_peptides/obafluorin.yaml
  label: obafluorin
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
  description: Partial exact-owner interpretation of all named raw arrays, accepted
    actual intake, saved two-encoding diagnostics and the own publication evidence
    identified here.
  selection: One record selected in canonical path order from the actual batch92 remaining-record
    catalogue; all of this owner and its named local source rows were read.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-6dc8b75919
  exclusions:
  - target: Independent figure/spectrum/supplement reanalysis
    reason: Outside the available evidence and explicitly bounded scientific coverage;
      see claim-specific assessments and limitations.
  - target: Natural configuration from normalized-key agreement
    reason: Outside the available evidence and explicitly bounded scientific coverage;
      see claim-specific assessments and limitations.
  - target: Transfer of family or purified-fragment results to exact-congener activity
    reason: Outside the available evidence and explicitly bounded scientific coverage;
      see claim-specific assessments and limitations.
  - target: Uninspected taxonomy, sequence-version or protein authority verification
    reason: Outside the available evidence and explicitly bounded scientific coverage;
      see claim-specific assessments and limitations.
checks:
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its
    pinned path.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.338684Z;
    finished 2026-10-28T21:33:29.829334Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-corpus.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-corpus.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: Fresh reproduction gate passed:all3116 records are byte-identical to seeding
    from maintained inputs.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.338638Z;
    finished 2026-10-28T21:33:44.898261Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-reproduction.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/verify-reproduction.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: Fresh deterministic review queue produced8922 rows across12 queues; this
    is not scientific review coverage.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just review-queue --tsv /private/tmp/npm-review-queue-batch-087-freshce6a5498-001.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.340163Z;
    finished 2026-10-28T21:33:21.471992Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/review-queue.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/review-queue.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: Fresh configured identifier-label gate passed:13472 canonical,657 synonym
    and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain
    explicit.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:09.340947Z;
    finished 2026-10-28T21:33:45.063118Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/validate-products.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/validate-products.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency
    warnings;3116 closed-schema records have zero errors; site freshness, reproduction
    and lockfile checks passed, alongside22 governed artifacts and15 raw inventories.
  command: env -u PYTEST_ADDOPTS UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache
    RECORD_REVIEW_BASE=ce6a5498df5be51116bd5e0c119023ee62bb5464 PYTHONDONTWRITEBYTECODE=1
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: Fresh batch087 command on ce6a5498df5be51116bd5e0c119023ee62bb5464 in
    /private/tmp/npm-record-reviews-20261021. Started 2026-10-28T21:33:14.328372Z;
    finished 2026-10-28T21:38:03.336464Z; ROOT observed at 2026-10-28T21:38:57.679080Z.
    Original receipt /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/qc.json;
    transcript /private/tmp/npm-native-checks/batch-087/fresh-ce6a5498-001/qc.log.
    PYTEST_ADDOPTS was explicitly unset. Full tracked byte/mode capture and recheck
    occurred separately after these gates; no pre-gate capture is inferred. Warnings,
    configured exceptions and skips remain in the original transcript.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/obafluorin.yaml
    --out /private/tmp/npm-review-work/916/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-29T06:15:51.868096Z. Original
    receipt: /private/tmp/npm-review-work/916/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
- check_id: SCI916-LOCAL
  name: Whole owner, raw arrays and actual intake fidelity
  status: passed
  required: true
  summary: The complete owner, retained history and nine named source arrays match
    their raw-table rows. Accepted actual intake reproduces the owner and six official
    arrays with37 captured inputs. Empty arrays are scoped to the named tables and
    exact join keys.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ROWS
  - SCI916-INTAKE
  scope_note: Evidence applies only to the exact source placement and interpretation
    stated; native validation and normalized-key agreement do not establish complete
    natural identity.
- check_id: SCI916-ENCODINGS
  name: Saved dual-encoding consistency
  status: passed
  required: true
  summary: Both saved input encodings parsed and match the declared full key and formulaC17H14N2O7,
    net charge0 and1 component. Both canonical-SMILES equality flags are false and
    the complete atom map is empty; those differences are preserved without inferring
    a different natural compound. SMILES reports0 unspecified potential sites; InChI
    reports1. The retained flag is true and both tetrahedral sites are specified.
    Neutral nitro syntax normalizes successfully; the extra InChI potential site is
    C=N.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ENCODINGS
  - SCI916-STEREO-METHOD
  scope_note: Evidence applies only to the exact source placement and interpretation
    stated; native validation and normalized-key agreement do not establish complete
    natural identity.
- check_id: SCI916-SOURCE
  name: Own publication scope
  status: passed
  required: true
  summary: The own abstract describes ObiF thioesterase-mediated β-lactone release
    and genetic/biochemical characterization of the obafluorin BGC in Pseudomonas
    fluorescens ATCC39502. It is abstract-level support, not a reading of complete
    methods, spectra or all occurrence citations.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-PMID
  - SCI916-ROWS
  scope_note: Evidence applies only to the exact source placement and interpretation
    stated; native validation and normalized-key agreement do not establish complete
    natural identity.
- check_id: SCI916-NITRO
  name: Successful nitro sanitization
  status: passed
  required: true
  summary: Both saved encodings match the declared full key and C17H14N2O7, with two
    specified tetrahedral sites. Original N(=O)=O sanitizes to [N+](=O)[O-]; this
    is not a malformed-SMILES defect. The one additional unspecified InChI potential
    double-bond environment is C15=N17, not a natural C=C assignment. Natural absolute
    configuration is not established by these computations.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ENCODINGS
  scope_note: Evidence applies only to the exact source placement and interpretation
    stated; native validation and normalized-key agreement do not establish complete
    natural identity.
evidence:
- evidence_id: SCI916-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/obafluorin.yaml
  locator: 'whole owner: identity, chemistry, classifications, producer/locus/occurrence
    assertions and retained history'
  accessed_at: '2026-10-29T05:04:57.292089Z'
  snapshot_sha256: 9db703ad21ba8fcf8a9bc3b62c885a3282a1bd7b7aa6c42e7ecda1c87ae1f72d
  support: context_only
  summary: The whole owner was read and is byte-identical to the accepted current
    intake owner. Source assertions are not independent proof of natural identity.
- evidence_id: SCI916-ROWS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch092-tentative/source-science-preparation/bgc-tentative92-owner-source-scientific-reconnaissance-DATA-001.json
  locator: /records/5/retained_rows, supplemental_rows and row_guards; complete exact-key
    named table joins
  accessed_at: '2026-10-29T05:04:57.292089Z'
  snapshot_sha256: c509bee81e443a047964c678381e046cdf85a61110d7faed30196393419aff86
  support: supports
  summary: All nine named retained and supplemental source arrays were matched to
    pinned raw tables and exact row positions, including empty arrays; 9 rows are
    retained. These joins establish local provenance and reproducibility, not external
    identity.
- evidence_id: SCI916-INTAKE
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch092/native-current92-intake-reconciliation-001.json
  locator: '/records[order=916]: whole_owner_and_six_official_arrays_equal, original_clocks
    and37 source inputs'
  accessed_at: '2026-10-29T06:15:51.926296Z'
  snapshot_sha256: 03bedeacfc9f534a456d954d81453d1739088810759d84918f7b5721be7c3026
  support: supports
  summary: Actual intake preserves the whole owner and six official arrays with37
    original captured inputs. Strict validation passed; its original clocks and warning
    text are retained separately from the two-encoding diagnostic.
- evidence_id: SCI916-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch092-tentative/source-science-preparation/review-support-tentative92-ten-owner-dual-encoding-results-001.json
  locator: '/records/5: both original strings, parse clocks, full atoms/bonds, stereo_counts,
    comparisons and atom_correspondence'
  accessed_at: '2026-10-29T06:02:24.993284Z'
  snapshot_sha256: f637677ccdb47575ad59caef921bcca37ea3f12e019ed9b92606a5917d2323da
  support: partial
  summary: Both saved input encodings parsed and match the declared full key and formulaC17H14N2O7,
    net charge0 and1 component. Both canonical-SMILES equality flags are false and
    the complete atom map is empty; those differences are preserved without inferring
    a different natural compound. SMILES reports0 unspecified potential sites; InChI
    reports1. The retained flag is true and both tetrahedral sites are specified.
    Neutral nitro syntax normalizes successfully; the extra InChI potential site is
    C=N.
- evidence_id: SCI916-PMID
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch092-tentative/literature-preparation/public-metadata-seven-PubMed-001/pmid-28504677.xml
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle and Abstract; own
    PubmedData/ArticleIdList and Article/DataBankList; references excluded
  accessed_at: '2026-10-29T06:01:19.768829Z'
  snapshot_sha256: 76ce4e81ee66888eb26c425dae2c3cacbf36c91b416a0c57f55e3e5beeb75d57
  support: partial
  summary: The own abstract describes ObiF thioesterase-mediated β-lactone release
    and genetic/biochemical characterization of the obafluorin BGC in Pseudomonas
    fluorescens ATCC39502. It is abstract-level support, not a reading of complete
    methods, spectra or all occurrence citations.
- evidence_id: SCI916-STEREO-METHOD
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'structure_fields: stereo_complete from FindMolChiralCenters(includeUnassigned=True)'
  accessed_at: '2026-10-29T06:28:13.929285Z'
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
  support: context_only
  summary: The retained completeness flag concerns undefined tetrahedral centres;
    extra potential double-bond sites in a saved InChI representation are not an automatic
    schema violation.
assessments:
- assessment_id: SCI916-LOCAL
  area: provenance
  topic: Whole owner and source fidelity
  outcome: supported
  summary: The complete owner, retained history and nine named source arrays match
    their raw-table rows. Accepted actual intake reproduces the owner and six official
    arrays with37 captured inputs. Empty arrays are scoped to the named tables and
    exact join keys.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ROWS
  - SCI916-INTAKE
- assessment_id: SCI916-ENCODINGS
  area: consistency
  topic: Saved encodings and stereochemical limits
  outcome: supported
  summary: Both saved input encodings parsed and match the declared full key and formulaC17H14N2O7,
    net charge0 and1 component. Both canonical-SMILES equality flags are false and
    the complete atom map is empty; those differences are preserved without inferring
    a different natural compound. SMILES reports0 unspecified potential sites; InChI
    reports1. The retained flag is true and both tetrahedral sites are specified.
    Neutral nitro syntax normalizes successfully; the extra InChI potential site is
    C=N.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ENCODINGS
  - SCI916-STEREO-METHOD
  dimensions:
  - name: stereochemical_resolution
    value: Literal stereo_complete=True; SMILES0 and InChI1 unspecified potential
      sites.
    definition: Saved graph diagnostics are distinct from natural stereochemistry
      proof.
    evidence_ids:
    - SCI916-LOCAL
    - SCI916-ENCODINGS
    - SCI916-STEREO-METHOD
- assessment_id: SCI916-IDENTITY
  area: identity
  topic: Exact named-product correspondence
  outcome: unknown
  summary: Both saved encodings match the declared full key and C17H14N2O7, with two
    specified tetrahedral sites. Original N(=O)=O sanitizes to [N+](=O)[O-]; this
    is not a malformed-SMILES defect. The one additional unspecified InChI potential
    double-bond environment is C15=N17, not a natural C=C assignment. Natural absolute
    configuration is not established by these computations.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ROWS
  - SCI916-ENCODINGS
  - SCI916-PMID
- assessment_id: SCI916-PRODUCER
  area: evidence
  topic: Producer, strain and cluster applicability
  outcome: supported
  summary: Own PMID28504677 describes genetic and biochemical characterization of
    the obafluorin BGC in Pseudomonas fluorescens ATCC39502 and the catalytic cysteine
    of ObiF’s thioesterase domain. This supports the reported producer/biosynthetic
    context and is compatible with retained BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED
    grades. The abstract does not verify KX931446.1 or every individual knockout experiment;
    its DataBank entries are PubChem substances, not that sequence accession.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ROWS
  - SCI916-PMID
  dimensions:
  - name: taxon_strain
    value: Own PMID28504677 describes genetic and biochemical characterization of
      the obafluorin BGC in Pseudomonas fluorescens ATCC39502 and the catalytic cysteine
      of ObiF’s thioesterase domain. This supports the reported producer/biosynthetic
      context and is compatible with retained BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED
      grades. The abstract does not verify KX931446.1 or every individual knockout
      experiment; its DataBank entries are PubChem substances, not that sequence accession.
    definition: Native producer, heterologous host, strain and accession-version claims
      require separate source support.
    evidence_ids:
    - SCI916-LOCAL
    - SCI916-ROWS
    - SCI916-PMID
  - name: evidence_tier
    value: BGC_CHARACTERIZED / CLUSTER_DEMONSTRATED; ENTRY citation routing.
    definition: Stored database grades remain separate from the scope of inspected
      experimental text.
    evidence_ids:
    - SCI916-ROWS
    - SCI916-PMID
  - name: source_version
    value: MIBiG BGC0001437:1 version5; NPClassifier npclassifier.gnps2.org@2026-09-07.
    definition: Exact retained versions; own metadata access and later interpretation
      clocks are distinct.
    evidence_ids:
    - SCI916-ROWS
    - SCI916-PMID
- assessment_id: SCI916-CLASSIFICATION
  area: consistency
  topic: Structural class and filing
  outcome: supported
  summary: Amino-acids-and-peptides filing and the MIBiG NRPS assertion are compatible
    with the abstract’s NRPS β-lactone biosynthesis. Empty NPClassifier superclass/class
    lists are not evidence that the structure is malformed.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ROWS
  - SCI916-PMID
- assessment_id: SCI916-ACTIVITY
  area: evidence
  topic: Assay and target specificity
  outcome: unknown
  summary: The own abstract describes antibiotic obafluorin and a biosynthetic enzyme
    mechanism, not a compound-specific potency measurement. The single PubChem CID146354
    row has a blank AID and literal no-assay-data sentinel; it is not an assay or
    evidence of inactivity. Named BindingDB and AntibioticMech arrays are empty.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-ROWS
  - SCI916-PMID
- assessment_id: SCI916-GRAPH
  area: grounding
  topic: Graph and protein grounding scope
  outcome: not_applicable
  summary: No inline causal graph, molecular targets or pathway steps are asserted.
    The abstract provides an ObiF catalytic-domain lead, but no new protein identifier,
    mechanism graph or experimental detail is added here.
  target_ids:
  - naturalproductmech:mibig-6dc8b75919
  evidence_ids:
  - SCI916-LOCAL
  - SCI916-PMID
findings: []
actions: []
limitations:
- 'Partial scientific coverage: own publication evidence is the saved title/abstract
  and explicitly identified metadata; uninspected full texts, figures, spectra, supplements
  and independent sequence/taxonomy authorities are not verified.'
- Both canonical-SMILES differences and empty complete atom maps are retained. Eight
  combined diagnostic warnings remain unattributed to individual records; no chemistry
  was rerun.
- LOTUS occurrence and MIBiG producer/locus claims are separate; publication independence
  and uninspected cross-references are not assumed.
- The six distinct LOTUS occurrence citations were not read as primary articles. The
  different own DOI10.1038/nchembio.2374 and occurrence DOI10.1038/NCOMMS15935 are
  not alone a citation error.
- The blank-AID PubChem row is an availability sentinel, not negative activity evidence.
- Source seeding retains five unresolved assay-organism targets (one distinct Human
  label),42 withheld nonspecific producer claims and161 merged-taxonomy rewrites.
- Queue diagnostics rank deterministic curation questions and do not prove literature
  support or review completion.
- 499 configured nonblocking mismatches remain warnings;4898 pairs lacked an adapter.35
  exception and657 synonym matches retain their configured scope; no fresh ontology
  authority retrieval is asserted.
- Four tests were skipped; two dependency deprecations concern LinkML dataclass and
  Pandas copy-on-write behavior. Source seeding warnings and configured gate boundaries
  are retained in the full log.
- Native baseline gates establish configured consistency, not independent biological
  production, exact stereochemistry or primary-source adequacy.
- Configured ontology caches and scientific/test skips retain their original scope;
  a new command execution is not a fresh retrieval of every authority.
- All tracked link objects are hashed as link-target bytes without dereferencing;
  canonical record source intake remains regular-file-only and uses the separately
  reviewed AGENTS.md context projection.
notes:
- The whole local owner and retained source rows were read. Full-owner scientific
  verification remains false; scientific_review denotes the bounded scientific interpretation
  in this report.
- Original owner/source reading, two-encoding computation, primary-text reading, HTTP
  retrieval and later metadata reading retain separate clocks. Official intake separately
  computed SMILES facts.
- No scientific record, maintained input or native curation status was changed. Any
  findings and actions record ROOT-adopted proposed work; exact-source limitations
  and unavailable checks remain explicit.
```
