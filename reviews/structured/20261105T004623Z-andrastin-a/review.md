# Local evidence review: andrastin A

- Review: 20261105T004623Z-andrastin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T23:57:06.257393Z
- Finished UTC: 2026-11-05T00:46:23.131209Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Andrastin A retains a fully specified deposited tetrahedral encoding and the source 19-oxosteroid/meroterpenoid descriptions with separate model and source scopes. Producer evidence remains SOURCE_ASSERTION and locus evidence remains CLUSTER_UNSTATED. Diverse occurrence annotations and a definition-level farnesyltransferase claim do not become native assay or causal-production evidence.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2483; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:142842 | data/natural_products/unclassified/andrastin-a.yaml | generated | andrastin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:142842 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:142842 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:142842 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:142842 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:142842 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:142842 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:142842 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:142842 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: CHEBI:142842.

CHEBI:142842 and the retained MIBiG BGC0001508 structure identify the saved C28H38O7 encoding; both forms reproduce its full key and normalized InChI. The ChEBI definition describes a19-oxosteroid and farnesyltransferase inhibitor, which remains a source definition rather than independent structural authentication or a measured native assay. No exact direct companion is asserted by the declared census.

### Stored-form topology and stereochemical scope

representation: supported. Targets: CHEBI:142842.

Both neutral saved forms contain35 atoms and38 bonds; all ten comparisons are true and the direct map spans35 atoms, with full_graph_identity_established:false retained. Seven tetrahedral centers are specified with no additional unspecified potential centers in these results. The literal true flag is consistent with the maintained tetrahedral check; it does not independently prove natural stereochemistry or every positional name.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: CHEBI:142842.

BGC0001508 version 3 retains Penicillium roqueforti NCBITaxon:5082 as SOURCE_ASSERTION and KY349137.1 as a CLUSTER_UNSTATED locus without declared coordinates or methods. Seven ChEBI origin rows plus one LOTUS row contain six source taxon IDs; they remain occurrence annotations, not six proven producers. The FO-3929 strain comment belongs specifically to P.simplicissimum69488. Source Penicillium camponotum at2072477 and cached P.camponoti remain separately labelled; no current spelling/taxonomic correction is asserted.

### Citation tiers and complete history scope

evidence: supported. Targets: CHEBI:142842.

MIBiG ENTRY PMID28529508, each ChEBI origin citation/comment and the LOTUS DOI preserve their source roles. The two P.roqueforti origin rows cite PMID15826038 and PMID19837474 separately; PMID27616792 is shared by the P.camponotum, P.cataractarum and P.costaricense rows. Repeated taxon placements and overlapping article references do not establish independent experiments. All three seed-history events are retained. The inhibitor phrase in the ChEBI definition is not a freshly checked primary assay.

### Source-specific occurrence and assay assertions

evidence: supported. Targets: CHEBI:142842.

All eight source occurrence placements are retained with their taxon/reference scope. The complete owner has no native bioactivity, causal graph, pathway, component-reference or molecular-target root, and no exact saved PubChem/BindingDB assay supplies a potency result. A definition-level farnesyltransferase-inhibitor statement does not justify adding a target or transferring activity to every occurrence.

### Reported model families and bounded structural compatibility

consistency: supported. Targets: CHEBI:142842.

The source PKS category, ChEBI19-oxosteroid description and versioned Tetraketide meroterpenoids model label answer different questions. The fused-ring/aldehyde/ester topology is compatible with the retained structural description; neither topology nor model output independently establishes the PKS/terpene biosynthetic contribution. The UNCLASSIFIED filing and exact model arrays are preserved without treating model labels as source assertions.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: CHEBI:142842.

