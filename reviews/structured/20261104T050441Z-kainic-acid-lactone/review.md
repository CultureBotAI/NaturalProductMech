# Local evidence review: Kainic acid lactone

- Review: 20261104T050441Z-kainic-acid-lactone
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T04:24:34.138542Z
- Finished UTC: 2026-11-04T05:04:41.459615Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Kainic acid lactone has a locally consistent C10H15NO4 lactone/amine structure with three specified tetrahedral centres. Its exact compound-evidence citation and source-asserted Digenea origin remain distinct from the separate kainic acid companion. Local structure and source preservation do not establish a complete biosynthetic mechanism or new natural-identity verification.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2343; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-821d9ffc0f | data/natural_products/terpenoids/kainic-acid-lactone.yaml | generated | Kainic acid lactone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-821d9ffc0f | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-821d9ffc0f | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-821d9ffc0f | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-821d9ffc0f | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-821d9ffc0f | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-821d9ffc0f | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-821d9ffc0f | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-821d9ffc0f | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and form consistency; exact natural identity unverified

identity: supported. Targets: naturalproductmech:mibig-821d9ffc0f.

The owner naturalproductmech:mibig-821d9ffc0f preserves Kainic acid lactone and full key GPHFPCZKKXKXCJ-HAFWLYHUSA-N from its exact retained MIBiG compound row. MINTED grounding and the historical no-3-star-ChEBI-match note remain bounded by the current empty exact-key ChEBI join. Both saved forms agree on this specific C10H15NO4 representation. The shared-BGC kainic acid companion has a different full key and C9H13NO4 structure; it is not a synonym or substitute. Its predicted classification, chemistry and any evidence cannot be transferred merely because the names and locus are related.

### Stored molecular representation

representation: supported. Targets: naturalproductmech:mibig-821d9ffc0f.

Both saved forms describe one neutral C10H15NO4 component of 15 heavy atoms and 16 bonds. A six-membered lactone and five-membered nitrogen heterocycle share the SMILES 6-7 edge. The lactone contains C3=O4 and ring O2, and a separate carboxylic acid is C10(=O12)-O11H. Ring N13H is a secondary amine, not an amide; no carbon-carbon double bond is present. The three potential tetrahedral centres are all specified (SMILES 6R, 7S and 9S). The detected six-membered C5O cycle [1,2,3,6,7,8] is the carbonyl-containing lactone, not a separately attached sugar. Its intraring ester bond does not constitute evidence of glycosylation. The maintained stereo_complete field is derived from tetrahedral-centre assignment and is not a universal bond-geometry, optical-sign or natural-identity certificate. All ten original pair-comparison flags and complete atom-count correspondence are true for this record, while full_graph_identity_established remains false. No new molecular parse or alternate structure was introduced.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-821d9ffc0f.

MIBiG compound row 2281 belongs to BGC0001974 version 2, with Digenea simplex NCBITaxon:945030 at SOURCE_ASSERTION grade. The MK312630.1 locus is CLUSTER_UNSTATED with no retained experimental locus method; its BGC class is OTHER, while the compound class is Monoterpenoid. These separate fields do not assert that this exact compound’s full pathway is experimentally represented. The cached taxon stanza is local terminology support, not a renewed organism or production determination.

### Citation scope

evidence: supported. Targets: naturalproductmech:mibig-821d9ffc0f.

The selected row explicitly assigns DOI:10.1002/anie.201902910 at COMPOUND_EVIDENCE level. This is more specific source placement than an undifferentiated entry bibliography, but its contents and exact experimental support have not been fetched or newly evaluated here. Shared publication and BGC membership with the distinct kainic acid companion do not prove that every compound-level result is interchangeable or independent. The review preserves the exact citation role and reports its present verification limit.

### Occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-821d9ffc0f.

No occurrence, bioactivity or molecular-target object is written in the owner. The exact saved LOTUS, ChEBI-origin, CyanometDB, PubChem, BindingDB and AntibioticMech frames contain no matching occurrence or assay/target result for this key. The Digenea producer assertion is retained as production provenance, not converted into an independently evidenced occurrence record. These finite no-match results do not imply inactivity or exhaustive absence from other sources, and no companion activity is transferred.

### Computed classification applicability

consistency: supported. Targets: naturalproductmech:mibig-821d9ffc0f.

The retained compound class Monoterpenoid and NPClassifier npclassifier.gnps2.org@2026-09-07 Terpenoids/Monoterpenoids output are separately attributed; the model class list is empty and is_glycoside:false. The complete lactone/amine graph and absence of a separate sugar residue are compatible with the latter flag. A C10 formula, ring motif or matching class words alone does not establish a biosynthetic route, especially when the source BGC class is OTHER and no mechanism is curated here. The different amino-acid-related prediction on kainic acid cannot replace this owner’s exact versioned output. No local ingestion or identity defect is established.

### Scientific completion

completeness: unknown. Targets: naturalproductmech:mibig-821d9ffc0f.

