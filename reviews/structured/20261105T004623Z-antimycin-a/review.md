# Local evidence review: antimycin A

- Review: 20261105T004623Z-antimycin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T23:57:06.261665Z
- Finished UTC: 2026-11-05T00:46:23.150875Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Antimycin A retains a stereospecified dilactone encoding, a characterized source BGC and a large set of assay-specific annotations. Its amide/imidic representations and selected stereo-unspecified A1B comparison remain distinct. The172 retained assay rows,25 written activities and147 further results do not collapse into a single potency, direct-binding mechanism or independent-experiment count.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2485; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:2762 | data/natural_products/unclassified/antimycin-a.yaml | generated | antimycin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:2762 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:2762 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:2762 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:2762 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:2762 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:2762 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:2762 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:2762 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: CHEBI:2762.

CHEBI:2762, CID14957 and full key UIFFUZWRFRDZJC-SBOOETFBSA-N identify the selected stereospecified C28H40N2O9 encoding. Already-selected Antimycin A1B has the same formula/connectivity block but full key UIFFUZWRFRDZJC-UHFFFAOYSA-N and CID12550, with five unspecified tetrahedral centers. The same-form nonisomeric strings agree across these selected encodings, while their stereochemical scope differs. This explicit comparison is not a census BGC companion, name-based deduplication, congener identity proof or permission to transfer A1B5/7nM target claims.

### Stored-form topology and stereochemical scope

representation: supported. Targets: CHEBI:2762.

Both neutral selected forms contain39 atoms/40 bonds and reproduce the declared normalized InChI/full key. Their canonical isomeric and nonisomeric SMILES differ and direct correspondence is empty: SMILES C19(=O20)-N18H and formamide C28(=O29)-N27H become two C(OH)=N sites in the regenerated form. Five specified tetrahedral centers persist; two additional unspecified C=N potentials are representation-dependent. The literal stereo_complete:true is scoped to the maintained tetrahedral test, not complete imine geometry or natural-state proof. A1B instead leaves the five tetrahedral centers unspecified.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: CHEBI:2762.

BGC0000958 version5 retains Streptomyces sp.S4 NCBITaxon:889487 as BGC_CHARACTERIZED and a distinct CLUSTER_DEMONSTRATED locus NZ_FR873698.1:81953–106578 with four reported methods. Nine LOTUS source placements reconcile to seven exact owner taxon/DOI occurrence tuples. The saved67295→1911 forward merge and source S.setonii versus cached S.griseus (with S.setonii synonym) remain explicit; this cached reconciliation does not freshly validate taxonomy, producing strains or causal production in every occurrence.

### Citation tiers and complete history scope

evidence: supported. Targets: CHEBI:2762.

MIBiG ENTRY PMID21857911, each LOTUS occurrence DOI, exact PubChem AID/PMID/target tuples and the retained AntibioticMech link keep their distinct evidentiary tiers. Repeated assay rows, target-enriched rows and article placements are not independent experiments. All four seed-history events are retained. The ANTIFUNGAL summary is traceable to the exact full-key AntibioticMech row at pinned commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976; it is not a newly verified native antifungal experiment.

### Source-specific occurrence and assay assertions

evidence: supported. Targets: CHEBI:2762.

ROOT personally read all172 retained PubChem assay rows, with all fields, and the remaining13 source rows for this owner. The source-to-owner reconciliation preserves25 written bioactivities plus a note about147 further results. Deposited ACTIVE, INACTIVE and INCONCLUSIVE calls remain assay-specific; INCONCLUSIVE maps to NOT_DETERMINED. Numeric values attached to inactive or inconclusive calls do not reverse those calls. Source Potency remains endpoint OTHER rather than inferred IC50, EC50 or MIC. LOTUS detection and the separate AntibioticMech ANTIFUNGAL annotation do not establish a common mechanism or potency.

### Reported model families and bounded structural compatibility

consistency: supported. Targets: CHEBI:2762.

The versioned Antimycins/Macrolides model output is compatible with the observed dilactone/amide structural family, while source NRPS&#124;PKS remains a separate biosynthetic annotation. The specific model label and ChEBI description are retained with their own provenance; neither computed family nor structural compatibility independently establishes direct binding, an antifungal mechanism, a natural congener mixture or exact biosynthetic experiments.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: CHEBI:2762.

