# Local evidence review: coelimycin P1

- Review: 20261105T145723Z-coelimycin-p1
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T13:44:18.251866Z
- Finished UTC: 2026-11-05T14:57:23.321901Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Coelimycin P1 identity and all five preserved graphs retain their limits: native-reference assertions and two disconnected inferred reactions do not establish a complete pathway.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2569; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5c75ae209a | data/natural_products/unclassified/coelimycin-p1.yaml | generated | coelimycin P1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for coelimycin-p1 | passed | True | naturalproductmech:mibig-5c75ae209a | One accepted offline maintained-reader call preserved the complete owner, five graphs, 14 nodes, nine edges, 18 reference placements and three histories; no molecular or experimental validation is implied. |
| strict_ten | passed | True | naturalproductmech:mibig-5c75ae209a | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5c75ae209a | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5c75ae209a | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5c75ae209a | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5c75ae209a | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5c75ae209a | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5c75ae209a | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5c75ae209a | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding scope

identity: supported. Targets: naturalproductmech:mibig-5c75ae209a.

The retained MINTED owner naturalproductmech:mibig-5c75ae209a preserves the complete key RHGMVWUZXGSXCT-HXNNLKDLSA-N, its MIBiG structure and source label. Both saved forms reproduce the declared Standard InChI and full key. The exact retained ChEBI structure frame is empty; this bounds the stored grounding rationale without a fresh authority search. Name, shared locus and connectivity-block similarity are not substituted for exact owner identity.

### Stored representations and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-5c75ae209a.

Both forms retain neutral C17H20N2O4S and the declared normalized identifiers, but canonical strings differ and the direct map is empty. The N-acetyl amide becomes an imidic site; the ketone and ester remain. One tetrahedral center is unspecified and three double bonds are specified, consistent with the stored incomplete flag. The extra imidic geometry is representation-specific. The eight-member sulfur/ester-containing ring and separate unsaturated nitrogen ring do not validate the inferred enzyme models.

### Producer, locus and taxonomy scope

provenance: supported. Targets: naturalproductmech:mibig-5c75ae209a.

BGC0000038 version 5 retains Streptomyces coelicolor A3(2) at NCBITaxon:100226 as BGC_CHARACTERIZED and AL645882.2:6890528..6948414 as CLUSTER_DEMONSTRATED with knock-out studies. These are retained source grades; present local review does not independently repeat or verify those experiments. Cached identifiers, names and synonyms do not newly verify rank, ancestry or strain equivalence.

### Citation categories and source access

evidence: supported. Targets: naturalproductmech:mibig-5c75ae209a.

DOI:10.1039/c2sc20410j has exact COMPOUND_EVIDENCE scope. The two LOTUS occurrence rows cite DOI:10.1007/S00203-006-0176-7. Historical sequence/structure access, abstract-only coverage and 403 responses are record content unless original source bytes are actually retained and read now.

### Occurrence, activity and companion boundaries

evidence: supported. Targets: naturalproductmech:mibig-5c75ae209a.

LOTUS taxon 1886 albidoflavus and 1902 coelicolor naming assertions remain distinct from the selected strain 100226. Exact saved assay/target query frames are empty.

### Computed classification applicability

consistency: not_applicable. Targets: naturalproductmech:mibig-5c75ae209a.

All three computed classification axes are empty. The source PKS class is distinct from the sulfur/ester-containing ring and nitrogen-ring topology. The five graphs contain no ordered pathway and do not fill a missing classification result or prove a complete biosynthetic route to this owner.

### Native-reference and inferred reaction graphs

graph: supported. Targets: naturalproductmech:mibig-5c75ae209a.

The complete maintained view preserves three native-reference graphs for Q9EX55, Q93S10 and Q93S08 and two explicitly inferred MITE reaction graphs. Reference-sequence mappings do not prove expression, processed constructs, cofactor use or individual enzyme activity. SCO6279’s modeled product and SCO6272’s substrate share a connectivity block but have different full-key suffixes, so no inter-graph reaction order is established. SCO6281’s reaction remains withheld under retained issue 695: C12H19NO3 to C12H17NO3 retains the oxygen count despite the historical monooxygenation label. Ungrounded intermediates, incomplete model stereochemistry and historical abstract-only access remain explicit; no exact P1 product edge, P1/P2 equivalence or complete pathway is asserted.

### Evidence coverage and review completion

completeness: unknown. Targets: naturalproductmech:mibig-5c75ae209a.

