# Local evidence review: bombyxamycin A

- Review: 20261105T092954Z-bombyxamycin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T08:20:00.292824Z
- Finished UTC: 2026-11-05T09:29:54.077808Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Bombyxamycin A is retained as a macrocyclic lactam encoding with two specified atom centers but two unspecified double-bond geometries. The true stereo_complete flag is compatible with its implemented atom-center scope; it does not establish all bond geometry.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2532; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-05a2069b99 | data/natural_products/unclassified/bombyxamycin-a.yaml | generated | bombyxamycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-05a2069b99 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-05a2069b99 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-05a2069b99 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-05a2069b99 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-05a2069b99 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-05a2069b99 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-05a2069b99 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-05a2069b99 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-05a2069b99.

The minted identifier naturalproductmech:mibig-05a2069b99, full key NCLKPTJQVKBQEN-YBNREDKZSA-N, formula C27H33NO3 and NPAtlas NPA026755 are mutually retained record assertions. Direct companion Bombyxamycin B has formula C27H31NO5, a different full key and different oxygenated ring topology. Their shared BGC0002376 does not establish identity or permit stereochemistry, activity or mechanistic transfer. The statement that no qualifying ChEBI entry shared the structure remains a historical grounding result, not an exhaustive current authority search.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-05a2069b99.

The two tetrahedral centers are specified in both forms and no unspecified tetrahedral center is reported. Seven of the nine original C=C bonds are specified (three E and four Z), while two are unspecified; the literal InChI /b15-11? and /b23-19? layers refer to those bond geometries. The InChI-derived imidic form adds another unspecified potential C=N geometry. The maintained extractor computes stereo_complete from FindMolChiralCenters with includeUnassigned=True and useLegacyImplementation=False; the true flag therefore does not contradict these unresolved double bonds. This review does not upgrade the record to a fully stereochemically proven natural isolate.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-05a2069b99.

MIBiG BGC0002376 version 2 reports a BGC_CHARACTERIZED producer assertion for Streptomyces sp. (NCBITaxon:1931) and a distinct CLUSTER_DEMONSTRATED locus link at MK433001.1 positions 1–113079. The methods are knock-out studies and gene expression correlated with compound production. The source PKS category and those locus methods do not specify a complete reaction pathway or prove each protein function. LOTUS uses Streptomyces taxon 1883 at genus scope; it must not be collapsed into the unspecified-strain producer label. Saved cache names and synonyms add no independent rank, strain or production verification.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-05a2069b99.

The retained MIBiG reference basis is COMPOUND_EVIDENCE for DOI:10.1021/acs.orglett.9b00384. LOTUS repeats that DOI with uppercase letters; these are not independent publications. Both seeding history events remain explicit. Source database assertions and the historical grounding note are not fresh primary-paper or ChEBI checks.

### Source-specific occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-05a2069b99.

The single retained LOTUS row asserts occurrence at Streptomyces genus scope and shares the compound-evidence DOI used by MIBiG. It does not independently establish biosynthetic production by a particular strain. The direct Bombyxamycin B context remains a different encoded compound, so no measurements or mechanistic conclusions are imported from it.

### Reported model families and qualified applicability

consistency: supported. Targets: naturalproductmech:mibig-05a2069b99.

The named NPClassifier output reports Amino acids and Peptides and Polyketides, superclass Macrolides and class Macrolide lactams, with is_glycoside false. The 26-membered lactam topology is compatible with the class label and lacks a detected sugar-ring motif. The mixed computed pathways explain UNCLASSIFIED filing under the maintained rule; they do not override the separate MIBiG PKS category or establish a mixed biosynthetic mechanism.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-05a2069b99.

