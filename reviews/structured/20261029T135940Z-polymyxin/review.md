# Scientific review of polymyxin

- Review: 20261029T135940Z-polymyxin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-29T13:15:06.192224Z
- Finished UTC: 2026-10-29T13:59:40.830759Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The saved structure is a partially specified polymyxin-like decapeptide with a separate sulfuric-acid component. The E681 abstract supports the pmx locus generally; exact congener, sulfate-form and natural stereochemical correspondence remain unresolved.

## Scope And Provenance

Whole owner, all nine named local-source arrays, actual official intake, saved dual-encoding results and explicitly identified publication evidence. Source scope: Own PubMed abstract and saved graph/assay provenance only; primary route failed before HTTP. Unresolved curation questions: Resolve the E681 product identity and isolated form using a verified structural source before assigning a congener or filling stereochemistry. Any later evidence-supported change must use maintained source harmonization and pass strict validation, source reproduction and corpus checks.

Selection: One record selected in canonical path order from the actual batch96 remaining-record catalogue; the whole owner and all named local source rows were read.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-2f5f003d07 | data/natural_products/amino_acids_and_peptides/polymyxin.yaml | generated | polymyxin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-2f5f003d07 | Fresh corpus gate passed:3116 PATHS.tsv rows and3116 files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-2f5f003d07 | Fresh reproduction gate passed:all3116 records are byte-identical to seeding from maintained inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-2f5f003d07 | Fresh deterministic review queue produced8922 rows across12 queues; this is not scientific review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-2f5f003d07 | Fresh configured identifier-label gate passed:13472 canonical,657 synonym and35 exception matches;499 nonblocking mismatches and4898 no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-2f5f003d07 | Fresh full quality gate passed:1024 tests passed,4 skipped,2 dependency warnings;3116 closed-schema records have zero errors; site freshness, reproduction and lockfile checks passed, alongside22 governed artifacts and15 raw inventories. |
| Native strict target validation | passed | True | naturalproductmech:mibig-2f5f003d07 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Whole owner and raw-source fidelity | passed | True | naturalproductmech:mibig-2f5f003d07 | The whole owner and nine named retained/supplemental source arrays match the saved local provenance (21 retained rows; 2 official rows). Accepted actual intake preserves the whole owner, six official arrays and 37 source inputs. This supports exact local provenance, not independent natural identity; empty named arrays do not establish global absence. |
| Saved dual-encoding internal consistency | passed | True | naturalproductmech:mibig-2f5f003d07 | Saved parses agree on declared full key HFMDLUQUEXNBOP-UHFFFAOYSA-N, formula C56H100N16O17S and Standard InChI. Saved SMILES stereo counts are [('Atom_Tetrahedral', 0, 13), ('Bond_Double', 0, 0)]; InChI counts are [('Atom_Tetrahedral', 0, 13), ('Bond_Double', 0, 11)]. Canonical isomeric/nonisomeric SMILES equality and direct atom correspondence retain their original saved values; representation-level disagreement is not automatically a natural-identity error. No new chemistry or stereochemical assignment was performed. |
| Claim-level source and saved-fact scope | passed | False | naturalproductmech:mibig-2f5f003d07 | The cited source observations and bounded comparison preserve their original scope and clocks. This check does not certify complete natural identity. |

## Scientific And Domain Assessments

### Whole owner and exact local-source fidelity

provenance: supported. Targets: naturalproductmech:mibig-2f5f003d07.

The whole owner and nine named retained/supplemental source arrays match the saved local provenance (21 retained rows; 2 official rows). Accepted actual intake preserves the whole owner, six official arrays and 37 source inputs. This supports exact local provenance, not independent natural identity; empty named arrays do not establish global absence.

### Saved dual-encoding scope

consistency: supported. Targets: naturalproductmech:mibig-2f5f003d07.

Saved parses agree on declared full key HFMDLUQUEXNBOP-UHFFFAOYSA-N, formula C56H100N16O17S and Standard InChI. Saved SMILES stereo counts are [('Atom_Tetrahedral', 0, 13), ('Bond_Double', 0, 0)]; InChI counts are [('Atom_Tetrahedral', 0, 13), ('Bond_Double', 0, 11)]. Canonical isomeric/nonisomeric SMILES equality and direct atom correspondence retain their original saved values; representation-level disagreement is not automatically a natural-identity error. No new chemistry or stereochemical assignment was performed.

### Peptide and component boundary

identity: supported. Targets: naturalproductmech:mibig-2f5f003d07.

