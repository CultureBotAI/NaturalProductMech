# Local evidence review: N-tetradecanoyl tyrosine

- Review: 20261107T021905Z-n-tetradecanoyl-tyrosine
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T01:29:28.080242Z
- Finished UTC: 2026-11-07T02:19:05.268181Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The retained source label and stored graph disagree materially: the acyl fragment has 12 carbons including its carbonyl, and the terminal group is CH(OH)2 rather than a tyrosine carboxyl group. Both MIBiG rows carry the same mismatch. This confirmed local inconsistency requires curation; the correct upstream name or structure and the existing shared-structure question remain unresolved.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2810; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5f6e775235 | data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml | generated | N-tetradecanoyl tyrosine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-5f6e775235 | Both stored forms parsed and retain declared normalized keys; Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| strict_ten | passed | True | naturalproductmech:mibig-5f6e775235 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5f6e775235 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5f6e775235 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5f6e775235 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5f6e775235 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5f6e775235 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5f6e775235 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5f6e775235 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: concern. Targets: naturalproductmech:mibig-5f6e775235.

BGC0001591 version 4, index 2 and BGC0001687 version 3, index 1 both label the full key JJNOOOPGJKEVQC-IBGZPJMESA-N 'N-tetradecanoyl tyrosine'. Both rows are active with questionable quality and unknown completeness. Exact-key grouping preserves their separate source concepts but does not close the OPEN shared-structure discussion or establish natural identity. The retained label 'N-tetradecanoyl tyrosine' conflicts with the same structure in both MIBiG rows and the generated owner. The saved graph has 12 acyl carbons including its carbonyl, not 14, and an alpha-linked terminal CH(OH)2 instead of the tyrosine carboxyl group. Both properties persist in the InChI-derived saved form despite amide/imidic normalization. The mismatch is confirmed locally; which upstream name or structure is correct is not established, and no replacement molecule or identity merger is proposed. Severity is major because a material source name/structure correspondence is unsupported, rather than a claimed invalid valence or independently proven wrong natural-product identity.

### Saved molecular forms and stereochemical scope

representation: concern. Targets: naturalproductmech:mibig-5f6e775235.

Both saved forms have C21H35NO4, 26 atoms, 26 bonds and zero net formal charge. Normalized InChI, full key and formula agree, but canonical SMILES comparisons are false: the SMILES amide becomes an imidic C(OH)=N representation. The map is empty and full graph identity remains false. Internal normalized agreement does not resolve the label–graph disagreement. SMILES carbon atoms C0–C11 form the uninterrupted acyl path, including carbonyl C11: terminal C0 is CH3 and C1–C10 are ten CH2 groups, giving 12 acyl carbons rather than the 14 named by tetradecanoyl. C11(=O12)-N13 links alpha C14(S), benzyl C15 and a para-hydroxylated aromatic six-ring. Terminal C23 has one hydrogen and single bonds to alpha C14, O24H and O25H: it is CH(OH)2, not C(=O)OH. In the InChI form, C0–C10 plus C19 retain the 12-carbon chain, C19(OH23)=N21 is imidic, and C20H(OH24)(OH25) retains the geminal diol. Both forms have one aromatic ring/cycle rank 1; the stored strict terminal-carbonyl predicate is empty. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.

### Compound-specific producer, locus and taxon

provenance: supported. Targets: naturalproductmech:mibig-5f6e775235.

Uncultured bacterium CSLC2 (1091571) belongs to BGC0001591 and uncultured bacterium CSL12 (1091567) to BGC0001687. Both remain SOURCE_ASSERTION, not demonstrated production. Their cached named nodes do not establish cultured strains, species identity or equivalence. BGC0001591 version 4/JF429413.1 and BGC0001687 version 3/JF429409.1 retain OTHER classes, CLUSTER_UNSTATED grades and blank methods/coordinates. Unknown completeness stays unknown; no incomplete-entry or causal-locus claim is inferred.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-5f6e775235.

PMID:12188643 and PMID:15528554 are distinct ENTRY-level MIBiG database assertions for their respective source rows. They have not been freshly read as primary proof of the name or structure. The two seed histories and OPEN shared-structure discussion remain intact.

### Occurrence and assay limits

evidence: supported. Targets: naturalproductmech:mibig-5f6e775235.

No exact-key LOTUS or CyanoMetDB occurrence row is retained. The two producer assertions are not converted into occurrence evidence or broadened to other taxa. No actual assay, target, ChEBI or AntibioticMech payload is retained under the owner's saved predicates. This neither supplies a replacement structure nor establishes biological inactivity.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-5f6e775235.

NPClassifier version npclassifier.gnps2.org@2026-09-07 repeats the stored SMILES and has empty categories with false glycoside. This model row is not independent confirmation of the label. UNCLASSIFIED filing correctly follows empty predictions; the material issue lies in name/structure correspondence, not filing.

### Earned work and unavailable authority

completeness: concern. Targets: naturalproductmech:mibig-5f6e775235.

Complete assigned raw/source/intake and both saved molecular forms were read. No graph, graph reference, component, pathway, target or activity root is present and no maintained reader is assigned. The curation concern is a source-derived chemical identity annotation, not a missing curated mechanism. The major local label–graph finding remains open. Five local native commands pass; full QC, complete OAK and fresh primary verification remain unavailable. Completion is partial, native SEEDED status unchanged.

## Findings

### support-2810-label-structure-acyl-terminal-mismatch: Source label disagrees with acyl length and terminal group in the stored graph

major / open / confirmed; issue key: n-tetradecanoyl-tyrosine-source-label-structure-mismatch.

The retained label 'N-tetradecanoyl tyrosine' conflicts with the same structure in both MIBiG rows and the generated owner. The saved graph has 12 acyl carbons including its carbonyl, not 14, and an alpha-linked terminal CH(OH)2 instead of the tyrosine carboxyl group. Both properties persist in the InChI-derived saved form despite amide/imidic normalization. The mismatch is confirmed locally; which upstream name or structure is correct is not established, and no replacement molecule or identity merger is proposed. Severity is major because a material source name/structure correspondence is unsupported, rather than a claimed invalid valence or independently proven wrong natural-product identity.

## Recommended Actions And Acceptance Checks

### support-2810-reconcile-source-name-and-structure

Adjudicate both BGC0001591:2 and BGC0001687:1 source name/structure pairs through a separately authorized maintained source-correction workflow. Determine whether the name, acyl chain, terminal group or upstream source mapping requires correction using appropriate primary evidence; do not choose a replacement from the label alone. Preserve both source concepts and the OPEN shared-structure discussion until that separate question is resolved. The existing ChEBI correction actions require an actual supported target and are not a generic freeform SMILES patch.