The complete current owner/history, exact source rows and zero-match query frames, cached taxon scope, actual canonical intake ownership and both full molecular forms were assessed. No maintained mechanism reader applies to this owner. Accepted local diagnostics and gates support only their mechanical scope; Full QC, complete OAK coverage and fresh primary/identity authority remain unavailable. This remains a partial scientific review with source-specific limits and no supported curation finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2343-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/kainic-acid-lactone.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner and all 2 history entries; native curation_status remains SEEDED. |
| bgc-2343-capture | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/2 | supports | Complete captured owner preserves every written field/history; selected maintained-reader applicability is false and no component reference is declared. |
| bgc-2343-intake | /private/tmp/npm-review-work/shared-next-batch235/intakes/2343-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-821d9ffc0f; 38 pinned input placements and explicit maintained source/curator ownership. |
| bgc-2343-grounding-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"chemical_structure":{"smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001974"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-821d9ffc0f","label":"Kainic acid lactone","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-821d9ffc0f","source":"MIBIG","source_id":"BGC0001974","source_label":"Kainic acid lactone","source_version":"2"}]} |
| bgc-2343-origin-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001974","bgc_class":["OTHER"],"entry_status":"active","entry_version":"2","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001974 entry version 2; citation taken from the compound evidence level","reference":"DOI:10.1002/anie.201902910"}],"genome_accession":"genbank:MK312630.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Digenea simplex","organism_taxon_id":"NCBITaxon:945030"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001974","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001974 entry version 2; citation taken from the compound evidence level","reference":"DOI:10.1002/anie.201902910"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"2","taxon_id":"NCBITaxon:945030","taxon_label":"Digenea simplex"}],"producer_taxon_groups":["RED_ALGAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-821d9ffc0f","source":"MIBIG","source_id":"BGC0001974","source_label":"Kainic acid lactone","source_version":"2"}]} |
| bgc-2343-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier."} |
| bgc-2343-assay-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {} |
| bgc-2343-classification-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"bgc_class":["OTHER"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Monoterpenoid"],"np_classification":{"class_results":[],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Monoterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2343-chemistry | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/smiles/status; /records/2/inchi/status; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons; /records/2/atom_correspondence | supports | Both stored forms parsed. Exact original comparison/correspondence and stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[0,9,14,6,11,1,5,4,2,7,8,13,12,10,3]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001974"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Specified":3},"smiles":{"Atom_Tetrahedral:Specified":3}}} |
| bgc-2343-topology | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence | supports | Complete saved topology interpretation: Both saved forms describe one neutral C10H15NO4 component of 15 heavy atoms and 16 bonds. A six-membered lactone and five-membered nitrogen heterocycle share the SMILES 6-7 edge. The lactone contains C3=O4 and ring O2, and a separate carboxylic acid is C10(=O12)-O11H. Ring N13H is a secondary amine, not an amide; no carbon-carbon double bond is present. The three potential tetrahedral centres are all specified (SMILES 6R, 7S and 9S). The detected six-membered C5O cycle [1,2,3,6,7,8] is the carbonyl-containing lactone, not a separately attached sugar. Its intraring ester bond does not constitute evidence of glycosylation. |
| bgc-2343-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json; Whole current diagnostic-execution | supports | ROOT operated one original stored-form diagnostic, exit 0, one attempt, preserved original streams and closed environment. This execution receipt is not independent scientific verification. |
| bgc-2343-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution; /verification; /warning_scope; /limits | supports | ROOT accepts the original 20 stored parses and exact original comparisons/key/capture joins. Two original undefined-stereo and two charge-rearrangement warnings remain global and unassigned. Acceptance establishes local execution integrity, not natural identity or full graph proof. |
| bgc-2343-native-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json; Whole current native-acceptance | supports | Five original local gates passed. Full QC and complete OAK coverage remain unavailable, so these results do not establish all required validation or a scientific verdict. |
| bgc-2343-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json; Whole current intake-acceptance | supports | ROOT accepts ten actual canonical intakes and exact current source ownership/input plans; scientific assessment is separate. |
| bgc-2343-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json; Whole current inventory-acceptance | supports | ROOT accepts the original saved inventory and current input/raw/query/row joins. Complete meaning reading is separately attributed in source notes. |
| bgc-2343-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json; Whole current plan-acceptance | supports | ROOT accepts the actual input plan and preserved source contexts, without a scientific verdict. |
| bgc-2343-plan | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json; /records/2 | supports | Current one-record input plan with exact direct companions, predicates and input roles. |
| bgc-2343-source-notes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading and exact carries, with compound-specific cautions; source planning did not adjudicate pre-intake science. |
| bgc-2343-curation-scope | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /curation | supports | ROOT explicitly opened eight implemented curation tables, including ignored files, over 1233 casefolded literal tokens. One taxon-only rationale hit at unrelated BGC0001648:1 does not support any present compound/locus strain transfer; there was no current key, identifier, owned-BGC, label or slug hit. Reserved decisions.tsv, queue and unresolved-taxon routes were not consumed. This is bounded coverage, not universal absence. |
| bgc-2343-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":2281,"physical_line":2281,"raw_tsv_record":"BGC0001974\t2\tactive\tquestionable\tunknown\tKainic acid lactone\t2\tCC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2\tInChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1\tGPHFPCZKKXKXCJ-HAFWLYHUSA-N\ttrue\tMonoterpenoid\t\tNCBITaxon:945030\tDigenea simplex\tother\tother\tMK312630.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1002/anie.201902910\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"other","bgc_subclasses":"other","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Monoterpenoid","compound_index":"2","compound_name":"Kainic acid lactone","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK312630.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001974","primary_reference":"DOI:10.1002/anie.201902910","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:945030","taxon_label":"Digenea simplex"},"row_sha256":"63735c8b3013edced89f9c137fa226ad295eb8ae3ddcabcaf083ee6d393468ba"}],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2281–2281, row_sha256 63735c8b3013edced89f9c137fa226ad295eb8ae3ddcabcaf083ee6d393468ba | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"other","bgc_subclasses":"other","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Monoterpenoid","compound_index":"2","compound_name":"Kainic acid lactone","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK312630.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001974","primary_reference":"DOI:10.1002/anie.201902910","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:945030","taxon_label":"Digenea simplex"}] |
| bgc-2343-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":728,"physical_line":728,"raw_tsv_record":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N\tCC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2\tTerpenoids\tMonoterpenoids\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","superclass_results":"Monoterpenoids"},"row_sha256":"78758d673238d7705781d4d444a9be56a456482bf4797572b37365931fb146e6"}],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 728–728, row_sha256 78758d673238d7705781d4d444a9be56a456482bf4797572b37365931fb146e6 | supports | Complete retained physical row payloads, every field: [{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","superclass_results":"Monoterpenoids"}] |
| bgc-2343-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"} |
| bgc-2343-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2343-source-routes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/source_taxa; /contexts/6/source_scope_inventory/forward_taxon_merge_matches; /contexts/6/source_scope_inventory/nonorganism_matches; /contexts/6/source_scope_inventory/actual_assay_rows; /contexts/6/source_scope_inventory/blank_AID_sentinels; /contexts/6/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists; source_taxa is distinct from the empty forward/nonorganism and actual-assay/related routes; a blank-AID sentinel is separate: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:945030"]} |
| bgc-2343-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/750 | supports | Complete relevant cached stanzas, with no fresh taxonomy verification: [{"complete_stanza":"[Term]\nid: NCBITaxon:945030\nname: Digenea simplex\nsynonym: \"Conferva simplex\" EXACT []\n\n","id":"NCBITaxon:945030","physical_line":113538}] |
| bgc-2343-direct-contexts | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /records/2/direct_companion_paths; /records/2/direct_companion_predicates | supports | Exact one-hop scope, with no claim transfer: {"direct_companion_paths":["data/natural_products/amino_acids_and_peptides/kainic-acid.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/amino_acids_and_peptides/kainic-acid.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001974"]}]} |
| bgc-2343-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/0 | supports | Complete context meanings/raw histories are attributed in the notes; exact identity/root boundaries: [{"declared_mechanism_roots_literal":[],"history_count":2,"identifier":"naturalproductmech:mibig-a36b57cc8e","label":"kainic acid","owned_bgc_ids":["BGC0001974"],"path":"data/natural_products/amino_acids_and_peptides/kainic-acid.yaml","standard_inchi_key":"MJUWVAFFSWEHNC-VQVTYTSYSA-N"}] |
| bgc-2343-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | The structure flag describes undefined stereocentres. ComputedClassification is explicitly a named/versioned prediction from structure, never a source assertion or an admission criterion. |
| bgc-2343-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and absence of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity proof. |
| bgc-2343-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 972–1020 | supports | Maintained seeding preserves lead source structures and named/versioned computed predictions separately; the computed pathway can control filing without becoming a source assertion. |
| bgc-2343-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record claim-level scientific review requires twelve dimensions and truthful partial completion/unavailable-check limits. |
| bgc-2343-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit source records; the overriding absolute no-request instruction limits evidence access to retained local files. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-235/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-235/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-235/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-235/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally. No external identifier, taxonomy, primary publication, protein sequence or natural stereochemical assignment was refreshed under the absolute no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gate and parse success establish only their explicit mechanical scope. No maintained reader applies to this owner.
- Exact no-match joins are bounded by saved predicates/snapshots. Shared names, loci, taxa, citations or companions do not transfer compound-specific production, activity, mechanism or independent-study status.
- Two original undefined-stereo and two charge-rearrangement warnings are global and unassigned. No additional molecular/YAML parse, source query or target invocation occurred during this scientific authoring.
- No source record, native status or history is edited. Any supported future correction belongs to the maintained source/curator owners listed in the actual canonical intake.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and actual intake were read. Full source payload meanings and direct-companion/raw-history carries remain explicitly attributed in pinned source notes.
- BGC personally read all ten first-five molecular forms: 302 atom rows / 334 bond rows plus complete scalars, ring/stereo/motif tables and original comparisons/maps. Diagnostic indices are zero-based, not biochemical locants.
- ROOT operated original activation/capture, collector/composer, canonical intakes and chemistry; Native operated original gates and the one applicable Juniperol maintained reader. BGC authored source planning and these scientific assessments without invoking any target during scientific authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T050441Z-kainic-acid-lactone
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Kainic acid lactone'
started_at: '2026-11-04T04:24:34.138542Z'
finished_at: '2026-11-04T05:04:41.459615Z'
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
summary: Kainic acid lactone has a locally consistent C10H15NO4 lactone/amine structure
  with three specified tetrahedral centres. Its exact compound-evidence citation and
  source-asserted Digenea origin remain distinct from the separate kainic acid companion.
  Local structure and source preservation do not establish a complete biosynthetic
  mechanism or new natural-identity verification.
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
  - path: data/natural_products/amino_acids_and_peptides/kainic-acid.yaml
    sha256: eff5fe3c32f7856c2424e69c0ae675625e3e286225dc9f3f789ab0191dcbdca2
    role: context
  - path: data/natural_products/terpenoids/kainic-acid-lactone.yaml
    sha256: 8119e78b744d33fab6cc776605989e0942aab9f74dd40036e2ec8b83e70c28c1
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
  selection: Campaign path order 2343; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-821d9ffc0f