The retained identity, source grades and local chemistry are reviewable within the stated limits. Required full QC and OAK coverage remain unavailable, and primary publications and fresh authorities were not accessed. Completion is partial; no unambiguous source defect requiring a record edit was established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2569-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/coelimycin-p1.yaml; Whole current plaintext including complete curation_history | supports | Complete current selected owner and all 3 history events; no native record/status/history changes. |
| support-2569-capture | /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete captured owner and every present root. Root presence and absence are retained exactly for this owner. |
| support-2569-grounding-owner | /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Exact retained identifier, full key, source structure and present source/grounding fields; no fresh natural identity validation. |
| support-2569-origin-owner | /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/producer_taxon_groups | supports | Complete producer and locus claims with separate evidence grades, methods, coordinates and source classes. |
| support-2569-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete owner preserves exact occurrence, activity, target and mechanism root presence or absence; production context is distinct from pharmacological activity. |
| support-2569-classification-owner | /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin | supports | Versioned model output, source BGC classes and UNCLASSIFIED filing remain separate assertions. |
| support-2569-direct-contexts | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates; /records/8/identity_comparison_paths; /records/8/additional_context_roles | context_only | Exact owner-local direct companion, identity-comparison and additional-input roles. Five diagnostic/query inputs are included for this owner; maintained-reader source roles follow this owner’s literal applicability. Input capture is distinct from positive evidence. |
| support-2569-intake | /private/tmp/npm-review-work/shared-next-batch257/intakes/2569-inspect-001.json; /targets; /source | supports | Actual canonical target, source inputs and maintained ownership are retained. |
| support-2569-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch257/root-intake-acceptance-001.json; /status; /intakes/8; /source_plan; /verification | supports | ROOT accepts this original canonical intake and its exact source-plan/input joins. |
| support-2569-intake-reading | /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-last-five-molecular-intake-reading-001.json; /records/3/target_id; /records/3/actual_intake; /totals | supports | Support read the five actual canonical target/ownership documents and verified 226 captured input placements across 62 paths. This does not claim scientific reading of entire underlying corpus files. |
| support-2569-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch257/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; this is not primary-paper verification. |
| support-2569-plan | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-target-input-plan-001.json; /records/8/proposed_input_paths; /records/8/proposed_input_count | supports | The accepted input map agrees exactly with this canonical intake. |
| support-2569-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch257/root-source-plan-acceptance-001.json; /status; /verification | supports | ROOT accepts the operative 458-placement, 68-path plan with five diagnostic/query inputs in every intake. Positive source rows remain separately scoped. |
| support-2569-source-reading | /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-assigned-source-reading-001.json; /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows; /cautions; /reading_method | supports | Support personally read 13 assigned contexts: 117 saved frames, 77 positive row placements and 865 fields. Five selected owners contribute 45 frames, 16 rows and 206 fields; eight companion contexts and the one historical taxon-merge row remain separate. BGC owns the other 12 contexts; no new primary-literature verification is implied. |
| support-2569-source-notes | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes retain disjoint BGC 48/Support 77/Native 0 positive-row reading attribution, original 458-placement/68-path input scope, and explicit retained-source and companion limits. This receipt does not establish subsequent intake or scientific outcomes. |
| support-2569-molecular-reading | /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-last-five-molecular-intake-reading-001.json; /records/3; /totals; /whole_table_reading_method; /warning_scope; /limits | supports | Support personally read all ten complete saved forms: 376 atom rows and 388 bond rows, with complete stereo, motif and comparison fields. Corresponding actual intake metadata and 226 captured input hashes/ownership declarations were verified; this is not whole-corpus scientific reading. |
| support-2569-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/19 | context_only | Complete relevant retained cache stanzas preserve identifiers, names and synonyms only. They contain no explicit rank or lineage fields and do not prove ancestry, strain equivalence, native production or fresh taxonomy. |
| support-2569-taxonomy-query-routes | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/source_taxa; /contexts/15/source_scope_inventory/forward_taxon_merge_matches; /contexts/15/source_scope_inventory/nonorganism_matches | context_only | Complete retained source taxon IDs and saved forward-merge/non-organism results; historical merge routes are distinct from current nomenclatural, rank or ancestry verification. |
| support-2569-raw-reading | /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-assigned-source-reading-001.json; /raw_reading; /selected_scope; /companion_scope | context_only | This assigned-reading receipt records complete selected owner/history reading and separately attributed companion reading. Historical source-access assertions remain record content, not fresh verification. |
| support-2569-required-gates | /private/tmp/npm-review-work/shared-next-batch257/root-current257-five-gates-acceptance-001.json; /status; /verification; /unavailable_required_gates | supports | ROOT accepts five local gate results; the required QC and OAK checks remain unavailable, so completion is partial. |
| support-2569-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch257-tentative/native-prep/native-current257-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation; /routes | context_only | Native complete cache and route interpretation remains attributed; owner-local retained stanzas carry only their exact saved fields. |
| support-2569-curation-scope | /private/tmp/npm-review-work/shared-next-batch257-tentative/native-prep/native-current257-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | The bounded implemented-table scan found no applicable exact replacement for these owners; unrelated lexical hits are not imported as owner evidence. |
| support-2569-chemistry | /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope; /records/8/comparisons; /records/8/atom_correspondence | supports | Both canonical-SMILES comparisons are false; the direct map is empty. Normalized identifiers, formula and charge agree while amide/imidic representations differ. |
| support-2569-topology | /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles; /records/8/inchi | supports | Complete saved atom/bond/ring/stereo/motif tables retain representation-specific counts and stereochemical assignments; no new parse or natural-state claim. |
| support-2569-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /limits | supports | ROOT accepts the single original stored-form diagnostic and its saved results. Complete scientific table reading is separately attributed; normalization is not natural-identity proof. |
| support-2569-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, terminal exit and stream pins; no retry or external request. |
| support-2569-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Six original omitted-undefined-stereo warnings remain global, without assignment to an owner or form. |
| support-2569-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2569-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2569-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2569-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2569-reader-DATA | /private/tmp/npm-review-work/shared-next-batch257/native-current257-coelimycin-p1-maintained-reader-DATA-001.json; /resolved_view; /returned_view_equals_expected_complete_owner; /counts; /errors; /unexpected_denials; /external_requests | supports | The accepted single maintained-reader result preserves the complete owner, five graphs, 14 nodes, nine edges, 18 graph reference placements and three histories; technical preservation does not prove enzyme activity. |
| support-2569-reader-execution | /private/tmp/npm-review-work/shared-next-batch257/native-current257-coelimycin-p1-reader-execution-001.json; /exit_code; /command | supports | Genuine original maintained-reader execution exited zero; no retry or new experimental evidence. |
| support-2569-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch257/root-native-reader-2569-acceptance-001.json; /status; /accepted; /DATA; /execution; /verification; /review_check_contract; /limits | supports | ROOT accepts the exact complete-owner preservation result and supplies the required typed check contract; all scientific scope limits remain. |
| support-2569-reader-whole-reading | /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-coelimycin-maintained-view-reading-001.json; /reading; /equalities; /interpretation; /technical_scope | context_only | Support personally read the entire unique maintained owner, all five graphs and 18 reference placements, and all three histories. Retained sequence and abstract-access assertions are not freshly accessed sources. |
| support-2569-graph-content | /private/tmp/npm-review-work/shared-next-batch257/native-current257-coelimycin-p1-maintained-reader-DATA-001.json; /resolved_view/causal_graphs; /resolved_view/curation_history | supports | Three native-reference identity graphs and two genomic/chemical inference models retain exact identifiers, model keys, ungrounded intermediates and source qualifications. SCO6281 reaction remains withheld; no ordered pathway or P1/P2 equivalence is added. |
| support-2569-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained physical row 50, all 25 fields: BGC0000038 version 5; Streptomyces coelicolor A3(2), producer BGC_CHARACTERIZED, locus CLUSTER_DEMONSTRATED; DOI:10.1039/c2sc20410j at COMPOUND_EVIDENCE scope. Source structure, methods and classes remain exact. |
| support-2569-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 50 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2569-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 2 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained physical row 7722, all 6 fields: Streptomyces albidoflavus (NCBITaxon:1886), DOI:10.1007/S00203-006-0176-7; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2569-source-lotus_occurrences-1 | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/lotus_occurrences/matches/1 | supports | Complete retained physical row 7723, all 6 fields: Streptomyces coelicolor (NCBITaxon:1902), DOI:10.1007/S00203-006-0176-7; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2569-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 7722, 7723 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2569-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained physical row 2110, all 7 fields: npclassifier.gnps2.org@2026-09-07: //; glycoside=false, model assertion only. |
| support-2569-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 2110 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2569-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2569-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json; /contexts/15/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-257/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-257/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-257/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-257/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-257/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; no newly inspected original publications, sequence databases, fresh taxonomy or independent natural-identity verification.
- Normalized identifiers, canonical comparisons and substructure mappings have separate scopes. Six global undefined-stereo warnings remain unassigned to individual forms or owners.
- Required full QC and OAK coverage remain unavailable. No source record, native status or history was edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete owner/history and saved molecular-table readings are distinct from verification of captured input hashes and ownership declarations. Input capture does not claim scientific reading of entire underlying corpus tables.
- Assigned retained-source reading covers 13 contexts: 117 saved query frames, 77 positive row placements and 865 fields. The five selected owners account for 45 frames, 16 rows and 206 fields; eight companions remain separately attributed.
- No source query, molecular parse or maintained-reader replay was performed in authoring these assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T145723Z-coelimycin-p1
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: coelimycin P1'
started_at: '2026-11-05T13:44:18.251866Z'
finished_at: '2026-11-05T14:57:23.321901Z'
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
summary: 'Coelimycin P1 identity and all five preserved graphs retain their limits:
  native-reference assertions and two disconnected inferred reactions do not establish
  a complete pathway.'
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
  - path: data/natural_products/unclassified/coelimycin-p1.yaml
    sha256: 4c33d0500307a16af98db0e0d26f02b9165a7c6d78850138abe5506f7355e3e4
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
  selection: Campaign path order 2569; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5c75ae209a
