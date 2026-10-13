# bryostatin: scoped isolate and congener disposition

- Review: 20261013T232106Z-bryostatin-scoped-disposition
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-13T23:20:17.641800Z
- Finished UTC: 2026-10-13T23:21:06.261737Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed isolate provenance omission resolved; provisional exact-congener/locus assignment remains open.

## Scope And Provenance

One exact owner; scoped reassessment of predecessor findings after authorized remediation.

Selection: Exact predecessor target, not a new sample or coverage increment.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 90ff2460ce59e7373499e77e539ad5a3d85fe1f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-45bd834dfa | data/natural_products/polyketides/bryostatin.yaml | generated | bryostatin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| prepare | passed | True | naturalproductmech:mibig-45bd834dfa | Canonical inspection and complete native resolved read succeeded. |
| scope | passed | True | naturalproductmech:mibig-45bd834dfa | Full owner/component/input and immutable predecessor scope audit passed. |
| focused-complete | passed | True | naturalproductmech:mibig-45bd834dfa | 260 tests passed, including source drift, missing/duplicate/unknown fields, withheld producers, structure-correction conflicts, sibling isolation, legacy strains and current owners. |
| strict-complete | passed | True | naturalproductmech:mibig-45bd834dfa | Both complete owners passed closed-schema validation with zero errors. |
| Primary exact-congener adjudication | unavailable | True | naturalproductmech:mibig-45bd834dfa | No new primary retrieval or bypass. Required compound-specific full-text structures, figures and supplements remain unadjudicated as documented in the predecessor. |

## Scientific And Domain Assessments

### Literal deposited isolate scope

provenance: supported. Targets: naturalproductmech:mibig-45bd834dfa.

Inspected deposits and tested maintained decisions preserve DEEP as an isolate qualifier only. Existing producer assertions, evidence grades and species identity remain unchanged.

### Exact-congener assignment remains unresolved

identity: concern. Targets: naturalproductmech:mibig-45bd834dfa.

Exact registry equivalence is retained, but final-congener and locus-sufficiency questions require primary evidence. OPEN discussion is qualification, not adjudication or native status promotion.

## Findings

### F1: Generic bryostatin label leaves the exact congener-to-locus assignment unresolved

major / open / provisional; issue key: bryostatin-exact-congener-locus-scope.

The database attaches this exact graph to a generic family label and a deposited gene region. The same label also names a chemically distinct owner; exact PubChem agreement establishes registry equivalence, not which final congener this region yields. Connectivity matches a bryostatin1 registry candidate, but stereo differs and the cited primary paper has not been adjudicated for this exact graph. Missing primary access is a limitation, not proof that the biological assertion is false. Preserve the source assertion while obtaining exact-congener evidence/qualification.

Disposition: A cited OPEN discussion makes the unresolved scope explicit. Exact congener assignment and each region's contribution remain open under #950. No label/structure migration, merge, stereo completion, xref exclusion or REVIEWED promotion is justified.

### F2: Producer omits the deposited DEEP isolate context

minor / resolved / confirmed; issue key: bryostatin-deposited-isolate-context.

DQ889941.1 explicitly records source qualifier isolate=DEEP, while the native producer names only species62101 and has no such qualifier in notes. Both deposits use DEEP; this is provenance loss, not evidence of different producers. Do not silently relabel an isolate as a characterized culture strain.

Disposition: Both exact deposits retain literal DEEP isolate context in generated producer notes and separate claim-level evidence. The complete raw row is pinned, drift fails closed, and no strain field or grade is inferred. Scoped resolution of issue #949 only.

## Recommended Actions And Acceptance Checks

### A1

Obtain primary product/structure evidence and adjudicate the exact congener and contribution of each gene region. Preserve original generic labels as provenance; add a cited unresolved discussion through the guarded curator path if appropriate. Any generated label/structure change needs maintained inputs and tests. Do not merge owners, infer missing stereo, add connectivity-only xrefs, or upgrade evidence/status.

