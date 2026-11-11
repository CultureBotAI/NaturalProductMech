# Local evidence review: pactamycin

- Review: 20261104T074022Z-pactamycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T07:03:23.606992Z
- Finished UTC: 2026-11-04T07:40:22.311873Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pactamycin retains exact local source-key grounding and a clearly limited urea/imidic representation difference. Its two canonical-SMILES equality flags are false and the saved atom map is empty despite equal standardized InChI, full key, formula and charge. The Terpenoids prediction versus PKS source class remains an applicability concern; the sibling ANTIBACTERIAL assertion supplies no fresh assay or mechanism. No source defect is proved; completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2369; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-608a44baf3 | data/natural_products/terpenoids/pactamycin.yaml | generated | pactamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-608a44baf3 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-608a44baf3 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-608a44baf3 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-608a44baf3 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-608a44baf3 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-608a44baf3 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-608a44baf3 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-608a44baf3 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained structure and identifier correspondence

identity: supported. Targets: naturalproductmech:mibig-608a44baf3.

The minted identifier naturalproductmech:mibig-608a44baf3 and full key WVIUOSJLUCTGFK-JUJPXXQGSA-N agree with MIBiG BGC0000118 version 5 and the exact-key AntibioticMech row. The retained PubChem link is 5289124, and no exact-key ChEBI structure is returned. Both stored forms reproduce the declared standardized key, but that does not resolve their fixed-bond representation difference or authenticate natural identity. SAME_INCHIKEY is the stated basis for the sibling SAME_STRUCTURE relation, not a new proof of every stereochemical and tautomeric detail.

### Stored representation and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-608a44baf3.

Both forms have neutral C28H38N4O8, 40 heavy atoms and 42 bonds, with six specified tetrahedral centers. The stored SMILES has urea N22(H)–C23(=O24)–N25(Me2); the InChI-derived form has N30=C24(–O36H)–N31(Me2), consistent with the retained mobile-H layer (H,31,37). Hydrogen moves from the urea nitrogen to oxygen and the C–N/C–O bond orders change. The reconstructed C=N adds one unspecified double-bond site. Both canonical-SMILES comparisons remain false and the chirality-aware atom map remains empty. This is a bounded normalization interpretation, not a claim of identical fixed graphs, a different natural compound or missing experimental stereochemistry.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-608a44baf3.

MIBiG BGC0000118 version 5 records Streptomyces pactum, taxon 68249, as SOURCE_ASSERTION and the AB303063.1 locus as CLUSTER_UNSTATED. Locus coordinates and evidence methods are absent in this retained row; the source class is PKS. Neither a shared species occurrence nor the sibling antimicrobial label upgrades these grades. The saved questionable quality and unknown completeness are source metadata, not independently adjudicated defects or evidence that a pathway has been fully resolved.

### Citation roles

evidence: supported. Targets: naturalproductmech:mibig-608a44baf3.

PMID:17827660 is the entry-level MIBiG citation. Nine LOTUS rows preserve nine literal DOI placements, including one genus-level Streptomyces record and eight Streptomyces pactum records; their publications were not reopened or treated as independent experiments merely because the strings differ. AntibioticMech’s exact-key association is pinned to commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976. That versioned sibling link is distinct from primary producer, structural and pharmacological evidence.

### Occurrence and activity scope

evidence: supported. Targets: naturalproductmech:mibig-608a44baf3.

The owner preserves nine LOTUS occurrence placements: one at genus ID 1883 and eight at species ID 68249. Cached species synonyms retain pactum/pactus wording locally without a taxonomy refresh. The exact-key AntibioticMech row supplies ANTIBACTERIAL and the corresponding coarse bioactivity_summary; the owner has no detailed assay observations or molecular-target root, and the PubChem/binding frames are empty. No potency, target, activity mechanism or assay inactivity is inferred from the sibling summary or local no-match frames.

### Versioned classification applicability

consistency: concern. Targets: naturalproductmech:mibig-608a44baf3.

The model faithfully reports Terpenoids with empty superclass/class arrays and glycoside:false, while MIBiG reports PKS. The saved topology contains two aromatic rings, a multiply substituted aminocyclopentane, ester, aromatic ketone and a urea/imidic group; it does not independently establish a terpene biosynthetic origin. The model/source-class tension is an applicability concern, not a demonstrated wrong source structure or a license to replace the filing category. No separate sugar residue is identified from the stored topology; the faithful versioned prediction remains preserved.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-608a44baf3.