targets:
- target_id: naturalproductmech:mibig-5c75ae209a
  path: data/natural_products/unclassified/coelimycin-p1.yaml
  label: coelimycin P1
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
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/coelimycin-p1.yaml
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
- name: Complete offline maintained reader for coelimycin-p1
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch257/read-selected-mechanism-guarded-001.py
    2569 05182960861d7f4c17251a2816823d29c6667e49a2671b6ece1ceb4d8af408c7 65f59fe9d470f7306f1046fa25a627b118e5b95387da365ddcb072ec77790f32
    f0671699406f0363cf2d44e1d0d02a8c43fb8bcfd9ba9c060550511d0e0e09e7 9dfb56e27c0b220291f25b00e78d01bc9a34e67f0fc699b4e4b0d6e5f4bf36bb
    a1b28875b59f90260308ad666eba22dc4a5d7165fd6ccde2b71e7c813393b883
  status: passed
  required: true
  exit_code: 0
  check_id: maintained-mechanism-reader
  expected_exit_code: 0
  summary: One accepted offline maintained-reader call preserved the complete owner,
    five graphs, 14 nodes, nine edges, 18 reference placements and three histories;
    no molecular or experimental validation is implied.
  evidence_ids:
  - support-2569-reader-DATA
  - support-2569-reader-execution
  - support-2569-reader-acceptance
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  command: just validate-strict data/natural_products/unclassified/clifednamide-a-2.yaml
    data/natural_products/unclassified/clifednamide-a.yaml data/natural_products/unclassified/clifednamide-e.yaml
    data/natural_products/unclassified/clifednamide-f.yaml data/natural_products/unclassified/clifednamide-i.yaml
    data/natural_products/unclassified/clifednamide-j.yaml data/natural_products/unclassified/clovibactin.yaml
    data/natural_products/unclassified/cmc-thuggacin-b.yaml data/natural_products/unclassified/coelimycin-p1.yaml
    data/natural_products/unclassified/colletochlorin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-257/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-5c75ae209a
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-257/validate-all-001.tsv
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
  - naturalproductmech:mibig-5c75ae209a
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
  - naturalproductmech:mibig-5c75ae209a
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
  - naturalproductmech:mibig-5c75ae209a
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-257/review-queue-001.tsv
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
  - naturalproductmech:mibig-5c75ae209a
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2569-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/coelimycin-p1.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Complete current selected owner and all 3 history events; no native record/status/history
    changes.
  snapshot_sha256: 4c33d0500307a16af98db0e0d26f02b9165a7c6d78850138abe5506f7355e3e4