The complete raw owner/history, accepted canonical intake and retained source frames were read, together with both complete saved molecular forms. No mechanism root applies to a maintained-reader check for this owner. The review remains partial because external authority/publication verification and full QC/OAK are unavailable; native status, source content and open issues are unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2532-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/bombyxamycin-a.yaml; Complete plaintext including every curation_history entry | supports | Complete bombyxamycin A owner and 2 history events; earlier whole reading carries by current identical bytes. |
| bgc-2532-capture | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2532-intake | /private/tmp/npm-review-work/shared-next-batch254/intakes/2532-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, maintained ownership and all 38 input placements joined to the accepted plan and current hashes. |
| bgc-2532-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch254/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/1 | supports | ROOT accepted this original canonical intake and its exact plan, inspection and receipt pins. |
| bgc-2532-grounding-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/label; /records/1/owner_document/chemical_structure; /records/1/owner_document/xrefs; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status; /records/1/owner_document/grounding_notes | supports | Exact retained identifier, structure, cross-references where present, source concepts and grounding fields. Historical annotations do not constitute a fresh authority lookup. |
| bgc-2532-origin-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups; /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, coordinates where declared and citation tiers. |
| bgc-2532-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete owner supplies retained occurrences, definitions and all bioactivities where present, with their source-specific fields and notes. Missing observations are not biological inactivity. |
| bgc-2532-classification-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing and separate source categories; applicability is assessed separately. |
| bgc-2532-history-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1/owner_document/curation_status; /records/1/owner_document/curation_history | supports | Complete history and status; seeding and historical curation do not imply new primary verification. |
| bgc-2532-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/1/owner_document | supports | The complete owner has no graph, graph-reference, component, pathway, molecular-target or bioactivity root. No maintained reader applies; bounded root absence is not inactivity. |
| bgc-2532-chemistry | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/formula; /records/1/smiles/computed/formal_charge; /records/1/smiles/computed/standard_inchi; /records/1/smiles/computed/standard_inchi_key; /records/1/smiles/computed/canonical_isomeric_smiles; /records/1/smiles/computed/canonical_nonisomeric_smiles; /records/1/smiles/computed/atom_count; /records/1/smiles/computed/heavy_atom_count; /records/1/smiles/computed/bond_count; /records/1/smiles/computed/element_counts; /records/1/smiles/computed/stereo_counts; /records/1/inchi/computed/formula; /records/1/inchi/computed/formal_charge; /records/1/inchi/computed/standard_inchi; /records/1/inchi/computed/standard_inchi_key; /records/1/inchi/computed/canonical_isomeric_smiles; /records/1/inchi/computed/canonical_nonisomeric_smiles; /records/1/inchi/computed/atom_count; /records/1/inchi/computed/heavy_atom_count; /records/1/inchi/computed/bond_count; /records/1/inchi/computed/element_counts; /records/1/inchi/computed/stereo_counts | supports | Both forms give the declared normalized InChI/full key, formula C27H33NO3, charge zero, 31 atoms and 31 bonds. Eight comparisons are true; both canonical SMILES comparisons are false. The SMILES amide C23(=O24)-N22 is represented as C26(OH30)=N27 in the InChI-derived form. The direct atom map is empty and full_graph_identity_established is false; normalized agreement supports the retained encoding at its stated scope without proving full graph or natural identity. |
| bgc-2532-topology | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds; /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo; /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices; /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings; /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs; /records/1/inchi/computed/fragment_atom_indices | supports | The saved cycle basis is a single 26-membered macrocycle. The SMILES form contains one lactam carbonyl, a separate ketone and one hydroxyl; the InChI-derived form changes the lactam to an imidic-acid site while retaining the other oxygen functions. No ester, carbon–oxygen–carbon bridge or saturated C5O sugar-ring candidate is reported. The actual topology supports a qualified macrolactam description, not a complete biosynthetic route. |
| bgc-2532-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-current254-first-five-molecular-intake-reading-001.json; /records/1; /counts; /reading_scope; /intake_reading; /source_reading; /limits | supports | BGC complete saved first-five molecular and intake reading, with exact per-form table counts and reading attribution; no new parse. |
| bgc-2532-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /readback; /admission; /actual_intake_acceptance; /operator; /delegated_by; /original_terminal; /verification; /ROOT_readings; /limits; /external_requests | supports | ROOT accepted the original twenty stored-form diagnostics. Global warning interpretation and method limits remain explicit; no per-record warning assignment is inferred. |
| bgc-2532-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins. |
| bgc-2532-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | Structure stereochemistry and named/versioned computed classification have distinct evidence scopes. |
| bgc-2532-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The maintained stereo_complete calculation uses unassigned molecular chiral centers; it is not a count of literal question marks in InChI. Atom type and double-bond geometry require separate interpretation. |
| bgc-2532-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while exact model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2532-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 126–145; 1318–1382 | supports | Deposited calls, endpoints and values retain their source scope. Activity classes derived from active assay titles do not independently prove mechanisms or direct binding. |
| bgc-2532-source-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-current254-assigned-source-reading-001.json; /primary_scope; /contexts; /raw_history_carries; /whole_reading_terminals; /remaining_attribution; /verification | supports | BGC wholly read contexts 0–6: two unselected companions and the selected first five, totaling 63 frames, 23 rows and 316 fields. The selected five account for 16 rows and 215 fields; seven companion rows add no selected coverage or transferred activity. These are retained database-row readings, not newly inspected primary publications. |
| bgc-2532-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete retained-source reading covers 108 frames, 39 rows and 512 fields: BGC 23 rows and Support 16 rows. Native taxonomy/curation has zero positive-source-row credit; overlapping readings add no disjoint row credit. |
| bgc-2532-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch254/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope | supports | One original composer produced the accepted plan at 388 placements across 50 paths, with exact source notes and attributed reading receipts. This fragment consumes saved results only. |
| bgc-2532-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch254/root-current254-source-plan-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /plan; /derivation; /execution; /original_tools; /admission; /source; /notes; /inventory; /inventory_acceptance; /source_reading_scope; /verification; /ROOT_readings; /limits; /external_requests | supports | ROOT accepted the exact 388-placement/50-path source plan and original results; no query or input expansion is inferred. |
| bgc-2532-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch254/root-current254-five-gates-acceptance-001.json; /status; /verification; /all_native_gates_passed; /unavailable_required_gates; /execution | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed remains false. Technical checks do not complete scientific verification. |
| bgc-2532-curation-scope | /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | The bounded ignored-inclusive Native scan found 27 lexical rows and zero exact applicable implemented corrections or exclusions. All six applicability flags on those rows are false. No actual AID or blank-AID sentinel occurs in the complete current inventory; this does not imply biological inactivity. |
| bgc-2532-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/0; /cached_taxonomy/whole_stanzas/1 | supports | Complete saved cache names and synonyms for this owner’s source IDs; no independent taxonomic rank, strain, occurrence or producer validation. |
| bgc-2532-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/source_taxa; /contexts/3/source_scope_inventory/forward_taxon_merge_matches; /contexts/3/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh taxonomy request. |
| bgc-2532-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /routes; /interpretation | supports | Native read all nine whole retained stanzas and twelve routes, with no unmatched, forward-merge or nonorganism entry in this exact scope. Source labels, cached names and synonyms do not establish strain equivalence, taxonomic rank or biological production. |
| bgc-2532-direct-contexts | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-target-input-plan-001.json; /records/1/proposed_companion_paths; /records/1/direct_companion_predicates | supports | Exact immediate owned-BGC context inputs; shared locus/citation is not identity, stereochemistry, assay or mechanism transfer. No transitive or name-based expansion. |
| bgc-2532-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/4/path; /contexts/4/identifier; /contexts/4/label; /contexts/4/standard_inchi_key; /contexts/4/complete_raw_text; /contexts/4/complete_raw_history; /contexts/4/source_scope_inventory | supports | Complete directly linked companion encodings, histories and saved source frames, each with its own exact structure, source identifiers and grades. Shared owned BGC links define bounded context; no identity, activity, stereochemistry, evidence-grade or selected coverage transfer follows. |
| bgc-2532-raw-reading-carry | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-first-five-whole-reading-001.json; /observer; /recorded_at; /status; /conditional_membership; /preview_basis; /original_tools; /reading_attribution; /records; /totals; /qualified_scope_notes; /limits; /actual254_authorities; /external_requests; /target_invocations | supports | BGC personally read the five selected first-half owners and their complete histories. This pinned receipt is carried only by exact current byte equality; it does not claim other readers or companion coverage. |
| bgc-2532-companion-reading-carry | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-current254-two-companion-whole-reading-001.json; /observer; /recorded_at; /status; /census; /owners; /scope; /bounded_cautions; /raw_bytes; /raw_lines; /history_entries; /selected_review_credit; /retained_source_row_credit; /scientific_verdicts; /external_requests; /target_invocations | supports | BGC personally read both unselected immediate companion owners, Bolagladin A and Brasiliamide I, including complete histories. This receipt supplies bounded raw context only, without selected coverage or identity, stereochemistry or assay transfer. |
| bgc-2532-support-raw-reading-carry | /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-last-five-whole-owner-reading-001.json; /observer; /recorded_at; /status; /membership_freeze; /records; /scope; /boundaries; /target_invocations; /external_requests | supports | Support personally read the five selected last-half owners and complete histories, including Brasiliamide D. This attributed receipt supplies current raw context without transferring identity, assays or selected review coverage. |
| bgc-2532-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2532-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2925–2925; row_sha256 10c834e40153988212da883c59e598a9c06e93283be9bd8ac859f6704f173d0f | supports | Exact retained compound/version, structure/key, xrefs, producer/locus grades and citation tiers. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2532-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2532-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2532-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 5841–5841; row_sha256 4bcb6a960081ea07562de14b2f59592cfca611eb1534216947630a0d8848a8cf | supports | Exact organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2532-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2532-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2532-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1576–1576; row_sha256 01d9ef2e5b348443aa8388bf21d29c47d7ce216641c19f0fc8b5535399188aa1 | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability remains separate. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2532-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2532-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2532-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2532-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/3/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 row placements, exact predicate/query and all fields. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-254/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-254/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-254/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-254/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-254/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Only retained local records, database rows, historical annotations and accepted offline outputs were inspected; no fresh publication, authority, protein sequence, construct or experimental verification was performed.
- Full QC and OAK were unavailable, all_native_gates_passed remains false, and this review is partial.
- The six diagnostic warnings are global and are not assigned to individual records. No additional molecular parsing was performed.
- Two original double-bond geometries remain unspecified despite the atom-center completeness flag; no full atom map or independent natural-identity verification is available.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five saved molecular forms (372 atom rows and 384 bond rows) and 196 actual intake placements across 46 paths, without new parsing.
- Disjoint retained-source reading: BGC first-five selected plus two companions, 63 frames/23 rows/316 fields; Support last-five selected, 45 frames/16 rows/196 fields. Native cache/curation receives zero positive-source-row credit.
- BGC operated original collector/composer; Support operated canonical intakes; Native operated the diagnostic and Bolagladin B maintained reader under ROOT delegation. Only order 2531 requires a reader in this fragment scope. These fragments consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T092954Z-bombyxamycin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: bombyxamycin A'
started_at: '2026-11-05T08:20:00.292824Z'
finished_at: '2026-11-05T09:29:54.077808Z'
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
summary: Bombyxamycin A is retained as a macrocyclic lactam encoding with two specified
  atom centers but two unspecified double-bond geometries. The true stereo_complete
  flag is compatible with its implemented atom-center scope; it does not establish
  all bond geometry.
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
  - path: data/natural_products/unclassified/bombyxamycin-a.yaml
    sha256: ba70c7ea87940fb01fdf0d33b4eaa336c6696bdd1c4167bd08690ae90b1626ec
    role: target
  - path: data/natural_products/unclassified/bombyxamycin-b.yaml
    sha256: ed6a7ec2112fe25b7da50a9b1af5d7ec4ba9eaf4b64fd8cd32916d0f14490f90
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
  selection: Campaign path order 2532; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-05a2069b99
