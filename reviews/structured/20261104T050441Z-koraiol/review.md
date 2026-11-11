# Local evidence review: koraiol

- Review: 20261104T050441Z-koraiol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T04:24:34.139809Z
- Finished UTC: 2026-11-04T05:04:41.470810Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Koraiol retains a consistent neutral C15H26O bridged polycyclic alcohol representation with all five potential tetrahedral centres unspecified. The Fusarium producer assertion and Pinus occurrence remain distinct. The versioned scaffold prediction is preserved without assigning an unencoded natural stereoisomer or a complete mechanism.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2344; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-8ecf532445 | data/natural_products/terpenoids/koraiol.yaml | generated | koraiol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-8ecf532445 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-8ecf532445 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-8ecf532445 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-8ecf532445 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-8ecf532445 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-8ecf532445 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-8ecf532445 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-8ecf532445 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and form consistency; exact natural identity unverified

identity: supported. Targets: naturalproductmech:mibig-8ecf532445.

The owner naturalproductmech:mibig-8ecf532445 preserves literal koraiol and full key CPLGPDHGFNXBOA-UHFFFAOYSA-N. Its MINTED status and historical no-3-star-ChEBI-match note agree with the bounded empty exact-key source join, without claiming that no external identity exists. Both stored forms agree on connectivity and unresolved stereochemical status. No tetrahedral configuration is specified, so the record does not establish one exact natural stereoisomer from its name or model class. No direct companion is admitted for this selected key.

### Stored molecular representation

representation: supported. Targets: naturalproductmech:mibig-8ecf532445.

Both saved forms are neutral C15H26O with 16 heavy atoms and 18 single bonds. The saved carbocyclic ring basis has sizes 4, 7 and 4 in a polycyclic framework. Its single oxygen is a tertiary hydroxyl, SMILES O14H attached to C7; no ether, carbonyl or alkene is present. All five potential tetrahedral centres, SMILES 3, 4, 7, 8 and 9, are unspecified in both forms. The graph contains no separate sugar residue or glycosidic linkage. The full key and canonical correspondence preserve this partial structure rather than supplying missing stereochemistry. The maintained stereo_complete field is derived from tetrahedral-centre assignment and is not a universal bond-geometry, optical-sign or natural-identity certificate. All ten original pair-comparison flags and complete atom-count correspondence are true for this record, while full_graph_identity_established remains false. No new molecular parse or alternate structure was introduced.

### Producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-8ecf532445.

MIBiG row 1962 belongs to BGC0001642 version 3 and asserts Fusarium fujikuroi IMI 58289, NCBITaxon:1279085, as producer at SOURCE_ASSERTION grade. The TERPENE locus HF679030.1:2313680-2315399 is CLUSTER_UNSTATED with no retained experimental method. The Pinus koraiensis occurrence at NCBITaxon:88728 is a separately attributed source observation, not evidence that the fungal strain assertion or exact biosynthetic locus was newly verified. Cached taxon names preserve their own local scope.

### Citation scope

evidence: supported. Targets: naturalproductmech:mibig-8ecf532445.

The locus source retains PMID:23335243 at ENTRY level. The Pinus occurrence instead cites DOI:10.1007/BF00565927. These distinct roles must remain attached to their corresponding claims; the entry citation is not automatically a compound-specific structure, enzyme or activity assay. Neither publication was accessed anew, and differing identifier strings alone do not establish independent experimental confirmation of the exact partial-stereo structure.

### Occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-8ecf532445.

The written Pinus koraiensis occurrence matches the retained LOTUS row and DOI:10.1007/BF00565927. It supports that database occurrence assertion, not a transfer of fungal producer, locus or mechanism evidence. No bioactivity or molecular target is written, and the exact saved PubChem, BindingDB and AntibioticMech joins have no result. Those bounded negatives do not imply inactivity or the absence of all published assays; no phenotype or enzyme claim is inferred from the name.

### Computed classification applicability

consistency: supported. Targets: naturalproductmech:mibig-8ecf532445.

NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids, Sesquiterpenoids, Presilphiperfolane and Probotryane sesquiterpenoids, and is_glycoside:false. The C15 polycyclic alcohol and absence of a separate sugar are compatible with broad sesquiterpenoid and non-glycoside applicability. The finer class is still a named/versioned prediction and does not resolve any of the five unspecified stereocentres or prove a specific rearrangement pathway. Source TERPENE membership and model output are retained separately; no exact natural stereoisomer or unrepresented mechanism is supplied.

### Scientific completion

completeness: unknown. Targets: naturalproductmech:mibig-8ecf532445.