- evidence_id: support-2569-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Complete captured owner and every present root. Root presence and absence
    are retained exactly for this owner.
  snapshot_sha256: 9dfb56e27c0b220291f25b00e78d01bc9a34e67f0fc699b4e4b0d6e5f4bf36bb
- evidence_id: support-2569-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Exact retained identifier, full key, source structure and present source/grounding
    fields; no fresh natural identity validation.
  snapshot_sha256: 9dfb56e27c0b220291f25b00e78d01bc9a34e67f0fc699b4e4b0d6e5f4bf36bb
- evidence_id: support-2569-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/producer_taxon_groups
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Complete producer and locus claims with separate evidence grades, methods,
    coordinates and source classes.
  snapshot_sha256: 9dfb56e27c0b220291f25b00e78d01bc9a34e67f0fc699b4e4b0d6e5f4bf36bb
- evidence_id: support-2569-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Complete owner preserves exact occurrence, activity, target and mechanism
    root presence or absence; production context is distinct from pharmacological
    activity.
  snapshot_sha256: 9dfb56e27c0b220291f25b00e78d01bc9a34e67f0fc699b4e4b0d6e5f4bf36bb
- evidence_id: support-2569-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Versioned model output, source BGC classes and UNCLASSIFIED filing remain
    separate assertions.
  snapshot_sha256: 9dfb56e27c0b220291f25b00e78d01bc9a34e67f0fc699b4e4b0d6e5f4bf36bb
- evidence_id: support-2569-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates;
    /records/8/identity_comparison_paths; /records/8/additional_context_roles
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Exact owner-local direct companion, identity-comparison and additional-input
    roles. Five diagnostic/query inputs are included for this owner; maintained-reader
    source roles follow this owner’s literal applicability. Input capture is distinct
    from positive evidence.
  snapshot_sha256: 11ff99dffc837597d0ba21ff6c59287f8ed50c18b79faded6acafff16bd862ac
- evidence_id: support-2569-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/intakes/2569-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Actual canonical target, source inputs and maintained ownership are retained.
  snapshot_sha256: 65f59fe9d470f7306f1046fa25a627b118e5b95387da365ddcb072ec77790f32
- evidence_id: support-2569-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/root-intake-acceptance-001.json
  locator: /status; /intakes/8; /source_plan; /verification
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: ROOT accepts this original canonical intake and its exact source-plan/input
    joins.
  snapshot_sha256: af623a0605b56940f20bbcfa1397f655cffd6a46c7217fdc08e33868397395be
- evidence_id: support-2569-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-last-five-molecular-intake-reading-001.json
  locator: /records/3/target_id; /records/3/actual_intake; /totals
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Support read the five actual canonical target/ownership documents and verified
    226 captured input placements across 62 paths. This does not claim scientific
    reading of entire underlying corpus files.
  snapshot_sha256: 21725ff2a7ddc02e3ceba0f075eeac2128059e4bbbe700483778ae4e260cfa15
- evidence_id: support-2569-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; this is not primary-paper
    verification.
  snapshot_sha256: 65669351dfccf9b95f36f311185064ba0c32bd8d2ac90905bf4190892f547b48
- evidence_id: support-2569-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-target-input-plan-001.json
  locator: /records/8/proposed_input_paths; /records/8/proposed_input_count
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: The accepted input map agrees exactly with this canonical intake.
  snapshot_sha256: 11ff99dffc837597d0ba21ff6c59287f8ed50c18b79faded6acafff16bd862ac
- evidence_id: support-2569-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/root-source-plan-acceptance-001.json
  locator: /status; /verification
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: ROOT accepts the operative 458-placement, 68-path plan with five diagnostic/query
    inputs in every intake. Positive source rows remain separately scoped.
  snapshot_sha256: 12ff1f6bc3e96e74e3827fdd3260edfd94e8592fb38c9a44ae2d76c7c17f0344
- evidence_id: support-2569-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-assigned-source-reading-001.json
  locator: /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows;
    /cautions; /reading_method
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: 'Support personally read 13 assigned contexts: 117 saved frames, 77 positive
    row placements and 865 fields. Five selected owners contribute 45 frames, 16 rows
    and 206 fields; eight companion contexts and the one historical taxon-merge row
    remain separate. BGC owns the other 12 contexts; no new primary-literature verification
    is implied.'
  snapshot_sha256: 60df14839b7e23469bb003a9994659a6239147050e04c380cc5a8bac4650913e
- evidence_id: support-2569-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Joint notes retain disjoint BGC 48/Support 77/Native 0 positive-row reading
    attribution, original 458-placement/68-path input scope, and explicit retained-source
    and companion limits. This receipt does not establish subsequent intake or scientific
    outcomes.
  snapshot_sha256: ae7ed2670cc732e1a52b3f0e371766747f7c193f2a09d5949b4d2b876434275b
- evidence_id: support-2569-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-last-five-molecular-intake-reading-001.json
  locator: /records/3; /totals; /whole_table_reading_method; /warning_scope; /limits
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: 'Support personally read all ten complete saved forms: 376 atom rows and
    388 bond rows, with complete stereo, motif and comparison fields. Corresponding
    actual intake metadata and 226 captured input hashes/ownership declarations were
    verified; this is not whole-corpus scientific reading.'
  snapshot_sha256: 21725ff2a7ddc02e3ceba0f075eeac2128059e4bbbe700483778ae4e260cfa15
- evidence_id: support-2569-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/19
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve identifiers, names and
    synonyms only. They contain no explicit rank or lineage fields and do not prove
    ancestry, strain equivalence, native production or fresh taxonomy.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
- evidence_id: support-2569-taxonomy-query-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/source_taxa; /contexts/15/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/15/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Complete retained source taxon IDs and saved forward-merge/non-organism
    results; historical merge routes are distinct from current nomenclatural, rank
    or ancestry verification.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