- Document exact source-row versions, parsed-row digest pins and evidence for each affected source compound, keeping source and natural identity claims separate.
- Show that the adopted label and structure agree on acyl-carbon count, terminal functional group, formula, charge and supported stereochemistry; retain disagreements explicitly rather than inventing a structure.
- Use an implemented, tested correction path only when its prerequisites are met; otherwise implement the necessary maintained consumer with focused name/structure regression coverage. Do not use reserved decisions.tsv or hand-edit the generated record.
- In a separately authorized correction workflow, regenerate through the validated writer and verify source ownership, identifier/path migration if needed, append-only history, corpus integrity and reproduction without silently closing the shared-structure discussion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2810-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml; complete file: identifier, label, chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification, discussions and curation_history | supports | Complete current owner retained; generated facts and curator-owned annotations remain distinct. |
| support-2810-capture | /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json; /records/9/owner_document; /records/9/component_captures | supports | Whole accepted owner capture; no component or target transfer. |
| support-2810-source | /private/tmp/npm-review-work/shared-next-batch281-tentative/support-prep/support-current281-assigned-source-reading-001.json; /contexts/14; /selected_counts; /counts; /global_cautions | supports | Complete assigned saved source context. Own selected credit totals 20 rows/248 fields/45 frames/29 negatives; ten companions have separate context-only credit. |
| support-2810-plan | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-target-input-plan-001.json; /records/9; /source_placement_count; /unique_source_path_count | supports | Actual 470-placement/71-path plan; this owner has 44 captured inputs. |
| support-2810-planaccept | /private/tmp/npm-review-work/shared-next-batch281/root-current281-input-plan-acceptance-001.json; /status; /accepted; /input_plan | supports | ROOT accepted this original current source plan. |
| support-2810-notes | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current notes retain disjoint source and Native taxonomy/curation interpretations; no added primary credit. |
| support-2810-intake | /private/tmp/npm-review-work/shared-next-batch281/intakes-001/2810-inspect-001.json; /status; /source; /targets | supports | Actual intake fixes generated target, maintained owners and current relative input hashes. |
| support-2810-intakeaccept | /private/tmp/npm-review-work/shared-next-batch281/root-current281-intake-acceptance-001.json; /status; /accepted; /intake_summary | supports | ROOT accepted all ten original intakes, all exit zero with empty stderr. |
| support-2810-data | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope | supports | Both saved forms have C21H35NO4, 26 atoms, 26 bonds and zero net formal charge. Normalized InChI, full key and formula agree, but canonical SMILES comparisons are false: the SMILES amide becomes an imidic C(OH)=N representation. The map is empty and full graph identity remains false. Internal normalized agreement does not resolve the label–graph disagreement. Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. |
| support-2810-stereo | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/atoms; /records/9/smiles/computed/potential_stereo; /records/9/smiles/computed/bonds; /records/9/inchi/computed/atoms; /records/9/inchi/computed/potential_stereo; /records/9/inchi/computed/bonds | supports | The alpha centre is specified S (SMILES C14/InChI C18) in both forms; no unknown tetrahedron is listed. The true source atom-centre flag is compatible with that limited count and does not repair the connectivity/name issue. The InChI form adds a potential unspecified imidic C=N, a representation-dependent geometry candidate rather than new experimental evidence. |
| support-2810-motifs | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/motifs; /records/9/smiles/computed/rings; /records/9/smiles/computed/bonds; /records/9/smiles/computed/atoms; /records/9/inchi/computed/motifs; /records/9/inchi/computed/rings; /records/9/inchi/computed/bonds; /records/9/inchi/computed/atoms | supports | SMILES carbon atoms C0–C11 form the uninterrupted acyl path, including carbonyl C11: terminal C0 is CH3 and C1–C10 are ten CH2 groups, giving 12 acyl carbons rather than the 14 named by tetradecanoyl. C11(=O12)-N13 links alpha C14(S), benzyl C15 and a para-hydroxylated aromatic six-ring. Terminal C23 has one hydrogen and single bonds to alpha C14, O24H and O25H: it is CH(OH)2, not C(=O)OH. In the InChI form, C0–C10 plus C19 retain the 12-carbon chain, C19(OH23)=N21 is imidic, and C20H(OH24)(OH25) retains the geminal diol. Both forms have one aromatic ring/cycle rank 1; the stored strict terminal-carbonyl predicate is empty. |
| support-2810-molecularreading | /private/tmp/npm-review-work/shared-next-batch281-tentative/support-prep/support-current281-last-five-molecular-intake-reading-001.json; /records/4; /counts; /warnings | supports | Complete ten saved forms personally read; no molecular replay. Four original undefined-stereo warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2810-execution | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | Single original diagnostic command and retained streams; no replay. |
| support-2810-diagaccept | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/root-current281-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /execution | supports | ROOT accepted the original stored-form diagnostic. |
| support-2810-stderr | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-original-001.stderr; complete four original warning lines | supports | Four original undefined-stereo warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2810-taxonomy | /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-cached-taxonomy-reading-001.json; /context_interpretations/25; /physical_negative_query_scopes/25; /whole_stanzas | supports | Keep uncultured bacterium CSLC2 (1091571), BGC0001591/JF429413.1, separate from uncultured bacterium CSL12 (1091567), BGC0001687/JF429409.1. These specifically named cached nodes have no retained nonorganism exclusion; that does not establish cultured strains, species identity or demonstrated production. All saved source taxon IDs have complete cache stanzas; no forward merge or nonorganism match is retained for this context. Cached labels/synonyms do not establish current remote taxonomy, lineage, production or strain identity. |
| support-2810-curation | /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | No current exact applicable maintained correction; lexical names and unrelated BGC rows do not transfer decisions. |
| support-2810-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete method grading table | supports | Producer evidence and locus methods answer different questions; unstated methods retain their grade. |
| support-2810-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172, atom-centre completeness predicate | supports | Retained stereo_complete checks unassigned atom centres, not all geometry or natural identity. |
| support-2810-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306, choose_pathway | supports | One supported normalized pathway selects filing; multiple, none or unsupported values retain UNCLASSIFIED. |
| support-2810-gates | /private/tmp/npm-review-work/shared-next-batch281/root-current281-five-gates-acceptance-001.json; /records; /all_native_gates_passed; /selected_queue_rows; /unavailable_required_gates | supports | Five local gates pass, with required QC/OAK unavailable. Actual queue entries are diagnostic leads, not automatic scientific findings. |
| support-2810-history | /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json; /records/9/owner_document/curation_history; /records/9/owner_document/source_concepts | supports | PMID:12188643 and PMID:15528554 are distinct ENTRY-level MIBiG database assertions for their respective source rows. They have not been freshly read as primary proof of the name or structure. The two seed histories and OPEN shared-structure discussion remain intact. |
| support-2810-scope | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-target-input-plan-001.json; /records/9/complete_root_keys; /records/9/declared_mechanism_roots_literal; /records/9/component_paths; /records/9/complete_raw_mechanism_sections | supports | No graph, graph reference, component, pathway, target or activity root is present and no maintained reader is assigned. The curation concern is a source-derived chemical identity annotation, not a missing curated mechanism. |
| support-2810-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 2 positive placements read. |
| support-2810-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 1908, raw UTF-8 row SHA-256 403fffc28f7f734a7c3eb020ba5915c0ea59e4424b7c18daf57baad1da9b59b6; physical line 2010, raw UTF-8 row SHA-256 a607e578133f1b536d13e5fa1434a4b0b6243f707ee1aefe1d9694e6cd12fa90 | supports | BGC0001591 version 4, index 2 and BGC0001687 version 3, index 1 both label the full key JJNOOOPGJKEVQC-IBGZPJMESA-N 'N-tetradecanoyl tyrosine'. Both rows are active with questionable quality and unknown completeness. Exact-key grouping preserves their separate source concepts but does not close the OPEN shared-structure discussion or establish natural identity. Uncultured bacterium CSLC2 (1091571) belongs to BGC0001591 and uncultured bacterium CSL12 (1091567) to BGC0001687. Both remain SOURCE_ASSERTION, not demonstrated production. Their cached named nodes do not establish cultured strains, species identity or equivalence. BGC0001591 version 4/JF429413.1 and BGC0001687 version 3/JF429409.1 retain OTHER classes, CLUSTER_UNSTATED grades and blank methods/coordinates. Unknown completeness stays unknown; no incomplete-entry or causal-locus claim is inferred. |
| support-2810-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame with 0 positive placements read. |
| support-2810-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 0 positive placements read. |
| support-2810-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame with 0 positive placements read. |
| support-2810-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 positive placements read. |
| support-2810-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 1121, raw UTF-8 row SHA-256 23adbe4aa848e42803ccca41e39118e0d9aa3ff17f2ad619ed75a1a62f8e2a92 | supports | NPClassifier version npclassifier.gnps2.org@2026-09-07 repeats the stored SMILES and has empty categories with false glycoside. This model row is not independent confirmation of the label. UNCLASSIFIED filing correctly follows empty predictions; the material issue lies in name/structure correspondence, not filing. |
| support-2810-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame with 0 positive placements read. |
| support-2810-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame with 0 positive placements read. |
| support-2810-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame with 0 positive placements read. |
| support-2810-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json; /contexts/25/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame with 0 positive placements read. |
| support-2810-finding-topology | /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds; /records/9/comparisons | supports | The retained label 'N-tetradecanoyl tyrosine' conflicts with the same structure in both MIBiG rows and the generated owner. The saved graph has 12 acyl carbons including its carbonyl, not 14, and an alpha-linked terminal CH(OH)2 instead of the tyrosine carboxyl group. Both properties persist in the InChI-derived saved form despite amide/imidic normalization. The mismatch is confirmed locally; which upstream name or structure is correct is not established, and no replacement molecule or identity merger is proposed. Severity is major because a material source name/structure correspondence is unsupported, rather than a claimed invalid valence or independently proven wrong natural-product identity. |
| support-2810-source-owner | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 948-999, source names and lead structure to generated label/chemical_structure | supports | The generator takes names from retained rows and chemistry from the lead source row; it does not establish semantic name–structure equivalence. |
| support-2810-correction-policy | /private/tmp/npm-record-reviews-20261021/docs/CURATION.md; lines 23-46 and 60-65, implemented structure corrections and guarded migration; lines 279-281, generated-field ownership | supports | Existing structure corrections require a supported unambiguous ChEBI target and exact source pins; none has been established here. Do not invent a target, use reserved decisions.tsv as an effective fix, or hand-edit generated YAML. |
| support-2810-review-policy | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Native questions and ownership | supports | Source-derived facts belong to maintained inventories, implemented overlays, extractors and seeder. No native status promotion follows a saved review. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-281/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-281/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-281/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-281/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-281/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established is false. The alpha centre is specified S (SMILES C14/InChI C18) in both forms; no unknown tetrahedron is listed. The true source atom-centre flag is compatible with that limited count and does not repair the connectivity/name issue. The InChI form adds a potential unspecified imidic C=N, a representation-dependent geometry candidate rather than new experimental evidence.
- Four original undefined-stereo warning lines remain globally unassigned; none is assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 281 evidence and judgments; prior batches provide interface logic only.
- No source row, record, campaign or native status was changed; no query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks. These last-five owners have negative mechanism scope and receive no maintained-reader checks.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T021905Z-n-tetradecanoyl-tyrosine
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: N-tetradecanoyl tyrosine'
started_at: '2026-11-07T01:29:28.080242Z'
finished_at: '2026-11-07T02:19:05.268181Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'The retained source label and stored graph disagree materially: the acyl
  fragment has 12 carbons including its carbonyl, and the terminal group is CH(OH)2
  rather than a tyrosine carboxyl group. Both MIBiG rows carry the same mismatch.
  This confirmed local inconsistency requires curation; the correct upstream name
  or structure and the existing shared-structure question remain unresolved.'
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
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: curation/unresolved_taxa.tsv
    sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml
    sha256: 9843bf4a4629f809a1420316790980a1ae02ed75257eb03a56d24cc3d6626a3d
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
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
    role: context
  - path: data/raw/taxon_non_organism.tsv
    sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
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
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2810; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5f6e775235
targets:
- target_id: naturalproductmech:mibig-5f6e775235
  path: data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml
  label: N-tetradecanoyl tyrosine
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
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Retained exclusion-table diagnostic context captured for every review; applicable
      exact assay exclusions and biological rows must be derived from actual retained
      inventory, not file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Retained explicit forward-merge table used by positive and negative taxon
      queries for each owner; historical route evidence only, no fresh taxonomy.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism table used by positive and negative taxon queries
      for each owner; diagnostic scope only, not a taxon verdict from file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained exclusion identity, source-row digest and attributed-rationale
      implementation context; no execution or new assay evidence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: 'Maintained producer-strain qualification implementation: source-row and
      digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency,
      no execution or grade/taxon upgrade.'
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: 'Maintained row_digest implementation used by qualification guards: sorted
      ensure_ascii JSON digest only; input presence does not claim an audit or application
      of other structure-correction behavior.'
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnose281-001.py
    39d094b3fb91806d9fc15040748c5adfccb89cfc7a705122dc84ceec8346e971 dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
    f2b54906126f773c478253bc0fb9feb17399b2f2da565d486a024c578dbd71a1
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and retain declared normalized keys; Both canonical
    SMILES comparisons are false; the saved map is empty, complete_atom_count_match
    is false and full_graph_identity_established is false.
  scope_note: 'Both saved forms have C21H35NO4, 26 atoms, 26 bonds and zero net formal
    charge. Normalized InChI, full key and formula agree, but canonical SMILES comparisons
    are false: the SMILES amide becomes an imidic C(OH)=N representation. The map
    is empty and full graph identity remains false. Internal normalized agreement
    does not resolve the label–graph disagreement. The alpha centre is specified S
    (SMILES C14/InChI C18) in both forms; no unknown tetrahedron is listed. The true
    source atom-centre flag is compatible with that limited count and does not repair
    the connectivity/name issue. The InChI form adds a potential unspecified imidic
    C=N, a representation-dependent geometry candidate rather than new experimental
    evidence. Four original undefined-stereo warning lines remain globally unassigned;
    none is assigned to an individual owner.'
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-data
  - support-2810-execution
  - support-2810-diagaccept
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  command: just validate-strict data/natural_products/unclassified/myxochromide-d-2.yaml
    data/natural_products/unclassified/myxochromide-d.yaml data/natural_products/unclassified/myxochromide-s.yaml
    data/natural_products/unclassified/myxofacycline-d.yaml data/natural_products/unclassified/myxothiazol.yaml
    data/natural_products/unclassified/myxovirescin-a1.yaml data/natural_products/unclassified/n-coronafacoyl-l-isoleucine.yaml
    data/natural_products/unclassified/n-methylwelwitindolinone-c-isothiocyanate.yaml
    data/natural_products/unclassified/n-methylwelwitinsolinone-c-isonitrile.yaml
    data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-281/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-5f6e775235
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-281/validate-all-001.tsv
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
  - naturalproductmech:mibig-5f6e775235
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
  - naturalproductmech:mibig-5f6e775235
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
  - naturalproductmech:mibig-5f6e775235
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-281/review-queue-001.tsv
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
  - naturalproductmech:mibig-5f6e775235
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2810-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/n-tetradecanoyl-tyrosine.yaml
  locator: 'complete file: identifier, label, chemical_structure, source_concepts,
    producer_organisms, biosynthetic_gene_clusters, classification, discussions and
    curation_history'
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete current owner retained; generated facts and curator-owned annotations
    remain distinct.
  snapshot_sha256: 9843bf4a4629f809a1420316790980a1ae02ed75257eb03a56d24cc3d6626a3d
