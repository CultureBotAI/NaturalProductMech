# Local evidence review: chejuenolide A

- Review: 20261103T210813Z-chejuenolide-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T20:21:12.269955Z
- Finished UTC: 2026-11-03T21:08:13.277249Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chejuenolide A preserves its distinct full stereochemical key and retained source claims. The saved SMILES and InChI parses differ by an amide–imidic representation change; normalized identifiers agree while canonical forms and the original map do not. Scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2297; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-24b010d9e9 | data/natural_products/terpenoids/chejuenolide-a.yaml | generated | chejuenolide A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-24b010d9e9 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-24b010d9e9 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-24b010d9e9 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-24b010d9e9 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-24b010d9e9 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-24b010d9e9 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-24b010d9e9 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-24b010d9e9 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-24b010d9e9.

The minted identifier retains UTURGGMCWRWPTG-YOFHZKFDSA-N from BGC0001543 version 3, compound index 1. The exact retained ChEBI structure join is empty. Both saved forms produce C23H33NO4 and the same declared standardized key, while the false canonical comparisons remain visible. Chejuenolide B has a different full stereochemical key and the opposite configuration at SMILES atom 1; shared connectivity and locus do not justify merging them.

### Representation

representation: supported. Targets: naturalproductmech:mibig-24b010d9e9.

Both forms are neutral C23H33NO4 with 28 atoms, 28 bonds and a 17-carbon macrocycle. Five E alkenes and four tetrahedral centres are specified in the stored form. The original canonical isomeric and nonisomeric SMILES comparisons are false, and the diagnostic correspondence is empty. Support's complete saved-table witness maps source N3 to derived N23 with one fewer H and source O6 to O24 with one additional H: C4–N3 becomes C18=N23 and C4=O6 becomes C18–O24. Other mapped adjacency, rings and retained stereochemistry agree. The mobile-H normalization is consistent with an N-acetyl amide becoming an imidic C(O)=N form, which adds an unspecified C=N potential element. This narrower manual witness does not replace the original empty map or its full_graph_identity_established:false result. The source true flag describes its tetrahedral-centre test, not all possible bond geometry.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-24b010d9e9.

The retained BGC0001543 version 3 entry is active, questionable quality and unknown completeness. Hahella chejuensis (158327) is a SOURCE_ASSERTION producer; no locus method is stated, and the locus is CLUSTER_UNSTATED. The source interval HE664023.1:1–51429 and the matching cached species label are preserved. Species-level LOTUS occurrence claims do not upgrade the producer or locus grade.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-24b010d9e9.

ENTRY-level PMID:29483632 is reused in the producer and locus database assertions. Two LOTUS rows cite DOI:10.1016/J.TETLET.2008.09.143 and DOI:10.1038/S41429-017-0023-X. Their relationship to the PMID and their experimental independence were not freshly verified. The B congener's shared locus and one shared DOI do not transfer identity, activity or mechanism.

### Occurrence and activity

evidence: supported. Targets: naturalproductmech:mibig-24b010d9e9.

Two retained LOTUS assertions name Hahella chejuensis (158327); these are two citation placements, not two proven independent production studies. The complete owner has no written assay, activity summary, target or mechanism roots. Exact saved PubChem, BindingDB, AntibioticMech, ChEBI-origin and CyanometDB joins are empty. No biological inactivity or global absence claim follows.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-24b010d9e9.

The source BGC class is PKS, whereas NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids / Diterpenoids with an empty class list and is_glycoside:false. Those are distinct source and computed axes. The stored macrocycle contains an N-acetyl amide, a ketone and hydroxyl substituents, not an ester ring established by the name suffix. No carbohydrate residue is established by the complete graph. The model label does not independently prove a terpene biosynthetic origin or invalidate the retained PKS source; no automatic filing or identity correction is warranted.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-24b010d9e9.

