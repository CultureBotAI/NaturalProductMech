# Local evidence review: betaestacin I

- Review: 20261103T185021Z-betaestacin-i
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T18:10:20.613936Z
- Finished UTC: 2026-11-03T18:50:21.990647Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Betaestacin I is locally consistent as a C25 hydrocarbon with five specified tetrahedral centres, two specified alkene geometries and one explicitly unresolved double bond. Its true extractor flag covers tetrahedral centres and is not evidence that all stereochemistry is known. Scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2275; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b113a8e29e | data/natural_products/terpenoids/betaestacin-i.yaml | generated | betaestacin I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-b113a8e29e | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b113a8e29e | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b113a8e29e | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b113a8e29e | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b113a8e29e | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b113a8e29e | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b113a8e29e | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b113a8e29e | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-b113a8e29e.

The minted identifier retains complete key RGXPVTCXXHGAHK-QFIDHXJRSA-N from MIBiG BGC0001528 version 4 compound index 1; the exact retained ChEBI structure join is empty. Both stored forms agree on C25H40 while explicitly retaining unresolved double-bond geometry. Direct companion Betaestacin II has a different complete key, so shared locus and model family do not supply missing geometry or identity.

### Representation

representation: supported. Targets: naturalproductmech:mibig-b113a8e29e.

Both forms are neutral C25H40 with 25 carbon atoms, 27 bonds and one fragment. SMILES centres C4 S, C7 S, C12 R, C17 S and C19 S are specified; two alkenes are Z/E and C1=C2 remains unspecified. The corresponding InChI bond C12=C17 is Unknown/STEREOANY with literal /b18-13?. The true stereo_complete flag follows the retained extractor's tetrahedral-centre test and does not resolve that bond. All ten comparisons and the stored correspondence agree without proving complete natural stereochemistry or independent full-graph identity.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-b113a8e29e.

MIBiG BGC0001528 version 4 is active, questionable and of unknown completeness. The source label Phoma betae at taxon 1979465 remains a SOURCE_ASSERTION, while the locus is CLUSTER_UNSTATED with genbank:LC274619.1 and no method or interval stated. The cached current name Neocamarosporium betae explicitly includes Phoma betae as an exact synonym; this retained name continuity does not upgrade production or locus evidence.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-b113a8e29e.

DOI:10.1021/acs.orglett.7b03418 is explicitly taken from the MIBiG compound evidence level and reused for producer and locus assertions. Its presence does not establish that the complete pathway, native genome context or unresolved alkene configuration was experimentally verified in this review. The distinct Betaestacin II companion remains separately owned despite shared BGC metadata.

### Bioactivity

evidence: supported. Targets: naturalproductmech:mibig-b113a8e29e.

The owner writes no occurrences, bioactivities, molecular targets or mechanism roots. Its exact retained occurrence, PubChem, BindingDB and AntibioticMech routes are empty. Betaestacin II's blank-AID no-assay-data sentinel belongs to that companion and transfers no activity or inactivity to Betaestacin I. No global biological-absence claim follows.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-b113a8e29e.

The source TERPENE/Sesterterpene class is separate from NPClassifier Terpenoids / Sesterterpenoids / Betaestacin-type sesterterpenoids and is_glycoside:false. The complete C25 carbocyclic hydrocarbon topology is compatible with the broad filing and cannot itself contain an O-glycosidic linkage or sugar residue. This structural compatibility does not validate the biosynthetic route or supply the unresolved double-bond geometry.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-b113a8e29e.