- evidence_id: support-2810-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json
  locator: /records/9/owner_document; /records/9/component_captures
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Whole accepted owner capture; no component or target transfer.
  snapshot_sha256: dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
- evidence_id: support-2810-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/support-prep/support-current281-assigned-source-reading-001.json
  locator: /contexts/14; /selected_counts; /counts; /global_cautions
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete assigned saved source context. Own selected credit totals 20 rows/248
    fields/45 frames/29 negatives; ten companions have separate context-only credit.
  snapshot_sha256: f4f29428cca52b3fdd69a3e96cb5d4cd455b996f10084be86ae8c709475de30c
- evidence_id: support-2810-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-target-input-plan-001.json
  locator: /records/9; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Actual 470-placement/71-path plan; this owner has 44 captured inputs.
  snapshot_sha256: 1768138ada2bdcae10e503fb5367f29803b483a4a1b9292857d128b2806dd3b2
- evidence_id: support-2810-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/root-current281-input-plan-acceptance-001.json
  locator: /status; /accepted; /input_plan
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: ROOT accepted this original current source plan.
  snapshot_sha256: a0999f7c6f038c5a7a25face71298a63adf5773b69ae6b5c5f5f513bf697e117
- evidence_id: support-2810-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Current notes retain disjoint source and Native taxonomy/curation interpretations;
    no added primary credit.
  snapshot_sha256: d1ca69f6f2602123f4e78b56ad442002a36a9d9fe9500a36c7efbce2163569ec