All twelve scientific dimensions were assessed against complete current owner/history, actual canonical intake, retained source payloads and the attributed complete saved molecular tables. The five original local commands passed, while full QC, complete OAK authority coverage and fresh external verification remain unavailable. No mechanism root or reader is applicable to this owner. The completed eight-table curation scan found no matching exact cohort token within its declared ignore-independent scope. No supported new source correction is established; scientific completion remains partial and native curation status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2297-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/chejuenolide-a.yaml; Whole owner plaintext and complete curation_history | supports | Complete current owner with all 3 history entries. Whole reading and exact prior carries are explicitly attributed; native curation_status remains SEEDED. |
| bgc-2297-capture | /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json; /records/6/owner_pin; /records/6/owner_document | supports | Complete captured owner retains all written fields and history. |
| bgc-2297-intake | /private/tmp/npm-review-work/shared-next-batch230/intakes/2297-inspect-001.json; /source; /targets | supports | Actual one-record canonical intake for naturalproductmech:mibig-24b010d9e9; 38 pinned input placements and explicit maintained ownership. |
| bgc-2297-grounding-owner | /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete written field projection, with absence bounded by the complete captured owner: {"chemical_structure":{"smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi":"InChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001543"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-24b010d9e9","label":"chejuenolide A","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-24b010d9e9","source":"MIBIG","source_id":"BGC0001543","source_label":"chejuenolide A","source_version":"3"}],"xrefs":["npatlas:NPA015931"]} |
| bgc-2297-origin-owner | /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete written field projection, with absence bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001543","bgc_class":["PKS"],"entry_status":"active","entry_version":"3","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001543 entry version 3; citation taken from the entry level","reference":"PMID:29483632"}],"genome_accession":"genbank:HE664023.1","link_evidence_basis":"CLUSTER_UNSTATED","locus_from":1,"locus_to":51429,"organism_label":"Hahella chejuensis","organism_taxon_id":"NCBITaxon:158327"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001543","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001543 entry version 3; citation taken from the entry level","reference":"PMID:29483632"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"3","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella chejuensis"}],"producer_taxon_groups":["OTHER_BACTERIAL"]} |
| bgc-2297-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete written field projection, with absence bounded by the complete captured owner: {"occurrence_taxon_groups":["OTHER_BACTERIAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/J.TETLET.2008.09.143"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q21265633 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.","source":"LOTUS","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella chejuensis","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1038/S41429-017-0023-X"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q21265633 This taxon is also recorded as a producer. Production and occurrence are distinct claims; their citations may refer to the same publication. Publication independence has not been established.","source":"LOTUS","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella chejuensis","taxon_source":"NCBITaxon"}]} |
| bgc-2297-assay-owner | /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete written field projection, with absence bounded by the complete captured owner: {} |
| bgc-2297-classification-owner | /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json; /records/6/owner_document | supports | Complete written field projection, with absence bounded by the complete captured owner: {"bgc_class":["PKS"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":[],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2297-chemistry | /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/smiles/status; /records/6/inchi/status; /records/6/smiles/computed; /records/6/inchi/computed; /records/6/comparisons; /records/6/atom_correspondence | supports | Both stored forms parsed. Exact original comparison and correspondence values are retained: {"atom_correspondence":{"complete_atom_count_match":false,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":false,"canonical_nonisomeric_smiles_equal":false,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true}} Complete saved atom/bond/ring/stereo/motif dictionaries are selected. |
| bgc-2297-topology | /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed | supports | {"inchi_formula":"C23H33NO4","inchi_rings":[[5,9,19,11,7,15,13,21,17,22,16,8,12,20,10,6,14]],"inchi_stereo":{"Atom_Tetrahedral:Specified":4,"Bond_Double:Specified":5,"Bond_Double:Unspecified":1},"scope":"The selected complete saved computed objects include all atom/bond/motif fields; no new parse or identity inference.","smiles_formula":"C23H33NO4","smiles_rings":[[1,2,7,8,10,11,12,14,15,16,18,19,20,22,23,24,26]],"smiles_stereo":{"Atom_Tetrahedral:Specified":4,"Bond_Double:Specified":5}} |
| bgc-2297-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch230/bgc-current230-combined-diagnostic-reading-001.json; /whole_reading; /per_owner_interpretation; /limitations | supports | BGC first-five and Support last-five complete saved-table interpretations are separately attributed, with original false comparisons, global warnings and natural-identity limits preserved. |
| bgc-2297-support-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch230-tentative/support-prep/support-current230-last-five-diagnostic-reading-001.json; /scope; /readings; /meanings; /Cheju_saved_table_witness; /limits | supports | Support personally read the complete last-five tables. Its manually identified Cheju correspondence is a separate saved-row witness and does not overwrite the original diagnostic maps. |
| bgc-2297-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-execution-001.json; /observer; /command; /cwd; /started_at; /finished_at; /exit_code; /source; /source_admission; /environment_manifest; /actual_environment; /stdout; /stderr; /external_requests | supports | Original execution receipt retains the command, clocks, exit 0 and exact stdout/stderr pins; no new diagnostic execution is claimed. |
| bgc-2297-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch230/root-chemistry-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /capture; /intake_summary; /molecular_parse_attempts; /false_comparisons; /original_stderr; /ROOT_reading; /scientific_reading; /limits; /external_requests; /molecular_replays | supports | ROOT accepts the original twenty stored-form parses and saved integrity. Two false canonical flags for each Cheju owner and the global unassigned stderr warnings remain explicit. |
| bgc-2297-native-acceptance | /private/tmp/npm-review-work/shared-next-batch230/root-native-gates-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /execution; /original_tools; /native_readback; /checks; /unavailable_required_gates; /five_local_commands_passed; /all_native_gates_passed; /ROOT_reading; /external_requests; /gate_replays; /scientific_verdicts | supports | ROOT accepts five original local commands. all_native_gates_passed remains false; full QC and OAK are unavailable, and command success does not certify scientific identity. |
| bgc-2297-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch230/root-intake-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /intake_summary; /controller_execution; /original_tools; /source_admission; /input_plan; /selection; /capture; /counts; /per_owner; /ROOT_reading; /external_requests; /canonical_target_replays | supports | ROOT accepts the original ten canonical intakes and their exact current input/owner maps. |
| bgc-2297-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch230-tentative/root-source-inventory-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /inventory; /execution; /original_tools; /source_admission; /capture_acceptance; /totals; /per_order_input_counts; /ROOT_reading; /scientific_reading; /scope; /external_requests; /source_query_replays; /YAML_or_molecular_parses | supports | ROOT accepts the original saved source inventory and current input pins; semantic reading is separately attributed. |
| bgc-2297-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch230-tentative/root-input-plan-acceptance-001.json; /observer; /recorded_at; /accepted; /status; /input_plan; /derivation; /execution; /original_tools; /source_admission; /inventory; /source_notes; /counts; /reader_orders; /ROOT_reading; /scientific_verdicts; /external_requests | supports | ROOT accepts the actual target-input plan; four other selected owners require maintained readers, while this exact owner has no mechanism roots. |
| bgc-2297-plan | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-target-input-plan-001.json; /records/6 | supports | Accepted owner-specific source projection, exact direct contexts and input ownership; no selected mechanism reader applies to this owner. |
| bgc-2297-source-notes | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source-payload/cache reading, whole raw/history carries and mechanism-context boundaries are attributed; no source query was replayed during authoring. |
| bgc-2297-curation-scope | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-scope-notes-001.json; /curation | supports | The completed case-sensitive literal scan tested 416 exact cohort tokens against eight directly opened implemented curation tables, including ignored files and headers, and found zero matches in that bounded scope. Reserved decisions.tsv was not consumed. |
| bgc-2297-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[{"last_physical_line":1854,"physical_line":1854,"raw_tsv_record":"BGC0001543\t3\tactive\tquestionable\tunknown\tchejuenolide A\t1\tC[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O\tInChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1\tUTURGGMCWRWPTG-YOFHZKFDSA-N\ttrue\t\tnpatlas:NPA015931\tNCBITaxon:158327\tHahella chejuensis\tPKS\tUnknown\tHE664023.1\t1\t51429\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:29483632\tENTRY\n","row":{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"chejuenolide A","database_ids":"npatlas:NPA015931","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HE664023.1","locus_evidence_methods":"","locus_from":"1","locus_to":"51429","mibig_accession":"BGC0001543","primary_reference":"PMID:29483632","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi":"InChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella chejuensis"},"row_sha256":"5beab1a9e1c15967ebb4196c5d8f3a13daa8dd640bae067cde7d03667608834c"}],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1854–1854; row_sha256 5beab1a9e1c15967ebb4196c5d8f3a13daa8dd640bae067cde7d03667608834c | supports | Complete retained physical payloads, every field: [{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"chejuenolide A","database_ids":"npatlas:NPA015931","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HE664023.1","locus_evidence_methods":"","locus_from":"1","locus_to":"51429","mibig_accession":"BGC0001543","primary_reference":"PMID:29483632","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi":"InChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella chejuensis"}] |
| bgc-2297-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[{"last_physical_line":8913,"physical_line":8913,"raw_tsv_record":"UTURGGMCWRWPTG-YOFHZKFDSA-N\tHahella chejuensis\tNCBITaxon:158327\thttp://www.wikidata.org/entity/Q21265633\t10.1016/J.TETLET.2008.09.143\thttp://www.wikidata.org/entity/Q77568244\n","row":{"organism_name":"Hahella chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1016/J.TETLET.2008.09.143","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"},"row_sha256":"eaea5e133861c2512e6a5f161b6763d7211f8f5c57c7ecb8335e6aebbf255c9f"},{"last_physical_line":8914,"physical_line":8914,"raw_tsv_record":"UTURGGMCWRWPTG-YOFHZKFDSA-N\tHahella chejuensis\tNCBITaxon:158327\thttp://www.wikidata.org/entity/Q21265633\t10.1038/S41429-017-0023-X\thttp://www.wikidata.org/entity/Q77568244\n","row":{"organism_name":"Hahella chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1038/S41429-017-0023-X","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"},"row_sha256":"42ba8e43ea727f6fb815f2bfc77066aea30c929b95179a49505ce821a4338010"}],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 8913–8913; row_sha256 eaea5e133861c2512e6a5f161b6763d7211f8f5c57c7ecb8335e6aebbf255c9f; physical lines 8914–8914; row_sha256 42ba8e43ea727f6fb815f2bfc77066aea30c929b95179a49505ce821a4338010 | supports | Complete retained physical payloads, every field: [{"organism_name":"Hahella chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1016/J.TETLET.2008.09.143","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"},{"organism_name":"Hahella chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1038/S41429-017-0023-X","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"}] |
| bgc-2297-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[{"last_physical_line":2461,"physical_line":2461,"raw_tsv_record":"UTURGGMCWRWPTG-YOFHZKFDSA-N\tC[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O\tTerpenoids\tDiterpenoids\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","superclass_results":"Diterpenoids"},"row_sha256":"8f2b09fc5001d64763e19e1036b937fb91abbd9ad3a931b438e0bebd8e04790e"}],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2461–2461; row_sha256 8f2b09fc5001d64763e19e1036b937fb91abbd9ad3a931b438e0bebd8e04790e | supports | Complete retained physical payloads, every field: [{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","superclass_results":"Diterpenoids"}] |
| bgc-2297-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"} |
| bgc-2297-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame with literal predicates and all matched fields, including no-match results: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2297-source-routes | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/source_taxa; /contexts/13/source_scope_inventory/forward_taxon_merge_matches; /contexts/13/source_scope_inventory/nonorganism_matches; /contexts/13/source_scope_inventory/actual_assay_rows; /contexts/13/source_scope_inventory/blank_AID_sentinels; /contexts/13/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists; only the forward-merge/nonorganism/assay lists are asserted empty where shown: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:158327"]} |
| bgc-2297-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/245 | supports | Complete retained source-taxon stanzas; local cache labels and synonyms are not fresh authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:158327\nname: Hahella chejuensis\n\n","id":"NCBITaxon:158327","physical_line":54382}] |
| bgc-2297-direct-contexts | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /records/6/direct_companion_paths; /records/6/direct_companion_predicates | supports | Exact one-hop contexts/predicates, without transitive identity or claim transfer: {"direct_companion_paths":["data/natural_products/terpenoids/chejuenolide-b.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/chejuenolide-b.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001543"]}]} |
| bgc-2297-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json; /contexts/14 | supports | Whole direct raw/history/source contexts are retained and already read with exact attribution in the source notes. Their full keys and citation roles remain distinct: [{"fullkey":"UTURGGMCWRWPTG-PFBVZISFSA-N","identifier":"naturalproductmech:mibig-f2fa461bbb","owned_BGCs":["BGC0001543"],"path":"data/natural_products/terpenoids/chejuenolide-b.yaml"}] |
| bgc-2297-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure preserves source representation and explicitly limits standardized identity and undefined centres. ComputedClassification is a named/versioned prediction, never a source assertion or admission criterion. |
| bgc-2297-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained extraction derives stereo_complete from FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False) and absence of question-mark centre tags; it is not an all-bond-geometry proof. |
| bgc-2297-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 974–1065 | supports | Maintained seeding preserves the source structure and complete named/versioned prediction including is_glycoside, while keeping source BGC classes separately. |
| bgc-2297-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile | supports | One-record review requires claim-level evidence and all dimensions, with truthful unavailable-check and partial-completion limits. |
| bgc-2297-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole skill | supports | The review procedure does not edit records, and source access must remain honestly bounded by the overriding no-request instruction. |
| bgc-2297-congener-structure | /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/7/declared_structure; /records/6/smiles/computed; /records/7/smiles/computed | supports | Both Cheju source-form structures and complete atom tables preserve distinct full keys and the R/S difference at SMILES atom 1. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-230/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-230/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-230/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-230/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-230/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally; external identifiers, primary publications, taxonomy, accessions and natural stereochemical assignments were not refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates and parsed representations establish only their stated mechanical scope.
- Empty joins concern only the exact saved predicates and snapshots. Shared loci, taxa and citations do not transfer compound-specific activity, production, mechanism or independent-study status.
- The two original undefined-stereo warnings remain global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during this scientific authoring.
- The review proposes no source-record, native-status or history edit; any later correction belongs to the exact maintained owners listed in the accepted intake.
- The manual saved-table amide–imidic witness does not establish exact-form identity and does not overwrite the original false comparisons or empty correspondence.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual intake have been read; whole-source and exact companion carries are attributed in the pinned notes.
- BGC personally interpreted the Calidoustene B/C molecular tables; Support personally interpreted the complete later-five tables and exact Cheju witness. The combined reading note preserves this attribution.
- ROOT executed the original collector, composer, capture, canonical intakes and chemistry; Native executed the five original local gates. No new target was invoked for these six assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T210813Z-chejuenolide-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: chejuenolide A'
started_at: '2026-11-03T20:21:12.269955Z'
finished_at: '2026-11-03T21:08:13.277249Z'
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
summary: Chejuenolide A preserves its distinct full stereochemical key and retained
  source claims. The saved SMILES and InChI parses differ by an amide–imidic representation
  change; normalized identifiers agree while canonical forms and the original map
  do not. Scientific completion remains partial.
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
  - path: data/natural_products/terpenoids/chejuenolide-a.yaml
    sha256: c3a20959a8a2f4bf6bc6ed5f113ac22b7db7efcc6dde10d19c6ff47b9e9cd85a
    role: target
  - path: data/natural_products/terpenoids/chejuenolide-b.yaml
    sha256: a6187959ef02b1ad893553d50b851aad218ee266925e750f0c1285cb6757049f
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
  selection: Campaign path order 2297; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-24b010d9e9