Saved connectivity traces fatty-acyl–Dab–Thr–Dab–Dab–Dab–Phe–Leu–Dab–Dab–Thr, with the residue-10 carbonyl joined to the residue-4 sidechain nitrogen. The separate H2SO4 component is not a covalent sulfation or an explicitly encoded sulfate dianion.

### Partially specified stereochemistry

identity: unknown. Targets: naturalproductmech:mibig-2f5f003d07.

The graph retains 13 unspecified tetrahedral sites: ten alpha carbons, two threonine beta carbons and the fatty-acyl C6 site. These declared gaps and the sulfate-related component do not automatically establish a wrong natural structure or a specific E681 congener.

### Component-total formula equivalence

consistency: supported. Targets: naturalproductmech:mibig-2f5f003d07.

The literal dotted formula C56H98N16O13.H2O4S and aggregate C56H100N16O17S have the same elemental totals. The saved literal formula-comparison flag remains false as a formatting distinction, not a chemical mismatch.

### E681 locus versus exact product identity

evidence: supported. Targets: naturalproductmech:mibig-2f5f003d07.

The abstract reports pmxABCDE involvement, loss after pmxE disruption and heterologous Bacillus subtilis production with L-Dab supplementation. This supports the general locus experiment while leaving exact congener, form and stereoisomer correspondence unresolved.

### Retained PubChem activity rows

scope: unknown. Targets: naturalproductmech:mibig-2f5f003d07.

All 19 retained rows map to the same CID 5702105 and full structure key across 17 AIDs: ten active, eight inconclusive and one inactive. AID 2782 and AID 2783 each have rows for target protein accessions NP_000235 and NP_005924; these are not separate compound identifiers or independent chemical identities. Assay-specific values and target labels do not establish a molecular mechanism or the exact natural form; censored and missing values remain distinct.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI956-LOCAL | /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/polymyxin.yaml; whole owner | context_only | Whole stored owner assertions, literal chemistry and history; not independent natural-identity evidence. |
| SCI956-ROWS | /private/tmp/npm-review-work/shared-next-batch096-tentative/source-science-preparation/native-tentative96-owner-source-reconnaissance-DATA-001.json; /records/5/retained_rows; /records/5/supplemental_rows; /records/5/row_guards | supports | The whole owner and nine named retained/supplemental source arrays match the saved local provenance (21 retained rows; 2 official rows). Accepted actual intake preserves the whole owner, six official arrays and 37 source inputs. This supports exact local provenance, not independent natural identity; empty named arrays do not establish global absence. |
| SCI956-INTAKE | /private/tmp/npm-review-work/shared-next-batch096/native-current96-intake-reconciliation-001.json; /records/5 | partial | The original intake event passed strict/source-fidelity checks. The cited reconciliation is a later archive preserving that event and its original clock; accessed_at is the original intake completion, not the later archive creation or scientific verification time. |
| SCI956-ENCODINGS | /private/tmp/npm-review-work/shared-next-batch096-tentative/source-science-preparation/native-tentative96-ten-owner-dual-encoding-results-001.json; /records/5 | partial | Saved parses agree on declared full key HFMDLUQUEXNBOP-UHFFFAOYSA-N, formula C56H100N16O17S and Standard InChI. Saved SMILES stereo counts are [('Atom_Tetrahedral', 0, 13), ('Bond_Double', 0, 0)]; InChI counts are [('Atom_Tetrahedral', 0, 13), ('Bond_Double', 0, 11)]. Canonical isomeric/nonisomeric SMILES equality and direct atom correspondence retain their original saved values; representation-level disagreement is not automatically a natural-identity error. No new chemistry or stereochemical assignment was performed. |
| SCI956-PUB | /private/tmp/npm-review-work/shared-next-batch096-tentative/literature-preparation/public-metadata-six-initial-PubMed-001/pmid-19304848.xml; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract | partial | The own E681 abstract reports pmxABCDE, pmxE disruption and heterologous Bacillus subtilis production with L-Dab supplementation, without resolving the exact congener, sulfate form or complete stereochemistry. |
| SCI956-ANNOTATION | /private/tmp/npm-review-work/shared-next-batch096-tentative/literature-preparation/bgc-tentative96-polymyxin956-bounded-scientific-assessment-DATA-001.json; /stored_connectivity; /stereochemical_scope; /assay_provenance | partial | Saved graph and retained-row assessment traces the decapeptide/lactam, separate H2SO4 component, 13 unspecified sites and 19 assay rows for CID 5702105 across 17 AIDs. The duplicated AID 2782 and 2783 rows distinguish target protein accessions NP_000235 and NP_005924, not compound identifiers. |