Own complete raw/history, first-five intake and molecular reading are joined to ROOT’s complete context4 source reading (9 frames/185 rows/1990 fields) and Native’s bounded cache/curation reconciliation. No exact current assay exclusion applies, but that finite table result does not validate protocols or resolve assay discordance. Representation and congener-stereochemistry limits, source-specific activity semantics and unavailable primary verification keep this review partial without transferring the separate A1B findings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2485-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/antimycin-a.yaml; Complete plaintext including every curation_history entry | supports | Complete antimycin A owner with 4 history events; prior complete raw reading carries with current identical bytes. No source/status/history edit. |
| bgc-2485-capture | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2485-intake | /private/tmp/npm-review-work/shared-next-batch249/intakes/2485-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, ownership and all 41 input placements joined to current plan hashes. |
| bgc-2485-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/4 | supports | ROOT accepted the original canonical intake and exact supplemental plan; this owner’s actual inspection and receipt pins are located. |
| bgc-2485-grounding-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/label; /records/4/owner_document/definition; /records/4/owner_document/definition_source; /records/4/owner_document/chemical_structure; /records/4/owner_document/xrefs; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status | supports | Exact retained identifier, structure, source concepts, definition where present, cross-references and grounding fields. Historical annotations are not fresh authority searches. |
| bgc-2485-origin-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/producer_taxon_groups; /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, declared coordinates and citation tiers; absent fields are not filled. |
| bgc-2485-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete owner supplies exact occurrence, activity and nested target assertions or bounded absence. Detection does not prove production; absent assays do not mean inactivity. |
| bgc-2485-classification-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway; /records/4/owner_document/bgc_class | supports | Exact named/versioned model arrays, glycoside flag, filing and separate source categories; retention fidelity is not biological-family or biosynthetic proof. |
| bgc-2485-history-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document/curation_status; /records/4/owner_document/curation_history | supports | All history events and status are preserved; seeding/import remains distinct from fresh primary verification. |
| bgc-2485-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets roots; no maintained reader applies. Its 25 native bioactivities and any nested target annotations remain separately retained. |
| bgc-2485-chemistry | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence; /records/4/smiles/computed/formula; /records/4/smiles/computed/formal_charge; /records/4/smiles/computed/standard_inchi; /records/4/smiles/computed/standard_inchi_key; /records/4/smiles/computed/canonical_isomeric_smiles; /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/atom_count; /records/4/smiles/computed/heavy_atom_count; /records/4/smiles/computed/bond_count; /records/4/smiles/computed/element_counts; /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/formula; /records/4/inchi/computed/formal_charge; /records/4/inchi/computed/standard_inchi; /records/4/inchi/computed/standard_inchi_key; /records/4/inchi/computed/canonical_isomeric_smiles; /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/atom_count; /records/4/inchi/computed/heavy_atom_count; /records/4/inchi/computed/bond_count; /records/4/inchi/computed/element_counts; /records/4/inchi/computed/stereo_counts | supports | Eight of ten comparisons are true: normalized InChI/full key, formula, charge and atom/bond counts agree, but both canonical SMILES comparisons are false and direct atom correspondence is empty. Natural identity, tautomer preference and complete stereochemistry are not established by these booleans. |
| bgc-2485-topology | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings; /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/motifs; /records/4/smiles/computed/fragment_atom_indices; /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/motifs; /records/4/inchi/computed/fragment_atom_indices | supports | The saved SMILES contains a nine-membered dilactone ring, with C10(=O11)-O9-C8 and C15(=O16)-O14-C13, plus external ester C33(=O34)-O32-C7 and an aromatic amide/formamide region. The regenerated form keeps three ester motifs but replaces both amides by C14(OH30)=N28 and C25(OH33)=N29. No saturated C5O candidate sugar cycle is present. This is bounded structural support for an antimycin-type dilactone; it does not identify an assay mechanism or natural tautomer. |
| bgc-2485-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-first-five-diagnostic-reading-001.json; /records/4; /read_scope; /totals; /representation; /reading_caveats; /reader | supports | BGC personally read all ten complete first-five forms:604 atom and636 bond rows and all191 intake placements/47 paths. Whole Anditomin graph/history meanings factor to exact actual full-owner preservation; saved-result limits and display recovery are recorded. |
| bgc-2485-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/4; /molecular_parse_attempts; /parsed; /global_warning_count; /method_scope; /interpretation_boundary | supports | ROOT accepted the original twenty stored forms. This owner’s actual comparison scope is located; four warnings remain global and unassigned. No alternate parse or normalization repair is inferred. |
| bgc-2485-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins; stream interpretation is supplied separately. |
| bgc-2485-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–433 | supports | Undefined stereocenters remain explicit; named/versioned computed classification is never a source assertion. |
| bgc-2485-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines165–173 | supports | The maintained stereo_complete flag tests unassigned tetrahedral centers; natural identity and double-bond geometry need their separate evidence scopes. |
| bgc-2485-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines295–306;988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2485-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines126–145;1318–1382 | supports | Source assay calls, endpoint values and target accessions are retained. Activity classes use assay-name matching on active rows and summaries derive from written classes; these are not independent potency measurements or protocol validation. |
| bgc-2485-source-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-assigned-source-reading-001.json; /selected_indices; /reading; /counts; /frames; /cautions | supports | BGC personally read contexts0–3:36 complete frames/22 rows/225 fields, including the Anditomin blank-AID sentinel. This does not claim ROOT’s Antimycin source-row credit. |
| bgc-2485-root-source-reading | /private/tmp/npm-review-work/shared-next-batch249/root-current249-source-row-reading-001.json; /context_indices; /named_query_frames; /positive_row_placements; /positive_row_fields; /whole_payload_readings; /scientific_cautions | supports | ROOT personally read Antimycin A context4:9 complete frames/185 rows/1990 fields, including all172 assay rows. Attribution remains ROOT; no duplicate source-row credit. |
| bgc-2485-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Complete disjoint source reading covers90 frames/222 rows/2415 fields: BGC22, ROOT185 and Support15 rows. Native cache/curation has zero positive-row credit; overlapping readings add none. |
| bgc-2485-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch249/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /notes; /verification; /supplement_scope | supports | One original composer produced historical plan001 at379 placements/51 paths. Inventory and original source counts remain unchanged; the separate accepted supplement adds three A1B rule/transform inputs only. |
| bgc-2485-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-target-input-plan-acceptance-001.json; /status; /accepted; /plan; /original_plan; /supplement_derivation; /source_placements; /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification | supports | ROOT accepted supplemental plan002 at382 placements/54 paths. Only2486 gains three rule/transform inputs; no source query, context or positive-row count is added. |
| bgc-2485-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch249/root-current249-native-gates-acceptance-001.json; /status; /counts; /all_native_gates_passed; /unavailable | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed is false. Local validation does not complete scientific verification. |
| bgc-2485-curation-scope | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | The bounded Native scan found no applicable implemented correction/exclusion and26 unrelated lexical hits. No exact assay exclusion applies among172 retained tuples; one blank sentinel remains separate. |
| bgc-2485-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/whole_stanzas/14; /cached_taxonomy/whole_stanzas/20 | supports | Complete saved cache names and synonyms for this owner’s source taxon IDs. They do not independently validate taxonomic rank, source strain labels, occurrence or production; no fresh taxonomy lookup. |
| bgc-2485-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/source_taxa; /contexts/4/source_scope_inventory/forward_taxon_merge_matches; /contexts/4/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and saved forwarding/nonorganism routes for this owner; no fresh taxonomy request. |
| bgc-2485-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /forward_routes; /interpretation | supports | Native personally read all26 saved cache stanzas/10 routes, including67295→1911. Cached names/synonyms and routes do not upgrade species, strain, occurrence or producer evidence. |
| bgc-2485-direct-contexts | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json; /records/4/proposed_companion_paths; /records/4/direct_companion_predicates | supports | Exact declared one-hop direct map is empty for this batch. Selected Antimycin identity comparison is separate; no transitive expansion or biological claim transfer is inferred. |
| bgc-2485-selected-identity-comparison | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/4/owner_document; /records/5/owner_document | supports | Selected Antimycin A and A1B have distinct full stereokeys/CIDs and specified versus unspecified tetrahedral encodings; complete owners retain different sources, histories and activity/target assertions. No name-based deduplication or assay transfer. |
| bgc-2485-selected-comparison-source | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds; /contexts/4/source_scope_inventory/joins/pubchem_bioassay; /contexts/4/source_scope_inventory/joins/bindingdb_targets; /contexts/5/source_scope_inventory/joins/mibig_compounds; /contexts/5/source_scope_inventory/joins/pubchem_bioassay; /contexts/5/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained identity-bearing MIBiG rows and exact assay/target frames for both selected owners. Antimycin A assays remain separate from A1B BindingDB5/7nM target rows. |
| bgc-2485-selected-comparison-plan | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json; /records/4/identity_comparison_paths; /records/4/additional_context_roles | supports | Explicit already-selected encoded-identity comparison input; separate from the empty direct census map and adds no source-query context. |
| bgc-2485-selected-comparison-chemistry | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/comparisons; /records/4/atom_correspondence; /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence; /records/4/smiles/computed/formula; /records/4/smiles/computed/canonical_isomeric_smiles; /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/formula; /records/4/inchi/computed/canonical_isomeric_smiles; /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/stereo_counts; /records/5/smiles/computed/formula; /records/5/smiles/computed/canonical_isomeric_smiles; /records/5/smiles/computed/canonical_nonisomeric_smiles; /records/5/smiles/computed/potential_stereo; /records/5/smiles/computed/stereo_counts; /records/5/inchi/computed/formula; /records/5/inchi/computed/canonical_isomeric_smiles; /records/5/inchi/computed/canonical_nonisomeric_smiles; /records/5/inchi/computed/potential_stereo; /records/5/inchi/computed/stereo_counts | supports | Exact paired encodings: Antimycin A has five specified tetrahedral centers, A1B five unspecified. Same-form nonisomeric strings and formulas agree across owners, while full stereokeys and isomeric encodings differ. Neither comparison establishes congener identity or transfers activity. |
| bgc-2485-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2485-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines 1057–1057; row_sha256 97df00d60282c01b48884ee49997a5907e033a94abb1a7014036145e07ad8d4f | supports | Exact compound/version, structure/key, database IDs, producer/locus grades and citation tiers. ROOT complete source reading has primary positive-row credit; current physical bytes are independently joined. |
| bgc-2485-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2485-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line1; physical lines 409–409; row_sha256 45ac22cebad66676397fd469739ebb4b462522a3a1374dedf4ee7351a137ba28 | supports | Exact retained ChEBI identifier/full key/label/definition/structure fields with source grounding; no fresh authority lookup. ROOT complete source reading has primary positive-row credit; current physical bytes are independently joined. |
| bgc-2485-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame has 9 placements with exact query, predicate and all matched fields. |
| bgc-2485-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line1; physical lines 8747–8747; row_sha256 1a85840348053c39ebffaffab73cba119084810bf4922d0d707b8f3bbb97d91b; physical lines 8748–8748; row_sha256 5ca7f07a84bbe5db5d2f0be7c0cb597176c21d535a712bd44ada5fcd196b3ade; physical lines 8749–8749; row_sha256 bebd7c888716609f8899ae87f65b6e90f847cecf93afe9d158bae9ab22285da8; physical lines 8750–8750; row_sha256 28566fc6cefff287adbcebf2001ad7c7f93862376216bd1ec8b3cbafd96294fc; physical lines 8751–8751; row_sha256 8b35cbdcf4bdbf15930329ab32d82784a5a6d5b52a6a1d6ecfa5077023a22653; physical lines 8752–8752; row_sha256 a1511c98601131a087c81ee1be22c0c678c56fb11de0a26c25c4312e8f91a1d0; physical lines 8753–8753; row_sha256 86d8b8f763b90a90aea51a87a2af780c85fd71c91b949aa4ba982c9892c02cc5; physical lines 8754–8754; row_sha256 1598968c1976dcaa6aea704d5a902e855946115915731ebe0075b2842c2ddc8a; physical lines 8755–8755; row_sha256 7eaebfe3a87a139d2295c3236e97b999193da2688148fd2684ef55f2243b5fb5 | supports | Complete organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. ROOT complete source reading has primary positive-row credit; current physical bytes are independently joined. |
| bgc-2485-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2485-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2485-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines 2401–2401; row_sha256 10822436f99fc008e6faa80e17bf58e4c26e1dc492196851aabc0b706cc918df | supports | Exact named/versioned model arrays and glycoside flag; applicability is assessed separately. ROOT complete source reading has primary positive-row credit; current physical bytes are independently joined. |
| bgc-2485-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame has 172 placements with exact query, predicate and all matched fields. |
| bgc-2485-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line1; physical lines 8064–8064; row_sha256 f7e024fcde4f722169d7eaad769bcb9cd88e47d82146f2375c2609aa7060c7f5; physical lines 8065–8065; row_sha256 b50607dbfe6918dbb4eed58eeac1e505a6a2858e900fd9993ba17c2e5c8ca5c2; physical lines 8066–8066; row_sha256 77634d229b3dd810e3ae631e48c9f2a2d57cae824baa15ff2375149c059743c7; physical lines 8067–8067; row_sha256 2d10d95f4d3067d8cb09b4da550bd52aea9e313feef8fbfaf132b3a1de3c92dc; physical lines 8068–8068; row_sha256 1cf00a74f0cf728d6fd2a2e6a724e106620c7832f7cd62aae275e4b4e65c4589; physical lines 8069–8069; row_sha256 5ee967537445d72c992d351d197a1d61f08b21fff769711fadb7151ba59d7153; physical lines 8070–8070; row_sha256 43453be82786e3894169a88663970f93ba5ce1b40d6536f2a8ae7630bc345913; physical lines 8071–8071; row_sha256 a4359c0afe33300bb6fdd38f122afba00e7f353f1b0a63a80bf5d4da08251166; physical lines 8072–8072; row_sha256 dee3aa439d6947b051b788f3c2ac42a0c0eb4729c6c2e906695e711984538215; physical lines 8073–8073; row_sha256 5668e926aa60b5859ad133942e85870523408578f5a4e032ba7c5fd218721030; physical lines 8074–8074; row_sha256 3f9312ef7cc0ad084a787af7b77288850f3c002ee99784611fcf8e7a765d9234; physical lines 8075–8075; row_sha256 d4ed509c630aedb5152b49b8033725c35f5d41571eaa7629b9987189cab232a1; physical lines 8076–8076; row_sha256 db8e2ea60c84b4affd73f2b90ab7e251d8090b2121aed71ba35e20c3e196eed4; physical lines 8077–8077; row_sha256 ff817a5f50c15fc8238d1ac3332618748e7b354e7f171918cb4011e5afe6d0f8; physical lines 8078–8078; row_sha256 6dc17d8fb44d5a29a53842c5df653c683697090fe619fcaf56b33480afe4f862; physical lines 8079–8079; row_sha256 6a348b71c798fe66facd82df86e5d94a506e3f7f7a96879602091668f00c0cec; physical lines 8080–8080; row_sha256 dcde25bbf30f6d2dd2818e4211cfea4d2f4b3e7110e5b501bb461da71945de78; physical lines 8081–8081; row_sha256 d424b6deafb23c26132b5c10fbecb537cd3ee83e3cafa13c28bb1e7358358737; physical lines 8082–8082; row_sha256 389df546c0fdcfbb4ab73e0aa566f93565f5d7148816468626abe1d2263a7087; physical lines 8083–8083; row_sha256 719d4203b3f2ec7f7624b1f32aa4cc9dc69f9116afb2d024a3210a5c48bc26d0; physical lines 8084–8084; row_sha256 8ccdd32ccddeb2ed44bd436bdc01586f1ca1369766b7f5aa812803fd9fda92ee; physical lines 8085–8085; row_sha256 34b3665639bf20cfb290b085e3a4fbd69c8b7feb50ed70547dba77d303fb8699; physical lines 8086–8086; row_sha256 aa3abeed257319dcdb38da4560dd8ed30dbd25978289bd992b9ff2a280b0e445; physical lines 8087–8087; row_sha256 27150deba2083f05882317eff7e68cdcb40559f4f61d3095b25842e3e60c0263; physical lines 8088–8088; row_sha256 e8731f3759957375c02a791052a81f6bd0f02a2da799e5926d351486ffa57c2a; physical lines 8089–8089; row_sha256 090aabf570a6dfb026cf6ad7292d699855802da7fd1873af4825181a732e66cc; physical lines 8090–8090; row_sha256 2dca1d79f2ae984c6a0b43b265cd5d489f95fdb9f645058d5db06eafe5a26360; physical lines 8091–8091; row_sha256 d99b1174ded220ed4e85d91c50bd08fc6ec50592559aed04df23521e93c5d4f2; physical lines 8092–8092; row_sha256 55c1e0156092a8ce67740b7ea29e55fe39fb27c4b1bf8705aef6e95a3de23f3d; physical lines 8093–8093; row_sha256 9ffd19d221cc4e37afd61e30f92c216e50ce2cd4973558c9f46111c16db10a24; physical lines 8094–8094; row_sha256 b7a79c7d5c3469e073414a07b4db57f1fc1ee1497afd4d3fb57c209e08495672; physical lines 8095–8095; row_sha256 6db509773fb1533d383f20209c1eef81a781edc7335173dc0f0045aadb27aaa4; physical lines 8096–8096; row_sha256 bad0a00e7bab9a724dcdce3f7104a40f6d59747076b7e069eb949d8cf395d092; physical lines 8097–8097; row_sha256 993f84c4b5ae350f33ab9781d325daca8109426f14635ac7bd51b9e4f9910d3c; physical lines 8098–8098; row_sha256 d7b998c8a1b8fc2eca334718834f106fb33ab0007c3af4f98d4c5b4eed582cfb; physical lines 8099–8099; row_sha256 20eb3347617eed4f61260d33379031f18f1ee680d931a0b1fed24b817624415c; physical lines 8100–8100; row_sha256 6d3b44438cab7de1cc782b1d15de75e322869bd7851a78acfd7cad5961d3b633; physical lines 8101–8101; row_sha256 7c2a2c963127d089b17460d8ca2f1ba48e236886f3c2f5ff55fa56fc03763ad0; physical lines 8102–8102; row_sha256 fd0552a3d8dda386e23974ae77b0e07b53df4bf0a369377c4262a9d2a0db63ce; physical lines 8103–8103; row_sha256 334087afc5a8f0d51633ae1044ead949ebf314afbfca61881c27cca41ba4d304; physical lines 8104–8104; row_sha256 c8742896093958d80832fb451a9162eb453cf9b255c6a91299eb2f8076389ef0; physical lines 8105–8105; row_sha256 d20e7829303afb61911e079147cb9ffa1e56e7ea962fbdef3950f88000b59c04; physical lines 8106–8106; row_sha256 08436ce5c7b146654029c4c5e7f0af1c49bcbfa355e2c626f6969fa0ba27dcdc; physical lines 8107–8107; row_sha256 fa5d054a7d68a7721696c2469c648c2670232708c42f26c97d3af4a66bb5d0b3; physical lines 8108–8108; row_sha256 8670f4638a47fa9128590dc7647b9798a79a16e5fdb089a81d8c68a32cee596e; physical lines 8109–8109; row_sha256 e9f61d8130dde6a46cf1b983ad0b90af183bfd43d8493608f9c8f5e5a21af510; physical lines 8110–8110; row_sha256 d780b8efc376644322437c414fac347fc0507e516721d774660c35834b39185a; physical lines 8111–8111; row_sha256 61cbd47692b631ca4e19d2de01c0d7593a12e7849e65c517e62d1ef2787c4887; physical lines 8112–8112; row_sha256 254e5e4c222688a8b1ec0d8f851d54c90b5377ea69cc65bf3fe2fb381c9e763f; physical lines 8113–8113; row_sha256 09db3601cc9b98aef7bb533d99f4c70f13ab232a088e621eebc27867f990d1a6; physical lines 8114–8114; row_sha256 6e93fb88fb54dcfc2cd0cebc6b220fb23a22f54d033edfd3ef1f90f993748f5a; physical lines 8115–8115; row_sha256 1fadfafa302d1c6d85948ff719f64f396ab9584db0b7990dabe28102b9a49fdc; physical lines 8116–8116; row_sha256 de11ea66618ed5a5ef63700daee9bb8a60a72ac022a268ade95dab4926153442; physical lines 8117–8117; row_sha256 8bd154480b5c32526029bd8a00eca17a5728e8b83a1acb215a45005fadccb31d; physical lines 8118–8118; row_sha256 c5814835054a455ed676b4ad2959e24fdcd3c2e110b27b72d6c8c31bf32232a5; physical lines 8119–8119; row_sha256 25f805a7bf495fe315f8e7119fd0978c87b3d35d2a394c180e307a84b16abe78; physical lines 8120–8120; row_sha256 5e40862316476e61dcc3c2fe8fd328ca84cd2599d3a21a272b595b453755a492; physical lines 8121–8121; row_sha256 425ba10d750577aec0c19846774350942466ab64819d2f4102e3013e88e019f4; physical lines 8122–8122; row_sha256 74910ee494f380e29627be8a92e71b3ae4e1b19710520df2ce6c14fdfd07984c; physical lines 8123–8123; row_sha256 e5d1678c151dcd70f61fdfdeed635f14752856e48e4e335d5ce33d6aa62394ef; physical lines 8124–8124; row_sha256 05091fdade03c1057a8a5b9dd65836799fa26da2a5fdb1f181fa0ad1fe9278b8; physical lines 8125–8125; row_sha256 356d806460783bbe520b592248fcd0decfa4ec87d3bb6116accd387f5e8c886a; physical lines 8126–8126; row_sha256 4c755e5ed546714e26b464ba56235a3e651e9a45e365bd785d9430661ca9a5d4; physical lines 8127–8127; row_sha256 7663e64a6a9bf1f1dab30a0a83c8add54629e8d4bacce63f0e0ea106c14e68d8; physical lines 8128–8128; row_sha256 80a1d6056f5f24c1a7dfc7a0b52f388f982441db6cae9291055bd9bd8be847bc; physical lines 8129–8129; row_sha256 5c10c0d11af82469e09f6ac36157e9bf7802dada802556533263d1593369f922; physical lines 8130–8130; row_sha256 33dcecedf4ec4846c227bb73a14a8fccb7a92271989e507a0efccd9a5b3ee707; physical lines 8131–8131; row_sha256 9b344ecf746643e542b84b9cabe2e19dcfd45f91429538212e34e58a2dac6631; physical lines 8132–8132; row_sha256 4b77ec86fe4a35d03edd75ec6f92594c92c7d7d434c19971c2a6f106dc903a6a; physical lines 8133–8133; row_sha256 10e3d63c30b4f3cd82c1b52abd089d149fe607abdb18248647f831d00e99a394; physical lines 8134–8134; row_sha256 57eff88630bd3fc55dbb4581fc2a563482a3f4b1b302092c934511e50fb67ef7; physical lines 8135–8135; row_sha256 eb1e9c3cab2de1d439a9d04e845d8e26b505a3905af62ffebd86655ee4256384; physical lines 8136–8136; row_sha256 3ce2aae7376b29f952eb8b645942afac513b7ea7043aad3d36d5f03ab7e38adf; physical lines 8137–8137; row_sha256 2dbc45f98c5e4a034beb09ec7d6c5a5421f62e698428a7cab437c91bd2dd7c5f; physical lines 8138–8138; row_sha256 0e5deb05d61db541dc161cfdf3c4a12501632f2e1cddb809c28e76d92fcdd3f5; physical lines 8139–8139; row_sha256 e224b9987b6f26fc934e49f0f19ead063b25b41e1e9df3093a0730f98db3bc54; physical lines 8140–8140; row_sha256 0c42fa99d89a748da1e2063a52b2de67fc01e4a6f5c6d11929b9cac50c37fff6; physical lines 8141–8141; row_sha256 cfa5edd8014fd202e75ec4acd4ea646426b04b82dde1c7f967b373cd9a6a9493; physical lines 8142–8142; row_sha256 72e1ff60889cc31b8e77957fba3a68d3b5744d19d252673f3b86da53cffc4503; physical lines 8143–8143; row_sha256 15ec7b5ac741d5dc2a0bc9a3e4aa6f3f160e36a0aa61744e01a093ac8f47ff42; physical lines 8144–8144; row_sha256 e4ed83530f9631190c89ebbe79eaabf03752748f4a7cdc66d30ac9c0cfdc2194; physical lines 8145–8145; row_sha256 c0a348202d3464e35a04d761dfb9d384a713fcff09489e061c9655a738a76aa5; physical lines 8146–8146; row_sha256 218da6b9721ce449f22f65e786a40d2cbe60385d245adc1b40595385171fdc17; physical lines 8147–8147; row_sha256 85706e19b4d9bb1e64b62dcbb8b5e472f0ac28f0abec8a99f837d37beaf13e02; physical lines 8148–8148; row_sha256 416240501e59b3114afcb69cff22762a99eb8191b50f754f3106612bacf1c980; physical lines 8149–8149; row_sha256 a7337538e68267a8468a5e6bdcc7230e0e5bbe1fedc625bb5d7274eb7249ba53; physical lines 8150–8150; row_sha256 509cb8b34e08749ceaeaf4de78ac367dac8d6956af99885fd4cc1596d7915232; physical lines 8151–8151; row_sha256 9aa3a229192b71c5f5233d86fc94432509e700715213db0e28d93f6a6dc31e5e; physical lines 8152–8152; row_sha256 1247386ee82d3634a51d83c2239cbbb92cd4d772c24df0a8df1fddf2def99462; physical lines 8153–8153; row_sha256 45028a5faff220c318054a55a9295c0fa2db4721a2e153c1d31a50ca977f3d1a; physical lines 8154–8154; row_sha256 4f9b4eb2cef97f02a909ab125ef3b0a8710da386117c351f907de35c61b18a85; physical lines 8155–8155; row_sha256 2e3a54b77cd80921b666942d14cb49a9c93ba5c9268d4238a2ac25cf6e35cbca; physical lines 8156–8156; row_sha256 f3ca0950ffda5e0da905b0f92ca2113b909bcec68de319667b6fc96bed9581a8; physical lines 8157–8157; row_sha256 b67e2b8e8c004d51070b3aad2ee652a01d24858b9eb28e27b942ff09796d445d; physical lines 8158–8158; row_sha256 0c154c95276f91725fb532853c8dea17c2229ced2c74b917a61bc7ae181e3e8e; physical lines 8159–8159; row_sha256 51827e663d30b2090ea05b115165955233599f075c992e3337a17247c20de506; physical lines 8160–8160; row_sha256 8d351959549263cbbb654c6d5b5a56ee79bece432a8b4a83fbf046ce4cf19eeb; physical lines 8161–8161; row_sha256 0bc306775c6597418bb9a9561907592288bfa1f50428ec722e22b0225c5cb94a; physical lines 8162–8162; row_sha256 db1573981cd37f4b744989dd7e41f810cb3899d81258635e9a76eea89842d68d; physical lines 8163–8163; row_sha256 65a95d3168f33b818d1042d71e6e1991b13d327fee2a28c29cfc03fd7f55ef36; physical lines 8164–8164; row_sha256 d9d627ee60678cd3de90f58dfc5beb6c2875380321fe94fec97e90258f3880d3; physical lines 8165–8165; row_sha256 6d891868c412c03984d42749588b089d1a9a2d6fb2ecd977a3468f01f497a413; physical lines 8166–8166; row_sha256 10cdcb2730fa20bbebd1a4b4a685c2cae0e3d41f8cc076830adbbc5059f6bfa5; physical lines 8167–8167; row_sha256 43565264989da6c603b9150dcff9200b66350f68e8bcfd043f877950dc868157; physical lines 8168–8168; row_sha256 b74b6009ff6edacf3e201ef417c4d3c398b29fd6c8d69c530a868507fb9ef88f; physical lines 8169–8169; row_sha256 07a08c6a00b80b4d313b9225291d0994a2abd2fa80c7fac26b440aaab544ad4a; physical lines 8170–8170; row_sha256 5c076d1e7cf6626dbdbc41f845e93b872e1fd51cc5a2f395d117a36aff562d99; physical lines 8171–8171; row_sha256 7be80682ae23a486a9e83b76451aaf99e666920aa768c0009e2ea0b8030319f9; physical lines 8172–8172; row_sha256 c5d31db6badc3417948d7396fe7e819c3a23d8e36f1af2cff5878fdb35afac14; physical lines 8173–8173; row_sha256 6c5c0266c7b62e290d4be79d8b0c65d0a380e1897adf8a692112df15c2ed3fe8; physical lines 8174–8174; row_sha256 e56683eb345857a5eaa95329c9dac03d36be3700f128bbc6a20c66e98595b7b7; physical lines 8175–8175; row_sha256 3ffc97758b73eacdfc2797a25feebe5e524658e03ffa57b64425d76154e7a9e5; physical lines 8176–8176; row_sha256 dcdd299c7d550c778142f69060db4f6916f4fb95d93b8cf73649f106dfb6febd; physical lines 8177–8177; row_sha256 f81b50b27e60236816edd037d2735c926a145590134e2cfa089c5c631c0bca60; physical lines 8178–8178; row_sha256 a35b42448c8838026170fe49c22eebecf60d0e6fb3a00212a1e07075d0e910b2; physical lines 8179–8179; row_sha256 854caf7fa799741ac9ab2fd3a8b44b11db51b6da38b77e9f9bae58806cbd0ce4; physical lines 8180–8180; row_sha256 fae00373286b6d0a4402a9cb399e79212baaa6d3797bd016fed7ff696fda1456; physical lines 8181–8181; row_sha256 c72f84765afc304be327b0dbbeeff46fef8c9ec4c51d0b748f80ad6b28eae454; physical lines 8182–8182; row_sha256 3642bb89dcfb817b3fa7628e6f0ac55ffd537e8103bc2f830110c38f149af988; physical lines 8183–8183; row_sha256 96afc2e8250ba7fa24b35991647dc1ea6b635b078670040aca057b0c2cea5bf3; physical lines 8184–8184; row_sha256 70d701fb2ddccc606b27cc6d9584bf6f0a082c1f8829d5585245c314c7b5a9ee; physical lines 8185–8185; row_sha256 fa799af04adae93ca25a05963544c5756126653a3b52e8030725503a0ce91f32; physical lines 8186–8186; row_sha256 e0815bc2aeb481413ecd59582dde18faad2593a67bce95f651d9d1560f4271ee; physical lines 8187–8187; row_sha256 ca89bf1b6017f2eade11c0c80b5a78adef4e8bc9319157400e13ac6787739494; physical lines 8188–8188; row_sha256 abf71bd637572ebdb6712eb533a9d285c1e338ab7cca5053e151105e6fcf92d2; physical lines 8189–8189; row_sha256 c0cb2d0c15f5b11c54c0c6c65b096d700f640862a625b8005de371d789945bd4; physical lines 8190–8190; row_sha256 118cfa4bdcfb978bd4fe5902f782597e474916cef65fa0432771c4b5d38f6c50; physical lines 8191–8191; row_sha256 cbca0ddf7332ce2f7e5b43ef4b24e5d845e57d88f92558e6cc135b36f92bde42; physical lines 8192–8192; row_sha256 6b9a1fead7093ce552c767517cf4c564824c5512205a38b6c04ca8442f90fb11; physical lines 8193–8193; row_sha256 22b568658f706965d32ab6fe3611d5c7af1f4e58b1bb36ce294f768e1bdf5b78; physical lines 8194–8194; row_sha256 11afe6493328b27bae5e2c6283006aba89ee83d6b1c7f9e73faa6ba564818a9c; physical lines 8195–8195; row_sha256 564775ef29eeda4f1546456225a36a3948859dd90330b447c31e42aed6bd8e48; physical lines 8196–8196; row_sha256 5dd0698a8369b65133dd5042b9206b630598ed39645e81d1b329f37d8f8a8403; physical lines 8197–8197; row_sha256 566946adb42432cb7e30ab09f2d0becf45c7eaa07e03ab691609344cc6f43390; physical lines 8198–8198; row_sha256 a8fd475f90f15ece347559ea6e500399e859d11db3805b490d3bef3389fa5758; physical lines 8199–8199; row_sha256 c2d78025650af8cfe38e71a267e9b950d700869fb62153affb1309c8c2c06372; physical lines 8200–8200; row_sha256 528ee661b2d558bd9d9d3878a4a41f68660d187d895a3e99cefa9e12c97aedff; physical lines 8201–8201; row_sha256 6839ef0f3f06ce78f0653743ed5d87dd289d643224500fc815868d6f18ceb964; physical lines 8202–8202; row_sha256 fcf3a6a838834c8a7ef0a36256096122716367c7e903b759ba735708bae456c9; physical lines 8203–8203; row_sha256 ca4430e2d8d1683e5fbae3720db24d40fd859019c8ad45a3080e686bc0680c36; physical lines 8204–8204; row_sha256 4a768d8a2a0b82c37b4735673d352edccf94d3ccfea6504409c24286f9046f7e; physical lines 8205–8205; row_sha256 1de8ccf746fb80c8e7f63ba28a41b8202306ad0d9d66f4a1bdf753f6aa60a80a; physical lines 8206–8206; row_sha256 94c18ba9b813d2d95c0c884a1cf291441e8195d0af1626316e3e5a72b0f60b7b; physical lines 8207–8207; row_sha256 9a777af57a1eff7d52bfc5d2b6b2d2cb469efeada1e1cabb04285eea06940554; physical lines 8208–8208; row_sha256 5e79616a599528ede84a4da55db881736c762432e342e3ad1309efe5c2a0600f; physical lines 8209–8209; row_sha256 9b9582eb1cf0c5041fa1342fc0ac025b864f0e490bb071f58d2b8a21838b9abb; physical lines 8210–8210; row_sha256 6809ef723b524255107472a9e5d86ba5c87db627cb4737b3585cd09705e95ba2; physical lines 8211–8211; row_sha256 5a8b32ab9ca0d77ddf0800892427a8b50414340ae209904b8f039739ce344992; physical lines 8212–8212; row_sha256 9d3db681ba75aebd987566cfdd04369335089f54f88e6a9bcd839b82f9149899; physical lines 8213–8213; row_sha256 e4c44362ed4b4ff3eab71ea532d53a9252e8041178df985ba90cea4ba21327f8; physical lines 8214–8214; row_sha256 479c388fd81d6fd7cfd17e3f0537dafddff46f777b9a915034992f2e0ad084e9; physical lines 8215–8215; row_sha256 0750682ab13ca552921cb9f2e261edf98e19ecedecbbe6763b418c4e1e5f8c6c; physical lines 8216–8216; row_sha256 47488ea1fc48c516fd739e7a015e06f8b9d618b447396e0aa1bddae7e0d6cece; physical lines 8217–8217; row_sha256 9b44fcaa6eeb0cc05c8a6a65e76c4e70038ebd1582f16bb5e53f47b1572651d5; physical lines 8218–8218; row_sha256 a8a637e847819725ec5bec7243f376a5d651b9a1f510d146cfaf928f4a37a171; physical lines 8219–8219; row_sha256 a478fd46a916857e271fff1cbbbaa83571365531f020ae2a8ab823ba1ae63b60; physical lines 8220–8220; row_sha256 0879d5824f8929d4025b0ef7bf8694762bba71c608dac369f1cd136dd1f89bcc; physical lines 8221–8221; row_sha256 0a5e4a03d499d3f047af440f15b33492ead3da5424d8f07bbba5ae5889a58e88; physical lines 8222–8222; row_sha256 431c529837b4dc591fb9be7250a4b21ae9b375378bbe8bf5c5f52397b3e91fb0; physical lines 8223–8223; row_sha256 2939cc28151532dd0bcfdba736ff24be44ab367ddb230b655a82f8c99e7f687a; physical lines 8224–8224; row_sha256 fc9912f8277aa492276dffa368ef3ce89cb039d18d64f9f5fd6a60d7e7b890a1; physical lines 8225–8225; row_sha256 1e2bbf043a1aa241d5347bf3c76b589efbcfcefd27b66305d2b4ea466c135ed2; physical lines 8226–8226; row_sha256 bda354937993450ea02b648edab7e4e9e47b3471b8d9c20e03f43fa3827711b3; physical lines 8227–8227; row_sha256 268809785f6b4f5138f87a26a4d834f0e595546cc1d0630ef2aaf912aaba8e41; physical lines 8228–8228; row_sha256 48d43dc9f3d867bcf8e121609854a702f8f205b4092808a88e4a509379c763c9; physical lines 8229–8229; row_sha256 30519db55eddccc5f831a6b15dbd243ef09c91bce697f9b90b01c4097ca721e6; physical lines 8230–8230; row_sha256 0972ea0fe248a2c000b12debed76f94d3164857bdf2360a6b85c4b657f6e8ce8; physical lines 8231–8231; row_sha256 8c07226b1a511902f45d6733e7a5b70c3bd1fdc1921709aa308562526530f87d; physical lines 8232–8232; row_sha256 9fbe14da2a39c69beafe6af75c9891609f45fc4f407ab1588b6b7a55a5a31ad0; physical lines 8233–8233; row_sha256 f1f3873f22a8b138eb8399c1c671a8eaf154a64deff15f166bdc27e497758221; physical lines 8234–8234; row_sha256 d0f98d3043b98c29258aa3e9eef6c4cee28e5a9a1fd94dbaedf2499a6250d934; physical lines 8235–8235; row_sha256 f3d13b5e6d595365baa0ae0c95e6d4babfc47f9b369d0298ad55109cbfdae38d | supports | Exact full-key/CID/AID tuples, deposited outcomes, endpoint/value/units, targets and references where supplied. Blank AID is no-data, not inactivity; protocol and primary measurements are not independently verified. ROOT complete source reading has primary positive-row credit; current physical bytes are independently joined. |
| bgc-2485-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2485-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2485-source-antibioticmech_inchikeys | /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv; Header line1; physical lines 2194–2194; row_sha256 a480c0fa64a0547b707d7748c69e7a669f39af737bcc079a09e47debbce9fd04 | supports | Exact cross-corpus full-key record link, mechanism summary and pinned source commit; retained ANTIFUNGAL annotation is not a newly verified native assay. ROOT complete source reading has primary positive-row credit; current physical bytes are independently joined. |
| bgc-2485-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame has 0 placements with exact query, predicate and all matched fields. |
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
- Own complete raw/history, first-five intake and molecular reading are joined to ROOT’s complete context4 source reading (9 frames/185 rows/1990 fields) and Native’s bounded cache/curation reconciliation. No exact current assay exclusion applies, but that finite table result does not validate protocols or resolve assay discordance. Representation and congener-stereochemistry limits, source-specific activity semantics and unavailable primary verification keep this review partial without transferring the separate A1B findings.
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
review_id: 20261105T004623Z-antimycin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: antimycin A'
started_at: '2026-11-04T23:57:06.261665Z'
finished_at: '2026-11-05T00:46:23.150875Z'
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
summary: Antimycin A retains a stereospecified dilactone encoding, a characterized
  source BGC and a large set of assay-specific annotations. Its amide/imidic representations
  and selected stereo-unspecified A1B comparison remain distinct. The172 retained
  assay rows,25 written activities and147 further results do not collapse into a single
  potency, direct-binding mechanism or independent-experiment count.
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
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/unclassified/antimycin-a.yaml
    sha256: af65d096fdcb6ef4d6e9eb3d883a9b07efbddc24c7a150ff2eaa989e3f8a2e53
    role: target
  - path: data/natural_products/unclassified/antimycin-a1b.yaml
    sha256: 4882d0d0b724c3cc00af8d66e71618031eda03f9f400be894efd5a99d01c12d0
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
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2485; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:2762
targets:
- target_id: CHEBI:2762
  path: data/natural_products/unclassified/antimycin-a.yaml
  label: antimycin A
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/antibioticmech_inchikeys.tsv
    role: Pinned full-key AntibioticMech structure links and coarse activity summaries;
      no transfer of mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/antimycin-a1b.yaml
    role: Explicit ROOT-requested already-selected encoded identity comparison only;
      not a census companion or extra source-query context.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Exact retained selected/direct taxon decision; no fresh authority.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained source-row identity/digest guard; text-only dependency.
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
  - CHEBI:2762
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
  - CHEBI:2762
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
  - CHEBI:2762
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
  - CHEBI:2762
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
  - CHEBI:2762
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
  - CHEBI:2762
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:2762
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:2762
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2485-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/antimycin-a.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete antimycin A owner with 4 history events; prior complete raw reading
    carries with current identical bytes. No source/status/history edit.
  snapshot_sha256: af65d096fdcb6ef4d6e9eb3d883a9b07efbddc24c7a150ff2eaa989e3f8a2e53
