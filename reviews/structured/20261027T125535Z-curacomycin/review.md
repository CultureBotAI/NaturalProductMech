# Scientific review of curacomycin

- Review: 20261027T125535Z-curacomycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-27T12:41:49.812704Z
- Finished UTC: 2026-10-27T12:55:35.024431Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Local encodings agree with the retained chlorinated curacomycin structure. A provisional major finding identifies a likely cross-congener citation assignment in the ChEBI-derived S. noursei NBRC 15452 occurrence: the cited abstract assigns that strain to dechlorocuracomycin. Full primary reconciliation and a maintained-source correction are proposed; other identity, strain and locus questions remain unresolved.

## Scope And Provenance

Whole retained owner and source rows, local chemical consistency, inspected own publication metadata and supplied abstracts; exact primary and current-authority verification is partial.

Selection: One resolved record in canonical path order from the unreviewed corpus; current official intake reconciled to the earlier evidence snapshots.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 14373517042b407747272446f79953ae86d51fa4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156426 | data/natural_products/amino_acids_and_peptides/curacomycin.yaml | generated | curacomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corpus path and filing integrity | passed | True | CHEBI:156426 | Fresh canonical corpus gate passed:3116 lockfile rows/files, each at its pinned path. |
| Corpus reproduction | passed | True | CHEBI:156426 | Fresh canonical reproduction gate passed:all3116 records byte-identical to source seeding; source warnings remain retained. |
| Native deterministic review queue | passed | True | CHEBI:156426 | Fresh deterministic review queue completed:8922 rows across12 queues. Queue output is not scientific-review coverage. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:156426 | Fresh configured identifier-label gate passed:13472canonical,657synonym,35exception;499non-blocking mismatches and4898no-adapter skips remain explicit. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:156426 | Canonical just qc completed with actual terminal exit0:1024 tests passed,4 skipped,2 dependency warnings;3116 records passed closed schema validation, site freshness, byte reproduction and lockfile integrity.22 governed artifacts and15 raw inventories passed. Prior DNS failed001 remains preserved. |
| Native strict target validation | passed | True | CHEBI:156426 | The exact selected owner passed the documented strict validator; this is a configured consistency result. |
| Saved local owner-encoding consistency | passed | True | CHEBI:156426 | The saved local computation reproduces the declared full Standard InChIKey CUXAULQHGRSWLF-IKVCUCANSA-N from both owner encodings and reports formula C37H56ClN9O8. Both representations have 2 unspecified tetrahedral centers. This is retained-encoding consistency, not proof of the natural absolute configuration. |
| Own article identifier and abstract applicability | passed | True | CHEBI:156426 | The stored response own identifiers match this exact cited publication; the complete own abstract and title were read. Publication identity does not establish all retained compound/strain/locus assertions. |
| Full exact-material and current authority verification | unavailable | True | CHEBI:156426 | Full primary/SI, natural stereochemistry, exact MIBiG accession-to-product mapping and current authorities remain unverified. The separate provisional occurrence-citation finding is based on the inspected abstract and exact retained ChEBI row. |

## Scientific And Domain Assessments

### Named material and source-specific biological-origin support

evidence: supported. Targets: CHEBI:156426.

The own Crossref abstract names curacomycin1 as a six-residue chlorinated cyclic peptide isolated from S. curacoi NBRC12761T, separately from dechlorocuracomycin2 from S. noursei NBRC15452T. This supports bounded curacomycin material and S. curacoi origin context. Repeated MIBiG, LOTUS and ChEBI citations here all refer to the same paper and are not independent publications.

### Retained encodings and limited local stereochemistry

representation: supported. Targets: CHEBI:156426.

The saved local computation reproduces the declared full Standard InChIKey CUXAULQHGRSWLF-IKVCUCANSA-N from both owner encodings and reports formula C37H56ClN9O8. Both representations have 2 unspecified tetrahedral centers. This is retained-encoding consistency, not proof of the natural absolute configuration. Unspecified tetrahedral centers occur in both owner representations, consistent with the retained stereo_complete=false scope. This is representational incompleteness, not evidence identifying the missing natural configurations. Two unspecified adjacent carbon centers are SMILES atoms38/39 (InChI28/29); one has a nitrogen neighbor and the other an OH neighbor. They lie in the explicit C(C(O)C(N)=O) peptide segment; no published atom numbering or natural configuration is assigned. Parsed-InChI C=N flags are interpreted only through the saved neighbor addendum; this interpretation reuses the saved two-encoding result. The exact retained ChEBI alternative failed its original parse and its comparison remains null; no retry, repaired SMILES or replacement structure is asserted.

