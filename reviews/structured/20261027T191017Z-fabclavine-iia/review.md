# Scientific review of fabclavine IIa

- Review: 20261027T191017Z-fabclavine-iia
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T19:09:18.603115Z
- Finished UTC: 2026-10-27T19:10:17.179417Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fabclavine IIa has internally consistent retained encodings and family-level abstract support for peptide-polyketide-polyamino hybrids from Xenorhabdus. Its 14 unspecified tetrahedral carbon sites remain unresolved. The available abstract does not independently establish the exact IIa natural structure, stock, locus interval or individual-congener activity.

## Scope And Provenance

Review fabclavine IIa identity, retained source assertions and two local chemical encodings. Interpret the inspected PMID 24532262 abstract as family-level evidence for Xenorhabdus peptide-polyketide-polyamino hybrids, preserving unspecified stereochemistry and the correlated producer/locus tiers.

Selection: One owner selected in canonical unreviewed path order as campaign review 701; whole retained owner, referenced components and local source rows read, with bounded scientific interpretation.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a562b76392 | data/natural_products/amino_acids_and_peptides/fabclavine-iia.yaml | generated | fabclavine IIa |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-a562b76392 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-a562b76392 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-a562b76392 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-a562b76392 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-a562b76392 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | naturalproductmech:mibig-a562b76392 | The selected owner passed the documented strict validator. This establishes configured consistency only. |
| Saved two-encoding internal consistency | passed | True | naturalproductmech:mibig-a562b76392 | Saved RDKit 2026.03.5 results regenerate BPJNOLJFUQBQGC-UHFFFAOYSA-N from both owner encodings, with formula C67H123N15O13, one fragment and formal charge zero. Standard InChI agrees between encodings. These results support internal encoding consistency only. |
| Exact retained owner and source-array joins | passed | True | naturalproductmech:mibig-a562b76392 | The seven retained arrays and two supplemental arrays reproduce their exact ordered row guards and source table indices. This checks the original frozen local inventory; current official intake was reconciled separately. |
| Own metadata identity and access | passed | True | naturalproductmech:mibig-a562b76392 | The retained complete HTTP 200 response owns PMID 24532262 and DOI 10.1002/cbic.201300802 in its ArticleIdList. Its original HTTP access object and later ROOT reading clock remain separate. |
| Exact natural identity and configuration | unavailable | True | naturalproductmech:mibig-a562b76392 | Both retained fabclavine IIa encodings have 14 unspecified tetrahedral carbon sites, consistent with the existing stereo_complete=false declaration. Seven additional C(-O)=N flags in the parsed InChI representation are imidic forms, not seven missing C=C configurations. No natural stereoisomer is established by these diagnostics. The family abstract does not resolve the individual congener structure. |
| Current chemical, taxon and sequence authorities | unavailable | True | naturalproductmech:mibig-a562b76392 | The retained accessions and source labels have not been checked against current external authorities in this review scope. Local full-key agreement does not verify natural identity, stock identity or locus provenance. |

## Scientific And Domain Assessments

### Internal chemical encoding

representation: supported. Targets: naturalproductmech:mibig-a562b76392.

Saved RDKit 2026.03.5 results regenerate BPJNOLJFUQBQGC-UHFFFAOYSA-N from both owner encodings, with formula C67H123N15O13, one fragment and formal charge zero. Standard InChI agrees between encodings. These results support internal encoding consistency only.

### Own abstract and family-level discovery

evidence: supported. Targets: naturalproductmech:mibig-a562b76392.

The own PMID 24532262 abstract describes fabclavines as mixtures of nonribosomal peptide-polyketide hybrids linked to a polyamino moiety, characterized by detailed NMR and MS. It reports two Xenorhabdus strains, cluster identification and initial mutagenesis supporting a proposed pathway, including an unusual fatty acid synthase contribution. It does not name IIa or IIb individually.

### Exact congener and natural configuration

identity: unknown. Targets: naturalproductmech:mibig-a562b76392.

Both retained fabclavine IIa encodings have 14 unspecified tetrahedral carbon sites, consistent with the existing stereo_complete=false declaration. Seven additional C(-O)=N flags in the parsed InChI representation are imidic forms, not seven missing C=C configurations. No natural stereoisomer is established by these diagnostics. The MIBiG row names fabclavine IIa at compound index 3; the own abstract does not independently identify that entry as the experimentally characterized material.

### Producer and exact stock

provenance: unknown. Targets: naturalproductmech:mibig-a562b76392.