- evidence_id: bgc-2485-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/intakes/2485-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Actual canonical target, ownership and all 41 input placements joined to
    current plan hashes.
  snapshot_sha256: f8bf94ebd66842bedc4c1684191660dbb406364ce988a2970e3ceb0c8b0d3874
- evidence_id: bgc-2485-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/4
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted the original canonical intake and exact supplemental plan;
    this owner’s actual inspection and receipt pins are located.
  snapshot_sha256: f4ee1f9dc4160c60cc3201b9246bb2ee1bd3ec750d96493dccd37dbd1725a6e5
- evidence_id: bgc-2485-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/label;
    /records/4/owner_document/definition; /records/4/owner_document/definition_source;
    /records/4/owner_document/chemical_structure; /records/4/owner_document/xrefs;
    /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact retained identifier, structure, source concepts, definition where
    present, cross-references and grounding fields. Historical annotations are not
    fresh authority searches.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/producer_taxon_groups;
    /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, declared coordinates
    and citation tiers; absent fields are not filled.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete owner supplies exact occurrence, activity and nested target assertions
    or bounded absence. Detection does not prove production; absent assays do not
    mean inactivity.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway;
    /records/4/owner_document/bgc_class
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact named/versioned model arrays, glycoside flag, filing and separate
    source categories; retention fidelity is not biological-family or biosynthetic
    proof.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document/curation_status; /records/4/owner_document/curation_history
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: All history events and status are preserved; seeding/import remains distinct
    from fresh primary verification.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets roots; no maintained reader applies. Its 25 native bioactivities
    and any nested target annotations remain separately retained.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/smiles/computed/formula; /records/4/smiles/computed/formal_charge;
    /records/4/smiles/computed/standard_inchi; /records/4/smiles/computed/standard_inchi_key;
    /records/4/smiles/computed/canonical_isomeric_smiles; /records/4/smiles/computed/canonical_nonisomeric_smiles;
    /records/4/smiles/computed/atom_count; /records/4/smiles/computed/heavy_atom_count;
    /records/4/smiles/computed/bond_count; /records/4/smiles/computed/element_counts;
    /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/formula; /records/4/inchi/computed/formal_charge;
    /records/4/inchi/computed/standard_inchi; /records/4/inchi/computed/standard_inchi_key;
    /records/4/inchi/computed/canonical_isomeric_smiles; /records/4/inchi/computed/canonical_nonisomeric_smiles;
    /records/4/inchi/computed/atom_count; /records/4/inchi/computed/heavy_atom_count;
    /records/4/inchi/computed/bond_count; /records/4/inchi/computed/element_counts;
    /records/4/inchi/computed/stereo_counts
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: 'Eight of ten comparisons are true: normalized InChI/full key, formula,
    charge and atom/bond counts agree, but both canonical SMILES comparisons are false
    and direct atom correspondence is empty. Natural identity, tautomer preference
    and complete stereochemistry are not established by these booleans.'
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2485-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds;
    /records/4/smiles/computed/rings; /records/4/smiles/computed/potential_stereo;
    /records/4/smiles/computed/motifs; /records/4/smiles/computed/fragment_atom_indices;
    /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings;
    /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/motifs;
    /records/4/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: The saved SMILES contains a nine-membered dilactone ring, with C10(=O11)-O9-C8
    and C15(=O16)-O14-C13, plus external ester C33(=O34)-O32-C7 and an aromatic amide/formamide
    region. The regenerated form keeps three ester motifs but replaces both amides
    by C14(OH30)=N28 and C25(OH33)=N29. No saturated C5O candidate sugar cycle is
    present. This is bounded structural support for an antimycin-type dilactone; it
    does not identify an assay mechanism or natural tautomer.
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2485-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-first-five-diagnostic-reading-001.json
  locator: /records/4; /read_scope; /totals; /representation; /reading_caveats; /reader
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: BGC personally read all ten complete first-five forms:604 atom and636 bond
    rows and all191 intake placements/47 paths. Whole Anditomin graph/history meanings
    factor to exact actual full-owner preservation; saved-result limits and display
    recovery are recorded.
  snapshot_sha256: 8f02ce5ed547abe9ee3e3738e23cec650136884c62b12e64de9dc31dfa480a63