targets:
- target_id: naturalproductmech:mibig-24b010d9e9
  path: data/natural_products/terpenoids/chejuenolide-a.yaml
  label: chejuenolide A
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
  - naturalproductmech:mibig-24b010d9e9
  command: just validate-strict data/natural_products/terpenoids/calidoustene-b.yaml
    data/natural_products/terpenoids/calidoustene-c.yaml data/natural_products/terpenoids/capsidiol.yaml
    data/natural_products/terpenoids/carotene.yaml data/natural_products/terpenoids/casbene.yaml
    data/natural_products/terpenoids/cattleyene.yaml data/natural_products/terpenoids/chejuenolide-a.yaml
    data/natural_products/terpenoids/chejuenolide-b.yaml data/natural_products/terpenoids/clavaric-acid.yaml
    data/natural_products/terpenoids/compound-11.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-230/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-24b010d9e9
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-230/validate-all-001.tsv
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
  - naturalproductmech:mibig-24b010d9e9
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
  - naturalproductmech:mibig-24b010d9e9
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
  - naturalproductmech:mibig-24b010d9e9
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-230/review-queue-001.tsv
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
  - naturalproductmech:mibig-24b010d9e9
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2297-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/chejuenolide-a.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Complete current owner with all 3 history entries. Whole reading and exact
    prior carries are explicitly attributed; native curation_status remains SEEDED.
  snapshot_sha256: c3a20959a8a2f4bf6bc6ed5f113ac22b7db7efcc6dde10d19c6ff47b9e9cd85a
