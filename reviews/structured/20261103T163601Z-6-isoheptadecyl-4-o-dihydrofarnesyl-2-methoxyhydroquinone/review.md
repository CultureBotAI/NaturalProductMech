# Local evidence review: 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone

- Review: 20261103T163601Z-6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T16:10:24.067092Z
- Finished UTC: 2026-11-03T16:36:01.180327Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone is locally consistent with its retained full-key MIBiG identity and alkyl/prenyl aromatic-ether structure. One unspecified tetrahedral centre, with one specified E alkene; retained false flag. Producer and locus support remain source assertion and CLUSTER_UNSTATED respectively; model filing, direct congeners and the shared citation do not expand that support. Scientific completion remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2253; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-447235379c | data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml | generated | 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-447235379c | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-447235379c | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-447235379c | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-447235379c | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-447235379c | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-447235379c | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-447235379c | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-447235379c | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-447235379c.

The minted identity naturalproductmech:mibig-447235379c follows exact MIBiG BGC0001077 version 4 compound index 10 and full key DXVIRWBLDDUQRP-DNGXXSEMSA-N. The saved exact ChEBI query is empty. The isoheptadecyl branch is not interchangeable with the same-formula anteisoheptadecyl branch. All nine direct companions remain separate owners; shared BGC membership does not permit a grounding or identity substitution.

### Representation

representation: supported. Targets: naturalproductmech:mibig-447235379c.

Both stored forms give neutral C38H66O3, 41 atoms and 41 bonds, with one connected fragment, all ten comparison flags true and a complete stored chirality-aware correspondence. One unspecified tetrahedral centre in the dihydrofarnesyl branch, SMILES atom 28 corresponding to InChI atom 32. The isoalkyl terminus has two identical methyl groups and is not an additional tetrahedral stereocentre. Each form has the proximal alkene specified E; the distal alkene has two identical methyl substituents, so it does not create an additional E/Z site. Local Cis/Trans potential-stereo descriptors differ with reference ordering while the mapped bond stereochemistry agrees. The retained false flag is consistent with the extractor’s tetrahedral-centre scope. The diagnostic leaves full_graph_identity_established false; none of this authenticates the natural isolated stereoisomer.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-447235379c.

MIBiG BGC0001077 version 4 is active, of questionable quality and unknown completeness. The retained strain Actinoplanes missouriensis 431, NCBITaxon:512565, has SOURCE_ASSERTION producer evidence. The locus remains CLUSTER_UNSTATED with no stated method. Its source PKS/Type III label and genbank:AP012319.1 interval 8379670–8386219 do not constitute a demonstrated complete pathway. The complete cached stanza names the same strain and records str. 431/strain 431 synonyms; no ancestry or fresh accession verification is inferred.

### Citations

evidence: unknown. Targets: naturalproductmech:mibig-447235379c.

DOI:10.1002/cbic.201000628 is retained at COMPOUND_EVIDENCE level and appears as DATABASE_ASSERTION on both the written producer and locus. Those placements do not constitute two independent experiments or fresh primary verification. The local source row does not supply an experimental locus method. Other BGC0001077 congeners and the separately curated 6-isopalmityl-4-O-geranyl graphs do not upgrade this owner’s claims.

### Bioactivity

evidence: supported. Targets: naturalproductmech:mibig-447235379c.

The complete owner writes no occurrences, assay observations, activity summary, molecular targets or mechanism roots. Exact saved LOTUS, ChEBI-origin, CyanometDB, PubChem, BindingDB and AntibioticMech routes are empty; no blank-AID sentinel is present for this owner. This is a bounded absence of retained assertions, not evidence of biological inactivity. The shared-locus congener with causal graphs remains a separate owner.

### Classification

consistency: unknown. Targets: naturalproductmech:mibig-447235379c.

NPClassifier version npclassifier.gnps2.org@2026-09-07 supplies Terpenoids and is_glycoside:false, with filing value TERPENOIDS. Empty superclass and class lists are retained. Separately, the source records PKS/Type III at the locus and Alkylresorcinol/phloroglucinol polyketide plus Sesquiterpenoid at compound level. The complete paired topology contains a substituted aromatic carbon ring, one phenolic OH and two ethers, with no sugar residue or sugar–aglycone linkage. That is compatible with the false glycoside prediction without turning a model output into independent biosynthetic or identity evidence. These distinct classification axes do not establish a local curation defect.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-447235379c.