- evidence_id: bgc-2485-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/4; /molecular_parse_attempts; /parsed;
    /global_warning_count; /method_scope; /interpretation_boundary
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted the original twenty stored forms. This owner’s actual comparison
    scope is located; four warnings remain global and unassigned. No alternate parse
    or normalization repair is inferred.
  snapshot_sha256: 85f657ea1d785c1aca4e78bdcf54056041799b0913a9df5155fb43b6ed51e491
- evidence_id: bgc-2485-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins;
    stream interpretation is supplied separately.
  snapshot_sha256: 7955c4e94046cc4fedde2ebda7bd56f32eb9cb544f5367b1955b30ae11d58c88
- evidence_id: bgc-2485-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–433
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Undefined stereocenters remain explicit; named/versioned computed classification
    is never a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2485-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines165–173
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: The maintained stereo_complete flag tests unassigned tetrahedral centers;
    natural identity and double-bond geometry need their separate evidence scopes.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2485-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines295–306;988–1022
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays
    remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2485-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines126–145;1318–1382
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Source assay calls, endpoint values and target accessions are retained.
    Activity classes use assay-name matching on active rows and summaries derive from
    written classes; these are not independent potency measurements or protocol validation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2485-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-assigned-source-reading-001.json
  locator: /selected_indices; /reading; /counts; /frames; /cautions
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: BGC personally read contexts0–3:36 complete frames/22 rows/225 fields,
    including the Anditomin blank-AID sentinel. This does not claim ROOT’s Antimycin
    source-row credit.
  snapshot_sha256: 8204ce76b856283f97da2268d1a5738b9616c5da78d6a2996ffb2b5bfce43737
- evidence_id: bgc-2485-root-source-reading
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
- evidence_id: bgc-2485-joint-source-notes
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
- evidence_id: bgc-2485-source-plan-execution
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
- evidence_id: bgc-2485-source-plan-acceptance
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
- evidence_id: bgc-2485-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-current249-native-gates-acceptance-001.json
  locator: /status; /counts; /all_native_gates_passed; /unavailable
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    is false. Local validation does not complete scientific verification.
  snapshot_sha256: 7c4057fa2e4c45bd5339590edd15f460011ae95df0211342b097be1e9b76b94a
- evidence_id: bgc-2485-curation-scope
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
- evidence_id: bgc-2485-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/5;
    /cached_taxonomy/whole_stanzas/9; /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/whole_stanzas/14;
    /cached_taxonomy/whole_stanzas/20
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source taxon IDs.
    They do not independently validate taxonomic rank, source strain labels, occurrence
    or production; no fresh taxonomy lookup.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2485-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/source_taxa; /contexts/4/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/4/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact source taxon IDs and saved forwarding/nonorganism routes for this
    owner; no fresh taxonomy request.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2485-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /forward_routes; /interpretation
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Native personally read all26 saved cache stanzas/10 routes, including67295→1911.
    Cached names/synonyms and routes do not upgrade species, strain, occurrence or
    producer evidence.
  snapshot_sha256: 781f62e73b1694225f8ccdca96b95bbc58bea281997f4ef1152a7ccf2d5ecc88