- evidence_id: bgc-2297-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json
  locator: /records/6/owner_pin; /records/6/owner_document
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Complete captured owner retains all written fields and history.
  snapshot_sha256: 7b80365e39c220cc3416538128a85259a945fa33377cbd799850dbe626a62b1c
- evidence_id: bgc-2297-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/intakes/2297-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Actual one-record canonical intake for naturalproductmech:mibig-24b010d9e9;
    38 pinned input placements and explicit maintained ownership.
  snapshot_sha256: c9edde68c2365d86ad020d32e10694ff233beec5f09596794de712a4f5e37df2
- evidence_id: bgc-2297-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete written field projection, with absence bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi":"InChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001543"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-24b010d9e9","label":"chejuenolide
    A","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-24b010d9e9","source":"MIBIG","source_id":"BGC0001543","source_label":"chejuenolide
    A","source_version":"3"}],"xrefs":["npatlas:NPA015931"]}'
  snapshot_sha256: 7b80365e39c220cc3416538128a85259a945fa33377cbd799850dbe626a62b1c
- evidence_id: bgc-2297-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete written field projection, with absence bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001543","bgc_class":["PKS"],"entry_status":"active","entry_version":"3","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001543 entry version 3; citation taken from the entry level","reference":"PMID:29483632"}],"genome_accession":"genbank:HE664023.1","link_evidence_basis":"CLUSTER_UNSTATED","locus_from":1,"locus_to":51429,"organism_label":"Hahella
    chejuensis","organism_taxon_id":"NCBITaxon:158327"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001543","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001543 entry version 3; citation taken from the entry level","reference":"PMID:29483632"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"3","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella
    chejuensis"}],"producer_taxon_groups":["OTHER_BACTERIAL"]}'
  snapshot_sha256: 7b80365e39c220cc3416538128a85259a945fa33377cbd799850dbe626a62b1c