- evidence_id: support-2810-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/intakes-001/2810-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Actual intake fixes generated target, maintained owners and current relative
    input hashes.
  snapshot_sha256: bf6b92c666ab78d60a2f90437826c8e9ea5eb17d35b0528539d4a9b750c528e4
- evidence_id: support-2810-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/root-current281-intake-acceptance-001.json
  locator: /status; /accepted; /intake_summary
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: ROOT accepted all ten original intakes, all exit zero with empty stderr.
  snapshot_sha256: c3101664e021d9412d0a28e7dbbc23673a92eaac35271fbc0400a2dc358e9ad1
- evidence_id: support-2810-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence;
    /records/9/literal_InChI_layers; /records/9/formula_comparison_scope
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: 'Both saved forms have C21H35NO4, 26 atoms, 26 bonds and zero net formal
    charge. Normalized InChI, full key and formula agree, but canonical SMILES comparisons
    are false: the SMILES amide becomes an imidic C(OH)=N representation. The map
    is empty and full graph identity remains false. Internal normalized agreement
    does not resolve the label–graph disagreement. Both canonical SMILES comparisons
    are false; the saved map is empty, complete_atom_count_match is false and full_graph_identity_established
    is false.'
  snapshot_sha256: f9503e14398594b03f4d7d0fefbbc595cb6cfd4d81dc07b456a97f975be3f769
- evidence_id: support-2810-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/atoms; /records/9/smiles/computed/potential_stereo;
    /records/9/smiles/computed/bonds; /records/9/inchi/computed/atoms; /records/9/inchi/computed/potential_stereo;
    /records/9/inchi/computed/bonds
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: The alpha centre is specified S (SMILES C14/InChI C18) in both forms; no
    unknown tetrahedron is listed. The true source atom-centre flag is compatible
    with that limited count and does not repair the connectivity/name issue. The InChI
    form adds a potential unspecified imidic C=N, a representation-dependent geometry
    candidate rather than new experimental evidence.
  snapshot_sha256: f9503e14398594b03f4d7d0fefbbc595cb6cfd4d81dc07b456a97f975be3f769
- evidence_id: support-2810-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/motifs; /records/9/smiles/computed/rings; /records/9/smiles/computed/bonds;
    /records/9/smiles/computed/atoms; /records/9/inchi/computed/motifs; /records/9/inchi/computed/rings;
    /records/9/inchi/computed/bonds; /records/9/inchi/computed/atoms
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: 'SMILES carbon atoms C0–C11 form the uninterrupted acyl path, including
    carbonyl C11: terminal C0 is CH3 and C1–C10 are ten CH2 groups, giving 12 acyl
    carbons rather than the 14 named by tetradecanoyl. C11(=O12)-N13 links alpha C14(S),
    benzyl C15 and a para-hydroxylated aromatic six-ring. Terminal C23 has one hydrogen
    and single bonds to alpha C14, O24H and O25H: it is CH(OH)2, not C(=O)OH. In the
    InChI form, C0–C10 plus C19 retain the 12-carbon chain, C19(OH23)=N21 is imidic,
    and C20H(OH24)(OH25) retains the geminal diol. Both forms have one aromatic ring/cycle
    rank 1; the stored strict terminal-carbonyl predicate is empty.'
  snapshot_sha256: f9503e14398594b03f4d7d0fefbbc595cb6cfd4d81dc07b456a97f975be3f769
- evidence_id: support-2810-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/support-prep/support-current281-last-five-molecular-intake-reading-001.json
  locator: /records/4; /counts; /warnings
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete ten saved forms personally read; no molecular replay. Four original
    undefined-stereo warning lines remain globally unassigned; none is assigned to
    an individual owner.
  snapshot_sha256: c9afde29330bd9367badacc73eda86f5036d62b554936e1f66812d87d912cde5