- evidence_id: bgc-2485-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json
  locator: /records/4/proposed_companion_paths; /records/4/direct_companion_predicates
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact declared one-hop direct map is empty for this batch. Selected Antimycin
    identity comparison is separate; no transitive expansion or biological claim transfer
    is inferred.
  snapshot_sha256: 4c92dba7f8c9b89c7fe05a9e64e3721282d76814855c144975ff46e930b901b0
- evidence_id: bgc-2485-selected-identity-comparison
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/4/owner_document; /records/5/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Selected Antimycin A and A1B have distinct full stereokeys/CIDs and specified
    versus unspecified tetrahedral encodings; complete owners retain different sources,
    histories and activity/target assertions. No name-based deduplication or assay
    transfer.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2485-selected-comparison-source
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds; /contexts/4/source_scope_inventory/joins/pubchem_bioassay;
    /contexts/4/source_scope_inventory/joins/bindingdb_targets; /contexts/5/source_scope_inventory/joins/mibig_compounds;
    /contexts/5/source_scope_inventory/joins/pubchem_bioassay; /contexts/5/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete retained identity-bearing MIBiG rows and exact assay/target frames
    for both selected owners. Antimycin A assays remain separate from A1B BindingDB5/7nM
    target rows.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2485-selected-comparison-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json
  locator: /records/4/identity_comparison_paths; /records/4/additional_context_roles
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Explicit already-selected encoded-identity comparison input; separate from
    the empty direct census map and adds no source-query context.
  snapshot_sha256: 4c92dba7f8c9b89c7fe05a9e64e3721282d76814855c144975ff46e930b901b0
- evidence_id: bgc-2485-selected-comparison-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/comparisons; /records/4/atom_correspondence;
    /records/5/declared_structure; /records/5/comparisons; /records/5/atom_correspondence;
    /records/4/smiles/computed/formula; /records/4/smiles/computed/canonical_isomeric_smiles;
    /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/potential_stereo;
    /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/formula; /records/4/inchi/computed/canonical_isomeric_smiles;
    /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/potential_stereo;
    /records/4/inchi/computed/stereo_counts; /records/5/smiles/computed/formula; /records/5/smiles/computed/canonical_isomeric_smiles;
    /records/5/smiles/computed/canonical_nonisomeric_smiles; /records/5/smiles/computed/potential_stereo;
    /records/5/smiles/computed/stereo_counts; /records/5/inchi/computed/formula; /records/5/inchi/computed/canonical_isomeric_smiles;
    /records/5/inchi/computed/canonical_nonisomeric_smiles; /records/5/inchi/computed/potential_stereo;
    /records/5/inchi/computed/stereo_counts
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: 'Exact paired encodings: Antimycin A has five specified tetrahedral centers,
    A1B five unspecified. Same-form nonisomeric strings and formulas agree across
    owners, while full stereokeys and isomeric encodings differ. Neither comparison
    establishes congener identity or transfers activity.'
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2485-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved mibig_compounds frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines 1057–1057; row_sha256 97df00d60282c01b48884ee49997a5907e033a94abb1a7014036145e07ad8d4f
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact compound/version, structure/key, database IDs, producer/locus grades
    and citation tiers. ROOT complete source reading has primary positive-row credit;
    current physical bytes are independently joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2485-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved chebi_structures frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line1; physical lines 409–409; row_sha256 45ac22cebad66676397fd469739ebb4b462522a3a1374dedf4ee7351a137ba28
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact retained ChEBI identifier/full key/label/definition/structure fields
    with source grounding; no fresh authority lookup. ROOT complete source reading
    has primary positive-row credit; current physical bytes are independently joined.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2485-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved lotus_occurrences frame has 9 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line1; physical lines 8747–8747; row_sha256 1a85840348053c39ebffaffab73cba119084810bf4922d0d707b8f3bbb97d91b;
    physical lines 8748–8748; row_sha256 5ca7f07a84bbe5db5d2f0be7c0cb597176c21d535a712bd44ada5fcd196b3ade;
    physical lines 8749–8749; row_sha256 bebd7c888716609f8899ae87f65b6e90f847cecf93afe9d158bae9ab22285da8;
    physical lines 8750–8750; row_sha256 28566fc6cefff287adbcebf2001ad7c7f93862376216bd1ec8b3cbafd96294fc;
    physical lines 8751–8751; row_sha256 8b35cbdcf4bdbf15930329ab32d82784a5a6d5b52a6a1d6ecfa5077023a22653;
    physical lines 8752–8752; row_sha256 a1511c98601131a087c81ee1be22c0c678c56fb11de0a26c25c4312e8f91a1d0;
    physical lines 8753–8753; row_sha256 86d8b8f763b90a90aea51a87a2af780c85fd71c91b949aa4ba982c9892c02cc5;
    physical lines 8754–8754; row_sha256 1598968c1976dcaa6aea704d5a902e855946115915731ebe0075b2842c2ddc8a;
    physical lines 8755–8755; row_sha256 7eaebfe3a87a139d2295c3236e97b999193da2688148fd2684ef55f2243b5fb5
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. ROOT complete
    source reading has primary positive-row credit; current physical bytes are independently
    joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2485-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved npclassifier frame has 1 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching payload or the empty
    frame is retained; no query replay.