targets:
- target_id: naturalproductmech:mibig-05a2069b99
  path: data/natural_products/unclassified/bombyxamycin-a.yaml
  label: bombyxamycin A
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
  - naturalproductmech:mibig-05a2069b99
  command: just validate-strict data/natural_products/unclassified/bolagladin-b.yaml
    data/natural_products/unclassified/bombyxamycin-a.yaml data/natural_products/unclassified/bombyxamycin-b.yaml
    data/natural_products/unclassified/brasiliamide-a.yaml data/natural_products/unclassified/brasiliamide-b.yaml
    data/natural_products/unclassified/brasiliamide-d.yaml data/natural_products/unclassified/burkholdac-a.yaml
    data/natural_products/unclassified/burkholdac-b.yaml data/natural_products/unclassified/burnettramic-acid-a.yaml
    data/natural_products/unclassified/caboxamycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-254/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-05a2069b99
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-254/validate-all-001.tsv
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
  - naturalproductmech:mibig-05a2069b99
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
  - naturalproductmech:mibig-05a2069b99
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
  - naturalproductmech:mibig-05a2069b99
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-254/review-queue-001.tsv
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
  - naturalproductmech:mibig-05a2069b99
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2532-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/bombyxamycin-a.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Complete bombyxamycin A owner and 2 history events; earlier whole reading
    carries by current identical bytes.
  snapshot_sha256: ba70c7ea87940fb01fdf0d33b4eaa336c6696bdd1c4167bd08690ae90b1626ec
- evidence_id: bgc-2532-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/intakes/2532-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Actual canonical target, maintained ownership and all 38 input placements
    joined to the accepted plan and current hashes.
  snapshot_sha256: bce4762fce897eec6318ae41582635c99d6ed5c627c257bf62dbd9e7e83716c8
- evidence_id: bgc-2532-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/1
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: ROOT accepted this original canonical intake and its exact plan, inspection
    and receipt pins.
  snapshot_sha256: 3d01634e3cce9bed07e36a8432d302136d52eccdbb824359475ecf6f1212fe4a