The complete current owner/history, actual intake, all twelve selected source rows, relevant cached taxonomy and both complete molecular forms were read. The two false canonical comparisons and empty atom map are retained rather than normalized away. All four mechanism roots are absent. Full QC, complete OAK authority coverage and fresh external verification remain unavailable; no supported source-edit finding or action is established, and this review remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2369-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/pactamycin.yaml; Whole current plaintext; complete curation_history | supports | Whole current owner and all 3 history events retain the exact prior complete reading. Native status SEEDED is unchanged. |
| support-2369-capture | /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json; /records/8/owner_document | supports | Accepted whole-owner capture preserves every field and establishes the absence of all four selected mechanism roots. No maintained-reader result is applicable. |
| support-2369-grounding-owner | /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Exact identifier, full key, stored structures, retained labels and grounding provenance. Natural identity is not freshly verified. |
| support-2369-origin-owner | /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/producer_taxon_groups; /records/8/owner_document/biosynthetic_gene_clusters | supports | Retained producer/locus grades, method labels, source versions and citation roles remain separate claims. |
| support-2369-classification-owner | /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/bgc_class | supports | Versioned model predictions, filing and source BGC/compound classes are separately preserved. |
| support-2369-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json; /records/8/owner_document/occurrences | supports | The whole selected owner preserves 9 written occurrence placements. |
| support-2369-activity-owner | /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json; /records/8/owner_document | supports | Whole owner retains the coarse ANTIBACTERIAL summary and versioned SAME_INCHIKEY sibling relation, with no detailed assay observations or molecular-target root. |
| support-2369-chemistry | /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/comparisons; /records/8/atom_correspondence; /records/8/formula_comparison_scope | supports | The two canonical-SMILES flags remain false and the saved atom map empty; equal normalized identifiers/formula/charge do not prove fixed-graph identity. |
| support-2369-topology | /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles/computed; /records/8/inchi/computed; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/comparisons; /records/8/atom_correspondence | supports | Both forms have neutral C28H38N4O8, 40 heavy atoms and 42 bonds, with six specified tetrahedral centers. The stored SMILES has urea N22(H)–C23(=O24)–N25(Me2); the InChI-derived form has N30=C24(–O36H)–N31(Me2), consistent with the retained mobile-H layer (H,31,37). Hydrogen moves from the urea nitrogen to oxygen and the C–N/C–O bond orders change. The reconstructed C=N adds one unspecified double-bond site. Both canonical-SMILES comparisons remain false and the chirality-aware atom map remains empty. This is a bounded normalization interpretation, not a claim of identical fixed graphs, a different natural compound or missing experimental stereochemistry. |
| support-2369-intake | /private/tmp/npm-review-work/shared-next-batch237/intakes/2369-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake preserves this target, correction ownership and all 37 exact source inputs. |
| support-2369-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch237/root-intake-acceptance-001.json; /accepted; /status; /source_header; /records/8 | supports | ROOT accepts the original canonical intake and its current working-tree input provenance; scientific conclusions are separate. |
| support-2369-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch237/root-source-inventory-acceptance-001.json; /accepted; /status; /inventory; /totals | supports | ROOT accepts the original saved source inventory and current input scope; source meanings retain explicit reading attribution. |
| support-2369-plan | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-target-input-plan-001.json; /records/8 | supports | The final source plan preserves this actual intake map and direct context scope, with no source-query replay or input refresh. |
| support-2369-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch237/root-input-plan-acceptance-001.json; /accepted; /status | supports | ROOT accepts the actual source plan after reconciliation with all ten original intake maps. |
| support-2369-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution; /comparison_exceptions; /scope | supports | ROOT accepts the single original twenty-form diagnostic; Pactamycin false comparisons remain listed, and two warnings are global and unassigned. |
| support-2369-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-execution-001.json; /observer; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | ROOT operated the original diagnostic once. Scientific authoring does not replay parsing or alter stored forms. |
| support-2369-diagnostic-warnings | /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-original-001.stderr; Whole original stderr stream | supports | Exactly two omitted-undefined-stereo warnings are retained globally, without assignment to particular owners. |
| support-2369-source-reading | /private/tmp/npm-review-work/shared-next-batch237-tentative/support-prep/support-current237-source-reading-001.json; /personal_reading; /source_cautions; /counts; /cache | supports | Support completely read its assigned 26 contexts/113 rows/234 frames and all 20 cached stanzas; prior whole raw/history and BGC companion attributions remain explicit. |
| support-2369-curation-scope | /private/tmp/npm-review-work/shared-next-batch237/root-curation-scan-001.json; /scope; /scans | supports | ROOT’s ignored-inclusive bounded literal scan reports no matching rows. Reserved decisions.tsv was inspected but remains unconsumed and is not an effective correction owner. |
| support-2369-source-routes | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/matched_chebi_ids; /contexts/25/source_scope_inventory/source_taxa; /contexts/25/source_scope_inventory/forward_taxon_merge_matches; /contexts/25/source_scope_inventory/nonorganism_matches; /contexts/25/source_scope_inventory/actual_assay_rows; /contexts/25/source_scope_inventory/blank_AID_sentinels; /contexts/25/source_scope_inventory/related_corpus_rows | supports | Exact retained route metadata has no actual AID rows, forward merges or nonorganism rows; 0 blank-AID sentinels are preserved as such. |
| support-2369-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/11 | supports | Relevant complete cached names and synonyms are local taxonomy evidence; no fresh authority or producer-grade transfer is inferred. |
| support-2369-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/mibig_compounds | supports | Complete exact retained mibig_compounds query frame: 1 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 155–155, row_sha256 c0b1574a93eaa4d13b04731e1666950d446f915f9625d951d601e7b7b9436fbd | supports | All 1 physical rows and every field equal the saved frame. Claim-specific meanings are scoped in the linked assessments. |
| support-2369-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/chebi_structures | supports | Complete exact retained chebi_structures query frame: 0 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/lotus_occurrences | supports | Complete exact retained lotus_occurrences query frame: 9 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 9420–9420, row_sha256 f34276c3eac647dab3a1ee3fd6ed8248ba93a942854b50bd7b533afbb12fed2b; physical lines 9421–9421, row_sha256 52af53303780da3cb99d60e91f4dfade003933bd76a1c15310df6f59adf5469a; physical lines 9422–9422, row_sha256 a04cf13ce641c3b347247f5b75a274d5943ab590b2af36a5458c7a3191500ef0; physical lines 9423–9423, row_sha256 eca15895bb25dae420a21786c6416bb33af835bac0e99068e013fd8be0cfe715; physical lines 9424–9424, row_sha256 58ecb75de0a01ffa7f9d643479081c5d6eb29d897160847b11898e92b37c72e4; physical lines 9425–9425, row_sha256 f89cfe2049f16e5b844d6b6f4c1d46b7f7ee39f7614ba70c6a49f63122f29277; physical lines 9426–9426, row_sha256 8bb5defbdaaecbc0f72cc19ccc706fce7144d2d3ceb7b3790a8ab5bad235df36; physical lines 9427–9427, row_sha256 6960b1dd0c6fdb666c3b677d3048b86e35c99f7cd35a5cbc4c45544cf1285165; physical lines 9428–9428, row_sha256 e3c858155c8dafdf528c07aaa5921bb3e6cf64d47a6c76220c9530101ed33171 | supports | All 9 physical rows and every field equal the saved frame. Claim-specific meanings are scoped in the linked assessments. |
| support-2369-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete exact retained cyanometdb_occurrences query frame: 0 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/npclassifier | supports | Complete exact retained npclassifier query frame: 1 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2703–2703, row_sha256 324faba42b29053516f543c0a192378072353aa050882b2561327f7bd0ba7d8b | supports | All 1 physical rows and every field equal the saved frame. Claim-specific meanings are scoped in the linked assessments. |
| support-2369-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/pubchem_bioassay | supports | Complete exact retained pubchem_bioassay query frame: 0 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/bindingdb_targets | supports | Complete exact retained bindingdb_targets query frame: 0 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete exact retained antibioticmech_inchikeys query frame: 1 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-source-antibioticmech_inchikeys | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Header line 1; physical lines 2500–2500, row_sha256 bd5c669fd8c4357dc70ae4f0aefe92ef9d1da34db75e540e30ff768f0e5e2265 | supports | All 1 physical rows and every field equal the saved frame. Claim-specific meanings are scoped in the linked assessments. |
| support-2369-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/chebi_origins | supports | Complete exact retained chebi_origins query frame: 0 positive placements. No-match scope is limited to the saved predicate and snapshot. |
| support-2369-direct-contexts | /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json; /records/8/direct_companion_paths; /records/8/direct_companion_predicates | supports | All 0 admitted direct companion contexts retain exact identity, source and whole-raw scopes; no mechanism, occurrence or activity is transferred to this selected owner. |
| support-2369-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 368–435 | supports | Schema preserves source SMILES and partial stereochemistry and treats computed classification as a named/versioned prediction, not a source assertion. |
| support-2369-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 145–174 | supports | The retained stereo_complete method checks undefined tetrahedral centers in source SMILES. It does not independently establish natural stereochemistry or every potential double-bond configuration. |
| support-2369-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 296–307; lines 982–1020 | supports | Maintained source harmonization copies retained structures, stereo flags and versioned classifications; no regeneration or source edit occurred. |
| support-2369-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current scientific dimension profile | supports | Scientific dimensions and partial completion preserve unavailable required checks and evidence-access limitations. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-237/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-237/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-237/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-237/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-237/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. Natural identity, primary publications, current taxonomy and external identifiers were not freshly verified.
- Full QC, complete OAK authority coverage and fresh external verification remain unavailable; successful local gates and parsing do not substitute for them.
- Exact no-match queries and cached names have bounded snapshot scope. Shared loci, taxa or citations do not transfer claims across distinct full keys.
- Two original omitted-undefined-stereo warnings remain global and unassigned. Pactamycin’s false canonical comparisons and empty atom match remain visible.
- No source record, native status or history was edited. Model applicability concerns do not automatically constitute a maintained-source defect.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read the five complete owners/history, actual intakes, all ten saved molecular forms and assigned complete source payloads/cache. Exact prior companion-reading carries remain attributed.
- The complete molecular reading covers 248 atom and 272 bond rows plus all scalar/ring/stereo/motif/map fields using lossless table factoring, with no new molecular parse.
- ROOT operated capture, source inventory/composer, intakes and diagnostic; Native operated five local gates. Scientific authoring invoked no target. There are no applicable selected maintained readers.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T074022Z-pactamycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: pactamycin'
started_at: '2026-11-04T07:03:23.606992Z'
finished_at: '2026-11-04T07:40:22.311873Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Pactamycin retains exact local source-key grounding and a clearly limited
  urea/imidic representation difference. Its two canonical-SMILES equality flags are
  false and the saved atom map is empty despite equal standardized InChI, full key,
  formula and charge. The Terpenoids prediction versus PKS source class remains an
  applicability concern; the sibling ANTIBACTERIAL assertion supplies no fresh assay
  or mechanism. No source defect is proved; completion is partial.
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
  - path: data/natural_products/terpenoids/pactamycin.yaml
    sha256: 03df945ecfc0635a09f40744d08307613cf2935f7d7e2f95479c47f42e3f59a0
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
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2369; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-608a44baf3
targets:
- target_id: naturalproductmech:mibig-608a44baf3
  path: data/natural_products/terpenoids/pactamycin.yaml
  label: pactamycin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Retained MIBiG structure, producer and compound-specific locus assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned computed classification and filing assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained extraction of MIBiG compound names, structures, stereochemistry
      flags and source provenance.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Retained cited occurrence assertions, distinct from demonstrated production.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  command: just validate-strict data/natural_products/terpenoids/nanangelenin-a.yaml
    data/natural_products/terpenoids/napyradiomycin-a80915c.yaml data/natural_products/terpenoids/napyradiomycin.yaml
    data/natural_products/terpenoids/nfat-133.yaml data/natural_products/terpenoids/nivalenol.yaml
    data/natural_products/terpenoids/norbotrydialone-acetate.yaml data/natural_products/terpenoids/o-methylkolavelool.yaml
    data/natural_products/terpenoids/oryzalides.yaml data/natural_products/terpenoids/pactamycin.yaml
    data/natural_products/terpenoids/penifulvin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-237/validate-strict-selected10-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-strict_ten
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-strict_full
  name: strict_full
  status: passed
  required: true
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-237/validate-all-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-strict_full
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-lockfile
  name: lockfile
  status: passed
  required: true
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  command: just verify-corpus --summary
  exit_code: 0
  evidence_ids:
  - root-native-lockfile
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-reproduction
  name: reproduction
  status: passed
  required: true
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  command: just verify-reproduction
  exit_code: 0
  evidence_ids:
  - root-native-reproduction
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-native-queue
  name: queue
  status: passed
  required: true
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-237/review-queue-001.tsv
  exit_code: 0
  evidence_ids:
  - root-native-queue
  scope_note: Batch-local execution also covers this individual target; full-corpus
    checks retain their full scope.