Both complete molecular forms, all actual intake inputs, raw/history and complete saved source payloads are read. Structural consistency and retained annotation scope are supported locally; primary natural identity, producer experiments and inhibitor protocol remain unverified. The review remains partial without a demonstrated source-edit defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2483-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/andrastin-a.yaml; Complete plaintext including every curation_history entry | supports | Complete andrastin A owner with 3 history events; prior complete raw reading carries with current identical bytes. No source/status/history edit. |
| bgc-2483-capture | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2483-intake | /private/tmp/npm-review-work/shared-next-batch249/intakes/2483-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, ownership and all 37 input placements joined to current plan hashes. |
| bgc-2483-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/2 | supports | ROOT accepted the original canonical intake and exact supplemental plan; this owner’s actual inspection and receipt pins are located. |
| bgc-2483-grounding-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/definition; /records/2/owner_document/definition_source; /records/2/owner_document/chemical_structure; /records/2/owner_document/xrefs; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status | supports | Exact retained identifier, structure, source concepts, definition where present, cross-references and grounding fields. Historical annotations are not fresh authority searches. |
| bgc-2483-origin-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, declared coordinates and citation tiers; absent fields are not filled. |
| bgc-2483-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete owner supplies exact occurrence, activity and nested target assertions or bounded absence. Detection does not prove production; absent assays do not mean inactivity. |
| bgc-2483-classification-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2/owner_document/np_classification; /records/2/owner_document/np_pathway; /records/2/owner_document/bgc_class | supports | Exact named/versioned model arrays, glycoside flag, filing and separate source categories; retention fidelity is not biological-family or biosynthetic proof. |
| bgc-2483-history-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2/owner_document/curation_status; /records/2/owner_document/curation_history | supports | All history events and status are preserved; seeding/import remains distinct from fresh primary verification. |
| bgc-2483-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets roots; no maintained reader applies. Its 0 native bioactivities and any nested target annotations remain separately retained. |
| bgc-2483-chemistry | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence; /records/2/smiles/computed/formula; /records/2/smiles/computed/formal_charge; /records/2/smiles/computed/standard_inchi; /records/2/smiles/computed/standard_inchi_key; /records/2/smiles/computed/canonical_isomeric_smiles; /records/2/smiles/computed/canonical_nonisomeric_smiles; /records/2/smiles/computed/atom_count; /records/2/smiles/computed/heavy_atom_count; /records/2/smiles/computed/bond_count; /records/2/smiles/computed/element_counts; /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/formula; /records/2/inchi/computed/formal_charge; /records/2/inchi/computed/standard_inchi; /records/2/inchi/computed/standard_inchi_key; /records/2/inchi/computed/canonical_isomeric_smiles; /records/2/inchi/computed/canonical_nonisomeric_smiles; /records/2/inchi/computed/atom_count; /records/2/inchi/computed/heavy_atom_count; /records/2/inchi/computed/bond_count; /records/2/inchi/computed/element_counts; /records/2/inchi/computed/stereo_counts | supports | All ten stored-form comparisons are true and the direct map spans atom counts; full_graph_identity_established remains false. Natural identity, tautomer preference and complete stereochemistry are not established by these booleans. |
| bgc-2483-topology | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/motifs; /records/2/smiles/computed/fragment_atom_indices; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings; /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs; /records/2/inchi/computed/fragment_atom_indices | supports | The four fused ring-basis sizes6,6,5,6 are compatible with a steroid-like6/6/6/5 skeleton. SMILES C33=O34 bears one hydrogen (aldehyde), C11=O12 is ketonic and C15-O16H is enolic. Ester branches C18(=O19)-O20-C21 and C27(=O29)-O26-C25 retain methyl-ester and acetate environments. No amide or saturated C5O candidate sugar cycle is detected. These observations support the retained oxygenated fused-ring description without independently assigning biochemical positions. |
| bgc-2483-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-first-five-diagnostic-reading-001.json; /records/2; /read_scope; /totals; /representation; /reading_caveats; /reader | supports | BGC personally read all ten complete first-five forms:604 atom and636 bond rows and all191 intake placements/47 paths. Whole Anditomin graph/history meanings factor to exact actual full-owner preservation; saved-result limits and display recovery are recorded. |
| bgc-2483-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/2; /molecular_parse_attempts; /parsed; /global_warning_count; /method_scope; /interpretation_boundary | supports | ROOT accepted the original twenty stored forms. This owner’s actual comparison scope is located; four warnings remain global and unassigned. No alternate parse or normalization repair is inferred. |
| bgc-2483-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins; stream interpretation is supplied separately. |
| bgc-2483-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–433 | supports | Undefined stereocenters remain explicit; named/versioned computed classification is never a source assertion. |
| bgc-2483-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines165–173 | supports | The maintained stereo_complete flag tests unassigned tetrahedral centers; natural identity and double-bond geometry need their separate evidence scopes. |
| bgc-2483-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines295–306;988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2483-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines126–145;1318–1382 | supports | Source assay calls, endpoint values and target accessions are retained. Activity classes use assay-name matching on active rows and summaries derive from written classes; these are not independent potency measurements or protocol validation. |
| bgc-2483-source-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-assigned-source-reading-001.json; /selected_indices; /reading; /counts; /frames; /cautions | supports | BGC personally read contexts0–3:36 complete frames/22 rows/225 fields, including the Anditomin blank-AID sentinel. This does not claim ROOT’s Antimycin source-row credit. |
| bgc-2483-root-source-reading | /private/tmp/npm-review-work/shared-next-batch249/root-current249-source-row-reading-001.json; /context_indices; /named_query_frames; /positive_row_placements; /positive_row_fields; /whole_payload_readings; /scientific_cautions | supports | ROOT personally read Antimycin A context4:9 complete frames/185 rows/1990 fields, including all172 assay rows. Attribution remains ROOT; no duplicate source-row credit. |
| bgc-2483-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Complete disjoint source reading covers90 frames/222 rows/2415 fields: BGC22, ROOT185 and Support15 rows. Native cache/curation has zero positive-row credit; overlapping readings add none. |
| bgc-2483-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch249/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /notes; /verification; /supplement_scope | supports | One original composer produced historical plan001 at379 placements/51 paths. Inventory and original source counts remain unchanged; the separate accepted supplement adds three A1B rule/transform inputs only. |
| bgc-2483-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-target-input-plan-acceptance-001.json; /status; /accepted; /plan; /original_plan; /supplement_derivation; /source_placements; /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification | supports | ROOT accepted supplemental plan002 at382 placements/54 paths. Only2486 gains three rule/transform inputs; no source query, context or positive-row count is added. |
| bgc-2483-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch249/root-current249-native-gates-acceptance-001.json; /status; /counts; /all_native_gates_passed; /unavailable | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed is false. Local validation does not complete scientific verification. |
| bgc-2483-curation-scope | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | The bounded Native scan found no applicable implemented correction/exclusion and26 unrelated lexical hits. No exact assay exclusion applies among172 retained tuples; one blank sentinel remains separate. |
| bgc-2483-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/6; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/12; /cached_taxonomy/whole_stanzas/22; /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/24 | supports | Complete saved cache names and synonyms for this owner’s source taxon IDs. They do not independently validate taxonomic rank, source strain labels, occurrence or production; no fresh taxonomy lookup. |
| bgc-2483-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/source_taxa; /contexts/2/source_scope_inventory/forward_taxon_merge_matches; /contexts/2/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and saved forwarding/nonorganism routes for this owner; no fresh taxonomy request. |
| bgc-2483-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /forward_routes; /interpretation | supports | Native personally read all26 saved cache stanzas/10 routes, including67295→1911. Cached names/synonyms and routes do not upgrade species, strain, occurrence or producer evidence. |
| bgc-2483-direct-contexts | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json; /records/2/proposed_companion_paths; /records/2/direct_companion_predicates | supports | Exact declared one-hop direct map is empty for this batch. Selected Antimycin identity comparison is separate; no transitive expansion or biological claim transfer is inferred. |
| bgc-2483-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2483-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines 1819–1819; row_sha256 45ca75bd8732f812b1ff18f33b9193a6282240131ba2c4d334288d2288ae7270 | supports | Exact compound/version, structure/key, database IDs, producer/locus grades and citation tiers. BGC complete source reading and current physical bytes are joined. |
| bgc-2483-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2483-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line1; physical lines 40756–40756; row_sha256 144d43758a33d8df6044c12bf7771a696a9d63e4cac4ef5c08956536cdeb89b1 | supports | Exact retained ChEBI identifier/full key/label/definition/structure fields with source grounding; no fresh authority lookup. BGC complete source reading and current physical bytes are joined. |
| bgc-2483-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2483-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line1; physical lines 8441–8441; row_sha256 50da809bf24724908e77fe71ebb7706d3e5345cbec61d0af4bb3c40b8908d124 | supports | Complete organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. BGC complete source reading and current physical bytes are joined. |
| bgc-2483-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2483-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2483-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines 2275–2275; row_sha256 0b125ae415111f3289d84327580e2b07ff68efe820b47225c7d855a32d655fad | supports | Exact named/versioned model arrays and glycoside flag; applicability is assessed separately. BGC complete source reading and current physical bytes are joined. |
| bgc-2483-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2483-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2483-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2483-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/2/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame has 7 placements with exact query, predicate and all matched fields. |
| bgc-2483-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; Header line1; physical lines 16467–16467; row_sha256 d55b550b8b7693bfc590474b8f2e365f60e50913faa491fd260941b24a64353f; physical lines 16468–16468; row_sha256 6bdfc82091ac524cc88f6e220f06d977a98d0a9365df651fe7f43f6842231c9a; physical lines 16469–16469; row_sha256 a2cf1483581584ec50c9b8c366cdb481c687b0fc9aed4a56b436bc63d1c6997e; physical lines 16470–16470; row_sha256 dddbd88ff99f06bf1666cf704e662e0c26ff2a29dbd955da92040cec379bed99; physical lines 16471–16471; row_sha256 2470e5160eddbc2743791f65c9f55a4f9c604c9c4b26588077d68af50e4145fb; physical lines 16472–16472; row_sha256 c56d1700caf2fc8bfa484ada0bc90930e22b1f5a6791356c56b654d611a6f46f; physical lines 16473–16473; row_sha256 b21a45079bc99ad6975867cbc34b5a4aa0b7b71e40428eb5982855796fd88901 | supports | Exact retained ChEBI origin annotation, organism and reference; distinct from causal production and repeated citations. BGC complete source reading and current physical bytes are joined. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-249/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-249/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-249/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-249/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-249/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; fresh primary literature, current authority/taxonomy, assay protocols and independent natural identity/stereochemical authentication remain unavailable.
- Five local commands passed; full QC and OAK remain unavailable. Four diagnostic warnings remain global and unassigned. Normalized identifiers and counts do not establish full graph or natural identity.
- Producer, locus, occurrence, strain and citation tiers remain separate; repeated references and target-enriched assay rows do not establish independent experiments.
- Model-family applicability stays qualified. Anditomin historical enzyme/sequence claims are not freshly validated; Antimycin A and selected stereo-unspecified A1B retain distinct assay and identity scopes.
- Both complete molecular forms, all actual intake inputs, raw/history and complete saved source payloads are read. Structural consistency and retained annotation scope are supported locally; primary natural identity, producer experiments and inhibitor protocol remain unverified. The review remains partial without a demonstrated source-edit defect.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all first-five ten complete forms:604 atom/636 bond rows and191 actual intake placements/47 paths. No new molecular parse.
- Source reading is disjoint: BGC contexts0–3/36 frames/22 rows/225 fields; ROOT context4/9 frames/185 rows/1990 fields; Support contexts5–9/45 frames/15 rows/200 fields. Native cache/curation receives zero positive-row credit.
- BGC operated original collector/composer; Support operated canonical intakes; Native operated diagnostic and maintained readers under ROOT delegation. These fragments consume saved results only.
- No first-five source-edit finding is proposed. Separate A1B findings remain in Support’s last-five review and are not transferred to Antimycin A.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T004623Z-andrastin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: andrastin A'
started_at: '2026-11-04T23:57:06.257393Z'
finished_at: '2026-11-05T00:46:23.131209Z'
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
summary: Andrastin A retains a fully specified deposited tetrahedral encoding and
  the source 19-oxosteroid/meroterpenoid descriptions with separate model and source
  scopes. Producer evidence remains SOURCE_ASSERTION and locus evidence remains CLUSTER_UNSTATED.
  Diverse occurrence annotations and a definition-level farnesyltransferase claim
  do not become native assay or causal-production evidence.
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
  - path: data/natural_products/unclassified/andrastin-a.yaml
    sha256: df90f2c255ac518d99a8c1005d292a1247f4110e0b092da7672eff42630045b2
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
  selection: Campaign path order 2483; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:142842