The complete owner/history, exact retained source payloads, actual 46-input intake and both full saved molecular tables were reviewed. No supported local curation defect is established in this bounded scope. Five local gates passed; full QC, complete OAK and fresh external primary-source/taxonomy/accession verification were unavailable. No maintained reader is required for this owner’s absent mechanism roots. Scientific completion remains partial, with native curation status and history unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2253-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml; Whole owner plaintext and complete curation_history | supports | Complete 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone owner with two SEEDED_FROM_SOURCES history events and native curation status SEEDED. |
| bgc-2253-capture | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/2/owner_pin; /records/2/owner_document | supports | Complete saved owner and exact raw pin for order 2253. |
| bgc-2253-intake | /private/tmp/npm-review-work/shared-next-batch226/intakes/2253-inspect-001.json; /source; /targets | supports | Actual one-record intake for naturalproductmech:mibig-447235379c; 46 source placements, four declared maintained ownership paths and inspection-only ownership note. |
| bgc-2253-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-intake-ready-001.json; /accepted | supports | ROOT acceptance of the original ten actual intakes and their source-input joins. |
| bgc-2253-grounding-owner | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes | supports | MINTED owner naturalproductmech:mibig-447235379c, exact full key DXVIRWBLDDUQRP-DNGXXSEMSA-N, retained MIBiG source concept and source structure. |
| bgc-2253-origin-owner | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/bgc_class | supports | Written producer Actinoplanes missouriensis 431, NCBITaxon:512565, SOURCE_ASSERTION; BGC0001077 version 4, CLUSTER_UNSTATED, PKS and genbank:AP012319.1 coordinates 8379670–8386219. Both written evidence lists attach DOI:10.1002/cbic.201000628 as DATABASE_ASSERTION. |
| bgc-2253-assay-owner | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/2/owner_document | supports | The complete captured owner writes no bioactivities, bioactivity_summary, molecular_targets, causal_graphs, causal_graph_refs or biosynthetic_pathway root. |
| bgc-2253-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/2/owner_document | supports | The complete captured owner writes no occurrences root. |
| bgc-2253-classification-owner | /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json; /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class; /records/2/owner_document/compound_classes | supports | Literal written classification: {"bgc_class": ["PKS"], "compound_classes": ["Alkylresorcinol/phloroglucinol polyketide", "Sesquiterpenoid"], "np_classification": {"class_results": [], "is_glycoside": false, "pathway_results": ["Terpenoids"], "superclass_results": [], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"}, "np_pathway": "TERPENOIDS"} |
| bgc-2253-chemistry | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/smiles/status; /records/2/inchi/status; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons; /records/2/atom_correspondence | supports | Both stored forms parsed as neutral C38H66O3, 41 atoms and 41 bonds, one fragment and one ring. All ten comparison flags are true and the stored atom correspondence is complete; full_graph_identity_established remains false. Saved stereo_counts: {"inchi": {"Atom_Tetrahedral:Unspecified": 1, "Bond_Double:Specified": 1}, "smiles": {"Atom_Tetrahedral:Unspecified": 1, "Bond_Double:Specified": 1}} |
| bgc-2253-topology | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/atom_correspondence; /records/0/smiles/computed; /records/0/inchi/computed | supports | The full SMILES table contains aromatic ring atoms 1, 2, 19, 20, 37 and 38, phenolic oxygen 0, the prenyl ether through O21 and methoxy O39. The isoalkyl terminus differs from the anteiso congener despite the shared molecular formula. Both complete tables show one six-carbon aromatic ring, one phenolic OH, two carbon–oxygen–carbon ethers and two acyclic double bonds, with no carbonyl, ring oxygen or sugar residue topology. One unspecified tetrahedral centre in the dihydrofarnesyl branch, SMILES atom 28 corresponding to InChI atom 32. The isoalkyl terminus has two identical methyl groups and is not an additional tetrahedral stereocentre. The proximal alkene is E in both stored bond tables; the distal alkene has two identical methyl substituents and is not an additional E/Z site. Local Bond_Cis/Bond_Trans potential-stereo descriptors use different reference atom orderings and do not indicate a conflict here. |
| bgc-2253-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /external_requests; /retries | supports | Original saved diagnostic execution exited 0 with retries 0 and external_requests false; exact stdout and stderr paths and hashes are retained. |
| bgc-2253-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-001.stderr; Whole original stderr, eight warning entries | supports | Eight original batch-level omitted-undefined-stereo warnings are present. The stream does not identify record order; none is assigned to this owner. |
| bgc-2253-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-local-diagnostics-acceptance-001.json; /status; /DATA; /execution; /actual_intake_authority; /successful_forms; /comparison_flags_true; /comparison_flags_false; /scientific_reading; /limits; /full_QC_and_OAK | supports | ROOT accepts the original twenty successful saved forms with 98 true and two false comparison flags, preserves their limits, and separately attributes whole scientific readings. Only order 2257 has false canonical-SMILES flags; this is mechanical acceptance, not natural identity authentication. Full QC and OAK remain unavailable. |
| bgc-2253-native-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-native-five-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /scope | supports | ROOT accepts five local commands; all_native_gates_passed is false because full QC and ontology-consistency OAK are unavailable. Scope and original evidence remain explicit. |
| bgc-2253-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-source-inventory-acceptance-001.json; /accepted; /inventory; /source_placements; /source_paths; /technical_scope | supports | ROOT mechanically accepts the saved inventory, its 448 source placements and 72 paths, retaining scientific interpretation as a separate task. |
| bgc-2253-source-plan | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json; /records/2; /source_placement_count; /unique_source_path_count | supports | Accepted saved plan retains this complete owner and source context with 46 proposed input paths and no selected-reader requirement for this owner; batch source map totals 448 placements and 72 paths. |
| bgc-2253-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch226/root-input-plan-acceptance-001.json; /accepted; /plan; /source_notes; /source_placements; /unique_source_paths | supports | ROOT accepts the exact plan and source notes with 448 placements and 72 source paths; this is source planning rather than a scientific verdict. |
| bgc-2253-source-notes | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-scope-notes-001.json; /reading; /curation; /cautions; /inventory_ROOT_acceptance | supports | Pinned personal/delegated reading covers all 34 complete owner/history bodies, 306 query frames, 117 full positive payloads, 1387 CSV fields and 11 cached stanzas. The case-sensitive 84-literal direct-file scan of eight named curation tables has zero hits only in its declared scope; the PubChem exclusion scan is supplemental, and reserved decisions.tsv was not consumed. |
| bgc-2253-direct-contexts | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /records/2/direct_companion_predicates; /contexts/0/identifier; /contexts/0/standard_inchi_key; /contexts/0/owned_bgc_ids; /contexts/0/declared_mechanism_roots_literal; /contexts/1/identifier; /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/1/declared_mechanism_roots_literal; /contexts/2/identifier; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/2/declared_mechanism_roots_literal; /contexts/3/identifier; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/3/declared_mechanism_roots_literal; /contexts/13/identifier; /contexts/13/standard_inchi_key; /contexts/13/owned_bgc_ids; /contexts/13/declared_mechanism_roots_literal; /contexts/14/identifier; /contexts/14/standard_inchi_key; /contexts/14/owned_bgc_ids; /contexts/14/declared_mechanism_roots_literal; /contexts/16/identifier; /contexts/16/standard_inchi_key; /contexts/16/owned_bgc_ids; /contexts/16/declared_mechanism_roots_literal; /contexts/17/identifier; /contexts/17/standard_inchi_key; /contexts/17/owned_bgc_ids; /contexts/17/declared_mechanism_roots_literal; /contexts/18/identifier; /contexts/18/standard_inchi_key; /contexts/18/owned_bgc_ids; /contexts/18/declared_mechanism_roots_literal | supports | Nine direct companions share owned BGC0001077 but have distinct root identifiers and complete keys. The 6-isopalmityl-4-O-geranyl congener has retained causal_graphs; these are context for that separate owner and do not supply this owner with an enzyme, pathway or activity assertion. Exact companion profiles: [{"identifier": "naturalproductmech:mibig-3b73f6a516", "standard_inchi_key": "NOPAZUFYUXZIPZ-UHFFFAOYSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-1253be8cf8", "standard_inchi_key": "HPAIKUJKASWMKP-UHFFFAOYSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-9c1beabea6", "standard_inchi_key": "CEACUCBTLUKKIY-MUGXBBEHSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-cd91f14897", "standard_inchi_key": "RHKVCMWMMGYUTG-WEMUOSSPSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-8a8aaf4fce", "standard_inchi_key": "CVTKJHUYRMFMCV-DNGXXSEMSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-36f47126b7", "standard_inchi_key": "WOCMOPRAFKEPAY-BYNJWEBRSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-0d66b83278", "standard_inchi_key": "RRVPCBLEVREXDD-BYNJWEBRSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-6f48d22ee3", "standard_inchi_key": "XZJZCONDRDOIHG-MHTZHOPKSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier": "naturalproductmech:mibig-b6f11fae29", "standard_inchi_key": "PBBKVCVGOJSEOQ-XAYXJRQQSA-N", "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": ["causal_graphs"]}] |
| bgc-2253-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/8 | supports | Complete cached stanza: [Term]<br>id: NCBITaxon:512565<br>name: Actinoplanes missouriensis 431<br>synonym: "Actinoplanes missouriensis str. 431" EXACT []<br>synonym: "Actinoplanes missouriensis strain 431" EXACT []<br><br>This name/synonym stanza is not an ancestry or experimental production proof. |
| bgc-2253-source-routes | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/source_taxa; /contexts/15/source_scope_inventory/forward_taxon_merge_matches; /contexts/15/source_scope_inventory/nonorganism_matches; /contexts/15/source_scope_inventory/actual_assay_rows; /contexts/15/source_scope_inventory/blank_AID_sentinels; /contexts/15/source_scope_inventory/related_corpus_rows | supports | Retained taxon scope is NCBITaxon:512565; no matching forward-merge/nonorganism rows, actual assays, blank-AID sentinels or related-corpus rows in these exact saved routes. |
| bgc-2253-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 368–430 | supports | ChemicalStructure documents full-key limitations and undefined stereocentres. ComputedClassification is a named, versioned prediction, never a source assertion or reason for admission. |
| bgc-2253-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 142–173 | supports | The maintained structure_fields function derives standardized InChI/key from SMILES and sets stereo_complete from unassigned tetrahedral chiral-centre results. This source reading invokes no parser and does not broaden that flag into proof of natural stereochemistry. |
| bgc-2253-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 971–1037 | supports | The seeder retains minted grounding where no single ChEBI match is adopted, copies source structure fields, and copies versioned NPClassifier lists and its is_glycoside boolean. |
| bgc-2253-origin-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 1093–1151 | supports | The seeder separately emits the producer evidence basis and locus linkage basis, preserves claim citations, and writes source genome coordinates and applicable methods. |
| bgc-2253-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole profile; identity, source evidence, scientific dimensions and partial-review requirements | supports | The maintained review profile requires claim-level scientific interpretation, explicit source limits and independent evidence for producer, occurrence, locus and mechanism claims. |
| bgc-2253-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Whole review skill; evidence access and structured-review scope | supports | The one-record review procedure separates scientific review from curation edits and mechanical validation; unavailable verification remains explicit. The absolute no-request instruction controls external access. |
| bgc-2253-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/mibig_compounds | supports | Exact saved mibig_compounds predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 1 matched physical row(s). |
| bgc-2253-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV line 1251; header line 1; row SHA256 96b46cceb8053cb9d07e026d4c6c78b3cce4da3dccb11bb2edcb0a7fed1fde4e | supports | Complete retained row fields: {"bgc_classes": "PKS", "bgc_subclasses": "Type III", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "Alkylresorcinol/phloroglucinol polyketide&#124;Sesquiterpenoid", "compound_index": "10", "compound_name": "6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone", "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "4", "genome_accession": "AP012319.1", "locus_evidence_methods": "", "locus_from": "8379670", "locus_to": "8386219", "mibig_accession": "BGC0001077", "primary_reference": "DOI:10.1002/cbic.201000628", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_EVIDENCE", "smiles": "OC1=C(CCCCCCCCCCCCCC(C)C)C=C(OC/C=C(CCCC(CC/C=C(C)/C)C)\\C)C=C1OC", "standard_inchi": "InChI=1S/C38H66O3/c1-31(2)21-17-15-13-11-9-8-10-12-14-16-18-26-35-29-36(30-37(40-7)38(35)39)41-28-27-34(6)25-20-24-33(5)23-19-22-32(3)4/h22,27,29-31,33,39H,8-21,23-26,28H2,1-7H3/b34-27+", "standard_inchi_key": "DXVIRWBLDDUQRP-DNGXXSEMSA-N", "stereo_complete": "false", "taxon_id": "NCBITaxon:512565", "taxon_label": "Actinoplanes missouriensis 431"} |
| bgc-2253-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/chebi_structures | supports | Exact saved chebi_structures predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| bgc-2253-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/lotus_occurrences | supports | Exact saved lotus_occurrences predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| bgc-2253-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/cyanometdb_occurrences | supports | Exact saved cyanometdb_occurrences predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| bgc-2253-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/npclassifier | supports | Exact saved npclassifier predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 1 matched physical row(s). |
| bgc-2253-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV line 495; header line 1; row SHA256 8595522f3e85b9d0cd799e00d3ab30558a8946406de552beee9a89aff575823f | supports | Complete retained row fields: {"class_results": "", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids", "smiles": "OC1=C(CCCCCCCCCCCCCC(C)C)C=C(OC/C=C(CCCC(CC/C=C(C)/C)C)\\C)C=C1OC", "standard_inchi_key": "DXVIRWBLDDUQRP-DNGXXSEMSA-N", "superclass_results": ""} |
| bgc-2253-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/pubchem_bioassay | supports | Exact saved pubchem_bioassay predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| bgc-2253-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/bindingdb_targets | supports | Exact saved bindingdb_targets predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| bgc-2253-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Exact saved antibioticmech_inchikeys predicate exact complete standard_inchi_key equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| bgc-2253-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/chebi_origins | supports | Exact saved chebi_origins predicate exact chebi_id from exact full-key structure rows; query []. Only this retained table snapshot is covered. The complete frame contains 0 matched physical row(s). |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-226/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-226/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-226/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-226/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-226/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, genome accessions and primary publications were not refreshed under the absolute no-request instruction. Historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form parsing establish only their declared mechanical scope.
- Empty joins refer only to the retained exact predicates and snapshots; they do not establish biological absence. Shared loci, citations and congeners do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete retained source payloads and direct-context whole-reading attributions are in the pinned source notes. This owner/history, its actual intake and both full saved molecular tables were personally read.
- Eight original batch-level undefined-stereo warnings remain globally unassigned. True comparison flags and a complete stored atom correspondence do not override full_graph_identity_established:false.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T163601Z-6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone'
started_at: '2026-11-03T16:10:24.067092Z'
finished_at: '2026-11-03T16:36:01.180327Z'
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
summary: 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone is locally consistent
  with its retained full-key MIBiG identity and alkyl/prenyl aromatic-ether structure.
  One unspecified tetrahedral centre, with one specified E alkene; retained false
  flag. Producer and locus support remain source assertion and CLUSTER_UNSTATED respectively;
  model filing, direct congeners and the shared citation do not expand that support.
  Scientific completion remains partial.
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
  - path: data/natural_products/polyketides/6-anteisoheptadecyl-4-o-dihydrogeranyl-2-methoxyhydroquinone.yaml
    sha256: dcbca401b3c9f930f03adf2a7886e2e3e4ef7af5717c1611030c96745806d0a1
    role: context
  - path: data/natural_products/polyketides/6-isoheptadecyl-4-o-dihydrogeranyl-2-methoxyhydroquinone.yaml
    sha256: 44db959a58944d282a404f37106b89b9f00b4dcc8b3b960cee1d393d93154986
    role: context
  - path: data/natural_products/polyketides/6-palmityl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    sha256: f017686fda495139efc3619691fe8a4f03f84e159690c82fddb8ec66d7c9039d
    role: context
  - path: data/natural_products/polyketides/6-palmityl-4-o-geranyl-2-methoxyhydroquinone.yaml
    sha256: 6237d4d031c57950e00dd5a377922e5f62cd3b82ba614c07a641ad610ba7c307
    role: context
  - path: data/natural_products/terpenoids/6-anteisoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    sha256: f3bd1ecd23cdd69354226cb087d338951268b812d327584004571ac955d8a58a
    role: context
  - path: data/natural_products/terpenoids/6-anteisoheptadecyl-4-o-geranyl-2-methoxyhydroquinone.yaml
    sha256: 7143c780058e8d8ffd06a3b476937f37a445f34c4f25f8f2b9753071da62c350
    role: context
  - path: data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    sha256: 3616cf947864a884959adfd7b1df759cab5d0da2af59a9050cb7cd4c4b7f9a86
    role: target
  - path: data/natural_products/terpenoids/6-isoheptadecyl-4-o-geranyl-2-methoxyhydroquinone.yaml
    sha256: 5c0b9a54b761e4adeb550a6356bbd8840df563cca8d6cef0eb2f067e04119a44
    role: context
  - path: data/natural_products/terpenoids/6-isopalmityl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    sha256: 925ed5babe9861fd5935d772f3d972eacb3f1ebd78b3c8d66b9ecdab6aaab5c1
    role: context
  - path: data/natural_products/terpenoids/6-isopalmityl-4-o-geranyl-2-methoxyhydroquinone.yaml
    sha256: c8dc8e2707a89ec503e1aa8d55a313ac098e36d257f1335829143172a57b58c2
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
  selection: Campaign path order 2253; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-447235379c
targets:
- target_id: naturalproductmech:mibig-447235379c
  path: data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
  label: 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone
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
  - naturalproductmech:mibig-447235379c
  command: just validate-strict data/natural_products/terpenoids/6-anteisoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-anteisoheptadecyl-4-o-geranyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isoheptadecyl-4-o-geranyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isopalmityl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/6-isopalmityl-4-o-geranyl-2-methoxyhydroquinone.yaml
    data/natural_products/terpenoids/7-deoxypactamycin.yaml data/natural_products/terpenoids/8-9-epibotrydial.yaml
    data/natural_products/terpenoids/8-hydroxy-6-protoilludene.yaml data/natural_products/terpenoids/acorenol.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-226/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-447235379c
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-226/validate-all-001.tsv
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
  - naturalproductmech:mibig-447235379c
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
  - naturalproductmech:mibig-447235379c
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
  - naturalproductmech:mibig-447235379c
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-226/review-queue-001.tsv
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
  - naturalproductmech:mibig-447235379c
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-447235379c
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-447235379c
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2253-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/6-isoheptadecyl-4-o-dihydrofarnesyl-2-methoxyhydroquinone.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Complete 6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone owner
    with two SEEDED_FROM_SOURCES history events and native curation status SEEDED.
  snapshot_sha256: 3616cf947864a884959adfd7b1df759cab5d0da2af59a9050cb7cd4c4b7f9a86
- evidence_id: bgc-2253-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/2/owner_pin; /records/2/owner_document
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Complete saved owner and exact raw pin for order 2253.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
- evidence_id: bgc-2253-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/intakes/2253-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Actual one-record intake for naturalproductmech:mibig-447235379c; 46 source
    placements, four declared maintained ownership paths and inspection-only ownership
    note.
  snapshot_sha256: a17c69faf1c62d1147c67fe1028f0229da54dc080a96de82cf50f29ac0746739
- evidence_id: bgc-2253-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-intake-ready-001.json
  locator: /accepted
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: ROOT acceptance of the original ten actual intakes and their source-input
    joins.
  snapshot_sha256: cee04496c89499477fb14b1f5bd349baff9a19879f761f843ba1ef13423cfc52
- evidence_id: bgc-2253-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: MINTED owner naturalproductmech:mibig-447235379c, exact full key DXVIRWBLDDUQRP-DNGXXSEMSA-N,
    retained MIBiG source concept and source structure.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
- evidence_id: bgc-2253-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/bgc_class
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Written producer Actinoplanes missouriensis 431, NCBITaxon:512565, SOURCE_ASSERTION;
    BGC0001077 version 4, CLUSTER_UNSTATED, PKS and genbank:AP012319.1 coordinates
    8379670–8386219. Both written evidence lists attach DOI:10.1002/cbic.201000628
    as DATABASE_ASSERTION.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
- evidence_id: bgc-2253-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The complete captured owner writes no bioactivities, bioactivity_summary,
    molecular_targets, causal_graphs, causal_graph_refs or biosynthetic_pathway root.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
  search_scope: Complete captured owner object only; no global biological absence
    claim.
- evidence_id: bgc-2253-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The complete captured owner writes no occurrences root.
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
  search_scope: Complete captured owner object only.
- evidence_id: bgc-2253-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_pathway; /records/2/owner_document/np_classification;
    /records/2/owner_document/bgc_class; /records/2/owner_document/compound_classes
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: 'Literal written classification: {"bgc_class": ["PKS"], "compound_classes":
    ["Alkylresorcinol/phloroglucinol polyketide", "Sesquiterpenoid"], "np_classification":
    {"class_results": [], "is_glycoside": false, "pathway_results": ["Terpenoids"],
    "superclass_results": [], "tool": "NPClassifier", "tool_version": "npclassifier.gnps2.org@2026-09-07"},
    "np_pathway": "TERPENOIDS"}'
  snapshot_sha256: 39a09efef203ca9e288817223f63671042244ab58ffd48c19989979b25cdf028
- evidence_id: bgc-2253-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/smiles/status; /records/2/inchi/status;
    /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons;
    /records/2/atom_correspondence
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: 'Both stored forms parsed as neutral C38H66O3, 41 atoms and 41 bonds, one
    fragment and one ring. All ten comparison flags are true and the stored atom correspondence
    is complete; full_graph_identity_established remains false. Saved stereo_counts:
    {"inchi": {"Atom_Tetrahedral:Unspecified": 1, "Bond_Double:Specified": 1}, "smiles":
    {"Atom_Tetrahedral:Unspecified": 1, "Bond_Double:Specified": 1}}'
  snapshot_sha256: 9402e619ad45ee271669f7c409f81b7af6e2e529a58aed6239da2c56d05b22e2
- evidence_id: bgc-2253-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed; /records/2/inchi/computed; /records/2/atom_correspondence;
    /records/0/smiles/computed; /records/0/inchi/computed
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The full SMILES table contains aromatic ring atoms 1, 2, 19, 20, 37 and
    38, phenolic oxygen 0, the prenyl ether through O21 and methoxy O39. The isoalkyl
    terminus differs from the anteiso congener despite the shared molecular formula.
    Both complete tables show one six-carbon aromatic ring, one phenolic OH, two carbon–oxygen–carbon
    ethers and two acyclic double bonds, with no carbonyl, ring oxygen or sugar residue
    topology. One unspecified tetrahedral centre in the dihydrofarnesyl branch, SMILES
    atom 28 corresponding to InChI atom 32. The isoalkyl terminus has two identical
    methyl groups and is not an additional tetrahedral stereocentre. The proximal
    alkene is E in both stored bond tables; the distal alkene has two identical methyl
    substituents and is not an additional E/Z site. Local Bond_Cis/Bond_Trans potential-stereo
    descriptors use different reference atom orderings and do not indicate a conflict
    here.
  snapshot_sha256: 9402e619ad45ee271669f7c409f81b7af6e2e529a58aed6239da2c56d05b22e2
- evidence_id: bgc-2253-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /external_requests; /retries
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Original saved diagnostic execution exited 0 with retries 0 and external_requests
    false; exact stdout and stderr paths and hashes are retained.
  snapshot_sha256: 31d79354b21eee031db3ba3dcf19679c5c456728ccf47fccd7ae84163f290d61
- evidence_id: bgc-2253-diagnostic-stderr
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/chemistry-local/diagnostic-001.stderr
  locator: Whole original stderr, eight warning entries
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Eight original batch-level omitted-undefined-stereo warnings are present.
    The stream does not identify record order; none is assigned to this owner.
  snapshot_sha256: 6ead57c2a582177efef8b248140360c13abecc00d4c87cbe160b989f0e16cbb0
- evidence_id: bgc-2253-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-local-diagnostics-acceptance-001.json
  locator: /status; /DATA; /execution; /actual_intake_authority; /successful_forms;
    /comparison_flags_true; /comparison_flags_false; /scientific_reading; /limits;
    /full_QC_and_OAK
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: ROOT accepts the original twenty successful saved forms with 98 true and
    two false comparison flags, preserves their limits, and separately attributes
    whole scientific readings. Only order 2257 has false canonical-SMILES flags; this
    is mechanical acceptance, not natural identity authentication. Full QC and OAK
    remain unavailable.
  snapshot_sha256: 67c8acc7ddac7662cd7f52c95e058806b4dfc64ee849c335a75ab601fecc35cf
- evidence_id: bgc-2253-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-native-five-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /scope
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: ROOT accepts five local commands; all_native_gates_passed is false because
    full QC and ontology-consistency OAK are unavailable. Scope and original evidence
    remain explicit.
  snapshot_sha256: 66ab88f5308b0868c13d372cd15007e234fd6213978218e700b8b4998ae0ee5a
- evidence_id: bgc-2253-inventory-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-source-inventory-acceptance-001.json
  locator: /accepted; /inventory; /source_placements; /source_paths; /technical_scope
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: ROOT mechanically accepts the saved inventory, its 448 source placements
    and 72 paths, retaining scientific interpretation as a separate task.
  snapshot_sha256: 729e10fc39b2b62c5fa4fd8a7d5b91e1ebeb291d625c55d9cfa5b6343a37ca1d
- evidence_id: bgc-2253-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-target-input-plan-001.json
  locator: /records/2; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Accepted saved plan retains this complete owner and source context with
    46 proposed input paths and no selected-reader requirement for this owner; batch
    source map totals 448 placements and 72 paths.
  snapshot_sha256: 5d36a99b7ee05f0c9ceb3903fe8e49600ac44f6442f21e499ef04d738a8870eb
- evidence_id: bgc-2253-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226/root-input-plan-acceptance-001.json
  locator: /accepted; /plan; /source_notes; /source_placements; /unique_source_paths
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: ROOT accepts the exact plan and source notes with 448 placements and 72
    source paths; this is source planning rather than a scientific verdict.
  snapshot_sha256: c4eb227ed6d0e6bf96877c3b5f15e9275f07ebb86aff2d4edf7d9749a8871251
- evidence_id: bgc-2253-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-scope-notes-001.json
  locator: /reading; /curation; /cautions; /inventory_ROOT_acceptance
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Pinned personal/delegated reading covers all 34 complete owner/history
    bodies, 306 query frames, 117 full positive payloads, 1387 CSV fields and 11 cached
    stanzas. The case-sensitive 84-literal direct-file scan of eight named curation
    tables has zero hits only in its declared scope; the PubChem exclusion scan is
    supplemental, and reserved decisions.tsv was not consumed.
  snapshot_sha256: 1597c81b8311af685af0357a207d5e49353a00216d5c48d722f31a05f06be0b4
- evidence_id: bgc-2253-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /records/2/direct_companion_predicates; /contexts/0/identifier; /contexts/0/standard_inchi_key;
    /contexts/0/owned_bgc_ids; /contexts/0/declared_mechanism_roots_literal; /contexts/1/identifier;
    /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/1/declared_mechanism_roots_literal;
    /contexts/2/identifier; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids;
    /contexts/2/declared_mechanism_roots_literal; /contexts/3/identifier; /contexts/3/standard_inchi_key;
    /contexts/3/owned_bgc_ids; /contexts/3/declared_mechanism_roots_literal; /contexts/13/identifier;
    /contexts/13/standard_inchi_key; /contexts/13/owned_bgc_ids; /contexts/13/declared_mechanism_roots_literal;
    /contexts/14/identifier; /contexts/14/standard_inchi_key; /contexts/14/owned_bgc_ids;
    /contexts/14/declared_mechanism_roots_literal; /contexts/16/identifier; /contexts/16/standard_inchi_key;
    /contexts/16/owned_bgc_ids; /contexts/16/declared_mechanism_roots_literal; /contexts/17/identifier;
    /contexts/17/standard_inchi_key; /contexts/17/owned_bgc_ids; /contexts/17/declared_mechanism_roots_literal;
    /contexts/18/identifier; /contexts/18/standard_inchi_key; /contexts/18/owned_bgc_ids;
    /contexts/18/declared_mechanism_roots_literal
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: 'Nine direct companions share owned BGC0001077 but have distinct root identifiers
    and complete keys. The 6-isopalmityl-4-O-geranyl congener has retained causal_graphs;
    these are context for that separate owner and do not supply this owner with an
    enzyme, pathway or activity assertion. Exact companion profiles: [{"identifier":
    "naturalproductmech:mibig-3b73f6a516", "standard_inchi_key": "NOPAZUFYUXZIPZ-UHFFFAOYSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-1253be8cf8", "standard_inchi_key": "HPAIKUJKASWMKP-UHFFFAOYSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-9c1beabea6", "standard_inchi_key": "CEACUCBTLUKKIY-MUGXBBEHSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-cd91f14897", "standard_inchi_key": "RHKVCMWMMGYUTG-WEMUOSSPSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-8a8aaf4fce", "standard_inchi_key": "CVTKJHUYRMFMCV-DNGXXSEMSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-36f47126b7", "standard_inchi_key": "WOCMOPRAFKEPAY-BYNJWEBRSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-0d66b83278", "standard_inchi_key": "RRVPCBLEVREXDD-BYNJWEBRSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-6f48d22ee3", "standard_inchi_key": "XZJZCONDRDOIHG-MHTZHOPKSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": []}, {"identifier":
    "naturalproductmech:mibig-b6f11fae29", "standard_inchi_key": "PBBKVCVGOJSEOQ-XAYXJRQQSA-N",
    "owned_bgc_ids": ["BGC0001077"], "declared_mechanism_roots_literal": ["causal_graphs"]}]'
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
- evidence_id: bgc-2253-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /cached_taxonomy/input; /cached_taxonomy/whole_stanzas/8
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: 'Complete cached stanza: [Term]

    id: NCBITaxon:512565

    name: Actinoplanes missouriensis 431

    synonym: "Actinoplanes missouriensis str. 431" EXACT []

    synonym: "Actinoplanes missouriensis strain 431" EXACT []


    This name/synonym stanza is not an ancestry or experimental production proof.'
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
- evidence_id: bgc-2253-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/source_taxa; /contexts/15/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/15/source_scope_inventory/nonorganism_matches; /contexts/15/source_scope_inventory/actual_assay_rows;
    /contexts/15/source_scope_inventory/blank_AID_sentinels; /contexts/15/source_scope_inventory/related_corpus_rows
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Retained taxon scope is NCBITaxon:512565; no matching forward-merge/nonorganism
    rows, actual assays, blank-AID sentinels or related-corpus rows in these exact
    saved routes.
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact current owner routes retained in the named inventory context.
- evidence_id: bgc-2253-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 368–430
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: ChemicalStructure documents full-key limitations and undefined stereocentres.
    ComputedClassification is a named, versioned prediction, never a source assertion
    or reason for admission.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2253-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 142–173
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The maintained structure_fields function derives standardized InChI/key
    from SMILES and sets stereo_complete from unassigned tetrahedral chiral-centre
    results. This source reading invokes no parser and does not broaden that flag
    into proof of natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2253-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 971–1037
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The seeder retains minted grounding where no single ChEBI match is adopted,
    copies source structure fields, and copies versioned NPClassifier lists and its
    is_glycoside boolean.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2253-origin-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 1093–1151
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The seeder separately emits the producer evidence basis and locus linkage
    basis, preserves claim citations, and writes source genome coordinates and applicable
    methods.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2253-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole profile; identity, source evidence, scientific dimensions and partial-review
    requirements
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The maintained review profile requires claim-level scientific interpretation,
    explicit source limits and independent evidence for producer, occurrence, locus
    and mechanism claims.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2253-review-skill
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Whole review skill; evidence access and structured-review scope
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: The one-record review procedure separates scientific review from curation
    edits and mechanical validation; unavailable verification remains explicit. The
    absolute no-request instruction controls external access.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2253-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved mibig_compounds predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 1 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved mibig_compounds predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV line 1251; header line 1; row SHA256 96b46cceb8053cb9d07e026d4c6c78b3cce4da3dccb11bb2edcb0a7fed1fde4e
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: 'Complete retained row fields: {"bgc_classes": "PKS", "bgc_subclasses":
    "Type III", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes":
    "Alkylresorcinol/phloroglucinol polyketide|Sesquiterpenoid", "compound_index":
    "10", "compound_name": "6-isoheptadecyl-4-O-dihydrofarnesyl-2-methoxyhydroquinone",
    "database_ids": "", "entry_completeness": "unknown", "entry_quality": "questionable",
    "entry_status": "active", "entry_version": "4", "genome_accession": "AP012319.1",
    "locus_evidence_methods": "", "locus_from": "8379670", "locus_to": "8386219",
    "mibig_accession": "BGC0001077", "primary_reference": "DOI:10.1002/cbic.201000628",
    "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_EVIDENCE",
    "smiles": "OC1=C(CCCCCCCCCCCCCC(C)C)C=C(OC/C=C(CCCC(CC/C=C(C)/C)C)\\C)C=C1OC",
    "standard_inchi": "InChI=1S/C38H66O3/c1-31(2)21-17-15-13-11-9-8-10-12-14-16-18-26-35-29-36(30-37(40-7)38(35)39)41-28-27-34(6)25-20-24-33(5)23-19-22-32(3)4/h22,27,29-31,33,39H,8-21,23-26,28H2,1-7H3/b34-27+",
    "standard_inchi_key": "DXVIRWBLDDUQRP-DNGXXSEMSA-N", "stereo_complete": "false",
    "taxon_id": "NCBITaxon:512565", "taxon_label": "Actinoplanes missouriensis 431"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2253-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved chebi_structures predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved chebi_structures predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved lotus_occurrences predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved lotus_occurrences predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved cyanometdb_occurrences predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved cyanometdb_occurrences predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved npclassifier predicate exact complete standard_inchi_key equality;
    query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot is covered.
    The complete frame contains 1 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved npclassifier predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV line 495; header line 1; row SHA256 8595522f3e85b9d0cd799e00d3ab30558a8946406de552beee9a89aff575823f
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: 'Complete retained row fields: {"class_results": "", "is_glycoside": "false",
    "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Terpenoids",
    "smiles": "OC1=C(CCCCCCCCCCCCCC(C)C)C=C(OC/C=C(CCCC(CC/C=C(C)/C)C)\\C)C=C1OC",
    "standard_inchi_key": "DXVIRWBLDDUQRP-DNGXXSEMSA-N", "superclass_results": ""}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2253-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved pubchem_bioassay predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved pubchem_bioassay predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved bindingdb_targets predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved bindingdb_targets predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved antibioticmech_inchikeys predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered. The complete frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved antibioticmech_inchikeys predicate exact complete standard_inchi_key
    equality; query "DXVIRWBLDDUQRP-DNGXXSEMSA-N". Only this retained table snapshot
    is covered.
- evidence_id: bgc-2253-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch226-tentative/bgc-prep/bgc-conditional226-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T16:26:49.319083Z'
  support: supports
  summary: Exact saved chebi_origins predicate exact chebi_id from exact full-key
    structure rows; query []. Only this retained table snapshot is covered. The complete
    frame contains 0 matched physical row(s).
  snapshot_sha256: 59a47a79b18ff7d21c3dcb5fe8902955275f4952069cc7e6e6bb722c3994389f
  search_scope: Exact saved chebi_origins predicate exact chebi_id from exact full-key
    structure rows; query []. Only this retained table snapshot is covered.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:11:35.707228Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 3fa23498b91d1b30f655811c3728349e2862f93bc03bc07753c393f7ca5481c4
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:12:01.451422Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 48c2f4b016834c4f1144f8443efbd602f5e144b6e9f62e4980e5d8de20ea3584
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:12:21.633510Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:12:56.658279Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-226/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-226/native-current226-five-gates-execution-001.json
  accessed_at: '2026-11-03T16:13:08.681619Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 471651bc2d9c52a88f0d76e62dd1d43baf68fe35de766f6346cf3befbab82970
assessments:
- assessment_id: bgc-2253-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted identity naturalproductmech:mibig-447235379c follows exact MIBiG
    BGC0001077 version 4 compound index 10 and full key DXVIRWBLDDUQRP-DNGXXSEMSA-N.
    The saved exact ChEBI query is empty. The isoheptadecyl branch is not interchangeable
    with the same-formula anteisoheptadecyl branch. All nine direct companions remain
    separate owners; shared BGC membership does not permit a grounding or identity
    substitution.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-grounding-owner
  - bgc-2253-source-mibig_compounds
  - bgc-2253-query-chebi_structures
  - bgc-2253-chemistry
  - bgc-2253-topology
  - bgc-2253-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: DXVIRWBLDDUQRP-DNGXXSEMSA-N; exact full-key source owner.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2253-grounding-owner
    - bgc-2253-source-mibig_compounds
    - bgc-2253-query-chebi_structures
    - bgc-2253-chemistry
    - bgc-2253-topology
    - bgc-2253-direct-contexts
  - name: grounding_scope
    value: MINTED BGC0001077 compound index 10; bounded empty exact ChEBI join, no
      congener substitution.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2253-grounding-owner
    - bgc-2253-source-mibig_compounds
    - bgc-2253-query-chebi_structures
    - bgc-2253-chemistry
    - bgc-2253-topology
    - bgc-2253-direct-contexts
- assessment_id: bgc-2253-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both stored forms give neutral C38H66O3, 41 atoms and 41 bonds, with one
    connected fragment, all ten comparison flags true and a complete stored chirality-aware
    correspondence. One unspecified tetrahedral centre in the dihydrofarnesyl branch,
    SMILES atom 28 corresponding to InChI atom 32. The isoalkyl terminus has two identical
    methyl groups and is not an additional tetrahedral stereocentre. Each form has
    the proximal alkene specified E; the distal alkene has two identical methyl substituents,
    so it does not create an additional E/Z site. Local Cis/Trans potential-stereo
    descriptors differ with reference ordering while the mapped bond stereochemistry
    agrees. The retained false flag is consistent with the extractor’s tetrahedral-centre
    scope. The diagnostic leaves full_graph_identity_established false; none of this
    authenticates the natural isolated stereoisomer.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-grounding-owner
  - bgc-2253-chemistry
  - bgc-2253-topology
  - bgc-2253-diagnostic-acceptance
  - bgc-2253-structure-schema
  - bgc-2253-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: One unspecified tetrahedral centre, with one specified E alkene; retained
      false flag.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2253-grounding-owner
    - bgc-2253-chemistry
    - bgc-2253-topology
    - bgc-2253-diagnostic-acceptance
    - bgc-2253-structure-schema
    - bgc-2253-stereo-method
  - name: representation_correspondence
    value: Ten true comparison flags and complete stored correspondence; independent
      full-graph and natural identity remain unestablished.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2253-grounding-owner
    - bgc-2253-chemistry
    - bgc-2253-topology
    - bgc-2253-diagnostic-acceptance
    - bgc-2253-structure-schema
    - bgc-2253-stereo-method
- assessment_id: bgc-2253-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: MIBiG BGC0001077 version 4 is active, of questionable quality and unknown
    completeness. The retained strain Actinoplanes missouriensis 431, NCBITaxon:512565,
    has SOURCE_ASSERTION producer evidence. The locus remains CLUSTER_UNSTATED with
    no stated method. Its source PKS/Type III label and genbank:AP012319.1 interval
    8379670–8386219 do not constitute a demonstrated complete pathway. The complete
    cached stanza names the same strain and records str. 431/strain 431 synonyms;
    no ancestry or fresh accession verification is inferred.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-origin-owner
  - bgc-2253-source-mibig_compounds
  - bgc-2253-cached-taxonomy
  - bgc-2253-source-routes
  - bgc-2253-origin-seeder
  - bgc-2253-direct-contexts
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:512565 is the retained Actinoplanes missouriensis 431 strain,
      with cached strain-name variants.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2253-origin-owner
    - bgc-2253-source-mibig_compounds
    - bgc-2253-cached-taxonomy
    - bgc-2253-source-routes
    - bgc-2253-origin-seeder
    - bgc-2253-direct-contexts
  - name: producer_evidence
    value: SOURCE_ASSERTION; no promotion from the shared locus or another congener’s
      graph.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2253-origin-owner
    - bgc-2253-source-mibig_compounds
    - bgc-2253-cached-taxonomy
    - bgc-2253-source-routes
    - bgc-2253-origin-seeder
    - bgc-2253-direct-contexts
  - name: locus_evidence
    value: BGC0001077 version 4, active/questionable/unknown; PKS Type III source
      label, CLUSTER_UNSTATED and no stated experimental method.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2253-origin-owner
    - bgc-2253-source-mibig_compounds
    - bgc-2253-cached-taxonomy
    - bgc-2253-source-routes
    - bgc-2253-origin-seeder
    - bgc-2253-direct-contexts
- assessment_id: bgc-2253-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: DOI:10.1002/cbic.201000628 is retained at COMPOUND_EVIDENCE level and appears
    as DATABASE_ASSERTION on both the written producer and locus. Those placements
    do not constitute two independent experiments or fresh primary verification. The
    local source row does not supply an experimental locus method. Other BGC0001077
    congeners and the separately curated 6-isopalmityl-4-O-geranyl graphs do not upgrade
    this owner’s claims.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-origin-owner
  - bgc-2253-source-mibig_compounds
  - bgc-2253-source-notes
  - bgc-2253-direct-contexts
  - bgc-2253-origin-seeder
  dimensions:
  - name: citation_scope
    value: Compound-evidence DOI:10.1002/cbic.201000628, retained database assertion;
      primary text and compound-specific methods were not refreshed.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2253-origin-owner
    - bgc-2253-source-mibig_compounds
    - bgc-2253-source-notes
    - bgc-2253-direct-contexts
    - bgc-2253-origin-seeder
- assessment_id: bgc-2253-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The complete owner writes no occurrences, assay observations, activity
    summary, molecular targets or mechanism roots. Exact saved LOTUS, ChEBI-origin,
    CyanometDB, PubChem, BindingDB and AntibioticMech routes are empty; no blank-AID
    sentinel is present for this owner. This is a bounded absence of retained assertions,
    not evidence of biological inactivity. The shared-locus congener with causal graphs
    remains a separate owner.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-assay-owner
  - bgc-2253-occurrence-owner
  - bgc-2253-query-lotus_occurrences
  - bgc-2253-query-chebi_origins
  - bgc-2253-query-cyanometdb_occurrences
  - bgc-2253-query-pubchem_bioassay
  - bgc-2253-query-bindingdb_targets
  - bgc-2253-query-antibioticmech_inchikeys
  - bgc-2253-source-routes
  - bgc-2253-direct-contexts
  - bgc-2253-source-plan
  dimensions:
  - name: occurrence_scope
    value: No written occurrence; exact retained occurrence joins empty.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2253-assay-owner
    - bgc-2253-occurrence-owner
    - bgc-2253-query-lotus_occurrences
    - bgc-2253-query-chebi_origins
    - bgc-2253-query-cyanometdb_occurrences
    - bgc-2253-query-pubchem_bioassay
    - bgc-2253-query-bindingdb_targets
    - bgc-2253-query-antibioticmech_inchikeys
    - bgc-2253-source-routes
    - bgc-2253-direct-contexts
    - bgc-2253-source-plan
  - name: assay_target_scope
    value: No written assays, targets or mechanisms; exact activity routes empty,
      with no sentinel or congener transfer.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2253-assay-owner
    - bgc-2253-occurrence-owner
    - bgc-2253-query-lotus_occurrences
    - bgc-2253-query-chebi_origins
    - bgc-2253-query-cyanometdb_occurrences
    - bgc-2253-query-pubchem_bioassay
    - bgc-2253-query-bindingdb_targets
    - bgc-2253-query-antibioticmech_inchikeys
    - bgc-2253-source-routes
    - bgc-2253-direct-contexts
    - bgc-2253-source-plan
- assessment_id: bgc-2253-classification
  area: consistency
  topic: Classification
  outcome: unknown
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 supplies Terpenoids
    and is_glycoside:false, with filing value TERPENOIDS. Empty superclass and class
    lists are retained. Separately, the source records PKS/Type III at the locus and
    Alkylresorcinol/phloroglucinol polyketide plus Sesquiterpenoid at compound level.
    The complete paired topology contains a substituted aromatic carbon ring, one
    phenolic OH and two ethers, with no sugar residue or sugar–aglycone linkage. That
    is compatible with the false glycoside prediction without turning a model output
    into independent biosynthetic or identity evidence. These distinct classification
    axes do not establish a local curation defect.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-classification-owner
  - bgc-2253-source-npclassifier
  - bgc-2253-source-mibig_compounds
  - bgc-2253-chemistry
  - bgc-2253-topology
  - bgc-2253-structure-schema
  - bgc-2253-classification-seeder
  - bgc-2253-review-profile
  dimensions:
  - name: classification_applicability
    value: Versioned Terpenoids and false glycoside prediction; observed alkyl/prenyl
      aromatic ether topology and source polyketide/terpenoid labels kept distinct.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2253-classification-owner
    - bgc-2253-source-npclassifier
    - bgc-2253-source-mibig_compounds
    - bgc-2253-chemistry
    - bgc-2253-topology
    - bgc-2253-structure-schema
    - bgc-2253-classification-seeder
    - bgc-2253-review-profile
- assessment_id: bgc-2253-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: The complete owner/history, exact retained source payloads, actual 46-input
    intake and both full saved molecular tables were reviewed. No supported local
    curation defect is established in this bounded scope. Five local gates passed;
    full QC, complete OAK and fresh external primary-source/taxonomy/accession verification
    were unavailable. No maintained reader is required for this owner’s absent mechanism
    roots. Scientific completion remains partial, with native curation status and
    history unchanged.
  target_ids:
  - naturalproductmech:mibig-447235379c
  evidence_ids:
  - bgc-2253-owner
  - bgc-2253-capture
  - bgc-2253-intake
  - bgc-2253-intake-acceptance
  - bgc-2253-source-notes
  - bgc-2253-inventory-acceptance
  - bgc-2253-native-acceptance
  - bgc-2253-diagnostic-execution
  - bgc-2253-diagnostic-stderr
  - bgc-2253-diagnostic-acceptance
  - bgc-2253-source-plan
  - bgc-2253-plan-acceptance
  - bgc-2253-review-skill
  - bgc-2253-review-profile
  dimensions:
  - name: review_completion
    value: Partial qualified local review; full QC, complete OAK and fresh external
      authorities unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2253-owner
    - bgc-2253-capture
    - bgc-2253-intake
    - bgc-2253-intake-acceptance
    - bgc-2253-source-notes
    - bgc-2253-inventory-acceptance
    - bgc-2253-native-acceptance
    - bgc-2253-diagnostic-execution
    - bgc-2253-diagnostic-stderr
    - bgc-2253-diagnostic-acceptance
    - bgc-2253-source-plan
    - bgc-2253-plan-acceptance
    - bgc-2253-review-skill
    - bgc-2253-review-profile
findings: []
actions: []
limitations:
- External identifiers, taxonomy, genome accessions and primary publications were
  not refreshed under the absolute no-request instruction. Historical and database
  assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and stored-form
  parsing establish only their declared mechanical scope.
- Empty joins refer only to the retained exact predicates and snapshots; they do not
  establish biological absence. Shared loci, citations and congeners do not transfer
  compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete retained source payloads and direct-context whole-reading attributions
  are in the pinned source notes. This owner/history, its actual intake and both full
  saved molecular tables were personally read.
- Eight original batch-level undefined-stereo warnings remain globally unassigned.
  True comparison flags and a complete stored atom correspondence do not override
  full_graph_identity_established:false.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-226
```