- evidence_id: support-2569-raw-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-assigned-source-reading-001.json
  locator: /raw_reading; /selected_scope; /companion_scope
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: This assigned-reading receipt records complete selected owner/history reading
    and separately attributed companion reading. Historical source-access assertions
    remain record content, not fresh verification.
  snapshot_sha256: 60df14839b7e23469bb003a9994659a6239147050e04c380cc5a8bac4650913e
- evidence_id: support-2569-required-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/root-current257-five-gates-acceptance-001.json
  locator: /status; /verification; /unavailable_required_gates
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: ROOT accepts five local gate results; the required QC and OAK checks remain
    unavailable, so completion is partial.
  snapshot_sha256: 34ebd316312149ba3188bc13bb539d04f090a52a6dcb47ad863f22935fb412a2
- evidence_id: support-2569-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/native-prep/native-current257-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation; /routes
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Native complete cache and route interpretation remains attributed; owner-local
    retained stanzas carry only their exact saved fields.
  snapshot_sha256: 636261dde51ff78122931cea95307ef48dee471ff6960228cdcf3a3703c597b9
- evidence_id: support-2569-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/native-prep/native-current257-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: The bounded implemented-table scan found no applicable exact replacement
    for these owners; unrelated lexical hits are not imported as owner evidence.
  snapshot_sha256: 6cabd8e87111e27c4165f4878b4261750cc85f41fae3274ac6e2c12f553c3569
  search_scope: '{"selected_identifier": "naturalproductmech:mibig-5c75ae209a", "full_key":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "scope": "Eleven enumerated retained curation tables,
    nine implemented tables and exact predicates; ignored-file-independent inspection
    is bounded, not universal absence."}'
- evidence_id: support-2569-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope;
    /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Both canonical-SMILES comparisons are false; the direct map is empty. Normalized
    identifiers, formula and charge agree while amide/imidic representations differ.
  snapshot_sha256: fbf58f78222a543b93feb5c3f090ddbcb867368ea8c32af60aa5358729cbd873
- evidence_id: support-2569-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles; /records/8/inchi
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif tables retain representation-specific
    counts and stereochemical assignments; no new parse or natural-state claim.
  snapshot_sha256: fbf58f78222a543b93feb5c3f090ddbcb867368ea8c32af60aa5358729cbd873
- evidence_id: support-2569-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /limits
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: ROOT accepts the single original stored-form diagnostic and its saved results.
    Complete scientific table reading is separately attributed; normalization is not
    natural-identity proof.
  snapshot_sha256: a5145a914547b1c329af7e0f8b9560fd7360abda2c467a392be99f5943d5ff77
- evidence_id: support-2569-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Exact original diagnostic command/source, terminal exit and stream pins;
    no retry or external request.
  snapshot_sha256: baf44902960468bde86f8595568197176308fc32a4adc4f8cbda63e96716cfd5
- evidence_id: support-2569-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Six original omitted-undefined-stereo warnings remain global, without assignment
    to an owner or form.
  snapshot_sha256: 00cae42342553e75fe6b2a8688bd27c9af478f8adab3510c600a3d7845646a73
- evidence_id: support-2569-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2569-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2569-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2569-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2569-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/native-current257-coelimycin-p1-maintained-reader-DATA-001.json
  locator: /resolved_view; /returned_view_equals_expected_complete_owner; /counts;
    /errors; /unexpected_denials; /external_requests
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: The accepted single maintained-reader result preserves the complete owner,
    five graphs, 14 nodes, nine edges, 18 graph reference placements and three histories;
    technical preservation does not prove enzyme activity.
  snapshot_sha256: 720121270be4d108640401053ec7935e7da2f4dee38fe2b6ddc9ba601791eb9b
- evidence_id: support-2569-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/native-current257-coelimycin-p1-reader-execution-001.json
  locator: /exit_code; /command
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Genuine original maintained-reader execution exited zero; no retry or new
    experimental evidence.
  snapshot_sha256: 06113c675bc3efa36935b5eda40b1c42323a52705e8ddade0209a8a4d416a840
- evidence_id: support-2569-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch257/root-native-reader-2569-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /verification; /review_check_contract;
    /limits
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: ROOT accepts the exact complete-owner preservation result and supplies
    the required typed check contract; all scientific scope limits remain.
  snapshot_sha256: ff71799743c2ea1f0e9e23c9f927b5c9f28926b65011f1bd3cef1a2c0a5b04bb
- evidence_id: support-2569-reader-whole-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/support-prep/support-current257-coelimycin-maintained-view-reading-001.json
  locator: /reading; /equalities; /interpretation; /technical_scope
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Support personally read the entire unique maintained owner, all five graphs
    and 18 reference placements, and all three histories. Retained sequence and abstract-access
    assertions are not freshly accessed sources.
  snapshot_sha256: c7c25a8b2058f722eb4eb81764fb482256d8c8183cfe8b1ffc5873411cfaab07
- evidence_id: support-2569-graph-content
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch257/native-current257-coelimycin-p1-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs; /resolved_view/curation_history
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Three native-reference identity graphs and two genomic/chemical inference
    models retain exact identifiers, model keys, ungrounded intermediates and source
    qualifications. SCO6281 reaction remains withheld; no ordered pathway or P1/P2
    equivalence is added.
  snapshot_sha256: 720121270be4d108640401053ec7935e7da2f4dee38fe2b6ddc9ba601791eb9b
