# Local evidence review: ferroverdin

- Review: 20261103T113308Z-ferroverdin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T11:08:47.845489Z
- Finished UTC: 2026-11-03T11:33:08.328860Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified local review of exact retained identity, source grades, stored molecular forms and claim scope; external verification and required full gates remain incomplete.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2205; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ac342ce038 | data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml | generated | ferroverdin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-ac342ce038 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-ac342ce038 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-ac342ce038 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-ac342ce038 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-ac342ce038 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-ac342ce038 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-ac342ce038 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-ac342ce038 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-ac342ce038.

The complete key OVMCOCUPINBXRQ-UHFFFAOYSA-K joins the retained BGC0001592 v5 compound and the MINTED Ferroverdin owner. Both declared forms explicitly represent three organic anions, sodium and Fe(II); this salt is not silently replaced by a neutral ligand or an assumed connected coordination complex. The exact retained ChEBI structure join is empty. The stored name and normalized key remain source identity assertions, not fresh isolate identification.

### Representation

representation: supported. Targets: naturalproductmech:mibig-ac342ce038.

Both saved forms yield C45H30FeN3NaO12, formal charge zero, 62 atoms, 63 bonds and five disconnected fragments. Three phenolate oxygens each carry −1, sodium +1 and iron +2; neither metal has any represented bond. The InChI main layer 3C15H11NO4.Fe.Na together with /q;;;+2;+1/p-3 explains the sole false literal-main-formula comparison. The two computed formulas and all other comparisons agree. No potential stereoelement is reported for this disconnected graph, which does not establish metal coordination geometry or coordination stereochemical completeness; full_graph_identity_established remains false.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-ac342ce038.

MIBiG BGC0001592 v5 is active/questionable/unknown and grades Streptomyces lunaelactis (NCBITaxon:1535768) SOURCE_ASSERTION and the locus CLUSTER_UNSTATED. Genome MG708299.1 and entry-level PMID:31409675 are retained, with no stated locus-evidence method. The cached species label agrees locally. No written occurrence or exact retained LOTUS/ChEBI-origin row supplies independent production evidence.

### Citations

evidence: unknown. Targets: naturalproductmech:mibig-ac342ce038.

PMID:31409675 is explicitly the MIBiG entry-level reference carried on both producer and locus. Repeating that reference in two fields does not make two experiments. The record has no separate occurrence or assay citation in the inspected source scope. The original article, genome and taxonomy accession were not freshly verified.

### Bioactivity

evidence: supported. Targets: naturalproductmech:mibig-ac342ce038.

The complete owner writes no occurrences, bioactivities, activity summary, molecular targets or mechanism roots. Its exact retained occurrence, PubChem, BindingDB and AntibioticMech joins are empty, without an assay sentinel. Those bounded negatives do not establish absent biological activity or a complete literature survey. The producer assertion is preserved at its stated grade.

### Classification

consistency: unknown. Targets: naturalproductmech:mibig-ac342ce038.

The full graph contains three identical nitroso-substituted phenolate ester ligands, each with two benzene rings and a terminal vinyl group, plus disconnected Na+ and Fe2+. In the SMILES table the ester linkages are C9(=O10)–O8–C5, C29(=O30)–O28–C25 and C49(=O50)–O48–C45; there is no oxygenated C5O sugar cycle. The model’s Bagremycins, Shikimic acids and derivatives, Simple phenolic acids and Phenolic acids (C6-C1) labels describe limited organic-scaffold features, not an experimentally established metal-complex class or coordination model. is_glycoside=false is consistent with the represented ligand topology; MIBiG OTHER remains a separate source class.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-ac342ce038.