- Primary compound and stereochemical evidence identifies the supported exact form or explicitly qualifies unresolved scope.
- Each producer and locus claim is re-audited for that form; ABCDX/PQRS regions are not treated as independently sufficient without experiments.
- Exact-key PubChem matches remain unless separately disproved; no same-name claim transfer; native strict/reproduction/QC gates pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current | data/natural_products/polyketides/bryostatin.yaml | supports | Complete current owner and resolved mechanism read. Literal DEEP isolate context and cited OPEN congener qualification added; chemistry, xrefs, taxon IDs, tiers and SEEDED status retained. |
| prior | reviews/structured/20261013T230511Z-bryostatin/review.yaml | supports | Immutable predecessor full-owner partial assessment. Its primary-source limitations remain; this scoped successor does not complete scientific review. |
| isolates | curation/mibig_producer_isolates.tsv | supports | Two exact full-row-pinned DEEP isolate decisions with separate versioned GenBank citations. Shared validation and guarded seeding preserve isolate semantics, not strain assertions. |
| scope | /private/tmp/npmech-bryostatin-publish-xDdyDA/scope-audit.json | supports | All 3115 owners, 243 components, 54 prior review pairs and tracked raw inputs checked. Only two owners changed, within the asserted notes/evidence/discussion/history boundary. |
| sequences | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=DQ889941.1,DQ889942.1&amp;rettype=gbwithparts&amp;retmode=xml; Source qualifiers, feature products/protein accessions and references; nucleotide sequence was captured but not experimentally revalidated; payload /private/tmp/npmech-gentamicin-review-c2YN3q/bry-sequences.xml; original retrieval 2026-10-13T22:08:59.009446Z..2026-10-13T22:08:59.508988Z; accessed_at is local reinspection | supports | Both exact deposits identify isolate DEEP and taxon62101. DQ889941.1 contains bryABCDX PKS annotations; DQ889942.1 contains bryPQRS with flanking transposase-like/oxidoreductase genes. These are two deposited regions of the same named isolate, not evidence of two different producers or independent complete pathways. Their references identify PMID15556005 and/or PMID17253852. |
| pubchem | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/25235992,6438934/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Official property objects; payload /private/tmp/npmech-gentamicin-review-c2YN3q/bry-pubchem.json; original retrieval 2026-10-13T22:08:58.269867Z..2026-10-13T22:08:58.822778Z; accessed_at is local reinspection | supports | CID25235992 exactly matches MJQUEDHRCUIRLF-YFQOKXJGSA-N; CID6438934 exactly matches NJMZVUZEDLKEGZ-XMADZBCLSA-N. Full InChI, not just first key block, agrees in each case. Preserve these xrefs. |
| prepare | /private/tmp/npmech-bryostatin-publish-xDdyDA/prepare.log | supports | Canonical inspection and complete native resolved read succeeded. |
| scope-check | /private/tmp/npmech-bryostatin-publish-xDdyDA/scope.log | supports | Full owner/component/input and immutable predecessor scope audit passed. |
| focused-complete | /private/tmp/npmech-bryostatin-publish-xDdyDA/focused-complete.log | supports | 260 tests passed, including source drift, missing/duplicate/unknown fields, withheld producers, structure-correction conflicts, sibling isolation, legacy strains and current owners. |
| strict-complete | /private/tmp/npmech-bryostatin-publish-xDdyDA/strict-complete.log | supports | Both complete owners passed closed-schema validation with zero errors. |

## Limits And Additional Notes

- Scoped disposition only; no additional full-owner coverage or completed scientific review.
- No new primary retrieval. All predecessor access stops and scientific evidence limitations remain.
- Current working-tree hashes attest to inspected bytes; they do not claim those bytes existed at the base commit. The base is retained by review-base/bryostatin-20261013.
- Only focused, strict and scope gates are asserted here. Final full QC, review-contract checks and CI follow before merge.
- Initial test expected a narrower drift error than the loader provides; corrected. An initial discussion draft was rejected before writing by the shared evidence schema, and current-owner tests failed until the corrected guarded write. Subsequent focused and strict checks passed; failed receipts retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T232106Z-bryostatin-scoped-disposition
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'bryostatin: scoped isolate and congener disposition'
started_at: '2026-10-13T23:20:17.641800Z'
finished_at: '2026-10-13T23:21:06.261737Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Implementing assistant carrying out a separate adversarial pass;
    not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Confirmed isolate provenance omission resolved; provisional exact-congener/locus
  assignment remains open.
