# Local evidence review: Dihydrobotrydial

- Review: 20261103T233839Z-dihydrobotrydial
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T23:01:25.988517Z
- Finished UTC: 2026-11-03T23:38:39.011636Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Dihydrobotrydial preserves its fully specified local stereo representation, compound-evidence citation and separate strain-level production versus species-level occurrence assertions. The retained glycoside prediction has a bounded applicability concern; no maintained-source defect is established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2318; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b5ca742a5e | data/natural_products/terpenoids/dihydrobotrydial.yaml | generated | Dihydrobotrydial |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-b5ca742a5e | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b5ca742a5e | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b5ca742a5e | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b5ca742a5e | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b5ca742a5e | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b5ca742a5e | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b5ca742a5e | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b5ca742a5e | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-b5ca742a5e.

The MINTED identifier retains QUGYVDURDBEQRB-CJNHKLDISA-N for BGC0000631 version 5, compound index 4. The exact ChEBI structure join is empty. The written npatlas:NPA019254 cross-reference is a literal source-row assertion, not a freshly resolved identity. Twenty direct locus companions include different full stereo keys; the 10-epi congener and Botrydial do not supply this owner with their identity, activity or mechanism.

### Representation

representation: supported. Targets: naturalproductmech:mibig-b5ca742a5e.

Both forms are neutral C17H28O5, one connected component with 22 heavy atoms and 24 bonds. The three-ring polycyclic framework has two hydroxyls, one cyclic ether/hemiacetal and a separate acetate ester. SMILES O8 connects C7 and C9; C7 also bears hydroxyl O16, while hydroxyl O17 is attached to C5. The acetate is C3-O18-C19(=O20)-C21. Seven tetrahedral centres are specified in both forms, with no unspecified potential centre, consistent with the true flag. All ten comparisons and the complete saved correspondence agree; full_graph_identity_established remains false. Atom numbers here are zero-based diagnostic indices, not biochemical locants.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-b5ca742a5e.

The producer assertion names Botrytis cinerea B05.10, NCBITaxon:332648, with BGC_CHARACTERIZED evidence. The four LOTUS occurrences instead name species-level NCBITaxon:40559; those taxa are not interchangeable. Cached Botryotinia synonyms preserve local name usage without a new taxonomy lookup. BGC0000631 version 5 is active, questionable and complete; knock-out studies support CLUSTER_DEMONSTRATED at CP009816.1:2216500-2246000. A demonstrated locus link does not import the unselected Botrydial graph into this record.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-b5ca742a5e.

DOI:10.1021/cb800225v is explicitly COMPOUND_EVIDENCE provenance for the MIBiG producer/locus claims. Four written LOTUS assertions retain four different literal DOI strings. They are database occurrence triples, not four independently verified experiments, and they do not replace the compound-evidence citation or establish a producer strain. Shared BGC0000631 membership does not make each congener citation interchangeable.

### Occurrence and activity

evidence: supported. Targets: naturalproductmech:mibig-b5ca742a5e.

All four written Botrytis cinerea occurrence assertions reproduce the four exact LOTUS rows and their distinct DOI strings. They report occurrence rather than production by B05.10. No bioactivity or molecular target is written, and the exact retained PubChem, BindingDB and AntibioticMech joins are empty. No Botrydial activity or mechanism is transferred; these source limits do not establish inactivity.

### Classification

consistency: concern. Targets: naturalproductmech:mibig-b5ca742a5e.

NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids / Sesquiterpenoids / Botryane sesquiterpenoids and is_glycoside:true. The saturated C5O cycle is integrated into the polycyclic scaffold: it shares carbon-framework connections and contains the C7-O8-C9 hemiacetal ether. The other carbon-O-carbon bridge is the acetate O18. The complete saved topology does not identify a separate sugar residue or a sugar-aglycone linkage, so the C5O motif alone cannot establish a glycoside. This is a concern about applicability of the preserved model output, not proof of a wrong source identity or schema violation. The schema explicitly treats this field as a named/versioned computation; there is no supported replacement value or source correction here.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-b5ca742a5e.