- check_id: root-full-qc
  name: Full just qc
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2369-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/pactamycin.yaml
  locator: Whole current plaintext; complete curation_history
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Whole current owner and all 3 history events retain the exact prior complete
    reading. Native status SEEDED is unchanged.
  snapshot_sha256: 03df945ecfc0635a09f40744d08307613cf2935f7d7e2f95479c47f42e3f59a0
- evidence_id: support-2369-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Accepted whole-owner capture preserves every field and establishes the
    absence of all four selected mechanism roots. No maintained-reader result is applicable.
  snapshot_sha256: 9b3e6f1d83156b5a3fcdf3db8fe1413f8005781c272fca2e15a9d29989242802
- evidence_id: support-2369-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Exact identifier, full key, stored structures, retained labels and grounding
    provenance. Natural identity is not freshly verified.
  snapshot_sha256: 9b3e6f1d83156b5a3fcdf3db8fe1413f8005781c272fca2e15a9d29989242802
- evidence_id: support-2369-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/producer_taxon_groups;
    /records/8/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Retained producer/locus grades, method labels, source versions and citation
    roles remain separate claims.
  snapshot_sha256: 9b3e6f1d83156b5a3fcdf3db8fe1413f8005781c272fca2e15a9d29989242802
- evidence_id: support-2369-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/bgc_class
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Versioned model predictions, filing and source BGC/compound classes are
    separately preserved.
  snapshot_sha256: 9b3e6f1d83156b5a3fcdf3db8fe1413f8005781c272fca2e15a9d29989242802