- evidence_id: bgc-2532-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/label;
    /records/1/owner_document/chemical_structure; /records/1/owner_document/xrefs;
    /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status;
    /records/1/owner_document/grounding_notes
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact retained identifier, structure, cross-references where present, source
    concepts and grounding fields. Historical annotations do not constitute a fresh
    authority lookup.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups;
    /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, coordinates
    where declared and citation tiers.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Complete owner supplies retained occurrences, definitions and all bioactivities
    where present, with their source-specific fields and notes. Missing observations
    are not biological inactivity.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing and separate
    source categories; applicability is assessed separately.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1/owner_document/curation_status; /records/1/owner_document/curation_history
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Complete history and status; seeding and historical curation do not imply
    new primary verification.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: The complete owner has no graph, graph-reference, component, pathway, molecular-target
    or bioactivity root. No maintained reader applies; bounded root absence is not
    inactivity.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: bgc-2532-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/smiles/computed/formula; /records/1/smiles/computed/formal_charge;
    /records/1/smiles/computed/standard_inchi; /records/1/smiles/computed/standard_inchi_key;
    /records/1/smiles/computed/canonical_isomeric_smiles; /records/1/smiles/computed/canonical_nonisomeric_smiles;
    /records/1/smiles/computed/atom_count; /records/1/smiles/computed/heavy_atom_count;
    /records/1/smiles/computed/bond_count; /records/1/smiles/computed/element_counts;
    /records/1/smiles/computed/stereo_counts; /records/1/inchi/computed/formula; /records/1/inchi/computed/formal_charge;
    /records/1/inchi/computed/standard_inchi; /records/1/inchi/computed/standard_inchi_key;
    /records/1/inchi/computed/canonical_isomeric_smiles; /records/1/inchi/computed/canonical_nonisomeric_smiles;
    /records/1/inchi/computed/atom_count; /records/1/inchi/computed/heavy_atom_count;
    /records/1/inchi/computed/bond_count; /records/1/inchi/computed/element_counts;
    /records/1/inchi/computed/stereo_counts
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Both forms give the declared normalized InChI/full key, formula C27H33NO3,
    charge zero, 31 atoms and 31 bonds. Eight comparisons are true; both canonical
    SMILES comparisons are false. The SMILES amide C23(=O24)-N22 is represented as
    C26(OH30)=N27 in the InChI-derived form. The direct atom map is empty and full_graph_identity_established
    is false; normalized agreement supports the retained encoding at its stated scope
    without proving full graph or natural identity.
  snapshot_sha256: 6d253472dfe91844e124611b6d35a253691ac62122bafe126fd25c6a10abc9e5
- evidence_id: bgc-2532-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds;
    /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo;
    /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices;
    /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings;
    /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs;
    /records/1/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: The saved cycle basis is a single 26-membered macrocycle. The SMILES form
    contains one lactam carbonyl, a separate ketone and one hydroxyl; the InChI-derived
    form changes the lactam to an imidic-acid site while retaining the other oxygen
    functions. No ester, carbon–oxygen–carbon bridge or saturated C5O sugar-ring candidate
    is reported. The actual topology supports a qualified macrolactam description,
    not a complete biosynthetic route.
  snapshot_sha256: 6d253472dfe91844e124611b6d35a253691ac62122bafe126fd25c6a10abc9e5
- evidence_id: bgc-2532-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-current254-first-five-molecular-intake-reading-001.json
  locator: /records/1; /counts; /reading_scope; /intake_reading; /source_reading;
    /limits
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: BGC complete saved first-five molecular and intake reading, with exact
    per-form table counts and reading attribution; no new parse.
  snapshot_sha256: e4aa03629647f69ed20b80849e7384dfea32b31e914c8e9111a76e60e8b0e177
- evidence_id: bgc-2532-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /readback; /admission; /actual_intake_acceptance; /operator; /delegated_by; /original_terminal;
    /verification; /ROOT_readings; /limits; /external_requests
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostics. Global warning
    interpretation and method limits remain explicit; no per-record warning assignment
    is inferred.
  snapshot_sha256: 79eaee81115f631249c5c505fd5c06b17e54a99cf34d9887c4a841fdcfba8f0d
- evidence_id: bgc-2532-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins.
  snapshot_sha256: bccd14404151f3fca2e384b55178c2eadc18bc707e81a6ee87b54875428e321b
- evidence_id: bgc-2532-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Structure stereochemistry and named/versioned computed classification have
    distinct evidence scopes.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2532-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: The maintained stereo_complete calculation uses unassigned molecular chiral
    centers; it is not a count of literal question marks in InChI. Atom type and double-bond
    geometry require separate interpretation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2532-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while exact model
    arrays remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2532-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 126–145; 1318–1382
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Deposited calls, endpoints and values retain their source scope. Activity
    classes derived from active assay titles do not independently prove mechanisms
    or direct binding.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2532-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-current254-assigned-source-reading-001.json
  locator: /primary_scope; /contexts; /raw_history_carries; /whole_reading_terminals;
    /remaining_attribution; /verification
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'BGC wholly read contexts 0–6: two unselected companions and the selected
    first five, totaling 63 frames, 23 rows and 316 fields. The selected five account
    for 16 rows and 215 fields; seven companion rows add no selected coverage or transferred
    activity. These are retained database-row readings, not newly inspected primary
    publications.'
  snapshot_sha256: 9f61b5edc55fb784118543b46322d3752d6546aba66539fd6cadd2f548a40c86
- evidence_id: bgc-2532-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Disjoint complete retained-source reading covers 108 frames, 39 rows and
    512 fields: BGC 23 rows and Support 16 rows. Native taxonomy/curation has zero
    positive-source-row credit; overlapping readings add no disjoint row credit.'
  snapshot_sha256: c4d71e9cc9feadeff58f0fc9381158cfb4104f7fdd285c7e4b90f63329e3d39a
- evidence_id: bgc-2532-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /terminal_chunk; /original_exit_code;
    /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: One original composer produced the accepted plan at 388 placements across
    50 paths, with exact source notes and attributed reading receipts. This fragment
    consumes saved results only.
  snapshot_sha256: 6918d768d22fc83472b59d81e0d3f255bb24a093046d2630fdce1ac8e967f42a
- evidence_id: bgc-2532-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/root-current254-source-plan-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /plan; /derivation; /execution;
    /original_tools; /admission; /source; /notes; /inventory; /inventory_acceptance;
    /source_reading_scope; /verification; /ROOT_readings; /limits; /external_requests
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: ROOT accepted the exact 388-placement/50-path source plan and original
    results; no query or input expansion is inferred.
  snapshot_sha256: e1594023691731921ba30963fa0f4932281c6be5fd035aed39ff598a31f47e17
- evidence_id: bgc-2532-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/root-current254-five-gates-acceptance-001.json
  locator: /status; /verification; /all_native_gates_passed; /unavailable_required_gates;
    /execution
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    remains false. Technical checks do not complete scientific verification.
  snapshot_sha256: 97e40634cc818aa894f9ddb3f4e3fd3e4a8c8aee5bba965f2be16f2c6b986ec6