- evidence_id: support-2810-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Single original diagnostic command and retained streams; no replay.
  snapshot_sha256: 71bbb4159caead14c60c52f68bc5fba6c7c01c202065c7d884060845dcc8dfbb
- evidence_id: support-2810-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/root-current281-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /execution
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: ROOT accepted the original stored-form diagnostic.
  snapshot_sha256: 59aa0376922e13348c35507038d8316ea84cec456b334ca658b5ef604695f996
- evidence_id: support-2810-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-original-001.stderr
  locator: complete four original warning lines
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Four original undefined-stereo warning lines remain globally unassigned;
    none is assigned to an individual owner.
  snapshot_sha256: 5d01f97b54087f4a5b02d5bfa8256e2c3dd0ef1eedd4f53b44b3f15175e371eb
- evidence_id: support-2810-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-cached-taxonomy-reading-001.json
  locator: /context_interpretations/25; /physical_negative_query_scopes/25; /whole_stanzas
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Keep uncultured bacterium CSLC2 (1091571), BGC0001591/JF429413.1, separate
    from uncultured bacterium CSL12 (1091567), BGC0001687/JF429409.1. These specifically
    named cached nodes have no retained nonorganism exclusion; that does not establish
    cultured strains, species identity or demonstrated production. All saved source
    taxon IDs have complete cache stanzas; no forward merge or nonorganism match is
    retained for this context. Cached labels/synonyms do not establish current remote
    taxonomy, lineage, production or strain identity.
  snapshot_sha256: 5c1f8bf064a6a33157f3bd0a91780fee3194a6e3f6a0bf388ebfa8a4a1039672
- evidence_id: support-2810-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/native-prep/native-current281-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: No current exact applicable maintained correction; lexical names and unrelated
    BGC rows do not transfer decisions.
  snapshot_sha256: a3ef3db1fbabc749d3da41afdf67beb422a7534fb4a5ea302d922bd0ffb166f3
  search_scope: Native complete nine-table/3422-row bounded scan, exact owner/full-key/BGC/occurrence/assay
    predicates; no new query or universal absence.
- evidence_id: support-2810-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete method grading table
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Producer evidence and locus methods answer different questions; unstated
    methods retain their grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2810-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165-172, atom-centre completeness predicate
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Retained stereo_complete checks unassigned atom centres, not all geometry
    or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2810-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306, choose_pathway
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: One supported normalized pathway selects filing; multiple, none or unsupported
    values retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2810-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/root-current281-five-gates-acceptance-001.json
  locator: /records; /all_native_gates_passed; /selected_queue_rows; /unavailable_required_gates
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Five local gates pass, with required QC/OAK unavailable. Actual queue entries
    are diagnostic leads, not automatic scientific findings.
  snapshot_sha256: bee633ce4ef4b1ffa11a1442e4684d04cd28725d99a824e742150ba78847f993
- evidence_id: support-2810-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281/owner-capture-DATA-001.json
  locator: /records/9/owner_document/curation_history; /records/9/owner_document/source_concepts
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: PMID:12188643 and PMID:15528554 are distinct ENTRY-level MIBiG database
    assertions for their respective source rows. They have not been freshly read as
    primary proof of the name or structure. The two seed histories and OPEN shared-structure
    discussion remain intact.
  snapshot_sha256: dd20c76fb6a393cb3ddb8385f086f3cceb91cd099a75233730ca46241a9d680e
- evidence_id: support-2810-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-target-input-plan-001.json
  locator: /records/9/complete_root_keys; /records/9/declared_mechanism_roots_literal;
    /records/9/component_paths; /records/9/complete_raw_mechanism_sections
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: No graph, graph reference, component, pathway, target or activity root
    is present and no maintained reader is assigned. The curation concern is a source-derived
    chemical identity annotation, not a missing curated mechanism.
  snapshot_sha256: 1768138ada2bdcae10e503fb5367f29803b483a4a1b9292857d128b2806dd3b2
- evidence_id: support-2810-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 2 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 1908, raw UTF-8 row SHA-256 403fffc28f7f734a7c3eb020ba5915c0ea59e4424b7c18daf57baad1da9b59b6;
    physical line 2010, raw UTF-8 row SHA-256 a607e578133f1b536d13e5fa1434a4b0b6243f707ee1aefe1d9694e6cd12fa90
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: BGC0001591 version 4, index 2 and BGC0001687 version 3, index 1 both label
    the full key JJNOOOPGJKEVQC-IBGZPJMESA-N 'N-tetradecanoyl tyrosine'. Both rows
    are active with questionable quality and unknown completeness. Exact-key grouping
    preserves their separate source concepts but does not close the OPEN shared-structure
    discussion or establish natural identity. Uncultured bacterium CSLC2 (1091571)
    belongs to BGC0001591 and uncultured bacterium CSL12 (1091567) to BGC0001687.
    Both remain SOURCE_ASSERTION, not demonstrated production. Their cached named
    nodes do not establish cultured strains, species identity or equivalence. BGC0001591
    version 4/JF429413.1 and BGC0001687 version 3/JF429409.1 retain OTHER classes,
    CLUSTER_UNSTATED grades and blank methods/coordinates. Unknown completeness stays
    unknown; no incomplete-entry or causal-locus claim is inferred.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2810-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved chebi_structures frame with 0 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 0 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame with 0 positive placements
    read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 1121, raw UTF-8 row SHA-256 23adbe4aa848e42803ccca41e39118e0d9aa3ff17f2ad619ed75a1a62f8e2a92
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 repeats the stored
    SMILES and has empty categories with false glycoside. This model row is not independent
    confirmation of the label. UNCLASSIFIED filing correctly follows empty predictions;
    the material issue lies in name/structure correspondence, not filing.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2810-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame with 0 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved bindingdb_targets frame with 0 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame with 0 positive placements
    read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "JJNOOOPGJKEVQC-IBGZPJMESA-N" only; no source replay or universal absence.
- evidence_id: support-2810-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch281-tentative/bgc-prep/bgc-conditional281-source-inventory-DATA-001.json
  locator: /contexts/25/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Complete saved chebi_origins frame with 0 positive placements read.
  snapshot_sha256: 7addd388bd8c471fcd1acb940ca44d559b218d9ce48b6c1ca589bc54d01ec04c
  search_scope: Retained uncapped predicate exact chebi_id from exact full-key structure
    rows and query [] only; no source replay or universal absence.