The retained MIBiG producer is Xenorhabdus budapestensis, NCBITaxon:290110, with BGC_CORRELATED evidence. The abstract reports two Xenorhabdus strains without naming their stocks or assigning IIa individually. It therefore supports the family context but does not independently verify this exact producer claim.

### Biosynthetic locus and evidence grade

provenance: unknown. Targets: naturalproductmech:mibig-a562b76392.

BGC0001130 version 5 is retained at NIBS01000014.1:52424-100650 with NRPS and PKS classes. Its locus grade CLUSTER_CORRELATED derives from gene expression correlated with compound production, while the citation is ENTRY-level. The abstract reports cluster analysis and initial mutagenesis, but does not identify this accession interval or establish which experiment applies to this congener. The retained grade is not upgraded.

### Individual-congener activity

evidence: unknown. Targets: naturalproductmech:mibig-a562b76392.

The abstract reports antibacterial, antifungal and other eukaryotic-cell activity for fabclavines collectively. It supplies no IIa-specific quantitative potency, target assay or evidence that every congener has identical activity. The ecological protection role remains the authors’ hypothesis. No bioactivity annotation is present in this local owner.

### Class labels and causal coverage

completeness: unknown. Targets: naturalproductmech:mibig-a562b76392.

The retained NRPS/PKS and model-derived lipopeptide labels are broadly compatible with the family account. The predicted fatty acid synthase contribution is not a contradiction of those broad labels. The NPClassifier output is not experimental structure proof, and no causal graph is retained for this owner. Exact congener structure and biosynthetic detail remain incompletely supported.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI701-LOCAL | /private/tmp/npm-review-work/shared-next-batch071-tentative/tentative-owner-source-inventory-001.json; /entries/0/owner_document; /entries/0/rows; /entries/0/row_guards; /entries/0/supplemental_retained_rows | context_only | The whole retained fabclavine IIa owner and seven source arrays contain one exact-key MIBiG compound row and one NPClassifier row. The two supplemental arrays are empty. The source grades, citation tier, original histories and distinct congener identity are preserved. |
| SCI701-CHEM | /private/tmp/npm-review-work/shared-next-batch071-tentative/source-science-preparation/root-tentative71-local-chemical-consistency-and-neighbors-001.json; /records/0/comparisons; /records/0/smiles/computed; /records/0/inchi/computed; /records/0/smiles/unspecified_neighbors; /records/0/inchi/unspecified_neighbors | supports | Saved RDKit 2026.03.5 results regenerate BPJNOLJFUQBQGC-UHFFFAOYSA-N from both owner encodings, with formula C67H123N15O13, one fragment and formal charge zero. Standard InChI agrees between encodings. These results support internal encoding consistency only. Both retained fabclavine IIa encodings have 14 unspecified tetrahedral carbon sites, consistent with the existing stereo_complete=false declaration. Seven additional C(-O)=N flags in the parsed InChI representation are imidic forms, not seven missing C=C configurations. No natural stereoisomer is established by these diagnostics. |
| SCI701-OWN-ABSTRACT | /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-metadata-001/pmid-24532262.xml; ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle; ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList/ArticleId | partial | The own PMID 24532262 abstract describes fabclavines as mixtures of nonribosomal peptide-polyketide hybrids linked to a polyamino moiety, characterized by detailed NMR and MS. It reports two Xenorhabdus strains, cluster identification and initial mutagenesis supporting a proposed pathway, including an unusual fatty acid synthase contribution. It does not name IIa or IIb individually. |
| SCI701-ROOT-CHEM-READ | /private/tmp/npm-review-work/shared-next-batch071-tentative/source-science-preparation/root-tentative71-local-chemical-reading-001.json; /records/0; /interpretation; /scope | context_only | ROOT subsequently read the saved chemical representation results and their limits. The original computation interval is preserved separately; this reading is not a new calculation or natural-identity verification. |

## Limits And Additional Notes