source:
  git_revision: 90ff2460ce59e7373499e77e539ad5a3d85fe1f5
  state: working_tree
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
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 6f879bb9f2c9be6b6e8de8c013dbaebe09075b7e106790ea303a17006761ea11
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: 5b1edc057cdcc732f61de2964cd175fa3bc2dca929c5d2823142f61313545a7e
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: f61d7ba85ffd21837cd2b625f83c4681c4663e72503466b40eba3f4ab0204bc1
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 18b61c1e5a69112c99cea1373791cd1ec571b7084bfd9198ab68fa551f5d531a
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: bf38e4f0c7e4bcbdf184a4e7b8b024752251e8f34c015c0b82cedca98a8a5729
    role: context
  - path: data/natural_products/polyketides/bryostatin-2.yaml
    sha256: 4203620fc9cb2cfcc2f50b7499595d1af3e79a7bd173c40a313ec09d2d7a46eb
    role: context
  - path: data/natural_products/polyketides/bryostatin.yaml
    sha256: 58f1f3950bd2eb911184aa9fb719cc994a82a113a9e0d6097a39c4f8503d2250
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
    sha256: 3ab166b341e5f3f1eaaee1b2af2485ac575c1a1eab1570bbf1d8d2d3ba76e53e
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
  - path: reviews/structured/20261013T230511Z-bryostatin/review.yaml
    sha256: 7927b09656b2bad4002f797f682cf52b35e2d0469e082308a78dfccb6c018e3d
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
  - path: scripts/extract_pubchem_bioassay.py
    sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/run_qc.py
    sha256: ff44ed3e40a9b3582eb84e38a81301745ae80d16445756d09a7efb2a480b1abb
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 09a5881dfc8eda563a6c688741e667b53298e5f23a8f482e7adb440a2fa68c1c
    role: context
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
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
  - path: tests/test_bryostatin_curation.py
    sha256: b94f12fc7fcf1b2977d5bab51c0c9091a2a7405e213943f4f2e7210f6c3b6d06
    role: context
  - path: tests/test_producer_isolates.py
    sha256: 8f96b00fbb66564f2d5e5c2108c991135eec8731b10d9f2d9f2f73830080ccd9
    role: context
  - path: uv.lock
    sha256: c62a5739e3ffeb12cc57b3bf12a31dcf9cdfbf00b417f4ba3a801d51ef9efbe3
    role: context
targets:
- target_id: naturalproductmech:mibig-45bd834dfa
  path: data/natural_products/polyketides/bryostatin.yaml
  label: bryostatin
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
    path: data/raw/pubchem_bioassay.tsv
    role: Imported compound-specific assay observations
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: BioAssay extraction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_isolates.tsv
    role: Full-row-pinned literal isolate qualifications
scope:
  description: One exact owner; scoped reassessment of predecessor findings after
    authorized remediation.
  selection: Exact predecessor target, not a new sample or coverage increment.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-45bd834dfa
checks:
- check_id: prepare
  name: prepare
  status: passed
  required: true
  command: uv run python /private/tmp/npmech-bryostatin-publish-xDdyDA/prepare_disposition.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  summary: Canonical inspection and complete native resolved read succeeded.
  scope_note: Actual execution 2026-10-13T23:20:16.450680Z..2026-10-13T23:20:21.583013Z;
    log /private/tmp/npmech-bryostatin-publish-xDdyDA/prepare.log; SHA256 8e60132e0ef2853c96b32d17b6f5afb869706d10e9993af96e1204f3af85de6e
- check_id: scope
  name: scope
  status: passed
  required: true
  command: uv run python /private/tmp/npmech-bryostatin-publish-xDdyDA/audit.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  summary: Full owner/component/input and immutable predecessor scope audit passed.
  scope_note: Actual execution 2026-10-13T23:20:17.610249Z..2026-10-13T23:20:18.411321Z;
    log /private/tmp/npmech-bryostatin-publish-xDdyDA/scope.log; SHA256 c1eadb07773afc40876bea9c12adf3215cd0faf58ea57e83e5d0b8241240955c