The complete owner/history, exact retained source payloads, actual intake and both full saved molecular profiles were reviewed. The apparent literal-formula mismatch is explained by the explicit protonation layer and does not establish a curation defect. Coordination structure and natural identity remain unverified, alongside the source-only producer/locus evidence. Native commands passed; external verification, full QC and OAK were unavailable. This is a qualified partial review with no source or native-status change.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2205-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner and history personally read; generated identity, source claims and native SEEDED status retained. |
| bgc-2205-capture | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete original captured owner, including all fields and both historical seed events. |
| bgc-2205-intake | /private/tmp/npm-review-work/shared-next-batch221/intakes/2205-inspect-001.json; /source; /targets | supports | Original canonical inspect preserves the exact target and 37 source inputs; it is a provenance snapshot, not a scientific verdict. |
| bgc-2205-source-plan | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4 | supports | Complete selected owner/source context and exact direct-companion/input map; historical future-result nulls remain unchanged. |
| bgc-2205-source-notes | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-scope-notes-001.json; /reading; /cautions; /curation | supports | Complete reading attribution, source cautions and bounded implemented-curation-table scan; delegated reading is identified explicitly. |
| bgc-2205-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch221/root-target-input-plan-acceptance-001.json; /status; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths; /verification | supports | ROOT acceptance of the saved source plan, exact membership and current 396-placement/57-path input maps. |
| bgc-2205-grounding-owner | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/chemical_structure; /records/4/owner_document/grounding_status; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_notes | supports | Written identity, full stored structure, source concept, grounding notes and xrefs when present. |
| bgc-2205-origin-owner | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters | supports | Written producer and locus claims, exact citations and source versions/grades. |
| bgc-2205-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/4/owner_document | supports | Written occurrence fields only; absent occurrence fields are assessed against the complete owner. |
| bgc-2205-classification-owner | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway; /records/4/owner_document/bgc_class | supports | Written model classification, filing path and separate source BGC class. |
| bgc-2205-assay-owner | /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json; /records/4/owner_document | supports | The complete captured owner contains no written bioactivities, activity summary, related record or molecular target field. |
| bgc-2205-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved query frame has 1 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned mibig_compounds table; no new query or external lookup. |
| bgc-2205-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1909 | supports | Complete retained fields, including blanks, with exact physical-frame hashes: [{"physical_line":1909,"row_sha256":"bf85cd9265216a72b083cd6488d12706b4d607e2fbc0c952b6698888a762ec3b","row":{"mibig_accession":"BGC0001592","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"ferroverdin","compound_index":"1","smiles":"C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.[Na+].[Fe+2]","standard_inchi":"InChI=1S/3C15H11NO4.Fe.Na/c3*1-2-10-3-6-12(7-4-10)20-15(18)11-5-8-14(17)13(9-11)16-19;;/h3*2-9,17H,1H2;;/q;;;+2;+1/p-3","standard_inchi_key":"OVMCOCUPINBXRQ-UHFFFAOYSA-K","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1535768","taxon_label":"Streptomyces lunaelactis","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"MG708299.1","locus_from":"","locus_to":"","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:31409675","reference_basis":"ENTRY"}}] |
| bgc-2205-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/chebi_structures | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned chebi_structures table; no new query or external lookup. |
| bgc-2205-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned lotus_occurrences table; no new query or external lookup. |
| bgc-2205-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned cyanometdb_occurrences table; no new query or external lookup. |
| bgc-2205-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/npclassifier | supports | Complete saved query frame has 1 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned npclassifier table; no new query or external lookup. |
| bgc-2205-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1803 | supports | Complete retained fields, including blanks, with exact physical-frame hashes: [{"physical_line":1803,"row_sha256":"e2b97c097dfea88675d4e1b2fc44b20afeea861c4d98d4806f54ef1ad2dc72b8","row":{"standard_inchi_key":"OVMCOCUPINBXRQ-UHFFFAOYSA-K","smiles":"C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.[Na+].[Fe+2]","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Bagremycins&#124;Shikimic acids and derivatives&#124;Simple phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}] |
| bgc-2205-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned pubchem_bioassay table; no new query or external lookup. |
| bgc-2205-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned bindingdb_targets table; no new query or external lookup. |
| bgc-2205-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned antibioticmech_inchikeys table; no new query or external lookup. |
| bgc-2205-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/joins/chebi_origins | supports | Complete saved query frame has 0 matched rows. Exact saved predicate exact chebi_id from exact full-key structure rows with query [] over the pinned chebi_origins table; no new query or external lookup. |
| bgc-2205-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/31 | supports | Personally read complete saved stanzas preserve labels and synonyms only: [{"id":"NCBITaxon:1535768","physical_line":132429,"complete_stanza":"[Term]\nid: NCBITaxon:1535768\nname: Streptomyces lunaelactis\n\n"}] |
| bgc-2205-source-routes | /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json; /records/4/source_scope_inventory/source_taxa; /records/4/source_scope_inventory/forward_taxon_merge_matches; /records/4/source_scope_inventory/nonorganism_matches | supports | Complete selected-source taxon and route frames; all retained forward-merge/nonorganism lists are empty in this selected scope. |
| bgc-2205-chemistry | /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/smiles; /records/4/inchi; /records/4/comparisons; /records/4/atom_correspondence; /records/4/literal_InChI_layers; /records/4/formula_comparison_scope | supports | Original saved paired profiles and full tables: {"comparisons":{"formula_equal":true,"formal_charge_equal":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"smiles_formula_equals_literal_InChI_main_layer":false},"smiles_stereo":{},"inchi_stereo":{}} |
| bgc-2205-topology | /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings; /records/4/smiles/computed/motifs; /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/fragment_atom_indices; /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/motifs; /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/fragment_atom_indices; /records/4/atom_correspondence; /records/4/declared_structure | supports | Both complete atom/bond/ring/motif/stereo/fragment tables personally read. Motif candidates have bounded applicability; explicit full-graph identity remains unestablished. |
| bgc-2205-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch221/root-chemistry-acceptance-001.json; /status; /data; /execution; /original_terminal; /personal_scope; /false_comparisons | supports | ROOT accepted the original local computation and current input pins, with no scientific verdict; full table interpretation remains the author’s responsibility. |
| bgc-2205-native-acceptance | /private/tmp/npm-review-work/shared-next-batch221/root-native-gates-acceptance-001.json; /accepted; /results; /unavailable_required_gates; /scientific_correctness_established | supports | Five original local commands passed; full QC/OAK remain unavailable, and scientific correctness is not established by gate success. |
| bgc-2205-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Claim-level evidence, scope preservation, major unsupported-claim severity and immutable partial review requirements. |
| bgc-2205-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Native questions and ownership; Native checks and queue | supports | Producer/occurrence/locus/model distinctions, maintained fix ownership and limitations of native gates; reserved decisions.tsv is not an implemented correction route. |
| bgc-2205-stereo-extraction | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 144–173 | supports | The retained stereo_complete flag is derived from FindMolChiralCenters on the source SMILES; it does not independently verify natural stereochemistry or every double-bond geometry. |
| bgc-2205-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–402 | supports | Standard InChIKey limits and source stereochemistry requirements; matching keys do not prove all explicit graph or natural-form identity. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-221/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-221/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-221/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-221/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-221/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is local and retained. No outbound request was made; primary papers, accessions, external identifiers and live taxonomy were not freshly verified.
- Full QC and OAK were unavailable. Five passed native commands and agreement between stored molecular forms do not establish scientific correctness or complete source verification.
- Molecular conclusions use the original saved two-form diagnostic. No additional molecule parse was performed during fragment authoring; normalized keys and one atom correspondence do not independently establish natural identity or complete stereochemistry.
- Source grades, genus/species/strain scopes, computational classes and direct-companion context are kept distinct. No record, native curation status or history was changed by this review.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Source inventory/composer and first-five scientific authorship overlap is disclosed; the opposite-half cross-peer is independent of these authored judgments.
- No selected mechanism roots or components are present; no maintained reader is required for this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T113308Z-ferroverdin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: ferroverdin'
started_at: '2026-11-03T11:08:47.845489Z'
finished_at: '2026-11-03T11:33:08.328860Z'
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
summary: Qualified local review of exact retained identity, source grades, stored
  molecular forms and claim scope; external verification and required full gates remain
  incomplete.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml
    sha256: a4b1f5be4f784f4f3f4d67cc9491480893f949dea5ceea969735c9cb3449a2ef
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
  selection: Campaign path order 2205; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-ac342ce038
targets:
- target_id: naturalproductmech:mibig-ac342ce038
  path: data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml
  label: ferroverdin
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
  - naturalproductmech:mibig-ac342ce038
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/echoside-b.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-c.yaml data/natural_products/shikimates_and_phenylpropanoids/echoside-d.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-e.yaml data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/hydroxytropodithietic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/legioliulin.yaml data/natural_products/shikimates_and_phenylpropanoids/mellein.yaml
    data/natural_products/shikimates_and_phenylpropanoids/microperfuranone.yaml data/natural_products/shikimates_and_phenylpropanoids/morpholine-containing-hemiacetal-piperazine-compound.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-221/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-ac342ce038
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-221/validate-all-001.tsv
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
  - naturalproductmech:mibig-ac342ce038
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
  - naturalproductmech:mibig-ac342ce038
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
  - naturalproductmech:mibig-ac342ce038
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-221/review-queue-001.tsv
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
  - naturalproductmech:mibig-ac342ce038
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2205-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/ferroverdin.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete current owner and history personally read; generated identity,
    source claims and native SEEDED status retained.
  snapshot_sha256: a4b1f5be4f784f4f3f4d67cc9491480893f949dea5ceea969735c9cb3449a2ef
- evidence_id: bgc-2205-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete original captured owner, including all fields and both historical
    seed events.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: bgc-2205-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/intakes/2205-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Original canonical inspect preserves the exact target and 37 source inputs;
    it is a provenance snapshot, not a scientific verdict.
  snapshot_sha256: 0e63d5784a402a03066de5937f88146b6c289ce39fe1f6e53707949f5b852a5e
- evidence_id: bgc-2205-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete selected owner/source context and exact direct-companion/input
    map; historical future-result nulls remain unchanged.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: bgc-2205-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-scope-notes-001.json
  locator: /reading; /cautions; /curation
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete reading attribution, source cautions and bounded implemented-curation-table
    scan; delegated reading is identified explicitly.
  snapshot_sha256: 1590fe4aff9489e2d4bfba3444f56a607f01c0029f46288d01cecfbbaf9eaf72
- evidence_id: bgc-2205-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-target-input-plan-acceptance-001.json
  locator: /status; /plan; /inventory; /source_notes; /source_placements; /unique_source_paths;
    /verification
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: ROOT acceptance of the saved source plan, exact membership and current
    396-placement/57-path input maps.
  snapshot_sha256: 9156574ffb4dba0fb5d018bf09b5a93625abd4d184b8b5305f5ad79eb6090180
- evidence_id: bgc-2205-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/chemical_structure;
    /records/4/owner_document/grounding_status; /records/4/owner_document/source_concepts;
    /records/4/owner_document/grounding_notes
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Written identity, full stored structure, source concept, grounding notes
    and xrefs when present.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: bgc-2205-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Written producer and locus claims, exact citations and source versions/grades.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: bgc-2205-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Written occurrence fields only; absent occurrence fields are assessed against
    the complete owner.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: bgc-2205-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway;
    /records/4/owner_document/bgc_class
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Written model classification, filing path and separate source BGC class.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: bgc-2205-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: The complete captured owner contains no written bioactivities, activity
    summary, related record or molecular target field.
  snapshot_sha256: 2210415fa28b6922444699bb73205eb3fe195a9daa94f96d193aae706d0b1b55
- evidence_id: bgc-2205-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 1 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned mibig_compounds table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned mibig_compounds table; no
    new query or external lookup.
- evidence_id: bgc-2205-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1909
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: 'Complete retained fields, including blanks, with exact physical-frame
    hashes: [{"physical_line":1909,"row_sha256":"bf85cd9265216a72b083cd6488d12706b4d607e2fbc0c952b6698888a762ec3b","row":{"mibig_accession":"BGC0001592","entry_version":"5","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"ferroverdin","compound_index":"1","smiles":"C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.[Na+].[Fe+2]","standard_inchi":"InChI=1S/3C15H11NO4.Fe.Na/c3*1-2-10-3-6-12(7-4-10)20-15(18)11-5-8-14(17)13(9-11)16-19;;/h3*2-9,17H,1H2;;/q;;;+2;+1/p-3","standard_inchi_key":"OVMCOCUPINBXRQ-UHFFFAOYSA-K","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1535768","taxon_label":"Streptomyces
    lunaelactis","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"MG708299.1","locus_from":"","locus_to":"","locus_evidence_methods":"","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_UNSTATED","primary_reference":"PMID:31409675","reference_basis":"ENTRY"}}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2205-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned chebi_structures table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned chebi_structures table; no
    new query or external lookup.
- evidence_id: bgc-2205-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned lotus_occurrences table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned lotus_occurrences table; no
    new query or external lookup.
- evidence_id: bgc-2205-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned cyanometdb_occurrences table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned cyanometdb_occurrences table;
    no new query or external lookup.
- evidence_id: bgc-2205-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 1 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned npclassifier table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned npclassifier table; no new
    query or external lookup.
- evidence_id: bgc-2205-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1803
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: 'Complete retained fields, including blanks, with exact physical-frame
    hashes: [{"physical_line":1803,"row_sha256":"e2b97c097dfea88675d4e1b2fc44b20afeea861c4d98d4806f54ef1ad2dc72b8","row":{"standard_inchi_key":"OVMCOCUPINBXRQ-UHFFFAOYSA-K","smiles":"C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.C=CC1=CC=C(C=C1)OC(=O)C2=CC(=C(C=C2)[O-])N=O.[Na+].[Fe+2]","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Bagremycins|Shikimic
    acids and derivatives|Simple phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2205-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned pubchem_bioassay table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned pubchem_bioassay table; no
    new query or external lookup.
- evidence_id: bgc-2205-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned bindingdb_targets table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned bindingdb_targets table; no
    new query or external lookup.
- evidence_id: bgc-2205-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    complete standard_inchi_key equality with query "OVMCOCUPINBXRQ-UHFFFAOYSA-K"
    over the pinned antibioticmech_inchikeys table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact complete standard_inchi_key equality with
    query "OVMCOCUPINBXRQ-UHFFFAOYSA-K" over the pinned antibioticmech_inchikeys table;
    no new query or external lookup.
- evidence_id: bgc-2205-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete saved query frame has 0 matched rows. Exact saved predicate exact
    chebi_id from exact full-key structure rows with query [] over the pinned chebi_origins
    table; no new query or external lookup.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
  search_scope: Exact saved predicate exact chebi_id from exact full-key structure
    rows with query [] over the pinned chebi_origins table; no new query or external
    lookup.
- evidence_id: bgc-2205-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/31
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: 'Personally read complete saved stanzas preserve labels and synonyms only:
    [{"id":"NCBITaxon:1535768","physical_line":132429,"complete_stanza":"[Term]\nid:
    NCBITaxon:1535768\nname: Streptomyces lunaelactis\n\n"}]'
  snapshot_sha256: b95aa285c01c324a1b2df722b83db4832436cfe04b4f3dec4c5efaf2aee959f5
- evidence_id: bgc-2205-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch221-tentative/bgc-prep/bgc-conditional221-target-input-plan-001.json
  locator: /records/4/source_scope_inventory/source_taxa; /records/4/source_scope_inventory/forward_taxon_merge_matches;
    /records/4/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Complete selected-source taxon and route frames; all retained forward-merge/nonorganism
    lists are empty in this selected scope.
  snapshot_sha256: 820a0055215cac39c3b8163478767b2dec57c131d114826aefc03b603bd4b00e
- evidence_id: bgc-2205-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/smiles; /records/4/inchi; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/literal_InChI_layers; /records/4/formula_comparison_scope
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: 'Original saved paired profiles and full tables: {"comparisons":{"formula_equal":true,"formal_charge_equal":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"smiles_formula_equals_literal_InChI_main_layer":false},"smiles_stereo":{},"inchi_stereo":{}}'
  snapshot_sha256: 3442ee764bfa4a6dc5c45524b05d448402c881cdae0b10bca2a6200d162d984f
- evidence_id: bgc-2205-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings;
    /records/4/smiles/computed/motifs; /records/4/smiles/computed/potential_stereo;
    /records/4/smiles/computed/fragment_atom_indices; /records/4/inchi/computed/atoms;
    /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/motifs;
    /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/fragment_atom_indices;
    /records/4/atom_correspondence; /records/4/declared_structure
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Both complete atom/bond/ring/motif/stereo/fragment tables personally read.
    Motif candidates have bounded applicability; explicit full-graph identity remains
    unestablished.
  snapshot_sha256: 3442ee764bfa4a6dc5c45524b05d448402c881cdae0b10bca2a6200d162d984f
- evidence_id: bgc-2205-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-chemistry-acceptance-001.json
  locator: /status; /data; /execution; /original_terminal; /personal_scope; /false_comparisons
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: ROOT accepted the original local computation and current input pins, with
    no scientific verdict; full table interpretation remains the author’s responsibility.
  snapshot_sha256: b8f9ad5a7e5ab5f998d1d2b594f633c6f8f75b20171c4385a57c8585cc135741
- evidence_id: bgc-2205-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch221/root-native-gates-acceptance-001.json
  locator: /accepted; /results; /unavailable_required_gates; /scientific_correctness_established
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Five original local commands passed; full QC/OAK remain unavailable, and
    scientific correctness is not established by gate success.
  snapshot_sha256: dd0cd192791e7954204141637854406302975cd1e4a2d56012ccbfc2dd05206d
- evidence_id: bgc-2205-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Claim-level evidence, scope preservation, major unsupported-claim severity
    and immutable partial review requirements.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2205-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Native questions and ownership; Native checks and queue
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Producer/occurrence/locus/model distinctions, maintained fix ownership
    and limitations of native gates; reserved decisions.tsv is not an implemented
    correction route.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2205-stereo-extraction
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 144–173
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: The retained stereo_complete flag is derived from FindMolChiralCenters
    on the source SMILES; it does not independently verify natural stereochemistry
    or every double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2205-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–402
  accessed_at: '2026-11-03T11:27:03.558066Z'
  support: supports
  summary: Standard InChIKey limits and source stereochemistry requirements; matching
    keys do not prove all explicit graph or natural-form identity.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:10:13.322718Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e7bac32597510403baf82edb26400e7ff5ec8175e48b494bb1e3d649da975c3b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:10:39.416135Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: d102de9a8e126b63c7ebecc65f3b0b96b8ce2117ac0ae0835ba385125e89b02b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:10:59.558620Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:11:34.402203Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-221/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-221/native-current221-five-gates-execution-001.json
  accessed_at: '2026-11-03T11:11:46.456820Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: afe3bd09534d479f44cbec647a35fd4d3f395466bd25a250ca36dad1434726c4
assessments:
- assessment_id: bgc-2205-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The complete key OVMCOCUPINBXRQ-UHFFFAOYSA-K joins the retained BGC0001592
    v5 compound and the MINTED Ferroverdin owner. Both declared forms explicitly represent
    three organic anions, sodium and Fe(II); this salt is not silently replaced by
    a neutral ligand or an assumed connected coordination complex. The exact retained
    ChEBI structure join is empty. The stored name and normalized key remain source
    identity assertions, not fresh isolate identification.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-owner
  - bgc-2205-capture
  - bgc-2205-intake
  - bgc-2205-grounding-owner
  - bgc-2205-source-plan
  - bgc-2205-plan-acceptance
  - bgc-2205-query-chebi_structures
  - bgc-2205-source-mibig_compounds
  - bgc-2205-chemistry
  dimensions:
  - name: standard_inchi_key
    value: OVMCOCUPINBXRQ-UHFFFAOYSA-K
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2205-owner
    - bgc-2205-capture
    - bgc-2205-intake
    - bgc-2205-grounding-owner
    - bgc-2205-source-plan
    - bgc-2205-plan-acceptance
    - bgc-2205-query-chebi_structures
    - bgc-2205-source-mibig_compounds
    - bgc-2205-chemistry
  - name: grounding_scope
    value: MINTED BGC0001592 v5 disconnected three-ligand sodium/Fe(II) salt; exact
      retained ChEBI join empty.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2205-owner
    - bgc-2205-capture
    - bgc-2205-intake
    - bgc-2205-grounding-owner
    - bgc-2205-source-plan
    - bgc-2205-plan-acceptance
    - bgc-2205-query-chebi_structures
    - bgc-2205-source-mibig_compounds
    - bgc-2205-chemistry
- assessment_id: bgc-2205-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms yield C45H30FeN3NaO12, formal charge zero, 62 atoms, 63
    bonds and five disconnected fragments. Three phenolate oxygens each carry −1,
    sodium +1 and iron +2; neither metal has any represented bond. The InChI main
    layer 3C15H11NO4.Fe.Na together with /q;;;+2;+1/p-3 explains the sole false literal-main-formula
    comparison. The two computed formulas and all other comparisons agree. No potential
    stereoelement is reported for this disconnected graph, which does not establish
    metal coordination geometry or coordination stereochemical completeness; full_graph_identity_established
    remains false.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-chemistry
  - bgc-2205-topology
  - bgc-2205-diagnostic-acceptance
  - bgc-2205-stereo-extraction
  - bgc-2205-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: No potential stereoelements in the saved disconnected graph; source true
      flag does not establish metal coordination stereochemistry.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2205-chemistry
    - bgc-2205-topology
    - bgc-2205-diagnostic-acceptance
    - bgc-2205-stereo-extraction
    - bgc-2205-structure-schema
  - name: representation_correspondence
    value: Both formulas C45H30FeN3NaO12; 62 atoms/63 bonds/five fragments; nine comparisons
      true, literal main-layer comparison false because of /p-3.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2205-chemistry
    - bgc-2205-topology
    - bgc-2205-diagnostic-acceptance
    - bgc-2205-stereo-extraction
    - bgc-2205-structure-schema
- assessment_id: bgc-2205-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0001592 v5 is active/questionable/unknown and grades Streptomyces
    lunaelactis (NCBITaxon:1535768) SOURCE_ASSERTION and the locus CLUSTER_UNSTATED.
    Genome MG708299.1 and entry-level PMID:31409675 are retained, with no stated locus-evidence
    method. The cached species label agrees locally. No written occurrence or exact
    retained LOTUS/ChEBI-origin row supplies independent production evidence.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-origin-owner
  - bgc-2205-occurrence-owner
  - bgc-2205-source-mibig_compounds
  - bgc-2205-query-lotus_occurrences
  - bgc-2205-query-chebi_origins
  - bgc-2205-cached-taxonomy
  - bgc-2205-source-routes
  - bgc-2205-review-profile
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:1535768 Streptomyces lunaelactis species assertion, with exact
      cached label and no selected occurrence row.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2205-origin-owner
    - bgc-2205-occurrence-owner
    - bgc-2205-source-mibig_compounds
    - bgc-2205-query-lotus_occurrences
    - bgc-2205-query-chebi_origins
    - bgc-2205-cached-taxonomy
    - bgc-2205-source-routes
    - bgc-2205-review-profile
  - name: producer_evidence
    value: SOURCE_ASSERTION, MIBiG v5 species claim.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2205-origin-owner
    - bgc-2205-occurrence-owner
    - bgc-2205-source-mibig_compounds
    - bgc-2205-query-lotus_occurrences
    - bgc-2205-query-chebi_origins
    - bgc-2205-cached-taxonomy
    - bgc-2205-source-routes
    - bgc-2205-review-profile
  - name: locus_evidence
    value: BGC0001592 CLUSTER_UNSTATED; active/questionable/unknown; MG708299.1; no
      stated locus method.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2205-origin-owner
    - bgc-2205-occurrence-owner
    - bgc-2205-source-mibig_compounds
    - bgc-2205-query-lotus_occurrences
    - bgc-2205-query-chebi_origins
    - bgc-2205-cached-taxonomy
    - bgc-2205-source-routes
    - bgc-2205-review-profile
- assessment_id: bgc-2205-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: PMID:31409675 is explicitly the MIBiG entry-level reference carried on
    both producer and locus. Repeating that reference in two fields does not make
    two experiments. The record has no separate occurrence or assay citation in the
    inspected source scope. The original article, genome and taxonomy accession were
    not freshly verified.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-origin-owner
  - bgc-2205-occurrence-owner
  - bgc-2205-source-mibig_compounds
  - bgc-2205-assay-owner
  dimensions:
  - name: citation_scope
    value: Entry-level PMID:31409675 copied to producer/locus; one citation role,
      no newly inspected experiment.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2205-origin-owner
    - bgc-2205-occurrence-owner
    - bgc-2205-source-mibig_compounds
    - bgc-2205-assay-owner
- assessment_id: bgc-2205-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The complete owner writes no occurrences, bioactivities, activity summary,
    molecular targets or mechanism roots. Its exact retained occurrence, PubChem,
    BindingDB and AntibioticMech joins are empty, without an assay sentinel. Those
    bounded negatives do not establish absent biological activity or a complete literature
    survey. The producer assertion is preserved at its stated grade.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-assay-owner
  - bgc-2205-occurrence-owner
  - bgc-2205-query-lotus_occurrences
  - bgc-2205-query-chebi_origins
  - bgc-2205-query-pubchem_bioassay
  - bgc-2205-query-bindingdb_targets
  - bgc-2205-query-antibioticmech_inchikeys
  - bgc-2205-source-plan
  dimensions:
  - name: occurrence_scope
    value: No written occurrences or exact retained occurrence rows; bounded source
      scope only.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2205-assay-owner
    - bgc-2205-occurrence-owner
    - bgc-2205-query-lotus_occurrences
    - bgc-2205-query-chebi_origins
    - bgc-2205-query-pubchem_bioassay
    - bgc-2205-query-bindingdb_targets
    - bgc-2205-query-antibioticmech_inchikeys
    - bgc-2205-source-plan
  - name: assay_target_scope
    value: No written assay/target/summary/mechanism; empty retained assay/target/sibling
      joins, not biological inactivity.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2205-assay-owner
    - bgc-2205-occurrence-owner
    - bgc-2205-query-lotus_occurrences
    - bgc-2205-query-chebi_origins
    - bgc-2205-query-pubchem_bioassay
    - bgc-2205-query-bindingdb_targets
    - bgc-2205-query-antibioticmech_inchikeys
    - bgc-2205-source-plan
- assessment_id: bgc-2205-classification
  area: consistency
  topic: Classification
  outcome: unknown
  summary: The full graph contains three identical nitroso-substituted phenolate ester
    ligands, each with two benzene rings and a terminal vinyl group, plus disconnected
    Na+ and Fe2+. In the SMILES table the ester linkages are C9(=O10)–O8–C5, C29(=O30)–O28–C25
    and C49(=O50)–O48–C45; there is no oxygenated C5O sugar cycle. The model’s Bagremycins,
    Shikimic acids and derivatives, Simple phenolic acids and Phenolic acids (C6-C1)
    labels describe limited organic-scaffold features, not an experimentally established
    metal-complex class or coordination model. is_glycoside=false is consistent with
    the represented ligand topology; MIBiG OTHER remains a separate source class.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-classification-owner
  - bgc-2205-source-npclassifier
  - bgc-2205-source-mibig_compounds
  - bgc-2205-chemistry
  - bgc-2205-topology
  - bgc-2205-review-profile
  dimensions:
  - name: classification_applicability
    value: Model phenolic-acid/Bagremycin labels have limited ligand applicability;
      three ester ligands, no sugar cycle, no represented metal coordination.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2205-classification-owner
    - bgc-2205-source-npclassifier
    - bgc-2205-source-mibig_compounds
    - bgc-2205-chemistry
    - bgc-2205-topology
    - bgc-2205-review-profile
- assessment_id: bgc-2205-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: The complete owner/history, exact retained source payloads, actual intake
    and both full saved molecular profiles were reviewed. The apparent literal-formula
    mismatch is explained by the explicit protonation layer and does not establish
    a curation defect. Coordination structure and natural identity remain unverified,
    alongside the source-only producer/locus evidence. Native commands passed; external
    verification, full QC and OAK were unavailable. This is a qualified partial review
    with no source or native-status change.
  target_ids:
  - naturalproductmech:mibig-ac342ce038
  evidence_ids:
  - bgc-2205-owner
  - bgc-2205-intake
  - bgc-2205-source-notes
  - bgc-2205-native-acceptance
  - bgc-2205-diagnostic-acceptance
  - bgc-2205-review-skill
  - bgc-2205-review-profile
  - bgc-2205-source-plan
  - bgc-2205-plan-acceptance
  dimensions:
  - name: review_completion
    value: Qualified partial; protonation explains literal-formula comparison; coordination
      and external/full QC/OAK questions remain unresolved.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2205-owner
    - bgc-2205-intake
    - bgc-2205-source-notes
    - bgc-2205-native-acceptance
    - bgc-2205-diagnostic-acceptance
    - bgc-2205-review-skill
    - bgc-2205-review-profile
    - bgc-2205-source-plan
    - bgc-2205-plan-acceptance
findings: []
actions: []
limitations:
- All evidence is local and retained. No outbound request was made; primary papers,
  accessions, external identifiers and live taxonomy were not freshly verified.
- Full QC and OAK were unavailable. Five passed native commands and agreement between
  stored molecular forms do not establish scientific correctness or complete source
  verification.
- Molecular conclusions use the original saved two-form diagnostic. No additional
  molecule parse was performed during fragment authoring; normalized keys and one
  atom correspondence do not independently establish natural identity or complete
  stereochemistry.
- Source grades, genus/species/strain scopes, computational classes and direct-companion
  context are kept distinct. No record, native curation status or history was changed
  by this review.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Source inventory/composer and first-five scientific authorship overlap is disclosed;
  the opposite-half cross-peer is independent of these authored judgments.
- No selected mechanism roots or components are present; no maintained reader is required
  for this owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-221
```