- evidence_id: support-2810-finding-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch281/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/inchi/computed/atoms;
    /records/9/inchi/computed/bonds; /records/9/comparisons
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: The retained label 'N-tetradecanoyl tyrosine' conflicts with the same structure
    in both MIBiG rows and the generated owner. The saved graph has 12 acyl carbons
    including its carbonyl, not 14, and an alpha-linked terminal CH(OH)2 instead of
    the tyrosine carboxyl group. Both properties persist in the InChI-derived saved
    form despite amide/imidic normalization. The mismatch is confirmed locally; which
    upstream name or structure is correct is not established, and no replacement molecule
    or identity merger is proposed. Severity is major because a material source name/structure
    correspondence is unsupported, rather than a claimed invalid valence or independently
    proven wrong natural-product identity.
  snapshot_sha256: f9503e14398594b03f4d7d0fefbbc595cb6cfd4d81dc07b456a97f975be3f769
- evidence_id: support-2810-source-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 948-999, source names and lead structure to generated label/chemical_structure
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: The generator takes names from retained rows and chemistry from the lead
    source row; it does not establish semantic name–structure equivalence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2810-correction-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/CURATION.md
  locator: lines 23-46 and 60-65, implemented structure corrections and guarded migration;
    lines 279-281, generated-field ownership
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Existing structure corrections require a supported unambiguous ChEBI target
    and exact source pins; none has been established here. Do not invent a target,
    use reserved decisions.tsv as an effective fix, or hand-edit generated YAML.
  snapshot_sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
- evidence_id: support-2810-review-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Native questions and ownership
  accessed_at: '2026-11-07T02:10:41.915569Z'
  support: supports
  summary: Source-derived facts belong to maintained inventories, implemented overlays,
    extractors and seeder. No native status promotion follows a saved review.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:30:24.330865Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 03a80e1e85942727ce16ef18e7738a8f6e4f475ae16c33bafdff14983e11c92b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:30:50.002163Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 82e9b13ab7c0c7d66e1b379908bd1f6d1808dfa47a52bbffbf993f138e0338e5
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:31:10.249345Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:31:44.888349Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-281/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-281/native-current281-five-gates-execution-001.json
  accessed_at: '2026-11-07T01:31:56.831286Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: d0c62425db906e0c8a82e0acf6b68378fb634710f508f7e411fc343e525870de
assessments:
- assessment_id: support-2810-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: BGC0001591 version 4, index 2 and BGC0001687 version 3, index 1 both label
    the full key JJNOOOPGJKEVQC-IBGZPJMESA-N 'N-tetradecanoyl tyrosine'. Both rows
    are active with questionable quality and unknown completeness. Exact-key grouping
    preserves their separate source concepts but does not close the OPEN shared-structure
    discussion or establish natural identity. The retained label 'N-tetradecanoyl
    tyrosine' conflicts with the same structure in both MIBiG rows and the generated
    owner. The saved graph has 12 acyl carbons including its carbonyl, not 14, and
    an alpha-linked terminal CH(OH)2 instead of the tyrosine carboxyl group. Both
    properties persist in the InChI-derived saved form despite amide/imidic normalization.
    The mismatch is confirmed locally; which upstream name or structure is correct
    is not established, and no replacement molecule or identity merger is proposed.
    Severity is major because a material source name/structure correspondence is unsupported,
    rather than a claimed invalid valence or independently proven wrong natural-product
    identity.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-owner
  - support-2810-capture
  - support-2810-source
  - support-2810-intake
  - support-2810-curation
  - support-2810-finding-topology
  - support-2810-source-owner
  - support-2810-correction-policy
  - support-2810-review-policy
  - support-2810-table-mibig_compounds
  - support-2810-table-npclassifier
  dimensions:
  - name: standard_inchi_key
    definition: Full key rather than label matching.
    value: JJNOOOPGJKEVQC-IBGZPJMESA-N
    evidence_ids:
    - support-2810-owner
    - support-2810-capture
    - support-2810-source
    - support-2810-intake
    - support-2810-curation
    - support-2810-finding-topology
    - support-2810-source-owner
    - support-2810-correction-policy
    - support-2810-review-policy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
  - name: grounding_scope
    definition: Retained source identity is distinct from natural identity.
    value: BGC0001591 version 4, index 2 and BGC0001687 version 3, index 1 both label
      the full key JJNOOOPGJKEVQC-IBGZPJMESA-N 'N-tetradecanoyl tyrosine'. Both rows
      are active with questionable quality and unknown completeness. Exact-key grouping
      preserves their separate source concepts but does not close the OPEN shared-structure
      discussion or establish natural identity.
    evidence_ids:
    - support-2810-owner
    - support-2810-capture
    - support-2810-source
    - support-2810-intake
    - support-2810-curation
    - support-2810-finding-topology
    - support-2810-source-owner
    - support-2810-correction-policy
    - support-2810-review-policy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
- assessment_id: support-2810-representation-assessment
  area: representation
  topic: Saved molecular forms and stereochemical scope
  summary: 'Both saved forms have C21H35NO4, 26 atoms, 26 bonds and zero net formal
    charge. Normalized InChI, full key and formula agree, but canonical SMILES comparisons
    are false: the SMILES amide becomes an imidic C(OH)=N representation. The map
    is empty and full graph identity remains false. Internal normalized agreement
    does not resolve the label–graph disagreement. SMILES carbon atoms C0–C11 form
    the uninterrupted acyl path, including carbonyl C11: terminal C0 is CH3 and C1–C10
    are ten CH2 groups, giving 12 acyl carbons rather than the 14 named by tetradecanoyl.
    C11(=O12)-N13 links alpha C14(S), benzyl C15 and a para-hydroxylated aromatic
    six-ring. Terminal C23 has one hydrogen and single bonds to alpha C14, O24H and
    O25H: it is CH(OH)2, not C(=O)OH. In the InChI form, C0–C10 plus C19 retain the
    12-carbon chain, C19(OH23)=N21 is imidic, and C20H(OH24)(OH25) retains the geminal
    diol. Both forms have one aromatic ring/cycle rank 1; the stored strict terminal-carbonyl
    predicate is empty. Both canonical SMILES comparisons are false; the saved map
    is empty, complete_atom_count_match is false and full_graph_identity_established
    is false. Normalized key/formula agreement and a successful local process do not
    establish independent full graph identity, natural-sample identity, experimental
    absolute stereochemistry, primary mechanism validation or a native status promotion.'
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-data
  - support-2810-stereo
  - support-2810-motifs
  - support-2810-molecularreading
  - support-2810-execution
  - support-2810-diagaccept
  - support-2810-stereopolicy
  - support-2810-finding-topology
  - support-2810-source-owner
  - support-2810-correction-policy
  - support-2810-review-policy
  - support-2810-table-mibig_compounds
  - support-2810-table-npclassifier
  dimensions:
  - name: stereochemistry_scope
    definition: Specified atom centres and representation-dependent candidates remain
      distinct.
    value: The alpha centre is specified S (SMILES C14/InChI C18) in both forms; no
      unknown tetrahedron is listed. The true source atom-centre flag is compatible
      with that limited count and does not repair the connectivity/name issue. The
      InChI form adds a potential unspecified imidic C=N, a representation-dependent
      geometry candidate rather than new experimental evidence.
    evidence_ids:
    - support-2810-data
    - support-2810-stereo
    - support-2810-motifs
    - support-2810-molecularreading
    - support-2810-execution
    - support-2810-diagaccept
    - support-2810-stereopolicy
    - support-2810-finding-topology
    - support-2810-source-owner
    - support-2810-correction-policy
    - support-2810-review-policy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
  - name: representation_correspondence
    definition: Saved limited comparison, not full identity.
    value: Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
      is false and full_graph_identity_established is false. Normalized key/formula
      agreement and a successful local process do not establish independent full graph
      identity, natural-sample identity, experimental absolute stereochemistry, primary
      mechanism validation or a native status promotion.
    evidence_ids:
    - support-2810-data
    - support-2810-stereo
    - support-2810-motifs
    - support-2810-molecularreading
    - support-2810-execution
    - support-2810-diagaccept
    - support-2810-stereopolicy
    - support-2810-finding-topology
    - support-2810-source-owner
    - support-2810-correction-policy
    - support-2810-review-policy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