- evidence_id: support-2369-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json
  locator: /records/8/owner_document/occurrences
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: The whole selected owner preserves 9 written occurrence placements.
  snapshot_sha256: 9b3e6f1d83156b5a3fcdf3db8fe1413f8005781c272fca2e15a9d29989242802
- evidence_id: support-2369-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Whole owner retains the coarse ANTIBACTERIAL summary and versioned SAME_INCHIKEY
    sibling relation, with no detailed assay observations or molecular-target root.
  snapshot_sha256: 9b3e6f1d83156b5a3fcdf3db8fe1413f8005781c272fca2e15a9d29989242802
- evidence_id: support-2369-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/comparisons;
    /records/8/atom_correspondence; /records/8/formula_comparison_scope
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: The two canonical-SMILES flags remain false and the saved atom map empty;
    equal normalized identifiers/formula/charge do not prove fixed-graph identity.
  snapshot_sha256: 92baf43612ba12d1b53cf4f6525f662a4219eb0b4275b05a88194fc07407ba14
- evidence_id: support-2369-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles/computed; /records/8/inchi/computed; /records/8/declared_structure;
    /records/8/literal_InChI_layers; /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Both forms have neutral C28H38N4O8, 40 heavy atoms and 42 bonds, with six
    specified tetrahedral centers. The stored SMILES has urea N22(H)–C23(=O24)–N25(Me2);
    the InChI-derived form has N30=C24(–O36H)–N31(Me2), consistent with the retained
    mobile-H layer (H,31,37). Hydrogen moves from the urea nitrogen to oxygen and
    the C–N/C–O bond orders change. The reconstructed C=N adds one unspecified double-bond
    site. Both canonical-SMILES comparisons remain false and the chirality-aware atom
    map remains empty. This is a bounded normalization interpretation, not a claim
    of identical fixed graphs, a different natural compound or missing experimental
    stereochemistry.
  snapshot_sha256: 92baf43612ba12d1b53cf4f6525f662a4219eb0b4275b05a88194fc07407ba14
- evidence_id: support-2369-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/intakes/2369-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Actual canonical intake preserves this target, correction ownership and
    all 37 exact source inputs.
  snapshot_sha256: 95555a0bd683155ead77b5f0ca8b3a2388d9a12a5a355f64f41f2e39fbd35ff9
- evidence_id: support-2369-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/root-intake-acceptance-001.json
  locator: /accepted; /status; /source_header; /records/8
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: ROOT accepts the original canonical intake and its current working-tree
    input provenance; scientific conclusions are separate.
  snapshot_sha256: 28e998429758bcbc0ee2fdfe63d869332148752d712908d306742f655aca0392
- evidence_id: support-2369-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/root-source-inventory-acceptance-001.json
  locator: /accepted; /status; /inventory; /totals
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: ROOT accepts the original saved source inventory and current input scope;
    source meanings retain explicit reading attribution.
  snapshot_sha256: e0324b77ef0f43df70b1989903c180959876b3fcceace602dc27bad3189a5869
- evidence_id: support-2369-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-target-input-plan-001.json
  locator: /records/8
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: The final source plan preserves this actual intake map and direct context
    scope, with no source-query replay or input refresh.
  snapshot_sha256: eaef6d60480b80c6cb9b74fa33ac8f1432d12ee2ddf5c1bce577d6629cc45107
- evidence_id: support-2369-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/root-input-plan-acceptance-001.json
  locator: /accepted; /status
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: ROOT accepts the actual source plan after reconciliation with all ten original
    intake maps.
  snapshot_sha256: 89bac599b6ac34b491f0fd22a19054049b6b4156052a3b8867e72f00cae0e74b
- evidence_id: support-2369-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution; /comparison_exceptions; /scope
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: ROOT accepts the single original twenty-form diagnostic; Pactamycin false
    comparisons remain listed, and two warnings are global and unassigned.
  snapshot_sha256: 9942879304b1c5f624b58778a9ea954acac1a9c61093a1bf330b7dbab444ba06
- evidence_id: support-2369-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-execution-001.json
  locator: /observer; /command; /started_at; /finished_at; /exit_code; /source; /stdout;
    /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: ROOT operated the original diagnostic once. Scientific authoring does not
    replay parsing or alter stored forms.
  snapshot_sha256: 91ea59067391942792f393af6b81083be1cd799f6f8b544c58423427dba5c2c9
- evidence_id: support-2369-diagnostic-warnings
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr stream
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Exactly two omitted-undefined-stereo warnings are retained globally, without
    assignment to particular owners.
  snapshot_sha256: a2c258ce1c32f8991b7c4cd4bf7069eb7a259cbc77f70451817082176b429a10
- evidence_id: support-2369-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/support-prep/support-current237-source-reading-001.json
  locator: /personal_reading; /source_cautions; /counts; /cache
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Support completely read its assigned 26 contexts/113 rows/234 frames and
    all 20 cached stanzas; prior whole raw/history and BGC companion attributions
    remain explicit.
  snapshot_sha256: 3929185d7e4dddd8d1f022e0513aef70346ebe586125f0d826c086e3c075c3d0