targets:
- target_id: CHEBI:142842
  path: data/natural_products/unclassified/andrastin-a.yaml
  label: andrastin A
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
    path: data/raw/chebi_structures.tsv
    role: Retained ChEBI identifiers, definitions and exact chemical forms.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Retained cited occurrence assertions, distinct from demonstrated production.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
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
  - CHEBI:142842
  command: just validate-strict data/natural_products/unclassified/andalusicin-a.yaml
    data/natural_products/unclassified/anditomin.yaml data/natural_products/unclassified/andrastin-a.yaml
    data/natural_products/unclassified/antalid.yaml data/natural_products/unclassified/antimycin-a.yaml
    data/natural_products/unclassified/antimycin-a1b.yaml data/natural_products/unclassified/ape-ec.yaml
    data/natural_products/unclassified/ape-vf.yaml data/natural_products/unclassified/apratoxin-a.yaml
    data/natural_products/unclassified/arthrofactin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-249/validate-strict-selected10-001.tsv
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
  - CHEBI:142842
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-249/validate-all-001.tsv
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
  - CHEBI:142842
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
  - CHEBI:142842
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
  - CHEBI:142842
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-249/review-queue-001.tsv
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
  - CHEBI:142842
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:142842
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:142842
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2483-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/andrastin-a.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete andrastin A owner with 3 history events; prior complete raw reading
    carries with current identical bytes. No source/status/history edit.
  snapshot_sha256: df90f2c255ac518d99a8c1005d292a1247f4110e0b092da7672eff42630045b2
- evidence_id: bgc-2483-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/intakes/2483-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Actual canonical target, ownership and all 37 input placements joined to
    current plan hashes.
  snapshot_sha256: ddb76317be878871fbd71912cf5b0aa99438513f149ae395792965351e01d2a7