targets:
- target_id: naturalproductmech:mibig-821d9ffc0f
  path: data/natural_products/terpenoids/kainic-acid-lactone.yaml
  label: Kainic acid lactone
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
  - naturalproductmech:mibig-821d9ffc0f
  command: just validate-strict data/natural_products/terpenoids/jerangolid-d.yaml
    data/natural_products/terpenoids/juniperol-longiborneol.yaml data/natural_products/terpenoids/kainic-acid-lactone.yaml
    data/natural_products/terpenoids/koraiol.yaml data/natural_products/terpenoids/ks-505a.yaml
    data/natural_products/terpenoids/lankacidin-c.yaml data/natural_products/terpenoids/lupeol.yaml
    data/natural_products/terpenoids/lycosantalonol.yaml data/natural_products/terpenoids/mangicol-a.yaml
    data/natural_products/terpenoids/marinoterpin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-821d9ffc0f
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-235/validate-all-001.tsv
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
  - naturalproductmech:mibig-821d9ffc0f
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
  - naturalproductmech:mibig-821d9ffc0f
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
  - naturalproductmech:mibig-821d9ffc0f
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-235/review-queue-001.tsv
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
  - naturalproductmech:mibig-821d9ffc0f
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2343-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/kainic-acid-lactone.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete current owner and all 2 history entries; native curation_status
    remains SEEDED.
  snapshot_sha256: 8119e78b744d33fab6cc776605989e0942aab9f74dd40036e2ec8b83e70c28c1