## Limits And Additional Notes

- PMC2687177 failed before HTTP; its empty local artifact contains no primary text or identity confirmation. The exact route is held without retry.
- The polymyxin family label, partial stereochemistry and separate acid component do not resolve a unique natural E681 product.
- Assay identifiers and values remain source-specific mappings; no molecular-target claim or congener-specific potency is inferred.
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
review_id: 20261029T135940Z-polymyxin
title: Scientific review of polymyxin
started_at: '2026-10-29T13:15:06.192224Z'
finished_at: '2026-10-29T13:59:40.830759Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The saved structure is a partially specified polymyxin-like decapeptide with
  a separate sulfuric-acid component. The E681 abstract supports the pmx locus generally;
  exact congener, sulfate-form and natural stereochemical correspondence remain unresolved.
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
  - path: data/natural_products/amino_acids_and_peptides/polymyxin.yaml
    sha256: 838e9eec893d4e93a193884ab5212da932e430c04474128afbadcb41fb5a910c
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
- target_id: naturalproductmech:mibig-2f5f003d07
  path: data/natural_products/amino_acids_and_peptides/polymyxin.yaml
  label: polymyxin
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
    path: data/natural_products/amino_acids_and_peptides/polymyxin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
scope:
  description: 'Whole owner, all nine named local-source arrays, actual official intake,
    saved dual-encoding results and explicitly identified publication evidence. Source
    scope: Own PubMed abstract and saved graph/assay provenance only; primary route
    failed before HTTP. Unresolved curation questions: Resolve the E681 product identity
    and isolated form using a verified structural source before assigning a congener
    or filling stereochemistry. Any later evidence-supported change must use maintained
    source harmonization and pass strict validation, source reproduction and corpus
    checks.'
  selection: One record selected in canonical path order from the actual batch96 remaining-record
    catalogue; the whole owner and all named local source rows were read.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-2f5f003d07
  exclusions:
  - target: Full-owner scientific verification
    reason: Claim-specific assessments and limitations identify the evidence gaps
      remaining after this partial review.
  - target: Uninspected structural figures, spectra and supplementary files
    reason: These materials were outside the completed primary-text reading.
  - target: Automatic evidence-grade promotion, congener merging or structural replacement
    reason: No corpus change is authorized by this review.
  - target: Full primary article results
    reason: Only the identified abstract or front matter was available within the
      closed source epoch.
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
  - naturalproductmech:mibig-2f5f003d07
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
  - naturalproductmech:mibig-2f5f003d07
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
  - naturalproductmech:mibig-2f5f003d07
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
  - naturalproductmech:mibig-2f5f003d07
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
  - naturalproductmech:mibig-2f5f003d07
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/polymyxin.yaml
    --out /private/tmp/npm-review-work/956/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-29T13:15:07.551641Z. Original
    receipt: /private/tmp/npm-review-work/956/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
- check_id: SCI956-LOCAL
  name: Whole owner and raw-source fidelity
  status: passed
  required: true
  summary: The whole owner and nine named retained/supplemental source arrays match
    the saved local provenance (21 retained rows; 2 official rows). Accepted actual
    intake preserves the whole owner, six official arrays and 37 source inputs. This
    supports exact local provenance, not independent natural identity; empty named
    arrays do not establish global absence.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-LOCAL
  - SCI956-ROWS
  - SCI956-INTAKE
  scope_note: Local fidelity only; no complete natural-identity claim.
- check_id: SCI956-ENCODINGS
  name: Saved dual-encoding internal consistency
  status: passed
  required: true
  summary: Saved parses agree on declared full key HFMDLUQUEXNBOP-UHFFFAOYSA-N, formula
    C56H100N16O17S and Standard InChI. Saved SMILES stereo counts are [('Atom_Tetrahedral',
    0, 13), ('Bond_Double', 0, 0)]; InChI counts are [('Atom_Tetrahedral', 0, 13),
    ('Bond_Double', 0, 11)]. Canonical isomeric/nonisomeric SMILES equality and direct
    atom correspondence retain their original saved values; representation-level disagreement
    is not automatically a natural-identity error. No new chemistry or stereochemical
    assignment was performed.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-LOCAL
  - SCI956-ROWS
  - SCI956-ENCODINGS
  scope_note: Saved parse facts only; no new chemistry or natural-configuration proof.