- evidence_id: support-2569-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/mibig_compounds",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: 'Complete retained physical row 50, all 25 fields: BGC0000038 version 5;
    Streptomyces coelicolor A3(2), producer BGC_CHARACTERIZED, locus CLUSTER_DEMONSTRATED;
    DOI:10.1039/c2sc20410j at COMPOUND_EVIDENCE scope. Source structure, methods and
    classes remain exact.'
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
- evidence_id: support-2569-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 50
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2569-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/chebi_structures",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved lotus_occurrences frame has 2 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: 'Complete retained physical row 7722, all 6 fields: Streptomyces albidoflavus
    (NCBITaxon:1886), DOI:10.1007/S00203-006-0176-7; occurrence is distinct from demonstrated
    production and independent-study corroboration.'
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
- evidence_id: support-2569-source-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/lotus_occurrences/matches/1
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: 'Complete retained physical row 7723, all 6 fields: Streptomyces coelicolor
    (NCBITaxon:1902), DOI:10.1007/S00203-006-0176-7; occurrence is distinct from demonstrated
    production and independent-study corroboration.'
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
- evidence_id: support-2569-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 7722, 7723
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2569-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; a zero is
    bounded to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; a zero is bounded to
    its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/npclassifier",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: 'Complete retained physical row 2110, all 7 fields: npclassifier.gnps2.org@2026-09-07:
    //; glycoside=false, model assertion only.'
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
- evidence_id: support-2569-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 2110
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2569-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; a zero
    is bounded to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "RHGMVWUZXGSXCT-HXNNLKDLSA-N", "saved_frame": "/contexts/15/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2569-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch257-tentative/bgc-prep/bgc-conditional257-source-inventory-DATA-001.json
  locator: /contexts/15/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T14:45:46.021750Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 689c48cecc300e6fbb2a93fdcc7576a908a17686a9779045ffd7c2f6d4fbb4d2
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/15/source_scope_inventory/joins/chebi_origins",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-257/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json
  accessed_at: '2026-11-05T13:50:39.034423Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 503597387d902c7f79f9313e200f520c56ae727eb7ce2c6cc825354f7053d290
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-257/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json
  accessed_at: '2026-11-05T13:51:04.666477Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: cf33edcfa05280db5aebd33d81c88dd91ca66c9c5b034ca968fcd9008fe90509
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-257/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json
  accessed_at: '2026-11-05T13:51:24.877740Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-257/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json
  accessed_at: '2026-11-05T13:51:59.839077Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-257/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-257/native-current257-five-gates-execution-001.json
  accessed_at: '2026-11-05T13:52:11.986151Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 2b3f35823db2a4e15ff98223af70c16bf27341d152bd8f83df90f8c8e3fc9b2c
assessments:
- area: identity
  topic: Retained identity and grounding scope
  outcome: supported
  summary: The retained MINTED owner naturalproductmech:mibig-5c75ae209a preserves
    the complete key RHGMVWUZXGSXCT-HXNNLKDLSA-N, its MIBiG structure and source label.
    Both saved forms reproduce the declared Standard InChI and full key. The exact
    retained ChEBI structure frame is empty; this bounds the stored grounding rationale
    without a fresh authority search. Name, shared locus and connectivity-block similarity
    are not substituted for exact owner identity.
  assessment_id: support-2569-identity
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-grounding-owner
  - support-2569-chemistry
  - support-2569-topology
  - support-2569-direct-contexts
  - support-2569-source-reading
  - support-2569-query-chebi_structures
  - support-2569-source-mibig_compounds-0
  - support-2569-graph-content
  - support-2569-reader-DATA
  - support-2569-reader-acceptance
  - support-2569-reader-whole-reading
  dimensions:
  - name: standard_inchi_key
    value: RHGMVWUZXGSXCT-HXNNLKDLSA-N
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2569-grounding-owner
    - support-2569-chemistry
    - support-2569-topology
    - support-2569-direct-contexts
    - support-2569-source-reading
    - support-2569-query-chebi_structures
    - support-2569-source-mibig_compounds-0
    - support-2569-graph-content
    - support-2569-reader-DATA
    - support-2569-reader-acceptance
    - support-2569-reader-whole-reading
  - name: grounding_scope
    value: Retained MINTED MIBiG identity; exact ChEBI frame empty; natural identity
      not independently established.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2569-grounding-owner
    - support-2569-chemistry
    - support-2569-topology
    - support-2569-direct-contexts
    - support-2569-source-reading
    - support-2569-query-chebi_structures
    - support-2569-source-mibig_compounds-0
    - support-2569-graph-content
    - support-2569-reader-DATA
    - support-2569-reader-acceptance
    - support-2569-reader-whole-reading
- area: representation
  topic: Stored representations and stereochemistry
  outcome: supported
  summary: Both forms retain neutral C17H20N2O4S and the declared normalized identifiers,
    but canonical strings differ and the direct map is empty. The N-acetyl amide becomes
    an imidic site; the ketone and ester remain. One tetrahedral center is unspecified
    and three double bonds are specified, consistent with the stored incomplete flag.
    The extra imidic geometry is representation-specific. The eight-member sulfur/ester-containing
    ring and separate unsaturated nitrogen ring do not validate the inferred enzyme
    models.
  assessment_id: support-2569-representation
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-grounding-owner
  - support-2569-chemistry
  - support-2569-topology
  - support-2569-molecular-reading
  - support-2569-diagnostic-acceptance
  - support-2569-structure-schema
  - support-2569-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: 'SMILES tetrahedral: 0 specified, 1 unspecified; stereo_complete=False.'
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2569-grounding-owner
    - support-2569-chemistry
    - support-2569-topology
    - support-2569-molecular-reading
    - support-2569-diagnostic-acceptance
    - support-2569-structure-schema
    - support-2569-stereo-method
  - name: representation_correspondence
    value: Canonical pair unequal; amide/imidic difference; empty direct map; normalized
      key/formula/charge agree.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2569-grounding-owner
    - support-2569-chemistry
    - support-2569-topology
    - support-2569-molecular-reading
    - support-2569-diagnostic-acceptance
    - support-2569-structure-schema
    - support-2569-stereo-method