- evidence_id: bgc-2483-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/2
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted the original canonical intake and exact supplemental plan;
    this owner’s actual inspection and receipt pins are located.
  snapshot_sha256: f4ee1f9dc4160c60cc3201b9246bb2ee1bd3ec750d96493dccd37dbd1725a6e5
- evidence_id: bgc-2483-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/definition; /records/2/owner_document/definition_source;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/xrefs;
    /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact retained identifier, structure, source concepts, definition where
    present, cross-references and grounding fields. Historical annotations are not
    fresh authority searches.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/producer_taxon_groups;
    /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, declared coordinates
    and citation tiers; absent fields are not filled.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete owner supplies exact occurrence, activity and nested target assertions
    or bounded absence. Detection does not prove production; absent assays do not
    mean inactivity.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_classification; /records/2/owner_document/np_pathway;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact named/versioned model arrays, glycoside flag, filing and separate
    source categories; retention fidelity is not biological-family or biosynthetic
    proof.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2/owner_document/curation_status; /records/2/owner_document/curation_history
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: All history events and status are preserved; seeding/import remains distinct
    from fresh primary verification.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets roots; no maintained reader applies. Its 0 native bioactivities
    and any nested target annotations remain separately retained.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2483-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons;
    /records/2/atom_correspondence; /records/2/smiles/computed/formula; /records/2/smiles/computed/formal_charge;
    /records/2/smiles/computed/standard_inchi; /records/2/smiles/computed/standard_inchi_key;
    /records/2/smiles/computed/canonical_isomeric_smiles; /records/2/smiles/computed/canonical_nonisomeric_smiles;
    /records/2/smiles/computed/atom_count; /records/2/smiles/computed/heavy_atom_count;
    /records/2/smiles/computed/bond_count; /records/2/smiles/computed/element_counts;
    /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/formula; /records/2/inchi/computed/formal_charge;
    /records/2/inchi/computed/standard_inchi; /records/2/inchi/computed/standard_inchi_key;
    /records/2/inchi/computed/canonical_isomeric_smiles; /records/2/inchi/computed/canonical_nonisomeric_smiles;
    /records/2/inchi/computed/atom_count; /records/2/inchi/computed/heavy_atom_count;
    /records/2/inchi/computed/bond_count; /records/2/inchi/computed/element_counts;
    /records/2/inchi/computed/stereo_counts
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: All ten stored-form comparisons are true and the direct map spans atom
    counts; full_graph_identity_established remains false. Natural identity, tautomer
    preference and complete stereochemistry are not established by these booleans.
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2483-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons;
    /records/2/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds;
    /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo;
    /records/2/smiles/computed/motifs; /records/2/smiles/computed/fragment_atom_indices;
    /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings;
    /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs;
    /records/2/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: The four fused ring-basis sizes6,6,5,6 are compatible with a steroid-like6/6/6/5
    skeleton. SMILES C33=O34 bears one hydrogen (aldehyde), C11=O12 is ketonic and
    C15-O16H is enolic. Ester branches C18(=O19)-O20-C21 and C27(=O29)-O26-C25 retain
    methyl-ester and acetate environments. No amide or saturated C5O candidate sugar
    cycle is detected. These observations support the retained oxygenated fused-ring
    description without independently assigning biochemical positions.
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2483-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-first-five-diagnostic-reading-001.json
  locator: /records/2; /read_scope; /totals; /representation; /reading_caveats; /reader
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: BGC personally read all ten complete first-five forms:604 atom and636 bond
    rows and all191 intake placements/47 paths. Whole Anditomin graph/history meanings
    factor to exact actual full-owner preservation; saved-result limits and display
    recovery are recorded.
  snapshot_sha256: 8f02ce5ed547abe9ee3e3738e23cec650136884c62b12e64de9dc31dfa480a63
- evidence_id: bgc-2483-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/2; /molecular_parse_attempts; /parsed;
    /global_warning_count; /method_scope; /interpretation_boundary
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted the original twenty stored forms. This owner’s actual comparison
    scope is located; four warnings remain global and unassigned. No alternate parse
    or normalization repair is inferred.
  snapshot_sha256: 85f657ea1d785c1aca4e78bdcf54056041799b0913a9df5155fb43b6ed51e491
- evidence_id: bgc-2483-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins;
    stream interpretation is supplied separately.
  snapshot_sha256: 7955c4e94046cc4fedde2ebda7bd56f32eb9cb544f5367b1955b30ae11d58c88
- evidence_id: bgc-2483-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–433
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Undefined stereocenters remain explicit; named/versioned computed classification
    is never a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2483-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines165–173
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: The maintained stereo_complete flag tests unassigned tetrahedral centers;
    natural identity and double-bond geometry need their separate evidence scopes.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2483-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines295–306;988–1022
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays
    remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2483-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines126–145;1318–1382
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Source assay calls, endpoint values and target accessions are retained.
    Activity classes use assay-name matching on active rows and summaries derive from
    written classes; these are not independent potency measurements or protocol validation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2483-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-assigned-source-reading-001.json
  locator: /selected_indices; /reading; /counts; /frames; /cautions
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: BGC personally read contexts0–3:36 complete frames/22 rows/225 fields,
    including the Anditomin blank-AID sentinel. This does not claim ROOT’s Antimycin
    source-row credit.
  snapshot_sha256: 8204ce76b856283f97da2268d1a5738b9616c5da78d6a2996ffb2b5bfce43737
- evidence_id: bgc-2483-root-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-current249-source-row-reading-001.json
  locator: /context_indices; /named_query_frames; /positive_row_placements; /positive_row_fields;
    /whole_payload_readings; /scientific_cautions
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT personally read Antimycin A context4:9 complete frames/185 rows/1990
    fields, including all172 assay rows. Attribution remains ROOT; no duplicate source-row
    credit.
  snapshot_sha256: 60a0d18b4dde9699fff69bc1c459a499b0e01e003cc7156c2bb90af82b35d44d