- evidence_id: support-2369-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237/root-curation-scan-001.json
  locator: /scope; /scans
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: ROOT’s ignored-inclusive bounded literal scan reports no matching rows.
    Reserved decisions.tsv was inspected but remains unconsumed and is not an effective
    correction owner.
  snapshot_sha256: fc3cd228e13694ece7f79846f3ac529e5ea675e75a265b2e40c244149c54bb1a
- evidence_id: support-2369-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/matched_chebi_ids; /contexts/25/source_scope_inventory/source_taxa;
    /contexts/25/source_scope_inventory/forward_taxon_merge_matches; /contexts/25/source_scope_inventory/nonorganism_matches;
    /contexts/25/source_scope_inventory/actual_assay_rows; /contexts/25/source_scope_inventory/blank_AID_sentinels;
    /contexts/25/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Exact retained route metadata has no actual AID rows, forward merges or
    nonorganism rows; 0 blank-AID sentinels are preserved as such.
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/11
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Relevant complete cached names and synonyms are local taxonomy evidence;
    no fresh authority or producer-grade transfer is inferred.
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained mibig_compounds query frame: 1 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 155–155, row_sha256 c0b1574a93eaa4d13b04731e1666950d446f915f9625d951d601e7b7b9436fbd
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: All 1 physical rows and every field equal the saved frame. Claim-specific
    meanings are scoped in the linked assessments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2369-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained chebi_structures query frame: 0 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained lotus_occurrences query frame: 9 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 9420–9420, row_sha256 f34276c3eac647dab3a1ee3fd6ed8248ba93a942854b50bd7b533afbb12fed2b;
    physical lines 9421–9421, row_sha256 52af53303780da3cb99d60e91f4dfade003933bd76a1c15310df6f59adf5469a;
    physical lines 9422–9422, row_sha256 a04cf13ce641c3b347247f5b75a274d5943ab590b2af36a5458c7a3191500ef0;
    physical lines 9423–9423, row_sha256 eca15895bb25dae420a21786c6416bb33af835bac0e99068e013fd8be0cfe715;
    physical lines 9424–9424, row_sha256 58ecb75de0a01ffa7f9d643479081c5d6eb29d897160847b11898e92b37c72e4;
    physical lines 9425–9425, row_sha256 f89cfe2049f16e5b844d6b6f4c1d46b7f7ee39f7614ba70c6a49f63122f29277;
    physical lines 9426–9426, row_sha256 8bb5defbdaaecbc0f72cc19ccc706fce7144d2d3ceb7b3790a8ab5bad235df36;
    physical lines 9427–9427, row_sha256 6960b1dd0c6fdb666c3b677d3048b86e35c99f7cd35a5cbc4c45544cf1285165;
    physical lines 9428–9428, row_sha256 e3c858155c8dafdf528c07aaa5921bb3e6cf64d47a6c76220c9530101ed33171
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: All 9 physical rows and every field equal the saved frame. Claim-specific
    meanings are scoped in the linked assessments.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2369-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained cyanometdb_occurrences query frame: 0 positive
    placements. No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained npclassifier query frame: 1 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2703–2703, row_sha256 324faba42b29053516f543c0a192378072353aa050882b2561327f7bd0ba7d8b
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: All 1 physical rows and every field equal the saved frame. Claim-specific
    meanings are scoped in the linked assessments.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2369-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained pubchem_bioassay query frame: 0 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained bindingdb_targets query frame: 0 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained antibioticmech_inchikeys query frame: 1 positive
    placements. No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-source-antibioticmech_inchikeys
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Header line 1; physical lines 2500–2500, row_sha256 bd5c669fd8c4357dc70ae4f0aefe92ef9d1da34db75e540e30ff768f0e5e2265
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: All 1 physical rows and every field equal the saved frame. Claim-specific
    meanings are scoped in the linked assessments.
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: support-2369-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: 'Complete exact retained chebi_origins query frame: 0 positive placements.
    No-match scope is limited to the saved predicate and snapshot.'
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch237-tentative/bgc-prep/bgc-conditional237-source-inventory-DATA-001.json
  locator: /records/8/direct_companion_paths; /records/8/direct_companion_predicates
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: All 0 admitted direct companion contexts retain exact identity, source
    and whole-raw scopes; no mechanism, occurrence or activity is transferred to this
    selected owner.
  snapshot_sha256: 472b28784488627c9ebf35fa9156501dae51875670b5be9c40d0bc31fe2b0442
- evidence_id: support-2369-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 368–435
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Schema preserves source SMILES and partial stereochemistry and treats computed
    classification as a named/versioned prediction, not a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2369-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 145–174
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: The retained stereo_complete method checks undefined tetrahedral centers
    in source SMILES. It does not independently establish natural stereochemistry
    or every potential double-bond configuration.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2369-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 296–307; lines 982–1020
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Maintained source harmonization copies retained structures, stereo flags
    and versioned classifications; no regeneration or source edit occurred.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2369-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current scientific dimension profile
  accessed_at: '2026-11-04T07:28:13.305627Z'
  support: supports
  summary: Scientific dimensions and partial completion preserve unavailable required
    checks and evidence-access limitations.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-237/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json
  accessed_at: '2026-11-04T07:10:52.488555Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: a67703f15d70f98f104d4f0d65e17b98ad3f5e826cd127e36500ea7e391e9e99
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-237/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json
  accessed_at: '2026-11-04T07:11:19.100254Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 51425f681f8e5f97614d36e3f41df583b16f6519c5d351e9c64404b53155360f
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-237/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json
  accessed_at: '2026-11-04T07:11:39.309162Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-237/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json
  accessed_at: '2026-11-04T07:12:14.319656Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-237/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-237/native-current237-five-gates-execution-001.json
  accessed_at: '2026-11-04T07:12:26.404016Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 2409cc8f74b1a429154f6b7b3be2ea91a4d405c1ac046a41284f31268fdb4d90