All twelve scientific dimensions were assessed using the complete current owner/history, actual canonical intake, retained source payloads and complete saved paired molecular tables. Five original local gates passed, but full QC, complete OAK authority coverage and fresh external verification remain unavailable. This owner has no mechanism root or selected reader. The bounded eight-table curation scan found no exact cohort-token match. No supported new maintained-source correction is established; scientific completion remains partial and native curation status is unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2318-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/dihydrobotrydial.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner and all 2 history entries; native curation_status remains SEEDED. |
| bgc-2318-capture | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/7 | supports | Complete captured owner preserves every written field and history; no mechanism root or component is present. |
| bgc-2318-intake | /private/tmp/npm-review-work/shared-next-batch232/intakes/2318-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-b5ca742a5e; 57 pinned input placements and explicit maintained source ownership. |
| bgc-2318-grounding-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"chemical_structure":{"smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi":"InChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000631"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-b5ca742a5e","label":"Dihydrobotrydial","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-b5ca742a5e","source":"MIBIG","source_id":"BGC0000631","source_label":"Dihydrobotrydial","source_version":"5"}],"xrefs":["npatlas:NPA019254"]} |
| bgc-2318-origin-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000631","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"5","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1021/cb800225v"}],"genome_accession":"genbank:CP009816.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Knock-out studies"],"locus_from":2216500,"locus_to":2246000,"organism_label":"Botrytis cinerea B05.10","organism_taxon_id":"NCBITaxon:332648"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000631","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1021/cb800225v"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus evidence: Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"5","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10"}],"producer_taxon_groups":["FUNGAL"]} |
| bgc-2318-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"occurrence_taxon_groups":["FUNGAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1002/CBER.19741070530"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0031-9422(94)00690-U"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4020(99)00032-0"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis cinerea","taxon_source":"NCBITaxon"}]} |
| bgc-2318-assay-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {} |
| bgc-2318-classification-owner | /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":["Botryane sesquiterpenoids"],"is_glycoside":true,"pathway_results":["Terpenoids"],"superclass_results":["Sesquiterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2318-chemistry | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/status; /records/7/inchi/status; /records/7/smiles/computed; /records/7/inchi/computed; /records/7/comparisons; /records/7/atom_correspondence | supports | Both stored forms parsed. Exact original comparison/correspondence and stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[0,8,5,10,12,16,11,13,20,7,15,6,14,2,3,4,18,19,21,9,17,1]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":7},"smiles_stereo":{"Atom_Tetrahedral:Specified":7}} |
| bgc-2318-topology | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json; /records/7/smiles/computed; /records/7/inchi/computed; /records/7/declared_structure; /records/7/literal_InChI_layers; /records/7/comparisons; /records/7/atom_correspondence | supports | Complete saved topology/stereo interpretation: Both forms are neutral C17H28O5, one connected component with 22 heavy atoms and 24 bonds. The three-ring polycyclic framework has two hydroxyls, one cyclic ether/hemiacetal and a separate acetate ester. SMILES O8 connects C7 and C9; C7 also bears hydroxyl O16, while hydroxyl O17 is attached to C5. The acetate is C3-O18-C19(=O20)-C21. Seven tetrahedral centres are specified in both forms, with no unspecified potential centre, consistent with the true flag. All ten comparisons and the complete saved correspondence agree; full_graph_identity_established remains false. Atom numbers here are zero-based diagnostic indices, not biochemical locants. |
| bgc-2318-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-execution-001.json; Whole original execution receipt | supports | Native operated one original stored-form diagnostic, exit 0, one attempt, preserved stdout/stderr and closed environment. The inherited DATA observer literal is not the operator attribution. |
| bgc-2318-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-diagnostic-acceptance-001.json; Whole ROOT diagnostic acceptance | supports | ROOT accepts the original 20 stored parses, 98 true/two false comparison flags (the latter confined to Cyslabdan C) and six global unassigned stereo warnings. This establishes no fresh natural identity or full-graph equivalence. |
| bgc-2318-native-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-native-gates-acceptance-001.json; Whole ROOT gate acceptance | supports | Five original local gates passed; all_native_gates_passed remains false because full QC and complete OAK coverage are unavailable. Gate success is not a scientific verdict. |
| bgc-2318-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-intake-acceptance-001.json; Whole ROOT intake acceptance | supports | ROOT accepts ten actual one-record intakes, 436 input placements / 75 paths and exact source ownership; scientific review remains separate. |
| bgc-2318-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-source-inventory-acceptance-001.json; Whole ROOT inventory acceptance | supports | ROOT accepts the single original local inventory and its current source/capture joins; complete meaning reading is separately attributed in the notes. |
| bgc-2318-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch232/root-input-plan-acceptance-001.json; Whole ROOT input-plan acceptance | supports | ROOT accepts the exact actual plan and preserved source contexts; no scientific verdict follows. |
| bgc-2318-plan | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-target-input-plan-001.json; /records/7 | supports | Current one-record input plan with exact direct companions, retained predicates and input roles. |
| bgc-2318-source-notes | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading attribution and compound-specific cautions; the notes do not assert pre-intake scientific verdicts. |
| bgc-2318-curation-scope | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json; /curation | supports | Eight pinned implemented curation tables were directly opened including ignored files: 101 exact cohort literals across 93 data rows gave zero textual hits in that bounded scope. Reserved decisions.tsv was not consumed. |
| bgc-2318-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":730,"physical_line":730,"raw_tsv_record":"BGC0000631\t5\tactive\tquestionable\tcomplete\tDihydrobotrydial\t4\tC[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C\tInChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1\tQUGYVDURDBEQRB-CJNHKLDISA-N\ttrue\t\tnpatlas:NPA019254\tNCBITaxon:332648\tBotrytis cinerea B05.10\tterpene\tSesquiterpene\tCP009816.1\t2216500\t2246000\tKnock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tDOI:10.1021/cb800225v\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"4","compound_name":"Dihydrobotrydial","database_ids":"npatlas:NPA019254","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1021/cb800225v","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi":"InChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10"},"row_sha256":"a77f37f564ae1eaf77495a4d2643cf6875d3d9bed278beca4dc9dffb73065b57"}],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 730–730, row_sha256 a77f37f564ae1eaf77495a4d2643cf6875d3d9bed278beca4dc9dffb73065b57 | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"4","compound_name":"Dihydrobotrydial","database_ids":"npatlas:NPA019254","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1021/cb800225v","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi":"InChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis cinerea B05.10"}] |
| bgc-2318-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":7415,"physical_line":7415,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1002/CBER.19741070530\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1002/CBER.19741070530","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"ace74b15c04350bd08b92c0c44d88f52bfcfc988c7c9f772a0386bc8fcd2b492"},{"last_physical_line":7416,"physical_line":7416,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/0031-9422(94)00690-U\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(94)00690-U","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"0f199e8b22d72bf84739a3a877ae4b76ef1e3e0afcaf097cc16250a3d9fe9367"},{"last_physical_line":7417,"physical_line":7417,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/0031-9422(95)00643-5\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"5614f720ea430f994c956f44bc81c80bbca055ce1575a64f86942ce80f57451e"},{"last_physical_line":7418,"physical_line":7418,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/S0040-4020(99)00032-0\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"ad2c0fbca6af6193c6377d2d8789a4c7a80a1c3f6affdca19626cd676e8e8ff1"}],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 7415–7415, row_sha256 ace74b15c04350bd08b92c0c44d88f52bfcfc988c7c9f772a0386bc8fcd2b492; physical lines 7416–7416, row_sha256 0f199e8b22d72bf84739a3a877ae4b76ef1e3e0afcaf097cc16250a3d9fe9367; physical lines 7417–7417, row_sha256 5614f720ea430f994c956f44bc81c80bbca055ce1575a64f86942ce80f57451e; physical lines 7418–7418, row_sha256 ad2c0fbca6af6193c6377d2d8789a4c7a80a1c3f6affdca19626cd676e8e8ff1 | supports | Complete retained physical row payloads, every field: [{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1002/CBER.19741070530","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(94)00690-U","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"}] |
| bgc-2318-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":2040,"physical_line":2040,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tC[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C\tTerpenoids\tSesquiterpenoids\tBotryane sesquiterpenoids\ttrue\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Botryane sesquiterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","superclass_results":"Sesquiterpenoids"},"row_sha256":"897d08828e777b6325cf7d4e8ff07078d34f8a40b0e75e17172d7fab0382080f"}],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2040–2040, row_sha256 897d08828e777b6325cf7d4e8ff07078d34f8a40b0e75e17172d7fab0382080f | supports | Complete retained physical row payloads, every field: [{"class_results":"Botryane sesquiterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","superclass_results":"Sesquiterpenoids"}] |
| bgc-2318-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"} |
| bgc-2318-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2318-source-routes | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/26/source_scope_inventory/source_taxa; /contexts/26/source_scope_inventory/forward_taxon_merge_matches; /contexts/26/source_scope_inventory/nonorganism_matches; /contexts/26/source_scope_inventory/actual_assay_rows; /contexts/26/source_scope_inventory/blank_AID_sentinels; /contexts/26/source_scope_inventory/related_corpus_rows | supports | Exact source taxon and route lists; source_taxa is distinct from the empty forward/nonorganism and assay/related routes: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:332648","NCBITaxon:40559"]} |
| bgc-2318-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/9 | supports | Complete relevant cached stanzas, with no fresh taxonomy verification: [{"complete_stanza":"[Term]\nid: NCBITaxon:40559\nname: Botrytis cinerea\nsynonym: \"Botryotinia fuckeliana\" EXACT []\nsynonym: \"Botrytis cinerea Pers., 1801\" EXACT []\nsynonym: \"Peziza fuckeliana\" EXACT []\nsynonym: \"Sclerotinia fuckeliana\" EXACT []\n\n","id":"NCBITaxon:40559","physical_line":18031},{"complete_stanza":"[Term]\nid: NCBITaxon:332648\nname: Botrytis cinerea B05.10\nsynonym: \"Botryotinia fuckeliana B05.10\" EXACT []\n\n","id":"NCBITaxon:332648","physical_line":83758}] |
| bgc-2318-direct-contexts | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /records/7/direct_companion_paths; /records/7/direct_companion_predicates | supports | Exact one-hop retained scope, without claim transfer: {"direct_companion_paths":["data/natural_products/terpenoids/1-epibotrydial.yaml","data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","data/natural_products/terpenoids/8-9-epibotrydial.yaml","data/natural_products/terpenoids/botrydial.yaml","data/natural_products/terpenoids/botrydienal.yaml","data/natural_products/terpenoids/botryenalol.yaml","data/natural_products/terpenoids/botryendial.yaml","data/natural_products/terpenoids/dehydrobotrydienol.yaml","data/natural_products/terpenoids/norbotrydialone-acetate.yaml","data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","data/natural_products/terpenoids/secobotrytriendiol.yaml","data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/1-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydienal.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botryenalol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botryendial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]}]} |
| bgc-2318-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json; /contexts/3; /contexts/4; /contexts/5; /contexts/6; /contexts/7; /contexts/8; /contexts/9; /contexts/10; /contexts/11; /contexts/12; /contexts/13; /contexts/14; /contexts/15; /contexts/16; /contexts/20; /contexts/33; /contexts/34; /contexts/35; /contexts/36; /contexts/37 | supports | Whole context meanings and raw/history carries are attributed in the notes; exact identities and root scopes: [{"fullkey":"SJFIYVCSGNWVPJ-SDLFRHKASA-N","identifier":"naturalproductmech:mibig-acc775e1b7","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/1-epibotrydial.yaml"},{"fullkey":"MBHVNAKPTPFWNG-MYFMSEKESA-N","identifier":"naturalproductmech:mibig-1e06238f05","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml"},{"fullkey":"QUGYVDURDBEQRB-VZJVBFQISA-N","identifier":"naturalproductmech:mibig-7950af79c1","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml"},{"fullkey":"MFOUCDNLAFNKML-SVLWDWOGSA-N","identifier":"naturalproductmech:mibig-e2d62600f5","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml"},{"fullkey":"CAMCSBCRRUTMEK-OAHLLOKOSA-N","identifier":"naturalproductmech:mibig-7b45e48275","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml"},{"fullkey":"PCEVLQFNPPWJEB-RFAUZJTJSA-N","identifier":"naturalproductmech:mibig-8b4cd14741","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml"},{"fullkey":"JUCMRFKOKIZVPS-OAHLLOKOSA-N","identifier":"naturalproductmech:mibig-bbb6f44666","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml"},{"fullkey":"YPJRKTIWVUVMDI-LSDHHAIUSA-N","identifier":"naturalproductmech:mibig-10fda622fe","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml"},{"fullkey":"RVXLTRZIAMMATE-JMTSMVSISA-N","identifier":"naturalproductmech:mibig-0bd6ab53bc","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml"},{"fullkey":"SJFIYVCSGNWVPJ-PQVRDHEWSA-N","identifier":"naturalproductmech:mibig-a2b74a45ae","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml"},{"fullkey":"SJFIYVCSGNWVPJ-GKKOWQTJSA-N","identifier":"CHEBI:3159","mechanism_roots":["causal_graphs"],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botrydial.yaml"},{"fullkey":"CFAMAVBUWMXYLX-MEBBXXQBSA-N","identifier":"naturalproductmech:mibig-a1c6942987","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botrydienal.yaml"},{"fullkey":"DSVSTMJOGQEZJX-BYLNDYCFSA-N","identifier":"naturalproductmech:mibig-d567f1a1cd","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botryenalol.yaml"},{"fullkey":"QWZKEROSOALLJP-BYLNDYCFSA-N","identifier":"naturalproductmech:mibig-79ce4aca52","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botryendial.yaml"},{"fullkey":"UQQKKLVKVVJDEX-OAHLLOKOSA-N","identifier":"naturalproductmech:mibig-247120aa23","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml"},{"fullkey":"OMZUEHMZFLBHNI-PCKWUFTNSA-N","identifier":"naturalproductmech:mibig-9b040d7e03","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml"},{"fullkey":"GYABYKLKVQPSPD-NVWZYQMFSA-N","identifier":"naturalproductmech:mibig-2cef442430","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml"},{"fullkey":"GNMCOKDZWITFBO-MGNGBMTDSA-N","identifier":"naturalproductmech:mibig-f478b3a4f7","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml"},{"fullkey":"BHNACKMCMDASDB-UJNBGNEJSA-N","identifier":"naturalproductmech:mibig-ff72b656ae","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml"},{"fullkey":"WLPOYIWCPMYYGM-KGRKPJGKSA-N","identifier":"naturalproductmech:mibig-1c14174a30","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml"}] |
| bgc-2318-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure retains standardized-key limits and undefined stereocentres. ComputedClassification is a named/versioned prediction, not a source assertion or admission criterion. |
| bgc-2318-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and absence of question-mark centre tags; it is not a blanket all-bond-geometry proof. |
| bgc-2318-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 974–1065 | supports | Maintained seeding preserves source structure and named/versioned model values separately from BGC/source compound classes and cross-reference assertions. |
| bgc-2318-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record scientific review requires claim-level evidence and twelve dimensions with truthful partial completion and unavailable-check limits. |
| bgc-2318-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit records; overriding no-request instructions bound evidence access. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-232/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-232/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-232/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-232/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-232/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. External identifiers, primary publications, taxonomy and natural stereochemical assignments were not refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gates and successful stored parses establish only their stated mechanical scope.
- Empty joins concern exact saved predicates and snapshots only. Shared loci, taxa, names and citations do not transfer compound-specific production, activity, mechanism or independent-study status.
- Six original undefined-stereo warnings remain global and unassigned to records. No additional molecular/YAML parse, source query or target invocation occurred during scientific authoring.
- No source record, native curation status or history is edited. Any later supported correction belongs to the maintained owners identified in the accepted canonical intake.
- The model glycoside:true value is retained faithfully. The integrated hemiacetal ring and acetate are not a separate sugar assignment; no replacement prediction or exact source correction is established.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual canonical intake were read. Full source payload and companion reading/carry attribution is retained in the pinned notes.
- BGC personally read all ten molecular forms for these five owners: 248 atom rows and 276 bond rows plus all scalars, ring/stereo/motif tables and original comparisons/maps. Diagnostic atom numbers are zero-based indices, not biochemical locants.
- ROOT operated original activation/capture, collector, composer and canonical intakes; Native operated original gates and chemistry. BGC authored the collector/composer source and notes but invoked no target for these scientific assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T233839Z-dihydrobotrydial
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Dihydrobotrydial'
started_at: '2026-11-03T23:01:25.988517Z'
finished_at: '2026-11-03T23:38:39.011636Z'
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
summary: Dihydrobotrydial preserves its fully specified local stereo representation,
  compound-evidence citation and separate strain-level production versus species-level
  occurrence assertions. The retained glycoside prediction has a bounded applicability
  concern; no maintained-source defect is established.
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
  - path: data/natural_products/terpenoids/1-epibotrydial.yaml
    sha256: de27183b14aeebdaa766502e80b533dae2b4fea8cbb8a1a1c3d3623793f80775
    role: context
  - path: data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml
    sha256: 755ae0d04e75ed4fb5510c53f3ac3d011a77064305a8e5e22f5fb24a2b4fc2c6
    role: context
  - path: data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml
    sha256: 5a35280153870595b8fa92396c1a4803d341f3618f91ff32c5c49fcab4044e48
    role: context
  - path: data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml
    sha256: 600744b216155b8a5c6e7e2cec0f0d47be3fb23ddf7d291b353035f0392b6bed
    role: context
  - path: data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml
    sha256: c3a205986d77c29236528a192299e9ce2f2d7011d6cb38300b7e07ec2865143f
    role: context
  - path: data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml
    sha256: 583c51cc539f04fc68e99a0fe5b1b86e7e2e0c76235227e5a19356847929bf0d
    role: context
  - path: data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml
    sha256: c25e2696521c9381fbaebaf01deac68cdc70cab04a9b7ab03eda82c595b0a561
    role: context
  - path: data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml
    sha256: d8a363fb5c558056a1c7ed69312e113e2310f8bfbbf787f8eb07a0030745ec54
    role: context
  - path: data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml
    sha256: c4c9d1c900ad07aac687e0b9ec51c5ba589e9e065c4f0116446a248ba366112e
    role: context
  - path: data/natural_products/terpenoids/8-9-epibotrydial.yaml
    sha256: 11f0440d7c378d961befc6e158afa3f9a839110ce672438ad032baa487a9cc33
    role: context
  - path: data/natural_products/terpenoids/botrydial.yaml
    sha256: f12d22645ff34656cf446630d1b2c838db1ffa59c978182a42c5e10fcd5134cd
    role: context
  - path: data/natural_products/terpenoids/botrydienal.yaml
    sha256: 7f18efdecb4f12ebcf7c8e9710f0cb70d630b33cad1ba3c79b2aa8f8db7af839
    role: context
  - path: data/natural_products/terpenoids/botryenalol.yaml
    sha256: 473ebf066845fe74c1373996eceff8390a4e4ee3583cd69b3cf751683b936add
    role: context
  - path: data/natural_products/terpenoids/botryendial.yaml
    sha256: 3c5281cc27c72cdcd4b4c0ff933483687532e1be9378618a7cf209a691a98761
    role: context
  - path: data/natural_products/terpenoids/dehydrobotrydienol.yaml
    sha256: 8a56db9386bde355c12ccb9e3b6a333857a96ccbb7db253a52765213ec4538b5
    role: context
  - path: data/natural_products/terpenoids/dihydrobotrydial.yaml
    sha256: aa738c13a340ea710c01fb6d36f9a794537660a87237bd1a576db8a9c2c9de9b
    role: target
  - path: data/natural_products/terpenoids/norbotrydialone-acetate.yaml
    sha256: 347f7627931387555bad558583abf5d0edd65f74374c37f7e462a24684485e97
    role: context
  - path: data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml
    sha256: 37a54d9f76ef5c6ff47b82d4852a012c27e62412d542e7e351cbf351bdbb6fc4
    role: context
  - path: data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml
    sha256: a650f624eca66433eda385fe89540aa42d5e2116b8cdd6f5af761e77b90c9478
    role: context
  - path: data/natural_products/terpenoids/secobotrytriendiol.yaml
    sha256: acd560fe75765a0826a9cdbebef3eee34e941dea669b57b331da785a71da0760
    role: context
  - path: data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml
    sha256: 8ef90288327387e143f9995ee7eef0e33ce55a8c01d323b9aeb2f0f603b01f70
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
  selection: Campaign path order 2318; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b5ca742a5e
targets:
- target_id: naturalproductmech:mibig-b5ca742a5e
  path: data/natural_products/terpenoids/dihydrobotrydial.yaml
  label: Dihydrobotrydial
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
  - naturalproductmech:mibig-b5ca742a5e
  command: just validate-strict data/natural_products/terpenoids/cyslabdan-c.yaml
    data/natural_products/terpenoids/dehydrobotrydienol.yaml data/natural_products/terpenoids/demethoxyviridin.yaml
    data/natural_products/terpenoids/desacetylfusarochromene.yaml data/natural_products/terpenoids/deschloro-merochlorin-a.yaml
    data/natural_products/terpenoids/deschloro-merochlorin-b.yaml data/natural_products/terpenoids/dichloro-merochlorin-b.yaml
    data/natural_products/terpenoids/dihydrobotrydial.yaml data/natural_products/terpenoids/ent-kauren-16alpha-ol-2.yaml
    data/natural_products/terpenoids/ent-kauren-16alpha-ol.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-232/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-b5ca742a5e
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-232/validate-all-001.tsv
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
  - naturalproductmech:mibig-b5ca742a5e
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
  - naturalproductmech:mibig-b5ca742a5e
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
  - naturalproductmech:mibig-b5ca742a5e
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-232/review-queue-001.tsv
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
  - naturalproductmech:mibig-b5ca742a5e
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2318-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/dihydrobotrydial.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Complete current owner and all 2 history entries; native curation_status
    remains SEEDED.
  snapshot_sha256: aa738c13a340ea710c01fb6d36f9a794537660a87237bd1a576db8a9c2c9de9b
- evidence_id: bgc-2318-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Complete captured owner preserves every written field and history; no mechanism
    root or component is present.
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: bgc-2318-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/intakes/2318-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Actual canonical intake for naturalproductmech:mibig-b5ca742a5e; 57 pinned
    input placements and explicit maintained source ownership.
  snapshot_sha256: 0f5083077d9a4aad0e199db0fd5d177a10feade6a8372ec2824fed7cb94836d0
- evidence_id: bgc-2318-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi":"InChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000631"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-b5ca742a5e","label":"Dihydrobotrydial","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-b5ca742a5e","source":"MIBIG","source_id":"BGC0000631","source_label":"Dihydrobotrydial","source_version":"5"}],"xrefs":["npatlas:NPA019254"]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: bgc-2318-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000631","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"5","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1021/cb800225v"}],"genome_accession":"genbank:CP009816.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Knock-out
    studies"],"locus_from":2216500,"locus_to":2246000,"organism_label":"Botrytis cinerea
    B05.10","organism_taxon_id":"NCBITaxon:332648"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000631","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000631 entry version 5; citation taken from the compound evidence level","reference":"DOI:10.1021/cb800225v"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus
    evidence: Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED;
    this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"5","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10"}],"producer_taxon_groups":["FUNGAL"]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: bgc-2318-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"occurrence_taxon_groups":["FUNGAL"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1002/CBER.19741070530"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0031-9422(94)00690-U"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0031-9422(95)00643-5"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/S0040-4020(99)00032-0"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1135851","source":"LOTUS","taxon_id":"NCBITaxon:40559","taxon_label":"Botrytis
    cinerea","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: bgc-2318-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: bgc-2318-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":["Botryane
    sesquiterpenoids"],"is_glycoside":true,"pathway_results":["Terpenoids"],"superclass_results":["Sesquiterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: 883150ac3453edd0ce7de64f9eebf1c40e147d525fe26395b2e28c38a1e64c0d
- evidence_id: bgc-2318-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/status; /records/7/inchi/status;
    /records/7/smiles/computed; /records/7/inchi/computed; /records/7/comparisons;
    /records/7/atom_correspondence
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison/correspondence and
    stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[0,8,5,10,12,16,11,13,20,7,15,6,14,2,3,4,18,19,21,9,17,1]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"inchi_stereo":{"Atom_Tetrahedral:Specified":7},"smiles_stereo":{"Atom_Tetrahedral:Specified":7}}'
  snapshot_sha256: 24e1f67161d916573d35a6640775a2330ce09969f6fc115611f39275865549b9