- Paper evidence is limited to the saved own citation, title, full supplied abstract and ArticleIdList. Full primary text, supplementary information, spectra and individual natural configuration assignments were not inspected.
- The abstract does not name IIa or provide its individual potency, exact producer stock or accession-level locus evidence. Family, mixture and congener claims remain distinct.
- Current chemical, taxon and sequence authorities remain unverified. Agreement between local encodings does not establish the experimental natural structure.
- Original inventory capture, ROOT local reading, chemical computation, HTTP access and later interpretation clocks remain distinct. Full-owner scientific verification remains false.
- The retained stereochemical incompleteness and limits of the available abstract identify unresolved evidence needs; they do not alone establish a corrective finding.
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
review_id: 20261027T191017Z-fabclavine-iia
title: Scientific review of fabclavine IIa
started_at: '2026-10-27T19:09:18.603115Z'
finished_at: '2026-10-27T19:10:17.179417Z'
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Fabclavine IIa has internally consistent retained encodings and family-level
  abstract support for peptide-polyketide-polyamino hybrids from Xenorhabdus. Its
  14 unspecified tetrahedral carbon sites remain unresolved. The available abstract
  does not independently establish the exact IIa natural structure, stock, locus interval
  or individual-congener activity.
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
  - path: data/natural_products/amino_acids_and_peptides/fabclavine-iia.yaml
    sha256: 53559fd69b184700fbd98a5ae8b9b2f5207bf4e1b68f7c2c96886d406238259a
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
- target_id: naturalproductmech:mibig-a562b76392
  path: data/natural_products/amino_acids_and_peptides/fabclavine-iia.yaml
  label: fabclavine IIa
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
  description: Review fabclavine IIa identity, retained source assertions and two
    local chemical encodings. Interpret the inspected PMID 24532262 abstract as family-level
    evidence for Xenorhabdus peptide-polyketide-polyamino hybrids, preserving unspecified
    stereochemistry and the correlated producer/locus tiers.
  selection: One owner selected in canonical unreviewed path order as campaign review
    701; whole retained owner, referenced components and local source rows read, with
    bounded scientific interpretation.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a562b76392
  exclusions:
  - target: Uninspected experiments and external authority claims
    reason: The abstract does not assign the exact IIa structure, natural stereochemistry,
      producing stock, locus interval or individual-congener potency. Full primary
      and supplementary evidence remain uninspected.
  - target: Whole-owner scientific verification
    reason: The complete local owner and retained rows were read, but full-owner scientific
      verification remains false. This report assesses the explicitly bounded evidence;
      configured validation does not establish all natural-product claims.
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
    Reused for batch071 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch071. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a562b76392
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
    Reused for batch071 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch071. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a562b76392
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
    Reused for batch071 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch071. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a562b76392
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
    Reused for batch071 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch071. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a562b76392
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
    Reused for batch071 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch071. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-a562b76392
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The selected owner passed the documented strict validator. This establishes
    configured consistency only.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/fabclavine-iia.yaml
    --out /private/tmp/npm-review-work/701/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual intake execution finished 2026-10-27T19:09:20.074292Z. Original
    receipt: /private/tmp/npm-review-work/701/strict-receipt.json.'
  target_ids:
  - naturalproductmech:mibig-a562b76392
- check_id: SCI701-ENCODING
  name: Saved two-encoding internal consistency
  status: passed
  required: true
  summary: Saved RDKit 2026.03.5 results regenerate BPJNOLJFUQBQGC-UHFFFAOYSA-N from
    both owner encodings, with formula C67H123N15O13, one fragment and formal charge
    zero. Standard InChI agrees between encodings. These results support internal
    encoding consistency only.
  evidence_ids:
  - SCI701-CHEM
  target_ids:
  - naturalproductmech:mibig-a562b76392
- check_id: SCI701-LOCAL-JOINS
  name: Exact retained owner and source-array joins
  status: passed
  required: true
  summary: The seven retained arrays and two supplemental arrays reproduce their exact
    ordered row guards and source table indices. This checks the original frozen local
    inventory; current official intake was reconciled separately.
  evidence_ids:
  - SCI701-LOCAL
  target_ids:
  - naturalproductmech:mibig-a562b76392
- check_id: SCI701-OWN-ID
  name: Own metadata identity and access
  status: passed
  required: true
  summary: The retained complete HTTP 200 response owns PMID 24532262 and DOI 10.1002/cbic.201300802
    in its ArticleIdList. Its original HTTP access object and later ROOT reading clock
    remain separate.
  evidence_ids:
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- check_id: SCI701-NATURAL-IDENTITY
  name: Exact natural identity and configuration
  status: unavailable
  required: true
  summary: Both retained fabclavine IIa encodings have 14 unspecified tetrahedral
    carbon sites, consistent with the existing stereo_complete=false declaration.
    Seven additional C(-O)=N flags in the parsed InChI representation are imidic forms,
    not seven missing C=C configurations. No natural stereoisomer is established by
    these diagnostics. The family abstract does not resolve the individual congener
    structure.
  evidence_ids:
  - SCI701-CHEM
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- check_id: SCI701-AUTHORITIES
  name: Current chemical, taxon and sequence authorities
  status: unavailable
  required: true
  summary: The retained accessions and source labels have not been checked against
    current external authorities in this review scope. Local full-key agreement does
    not verify natural identity, stock identity or locus provenance.
  evidence_ids:
  - SCI701-LOCAL
  - SCI701-CHEM
  target_ids:
  - naturalproductmech:mibig-a562b76392