All required scientific dimensions were assessed against the current owner, actual intake, retained source payloads and complete paired molecular tables. Five local gates passed, while full QC and complete OAK authority coverage remain unavailable. No selected mechanism reader is applicable to this owner. External facts remain unverified under the no-request instruction, so completion is partial and native curation status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2275-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/betaestacin-i.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner and all 2 ordered history entries personally read; native curation_status remains SEEDED. |
| bgc-2275-capture | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/4/owner_pin; /records/4/owner_document | supports | Exact complete captured owner, including all written fields and history. |
| bgc-2275-intake | /private/tmp/npm-review-work/shared-next-batch228/intakes/2275-inspect-001.json; /source; /targets | supports | Actual canonical one-record intake for naturalproductmech:mibig-b113a8e29e with 38 current source inputs and explicit field ownership. |
| bgc-2275-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-intake-ready-001.json; /accepted; /intake_summary; /verification | supports | ROOT accepts the ten original canonical intakes and their exact current ownership/source maps. |
| bgc-2275-grounding-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/label; /records/4/owner_document/chemical_structure; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status | supports | Complete written identity and definition/provenance fields: {"chemical_structure": {"smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1", "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1", "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001528"}, "grounding_status": "MINTED", "identifier": "naturalproductmech:mibig-b113a8e29e", "label": "betaestacin I", "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-b113a8e29e", "source": "MIBIG", "source_id": "BGC0001528", "source_label": "betaestacin I", "source_version": "4"}]} |
| bgc-2275-origin-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/producer_taxon_groups | supports | Complete written producer and locus claims with their separate evidence grades: {"biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001528", "bgc_class": ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001528 entry version 4; citation taken from the compound evidence level", "reference": "DOI:10.1021/acs.orglett.7b03418"}], "genome_accession": "genbank:LC274619.1", "link_evidence_basis": "CLUSTER_UNSTATED", "organism_label": "Phoma betae", "organism_taxon_id": "NCBITaxon:1979465"}], "producer_organisms": [{"biosynthetic_gene_cluster": "mibig:BGC0001528", "evidence": [{"evidence_type": "DATABASE_ASSERTION", "notes": "MIBiG BGC0001528 entry version 4; citation taken from the compound evidence level", "reference": "DOI:10.1021/acs.orglett.7b03418"}], "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.", "source": "MIBIG", "source_version": "4", "taxon_id": "NCBITaxon:1979465", "taxon_label": "Phoma betae"}], "producer_taxon_groups": ["FUNGAL"]} |
| bgc-2275-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/4/owner_document | supports | The complete owner establishes present or absent occurrences. Written occurrence fields and any omission notes: {} |
| bgc-2275-assay-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete owner establishes assay, target and mechanism-root presence without inferring biological absence: {} |
| bgc-2275-classification-owner | /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json; /records/4/owner_document/np_pathway; /records/4/owner_document/np_classification; /records/4/owner_document/bgc_class | supports | Literal source BGC classification and named/versioned computed classification remain separate: {"bgc_class": ["TERPENE"], "np_classification": {"class_results": ["Betaestacin-type sesterterpenoids"], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": ["Sesterterpenoids"], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"} |
| bgc-2275-chemistry | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/smiles/status; /records/4/inchi/status; /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons; /records/4/atom_correspondence | supports | Both saved forms parsed. Their complete atom/bond/ring/stereo/motif tables and correspondence were personally read. Saved declared structure and comparison facts: {"comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared": true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal": true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer": true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "declared_structure": {"smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1", "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1", "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": true, "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001528"}, "inchi_formula": "C25H40", "smiles_formula": "C25H40"} |
| bgc-2275-topology | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed; /records/4/inchi/computed; /records/4/atom_correspondence | supports | All 25 atoms are carbon. The saved rings have 12, five and five members. SMILES bond 1 C1=C2 lacks specified geometry and corresponds to InChI bond 16 C12=C17 marked STEREOANY, matching literal /b18-13?. SMILES C14=C15 is Z and C18=C23 is E; complete topology has no oxygen, sugar residue or glycosidic linkage. |
| bgc-2275-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-execution-001.json; /command; /cwd; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr; /external_requests | supports | Original process receipt has exit 0 and retains exact stdout/stderr, clocks, command and source; no external request. |
| bgc-2275-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-local-diagnostics-acceptance-001.json; /accepted; /DATA; /execution; /verification; /unspecified_stereo; /limits | supports | ROOT accepts the original 20 stored-form parses and current dependency joins. The two original undefined-stereo warnings remain global and unassigned; full QC/OAK and scientific verification limits remain explicit. |
| bgc-2275-native-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-native-five-gates-acceptance-001.json; /five_exits; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | supports | Five local gates passed. Full QC and complete OAK authority coverage remain unavailable; all_native_gates_passed is false. The selected queue is a local review aid, not proof of the scientific assertions. |
| bgc-2275-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch228-tentative/root-source-inventory-acceptance-001.json; /inventory; /verification; /reading_scope | supports | ROOT accepts the original retained inventory and exact current maps; scientific source-payload reading is separately attributed. |
| bgc-2275-plan | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json; /records/4; /source_placement_count; /unique_source_path_count | supports | Accepted source plan retains this exact owner and its input/context roles within 448 placements and 78 unique paths. |
| bgc-2275-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch228/root-input-plan-acceptance-001.json; /accepted; /plan; /source_notes; /source_placements; /unique_source_paths; /current_record_and_all_source_pins | supports | ROOT accepts the actual composed plan and current input/owner joins, separately from scientific judgments. |
| bgc-2275-source-notes | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json; /reading; /curation; /cautions | supports | Complete personal and delegated source readings, exact bounded curation scan, source grades and limits are recorded. No external source refresh or congener transfer is implied. |
| bgc-2275-direct-contexts | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /records/4/direct_companion_paths; /records/4/direct_companion_predicates | supports | Exact direct-context paths and one-hop predicates: {"direct_companion_paths": ["data/natural_products/terpenoids/betaestacin-ii.yaml"], "direct_companion_predicates": [{"path": "data/natural_products/terpenoids/betaestacin-ii.yaml", "same_complete_InChIKey": false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0001528"]}]} |
| bgc-2275-companion-20 | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/20/input; /contexts/20/complete_raw_text; /contexts/20/complete_raw_history; /contexts/20/source_scope_inventory | supports | Complete separately owned companion naturalproductmech:mibig-bc572fa775 with key OVLRNGJHUUCIHT-LLBDNSMRSA-N; its whole raw/source reading is attributed in the notes and conveys no congener claim transfer. |
| bgc-2275-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/mibig_compounds | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [{"last_physical_line": 1844, "physical_line": 1844, "raw_tsv_record": "BGC0001528\t4\tactive\tquestionable\tunknown\tbetaestacin I\t1\tCC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1\tInChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1\tRGXPVTCXXHGAHK-QFIDHXJRSA-N\ttrue\t\t\tNCBITaxon:1979465\tPhoma betae\tterpene\tSesterterpene\tLC274619.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1021/acs.orglett.7b03418\tCOMPOUND_EVIDENCE\n", "row": {"bgc_classes": "terpene", "bgc_subclasses": "Sesterterpene", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "betaestacin I", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "4", "genome_accession": "LC274619.1", "locus_evidence_methods": "", "locus_from": "", "locus_to": "", "mibig_accession": "BGC0001528", "primary_reference": "DOI:10.1021/acs.orglett.7b03418", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_EVIDENCE", "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1", "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1", "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1979465", "taxon_label": "Phoma betae"}, "row_sha256": "cf641d06dbb5ea24ddee1dacde8a131636aa450fed95f695051e055e5b47d336"}], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1844–1844; row_sha256 cf641d06dbb5ea24ddee1dacde8a131636aa450fed95f695051e055e5b47d336 | supports | Complete physical source rows, all fields personally read and joined to the pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Sesterterpene", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "betaestacin I", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "4", "genome_accession": "LC274619.1", "locus_evidence_methods": "", "locus_from": "", "locus_to": "", "mibig_accession": "BGC0001528", "primary_reference": "DOI:10.1021/acs.orglett.7b03418", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_EVIDENCE", "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1", "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1", "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1979465", "taxon_label": "Phoma betae"}] |
| bgc-2275-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/chebi_structures | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/lotus_occurrences | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/cyanometdb_occurrences | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/npclassifier | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [{"last_physical_line": 2107, "physical_line": 2107, "raw_tsv_record": "RGXPVTCXXHGAHK-QFIDHXJRSA-N\tCC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1\tTerpenoids\tSesterterpenoids\tBetaestacin-type sesterterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results": "Betaestacin-type sesterterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1", "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "superclass_results": "Sesterterpenoids"}, "row_sha256": "131db63860fcd1b3a0e471f49e4861f685beab839b8e82ed1fd03f40268131f7"}], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2107–2107; row_sha256 131db63860fcd1b3a0e471f49e4861f685beab839b8e82ed1fd03f40268131f7 | supports | Complete physical source rows, all fields personally read and joined to the pinned table: [{"class_results": "Betaestacin-type sesterterpenoids", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1", "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "superclass_results": "Sesterterpenoids"}] |
| bgc-2275-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/pubchem_bioassay | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/bindingdb_targets | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"} |
| bgc-2275-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/chebi_origins | supports | Exact retained predicate and query with all matched physical payloads: {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows", "query": []} |
| bgc-2275-source-routes | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/source_taxa; /contexts/19/source_scope_inventory/forward_taxon_merge_matches; /contexts/19/source_scope_inventory/nonorganism_matches; /contexts/19/source_scope_inventory/actual_assay_rows; /contexts/19/source_scope_inventory/blank_AID_sentinels; /contexts/19/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists, distinguishing forward merges/nonorganism matches and blank sentinels from actual assays: {"actual_assay_rows": [], "blank_AID_sentinels": [], "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows": [], "source_taxa": ["NCBITaxon:1979465"]} |
| bgc-2275-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/70; /cached_taxonomy/unmatched_ids | supports | Complete retained cache stanzas for this source-taxon scope, with cache misses retained globally and no fresh taxonomy or ancestry assertion: [{"complete_stanza": "[Term]\nid: NCBITaxon:1979465\nname: Neocamarosporium betae\nsynonym: \"Phoma betae\" EXACT []\nsynonym: \"Pleospora betae (Berl.) Nevod., 1915\" EXACT []\nsynonym: \"Pyrenophora echinella var. betae\" EXACT []\n\n", "id": "NCBITaxon:1979465", "physical_line": 142689}] |
| bgc-2275-curation-scope | /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json; /curation | supports | One bounded eight-table scan used 161 exact literals over 93 data rows, including ignored files by direct access. The only hit is the Avermitilol locus override at physical line 5; applicability is owner-specific. Reserved decisions.tsv was not consumed. PubChem exclusions were supplementary and are outside this batch input map. |
| bgc-2275-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure and ComputedClassification distinguish unspecified stereocentres, normalized keys and named/versioned model predictions; the latter are not source assertions or admission grounds. |
| bgc-2275-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–174 | supports | The maintained extractor computes stereo_complete from FindMolChiralCenters with unassigned centres included; it does not test every double-bond geometry. No extractor was invoked here. |
| bgc-2275-origin-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1067–1196 | supports | Producer and locus evidence grades are separately copied, with explicit merge/qualification handling. ChEBI occurrence assertions are not promoted to production. |
| bgc-2275-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 968–1060 | supports | Full-key source grounding, model prediction projection and source-concept preservation have separate maintained roles. |
| bgc-2275-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile | supports | The current review profile requires claim-level identity, representation, evidence, provenance and completion coverage without promoting unavailable checks. |
| bgc-2275-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole skill | supports | The current one-record review procedure keeps source evidence and required verification limits explicit and does not authorize record edits or external requests here. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-228/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-228/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-228/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-228/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, genome accessions and primary publications were not refreshed under the absolute no-request instruction. Historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form parsing establish only their declared mechanical scope.
- Empty joins refer only to retained exact predicates and snapshots; they do not establish biological absence. Shared loci, citations and congeners do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, native curation status and histories were not edited.
- The retained true stereo_complete flag is tetrahedral-centre scoped. Explicit unknown double-bond geometry remains represented and is not resolved by form agreement.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The complete owner/history, actual intake, exact assigned source payloads and both complete saved molecular tables were personally read. Complementary source and companion reading is explicitly attributed in the pinned notes.
- The original batch diagnostic has two global undefined-stereo warnings, not attributed to individual records. All true comparison flags leave full_graph_identity_established:false unchanged.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T185021Z-betaestacin-i
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: betaestacin I'
started_at: '2026-11-03T18:10:20.613936Z'
finished_at: '2026-11-03T18:50:21.990647Z'
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
summary: Betaestacin I is locally consistent as a C25 hydrocarbon with five specified
  tetrahedral centres, two specified alkene geometries and one explicitly unresolved
  double bond. Its true extractor flag covers tetrahedral centres and is not evidence
  that all stereochemistry is known. Scientific completion is partial.
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
  - path: data/natural_products/terpenoids/betaestacin-i.yaml
    sha256: 5b8c544acf3c96f21f96b2ecf07fea36fac414c6cd0229119f34c913893da90e
    role: target
  - path: data/natural_products/terpenoids/betaestacin-ii.yaml
    sha256: d7a1b74da79d0af66d59144e498665b127d7fb25e6ef2ecad54c2a24a84cc603
    role: context
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
  selection: Campaign path order 2275; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b113a8e29e
targets:
- target_id: naturalproductmech:mibig-b113a8e29e
  path: data/natural_products/terpenoids/betaestacin-i.yaml
  label: betaestacin I
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
  - naturalproductmech:mibig-b113a8e29e
  command: just validate-strict data/natural_products/terpenoids/aspterric-acid.yaml
    data/natural_products/terpenoids/astaxanthin.yaml data/natural_products/terpenoids/astellolide-a.yaml
    data/natural_products/terpenoids/avermitilol.yaml data/natural_products/terpenoids/betaestacin-i.yaml
    data/natural_products/terpenoids/betaestacin-ii.yaml data/natural_products/terpenoids/biscognienyne-b.yaml
    data/natural_products/terpenoids/botrydial.yaml data/natural_products/terpenoids/botrydienal.yaml
    data/natural_products/terpenoids/botryenalol.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-b113a8e29e
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-228/validate-all-001.tsv
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
  - naturalproductmech:mibig-b113a8e29e
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
  - naturalproductmech:mibig-b113a8e29e
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
  - naturalproductmech:mibig-b113a8e29e
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-228/review-queue-001.tsv
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
  - naturalproductmech:mibig-b113a8e29e
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2275-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/betaestacin-i.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Complete current owner and all 2 ordered history entries personally read;
    native curation_status remains SEEDED.
  snapshot_sha256: 5b8c544acf3c96f21f96b2ecf07fea36fac414c6cd0229119f34c913893da90e
- evidence_id: bgc-2275-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/4/owner_pin; /records/4/owner_document
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Exact complete captured owner, including all written fields and history.
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2275-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/intakes/2275-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Actual canonical one-record intake for naturalproductmech:mibig-b113a8e29e
    with 38 current source inputs and explicit field ownership.
  snapshot_sha256: 0cd53a4c3eb9a8ae452ec44dad221f953ab7e6653122c30e883901ed382ac669
- evidence_id: bgc-2275-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-intake-ready-001.json
  locator: /accepted; /intake_summary; /verification
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and their exact current
    ownership/source maps.
  snapshot_sha256: c2c258d6da649f48e76d7d8994bfdef5dd2afa511e1762a008b8f65ef40f8501
- evidence_id: bgc-2275-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/label;
    /records/4/owner_document/chemical_structure; /records/4/owner_document/source_concepts;
    /records/4/owner_document/grounding_status
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete written identity and definition/provenance fields: {"chemical_structure":
    {"smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1",
    "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1",
    "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001528"}, "grounding_status":
    "MINTED", "identifier": "naturalproductmech:mibig-b113a8e29e", "label": "betaestacin
    I", "source_concepts": [{"minted_identifier": "naturalproductmech:mibig-b113a8e29e",
    "source": "MIBIG", "source_id": "BGC0001528", "source_label": "betaestacin I",
    "source_version": "4"}]}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2275-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters;
    /records/4/owner_document/producer_taxon_groups
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete written producer and locus claims with their separate evidence
    grades: {"biosynthetic_gene_clusters": [{"accession": "mibig:BGC0001528", "bgc_class":
    ["TERPENE"], "entry_status": "active", "entry_version": "4", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0001528 entry version 4; citation taken
    from the compound evidence level", "reference": "DOI:10.1021/acs.orglett.7b03418"}],
    "genome_accession": "genbank:LC274619.1", "link_evidence_basis": "CLUSTER_UNSTATED",
    "organism_label": "Phoma betae", "organism_taxon_id": "NCBITaxon:1979465"}], "producer_organisms":
    [{"biosynthetic_gene_cluster": "mibig:BGC0001528", "evidence": [{"evidence_type":
    "DATABASE_ASSERTION", "notes": "MIBiG BGC0001528 entry version 4; citation taken
    from the compound evidence level", "reference": "DOI:10.1021/acs.orglett.7b03418"}],
    "evidence_basis": "SOURCE_ASSERTION", "notes": "Locus evidence: none stated. That
    evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim,
    which is a different question.", "source": "MIBIG", "source_version": "4", "taxon_id":
    "NCBITaxon:1979465", "taxon_label": "Phoma betae"}], "producer_taxon_groups":
    ["FUNGAL"]}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2275-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'The complete owner establishes present or absent occurrences. Written
    occurrence fields and any omission notes: {}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2275-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete owner establishes assay, target and mechanism-root presence without
    inferring biological absence: {}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2275-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_pathway; /records/4/owner_document/np_classification;
    /records/4/owner_document/bgc_class
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Literal source BGC classification and named/versioned computed classification
    remain separate: {"bgc_class": ["TERPENE"], "np_classification": {"class_results":
    ["Betaestacin-type sesterterpenoids"], "is_glycoside": false, "pathway_results":
    ["Terpenoids"], "superclass_results": ["Sesterterpenoids"], "tool": "NPClassifier",
    "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 9280223af2be592af18b62653684eb4e27ec0072d5e2b1f4f4a6e6fb028323b9
- evidence_id: bgc-2275-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/smiles/status; /records/4/inchi/status;
    /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons;
    /records/4/atom_correspondence
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Both saved forms parsed. Their complete atom/bond/ring/stereo/motif tables
    and correspondence were personally read. Saved declared structure and comparison
    facts: {"comparisons": {"atom_count_equal": true, "bond_count_equal": true, "both_keys_equal_declared":
    true, "canonical_isomeric_smiles_equal": true, "canonical_nonisomeric_smiles_equal":
    true, "formal_charge_equal": true, "formula_equal": true, "smiles_formula_equals_literal_InChI_main_layer":
    true, "standard_inchi_equal": true, "standard_inchi_key_equal": true}, "declared_structure":
    {"smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1",
    "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1",
    "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": true,
    "structure_source": "MIBIG", "structure_source_id": "mibig:BGC0001528"}, "inchi_formula":
    "C25H40", "smiles_formula": "C25H40"}'
  snapshot_sha256: d4c6eb70f0eb830267ca6a459d5b3f2f1ed0903dbbd02a6ea6cea1104beb62f9
- evidence_id: bgc-2275-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed; /records/4/inchi/computed; /records/4/atom_correspondence
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: All 25 atoms are carbon. The saved rings have 12, five and five members.
    SMILES bond 1 C1=C2 lacks specified geometry and corresponds to InChI bond 16
    C12=C17 marked STEREOANY, matching literal /b18-13?. SMILES C14=C15 is Z and C18=C23
    is E; complete topology has no oxygen, sugar residue or glycosidic linkage.
  snapshot_sha256: d4c6eb70f0eb830267ca6a459d5b3f2f1ed0903dbbd02a6ea6cea1104beb62f9
- evidence_id: bgc-2275-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/chemistry-local/diagnostic-execution-001.json
  locator: /command; /cwd; /started_at; /finished_at; /exit_code; /source; /stdout;
    /stderr; /external_requests
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Original process receipt has exit 0 and retains exact stdout/stderr, clocks,
    command and source; no external request.
  snapshot_sha256: cec83a5bb171e1fb8a233f2b4d0f0421461c308bf28a3b13540cd0baeb3ab3cf
- evidence_id: bgc-2275-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-local-diagnostics-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /unspecified_stereo; /limits
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the original 20 stored-form parses and current dependency
    joins. The two original undefined-stereo warnings remain global and unassigned;
    full QC/OAK and scientific verification limits remain explicit.
  snapshot_sha256: 538d4571fceb926adea82c64cc91c2cb0d058ceb5018e3d3261297b43223fcf8
- evidence_id: bgc-2275-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-native-five-gates-acceptance-001.json
  locator: /five_exits; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Five local gates passed. Full QC and complete OAK authority coverage remain
    unavailable; all_native_gates_passed is false. The selected queue is a local review
    aid, not proof of the scientific assertions.
  snapshot_sha256: 46a484e5df5e5ff5b717dd9fbef5c00cc5bc1843abdf9cab2629b498187c780a
- evidence_id: bgc-2275-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/root-source-inventory-acceptance-001.json
  locator: /inventory; /verification; /reading_scope
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the original retained inventory and exact current maps; scientific
    source-payload reading is separately attributed.
  snapshot_sha256: 2feaf455de349447001426cc4790a3fa85b20f1d257fef5061b48c27803f0f3d
- evidence_id: bgc-2275-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-target-input-plan-001.json
  locator: /records/4; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Accepted source plan retains this exact owner and its input/context roles
    within 448 placements and 78 unique paths.
  snapshot_sha256: b6fb1594773d9dc6936b2d71779c7547fa87fa6fa770868b027ab7bc36d53051
- evidence_id: bgc-2275-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228/root-input-plan-acceptance-001.json
  locator: /accepted; /plan; /source_notes; /source_placements; /unique_source_paths;
    /current_record_and_all_source_pins
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ROOT accepts the actual composed plan and current input/owner joins, separately
    from scientific judgments.
  snapshot_sha256: 006b60c3550a7c223f1a10b5a127034d9429c714d72ff96363275b808fe1a2d6
- evidence_id: bgc-2275-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json
  locator: /reading; /curation; /cautions
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Complete personal and delegated source readings, exact bounded curation
    scan, source grades and limits are recorded. No external source refresh or congener
    transfer is implied.
  snapshot_sha256: 63a4685a365402d997d4f20d1b80d7dce1b7f62d2d2264c93dae7fa581e52df5
- evidence_id: bgc-2275-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /records/4/direct_companion_paths; /records/4/direct_companion_predicates
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact direct-context paths and one-hop predicates: {"direct_companion_paths":
    ["data/natural_products/terpenoids/betaestacin-ii.yaml"], "direct_companion_predicates":
    [{"path": "data/natural_products/terpenoids/betaestacin-ii.yaml", "same_complete_InChIKey":
    false, "same_root_identifier": false, "shared_owned_BGCs": ["BGC0001528"]}]}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-companion-20
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/20/input; /contexts/20/complete_raw_text; /contexts/20/complete_raw_history;
    /contexts/20/source_scope_inventory
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Complete separately owned companion naturalproductmech:mibig-bc572fa775
    with key OVLRNGJHUUCIHT-LLBDNSMRSA-N; its whole raw/source reading is attributed
    in the notes and conveys no congener claim transfer.
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [{"last_physical_line": 1844, "physical_line": 1844, "raw_tsv_record":
    "BGC0001528\t4\tactive\tquestionable\tunknown\tbetaestacin I\t1\tCC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1\tInChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1\tRGXPVTCXXHGAHK-QFIDHXJRSA-N\ttrue\t\t\tNCBITaxon:1979465\tPhoma
    betae\tterpene\tSesterterpene\tLC274619.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1021/acs.orglett.7b03418\tCOMPOUND_EVIDENCE\n",
    "row": {"bgc_classes": "terpene", "bgc_subclasses": "Sesterterpene", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "betaestacin I", "database_ids": "", "entry_completeness": "unknown", "entry_quality":
    "questionable", "entry_status": "active", "entry_version": "4", "genome_accession":
    "LC274619.1", "locus_evidence_methods": "", "locus_from": "", "locus_to": "",
    "mibig_accession": "BGC0001528", "primary_reference": "DOI:10.1021/acs.orglett.7b03418",
    "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_EVIDENCE",
    "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1",
    "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1",
    "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1979465", "taxon_label": "Phoma betae"}, "row_sha256":
    "cf641d06dbb5ea24ddee1dacde8a131636aa450fed95f695051e055e5b47d336"}], "predicate":
    "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1844–1844; row_sha256 cf641d06dbb5ea24ddee1dacde8a131636aa450fed95f695051e055e5b47d336
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete physical source rows, all fields personally read and joined to
    the pinned table: [{"bgc_classes": "terpene", "bgc_subclasses": "Sesterterpene",
    "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index":
    "1", "compound_name": "betaestacin I", "database_ids": "", "entry_completeness":
    "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version":
    "4", "genome_accession": "LC274619.1", "locus_evidence_methods": "", "locus_from":
    "", "locus_to": "", "mibig_accession": "BGC0001528", "primary_reference": "DOI:10.1021/acs.orglett.7b03418",
    "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_EVIDENCE",
    "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1",
    "standard_inchi": "InChI=1S/C25H40/c1-17(2)21-14-16-25(6)15-13-18(3)7-10-22-19(4)8-11-23(22)20(5)9-12-24(21)25/h9-10,13,17,19,21,23-24H,7-8,11-12,14-16H2,1-6H3/b18-13?,20-9-,22-10+/t19-,21-,23-,24+,25+/m0/s1",
    "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1979465", "taxon_label": "Phoma betae"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2275-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [{"last_physical_line": 2107, "physical_line": 2107, "raw_tsv_record":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N\tCC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1\tTerpenoids\tSesterterpenoids\tBetaestacin-type
    sesterterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n", "row": {"class_results":
    "Betaestacin-type sesterterpenoids", "is_glycoside": "false", "model_version":
    "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles":
    "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1",
    "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "superclass_results": "Sesterterpenoids"},
    "row_sha256": "131db63860fcd1b3a0e471f49e4861f685beab839b8e82ed1fd03f40268131f7"}],
    "predicate": "exact complete standard_inchi_key equality", "query": "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2107–2107; row_sha256 131db63860fcd1b3a0e471f49e4861f685beab839b8e82ed1fd03f40268131f7
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete physical source rows, all fields personally read and joined to
    the pinned table: [{"class_results": "Betaestacin-type sesterterpenoids", "is_glycoside":
    "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results":
    "Terpenoids", "smiles": "CC1=CC[C@@](CC[C@H]2C(C)C)(C)[C@]2([H])C/C=C(C)\\[C@@]3([H])/C([C@@H](C)CC3)=C/C1",
    "standard_inchi_key": "RGXPVTCXXHGAHK-QFIDHXJRSA-N", "superclass_results": "Sesterterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2275-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact complete standard_inchi_key equality", "query":
    "RGXPVTCXXHGAHK-QFIDHXJRSA-N"}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact retained predicate and query with all matched physical payloads:
    {"matches": [], "predicate": "exact chebi_id from exact full-key structure rows",
    "query": []}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/source_taxa; /contexts/19/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/19/source_scope_inventory/nonorganism_matches; /contexts/19/source_scope_inventory/actual_assay_rows;
    /contexts/19/source_scope_inventory/blank_AID_sentinels; /contexts/19/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Exact source taxa and route lists, distinguishing forward merges/nonorganism
    matches and blank sentinels from actual assays: {"actual_assay_rows": [], "blank_AID_sentinels":
    [], "forward_taxon_merge_matches": [], "nonorganism_matches": [], "related_corpus_rows":
    [], "source_taxa": ["NCBITaxon:1979465"]}'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/70; /cached_taxonomy/unmatched_ids
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: 'Complete retained cache stanzas for this source-taxon scope, with cache
    misses retained globally and no fresh taxonomy or ancestry assertion: [{"complete_stanza":
    "[Term]\nid: NCBITaxon:1979465\nname: Neocamarosporium betae\nsynonym: \"Phoma
    betae\" EXACT []\nsynonym: \"Pleospora betae (Berl.) Nevod., 1915\" EXACT []\nsynonym:
    \"Pyrenophora echinella var. betae\" EXACT []\n\n", "id": "NCBITaxon:1979465",
    "physical_line": 142689}]'
  snapshot_sha256: 89211d5362eaa0fa9944acffc040fe9819637641b76a279e6339d90925fa7d0d
- evidence_id: bgc-2275-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch228-tentative/bgc-prep/bgc-conditional228-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: One bounded eight-table scan used 161 exact literals over 93 data rows,
    including ignored files by direct access. The only hit is the Avermitilol locus
    override at physical line 5; applicability is owner-specific. Reserved decisions.tsv
    was not consumed. PubChem exclusions were supplementary and are outside this batch
    input map.
  snapshot_sha256: 63a4685a365402d997d4f20d1b80d7dce1b7f62d2d2264c93dae7fa581e52df5
- evidence_id: bgc-2275-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: ChemicalStructure and ComputedClassification distinguish unspecified stereocentres,
    normalized keys and named/versioned model predictions; the latter are not source
    assertions or admission grounds.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2275-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–174
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The maintained extractor computes stereo_complete from FindMolChiralCenters
    with unassigned centres included; it does not test every double-bond geometry.
    No extractor was invoked here.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2275-origin-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1067–1196
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Producer and locus evidence grades are separately copied, with explicit
    merge/qualification handling. ChEBI occurrence assertions are not promoted to
    production.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2275-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 968–1060
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: Full-key source grounding, model prediction projection and source-concept
    preservation have separate maintained roles.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2275-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The current review profile requires claim-level identity, representation,
    evidence, provenance and completion coverage without promoting unavailable checks.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2275-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole skill
  accessed_at: '2026-11-03T18:38:32.836999Z'
  support: supports
  summary: The current one-record review procedure keeps source evidence and required
    verification limits explicit and does not authorize record edits or external requests
    here.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:12:47.775053Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: c21e163f3196cf186958794725f1b00a467ef5cca041142eb77868d0f57002a8
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:13:12.316523Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 87b8d13781a6e8b29a6548c0231420c70cfb7201c9942069049f0adfaa3a91dc
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:13:32.394271Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:14:07.640893Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-228/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-228/native-current228-five-gates-execution-001.json
  accessed_at: '2026-11-03T18:14:19.806834Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 8a9b4b2d4725b4513fcae189afd5e5e6f81b1ec228cdd2b2b100ff2dd2472a63
assessments:
- assessment_id: bgc-2275-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted identifier retains complete key RGXPVTCXXHGAHK-QFIDHXJRSA-N
    from MIBiG BGC0001528 version 4 compound index 1; the exact retained ChEBI structure
    join is empty. Both stored forms agree on C25H40 while explicitly retaining unresolved
    double-bond geometry. Direct companion Betaestacin II has a different complete
    key, so shared locus and model family do not supply missing geometry or identity.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-grounding-owner
  - bgc-2275-source-mibig_compounds
  - bgc-2275-query-chebi_structures
  - bgc-2275-chemistry
  - bgc-2275-topology
  - bgc-2275-direct-contexts
  - bgc-2275-companion-20
  dimensions:
  - name: standard_inchi_key
    value: RGXPVTCXXHGAHK-QFIDHXJRSA-N; full key retains the explicit geometry uncertainty.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2275-grounding-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-query-chebi_structures
    - bgc-2275-chemistry
    - bgc-2275-topology
    - bgc-2275-direct-contexts
    - bgc-2275-companion-20
  - name: grounding_scope
    value: MINTED with no exact retained ChEBI match; Betaestacin II is a distinct
      full-key owner.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2275-grounding-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-query-chebi_structures
    - bgc-2275-chemistry
    - bgc-2275-topology
    - bgc-2275-direct-contexts
    - bgc-2275-companion-20
- assessment_id: bgc-2275-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms are neutral C25H40 with 25 carbon atoms, 27 bonds and one fragment.
    SMILES centres C4 S, C7 S, C12 R, C17 S and C19 S are specified; two alkenes are
    Z/E and C1=C2 remains unspecified. The corresponding InChI bond C12=C17 is Unknown/STEREOANY
    with literal /b18-13?. The true stereo_complete flag follows the retained extractor's
    tetrahedral-centre test and does not resolve that bond. All ten comparisons and
    the stored correspondence agree without proving complete natural stereochemistry
    or independent full-graph identity.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-grounding-owner
  - bgc-2275-chemistry
  - bgc-2275-topology
  - bgc-2275-diagnostic-acceptance
  - bgc-2275-structure-schema
  - bgc-2275-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Five specified tetrahedra; two specified alkenes and one unresolved /b18-13?
      bond. True flag is centre-scoped.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2275-grounding-owner
    - bgc-2275-chemistry
    - bgc-2275-topology
    - bgc-2275-diagnostic-acceptance
    - bgc-2275-structure-schema
    - bgc-2275-stereo-method
  - name: representation_correspondence
    value: Ten true comparisons and complete correspondence; unspecified geometry
      and full_graph_identity_established:false remain.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2275-grounding-owner
    - bgc-2275-chemistry
    - bgc-2275-topology
    - bgc-2275-diagnostic-acceptance
    - bgc-2275-structure-schema
    - bgc-2275-stereo-method
- assessment_id: bgc-2275-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0001528 version 4 is active, questionable and of unknown completeness.
    The source label Phoma betae at taxon 1979465 remains a SOURCE_ASSERTION, while
    the locus is CLUSTER_UNSTATED with genbank:LC274619.1 and no method or interval
    stated. The cached current name Neocamarosporium betae explicitly includes Phoma
    betae as an exact synonym; this retained name continuity does not upgrade production
    or locus evidence.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-origin-owner
  - bgc-2275-source-mibig_compounds
  - bgc-2275-cached-taxonomy
  - bgc-2275-source-routes
  - bgc-2275-origin-seeder
  dimensions:
  - name: taxon_scope
    value: Historical Phoma betae 1979465 is an exact cached synonym of Neocamarosporium
      betae.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2275-origin-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-cached-taxonomy
    - bgc-2275-source-routes
    - bgc-2275-origin-seeder
  - name: producer_evidence
    value: SOURCE_ASSERTION only.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2275-origin-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-cached-taxonomy
    - bgc-2275-source-routes
    - bgc-2275-origin-seeder
  - name: locus_evidence
    value: BGC0001528 version 4, questionable/unknown, CLUSTER_UNSTATED; no method
      or bounds.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2275-origin-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-cached-taxonomy
    - bgc-2275-source-routes
    - bgc-2275-origin-seeder
- assessment_id: bgc-2275-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: DOI:10.1021/acs.orglett.7b03418 is explicitly taken from the MIBiG compound
    evidence level and reused for producer and locus assertions. Its presence does
    not establish that the complete pathway, native genome context or unresolved alkene
    configuration was experimentally verified in this review. The distinct Betaestacin
    II companion remains separately owned despite shared BGC metadata.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-origin-owner
  - bgc-2275-occurrence-owner
  - bgc-2275-source-mibig_compounds
  - bgc-2275-query-chebi_origins
  - bgc-2275-source-notes
  - bgc-2275-direct-contexts
  - bgc-2275-companion-20
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI:10.1021/acs.orglett.7b03418, not fresh pathway or
      stereo verification.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2275-origin-owner
    - bgc-2275-occurrence-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-query-chebi_origins
    - bgc-2275-source-notes
    - bgc-2275-direct-contexts
    - bgc-2275-companion-20
- assessment_id: bgc-2275-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The owner writes no occurrences, bioactivities, molecular targets or mechanism
    roots. Its exact retained occurrence, PubChem, BindingDB and AntibioticMech routes
    are empty. Betaestacin II's blank-AID no-assay-data sentinel belongs to that companion
    and transfers no activity or inactivity to Betaestacin I. No global biological-absence
    claim follows.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-occurrence-owner
  - bgc-2275-assay-owner
  - bgc-2275-source-routes
  - bgc-2275-cached-taxonomy
  - bgc-2275-query-lotus_occurrences
  - bgc-2275-query-chebi_origins
  - bgc-2275-query-cyanometdb_occurrences
  - bgc-2275-query-pubchem_bioassay
  - bgc-2275-query-bindingdb_targets
  - bgc-2275-query-antibioticmech_inchikeys
  - bgc-2275-companion-20
  dimensions:
  - name: occurrence_scope
    value: No written occurrences and bounded empty exact occurrence routes.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2275-occurrence-owner
    - bgc-2275-assay-owner
    - bgc-2275-source-routes
    - bgc-2275-cached-taxonomy
    - bgc-2275-query-lotus_occurrences
    - bgc-2275-query-chebi_origins
    - bgc-2275-query-cyanometdb_occurrences
    - bgc-2275-query-pubchem_bioassay
    - bgc-2275-query-bindingdb_targets
    - bgc-2275-query-antibioticmech_inchikeys
    - bgc-2275-companion-20
  - name: assay_target_scope
    value: No own assay/target rows; companion blank-AID sentinel is not transferred.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2275-occurrence-owner
    - bgc-2275-assay-owner
    - bgc-2275-source-routes
    - bgc-2275-cached-taxonomy
    - bgc-2275-query-lotus_occurrences
    - bgc-2275-query-chebi_origins
    - bgc-2275-query-cyanometdb_occurrences
    - bgc-2275-query-pubchem_bioassay
    - bgc-2275-query-bindingdb_targets
    - bgc-2275-query-antibioticmech_inchikeys
    - bgc-2275-companion-20
- assessment_id: bgc-2275-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The source TERPENE/Sesterterpene class is separate from NPClassifier Terpenoids
    / Sesterterpenoids / Betaestacin-type sesterterpenoids and is_glycoside:false.
    The complete C25 carbocyclic hydrocarbon topology is compatible with the broad
    filing and cannot itself contain an O-glycosidic linkage or sugar residue. This
    structural compatibility does not validate the biosynthetic route or supply the
    unresolved double-bond geometry.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-classification-owner
  - bgc-2275-source-mibig_compounds
  - bgc-2275-source-npclassifier
  - bgc-2275-chemistry
  - bgc-2275-topology
  - bgc-2275-structure-schema
  - bgc-2275-classification-seeder
  dimensions:
  - name: classification_applicability
    value: Named Betaestacin-type model and false glycoside prediction; C25 hydrocarbon
      topology does not prove biosynthesis.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2275-classification-owner
    - bgc-2275-source-mibig_compounds
    - bgc-2275-source-npclassifier
    - bgc-2275-chemistry
    - bgc-2275-topology
    - bgc-2275-structure-schema
    - bgc-2275-classification-seeder
- assessment_id: bgc-2275-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All required scientific dimensions were assessed against the current owner,
    actual intake, retained source payloads and complete paired molecular tables.
    Five local gates passed, while full QC and complete OAK authority coverage remain
    unavailable. No selected mechanism reader is applicable to this owner. External
    facts remain unverified under the no-request instruction, so completion is partial
    and native curation status is unchanged.
  target_ids:
  - naturalproductmech:mibig-b113a8e29e
  evidence_ids:
  - bgc-2275-owner
  - bgc-2275-intake
  - bgc-2275-intake-acceptance
  - bgc-2275-inventory-acceptance
  - bgc-2275-plan
  - bgc-2275-plan-acceptance
  - bgc-2275-source-notes
  - bgc-2275-curation-scope
  - bgc-2275-diagnostic-execution
  - bgc-2275-diagnostic-acceptance
  - bgc-2275-native-acceptance
  - bgc-2275-review-profile
  - bgc-2275-review-skill
  dimensions:
  - name: review_completion
    value: Partial scientific review; actual intake and stored-form checks accepted,
      full QC/OAK and fresh external verification unavailable. No supported local
      curation defect identified.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2275-owner
    - bgc-2275-intake
    - bgc-2275-intake-acceptance
    - bgc-2275-inventory-acceptance
    - bgc-2275-plan
    - bgc-2275-plan-acceptance
    - bgc-2275-source-notes
    - bgc-2275-curation-scope
    - bgc-2275-diagnostic-execution
    - bgc-2275-diagnostic-acceptance
    - bgc-2275-native-acceptance
    - bgc-2275-review-profile
    - bgc-2275-review-skill
findings: []
actions: []
limitations:
- External identifiers, taxonomy, genome accessions and primary publications were
  not refreshed under the absolute no-request instruction. Historical and database
  assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form
  parsing establish only their declared mechanical scope.
- Empty joins refer only to retained exact predicates and snapshots; they do not establish
  biological absence. Shared loci, citations and congeners do not transfer compound-specific
  claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, native curation status and histories were not edited.
- The retained true stereo_complete flag is tetrahedral-centre scoped. Explicit unknown
  double-bond geometry remains represented and is not resolved by form agreement.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The complete owner/history, actual intake, exact assigned source payloads and both
  complete saved molecular tables were personally read. Complementary source and companion
  reading is explicitly attributed in the pinned notes.
- The original batch diagnostic has two global undefined-stereo warnings, not attributed
  to individual records. All true comparison flags leave full_graph_identity_established:false
  unchanged.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-228
```