- evidence_id: bgc-2318-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/smiles/computed; /records/7/inchi/computed; /records/7/declared_structure;
    /records/7/literal_InChI_layers; /records/7/comparisons; /records/7/atom_correspondence
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete saved topology/stereo interpretation: Both forms are neutral
    C17H28O5, one connected component with 22 heavy atoms and 24 bonds. The three-ring
    polycyclic framework has two hydroxyls, one cyclic ether/hemiacetal and a separate
    acetate ester. SMILES O8 connects C7 and C9; C7 also bears hydroxyl O16, while
    hydroxyl O17 is attached to C5. The acetate is C3-O18-C19(=O20)-C21. Seven tetrahedral
    centres are specified in both forms, with no unspecified potential centre, consistent
    with the true flag. All ten comparisons and the complete saved correspondence
    agree; full_graph_identity_established remains false. Atom numbers here are zero-based
    diagnostic indices, not biochemical locants.'
  snapshot_sha256: 24e1f67161d916573d35a6640775a2330ce09969f6fc115611f39275865549b9
- evidence_id: bgc-2318-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/chemistry-local/diagnostic-execution-001.json
  locator: Whole original execution receipt
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Native operated one original stored-form diagnostic, exit 0, one attempt,
    preserved stdout/stderr and closed environment. The inherited DATA observer literal
    is not the operator attribution.
  snapshot_sha256: 15c8254e0158f96b799ce154e0da4573fcbab5d68a0220d3ae7d9e58b1363a58