- evidence_id: bgc-2485-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines 2401–2401; row_sha256 10822436f99fc008e6faa80e17bf58e4c26e1dc492196851aabc0b706cc918df
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; applicability is
    assessed separately. ROOT complete source reading has primary positive-row credit;
    current physical bytes are independently joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2485-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame has 172 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line1; physical lines 8064–8064; row_sha256 f7e024fcde4f722169d7eaad769bcb9cd88e47d82146f2375c2609aa7060c7f5;
    physical lines 8065–8065; row_sha256 b50607dbfe6918dbb4eed58eeac1e505a6a2858e900fd9993ba17c2e5c8ca5c2;
    physical lines 8066–8066; row_sha256 77634d229b3dd810e3ae631e48c9f2a2d57cae824baa15ff2375149c059743c7;
    physical lines 8067–8067; row_sha256 2d10d95f4d3067d8cb09b4da550bd52aea9e313feef8fbfaf132b3a1de3c92dc;
    physical lines 8068–8068; row_sha256 1cf00a74f0cf728d6fd2a2e6a724e106620c7832f7cd62aae275e4b4e65c4589;
    physical lines 8069–8069; row_sha256 5ee967537445d72c992d351d197a1d61f08b21fff769711fadb7151ba59d7153;
    physical lines 8070–8070; row_sha256 43453be82786e3894169a88663970f93ba5ce1b40d6536f2a8ae7630bc345913;
    physical lines 8071–8071; row_sha256 a4359c0afe33300bb6fdd38f122afba00e7f353f1b0a63a80bf5d4da08251166;
    physical lines 8072–8072; row_sha256 dee3aa439d6947b051b788f3c2ac42a0c0eb4729c6c2e906695e711984538215;
    physical lines 8073–8073; row_sha256 5668e926aa60b5859ad133942e85870523408578f5a4e032ba7c5fd218721030;
    physical lines 8074–8074; row_sha256 3f9312ef7cc0ad084a787af7b77288850f3c002ee99784611fcf8e7a765d9234;
    physical lines 8075–8075; row_sha256 d4ed509c630aedb5152b49b8033725c35f5d41571eaa7629b9987189cab232a1;
    physical lines 8076–8076; row_sha256 db8e2ea60c84b4affd73f2b90ab7e251d8090b2121aed71ba35e20c3e196eed4;
    physical lines 8077–8077; row_sha256 ff817a5f50c15fc8238d1ac3332618748e7b354e7f171918cb4011e5afe6d0f8;
    physical lines 8078–8078; row_sha256 6dc17d8fb44d5a29a53842c5df653c683697090fe619fcaf56b33480afe4f862;
    physical lines 8079–8079; row_sha256 6a348b71c798fe66facd82df86e5d94a506e3f7f7a96879602091668f00c0cec;
    physical lines 8080–8080; row_sha256 dcde25bbf30f6d2dd2818e4211cfea4d2f4b3e7110e5b501bb461da71945de78;
    physical lines 8081–8081; row_sha256 d424b6deafb23c26132b5c10fbecb537cd3ee83e3cafa13c28bb1e7358358737;
    physical lines 8082–8082; row_sha256 389df546c0fdcfbb4ab73e0aa566f93565f5d7148816468626abe1d2263a7087;
    physical lines 8083–8083; row_sha256 719d4203b3f2ec7f7624b1f32aa4cc9dc69f9116afb2d024a3210a5c48bc26d0;
    physical lines 8084–8084; row_sha256 8ccdd32ccddeb2ed44bd436bdc01586f1ca1369766b7f5aa812803fd9fda92ee;
    physical lines 8085–8085; row_sha256 34b3665639bf20cfb290b085e3a4fbd69c8b7feb50ed70547dba77d303fb8699;
    physical lines 8086–8086; row_sha256 aa3abeed257319dcdb38da4560dd8ed30dbd25978289bd992b9ff2a280b0e445;
    physical lines 8087–8087; row_sha256 27150deba2083f05882317eff7e68cdcb40559f4f61d3095b25842e3e60c0263;
    physical lines 8088–8088; row_sha256 e8731f3759957375c02a791052a81f6bd0f02a2da799e5926d351486ffa57c2a;
    physical lines 8089–8089; row_sha256 090aabf570a6dfb026cf6ad7292d699855802da7fd1873af4825181a732e66cc;
    physical lines 8090–8090; row_sha256 2dca1d79f2ae984c6a0b43b265cd5d489f95fdb9f645058d5db06eafe5a26360;
    physical lines 8091–8091; row_sha256 d99b1174ded220ed4e85d91c50bd08fc6ec50592559aed04df23521e93c5d4f2;
    physical lines 8092–8092; row_sha256 55c1e0156092a8ce67740b7ea29e55fe39fb27c4b1bf8705aef6e95a3de23f3d;
    physical lines 8093–8093; row_sha256 9ffd19d221cc4e37afd61e30f92c216e50ce2cd4973558c9f46111c16db10a24;
    physical lines 8094–8094; row_sha256 b7a79c7d5c3469e073414a07b4db57f1fc1ee1497afd4d3fb57c209e08495672;
    physical lines 8095–8095; row_sha256 6db509773fb1533d383f20209c1eef81a781edc7335173dc0f0045aadb27aaa4;
    physical lines 8096–8096; row_sha256 bad0a00e7bab9a724dcdce3f7104a40f6d59747076b7e069eb949d8cf395d092;
    physical lines 8097–8097; row_sha256 993f84c4b5ae350f33ab9781d325daca8109426f14635ac7bd51b9e4f9910d3c;
    physical lines 8098–8098; row_sha256 d7b998c8a1b8fc2eca334718834f106fb33ab0007c3af4f98d4c5b4eed582cfb;
    physical lines 8099–8099; row_sha256 20eb3347617eed4f61260d33379031f18f1ee680d931a0b1fed24b817624415c;
    physical lines 8100–8100; row_sha256 6d3b44438cab7de1cc782b1d15de75e322869bd7851a78acfd7cad5961d3b633;
    physical lines 8101–8101; row_sha256 7c2a2c963127d089b17460d8ca2f1ba48e236886f3c2f5ff55fa56fc03763ad0;
    physical lines 8102–8102; row_sha256 fd0552a3d8dda386e23974ae77b0e07b53df4bf0a369377c4262a9d2a0db63ce;
    physical lines 8103–8103; row_sha256 334087afc5a8f0d51633ae1044ead949ebf314afbfca61881c27cca41ba4d304;
    physical lines 8104–8104; row_sha256 c8742896093958d80832fb451a9162eb453cf9b255c6a91299eb2f8076389ef0;
    physical lines 8105–8105; row_sha256 d20e7829303afb61911e079147cb9ffa1e56e7ea962fbdef3950f88000b59c04;
    physical lines 8106–8106; row_sha256 08436ce5c7b146654029c4c5e7f0af1c49bcbfa355e2c626f6969fa0ba27dcdc;
    physical lines 8107–8107; row_sha256 fa5d054a7d68a7721696c2469c648c2670232708c42f26c97d3af4a66bb5d0b3;
    physical lines 8108–8108; row_sha256 8670f4638a47fa9128590dc7647b9798a79a16e5fdb089a81d8c68a32cee596e;
    physical lines 8109–8109; row_sha256 e9f61d8130dde6a46cf1b983ad0b90af183bfd43d8493608f9c8f5e5a21af510;
    physical lines 8110–8110; row_sha256 d780b8efc376644322437c414fac347fc0507e516721d774660c35834b39185a;
    physical lines 8111–8111; row_sha256 61cbd47692b631ca4e19d2de01c0d7593a12e7849e65c517e62d1ef2787c4887;
    physical lines 8112–8112; row_sha256 254e5e4c222688a8b1ec0d8f851d54c90b5377ea69cc65bf3fe2fb381c9e763f;
    physical lines 8113–8113; row_sha256 09db3601cc9b98aef7bb533d99f4c70f13ab232a088e621eebc27867f990d1a6;
    physical lines 8114–8114; row_sha256 6e93fb88fb54dcfc2cd0cebc6b220fb23a22f54d033edfd3ef1f90f993748f5a;
    physical lines 8115–8115; row_sha256 1fadfafa302d1c6d85948ff719f64f396ab9584db0b7990dabe28102b9a49fdc;
    physical lines 8116–8116; row_sha256 de11ea66618ed5a5ef63700daee9bb8a60a72ac022a268ade95dab4926153442;
    physical lines 8117–8117; row_sha256 8bd154480b5c32526029bd8a00eca17a5728e8b83a1acb215a45005fadccb31d;
    physical lines 8118–8118; row_sha256 c5814835054a455ed676b4ad2959e24fdcd3c2e110b27b72d6c8c31bf32232a5;
    physical lines 8119–8119; row_sha256 25f805a7bf495fe315f8e7119fd0978c87b3d35d2a394c180e307a84b16abe78;
    physical lines 8120–8120; row_sha256 5e40862316476e61dcc3c2fe8fd328ca84cd2599d3a21a272b595b453755a492;
    physical lines 8121–8121; row_sha256 425ba10d750577aec0c19846774350942466ab64819d2f4102e3013e88e019f4;
    physical lines 8122–8122; row_sha256 74910ee494f380e29627be8a92e71b3ae4e1b19710520df2ce6c14fdfd07984c;
    physical lines 8123–8123; row_sha256 e5d1678c151dcd70f61fdfdeed635f14752856e48e4e335d5ce33d6aa62394ef;
    physical lines 8124–8124; row_sha256 05091fdade03c1057a8a5b9dd65836799fa26da2a5fdb1f181fa0ad1fe9278b8;
    physical lines 8125–8125; row_sha256 356d806460783bbe520b592248fcd0decfa4ec87d3bb6116accd387f5e8c886a;
    physical lines 8126–8126; row_sha256 4c755e5ed546714e26b464ba56235a3e651e9a45e365bd785d9430661ca9a5d4;
    physical lines 8127–8127; row_sha256 7663e64a6a9bf1f1dab30a0a83c8add54629e8d4bacce63f0e0ea106c14e68d8;
    physical lines 8128–8128; row_sha256 80a1d6056f5f24c1a7dfc7a0b52f388f982441db6cae9291055bd9bd8be847bc;
    physical lines 8129–8129; row_sha256 5c10c0d11af82469e09f6ac36157e9bf7802dada802556533263d1593369f922;
    physical lines 8130–8130; row_sha256 33dcecedf4ec4846c227bb73a14a8fccb7a92271989e507a0efccd9a5b3ee707;
    physical lines 8131–8131; row_sha256 9b344ecf746643e542b84b9cabe2e19dcfd45f91429538212e34e58a2dac6631;
    physical lines 8132–8132; row_sha256 4b77ec86fe4a35d03edd75ec6f92594c92c7d7d434c19971c2a6f106dc903a6a;
    physical lines 8133–8133; row_sha256 10e3d63c30b4f3cd82c1b52abd089d149fe607abdb18248647f831d00e99a394;
    physical lines 8134–8134; row_sha256 57eff88630bd3fc55dbb4581fc2a563482a3f4b1b302092c934511e50fb67ef7;
    physical lines 8135–8135; row_sha256 eb1e9c3cab2de1d439a9d04e845d8e26b505a3905af62ffebd86655ee4256384;
    physical lines 8136–8136; row_sha256 3ce2aae7376b29f952eb8b645942afac513b7ea7043aad3d36d5f03ab7e38adf;
    physical lines 8137–8137; row_sha256 2dbc45f98c5e4a034beb09ec7d6c5a5421f62e698428a7cab437c91bd2dd7c5f;
    physical lines 8138–8138; row_sha256 0e5deb05d61db541dc161cfdf3c4a12501632f2e1cddb809c28e76d92fcdd3f5;
    physical lines 8139–8139; row_sha256 e224b9987b6f26fc934e49f0f19ead063b25b41e1e9df3093a0730f98db3bc54;
    physical lines 8140–8140; row_sha256 0c42fa99d89a748da1e2063a52b2de67fc01e4a6f5c6d11929b9cac50c37fff6;
    physical lines 8141–8141; row_sha256 cfa5edd8014fd202e75ec4acd4ea646426b04b82dde1c7f967b373cd9a6a9493;
    physical lines 8142–8142; row_sha256 72e1ff60889cc31b8e77957fba3a68d3b5744d19d252673f3b86da53cffc4503;
    physical lines 8143–8143; row_sha256 15ec7b5ac741d5dc2a0bc9a3e4aa6f3f160e36a0aa61744e01a093ac8f47ff42;
    physical lines 8144–8144; row_sha256 e4ed83530f9631190c89ebbe79eaabf03752748f4a7cdc66d30ac9c0cfdc2194;
    physical lines 8145–8145; row_sha256 c0a348202d3464e35a04d761dfb9d384a713fcff09489e061c9655a738a76aa5;
    physical lines 8146–8146; row_sha256 218da6b9721ce449f22f65e786a40d2cbe60385d245adc1b40595385171fdc17;
    physical lines 8147–8147; row_sha256 85706e19b4d9bb1e64b62dcbb8b5e472f0ac28f0abec8a99f837d37beaf13e02;
    physical lines 8148–8148; row_sha256 416240501e59b3114afcb69cff22762a99eb8191b50f754f3106612bacf1c980;
    physical lines 8149–8149; row_sha256 a7337538e68267a8468a5e6bdcc7230e0e5bbe1fedc625bb5d7274eb7249ba53;
    physical lines 8150–8150; row_sha256 509cb8b34e08749ceaeaf4de78ac367dac8d6956af99885fd4cc1596d7915232;
    physical lines 8151–8151; row_sha256 9aa3a229192b71c5f5233d86fc94432509e700715213db0e28d93f6a6dc31e5e;
    physical lines 8152–8152; row_sha256 1247386ee82d3634a51d83c2239cbbb92cd4d772c24df0a8df1fddf2def99462;
    physical lines 8153–8153; row_sha256 45028a5faff220c318054a55a9295c0fa2db4721a2e153c1d31a50ca977f3d1a;
    physical lines 8154–8154; row_sha256 4f9b4eb2cef97f02a909ab125ef3b0a8710da386117c351f907de35c61b18a85;
    physical lines 8155–8155; row_sha256 2e3a54b77cd80921b666942d14cb49a9c93ba5c9268d4238a2ac25cf6e35cbca;
    physical lines 8156–8156; row_sha256 f3ca0950ffda5e0da905b0f92ca2113b909bcec68de319667b6fc96bed9581a8;
    physical lines 8157–8157; row_sha256 b67e2b8e8c004d51070b3aad2ee652a01d24858b9eb28e27b942ff09796d445d;
    physical lines 8158–8158; row_sha256 0c154c95276f91725fb532853c8dea17c2229ced2c74b917a61bc7ae181e3e8e;
    physical lines 8159–8159; row_sha256 51827e663d30b2090ea05b115165955233599f075c992e3337a17247c20de506;
    physical lines 8160–8160; row_sha256 8d351959549263cbbb654c6d5b5a56ee79bece432a8b4a83fbf046ce4cf19eeb;
    physical lines 8161–8161; row_sha256 0bc306775c6597418bb9a9561907592288bfa1f50428ec722e22b0225c5cb94a;
    physical lines 8162–8162; row_sha256 db1573981cd37f4b744989dd7e41f810cb3899d81258635e9a76eea89842d68d;
    physical lines 8163–8163; row_sha256 65a95d3168f33b818d1042d71e6e1991b13d327fee2a28c29cfc03fd7f55ef36;
    physical lines 8164–8164; row_sha256 d9d627ee60678cd3de90f58dfc5beb6c2875380321fe94fec97e90258f3880d3;
    physical lines 8165–8165; row_sha256 6d891868c412c03984d42749588b089d1a9a2d6fb2ecd977a3468f01f497a413;
    physical lines 8166–8166; row_sha256 10cdcb2730fa20bbebd1a4b4a685c2cae0e3d41f8cc076830adbbc5059f6bfa5;
    physical lines 8167–8167; row_sha256 43565264989da6c603b9150dcff9200b66350f68e8bcfd043f877950dc868157;
    physical lines 8168–8168; row_sha256 b74b6009ff6edacf3e201ef417c4d3c398b29fd6c8d69c530a868507fb9ef88f;
    physical lines 8169–8169; row_sha256 07a08c6a00b80b4d313b9225291d0994a2abd2fa80c7fac26b440aaab544ad4a;
    physical lines 8170–8170; row_sha256 5c076d1e7cf6626dbdbc41f845e93b872e1fd51cc5a2f395d117a36aff562d99;
    physical lines 8171–8171; row_sha256 7be80682ae23a486a9e83b76451aaf99e666920aa768c0009e2ea0b8030319f9;
    physical lines 8172–8172; row_sha256 c5d31db6badc3417948d7396fe7e819c3a23d8e36f1af2cff5878fdb35afac14;
    physical lines 8173–8173; row_sha256 6c5c0266c7b62e290d4be79d8b0c65d0a380e1897adf8a692112df15c2ed3fe8;
    physical lines 8174–8174; row_sha256 e56683eb345857a5eaa95329c9dac03d36be3700f128bbc6a20c66e98595b7b7;
    physical lines 8175–8175; row_sha256 3ffc97758b73eacdfc2797a25feebe5e524658e03ffa57b64425d76154e7a9e5;
    physical lines 8176–8176; row_sha256 dcdd299c7d550c778142f69060db4f6916f4fb95d93b8cf73649f106dfb6febd;
    physical lines 8177–8177; row_sha256 f81b50b27e60236816edd037d2735c926a145590134e2cfa089c5c631c0bca60;
    physical lines 8178–8178; row_sha256 a35b42448c8838026170fe49c22eebecf60d0e6fb3a00212a1e07075d0e910b2;
    physical lines 8179–8179; row_sha256 854caf7fa799741ac9ab2fd3a8b44b11db51b6da38b77e9f9bae58806cbd0ce4;
    physical lines 8180–8180; row_sha256 fae00373286b6d0a4402a9cb399e79212baaa6d3797bd016fed7ff696fda1456;
    physical lines 8181–8181; row_sha256 c72f84765afc304be327b0dbbeeff46fef8c9ec4c51d0b748f80ad6b28eae454;
    physical lines 8182–8182; row_sha256 3642bb89dcfb817b3fa7628e6f0ac55ffd537e8103bc2f830110c38f149af988;
    physical lines 8183–8183; row_sha256 96afc2e8250ba7fa24b35991647dc1ea6b635b078670040aca057b0c2cea5bf3;
    physical lines 8184–8184; row_sha256 70d701fb2ddccc606b27cc6d9584bf6f0a082c1f8829d5585245c314c7b5a9ee;
    physical lines 8185–8185; row_sha256 fa799af04adae93ca25a05963544c5756126653a3b52e8030725503a0ce91f32;
    physical lines 8186–8186; row_sha256 e0815bc2aeb481413ecd59582dde18faad2593a67bce95f651d9d1560f4271ee;
    physical lines 8187–8187; row_sha256 ca89bf1b6017f2eade11c0c80b5a78adef4e8bc9319157400e13ac6787739494;
    physical lines 8188–8188; row_sha256 abf71bd637572ebdb6712eb533a9d285c1e338ab7cca5053e151105e6fcf92d2;
    physical lines 8189–8189; row_sha256 c0cb2d0c15f5b11c54c0c6c65b096d700f640862a625b8005de371d789945bd4;
    physical lines 8190–8190; row_sha256 118cfa4bdcfb978bd4fe5902f782597e474916cef65fa0432771c4b5d38f6c50;
    physical lines 8191–8191; row_sha256 cbca0ddf7332ce2f7e5b43ef4b24e5d845e57d88f92558e6cc135b36f92bde42;
    physical lines 8192–8192; row_sha256 6b9a1fead7093ce552c767517cf4c564824c5512205a38b6c04ca8442f90fb11;
    physical lines 8193–8193; row_sha256 22b568658f706965d32ab6fe3611d5c7af1f4e58b1bb36ce294f768e1bdf5b78;
    physical lines 8194–8194; row_sha256 11afe6493328b27bae5e2c6283006aba89ee83d6b1c7f9e73faa6ba564818a9c;
    physical lines 8195–8195; row_sha256 564775ef29eeda4f1546456225a36a3948859dd90330b447c31e42aed6bd8e48;
    physical lines 8196–8196; row_sha256 5dd0698a8369b65133dd5042b9206b630598ed39645e81d1b329f37d8f8a8403;
    physical lines 8197–8197; row_sha256 566946adb42432cb7e30ab09f2d0becf45c7eaa07e03ab691609344cc6f43390;
    physical lines 8198–8198; row_sha256 a8fd475f90f15ece347559ea6e500399e859d11db3805b490d3bef3389fa5758;
    physical lines 8199–8199; row_sha256 c2d78025650af8cfe38e71a267e9b950d700869fb62153affb1309c8c2c06372;
    physical lines 8200–8200; row_sha256 528ee661b2d558bd9d9d3878a4a41f68660d187d895a3e99cefa9e12c97aedff;
    physical lines 8201–8201; row_sha256 6839ef0f3f06ce78f0653743ed5d87dd289d643224500fc815868d6f18ceb964;
    physical lines 8202–8202; row_sha256 fcf3a6a838834c8a7ef0a36256096122716367c7e903b759ba735708bae456c9;
    physical lines 8203–8203; row_sha256 ca4430e2d8d1683e5fbae3720db24d40fd859019c8ad45a3080e686bc0680c36;
    physical lines 8204–8204; row_sha256 4a768d8a2a0b82c37b4735673d352edccf94d3ccfea6504409c24286f9046f7e;
    physical lines 8205–8205; row_sha256 1de8ccf746fb80c8e7f63ba28a41b8202306ad0d9d66f4a1bdf753f6aa60a80a;
    physical lines 8206–8206; row_sha256 94c18ba9b813d2d95c0c884a1cf291441e8195d0af1626316e3e5a72b0f60b7b;
    physical lines 8207–8207; row_sha256 9a777af57a1eff7d52bfc5d2b6b2d2cb469efeada1e1cabb04285eea06940554;
    physical lines 8208–8208; row_sha256 5e79616a599528ede84a4da55db881736c762432e342e3ad1309efe5c2a0600f;
    physical lines 8209–8209; row_sha256 9b9582eb1cf0c5041fa1342fc0ac025b864f0e490bb071f58d2b8a21838b9abb;
    physical lines 8210–8210; row_sha256 6809ef723b524255107472a9e5d86ba5c87db627cb4737b3585cd09705e95ba2;
    physical lines 8211–8211; row_sha256 5a8b32ab9ca0d77ddf0800892427a8b50414340ae209904b8f039739ce344992;
    physical lines 8212–8212; row_sha256 9d3db681ba75aebd987566cfdd04369335089f54f88e6a9bcd839b82f9149899;
    physical lines 8213–8213; row_sha256 e4c44362ed4b4ff3eab71ea532d53a9252e8041178df985ba90cea4ba21327f8;
    physical lines 8214–8214; row_sha256 479c388fd81d6fd7cfd17e3f0537dafddff46f777b9a915034992f2e0ad084e9;
    physical lines 8215–8215; row_sha256 0750682ab13ca552921cb9f2e261edf98e19ecedecbbe6763b418c4e1e5f8c6c;
    physical lines 8216–8216; row_sha256 47488ea1fc48c516fd739e7a015e06f8b9d618b447396e0aa1bddae7e0d6cece;
    physical lines 8217–8217; row_sha256 9b44fcaa6eeb0cc05c8a6a65e76c4e70038ebd1582f16bb5e53f47b1572651d5;
    physical lines 8218–8218; row_sha256 a8a637e847819725ec5bec7243f376a5d651b9a1f510d146cfaf928f4a37a171;
    physical lines 8219–8219; row_sha256 a478fd46a916857e271fff1cbbbaa83571365531f020ae2a8ab823ba1ae63b60;
    physical lines 8220–8220; row_sha256 0879d5824f8929d4025b0ef7bf8694762bba71c608dac369f1cd136dd1f89bcc;
    physical lines 8221–8221; row_sha256 0a5e4a03d499d3f047af440f15b33492ead3da5424d8f07bbba5ae5889a58e88;
    physical lines 8222–8222; row_sha256 431c529837b4dc591fb9be7250a4b21ae9b375378bbe8bf5c5f52397b3e91fb0;
    physical lines 8223–8223; row_sha256 2939cc28151532dd0bcfdba736ff24be44ab367ddb230b655a82f8c99e7f687a;
    physical lines 8224–8224; row_sha256 fc9912f8277aa492276dffa368ef3ce89cb039d18d64f9f5fd6a60d7e7b890a1;
    physical lines 8225–8225; row_sha256 1e2bbf043a1aa241d5347bf3c76b589efbcfcefd27b66305d2b4ea466c135ed2;
    physical lines 8226–8226; row_sha256 bda354937993450ea02b648edab7e4e9e47b3471b8d9c20e03f43fa3827711b3;
    physical lines 8227–8227; row_sha256 268809785f6b4f5138f87a26a4d834f0e595546cc1d0630ef2aaf912aaba8e41;
    physical lines 8228–8228; row_sha256 48d43dc9f3d867bcf8e121609854a702f8f205b4092808a88e4a509379c763c9;
    physical lines 8229–8229; row_sha256 30519db55eddccc5f831a6b15dbd243ef09c91bce697f9b90b01c4097ca721e6;
    physical lines 8230–8230; row_sha256 0972ea0fe248a2c000b12debed76f94d3164857bdf2360a6b85c4b657f6e8ce8;
    physical lines 8231–8231; row_sha256 8c07226b1a511902f45d6733e7a5b70c3bd1fdc1921709aa308562526530f87d;
    physical lines 8232–8232; row_sha256 9fbe14da2a39c69beafe6af75c9891609f45fc4f407ab1588b6b7a55a5a31ad0;
    physical lines 8233–8233; row_sha256 f1f3873f22a8b138eb8399c1c671a8eaf154a64deff15f166bdc27e497758221;
    physical lines 8234–8234; row_sha256 d0f98d3043b98c29258aa3e9eef6c4cee28e5a9a1fd94dbaedf2499a6250d934;
    physical lines 8235–8235; row_sha256 f3d13b5e6d595365baa0ae0c95e6d4babfc47f9b369d0298ad55109cbfdae38d
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact full-key/CID/AID tuples, deposited outcomes, endpoint/value/units,
    targets and references where supplied. Blank AID is no-data, not inactivity; protocol
    and primary measurements are not independently verified. ROOT complete source
    reading has primary positive-row credit; current physical bytes are independently
    joined.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2485-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved bindingdb_targets frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame has 1 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "UIFFUZWRFRDZJC-SBOOETFBSA-N". Every
    matching payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2485-source-antibioticmech_inchikeys
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/antibioticmech_inchikeys.tsv
  locator: Header line1; physical lines 2194–2194; row_sha256 a480c0fa64a0547b707d7748c69e7a669f39af737bcc079a09e47debbce9fd04
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact cross-corpus full-key record link, mechanism summary and pinned source
    commit; retained ANTIFUNGAL annotation is not a newly verified native assay. ROOT
    complete source reading has primary positive-row credit; current physical bytes
    are independently joined.
  snapshot_sha256: ca8a487bf0868b96d097268db7422f07e0146258b7ca9e51fd21a3aaacdd92a6