- assessment_id: support-2810-provenance-assessment
  area: provenance
  topic: Compound-specific producer, locus and taxon
  summary: Uncultured bacterium CSLC2 (1091571) belongs to BGC0001591 and uncultured
    bacterium CSL12 (1091567) to BGC0001687. Both remain SOURCE_ASSERTION, not demonstrated
    production. Their cached named nodes do not establish cultured strains, species
    identity or equivalence. BGC0001591 version 4/JF429413.1 and BGC0001687 version
    3/JF429409.1 retain OTHER classes, CLUSTER_UNSTATED grades and blank methods/coordinates.
    Unknown completeness stays unknown; no incomplete-entry or causal-locus claim
    is inferred.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-source
  - support-2810-capture
  - support-2810-taxonomy
  - support-2810-curation
  - support-2810-producerpolicy
  - support-2810-table-mibig_compounds
  - support-2810-table-npclassifier
  dimensions:
  - name: taxon_scope
    definition: Cached names do not establish current lineage or strain equivalence.
    value: Keep uncultured bacterium CSLC2 (1091571), BGC0001591/JF429413.1, separate
      from uncultured bacterium CSL12 (1091567), BGC0001687/JF429409.1. These specifically
      named cached nodes have no retained nonorganism exclusion; that does not establish
      cultured strains, species identity or demonstrated production. All saved source
      taxon IDs have complete cache stanzas; no forward merge or nonorganism match
      is retained for this context. Cached labels/synonyms do not establish current
      remote taxonomy, lineage, production or strain identity.
    evidence_ids:
    - support-2810-source
    - support-2810-capture
    - support-2810-taxonomy
    - support-2810-curation
    - support-2810-producerpolicy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
  - name: producer_evidence
    definition: Producer and locus evidence remain separate.
    value: Uncultured bacterium CSLC2 (1091571) belongs to BGC0001591 and uncultured
      bacterium CSL12 (1091567) to BGC0001687. Both remain SOURCE_ASSERTION, not demonstrated
      production. Their cached named nodes do not establish cultured strains, species
      identity or equivalence.
    evidence_ids:
    - support-2810-source
    - support-2810-capture
    - support-2810-taxonomy
    - support-2810-curation
    - support-2810-producerpolicy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
  - name: locus_evidence
    definition: Exact source version, endpoints and methods delimit the claim.
    value: BGC0001591 version 4/JF429413.1 and BGC0001687 version 3/JF429409.1 retain
      OTHER classes, CLUSTER_UNSTATED grades and blank methods/coordinates. Unknown
      completeness stays unknown; no incomplete-entry or causal-locus claim is inferred.
    evidence_ids:
    - support-2810-source
    - support-2810-capture
    - support-2810-taxonomy
    - support-2810-curation
    - support-2810-producerpolicy
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
- assessment_id: support-2810-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: PMID:12188643 and PMID:15528554 are distinct ENTRY-level MIBiG database
    assertions for their respective source rows. They have not been freshly read as
    primary proof of the name or structure. The two seed histories and OPEN shared-structure
    discussion remain intact.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-owner
  - support-2810-source
  - support-2810-capture
  - support-2810-history
  - support-2810-table-mibig_compounds
  - support-2810-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Repeated annotations are not independent primary proof.
    value: PMID:12188643 and PMID:15528554 are distinct ENTRY-level MIBiG database
      assertions for their respective source rows. They have not been freshly read
      as primary proof of the name or structure. The two seed histories and OPEN shared-structure
      discussion remain intact.
    evidence_ids:
    - support-2810-owner
    - support-2810-source
    - support-2810-capture
    - support-2810-history
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
- assessment_id: support-2810-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay limits
  summary: No exact-key LOTUS or CyanoMetDB occurrence row is retained. The two producer
    assertions are not converted into occurrence evidence or broadened to other taxa.
    No actual assay, target, ChEBI or AntibioticMech payload is retained under the
    owner's saved predicates. This neither supplies a replacement structure nor establishes
    biological inactivity.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-source
  - support-2810-taxonomy
  - support-2810-curation
  - support-2810-plan
  - support-2810-query-mibig_compounds
  - support-2810-query-chebi_structures
  - support-2810-query-lotus_occurrences
  - support-2810-query-cyanometdb_occurrences
  - support-2810-query-npclassifier
  - support-2810-query-pubchem_bioassay
  - support-2810-query-bindingdb_targets
  - support-2810-query-antibioticmech_inchikeys
  - support-2810-query-chebi_origins
  dimensions:
  - name: occurrence_scope
    definition: Occurrence does not establish production.
    value: No exact-key LOTUS or CyanoMetDB occurrence row is retained. The two producer
      assertions are not converted into occurrence evidence or broadened to other
      taxa.
    evidence_ids:
    - support-2810-source
    - support-2810-taxonomy
    - support-2810-curation
    - support-2810-plan
    - support-2810-query-mibig_compounds
    - support-2810-query-chebi_structures
    - support-2810-query-lotus_occurrences
    - support-2810-query-cyanometdb_occurrences
    - support-2810-query-npclassifier
    - support-2810-query-pubchem_bioassay
    - support-2810-query-bindingdb_targets
    - support-2810-query-antibioticmech_inchikeys
    - support-2810-query-chebi_origins
  - name: assay_target_scope
    definition: Blank sentinels and bounded negatives are not inactivity.
    value: No actual assay, target, ChEBI or AntibioticMech payload is retained under
      the owner's saved predicates. This neither supplies a replacement structure
      nor establishes biological inactivity.
    evidence_ids:
    - support-2810-source
    - support-2810-taxonomy
    - support-2810-curation
    - support-2810-plan
    - support-2810-query-mibig_compounds
    - support-2810-query-chebi_structures
    - support-2810-query-lotus_occurrences
    - support-2810-query-cyanometdb_occurrences
    - support-2810-query-npclassifier
    - support-2810-query-pubchem_bioassay
    - support-2810-query-bindingdb_targets
    - support-2810-query-antibioticmech_inchikeys
    - support-2810-query-chebi_origins