- check_id: focused-complete
  name: focused-complete
  status: passed
  required: true
  command: uv run pytest -q tests/test_producer_isolates.py tests/test_producer_strains.py
    tests/test_bryostatin_curation.py tests/test_seed_skeleton.py tests/test_structure_corrections.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  summary: 260 tests passed, including source drift, missing/duplicate/unknown fields,
    withheld producers, structure-correction conflicts, sibling isolation, legacy
    strains and current owners.
  scope_note: Actual execution 2026-10-13T23:19:50.064765Z..2026-10-13T23:20:10.483891Z;
    log /private/tmp/npmech-bryostatin-publish-xDdyDA/focused-complete.log; SHA256
    572960758a62c0f994e6edbc1b76368289f51a4f9c387fc5c1f4c6d07a690fcb
- check_id: strict-complete
  name: strict-complete
  status: passed
  required: true
  command: uv run python scripts/validate_strict.py data/natural_products/polyketides/bryostatin.yaml
    data/natural_products/polyketides/bryostatin-2.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  summary: Both complete owners passed closed-schema validation with zero errors.
  scope_note: Actual execution 2026-10-13T23:19:51.225932Z..2026-10-13T23:19:54.505925Z;
    log /private/tmp/npmech-bryostatin-publish-xDdyDA/strict-complete.log; SHA256
    28fd810d7be4b1afb0685b623e7126b77927eb549d8f7f8b0e5504feb68d59af
- check_id: primary-congener
  name: Primary exact-congener adjudication
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  summary: No new primary retrieval or bypass. Required compound-specific full-text
    structures, figures and supplements remain unadjudicated as documented in the
    predecessor.
evidence:
- evidence_id: current
  kind: record_content
  reference: data/natural_products/polyketides/bryostatin.yaml
  accessed_at: '2026-10-13T23:21:06.259512Z'
  support: supports
  summary: Complete current owner and resolved mechanism read. Literal DEEP isolate
    context and cited OPEN congener qualification added; chemistry, xrefs, taxon IDs,
    tiers and SEEDED status retained.
  snapshot_sha256: 58f1f3950bd2eb911184aa9fb719cc994a82a113a9e0d6097a39c4f8503d2250
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261013T230511Z-bryostatin/review.yaml
  accessed_at: '2026-10-13T23:21:06.259948Z'
  support: supports
  summary: Immutable predecessor full-owner partial assessment. Its primary-source
    limitations remain; this scoped successor does not complete scientific review.
  snapshot_sha256: 7927b09656b2bad4002f797f682cf52b35e2d0469e082308a78dfccb6c018e3d
- evidence_id: isolates
  kind: record_content
  reference: curation/mibig_producer_isolates.tsv
  accessed_at: '2026-10-13T23:21:06.260186Z'
  support: supports
  summary: Two exact full-row-pinned DEEP isolate decisions with separate versioned
    GenBank citations. Shared validation and guarded seeding preserve isolate semantics,
    not strain assertions.
  snapshot_sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
- evidence_id: scope
  kind: validation
  reference: /private/tmp/npmech-bryostatin-publish-xDdyDA/scope-audit.json
  accessed_at: '2026-10-13T23:21:06.260307Z'
  support: supports
  summary: All 3115 owners, 243 components, 54 prior review pairs and tracked raw
    inputs checked. Only two owners changed, within the asserted notes/evidence/discussion/history
    boundary.
  snapshot_sha256: 73663b5b3cd0c09d73557aa75c85068979bcdfc110c5fc3ab1675a3adb42034d
- evidence_id: sequences
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=DQ889941.1,DQ889942.1&rettype=gbwithparts&retmode=xml
  summary: Both exact deposits identify isolate DEEP and taxon62101. DQ889941.1 contains
    bryABCDX PKS annotations; DQ889942.1 contains bryPQRS with flanking transposase-like/oxidoreductase
    genes. These are two deposited regions of the same named isolate, not evidence
    of two different producers or independent complete pathways. Their references
    identify PMID15556005 and/or PMID17253852.
  locator: Source qualifiers, feature products/protein accessions and references;
    nucleotide sequence was captured but not experimentally revalidated; payload /private/tmp/npmech-gentamicin-review-c2YN3q/bry-sequences.xml;
    original retrieval 2026-10-13T22:08:59.009446Z..2026-10-13T22:08:59.508988Z; accessed_at
    is local reinspection
  accessed_at: '2026-10-13T23:05:09.560657Z'
  support: supports
  snapshot_sha256: faa76bee97d1e6573f3aebe1c30e45fe1cdd4488d9c7e79fc0265d5e2b23a37a