- evidence_id: bgc-2343-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete captured owner preserves every written field/history; selected
    maintained-reader applicability is false and no component reference is declared.
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2343-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/intakes/2343-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Actual canonical intake for naturalproductmech:mibig-821d9ffc0f; 38 pinned
    input placements and explicit maintained source/curator ownership.
  snapshot_sha256: 4adde9f0565cf9b2c34843c5b1c483ecc8583fadc6e9c1fbb3209f2081acb819
- evidence_id: bgc-2343-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001974"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-821d9ffc0f","label":"Kainic
    acid lactone","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-821d9ffc0f","source":"MIBIG","source_id":"BGC0001974","source_label":"Kainic
    acid lactone","source_version":"2"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2343-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001974","bgc_class":["OTHER"],"entry_status":"active","entry_version":"2","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001974 entry version 2; citation taken from the compound evidence level","reference":"DOI:10.1002/anie.201902910"}],"genome_accession":"genbank:MK312630.1","link_evidence_basis":"CLUSTER_UNSTATED","organism_label":"Digenea
    simplex","organism_taxon_id":"NCBITaxon:945030"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001974","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001974 entry version 2; citation taken from the compound evidence level","reference":"DOI:10.1002/anie.201902910"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"2","taxon_id":"NCBITaxon:945030","taxon_label":"Digenea
    simplex"}],"producer_taxon_groups":["RED_ALGAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-821d9ffc0f","source":"MIBIG","source_id":"BGC0001974","source_label":"Kainic
    acid lactone","source_version":"2"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2343-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure,
    so the record keeps a content-hashed identifier."}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2343-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2343-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"bgc_class":["OTHER"],"biosynthesis_origin":"NATURAL_PRODUCT","compound_classes":["Monoterpenoid"],"np_classification":{"class_results":[],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Monoterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2343-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/smiles/status; /records/2/inchi/status;
    /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons;
    /records/2/atom_correspondence
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison/correspondence and
    stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[0,9,14,6,11,1,5,4,2,7,8,13,12,10,3]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":true,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001974"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Specified":3},"smiles":{"Atom_Tetrahedral:Specified":3}}}'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: bgc-2343-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed; /records/2/inchi/computed; /records/2/declared_structure;
    /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete saved topology interpretation: Both saved forms describe one
    neutral C10H15NO4 component of 15 heavy atoms and 16 bonds. A six-membered lactone
    and five-membered nitrogen heterocycle share the SMILES 6-7 edge. The lactone
    contains C3=O4 and ring O2, and a separate carboxylic acid is C10(=O12)-O11H.
    Ring N13H is a secondary amine, not an amide; no carbon-carbon double bond is
    present. The three potential tetrahedral centres are all specified (SMILES 6R,
    7S and 9S). The detected six-membered C5O cycle [1,2,3,6,7,8] is the carbonyl-containing
    lactone, not a separately attached sugar. Its intraring ester bond does not constitute
    evidence of glycosylation.'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: bgc-2343-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json
  locator: Whole current diagnostic-execution
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT operated one original stored-form diagnostic, exit 0, one attempt,
    preserved original streams and closed environment. This execution receipt is not
    independent scientific verification.
  snapshot_sha256: c6f0da32c1be702c997e92c5892ea02e38a069abc6c0b720fa4e1338b674661c
- evidence_id: bgc-2343-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /verification; /warning_scope; /limits
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the original 20 stored parses and exact original comparisons/key/capture
    joins. Two original undefined-stereo and two charge-rearrangement warnings remain
    global and unassigned. Acceptance establishes local execution integrity, not natural
    identity or full graph proof.
  snapshot_sha256: 5c7d1831ae5c8d9ffdafa16a84aaf306a7641eec7b63ed29999a7182721156f6
- evidence_id: bgc-2343-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json
  locator: Whole current native-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Five original local gates passed. Full QC and complete OAK coverage remain
    unavailable, so these results do not establish all required validation or a scientific
    verdict.
  snapshot_sha256: 713d96670fed493630776183217dec028aa27c64ca70142c925e14679e8064bc
- evidence_id: bgc-2343-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json
  locator: Whole current intake-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts ten actual canonical intakes and exact current source ownership/input
    plans; scientific assessment is separate.
  snapshot_sha256: 97b8f40e4ce5c08c4508e916b5951f267a4aba333bf78abf8275d7c8c865e7f0
- evidence_id: bgc-2343-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json
  locator: Whole current inventory-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the original saved inventory and current input/raw/query/row
    joins. Complete meaning reading is separately attributed in source notes.
  snapshot_sha256: efe55c8fc90acc75742e2e133be3d52885ba31a8027a7ef4736e7bc020950af9
- evidence_id: bgc-2343-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json
  locator: Whole current plan-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the actual input plan and preserved source contexts, without
    a scientific verdict.
  snapshot_sha256: ebd812deb22f4b63b07c62f2cfb77b5ccaefd41fa85e5da34e9ad033ab96431c
- evidence_id: bgc-2343-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json
  locator: /records/2
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Current one-record input plan with exact direct companions, predicates
    and input roles.
  snapshot_sha256: 4534eaf8666f0c106f388a2d17af4dc6b1edc20f665e7aef9a03813706c19ddb