- evidence_id: bgc-2318-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-diagnostic-acceptance-001.json
  locator: Whole ROOT diagnostic acceptance
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses, 98 true/two false comparison
    flags (the latter confined to Cyslabdan C) and six global unassigned stereo warnings.
    This establishes no fresh natural identity or full-graph equivalence.
  snapshot_sha256: 7b2881f00f40f445f7f8a07b77560f80516976679c6c7ab7bdc5a0d6bbbf42c1
- evidence_id: bgc-2318-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-native-gates-acceptance-001.json
  locator: Whole ROOT gate acceptance
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Five original local gates passed; all_native_gates_passed remains false
    because full QC and complete OAK coverage are unavailable. Gate success is not
    a scientific verdict.
  snapshot_sha256: a95313b79d0a1105500acbfbd4cd8633d3878a9fd0176bdb2130446ee881a049
- evidence_id: bgc-2318-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-intake-acceptance-001.json
  locator: Whole ROOT intake acceptance
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: ROOT accepts ten actual one-record intakes, 436 input placements / 75 paths
    and exact source ownership; scientific review remains separate.
  snapshot_sha256: 8fcc103949fe722e55e277ca6ebd8c7e6a91535ced87dcc906209bd397b5a926
- evidence_id: bgc-2318-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-source-inventory-acceptance-001.json
  locator: Whole ROOT inventory acceptance
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: ROOT accepts the single original local inventory and its current source/capture
    joins; complete meaning reading is separately attributed in the notes.
  snapshot_sha256: 1be82b2a714236a0bf38785ec588e0dbc35d6d0c52e614aa4dc66faf9e19742f