- evidence_id: bgc-2297-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete written field projection, with absence bounded by the complete
    captured owner: {"occurrence_taxon_groups":["OTHER_BACTERIAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/J.TETLET.2008.09.143"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q21265633 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.","source":"LOTUS","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella
    chejuensis","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1038/S41429-017-0023-X"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q21265633 This taxon is also recorded
    as a producer. Production and occurrence are distinct claims; their citations
    may refer to the same publication. Publication independence has not been established.","source":"LOTUS","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella
    chejuensis","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: 7b80365e39c220cc3416538128a85259a945fa33377cbd799850dbe626a62b1c
- evidence_id: bgc-2297-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete written field projection, with absence bounded by the complete
    captured owner: {}'
  snapshot_sha256: 7b80365e39c220cc3416538128a85259a945fa33377cbd799850dbe626a62b1c
- evidence_id: bgc-2297-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/owner-capture-DATA-001.json
  locator: /records/6/owner_document
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete written field projection, with absence bounded by the complete
    captured owner: {"bgc_class":["PKS"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":[],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: 7b80365e39c220cc3416538128a85259a945fa33377cbd799850dbe626a62b1c
- evidence_id: bgc-2297-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/smiles/status; /records/6/inchi/status;
    /records/6/smiles/computed; /records/6/inchi/computed; /records/6/comparisons;
    /records/6/atom_correspondence
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison and correspondence
    values are retained: {"atom_correspondence":{"complete_atom_count_match":false,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":false,"canonical_nonisomeric_smiles_equal":false,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true}}
    Complete saved atom/bond/ring/stereo/motif dictionaries are selected.'
  snapshot_sha256: 96dda81188846db96a060530063819053908a4cfca966a26b040e1263f1c0d1f
- evidence_id: bgc-2297-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: '{"inchi_formula":"C23H33NO4","inchi_rings":[[5,9,19,11,7,15,13,21,17,22,16,8,12,20,10,6,14]],"inchi_stereo":{"Atom_Tetrahedral:Specified":4,"Bond_Double:Specified":5,"Bond_Double:Unspecified":1},"scope":"The
    selected complete saved computed objects include all atom/bond/motif fields; no
    new parse or identity inference.","smiles_formula":"C23H33NO4","smiles_rings":[[1,2,7,8,10,11,12,14,15,16,18,19,20,22,23,24,26]],"smiles_stereo":{"Atom_Tetrahedral:Specified":4,"Bond_Double:Specified":5}}'
  snapshot_sha256: 96dda81188846db96a060530063819053908a4cfca966a26b040e1263f1c0d1f
- evidence_id: bgc-2297-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/bgc-current230-combined-diagnostic-reading-001.json
  locator: /whole_reading; /per_owner_interpretation; /limitations
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: BGC first-five and Support last-five complete saved-table interpretations
    are separately attributed, with original false comparisons, global warnings and
    natural-identity limits preserved.
  snapshot_sha256: a9f1e3364c2e966017b34e7002684a7fbf573e7f800176f47c5999b678f10d20
- evidence_id: bgc-2297-support-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/support-prep/support-current230-last-five-diagnostic-reading-001.json
  locator: /scope; /readings; /meanings; /Cheju_saved_table_witness; /limits
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Support personally read the complete last-five tables. Its manually identified
    Cheju correspondence is a separate saved-row witness and does not overwrite the
    original diagnostic maps.
  snapshot_sha256: ef1ef7e0e1b6145aefcf222de957f960786bc5fb0ce698d9f75d90ecfb0f8745
- evidence_id: bgc-2297-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-execution-001.json
  locator: /observer; /command; /cwd; /started_at; /finished_at; /exit_code; /source;
    /source_admission; /environment_manifest; /actual_environment; /stdout; /stderr;
    /external_requests
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Original execution receipt retains the command, clocks, exit 0 and exact
    stdout/stderr pins; no new diagnostic execution is claimed.
  snapshot_sha256: 837af035d4d527f6fb7c9142080b7b05e02020e2e12a94966de93a00e7307284
- evidence_id: bgc-2297-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/root-chemistry-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /capture; /intake_summary; /molecular_parse_attempts; /false_comparisons; /original_stderr;
    /ROOT_reading; /scientific_reading; /limits; /external_requests; /molecular_replays
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: ROOT accepts the original twenty stored-form parses and saved integrity.
    Two false canonical flags for each Cheju owner and the global unassigned stderr
    warnings remain explicit.
  snapshot_sha256: 3bdca09956eda07943344859a3fbe8c3080f91b20f921966cdfce552f165f492
- evidence_id: bgc-2297-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/root-native-gates-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /execution; /original_tools;
    /native_readback; /checks; /unavailable_required_gates; /five_local_commands_passed;
    /all_native_gates_passed; /ROOT_reading; /external_requests; /gate_replays; /scientific_verdicts
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: ROOT accepts five original local commands. all_native_gates_passed remains
    false; full QC and OAK are unavailable, and command success does not certify scientific
    identity.
  snapshot_sha256: d9c9c2383b0c2fbc8d9909fbd8d69cd87fc27bfa531084c338091403dc7d733f
- evidence_id: bgc-2297-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/root-intake-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /intake_summary; /controller_execution;
    /original_tools; /source_admission; /input_plan; /selection; /capture; /counts;
    /per_owner; /ROOT_reading; /external_requests; /canonical_target_replays
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: ROOT accepts the original ten canonical intakes and their exact current
    input/owner maps.
  snapshot_sha256: 42ccf246dce2085c37c35b04737a6546e030ca92afd2bedff69b89a0b172296c
- evidence_id: bgc-2297-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/root-source-inventory-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /inventory; /execution; /original_tools;
    /source_admission; /capture_acceptance; /totals; /per_order_input_counts; /ROOT_reading;
    /scientific_reading; /scope; /external_requests; /source_query_replays; /YAML_or_molecular_parses
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: ROOT accepts the original saved source inventory and current input pins;
    semantic reading is separately attributed.
  snapshot_sha256: 463d30a2886bffa6358db246613d007802e8a07225cb82419011c6ae9735ef52
- evidence_id: bgc-2297-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/root-input-plan-acceptance-001.json
  locator: /observer; /recorded_at; /accepted; /status; /input_plan; /derivation;
    /execution; /original_tools; /source_admission; /inventory; /source_notes; /counts;
    /reader_orders; /ROOT_reading; /scientific_verdicts; /external_requests
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: ROOT accepts the actual target-input plan; four other selected owners require
    maintained readers, while this exact owner has no mechanism roots.
  snapshot_sha256: 780cacb47734317cde06ab5584737902b10372dfb2267283c255219b4280e415
- evidence_id: bgc-2297-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Accepted owner-specific source projection, exact direct contexts and input
    ownership; no selected mechanism reader applies to this owner.
  snapshot_sha256: 8c93a5bac649164b594d490b9a38136e954a2cc79f8336a847094e70f96c652b
- evidence_id: bgc-2297-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Complete disjoint source-payload/cache reading, whole raw/history carries
    and mechanism-context boundaries are attributed; no source query was replayed
    during authoring.
  snapshot_sha256: 035d677fd8738eb6df5cc3629e225c624de49bdb8f9779573bd67f9c73c6cdcd
- evidence_id: bgc-2297-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: The completed case-sensitive literal scan tested 416 exact cohort tokens
    against eight directly opened implemented curation tables, including ignored files
    and headers, and found zero matches in that bounded scope. Reserved decisions.tsv
    was not consumed.
  snapshot_sha256: 035d677fd8738eb6df5cc3629e225c624de49bdb8f9779573bd67f9c73c6cdcd
- evidence_id: bgc-2297-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[{"last_physical_line":1854,"physical_line":1854,"raw_tsv_record":"BGC0001543\t3\tactive\tquestionable\tunknown\tchejuenolide
    A\t1\tC[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O\tInChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1\tUTURGGMCWRWPTG-YOFHZKFDSA-N\ttrue\t\tnpatlas:NPA015931\tNCBITaxon:158327\tHahella
    chejuensis\tPKS\tUnknown\tHE664023.1\t1\t51429\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:29483632\tENTRY\n","row":{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"chejuenolide
    A","database_ids":"npatlas:NPA015931","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HE664023.1","locus_evidence_methods":"","locus_from":"1","locus_to":"51429","mibig_accession":"BGC0001543","primary_reference":"PMID:29483632","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi":"InChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella
    chejuensis"},"row_sha256":"5beab1a9e1c15967ebb4196c5d8f3a13daa8dd640bae067cde7d03667608834c"}],"predicate":"exact
    complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1854–1854; row_sha256 5beab1a9e1c15967ebb4196c5d8f3a13daa8dd640bae067cde7d03667608834c
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained physical payloads, every field: [{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"chejuenolide
    A","database_ids":"npatlas:NPA015931","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HE664023.1","locus_evidence_methods":"","locus_from":"1","locus_to":"51429","mibig_accession":"BGC0001543","primary_reference":"PMID:29483632","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi":"InChI=1S/C23H33NO4/c1-15-6-10-20(26)12-8-16(2)14-22(24-19(5)25)18(4)23(28)17(3)9-13-21(27)11-7-15/h6-9,11-12,14,18,20-22,26-27H,10,13H2,1-5H3,(H,24,25)/b11-7+,12-8+,15-6+,16-14+,17-9+/t18-,20-,21-,22+/m1/s1","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:158327","taxon_label":"Hahella
    chejuensis"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2297-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[{"last_physical_line":8913,"physical_line":8913,"raw_tsv_record":"UTURGGMCWRWPTG-YOFHZKFDSA-N\tHahella
    chejuensis\tNCBITaxon:158327\thttp://www.wikidata.org/entity/Q21265633\t10.1016/J.TETLET.2008.09.143\thttp://www.wikidata.org/entity/Q77568244\n","row":{"organism_name":"Hahella
    chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1016/J.TETLET.2008.09.143","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"},"row_sha256":"eaea5e133861c2512e6a5f161b6763d7211f8f5c57c7ecb8335e6aebbf255c9f"},{"last_physical_line":8914,"physical_line":8914,"raw_tsv_record":"UTURGGMCWRWPTG-YOFHZKFDSA-N\tHahella
    chejuensis\tNCBITaxon:158327\thttp://www.wikidata.org/entity/Q21265633\t10.1038/S41429-017-0023-X\thttp://www.wikidata.org/entity/Q77568244\n","row":{"organism_name":"Hahella
    chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1038/S41429-017-0023-X","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"},"row_sha256":"42ba8e43ea727f6fb815f2bfc77066aea30c929b95179a49505ce821a4338010"}],"predicate":"exact
    complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 8913–8913; row_sha256 eaea5e133861c2512e6a5f161b6763d7211f8f5c57c7ecb8335e6aebbf255c9f;
    physical lines 8914–8914; row_sha256 42ba8e43ea727f6fb815f2bfc77066aea30c929b95179a49505ce821a4338010
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained physical payloads, every field: [{"organism_name":"Hahella
    chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1016/J.TETLET.2008.09.143","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"},{"organism_name":"Hahella
    chejuensis","organism_wikidata":"http://www.wikidata.org/entity/Q21265633","reference_doi":"10.1038/S41429-017-0023-X","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q77568244","taxon_id":"NCBITaxon:158327"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2297-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[{"last_physical_line":2461,"physical_line":2461,"raw_tsv_record":"UTURGGMCWRWPTG-YOFHZKFDSA-N\tC[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O\tTerpenoids\tDiterpenoids\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","superclass_results":"Diterpenoids"},"row_sha256":"8f2b09fc5001d64763e19e1036b937fb91abbd9ad3a931b438e0bebd8e04790e"}],"predicate":"exact
    complete standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2461–2461; row_sha256 8f2b09fc5001d64763e19e1036b937fb91abbd9ad3a931b438e0bebd8e04790e
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained physical payloads, every field: [{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1[C@@H](NC(C)=O)\\C=C(/C)\\C=C\\[C@H](O)C\\C=C(/C)\\C=C\\[C@@H](O)C\\C=C(C)\\C1=O","standard_inchi_key":"UTURGGMCWRWPTG-YOFHZKFDSA-N","superclass_results":"Diterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2297-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[],"predicate":"exact complete
    standard_inchi_key equality","query":"UTURGGMCWRWPTG-YOFHZKFDSA-N"}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained query frame with literal predicates and all matched
    fields, including no-match results: {"matches":[],"predicate":"exact chebi_id
    from exact full-key structure rows","query":[]}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/source_taxa; /contexts/13/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/13/source_scope_inventory/nonorganism_matches; /contexts/13/source_scope_inventory/actual_assay_rows;
    /contexts/13/source_scope_inventory/blank_AID_sentinels; /contexts/13/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Exact source taxa and route lists; only the forward-merge/nonorganism/assay
    lists are asserted empty where shown: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:158327"]}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/245
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Complete retained source-taxon stanzas; local cache labels and synonyms
    are not fresh authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:158327\nname:
    Hahella chejuensis\n\n","id":"NCBITaxon:158327","physical_line":54382}]'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /records/6/direct_companion_paths; /records/6/direct_companion_predicates
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Exact one-hop contexts/predicates, without transitive identity or claim
    transfer: {"direct_companion_paths":["data/natural_products/terpenoids/chejuenolide-b.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/chejuenolide-b.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001543"]}]}'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230-tentative/bgc-prep/bgc-conditional230-source-inventory-DATA-001.json
  locator: /contexts/14
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: 'Whole direct raw/history/source contexts are retained and already read
    with exact attribution in the source notes. Their full keys and citation roles
    remain distinct: [{"fullkey":"UTURGGMCWRWPTG-PFBVZISFSA-N","identifier":"naturalproductmech:mibig-f2fa461bbb","owned_BGCs":["BGC0001543"],"path":"data/natural_products/terpenoids/chejuenolide-b.yaml"}]'
  snapshot_sha256: 4153fd4a2fff93d8644d4e4d63c614d55c5ef092d02809d2b96d25cf896fdcd7
- evidence_id: bgc-2297-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: ChemicalStructure preserves source representation and explicitly limits
    standardized identity and undefined centres. ComputedClassification is a named/versioned
    prediction, never a source assertion or admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2297-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Maintained extraction derives stereo_complete from FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False)
    and absence of question-mark centre tags; it is not an all-bond-geometry proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2297-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 974–1065
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Maintained seeding preserves the source structure and complete named/versioned
    prediction including is_glycoside, while keeping source BGC classes separately.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2297-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: One-record review requires claim-level evidence and all dimensions, with
    truthful unavailable-check and partial-completion limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2297-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole skill
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: The review procedure does not edit records, and source access must remain
    honestly bounded by the overriding no-request instruction.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2297-congener-structure
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch230/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/7/declared_structure; /records/6/smiles/computed;
    /records/7/smiles/computed
  accessed_at: '2026-11-03T20:54:32.790049Z'
  support: supports
  summary: Both Cheju source-form structures and complete atom tables preserve distinct
    full keys and the R/S difference at SMILES atom 1.
  snapshot_sha256: 96dda81188846db96a060530063819053908a4cfca966a26b040e1263f1c0d1f
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-230/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json
  accessed_at: '2026-11-03T20:29:38.741215Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: a3875b4c9e9c43c34d0c1f5e6ddd8ac7a8e1a6cc41fcc2ea3bc454b6d67b9bb2
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-230/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json
  accessed_at: '2026-11-03T20:30:02.867772Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 6bbb392ff804dc1f5a1158ba06efb5bde54fb2b99ee2b5a2838b751f37839f1c
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-230/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json
  accessed_at: '2026-11-03T20:30:21.827483Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-230/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json
  accessed_at: '2026-11-03T20:30:55.073745Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-230/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-230/native-current230-five-gates-execution-001.json
  accessed_at: '2026-11-03T20:31:06.584669Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: e50a33f59037ecc6b16b3fbc2ccf44aced4fc709d2531e0cf1a41416a1108496
assessments:
- assessment_id: bgc-2297-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted identifier retains UTURGGMCWRWPTG-YOFHZKFDSA-N from BGC0001543
    version 3, compound index 1. The exact retained ChEBI structure join is empty.
    Both saved forms produce C23H33NO4 and the same declared standardized key, while
    the false canonical comparisons remain visible. Chejuenolide B has a different
    full stereochemical key and the opposite configuration at SMILES atom 1; shared
    connectivity and locus do not justify merging them.
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-grounding-owner
  - bgc-2297-source-mibig_compounds
  - bgc-2297-query-chebi_structures
  - bgc-2297-chemistry
  - bgc-2297-direct-contexts
  - bgc-2297-companion-boundaries
  - bgc-2297-congener-structure
  dimensions:
  - name: standard_inchi_key
    value: UTURGGMCWRWPTG-YOFHZKFDSA-N; exact complete retained MIBiG key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2297-grounding-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-query-chebi_structures
    - bgc-2297-chemistry
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
    - bgc-2297-congener-structure
  - name: grounding_scope
    value: MINTED with an exact empty retained ChEBI structure join; natural identity
      is not freshly verified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2297-grounding-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-query-chebi_structures
    - bgc-2297-chemistry
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
    - bgc-2297-congener-structure
- assessment_id: bgc-2297-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: 'Both forms are neutral C23H33NO4 with 28 atoms, 28 bonds and a 17-carbon
    macrocycle. Five E alkenes and four tetrahedral centres are specified in the stored
    form. The original canonical isomeric and nonisomeric SMILES comparisons are false,
    and the diagnostic correspondence is empty. Support''s complete saved-table witness
    maps source N3 to derived N23 with one fewer H and source O6 to O24 with one additional
    H: C4–N3 becomes C18=N23 and C4=O6 becomes C18–O24. Other mapped adjacency, rings
    and retained stereochemistry agree. The mobile-H normalization is consistent with
    an N-acetyl amide becoming an imidic C(O)=N form, which adds an unspecified C=N
    potential element. This narrower manual witness does not replace the original
    empty map or its full_graph_identity_established:false result. The source true
    flag describes its tetrahedral-centre test, not all possible bond geometry.'
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-grounding-owner
  - bgc-2297-chemistry
  - bgc-2297-topology
  - bgc-2297-diagnostic-reading
  - bgc-2297-support-diagnostic-reading
  - bgc-2297-diagnostic-acceptance
  - bgc-2297-structure-schema
  - bgc-2297-stereo-method
  - bgc-2297-congener-structure
  dimensions:
  - name: stereochemistry_scope
    value: Four specified tetrahedral centres and five E alkenes; the InChI-derived
      imidic form adds an unspecified C=N potential element.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2297-grounding-owner
    - bgc-2297-chemistry
    - bgc-2297-topology
    - bgc-2297-diagnostic-reading
    - bgc-2297-support-diagnostic-reading
    - bgc-2297-diagnostic-acceptance
    - bgc-2297-structure-schema
    - bgc-2297-stereo-method
    - bgc-2297-congener-structure
  - name: representation_correspondence
    value: Eight true and two false canonical comparisons; original atom map empty/full_graph_identity
      false. Separately attributed saved-row amide–imidic witness is narrower.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2297-grounding-owner
    - bgc-2297-chemistry
    - bgc-2297-topology
    - bgc-2297-diagnostic-reading
    - bgc-2297-support-diagnostic-reading
    - bgc-2297-diagnostic-acceptance
    - bgc-2297-structure-schema
    - bgc-2297-stereo-method
    - bgc-2297-congener-structure
- assessment_id: bgc-2297-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: The retained BGC0001543 version 3 entry is active, questionable quality
    and unknown completeness. Hahella chejuensis (158327) is a SOURCE_ASSERTION producer;
    no locus method is stated, and the locus is CLUSTER_UNSTATED. The source interval
    HE664023.1:1–51429 and the matching cached species label are preserved. Species-level
    LOTUS occurrence claims do not upgrade the producer or locus grade.
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-origin-owner
  - bgc-2297-source-mibig_compounds
  - bgc-2297-cached-taxonomy
  - bgc-2297-source-routes
  - bgc-2297-direct-contexts
  - bgc-2297-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: Hahella chejuensis 158327 producer assertion and two occurrence citations
      remain separate.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2297-origin-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-cached-taxonomy
    - bgc-2297-source-routes
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
  - name: producer_evidence
    value: SOURCE_ASSERTION, MIBiG version 3; no upgrade from occurrence rows.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2297-origin-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-cached-taxonomy
    - bgc-2297-source-routes
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
  - name: locus_evidence
    value: BGC0001543 v3 active/questionable/unknown; no stated method, CLUSTER_UNSTATED.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2297-origin-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-cached-taxonomy
    - bgc-2297-source-routes
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
- assessment_id: bgc-2297-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: ENTRY-level PMID:29483632 is reused in the producer and locus database
    assertions. Two LOTUS rows cite DOI:10.1016/J.TETLET.2008.09.143 and DOI:10.1038/S41429-017-0023-X.
    Their relationship to the PMID and their experimental independence were not freshly
    verified. The B congener's shared locus and one shared DOI do not transfer identity,
    activity or mechanism.
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-origin-owner
  - bgc-2297-occurrence-owner
  - bgc-2297-source-mibig_compounds
  - bgc-2297-source-lotus_occurrences
  - bgc-2297-source-notes
  - bgc-2297-direct-contexts
  - bgc-2297-companion-boundaries
  dimensions:
  - name: citation_scope
    value: ENTRY PMID plus two literal LOTUS DOI placements; no publication-independence
      inference.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2297-origin-owner
    - bgc-2297-occurrence-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-source-lotus_occurrences
    - bgc-2297-source-notes
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
- assessment_id: bgc-2297-bioactivity
  area: evidence
  topic: Occurrence and activity
  outcome: supported
  summary: Two retained LOTUS assertions name Hahella chejuensis (158327); these are
    two citation placements, not two proven independent production studies. The complete
    owner has no written assay, activity summary, target or mechanism roots. Exact
    saved PubChem, BindingDB, AntibioticMech, ChEBI-origin and CyanometDB joins are
    empty. No biological inactivity or global absence claim follows.
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-occurrence-owner
  - bgc-2297-assay-owner
  - bgc-2297-source-routes
  - bgc-2297-cached-taxonomy
  - bgc-2297-query-lotus_occurrences
  - bgc-2297-query-chebi_origins
  - bgc-2297-query-cyanometdb_occurrences
  - bgc-2297-query-pubchem_bioassay
  - bgc-2297-query-bindingdb_targets
  - bgc-2297-query-antibioticmech_inchikeys
  - bgc-2297-direct-contexts
  - bgc-2297-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: Two species-level LOTUS citations, not two established producer experiments.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2297-occurrence-owner
    - bgc-2297-assay-owner
    - bgc-2297-source-routes
    - bgc-2297-cached-taxonomy
    - bgc-2297-query-lotus_occurrences
    - bgc-2297-query-chebi_origins
    - bgc-2297-query-cyanometdb_occurrences
    - bgc-2297-query-pubchem_bioassay
    - bgc-2297-query-bindingdb_targets
    - bgc-2297-query-antibioticmech_inchikeys
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
  - name: assay_target_scope
    value: No written assay/target and bounded empty saved activity routes; no inactivity
      conclusion.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2297-occurrence-owner
    - bgc-2297-assay-owner
    - bgc-2297-source-routes
    - bgc-2297-cached-taxonomy
    - bgc-2297-query-lotus_occurrences
    - bgc-2297-query-chebi_origins
    - bgc-2297-query-cyanometdb_occurrences
    - bgc-2297-query-pubchem_bioassay
    - bgc-2297-query-bindingdb_targets
    - bgc-2297-query-antibioticmech_inchikeys
    - bgc-2297-direct-contexts
    - bgc-2297-companion-boundaries
- assessment_id: bgc-2297-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: The source BGC class is PKS, whereas NPClassifier npclassifier.gnps2.org@2026-09-07
    reports Terpenoids / Diterpenoids with an empty class list and is_glycoside:false.
    Those are distinct source and computed axes. The stored macrocycle contains an
    N-acetyl amide, a ketone and hydroxyl substituents, not an ester ring established
    by the name suffix. No carbohydrate residue is established by the complete graph.
    The model label does not independently prove a terpene biosynthetic origin or
    invalidate the retained PKS source; no automatic filing or identity correction
    is warranted.
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-classification-owner
  - bgc-2297-source-mibig_compounds
  - bgc-2297-source-npclassifier
  - bgc-2297-chemistry
  - bgc-2297-topology
  - bgc-2297-diagnostic-reading
  - bgc-2297-support-diagnostic-reading
  - bgc-2297-structure-schema
  - bgc-2297-classification-seeder
  dimensions:
  - name: classification_applicability
    value: PKS source class and versioned Terpenoids/Diterpenoids prediction are separate;
      neither name suffix nor model proves an ester ring or pathway.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2297-classification-owner
    - bgc-2297-source-mibig_compounds
    - bgc-2297-source-npclassifier
    - bgc-2297-chemistry
    - bgc-2297-topology
    - bgc-2297-diagnostic-reading
    - bgc-2297-support-diagnostic-reading
    - bgc-2297-structure-schema
    - bgc-2297-classification-seeder
- assessment_id: bgc-2297-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed against complete current
    owner/history, actual canonical intake, retained source payloads and the attributed
    complete saved molecular tables. The five original local commands passed, while
    full QC, complete OAK authority coverage and fresh external verification remain
    unavailable. No mechanism root or reader is applicable to this owner. The completed
    eight-table curation scan found no matching exact cohort token within its declared
    ignore-independent scope. No supported new source correction is established; scientific
    completion remains partial and native curation status is unchanged.
  target_ids:
  - naturalproductmech:mibig-24b010d9e9
  evidence_ids:
  - bgc-2297-owner
  - bgc-2297-intake
  - bgc-2297-intake-acceptance
  - bgc-2297-inventory-acceptance
  - bgc-2297-plan
  - bgc-2297-plan-acceptance
  - bgc-2297-source-notes
  - bgc-2297-curation-scope
  - bgc-2297-diagnostic-execution
  - bgc-2297-diagnostic-acceptance
  - bgc-2297-native-acceptance
  - bgc-2297-review-profile
  - bgc-2297-review-skill
  dimensions:
  - name: review_completion
    value: Partial scientific review; retained source fidelity and saved representations
      assessed, with natural identity/primary verification and full QC/OAK unresolved.
      No record edit or curation-status promotion.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2297-owner
    - bgc-2297-intake
    - bgc-2297-intake-acceptance
    - bgc-2297-inventory-acceptance
    - bgc-2297-plan
    - bgc-2297-plan-acceptance
    - bgc-2297-source-notes
    - bgc-2297-curation-scope
    - bgc-2297-diagnostic-execution
    - bgc-2297-diagnostic-acceptance
    - bgc-2297-native-acceptance
    - bgc-2297-review-profile
    - bgc-2297-review-skill
findings: []
actions: []
limitations:
- All evidence is retained locally; external identifiers, primary publications, taxonomy,
  accessions and natural stereochemical assignments were not refreshed under the absolute
  no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates
  and parsed representations establish only their stated mechanical scope.
- Empty joins concern only the exact saved predicates and snapshots. Shared loci,
  taxa and citations do not transfer compound-specific activity, production, mechanism
  or independent-study status.
- The two original undefined-stereo warnings remain global and unassigned. No additional
  molecular/YAML parse, source query or target invocation occurred during this scientific
  authoring.
- The review proposes no source-record, native-status or history edit; any later correction
  belongs to the exact maintained owners listed in the accepted intake.
- The manual saved-table amide–imidic witness does not establish exact-form identity
  and does not overwrite the original false comparisons or empty correspondence.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and actual intake have been read; whole-source and exact
  companion carries are attributed in the pinned notes.
- BGC personally interpreted the Calidoustene B/C molecular tables; Support personally
  interpreted the complete later-five tables and exact Cheju witness. The combined
  reading note preserves this attribution.
- ROOT executed the original collector, composer, capture, canonical intakes and chemistry;
  Native executed the five original local gates. No new target was invoked for these
  six assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-230
```