- assessment_id: support-2810-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 repeats the stored
    SMILES and has empty categories with false glycoside. This model row is not independent
    confirmation of the label. UNCLASSIFIED filing correctly follows empty predictions;
    the material issue lies in name/structure correspondence, not filing.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-source
  - support-2810-owner
  - support-2810-motifs
  - support-2810-filingpolicy
  - support-2810-gates
  - support-2810-table-mibig_compounds
  - support-2810-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Model, source and saved topology are separate evidence.
    value: NPClassifier version npclassifier.gnps2.org@2026-09-07 repeats the stored
      SMILES and has empty categories with false glycoside. This model row is not
      independent confirmation of the label. UNCLASSIFIED filing correctly follows
      empty predictions; the material issue lies in name/structure correspondence,
      not filing.
    evidence_ids:
    - support-2810-source
    - support-2810-owner
    - support-2810-motifs
    - support-2810-filingpolicy
    - support-2810-gates
    - support-2810-table-mibig_compounds
    - support-2810-table-npclassifier
- assessment_id: support-2810-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: Complete assigned raw/source/intake and both saved molecular forms were
    read. No graph, graph reference, component, pathway, target or activity root is
    present and no maintained reader is assigned. The curation concern is a source-derived
    chemical identity annotation, not a missing curated mechanism. The major local
    label–graph finding remains open. Five local native commands pass; full QC, complete
    OAK and fresh primary verification remain unavailable. Completion is partial,
    native SEEDED status unchanged.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  evidence_ids:
  - support-2810-intake
  - support-2810-intakeaccept
  - support-2810-plan
  - support-2810-planaccept
  - support-2810-notes
  - support-2810-gates
  - support-2810-data
  - support-2810-diagaccept
  - support-2810-scope
  dimensions:
  - name: review_completion
    definition: Local review does not promote native status or substitute for unavailable
      checks.
    value: Complete assigned raw/source/intake and both saved molecular forms were
      read. No graph, graph reference, component, pathway, target or activity root
      is present and no maintained reader is assigned. The curation concern is a source-derived
      chemical identity annotation, not a missing curated mechanism. The major local
      label–graph finding remains open. Five local native commands pass; full QC,
      complete OAK and fresh primary verification remain unavailable. Completion is
      partial, native SEEDED status unchanged.
    evidence_ids:
    - support-2810-intake
    - support-2810-intakeaccept
    - support-2810-plan
    - support-2810-planaccept
    - support-2810-notes
    - support-2810-gates
    - support-2810-data
    - support-2810-diagaccept
    - support-2810-scope
findings:
- finding_id: support-2810-label-structure-acyl-terminal-mismatch
  issue_key: n-tetradecanoyl-tyrosine-source-label-structure-mismatch
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Source label disagrees with acyl length and terminal group in the stored
    graph
  description: The retained label 'N-tetradecanoyl tyrosine' conflicts with the same
    structure in both MIBiG rows and the generated owner. The saved graph has 12 acyl
    carbons including its carbonyl, not 14, and an alpha-linked terminal CH(OH)2 instead
    of the tyrosine carboxyl group. Both properties persist in the InChI-derived saved
    form despite amide/imidic normalization. The mismatch is confirmed locally; which
    upstream name or structure is correct is not established, and no replacement molecule
    or identity merger is proposed. Severity is major because a material source name/structure
    correspondence is unsupported, rather than a claimed invalid valence or independently
    proven wrong natural-product identity.
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  field_paths:
  - /label
  - /chemical_structure/smiles
  - /chemical_structure/standard_inchi
  - /source_concepts
  evidence_ids:
  - support-2810-owner
  - support-2810-capture
  - support-2810-table-mibig_compounds
  - support-2810-finding-topology
  - support-2810-data
  - support-2810-diagaccept
  - support-2810-intake
  - support-2810-curation
  - support-2810-source-owner
  - support-2810-correction-policy
  - support-2810-review-policy
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Retained MIBiG structure, producer and compound-specific locus assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained extraction of MIBiG compound names, structures, stereochemistry
      flags and source provenance.
  ownership_note: The exact retained source name/structure correspondence is confirmed
    inconsistent; the correct upstream replacement is unresolved. Seeded chemistry
    and label are owned by maintained source/extraction/harmonization inputs, not
    hand edits to generated YAML or pages.
actions:
- action_id: support-2810-reconcile-source-name-and-structure
  description: Adjudicate both BGC0001591:2 and BGC0001687:1 source name/structure
    pairs through a separately authorized maintained source-correction workflow. Determine
    whether the name, acyl chain, terminal group or upstream source mapping requires
    correction using appropriate primary evidence; do not choose a replacement from
    the label alone. Preserve both source concepts and the OPEN shared-structure discussion
    until that separate question is resolved. The existing ChEBI correction actions
    require an actual supported target and are not a generic freeform SMILES patch.
  finding_ids:
  - support-2810-label-structure-acyl-terminal-mismatch
  target_ids:
  - naturalproductmech:mibig-5f6e775235
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Retained MIBiG structure, producer and compound-specific locus assertions.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: Maintained extraction of MIBiG compound names, structures, stereochemistry
      flags and source provenance.
  ownership_note: Proposed maintained source/extractor/seeder correction only; no
    source, YAML, classification, identifier, path, history or campaign edit is performed
    here. No external work is started, queued or authorized by this action.
  acceptance_checks:
  - Document exact source-row versions, parsed-row digest pins and evidence for each
    affected source compound, keeping source and natural identity claims separate.
  - Show that the adopted label and structure agree on acyl-carbon count, terminal
    functional group, formula, charge and supported stereochemistry; retain disagreements
    explicitly rather than inventing a structure.
  - Use an implemented, tested correction path only when its prerequisites are met;
    otherwise implement the necessary maintained consumer with focused name/structure
    regression coverage. Do not use reserved decisions.tsv or hand-edit the generated
    record.
  - In a separately authorized correction workflow, regenerate through the validated
    writer and verify source ownership, identifier/path migration if needed, append-only
    history, corpus integrity and reproduction without silently closing the shared-structure
    discussion.
limitations:
- Normalized key/formula agreement and a successful local process do not establish
  independent full graph identity, natural-sample identity, experimental absolute
  stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons are false; the saved map is empty, complete_atom_count_match
  is false and full_graph_identity_established is false. The alpha centre is specified
  S (SMILES C14/InChI C18) in both forms; no unknown tetrahedron is listed. The true
  source atom-centre flag is compatible with that limited count and does not repair
  the connectivity/name issue. The InChI form adds a potential unspecified imidic
  C=N, a representation-dependent geometry candidate rather than new experimental
  evidence.
- Four original undefined-stereo warning lines remain globally unassigned; none is
  assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 281 evidence and judgments; prior batches provide interface logic
  only.
- No source row, record, campaign or native status was changed; no query, molecular
  parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks. These
  last-five owners have negative mechanism scope and receive no maintained-reader
  checks.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-281
```