assessments:
- assessment_id: support-2369-identity
  area: identity
  topic: Retained structure and identifier correspondence
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-608a44baf3 and full key
    WVIUOSJLUCTGFK-JUJPXXQGSA-N agree with MIBiG BGC0000118 version 5 and the exact-key
    AntibioticMech row. The retained PubChem link is 5289124, and no exact-key ChEBI
    structure is returned. Both stored forms reproduce the declared standardized key,
    but that does not resolve their fixed-bond representation difference or authenticate
    natural identity. SAME_INCHIKEY is the stated basis for the sibling SAME_STRUCTURE
    relation, not a new proof of every stereochemical and tautomeric detail.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-grounding-owner
  - support-2369-source-mibig_compounds
  - support-2369-query-chebi_structures
  - support-2369-chemistry
  - support-2369-direct-contexts
  - support-2369-source-antibioticmech_inchikeys
  dimensions:
  - name: standard_inchi_key
    value: WVIUOSJLUCTGFK-JUJPXXQGSA-N; exact retained full key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - support-2369-grounding-owner
    - support-2369-source-mibig_compounds
    - support-2369-query-chebi_structures
    - support-2369-chemistry
    - support-2369-direct-contexts
    - support-2369-source-antibioticmech_inchikeys
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-608a44baf3 and full key
      WVIUOSJLUCTGFK-JUJPXXQGSA-N agree with MIBiG BGC0000118 version 5 and the exact-key
      AntibioticMech row. The retained PubChem link is 5289124, and no exact-key ChEBI
      structure is returned. Both stored forms reproduce the declared standardized
      key, but that does not resolve their fixed-bond representation difference or
      authenticate natural identity. SAME_INCHIKEY is the stated basis for the sibling
      SAME_STRUCTURE relation, not a new proof of every stereochemical and tautomeric
      detail.
    definition: Retained local grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2369-grounding-owner
    - support-2369-source-mibig_compounds
    - support-2369-query-chebi_structures
    - support-2369-chemistry
    - support-2369-direct-contexts
    - support-2369-source-antibioticmech_inchikeys
- assessment_id: support-2369-representation
  area: representation
  topic: Stored representation and stereochemical scope
  outcome: supported
  summary: Both forms have neutral C28H38N4O8, 40 heavy atoms and 42 bonds, with six
    specified tetrahedral centers. The stored SMILES has urea N22(H)–C23(=O24)–N25(Me2);
    the InChI-derived form has N30=C24(–O36H)–N31(Me2), consistent with the retained
    mobile-H layer (H,31,37). Hydrogen moves from the urea nitrogen to oxygen and
    the C–N/C–O bond orders change. The reconstructed C=N adds one unspecified double-bond
    site. Both canonical-SMILES comparisons remain false and the chirality-aware atom
    map remains empty. This is a bounded normalization interpretation, not a claim
    of identical fixed graphs, a different natural compound or missing experimental
    stereochemistry.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-grounding-owner
  - support-2369-chemistry
  - support-2369-topology
  - support-2369-diagnostic-acceptance
  - support-2369-structure-schema
  - support-2369-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms have neutral C28H38N4O8, 40 heavy atoms and 42 bonds, with six
      specified tetrahedral centers. The stored SMILES has urea N22(H)–C23(=O24)–N25(Me2);
      the InChI-derived form has N30=C24(–O36H)–N31(Me2), consistent with the retained
      mobile-H layer (H,31,37). Hydrogen moves from the urea nitrogen to oxygen and
      the C–N/C–O bond orders change. The reconstructed C=N adds one unspecified double-bond
      site. Both canonical-SMILES comparisons remain false and the chirality-aware
      atom map remains empty. This is a bounded normalization interpretation, not
      a claim of identical fixed graphs, a different natural compound or missing experimental
      stereochemistry.
    definition: Complete saved stereo, atom and bond interpretation; no new parse
      or experimental assignment.
    evidence_ids:
    - support-2369-grounding-owner
    - support-2369-chemistry
    - support-2369-topology
    - support-2369-diagnostic-acceptance
    - support-2369-structure-schema
    - support-2369-stereo-method
  - name: representation_correspondence
    value: Both forms have neutral C28H38N4O8, 40 heavy atoms and 42 bonds, with six
      specified tetrahedral centers. The stored SMILES has urea N22(H)–C23(=O24)–N25(Me2);
      the InChI-derived form has N30=C24(–O36H)–N31(Me2), consistent with the retained
      mobile-H layer (H,31,37). Hydrogen moves from the urea nitrogen to oxygen and
      the C–N/C–O bond orders change. The reconstructed C=N adds one unspecified double-bond
      site. Both canonical-SMILES comparisons remain false and the chirality-aware
      atom map remains empty. This is a bounded normalization interpretation, not
      a claim of identical fixed graphs, a different natural compound or missing experimental
      stereochemistry.
    definition: Normalized identifier agreement does not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2369-grounding-owner
    - support-2369-chemistry
    - support-2369-topology
    - support-2369-diagnostic-acceptance
    - support-2369-structure-schema
    - support-2369-stereo-method