- evidence_id: pubchem
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/25235992,6438934/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  summary: CID25235992 exactly matches MJQUEDHRCUIRLF-YFQOKXJGSA-N; CID6438934 exactly
    matches NJMZVUZEDLKEGZ-XMADZBCLSA-N. Full InChI, not just first key block, agrees
    in each case. Preserve these xrefs.
  locator: Official property objects; payload /private/tmp/npmech-gentamicin-review-c2YN3q/bry-pubchem.json;
    original retrieval 2026-10-13T22:08:58.269867Z..2026-10-13T22:08:58.822778Z; accessed_at
    is local reinspection
  accessed_at: '2026-10-13T23:05:09.559155Z'
  support: supports
  snapshot_sha256: b0e4d6bcb73c485edc5bee1d4ce7cf08518452a9427f02a243d8311a2dc5a9b6
- evidence_id: prepare
  kind: validation
  reference: /private/tmp/npmech-bryostatin-publish-xDdyDA/prepare.log
  accessed_at: '2026-10-13T23:21:06.260686Z'
  support: supports
  summary: Canonical inspection and complete native resolved read succeeded.
  snapshot_sha256: 8e60132e0ef2853c96b32d17b6f5afb869706d10e9993af96e1204f3af85de6e
- evidence_id: scope-check
  kind: validation
  reference: /private/tmp/npmech-bryostatin-publish-xDdyDA/scope.log
  accessed_at: '2026-10-13T23:21:06.260991Z'
  support: supports
  summary: Full owner/component/input and immutable predecessor scope audit passed.
  snapshot_sha256: c1eadb07773afc40876bea9c12adf3215cd0faf58ea57e83e5d0b8241240955c
- evidence_id: focused-complete
  kind: validation
  reference: /private/tmp/npmech-bryostatin-publish-xDdyDA/focused-complete.log
  accessed_at: '2026-10-13T23:21:06.261296Z'
  support: supports
  summary: 260 tests passed, including source drift, missing/duplicate/unknown fields,
    withheld producers, structure-correction conflicts, sibling isolation, legacy
    strains and current owners.
  snapshot_sha256: 572960758a62c0f994e6edbc1b76368289f51a4f9c387fc5c1f4c6d07a690fcb
- evidence_id: strict-complete
  kind: validation
  reference: /private/tmp/npmech-bryostatin-publish-xDdyDA/strict-complete.log
  accessed_at: '2026-10-13T23:21:06.261592Z'
  support: supports
  summary: Both complete owners passed closed-schema validation with zero errors.
  snapshot_sha256: 28fd810d7be4b1afb0685b623e7126b77927eb549d8f7f8b0e5504feb68d59af
findings:
- finding_id: F1
  issue_key: bryostatin-exact-congener-locus-scope
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: Generic bryostatin label leaves the exact congener-to-locus assignment unresolved
  description: The database attaches this exact graph to a generic family label and
    a deposited gene region. The same label also names a chemically distinct owner;
    exact PubChem agreement establishes registry equivalence, not which final congener
    this region yields. Connectivity matches a bryostatin1 registry candidate, but
    stereo differs and the cited primary paper has not been adjudicated for this exact
    graph. Missing primary access is a limitation, not proof that the biological assertion
    is false. Preserve the source assertion while obtaining exact-congener evidence/qualification.
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  field_paths:
  - label
  - chemical_structure
  - producer_organisms
  - biosynthetic_gene_clusters
  evidence_ids:
  - current
  - prior
  - isolates
  - scope
  - sequences
  - pubchem
  - focused-complete
  rule_id: NaturalProductRecord identity and compound-specific BGC checklist
  native_severity: major
  normalization_reason: Material unresolved exact-product scope prevents scientific
    sign-off; not a confirmed wrong-structure blocker.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Compound label/structure and locus extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated exact-key harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source assertion, never silently rewritten
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T230511Z-bryostatin
    finding_id: F1
  disposition_reason: 'A cited OPEN discussion makes the unresolved scope explicit.
    Exact congener assignment and each region''s contribution remain open under #950.
    No label/structure migration, merge, stereo completion, xref exclusion or REVIEWED
    promotion is justified.'