- evidence_id: bgc-2532-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: The bounded ignored-inclusive Native scan found 27 lexical rows and zero
    exact applicable implemented corrections or exclusions. All six applicability
    flags on those rows are false. No actual AID or blank-AID sentinel occurs in the
    complete current inventory; this does not imply biological inactivity.
  snapshot_sha256: eaab179e607165b23f47bdb4c8b4ca8cb1d86120bde0c2a65ceb9e7168438d5f
  search_scope: Twelve exact retained contexts across eleven enumerated curation TSVs
    including ignored files; nine implemented tables and 3422 rows, using exact owner/source/BGC/full-key/assay/occurrence
    predicates. Reserved decisions/source_queue inputs are not effective overrides.
    This is not a global absence or assay-protocol claim.
- evidence_id: bgc-2532-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/0; /cached_taxonomy/whole_stanzas/1
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source IDs; no
    independent taxonomic rank, strain, occurrence or producer validation.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: bgc-2532-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/source_taxa; /contexts/3/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/3/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh
    taxonomy request.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: bgc-2532-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /routes; /interpretation
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Native read all nine whole retained stanzas and twelve routes, with no
    unmatched, forward-merge or nonorganism entry in this exact scope. Source labels,
    cached names and synonyms do not establish strain equivalence, taxonomic rank
    or biological production.
  snapshot_sha256: e800f0a3c08f18400a2cfe4155fa0172bf6395fd5df8425c6b7fab66333b7c6d
- evidence_id: bgc-2532-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-target-input-plan-001.json
  locator: /records/1/proposed_companion_paths; /records/1/direct_companion_predicates
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact immediate owned-BGC context inputs; shared locus/citation is not
    identity, stereochemistry, assay or mechanism transfer. No transitive or name-based
    expansion.
  snapshot_sha256: a3befc1a2429cf92f217bfdcb48cf72dda39597d5bcef98901a61c6b4bf6a8cb
- evidence_id: bgc-2532-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/4/path; /contexts/4/identifier; /contexts/4/label; /contexts/4/standard_inchi_key;
    /contexts/4/complete_raw_text; /contexts/4/complete_raw_history; /contexts/4/source_scope_inventory
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Complete directly linked companion encodings, histories and saved source
    frames, each with its own exact structure, source identifiers and grades. Shared
    owned BGC links define bounded context; no identity, activity, stereochemistry,
    evidence-grade or selected coverage transfer follows.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: bgc-2532-raw-reading-carry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-first-five-whole-reading-001.json
  locator: /observer; /recorded_at; /status; /conditional_membership; /preview_basis;
    /original_tools; /reading_attribution; /records; /totals; /qualified_scope_notes;
    /limits; /actual254_authorities; /external_requests; /target_invocations
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: BGC personally read the five selected first-half owners and their complete
    histories. This pinned receipt is carried only by exact current byte equality;
    it does not claim other readers or companion coverage.
  snapshot_sha256: 78f858da508c69ecd6ca7d0bb1c4d46af342b81f4c784d83e48f874d52d5811b
- evidence_id: bgc-2532-companion-reading-carry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-current254-two-companion-whole-reading-001.json
  locator: /observer; /recorded_at; /status; /census; /owners; /scope; /bounded_cautions;
    /raw_bytes; /raw_lines; /history_entries; /selected_review_credit; /retained_source_row_credit;
    /scientific_verdicts; /external_requests; /target_invocations
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: BGC personally read both unselected immediate companion owners, Bolagladin
    A and Brasiliamide I, including complete histories. This receipt supplies bounded
    raw context only, without selected coverage or identity, stereochemistry or assay
    transfer.
  snapshot_sha256: 90377da62a47d77c55b2465f9a3d3000d335962da904eaaa184cecd5281c8800
- evidence_id: bgc-2532-support-raw-reading-carry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-last-five-whole-owner-reading-001.json
  locator: /observer; /recorded_at; /status; /membership_freeze; /records; /scope;
    /boundaries; /target_invocations; /external_requests
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Support personally read the five selected last-half owners and complete
    histories, including Brasiliamide D. This attributed receipt supplies current
    raw context without transferring identity, assays or selected review coverage.
  snapshot_sha256: 0a0332d6f4656e905b1c0f8fe8855cf04f015d188bb3ff3872833b2a2a919889