- evidence_id: bgc-2483-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: 'Complete disjoint source reading covers90 frames/222 rows/2415 fields:
    BGC22, ROOT185 and Support15 rows. Native cache/curation has zero positive-row
    credit; overlapping readings add none.'
  snapshot_sha256: b326cf0f50a7ed128bba21bf3e4554fac446e8a221bdddcb80d0c6390818f2fb
- evidence_id: bgc-2483-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /terminal_chunk; /original_exit_code;
    /plan; /derivation; /inventory; /notes; /verification; /supplement_scope
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: One original composer produced historical plan001 at379 placements/51 paths.
    Inventory and original source counts remain unchanged; the separate accepted supplement
    adds three A1B rule/transform inputs only.
  snapshot_sha256: fbfa1b83fa8730137b861584e61d254cca5b43dfd5f2f2a92ce289c40f630029
- evidence_id: bgc-2483-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-target-input-plan-acceptance-001.json
  locator: /status; /accepted; /plan; /original_plan; /supplement_derivation; /source_placements;
    /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted supplemental plan002 at382 placements/54 paths. Only2486
    gains three rule/transform inputs; no source query, context or positive-row count
    is added.
  snapshot_sha256: 68262c91ae1a1ebc2517faaa1f59c227db9a7d17f53a0a47f108b614d968ac7b
- evidence_id: bgc-2483-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-current249-native-gates-acceptance-001.json
  locator: /status; /counts; /all_native_gates_passed; /unavailable
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    is false. Local validation does not complete scientific verification.
  snapshot_sha256: 7c4057fa2e4c45bd5339590edd15f460011ae95df0211342b097be1e9b76b94a
- evidence_id: bgc-2483-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: The bounded Native scan found no applicable implemented correction/exclusion
    and26 unrelated lexical hits. No exact assay exclusion applies among172 retained
    tuples; one blank sentinel remains separate.
  snapshot_sha256: 0cfa769044caf4976e7fec895a44e667bf21c3bc8d9a0cabd465916034f98ed1
  search_scope: All10 current contexts,283 literal tokens and11 enumerated TSVs including
    ignored files; nine eligible tables/3422 rows. Exact applicability uses retained
    owner/source/full-key/BGC/name/taxon predicates, not global absence or assay-protocol
    validation.
- evidence_id: bgc-2483-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/6; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/12;
    /cached_taxonomy/whole_stanzas/22; /cached_taxonomy/whole_stanzas/23; /cached_taxonomy/whole_stanzas/24
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source taxon IDs.
    They do not independently validate taxonomic rank, source strain labels, occurrence
    or production; no fresh taxonomy lookup.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2483-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/source_taxa; /contexts/2/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/2/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact source taxon IDs and saved forwarding/nonorganism routes for this
    owner; no fresh taxonomy request.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2483-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /forward_routes; /interpretation
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Native personally read all26 saved cache stanzas/10 routes, including67295→1911.
    Cached names/synonyms and routes do not upgrade species, strain, occurrence or
    producer evidence.
  snapshot_sha256: 781f62e73b1694225f8ccdca96b95bbc58bea281997f4ef1152a7ccf2d5ecc88
- evidence_id: bgc-2483-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json
  locator: /records/2/proposed_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact declared one-hop direct map is empty for this batch. Selected Antimycin
    identity comparison is separate; no transitive expansion or biological claim transfer
    is inferred.
  snapshot_sha256: 4c92dba7f8c9b89c7fe05a9e64e3721282d76814855c144975ff46e930b901b0
- evidence_id: bgc-2483-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved mibig_compounds frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines 1819–1819; row_sha256 45ca75bd8732f812b1ff18f33b9193a6282240131ba2c4d334288d2288ae7270
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact compound/version, structure/key, database IDs, producer/locus grades
    and citation tiers. BGC complete source reading and current physical bytes are
    joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2483-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved chebi_structures frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line1; physical lines 40756–40756; row_sha256 144d43758a33d8df6044c12bf7771a696a9d63e4cac4ef5c08956536cdeb89b1
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact retained ChEBI identifier/full key/label/definition/structure fields
    with source grounding; no fresh authority lookup. BGC complete source reading
    and current physical bytes are joined.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2483-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved lotus_occurrences frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line1; physical lines 8441–8441; row_sha256 50da809bf24724908e77fe71ebb7706d3e5345cbec61d0af4bb3c40b8908d124
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. BGC complete
    source reading and current physical bytes are joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2483-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved npclassifier frame has 1 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching payload or the empty
    frame is retained; no query replay.
- evidence_id: bgc-2483-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines 2275–2275; row_sha256 0b125ae415111f3289d84327580e2b07ff68efe820b47225c7d855a32d655fad
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; applicability is
    assessed separately. BGC complete source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2483-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved bindingdb_targets frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "SNSSSENJBPCLPM-OXILWVMOSA-N". Every
    matching payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/2/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved chebi_origins frame has 7 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query ["CHEBI:142842"]. Every matching payload
    or the empty frame is retained; no query replay.
- evidence_id: bgc-2483-source-chebi_origins
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: Header line1; physical lines 16467–16467; row_sha256 d55b550b8b7693bfc590474b8f2e365f60e50913faa491fd260941b24a64353f;
    physical lines 16468–16468; row_sha256 6bdfc82091ac524cc88f6e220f06d977a98d0a9365df651fe7f43f6842231c9a;
    physical lines 16469–16469; row_sha256 a2cf1483581584ec50c9b8c366cdb481c687b0fc9aed4a56b436bc63d1c6997e;
    physical lines 16470–16470; row_sha256 dddbd88ff99f06bf1666cf704e662e0c26ff2a29dbd955da92040cec379bed99;
    physical lines 16471–16471; row_sha256 2470e5160eddbc2743791f65c9f55a4f9c604c9c4b26588077d68af50e4145fb;
    physical lines 16472–16472; row_sha256 c56d1700caf2fc8bfa484ada0bc90930e22b1f5a6791356c56b654d611a6f46f;
    physical lines 16473–16473; row_sha256 b21a45079bc99ad6975867cbc34b5a4aa0b7b71e40428eb5982855796fd88901
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact retained ChEBI origin annotation, organism and reference; distinct
    from causal production and repeated citations. BGC complete source reading and
    current physical bytes are joined.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:00:36.010567Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 27ebd661adce0e3ead194e6f0d627ebecf75c8d49a30ea4594cbe1d40e3eaf61
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:01:00.665052Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: ad956e928d3adb01dc4ca3be63be5560456a61997bb7d9463bd40e44e29a321e
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:01:21.006602Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:01:56.490347Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-249/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-249/native-current249-five-gates-execution-001.json
  accessed_at: '2026-11-05T00:02:08.678647Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 37db480802437fd52339442d7179165d3a7097a76a08ad575413b5858998667f