### Exact congener/strain/locus and natural-identity scope

provenance: concern. Targets: CHEBI:156426.

The retained S. noursei NBRC 15452 occurrence cites an abstract assigning that strain to dechlorocuracomycin. This is a provisional major citation-applicability finding on the chlorinated curacomycin owner; natural production capability and full-paper observations remain unresolved.

### Pinned cross-corpus structure link

consistency: supported. Targets: CHEBI:156426.

The related-record link reproduces the exact full-key row in the pinned sibling export; no mechanism or current external equivalence is inferred.

## Findings

### SCI637-OCCURRENCE-CITATION: Cited S. noursei observation appears to belong to dechlorocuracomycin

major / open / provisional; issue key: npm-chebi156426-noursei15452-curacomycin-citation.

The CHEBI:156426 occurrence for Streptomyces noursei NBRC 15452 cites DOI:10.1002/ajoc.201700433. Its inspected abstract assigns curacomycin (compound 1) to S. curacoi NBRC 12761 and dechlorocuracomycin (compound 2) to S. noursei NBRC 15452, respectively. The cited isolation does not support the chlorinated-congener occurrence as currently placed. The finding is provisional because full text and supplementary material could contain additional observations; it does not assert that this species cannot produce curacomycin.

## Recommended Actions And Acceptance Checks

### SCI637-RECONCILE-OCCURRENCE

Inspect the full cited article and supplementary material for the exact chlorinated curacomycin/strain pairing. If the source contains additional supporting material, qualify the occurrence with that exact evidence. Otherwise implement and document a strictly row-pinned ChEBI-origin exclusion or qualification consumer before adopting a curation decision. The existing LOTUS exclusion table does not affect ChEBI origins, and curation/decisions.tsv is not consumed. Preserve the raw seven-field row and its explanation; keep other occurrences, structures, producers and loci outside this bounded correction.