- assessment_id: support-2369-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: MIBiG BGC0000118 version 5 records Streptomyces pactum, taxon 68249, as
    SOURCE_ASSERTION and the AB303063.1 locus as CLUSTER_UNSTATED. Locus coordinates
    and evidence methods are absent in this retained row; the source class is PKS.
    Neither a shared species occurrence nor the sibling antimicrobial label upgrades
    these grades. The saved questionable quality and unknown completeness are source
    metadata, not independently adjudicated defects or evidence that a pathway has
    been fully resolved.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-origin-owner
  - support-2369-source-mibig_compounds
  - support-2369-cached-taxonomy
  - support-2369-source-routes
  - support-2369-direct-contexts
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0000118 version 5 records Streptomyces pactum, taxon 68249, as
      SOURCE_ASSERTION and the AB303063.1 locus as CLUSTER_UNSTATED. Locus coordinates
      and evidence methods are absent in this retained row; the source class is PKS.
      Neither a shared species occurrence nor the sibling antimicrobial label upgrades
      these grades. The saved questionable quality and unknown completeness are source
      metadata, not independently adjudicated defects or evidence that a pathway has
      been fully resolved.
    definition: Producer, occurrence, species, strain and unresolved labels retain
      separate scope; cached labels are not fresh authority.
    evidence_ids:
    - support-2369-origin-owner
    - support-2369-source-mibig_compounds
    - support-2369-cached-taxonomy
    - support-2369-source-routes
    - support-2369-direct-contexts
  - name: producer_evidence
    value: MIBiG BGC0000118 version 5 records Streptomyces pactum, taxon 68249, as
      SOURCE_ASSERTION and the AB303063.1 locus as CLUSTER_UNSTATED. Locus coordinates
      and evidence methods are absent in this retained row; the source class is PKS.
      Neither a shared species occurrence nor the sibling antimicrobial label upgrades
      these grades. The saved questionable quality and unknown completeness are source
      metadata, not independently adjudicated defects or evidence that a pathway has
      been fully resolved.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - support-2369-origin-owner
    - support-2369-source-mibig_compounds
    - support-2369-cached-taxonomy
    - support-2369-source-routes
    - support-2369-direct-contexts
  - name: locus_evidence
    value: MIBiG BGC0000118 version 5 records Streptomyces pactum, taxon 68249, as
      SOURCE_ASSERTION and the AB303063.1 locus as CLUSTER_UNSTATED. Locus coordinates
      and evidence methods are absent in this retained row; the source class is PKS.
      Neither a shared species occurrence nor the sibling antimicrobial label upgrades
      these grades. The saved questionable quality and unknown completeness are source
      metadata, not independently adjudicated defects or evidence that a pathway has
      been fully resolved.
    definition: Source version, status, method and grade are not a complete pathway
      or fresh primary verification.
    evidence_ids:
    - support-2369-origin-owner
    - support-2369-source-mibig_compounds
    - support-2369-cached-taxonomy
    - support-2369-source-routes
    - support-2369-direct-contexts
- assessment_id: support-2369-citations
  area: evidence
  topic: Citation roles
  outcome: supported
  summary: PMID:17827660 is the entry-level MIBiG citation. Nine LOTUS rows preserve
    nine literal DOI placements, including one genus-level Streptomyces record and
    eight Streptomyces pactum records; their publications were not reopened or treated
    as independent experiments merely because the strings differ. AntibioticMech’s
    exact-key association is pinned to commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976.
    That versioned sibling link is distinct from primary producer, structural and
    pharmacological evidence.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-origin-owner
  - support-2369-occurrence-owner
  - support-2369-source-mibig_compounds
  - support-2369-source-reading
  - support-2369-source-lotus_occurrences
  - support-2369-source-antibioticmech_inchikeys
  dimensions:
  - name: citation_scope
    value: PMID:17827660 is the entry-level MIBiG citation. Nine LOTUS rows preserve
      nine literal DOI placements, including one genus-level Streptomyces record and
      eight Streptomyces pactum records; their publications were not reopened or treated
      as independent experiments merely because the strings differ. AntibioticMech’s
      exact-key association is pinned to commit 74f6cc8362498900f2fe2c13d0b6fdb66dd30976.
      That versioned sibling link is distinct from primary producer, structural and
      pharmacological evidence.
    definition: Database provenance and occurrence citations retain distinct roles;
      no publication independence or fresh source access is assumed.
    evidence_ids:
    - support-2369-origin-owner
    - support-2369-occurrence-owner
    - support-2369-source-mibig_compounds
    - support-2369-source-reading
    - support-2369-source-lotus_occurrences
    - support-2369-source-antibioticmech_inchikeys
- assessment_id: support-2369-occurrence
  area: evidence
  topic: Occurrence and activity scope
  outcome: supported
  summary: 'The owner preserves nine LOTUS occurrence placements: one at genus ID
    1883 and eight at species ID 68249. Cached species synonyms retain pactum/pactus
    wording locally without a taxonomy refresh. The exact-key AntibioticMech row supplies
    ANTIBACTERIAL and the corresponding coarse bioactivity_summary; the owner has
    no detailed assay observations or molecular-target root, and the PubChem/binding
    frames are empty. No potency, target, activity mechanism or assay inactivity is
    inferred from the sibling summary or local no-match frames.'
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-occurrence-owner
  - support-2369-activity-owner
  - support-2369-source-routes
  - support-2369-cached-taxonomy
  - support-2369-direct-contexts
  - support-2369-query-lotus_occurrences
  - support-2369-query-chebi_origins
  - support-2369-query-cyanometdb_occurrences
  - support-2369-query-pubchem_bioassay
  - support-2369-query-bindingdb_targets
  - support-2369-query-antibioticmech_inchikeys
  - support-2369-source-antibioticmech_inchikeys
  dimensions:
  - name: occurrence_scope
    value: 'The owner preserves nine LOTUS occurrence placements: one at genus ID
      1883 and eight at species ID 68249. Cached species synonyms retain pactum/pactus
      wording locally without a taxonomy refresh. The exact-key AntibioticMech row
      supplies ANTIBACTERIAL and the corresponding coarse bioactivity_summary; the
      owner has no detailed assay observations or molecular-target root, and the PubChem/binding
      frames are empty. No potency, target, activity mechanism or assay inactivity
      is inferred from the sibling summary or local no-match frames.'
    definition: Occurrence placements are not counts of independent experiments or
      demonstrated producers.
    evidence_ids:
    - support-2369-occurrence-owner
    - support-2369-activity-owner
    - support-2369-source-routes
    - support-2369-cached-taxonomy
    - support-2369-direct-contexts
    - support-2369-query-lotus_occurrences
    - support-2369-query-chebi_origins
    - support-2369-query-cyanometdb_occurrences
    - support-2369-query-pubchem_bioassay
    - support-2369-query-bindingdb_targets
    - support-2369-query-antibioticmech_inchikeys
    - support-2369-source-antibioticmech_inchikeys
  - name: assay_target_scope
    value: 'The owner preserves nine LOTUS occurrence placements: one at genus ID
      1883 and eight at species ID 68249. Cached species synonyms retain pactum/pactus
      wording locally without a taxonomy refresh. The exact-key AntibioticMech row
      supplies ANTIBACTERIAL and the corresponding coarse bioactivity_summary; the
      owner has no detailed assay observations or molecular-target root, and the PubChem/binding
      frames are empty. No potency, target, activity mechanism or assay inactivity
      is inferred from the sibling summary or local no-match frames.'
    definition: Retained assay and target assertions are bounded; biosynthetic proteins
      are not pharmacological target evidence.
    evidence_ids:
    - support-2369-occurrence-owner
    - support-2369-activity-owner
    - support-2369-source-routes
    - support-2369-cached-taxonomy
    - support-2369-direct-contexts
    - support-2369-query-lotus_occurrences
    - support-2369-query-chebi_origins
    - support-2369-query-cyanometdb_occurrences
    - support-2369-query-pubchem_bioassay
    - support-2369-query-bindingdb_targets
    - support-2369-query-antibioticmech_inchikeys
    - support-2369-source-antibioticmech_inchikeys