- evidence_id: bgc-2318-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232/root-input-plan-acceptance-001.json
  locator: Whole ROOT input-plan acceptance
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: ROOT accepts the exact actual plan and preserved source contexts; no scientific
    verdict follows.
  snapshot_sha256: ac91e6edf46b06471c00f82f4e414d90618c1520b4a4634518c4b2ac43f43630
- evidence_id: bgc-2318-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-target-input-plan-001.json
  locator: /records/7
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Current one-record input plan with exact direct companions, retained predicates
    and input roles.
  snapshot_sha256: 94f01db8f3a55101c987af4aa40300302ac195827d11910711925264210ed158
- evidence_id: bgc-2318-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Complete disjoint source/raw-history reading attribution and compound-specific
    cautions; the notes do not assert pre-intake scientific verdicts.
  snapshot_sha256: 725071a2a2a8f19fa72422d9eefda4482682b9ae2ccc4471cbc38618a7f38a25
- evidence_id: bgc-2318-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-scope-notes-002.json
  locator: /curation
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Eight pinned implemented curation tables were directly opened including
    ignored files: 101 exact cohort literals across 93 data rows gave zero textual
    hits in that bounded scope. Reserved decisions.tsv was not consumed.'
  snapshot_sha256: 725071a2a2a8f19fa72422d9eefda4482682b9ae2ccc4471cbc38618a7f38a25
