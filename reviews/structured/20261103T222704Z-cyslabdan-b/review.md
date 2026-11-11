# Local evidence review: cyslabdan B

- Review: 20261103T222704Z-cyslabdan-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T21:43:37.810799Z
- Finished UTC: 2026-11-03T22:27:04.921412Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Cyslabdan B preserves source identity and claim scope while its saved amide/imidic representation difference remains explicit. Cyslabdan A mechanism claims do not transfer; scientific completion is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2310; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-826d2ff0d3 | data/natural_products/terpenoids/cyslabdan-b.yaml | generated | cyslabdan B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-826d2ff0d3 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-826d2ff0d3 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-826d2ff0d3 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-826d2ff0d3 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-826d2ff0d3 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-826d2ff0d3 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-826d2ff0d3 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-826d2ff0d3 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-826d2ff0d3.

The minted identifier preserves complete key MTFOIHQNFFXXRF-XXBLPORFSA-N and source name cyslabdan B from BGC0001910 version 4, compound index 2. No exact retained ChEBI structure row joins it. Cyslabdan A and C have distinct full keys and retain separate identity, activity and mechanism scope.

### Representation

representation: supported. Targets: naturalproductmech:mibig-826d2ff0d3.

Both forms are neutral C25H41NO6S with 33 atoms and 34 bonds, two six-carbon rings, a terminal alkene, one E alkene, three scaffold hydroxyls, a sulfur bridge and an N-acetylcysteine-like substituent. Seven specified tetrahedral centres retain corresponding CIP labels. The stored SMILES has N26–C27(=O29), whereas the InChI-decoded form has N25=C15–O26: nitrogen loses one hydrogen and oxygen gains one. This is a local amide/imidic mobile-H representation difference, with an additional unspecified C=N geometry only in the decoded form. Formula, charge, standard InChI and full key agree, but both canonical SMILES comparisons are false and the diagnostic atom map is empty; complete_atom_count_match and full_graph_identity_established remain false. The true source stereo flag is the maintained tetrahedral-centre diagnostic, not blanket proof of every derived double-bond geometry.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-826d2ff0d3.

Streptomyces cyslabdanicus NCBITaxon:1470456 is a SOURCE_ASSERTION producer under active BGC0001910 version 4, whose retained quality is questionable and completeness unknown. There is no stated locus method and the link remains CLUSTER_UNSTATED. Streptomyces avermitilis NCBITaxon:33903 is a separate LOTUS occurrence; the retained heterologous-host context is not evidence that it is the native producer.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-826d2ff0d3.

DOI:10.1007/s10295-015-1694-6 is retained at COMPOUND_EVIDENCE level, while LOTUS preserves the case-different string DOI:10.1007/S10295-015-1694-6. These are not two independent publications or production experiments. Cyslabdan A's historical Mca assertion concerns A and cannot be transferred to B from this shared citation/locus.

### Occurrence and activity

evidence: supported. Targets: naturalproductmech:mibig-826d2ff0d3.

One Streptomyces avermitilis occurrence is written, with no activity or target. The exact saved assay/target joins for B are empty. Neither the occurrence nor Cyslabdan A's terminal Mca mechanism supplies a B-specific enzyme, assay or biological outcome.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-826d2ff0d3.

The source Diterpenoid compound class and Diterpene cluster subclass are distinct from NPClassifier's Terpenoids / Diterpenoids / Labdane diterpenoids prediction and is_glycoside:false. Total C25 alone is not a contradiction: the represented nitrogen/sulfur-containing conjugate must be assessed at scaffold and substituent level. The model does not establish a complete pathway. The saved two-ring carbon framework is attached through sulfur to a five-carbon nitrogen-containing substituent, making scaffold-level Diterpenoids compatible with total C25. Neither saved graph establishes a carbohydrate residue or glycosidic linkage.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-826d2ff0d3.