- assessment_id: support-2369-classification
  area: consistency
  topic: Versioned classification applicability
  outcome: concern
  summary: The model faithfully reports Terpenoids with empty superclass/class arrays
    and glycoside:false, while MIBiG reports PKS. The saved topology contains two
    aromatic rings, a multiply substituted aminocyclopentane, ester, aromatic ketone
    and a urea/imidic group; it does not independently establish a terpene biosynthetic
    origin. The model/source-class tension is an applicability concern, not a demonstrated
    wrong source structure or a license to replace the filing category. No separate
    sugar residue is identified from the stored topology; the faithful versioned prediction
    remains preserved.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-classification-owner
  - support-2369-source-mibig_compounds
  - support-2369-source-npclassifier
  - support-2369-chemistry
  - support-2369-topology
  - support-2369-structure-schema
  - support-2369-classification-seeder
  dimensions:
  - name: classification_applicability
    value: The model faithfully reports Terpenoids with empty superclass/class arrays
      and glycoside:false, while MIBiG reports PKS. The saved topology contains two
      aromatic rings, a multiply substituted aminocyclopentane, ester, aromatic ketone
      and a urea/imidic group; it does not independently establish a terpene biosynthetic
      origin. The model/source-class tension is an applicability concern, not a demonstrated
      wrong source structure or a license to replace the filing category. No separate
      sugar residue is identified from the stored topology; the faithful versioned
      prediction remains preserved.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct evidence types.
    evidence_ids:
    - support-2369-classification-owner
    - support-2369-source-mibig_compounds
    - support-2369-source-npclassifier
    - support-2369-chemistry
    - support-2369-topology
    - support-2369-structure-schema
    - support-2369-classification-seeder
- assessment_id: support-2369-completion
  area: completeness
  topic: Review completion
  outcome: unknown
  summary: The complete current owner/history, actual intake, all twelve selected
    source rows, relevant cached taxonomy and both complete molecular forms were read.
    The two false canonical comparisons and empty atom map are retained rather than
    normalized away. All four mechanism roots are absent. Full QC, complete OAK authority
    coverage and fresh external verification remain unavailable; no supported source-edit
    finding or action is established, and this review remains partial.
  target_ids:
  - naturalproductmech:mibig-608a44baf3
  evidence_ids:
  - support-2369-owner
  - support-2369-capture
  - support-2369-intake
  - support-2369-intake-acceptance
  - support-2369-inventory-acceptance
  - support-2369-plan
  - support-2369-plan-acceptance
  - support-2369-source-reading
  - support-2369-curation-scope
  - support-2369-diagnostic-execution
  - support-2369-diagnostic-warnings
  - support-2369-diagnostic-acceptance
  - support-2369-review-profile
  - support-2369-query-mibig_compounds
  - support-2369-query-chebi_structures
  - support-2369-query-lotus_occurrences
  - support-2369-query-cyanometdb_occurrences
  - support-2369-query-npclassifier
  - support-2369-query-pubchem_bioassay
  - support-2369-query-bindingdb_targets
  - support-2369-query-antibioticmech_inchikeys
  - support-2369-query-chebi_origins
  dimensions:
  - name: review_completion
    value: The complete current owner/history, actual intake, all twelve selected
      source rows, relevant cached taxonomy and both complete molecular forms were
      read. The two false canonical comparisons and empty atom map are retained rather
      than normalized away. All four mechanism roots are absent. Full QC, complete
      OAK authority coverage and fresh external verification remain unavailable; no
      supported source-edit finding or action is established, and this review remains
      partial.
    definition: Completion reflects actual access and required-check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - support-2369-owner
    - support-2369-capture
    - support-2369-intake
    - support-2369-intake-acceptance
    - support-2369-inventory-acceptance
    - support-2369-plan
    - support-2369-plan-acceptance
    - support-2369-source-reading
    - support-2369-curation-scope
    - support-2369-diagnostic-execution
    - support-2369-diagnostic-warnings
    - support-2369-diagnostic-acceptance
    - support-2369-review-profile
    - support-2369-query-mibig_compounds
    - support-2369-query-chebi_structures
    - support-2369-query-lotus_occurrences
    - support-2369-query-cyanometdb_occurrences
    - support-2369-query-npclassifier
    - support-2369-query-pubchem_bioassay
    - support-2369-query-bindingdb_targets
    - support-2369-query-antibioticmech_inchikeys
    - support-2369-query-chebi_origins
findings: []
actions: []
limitations:
- All evidence is retained locally. Natural identity, primary publications, current
  taxonomy and external identifiers were not freshly verified.
- Full QC, complete OAK authority coverage and fresh external verification remain
  unavailable; successful local gates and parsing do not substitute for them.
- Exact no-match queries and cached names have bounded snapshot scope. Shared loci,
  taxa or citations do not transfer claims across distinct full keys.
- Two original omitted-undefined-stereo warnings remain global and unassigned. Pactamycin’s
  false canonical comparisons and empty atom match remain visible.
- No source record, native status or history was edited. Model applicability concerns
  do not automatically constitute a maintained-source defect.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read the five complete owners/history, actual intakes, all ten
  saved molecular forms and assigned complete source payloads/cache. Exact prior companion-reading
  carries remain attributed.
- The complete molecular reading covers 248 atom and 272 bond rows plus all scalar/ring/stereo/motif/map
  fields using lossless table factoring, with no new molecular parse.
- ROOT operated capture, source inventory/composer, intakes and diagnostic; Native
  operated five local gates. Scientific authoring invoked no target. There are no
  applicable selected maintained readers.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-237
```
