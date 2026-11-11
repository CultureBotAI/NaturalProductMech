# Local evidence review: enterocin

- Review: 20261104T021206Z-enterocin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T01:29:01.318070Z
- Finished UTC: 2026-11-04T02:12:06.139118Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Enterocin preserves a shared full structure key across two independently described PKS loci and an explicitly partial Streptomyces maritimus EncM mechanism. Stored molecular forms agree locally; the Terpenoids model label and exact producer/source identity remain qualified, with the existing shared-structure discussion open.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2322; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5172626ac8 | data/natural_products/terpenoids/enterocin.yaml | generated | enterocin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for enterocin | passed | True | naturalproductmech:mibig-5172626ac8 | The original offline maintained reader returned the complete expected owner for order 2322: 1 graph, 4 nodes, 3 edges, 1 pathway entry and 3 history events. Complete owner equality and original exit 0 are ROOT-accepted. This is local preservation, not independent biological or primary-source verification. |
| strict_ten | passed | True | naturalproductmech:mibig-5172626ac8 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5172626ac8 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5172626ac8 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5172626ac8 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5172626ac8 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5172626ac8 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5172626ac8 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5172626ac8 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-5172626ac8.

The MINTED owner keeps complete key CTBBEXWJRAPJIZ-VHPBLNRZSA-N across BGC0000220 version 4 and BGC0002366 version 2. Their source SMILES serializations differ while the retained full key and InChI coincide. The existing OPEN shared-structure discussion is not closed by normalized-form agreement or reader preservation. No exact retained ChEBI structure match resolves it. Neoenterocin A and B have distinct full keys and remain direct context, not identity substitutes.

### Stored molecular representation

representation: supported. Targets: naturalproductmech:mibig-5172626ac8.

Both saved forms are neutral C22H20O10 with 32 atoms, 36 bonds and five rings in the saved basis. The central polycyclic framework is accompanied by phenyl and pyrone rings. Seven tetrahedral centres are specified. In the SMILES table the three carbonyls are 11=12, 17=18 and 27=28; hydroxyl oxygens 3, 15, 26 and 31 are attached to carbons 2, 14, 25 and 30. The methoxy connection is 7–8–9, and the lactone linkage 27(=28)–29–0 belongs to the integrated ring [0,1,2,25,27,29]. A C5O cycle containing a carbonyl carbon is not itself a sugar or glycosidic-linkage assignment. All ten comparisons and complete atom-count correspondence are true, but full_graph_identity_established remains false and natural identity is not independently proven.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-5172626ac8.

The two PKS source loci remain distinct. BGC0000220 version 4 names Streptomyces maritimus 115828, AF254925.1, complete cluster completeness and multiple knockout/enzymatic/heterologous/expression methods. BGC0002366 version 2 names Streptomyces sp. SCSIO 11863 taxon 1333476, MK388865.1, unknown completeness and heterologous/knockout methods. Both retain questionable quality, BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus grades. Those grades do not prove that every strain/source claim refers to an independently verified identical natural stereoisomer.

### Citation scope

evidence: supported. Targets: naturalproductmech:mibig-5172626ac8.

MIBiG ENTRY citations PMID24162851 and PMID31657934 belong to the respective loci and are not interchangeable compound-specific experiments. The historical EncM mechanism uses DOI 10.1021/ol0255155, 10.1038/nature12643 and 10.1016/s1074-5521(00)00044-2 plus separately typed UniProt/GenBank database assertions. Repeated complete evidence on three edges and one step does not multiply independent studies. Current local snapshots were read; the cited papers, protein records and their exact experimental scope were not freshly retrieved.

### Occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-5172626ac8.

Three retained LOTUS occurrences are Didemnum genus 107394 with DOI 10.1021/JO951794G and Streptomyces genus 1883 with two separate DOI strings. Their genus-level scope differs from both source producer taxa. They do not establish producer-strain identity, endogenous biosynthesis or three independent experiments. No written bioactivity object and no exact saved PubChem, BindingDB or AntibioticMech match is present; this is a bounded source result, not global inactivity.

### Computed classification applicability

consistency: concern. Targets: naturalproductmech:mibig-5172626ac8.

The named/versioned NPClassifier result is Terpenoids with blank finer classes and is_glycoside false. Both source loci are explicitly PKS, and the historical EncM mechanism acts on a polyketide precursor. This is a concrete applicability conflict between the computed coarse label and retained biosynthetic evidence, not a demonstrated failure to copy the model output. The schema keeps computed predictions separate from source assertions and admission criteria. No replacement prediction or wrong-structure conclusion is justified; the model limitation is explicit without a source-edit finding.

### Partial retained mechanism

graph: supported. Targets: naturalproductmech:mibig-5172626ac8.

The preserved partial EncM graph has four nodes and three edges: an ungrounded unrearranged polyketide is oxidized by grounded Q9KHK2, which triggers an ungrounded Favorskii-rearrangement process leading to an ungrounded rearranged intermediate. The one pathway step does not assign a stable substrate/product identifier. The raw notes explicitly retain further EncK activity before mature enterocin; this graph therefore does not claim complete terminal production. The S. maritimus mechanism must not transfer to SCSIO 11863 or its Neoenterocin companions.

### Protein and construct scope

grounding: supported. Targets: naturalproductmech:mibig-5172626ac8.

Q9KHK2 is retained as an unreviewed 464-residue EncM example from S. maritimus, with historical AF254925.1 / AAF81732.1 sequence correspondence. Database assertions remain distinct from the biochemical/structural and gene-inactivation evidence. Grounding a protein node does not verify an assay construct or reproduce flavin-mediated oxidation/Favorskii chemistry. No fresh sequence translation, alignment, domain/construct boundary or protein-record validation occurred; unstable immediate substrates and products remain deliberately ungrounded.

### Scientific completion

completeness: unknown. Targets: naturalproductmech:mibig-5172626ac8.