All twelve scientific dimensions were assessed against the complete current owner/history, actual canonical intake, retained source payloads and complete saved paired molecular tables. Five original local gates passed, but full QC, complete OAK authority coverage and fresh external verification remain unavailable. This owner has no mechanism root or selected reader. The bounded eight-table curation scan found no exact cohort-token match; no supported new maintained-source correction is established. Scientific completion remains partial and native curation status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2310-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/cyslabdan-b.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner with all 2 history entries. The complete plaintext reading is attributed in source notes; native curation_status remains SEEDED. |
| bgc-2310-capture | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/9 | supports | Complete captured owner retains every written field and history; no mechanism root or component is present for this owner. |
| bgc-2310-intake | /private/tmp/npm-review-work/shared-next-batch231/intakes/2310-inspect-001.json; /status; /repository; /source; /targets | supports | Actual one-record canonical intake for naturalproductmech:mibig-826d2ff0d3; 39 pinned input placements and explicit maintained source ownership. |
| bgc-2310-grounding-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"chemical_structure":{"smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi":"InChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001910"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-826d2ff0d3","label":"cyslabdan B","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-826d2ff0d3","source":"MIBIG","source_id":"BGC0001910","source_label":"cyslabdan B","source_version":"4"}],"xrefs":["npatlas:NPA002918"]} |
| bgc-2310-origin-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001910","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"4","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"genome_accession":"genbank:LC064028.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Streptomyces cyslabdanicus","organism_taxon_id":"NCBITaxon:1470456"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001910","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"4","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus"}],"producer_taxon_groups":["ACTINOBACTERIAL"]} |
| bgc-2310-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"occurrence_taxon_groups":["ACTINOBACTERIAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1007/S10295-015-1694-6"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1946562","source":"LOTUS","taxon_id":"NCBITaxon:33903","taxon_label":"Streptomyces avermitilis","taxon_source":"NCBITaxon"}]} |
| bgc-2310-assay-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {} |
| bgc-2310-classification-owner | /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete written field projection, with absent fields bounded by the complete captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Diterpenoid"],"np_classification":{"class_results":["Labdane diterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2310-chemistry | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/smiles/status; /records/9/inchi/status; /records/9/smiles/computed; /records/9/inchi/computed; /records/9/comparisons; /records/9/atom_correspondence | supports | Both stored forms parsed. Exact original comparison and correspondence values: {"atom_correspondence":{"complete_atom_count_match":false,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":false,"canonical_nonisomeric_smiles_equal":false,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":7,"Bond_Double:Specified":1,"Bond_Double:Unspecified":1},"smiles_stereo":{"Atom_Tetrahedral:Specified":7,"Bond_Double:Specified":1}} |
| bgc-2310-topology | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed; /records/9/inchi/computed; /records/9/declared_structure; /records/9/comparisons; /records/9/atom_correspondence | supports | Both forms are neutral C25H41NO6S with 33 atoms and 34 bonds, two six-carbon rings, a terminal alkene, one E alkene, three scaffold hydroxyls, a sulfur bridge and an N-acetylcysteine-like substituent. Seven specified tetrahedral centres retain corresponding CIP labels. The stored SMILES has N26–C27(=O29), whereas the InChI-decoded form has N25=C15–O26: nitrogen loses one hydrogen and oxygen gains one. This is a local amide/imidic mobile-H representation difference, with an additional unspecified C=N geometry only in the decoded form. Formula, charge, standard InChI and full key agree, but both canonical SMILES comparisons are false and the diagnostic atom map is empty; complete_atom_count_match and full_graph_identity_established remain false. |
| bgc-2310-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | Native operated one original stored-form diagnostic, exit 0, with preserved stdout/stderr and closed environment. The inherited DATA observer literal is not the operator attribution. |
| bgc-2310-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-chemistry-acceptance-001.json; Whole ROOT chemistry acceptance | supports | ROOT accepts the original 20 stored parses and retains 96 true/four false flags, two empty maps and four global unassigned warnings; it establishes no natural identity or fixed-graph equivalence. |
| bgc-2310-native-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-native-gates-acceptance-001.json; Whole ROOT gate acceptance and selected queue rows | supports | Five original local gates passed; all_native_gates_passed is false because full QC and complete OAK remain unavailable. Selected queues are follow-up context, not automatic scientific findings. |
| bgc-2310-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-intake-acceptance-001.json; Whole ROOT intake acceptance | supports | ROOT accepts ten actual one-record intakes, 411 source placements / 68 paths and exact ownership; no scientific verdict follows from intake success. |
| bgc-2310-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-source-inventory-acceptance-001.json; Whole ROOT source-inventory acceptance | supports | ROOT accepts the one original local inventory and its current input/capture/source joins; complete scientific reading is separately attributed in the notes. |
| bgc-2310-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch231/root-input-plan-acceptance-001.json; Whole ROOT input-plan acceptance | supports | ROOT accepts the exact current plan and preserved source contexts; no scientific verdict or future reader success is inferred. |
| bgc-2310-plan | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-target-input-plan-001.json; /records/9 | supports | Current one-record input plan with direct companions, retained source predicates and input roles. |
| bgc-2310-source-notes | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading attribution and bounded compound-specific cautions; no pre-intake verdict was asserted. |
| bgc-2310-curation-scope | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json; /curation | supports | Eight current pinned implemented curation tables were directly opened ignoring ignore rules; 101 exact case-sensitive cohort literals against 93 data rows yielded zero matches within that scope. Reserved decisions.tsv was not consumed. |
| bgc-2310-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[{"last_physical_line":2234,"physical_line":2234,"raw_tsv_record":"BGC0001910\t4\tactive\tquestionable\tunknown\tcyslabdan B\t2\tC=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O\tInChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1\tMTFOIHQNFFXXRF-XXBLPORFSA-N\ttrue\tDiterpenoid\tnpatlas:NPA002918\tNCBITaxon:1470456\tStreptomyces cyslabdanicus\tterpene\tDiterpene\tLC064028.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1007/s10295-015-1694-6\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"2","compound_name":"cyslabdan B","database_ids":"npatlas:NPA002918","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi":"InChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus"},"row_sha256":"9f8a91e23dfc30e506271c23aa6fee6e60266d52e592abb66dc842f0bbe06545"}],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2234–2234, row_sha256 9f8a91e23dfc30e506271c23aa6fee6e60266d52e592abb66dc842f0bbe06545 | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"2","compound_name":"cyslabdan B","database_ids":"npatlas:NPA002918","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi":"InChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces cyslabdanicus"}] |
| bgc-2310-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[{"last_physical_line":5758,"physical_line":5758,"raw_tsv_record":"MTFOIHQNFFXXRF-XXBLPORFSA-N\tStreptomyces avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1007/S10295-015-1694-6\thttp://www.wikidata.org/entity/Q110171277\n","row":{"organism_name":"Streptomyces avermitilis","organism_wikidata":"http://www.wikidata.org/entity/Q1946562","reference_doi":"10.1007/S10295-015-1694-6","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q110171277","taxon_id":"NCBITaxon:33903"},"row_sha256":"3b0f04b1b8d1e41b1a918a081bb2e85fdc6fb7fa6bdf4a3a2c5528053ba687ec"}],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 5758–5758, row_sha256 3b0f04b1b8d1e41b1a918a081bb2e85fdc6fb7fa6bdf4a3a2c5528053ba687ec | supports | Complete retained physical row payloads, every field: [{"organism_name":"Streptomyces avermitilis","organism_wikidata":"http://www.wikidata.org/entity/Q1946562","reference_doi":"10.1007/S10295-015-1694-6","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q110171277","taxon_id":"NCBITaxon:33903"}] |
| bgc-2310-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[{"last_physical_line":1531,"physical_line":1531,"raw_tsv_record":"MTFOIHQNFFXXRF-XXBLPORFSA-N\tC=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O\tTerpenoids\tDiterpenoids\tLabdane diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Labdane diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","superclass_results":"Diterpenoids"},"row_sha256":"6ab11fc7dc3f0b2563079ab89860cb02c35e9bf72ea0fff75e5853a5237c3867"}],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1531–1531, row_sha256 6ab11fc7dc3f0b2563079ab89860cb02c35e9bf72ea0fff75e5853a5237c3867 | supports | Complete retained physical row payloads, every field: [{"class_results":"Labdane diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","superclass_results":"Diterpenoids"}] |
| bgc-2310-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"} |
| bgc-2310-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, including the exact predicate and no-match result where empty: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2310-source-routes | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/21/source_scope_inventory/source_taxa; /contexts/21/source_scope_inventory/forward_taxon_merge_matches; /contexts/21/source_scope_inventory/nonorganism_matches; /contexts/21/source_scope_inventory/actual_assay_rows; /contexts/21/source_scope_inventory/blank_AID_sentinels; /contexts/21/source_scope_inventory/related_corpus_rows | supports | Exact source-taxon and route lists; only the forward-merge/nonorganism lists are empty cohortwide, and assay/sentinel outcomes retain their exact values: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:1470456","NCBITaxon:33903"]} |
| bgc-2310-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/30 | supports | Complete retained relevant stanzas; cached labels/synonyms are not fresh external authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:33903\nname: Streptomyces avermitilis\nsynonym: \"Streptomyces avermectinius\" EXACT []\n\n","id":"NCBITaxon:33903","physical_line":14687},{"complete_stanza":"[Term]\nid: NCBITaxon:1470456\nname: Streptomyces cyslabdanicus\n\n","id":"NCBITaxon:1470456","physical_line":130135}] |
| bgc-2310-direct-contexts | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /records/9/direct_companion_paths; /records/9/direct_companion_predicates | supports | Exact one-hop scope without claim transfer: {"direct_companion_paths":["data/natural_products/terpenoids/cyslabdan-a.yaml","data/natural_products/terpenoids/cyslabdan-c.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/cyslabdan-a.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]},{"path":"data/natural_products/terpenoids/cyslabdan-c.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]}]} |
| bgc-2310-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json; /contexts/20; /contexts/22 | supports | Whole raw/history/source contexts were read with exact attribution in the notes; full keys and citation roles remain distinct: [{"fullkey":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","identifier":"naturalproductmech:mibig-f3cb15d2b6","mechanism_roots":["causal_graphs","biosynthetic_pathway"],"owned_BGCs":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-a.yaml"},{"fullkey":"PTRRHQHGAOYEKT-KYXZTKSHSA-N","identifier":"naturalproductmech:mibig-04c341bc33","mechanism_roots":[],"owned_BGCs":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-c.yaml"}] |
| bgc-2310-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure preserves source representation and standardized-key limitations. stereo_complete describes undefined centres; ComputedClassification is a named/versioned prediction, never a source assertion or admission criterion. |
| bgc-2310-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and the absence of question-mark centre tags; it is not a blanket all-bond-geometry proof. |
| bgc-2310-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 974–1065 | supports | Maintained seeding preserves the source structure and named/versioned classifier output while separately retaining BGC and source compound classes. |
| bgc-2310-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record scientific review requires claim-level evidence and twelve dimensions with truthful partial-completion/unavailable-check limits. |
| bgc-2310-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit records; source access is bounded by the overriding no-request instruction. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-231/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-231/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-231/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-231/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-231/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. External identifiers, primary publications, taxonomy and natural stereochemical assignments were not refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates and successful stored parses establish only their stated mechanical scope.
- Empty joins concern only exact saved predicates and snapshots. Shared loci, taxa and citations do not transfer compound-specific production, activity, mechanism or independent-study status.
- Four original undefined-stereo warnings remain global and unassigned to records. No additional molecular/YAML parse, source query or target invocation occurred during scientific authoring.
- No source record, native curation status or history is edited. Any later correction belongs to the maintained owners listed in the accepted canonical intake.
- The amide/imidic local witness explains the canonical-form difference without replacing the original empty atom map, claiming exact fixed-graph identity, or assigning the added imidic double-bond geometry.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual canonical intake were read; all matching source payload and companion reading/carry attribution is retained in the pinned source notes.
- BGC personally read all fourteen saved molecular forms for these seven owners: 342 atom rows and 362 bond rows plus every scalar, stereo/ring/motif table and original comparison/map.
- ROOT operated original activation/capture; Support operated original canonical intakes; Native operated original gates and chemistry; BGC operated the admitted original collector/composer. No new target was invoked for these assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T222704Z-cyslabdan-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: cyslabdan B'
started_at: '2026-11-03T21:43:37.810799Z'
finished_at: '2026-11-03T22:27:04.921412Z'
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
summary: Cyslabdan B preserves source identity and claim scope while its saved amide/imidic
  representation difference remains explicit. Cyslabdan A mechanism claims do not
  transfer; scientific completion is partial.
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
  - path: data/natural_products/terpenoids/cyslabdan-a.yaml
    sha256: 49f630e192b2c029fccafb33e4506b0c4f6c2dc4786b2df278887c8cae21f5ae
    role: context
  - path: data/natural_products/terpenoids/cyslabdan-b.yaml
    sha256: d505c35b58d2eb17171996ca53704aedfbb0fd7a2db369f9e761ac3197ed12df
    role: target
  - path: data/natural_products/terpenoids/cyslabdan-c.yaml
    sha256: 6ab0f6ad6f58fd49b40cd8f0243a743d9d5f8e06d1f7f9c0adfd77c8e254a42a
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
  selection: Campaign path order 2310; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-826d2ff0d3
targets:
- target_id: naturalproductmech:mibig-826d2ff0d3
  path: data/natural_products/terpenoids/cyslabdan-b.yaml
  label: cyslabdan B
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
  - naturalproductmech:mibig-826d2ff0d3
  command: just validate-strict data/natural_products/terpenoids/compound-12.yaml
    data/natural_products/terpenoids/compound-15.yaml data/natural_products/terpenoids/compound-7a.yaml
    data/natural_products/terpenoids/conidiogenone.yaml data/natural_products/terpenoids/cucurbitacin-c.yaml
    data/natural_products/terpenoids/culmorin.yaml data/natural_products/terpenoids/cyatha-3-12-diene.yaml
    data/natural_products/terpenoids/cyclooctatin.yaml data/natural_products/terpenoids/cyslabdan-a.yaml
    data/natural_products/terpenoids/cyslabdan-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-231/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-826d2ff0d3
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-231/validate-all-001.tsv
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
  - naturalproductmech:mibig-826d2ff0d3
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
  - naturalproductmech:mibig-826d2ff0d3
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
  - naturalproductmech:mibig-826d2ff0d3
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-231/review-queue-001.tsv
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
  - naturalproductmech:mibig-826d2ff0d3
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2310-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/cyslabdan-b.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Complete current owner with all 2 history entries. The complete plaintext
    reading is attributed in source notes; native curation_status remains SEEDED.
  snapshot_sha256: d505c35b58d2eb17171996ca53704aedfbb0fd7a2db369f9e761ac3197ed12df
- evidence_id: bgc-2310-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/9
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Complete captured owner retains every written field and history; no mechanism
    root or component is present for this owner.
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: bgc-2310-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/intakes/2310-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Actual one-record canonical intake for naturalproductmech:mibig-826d2ff0d3;
    39 pinned input placements and explicit maintained source ownership.
  snapshot_sha256: 70da6d4cbf31ad62a3517da20f546896a02c0594ce8c4c9d1187a1303b4b8e6a
- evidence_id: bgc-2310-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi":"InChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001910"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-826d2ff0d3","label":"cyslabdan
    B","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-826d2ff0d3","source":"MIBIG","source_id":"BGC0001910","source_label":"cyslabdan
    B","source_version":"4"}],"xrefs":["npatlas:NPA002918"]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: bgc-2310-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001910","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"4","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"genome_accession":"genbank:LC064028.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Streptomyces
    cyslabdanicus","organism_taxon_id":"NCBITaxon:1470456"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001910","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001910 entry version 4; citation taken from the compound evidence level","reference":"DOI:10.1007/s10295-015-1694-6"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"4","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus"}],"producer_taxon_groups":["ACTINOBACTERIAL"]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: bgc-2310-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"occurrence_taxon_groups":["ACTINOBACTERIAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1007/S10295-015-1694-6"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1946562","source":"LOTUS","taxon_id":"NCBITaxon:33903","taxon_label":"Streptomyces
    avermitilis","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: bgc-2310-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: bgc-2310-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete written field projection, with absent fields bounded by the complete
    captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Diterpenoid"],"np_classification":{"class_results":["Labdane
    diterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Diterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: d84d66f3894eb1e6982ca23b38ceb3de84e6f7ca4b5c805ae0f4271536420af7
- evidence_id: bgc-2310-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/smiles/status; /records/9/inchi/status;
    /records/9/smiles/computed; /records/9/inchi/computed; /records/9/comparisons;
    /records/9/atom_correspondence
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison and correspondence
    values: {"atom_correspondence":{"complete_atom_count_match":false,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":false,"canonical_nonisomeric_smiles_equal":false,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":7,"Bond_Double:Specified":1,"Bond_Double:Unspecified":1},"smiles_stereo":{"Atom_Tetrahedral:Specified":7,"Bond_Double:Specified":1}}'
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: bgc-2310-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed; /records/9/inchi/computed; /records/9/declared_structure;
    /records/9/comparisons; /records/9/atom_correspondence
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Both forms are neutral C25H41NO6S with 33 atoms and 34 bonds, two six-carbon
    rings, a terminal alkene, one E alkene, three scaffold hydroxyls, a sulfur bridge
    and an N-acetylcysteine-like substituent. Seven specified tetrahedral centres
    retain corresponding CIP labels. The stored SMILES has N26–C27(=O29), whereas
    the InChI-decoded form has N25=C15–O26: nitrogen loses one hydrogen and oxygen
    gains one. This is a local amide/imidic mobile-H representation difference, with
    an additional unspecified C=N geometry only in the decoded form. Formula, charge,
    standard InChI and full key agree, but both canonical SMILES comparisons are false
    and the diagnostic atom map is empty; complete_atom_count_match and full_graph_identity_established
    remain false.'
  snapshot_sha256: 5696325ae03369015ee813b99d1d51da767e934b2ac887dd9e29f2c27d0405bf
- evidence_id: bgc-2310-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Native operated one original stored-form diagnostic, exit 0, with preserved
    stdout/stderr and closed environment. The inherited DATA observer literal is not
    the operator attribution.
  snapshot_sha256: 65040543ad69a2d54b0cf784884a78bf49a7bf1c68cdec31272f1ada872be8db
- evidence_id: bgc-2310-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-chemistry-acceptance-001.json
  locator: Whole ROOT chemistry acceptance
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses and retains 96 true/four false
    flags, two empty maps and four global unassigned warnings; it establishes no natural
    identity or fixed-graph equivalence.
  snapshot_sha256: 129083683fbfc7528e17bfe7fcd04e7ceb7e44708a11682d024e10f384d5c740
- evidence_id: bgc-2310-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-native-gates-acceptance-001.json
  locator: Whole ROOT gate acceptance and selected queue rows
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Five original local gates passed; all_native_gates_passed is false because
    full QC and complete OAK remain unavailable. Selected queues are follow-up context,
    not automatic scientific findings.
  snapshot_sha256: b7921dc6afa5d8ce9587a5a097e427772c0b5b739481a22f8e61ce9bcb9e78cc
- evidence_id: bgc-2310-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-intake-acceptance-001.json
  locator: Whole ROOT intake acceptance
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: ROOT accepts ten actual one-record intakes, 411 source placements / 68
    paths and exact ownership; no scientific verdict follows from intake success.
  snapshot_sha256: af10db4855db731afb28ba6c9d972835e1c1689b3b6089b80d9ed7a76dd1118f
- evidence_id: bgc-2310-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-source-inventory-acceptance-001.json
  locator: Whole ROOT source-inventory acceptance
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: ROOT accepts the one original local inventory and its current input/capture/source
    joins; complete scientific reading is separately attributed in the notes.
  snapshot_sha256: a50f4decab71502d06fc10d04836ee324c2b09c0fdf118ea5826e7e7c4640d03
- evidence_id: bgc-2310-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231/root-input-plan-acceptance-001.json
  locator: Whole ROOT input-plan acceptance
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: ROOT accepts the exact current plan and preserved source contexts; no scientific
    verdict or future reader success is inferred.
  snapshot_sha256: 2f7c566f713e12b9b357d9e9c870cb6c05ee90ca30a53c0879a5e5d6a547fa6f
- evidence_id: bgc-2310-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-target-input-plan-001.json
  locator: /records/9
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Current one-record input plan with direct companions, retained source predicates
    and input roles.
  snapshot_sha256: 641feb36d59176354fbea2afb95ff2e5d7c1ea3253b71291ca442c15482dab14
- evidence_id: bgc-2310-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Complete disjoint source/raw-history reading attribution and bounded compound-specific
    cautions; no pre-intake verdict was asserted.
  snapshot_sha256: c178e2f5d22e7bf22457f90632cb8bd1b05ce4caf2a993684e4a357a81188afd
- evidence_id: bgc-2310-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Eight current pinned implemented curation tables were directly opened ignoring
    ignore rules; 101 exact case-sensitive cohort literals against 93 data rows yielded
    zero matches within that scope. Reserved decisions.tsv was not consumed.
  snapshot_sha256: c178e2f5d22e7bf22457f90632cb8bd1b05ce4caf2a993684e4a357a81188afd
- evidence_id: bgc-2310-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[{"last_physical_line":2234,"physical_line":2234,"raw_tsv_record":"BGC0001910\t4\tactive\tquestionable\tunknown\tcyslabdan
    B\t2\tC=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O\tInChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1\tMTFOIHQNFFXXRF-XXBLPORFSA-N\ttrue\tDiterpenoid\tnpatlas:NPA002918\tNCBITaxon:1470456\tStreptomyces
    cyslabdanicus\tterpene\tDiterpene\tLC064028.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1007/s10295-015-1694-6\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"2","compound_name":"cyslabdan
    B","database_ids":"npatlas:NPA002918","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi":"InChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus"},"row_sha256":"9f8a91e23dfc30e506271c23aa6fee6e60266d52e592abb66dc842f0bbe06545"}],"predicate":"exact
    complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2234–2234, row_sha256 9f8a91e23dfc30e506271c23aa6fee6e60266d52e592abb66dc842f0bbe06545
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Diterpene","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Diterpenoid","compound_index":"2","compound_name":"cyslabdan
    B","database_ids":"npatlas:NPA002918","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"LC064028.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001910","primary_reference":"DOI:10.1007/s10295-015-1694-6","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi":"InChI=1S/C25H41NO6S/c1-7-15(2)9-10-18-24(6)12-8-11-23(4,5)19(24)13-20(28)25(18,32)22(31)33-14-17(21(29)30)26-16(3)27/h7,9,17-20,22,28,31-32H,1,8,10-14H2,2-6H3,(H,26,27)(H,29,30)/b15-9+/t17-,18+,19-,20-,22-,24+,25+/m0/s1","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1470456","taxon_label":"Streptomyces
    cyslabdanicus"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2310-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key
    equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[{"last_physical_line":5758,"physical_line":5758,"raw_tsv_record":"MTFOIHQNFFXXRF-XXBLPORFSA-N\tStreptomyces
    avermitilis\tNCBITaxon:33903\thttp://www.wikidata.org/entity/Q1946562\t10.1007/S10295-015-1694-6\thttp://www.wikidata.org/entity/Q110171277\n","row":{"organism_name":"Streptomyces
    avermitilis","organism_wikidata":"http://www.wikidata.org/entity/Q1946562","reference_doi":"10.1007/S10295-015-1694-6","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q110171277","taxon_id":"NCBITaxon:33903"},"row_sha256":"3b0f04b1b8d1e41b1a918a081bb2e85fdc6fb7fa6bdf4a3a2c5528053ba687ec"}],"predicate":"exact
    complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 5758–5758, row_sha256 3b0f04b1b8d1e41b1a918a081bb2e85fdc6fb7fa6bdf4a3a2c5528053ba687ec
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"organism_name":"Streptomyces
    avermitilis","organism_wikidata":"http://www.wikidata.org/entity/Q1946562","reference_doi":"10.1007/S10295-015-1694-6","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q110171277","taxon_id":"NCBITaxon:33903"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2310-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key
    equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[{"last_physical_line":1531,"physical_line":1531,"raw_tsv_record":"MTFOIHQNFFXXRF-XXBLPORFSA-N\tC=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O\tTerpenoids\tDiterpenoids\tLabdane
    diterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Labdane
    diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","superclass_results":"Diterpenoids"},"row_sha256":"6ab11fc7dc3f0b2563079ab89860cb02c35e9bf72ea0fff75e5853a5237c3867"}],"predicate":"exact
    complete standard_inchi_key equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1531–1531, row_sha256 6ab11fc7dc3f0b2563079ab89860cb02c35e9bf72ea0fff75e5853a5237c3867
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"Labdane
    diterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C=C/C(C)=C/C[C@@H]1[C@@]2(C)CCCC(C)(C)[C@@H]2C[C@H](O)[C@@]1(O)[C@@H](O)SC[C@H](NC(C)=O)C(=O)O","standard_inchi_key":"MTFOIHQNFFXXRF-XXBLPORFSA-N","superclass_results":"Diterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2310-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key
    equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key
    equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[],"predicate":"exact complete standard_inchi_key
    equality","query":"MTFOIHQNFFXXRF-XXBLPORFSA-N"}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained query frame, including the exact predicate and no-match
    result where empty: {"matches":[],"predicate":"exact chebi_id from exact full-key
    structure rows","query":[]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/21/source_scope_inventory/source_taxa; /contexts/21/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/21/source_scope_inventory/nonorganism_matches; /contexts/21/source_scope_inventory/actual_assay_rows;
    /contexts/21/source_scope_inventory/blank_AID_sentinels; /contexts/21/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Exact source-taxon and route lists; only the forward-merge/nonorganism
    lists are empty cohortwide, and assay/sentinel outcomes retain their exact values:
    {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:1470456","NCBITaxon:33903"]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/30
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Complete retained relevant stanzas; cached labels/synonyms are not fresh
    external authority: [{"complete_stanza":"[Term]\nid: NCBITaxon:33903\nname: Streptomyces
    avermitilis\nsynonym: \"Streptomyces avermectinius\" EXACT []\n\n","id":"NCBITaxon:33903","physical_line":14687},{"complete_stanza":"[Term]\nid:
    NCBITaxon:1470456\nname: Streptomyces cyslabdanicus\n\n","id":"NCBITaxon:1470456","physical_line":130135}]'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /records/9/direct_companion_paths; /records/9/direct_companion_predicates
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Exact one-hop scope without claim transfer: {"direct_companion_paths":["data/natural_products/terpenoids/cyslabdan-a.yaml","data/natural_products/terpenoids/cyslabdan-c.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/cyslabdan-a.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]},{"path":"data/natural_products/terpenoids/cyslabdan-c.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001910"]}]}'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch231-tentative/bgc-prep/bgc-conditional231-source-inventory-DATA-001.json
  locator: /contexts/20; /contexts/22
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: 'Whole raw/history/source contexts were read with exact attribution in
    the notes; full keys and citation roles remain distinct: [{"fullkey":"PSUMRJNLBIVEFF-RIVHMUOTSA-N","identifier":"naturalproductmech:mibig-f3cb15d2b6","mechanism_roots":["causal_graphs","biosynthetic_pathway"],"owned_BGCs":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-a.yaml"},{"fullkey":"PTRRHQHGAOYEKT-KYXZTKSHSA-N","identifier":"naturalproductmech:mibig-04c341bc33","mechanism_roots":[],"owned_BGCs":["BGC0001910"],"path":"data/natural_products/terpenoids/cyslabdan-c.yaml"}]'
  snapshot_sha256: 2fa0122c6e1b529e09cd05458ff38c77edb0d075456144c528ebe0237078b3b6
- evidence_id: bgc-2310-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: ChemicalStructure preserves source representation and standardized-key
    limitations. stereo_complete describes undefined centres; ComputedClassification
    is a named/versioned prediction, never a source assertion or admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2310-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and the absence
    of question-mark centre tags; it is not a blanket all-bond-geometry proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2310-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 974–1065
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: Maintained seeding preserves the source structure and named/versioned classifier
    output while separately retaining BGC and source compound classes.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2310-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: One-record scientific review requires claim-level evidence and twelve dimensions
    with truthful partial-completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2310-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-03T22:05:05.458512Z'
  support: supports
  summary: The review does not edit records; source access is bounded by the overriding
    no-request instruction.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:45:24.517787Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: b9cbdcc780498767fa6886409792cfedcdf872922813124081aff76c166efaab
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:45:49.043451Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0fd8658ae562b1dfcb46dc521794fb6cd3f0991f7fb047b756120acde0412b7a
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:46:08.738233Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:46:42.527754Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-231/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-231/native-current231-five-gates-execution-001.json
  accessed_at: '2026-11-03T21:46:54.303959Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: e760c01e6aac640808752417dde3e98f774512d6edde19a22ad69372e87adaeb
assessments:
- assessment_id: bgc-2310-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted identifier preserves complete key MTFOIHQNFFXXRF-XXBLPORFSA-N
    and source name cyslabdan B from BGC0001910 version 4, compound index 2. No exact
    retained ChEBI structure row joins it. Cyslabdan A and C have distinct full keys
    and retain separate identity, activity and mechanism scope.
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-grounding-owner
  - bgc-2310-source-mibig_compounds
  - bgc-2310-query-chebi_structures
  - bgc-2310-chemistry
  - bgc-2310-direct-contexts
  - bgc-2310-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: MTFOIHQNFFXXRF-XXBLPORFSA-N; exact complete retained MIBiG key.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2310-grounding-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-query-chebi_structures
    - bgc-2310-chemistry
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
  - name: grounding_scope
    value: MINTED with an empty exact retained ChEBI structure join; natural identity
      and external cross-references are not freshly verified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2310-grounding-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-query-chebi_structures
    - bgc-2310-chemistry
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
- assessment_id: bgc-2310-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: 'Both forms are neutral C25H41NO6S with 33 atoms and 34 bonds, two six-carbon
    rings, a terminal alkene, one E alkene, three scaffold hydroxyls, a sulfur bridge
    and an N-acetylcysteine-like substituent. Seven specified tetrahedral centres
    retain corresponding CIP labels. The stored SMILES has N26–C27(=O29), whereas
    the InChI-decoded form has N25=C15–O26: nitrogen loses one hydrogen and oxygen
    gains one. This is a local amide/imidic mobile-H representation difference, with
    an additional unspecified C=N geometry only in the decoded form. Formula, charge,
    standard InChI and full key agree, but both canonical SMILES comparisons are false
    and the diagnostic atom map is empty; complete_atom_count_match and full_graph_identity_established
    remain false. The true source stereo flag is the maintained tetrahedral-centre
    diagnostic, not blanket proof of every derived double-bond geometry.'
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-grounding-owner
  - bgc-2310-chemistry
  - bgc-2310-topology
  - bgc-2310-diagnostic-acceptance
  - bgc-2310-structure-schema
  - bgc-2310-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Seven specified tetrahedral centres and one E alkene; decoded imidic C=N
      adds an unspecified double-bond slot, beyond the source tetrahedral flag.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2310-grounding-owner
    - bgc-2310-chemistry
    - bgc-2310-topology
    - bgc-2310-diagnostic-acceptance
    - bgc-2310-structure-schema
    - bgc-2310-stereo-method
  - name: representation_correspondence
    value: Two false canonical SMILES flags; standard InChI/key/formula/charge agree;
      original correspondence remains empty and full_graph_identity_established false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2310-grounding-owner
    - bgc-2310-chemistry
    - bgc-2310-topology
    - bgc-2310-diagnostic-acceptance
    - bgc-2310-structure-schema
    - bgc-2310-stereo-method
- assessment_id: bgc-2310-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Streptomyces cyslabdanicus NCBITaxon:1470456 is a SOURCE_ASSERTION producer
    under active BGC0001910 version 4, whose retained quality is questionable and
    completeness unknown. There is no stated locus method and the link remains CLUSTER_UNSTATED.
    Streptomyces avermitilis NCBITaxon:33903 is a separate LOTUS occurrence; the retained
    heterologous-host context is not evidence that it is the native producer.
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-origin-owner
  - bgc-2310-source-mibig_compounds
  - bgc-2310-cached-taxonomy
  - bgc-2310-source-routes
  - bgc-2310-direct-contexts
  - bgc-2310-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: S. cyslabdanicus 1470456 producer versus S. avermitilis 33903 occurrence
      with retained host-context limits.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2310-origin-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-cached-taxonomy
    - bgc-2310-source-routes
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
  - name: producer_evidence
    value: SOURCE_ASSERTION; retained version 4 source assertion, separate from locus
      grade.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2310-origin-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-cached-taxonomy
    - bgc-2310-source-routes
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
  - name: locus_evidence
    value: BGC0001910 version 4, active/questionable/unknown; no stated method; CLUSTER_UNSTATED.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2310-origin-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-cached-taxonomy
    - bgc-2310-source-routes
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
- assessment_id: bgc-2310-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: DOI:10.1007/s10295-015-1694-6 is retained at COMPOUND_EVIDENCE level, while
    LOTUS preserves the case-different string DOI:10.1007/S10295-015-1694-6. These
    are not two independent publications or production experiments. Cyslabdan A's
    historical Mca assertion concerns A and cannot be transferred to B from this shared
    citation/locus.
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-origin-owner
  - bgc-2310-occurrence-owner
  - bgc-2310-source-mibig_compounds
  - bgc-2310-source-lotus_occurrences
  - bgc-2310-source-notes
  - bgc-2310-direct-contexts
  - bgc-2310-companion-boundaries
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI and case-different LOTUS DOI denote no independently
      established second publication.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2310-origin-owner
    - bgc-2310-occurrence-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-source-lotus_occurrences
    - bgc-2310-source-notes
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
- assessment_id: bgc-2310-bioactivity
  area: evidence
  topic: Occurrence and activity
  outcome: supported
  summary: One Streptomyces avermitilis occurrence is written, with no activity or
    target. The exact saved assay/target joins for B are empty. Neither the occurrence
    nor Cyslabdan A's terminal Mca mechanism supplies a B-specific enzyme, assay or
    biological outcome.
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-occurrence-owner
  - bgc-2310-assay-owner
  - bgc-2310-source-routes
  - bgc-2310-cached-taxonomy
  - bgc-2310-query-lotus_occurrences
  - bgc-2310-query-chebi_origins
  - bgc-2310-query-cyanometdb_occurrences
  - bgc-2310-query-pubchem_bioassay
  - bgc-2310-query-bindingdb_targets
  - bgc-2310-query-antibioticmech_inchikeys
  - bgc-2310-source-lotus_occurrences
  - bgc-2310-direct-contexts
  - bgc-2310-companion-boundaries
  dimensions:
  - name: occurrence_scope
    value: 1 written occurrence assertions; distinct from demonstrated production
      and independent-study counts.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2310-occurrence-owner
    - bgc-2310-assay-owner
    - bgc-2310-source-routes
    - bgc-2310-cached-taxonomy
    - bgc-2310-query-lotus_occurrences
    - bgc-2310-query-chebi_origins
    - bgc-2310-query-cyanometdb_occurrences
    - bgc-2310-query-pubchem_bioassay
    - bgc-2310-query-bindingdb_targets
    - bgc-2310-query-antibioticmech_inchikeys
    - bgc-2310-source-lotus_occurrences
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
  - name: assay_target_scope
    value: No written activity/target; Cyslabdan A terminal Mca claim does not transfer
      to B.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2310-occurrence-owner
    - bgc-2310-assay-owner
    - bgc-2310-source-routes
    - bgc-2310-cached-taxonomy
    - bgc-2310-query-lotus_occurrences
    - bgc-2310-query-chebi_origins
    - bgc-2310-query-cyanometdb_occurrences
    - bgc-2310-query-pubchem_bioassay
    - bgc-2310-query-bindingdb_targets
    - bgc-2310-query-antibioticmech_inchikeys
    - bgc-2310-source-lotus_occurrences
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
- assessment_id: bgc-2310-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: 'The source Diterpenoid compound class and Diterpene cluster subclass are
    distinct from NPClassifier''s Terpenoids / Diterpenoids / Labdane diterpenoids
    prediction and is_glycoside:false. Total C25 alone is not a contradiction: the
    represented nitrogen/sulfur-containing conjugate must be assessed at scaffold
    and substituent level. The model does not establish a complete pathway. The saved
    two-ring carbon framework is attached through sulfur to a five-carbon nitrogen-containing
    substituent, making scaffold-level Diterpenoids compatible with total C25. Neither
    saved graph establishes a carbohydrate residue or glycosidic linkage.'
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-classification-owner
  - bgc-2310-source-mibig_compounds
  - bgc-2310-source-npclassifier
  - bgc-2310-chemistry
  - bgc-2310-topology
  - bgc-2310-structure-schema
  - bgc-2310-classification-seeder
  - bgc-2310-direct-contexts
  - bgc-2310-companion-boundaries
  dimensions:
  - name: classification_applicability
    value: Labdane/Diterpenoids is scaffold-compatible despite total C25 and the five-carbon
      nitrogen/sulfur substituent; no sugar linkage.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2310-classification-owner
    - bgc-2310-source-mibig_compounds
    - bgc-2310-source-npclassifier
    - bgc-2310-chemistry
    - bgc-2310-topology
    - bgc-2310-structure-schema
    - bgc-2310-classification-seeder
    - bgc-2310-direct-contexts
    - bgc-2310-companion-boundaries
- assessment_id: bgc-2310-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed against the complete current
    owner/history, actual canonical intake, retained source payloads and complete
    saved paired molecular tables. Five original local gates passed, but full QC,
    complete OAK authority coverage and fresh external verification remain unavailable.
    This owner has no mechanism root or selected reader. The bounded eight-table curation
    scan found no exact cohort-token match; no supported new maintained-source correction
    is established. Scientific completion remains partial and native curation status
    is unchanged.
  target_ids:
  - naturalproductmech:mibig-826d2ff0d3
  evidence_ids:
  - bgc-2310-owner
  - bgc-2310-intake
  - bgc-2310-intake-acceptance
  - bgc-2310-inventory-acceptance
  - bgc-2310-plan
  - bgc-2310-plan-acceptance
  - bgc-2310-source-notes
  - bgc-2310-curation-scope
  - bgc-2310-diagnostic-execution
  - bgc-2310-diagnostic-acceptance
  - bgc-2310-native-acceptance
  - bgc-2310-review-profile
  - bgc-2310-review-skill
  dimensions:
  - name: review_completion
    value: Partial scientific review from retained evidence; full QC/OAK, fresh primary/taxonomic
      verification and complete natural stereochemical identity remain unresolved.
      No native status promotion.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2310-owner
    - bgc-2310-intake
    - bgc-2310-intake-acceptance
    - bgc-2310-inventory-acceptance
    - bgc-2310-plan
    - bgc-2310-plan-acceptance
    - bgc-2310-source-notes
    - bgc-2310-curation-scope
    - bgc-2310-diagnostic-execution
    - bgc-2310-diagnostic-acceptance
    - bgc-2310-native-acceptance
    - bgc-2310-review-profile
    - bgc-2310-review-skill
findings: []
actions: []
limitations:
- All evidence is retained locally. External identifiers, primary publications, taxonomy
  and natural stereochemical assignments were not refreshed under the absolute no-request
  instruction.
- Full QC and complete OAK authority coverage remain unavailable. Original local gates
  and successful stored parses establish only their stated mechanical scope.
- Empty joins concern only exact saved predicates and snapshots. Shared loci, taxa
  and citations do not transfer compound-specific production, activity, mechanism
  or independent-study status.
- Four original undefined-stereo warnings remain global and unassigned to records.
  No additional molecular/YAML parse, source query or target invocation occurred during
  scientific authoring.
- No source record, native curation status or history is edited. Any later correction
  belongs to the maintained owners listed in the accepted canonical intake.
- The amide/imidic local witness explains the canonical-form difference without replacing
  the original empty atom map, claiming exact fixed-graph identity, or assigning the
  added imidic double-bond geometry.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and actual canonical intake were read; all matching source
  payload and companion reading/carry attribution is retained in the pinned source
  notes.
- 'BGC personally read all fourteen saved molecular forms for these seven owners:
  342 atom rows and 362 bond rows plus every scalar, stereo/ring/motif table and original
  comparison/map.'
- ROOT operated original activation/capture; Support operated original canonical intakes;
  Native operated original gates and chemistry; BGC operated the admitted original
  collector/composer. No new target was invoked for these assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-231
```