Complete owner/history, actual intake/source ownership, full retained matching rows and no-match frames, cache and both full saved molecular forms were read. No mechanism root or component is declared, so no maintained reader applies. The false source stereo_complete flag is preserved consistently with five unresolved centres. Full QC, complete OAK coverage and fresh primary/identity verification remain unavailable, leaving a partial review with no supported record correction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2344-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/koraiol.yaml; Whole current owner plaintext and complete curation_history | supports | Complete current owner and all 2 history entries; native curation_status remains SEEDED. |
| bgc-2344-capture | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/3 | supports | Complete captured owner preserves every written field/history; selected maintained-reader applicability is false and no component reference is declared. |
| bgc-2344-intake | /private/tmp/npm-review-work/shared-next-batch235/intakes/2344-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical intake for naturalproductmech:mibig-8ecf532445; 37 pinned input placements and explicit maintained source/curator ownership. |
| bgc-2344-grounding-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"chemical_structure":{"smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001642"},"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-8ecf532445","label":"koraiol","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-8ecf532445","source":"MIBIG","source_id":"BGC0001642","source_label":"koraiol","source_version":"3"}]} |
| bgc-2344-origin-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001642","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"3","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001642 entry version 3; citation taken from the entry level","reference":"PMID:23335243"}],"genome_accession":"genbank:HF679030.1","link_evidence_basis":"CLUSTER_UNSTATED","locus_from":2313680,"locus_to":2315399,"organism_label":"Fusarium fujikuroi IMI 58289","organism_taxon_id":"NCBITaxon:1279085"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001642","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG BGC0001642 entry version 3; citation taken from the entry level","reference":"PMID:23335243"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"3","taxon_id":"NCBITaxon:1279085","taxon_label":"Fusarium fujikuroi IMI 58289"}],"producer_taxon_groups":["FUNGAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-8ecf532445","source":"MIBIG","source_id":"BGC0001642","source_label":"koraiol","source_version":"3"}]} |
| bgc-2344-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure, so the record keeps a content-hashed identifier.","occurrence_taxon_groups":["LAND_PLANT"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS structure-organism-reference triple. LOTUS reports that the compound was found in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1007/BF00565927"}],"notes":"Wikidata organism http://www.wikidata.org/entity/Q301636","source":"LOTUS","taxon_id":"NCBITaxon:88728","taxon_label":"Pinus koraiensis","taxon_source":"NCBITaxon"}]} |
| bgc-2344-assay-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {} |
| bgc-2344-classification-owner | /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete written field projection; absence is bounded by the complete captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":["Presilphiperfolane and Probotryane sesquiterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Sesquiterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"} |
| bgc-2344-chemistry | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | supports | Both stored forms parsed. Exact original comparison/correspondence and stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One chirality-aware substructure match; no independent full graph or natural identity claim.","smiles_to_inchi_atom_indices":[0,12,8,10,9,4,7,14,11,13,6,5,2,3,15,1]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001642"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Unspecified":5},"smiles":{"Atom_Tetrahedral:Unspecified":5}}} |
| bgc-2344-topology | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/declared_structure; /records/3/literal_InChI_layers; /records/3/comparisons; /records/3/atom_correspondence | supports | Complete saved topology interpretation: Both saved forms are neutral C15H26O with 16 heavy atoms and 18 single bonds. The saved carbocyclic ring basis has sizes 4, 7 and 4 in a polycyclic framework. Its single oxygen is a tertiary hydroxyl, SMILES O14H attached to C7; no ether, carbonyl or alkene is present. All five potential tetrahedral centres, SMILES 3, 4, 7, 8 and 9, are unspecified in both forms. The graph contains no separate sugar residue or glycosidic linkage. The full key and canonical correspondence preserve this partial structure rather than supplying missing stereochemistry. |
| bgc-2344-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json; Whole current diagnostic-execution | supports | ROOT operated one original stored-form diagnostic, exit 0, one attempt, preserved original streams and closed environment. This execution receipt is not independent scientific verification. |
| bgc-2344-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /DATA; /execution; /verification; /warning_scope; /limits | supports | ROOT accepts the original 20 stored parses and exact original comparisons/key/capture joins. Two original undefined-stereo and two charge-rearrangement warnings remain global and unassigned. Acceptance establishes local execution integrity, not natural identity or full graph proof. |
| bgc-2344-native-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json; Whole current native-acceptance | supports | Five original local gates passed. Full QC and complete OAK coverage remain unavailable, so these results do not establish all required validation or a scientific verdict. |
| bgc-2344-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json; Whole current intake-acceptance | supports | ROOT accepts ten actual canonical intakes and exact current source ownership/input plans; scientific assessment is separate. |
| bgc-2344-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json; Whole current inventory-acceptance | supports | ROOT accepts the original saved inventory and current input/raw/query/row joins. Complete meaning reading is separately attributed in source notes. |
| bgc-2344-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json; Whole current plan-acceptance | supports | ROOT accepts the actual input plan and preserved source contexts, without a scientific verdict. |
| bgc-2344-plan | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json; /records/3 | supports | Current one-record input plan with exact direct companions, predicates and input roles. |
| bgc-2344-source-notes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /reading; /cautions; /scientific_limits | supports | Complete disjoint source/raw-history reading and exact carries, with compound-specific cautions; source planning did not adjudicate pre-intake science. |
| bgc-2344-curation-scope | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json; /curation | supports | ROOT explicitly opened eight implemented curation tables, including ignored files, over 1233 casefolded literal tokens. One taxon-only rationale hit at unrelated BGC0001648:1 does not support any present compound/locus strain transfer; there was no current key, identifier, owned-BGC, label or slug hit. Reserved decisions.tsv, queue and unresolved-taxon routes were not consumed. This is bounded coverage, not universal absence. |
| bgc-2344-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/mibig_compounds | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":1962,"physical_line":1962,"raw_tsv_record":"BGC0001642\t3\tactive\tquestionable\tunknown\tkoraiol\t1\tCC1(CC2C1CCC(C3C2(CC3)C)(C)O)C\tInChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3\tCPLGPDHGFNXBOA-UHFFFAOYSA-N\tfalse\t\t\tNCBITaxon:1279085\tFusarium fujikuroi IMI 58289\tterpene\tUnknown\tHF679030.1\t2313680\t2315399\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:23335243\tENTRY\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"koraiol","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HF679030.1","locus_evidence_methods":"","locus_from":"2313680","locus_to":"2315399","mibig_accession":"BGC0001642","primary_reference":"PMID:23335243","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:1279085","taxon_label":"Fusarium fujikuroi IMI 58289"},"row_sha256":"013088fc02071ab501c2f64186ffdc70966d181f68a086d79799395cb16c45a2"}],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1962–1962, row_sha256 013088fc02071ab501c2f64186ffdc70966d181f68a086d79799395cb16c45a2 | supports | Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"koraiol","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HF679030.1","locus_evidence_methods":"","locus_from":"2313680","locus_to":"2315399","mibig_accession":"BGC0001642","primary_reference":"PMID:23335243","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:1279085","taxon_label":"Fusarium fujikuroi IMI 58289"}] |
| bgc-2344-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_structures | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":844,"physical_line":844,"raw_tsv_record":"CPLGPDHGFNXBOA-UHFFFAOYSA-N\tPinus koraiensis\tNCBITaxon:88728\thttp://www.wikidata.org/entity/Q301636\t10.1007/BF00565927\thttp://www.wikidata.org/entity/Q104967629\n","row":{"organism_name":"Pinus koraiensis","organism_wikidata":"http://www.wikidata.org/entity/Q301636","reference_doi":"10.1007/BF00565927","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104967629","taxon_id":"NCBITaxon:88728"},"row_sha256":"32434af140b174a2c3a0407c3e591aad069142a50f36e35e26e9a5b91aedcfc5"}],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 844–844, row_sha256 32434af140b174a2c3a0407c3e591aad069142a50f36e35e26e9a5b91aedcfc5 | supports | Complete retained physical row payloads, every field: [{"organism_name":"Pinus koraiensis","organism_wikidata":"http://www.wikidata.org/entity/Q301636","reference_doi":"10.1007/BF00565927","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104967629","taxon_id":"NCBITaxon:88728"}] |
| bgc-2344-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/npclassifier | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[{"last_physical_line":323,"physical_line":323,"raw_tsv_record":"CPLGPDHGFNXBOA-UHFFFAOYSA-N\tCC1(CC2C1CCC(C3C2(CC3)C)(C)O)C\tTerpenoids\tSesquiterpenoids\tPresilphiperfolane and Probotryane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Presilphiperfolane and Probotryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","superclass_results":"Sesquiterpenoids"},"row_sha256":"610856e9820296007ba2519d9bb439a9c643aa474951faa65f7a60ba07f4a4e6"}],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 323–323, row_sha256 610856e9820296007ba2519d9bb439a9c643aa474951faa65f7a60ba07f4a4e6 | supports | Complete retained physical row payloads, every field: [{"class_results":"Presilphiperfolane and Probotryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","superclass_results":"Sesquiterpenoids"}] |
| bgc-2344-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"} |
| bgc-2344-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_origins | supports | Complete retained query frame, exact predicate and all matches/no-match fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure rows","query":[]} |
| bgc-2344-source-routes | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/source_taxa; /contexts/7/source_scope_inventory/forward_taxon_merge_matches; /contexts/7/source_scope_inventory/nonorganism_matches; /contexts/7/source_scope_inventory/actual_assay_rows; /contexts/7/source_scope_inventory/blank_AID_sentinels; /contexts/7/source_scope_inventory/related_corpus_rows | supports | Exact source taxa and route lists; source_taxa is distinct from the empty forward/nonorganism and actual-assay/related routes; a blank-AID sentinel is separate: {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:1279085","NCBITaxon:88728"]} |
| bgc-2344-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/285; /cached_taxonomy/whole_stanzas/837 | supports | Complete relevant cached stanzas, with no fresh taxonomy verification: [{"complete_stanza":"[Term]\nid: NCBITaxon:88728\nname: Pinus koraiensis\n\n","id":"NCBITaxon:88728","physical_line":38674},{"complete_stanza":"[Term]\nid: NCBITaxon:1279085\nname: Fusarium fujikuroi IMI 58289\nsynonym: \"Fusarium fujikuroi IMI58289\" EXACT []\nsynonym: \"Gibberella fujikuroi IMI 58289\" EXACT []\n\n","id":"NCBITaxon:1279085","physical_line":125091}] |
| bgc-2344-direct-contexts | /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json; /records/3/direct_companion_paths; /records/3/direct_companion_predicates | supports | Exact one-hop scope, with no claim transfer: {"direct_companion_paths":[],"direct_companion_predicates":[]} |
| bgc-2344-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | The structure flag describes undefined stereocentres. ComputedClassification is explicitly a named/versioned prediction from structure, never a source assertion or an admission criterion. |
| bgc-2344-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | Maintained stereo_complete derives from FindMolChiralCenters and absence of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity proof. |
| bgc-2344-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 972–1020 | supports | Maintained seeding preserves lead source structures and named/versioned computed predictions separately; the computed pathway can control filing without becoming a source assertion. |
| bgc-2344-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole current profile | supports | One-record claim-level scientific review requires twelve dimensions and truthful partial completion/unavailable-check limits. |
| bgc-2344-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole current skill | supports | The review does not edit source records; the overriding absolute no-request instruction limits evidence access to retained local files. |
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
review_id: 20261104T050441Z-koraiol
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: koraiol'
started_at: '2026-11-04T04:24:34.139809Z'
finished_at: '2026-11-04T05:04:41.470810Z'
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
summary: Koraiol retains a consistent neutral C15H26O bridged polycyclic alcohol representation
  with all five potential tetrahedral centres unspecified. The Fusarium producer assertion
  and Pinus occurrence remain distinct. The versioned scaffold prediction is preserved
  without assigning an unencoded natural stereoisomer or a complete mechanism.
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
  - path: data/natural_products/terpenoids/koraiol.yaml
    sha256: 19202a3b6f664f6e2c048e6e088dbaf33ebfb5d74ca29672652e588337e420d4
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
  selection: Campaign path order 2344; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-8ecf532445
targets:
- target_id: naturalproductmech:mibig-8ecf532445
  path: data/natural_products/terpenoids/koraiol.yaml
  label: koraiol
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
  - naturalproductmech:mibig-8ecf532445
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
  - naturalproductmech:mibig-8ecf532445
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
  - naturalproductmech:mibig-8ecf532445
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
  - naturalproductmech:mibig-8ecf532445
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
  - naturalproductmech:mibig-8ecf532445
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
  - naturalproductmech:mibig-8ecf532445
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2344-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/koraiol.yaml
  locator: Whole current owner plaintext and complete curation_history
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete current owner and all 2 history entries; native curation_status
    remains SEEDED.
  snapshot_sha256: 19202a3b6f664f6e2c048e6e088dbaf33ebfb5d74ca29672652e588337e420d4
- evidence_id: bgc-2344-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete captured owner preserves every written field/history; selected
    maintained-reader applicability is false and no component reference is declared.
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2344-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/intakes/2344-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Actual canonical intake for naturalproductmech:mibig-8ecf532445; 37 pinned
    input placements and explicit maintained source/curator ownership.
  snapshot_sha256: 4f4b321ab7494cf83bd531d1231ba146172d1e6594fc1424d61b3cc28692f31e
- evidence_id: bgc-2344-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"chemical_structure":{"smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001642"},"grounding_notes":"No
    3-star ChEBI entry shares this structure, so the record keeps a content-hashed
    identifier.","grounding_status":"MINTED","identifier":"naturalproductmech:mibig-8ecf532445","label":"koraiol","source_concepts":[{"minted_identifier":"naturalproductmech:mibig-8ecf532445","source":"MIBIG","source_id":"BGC0001642","source_label":"koraiol","source_version":"3"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2344-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"biosynthetic_gene_clusters":[{"accession":"mibig:BGC0001642","bgc_class":["TERPENE"],"entry_status":"active","entry_version":"3","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001642 entry version 3; citation taken from the entry level","reference":"PMID:23335243"}],"genome_accession":"genbank:HF679030.1","link_evidence_basis":"CLUSTER_UNSTATED","locus_from":2313680,"locus_to":2315399,"organism_label":"Fusarium
    fujikuroi IMI 58289","organism_taxon_id":"NCBITaxon:1279085"}],"producer_organisms":[{"biosynthetic_gene_cluster":"mibig:BGC0001642","evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"MIBiG
    BGC0001642 entry version 3; citation taken from the entry level","reference":"PMID:23335243"}],"evidence_basis":"SOURCE_ASSERTION","notes":"Locus
    evidence: none stated. That evidence grades the LOCUS as CLUSTER_UNSTATED; this
    field grades the taxon claim, which is a different question.","source":"MIBIG","source_version":"3","taxon_id":"NCBITaxon:1279085","taxon_label":"Fusarium
    fujikuroi IMI 58289"}],"producer_taxon_groups":["FUNGAL"],"source_concepts":[{"minted_identifier":"naturalproductmech:mibig-8ecf532445","source":"MIBIG","source_id":"BGC0001642","source_label":"koraiol","source_version":"3"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2344-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"grounding_notes":"No 3-star ChEBI entry shares this structure,
    so the record keeps a content-hashed identifier.","occurrence_taxon_groups":["LAND_PLANT"],"occurrences":[{"evidence":[{"evidence_type":"DATABASE_ASSERTION","notes":"LOTUS
    structure-organism-reference triple. LOTUS reports that the compound was found
    in the organism; it does not assert that the organism produces it.","reference":"DOI:10.1007/BF00565927"}],"notes":"Wikidata
    organism http://www.wikidata.org/entity/Q301636","source":"LOTUS","taxon_id":"NCBITaxon:88728","taxon_label":"Pinus
    koraiensis","taxon_source":"NCBITaxon"}]}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2344-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2344-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete written field projection; absence is bounded by the complete
    captured owner: {"bgc_class":["TERPENE"],"biosynthesis_origin":"NATURAL_PRODUCT","np_classification":{"class_results":["Presilphiperfolane
    and Probotryane sesquiterpenoids"],"is_glycoside":false,"pathway_results":["Terpenoids"],"superclass_results":["Sesquiterpenoids"],"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07"},"np_pathway":"TERPENOIDS"}'
  snapshot_sha256: 737113ad2be45fc9acc4de288533248ae3f569c8c5cb2b430be99880d0d8d705
- evidence_id: bgc-2344-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/smiles/status; /records/3/inchi/status;
    /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons;
    /records/3/atom_correspondence
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Both stored forms parsed. Exact original comparison/correspondence and
    stereo values: {"atom_correspondence":{"complete_atom_count_match":true,"full_graph_identity_established":false,"scope":"One
    chirality-aware substructure match; no independent full graph or natural identity
    claim.","smiles_to_inchi_atom_indices":[0,12,8,10,9,4,7,14,11,13,6,5,2,3,15,1]},"comparisons":{"atom_count_equal":true,"bond_count_equal":true,"both_keys_equal_declared":true,"canonical_isomeric_smiles_equal":true,"canonical_nonisomeric_smiles_equal":true,"formal_charge_equal":true,"formula_equal":true,"smiles_formula_equals_literal_InChI_main_layer":true,"standard_inchi_equal":true,"standard_inchi_key_equal":true},"declared_structure":{"smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":false,"structure_source":"MIBIG","structure_source_id":"mibig:BGC0001642"},"saved_stereo":{"inchi":{"Atom_Tetrahedral:Unspecified":5},"smiles":{"Atom_Tetrahedral:Unspecified":5}}}'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: bgc-2344-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed; /records/3/inchi/computed; /records/3/declared_structure;
    /records/3/literal_InChI_layers; /records/3/comparisons; /records/3/atom_correspondence
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete saved topology interpretation: Both saved forms are neutral C15H26O
    with 16 heavy atoms and 18 single bonds. The saved carbocyclic ring basis has
    sizes 4, 7 and 4 in a polycyclic framework. Its single oxygen is a tertiary hydroxyl,
    SMILES O14H attached to C7; no ether, carbonyl or alkene is present. All five
    potential tetrahedral centres, SMILES 3, 4, 7, 8 and 9, are unspecified in both
    forms. The graph contains no separate sugar residue or glycosidic linkage. The
    full key and canonical correspondence preserve this partial structure rather than
    supplying missing stereochemistry.'
  snapshot_sha256: aeff6d2db3c52b75fa7cd85438a014925445302087c33263b7522f3f556e0d4c
- evidence_id: bgc-2344-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/chemistry-local/diagnostic-execution-001.json
  locator: Whole current diagnostic-execution
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT operated one original stored-form diagnostic, exit 0, one attempt,
    preserved original streams and closed environment. This execution receipt is not
    independent scientific verification.
  snapshot_sha256: c6f0da32c1be702c997e92c5892ea02e38a069abc6c0b720fa4e1338b674661c
- evidence_id: bgc-2344-diagnostic-acceptance
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
- evidence_id: bgc-2344-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-native-five-gates-acceptance-001.json
  locator: Whole current native-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Five original local gates passed. Full QC and complete OAK coverage remain
    unavailable, so these results do not establish all required validation or a scientific
    verdict.
  snapshot_sha256: 713d96670fed493630776183217dec028aa27c64ca70142c925e14679e8064bc
- evidence_id: bgc-2344-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-intake-native-acceptance-001.json
  locator: Whole current intake-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts ten actual canonical intakes and exact current source ownership/input
    plans; scientific assessment is separate.
  snapshot_sha256: 97b8f40e4ce5c08c4508e916b5951f267a4aba333bf78abf8275d7c8c865e7f0
- evidence_id: bgc-2344-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-inventory-acceptance-001.json
  locator: Whole current inventory-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the original saved inventory and current input/raw/query/row
    joins. Complete meaning reading is separately attributed in source notes.
  snapshot_sha256: efe55c8fc90acc75742e2e133be3d52885ba31a8027a7ef4736e7bc020950af9
- evidence_id: bgc-2344-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235/root-source-plan-acceptance-001.json
  locator: Whole current plan-acceptance
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: ROOT accepts the actual input plan and preserved source contexts, without
    a scientific verdict.
  snapshot_sha256: ebd812deb22f4b63b07c62f2cfb77b5ccaefd41fa85e5da34e9ad033ab96431c
- evidence_id: bgc-2344-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Current one-record input plan with exact direct companions, predicates
    and input roles.
  snapshot_sha256: 4534eaf8666f0c106f388a2d17af4dc6b1edc20f665e7aef9a03813706c19ddb
- evidence_id: bgc-2344-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-scope-notes-001.json
  locator: /reading; /cautions; /scientific_limits
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Complete disjoint source/raw-history reading and exact carries, with compound-specific
    cautions; source planning did not adjudicate pre-intake science.
  snapshot_sha256: 8c85f257f59a062eabc086ac4dd94acabd196bf072e6d66aa20f1215dd31aaa7
- evidence_id: bgc-2344-curation-scope
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
- evidence_id: bgc-2344-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":1962,"physical_line":1962,"raw_tsv_record":"BGC0001642\t3\tactive\tquestionable\tunknown\tkoraiol\t1\tCC1(CC2C1CCC(C3C2(CC3)C)(C)O)C\tInChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3\tCPLGPDHGFNXBOA-UHFFFAOYSA-N\tfalse\t\t\tNCBITaxon:1279085\tFusarium
    fujikuroi IMI 58289\tterpene\tUnknown\tHF679030.1\t2313680\t2315399\t\tSOURCE_ASSERTION\tCLUSTER_UNSTATED\tPMID:23335243\tENTRY\n","row":{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"koraiol","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HF679030.1","locus_evidence_methods":"","locus_from":"2313680","locus_to":"2315399","mibig_accession":"BGC0001642","primary_reference":"PMID:23335243","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:1279085","taxon_label":"Fusarium
    fujikuroi IMI 58289"},"row_sha256":"013088fc02071ab501c2f64186ffdc70966d181f68a086d79799395cb16c45a2"}],"predicate":"exact
    complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1962–1962, row_sha256 013088fc02071ab501c2f64186ffdc70966d181f68a086d79799395cb16c45a2
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"bgc_classes":"terpene","bgc_subclasses":"Unknown","cluster_link_evidence_basis":"CLUSTER_UNSTATED","compound_classes":"","compound_index":"1","compound_name":"koraiol","database_ids":"","entry_completeness":"unknown","entry_quality":"questionable","entry_status":"active","entry_version":"3","genome_accession":"HF679030.1","locus_evidence_methods":"","locus_from":"2313680","locus_to":"2315399","mibig_accession":"BGC0001642","primary_reference":"PMID:23335243","producer_evidence_basis":"SOURCE_ASSERTION","reference_basis":"ENTRY","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi":"InChI=1S/C15H26O/c1-13(2)9-11-10(13)5-8-15(4,16)12-6-7-14(11,12)3/h10-12,16H,5-9H2,1-4H3","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","stereo_complete":"false","taxon_id":"NCBITaxon:1279085","taxon_label":"Fusarium
    fujikuroi IMI 58289"}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2344-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":844,"physical_line":844,"raw_tsv_record":"CPLGPDHGFNXBOA-UHFFFAOYSA-N\tPinus
    koraiensis\tNCBITaxon:88728\thttp://www.wikidata.org/entity/Q301636\t10.1007/BF00565927\thttp://www.wikidata.org/entity/Q104967629\n","row":{"organism_name":"Pinus
    koraiensis","organism_wikidata":"http://www.wikidata.org/entity/Q301636","reference_doi":"10.1007/BF00565927","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104967629","taxon_id":"NCBITaxon:88728"},"row_sha256":"32434af140b174a2c3a0407c3e591aad069142a50f36e35e26e9a5b91aedcfc5"}],"predicate":"exact
    complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 844–844, row_sha256 32434af140b174a2c3a0407c3e591aad069142a50f36e35e26e9a5b91aedcfc5
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"organism_name":"Pinus
    koraiensis","organism_wikidata":"http://www.wikidata.org/entity/Q301636","reference_doi":"10.1007/BF00565927","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","structure_wikidata":"http://www.wikidata.org/entity/Q104967629","taxon_id":"NCBITaxon:88728"}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2344-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[{"last_physical_line":323,"physical_line":323,"raw_tsv_record":"CPLGPDHGFNXBOA-UHFFFAOYSA-N\tCC1(CC2C1CCC(C3C2(CC3)C)(C)O)C\tTerpenoids\tSesquiterpenoids\tPresilphiperfolane
    and Probotryane sesquiterpenoids\tfalse\tnpclassifier.gnps2.org@2026-09-07\n","row":{"class_results":"Presilphiperfolane
    and Probotryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","superclass_results":"Sesquiterpenoids"},"row_sha256":"610856e9820296007ba2519d9bb439a9c643aa474951faa65f7a60ba07f4a4e6"}],"predicate":"exact
    complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 323–323, row_sha256 610856e9820296007ba2519d9bb439a9c643aa474951faa65f7a60ba07f4a4e6
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained physical row payloads, every field: [{"class_results":"Presilphiperfolane
    and Probotryane sesquiterpenoids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":"Terpenoids","smiles":"CC1(CC2C1CCC(C3C2(CC3)C)(C)O)C","standard_inchi_key":"CPLGPDHGFNXBOA-UHFFFAOYSA-N","superclass_results":"Sesquiterpenoids"}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2344-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact complete standard_inchi_key equality","query":"CPLGPDHGFNXBOA-UHFFFAOYSA-N"}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete retained query frame, exact predicate and all matches/no-match
    fields: {"matches":[],"predicate":"exact chebi_id from exact full-key structure
    rows","query":[]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/source_taxa; /contexts/7/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/7/source_scope_inventory/nonorganism_matches; /contexts/7/source_scope_inventory/actual_assay_rows;
    /contexts/7/source_scope_inventory/blank_AID_sentinels; /contexts/7/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Exact source taxa and route lists; source_taxa is distinct from the empty
    forward/nonorganism and actual-assay/related routes; a blank-AID sentinel is separate:
    {"actual_assay_rows":[],"blank_AID_sentinels":[],"forward_taxon_merge_matches":[],"nonorganism_matches":[],"related_corpus_rows":[],"source_taxa":["NCBITaxon:1279085","NCBITaxon:88728"]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/285; /cached_taxonomy/whole_stanzas/837
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Complete relevant cached stanzas, with no fresh taxonomy verification:
    [{"complete_stanza":"[Term]\nid: NCBITaxon:88728\nname: Pinus koraiensis\n\n","id":"NCBITaxon:88728","physical_line":38674},{"complete_stanza":"[Term]\nid:
    NCBITaxon:1279085\nname: Fusarium fujikuroi IMI 58289\nsynonym: \"Fusarium fujikuroi
    IMI58289\" EXACT []\nsynonym: \"Gibberella fujikuroi IMI 58289\" EXACT []\n\n","id":"NCBITaxon:1279085","physical_line":125091}]'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch235-tentative/bgc-prep/bgc-conditional235-source-inventory-DATA-001.json
  locator: /records/3/direct_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: 'Exact one-hop scope, with no claim transfer: {"direct_companion_paths":[],"direct_companion_predicates":[]}'
  snapshot_sha256: c2c0b5aea707e489d5ee15669255da5bd3355adc7faba67c80f438ee9dd68ca7
- evidence_id: bgc-2344-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: The structure flag describes undefined stereocentres. ComputedClassification
    is explicitly a named/versioned prediction from structure, never a source assertion
    or an admission criterion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2344-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Maintained stereo_complete derives from FindMolChiralCenters and absence
    of question-mark centre tags. It is not blanket all-bond-geometry or natural-identity
    proof.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2344-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 972–1020
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: Maintained seeding preserves lead source structures and named/versioned
    computed predictions separately; the computed pathway can control filing without
    becoming a source assertion.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2344-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole current profile
  accessed_at: '2026-11-04T04:55:26.828096Z'
  support: supports
  summary: One-record claim-level scientific review requires twelve dimensions and
    truthful partial completion/unavailable-check limits.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2344-review-skill
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
- assessment_id: bgc-2344-identity
  area: identity
  topic: Retained identity and form consistency; exact natural identity unverified
  outcome: supported
  summary: The owner naturalproductmech:mibig-8ecf532445 preserves literal koraiol
    and full key CPLGPDHGFNXBOA-UHFFFAOYSA-N. Its MINTED status and historical no-3-star-ChEBI-match
    note agree with the bounded empty exact-key source join, without claiming that
    no external identity exists. Both stored forms agree on connectivity and unresolved
    stereochemical status. No tetrahedral configuration is specified, so the record
    does not establish one exact natural stereoisomer from its name or model class.
    No direct companion is admitted for this selected key.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-grounding-owner
  - bgc-2344-source-mibig_compounds
  - bgc-2344-query-chebi_structures
  - bgc-2344-chemistry
  - bgc-2344-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: CPLGPDHGFNXBOA-UHFFFAOYSA-N; exact full retained key, not a name or connectivity-block
      substitute.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2344-grounding-owner
    - bgc-2344-source-mibig_compounds
    - bgc-2344-query-chebi_structures
    - bgc-2344-chemistry
    - bgc-2344-direct-contexts
  - name: grounding_scope
    value: The owner naturalproductmech:mibig-8ecf532445 preserves literal koraiol
      and full key CPLGPDHGFNXBOA-UHFFFAOYSA-N. Its MINTED status and historical no-3-star-ChEBI-match
      note agree with the bounded empty exact-key source join, without claiming that
      no external identity exists. Both stored forms agree on connectivity and unresolved
      stereochemical status. No tetrahedral configuration is specified, so the record
      does not establish one exact natural stereoisomer from its name or model class.
      No direct companion is admitted for this selected key.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2344-grounding-owner
    - bgc-2344-source-mibig_compounds
    - bgc-2344-query-chebi_structures
    - bgc-2344-chemistry
    - bgc-2344-direct-contexts
- assessment_id: bgc-2344-representation
  area: representation
  topic: Stored molecular representation
  outcome: supported
  summary: Both saved forms are neutral C15H26O with 16 heavy atoms and 18 single
    bonds. The saved carbocyclic ring basis has sizes 4, 7 and 4 in a polycyclic framework.
    Its single oxygen is a tertiary hydroxyl, SMILES O14H attached to C7; no ether,
    carbonyl or alkene is present. All five potential tetrahedral centres, SMILES
    3, 4, 7, 8 and 9, are unspecified in both forms. The graph contains no separate
    sugar residue or glycosidic linkage. The full key and canonical correspondence
    preserve this partial structure rather than supplying missing stereochemistry.
    The maintained stereo_complete field is derived from tetrahedral-centre assignment
    and is not a universal bond-geometry, optical-sign or natural-identity certificate.
    All ten original pair-comparison flags and complete atom-count correspondence
    are true for this record, while full_graph_identity_established remains false.
    No new molecular parse or alternate structure was introduced.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-chemistry
  - bgc-2344-topology
  - bgc-2344-grounding-owner
  - bgc-2344-stereo-method
  - bgc-2344-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms are neutral C15H26O with 16 heavy atoms and 18 single
      bonds. The saved carbocyclic ring basis has sizes 4, 7 and 4 in a polycyclic
      framework. Its single oxygen is a tertiary hydroxyl, SMILES O14H attached to
      C7; no ether, carbonyl or alkene is present. All five potential tetrahedral
      centres, SMILES 3, 4, 7, 8 and 9, are unspecified in both forms. The graph contains
      no separate sugar residue or glycosidic linkage. The full key and canonical
      correspondence preserve this partial structure rather than supplying missing
      stereochemistry. The maintained stereo_complete field is derived from tetrahedral-centre
      assignment and is not a universal bond-geometry, optical-sign or natural-identity
      certificate. All ten original pair-comparison flags and complete atom-count
      correspondence are true for this record, while full_graph_identity_established
      remains false. No new molecular parse or alternate structure was introduced.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2344-chemistry
    - bgc-2344-topology
    - bgc-2344-grounding-owner
    - bgc-2344-stereo-method
    - bgc-2344-structure-schema
  - name: representation_correspondence
    value: All ten saved comparisons and complete atom-count correspondence are true;
      original full_graph_identity_established remains false. Stored normalization
      is not independent exact natural-graph identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2344-chemistry
    - bgc-2344-topology
    - bgc-2344-grounding-owner
    - bgc-2344-stereo-method
    - bgc-2344-structure-schema
- assessment_id: bgc-2344-provenance
  area: provenance
  topic: Producer and locus evidence
  outcome: supported
  summary: MIBiG row 1962 belongs to BGC0001642 version 3 and asserts Fusarium fujikuroi
    IMI 58289, NCBITaxon:1279085, as producer at SOURCE_ASSERTION grade. The TERPENE
    locus HF679030.1:2313680-2315399 is CLUSTER_UNSTATED with no retained experimental
    method. The Pinus koraiensis occurrence at NCBITaxon:88728 is a separately attributed
    source observation, not evidence that the fungal strain assertion or exact biosynthetic
    locus was newly verified. Cached taxon names preserve their own local scope.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-origin-owner
  - bgc-2344-source-mibig_compounds
  - bgc-2344-cached-taxonomy
  - bgc-2344-source-routes
  dimensions:
  - name: taxon_scope
    value: MIBiG row 1962 belongs to BGC0001642 version 3 and asserts Fusarium fujikuroi
      IMI 58289, NCBITaxon:1279085, as producer at SOURCE_ASSERTION grade. The TERPENE
      locus HF679030.1:2313680-2315399 is CLUSTER_UNSTATED with no retained experimental
      method. The Pinus koraiensis occurrence at NCBITaxon:88728 is a separately attributed
      source observation, not evidence that the fungal strain assertion or exact biosynthetic
      locus was newly verified. Cached taxon names preserve their own local scope.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2344-origin-owner
    - bgc-2344-source-mibig_compounds
    - bgc-2344-cached-taxonomy
    - bgc-2344-source-routes
  - name: producer_evidence
    value: MIBiG row 1962 belongs to BGC0001642 version 3 and asserts Fusarium fujikuroi
      IMI 58289, NCBITaxon:1279085, as producer at SOURCE_ASSERTION grade. The TERPENE
      locus HF679030.1:2313680-2315399 is CLUSTER_UNSTATED with no retained experimental
      method. The Pinus koraiensis occurrence at NCBITaxon:88728 is a separately attributed
      source observation, not evidence that the fungal strain assertion or exact biosynthetic
      locus was newly verified. Cached taxon names preserve their own local scope.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2344-origin-owner
    - bgc-2344-source-mibig_compounds
    - bgc-2344-cached-taxonomy
    - bgc-2344-source-routes
  - name: locus_evidence
    value: MIBiG row 1962 belongs to BGC0001642 version 3 and asserts Fusarium fujikuroi
      IMI 58289, NCBITaxon:1279085, as producer at SOURCE_ASSERTION grade. The TERPENE
      locus HF679030.1:2313680-2315399 is CLUSTER_UNSTATED with no retained experimental
      method. The Pinus koraiensis occurrence at NCBITaxon:88728 is a separately attributed
      source observation, not evidence that the fungal strain assertion or exact biosynthetic
      locus was newly verified. Cached taxon names preserve their own local scope.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2344-origin-owner
    - bgc-2344-source-mibig_compounds
    - bgc-2344-cached-taxonomy
    - bgc-2344-source-routes
- assessment_id: bgc-2344-citations
  area: evidence
  topic: Citation scope
  outcome: supported
  summary: The locus source retains PMID:23335243 at ENTRY level. The Pinus occurrence
    instead cites DOI:10.1007/BF00565927. These distinct roles must remain attached
    to their corresponding claims; the entry citation is not automatically a compound-specific
    structure, enzyme or activity assay. Neither publication was accessed anew, and
    differing identifier strings alone do not establish independent experimental confirmation
    of the exact partial-stereo structure.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-grounding-owner
  - bgc-2344-origin-owner
  - bgc-2344-source-mibig_compounds
  - bgc-2344-source-lotus_occurrences
  - bgc-2344-source-notes
  - bgc-2344-direct-contexts
  dimensions:
  - name: citation_scope
    value: The locus source retains PMID:23335243 at ENTRY level. The Pinus occurrence
      instead cites DOI:10.1007/BF00565927. These distinct roles must remain attached
      to their corresponding claims; the entry citation is not automatically a compound-specific
      structure, enzyme or activity assay. Neither publication was accessed anew,
      and differing identifier strings alone do not establish independent experimental
      confirmation of the exact partial-stereo structure.
    definition: Database provenance, retained historical primary-experiment support
      and occurrence citations have distinct scopes; repeated placements do not establish
      independent studies, and no fresh external access is claimed.
    evidence_ids:
    - bgc-2344-grounding-owner
    - bgc-2344-origin-owner
    - bgc-2344-source-mibig_compounds
    - bgc-2344-source-lotus_occurrences
    - bgc-2344-source-notes
    - bgc-2344-direct-contexts
- assessment_id: bgc-2344-occurrence
  area: evidence
  topic: Occurrence and assay scope
  outcome: supported
  summary: The written Pinus koraiensis occurrence matches the retained LOTUS row
    and DOI:10.1007/BF00565927. It supports that database occurrence assertion, not
    a transfer of fungal producer, locus or mechanism evidence. No bioactivity or
    molecular target is written, and the exact saved PubChem, BindingDB and AntibioticMech
    joins have no result. Those bounded negatives do not imply inactivity or the absence
    of all published assays; no phenotype or enzyme claim is inferred from the name.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-occurrence-owner
  - bgc-2344-assay-owner
  - bgc-2344-source-lotus_occurrences
  - bgc-2344-query-lotus_occurrences
  - bgc-2344-query-chebi_origins
  - bgc-2344-query-cyanometdb_occurrences
  - bgc-2344-query-pubchem_bioassay
  - bgc-2344-query-bindingdb_targets
  - bgc-2344-query-antibioticmech_inchikeys
  - bgc-2344-source-routes
  - bgc-2344-cached-taxonomy
  - bgc-2344-source-notes
  dimensions:
  - name: occurrence_scope
    value: The written Pinus koraiensis occurrence matches the retained LOTUS row
      and DOI:10.1007/BF00565927. It supports that database occurrence assertion,
      not a transfer of fungal producer, locus or mechanism evidence. No bioactivity
      or molecular target is written, and the exact saved PubChem, BindingDB and AntibioticMech
      joins have no result. Those bounded negatives do not imply inactivity or the
      absence of all published assays; no phenotype or enzyme claim is inferred from
      the name.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2344-occurrence-owner
    - bgc-2344-assay-owner
    - bgc-2344-source-lotus_occurrences
    - bgc-2344-query-lotus_occurrences
    - bgc-2344-query-chebi_origins
    - bgc-2344-query-cyanometdb_occurrences
    - bgc-2344-query-pubchem_bioassay
    - bgc-2344-query-bindingdb_targets
    - bgc-2344-query-antibioticmech_inchikeys
    - bgc-2344-source-routes
    - bgc-2344-cached-taxonomy
    - bgc-2344-source-notes
  - name: assay_target_scope
    value: No written bioactivity or molecular target and no actual assay/target result
      in the exact retained PubChem/BindingDB/AntibioticMech joins. A blank-AID sentinel,
      where present, is not an activity result. This is a bounded source result, not
      global inactivity or absence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2344-occurrence-owner
    - bgc-2344-assay-owner
    - bgc-2344-source-lotus_occurrences
    - bgc-2344-query-lotus_occurrences
    - bgc-2344-query-chebi_origins
    - bgc-2344-query-cyanometdb_occurrences
    - bgc-2344-query-pubchem_bioassay
    - bgc-2344-query-bindingdb_targets
    - bgc-2344-query-antibioticmech_inchikeys
    - bgc-2344-source-routes
    - bgc-2344-cached-taxonomy
    - bgc-2344-source-notes
- assessment_id: bgc-2344-classification
  area: consistency
  topic: Computed classification applicability
  outcome: supported
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids, Sesquiterpenoids,
    Presilphiperfolane and Probotryane sesquiterpenoids, and is_glycoside:false. The
    C15 polycyclic alcohol and absence of a separate sugar are compatible with broad
    sesquiterpenoid and non-glycoside applicability. The finer class is still a named/versioned
    prediction and does not resolve any of the five unspecified stereocentres or prove
    a specific rearrangement pathway. Source TERPENE membership and model output are
    retained separately; no exact natural stereoisomer or unrepresented mechanism
    is supplied.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-classification-owner
  - bgc-2344-source-npclassifier
  - bgc-2344-source-mibig_compounds
  - bgc-2344-chemistry
  - bgc-2344-topology
  - bgc-2344-structure-schema
  - bgc-2344-classification-seeder
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 reports Terpenoids, Sesquiterpenoids,
      Presilphiperfolane and Probotryane sesquiterpenoids, and is_glycoside:false.
      The C15 polycyclic alcohol and absence of a separate sugar are compatible with
      broad sesquiterpenoid and non-glycoside applicability. The finer class is still
      a named/versioned prediction and does not resolve any of the five unspecified
      stereocentres or prove a specific rearrangement pathway. Source TERPENE membership
      and model output are retained separately; no exact natural stereoisomer or unrepresented
      mechanism is supplied.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2344-classification-owner
    - bgc-2344-source-npclassifier
    - bgc-2344-source-mibig_compounds
    - bgc-2344-chemistry
    - bgc-2344-topology
    - bgc-2344-structure-schema
    - bgc-2344-classification-seeder
- assessment_id: bgc-2344-completion
  area: completeness
  topic: Scientific completion
  outcome: unknown
  summary: Complete owner/history, actual intake/source ownership, full retained matching
    rows and no-match frames, cache and both full saved molecular forms were read.
    No mechanism root or component is declared, so no maintained reader applies. The
    false source stereo_complete flag is preserved consistently with five unresolved
    centres. Full QC, complete OAK coverage and fresh primary/identity verification
    remain unavailable, leaving a partial review with no supported record correction.
  target_ids:
  - naturalproductmech:mibig-8ecf532445
  evidence_ids:
  - bgc-2344-owner
  - bgc-2344-capture
  - bgc-2344-intake
  - bgc-2344-plan
  - bgc-2344-intake-acceptance
  - bgc-2344-inventory-acceptance
  - bgc-2344-plan-acceptance
  - bgc-2344-source-notes
  - bgc-2344-curation-scope
  - bgc-2344-diagnostic-execution
  - bgc-2344-diagnostic-acceptance
  - bgc-2344-native-acceptance
  - bgc-2344-review-profile
  - bgc-2344-review-skill
  dimensions:
  - name: review_completion
    value: 'Partial: complete actual evidence and saved forms assessed; no maintained
      mechanism reader applies. Full QC/OAK and fresh primary/identity authority remain
      unavailable.'
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2344-owner
    - bgc-2344-capture
    - bgc-2344-intake
    - bgc-2344-plan
    - bgc-2344-intake-acceptance
    - bgc-2344-inventory-acceptance
    - bgc-2344-plan-acceptance
    - bgc-2344-source-notes
    - bgc-2344-curation-scope
    - bgc-2344-diagnostic-execution
    - bgc-2344-diagnostic-acceptance
    - bgc-2344-native-acceptance
    - bgc-2344-review-profile
    - bgc-2344-review-skill
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