- area: provenance
  topic: Producer, locus and taxonomy scope
  outcome: supported
  summary: BGC0000038 version 5 retains Streptomyces coelicolor A3(2) at NCBITaxon:100226
    as BGC_CHARACTERIZED and AL645882.2:6890528..6948414 as CLUSTER_DEMONSTRATED with
    knock-out studies. These are retained source grades; present local review does
    not independently repeat or verify those experiments. Cached identifiers, names
    and synonyms do not newly verify rank, ancestry or strain equivalence.
  assessment_id: support-2569-provenance
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-origin-owner
  - support-2569-source-reading
  - support-2569-direct-contexts
  - support-2569-cached-taxonomy
  - support-2569-taxonomy-query-routes
  - support-2569-taxonomy-reading
  - support-2569-curation-scope
  - support-2569-source-mibig_compounds-0
  - support-2569-source-lotus_occurrences-0
  - support-2569-source-lotus_occurrences-1
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:100226; NCBITaxon:1886; NCBITaxon:1902; retained naming only,
      no verified rank/ancestry/strain equivalence.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2569-origin-owner
    - support-2569-source-reading
    - support-2569-direct-contexts
    - support-2569-cached-taxonomy
    - support-2569-taxonomy-query-routes
    - support-2569-taxonomy-reading
    - support-2569-curation-scope
    - support-2569-source-mibig_compounds-0
    - support-2569-source-lotus_occurrences-0
    - support-2569-source-lotus_occurrences-1
  - name: producer_evidence
    value: 'Streptomyces coelicolor A3(2): BGC_CHARACTERIZED'
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2569-origin-owner
    - support-2569-source-reading
    - support-2569-direct-contexts
    - support-2569-cached-taxonomy
    - support-2569-taxonomy-query-routes
    - support-2569-taxonomy-reading
    - support-2569-curation-scope
    - support-2569-source-mibig_compounds-0
    - support-2569-source-lotus_occurrences-0
    - support-2569-source-lotus_occurrences-1
  - name: locus_evidence
    value: 'BGC0000038: CLUSTER_DEMONSTRATED'
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2569-origin-owner
    - support-2569-source-reading
    - support-2569-direct-contexts
    - support-2569-cached-taxonomy
    - support-2569-taxonomy-query-routes
    - support-2569-taxonomy-reading
    - support-2569-curation-scope
    - support-2569-source-mibig_compounds-0
    - support-2569-source-lotus_occurrences-0
    - support-2569-source-lotus_occurrences-1
- area: evidence
  topic: Citation categories and source access
  outcome: supported
  summary: DOI:10.1039/c2sc20410j has exact COMPOUND_EVIDENCE scope. The two LOTUS
    occurrence rows cite DOI:10.1007/S00203-006-0176-7. Historical sequence/structure
    access, abstract-only coverage and 403 responses are record content unless original
    source bytes are actually retained and read now.
  assessment_id: support-2569-citations
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-owner
  - support-2569-raw-reading
  - support-2569-origin-owner
  - support-2569-occurrence-activity-owner
  - support-2569-source-reading
  - support-2569-direct-contexts
  - support-2569-source-mibig_compounds-0
  - support-2569-source-lotus_occurrences-0
  - support-2569-source-lotus_occurrences-1
  - support-2569-source-npclassifier-0
  - support-2569-graph-content
  - support-2569-reader-DATA
  - support-2569-reader-acceptance
  - support-2569-reader-whole-reading
  dimensions:
  - name: citation_scope
    value: DOI:10.1039/c2sc20410j [COMPOUND_EVIDENCE]; retained rows, no fresh primary-source
      access.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2569-owner
    - support-2569-raw-reading
    - support-2569-origin-owner
    - support-2569-occurrence-activity-owner
    - support-2569-source-reading
    - support-2569-direct-contexts
    - support-2569-source-mibig_compounds-0
    - support-2569-source-lotus_occurrences-0
    - support-2569-source-lotus_occurrences-1
    - support-2569-source-npclassifier-0
    - support-2569-graph-content
    - support-2569-reader-DATA
    - support-2569-reader-acceptance
    - support-2569-reader-whole-reading
- area: evidence
  topic: Occurrence, activity and companion boundaries
  outcome: supported
  summary: LOTUS taxon 1886 albidoflavus and 1902 coelicolor naming assertions remain
    distinct from the selected strain 100226. Exact saved assay/target query frames
    are empty.
  assessment_id: support-2569-occurrence
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-occurrence-activity-owner
  - support-2569-direct-contexts
  - support-2569-cached-taxonomy
  - support-2569-taxonomy-query-routes
  - support-2569-taxonomy-reading
  - support-2569-curation-scope
  - support-2569-source-reading
  - support-2569-query-lotus_occurrences
  - support-2569-query-chebi_origins
  - support-2569-query-cyanometdb_occurrences
  - support-2569-query-pubchem_bioassay
  - support-2569-query-bindingdb_targets
  - support-2569-query-antibioticmech_inchikeys
  - support-2569-source-lotus_occurrences-0
  - support-2569-source-lotus_occurrences-1
  dimensions:
  - name: occurrence_scope
    value: 2 selected LOTUS rows; occurrence is distinct from production.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2569-occurrence-activity-owner
    - support-2569-direct-contexts
    - support-2569-cached-taxonomy
    - support-2569-taxonomy-query-routes
    - support-2569-taxonomy-reading
    - support-2569-curation-scope
    - support-2569-source-reading
    - support-2569-query-lotus_occurrences
    - support-2569-query-chebi_origins
    - support-2569-query-cyanometdb_occurrences
    - support-2569-query-pubchem_bioassay
    - support-2569-query-bindingdb_targets
    - support-2569-query-antibioticmech_inchikeys
    - support-2569-source-lotus_occurrences-0
    - support-2569-source-lotus_occurrences-1
  - name: assay_target_scope
    value: 'Selected scope: 0 actual AID rows, 0 blank-AID sentinels; companion activity
      does not transfer.'
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2569-occurrence-activity-owner
    - support-2569-direct-contexts
    - support-2569-cached-taxonomy
    - support-2569-taxonomy-query-routes
    - support-2569-taxonomy-reading
    - support-2569-curation-scope
    - support-2569-source-reading
    - support-2569-query-lotus_occurrences
    - support-2569-query-chebi_origins
    - support-2569-query-cyanometdb_occurrences
    - support-2569-query-pubchem_bioassay
    - support-2569-query-bindingdb_targets
    - support-2569-query-antibioticmech_inchikeys
    - support-2569-source-lotus_occurrences-0
    - support-2569-source-lotus_occurrences-1