- check_id: SCI956-SOURCE-SCOPE
  name: Claim-level source and saved-fact scope
  status: passed
  required: false
  summary: The cited source observations and bounded comparison preserve their original
    scope and clocks. This check does not certify complete natural identity.
  scope_note: Own PubMed abstract and saved graph/assay provenance only; primary route
    failed before HTTP.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-PUB
  - SCI956-ANNOTATION
evidence:
- evidence_id: SCI956-LOCAL
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/amino_acids_and_peptides/polymyxin.yaml
  locator: whole owner
  accessed_at: '2026-10-29T12:12:23.560653Z'
  snapshot_sha256: 838e9eec893d4e93a193884ab5212da932e430c04474128afbadcb41fb5a910c
  support: context_only
  summary: Whole stored owner assertions, literal chemistry and history; not independent
    natural-identity evidence.
- evidence_id: SCI956-ROWS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch096-tentative/source-science-preparation/native-tentative96-owner-source-reconnaissance-DATA-001.json
  locator: /records/5/retained_rows; /records/5/supplemental_rows; /records/5/row_guards
  accessed_at: '2026-10-29T12:12:23.560653Z'
  snapshot_sha256: d5080bb7d48c0bf1dfe0bf83acedbcbf52af323aa089859d0e73be8279771768
  support: supports
  summary: The whole owner and nine named retained/supplemental source arrays match
    the saved local provenance (21 retained rows; 2 official rows). Accepted actual
    intake preserves the whole owner, six official arrays and 37 source inputs. This
    supports exact local provenance, not independent natural identity; empty named
    arrays do not establish global absence.
- evidence_id: SCI956-INTAKE
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch096/native-current96-intake-reconciliation-001.json
  locator: /records/5
  accessed_at: '2026-10-29T13:15:07.608838Z'
  snapshot_sha256: ad036657d1c39d4b5b71b030d3123271ed47b3d798933439ea8d47c06f642fb3
  support: partial
  summary: The original intake event passed strict/source-fidelity checks. The cited
    reconciliation is a later archive preserving that event and its original clock;
    accessed_at is the original intake completion, not the later archive creation
    or scientific verification time.
- evidence_id: SCI956-ENCODINGS
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch096-tentative/source-science-preparation/native-tentative96-ten-owner-dual-encoding-results-001.json
  locator: /records/5
  accessed_at: '2026-10-29T12:21:30.443686Z'
  snapshot_sha256: b3d038c839dd0983f7e919caebd0da4a042d6e276dc6a5118369f99a6ef50371
  support: partial
  summary: Saved parses agree on declared full key HFMDLUQUEXNBOP-UHFFFAOYSA-N, formula
    C56H100N16O17S and Standard InChI. Saved SMILES stereo counts are [('Atom_Tetrahedral',
    0, 13), ('Bond_Double', 0, 0)]; InChI counts are [('Atom_Tetrahedral', 0, 13),
    ('Bond_Double', 0, 11)]. Canonical isomeric/nonisomeric SMILES equality and direct
    atom correspondence retain their original saved values; representation-level disagreement
    is not automatically a natural-identity error. No new chemistry or stereochemical
    assignment was performed.
- evidence_id: SCI956-PUB
  kind: primary_source
  reference: /private/tmp/npm-review-work/shared-next-batch096-tentative/literature-preparation/public-metadata-six-initial-PubMed-001/pmid-19304848.xml
  locator: ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract
  accessed_at: '2026-10-29T12:52:39.737071Z'
  snapshot_sha256: 1353c92562f214ab58c57de92b93366a5eb9e250d06de5a44db6143c63314a5a
  support: partial
  summary: The own E681 abstract reports pmxABCDE, pmxE disruption and heterologous
    Bacillus subtilis production with L-Dab supplementation, without resolving the
    exact congener, sulfate form or complete stereochemistry.
- evidence_id: SCI956-ANNOTATION
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch096-tentative/literature-preparation/bgc-tentative96-polymyxin956-bounded-scientific-assessment-DATA-001.json
  locator: /stored_connectivity; /stereochemical_scope; /assay_provenance
  accessed_at: '2026-10-29T13:23:14.411297Z'
  snapshot_sha256: 4b0654e21338b37b13863ff6a6c5c226482b92e604b10c96e1660e6247838207
  support: partial
  summary: Saved graph and retained-row assessment traces the decapeptide/lactam,
    separate H2SO4 component, 13 unspecified sites and 19 assay rows for CID 5702105
    across 17 AIDs. The duplicated AID 2782 and 2783 rows distinguish target protein
    accessions NP_000235 and NP_005924, not compound identifiers.