Complete owner/history, both locus payloads, actual intake, three occurrence rows, companion scope and both full molecular forms have been assessed. The exact original maintained-reader preservation contract is now ROOT-accepted without adding biological or primary-source verification. The OPEN shared-structure discussion, computed-label applicability, fresh primary/protein verification and unavailable Full QC/OAK coverage remain explicit. No record/native-status/history edit is made and completion is partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2322-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/enterocin.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner and all 3 history entries; native curation_status remains SEEDED. |
| bgc-2322-capture | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/1 | supports | Complete captured owner preserves every written field/history; selected maintained-reader applicability is true and no component reference is declared. |
| bgc-2322-intake | /private/tmp/npm-review-work/shared-next-batch233/intakes/2322-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-5172626ac8; 41 pinned input placements and explicit maintained source/curator ownership. |
| bgc-2322-grounding-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"chemical_structure":{"smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000220"},"discussions":[{"discussion_id":"shared-structure","kind":"CURATION_TODO","prompt":"This structure is reported by more than one MIBiG entry: BGC0000220, BGC0002366. Confirm they describe the same compound rather than an upstream cross-reference error.","status":"OPEN"}],"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-5172626ac8","label":"enterocin","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-5172626ac8","source":"MIBIG","source_id":"BGC0000220","source_label":"enterocin","source_version":"4"},{"minted_identifier":"naturalproductmech:mibig-8209405036","source":"MIBIG","source_id":"BGC0002366","source_label":"enterocin","source_version":"2"}],"xrefs":["npatlas:NPA09644","npatlas:NPA009644","pubchem:23654446"]} |
| bgc-2322-origin-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000220","bgc_class":["PKS"],"entry_status":"active","entry_version":"4","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000220 entry version 4; citation taken from the entry level","reference":"PMID:24162851"}],"genome_accession":"genbank:AF254925.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Knock-out studies","Enzymatic assays","Heterologous expression","Gene expression correlated with compound production"],"organism_label":"Streptomyces maritimus","organism_taxon_id":"NCBITaxon:115828"},{"accession":"mibig:BGC0002366","bgc_class":["PKS"],"entry_status":"active","entry_version":"2","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0002366 entry version 2; citation taken from the entry level","reference":"PMID:31657934"}],"genome_accession":"genbank:MK388865.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Heterologous expression","Knock-out studies"],"organism_label":"Streptomyces sp. SCSIO 11863","organism_taxon_id":"NCBITaxon:1333476"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000220","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0000220 entry version 4; citation taken from the entry level","reference":"PMID:24162851"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus evidence: Knock-out studies&#124;Enzymatic assays&#124;Heterologous expression&#124;Gene expression correlated with compound production. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"4","taxon_id":"NCBITaxon:115828","taxon_label":"Streptomyces maritimus"},{"biosynthetic_gene_cluster":"mibig:BGC0002366","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0002366 entry version 2; citation taken from the entry level","reference":"PMID:31657934"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus evidence: Heterologous expression&#124;Knock-out studies. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"2","taxon_id":"NCBITaxon:1333476","taxon_label":"Streptomyces sp. SCSIO 11863"}],"producer_taxon_groups":["ACTINOBACTERIAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-5172626ac8","source":"MIBIG","source_id":"BGC0000220","source_label":"enterocin","source_version":"4"},{"minted_identifier":"naturalproductmech:mibig-8209405036","source":"MIBIG","source_id":"BGC0002366","source_label":"enterocin","source_version":"2"}]} |
| bgc-2322-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","occurrence_taxon_groups":["ACTINOBACTERIAL","CHORDATE"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1021/JO951794G"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q153605","source":"LOTUS","taxon_id":"NCBITaxon:107394","taxon_label":"Didemnum","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1002/MRC.4384"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1144013","source":"LOTUS","taxon_id":"NCBITaxon:1883","taxon_label":"Streptomyces","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0040-4020(96)00391-2"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q1144013","source":"LOTUS","taxon_id":"NCBITaxon:1883","taxon_label":"Streptomyces","taxon_source":"NCBITaxon"}]} |
| bgc-2322-assay-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {} |
| bgc-2322-classification-owner | /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"bgc_class":["PKS"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":[],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":[],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2322-chemistry | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/smiles/status; /records/1/inchi/status; /records/1/smiles/computed; /records/1/inchi/computed; /records/1/comparisons; /records/1/atom_correspondence | supports | Both stored forms parsed. Exact original comparison/correspondence and stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[12,8,19,26,15,11,6,10,29,0,7,13,22,30,20,27,16,14,23,9,4,2,1,3,5,21,28,18,25,31,17,24]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000220"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Specified":7},"smiles":{"Atom_Tetrahedral:Specified":7}}} |
| bgc-2322-topology | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json; /records/1/smiles/computed; /records/1/inchi/computed; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence | supports | Complete saved topology interpretation: Both saved forms are neutral C22H20O10 with 32 atoms, 36 bonds and five rings in the saved basis. The central polycyclic framework is accompanied by phenyl and pyrone rings. Seven tetrahedral centres are specified. In the SMILES table the three carbonyls are 11=12, 17=18 and 27=28; hydroxyl oxygens 3, 15, 26 and 31 are attached to carbons 2, 14, 25 and 30. The methoxy connection is 7–8–9, and the lactone linkage 27(=28)–29–0 belongs to the integrated ring [0,1,2,25,27,29]. A C5O cycle containing a carbonyl carbon is not itself a sugar or glycosidic-linkage assignment. All ten comparisons and complete atom-count correspondence are true, but full_graph_identity_established remains false and natural identity is not independently proven. |
| bgc-2322-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-execution-001.json; Whole current diagnostic-execution | supports | ROOT operated one original stored-form diagnostic, exit 0, one attempt, preserved original streams and closed environment. This execution receipt is not independent scientific verification. |
| bgc-2322-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-diagnostic-acceptance-001.json; Whole current diagnostic-acceptance | supports | ROOT accepts the original 20 stored parses and exact original comparisons/key/capture joins. Two original undefined-stereo warnings remain global and unassigned. Acceptance establishes local execution integrity, not natural identity or full graph proof. |
| bgc-2322-native-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-native-gates-acceptance-001.json; Whole current native-acceptance | supports | Five original local gates passed; all_native_gates_passed is false because full QC and complete OAK coverage are unavailable. Mechanical success is not a scientific verdict. |
| bgc-2322-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-intake-acceptance-001.json; Whole current intake-acceptance | supports | ROOT accepts ten actual canonical intakes and exact current source ownership/input plans; scientific assessment is separate. |
| bgc-2322-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-source-inventory-acceptance-001.json; Whole current inventory-acceptance | supports | ROOT accepts the original saved inventory and current input/raw/query/row joins. Complete meaning reading is separately attributed in source notes. |
| bgc-2322-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-input-plan-acceptance-001.json; Whole current plan-acceptance | supports | ROOT accepts the actual input plan and preserved source contexts, without a scientific verdict. |
| bgc-2322-plan | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-target-input-plan-001.json; /records/1 | supports | Current one-record input plan with exact direct companions, predicates and input roles. |
| bgc-2322-source-notes | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading and exact carries, with compound-specific cautions; source planning did not adjudicate pre-intake science. |
| bgc-2322-curation-scope | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json; /curation | supports | Eight explicitly opened implemented curation tables, including ignored files, were scanned over 169 distinct exact literals with zero textual hits in this bounded scope. Reserved decisions.tsv was not consumed. |
| bgc-2322-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":296,"physical_line":296,"raw_tsv_record":"BGC0000220\t4\tactive\tquestionable\tcomplete\tenterocin\t1\t[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O\tInChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1\tCTBBEXWJRAPJIZ-VHPBLNRZSA-N\ttrue\t\tnpatlas:NPA09644\tNCBITaxon:115828\tStreptomyces maritimus\tPKS\tType II\tAF254925.1\t\t\tKnock-out studies&#124;Enzymatic assays&#124;Heterologous expression&#124;Gene expression correlated with compound production\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:24162851\tENTRY\n","row":{"bgc_classes":"PKS","bgc_subclasses":"Type II","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA09644","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"AF254925.1","locus_evidence_methods":"Knock-out studies&#124;Enzymatic assays&#124;Heterologous expression&#124;Gene expression correlated with compound production","locus_from":"","locus_to":"","mibig_accession":"BGC0000220","primary_reference":"PMID:24162851","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:115828","taxon_label":"Streptomyces maritimus"},"row_sha256":"de3e7d236d2be8184f7338e6c77023cf08e53df56c6075b5aa5c4d5415dbde3b"},{"last_physical_line":2905,"physical_line":2905,"raw_tsv_record":"BGC0002366\t2\tactive\tquestionable\tunknown\tenterocin\t1\tCOC1=CC(=O)OC(=C1)[C@@H]2[C@@]3(C[C@@H]4[C@H]([C@]2([C@@H]([C@]3(C(=O)O4)O)C(=O)C5=CC=CC=C5)O)O)O\tInChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1\tCTBBEXWJRAPJIZ-VHPBLNRZSA-N\ttrue\t\tnpatlas:NPA009644&#124;pubchem:23654446&#124;chemspider:19978603\tNCBITaxon:1333476\tStreptomyces sp. SCSIO 11863\tPKS\tUnknown\tMK388865.1\t\t\tHeterologous expression&#124;Knock-out studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:31657934\tENTRY\n","row":{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA009644&#124;pubchem:23654446&#124;chemspider:19978603","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK388865.1","locus_evidence_methods":"Heterologous expression&#124;Knock-out studies","locus_from":"","locus_to":"","mibig_accession":"BGC0002366","primary_reference":"PMID:31657934","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"COC1=CC(=O)OC(=C1)[C@@H]2[C@@]3(C[C@@H]4[C@H]([C@]2([C@@H]([C@]3(C(=O)O4)O)C(=O)C5=CC=CC=C5)O)O)O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1333476","taxon_label":"Streptomyces sp. SCSIO 11863"},"row_sha256":"a72060bc915d89b85b8d3832c0e77406ddd40e3cf33520afd7fa8e1a4ea9da77"}],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 296–296, row_sha256 de3e7d236d2be8184f7338e6c77023cf08e53df56c6075b5aa5c4d5415dbde3b; physical lines 2905–2905, row_sha256 a72060bc915d89b85b8d3832c0e77406ddd40e3cf33520afd7fa8e1a4ea9da77 | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"PKS","bgc_subclasses":"Type II","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA09644","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"AF254925.1","locus_evidence_methods":"Knock-out studies&#124;Enzymatic assays&#124;Heterologous expression&#124;Gene expression correlated with compound production","locus_from":"","locus_to":"","mibig_accession":"BGC0000220","primary_reference":"PMID:24162851","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:115828","taxon_label":"Streptomyces maritimus"},{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA009644&#124;pubchem:23654446&#124;chemspider:19978603","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK388865.1","locus_evidence_methods":"Heterologous expression&#124;Knock-out studies","locus_from":"","locus_to":"","mibig_accession":"BGC0002366","primary_reference":"PMID:31657934","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"COC1=CC(=O)OC(=C1)[C@@H]2[C@@]3(C[C@@H]4[C@H]([C@]2([C@@H]([C@]3(C(=O)O4)O)C(=O)C5=CC=CC=C5)O)O)O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1333476","taxon_label":"Streptomyces sp. SCSIO 11863"}] |
| bgc-2322-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":900,"physical_line":900,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\tDidemnum\tNCBITaxon:107394\thttp://www.wikidata.org/entity/Q153605\t10.1021/JO951794G\thttp://www.wikidata.org/entity/Q72470750\n","row":{"organism_name":"Didemnum","organism_wikidata":"http://www.wikidata.org/entity/Q153605","reference_doi":"10.1021/JO951794G","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:107394"},"row_sha256":"03755c2fc69a18068f4ff0c4d700db55018b801718a05e169e105b317b3221b1"},{"last_physical_line":901,"physical_line":901,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1002/MRC.4384\thttp://www.wikidata.org/entity/Q72470750\n","row":{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1002/MRC.4384","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"},"row_sha256":"43b791fac02f6586bc050efd6035a312c96dd49135c49945d89d625640690a67"},{"last_physical_line":902,"physical_line":902,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1016/0040-4020(96)00391-2\thttp://www.wikidata.org/entity/Q72470750\n","row":{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1016/0040-4020(96)00391-2","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"},"row_sha256":"56dd3fb7985c7b87653e000dcbd4537f57c3285f5c4140ae766d3d168e9cd142"}],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 900–900, row_sha256 03755c2fc69a18068f4ff0c4d700db55018b801718a05e169e105b317b3221b1; physical lines 901–901, row_sha256 43b791fac02f6586bc050efd6035a312c96dd49135c49945d89d625640690a67; physical lines 902–902, row_sha256 56dd3fb7985c7b87653e000dcbd4537f57c3285f5c4140ae766d3d168e9cd142 | supports | Complete retained physical row payloads, every field: [{"organism_name":"Didemnum","organism_wikidata":"http://www.wikidata.org/entity/Q153605","reference_doi":"10.1021/JO951794G","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:107394"},{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1002/MRC.4384","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"},{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1016/0040-4020(96)00391-2","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"}] |
| bgc-2322-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":340,"physical_line":340,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\t[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O\tTerpenoids\t\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","superclass_results":""},"row_sha256":"204bf8db5f5bfc6bd767e6b511371801e4cb9f7f8678f6110a0310411e377202"}],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 340–340, row_sha256 204bf8db5f5bfc6bd767e6b511371801e4cb9f7f8678f6110a0310411e377202 | supports | Complete retained physical row payloads, every field: [{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","superclass_results":""}] |
| bgc-2322-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"} |
| bgc-2322-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2322-source-routes | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/18/source_scope_inventory/source_taxa; /contexts/18/source_scope_inventory/forward_taxon_merge_matches; /contexts/18/source_scope_inventory/nonorganism_matches; /contexts/18/source_scope_inventory/actual_assay_rows; /contexts/18/source_scope_inventory/blank_AID_sentinels; /contexts/18/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists; source_taxa is distinct from the empty forward/nonorganism and assay/related routes: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:107394","NCBITaxon:115828","NCBITaxon:1333476","NCBITaxon:1883"]} |
| bgc-2322-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/44; /cached_taxonomy/whole_stanzas/45; /cached_taxonomy/whole_stanzas/88 | supports | Complete relevant cached stanzas, with no fresh taxonomy verification: [{"complete_stanza":"[Term]\nid: NCBITaxon:1883\nname: Streptomyces\nsynonym: \"\\\"Microstreptospora\\\" Yan et al.\" EXACT []\nsynonym: \"Actinopycnidium Krasil'nikov 1962\" EXACT []\nsynonym: \"Actinosporangium Krasil'nikov and Yuan 1961\" EXACT []\nsynonym: \"Chainia\" EXACT []\nsynonym: \"Elytrosporangium Falcao de Morais et al. 1966\" EXACT []\nsynonym: \"Kitasatoa Matsumae and Hata 1968 (Approved Lists 1980)\" EXACT []\nsynonym: \"Microellobosporia\" EXACT []\nsynonym: \"Streptoverticillium Baldacci 1958\" EXACT []\n\n","id":"NCBITaxon:1883","physical_line":2798},{"complete_stanza":"[Term]\nid: NCBITaxon:107394\nname: Didemnum\n\n","id":"NCBITaxon:107394","physical_line":43346},{"complete_stanza":"[Term]\nid: NCBITaxon:115828\nname: Streptomyces maritimus\nsynonym: \"'Streptomyces maritimus'\" EXACT []\n\n","id":"NCBITaxon:115828","physical_line":45357},{"complete_stanza":"[Term]\nid: NCBITaxon:1333476\nname: Streptomyces sp. SCSIO 11863\n\n","id":"NCBITaxon:1333476","physical_line":126552}] |
| bgc-2322-direct-contexts | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /records/1/direct_companion_paths; /records/1/direct_companion_predicates | supports | Exact one-hop scope, with no claim transfer: {"direct_companion_paths":["data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml","data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0002366"]},{"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0002366"]}]} |
| bgc-2322-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json; /contexts/6; /contexts/7 | supports | Complete context meanings/raw histories are attributed in the notes; exact identity/root boundaries: [{"declared_mechanism_roots_literal":[],"history_count":2,"identifier":"naturalproductmech:mibig-6e0973d7ec","label":"neoenterocin A","owned_bgc_ids":["BGC0002366"],"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml","standard_inchi_key":"JBIMWARAATZDME-YKWSONSWSA-N"},{"declared_mechanism_roots_literal":[],"history_count":2,"identifier":"naturalproductmech:mibig-65ffea3920","label":"neoenterocin B","owned_bgc_ids":["BGC0002366"],"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml","standard_inchi_key":"BYCKRSGGJOJCOA-RHPXVONCSA-N"}] |
| bgc-2322-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | The structure flag describes undefined stereocentres. ComputedClassification is explicitly a named/versioned prediction from structure, never a source assertion or an admission criterion. |
| bgc-2322-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and absence of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity proof. |
| bgc-2322-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 972–1020 | supports | Maintained seeding preserves lead source structures and named/versioned computed predictions separately; the computed pathway can control filing without becoming a source assertion. |
| bgc-2322-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record claim-level scientific review requires twelve dimensions and truthful partial completion/unavailable-check limits. |
| bgc-2322-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit source records; the overriding absolute no-request instruction limits evidence access to retained local files. |
| bgc-2322-reader-DATA | /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json; /order; /status; /reader_call_count; /raw_owner; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials; /errors; /external_requests; /molecular_parses; /retries; /limitations | supports | Complete raw/expected/returned owner equality, original counts and exact positive content are retained. One known import-time IPv6 socket-construction capability probe was denied before action; no external request, unexpected denial, retry or molecular parse occurred. Preservation is not independent mechanism/protein/primary-source verification. |
| bgc-2322-reader-execution | /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-reader-execution-001.json; /observer; /order; /command; /exit_code; /stderr; /retries; /external_requests; /original_tool | supports | Native operated the original maintained reader once, exit 0, with empty stderr and zero retries/external requests. The original terminal is preserved in the execution receipt. |
| bgc-2322-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch233/root-current233-enterocin-maintained-reader-acceptance-001.json; /status; /accepted; /order; /DATA; /execution; /original_tools; /verification; /review_check_contract; /reading_scope; /observer_correction | supports | ROOT accepts the exact original reader, complete owner/positive-content equality and current authority joins. Every launch environment key is unchanged; the observed runtime-only encoding key is explicit. No observer correction caused a reader rerun. |
| bgc-2322-graph-0 | /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json; /resolved_view/causal_graphs/0 | supports | Complete graph metadata, nodes, edges, qualifiers and every evidence placement: {"description":"Partial Streptomyces maritimus enterocin biosynthesis graph for the EncM-catalyzed oxidation that triggers the Favorskii-type rearrangement.","edges":[{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster and showed that these genes are needed for the Favorskii-like rearrangement in enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation of either gene terminated enterocin production and caused the accumulation of four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel et al. biochemically and structurally characterized the EncM flavoenzyme oxidation that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A 21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin family of polyketides from 'S. maritimus' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"The direct EncM substrate is an unstable, unrearranged poly-beta-carbonyl rather than a ChEBI-grounded stable pathway intermediate.","object":"encm","predicate":"is oxidized by","subject":"unrearranged_polyketide"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster and showed that these genes are needed for the Favorskii-like rearrangement in enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation of either gene terminated enterocin production and caused the accumulation of four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel et al. biochemically and structurally characterized the EncM flavoenzyme oxidation that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A 21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin family of polyketides from 'S. maritimus' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"EncM performs the dual oxidation that initiates the Favorskii-type rearrangement; EncK also acts before mature enterocin is formed.","object":"favorskii_rearrangement","predicate":"triggers","subject":"encm"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster and showed that these genes are needed for the Favorskii-like rearrangement in enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation of either gene terminated enterocin production and caused the accumulation of four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel et al. biochemically and structurally characterized the EncM flavoenzyme oxidation that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A 21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin family of polyketides from 'S. maritimus' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"The rearranged pathway intermediate is left ungrounded because the exact immediate product of EncM in vivo is not a stable public ChEBI term.","object":"rearranged_enterocin_intermediate","predicate":"forms","subject":"favorskii_rearrangement"}],"graph_id":"enterocin-encm-biosynthesis","nodes":[{"grounding_status":"UNGROUNDED","label":"unrearranged poly-beta-carbonyl intermediate","node_id":"unrearranged_polyketide","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:Q9KHK2","label":"EncM","node_id":"encm","node_type":"ENZYME"},{"grounding_status":"UNGROUNDED","label":"Favorskii-type rearrangement","node_id":"favorskii_rearrangement","node_type":"PROCESS"},{"grounding_status":"UNGROUNDED","label":"Favorskii-rearranged enterocin intermediate","node_id":"rearranged_enterocin_intermediate","node_type":"PRECURSOR"}],"scope":"BIOSYNTHESIS"} |
| bgc-2322-pathway-0 | /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway/0 | supports | Complete retained pathway item with all evidence, qualifiers and grounding: {"enzyme_id":"UniProtKB:Q9KHK2","enzyme_label":"EncM","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster and showed that these genes are needed for the Favorskii-like rearrangement in enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation of either gene terminated enterocin production and caused the accumulation of four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel et al. biochemically and structurally characterized the EncM flavoenzyme oxidation that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A 21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin family of polyketides from 'S. maritimus' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"This curates only the Streptomyces maritimus EncM flavin-mediated oxidation that initiates the Favorskii-type rearrangement in enterocin biosynthesis; the reactive poly-beta-carbonyl substrate and rearranged pathway intermediate remain ungrounded.","step_number":1} |
| bgc-2322-history | /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json; /resolved_view/curation_history | supports | Complete retained owner history: [{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-10T05:54:04Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-25T03:01:43Z"},{"action":"RECORD_CURATED","changes":"Added the Streptomyces maritimus EncM flavin-mediated oxidation step and BIOSYNTHESIS causal graph grounded to UniProtKB:Q9KHK2.","curator":"codex","llm_assisted":true,"timestamp":"2026-09-27T07:55:36Z"}] |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-233/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-233/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-233/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-233/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-233/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external identifier, taxonomy, primary publication, protein sequence or natural stereochemical assignment was refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gate, parse and maintained-reader success establish only their explicit mechanical scope.
- Exact no-match joins are bounded by saved predicates/snapshots. Shared names, loci, taxa, citations or companions do not transfer compound-specific production, activity, mechanism or independent-study status.
- Two original undefined-stereo warnings are global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during this scientific authoring.
- No source record, native status or history is edited. Any supported future correction belongs to the maintained source/curator owners listed in the actual canonical intake.
- The named/versioned NPClassifier result is Terpenoids with blank finer classes and is_glycoside false. Both source loci are explicitly PKS, and the historical EncM mechanism acts on a polyketide precursor. This is a concrete applicability conflict between the computed coarse label and retained biosynthetic evidence, not a demonstrated failure to copy the model output. The schema keeps computed predictions separate from source assertions and admission criteria. No replacement prediction or wrong-structure conclusion is justified; the model limitation is explicit without a source-edit finding.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual intake were read. Full source payload meanings and direct-companion/raw-history carries remain explicitly attributed in pinned source notes.
- BGC personally read all ten first-five molecular forms: 236 atom rows / 260 bond rows plus complete scalars, ring/stereo/motif tables and original comparisons/maps. Diagnostic indices are zero-based, not biochemical locants.
- ROOT operated original activation/capture, collector/composer, canonical intakes and chemistry; Native operated original gates and maintained readers. BGC authored source planning and these scientific assessments without invoking any target during scientific authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T021206Z-enterocin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: enterocin'
started_at: '2026-11-04T01:29:01.318070Z'
finished_at: '2026-11-04T02:12:06.139118Z'
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
summary: Enterocin preserves a shared full structure key across two independently
  described PKS loci and an explicitly partial Streptomyces maritimus EncM mechanism.
  Stored molecular forms agree locally; the Terpenoids model label and exact producer/source
  identity remain qualified, with the existing shared-structure discussion open.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml
    sha256: 9a16c07af26f9fc742d9f6cc35b9e2d57b43fca2274b4c97ea8969e47a3ace8c
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml
    sha256: 34699c06d18059107f9eaa8492a700f51a01020a0c1e28194237862794b25bf7
    role: context
  - path: data/natural_products/terpenoids/enterocin.yaml
    sha256: 1bcd375c4b9badc3e68431915d75fa6a6b8a83ecc00123d15e71481c327075f2
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
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2322; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5172626ac8
targets:
- target_id: naturalproductmech:mibig-5172626ac8
  path: data/natural_products/terpenoids/enterocin.yaml
  label: enterocin
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
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/enterocin.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- name: Complete offline maintained reader for enterocin
  status: passed
  required: true
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch233/read-selected-mechanism-guarded-001.py
    2322 fd189cfeef53223564efc2e151e9ab13c9d4ff0eedbf2e9be9a97d35e2761db9 03110c0de1c3ec7dace02229bb009b2ab31dab824375a47020723f413346a8b4
    c6a354765f2590d29898156c1d68bac79ab532abcad168d75c278a0a0e3df077 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
    c40437dc157b29c3b4bf647a7e232564fff639b957c0ac7b3a604fc9c490d85a
  exit_code: 0
  check_id: maintained-mechanism-reader
  summary: 'The original offline maintained reader returned the complete expected
    owner for order 2322: 1 graph, 4 nodes, 3 edges, 1 pathway entry and 3 history
    events. Complete owner equality and original exit 0 are ROOT-accepted. This is
    local preservation, not independent biological or primary-source verification.'
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-reader-DATA
  - bgc-2322-reader-execution
  - bgc-2322-reader-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  command: just validate-strict data/natural_products/terpenoids/ent-quiannulatene.yaml
    data/natural_products/terpenoids/enterocin.yaml data/natural_products/terpenoids/eremophilene.yaml
    data/natural_products/terpenoids/euphol.yaml data/natural_products/terpenoids/eutypinic-acid.yaml
    data/natural_products/terpenoids/fumihopaside-a.yaml data/natural_products/terpenoids/fusarochromanone.yaml
    data/natural_products/terpenoids/geosmin.yaml data/natural_products/terpenoids/gibberellin.yaml
    data/natural_products/terpenoids/helvolic-acid.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-233/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-5172626ac8
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-233/validate-all-001.tsv
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
  - naturalproductmech:mibig-5172626ac8
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
  - naturalproductmech:mibig-5172626ac8
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
  - naturalproductmech:mibig-5172626ac8
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-233/review-queue-001.tsv
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
  - naturalproductmech:mibig-5172626ac8
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2322-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/enterocin.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Complete current owner and all 3 history entries; native curation_status
    remains SEEDED.
  snapshot_sha256: 1bcd375c4b9badc3e68431915d75fa6a6b8a83ecc00123d15e71481c327075f2
- evidence_id: bgc-2322-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/1
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Complete captured owner preserves every written field/history; selected
    maintained-reader applicability is true and no component reference is declared.
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: bgc-2322-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/intakes/2322-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Actual canonical intake for naturalproductmech:mibig-5172626ac8; 41 pinned
    input placements and explicit maintained source/curator ownership.
  snapshot_sha256: 03110c0de1c3ec7dace02229bb009b2ab31dab824375a47020723f413346a8b4
- evidence_id: bgc-2322-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000220"},"discussions":[{"discussion_id":"shared-structure","kind":"CURATION_TODO","prompt":"This
    structure is reported by more than one MIBiG entry: BGC0000220, BGC0002366. Confirm
    they describe the same compound rather than an upstream cross-reference error.","status":"OPEN"}],"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-5172626ac8","label":"enterocin","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-5172626ac8","source":"MIBIG","source_id":"BGC0000220","source_label":"enterocin","source_version":"4"},{"minted_identifier":"naturalproductmech:mibig-8209405036","source":"MIBIG","source_id":"BGC0002366","source_label":"enterocin","source_version":"2"}],"xrefs":["npatlas:NPA09644","npatlas:NPA009644","pubchem:23654446"]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: bgc-2322-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0000220","bgc_class":["PKS"],"entry_status":"active","entry_version":"4","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000220 entry version 4; citation taken from the entry level","reference":"PMID:24162851"}],"genome_accession":"genbank:AF254925.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Knock-out
    studies","Enzymatic assays","Heterologous expression","Gene expression correlated
    with compound production"],"organism_label":"Streptomyces maritimus","organism_taxon_id":"NCBITaxon:115828"},{"accession":"mibig:BGC0002366","bgc_class":["PKS"],"entry_status":"active","entry_version":"2","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0002366 entry version 2; citation taken from the entry level","reference":"PMID:31657934"}],"genome_accession":"genbank:MK388865.1","link_evidence_basis":"CLUSTER_DEMONSTRATED","locus_evidence_methods":["Heterologous
    expression","Knock-out studies"],"organism_label":"Streptomyces sp. SCSIO 11863","organism_taxon_id":"NCBITaxon:1333476"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0000220","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0000220 entry version 4; citation taken from the entry level","reference":"PMID:24162851"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus
    evidence: Knock-out studies|Enzymatic assays|Heterologous expression|Gene expression
    correlated with compound production. That evidence grades the LOCUS as CLUSTER_DEMONSTRATED;
    this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"4","taxon_id":"NCBITaxon:115828","taxon_label":"Streptomyces
    maritimus"},{"biosynthetic_gene_cluster":"mibig:BGC0002366","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0002366 entry version 2; citation taken from the entry level","reference":"PMID:31657934"}],"evidence_basis":"BGC_CHARACTERIZED","notes":"Locus
    evidence: Heterologous expression|Knock-out studies. That evidence grades the
    LOCUS as CLUSTER_DEMONSTRATED; this field grades the taxon claim, which is a different
    question.","source":"MIBIG","source_version":"2","taxon_id":"NCBITaxon:1333476","taxon_label":"Streptomyces
    sp. SCSIO 11863"}],"producer_taxon_groups":["ACTINOBACTERIAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-5172626ac8","source":"MIBIG","source_id":"BGC0000220","source_label":"enterocin","source_version":"4"},{"minted_identifier":"naturalproductmech:mibig-8209405036","source":"MIBIG","source_id":"BGC0002366","source_label":"enterocin","source_version":"2"}]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: bgc-2322-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure,
    so the record keeps a content-hashed identifier.","occurrence_taxon_groups":["ACTINOBACTERIAL","CHORDATE"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1021/JO951794G"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q153605","source":"LOTUS","taxon_id":"NCBITaxon:107394","taxon_label":"Didemnum","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1002/MRC.4384"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1144013","source":"LOTUS","taxon_id":"NCBITaxon:1883","taxon_label":"Streptomyces","taxon_source":"NCBITaxon"},{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1016/0040-4020(96)00391-2"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q1144013","source":"LOTUS","taxon_id":"NCBITaxon:1883","taxon_label":"Streptomyces","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: bgc-2322-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: bgc-2322-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"bgc_class":["PKS"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":[],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":[],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: 172447fb6267d84895ab4baa33cb1fba300712693dce13182a44712ad73b6927
- evidence_id: bgc-2322-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/smiles/status; /records/1/inchi/status;
    /records/1/smiles/computed; /records/1/inchi/computed; /records/1/comparisons;
    /records/1/atom_correspondence
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison/correspondence and
    stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[12,8,19,26,15,11,6,10,29,0,7,13,22,30,20,27,16,14,23,9,4,2,1,3,5,21,28,18,25,31,17,24]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0000220"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Specified":7},"smiles":{"Atom_Tetrahedral:Specified":7}}}'
  snapshot_sha256: 98d9bae4e307da83403d9b3e783897999469aca3e863fd37b097f1688bf1d4ee