- evidence_id: bgc-2532-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2925–2925; row_sha256 10c834e40153988212da883c59e598a9c06e93283be9bd8ac859f6704f173d0f
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact retained compound/version, structure/key, xrefs, producer/locus grades
    and citation tiers. BGC whole saved-source reading and current physical bytes
    are joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2532-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 5841–5841; row_sha256 4bcb6a960081ea07562de14b2f59592cfca611eb1534216947630a0d8848a8cf
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. BGC whole saved-source
    reading and current physical bytes are joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2532-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: bgc-2532-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1576–1576; row_sha256 01d9ef2e5b348443aa8388bf21d29c47d7ce216641c19f0fc8b5535399188aa1
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    remains separate. BGC whole saved-source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2532-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 row placements, exact
    predicate/query and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "NCLKPTJQVKBQEN-YBNREDKZSA-N". Complete
    matched payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2532-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/3/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T09:12:39.263319Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:25:53.433020Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: abde76276283777c27ca8f8cb3e993c54849c791d6c4c50a2b4b752ad4d63a34
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:26:19.438483Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 58288e3a0e8e1f4d32b86499befb70e491856d1d31f9ed7c4e9cdecd80cce987
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:26:39.349503Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:27:14.003223Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:27:26.021174Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: dcdc0438cb99a1ca1e0474633939a0e21f52b5ed7eed5055db8a09a5f824442f
assessments:
- assessment_id: bgc-2532-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-05a2069b99, full key NCLKPTJQVKBQEN-YBNREDKZSA-N,
    formula C27H33NO3 and NPAtlas NPA026755 are mutually retained record assertions.
    Direct companion Bombyxamycin B has formula C27H31NO5, a different full key and
    different oxygenated ring topology. Their shared BGC0002376 does not establish
    identity or permit stereochemistry, activity or mechanistic transfer. The statement
    that no qualifying ChEBI entry shared the structure remains a historical grounding
    result, not an exhaustive current authority search.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-grounding-owner
  - bgc-2532-chemistry
  - bgc-2532-source-mibig_compounds
  - bgc-2532-query-chebi_structures
  - bgc-2532-direct-contexts
  - bgc-2532-companion-boundaries
  - bgc-2532-raw-reading-carry
  - bgc-2532-companion-reading-carry
  - bgc-2532-support-raw-reading-carry
  dimensions:
  - name: standard_inchi_key
    value: NCLKPTJQVKBQEN-YBNREDKZSA-N; retained key, not independent natural-identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2532-grounding-owner
    - bgc-2532-chemistry
    - bgc-2532-source-mibig_compounds
    - bgc-2532-query-chebi_structures
    - bgc-2532-direct-contexts
    - bgc-2532-companion-boundaries
    - bgc-2532-raw-reading-carry
    - bgc-2532-companion-reading-carry
    - bgc-2532-support-raw-reading-carry
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-05a2069b99, full key NCLKPTJQVKBQEN-YBNREDKZSA-N,
      formula C27H33NO3 and NPAtlas NPA026755 are mutually retained record assertions.
      Direct companion Bombyxamycin B has formula C27H31NO5, a different full key
      and different oxygenated ring topology. Their shared BGC0002376 does not establish
      identity or permit stereochemistry, activity or mechanistic transfer. The statement
      that no qualifying ChEBI entry shared the structure remains a historical grounding
      result, not an exhaustive current authority search.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2532-grounding-owner
    - bgc-2532-chemistry
    - bgc-2532-source-mibig_compounds
    - bgc-2532-query-chebi_structures
    - bgc-2532-direct-contexts
    - bgc-2532-companion-boundaries
    - bgc-2532-raw-reading-carry
    - bgc-2532-companion-reading-carry
    - bgc-2532-support-raw-reading-carry
- assessment_id: bgc-2532-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: The two tetrahedral centers are specified in both forms and no unspecified
    tetrahedral center is reported. Seven of the nine original C=C bonds are specified
    (three E and four Z), while two are unspecified; the literal InChI /b15-11? and
    /b23-19? layers refer to those bond geometries. The InChI-derived imidic form
    adds another unspecified potential C=N geometry. The maintained extractor computes
    stereo_complete from FindMolChiralCenters with includeUnassigned=True and useLegacyImplementation=False;
    the true flag therefore does not contradict these unresolved double bonds. This
    review does not upgrade the record to a fully stereochemically proven natural
    isolate.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-grounding-owner
  - bgc-2532-chemistry
  - bgc-2532-topology
  - bgc-2532-diagnostic-reading
  - bgc-2532-diagnostic-acceptance
  - bgc-2532-structure-schema
  - bgc-2532-stereo-method
  - bgc-2532-companion-boundaries
  dimensions:
  - name: stereochemistry_scope
    value: The two tetrahedral centers are specified in both forms and no unspecified
      tetrahedral center is reported. Seven of the nine original C=C bonds are specified
      (three E and four Z), while two are unspecified; the literal InChI /b15-11?
      and /b23-19? layers refer to those bond geometries. The InChI-derived imidic
      form adds another unspecified potential C=N geometry. The maintained extractor
      computes stereo_complete from FindMolChiralCenters with includeUnassigned=True
      and useLegacyImplementation=False; the true flag therefore does not contradict
      these unresolved double bonds. This review does not upgrade the record to a
      fully stereochemically proven natural isolate.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2532-grounding-owner
    - bgc-2532-chemistry
    - bgc-2532-topology
    - bgc-2532-diagnostic-reading
    - bgc-2532-diagnostic-acceptance
    - bgc-2532-structure-schema
    - bgc-2532-stereo-method
    - bgc-2532-companion-boundaries
  - name: representation_correspondence
    value: Both forms give the declared normalized InChI/full key, formula C27H33NO3,
      charge zero, 31 atoms and 31 bonds. Eight comparisons are true; both canonical
      SMILES comparisons are false. The SMILES amide C23(=O24)-N22 is represented
      as C26(OH30)=N27 in the InChI-derived form. The direct atom map is empty and
      full_graph_identity_established is false; normalized agreement supports the
      retained encoding at its stated scope without proving full graph or natural
      identity.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2532-grounding-owner
    - bgc-2532-chemistry
    - bgc-2532-topology
    - bgc-2532-diagnostic-reading
    - bgc-2532-diagnostic-acceptance
    - bgc-2532-structure-schema
    - bgc-2532-stereo-method
    - bgc-2532-companion-boundaries