- evidence_id: bgc-2485-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved chebi_origins frame has 0 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query ["CHEBI:2762"]. Every matching payload or
    the empty frame is retained; no query replay.
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
- assessment_id: bgc-2485-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: CHEBI:2762, CID14957 and full key UIFFUZWRFRDZJC-SBOOETFBSA-N identify
    the selected stereospecified C28H40N2O9 encoding. Already-selected Antimycin A1B
    has the same formula/connectivity block but full key UIFFUZWRFRDZJC-UHFFFAOYSA-N
    and CID12550, with five unspecified tetrahedral centers. The same-form nonisomeric
    strings agree across these selected encodings, while their stereochemical scope
    differs. This explicit comparison is not a census BGC companion, name-based deduplication,
    congener identity proof or permission to transfer A1B5/7nM target claims.
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-grounding-owner
  - bgc-2485-chemistry
  - bgc-2485-source-mibig_compounds
  - bgc-2485-query-chebi_structures
  - bgc-2485-direct-contexts
  - bgc-2485-source-chebi_structures
  - bgc-2485-selected-identity-comparison
  - bgc-2485-selected-comparison-source
  - bgc-2485-selected-comparison-plan
  - bgc-2485-selected-comparison-chemistry
  dimensions:
  - name: standard_inchi_key
    value: UIFFUZWRFRDZJC-SBOOETFBSA-N; retained key, not natural-identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2485-grounding-owner
    - bgc-2485-chemistry
    - bgc-2485-source-mibig_compounds
    - bgc-2485-query-chebi_structures
    - bgc-2485-direct-contexts
    - bgc-2485-source-chebi_structures
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
  - name: grounding_scope
    value: CHEBI:2762, CID14957 and full key UIFFUZWRFRDZJC-SBOOETFBSA-N identify
      the selected stereospecified C28H40N2O9 encoding. Already-selected Antimycin
      A1B has the same formula/connectivity block but full key UIFFUZWRFRDZJC-UHFFFAOYSA-N
      and CID12550, with five unspecified tetrahedral centers. The same-form nonisomeric
      strings agree across these selected encodings, while their stereochemical scope
      differs. This explicit comparison is not a census BGC companion, name-based
      deduplication, congener identity proof or permission to transfer A1B5/7nM target
      claims.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2485-grounding-owner
    - bgc-2485-chemistry
    - bgc-2485-source-mibig_compounds
    - bgc-2485-query-chebi_structures
    - bgc-2485-direct-contexts
    - bgc-2485-source-chebi_structures
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
- assessment_id: bgc-2485-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: 'Both neutral selected forms contain39 atoms/40 bonds and reproduce the
    declared normalized InChI/full key. Their canonical isomeric and nonisomeric SMILES
    differ and direct correspondence is empty: SMILES C19(=O20)-N18H and formamide
    C28(=O29)-N27H become two C(OH)=N sites in the regenerated form. Five specified
    tetrahedral centers persist; two additional unspecified C=N potentials are representation-dependent.
    The literal stereo_complete:true is scoped to the maintained tetrahedral test,
    not complete imine geometry or natural-state proof. A1B instead leaves the five
    tetrahedral centers unspecified.'
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-grounding-owner
  - bgc-2485-chemistry
  - bgc-2485-topology
  - bgc-2485-diagnostic-reading
  - bgc-2485-diagnostic-acceptance
  - bgc-2485-structure-schema
  - bgc-2485-stereo-method
  - bgc-2485-source-chebi_structures
  - bgc-2485-selected-identity-comparison
  - bgc-2485-selected-comparison-source
  - bgc-2485-selected-comparison-plan
  - bgc-2485-selected-comparison-chemistry
  dimensions:
  - name: stereochemistry_scope
    value: 'Both neutral selected forms contain39 atoms/40 bonds and reproduce the
      declared normalized InChI/full key. Their canonical isomeric and nonisomeric
      SMILES differ and direct correspondence is empty: SMILES C19(=O20)-N18H and
      formamide C28(=O29)-N27H become two C(OH)=N sites in the regenerated form. Five
      specified tetrahedral centers persist; two additional unspecified C=N potentials
      are representation-dependent. The literal stereo_complete:true is scoped to
      the maintained tetrahedral test, not complete imine geometry or natural-state
      proof. A1B instead leaves the five tetrahedral centers unspecified.'
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2485-grounding-owner
    - bgc-2485-chemistry
    - bgc-2485-topology
    - bgc-2485-diagnostic-reading
    - bgc-2485-diagnostic-acceptance
    - bgc-2485-structure-schema
    - bgc-2485-stereo-method
    - bgc-2485-source-chebi_structures
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
  - name: representation_correspondence
    value: 'Eight of ten comparisons are true: normalized InChI/full key, formula,
      charge and atom/bond counts agree, but both canonical SMILES comparisons are
      false and direct atom correspondence is empty. Natural identity, tautomer preference
      and complete stereochemistry are not established by these booleans.'
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2485-grounding-owner
    - bgc-2485-chemistry
    - bgc-2485-topology
    - bgc-2485-diagnostic-reading
    - bgc-2485-diagnostic-acceptance
    - bgc-2485-structure-schema
    - bgc-2485-stereo-method
    - bgc-2485-source-chebi_structures
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
- assessment_id: bgc-2485-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: BGC0000958 version5 retains Streptomyces sp.S4 NCBITaxon:889487 as BGC_CHARACTERIZED
    and a distinct CLUSTER_DEMONSTRATED locus NZ_FR873698.1:81953–106578 with four
    reported methods. Nine LOTUS source placements reconcile to seven exact owner
    taxon/DOI occurrence tuples. The saved67295→1911 forward merge and source S.setonii
    versus cached S.griseus (with S.setonii synonym) remain explicit; this cached
    reconciliation does not freshly validate taxonomy, producing strains or causal
    production in every occurrence.
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-origin-owner
  - bgc-2485-occurrence-owner
  - bgc-2485-source-mibig_compounds
  - bgc-2485-cached-taxonomy
  - bgc-2485-taxonomy-routes
  - bgc-2485-curation-scope
  - bgc-2485-direct-contexts
  - bgc-2485-source-lotus_occurrences
  dimensions:
  - name: taxon_scope
    value: BGC0000958 version5 retains Streptomyces sp.S4 NCBITaxon:889487 as BGC_CHARACTERIZED
      and a distinct CLUSTER_DEMONSTRATED locus NZ_FR873698.1:81953–106578 with four
      reported methods. Nine LOTUS source placements reconcile to seven exact owner
      taxon/DOI occurrence tuples. The saved67295→1911 forward merge and source S.setonii
      versus cached S.griseus (with S.setonii synonym) remain explicit; this cached
      reconciliation does not freshly validate taxonomy, producing strains or causal
      production in every occurrence.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2485-origin-owner
    - bgc-2485-occurrence-owner
    - bgc-2485-source-mibig_compounds
    - bgc-2485-cached-taxonomy
    - bgc-2485-taxonomy-routes
    - bgc-2485-curation-scope
    - bgc-2485-direct-contexts
    - bgc-2485-source-lotus_occurrences
  - name: producer_evidence
    value: BGC0000958 version5 retains Streptomyces sp.S4 NCBITaxon:889487 as BGC_CHARACTERIZED
      and a distinct CLUSTER_DEMONSTRATED locus NZ_FR873698.1:81953–106578 with four
      reported methods. Nine LOTUS source placements reconcile to seven exact owner
      taxon/DOI occurrence tuples. The saved67295→1911 forward merge and source S.setonii
      versus cached S.griseus (with S.setonii synonym) remain explicit; this cached
      reconciliation does not freshly validate taxonomy, producing strains or causal
      production in every occurrence.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2485-origin-owner
    - bgc-2485-occurrence-owner
    - bgc-2485-source-mibig_compounds
    - bgc-2485-cached-taxonomy
    - bgc-2485-taxonomy-routes
    - bgc-2485-curation-scope
    - bgc-2485-direct-contexts
    - bgc-2485-source-lotus_occurrences
  - name: locus_evidence
    value: BGC0000958 version5 retains Streptomyces sp.S4 NCBITaxon:889487 as BGC_CHARACTERIZED
      and a distinct CLUSTER_DEMONSTRATED locus NZ_FR873698.1:81953–106578 with four
      reported methods. Nine LOTUS source placements reconcile to seven exact owner
      taxon/DOI occurrence tuples. The saved67295→1911 forward merge and source S.setonii
      versus cached S.griseus (with S.setonii synonym) remain explicit; this cached
      reconciliation does not freshly validate taxonomy, producing strains or causal
      production in every occurrence.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2485-origin-owner
    - bgc-2485-occurrence-owner
    - bgc-2485-source-mibig_compounds
    - bgc-2485-cached-taxonomy
    - bgc-2485-taxonomy-routes
    - bgc-2485-curation-scope
    - bgc-2485-direct-contexts
    - bgc-2485-source-lotus_occurrences