assessments:
- assessment_id: SCI956-LOCAL
  area: provenance
  topic: Whole owner and exact local-source fidelity
  outcome: supported
  summary: The whole owner and nine named retained/supplemental source arrays match
    the saved local provenance (21 retained rows; 2 official rows). Accepted actual
    intake preserves the whole owner, six official arrays and 37 source inputs. This
    supports exact local provenance, not independent natural identity; empty named
    arrays do not establish global absence.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-LOCAL
  - SCI956-ROWS
  - SCI956-INTAKE
- assessment_id: SCI956-ENCODINGS
  area: consistency
  topic: Saved dual-encoding scope
  outcome: supported
  summary: Saved parses agree on declared full key HFMDLUQUEXNBOP-UHFFFAOYSA-N, formula
    C56H100N16O17S and Standard InChI. Saved SMILES stereo counts are [('Atom_Tetrahedral',
    0, 13), ('Bond_Double', 0, 0)]; InChI counts are [('Atom_Tetrahedral', 0, 13),
    ('Bond_Double', 0, 11)]. Canonical isomeric/nonisomeric SMILES equality and direct
    atom correspondence retain their original saved values; representation-level disagreement
    is not automatically a natural-identity error. No new chemistry or stereochemical
    assignment was performed.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-LOCAL
  - SCI956-ROWS
  - SCI956-ENCODINGS
- assessment_id: SCI956-CONNECTIVITY
  area: identity
  topic: Peptide and component boundary
  outcome: supported
  summary: Saved connectivity traces fatty-acyl–Dab–Thr–Dab–Dab–Dab–Phe–Leu–Dab–Dab–Thr,
    with the residue-10 carbonyl joined to the residue-4 sidechain nitrogen. The separate
    H2SO4 component is not a covalent sulfation or an explicitly encoded sulfate dianion.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-LOCAL
  - SCI956-ENCODINGS
  - SCI956-ANNOTATION
- assessment_id: SCI956-STEREO
  area: identity
  topic: Partially specified stereochemistry
  outcome: unknown
  summary: 'The graph retains 13 unspecified tetrahedral sites: ten alpha carbons,
    two threonine beta carbons and the fatty-acyl C6 site. These declared gaps and
    the sulfate-related component do not automatically establish a wrong natural structure
    or a specific E681 congener.'
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-LOCAL
  - SCI956-ENCODINGS
  - SCI956-ANNOTATION
  - SCI956-PUB
- assessment_id: SCI956-FORMULA
  area: consistency
  topic: Component-total formula equivalence
  outcome: supported
  summary: The literal dotted formula C56H98N16O13.H2O4S and aggregate C56H100N16O17S
    have the same elemental totals. The saved literal formula-comparison flag remains
    false as a formatting distinction, not a chemical mismatch.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-ENCODINGS
  - SCI956-ANNOTATION
- assessment_id: SCI956-LOCUS
  area: evidence
  topic: E681 locus versus exact product identity
  outcome: supported
  summary: The abstract reports pmxABCDE involvement, loss after pmxE disruption and
    heterologous Bacillus subtilis production with L-Dab supplementation. This supports
    the general locus experiment while leaving exact congener, form and stereoisomer
    correspondence unresolved.
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-PUB
  - SCI956-ROWS
  - SCI956-ANNOTATION
- assessment_id: SCI956-ASSAYS
  area: scope
  topic: Retained PubChem activity rows
  outcome: unknown
  summary: 'All 19 retained rows map to the same CID 5702105 and full structure key
    across 17 AIDs: ten active, eight inconclusive and one inactive. AID 2782 and
    AID 2783 each have rows for target protein accessions NP_000235 and NP_005924;
    these are not separate compound identifiers or independent chemical identities.
    Assay-specific values and target labels do not establish a molecular mechanism
    or the exact natural form; censored and missing values remain distinct.'
  target_ids:
  - naturalproductmech:mibig-2f5f003d07
  evidence_ids:
  - SCI956-ROWS
  - SCI956-ANNOTATION
findings: []
actions: []
limitations:
- PMC2687177 failed before HTTP; its empty local artifact contains no primary text
  or identity confirmation. The exact route is held without retry.
- The polymyxin family label, partial stereochemistry and separate acid component
  do not resolve a unique natural E681 product.
- Assay identifiers and values remain source-specific mappings; no molecular-target
  claim or congener-specific potency is inferred.
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