evidence:
- evidence_id: SCI701-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch071-tentative/tentative-owner-source-inventory-001.json
  accessed_at: '2026-10-27T18:07:36.503995Z'
  locator: /entries/0/owner_document; /entries/0/rows; /entries/0/row_guards; /entries/0/supplemental_retained_rows
  snapshot_sha256: 53f900bba3e6dfe54d07ff9a08cd5fb64593163e809ecbeaa6748b322a48f883
  support: context_only
  summary: The whole retained fabclavine IIa owner and seven source arrays contain
    one exact-key MIBiG compound row and one NPClassifier row. The two supplemental
    arrays are empty. The source grades, citation tier, original histories and distinct
    congener identity are preserved.
- evidence_id: SCI701-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch071-tentative/source-science-preparation/root-tentative71-local-chemical-consistency-and-neighbors-001.json
  accessed_at: '2026-10-27T18:15:48.609294Z'
  locator: /records/0/comparisons; /records/0/smiles/computed; /records/0/inchi/computed;
    /records/0/smiles/unspecified_neighbors; /records/0/inchi/unspecified_neighbors
  snapshot_sha256: 3c7b05f7372948747c603d7b006b1e20dfb7e1e51dde5710676c02b15320ca4a
  support: supports
  summary: Saved RDKit 2026.03.5 results regenerate BPJNOLJFUQBQGC-UHFFFAOYSA-N from
    both owner encodings, with formula C67H123N15O13, one fragment and formal charge
    zero. Standard InChI agrees between encodings. These results support internal
    encoding consistency only. Both retained fabclavine IIa encodings have 14 unspecified
    tetrahedral carbon sites, consistent with the existing stereo_complete=false declaration.
    Seven additional C(-O)=N flags in the parsed InChI representation are imidic forms,
    not seven missing C=C configurations. No natural stereoisomer is established by
    these diagnostics.
- evidence_id: SCI701-OWN-ABSTRACT
  kind: primary_source
  reference: /private/tmp/npm-review-work/shared-next-batch070-tentative/literature-preparation/public-metadata-001/pmid-24532262.xml
  accessed_at: '2026-10-27T17:35:16.896126Z'
  locator: ./PubmedArticle/MedlineCitation/PMID; ./PubmedArticle/MedlineCitation/Article/ArticleTitle;
    ./PubmedArticle/MedlineCitation/Article/Abstract/AbstractText; ./PubmedArticle/PubmedData/ArticleIdList/ArticleId
  snapshot_sha256: 3a3b80ffc7ead1908333f2772bca8f3f78b7863e2d0973e2fd85263794fe1e51
  support: partial
  summary: The own PMID 24532262 abstract describes fabclavines as mixtures of nonribosomal
    peptide-polyketide hybrids linked to a polyamino moiety, characterized by detailed
    NMR and MS. It reports two Xenorhabdus strains, cluster identification and initial
    mutagenesis supporting a proposed pathway, including an unusual fatty acid synthase
    contribution. It does not name IIa or IIb individually.
- evidence_id: SCI701-ROOT-CHEM-READ
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch071-tentative/source-science-preparation/root-tentative71-local-chemical-reading-001.json
  accessed_at: '2026-10-27T18:16:57.571265Z'
  locator: /records/0; /interpretation; /scope
  snapshot_sha256: 20cbb5354832895441e3a6f8dc8fd0aa56c639782c708dd620345bd55ae363fb
  support: context_only
  summary: ROOT subsequently read the saved chemical representation results and their
    limits. The original computation interval is preserved separately; this reading
    is not a new calculation or natural-identity verification.
assessments:
- assessment_id: SCI701-ENCODING
  area: representation
  topic: Internal chemical encoding
  outcome: supported
  summary: Saved RDKit 2026.03.5 results regenerate BPJNOLJFUQBQGC-UHFFFAOYSA-N from
    both owner encodings, with formula C67H123N15O13, one fragment and formal charge
    zero. Standard InChI agrees between encodings. These results support internal
    encoding consistency only.
  evidence_ids:
  - SCI701-CHEM
  - SCI701-ROOT-CHEM-READ
  target_ids:
  - naturalproductmech:mibig-a562b76392