assessments:
- assessment_id: bgc-2483-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: CHEBI:142842 and the retained MIBiG BGC0001508 structure identify the saved
    C28H38O7 encoding; both forms reproduce its full key and normalized InChI. The
    ChEBI definition describes a19-oxosteroid and farnesyltransferase inhibitor, which
    remains a source definition rather than independent structural authentication
    or a measured native assay. No exact direct companion is asserted by the declared
    census.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-grounding-owner
  - bgc-2483-chemistry
  - bgc-2483-source-mibig_compounds
  - bgc-2483-query-chebi_structures
  - bgc-2483-direct-contexts
  - bgc-2483-source-chebi_structures
  dimensions:
  - name: standard_inchi_key
    value: SNSSSENJBPCLPM-OXILWVMOSA-N; retained key, not natural-identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2483-grounding-owner
    - bgc-2483-chemistry
    - bgc-2483-source-mibig_compounds
    - bgc-2483-query-chebi_structures
    - bgc-2483-direct-contexts
    - bgc-2483-source-chebi_structures
  - name: grounding_scope
    value: CHEBI:142842 and the retained MIBiG BGC0001508 structure identify the saved
      C28H38O7 encoding; both forms reproduce its full key and normalized InChI. The
      ChEBI definition describes a19-oxosteroid and farnesyltransferase inhibitor,
      which remains a source definition rather than independent structural authentication
      or a measured native assay. No exact direct companion is asserted by the declared
      census.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2483-grounding-owner
    - bgc-2483-chemistry
    - bgc-2483-source-mibig_compounds
    - bgc-2483-query-chebi_structures
    - bgc-2483-direct-contexts
    - bgc-2483-source-chebi_structures
- assessment_id: bgc-2483-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: Both neutral saved forms contain35 atoms and38 bonds; all ten comparisons
    are true and the direct map spans35 atoms, with full_graph_identity_established:false
    retained. Seven tetrahedral centers are specified with no additional unspecified
    potential centers in these results. The literal true flag is consistent with the
    maintained tetrahedral check; it does not independently prove natural stereochemistry
    or every positional name.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-grounding-owner
  - bgc-2483-chemistry
  - bgc-2483-topology
  - bgc-2483-diagnostic-reading
  - bgc-2483-diagnostic-acceptance
  - bgc-2483-structure-schema
  - bgc-2483-stereo-method
  - bgc-2483-source-chebi_structures
  dimensions:
  - name: stereochemistry_scope
    value: Both neutral saved forms contain35 atoms and38 bonds; all ten comparisons
      are true and the direct map spans35 atoms, with full_graph_identity_established:false
      retained. Seven tetrahedral centers are specified with no additional unspecified
      potential centers in these results. The literal true flag is consistent with
      the maintained tetrahedral check; it does not independently prove natural stereochemistry
      or every positional name.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2483-grounding-owner
    - bgc-2483-chemistry
    - bgc-2483-topology
    - bgc-2483-diagnostic-reading
    - bgc-2483-diagnostic-acceptance
    - bgc-2483-structure-schema
    - bgc-2483-stereo-method
    - bgc-2483-source-chebi_structures
  - name: representation_correspondence
    value: All ten stored-form comparisons are true and the direct map spans atom
      counts; full_graph_identity_established remains false. Natural identity, tautomer
      preference and complete stereochemistry are not established by these booleans.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2483-grounding-owner
    - bgc-2483-chemistry
    - bgc-2483-topology
    - bgc-2483-diagnostic-reading
    - bgc-2483-diagnostic-acceptance
    - bgc-2483-structure-schema
    - bgc-2483-stereo-method
    - bgc-2483-source-chebi_structures