- Reconcile compound numbers 1 and 2 with both exact strains in full primary material; record the evidence and whether it supports retention, qualification or withdrawal of this occurrence.
- Exact row removal only; preserve a different strain, DOI, ChEBI ID and full-key owner.
- Reject any drift in all seven source fields including blanks, missing/duplicate source matches, duplicate/unused decisions and incorrect owner join.
- Raw inventories and unaffected records remain byte-identical; recompute occurrence facets and protect table-owned adjudication from stale carried YAML.
- Record retains its two S.curacoi occurrences, structure, producers and clusters.
- Require exact current CHEBI:156426/full-key/NCBITaxon:1971/NBRC15452/DOI match and whole raw-row digest bce1a9c0367d52bc595f837caffa035c9db7f981656b2248a68988d9ac9b3eb7 before any future decision.
- After separately authorized implementation and canary inspection, demonstrate strict validation, byte reproduction, provenance and corpus checks; no such commands ran in this task.
- After an implemented correction, run just seed, inspect just seed-canary CHEBI:156426, then run just validate-strict data/natural_products/amino_acids_and_peptides/curacomycin.yaml, just verify-reproduction, just provenance-check, just verify-corpus --summary and just qc. These are proposed future checks, not results of this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| SCI637-LOCAL | /private/tmp/npm-review-work/shared-next-batch064-tentative/tentative-owner-source-inventory-001.json; /entries/6/owner_document; /entries/6/rows | context_only | Exact retained curacomycin owner and all seven source arrays (7 rows), including original imported producer/occurrence/locus grades and history. The current official intake matches these retained local claims. |
| SCI637-CHEM | /private/tmp/npm-review-work/shared-next-batch064-tentative/source-science-preparation/root-tentative64-local-chemical-consistency-001.json; /records/6 | supports | The saved local computation reproduces the declared full Standard InChIKey CUXAULQHGRSWLF-IKVCUCANSA-N from both owner encodings and reports formula C37H56ClN9O8. Both representations have 2 unspecified tetrahedral centers. This is retained-encoding consistency, not proof of the natural absolute configuration. |
| SCI637-INTERPRETATION | /private/tmp/npm-review-work/shared-next-batch064-tentative/source-science-preparation/tentative64-local-chemical-interpretation-addendum-001.json; /records/6; original_computation_clock and separate_neighbor_inspection_clock | context_only | Unspecified tetrahedral centers occur in both owner representations, consistent with the retained stereo_complete=false scope. This is representational incompleteness, not evidence identifying the missing natural configurations. Two unspecified adjacent carbon centers are SMILES atoms38/39 (InChI28/29); one has a nitrogen neighbor and the other an OH neighbor. They lie in the explicit C(C(O)C(N)=O) peptide segment; no published atom numbering or natural configuration is assigned. Parsed-InChI C=N flags are interpreted only through the saved neighbor addendum; this interpretation reuses the saved two-encoding result. The exact retained ChEBI alternative failed its original parse and its comparison remains null; no retry, repaired SMILES or replacement structure is asserted. |
| SCI637-ABSTRACT | DOI:10.1002/ajoc.201700433; /message/abstract; own article title/identifiers and complete abstract only in /private/tmp/npm-review-work/shared-next-batch064-tentative/literature-preparation/public-metadata-001/curacomycin-crossref.json | partial | The own Crossref abstract names curacomycin1 as a six-residue chlorinated cyclic peptide isolated from S. curacoi NBRC12761T, separately from dechlorocuracomycin2 from S. noursei NBRC15452T. This supports bounded curacomycin material and S. curacoi origin context. Repeated MIBiG, LOTUS and ChEBI citations here all refer to the same paper and are not independent publications. The transport is public metadata; no full primary body or SI was read. |
| SCI637-MAINTENANCE | /private/tmp/npm-review-work/shared-next-batch064-tentative/source-science-preparation/bgc-tentative64-curacomycin-occurrence-maintenance-route-proposal-001.json; /source_chain; /maintained_route/searches; /maintained_route/why_existing_routes_do_not_apply | context_only | The exact raw ChEBI row projects into occurrences[0]. Ignored-inclusive searches covered active scripts, src/naturalproductmech, curation, tests, docs and conf (Python bytecode excluded) and found no implemented ChEBI-origin correction interface there. ROOT also inspected the extractor, ChEBI seeder loop and LOTUS-only consumer. Any correction needs an implemented maintained-input route; the search makes no global historical-artifact absence claim. |
| SCI637-SIBLING-JOIN | data/raw/antibioticmech_inchikeys.tsv; standard_inchi_key=CUXAULQHGRSWLF-IKVCUCANSA-N; identifier=CHEBI:156426 | supports | One retained AntibioticMech export row matches the full key, CHEBI identifier and recorded source revision 74f6cc836249. This verifies the pinned local SAME_STRUCTURE join, not current sibling content or antimicrobial mechanism. |

## Limits And Additional Notes

- This is a full abstract delivered through Crossref metadata, not a read of full primary narrative, tables, spectra or supplementary files.
- The article's reported respective isolation pair does not prove that S. noursei can never produce chlorinated curacomycin; it questions whether this cited observation supports the current exact-congener occurrence.
- The two retained MIBiG entries both name S. curacoi and curacomycin; the abstract does not identify their accession-to-cluster mapping and cannot independently resolve the pre-existing shared-structure discussion.
- The saved raw ChEBI SMILES parsing failure and null comparison are a separate local-input diagnostic; no corrected structure or current ChEBI validation is asserted.
- Current authority checks and full primary/SI remain held. An own PMID/DOI match establishes publication identity, not exact natural structure, strain-role identity or locus-grade completeness.
- The earlier two-encoding computation, later intake SMILES computation, original owner reading and HTTP retrieval retain separate clocks. Full primary and current authority checks remain unavailable.
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
- The entire local owner and retained source rows were read. Full-owner scientific verification remains false; scientific_review denotes only the bounded scientific interpretation in evidence and assessments.
- Original owner reading, HTTP retrieval, two-encoding computation and later official-intake SMILES computation have separate preserved clocks. The review start/finish bound official intake and final adjudication; earlier evidence is reused.
- No scientific record, maintained source or native curation status was changed. Findings and actions describe proposed work; unavailable checks prevent completed status.

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
review_id: 20261027T125535Z-curacomycin
title: Scientific review of curacomycin
started_at: '2026-10-27T12:41:49.812704Z'
finished_at: '2026-10-27T12:55:35.024431Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Local encodings agree with the retained chlorinated curacomycin structure.
  A provisional major finding identifies a likely cross-congener citation assignment
  in the ChEBI-derived S. noursei NBRC 15452 occurrence: the cited abstract assigns
  that strain to dechlorocuracomycin. Full primary reconciliation and a maintained-source
  correction are proposed; other identity, strain and locus questions remain unresolved.'
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
  - path: data/natural_products/amino_acids_and_peptides/curacomycin.yaml
    sha256: c897a25656268d69ab62f6783e93272e24f125931bc097443d8c32359cbfd14e
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: CHEBI:156426
  path: data/natural_products/amino_acids_and_peptides/curacomycin.yaml
  label: curacomycin
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
    path: data/natural_products/amino_acids_and_peptides/curacomycin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: ChEBI cited compound-origin source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_chebi.py
    role: ChEBI origin extraction into maintained inventory