- assessment_id: bgc-2532-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: MIBiG BGC0002376 version 2 reports a BGC_CHARACTERIZED producer assertion
    for Streptomyces sp. (NCBITaxon:1931) and a distinct CLUSTER_DEMONSTRATED locus
    link at MK433001.1 positions 1–113079. The methods are knock-out studies and gene
    expression correlated with compound production. The source PKS category and those
    locus methods do not specify a complete reaction pathway or prove each protein
    function. LOTUS uses Streptomyces taxon 1883 at genus scope; it must not be collapsed
    into the unspecified-strain producer label. Saved cache names and synonyms add
    no independent rank, strain or production verification.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-origin-owner
  - bgc-2532-occurrence-owner
  - bgc-2532-source-mibig_compounds
  - bgc-2532-cached-taxonomy
  - bgc-2532-taxonomy-routes
  - bgc-2532-curation-scope
  - bgc-2532-direct-contexts
  - bgc-2532-source-lotus_occurrences
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0002376 version 2 reports a BGC_CHARACTERIZED producer assertion
      for Streptomyces sp. (NCBITaxon:1931) and a distinct CLUSTER_DEMONSTRATED locus
      link at MK433001.1 positions 1–113079. The methods are knock-out studies and
      gene expression correlated with compound production. The source PKS category
      and those locus methods do not specify a complete reaction pathway or prove
      each protein function. LOTUS uses Streptomyces taxon 1883 at genus scope; it
      must not be collapsed into the unspecified-strain producer label. Saved cache
      names and synonyms add no independent rank, strain or production verification.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2532-origin-owner
    - bgc-2532-occurrence-owner
    - bgc-2532-source-mibig_compounds
    - bgc-2532-cached-taxonomy
    - bgc-2532-taxonomy-routes
    - bgc-2532-curation-scope
    - bgc-2532-direct-contexts
    - bgc-2532-source-lotus_occurrences
  - name: producer_evidence
    value: MIBiG BGC0002376 version 2 reports a BGC_CHARACTERIZED producer assertion
      for Streptomyces sp. (NCBITaxon:1931) and a distinct CLUSTER_DEMONSTRATED locus
      link at MK433001.1 positions 1–113079. The methods are knock-out studies and
      gene expression correlated with compound production. The source PKS category
      and those locus methods do not specify a complete reaction pathway or prove
      each protein function. LOTUS uses Streptomyces taxon 1883 at genus scope; it
      must not be collapsed into the unspecified-strain producer label. Saved cache
      names and synonyms add no independent rank, strain or production verification.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2532-origin-owner
    - bgc-2532-occurrence-owner
    - bgc-2532-source-mibig_compounds
    - bgc-2532-cached-taxonomy
    - bgc-2532-taxonomy-routes
    - bgc-2532-curation-scope
    - bgc-2532-direct-contexts
    - bgc-2532-source-lotus_occurrences
  - name: locus_evidence
    value: MIBiG BGC0002376 version 2 reports a BGC_CHARACTERIZED producer assertion
      for Streptomyces sp. (NCBITaxon:1931) and a distinct CLUSTER_DEMONSTRATED locus
      link at MK433001.1 positions 1–113079. The methods are knock-out studies and
      gene expression correlated with compound production. The source PKS category
      and those locus methods do not specify a complete reaction pathway or prove
      each protein function. LOTUS uses Streptomyces taxon 1883 at genus scope; it
      must not be collapsed into the unspecified-strain producer label. Saved cache
      names and synonyms add no independent rank, strain or production verification.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2532-origin-owner
    - bgc-2532-occurrence-owner
    - bgc-2532-source-mibig_compounds
    - bgc-2532-cached-taxonomy
    - bgc-2532-taxonomy-routes
    - bgc-2532-curation-scope
    - bgc-2532-direct-contexts
    - bgc-2532-source-lotus_occurrences
- assessment_id: bgc-2532-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: The retained MIBiG reference basis is COMPOUND_EVIDENCE for DOI:10.1021/acs.orglett.9b00384.
    LOTUS repeats that DOI with uppercase letters; these are not independent publications.
    Both seeding history events remain explicit. Source database assertions and the
    historical grounding note are not fresh primary-paper or ChEBI checks.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-owner
  - bgc-2532-history-owner
  - bgc-2532-origin-owner
  - bgc-2532-occurrence-owner
  - bgc-2532-source-mibig_compounds
  - bgc-2532-source-reading
  - bgc-2532-source-lotus_occurrences
  - bgc-2532-companion-boundaries
  - bgc-2532-raw-reading-carry
  - bgc-2532-companion-reading-carry
  - bgc-2532-support-raw-reading-carry
  dimensions:
  - name: citation_scope
    value: The retained MIBiG reference basis is COMPOUND_EVIDENCE for DOI:10.1021/acs.orglett.9b00384.
      LOTUS repeats that DOI with uppercase letters; these are not independent publications.
      Both seeding history events remain explicit. Source database assertions and
      the historical grounding note are not fresh primary-paper or ChEBI checks.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2532-owner
    - bgc-2532-history-owner
    - bgc-2532-origin-owner
    - bgc-2532-occurrence-owner
    - bgc-2532-source-mibig_compounds
    - bgc-2532-source-reading
    - bgc-2532-source-lotus_occurrences
    - bgc-2532-companion-boundaries
    - bgc-2532-raw-reading-carry
    - bgc-2532-companion-reading-carry
    - bgc-2532-support-raw-reading-carry
- assessment_id: bgc-2532-occurrence
  area: evidence
  topic: Source-specific occurrence and assay boundaries
  outcome: supported
  summary: The single retained LOTUS row asserts occurrence at Streptomyces genus
    scope and shares the compound-evidence DOI used by MIBiG. It does not independently
    establish biosynthetic production by a particular strain. The direct Bombyxamycin
    B context remains a different encoded compound, so no measurements or mechanistic
    conclusions are imported from it.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-occurrence-owner
  - bgc-2532-mechanism-absence
  - bgc-2532-query-lotus_occurrences
  - bgc-2532-query-chebi_origins
  - bgc-2532-query-cyanometdb_occurrences
  - bgc-2532-query-pubchem_bioassay
  - bgc-2532-query-bindingdb_targets
  - bgc-2532-query-antibioticmech_inchikeys
  - bgc-2532-cached-taxonomy
  - bgc-2532-taxonomy-routes
  - bgc-2532-taxonomy-reading
  - bgc-2532-curation-scope
  - bgc-2532-bioactivity-seeder
  - bgc-2532-source-reading
  - bgc-2532-source-lotus_occurrences
  - bgc-2532-companion-boundaries
  - bgc-2532-raw-reading-carry
  - bgc-2532-companion-reading-carry
  - bgc-2532-support-raw-reading-carry
  dimensions:
  - name: occurrence_scope
    value: The single retained LOTUS row asserts occurrence at Streptomyces genus
      scope and shares the compound-evidence DOI used by MIBiG. It does not independently
      establish biosynthetic production by a particular strain. The direct Bombyxamycin
      B context remains a different encoded compound, so no measurements or mechanistic
      conclusions are imported from it.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2532-occurrence-owner
    - bgc-2532-mechanism-absence
    - bgc-2532-query-lotus_occurrences
    - bgc-2532-query-chebi_origins
    - bgc-2532-query-cyanometdb_occurrences
    - bgc-2532-query-pubchem_bioassay
    - bgc-2532-query-bindingdb_targets
    - bgc-2532-query-antibioticmech_inchikeys
    - bgc-2532-cached-taxonomy
    - bgc-2532-taxonomy-routes
    - bgc-2532-taxonomy-reading
    - bgc-2532-curation-scope
    - bgc-2532-bioactivity-seeder
    - bgc-2532-source-reading
    - bgc-2532-source-lotus_occurrences
    - bgc-2532-companion-boundaries
    - bgc-2532-raw-reading-carry
    - bgc-2532-companion-reading-carry
    - bgc-2532-support-raw-reading-carry
  - name: assay_target_scope
    value: The complete owner has no causal graph, graph references, components, biosynthetic
      pathway, molecular-target or bioactivity roots. No maintained reader applies.
      Empty exact local ChEBI, CyanoMetDB, PubChem BioAssay, BindingDB and AntibioticMech
      query frames do not establish global absence of activity, a negative experiment
      or absence of literature.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2532-occurrence-owner
    - bgc-2532-mechanism-absence
    - bgc-2532-query-lotus_occurrences
    - bgc-2532-query-chebi_origins
    - bgc-2532-query-cyanometdb_occurrences
    - bgc-2532-query-pubchem_bioassay
    - bgc-2532-query-bindingdb_targets
    - bgc-2532-query-antibioticmech_inchikeys
    - bgc-2532-cached-taxonomy
    - bgc-2532-taxonomy-routes
    - bgc-2532-taxonomy-reading
    - bgc-2532-curation-scope
    - bgc-2532-bioactivity-seeder
    - bgc-2532-source-reading
    - bgc-2532-source-lotus_occurrences
    - bgc-2532-companion-boundaries
    - bgc-2532-raw-reading-carry
    - bgc-2532-companion-reading-carry
    - bgc-2532-support-raw-reading-carry