- assessment_id: bgc-2485-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: MIBiG ENTRY PMID21857911, each LOTUS occurrence DOI, exact PubChem AID/PMID/target
    tuples and the retained AntibioticMech link keep their distinct evidentiary tiers.
    Repeated assay rows, target-enriched rows and article placements are not independent
    experiments. All four seed-history events are retained. The ANTIFUNGAL summary
    is traceable to the exact full-key AntibioticMech row at pinned commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976;
    it is not a newly verified native antifungal experiment.
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-owner
  - bgc-2485-history-owner
  - bgc-2485-origin-owner
  - bgc-2485-occurrence-owner
  - bgc-2485-source-mibig_compounds
  - bgc-2485-source-reading
  - bgc-2485-root-source-reading
  - bgc-2485-source-lotus_occurrences
  - bgc-2485-source-pubchem_bioassay
  - bgc-2485-source-chebi_structures
  - bgc-2485-source-antibioticmech_inchikeys
  - bgc-2485-selected-identity-comparison
  - bgc-2485-selected-comparison-source
  - bgc-2485-selected-comparison-plan
  - bgc-2485-selected-comparison-chemistry
  dimensions:
  - name: citation_scope
    value: MIBiG ENTRY PMID21857911, each LOTUS occurrence DOI, exact PubChem AID/PMID/target
      tuples and the retained AntibioticMech link keep their distinct evidentiary
      tiers. Repeated assay rows, target-enriched rows and article placements are
      not independent experiments. All four seed-history events are retained. The
      ANTIFUNGAL summary is traceable to the exact full-key AntibioticMech row at
      pinned commit74f6cc8362498900f2fe2c13d0b6fdb66dd30976; it is not a newly verified
      native antifungal experiment.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2485-owner
    - bgc-2485-history-owner
    - bgc-2485-origin-owner
    - bgc-2485-occurrence-owner
    - bgc-2485-source-mibig_compounds
    - bgc-2485-source-reading
    - bgc-2485-root-source-reading
    - bgc-2485-source-lotus_occurrences
    - bgc-2485-source-pubchem_bioassay
    - bgc-2485-source-chebi_structures
    - bgc-2485-source-antibioticmech_inchikeys
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
- assessment_id: bgc-2485-occurrence
  area: evidence
  topic: Source-specific occurrence and assay assertions
  outcome: supported
  summary: ROOT personally read all172 retained PubChem assay rows, with all fields,
    and the remaining13 source rows for this owner. The source-to-owner reconciliation
    preserves25 written bioactivities plus a note about147 further results. Deposited
    ACTIVE, INACTIVE and INCONCLUSIVE calls remain assay-specific; INCONCLUSIVE maps
    to NOT_DETERMINED. Numeric values attached to inactive or inconclusive calls do
    not reverse those calls. Source Potency remains endpoint OTHER rather than inferred
    IC50, EC50 or MIC. LOTUS detection and the separate AntibioticMech ANTIFUNGAL
    annotation do not establish a common mechanism or potency.
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-occurrence-owner
  - bgc-2485-mechanism-absence
  - bgc-2485-query-lotus_occurrences
  - bgc-2485-query-chebi_origins
  - bgc-2485-query-cyanometdb_occurrences
  - bgc-2485-query-pubchem_bioassay
  - bgc-2485-query-bindingdb_targets
  - bgc-2485-query-antibioticmech_inchikeys
  - bgc-2485-cached-taxonomy
  - bgc-2485-taxonomy-routes
  - bgc-2485-taxonomy-reading
  - bgc-2485-curation-scope
  - bgc-2485-bioactivity-seeder
  - bgc-2485-root-source-reading
  - bgc-2485-source-lotus_occurrences
  - bgc-2485-source-pubchem_bioassay
  - bgc-2485-source-antibioticmech_inchikeys
  - bgc-2485-selected-identity-comparison
  - bgc-2485-selected-comparison-source
  - bgc-2485-selected-comparison-plan
  - bgc-2485-selected-comparison-chemistry
  dimensions:
  - name: occurrence_scope
    value: ROOT personally read all172 retained PubChem assay rows, with all fields,
      and the remaining13 source rows for this owner. The source-to-owner reconciliation
      preserves25 written bioactivities plus a note about147 further results. Deposited
      ACTIVE, INACTIVE and INCONCLUSIVE calls remain assay-specific; INCONCLUSIVE
      maps to NOT_DETERMINED. Numeric values attached to inactive or inconclusive
      calls do not reverse those calls. Source Potency remains endpoint OTHER rather
      than inferred IC50, EC50 or MIC. LOTUS detection and the separate AntibioticMech
      ANTIFUNGAL annotation do not establish a common mechanism or potency.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2485-occurrence-owner
    - bgc-2485-mechanism-absence
    - bgc-2485-query-lotus_occurrences
    - bgc-2485-query-chebi_origins
    - bgc-2485-query-cyanometdb_occurrences
    - bgc-2485-query-pubchem_bioassay
    - bgc-2485-query-bindingdb_targets
    - bgc-2485-query-antibioticmech_inchikeys
    - bgc-2485-cached-taxonomy
    - bgc-2485-taxonomy-routes
    - bgc-2485-taxonomy-reading
    - bgc-2485-curation-scope
    - bgc-2485-bioactivity-seeder
    - bgc-2485-root-source-reading
    - bgc-2485-source-lotus_occurrences
    - bgc-2485-source-pubchem_bioassay
    - bgc-2485-source-antibioticmech_inchikeys
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
  - name: assay_target_scope
    value: For example, ACTIVE viability AID2202551 retains0.3474uM as OTHER, while
      INACTIVE AID1224825 and1224824 retain0.0935uM and0.0132uM with their inactive
      calls. No assay protocol was freshly checked. Nested P36969, P42858 and Q99700
      annotations do not independently establish direct binding or target causality;
      ASK51714 remains ungrounded. The complete owner has no native causal graph,
      pathway, component-reference or molecular-target root. Selected A1B BindingDB5/7nM
      rows and its graph assertions remain outside this owner’s assay evidence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2485-occurrence-owner
    - bgc-2485-mechanism-absence
    - bgc-2485-query-lotus_occurrences
    - bgc-2485-query-chebi_origins
    - bgc-2485-query-cyanometdb_occurrences
    - bgc-2485-query-pubchem_bioassay
    - bgc-2485-query-bindingdb_targets
    - bgc-2485-query-antibioticmech_inchikeys
    - bgc-2485-cached-taxonomy
    - bgc-2485-taxonomy-routes
    - bgc-2485-taxonomy-reading
    - bgc-2485-curation-scope
    - bgc-2485-bioactivity-seeder
    - bgc-2485-root-source-reading
    - bgc-2485-source-lotus_occurrences
    - bgc-2485-source-pubchem_bioassay
    - bgc-2485-source-antibioticmech_inchikeys
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
- assessment_id: bgc-2485-classification
  area: consistency
  topic: Reported model families and bounded structural compatibility
  outcome: supported
  summary: The versioned Antimycins/Macrolides model output is compatible with the
    observed dilactone/amide structural family, while source NRPS|PKS remains a separate
    biosynthetic annotation. The specific model label and ChEBI description are retained
    with their own provenance; neither computed family nor structural compatibility
    independently establishes direct binding, an antifungal mechanism, a natural congener
    mixture or exact biosynthetic experiments.
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-classification-owner
  - bgc-2485-source-npclassifier
  - bgc-2485-chemistry
  - bgc-2485-topology
  - bgc-2485-structure-schema
  - bgc-2485-classification-seeder
  - bgc-2485-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: The versioned Antimycins/Macrolides model output is compatible with the
      observed dilactone/amide structural family, while source NRPS|PKS remains a
      separate biosynthetic annotation. The specific model label and ChEBI description
      are retained with their own provenance; neither computed family nor structural
      compatibility independently establishes direct binding, an antifungal mechanism,
      a natural congener mixture or exact biosynthetic experiments.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2485-classification-owner
    - bgc-2485-source-npclassifier
    - bgc-2485-chemistry
    - bgc-2485-topology
    - bgc-2485-structure-schema
    - bgc-2485-classification-seeder
    - bgc-2485-source-mibig_compounds
- assessment_id: bgc-2485-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: Own complete raw/history, first-five intake and molecular reading are joined
    to ROOT’s complete context4 source reading (9 frames/185 rows/1990 fields) and
    Native’s bounded cache/curation reconciliation. No exact current assay exclusion
    applies, but that finite table result does not validate protocols or resolve assay
    discordance. Representation and congener-stereochemistry limits, source-specific
    activity semantics and unavailable primary verification keep this review partial
    without transferring the separate A1B findings.
  target_ids:
  - CHEBI:2762
  evidence_ids:
  - bgc-2485-owner
  - bgc-2485-capture
  - bgc-2485-intake
  - bgc-2485-intake-acceptance
  - bgc-2485-history-owner
  - bgc-2485-diagnostic-reading
  - bgc-2485-diagnostic-acceptance
  - bgc-2485-diagnostic-execution
  - bgc-2485-source-reading
  - bgc-2485-root-source-reading
  - bgc-2485-joint-source-notes
  - bgc-2485-source-plan-execution
  - bgc-2485-source-plan-acceptance
  - bgc-2485-native-gate-limits
  - bgc-2485-curation-scope
  - bgc-2485-mechanism-absence
  - bgc-2485-selected-identity-comparison
  - bgc-2485-selected-comparison-source
  - bgc-2485-selected-comparison-plan
  - bgc-2485-selected-comparison-chemistry
  dimensions:
  - name: review_completion
    value: Own complete raw/history, first-five intake and molecular reading are joined
      to ROOT’s complete context4 source reading (9 frames/185 rows/1990 fields) and
      Native’s bounded cache/curation reconciliation. No exact current assay exclusion
      applies, but that finite table result does not validate protocols or resolve
      assay discordance. Representation and congener-stereochemistry limits, source-specific
      activity semantics and unavailable primary verification keep this review partial
      without transferring the separate A1B findings.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2485-owner
    - bgc-2485-capture
    - bgc-2485-intake
    - bgc-2485-intake-acceptance
    - bgc-2485-history-owner
    - bgc-2485-diagnostic-reading
    - bgc-2485-diagnostic-acceptance
    - bgc-2485-diagnostic-execution
    - bgc-2485-source-reading
    - bgc-2485-root-source-reading
    - bgc-2485-joint-source-notes
    - bgc-2485-source-plan-execution
    - bgc-2485-source-plan-acceptance
    - bgc-2485-native-gate-limits
    - bgc-2485-curation-scope
    - bgc-2485-mechanism-absence
    - bgc-2485-selected-identity-comparison
    - bgc-2485-selected-comparison-source
    - bgc-2485-selected-comparison-plan
    - bgc-2485-selected-comparison-chemistry
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
- Own complete raw/history, first-five intake and molecular reading are joined to
  ROOT’s complete context4 source reading (9 frames/185 rows/1990 fields) and Native’s
  bounded cache/curation reconciliation. No exact current assay exclusion applies,
  but that finite table result does not validate protocols or resolve assay discordance.
  Representation and congener-stereochemistry limits, source-specific activity semantics
  and unavailable primary verification keep this review partial without transferring
  the separate A1B findings.
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