scope:
  description: Whole retained owner and source rows, local chemical consistency, inspected
    own publication metadata and supplied abstracts; exact primary and current-authority
    verification is partial.
  selection: One resolved record in canonical path order from the unreviewed corpus;
    current official intake reconciled to the earlier evidence snapshots.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156426
  exclusions:
  - target: Full primary material and current external authorities
    reason: No full article/SI or current authority refresh was inspected; unresolved
      exact claims are explicit below.
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
    Reused for batch064 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch064. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:156426
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
    Reused for batch064 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch064. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:156426
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
    Reused for batch064 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch064. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:156426
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
    Reused for batch064 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch064. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:156426
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
    Reused for batch064 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,233 tracked byte streams and modes (210,076,479 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch064. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - CHEBI:156426
- check_id: C-STRICT
  name: Native strict target validation
  status: passed
  required: true
  summary: The exact selected owner passed the documented strict validator; this is
    a configured consistency result.
  command: just validate-strict data/natural_products/amino_acids_and_peptides/curacomycin.yaml
    --out /private/tmp/npm-review-work/637/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Actual target intake execution finished 2026-10-27T12:41:51.144891Z.
    Original receipt: /private/tmp/npm-review-work/637/strict-receipt.json.'
  target_ids:
  - CHEBI:156426
- check_id: SCI637-LOCAL-ENCODING
  name: Saved local owner-encoding consistency
  status: passed
  required: true
  summary: The saved local computation reproduces the declared full Standard InChIKey
    CUXAULQHGRSWLF-IKVCUCANSA-N from both owner encodings and reports formula C37H56ClN9O8.
    Both representations have 2 unspecified tetrahedral centers. This is retained-encoding
    consistency, not proof of the natural absolute configuration.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-LOCAL
  - SCI637-CHEM
  - SCI637-INTERPRETATION
  scope_note: This check reuses the original two-encoding RDKit result; the official
    intake has a separate SMILES computation. No current authority lookup is claimed.
- check_id: SCI637-OWN-METADATA
  name: Own article identifier and abstract applicability
  status: passed
  required: true
  summary: The stored response own identifiers match this exact cited publication;
    the complete own abstract and title were read. Publication identity does not establish
    all retained compound/strain/locus assertions.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-ABSTRACT
- check_id: SCI637-EXACT-SOURCE
  name: Full exact-material and current authority verification
  status: unavailable
  required: true
  summary: Full primary/SI, natural stereochemistry, exact MIBiG accession-to-product
    mapping and current authorities remain unverified. The separate provisional occurrence-citation
    finding is based on the inspected abstract and exact retained ChEBI row.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-LOCAL
  - SCI637-ABSTRACT
evidence:
- evidence_id: SCI637-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch064-tentative/tentative-owner-source-inventory-001.json
  locator: /entries/6/owner_document; /entries/6/rows
  accessed_at: '2026-10-27T11:58:53.871064Z'
  snapshot_sha256: d326d9f06af4c4b90d76f1f911f6a473b4a68eb2c8d676cb09eaefcc78cdae83
  support: context_only
  summary: Exact retained curacomycin owner and all seven source arrays (7 rows),
    including original imported producer/occurrence/locus grades and history. The
    current official intake matches these retained local claims.
- evidence_id: SCI637-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch064-tentative/source-science-preparation/root-tentative64-local-chemical-consistency-001.json
  locator: /records/6
  accessed_at: '2026-10-27T12:03:57.718530Z'
  snapshot_sha256: 7948e99a7bf0c290c8791273d511956f3e48376b6cefcdee2324460dc486a413
  support: supports
  summary: The saved local computation reproduces the declared full Standard InChIKey
    CUXAULQHGRSWLF-IKVCUCANSA-N from both owner encodings and reports formula C37H56ClN9O8.
    Both representations have 2 unspecified tetrahedral centers. This is retained-encoding
    consistency, not proof of the natural absolute configuration.
- evidence_id: SCI637-INTERPRETATION
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch064-tentative/source-science-preparation/tentative64-local-chemical-interpretation-addendum-001.json
  locator: /records/6; original_computation_clock and separate_neighbor_inspection_clock
  accessed_at: '2026-10-27T12:10:51.366371Z'
  snapshot_sha256: d08b26c86cb477241550ca94f0f155a2d2c836125a57919f845ce5e9efd291fa
  support: context_only
  summary: Unspecified tetrahedral centers occur in both owner representations, consistent
    with the retained stereo_complete=false scope. This is representational incompleteness,
    not evidence identifying the missing natural configurations. Two unspecified adjacent
    carbon centers are SMILES atoms38/39 (InChI28/29); one has a nitrogen neighbor
    and the other an OH neighbor. They lie in the explicit C(C(O)C(N)=O) peptide segment;
    no published atom numbering or natural configuration is assigned. Parsed-InChI
    C=N flags are interpreted only through the saved neighbor addendum; this interpretation
    reuses the saved two-encoding result. The exact retained ChEBI alternative failed
    its original parse and its comparison remains null; no retry, repaired SMILES
    or replacement structure is asserted.
- evidence_id: SCI637-ABSTRACT
  kind: primary_source
  reference: DOI:10.1002/ajoc.201700433
  locator: /message/abstract; own article title/identifiers and complete abstract
    only in /private/tmp/npm-review-work/shared-next-batch064-tentative/literature-preparation/public-metadata-001/curacomycin-crossref.json
  accessed_at: '2026-10-27T12:22:45.619808Z'
  snapshot_sha256: 5e39bcad8fc39974d63f0163190dd224c658762d8311daa4bb715dbca4a90e28
  support: partial
  summary: The own Crossref abstract names curacomycin1 as a six-residue chlorinated
    cyclic peptide isolated from S. curacoi NBRC12761T, separately from dechlorocuracomycin2
    from S. noursei NBRC15452T. This supports bounded curacomycin material and S.
    curacoi origin context. Repeated MIBiG, LOTUS and ChEBI citations here all refer
    to the same paper and are not independent publications. The transport is public
    metadata; no full primary body or SI was read.
- evidence_id: SCI637-MAINTENANCE
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch064-tentative/source-science-preparation/bgc-tentative64-curacomycin-occurrence-maintenance-route-proposal-001.json
  locator: /source_chain; /maintained_route/searches; /maintained_route/why_existing_routes_do_not_apply
  accessed_at: '2026-10-27T12:50:40.661344Z'
  snapshot_sha256: 22db199adea60fa3cb0414118f91a8df0a682dea98a4c17438292ef019e99cca
  support: context_only
  summary: The exact raw ChEBI row projects into occurrences[0]. Ignored-inclusive
    searches covered active scripts, src/naturalproductmech, curation, tests, docs
    and conf (Python bytecode excluded) and found no implemented ChEBI-origin correction
    interface there. ROOT also inspected the extractor, ChEBI seeder loop and LOTUS-only
    consumer. Any correction needs an implemented maintained-input route; the search
    makes no global historical-artifact absence claim.
  search_scope: Repository /private/tmp/npm-record-reviews-20261021. Retained rg --no-ignore
    --hidden -n -i searches include ignored and hidden files, excluding **/__pycache__/**.
    Query chebi[_ -]?(origin|occurrence)[_ -]?(exclusion|correction|override)|load_chebi.*exclu|source-chebi-.*exclu
    covered scripts, src/naturalproductmech, curation, tests, docs and conf. Query
    curacomycin|CHEBI:156426|CUXAULQHGRSWLF|201700433 covered curation. Both returned
    exit1 with no matches. Exact argv, roots, and output are retained at /maintained_route/searches
    in the referenced snapshot; this is a bounded active-source search, not a historical/global
    or external-authority absence claim.
- evidence_id: SCI637-SIBLING-JOIN
  kind: database
  reference: data/raw/antibioticmech_inchikeys.tsv
  locator: standard_inchi_key=CUXAULQHGRSWLF-IKVCUCANSA-N; identifier=CHEBI:156426
  accessed_at: '2026-10-27T12:50:40.661344Z'
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
  support: supports
  summary: One retained AntibioticMech export row matches the full key, CHEBI identifier
    and recorded source revision 74f6cc836249. This verifies the pinned local SAME_STRUCTURE
    join, not current sibling content or antimicrobial mechanism.
assessments:
- assessment_id: SCI637-BOUNDED-SUPPORT
  area: evidence
  topic: Named material and source-specific biological-origin support
  outcome: supported
  summary: The own Crossref abstract names curacomycin1 as a six-residue chlorinated
    cyclic peptide isolated from S. curacoi NBRC12761T, separately from dechlorocuracomycin2
    from S. noursei NBRC15452T. This supports bounded curacomycin material and S.
    curacoi origin context. Repeated MIBiG, LOTUS and ChEBI citations here all refer
    to the same paper and are not independent publications.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-LOCAL
  - SCI637-ABSTRACT
- assessment_id: SCI637-REPRESENTATION
  area: representation
  topic: Retained encodings and limited local stereochemistry
  outcome: supported
  summary: The saved local computation reproduces the declared full Standard InChIKey
    CUXAULQHGRSWLF-IKVCUCANSA-N from both owner encodings and reports formula C37H56ClN9O8.
    Both representations have 2 unspecified tetrahedral centers. This is retained-encoding
    consistency, not proof of the natural absolute configuration. Unspecified tetrahedral
    centers occur in both owner representations, consistent with the retained stereo_complete=false
    scope. This is representational incompleteness, not evidence identifying the missing
    natural configurations. Two unspecified adjacent carbon centers are SMILES atoms38/39
    (InChI28/29); one has a nitrogen neighbor and the other an OH neighbor. They lie
    in the explicit C(C(O)C(N)=O) peptide segment; no published atom numbering or
    natural configuration is assigned. Parsed-InChI C=N flags are interpreted only
    through the saved neighbor addendum; this interpretation reuses the saved two-encoding
    result. The exact retained ChEBI alternative failed its original parse and its
    comparison remains null; no retry, repaired SMILES or replacement structure is
    asserted.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-CHEM
  - SCI637-INTERPRETATION
- assessment_id: SCI637-SCOPE-LIMIT
  area: provenance
  topic: Exact congener/strain/locus and natural-identity scope
  outcome: concern
  summary: The retained S. noursei NBRC 15452 occurrence cites an abstract assigning
    that strain to dechlorocuracomycin. This is a provisional major citation-applicability
    finding on the chlorinated curacomycin owner; natural production capability and
    full-paper observations remain unresolved.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-LOCAL
  - SCI637-ABSTRACT
- assessment_id: SCI637-SIBLING-JOIN
  area: consistency
  topic: Pinned cross-corpus structure link
  outcome: supported
  summary: The related-record link reproduces the exact full-key row in the pinned
    sibling export; no mechanism or current external equivalence is inferred.
  target_ids:
  - CHEBI:156426
  evidence_ids:
  - SCI637-SIBLING-JOIN
findings:
- finding_id: SCI637-OCCURRENCE-CITATION
  issue_key: npm-chebi156426-noursei15452-curacomycin-citation
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Cited S. noursei observation appears to belong to dechlorocuracomycin
  description: The CHEBI:156426 occurrence for Streptomyces noursei NBRC 15452 cites
    DOI:10.1002/ajoc.201700433. Its inspected abstract assigns curacomycin (compound
    1) to S. curacoi NBRC 12761 and dechlorocuracomycin (compound 2) to S. noursei
    NBRC 15452, respectively. The cited isolation does not support the chlorinated-congener
    occurrence as currently placed. The finding is provisional because full text and
    supplementary material could contain additional observations; it does not assert
    that this species cannot produce curacomycin.
  target_ids:
  - CHEBI:156426
  field_paths:
  - occurrences[0]
  - occurrences[0].evidence[0]
  evidence_ids:
  - SCI637-LOCAL
  - SCI637-ABSTRACT
  - SCI637-MAINTENANCE
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Retained cited ChEBI origin; preserve raw provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: ChEBI occurrence projection and future guarded curation consumer
  normalization_reason: A probable cross-congener citation assignment materially affects
    biological-occurrence evidence. Severity is major; certainty remains provisional
    at the inspected abstract tier.
  rule_id: 'CLAUDE.md: occurrence claims require evidence; review-yaml-record: preserve
    exact compound and strain scope'
  native_severity: major
actions:
- action_id: SCI637-RECONCILE-OCCURRENCE
  finding_ids:
  - SCI637-OCCURRENCE-CITATION
  target_ids:
  - CHEBI:156426
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Retained cited ChEBI origin; preserve raw provenance
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: ChEBI occurrence projection and future guarded curation consumer
  description: Inspect the full cited article and supplementary material for the exact
    chlorinated curacomycin/strain pairing. If the source contains additional supporting
    material, qualify the occurrence with that exact evidence. Otherwise implement
    and document a strictly row-pinned ChEBI-origin exclusion or qualification consumer
    before adopting a curation decision. The existing LOTUS exclusion table does not
    affect ChEBI origins, and curation/decisions.tsv is not consumed. Preserve the
    raw seven-field row and its explanation; keep other occurrences, structures, producers
    and loci outside this bounded correction.
  acceptance_checks:
  - Reconcile compound numbers 1 and 2 with both exact strains in full primary material;
    record the evidence and whether it supports retention, qualification or withdrawal
    of this occurrence.
  - Exact row removal only; preserve a different strain, DOI, ChEBI ID and full-key
    owner.
  - Reject any drift in all seven source fields including blanks, missing/duplicate
    source matches, duplicate/unused decisions and incorrect owner join.
  - Raw inventories and unaffected records remain byte-identical; recompute occurrence
    facets and protect table-owned adjudication from stale carried YAML.
  - Record retains its two S.curacoi occurrences, structure, producers and clusters.
  - Require exact current CHEBI:156426/full-key/NCBITaxon:1971/NBRC15452/DOI match
    and whole raw-row digest bce1a9c0367d52bc595f837caffa035c9db7f981656b2248a68988d9ac9b3eb7
    before any future decision.
  - After separately authorized implementation and canary inspection, demonstrate
    strict validation, byte reproduction, provenance and corpus checks; no such commands
    ran in this task.
  - After an implemented correction, run just seed, inspect just seed-canary CHEBI:156426,
    then run just validate-strict data/natural_products/amino_acids_and_peptides/curacomycin.yaml,
    just verify-reproduction, just provenance-check, just verify-corpus --summary
    and just qc. These are proposed future checks, not results of this review.
  generator: scripts/seed_from_sources.py, only after separately authorized guarded
    maintenance-route implementation
limitations:
- This is a full abstract delivered through Crossref metadata, not a read of full
  primary narrative, tables, spectra or supplementary files.
- The article's reported respective isolation pair does not prove that S. noursei
  can never produce chlorinated curacomycin; it questions whether this cited observation
  supports the current exact-congener occurrence.
- The two retained MIBiG entries both name S. curacoi and curacomycin; the abstract
  does not identify their accession-to-cluster mapping and cannot independently resolve
  the pre-existing shared-structure discussion.
- The saved raw ChEBI SMILES parsing failure and null comparison are a separate local-input
  diagnostic; no corrected structure or current ChEBI validation is asserted.
- Current authority checks and full primary/SI remain held. An own PMID/DOI match
  establishes publication identity, not exact natural structure, strain-role identity
  or locus-grade completeness.
- The earlier two-encoding computation, later intake SMILES computation, original
  owner reading and HTTP retrieval retain separate clocks. Full primary and current
  authority checks remain unavailable.
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
  verification remains false; scientific_review denotes only the bounded scientific
  interpretation in evidence and assessments.
- Original owner reading, HTTP retrieval, two-encoding computation and later official-intake
  SMILES computation have separate preserved clocks. The review start/finish bound
  official intake and final adjudication; earlier evidence is reused.
- No scientific record, maintained source or native curation status was changed. Findings
  and actions describe proposed work; unavailable checks prevent completed status.
```