- evidence_id: bgc-2343-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete disjoint source/raw-history reading and exact carries, with compound-specific
    cautions; source planning did not adjudicate pre-intake science.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: bgc-2343-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT explicitly opened eight implemented curation tables, including ignored
    files, over 1233 casefolded literal tokens. One taxon-only rationale hit at unrelated
    BGC0001648:1 does not support any present compound/locus strain transfer; there
    was no current key, identifier, owned-BGC, label or slug hit. Reserved decisions.tsv,
    queue and unresolved-taxon routes were not consumed. This is bounded coverage,
    not universal absence.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: bgc-2343-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":2281,"physical_line":2281,"raw_tsv_record":"BGC0001974\t2\tactive\tquestionable\tunknown\tKainic
    acid lactone\t2\tCC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2\tInChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1\tGPHFPCZKKXKXCJ-HAFWLYHUSA-N\ttrue\tMonoterpenoid\t\tNCBITaxon:945030\tDigenea
    simplex\tother\tother\tMK312630.1\t\t\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tDOI:10.1002/anie.201902910\tCOMPOUND_EVIDENCE\n","row":{"bgc_classes":"other","bgc_subclasses":"other","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Monoterpenoid","compound_index":"2","compound_name":"Kainic
    acid lactone","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK312630.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001974","primary_reference":"DOI:10.1002/anie.201902910","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:945030","taxon_label":"Digenea
    simplex"},"row_sha256":"63735c8b3013edced89f9c137fa226ad295eb8ae3ddcabcaf083ee6d393468ba"}],"predicate":"exact
    complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2281–2281, row_sha256 63735c8b3013edced89f9c137fa226ad295eb8ae3ddcabcaf083ee6d393468ba
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"other","bgc_subclasses":"other","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"Monoterpenoid","compound_index":"2","compound_name":"Kainic
    acid lactone","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"2","genome_accession":"MK312630.1","locus_evidence_methods":"","locus_from":"","locus_to":"","mibig_accession":"BGC0001974","primary_reference":"DOI:10.1002/anie.201902910","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"COMPOUND_EVIDENCE","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi":"InChI=1S/C10H15NO4/c1-10(2)6-4-11-8(9(13)14)5(6)3-7(12)15-10/h5-6,8,11H,3-4H2,1-2H3,(H,13,14)/t5-,6-,8-/m0/s1","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","stereo_complete":"true","taxon_id":"NCBITaxon:945030","taxon_label":"Digenea
    simplex"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2343-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":728,"physical_line":728,"raw_tsv_record":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N\tCC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2\tTerpenoids\tMonoterpenoids\t\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","superclass_results":"Monoterpenoids"},"row_sha256":"78758d673238d7705781d4d444a9be56a456482bf4797572b37365931fb146e6"}],"predicate":"exact
    complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 728–728, row_sha256 78758d673238d7705781d4d444a9be56a456482bf4797572b37365931fb146e6
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC(OC1=O)(C)[C@]2([H])[C@H](C1)[C@@H](C(O)=O)NC2","standard_inchi_key":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N","superclass_results":"Monoterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2343-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"GPHFPCZKKXKXCJ-HAFWLYHUSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure
    rows","query":[]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/source_taxa; /contexts/6/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/6/source_scope_inventory/nonorganism_matches; /contexts/6/source_scope_inventory/actual_assay_rows;
    /contexts/6/source_scope_inventory/blank_AID_sentinels; /contexts/6/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Exact source taxa and route lists; source_taxa is distinct from the empty
    forward/nonorganism and actual-assay/related routes; a blank-AID sentinel is separate:
    {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:945030"]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/750
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete relevant cached stanzas, with no fresh taxonomy verification:
    [{"complete_stanza":"[Term]\nid: NCBITaxon:945030\nname: Digenea simplex\nsynonym:
    \"Conferva simplex\" EXACT []\n\n","id":"NCBITaxon:945030","physical_line":113538}]'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /records/2/direct_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Exact one-hop scope, with no claim transfer: {"direct_companion_paths":["data/natural_products/amino_acids_and_peptides/kainic-acid.yaml"],"direct_companion_predicates":[{"path":"data/natural_products/amino_acids_and_peptides/kainic-acid.yaml","same_complete_InChIKey":false,"same_root_identifier":false,"shared_owned_BGCs":["BGC0001974"]}]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/0
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete context meanings/raw histories are attributed in the notes; exact
    identity/root boundaries: [{"declared_mechanism_roots_literal":[],"history_count":2,"identifier":"naturalproductmech:mibig-a36b57cc8e","label":"kainic
    acid","owned_bgc_ids":["BGC0001974"],"path":"data/natural_products/amino_acids_and_peptides/kainic-acid.yaml","standard_inchi_key":"MJUWVAFFSWEHNC-VQVTYTSYSA-N"}]'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2343-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: The structure flag describes undefined stereocentres. ComputedClassification
    is explicitly a named/versioned prediction from structure, never a source assertion
    or an admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2343-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and absence
    of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity
    proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2343-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 972–1020
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Maintained seeding preserves lead source structures and named/versioned
    computed predictions separately; the computed pathway can control filing without
    becoming a source assertion.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2343-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: One-record claim-level scientific review requires twelve dimensions and
    truthful partial completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2343-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole current skill
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: The review does not edit source records; the overriding absolute no-request
    instruction limits evidence access to retained local files.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:28:50.246712Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 451bdae3fced338f9cab6a0065481c50af073167c8f08ea2278221cdc9bd3b9f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:29:16.400882Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 855c8f91f20c1843d397c7f6cc176f7bc5b008882a65cac37c9d332069c3fa14
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:29:36.734590Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:30:13.718045Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-235/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-235/native-current235-five-gates-execution-001.json
  accessed_at: '2026-11-04T04:30:25.980598Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f0f15dd29bebbfeaee4046ecb5069d24cf4a36fdd1c6d046bf9208c3c24d4d57
assessments:
- assessment_id: bgc-2343-identity
  area: identity
  topic: Retained identity and form consistency; exact natural identity unverified
  outcome: supported
  summary: The owner naturalproductmech:mibig-821d9ffc0f preserves Kainic acid lactone
    and full key GPHFPCZKKXKXCJ-HAFWLYHUSA-N from its exact retained MIBiG compound
    row. MINTED grounding and the historical no-3-star-ChEBI-match note remain bounded
    by the current empty exact-key ChEBI join. Both saved forms agree on this specific
    C10H15NO4 representation. The shared-BGC kainic acid companion has a different
    full key and C9H13NO4 structure; it is not a synonym or substitute. Its predicted
    classification, chemistry and any evidence cannot be transferred merely because
    the names and locus are related.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-grounding-owner
  - bgc-2343-source-mibig_compounds
  - bgc-2343-query-chebi_structures
  - bgc-2343-chemistry
  - bgc-2343-direct-contexts
  - bgc-2343-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: GPHFPCZKKXKXCJ-HAFWLYHUSA-N; exact full retained key, not a name or connectivity-block
      substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2343-grounding-owner
    - bgc-2343-source-mibig_compounds
    - bgc-2343-query-chebi_structures
    - bgc-2343-chemistry
    - bgc-2343-direct-contexts
    - bgc-2343-companion-boundaries
  - name: grounding_scope
    value: The owner naturalproductmech:mibig-821d9ffc0f preserves Kainic acid lactone
      and full key GPHFPCZKKXKXCJ-HAFWLYHUSA-N from its exact retained MIBiG compound
      row. MINTED grounding and the historical no-3-star-ChEBI-match note remain bounded
      by the current empty exact-key ChEBI join. Both saved forms agree on this specific
      C10H15NO4 representation. The shared-BGC kainic acid companion has a different
      full key and C9H13NO4 structure; it is not a synonym or substitute. Its predicted
      classification, chemistry and any evidence cannot be transferred merely because
      the names and locus are related.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2343-grounding-owner
    - bgc-2343-source-mibig_compounds
    - bgc-2343-query-chebi_structures
    - bgc-2343-chemistry
    - bgc-2343-direct-contexts
    - bgc-2343-companion-boundaries
- assessment_id: bgc-2343-representation
  area: representation
  topic: Stored molecular representation
  outcome: supported
  summary: Both saved forms describe one neutral C10H15NO4 component of 15 heavy atoms
    and 16 bonds. A six-membered lactone and five-membered nitrogen heterocycle share
    the SMILES 6-7 edge. The lactone contains C3=O4 and ring O2, and a separate carboxylic
    acid is C10(=O12)-O11H. Ring N13H is a secondary amine, not an amide; no carbon-carbon
    double bond is present. The three potential tetrahedral centres are all specified
    (SMILES 6R, 7S and 9S). The detected six-membered C5O cycle [1,2,3,6,7,8] is the
    carbonyl-containing lactone, not a separately attached sugar. Its intraring ester
    bond does not constitute evidence of glycosylation. The maintained stereo_complete
    field is derived from tetrahedral-centre assignment and is not a universal bond-geometry,
    optical-sign or natural-identity certificate. All ten original pair-comparison
    flags and complete atom-count correspondence are true for this record, while full_graph_identity_established
    remains false. No new molecular parse or alternate structure was introduced.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-chemistry
  - bgc-2343-topology
  - bgc-2343-grounding-owner
  - bgc-2343-stereo-method
  - bgc-2343-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms describe one neutral C10H15NO4 component of 15 heavy atoms
      and 16 bonds. A six-membered lactone and five-membered nitrogen heterocycle
      share the SMILES 6-7 edge. The lactone contains C3=O4 and ring O2, and a separate
      carboxylic acid is C10(=O12)-O11H. Ring N13H is a secondary amine, not an amide;
      no carbon-carbon double bond is present. The three potential tetrahedral centres
      are all specified (SMILES 6R, 7S and 9S). The detected six-membered C5O cycle
      [1,2,3,6,7,8] is the carbonyl-containing lactone, not a separately attached
      sugar. Its intraring ester bond does not constitute evidence of glycosylation.
      The maintained stereo_complete field is derived from tetrahedral-centre assignment
      and is not a universal bond-geometry, optical-sign or natural-identity certificate.
      All ten original pair-comparison flags and complete atom-count correspondence
      are true for this record, while full_graph_identity_established remains false.
      No new molecular parse or alternate structure was introduced.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2343-chemistry
    - bgc-2343-topology
    - bgc-2343-grounding-owner
    - bgc-2343-stereo-method
    - bgc-2343-structure-schema
  - name: representation_correspondence
    value: All ten saved comparisons and complete atom-count correspondence are true;
      original full_graph_identity_established remains false. Stored normalization
      is not independent exact natural-graph identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2343-chemistry
    - bgc-2343-topology
    - bgc-2343-grounding-owner
    - bgc-2343-stereo-method
    - bgc-2343-structure-schema
- assessment_id: bgc-2343-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: MIBiG compound row 2281 belongs to BGC0001974 version 2, with Digenea simplex
    NCBITaxon:945030 at SOURCE_ASSERTION grade. The MK312630.1 locus is CLUSTER_UNSTATED
    with no retained experimental locus method; its BGC class is OTHER, while the
    compound class is Monoterpenoid. These separate fields do not assert that this
    exact compound’s full pathway is experimentally represented. The cached taxon
    stanza is local terminology support, not a renewed organism or production determination.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-origin-owner
  - bgc-2343-source-mibig_compounds
  - bgc-2343-cached-taxonomy
  - bgc-2343-source-routes
  dimensions:
  - name: taxon_scope
    value: MIBiG compound row 2281 belongs to BGC0001974 version 2, with Digenea simplex
      NCBITaxon:945030 at SOURCE_ASSERTION grade. The MK312630.1 locus is CLUSTER_UNSTATED
      with no retained experimental locus method; its BGC class is OTHER, while the
      compound class is Monoterpenoid. These separate fields do not assert that this
      exact compound’s full pathway is experimentally represented. The cached taxon
      stanza is local terminology support, not a renewed organism or production determination.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2343-origin-owner
    - bgc-2343-source-mibig_compounds
    - bgc-2343-cached-taxonomy
    - bgc-2343-source-routes
  - name: producer_evidence
    value: MIBiG compound row 2281 belongs to BGC0001974 version 2, with Digenea simplex
      NCBITaxon:945030 at SOURCE_ASSERTION grade. The MK312630.1 locus is CLUSTER_UNSTATED
      with no retained experimental locus method; its BGC class is OTHER, while the
      compound class is Monoterpenoid. These separate fields do not assert that this
      exact compound’s full pathway is experimentally represented. The cached taxon
      stanza is local terminology support, not a renewed organism or production determination.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2343-origin-owner
    - bgc-2343-source-mibig_compounds
    - bgc-2343-cached-taxonomy
    - bgc-2343-source-routes
  - name: locus_evidence
    value: MIBiG compound row 2281 belongs to BGC0001974 version 2, with Digenea simplex
      NCBITaxon:945030 at SOURCE_ASSERTION grade. The MK312630.1 locus is CLUSTER_UNSTATED
      with no retained experimental locus method; its BGC class is OTHER, while the
      compound class is Monoterpenoid. These separate fields do not assert that this
      exact compound’s full pathway is experimentally represented. The cached taxon
      stanza is local terminology support, not a renewed organism or production determination.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2343-origin-owner
    - bgc-2343-source-mibig_compounds
    - bgc-2343-cached-taxonomy
    - bgc-2343-source-routes
- assessment_id: bgc-2343-citations
  area: evidence
  topic: Citation scope
  outcome: supported
  summary: The selected row explicitly assigns DOI:10.1002/anie.201902910 at COMPOUND_EVIDENCE
    level. This is more specific source placement than an undifferentiated entry bibliography,
    but its contents and exact experimental support have not been fetched or newly
    evaluated here. Shared publication and BGC membership with the distinct kainic
    acid companion do not prove that every compound-level result is interchangeable
    or independent. The review preserves the exact citation role and reports its present
    verification limit.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-grounding-owner
  - bgc-2343-origin-owner
  - bgc-2343-source-mibig_compounds
  - bgc-2343-source-notes
  - bgc-2343-direct-contexts
  - bgc-2343-companion-boundaries
  dimensions:
  - name: citation_scope
    value: The selected row explicitly assigns DOI:10.1002/anie.201902910 at COMPOUND_EVIDENCE
      level. This is more specific source placement than an undifferentiated entry
      bibliography, but its contents and exact experimental support have not been
      fetched or newly evaluated here. Shared publication and BGC membership with
      the distinct kainic acid companion do not prove that every compound-level result
      is interchangeable or independent. The review preserves the exact citation role
      and reports its present verification limit.
    definition: Database provenance, retained historical primary-experiment support
      and occurrence citations have distinct scopes; repeated placements do not establish
      independent studies, and no fresh external access is claimed.
    evidence_ids:
    - bgc-2343-grounding-owner
    - bgc-2343-origin-owner
    - bgc-2343-source-mibig_compounds
    - bgc-2343-source-notes
    - bgc-2343-direct-contexts
    - bgc-2343-companion-boundaries
- assessment_id: bgc-2343-occurrence
  area: evidence
  topic: Occurrence and assay scope
  outcome: supported
  summary: No occurrence, bioactivity or molecular-target object is written in the
    owner. The exact saved LOTUS, ChEBI-origin, CyanometDB, PubChem, BindingDB and
    AntibioticMech frames contain no matching occurrence or assay/target result for
    this key. The Digenea producer assertion is retained as production provenance,
    not converted into an independently evidenced occurrence record. These finite
    no-match results do not imply inactivity or exhaustive absence from other sources,
    and no companion activity is transferred.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-occurrence-owner
  - bgc-2343-assay-owner
  - bgc-2343-query-lotus_occurrences
  - bgc-2343-query-chebi_origins
  - bgc-2343-query-cyanometdb_occurrences
  - bgc-2343-query-pubchem_bioassay
  - bgc-2343-query-bindingdb_targets
  - bgc-2343-query-antibioticmech_inchikeys
  - bgc-2343-source-routes
  - bgc-2343-cached-taxonomy
  - bgc-2343-source-notes
  dimensions:
  - name: occurrence_scope
    value: No occurrence, bioactivity or molecular-target object is written in the
      owner. The exact saved LOTUS, ChEBI-origin, CyanometDB, PubChem, BindingDB and
      AntibioticMech frames contain no matching occurrence or assay/target result
      for this key. The Digenea producer assertion is retained as production provenance,
      not converted into an independently evidenced occurrence record. These finite
      no-match results do not imply inactivity or exhaustive absence from other sources,
      and no companion activity is transferred.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2343-occurrence-owner
    - bgc-2343-assay-owner
    - bgc-2343-query-lotus_occurrences
    - bgc-2343-query-chebi_origins
    - bgc-2343-query-cyanometdb_occurrences
    - bgc-2343-query-pubchem_bioassay
    - bgc-2343-query-bindingdb_targets
    - bgc-2343-query-antibioticmech_inchikeys
    - bgc-2343-source-routes
    - bgc-2343-cached-taxonomy
    - bgc-2343-source-notes
  - name: assay_target_scope
    value: No written bioactivity or molecular target and no actual assay/target result
      in the exact retained PubChem/BindingDB/AntibioticMech joins. A blank-AID sentinel,
      where present, is not an activity result. This is a bounded source result, not
      global inactivity or absence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2343-occurrence-owner
    - bgc-2343-assay-owner
    - bgc-2343-query-lotus_occurrences
    - bgc-2343-query-chebi_origins
    - bgc-2343-query-cyanometdb_occurrences
    - bgc-2343-query-pubchem_bioassay
    - bgc-2343-query-bindingdb_targets
    - bgc-2343-query-antibioticmech_inchikeys
    - bgc-2343-source-routes
    - bgc-2343-cached-taxonomy
    - bgc-2343-source-notes
- assessment_id: bgc-2343-classification
  area: consistency
  topic: Computed classification applicability
  outcome: supported
  summary: The retained compound class Monoterpenoid and NPClassifier npclassifier.gnps2.org@2026-09-07
    Terpenoids/Monoterpenoids output are separately attributed; the model class list
    is empty and is_glycoside:false. The complete lactone/amine graph and absence
    of a separate sugar residue are compatible with the latter flag. A C10 formula,
    ring motif or matching class words alone does not establish a biosynthetic route,
    especially when the source BGC class is OTHER and no mechanism is curated here.
    The different amino-acid-related prediction on kainic acid cannot replace this
    owner’s exact versioned output. No local ingestion or identity defect is established.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-classification-owner
  - bgc-2343-source-npclassifier
  - bgc-2343-source-mibig_compounds
  - bgc-2343-chemistry
  - bgc-2343-topology
  - bgc-2343-structure-schema
  - bgc-2343-classification-seeder
  dimensions:
  - name: classification_applicability
    value: The retained compound class Monoterpenoid and NPClassifier npclassifier.gnps2.org@2026-09-07
      Terpenoids/Monoterpenoids output are separately attributed; the model class
      list is empty and is_glycoside:false. The complete lactone/amine graph and absence
      of a separate sugar residue are compatible with the latter flag. A C10 formula,
      ring motif or matching class words alone does not establish a biosynthetic route,
      especially when the source BGC class is OTHER and no mechanism is curated here.
      The different amino-acid-related prediction on kainic acid cannot replace this
      owner’s exact versioned output. No local ingestion or identity defect is established.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2343-classification-owner
    - bgc-2343-source-npclassifier
    - bgc-2343-source-mibig_compounds
    - bgc-2343-chemistry
    - bgc-2343-topology
    - bgc-2343-structure-schema
    - bgc-2343-classification-seeder
- assessment_id: bgc-2343-completion
  area: completeness
  topic: Scientific completion
  outcome: unknown
  summary: The complete current owner/history, exact source rows and zero-match query
    frames, cached taxon scope, actual canonical intake ownership and both full molecular
    forms were assessed. No maintained mechanism reader applies to this owner. Accepted
    local diagnostics and gates support only their mechanical scope; Full QC, complete
    OAK coverage and fresh primary/identity authority remain unavailable. This remains
    a partial scientific review with source-specific limits and no supported curation
    finding.
  target_ids:
  - naturalproductmech:mibig-821d9ffc0f
  evidence_ids:
  - bgc-2343-owner
  - bgc-2343-capture
  - bgc-2343-intake
  - bgc-2343-plan
  - bgc-2343-intake-acceptance
  - bgc-2343-inventory-acceptance
  - bgc-2343-plan-acceptance
  - bgc-2343-source-notes
  - bgc-2343-curation-scope
  - bgc-2343-diagnostic-execution
  - bgc-2343-diagnostic-acceptance
  - bgc-2343-native-acceptance
  - bgc-2343-review-profile
  - bgc-2343-review-skill
  dimensions:
  - name: review_completion
    value: 'Partial: complete actual evidence and saved forms assessed; no maintained
      mechanism reader applies. Full QC/OAK and fresh primary/identity authority remain
      unavailable.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2343-owner
    - bgc-2343-capture
    - bgc-2343-intake
    - bgc-2343-plan
    - bgc-2343-intake-acceptance
    - bgc-2343-inventory-acceptance
    - bgc-2343-plan-acceptance
    - bgc-2343-source-notes
    - bgc-2343-curation-scope
    - bgc-2343-diagnostic-execution
    - bgc-2343-diagnostic-acceptance
    - bgc-2343-native-acceptance
    - bgc-2343-review-profile
    - bgc-2343-review-skill
findings: []
actions: []
limitations:
- All evidence is retained locally. No external identifier, taxonomy, primary publication,
  protein sequence or natural stereochemical assignment was refreshed under the absolute
  no-request instruction.
- Full QC and complete OAK authority coverage remain unavailable. Local gate and parse
  success establish only their explicit mechanical scope. No maintained reader applies
  to this owner.
- Exact no-match joins are bounded by saved predicates/snapshots. Shared names, loci,
  taxa, citations or companions do not transfer compound-specific production, activity,
  mechanism or independent-study status.
- Two original undefined-stereo and two charge-rearrangement warnings are global and
  unassigned. No additional molecular/YAML parse, source query or target invocation
  occurred during this scientific authoring.
- No source record, native status or history is edited. Any supported future correction
  belongs to the maintained source/curator owners listed in the actual canonical intake.
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
- 'BGC personally read all ten first-five molecular forms: 302 atom rows / 334 bond
  rows plus complete scalars, ring/stereo/motif tables and original comparisons/maps.
  Diagnostic indices are zero-based, not biochemical locants.'
- ROOT operated original activation/capture, collector/composer, canonical intakes
  and chemistry; Native operated original gates and the one applicable Juniperol maintained
  reader. BGC authored source planning and these scientific assessments without invoking
  any target during scientific authoring.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-235
```