- evidence_id: bgc-2322-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/smiles/computed; /records/1/inchi/computed; /records/1/declared_structure;
    /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete saved topology interpretation: Both saved forms are neutral C22H20O10
    with 32 atoms, 36 bonds and five rings in the saved basis. The central polycyclic
    framework is accompanied by phenyl and pyrone rings. Seven tetrahedral centres
    are specified. In the SMILES table the three carbonyls are 11=12, 17=18 and 27=28;
    hydroxyl oxygens 3, 15, 26 and 31 are attached to carbons 2, 14, 25 and 30. The
    methoxy connection is 7–8–9, and the lactone linkage 27(=28)–29–0 belongs to the
    integrated ring [0,1,2,25,27,29]. A C5O cycle containing a carbonyl carbon is
    not itself a sugar or glycosidic-linkage assignment. All ten comparisons and complete
    atom-count correspondence are true, but full_graph_identity_established remains
    false and natural identity is not independently proven.'
  snapshot_sha256: 98d9bae4e307da83403d9b3e783897999469aca3e863fd37b097f1688bf1d4ee
- evidence_id: bgc-2322-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/chemistry-local/diagnostic-execution-001.json
  locator: Whole current diagnostic-execution
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: ROOT operated one original stored-form diagnostic, exit 0, one attempt,
    preserved original streams and closed environment. This execution receipt is not
    independent scientific verification.
  snapshot_sha256: 589a14084b2981120032bfc10e40bb0105f2afda5e7300a7d5b296e1388951c4