- assessment_id: bgc-2483-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: BGC0001508 version 3 retains Penicillium roqueforti NCBITaxon:5082 as SOURCE_ASSERTION
    and KY349137.1 as a CLUSTER_UNSTATED locus without declared coordinates or methods.
    Seven ChEBI origin rows plus one LOTUS row contain six source taxon IDs; they
    remain occurrence annotations, not six proven producers. The FO-3929 strain comment
    belongs specifically to P.simplicissimum69488. Source Penicillium camponotum at2072477
    and cached P.camponoti remain separately labelled; no current spelling/taxonomic
    correction is asserted.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-origin-owner
  - bgc-2483-occurrence-owner
  - bgc-2483-source-mibig_compounds
  - bgc-2483-cached-taxonomy
  - bgc-2483-taxonomy-routes
  - bgc-2483-curation-scope
  - bgc-2483-direct-contexts
  - bgc-2483-source-lotus_occurrences
  - bgc-2483-source-chebi_origins
  dimensions:
  - name: taxon_scope
    value: BGC0001508 version 3 retains Penicillium roqueforti NCBITaxon:5082 as SOURCE_ASSERTION
      and KY349137.1 as a CLUSTER_UNSTATED locus without declared coordinates or methods.
      Seven ChEBI origin rows plus one LOTUS row contain six source taxon IDs; they
      remain occurrence annotations, not six proven producers. The FO-3929 strain
      comment belongs specifically to P.simplicissimum69488. Source Penicillium camponotum
      at2072477 and cached P.camponoti remain separately labelled; no current spelling/taxonomic
      correction is asserted.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2483-origin-owner
    - bgc-2483-occurrence-owner
    - bgc-2483-source-mibig_compounds
    - bgc-2483-cached-taxonomy
    - bgc-2483-taxonomy-routes
    - bgc-2483-curation-scope
    - bgc-2483-direct-contexts
    - bgc-2483-source-lotus_occurrences
    - bgc-2483-source-chebi_origins
  - name: producer_evidence
    value: BGC0001508 version 3 retains Penicillium roqueforti NCBITaxon:5082 as SOURCE_ASSERTION
      and KY349137.1 as a CLUSTER_UNSTATED locus without declared coordinates or methods.
      Seven ChEBI origin rows plus one LOTUS row contain six source taxon IDs; they
      remain occurrence annotations, not six proven producers. The FO-3929 strain
      comment belongs specifically to P.simplicissimum69488. Source Penicillium camponotum
      at2072477 and cached P.camponoti remain separately labelled; no current spelling/taxonomic
      correction is asserted.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2483-origin-owner
    - bgc-2483-occurrence-owner
    - bgc-2483-source-mibig_compounds
    - bgc-2483-cached-taxonomy
    - bgc-2483-taxonomy-routes
    - bgc-2483-curation-scope
    - bgc-2483-direct-contexts
    - bgc-2483-source-lotus_occurrences
    - bgc-2483-source-chebi_origins
  - name: locus_evidence
    value: BGC0001508 version 3 retains Penicillium roqueforti NCBITaxon:5082 as SOURCE_ASSERTION
      and KY349137.1 as a CLUSTER_UNSTATED locus without declared coordinates or methods.
      Seven ChEBI origin rows plus one LOTUS row contain six source taxon IDs; they
      remain occurrence annotations, not six proven producers. The FO-3929 strain
      comment belongs specifically to P.simplicissimum69488. Source Penicillium camponotum
      at2072477 and cached P.camponoti remain separately labelled; no current spelling/taxonomic
      correction is asserted.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2483-origin-owner
    - bgc-2483-occurrence-owner
    - bgc-2483-source-mibig_compounds
    - bgc-2483-cached-taxonomy
    - bgc-2483-taxonomy-routes
    - bgc-2483-curation-scope
    - bgc-2483-direct-contexts
    - bgc-2483-source-lotus_occurrences
    - bgc-2483-source-chebi_origins
- assessment_id: bgc-2483-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: MIBiG ENTRY PMID28529508, each ChEBI origin citation/comment and the LOTUS
    DOI preserve their source roles. The two P.roqueforti origin rows cite PMID15826038
    and PMID19837474 separately; PMID27616792 is shared by the P.camponotum, P.cataractarum
    and P.costaricense rows. Repeated taxon placements and overlapping article references
    do not establish independent experiments. All three seed-history events are retained.
    The inhibitor phrase in the ChEBI definition is not a freshly checked primary
    assay.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-owner
  - bgc-2483-history-owner
  - bgc-2483-origin-owner
  - bgc-2483-occurrence-owner
  - bgc-2483-source-mibig_compounds
  - bgc-2483-source-reading
  - bgc-2483-root-source-reading
  - bgc-2483-source-lotus_occurrences
  - bgc-2483-source-chebi_structures
  - bgc-2483-source-chebi_origins
  dimensions:
  - name: citation_scope
    value: MIBiG ENTRY PMID28529508, each ChEBI origin citation/comment and the LOTUS
      DOI preserve their source roles. The two P.roqueforti origin rows cite PMID15826038
      and PMID19837474 separately; PMID27616792 is shared by the P.camponotum, P.cataractarum
      and P.costaricense rows. Repeated taxon placements and overlapping article references
      do not establish independent experiments. All three seed-history events are
      retained. The inhibitor phrase in the ChEBI definition is not a freshly checked
      primary assay.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2483-owner
    - bgc-2483-history-owner
    - bgc-2483-origin-owner
    - bgc-2483-occurrence-owner
    - bgc-2483-source-mibig_compounds
    - bgc-2483-source-reading
    - bgc-2483-root-source-reading
    - bgc-2483-source-lotus_occurrences
    - bgc-2483-source-chebi_structures
    - bgc-2483-source-chebi_origins
- assessment_id: bgc-2483-occurrence
  area: evidence
  topic: Source-specific occurrence and assay assertions
  outcome: supported
  summary: All eight source occurrence placements are retained with their taxon/reference
    scope. The complete owner has no native bioactivity, causal graph, pathway, component-reference
    or molecular-target root, and no exact saved PubChem/BindingDB assay supplies
    a potency result. A definition-level farnesyltransferase-inhibitor statement does
    not justify adding a target or transferring activity to every occurrence.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-occurrence-owner
  - bgc-2483-mechanism-absence
  - bgc-2483-query-lotus_occurrences
  - bgc-2483-query-chebi_origins
  - bgc-2483-query-cyanometdb_occurrences
  - bgc-2483-query-pubchem_bioassay
  - bgc-2483-query-bindingdb_targets
  - bgc-2483-query-antibioticmech_inchikeys
  - bgc-2483-cached-taxonomy
  - bgc-2483-taxonomy-routes
  - bgc-2483-taxonomy-reading
  - bgc-2483-curation-scope
  - bgc-2483-bioactivity-seeder
  - bgc-2483-root-source-reading
  - bgc-2483-source-lotus_occurrences
  - bgc-2483-source-chebi_origins
  dimensions:
  - name: occurrence_scope
    value: All eight source occurrence placements are retained with their taxon/reference
      scope. The complete owner has no native bioactivity, causal graph, pathway,
      component-reference or molecular-target root, and no exact saved PubChem/BindingDB
      assay supplies a potency result. A definition-level farnesyltransferase-inhibitor
      statement does not justify adding a target or transferring activity to every
      occurrence.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2483-occurrence-owner
    - bgc-2483-mechanism-absence
    - bgc-2483-query-lotus_occurrences
    - bgc-2483-query-chebi_origins
    - bgc-2483-query-cyanometdb_occurrences
    - bgc-2483-query-pubchem_bioassay
    - bgc-2483-query-bindingdb_targets
    - bgc-2483-query-antibioticmech_inchikeys
    - bgc-2483-cached-taxonomy
    - bgc-2483-taxonomy-routes
    - bgc-2483-taxonomy-reading
    - bgc-2483-curation-scope
    - bgc-2483-bioactivity-seeder
    - bgc-2483-root-source-reading
    - bgc-2483-source-lotus_occurrences
    - bgc-2483-source-chebi_origins
  - name: assay_target_scope
    value: No native or exact saved AID/BindingDB assay is available. The retained
      source definition may motivate later verification, but gives no locally verified
      assay modality, numerical potency, construct or causal target evidence here.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2483-occurrence-owner
    - bgc-2483-mechanism-absence
    - bgc-2483-query-lotus_occurrences
    - bgc-2483-query-chebi_origins
    - bgc-2483-query-cyanometdb_occurrences
    - bgc-2483-query-pubchem_bioassay
    - bgc-2483-query-bindingdb_targets
    - bgc-2483-query-antibioticmech_inchikeys
    - bgc-2483-cached-taxonomy
    - bgc-2483-taxonomy-routes
    - bgc-2483-taxonomy-reading
    - bgc-2483-curation-scope
    - bgc-2483-bioactivity-seeder
    - bgc-2483-root-source-reading
    - bgc-2483-source-lotus_occurrences
    - bgc-2483-source-chebi_origins