- finding_id: F2
  issue_key: bryostatin-deposited-isolate-context
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Producer omits the deposited DEEP isolate context
  description: DQ889941.1 explicitly records source qualifier isolate=DEEP, while
    the native producer names only species62101 and has no such qualifier in notes.
    Both deposits use DEEP; this is provenance loss, not evidence of different producers.
    Do not silently relabel an isolate as a characterized culture strain.
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  field_paths:
  - producer_organisms[0].notes
  evidence_ids:
  - current
  - prior
  - isolates
  - scope
  - sequences
  - pubchem
  - focused-complete
  rule_id: Producer scope and deposited context checklist
  native_severity: minor
  normalization_reason: Bounded sample provenance omission; correcting it does not
    settle exact product identity.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_isolates.tsv
    role: Implemented full-row-pinned literal isolate qualifications
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Guarded generated producer notes and evidence
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261013T230511Z-bryostatin
    finding_id: F2
  disposition_reason: 'Both exact deposits retain literal DEEP isolate context in
    generated producer notes and separate claim-level evidence. The complete raw row
    is pinned, drift fails closed, and no strain field or grade is inferred. Scoped
    resolution of issue #949 only.'
assessments:
- assessment_id: isolate
  area: provenance
  topic: Literal deposited isolate scope
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  evidence_ids:
  - current
  - isolates
  - sequences
  - scope
  - focused-complete
  summary: Inspected deposits and tested maintained decisions preserve DEEP as an
    isolate qualifier only. Existing producer assertions, evidence grades and species
    identity remain unchanged.
- assessment_id: identity
  area: identity
  topic: Exact-congener assignment remains unresolved
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  evidence_ids:
  - current
  - prior
  - pubchem
  - sequences
  summary: Exact registry equivalence is retained, but final-congener and locus-sufficiency
    questions require primary evidence. OPEN discussion is qualification, not adjudication
    or native status promotion.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - naturalproductmech:mibig-45bd834dfa
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Compound label/structure and locus extraction
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated exact-key harmonization
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned source assertion, never silently rewritten
  description: Obtain primary product/structure evidence and adjudicate the exact
    congener and contribution of each gene region. Preserve original generic labels
    as provenance; add a cited unresolved discussion through the guarded curator path
    if appropriate. Any generated label/structure change needs maintained inputs and
    tests. Do not merge owners, infer missing stereo, add connectivity-only xrefs,
    or upgrade evidence/status.
  acceptance_checks:
  - Primary compound and stereochemical evidence identifies the supported exact form
    or explicitly qualifies unresolved scope.
  - Each producer and locus claim is re-audited for that form; ABCDX/PQRS regions
    are not treated as independently sufficient without experiments.
  - Exact-key PubChem matches remain unless separately disproved; no same-name claim
    transfer; native strict/reproduction/QC gates pass.
  generator: 'Future scientific curation only: reviewed maintained inputs, guarded
    writer/history, reproduction and full QC. The current OPEN qualification does
    not complete this action.'
limitations:
- Scoped disposition only; no additional full-owner coverage or completed scientific
  review.
- No new primary retrieval. All predecessor access stops and scientific evidence limitations
  remain.
- Current working-tree hashes attest to inspected bytes; they do not claim those bytes
  existed at the base commit. The base is retained by review-base/bryostatin-20261013.
- Only focused, strict and scope gates are asserted here. Final full QC, review-contract
  checks and CI follow before merge.
- Initial test expected a narrower drift error than the loader provides; corrected.
  An initial discussion draft was rejected before writing by the shared evidence schema,
  and current-owner tests failed until the corrected guarded write. Subsequent focused
  and strict checks passed; failed receipts retained.
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261013T230511Z-bryostatin
  relationship: Exact predecessor; scoped findings disposition.
```