- assessment_id: SCI701-FAMILY
  area: evidence
  topic: Own abstract and family-level discovery
  outcome: supported
  summary: The own PMID 24532262 abstract describes fabclavines as mixtures of nonribosomal
    peptide-polyketide hybrids linked to a polyamino moiety, characterized by detailed
    NMR and MS. It reports two Xenorhabdus strains, cluster identification and initial
    mutagenesis supporting a proposed pathway, including an unusual fatty acid synthase
    contribution. It does not name IIa or IIb individually.
  evidence_ids:
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- assessment_id: SCI701-IDENTITY
  area: identity
  topic: Exact congener and natural configuration
  outcome: unknown
  summary: Both retained fabclavine IIa encodings have 14 unspecified tetrahedral
    carbon sites, consistent with the existing stereo_complete=false declaration.
    Seven additional C(-O)=N flags in the parsed InChI representation are imidic forms,
    not seven missing C=C configurations. No natural stereoisomer is established by
    these diagnostics. The MIBiG row names fabclavine IIa at compound index 3; the
    own abstract does not independently identify that entry as the experimentally
    characterized material.
  evidence_ids:
  - SCI701-LOCAL
  - SCI701-CHEM
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- assessment_id: SCI701-PRODUCER
  area: provenance
  topic: Producer and exact stock
  outcome: unknown
  summary: The retained MIBiG producer is Xenorhabdus budapestensis, NCBITaxon:290110,
    with BGC_CORRELATED evidence. The abstract reports two Xenorhabdus strains without
    naming their stocks or assigning IIa individually. It therefore supports the family
    context but does not independently verify this exact producer claim.
  evidence_ids:
  - SCI701-LOCAL
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- assessment_id: SCI701-LOCUS
  area: provenance
  topic: Biosynthetic locus and evidence grade
  outcome: unknown
  summary: BGC0001130 version 5 is retained at NIBS01000014.1:52424-100650 with NRPS
    and PKS classes. Its locus grade CLUSTER_CORRELATED derives from gene expression
    correlated with compound production, while the citation is ENTRY-level. The abstract
    reports cluster analysis and initial mutagenesis, but does not identify this accession
    interval or establish which experiment applies to this congener. The retained
    grade is not upgraded.
  evidence_ids:
  - SCI701-LOCAL
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- assessment_id: SCI701-ACTIVITY
  area: evidence
  topic: Individual-congener activity
  outcome: unknown
  summary: The abstract reports antibacterial, antifungal and other eukaryotic-cell
    activity for fabclavines collectively. It supplies no IIa-specific quantitative
    potency, target assay or evidence that every congener has identical activity.
    The ecological protection role remains the authors’ hypothesis. No bioactivity
    annotation is present in this local owner.
  evidence_ids:
  - SCI701-LOCAL
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
- assessment_id: SCI701-CLASS-COVERAGE
  area: completeness
  topic: Class labels and causal coverage
  outcome: unknown
  summary: The retained NRPS/PKS and model-derived lipopeptide labels are broadly
    compatible with the family account. The predicted fatty acid synthase contribution
    is not a contradiction of those broad labels. The NPClassifier output is not experimental
    structure proof, and no causal graph is retained for this owner. Exact congener
    structure and biosynthetic detail remain incompletely supported.
  evidence_ids:
  - SCI701-LOCAL
  - SCI701-CHEM
  - SCI701-OWN-ABSTRACT
  target_ids:
  - naturalproductmech:mibig-a562b76392
findings: []
actions: []
limitations:
- Paper evidence is limited to the saved own citation, title, full supplied abstract
  and ArticleIdList. Full primary text, supplementary information, spectra and individual
  natural configuration assignments were not inspected.
- The abstract does not name IIa or provide its individual potency, exact producer
  stock or accession-level locus evidence. Family, mixture and congener claims remain
  distinct.
- Current chemical, taxon and sequence authorities remain unverified. Agreement between
  local encodings does not establish the experimental natural structure.
- Original inventory capture, ROOT local reading, chemical computation, HTTP access
  and later interpretation clocks remain distinct. Full-owner scientific verification
  remains false.
- The retained stereochemical incompleteness and limits of the available abstract
  identify unresolved evidence needs; they do not alone establish a corrective finding.
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