- assessment_id: bgc-2483-classification
  area: consistency
  topic: Reported model families and bounded structural compatibility
  outcome: supported
  summary: The source PKS category, ChEBI19-oxosteroid description and versioned Tetraketide
    meroterpenoids model label answer different questions. The fused-ring/aldehyde/ester
    topology is compatible with the retained structural description; neither topology
    nor model output independently establishes the PKS/terpene biosynthetic contribution.
    The UNCLASSIFIED filing and exact model arrays are preserved without treating
    model labels as source assertions.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-classification-owner
  - bgc-2483-source-npclassifier
  - bgc-2483-chemistry
  - bgc-2483-topology
  - bgc-2483-structure-schema
  - bgc-2483-classification-seeder
  - bgc-2483-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: The source PKS category, ChEBI19-oxosteroid description and versioned Tetraketide
      meroterpenoids model label answer different questions. The fused-ring/aldehyde/ester
      topology is compatible with the retained structural description; neither topology
      nor model output independently establishes the PKS/terpene biosynthetic contribution.
      The UNCLASSIFIED filing and exact model arrays are preserved without treating
      model labels as source assertions.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2483-classification-owner
    - bgc-2483-source-npclassifier
    - bgc-2483-chemistry
    - bgc-2483-topology
    - bgc-2483-structure-schema
    - bgc-2483-classification-seeder
    - bgc-2483-source-mibig_compounds
- assessment_id: bgc-2483-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: Both complete molecular forms, all actual intake inputs, raw/history and
    complete saved source payloads are read. Structural consistency and retained annotation
    scope are supported locally; primary natural identity, producer experiments and
    inhibitor protocol remain unverified. The review remains partial without a demonstrated
    source-edit defect.
  target_ids:
  - CHEBI:142842
  evidence_ids:
  - bgc-2483-owner
  - bgc-2483-capture
  - bgc-2483-intake
  - bgc-2483-intake-acceptance
  - bgc-2483-history-owner
  - bgc-2483-diagnostic-reading
  - bgc-2483-diagnostic-acceptance
  - bgc-2483-diagnostic-execution
  - bgc-2483-source-reading
  - bgc-2483-root-source-reading
  - bgc-2483-joint-source-notes
  - bgc-2483-source-plan-execution
  - bgc-2483-source-plan-acceptance
  - bgc-2483-native-gate-limits
  - bgc-2483-curation-scope
  - bgc-2483-mechanism-absence
  dimensions:
  - name: review_completion
    value: Both complete molecular forms, all actual intake inputs, raw/history and
      complete saved source payloads are read. Structural consistency and retained
      annotation scope are supported locally; primary natural identity, producer experiments
      and inhibitor protocol remain unverified. The review remains partial without
      a demonstrated source-edit defect.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2483-owner
    - bgc-2483-capture
    - bgc-2483-intake
    - bgc-2483-intake-acceptance
    - bgc-2483-history-owner
    - bgc-2483-diagnostic-reading
    - bgc-2483-diagnostic-acceptance
    - bgc-2483-diagnostic-execution
    - bgc-2483-source-reading
    - bgc-2483-root-source-reading
    - bgc-2483-joint-source-notes
    - bgc-2483-source-plan-execution
    - bgc-2483-source-plan-acceptance
    - bgc-2483-native-gate-limits
    - bgc-2483-curation-scope
    - bgc-2483-mechanism-absence
findings: []
actions: []
limitations:
- Retained local evidence only; fresh primary literature, current authority/taxonomy,
  assay protocols and independent natural identity/stereochemical authentication remain
  unavailable.
- Five local commands passed; full QC and OAK remain unavailable. Four diagnostic
  warnings remain global and unassigned. Normalized identifiers and counts do not
  establish full graph or natural identity.
- Producer, locus, occurrence, strain and citation tiers remain separate; repeated
  references and target-enriched assay rows do not establish independent experiments.
- Model-family applicability stays qualified. Anditomin historical enzyme/sequence
  claims are not freshly validated; Antimycin A and selected stereo-unspecified A1B
  retain distinct assay and identity scopes.
- Both complete molecular forms, all actual intake inputs, raw/history and complete
  saved source payloads are read. Structural consistency and retained annotation scope
  are supported locally; primary natural identity, producer experiments and inhibitor
  protocol remain unverified. The review remains partial without a demonstrated source-edit
  defect.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all first-five ten complete forms:604 atom/636 bond rows and191
  actual intake placements/47 paths. No new molecular parse.
- 'Source reading is disjoint: BGC contexts0–3/36 frames/22 rows/225 fields; ROOT
  context4/9 frames/185 rows/1990 fields; Support contexts5–9/45 frames/15 rows/200
  fields. Native cache/curation receives zero positive-row credit.'
- BGC operated original collector/composer; Support operated canonical intakes; Native
  operated diagnostic and maintained readers under ROOT delegation. These fragments
  consume saved results only.
- No first-five source-edit finding is proposed. Separate A1B findings remain in Support’s
  last-five review and are not transferred to Antimycin A.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-249
```