- area: consistency
  topic: Computed classification applicability
  outcome: not_applicable
  summary: All three computed classification axes are empty. The source PKS class
    is distinct from the sulfur/ester-containing ring and nitrogen-ring topology.
    The five graphs contain no ordered pathway and do not fill a missing classification
    result or prove a complete biosynthetic route to this owner.
  assessment_id: support-2569-classification
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-classification-owner
  - support-2569-chemistry
  - support-2569-topology
  - support-2569-classification-seeder
  - support-2569-source-reading
  - support-2569-source-mibig_compounds-0
  - support-2569-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: Computed axes empty; source PKS and inferred graphs do not fill classification
      or complete a pathway.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2569-classification-owner
    - support-2569-chemistry
    - support-2569-topology
    - support-2569-classification-seeder
    - support-2569-source-reading
    - support-2569-source-mibig_compounds-0
    - support-2569-source-npclassifier-0
- area: graph
  topic: Native-reference and inferred reaction graphs
  outcome: supported
  summary: 'The complete maintained view preserves three native-reference graphs for
    Q9EX55, Q93S10 and Q93S08 and two explicitly inferred MITE reaction graphs. Reference-sequence
    mappings do not prove expression, processed constructs, cofactor use or individual
    enzyme activity. SCO6279’s modeled product and SCO6272’s substrate share a connectivity
    block but have different full-key suffixes, so no inter-graph reaction order is
    established. SCO6281’s reaction remains withheld under retained issue 695: C12H19NO3
    to C12H17NO3 retains the oxygen count despite the historical monooxygenation label.
    Ungrounded intermediates, incomplete model stereochemistry and historical abstract-only
    access remain explicit; no exact P1 product edge, P1/P2 equivalence or complete
    pathway is asserted.'
  assessment_id: support-2569-mechanism
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-capture
  - support-2569-graph-content
  - support-2569-reader-DATA
  - support-2569-reader-execution
  - support-2569-reader-acceptance
  - support-2569-reader-whole-reading
  - support-2569-source-reading
  - support-2569-source-mibig_compounds-0
  dimensions: []
- area: completeness
  topic: Evidence coverage and review completion
  outcome: unknown
  summary: The retained identity, source grades and local chemistry are reviewable
    within the stated limits. Required full QC and OAK coverage remain unavailable,
    and primary publications and fresh authorities were not accessed. Completion is
    partial; no unambiguous source defect requiring a record edit was established.
  assessment_id: support-2569-completion
  target_ids:
  - naturalproductmech:mibig-5c75ae209a
  evidence_ids:
  - support-2569-owner
  - support-2569-capture
  - support-2569-intake
  - support-2569-intake-acceptance
  - support-2569-intake-reading
  - support-2569-inventory-acceptance
  - support-2569-plan
  - support-2569-plan-acceptance
  - support-2569-source-reading
  - support-2569-source-notes
  - support-2569-molecular-reading
  - support-2569-diagnostic-acceptance
  - support-2569-diagnostic-execution
  - support-2569-diagnostic-stderr
  - support-2569-required-gates
  - support-2569-review-profile
  - support-2569-graph-content
  - support-2569-reader-DATA
  - support-2569-reader-acceptance
  - support-2569-reader-whole-reading
  dimensions:
  - name: review_completion
    value: Partial; full QC/OAK and fresh primary-source verification unavailable.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2569-owner
    - support-2569-capture
    - support-2569-intake
    - support-2569-intake-acceptance
    - support-2569-intake-reading
    - support-2569-inventory-acceptance
    - support-2569-plan
    - support-2569-plan-acceptance
    - support-2569-source-reading
    - support-2569-source-notes
    - support-2569-molecular-reading
    - support-2569-diagnostic-acceptance
    - support-2569-diagnostic-execution
    - support-2569-diagnostic-stderr
    - support-2569-required-gates
    - support-2569-review-profile
    - support-2569-graph-content
    - support-2569-reader-DATA
    - support-2569-reader-acceptance
    - support-2569-reader-whole-reading
findings: []
actions: []
limitations:
- Retained local evidence only; no newly inspected original publications, sequence
  databases, fresh taxonomy or independent natural-identity verification.
- Normalized identifiers, canonical comparisons and substructure mappings have separate
  scopes. Six global undefined-stereo warnings remain unassigned to individual forms
  or owners.
- Required full QC and OAK coverage remain unavailable. No source record, native status
  or history was edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete owner/history and saved molecular-table readings are distinct from verification
  of captured input hashes and ownership declarations. Input capture does not claim
  scientific reading of entire underlying corpus tables.
- 'Assigned retained-source reading covers 13 contexts: 117 saved query frames, 77
  positive row placements and 865 fields. The five selected owners account for 45
  frames, 16 rows and 206 fields; eight companions remain separately attributed.'
- No source query, molecular parse or maintained-reader replay was performed in authoring
  these assessments.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-257
```