- evidence_id: bgc-2322-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-diagnostic-acceptance-001.json
  locator: Whole current diagnostic-acceptance
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses and exact original comparisons/key/capture
    joins. Two original undefined-stereo warnings remain global and unassigned. Acceptance
    establishes local execution integrity, not natural identity or full graph proof.
  snapshot_sha256: aa8d2b7772b4907ebb043566a7016cd09fa16acee7cd80d449a7292b9f787125
- evidence_id: bgc-2322-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-native-gates-acceptance-001.json
  locator: Whole current native-acceptance
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Five original local gates passed; all_native_gates_passed is false because
    full QC and complete OAK coverage are unavailable. Mechanical success is not a
    scientific verdict.
  snapshot_sha256: 7a2daeeecc690ede6862e80925055bb819c81ad72c293b2ab5f980a47ce0aa42
- evidence_id: bgc-2322-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-intake-acceptance-001.json
  locator: Whole current intake-acceptance
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: ROOT accepts ten actual canonical intakes and exact current source ownership/input
    plans; scientific assessment is separate.
  snapshot_sha256: 3124e401a141d5fee52e3838ae8258cf2fc2b9c791050dfa2b6afd6ad1b308dd
- evidence_id: bgc-2322-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-source-inventory-acceptance-001.json
  locator: Whole current inventory-acceptance
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: ROOT accepts the original saved inventory and current input/raw/query/row
    joins. Complete meaning reading is separately attributed in source notes.
  snapshot_sha256: 8e3a8821fa52e78220f01f692579f368a6adb58d85d3624d16eeb7fa4c86b5e1
- evidence_id: bgc-2322-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-input-plan-acceptance-001.json
  locator: Whole current plan-acceptance
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: ROOT accepts the actual input plan and preserved source contexts, without
    a scientific verdict.
  snapshot_sha256: 4d76cf85f5594ce1d2b1990f9a8a3a1abbb6d2da1c9bc45456497364a4602999
- evidence_id: bgc-2322-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-target-input-plan-001.json
  locator: /records/1
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Current one-record input plan with exact direct companions, predicates
    and input roles.
  snapshot_sha256: bc361ca0270b857063f610d29fdc2c498e2ccf208d5f8ae3c0033c044923fe27