- evidence_id: bgc-2318-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":730,"physical_line":730,"raw_tsv_record":"BGC0000631\t5\tactive\tquestionable\tcomplete\tDihydrobotrydial\t4\tC[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C\tInChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1\tQUGYVDURDBEQRB-CJNHKLDISA-N\ttrue\t\tnpatlas:NPA019254\tNCBITaxon:332648\tBotrytis
    cinerea B05.10\tterpene\tSesquiterpene\tCP009816.1\t2216500\t2246000\tKnock-out
    studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tDOI:10.1021/cb800225v\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"4","compound_name":"Dihydrobotrydial","database_ids":"npatlas:NPA019254","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out
    studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1021/cb800225v","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi":"InChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10"},"row_sha256":"a77f37f564ae1eaf77495a4d2643cf6875d3d9bed278beca4dc9dffb73065b57"}],"predicate":"exact
    complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 730–730, row_sha256 a77f37f564ae1eaf77495a4d2643cf6875d3d9bed278beca4dc9dffb73065b57
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Sesquiterpene","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"4","compound_name":"Dihydrobotrydial","database_ids":"npatlas:NPA019254","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"5","genome_accession":"CP009816.1","locus_evidence_methods":"Knock-out
    studies","locus_from":"2216500","locus_to":"2246000","mibig_accession":"BGC0000631","primary_reference":"DOI:10.1021/cb800225v","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"COMPOUND_EVIDENCE","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi":"InChI=1S/C17H28O5/c1-9-6-11(22-10(2)18)13-15(3,4)7-16(5)8-21-14(19)12(9)17(13,16)20/h9,11-14,19-20H,6-8H2,1-5H3/t9-,11+,12-,13+,14+,16-,17-/m1/s1","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","stereo_complete":"true","taxon_id":"NCBITaxon:332648","taxon_label":"Botrytis
    cinerea B05.10"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2318-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":7415,"physical_line":7415,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1002/CBER.19741070530\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1002/CBER.19741070530","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"ace74b15c04350bd08b92c0c44d88f52bfcfc988c7c9f772a0386bc8fcd2b492"},{"last_physical_line":7416,"physical_line":7416,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/0031-9422(94)00690-U\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(94)00690-U","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"0f199e8b22d72bf84739a3a877ae4b76ef1e3e0afcaf097cc16250a3d9fe9367"},{"last_physical_line":7417,"physical_line":7417,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/0031-9422(95)00643-5\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"5614f720ea430f994c956f44bc81c80bbca055ce1575a64f86942ce80f57451e"},{"last_physical_line":7418,"physical_line":7418,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tBotrytis
    cinerea\tNCBITaxon:40559\thttp://www.wikidata.org/entity/Q1135851\t10.1016/S0040-4020(99)00032-0\thttp://www.wikidata.org/entity/Q104403379\n","row":{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},"row_sha256":"ad2c0fbca6af6193c6377d2d8789a4c7a80a1c3f6affdca19626cd676e8e8ff1"}],"predicate":"exact
    complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 7415–7415, row_sha256 ace74b15c04350bd08b92c0c44d88f52bfcfc988c7c9f772a0386bc8fcd2b492;
    physical lines 7416–7416, row_sha256 0f199e8b22d72bf84739a3a877ae4b76ef1e3e0afcaf097cc16250a3d9fe9367;
    physical lines 7417–7417, row_sha256 5614f720ea430f994c956f44bc81c80bbca055ce1575a64f86942ce80f57451e;
    physical lines 7418–7418, row_sha256 ad2c0fbca6af6193c6377d2d8789a4c7a80a1c3f6affdca19626cd676e8e8ff1
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1002/CBER.19741070530","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(94)00690-U","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/0031-9422(95)00643-5","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"},{"organism_name":"Botrytis
    cinerea","organism_wikidata":"http://www.wikidata.org/entity/Q1135851","reference_doi":"10.1016/S0040-4020(99)00032-0","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104403379","taxon_id":"NCBITaxon:40559"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2318-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":2040,"physical_line":2040,"raw_tsv_record":"QUGYVDURDBEQRB-CJNHKLDISA-N\tC[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C\tTerpenoids\tSesquiterpenoids\tBotryane
    sesquiterpenoids\ttrue\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Botryane
    sesquiterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","superclass_results":"Sesquiterpenoids"},"row_sha256":"897d08828e777b6325cf7d4e8ff07078d34f8a40b0e75e17172d7fab0382080f"}],"predicate":"exact
    complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2040–2040, row_sha256 897d08828e777b6325cf7d4e8ff07078d34f8a40b0e75e17172d7fab0382080f
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"Botryane
    sesquiterpenoids","is_glycoside":"true","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"C[C@@H]1C[C@@H]([C@@H]2[C@@]3([C@H]1[C@H](OC[C@]3(CC2(C)C)C)O)O)OC(=O)C","standard_inchi_key":"QUGYVDURDBEQRB-CJNHKLDISA-N","superclass_results":"Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2318-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"QUGYVDURDBEQRB-CJNHKLDISA-N"}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure
    rows","query":[]}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/26/source_scope_inventory/source_taxa; /contexts/26/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/26/source_scope_inventory/nonorganism_matches; /contexts/26/source_scope_inventory/actual_assay_rows;
    /contexts/26/source_scope_inventory/blank_AID_sentinels; /contexts/26/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Exact source taxon and route lists; source_taxa is distinct from the empty
    forward/nonorganism and assay/related routes: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:332648","NCBITaxon:40559"]}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/9
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Complete relevant cached stanzas, with no fresh taxonomy verification:
    [{"complete_stanza":"[Term]\nid: NCBITaxon:40559\nname: Botrytis cinerea\nsynonym:
    \"Botryotinia fuckeliana\" EXACT []\nsynonym: \"Botrytis cinerea Pers., 1801\"
    EXACT []\nsynonym: \"Peziza fuckeliana\" EXACT []\nsynonym: \"Sclerotinia fuckeliana\"
    EXACT []\n\n","id":"NCBITaxon:40559","physical_line":18031},{"complete_stanza":"[Term]\nid:
    NCBITaxon:332648\nname: Botrytis cinerea B05.10\nsynonym: \"Botryotinia fuckeliana
    B05.10\" EXACT []\n\n","id":"NCBITaxon:332648","physical_line":83758}]'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /records/7/direct_companion_paths; /records/7/direct_companion_predicates
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Exact one-hop retained scope, without claim transfer: {"direct_companion_paths":["data/natural_products/terpenoids/1-epibotrydial.yaml","data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","data/natural_products/terpenoids/8-9-epibotrydial.yaml","data/natural_products/terpenoids/botrydial.yaml","data/natural_products/terpenoids/botrydienal.yaml","data/natural_products/terpenoids/botryenalol.yaml","data/natural_products/terpenoids/botryendial.yaml","data/natural_products/terpenoids/dehydrobotrydienol.yaml","data/natural_products/terpenoids/norbotrydialone-acetate.yaml","data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","data/natural_products/terpenoids/secobotrytriendiol.yaml","data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/terpenoids/1-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botrydienal.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botryenalol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/botryendial.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]},{"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0000631"]}]}'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch232-tentative/bgc-prep/bgc-conditional232-source-inventory-DATA-001.json
  locator: /contexts/3; /contexts/4; /contexts/5; /contexts/6; /contexts/7; /contexts/8;
    /contexts/9; /contexts/10; /contexts/11; /contexts/12; /contexts/13; /contexts/14;
    /contexts/15; /contexts/16; /contexts/20; /contexts/33; /contexts/34; /contexts/35;
    /contexts/36; /contexts/37
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: 'Whole context meanings and raw/history carries are attributed in the notes;
    exact identities and root scopes: [{"fullkey":"SJFIYVCSGNWVPJ-SDLFRHKASA-N","identifier":"naturalproductmech:mibig-acc775e1b7","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/1-epibotrydial.yaml"},{"fullkey":"MBHVNAKPTPFWNG-MYFMSEKESA-N","identifier":"naturalproductmech:mibig-1e06238f05","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-dehydroxy-dihydrobotrydialone.yaml"},{"fullkey":"QUGYVDURDBEQRB-VZJVBFQISA-N","identifier":"naturalproductmech:mibig-7950af79c1","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-epi-dihydrobotrydial.yaml"},{"fullkey":"MFOUCDNLAFNKML-SVLWDWOGSA-N","identifier":"naturalproductmech:mibig-e2d62600f5","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-oxo-dihydrobotrydial.yaml"},{"fullkey":"CAMCSBCRRUTMEK-OAHLLOKOSA-N","identifier":"naturalproductmech:mibig-7b45e48275","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-oxodehydrodihydrobotrydial.yaml"},{"fullkey":"PCEVLQFNPPWJEB-RFAUZJTJSA-N","identifier":"naturalproductmech:mibig-8b4cd14741","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/10-oxodihydrobotry-1-9-4-5-diendial.yaml"},{"fullkey":"JUCMRFKOKIZVPS-OAHLLOKOSA-N","identifier":"naturalproductmech:mibig-bbb6f44666","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/11-hydroxydehydrobotrydienol.yaml"},{"fullkey":"YPJRKTIWVUVMDI-LSDHHAIUSA-N","identifier":"naturalproductmech:mibig-10fda622fe","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/12-hydroxydehydrobotrydienol.yaml"},{"fullkey":"RVXLTRZIAMMATE-JMTSMVSISA-N","identifier":"naturalproductmech:mibig-0bd6ab53bc","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/4-acetoxytetrahydrobotryslactone.yaml"},{"fullkey":"SJFIYVCSGNWVPJ-PQVRDHEWSA-N","identifier":"naturalproductmech:mibig-a2b74a45ae","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/8-9-epibotrydial.yaml"},{"fullkey":"SJFIYVCSGNWVPJ-GKKOWQTJSA-N","identifier":"CHEBI:3159","mechanism_roots":["causal_graphs"],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botrydial.yaml"},{"fullkey":"CFAMAVBUWMXYLX-MEBBXXQBSA-N","identifier":"naturalproductmech:mibig-a1c6942987","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botrydienal.yaml"},{"fullkey":"DSVSTMJOGQEZJX-BYLNDYCFSA-N","identifier":"naturalproductmech:mibig-d567f1a1cd","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botryenalol.yaml"},{"fullkey":"QWZKEROSOALLJP-BYLNDYCFSA-N","identifier":"naturalproductmech:mibig-79ce4aca52","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/botryendial.yaml"},{"fullkey":"UQQKKLVKVVJDEX-OAHLLOKOSA-N","identifier":"naturalproductmech:mibig-247120aa23","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/dehydrobotrydienol.yaml"},{"fullkey":"OMZUEHMZFLBHNI-PCKWUFTNSA-N","identifier":"naturalproductmech:mibig-9b040d7e03","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/norbotrydialone-acetate.yaml"},{"fullkey":"GYABYKLKVQPSPD-NVWZYQMFSA-N","identifier":"naturalproductmech:mibig-2cef442430","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrydiene-3-10-15-triol.yaml"},{"fullkey":"GNMCOKDZWITFBO-MGNGBMTDSA-N","identifier":"naturalproductmech:mibig-f478b3a4f7","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrydiene-3-4-10-15-tetraol.yaml"},{"fullkey":"BHNACKMCMDASDB-UJNBGNEJSA-N","identifier":"naturalproductmech:mibig-ff72b656ae","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrytriendiol.yaml"},{"fullkey":"WLPOYIWCPMYYGM-KGRKPJGKSA-N","identifier":"naturalproductmech:mibig-1c14174a30","mechanism_roots":[],"owned_BGCs":["BGC0000631"],"path":"data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml"}]'
  snapshot_sha256: a5d9879ae844721ebd2f3256381d8d8812c258a09e1a2563bb253dd4cded901a
- evidence_id: bgc-2318-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: ChemicalStructure retains standardized-key limits and undefined stereocentres.
    ComputedClassification is a named/versioned prediction, not a source assertion
    or admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2318-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and absence
    of question-mark centre tags; it is not a blanket all-bond-geometry proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2318-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 974–1065
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: Maintained seeding preserves source structure and named/versioned model
    values separately from BGC/source compound classes and cross-reference assertions.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2318-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: One-record scientific review requires claim-level evidence and twelve dimensions
    with truthful partial completion and unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2318-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-03T23:30:34.168730Z'
  support: supports
  summary: The review does not edit records; overriding no-request instructions bound
    evidence access.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:06:58.212721Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8f5917ea73bc1cfaff0acd36b896a8bf563a39d9fa0c06095a640ade8a7f0eb5
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:07:23.062519Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 905f0c596112665df821aae49a7d58f13c781433d2bbd42c17b090f83c29ba07
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:07:42.545614Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:08:16.218635Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-232/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-232/native-current232-five-gates-execution-001.json
  accessed_at: '2026-11-03T23:08:27.888600Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 135ad5a077a12b8b149dc037f520fc077338ad6bf40df6dfb82dc6c51e9e139b
assessments:
- assessment_id: bgc-2318-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The MINTED identifier retains QUGYVDURDBEQRB-CJNHKLDISA-N for BGC0000631
    version 5, compound index 4. The exact ChEBI structure join is empty. The written
    npatlas:NPA019254 cross-reference is a literal source-row assertion, not a freshly
    resolved identity. Twenty direct locus companions include different full stereo
    keys; the 10-epi congener and Botrydial do not supply this owner with their identity,
    activity or mechanism.
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-grounding-owner
  - bgc-2318-source-mibig_compounds
  - bgc-2318-query-chebi_structures
  - bgc-2318-chemistry
  - bgc-2318-direct-contexts
  - bgc-2318-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: QUGYVDURDBEQRB-CJNHKLDISA-N; exact full retained source key, not a name
      or first-block substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2318-grounding-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-query-chebi_structures
    - bgc-2318-chemistry
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
  - name: grounding_scope
    value: MINTED; empty exact retained ChEBI structure join. Natural identity and
      external cross-references are not freshly verified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2318-grounding-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-query-chebi_structures
    - bgc-2318-chemistry
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
- assessment_id: bgc-2318-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms are neutral C17H28O5, one connected component with 22 heavy
    atoms and 24 bonds. The three-ring polycyclic framework has two hydroxyls, one
    cyclic ether/hemiacetal and a separate acetate ester. SMILES O8 connects C7 and
    C9; C7 also bears hydroxyl O16, while hydroxyl O17 is attached to C5. The acetate
    is C3-O18-C19(=O20)-C21. Seven tetrahedral centres are specified in both forms,
    with no unspecified potential centre, consistent with the true flag. All ten comparisons
    and the complete saved correspondence agree; full_graph_identity_established remains
    false. Atom numbers here are zero-based diagnostic indices, not biochemical locants.
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-grounding-owner
  - bgc-2318-chemistry
  - bgc-2318-topology
  - bgc-2318-diagnostic-acceptance
  - bgc-2318-structure-schema
  - bgc-2318-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Seven specified tetrahedral centres, no unresolved potential centre; true
      flag describes the retained representation, not fresh natural stereochemistry.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2318-grounding-owner
    - bgc-2318-chemistry
    - bgc-2318-topology
    - bgc-2318-diagnostic-acceptance
    - bgc-2318-structure-schema
    - bgc-2318-stereo-method
  - name: representation_correspondence
    value: All ten within-record comparisons true with a complete stored chirality-aware
      correspondence; full_graph_identity_established remains false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2318-grounding-owner
    - bgc-2318-chemistry
    - bgc-2318-topology
    - bgc-2318-diagnostic-acceptance
    - bgc-2318-structure-schema
    - bgc-2318-stereo-method
- assessment_id: bgc-2318-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: The producer assertion names Botrytis cinerea B05.10, NCBITaxon:332648,
    with BGC_CHARACTERIZED evidence. The four LOTUS occurrences instead name species-level
    NCBITaxon:40559; those taxa are not interchangeable. Cached Botryotinia synonyms
    preserve local name usage without a new taxonomy lookup. BGC0000631 version 5
    is active, questionable and complete; knock-out studies support CLUSTER_DEMONSTRATED
    at CP009816.1:2216500-2246000. A demonstrated locus link does not import the unselected
    Botrydial graph into this record.
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-origin-owner
  - bgc-2318-source-mibig_compounds
  - bgc-2318-cached-taxonomy
  - bgc-2318-source-routes
  - bgc-2318-direct-contexts
  - bgc-2318-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: Producer strain 332648 is distinct from occurrence species 40559; cached
      Botryotinia synonyms are local label evidence only.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2318-origin-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-cached-taxonomy
    - bgc-2318-source-routes
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
  - name: producer_evidence
    value: BGC_CHARACTERIZED for Botrytis cinerea B05.10, separate from four species-level
      LOTUS occurrence assertions.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2318-origin-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-cached-taxonomy
    - bgc-2318-source-routes
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
  - name: locus_evidence
    value: BGC0000631 v5 active/questionable/complete; knock-out studies; CLUSTER_DEMONSTRATED
      at CP009816.1:2216500-2246000.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2318-origin-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-cached-taxonomy
    - bgc-2318-source-routes
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
- assessment_id: bgc-2318-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: DOI:10.1021/cb800225v is explicitly COMPOUND_EVIDENCE provenance for the
    MIBiG producer/locus claims. Four written LOTUS assertions retain four different
    literal DOI strings. They are database occurrence triples, not four independently
    verified experiments, and they do not replace the compound-evidence citation or
    establish a producer strain. Shared BGC0000631 membership does not make each congener
    citation interchangeable.
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-origin-owner
  - bgc-2318-occurrence-owner
  - bgc-2318-source-mibig_compounds
  - bgc-2318-source-notes
  - bgc-2318-direct-contexts
  - bgc-2318-companion-boundaries
  - bgc-2318-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: COMPOUND_EVIDENCE DOI:10.1021/cb800225v versus four distinct LOTUS DOI
      triples; publication independence is unverified.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2318-origin-owner
    - bgc-2318-occurrence-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-source-notes
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
    - bgc-2318-source-lotus_occurrences
- assessment_id: bgc-2318-bioactivity
  area: evidence
  topic: Occurrence and activity
  outcome: supported
  summary: All four written Botrytis cinerea occurrence assertions reproduce the four
    exact LOTUS rows and their distinct DOI strings. They report occurrence rather
    than production by B05.10. No bioactivity or molecular target is written, and
    the exact retained PubChem, BindingDB and AntibioticMech joins are empty. No Botrydial
    activity or mechanism is transferred; these source limits do not establish inactivity.
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-occurrence-owner
  - bgc-2318-assay-owner
  - bgc-2318-grounding-owner
  - bgc-2318-source-mibig_compounds
  - bgc-2318-source-routes
  - bgc-2318-cached-taxonomy
  - bgc-2318-query-lotus_occurrences
  - bgc-2318-query-chebi_origins
  - bgc-2318-query-cyanometdb_occurrences
  - bgc-2318-query-pubchem_bioassay
  - bgc-2318-query-bindingdb_targets
  - bgc-2318-query-antibioticmech_inchikeys
  - bgc-2318-direct-contexts
  - bgc-2318-companion-boundaries
  - bgc-2318-source-lotus_occurrences
  dimensions:
  - name: occurrence_scope
    value: Four written species-level LOTUS assertions exactly retained; distinct
      DOI strings do not establish four independent experiments or strain production.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2318-occurrence-owner
    - bgc-2318-assay-owner
    - bgc-2318-grounding-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-source-routes
    - bgc-2318-cached-taxonomy
    - bgc-2318-query-lotus_occurrences
    - bgc-2318-query-chebi_origins
    - bgc-2318-query-cyanometdb_occurrences
    - bgc-2318-query-pubchem_bioassay
    - bgc-2318-query-bindingdb_targets
    - bgc-2318-query-antibioticmech_inchikeys
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
    - bgc-2318-source-lotus_occurrences
  - name: assay_target_scope
    value: No written activity/target, no retained assay/target match; no inactivity
      or congener transfer inference.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2318-occurrence-owner
    - bgc-2318-assay-owner
    - bgc-2318-grounding-owner
    - bgc-2318-source-mibig_compounds
    - bgc-2318-source-routes
    - bgc-2318-cached-taxonomy
    - bgc-2318-query-lotus_occurrences
    - bgc-2318-query-chebi_origins
    - bgc-2318-query-cyanometdb_occurrences
    - bgc-2318-query-pubchem_bioassay
    - bgc-2318-query-bindingdb_targets
    - bgc-2318-query-antibioticmech_inchikeys
    - bgc-2318-direct-contexts
    - bgc-2318-companion-boundaries
    - bgc-2318-source-lotus_occurrences
- assessment_id: bgc-2318-classification
  area: consistency
  topic: Classification
  outcome: concern
  summary: 'NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids / Sesquiterpenoids
    / Botryane sesquiterpenoids and is_glycoside:true. The saturated C5O cycle is
    integrated into the polycyclic scaffold: it shares carbon-framework connections
    and contains the C7-O8-C9 hemiacetal ether. The other carbon-O-carbon bridge is
    the acetate O18. The complete saved topology does not identify a separate sugar
    residue or a sugar-aglycone linkage, so the C5O motif alone cannot establish a
    glycoside. This is a concern about applicability of the preserved model output,
    not proof of a wrong source identity or schema violation. The schema explicitly
    treats this field as a named/versioned computation; there is no supported replacement
    value or source correction here.'
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-classification-owner
  - bgc-2318-source-npclassifier
  - bgc-2318-source-mibig_compounds
  - bgc-2318-chemistry
  - bgc-2318-topology
  - bgc-2318-structure-schema
  - bgc-2318-classification-seeder
  dimensions:
  - name: classification_applicability
    value: Concern limited to applicability of faithful versioned glycoside:true;
      integrated hemiacetal/acetate topology is not a sugar-residue assignment.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2318-classification-owner
    - bgc-2318-source-npclassifier
    - bgc-2318-source-mibig_compounds
    - bgc-2318-chemistry
    - bgc-2318-topology
    - bgc-2318-structure-schema
    - bgc-2318-classification-seeder
- assessment_id: bgc-2318-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: All twelve scientific dimensions were assessed using the complete current
    owner/history, actual canonical intake, retained source payloads and complete
    saved paired molecular tables. Five original local gates passed, but full QC,
    complete OAK authority coverage and fresh external verification remain unavailable.
    This owner has no mechanism root or selected reader. The bounded eight-table curation
    scan found no exact cohort-token match. No supported new maintained-source correction
    is established; scientific completion remains partial and native curation status
    is unchanged.
  target_ids:
  - naturalproductmech:mibig-b5ca742a5e
  evidence_ids:
  - bgc-2318-owner
  - bgc-2318-capture
  - bgc-2318-intake
  - bgc-2318-intake-acceptance
  - bgc-2318-inventory-acceptance
  - bgc-2318-plan
  - bgc-2318-plan-acceptance
  - bgc-2318-source-notes
  - bgc-2318-curation-scope
  - bgc-2318-diagnostic-execution
  - bgc-2318-diagnostic-acceptance
  - bgc-2318-native-acceptance
  - bgc-2318-review-profile
  - bgc-2318-review-skill
  dimensions:
  - name: review_completion
    value: Partial scientific review from retained evidence; full QC/OAK and fresh
      primary/taxonomic/natural-identity verification remain unavailable. No native
      status promotion.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2318-owner
    - bgc-2318-capture
    - bgc-2318-intake
    - bgc-2318-intake-acceptance
    - bgc-2318-inventory-acceptance
    - bgc-2318-plan
    - bgc-2318-plan-acceptance
    - bgc-2318-source-notes
    - bgc-2318-curation-scope
    - bgc-2318-diagnostic-execution
    - bgc-2318-diagnostic-acceptance
    - bgc-2318-native-acceptance
    - bgc-2318-review-profile
    - bgc-2318-review-skill
findings: []
actions: []
limitations:
- All evidence is retained locally. External identifiers, primary publications, taxonomy
  and natural stereochemical assignments were not refreshed under the absolute no-request
  instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gates and
  successful stored parses establish only their stated mechanical scope.
- Empty joins concern exact saved predicates and snapshots only. Shared loci, taxa,
  names and citations do not transfer compound-specific production, activity, mechanism
  or independent-study status.
- Six original undefined-stereo warnings remain global and unassigned to records.
  No additional molecular/YAML parse, source query or target invocation occurred during
  scientific authoring.
- No source record, native curation status or history is edited. Any later supported
  correction belongs to the maintained owners identified in the accepted canonical
  intake.
- The model glycoside:true value is retained faithfully. The integrated hemiacetal
  ring and acetate are not a separate sugar assignment; no replacement prediction
  or exact source correction is established.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and actual canonical intake were read. Full source payload
  and companion reading/carry attribution is retained in the pinned notes.
- 'BGC personally read all ten molecular forms for these five owners: 248 atom rows
  and 276 bond rows plus all scalars, ring/stereo/motif tables and original comparisons/maps.
  Diagnostic atom numbers are zero-based indices, not biochemical locants.'
- ROOT operated original activation/capture, collector, composer and canonical intakes;
  Native operated original gates and chemistry. BGC authored the collector/composer
  source and notes but invoked no target for these scientific assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-232
```