- assessment_id: bgc-2532-classification
  area: consistency
  topic: Reported model families and qualified applicability
  outcome: supported
  summary: The named NPClassifier output reports Amino acids and Peptides and Polyketides,
    superclass Macrolides and class Macrolide lactams, with is_glycoside false. The
    26-membered lactam topology is compatible with the class label and lacks a detected
    sugar-ring motif. The mixed computed pathways explain UNCLASSIFIED filing under
    the maintained rule; they do not override the separate MIBiG PKS category or establish
    a mixed biosynthetic mechanism.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-classification-owner
  - bgc-2532-source-npclassifier
  - bgc-2532-chemistry
  - bgc-2532-topology
  - bgc-2532-structure-schema
  - bgc-2532-classification-seeder
  - bgc-2532-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: The named NPClassifier output reports Amino acids and Peptides and Polyketides,
      superclass Macrolides and class Macrolide lactams, with is_glycoside false.
      The 26-membered lactam topology is compatible with the class label and lacks
      a detected sugar-ring motif. The mixed computed pathways explain UNCLASSIFIED
      filing under the maintained rule; they do not override the separate MIBiG PKS
      category or establish a mixed biosynthetic mechanism.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2532-classification-owner
    - bgc-2532-source-npclassifier
    - bgc-2532-chemistry
    - bgc-2532-topology
    - bgc-2532-structure-schema
    - bgc-2532-classification-seeder
    - bgc-2532-source-mibig_compounds
- assessment_id: bgc-2532-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: The complete raw owner/history, accepted canonical intake and retained
    source frames were read, together with both complete saved molecular forms. No
    mechanism root applies to a maintained-reader check for this owner. The review
    remains partial because external authority/publication verification and full QC/OAK
    are unavailable; native status, source content and open issues are unchanged.
  target_ids:
  - naturalproductmech:mibig-05a2069b99
  evidence_ids:
  - bgc-2532-owner
  - bgc-2532-capture
  - bgc-2532-intake
  - bgc-2532-intake-acceptance
  - bgc-2532-history-owner
  - bgc-2532-diagnostic-reading
  - bgc-2532-diagnostic-acceptance
  - bgc-2532-diagnostic-execution
  - bgc-2532-source-reading
  - bgc-2532-joint-source-notes
  - bgc-2532-source-plan-execution
  - bgc-2532-source-plan-acceptance
  - bgc-2532-native-gate-limits
  - bgc-2532-curation-scope
  - bgc-2532-mechanism-absence
  - bgc-2532-companion-boundaries
  - bgc-2532-raw-reading-carry
  - bgc-2532-companion-reading-carry
  - bgc-2532-support-raw-reading-carry
  dimensions:
  - name: review_completion
    value: The complete raw owner/history, accepted canonical intake and retained
      source frames were read, together with both complete saved molecular forms.
      No mechanism root applies to a maintained-reader check for this owner. The review
      remains partial because external authority/publication verification and full
      QC/OAK are unavailable; native status, source content and open issues are unchanged.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2532-owner
    - bgc-2532-capture
    - bgc-2532-intake
    - bgc-2532-intake-acceptance
    - bgc-2532-history-owner
    - bgc-2532-diagnostic-reading
    - bgc-2532-diagnostic-acceptance
    - bgc-2532-diagnostic-execution
    - bgc-2532-source-reading
    - bgc-2532-joint-source-notes
    - bgc-2532-source-plan-execution
    - bgc-2532-source-plan-acceptance
    - bgc-2532-native-gate-limits
    - bgc-2532-curation-scope
    - bgc-2532-mechanism-absence
    - bgc-2532-companion-boundaries
    - bgc-2532-raw-reading-carry
    - bgc-2532-companion-reading-carry
    - bgc-2532-support-raw-reading-carry
findings: []
actions: []
limitations:
- Only retained local records, database rows, historical annotations and accepted
  offline outputs were inspected; no fresh publication, authority, protein sequence,
  construct or experimental verification was performed.
- Full QC and OAK were unavailable, all_native_gates_passed remains false, and this
  review is partial.
- The six diagnostic warnings are global and are not assigned to individual records.
  No additional molecular parsing was performed.
- Two original double-bond geometries remain unspecified despite the atom-center completeness
  flag; no full atom map or independent natural-identity verification is available.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all ten first-five saved molecular forms (372 atom rows and
  384 bond rows) and 196 actual intake placements across 46 paths, without new parsing.
- 'Disjoint retained-source reading: BGC first-five selected plus two companions,
  63 frames/23 rows/316 fields; Support last-five selected, 45 frames/16 rows/196
  fields. Native cache/curation receives zero positive-source-row credit.'
- BGC operated original collector/composer; Support operated canonical intakes; Native
  operated the diagnostic and Bolagladin B maintained reader under ROOT delegation.
  Only order 2531 requires a reader in this fragment scope. These fragments consume
  saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-254
```