- evidence_id: bgc-2322-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Complete disjoint source/raw-history reading and exact carries, with compound-specific
    cautions; source planning did not adjudicate pre-intake science.
  snapshot_sha256: 98c23811517a583723d42fb365b4549d207753a27bd0e0c6654e836596cfad99
- evidence_id: bgc-2322-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Eight explicitly opened implemented curation tables, including ignored
    files, were scanned over 169 distinct exact literals with zero textual hits in
    this bounded scope. Reserved decisions.tsv was not consumed.
  snapshot_sha256: 98c23811517a583723d42fb365b4549d207753a27bd0e0c6654e836596cfad99
- evidence_id: bgc-2322-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":296,"physical_line":296,"raw_tsv_record":"BGC0000220\t4\tactive\tquestionable\tcomplete\tenterocin\t1\t[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O\tInChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1\tCTBBEXWJRAPJIZ-VHPBLNRZSA-N\ttrue\t\tnpatlas:NPA09644\tNCBITaxon:115828\tStreptomyces
    maritimus\tPKS\tType II\tAF254925.1\t\t\tKnock-out studies|Enzymatic assays|Heterologous
    expression|Gene expression correlated with compound production\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:24162851\tENTRY\n","row":{"bgc_classes":"PKS","bgc_subclasses":"Type
    II","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA09644","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"AF254925.1","locus_evidence_methods":"Knock-out
    studies|Enzymatic assays|Heterologous expression|Gene expression correlated with
    compound production","locus_from":"","locus_to":"","mibig_accession":"BGC0000220","primary_reference":"PMID:24162851","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:115828","taxon_label":"Streptomyces
    maritimus"},"row_sha256":"de3e7d236d2be8184f7338e6c77023cf08e53df56c6075b5aa5c4d5415dbde3b"},{"last_physical_line":2905,"physical_line":2905,"raw_tsv_record":"BGC0002366\t2\tactive\tquestionable\tunknown\tenterocin\t1\tCOC1=CC(=O)OC(=C1)[C@@H]2[C@@]3(C[C@@H]4[C@H]([C@]2([C@@H]([C@]3(C(=O)O4)O)C(=O)C5=CC=CC=C5)O)O)O\tInChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1\tCTBBEXWJRAPJIZ-VHPBLNRZSA-N\ttrue\t\tnpatlas:NPA009644|pubchem:23654446|chemspider:19978603\tNCBITaxon:1333476\tStreptomyces
    sp. SCSIO 11863\tPKS\tUnknown\tMK388865.1\t\t\tHeterologous expression|Knock-out
    studies\tBGC_CHARACTERIZED\tCLUSTER_DEMONSTRATED\tPMID:31657934\tENTRY\n","row":{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA009644|pubchem:23654446|chemspider:19978603","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK388865.1","locus_evidence_methods":"Heterologous
    expression|Knock-out studies","locus_from":"","locus_to":"","mibig_accession":"BGC0002366","primary_reference":"PMID:31657934","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"COC1=CC(=O)OC(=C1)[C@@H]2[C@@]3(C[C@@H]4[C@H]([C@]2([C@@H]([C@]3(C(=O)O4)O)C(=O)C5=CC=CC=C5)O)O)O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1333476","taxon_label":"Streptomyces
    sp. SCSIO 11863"},"row_sha256":"a72060bc915d89b85b8d3832c0e77406ddd40e3cf33520afd7fa8e1a4ea9da77"}],"predicate":"exact
    complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 296–296, row_sha256 de3e7d236d2be8184f7338e6c77023cf08e53df56c6075b5aa5c4d5415dbde3b;
    physical lines 2905–2905, row_sha256 a72060bc915d89b85b8d3832c0e77406ddd40e3cf33520afd7fa8e1a4ea9da77
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"PKS","bgc_subclasses":"Type
    II","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA09644","entry_completeness":"complete","entry_quality":"questionable","entry_status":"active","entry_version":"4","genome_accession":"AF254925.1","locus_evidence_methods":"Knock-out
    studies|Enzymatic assays|Heterologous expression|Gene expression correlated with
    compound production","locus_from":"","locus_to":"","mibig_accession":"BGC0000220","primary_reference":"PMID:24162851","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:115828","taxon_label":"Streptomyces
    maritimus"},{"bgc_classes":"PKS","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","compound_classes":"","compound_index":"1","compound_name":"enterocin","database_ids":"npatlas:NPA009644|pubchem:23654446|chemspider:19978603","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK388865.1","locus_evidence_methods":"Heterologous
    expression|Knock-out studies","locus_from":"","locus_to":"","mibig_accession":"BGC0002366","primary_reference":"PMID:31657934","producer_evidence_basis":"BGC_CHARACTERIZED","reference_basis":"ENTRY","smiles":"COC1=CC(=O)OC(=C1)[C@@H]2[C@@]3(C[C@@H]4[C@H]([C@]2([C@@H]([C@]3(C(=O)O4)O)C(=O)C5=CC=CC=C5)O)O)O","standard_inchi":"InChI=1S/C22H20O10/c1-30-11-7-12(31-14(23)8-11)16-20(27)9-13-18(25)21(16,28)17(22(20,29)19(26)32-13)15(24)10-5-3-2-4-6-10/h2-8,13,16-18,25,27-29H,9H2,1H3/t13-,16-,17+,18-,20-,21+,22-/m1/s1","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:1333476","taxon_label":"Streptomyces
    sp. SCSIO 11863"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2322-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":900,"physical_line":900,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\tDidemnum\tNCBITaxon:107394\thttp://www.wikidata.org/entity/Q153605\t10.1021/JO951794G\thttp://www.wikidata.org/entity/Q72470750\n","row":{"organism_name":"Didemnum","organism_wikidata":"http://www.wikidata.org/entity/Q153605","reference_doi":"10.1021/JO951794G","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:107394"},"row_sha256":"03755c2fc69a18068f4ff0c4d700db55018b801718a05e169e105b317b3221b1"},{"last_physical_line":901,"physical_line":901,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1002/MRC.4384\thttp://www.wikidata.org/entity/Q72470750\n","row":{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1002/MRC.4384","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"},"row_sha256":"43b791fac02f6586bc050efd6035a312c96dd49135c49945d89d625640690a67"},{"last_physical_line":902,"physical_line":902,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\tStreptomyces\tNCBITaxon:1883\thttp://www.wikidata.org/entity/Q1144013\t10.1016/0040-4020(96)00391-2\thttp://www.wikidata.org/entity/Q72470750\n","row":{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1016/0040-4020(96)00391-2","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"},"row_sha256":"56dd3fb7985c7b87653e000dcbd4537f57c3285f5c4140ae766d3d168e9cd142"}],"predicate":"exact
    complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 900–900, row_sha256 03755c2fc69a18068f4ff0c4d700db55018b801718a05e169e105b317b3221b1;
    physical lines 901–901, row_sha256 43b791fac02f6586bc050efd6035a312c96dd49135c49945d89d625640690a67;
    physical lines 902–902, row_sha256 56dd3fb7985c7b87653e000dcbd4537f57c3285f5c4140ae766d3d168e9cd142
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"organism_name":"Didemnum","organism_wikidata":"http://www.wikidata.org/entity/Q153605","reference_doi":"10.1021/JO951794G","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:107394"},{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1002/MRC.4384","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"},{"organism_name":"Streptomyces","organism_wikidata":"http://www.wikidata.org/entity/Q1144013","reference_doi":"10.1016/0040-4020(96)00391-2","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q72470750","taxon_id":"NCBITaxon:1883"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2322-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":340,"physical_line":340,"raw_tsv_record":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N\t[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O\tTerpenoids\t\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","superclass_results":""},"row_sha256":"204bf8db5f5bfc6bd767e6b511371801e4cb9f7f8678f6110a0310411e377202"}],"predicate":"exact
    complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 340–340, row_sha256 204bf8db5f5bfc6bd767e6b511371801e4cb9f7f8678f6110a0310411e377202
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"[H][C@]12C[C@@]3(O)[C@@H](C4=CC(OC)=CC(=O)O4)[C@](O)([C@H](C(=O)C4=CC=CC=C4)[C@@]3(O)C(=O)O1)[C@@H]2O","standard_inchi_key":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N","superclass_results":""}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2322-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CTBBEXWJRAPJIZ-VHPBLNRZSA-N"}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure
    rows","query":[]}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/18/source_scope_inventory/source_taxa; /contexts/18/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/18/source_scope_inventory/nonorganism_matches; /contexts/18/source_scope_inventory/actual_assay_rows;
    /contexts/18/source_scope_inventory/blank_AID_sentinels; /contexts/18/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Exact source taxa and route lists; source_taxa is distinct from the empty
    forward/nonorganism and assay/related routes: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:107394","NCBITaxon:115828","NCBITaxon:1333476","NCBITaxon:1883"]}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/44;
    /cached_taxonomy/whole_stanzas/45; /cached_taxonomy/whole_stanzas/88
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete relevant cached stanzas, with no fresh taxonomy verification:
    [{"complete_stanza":"[Term]\nid: NCBITaxon:1883\nname: Streptomyces\nsynonym:
    \"\\\"Microstreptospora\\\" Yan et al.\" EXACT []\nsynonym: \"Actinopycnidium
    Krasil''nikov 1962\" EXACT []\nsynonym: \"Actinosporangium Krasil''nikov and Yuan
    1961\" EXACT []\nsynonym: \"Chainia\" EXACT []\nsynonym: \"Elytrosporangium Falcao
    de Morais et al. 1966\" EXACT []\nsynonym: \"Kitasatoa Matsumae and Hata 1968
    (Approved Lists 1980)\" EXACT []\nsynonym: \"Microellobosporia\" EXACT []\nsynonym:
    \"Streptoverticillium Baldacci 1958\" EXACT []\n\n","id":"NCBITaxon:1883","physical_line":2798},{"complete_stanza":"[Term]\nid:
    NCBITaxon:107394\nname: Didemnum\n\n","id":"NCBITaxon:107394","physical_line":43346},{"complete_stanza":"[Term]\nid:
    NCBITaxon:115828\nname: Streptomyces maritimus\nsynonym: \"''Streptomyces maritimus''\"
    EXACT []\n\n","id":"NCBITaxon:115828","physical_line":45357},{"complete_stanza":"[Term]\nid:
    NCBITaxon:1333476\nname: Streptomyces sp. SCSIO 11863\n\n","id":"NCBITaxon:1333476","physical_line":126552}]'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /records/1/direct_companion_paths; /records/1/direct_companion_predicates
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Exact one-hop scope, with no claim transfer: {"direct_companion_paths":["data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml","data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0002366"]},{"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0002366"]}]}'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233-tentative/bgc-prep/bgc-conditional233-source-inventory-DATA-001.json
  locator: /contexts/6; /contexts/7
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete context meanings/raw histories are attributed in the notes; exact
    identity/root boundaries: [{"declared_mechanism_roots_literal":[],"history_count":2,"identifier":"naturalproductmech:mibig-6e0973d7ec","label":"neoenterocin
    A","owned_bgc_ids":["BGC0002366"],"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-a.yaml","standard_inchi_key":"JBIMWARAATZDME-YKWSONSWSA-N"},{"declared_mechanism_roots_literal":[],"history_count":2,"identifier":"naturalproductmech:mibig-65ffea3920","label":"neoenterocin
    B","owned_bgc_ids":["BGC0002366"],"path":"data/natural_products/shikimates_and_phenylpropanoids/neoenterocin-b.yaml","standard_inchi_key":"BYCKRSGGJOJCOA-RHPXVONCSA-N"}]'
  snapshot_sha256: 4b0d3e3da384d400278579bca7fdc555ccf50e16fc29eaed319dba5fdfd8873e
- evidence_id: bgc-2322-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: The structure flag describes undefined stereocentres. ComputedClassification
    is explicitly a named/versioned prediction from structure, never a source assertion
    or an admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2322-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and absence
    of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity
    proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2322-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 972–1020
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Maintained seeding preserves lead source structures and named/versioned
    computed predictions separately; the computed pathway can control filing without
    becoming a source assertion.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2322-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: One-record claim-level scientific review requires twelve dimensions and
    truthful partial completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2322-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: The review does not edit source records; the overriding absolute no-request
    instruction limits evidence access to retained local files.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2322-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json
  locator: /order; /status; /reader_call_count; /raw_owner; /resolved_view; /expected_view;
    /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials;
    /errors; /external_requests; /molecular_parses; /retries; /limitations
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Complete raw/expected/returned owner equality, original counts and exact
    positive content are retained. One known import-time IPv6 socket-construction
    capability probe was denied before action; no external request, unexpected denial,
    retry or molecular parse occurred. Preservation is not independent mechanism/protein/primary-source
    verification.
  snapshot_sha256: da62e880970a4e7068a73b5b944b976e8f2544bd9c528861bd09c2f5636bd0c3
- evidence_id: bgc-2322-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-reader-execution-001.json
  locator: /observer; /order; /command; /exit_code; /stderr; /retries; /external_requests;
    /original_tool
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: Native operated the original maintained reader once, exit 0, with empty
    stderr and zero retries/external requests. The original terminal is preserved
    in the execution receipt.
  snapshot_sha256: 3367b968f45b6a1791ea6140ab391dc0e236a2d76a106df2ea67b7cf2e641b58
- evidence_id: bgc-2322-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/root-current233-enterocin-maintained-reader-acceptance-001.json
  locator: /status; /accepted; /order; /DATA; /execution; /original_tools; /verification;
    /review_check_contract; /reading_scope; /observer_correction
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: ROOT accepts the exact original reader, complete owner/positive-content
    equality and current authority joins. Every launch environment key is unchanged;
    the observed runtime-only encoding key is explicit. No observer correction caused
    a reader rerun.
  snapshot_sha256: 76fbb439494b2405d12ce2b8fd76ac26b6d5f8225ac0c08d1105aba323a9f001
- evidence_id: bgc-2322-graph-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs/0
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete graph metadata, nodes, edges, qualifiers and every evidence placement:
    {"description":"Partial Streptomyces maritimus enterocin biosynthesis graph for
    the EncM-catalyzed oxidation that triggers the Favorskii-type rearrangement.","edges":[{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang
    et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster
    and showed that these genes are needed for the Favorskii-like rearrangement in
    enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation
    of either gene terminated enterocin production and caused the accumulation of
    four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel
    et al. biochemically and structurally characterized the EncM flavoenzyme oxidation
    that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM
    catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation
    of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel
    et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin
    biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A
    21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin
    family of polyketides from ''S. maritimus'' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed
    UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and
    cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces
    maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"The
    direct EncM substrate is an unstable, unrearranged poly-beta-carbonyl rather than
    a ChEBI-grounded stable pathway intermediate.","object":"encm","predicate":"is
    oxidized by","subject":"unrearranged_polyketide"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang
    et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster
    and showed that these genes are needed for the Favorskii-like rearrangement in
    enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation
    of either gene terminated enterocin production and caused the accumulation of
    four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel
    et al. biochemically and structurally characterized the EncM flavoenzyme oxidation
    that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM
    catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation
    of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel
    et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin
    biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A
    21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin
    family of polyketides from ''S. maritimus'' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed
    UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and
    cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces
    maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"EncM
    performs the dual oxidation that initiates the Favorskii-type rearrangement; EncK
    also acts before mature enterocin is formed.","object":"favorskii_rearrangement","predicate":"triggers","subject":"encm"},{"evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang
    et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster
    and showed that these genes are needed for the Favorskii-like rearrangement in
    enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation
    of either gene terminated enterocin production and caused the accumulation of
    four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel
    et al. biochemically and structurally characterized the EncM flavoenzyme oxidation
    that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM
    catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation
    of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel
    et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin
    biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A
    21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin
    family of polyketides from ''S. maritimus'' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed
    UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and
    cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces
    maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"The
    rearranged pathway intermediate is left ungrounded because the exact immediate
    product of EncM in vivo is not a stable public ChEBI term.","object":"rearranged_enterocin_intermediate","predicate":"forms","subject":"favorskii_rearrangement"}],"graph_id":"enterocin-encm-biosynthesis","nodes":[{"grounding_status":"UNGROUNDED","label":"unrearranged
    poly-beta-carbonyl intermediate","node_id":"unrearranged_polyketide","node_type":"PRECURSOR"},{"grounding_status":"GROUNDED","identifier":"UniProtKB:Q9KHK2","label":"EncM","node_id":"encm","node_type":"ENZYME"},{"grounding_status":"UNGROUNDED","label":"Favorskii-type
    rearrangement","node_id":"favorskii_rearrangement","node_type":"PROCESS"},{"grounding_status":"UNGROUNDED","label":"Favorskii-rearranged
    enterocin intermediate","node_id":"rearranged_enterocin_intermediate","node_type":"PRECURSOR"}],"scope":"BIOSYNTHESIS"}'
  snapshot_sha256: da62e880970a4e7068a73b5b944b976e8f2544bd9c528861bd09c2f5636bd0c3
- evidence_id: bgc-2322-pathway-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway/0
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained pathway item with all evidence, qualifiers and grounding:
    {"enzyme_id":"UniProtKB:Q9KHK2","enzyme_label":"EncM","evidence":[{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Xiang
    et al. inactivated encM and encK in the Streptomyces maritimus enterocin cluster
    and showed that these genes are needed for the Favorskii-like rearrangement in
    enterocin biosynthesis.","reference":"DOI:10.1021/ol0255155","snippet":"Inactivation
    of either gene terminated enterocin production and caused the accumulation of
    four nonrearranged, nonmethylated polyketides."},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Teufel
    et al. biochemically and structurally characterized the EncM flavoenzyme oxidation
    that triggers the Favorskii-type rearrangement central to enterocin biosynthesis.","reference":"DOI:10.1038/nature12643","snippet":"EncM
    catalyses the peroxyflavin-independent oxygenation-dehydrogenation dual oxidation
    of a highly reactive poly(β-carbonyl)"},{"evidence_type":"PRIMARY_EXPERIMENT","notes":"Piel
    et al. cloned and sequenced GenBank AF254925.1, the Streptomyces maritimus enterocin
    biosynthetic gene cluster that contains encM.","reference":"DOI:10.1016/s1074-5521(00)00044-2","snippet":"A
    21.3 kb gene cluster encoding the biosynthesis of the enterocin and wailupemycin
    family of polyketides from ''S. maritimus'' has been cloned and sequenced."},{"evidence_type":"DATABASE_ASSERTION","notes":"Unreviewed
    UniProtKB:Q9KHK2 is Streptomyces maritimus EncM, gene encM, length 464 aa, and
    cross-references EMBL AF254925 protein AAF81732.1.","reference":"https://www.uniprot.org/uniprotkb/Q9KHK2","retrieved_on":"2026-09-27"},{"evidence_type":"DATABASE_ASSERTION","notes":"NCBI
    GenPept AAF81732.1 is the AF254925.1 encM coding sequence from the Streptomyces
    maritimus enterocin cluster and is sequence-identical to UniProtKB:Q9KHK2.","reference":"https://www.ncbi.nlm.nih.gov/protein/AAF81732.1","retrieved_on":"2026-09-27"}],"notes":"This
    curates only the Streptomyces maritimus EncM flavin-mediated oxidation that initiates
    the Favorskii-type rearrangement in enterocin biosynthesis; the reactive poly-beta-carbonyl
    substrate and rearranged pathway intermediate remain ungrounded.","step_number":1}'
  snapshot_sha256: da62e880970a4e7068a73b5b944b976e8f2544bd9c528861bd09c2f5636bd0c3
- evidence_id: bgc-2322-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch233/native-current233-enterocin-maintained-reader-DATA-001.json
  locator: /resolved_view/curation_history
  accessed_at: '2026-11-04T02:01:55.695350Z'
  support: supports
  summary: 'Complete retained owner history: [{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-10T05:54:04Z"},{"action":"SEEDED_FROM_SOURCES","changes":"Seeded
    from the committed inventories in data/raw/.","curator":"seed_from_sources","timestamp":"2026-09-25T03:01:43Z"},{"action":"RECORD_CURATED","changes":"Added
    the Streptomyces maritimus EncM flavin-mediated oxidation step and BIOSYNTHESIS
    causal graph grounded to UniProtKB:Q9KHK2.","curator":"codex","llm_assisted":true,"timestamp":"2026-09-27T07:55:36Z"}]'
  snapshot_sha256: da62e880970a4e7068a73b5b944b976e8f2544bd9c528861bd09c2f5636bd0c3
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:34:00.342391Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 2444131c9bbd175968f9d611c32bf3bbd12568e48a7b35408345deb11a289d74
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:34:25.871048Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 000c1c2d07219c9458f40443fecb23b8632036e95ae07b270a4f42ac7e26b30c
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:34:46.118004Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:35:21.245243Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-233/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-233/native-current233-five-gates-execution-001.json
  accessed_at: '2026-11-04T01:35:33.368121Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 23b82eee0ac99b361f8412dff6d8442ab42a37fb7d5a6453c6c277042174a02c
assessments:
- assessment_id: bgc-2322-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The MINTED owner keeps complete key CTBBEXWJRAPJIZ-VHPBLNRZSA-N across
    BGC0000220 version 4 and BGC0002366 version 2. Their source SMILES serializations
    differ while the retained full key and InChI coincide. The existing OPEN shared-structure
    discussion is not closed by normalized-form agreement or reader preservation.
    No exact retained ChEBI structure match resolves it. Neoenterocin A and B have
    distinct full keys and remain direct context, not identity substitutes.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-grounding-owner
  - bgc-2322-source-mibig_compounds
  - bgc-2322-query-chebi_structures
  - bgc-2322-chemistry
  - bgc-2322-direct-contexts
  - bgc-2322-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: CTBBEXWJRAPJIZ-VHPBLNRZSA-N; exact full retained key, not a name or connectivity-block
      substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2322-grounding-owner
    - bgc-2322-source-mibig_compounds
    - bgc-2322-query-chebi_structures
    - bgc-2322-chemistry
    - bgc-2322-direct-contexts
    - bgc-2322-companion-boundaries
  - name: grounding_scope
    value: The MINTED owner keeps complete key CTBBEXWJRAPJIZ-VHPBLNRZSA-N across
      BGC0000220 version 4 and BGC0002366 version 2. Their source SMILES serializations
      differ while the retained full key and InChI coincide. The existing OPEN shared-structure
      discussion is not closed by normalized-form agreement or reader preservation.
      No exact retained ChEBI structure match resolves it. Neoenterocin A and B have
      distinct full keys and remain direct context, not identity substitutes.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2322-grounding-owner
    - bgc-2322-source-mibig_compounds
    - bgc-2322-query-chebi_structures
    - bgc-2322-chemistry
    - bgc-2322-direct-contexts
    - bgc-2322-companion-boundaries
- assessment_id: bgc-2322-representation
  area: representation
  topic: Stored molecular representation
  outcome: supported
  summary: Both saved forms are neutral C22H20O10 with 32 atoms, 36 bonds and five
    rings in the saved basis. The central polycyclic framework is accompanied by phenyl
    and pyrone rings. Seven tetrahedral centres are specified. In the SMILES table
    the three carbonyls are 11=12, 17=18 and 27=28; hydroxyl oxygens 3, 15, 26 and
    31 are attached to carbons 2, 14, 25 and 30. The methoxy connection is 7–8–9,
    and the lactone linkage 27(=28)–29–0 belongs to the integrated ring [0,1,2,25,27,29].
    A C5O cycle containing a carbonyl carbon is not itself a sugar or glycosidic-linkage
    assignment. All ten comparisons and complete atom-count correspondence are true,
    but full_graph_identity_established remains false and natural identity is not
    independently proven.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-chemistry
  - bgc-2322-topology
  - bgc-2322-grounding-owner
  - bgc-2322-stereo-method
  - bgc-2322-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms are neutral C22H20O10 with 32 atoms, 36 bonds and five
      rings in the saved basis. The central polycyclic framework is accompanied by
      phenyl and pyrone rings. Seven tetrahedral centres are specified. In the SMILES
      table the three carbonyls are 11=12, 17=18 and 27=28; hydroxyl oxygens 3, 15,
      26 and 31 are attached to carbons 2, 14, 25 and 30. The methoxy connection is
      7–8–9, and the lactone linkage 27(=28)–29–0 belongs to the integrated ring [0,1,2,25,27,29].
      A C5O cycle containing a carbonyl carbon is not itself a sugar or glycosidic-linkage
      assignment. All ten comparisons and complete atom-count correspondence are true,
      but full_graph_identity_established remains false and natural identity is not
      independently proven.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2322-chemistry
    - bgc-2322-topology
    - bgc-2322-grounding-owner
    - bgc-2322-stereo-method
    - bgc-2322-structure-schema
  - name: representation_correspondence
    value: All ten saved comparisons and complete atom-count correspondence are true;
      original full_graph_identity_established remains false. Stored normalization
      is not independent exact natural-graph identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2322-chemistry
    - bgc-2322-topology
    - bgc-2322-grounding-owner
    - bgc-2322-stereo-method
    - bgc-2322-structure-schema
- assessment_id: bgc-2322-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: The two PKS source loci remain distinct. BGC0000220 version 4 names Streptomyces
    maritimus 115828, AF254925.1, complete cluster completeness and multiple knockout/enzymatic/heterologous/expression
    methods. BGC0002366 version 2 names Streptomyces sp. SCSIO 11863 taxon 1333476,
    MK388865.1, unknown completeness and heterologous/knockout methods. Both retain
    questionable quality, BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus
    grades. Those grades do not prove that every strain/source claim refers to an
    independently verified identical natural stereoisomer.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-origin-owner
  - bgc-2322-source-mibig_compounds
  - bgc-2322-cached-taxonomy
  - bgc-2322-source-routes
  dimensions:
  - name: taxon_scope
    value: The two PKS source loci remain distinct. BGC0000220 version 4 names Streptomyces
      maritimus 115828, AF254925.1, complete cluster completeness and multiple knockout/enzymatic/heterologous/expression
      methods. BGC0002366 version 2 names Streptomyces sp. SCSIO 11863 taxon 1333476,
      MK388865.1, unknown completeness and heterologous/knockout methods. Both retain
      questionable quality, BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus
      grades. Those grades do not prove that every strain/source claim refers to an
      independently verified identical natural stereoisomer.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2322-origin-owner
    - bgc-2322-source-mibig_compounds
    - bgc-2322-cached-taxonomy
    - bgc-2322-source-routes
  - name: producer_evidence
    value: The two PKS source loci remain distinct. BGC0000220 version 4 names Streptomyces
      maritimus 115828, AF254925.1, complete cluster completeness and multiple knockout/enzymatic/heterologous/expression
      methods. BGC0002366 version 2 names Streptomyces sp. SCSIO 11863 taxon 1333476,
      MK388865.1, unknown completeness and heterologous/knockout methods. Both retain
      questionable quality, BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus
      grades. Those grades do not prove that every strain/source claim refers to an
      independently verified identical natural stereoisomer.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2322-origin-owner
    - bgc-2322-source-mibig_compounds
    - bgc-2322-cached-taxonomy
    - bgc-2322-source-routes
  - name: locus_evidence
    value: The two PKS source loci remain distinct. BGC0000220 version 4 names Streptomyces
      maritimus 115828, AF254925.1, complete cluster completeness and multiple knockout/enzymatic/heterologous/expression
      methods. BGC0002366 version 2 names Streptomyces sp. SCSIO 11863 taxon 1333476,
      MK388865.1, unknown completeness and heterologous/knockout methods. Both retain
      questionable quality, BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus
      grades. Those grades do not prove that every strain/source claim refers to an
      independently verified identical natural stereoisomer.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2322-origin-owner
    - bgc-2322-source-mibig_compounds
    - bgc-2322-cached-taxonomy
    - bgc-2322-source-routes
- assessment_id: bgc-2322-citations
  area: evidence
  topic: Citation scope
  outcome: supported
  summary: MIBiG ENTRY citations PMID24162851 and PMID31657934 belong to the respective
    loci and are not interchangeable compound-specific experiments. The historical
    EncM mechanism uses DOI 10.1021/ol0255155, 10.1038/nature12643 and 10.1016/s1074-5521(00)00044-2
    plus separately typed UniProt/GenBank database assertions. Repeated complete evidence
    on three edges and one step does not multiply independent studies. Current local
    snapshots were read; the cited papers, protein records and their exact experimental
    scope were not freshly retrieved.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-grounding-owner
  - bgc-2322-origin-owner
  - bgc-2322-source-mibig_compounds
  - bgc-2322-source-lotus_occurrences
  - bgc-2322-source-notes
  - bgc-2322-direct-contexts
  - bgc-2322-companion-boundaries
  - bgc-2322-reader-DATA
  - bgc-2322-reader-execution
  - bgc-2322-reader-acceptance
  - bgc-2322-graph-0
  - bgc-2322-pathway-0
  - bgc-2322-history
  dimensions:
  - name: citation_scope
    value: MIBiG ENTRY citations PMID24162851 and PMID31657934 belong to the respective
      loci and are not interchangeable compound-specific experiments. The historical
      EncM mechanism uses DOI 10.1021/ol0255155, 10.1038/nature12643 and 10.1016/s1074-5521(00)00044-2
      plus separately typed UniProt/GenBank database assertions. Repeated complete
      evidence on three edges and one step does not multiply independent studies.
      Current local snapshots were read; the cited papers, protein records and their
      exact experimental scope were not freshly retrieved.
    definition: Database provenance, retained historical primary-experiment support
      and occurrence citations have distinct scopes; repeated placements do not establish
      independent studies, and no fresh external access is claimed.
    evidence_ids:
    - bgc-2322-grounding-owner
    - bgc-2322-origin-owner
    - bgc-2322-source-mibig_compounds
    - bgc-2322-source-lotus_occurrences
    - bgc-2322-source-notes
    - bgc-2322-direct-contexts
    - bgc-2322-companion-boundaries
    - bgc-2322-reader-DATA
    - bgc-2322-reader-execution
    - bgc-2322-reader-acceptance
    - bgc-2322-graph-0
    - bgc-2322-pathway-0
    - bgc-2322-history
- assessment_id: bgc-2322-occurrence
  area: evidence
  topic: Occurrence and assay scope
  outcome: supported
  summary: Three retained LOTUS occurrences are Didemnum genus 107394 with DOI 10.1021/JO951794G
    and Streptomyces genus 1883 with two separate DOI strings. Their genus-level scope
    differs from both source producer taxa. They do not establish producer-strain
    identity, endogenous biosynthesis or three independent experiments. No written
    bioactivity object and no exact saved PubChem, BindingDB or AntibioticMech match
    is present; this is a bounded source result, not global inactivity.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-occurrence-owner
  - bgc-2322-assay-owner
  - bgc-2322-source-lotus_occurrences
  - bgc-2322-query-lotus_occurrences
  - bgc-2322-query-chebi_origins
  - bgc-2322-query-cyanometdb_occurrences
  - bgc-2322-query-pubchem_bioassay
  - bgc-2322-query-bindingdb_targets
  - bgc-2322-query-antibioticmech_inchikeys
  - bgc-2322-source-routes
  - bgc-2322-cached-taxonomy
  - bgc-2322-source-notes
  dimensions:
  - name: occurrence_scope
    value: Three retained LOTUS occurrences are Didemnum genus 107394 with DOI 10.1021/JO951794G
      and Streptomyces genus 1883 with two separate DOI strings. Their genus-level
      scope differs from both source producer taxa. They do not establish producer-strain
      identity, endogenous biosynthesis or three independent experiments. No written
      bioactivity object and no exact saved PubChem, BindingDB or AntibioticMech match
      is present; this is a bounded source result, not global inactivity.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2322-occurrence-owner
    - bgc-2322-assay-owner
    - bgc-2322-source-lotus_occurrences
    - bgc-2322-query-lotus_occurrences
    - bgc-2322-query-chebi_origins
    - bgc-2322-query-cyanometdb_occurrences
    - bgc-2322-query-pubchem_bioassay
    - bgc-2322-query-bindingdb_targets
    - bgc-2322-query-antibioticmech_inchikeys
    - bgc-2322-source-routes
    - bgc-2322-cached-taxonomy
    - bgc-2322-source-notes
  - name: assay_target_scope
    value: No written bioactivity and no actual match in the exact retained PubChem/BindingDB/AntibioticMech
      joins; a bounded source result, not global inactivity or absence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2322-occurrence-owner
    - bgc-2322-assay-owner
    - bgc-2322-source-lotus_occurrences
    - bgc-2322-query-lotus_occurrences
    - bgc-2322-query-chebi_origins
    - bgc-2322-query-cyanometdb_occurrences
    - bgc-2322-query-pubchem_bioassay
    - bgc-2322-query-bindingdb_targets
    - bgc-2322-query-antibioticmech_inchikeys
    - bgc-2322-source-routes
    - bgc-2322-cached-taxonomy
    - bgc-2322-source-notes
- assessment_id: bgc-2322-classification
  area: consistency
  topic: Computed classification applicability
  outcome: concern
  summary: The named/versioned NPClassifier result is Terpenoids with blank finer
    classes and is_glycoside false. Both source loci are explicitly PKS, and the historical
    EncM mechanism acts on a polyketide precursor. This is a concrete applicability
    conflict between the computed coarse label and retained biosynthetic evidence,
    not a demonstrated failure to copy the model output. The schema keeps computed
    predictions separate from source assertions and admission criteria. No replacement
    prediction or wrong-structure conclusion is justified; the model limitation is
    explicit without a source-edit finding.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-classification-owner
  - bgc-2322-source-npclassifier
  - bgc-2322-source-mibig_compounds
  - bgc-2322-chemistry
  - bgc-2322-topology
  - bgc-2322-structure-schema
  - bgc-2322-classification-seeder
  - bgc-2322-reader-DATA
  - bgc-2322-reader-execution
  - bgc-2322-reader-acceptance
  - bgc-2322-graph-0
  - bgc-2322-pathway-0
  - bgc-2322-history
  dimensions:
  - name: classification_applicability
    value: The named/versioned NPClassifier result is Terpenoids with blank finer
      classes and is_glycoside false. Both source loci are explicitly PKS, and the
      historical EncM mechanism acts on a polyketide precursor. This is a concrete
      applicability conflict between the computed coarse label and retained biosynthetic
      evidence, not a demonstrated failure to copy the model output. The schema keeps
      computed predictions separate from source assertions and admission criteria.
      No replacement prediction or wrong-structure conclusion is justified; the model
      limitation is explicit without a source-edit finding.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2322-classification-owner
    - bgc-2322-source-npclassifier
    - bgc-2322-source-mibig_compounds
    - bgc-2322-chemistry
    - bgc-2322-topology
    - bgc-2322-structure-schema
    - bgc-2322-classification-seeder
    - bgc-2322-reader-DATA
    - bgc-2322-reader-execution
    - bgc-2322-reader-acceptance
    - bgc-2322-graph-0
    - bgc-2322-pathway-0
    - bgc-2322-history
- assessment_id: bgc-2322-mechanism
  area: graph
  topic: Partial retained mechanism
  outcome: supported
  summary: 'The preserved partial EncM graph has four nodes and three edges: an ungrounded
    unrearranged polyketide is oxidized by grounded Q9KHK2, which triggers an ungrounded
    Favorskii-rearrangement process leading to an ungrounded rearranged intermediate.
    The one pathway step does not assign a stable substrate/product identifier. The
    raw notes explicitly retain further EncK activity before mature enterocin; this
    graph therefore does not claim complete terminal production. The S. maritimus
    mechanism must not transfer to SCSIO 11863 or its Neoenterocin companions.'
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-reader-DATA
  - bgc-2322-reader-execution
  - bgc-2322-reader-acceptance
  - bgc-2322-graph-0
  - bgc-2322-pathway-0
  - bgc-2322-history
  - bgc-2322-grounding-owner
  - bgc-2322-origin-owner
  - bgc-2322-source-mibig_compounds
  dimensions: []
- assessment_id: bgc-2322-proteins
  area: grounding
  topic: Protein and construct scope
  outcome: supported
  summary: Q9KHK2 is retained as an unreviewed 464-residue EncM example from S. maritimus,
    with historical AF254925.1 / AAF81732.1 sequence correspondence. Database assertions
    remain distinct from the biochemical/structural and gene-inactivation evidence.
    Grounding a protein node does not verify an assay construct or reproduce flavin-mediated
    oxidation/Favorskii chemistry. No fresh sequence translation, alignment, domain/construct
    boundary or protein-record validation occurred; unstable immediate substrates
    and products remain deliberately ungrounded.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-reader-DATA
  - bgc-2322-reader-execution
  - bgc-2322-reader-acceptance
  - bgc-2322-graph-0
  - bgc-2322-pathway-0
  - bgc-2322-history
  - bgc-2322-grounding-owner
  - bgc-2322-origin-owner
  - bgc-2322-source-mibig_compounds
  dimensions: []
- assessment_id: bgc-2322-completion
  area: completeness
  topic: Scientific completion
  outcome: unknown
  summary: Complete owner/history, both locus payloads, actual intake, three occurrence
    rows, companion scope and both full molecular forms have been assessed. The exact
    original maintained-reader preservation contract is now ROOT-accepted without
    adding biological or primary-source verification. The OPEN shared-structure discussion,
    computed-label applicability, fresh primary/protein verification and unavailable
    Full QC/OAK coverage remain explicit. No record/native-status/history edit is
    made and completion is partial.
  target_ids:
  - naturalproductmech:mibig-5172626ac8
  evidence_ids:
  - bgc-2322-owner
  - bgc-2322-capture
  - bgc-2322-intake
  - bgc-2322-plan
  - bgc-2322-intake-acceptance
  - bgc-2322-inventory-acceptance
  - bgc-2322-plan-acceptance
  - bgc-2322-source-notes
  - bgc-2322-curation-scope
  - bgc-2322-diagnostic-execution
  - bgc-2322-diagnostic-acceptance
  - bgc-2322-native-acceptance
  - bgc-2322-review-profile
  - bgc-2322-review-skill
  - bgc-2322-reader-DATA
  - bgc-2322-reader-execution
  - bgc-2322-reader-acceptance
  - bgc-2322-graph-0
  - bgc-2322-pathway-0
  - bgc-2322-history
  dimensions:
  - name: review_completion
    value: 'Partial: actual retained evidence and required local reader preservation
      assessed where applicable; full QC/OAK and fresh primary/identity authority
      unavailable.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2322-owner
    - bgc-2322-capture
    - bgc-2322-intake
    - bgc-2322-plan
    - bgc-2322-intake-acceptance
    - bgc-2322-inventory-acceptance
    - bgc-2322-plan-acceptance
    - bgc-2322-source-notes
    - bgc-2322-curation-scope
    - bgc-2322-diagnostic-execution
    - bgc-2322-diagnostic-acceptance
    - bgc-2322-native-acceptance
    - bgc-2322-review-profile
    - bgc-2322-review-skill
    - bgc-2322-reader-DATA
    - bgc-2322-reader-execution
    - bgc-2322-reader-acceptance
    - bgc-2322-graph-0
    - bgc-2322-pathway-0
    - bgc-2322-history
findings: []
actions: []
limitations:
- All evidence is retained locally. No external identifier, taxonomy, primary publication,
  protein sequence or natural stereochemical assignment was refreshed under the absolute
  no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gate, parse
  and maintained-reader success establish only their explicit mechanical scope.
- Exact no-match joins are bounded by saved predicates/snapshots. Shared names, loci,
  taxa, citations or companions do not transfer compound-specific production, activity,
  mechanism or independent-study status.
- Two original undefined-stereo warnings are global and unassigned. No additional
  molecular/YAML parse, source query or target invocation occurred during this scientific
  authoring.
- No source record, native status or history is edited. Any supported future correction
  belongs to the maintained source/curator owners listed in the actual canonical intake.
- The named/versioned NPClassifier result is Terpenoids with blank finer classes and
  is_glycoside false. Both source loci are explicitly PKS, and the historical EncM
  mechanism acts on a polyketide precursor. This is a concrete applicability conflict
  between the computed coarse label and retained biosynthetic evidence, not a demonstrated
  failure to copy the model output. The schema keeps computed predictions separate
  from source assertions and admission criteria. No replacement prediction or wrong-structure
  conclusion is justified; the model limitation is explicit without a source-edit
  finding.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and actual intake were read. Full source payload meanings
  and direct-companion/raw-history carries remain explicitly attributed in pinned
  source notes.
- 'BGC personally read all ten first-five molecular forms: 236 atom rows / 260 bond
  rows plus complete scalars, ring/stereo/motif tables and original comparisons/maps.
  Diagnostic indices are zero-based, not biochemical locants.'
- ROOT operated original activation/capture, collector/composer, canonical intakes
  and chemistry; Native operated original gates and maintained readers. BGC authored
  source planning and these scientific assessments without invoking any target during
  scientific authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-233
```
