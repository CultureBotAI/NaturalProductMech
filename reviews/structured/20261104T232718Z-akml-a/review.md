# Local evidence review: AKML A

- Review: 20261104T232718Z-akml-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T22:54:09.202701Z
- Finished UTC: 2026-11-04T23:27:18.115516Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

AKML A is encoded as a nitrogen-free24-member macrolactone with specified stereo. Source NRPS/TypeI and model Macrolides/Polyketides remain distinct claims; the bioactivity-tier citation supplies no saved assay.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2474; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-f0284afc2a | data/natural_products/unclassified/akml-a.yaml | generated | AKML A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-f0284afc2a | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-f0284afc2a | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-f0284afc2a | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-f0284afc2a | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-f0284afc2a | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-f0284afc2a | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-f0284afc2a | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-f0284afc2a | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-f0284afc2a.

Minted naturalproductmech:mibig-f0284afc2a retains AKML A key JCCCGICXZGLIKZ-OEMYMMPLSA-N, literal C24H40O4 and the BGC0002227 v3 structure. Exact retained ChEBI/occurrence/assay frames are empty; historical MINTED grounding is not a current external-search claim. AKML B and the directly linked C/D records remain distinct congeners with their own full keys/structures; neither shared locus nor similar name transfers identity or activity.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-f0284afc2a.

Both forms are neutral C24H40O4,28atoms/28bonds, with three specified tetrahedral centers and three specified double bonds. SMILES1R/15R/20S correspond to InChI21R/20R/22S; all three saved alkene bond labels are E. No potential stereo site is marked unspecified. The true flag agrees with the tetrahedral inventory, while the explicit bond table separately supplies the alkene scope. All ten stored-form comparisons are true, including full key, normalized InChI, canonical SMILES, formula, charge and atom/bond counts. The chirality-aware atom map covers the form atom count, while full_graph_identity_established remains false: neither independent full-graph nor natural-state identity is established. Eight run-level undefined-stereo warnings remain global and are not assigned to this owner.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-f0284afc2a.

BGC0002227 v3 retains A.luchuensis IFO4308/1033177 as SOURCE_ASSERTION and DF126453.1:1267994-1286654 as CLUSTER_UNSTATED with no stated methods. The cached A.kawachii IFO4308 alias is historical naming context for that strain scope, not experimental confirmation or a generic species claim. Raw BGC classes NRPS and subclass TypeI remain source fields even though the encoded molecule and model filing raise a distinct chemical-applicability question.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-f0284afc2a.

DOI10.1021/acs.orglett.0c01975 is retained at COMPOUND_BIOACTIVITY citation tier for both producer and locus assertions. This tier does not supply an assay measurement or causal production evidence by itself. The same DOI and locus across AKML congeners do not establish independent experiments. Two complete seed-history events are preserved; no paper or assay protocol was retrieved.

### Source-specific occurrence and assay assertions

evidence: supported. Targets: naturalproductmech:mibig-f0284afc2a.

No LOTUS, ChEBI-origin or CyanometDB row occurs in the saved exact-key scope, and the complete owner has no occurrence assertion. That bounded absence does not exclude occurrence in nature. The direct-BGC B/C/D records are context only, not new occurrences or independent chemical matches.

### Encoded macrolide and model output versus source NRPS attribution

consistency: unknown. Targets: naturalproductmech:mibig-f0284afc2a.

The named/versioned model reports Fatty acids plus Polyketides, Macrolides superclass, empty class array and false glycoside flag; two pathways cause UNCLASSIFIED filing. This remains separate from the source NRPS/TypeI BGC annotation. The conflict in scope must not be resolved by silently relabelling either the source locus or the chemical record; primary biosynthetic applicability remains unverified. The observed24-member carbon/oxygen lactone supports the structural Macrolides superclass. It supplies no peptide/amide topology and cannot independently explain or invalidate the retained source NRPS BGC classification. Biosynthetic pathway applicability is therefore unresolved despite concrete macrolactone structure.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-f0284afc2a.

One source concept, two seed-history events and the exact BGC coordinate/grade assertions are preserved. No additional source activity or occurrence is inferred. The source-versus-model classification distinction remains an explicit limitation, with no supported source edit. Actual canonical intake and accepted stored-form diagnostics are joined. Review remains partial because primary literature, current external identifiers/taxonomy, assay protocols and independent natural-state authentication are unavailable; full QC/OAK also remain unavailable.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2474-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/akml-a.yaml; Complete plaintext including every curation_history entry | supports | Complete AKML A owner with 2 history events; prior complete raw reading carries with current identical bytes. No source/status/history edit. |
| bgc-2474-capture | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2474-intake | /private/tmp/npm-review-work/shared-next-batch248/intakes/2474-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, ownership and all 40 input placements joined to current plan hashes. |
| bgc-2474-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch248/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/3 | supports | ROOT accepted the original canonical intake and exact plan; this owner’s actual inspection and receipt pins are located. |
| bgc-2474-grounding-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/label; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status; /records/3/owner_document/grounding_notes | supports | Exact retained identifier, structure, source concepts, cross-references, grounding and any open discussion. Historical grounding notes are not fresh authority searches. |
| bgc-2474-origin-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/producer_taxon_groups; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, declared coordinates and citation tiers; absent fields are not filled. |
| bgc-2474-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete owner supplies exact occurrence, activity and nested target assertions or bounded absence. Detection does not prove production; absent assays do not mean inactivity. |
| bgc-2474-classification-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway; /records/3/owner_document/bgc_class | supports | Exact named/versioned model arrays, glycoside flag, filing and separate source categories; retention fidelity is not biological-family or biosynthetic proof. |
| bgc-2474-history-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3/owner_document/curation_status; /records/3/owner_document/curation_history | supports | All history events and status are preserved; seeding/import remains distinct from fresh primary verification. |
| bgc-2474-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets roots, so no maintained reader applies. Its 0 native bioactivities and any nested target annotations remain separately retained. |
| bgc-2474-chemistry | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/literal_InChI_layers; /records/3/comparisons; /records/3/atom_correspondence; /records/3/smiles/computed/formula; /records/3/smiles/computed/formal_charge; /records/3/smiles/computed/standard_inchi; /records/3/smiles/computed/standard_inchi_key; /records/3/smiles/computed/canonical_isomeric_smiles; /records/3/smiles/computed/canonical_nonisomeric_smiles; /records/3/smiles/computed/atom_count; /records/3/smiles/computed/heavy_atom_count; /records/3/smiles/computed/bond_count; /records/3/smiles/computed/element_counts; /records/3/smiles/computed/stereo_counts; /records/3/inchi/computed/formula; /records/3/inchi/computed/formal_charge; /records/3/inchi/computed/standard_inchi; /records/3/inchi/computed/standard_inchi_key; /records/3/inchi/computed/canonical_isomeric_smiles; /records/3/inchi/computed/canonical_nonisomeric_smiles; /records/3/inchi/computed/atom_count; /records/3/inchi/computed/heavy_atom_count; /records/3/inchi/computed/bond_count; /records/3/inchi/computed/element_counts; /records/3/inchi/computed/stereo_counts | supports | All ten stored-form comparisons are true: normalized InChI/full key, formula, charge, atom/bond counts and canonical SMILES agree. A chirality-aware direct map covers the atom count; full_graph_identity_established remains false. These checks do not independently authenticate natural identity, microstate or stereochemistry. |
| bgc-2474-topology | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/literal_InChI_layers; /records/3/comparisons; /records/3/atom_correspondence; /records/3/smiles/computed/atoms; /records/3/smiles/computed/bonds; /records/3/smiles/computed/rings; /records/3/smiles/computed/potential_stereo; /records/3/smiles/computed/motifs; /records/3/smiles/computed/fragment_atom_indices; /records/3/inchi/computed/atoms; /records/3/inchi/computed/bonds; /records/3/inchi/computed/rings; /records/3/inchi/computed/potential_stereo; /records/3/inchi/computed/motifs; /records/3/inchi/computed/fragment_atom_indices | supports | Each saved form contains one24-member ring with23carbons and one oxygen, one carbonyl ester and two hydroxyl oxygens. SMILES C25(=O27)-O26-C15 closes the macrocyclic lactone; bonds10,18,23 are E. There is no nitrogen, amide, phosphorus or saturated six-member C5O candidate. This directly supports macrolactone topology without identifying a biosynthetic enzyme system. |
| bgc-2474-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-current248-first-five-diagnostic-reading-001.json; /records/3; /read_scope; /totals; /representation; /reading_caveats | supports | BGC personally read all ten complete first-five forms: 258 atom and 284 bond rows, and all 202 intake placements/48 paths. Exact table and intake factoring, original terminals and limits are recorded. |
| bgc-2474-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/3; /molecular_parse_attempts; /parsed; /global_warning_count; /method_scope; /interpretation_boundary | supports | ROOT accepted the original twenty stored forms. This owner’s actual comparison scope is located; eight warnings remain global and unassigned. No alternate parse or normalization repair is inferred. |
| bgc-2474-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins; stream interpretation is supplied separately. |
| bgc-2474-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | Undefined stereocenters remain explicit; named/versioned computed classification is never a source assertion. |
| bgc-2474-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The maintained stereo_complete flag tests unassigned tetrahedral centers; natural identity and double-bond geometry need their separate evidence scopes. |
| bgc-2474-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2474-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 126–145; 1318–1382 | supports | Source assay calls, endpoint values and target accessions are retained. Activity classes use assay-name matching on active rows and summaries derive from written classes; these are not independent potency measurements or protocol validation. |
| bgc-2474-source-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-current248-assigned-source-reading-001.json; /scope; /reading; /contexts; /cautions | supports | BGC personally read all five assigned contexts: 45 frames, 38 rows and 493 fields, including ten actual assay tuples. Complete prior raw/history readings carry by exact current bytes. |
| bgc-2474-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Complete disjoint source reading covers 135 frames/115 rows/1296 fields: BGC 38, ROOT 63 and Support 14 rows. Native cache/curation has zero positive-row credit; overlapping readings add none. |
| bgc-2474-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch248/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /original_terminal; /exit_code; /plan; /derivation; /inventory; /notes; /verification | supports | One original composer produced the exact 394-placement/56-path plan with 32 derivation operations; contexts, cautions and four separate identity-comparison placements are preserved. Actual intake acceptance separately binds this plan. |
| bgc-2474-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch248/root-current248-native-gates-acceptance-001.json; /status; /counts; /all_native_gates_passed; /unavailable | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed is false. Local validation does not complete scientific verification. |
| bgc-2474-curation-scope | /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | The bounded Native scan found one already implemented Albonoursin locus override, outside these first five, and 57 unrelated lexical hits. No exact assay exclusion applies among 22 retained tuples; one blank sentinel remains separate. |
| bgc-2474-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/28 | supports | Complete saved cache stanzas for this owner’s source taxa; cached names and synonyms do not independently establish current taxonomy, strain or producer identity. |
| bgc-2474-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/source_taxa; /contexts/8/source_scope_inventory/forward_taxon_merge_matches; /contexts/8/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and saved forwarding/nonorganism routes for this owner; no fresh taxonomy request. |
| bgc-2474-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /forward_routes; /interpretation | supports | Native personally read all 34 saved cache stanzas and 15 routes, including three unique saved merges in four contexts. These cached routes do not upgrade species, strain, occurrence or producer evidence. |
| bgc-2474-direct-contexts | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-target-input-plan-001.json; /records/3/proposed_companion_paths; /records/3/direct_companion_predicates | supports | Exact one-hop owned-BGC paths and predicates, including empty lists. There is no transitive expansion, identity equivalence or biological claim transfer. |
| bgc-2474-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/1/path; /contexts/1/identifier; /contexts/1/label; /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/1/source_scope_inventory/joins/mibig_compounds; /contexts/2/path; /contexts/2/identifier; /contexts/2/label; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/2/source_scope_inventory/joins/mibig_compounds; /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key; /contexts/9/owned_bgc_ids; /contexts/9/source_scope_inventory/joins/mibig_compounds | supports | Distinct exact companion identifiers, full keys, owned loci and complete structure-bearing MIBiG rows provide bounded context; shared BGC membership does not establish chemical identity, assay activity or production. |
| bgc-2474-root-companion-reading | /private/tmp/npm-review-work/shared-next-batch248/root-current248-companion-whole-reading-001.json; /records; /counts; /scope; /context_limits | supports | ROOT personally read all five unselected companion owners/history: B2, sterigmatocystin, AKML C/D and alchivemycin A. Their mechanisms, structures and activities remain owner-specific. |
| bgc-2474-root-source-reading | /private/tmp/npm-review-work/shared-next-batch248/root-current248-source-row-reading-001.json; /context_indices; /named_query_frames; /positive_row_placements; /positive_row_fields; /whole_payload_readings; /scientific_cautions | supports | ROOT read all five unselected source contexts plus Albonoursin: 54 frames/63 rows/615 fields, separately credited and bounded to those owners. |
| bgc-2474-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2474-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2657–2657; row_sha256 23370542da7481d7ce9fd7506ed3d124d07f867f23a565cd8f8a360e0fe6ab32 | supports | Exact compound/version, structure/key, database IDs, producer/locus grades and citation tiers. BGC complete source reading and current physical bytes are joined. |
| bgc-2474-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2474-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2474-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2474-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2474-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1079–1079; row_sha256 7a3922cfbb2228a67bced1d22b8492a37a833f5158c6a240477607d48ad07c90 | supports | Exact named/versioned model arrays and glycoside flag; applicability is assessed separately. BGC complete source reading and current physical bytes are joined. |
| bgc-2474-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2474-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2474-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2474-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame has 0 placements with exact query, predicate and all matched fields. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-248/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-248/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-248/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-248/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-248/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; fresh primary literature, current authority/taxonomy, assay protocols and independent natural identity/stereochemical authentication remain unavailable.
- Five local commands passed, while full QC and OAK remain unavailable. All stored-form comparisons agree and maps span atom counts, but full_graph_identity_established remains false.
- Producer, locus, occurrence, strain and citation tiers remain separate; shared BGCs/CIDs and repeated references do not transfer biological claims or establish independent experiments.
- Model-family and biosynthetic applicability remain qualified. G1/generic shared-CID correspondence is unresolved; AKML structural macrolides do not by themselves validate or refute source NRPS attribution.
- No graph, pathway, component-reference or molecular-target root is declared in these five. B1/G1 bioactivities and B1 nested target remain explicit; no maintained-reader result, natural-state proof or source-edit promotion is claimed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read ten complete forms: 258 atoms and 284 bonds, all strings/scalars/rings/stereo/motifs/maps. Indices are diagnostic-local; eight warnings remain global and unassigned.
- Source reading is disjoint: BGC five contexts/45 frames/38 rows/493 fields; ROOT six contexts/54 frames/63 rows/615 fields; Support four contexts/36 frames/14 rows/188 fields. Native 34 cache stanzas and bounded curation receive zero positive-row credit.
- BGC operated the original collector and composer; Support operated canonical intakes; Native operated diagnostic under ROOT delegation. This fragment reads saved artifacts only.
- All five reviews remain partial. No supported source-edit finding or action is proposed; unresolved exact cross-reference correspondence is retained as an identity limitation.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T232718Z-akml-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: AKML A'
started_at: '2026-11-04T22:54:09.202701Z'
finished_at: '2026-11-04T23:27:18.115516Z'
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
summary: AKML A is encoded as a nitrogen-free24-member macrolactone with specified
  stereo. Source NRPS/TypeI and model Macrolides/Polyketides remain distinct claims;
  the bioactivity-tier citation supplies no saved assay.
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
  - path: data/natural_products/polyketides/akml-c.yaml
    sha256: 1e08ac5c8841ac58c6a4e6c86b8bf8c4a1d855f7dfe8a249a4ccd75061ce97b8
    role: context
  - path: data/natural_products/polyketides/akml-d.yaml
    sha256: 6d88ca3c7c6b5649bd44f0c240cef696c5e2f8421af511fda9585430b80926bb
    role: context
  - path: data/natural_products/unclassified/akml-a.yaml
    sha256: e9550f42ba806d9ffcddbefb7c7c852b22825f2c968ee7860a684b82ee49b7ba
    role: target
  - path: data/natural_products/unclassified/akml-b.yaml
    sha256: 774bbd7c9392d74ac62a4dbf22ff6e8d6f17ca34c2babad2dae7e68836153d4e
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
  selection: Campaign path order 2474; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-f0284afc2a
targets:
- target_id: naturalproductmech:mibig-f0284afc2a
  path: data/natural_products/unclassified/akml-a.yaml
  label: AKML A
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
  - naturalproductmech:mibig-f0284afc2a
  command: just validate-strict data/natural_products/unclassified/aflatoxin-b1.yaml
    data/natural_products/unclassified/aflatoxin-g1.yaml data/natural_products/unclassified/aflatoxin.yaml
    data/natural_products/unclassified/akml-a.yaml data/natural_products/unclassified/akml-b.yaml
    data/natural_products/unclassified/albonoursin.yaml data/natural_products/unclassified/alchivemycin-b.yaml
    data/natural_products/unclassified/althiomycin.yaml data/natural_products/unclassified/amipurimycin-2.yaml
    data/natural_products/unclassified/amipurimycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-248/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-f0284afc2a
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-248/validate-all-001.tsv
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
  - naturalproductmech:mibig-f0284afc2a
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
  - naturalproductmech:mibig-f0284afc2a
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
  - naturalproductmech:mibig-f0284afc2a
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-248/review-queue-001.tsv
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
  - naturalproductmech:mibig-f0284afc2a
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2474-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/akml-a.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete AKML A owner with 2 history events; prior complete raw reading
    carries with current identical bytes. No source/status/history edit.
  snapshot_sha256: e9550f42ba806d9ffcddbefb7c7c852b22825f2c968ee7860a684b82ee49b7ba
- evidence_id: bgc-2474-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/intakes/2474-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Actual canonical target, ownership and all 40 input placements joined to
    current plan hashes.
  snapshot_sha256: 3e4af88ea038a98f2f1b6eb835c602012a89f3c1b1f9cd514d6c1a9592b76070
- evidence_id: bgc-2474-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/3
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: ROOT accepted the original canonical intake and exact plan; this owner’s
    actual inspection and receipt pins are located.
  snapshot_sha256: f87f72eb2a281d4f80f9b05b6da75a212ac84262eb85a2c7deda4880bf4cb3ac
- evidence_id: bgc-2474-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/label;
    /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts;
    /records/3/owner_document/grounding_status; /records/3/owner_document/grounding_notes
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact retained identifier, structure, source concepts, cross-references,
    grounding and any open discussion. Historical grounding notes are not fresh authority
    searches.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/producer_taxon_groups;
    /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/source_concepts
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, declared coordinates
    and citation tiers; absent fields are not filled.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete owner supplies exact occurrence, activity and nested target assertions
    or bounded absence. Detection does not prove production; absent assays do not
    mean inactivity.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/np_pathway;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact named/versioned model arrays, glycoside flag, filing and separate
    source categories; retention fidelity is not biological-family or biosynthetic
    proof.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_status; /records/3/owner_document/curation_history
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: All history events and status are preserved; seeding/import remains distinct
    from fresh primary verification.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets roots, so no maintained reader applies. Its 0 native bioactivities
    and any nested target annotations remain separately retained.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: bgc-2474-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/literal_InChI_layers; /records/3/comparisons;
    /records/3/atom_correspondence; /records/3/smiles/computed/formula; /records/3/smiles/computed/formal_charge;
    /records/3/smiles/computed/standard_inchi; /records/3/smiles/computed/standard_inchi_key;
    /records/3/smiles/computed/canonical_isomeric_smiles; /records/3/smiles/computed/canonical_nonisomeric_smiles;
    /records/3/smiles/computed/atom_count; /records/3/smiles/computed/heavy_atom_count;
    /records/3/smiles/computed/bond_count; /records/3/smiles/computed/element_counts;
    /records/3/smiles/computed/stereo_counts; /records/3/inchi/computed/formula; /records/3/inchi/computed/formal_charge;
    /records/3/inchi/computed/standard_inchi; /records/3/inchi/computed/standard_inchi_key;
    /records/3/inchi/computed/canonical_isomeric_smiles; /records/3/inchi/computed/canonical_nonisomeric_smiles;
    /records/3/inchi/computed/atom_count; /records/3/inchi/computed/heavy_atom_count;
    /records/3/inchi/computed/bond_count; /records/3/inchi/computed/element_counts;
    /records/3/inchi/computed/stereo_counts
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: 'All ten stored-form comparisons are true: normalized InChI/full key, formula,
    charge, atom/bond counts and canonical SMILES agree. A chirality-aware direct
    map covers the atom count; full_graph_identity_established remains false. These
    checks do not independently authenticate natural identity, microstate or stereochemistry.'
  snapshot_sha256: fe37d4f7a6c507b5efcc54c9e6513c21060d9243d2794faa75d700b3b100ee3b
- evidence_id: bgc-2474-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/literal_InChI_layers; /records/3/comparisons;
    /records/3/atom_correspondence; /records/3/smiles/computed/atoms; /records/3/smiles/computed/bonds;
    /records/3/smiles/computed/rings; /records/3/smiles/computed/potential_stereo;
    /records/3/smiles/computed/motifs; /records/3/smiles/computed/fragment_atom_indices;
    /records/3/inchi/computed/atoms; /records/3/inchi/computed/bonds; /records/3/inchi/computed/rings;
    /records/3/inchi/computed/potential_stereo; /records/3/inchi/computed/motifs;
    /records/3/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Each saved form contains one24-member ring with23carbons and one oxygen,
    one carbonyl ester and two hydroxyl oxygens. SMILES C25(=O27)-O26-C15 closes the
    macrocyclic lactone; bonds10,18,23 are E. There is no nitrogen, amide, phosphorus
    or saturated six-member C5O candidate. This directly supports macrolactone topology
    without identifying a biosynthetic enzyme system.
  snapshot_sha256: fe37d4f7a6c507b5efcc54c9e6513c21060d9243d2794faa75d700b3b100ee3b
- evidence_id: bgc-2474-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-current248-first-five-diagnostic-reading-001.json
  locator: /records/3; /read_scope; /totals; /representation; /reading_caveats
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: 'BGC personally read all ten complete first-five forms: 258 atom and 284
    bond rows, and all 202 intake placements/48 paths. Exact table and intake factoring,
    original terminals and limits are recorded.'
  snapshot_sha256: b40879bdaab5c53ab68303db7f659f037621df138785d495f873addfb6397e9f
- evidence_id: bgc-2474-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/3; /molecular_parse_attempts; /parsed;
    /global_warning_count; /method_scope; /interpretation_boundary
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: ROOT accepted the original twenty stored forms. This owner’s actual comparison
    scope is located; eight warnings remain global and unassigned. No alternate parse
    or normalization repair is inferred.
  snapshot_sha256: 41385e734709ffb4be37d705ba14138074f919e8ec530b5fe226af2a54f084a3
- evidence_id: bgc-2474-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins;
    stream interpretation is supplied separately.
  snapshot_sha256: 50e6d82d0a03ece4185009e6997df38fc53c2ee4a2e5ee4731557c1554fcffbe
- evidence_id: bgc-2474-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Undefined stereocenters remain explicit; named/versioned computed classification
    is never a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2474-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: The maintained stereo_complete flag tests unassigned tetrahedral centers;
    natural identity and double-bond geometry need their separate evidence scopes.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2474-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays
    remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2474-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 126–145; 1318–1382
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Source assay calls, endpoint values and target accessions are retained.
    Activity classes use assay-name matching on active rows and summaries derive from
    written classes; these are not independent potency measurements or protocol validation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2474-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-current248-assigned-source-reading-001.json
  locator: /scope; /reading; /contexts; /cautions
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: 'BGC personally read all five assigned contexts: 45 frames, 38 rows and
    493 fields, including ten actual assay tuples. Complete prior raw/history readings
    carry by exact current bytes.'
  snapshot_sha256: 65e1d6b25177746987e9fbca3c2e652b0be93df5deef0aec1ce5bcfd444644d2
- evidence_id: bgc-2474-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: 'Complete disjoint source reading covers 135 frames/115 rows/1296 fields:
    BGC 38, ROOT 63 and Support 14 rows. Native cache/curation has zero positive-row
    credit; overlapping readings add none.'
  snapshot_sha256: 677fa47e38b38fd68d1bcf303c6c209b2f27162b6297c48aafdaf6faabdcd759
- evidence_id: bgc-2474-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /original_terminal; /exit_code; /plan;
    /derivation; /inventory; /notes; /verification
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: One original composer produced the exact 394-placement/56-path plan with
    32 derivation operations; contexts, cautions and four separate identity-comparison
    placements are preserved. Actual intake acceptance separately binds this plan.
  snapshot_sha256: d40c3e02d03edac5e9b1db9d96b102c645797330a4a7337c53b8cbb9f3e24fce
- evidence_id: bgc-2474-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-current248-native-gates-acceptance-001.json
  locator: /status; /counts; /all_native_gates_passed; /unavailable
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    is false. Local validation does not complete scientific verification.
  snapshot_sha256: d75d6732343dc0879691908d20a2421dbe9ae50115c682a64132249d8074a4b4
- evidence_id: bgc-2474-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: The bounded Native scan found one already implemented Albonoursin locus
    override, outside these first five, and 57 unrelated lexical hits. No exact assay
    exclusion applies among 22 retained tuples; one blank sentinel remains separate.
  snapshot_sha256: 74baac5175595ad8100603064c8b260f4478e6f3df17e0e3bd7a5f882a763638
  search_scope: All 15 current contexts, 230 literal tokens and 11 enumerated TSVs
    including ignored files; nine eligible tables/3422 rows. Exact applicability uses
    retained owner/source/full-key/BGC/name/taxon predicates, not global absence or
    assay-protocol validation.
- evidence_id: bgc-2474-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/28
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved cache stanzas for this owner’s source taxa; cached names
    and synonyms do not independently establish current taxonomy, strain or producer
    identity.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: bgc-2474-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/source_taxa; /contexts/8/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/8/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact source taxon IDs and saved forwarding/nonorganism routes for this
    owner; no fresh taxonomy request.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: bgc-2474-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /forward_routes; /interpretation
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Native personally read all 34 saved cache stanzas and 15 routes, including
    three unique saved merges in four contexts. These cached routes do not upgrade
    species, strain, occurrence or producer evidence.
  snapshot_sha256: a707cc6012faf88e8edeaddd6023fcb24a8468c3cad108257ee28d4b602e0bf6
- evidence_id: bgc-2474-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-target-input-plan-001.json
  locator: /records/3/proposed_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact one-hop owned-BGC paths and predicates, including empty lists. There
    is no transitive expansion, identity equivalence or biological claim transfer.
  snapshot_sha256: 0c3bd623561801ca680bca9af98bbd1e21a2f7dc5ca0bc13a2e8e8654159d436
- evidence_id: bgc-2474-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/1/path; /contexts/1/identifier; /contexts/1/label; /contexts/1/standard_inchi_key;
    /contexts/1/owned_bgc_ids; /contexts/1/source_scope_inventory/joins/mibig_compounds;
    /contexts/2/path; /contexts/2/identifier; /contexts/2/label; /contexts/2/standard_inchi_key;
    /contexts/2/owned_bgc_ids; /contexts/2/source_scope_inventory/joins/mibig_compounds;
    /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key;
    /contexts/9/owned_bgc_ids; /contexts/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Distinct exact companion identifiers, full keys, owned loci and complete
    structure-bearing MIBiG rows provide bounded context; shared BGC membership does
    not establish chemical identity, assay activity or production.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: bgc-2474-root-companion-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-current248-companion-whole-reading-001.json
  locator: /records; /counts; /scope; /context_limits
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: 'ROOT personally read all five unselected companion owners/history: B2,
    sterigmatocystin, AKML C/D and alchivemycin A. Their mechanisms, structures and
    activities remain owner-specific.'
  snapshot_sha256: 55900858ef082653d7865439b7ad581a12c6b98812ae2d48e6994feee3bdec7a
- evidence_id: bgc-2474-root-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-current248-source-row-reading-001.json
  locator: /context_indices; /named_query_frames; /positive_row_placements; /positive_row_fields;
    /whole_payload_readings; /scientific_cautions
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: 'ROOT read all five unselected source contexts plus Albonoursin: 54 frames/63
    rows/615 fields, separately credited and bounded to those owners.'
  snapshot_sha256: b03407dab38283949dfdecd53d2a3308b5b7e0d4fafcb1fb22adb26c4ad1277d
- evidence_id: bgc-2474-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved mibig_compounds frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2657–2657; row_sha256 23370542da7481d7ce9fd7506ed3d124d07f867f23a565cd8f8a360e0fe6ab32
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact compound/version, structure/key, database IDs, producer/locus grades
    and citation tiers. BGC complete source reading and current physical bytes are
    joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2474-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved chebi_structures frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved lotus_occurrences frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved npclassifier frame has 1 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching payload or the empty
    frame is retained; no query replay.
- evidence_id: bgc-2474-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1079–1079; row_sha256 7a3922cfbb2228a67bced1d22b8492a37a833f5158c6a240477607d48ad07c90
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; applicability is
    assessed separately. BGC complete source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2474-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved bindingdb_targets frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "JCCCGICXZGLIKZ-OEMYMMPLSA-N". Every
    matching payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2474-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T23:19:42.969113Z'
  support: supports
  summary: Complete saved chebi_origins frame has 0 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Every matching payload or the empty frame
    is retained; no query replay.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:00:05.428362Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 05f7ff44ff39609faa785f7d8316778db38b3e466a7b42ac04af854d325189d9
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:00:29.630261Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 573bb35b53b63fe06f28e8a2fde2228099a315c85116ab728b231cb78ca10e31
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:00:48.761900Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:01:22.418928Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:01:34.024377Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: aa37a5e7f7dca8035ff37f45b3abcecacfe21927b7db12caf18af4a107e9a98d
assessments:
- assessment_id: bgc-2474-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: Minted naturalproductmech:mibig-f0284afc2a retains AKML A key JCCCGICXZGLIKZ-OEMYMMPLSA-N,
    literal C24H40O4 and the BGC0002227 v3 structure. Exact retained ChEBI/occurrence/assay
    frames are empty; historical MINTED grounding is not a current external-search
    claim. AKML B and the directly linked C/D records remain distinct congeners with
    their own full keys/structures; neither shared locus nor similar name transfers
    identity or activity.
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-grounding-owner
  - bgc-2474-chemistry
  - bgc-2474-source-mibig_compounds
  - bgc-2474-query-chebi_structures
  - bgc-2474-direct-contexts
  - bgc-2474-companion-boundaries
  - bgc-2474-root-companion-reading
  - bgc-2474-root-source-reading
  dimensions:
  - name: standard_inchi_key
    value: JCCCGICXZGLIKZ-OEMYMMPLSA-N; retained key, not natural-identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2474-grounding-owner
    - bgc-2474-chemistry
    - bgc-2474-source-mibig_compounds
    - bgc-2474-query-chebi_structures
    - bgc-2474-direct-contexts
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
  - name: grounding_scope
    value: Minted naturalproductmech:mibig-f0284afc2a retains AKML A key JCCCGICXZGLIKZ-OEMYMMPLSA-N,
      literal C24H40O4 and the BGC0002227 v3 structure. Exact retained ChEBI/occurrence/assay
      frames are empty; historical MINTED grounding is not a current external-search
      claim. AKML B and the directly linked C/D records remain distinct congeners
      with their own full keys/structures; neither shared locus nor similar name transfers
      identity or activity.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2474-grounding-owner
    - bgc-2474-chemistry
    - bgc-2474-source-mibig_compounds
    - bgc-2474-query-chebi_structures
    - bgc-2474-direct-contexts
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
- assessment_id: bgc-2474-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: 'Both forms are neutral C24H40O4,28atoms/28bonds, with three specified
    tetrahedral centers and three specified double bonds. SMILES1R/15R/20S correspond
    to InChI21R/20R/22S; all three saved alkene bond labels are E. No potential stereo
    site is marked unspecified. The true flag agrees with the tetrahedral inventory,
    while the explicit bond table separately supplies the alkene scope. All ten stored-form
    comparisons are true, including full key, normalized InChI, canonical SMILES,
    formula, charge and atom/bond counts. The chirality-aware atom map covers the
    form atom count, while full_graph_identity_established remains false: neither
    independent full-graph nor natural-state identity is established. Eight run-level
    undefined-stereo warnings remain global and are not assigned to this owner.'
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-grounding-owner
  - bgc-2474-chemistry
  - bgc-2474-topology
  - bgc-2474-diagnostic-reading
  - bgc-2474-diagnostic-acceptance
  - bgc-2474-structure-schema
  - bgc-2474-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: 'Both forms are neutral C24H40O4,28atoms/28bonds, with three specified
      tetrahedral centers and three specified double bonds. SMILES1R/15R/20S correspond
      to InChI21R/20R/22S; all three saved alkene bond labels are E. No potential
      stereo site is marked unspecified. The true flag agrees with the tetrahedral
      inventory, while the explicit bond table separately supplies the alkene scope.
      All ten stored-form comparisons are true, including full key, normalized InChI,
      canonical SMILES, formula, charge and atom/bond counts. The chirality-aware
      atom map covers the form atom count, while full_graph_identity_established remains
      false: neither independent full-graph nor natural-state identity is established.
      Eight run-level undefined-stereo warnings remain global and are not assigned
      to this owner.'
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2474-grounding-owner
    - bgc-2474-chemistry
    - bgc-2474-topology
    - bgc-2474-diagnostic-reading
    - bgc-2474-diagnostic-acceptance
    - bgc-2474-structure-schema
    - bgc-2474-stereo-method
  - name: representation_correspondence
    value: 'All ten stored-form comparisons are true: normalized InChI/full key, formula,
      charge, atom/bond counts and canonical SMILES agree. A chirality-aware direct
      map covers the atom count; full_graph_identity_established remains false. These
      checks do not independently authenticate natural identity, microstate or stereochemistry.'
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2474-grounding-owner
    - bgc-2474-chemistry
    - bgc-2474-topology
    - bgc-2474-diagnostic-reading
    - bgc-2474-diagnostic-acceptance
    - bgc-2474-structure-schema
    - bgc-2474-stereo-method
- assessment_id: bgc-2474-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: BGC0002227 v3 retains A.luchuensis IFO4308/1033177 as SOURCE_ASSERTION
    and DF126453.1:1267994-1286654 as CLUSTER_UNSTATED with no stated methods. The
    cached A.kawachii IFO4308 alias is historical naming context for that strain scope,
    not experimental confirmation or a generic species claim. Raw BGC classes NRPS
    and subclass TypeI remain source fields even though the encoded molecule and model
    filing raise a distinct chemical-applicability question.
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-origin-owner
  - bgc-2474-occurrence-owner
  - bgc-2474-source-mibig_compounds
  - bgc-2474-cached-taxonomy
  - bgc-2474-taxonomy-routes
  - bgc-2474-curation-scope
  - bgc-2474-direct-contexts
  - bgc-2474-companion-boundaries
  - bgc-2474-root-companion-reading
  - bgc-2474-root-source-reading
  dimensions:
  - name: taxon_scope
    value: BGC0002227 v3 retains A.luchuensis IFO4308/1033177 as SOURCE_ASSERTION
      and DF126453.1:1267994-1286654 as CLUSTER_UNSTATED with no stated methods. The
      cached A.kawachii IFO4308 alias is historical naming context for that strain
      scope, not experimental confirmation or a generic species claim. Raw BGC classes
      NRPS and subclass TypeI remain source fields even though the encoded molecule
      and model filing raise a distinct chemical-applicability question.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2474-origin-owner
    - bgc-2474-occurrence-owner
    - bgc-2474-source-mibig_compounds
    - bgc-2474-cached-taxonomy
    - bgc-2474-taxonomy-routes
    - bgc-2474-curation-scope
    - bgc-2474-direct-contexts
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
  - name: producer_evidence
    value: BGC0002227 v3 retains A.luchuensis IFO4308/1033177 as SOURCE_ASSERTION
      and DF126453.1:1267994-1286654 as CLUSTER_UNSTATED with no stated methods. The
      cached A.kawachii IFO4308 alias is historical naming context for that strain
      scope, not experimental confirmation or a generic species claim. Raw BGC classes
      NRPS and subclass TypeI remain source fields even though the encoded molecule
      and model filing raise a distinct chemical-applicability question.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2474-origin-owner
    - bgc-2474-occurrence-owner
    - bgc-2474-source-mibig_compounds
    - bgc-2474-cached-taxonomy
    - bgc-2474-taxonomy-routes
    - bgc-2474-curation-scope
    - bgc-2474-direct-contexts
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
  - name: locus_evidence
    value: BGC0002227 v3 retains A.luchuensis IFO4308/1033177 as SOURCE_ASSERTION
      and DF126453.1:1267994-1286654 as CLUSTER_UNSTATED with no stated methods. The
      cached A.kawachii IFO4308 alias is historical naming context for that strain
      scope, not experimental confirmation or a generic species claim. Raw BGC classes
      NRPS and subclass TypeI remain source fields even though the encoded molecule
      and model filing raise a distinct chemical-applicability question.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2474-origin-owner
    - bgc-2474-occurrence-owner
    - bgc-2474-source-mibig_compounds
    - bgc-2474-cached-taxonomy
    - bgc-2474-taxonomy-routes
    - bgc-2474-curation-scope
    - bgc-2474-direct-contexts
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
- assessment_id: bgc-2474-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: DOI10.1021/acs.orglett.0c01975 is retained at COMPOUND_BIOACTIVITY citation
    tier for both producer and locus assertions. This tier does not supply an assay
    measurement or causal production evidence by itself. The same DOI and locus across
    AKML congeners do not establish independent experiments. Two complete seed-history
    events are preserved; no paper or assay protocol was retrieved.
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-owner
  - bgc-2474-history-owner
  - bgc-2474-origin-owner
  - bgc-2474-occurrence-owner
  - bgc-2474-source-mibig_compounds
  - bgc-2474-source-reading
  - bgc-2474-companion-boundaries
  - bgc-2474-root-companion-reading
  - bgc-2474-root-source-reading
  dimensions:
  - name: citation_scope
    value: DOI10.1021/acs.orglett.0c01975 is retained at COMPOUND_BIOACTIVITY citation
      tier for both producer and locus assertions. This tier does not supply an assay
      measurement or causal production evidence by itself. The same DOI and locus
      across AKML congeners do not establish independent experiments. Two complete
      seed-history events are preserved; no paper or assay protocol was retrieved.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2474-owner
    - bgc-2474-history-owner
    - bgc-2474-origin-owner
    - bgc-2474-occurrence-owner
    - bgc-2474-source-mibig_compounds
    - bgc-2474-source-reading
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
- assessment_id: bgc-2474-occurrence
  area: evidence
  topic: Source-specific occurrence and assay assertions
  outcome: supported
  summary: No LOTUS, ChEBI-origin or CyanometDB row occurs in the saved exact-key
    scope, and the complete owner has no occurrence assertion. That bounded absence
    does not exclude occurrence in nature. The direct-BGC B/C/D records are context
    only, not new occurrences or independent chemical matches.
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-occurrence-owner
  - bgc-2474-mechanism-absence
  - bgc-2474-query-lotus_occurrences
  - bgc-2474-query-chebi_origins
  - bgc-2474-query-cyanometdb_occurrences
  - bgc-2474-query-pubchem_bioassay
  - bgc-2474-query-bindingdb_targets
  - bgc-2474-query-antibioticmech_inchikeys
  - bgc-2474-cached-taxonomy
  - bgc-2474-taxonomy-routes
  - bgc-2474-taxonomy-reading
  - bgc-2474-curation-scope
  - bgc-2474-bioactivity-seeder
  - bgc-2474-companion-boundaries
  - bgc-2474-root-companion-reading
  - bgc-2474-root-source-reading
  dimensions:
  - name: occurrence_scope
    value: No LOTUS, ChEBI-origin or CyanometDB row occurs in the saved exact-key
      scope, and the complete owner has no occurrence assertion. That bounded absence
      does not exclude occurrence in nature. The direct-BGC B/C/D records are context
      only, not new occurrences or independent chemical matches.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2474-occurrence-owner
    - bgc-2474-mechanism-absence
    - bgc-2474-query-lotus_occurrences
    - bgc-2474-query-chebi_origins
    - bgc-2474-query-cyanometdb_occurrences
    - bgc-2474-query-pubchem_bioassay
    - bgc-2474-query-bindingdb_targets
    - bgc-2474-query-antibioticmech_inchikeys
    - bgc-2474-cached-taxonomy
    - bgc-2474-taxonomy-routes
    - bgc-2474-taxonomy-reading
    - bgc-2474-curation-scope
    - bgc-2474-bioactivity-seeder
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
  - name: assay_target_scope
    value: No native bioactivity or exact-key PubChem/BindingDB/AntibioticMech row
      is retained. The COMPOUND_BIOACTIVITY DOI is citation provenance, not an imported
      numerical assay or inactivity call. No causal graph, pathway, component or molecular_targets
      root applies and no maintained-reader outcome is asserted.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2474-occurrence-owner
    - bgc-2474-mechanism-absence
    - bgc-2474-query-lotus_occurrences
    - bgc-2474-query-chebi_origins
    - bgc-2474-query-cyanometdb_occurrences
    - bgc-2474-query-pubchem_bioassay
    - bgc-2474-query-bindingdb_targets
    - bgc-2474-query-antibioticmech_inchikeys
    - bgc-2474-cached-taxonomy
    - bgc-2474-taxonomy-routes
    - bgc-2474-taxonomy-reading
    - bgc-2474-curation-scope
    - bgc-2474-bioactivity-seeder
    - bgc-2474-companion-boundaries
    - bgc-2474-root-companion-reading
    - bgc-2474-root-source-reading
- assessment_id: bgc-2474-classification
  area: consistency
  topic: Encoded macrolide and model output versus source NRPS attribution
  outcome: unknown
  summary: The named/versioned model reports Fatty acids plus Polyketides, Macrolides
    superclass, empty class array and false glycoside flag; two pathways cause UNCLASSIFIED
    filing. This remains separate from the source NRPS/TypeI BGC annotation. The conflict
    in scope must not be resolved by silently relabelling either the source locus
    or the chemical record; primary biosynthetic applicability remains unverified.
    The observed24-member carbon/oxygen lactone supports the structural Macrolides
    superclass. It supplies no peptide/amide topology and cannot independently explain
    or invalidate the retained source NRPS BGC classification. Biosynthetic pathway
    applicability is therefore unresolved despite concrete macrolactone structure.
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-classification-owner
  - bgc-2474-source-npclassifier
  - bgc-2474-chemistry
  - bgc-2474-topology
  - bgc-2474-structure-schema
  - bgc-2474-classification-seeder
  - bgc-2474-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: The named/versioned model reports Fatty acids plus Polyketides, Macrolides
      superclass, empty class array and false glycoside flag; two pathways cause UNCLASSIFIED
      filing. This remains separate from the source NRPS/TypeI BGC annotation. The
      conflict in scope must not be resolved by silently relabelling either the source
      locus or the chemical record; primary biosynthetic applicability remains unverified.
      The observed24-member carbon/oxygen lactone supports the structural Macrolides
      superclass. It supplies no peptide/amide topology and cannot independently explain
      or invalidate the retained source NRPS BGC classification. Biosynthetic pathway
      applicability is therefore unresolved despite concrete macrolactone structure.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2474-classification-owner
    - bgc-2474-source-npclassifier
    - bgc-2474-chemistry
    - bgc-2474-topology
    - bgc-2474-structure-schema
    - bgc-2474-classification-seeder
    - bgc-2474-source-mibig_compounds
- assessment_id: bgc-2474-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: One source concept, two seed-history events and the exact BGC coordinate/grade
    assertions are preserved. No additional source activity or occurrence is inferred.
    The source-versus-model classification distinction remains an explicit limitation,
    with no supported source edit. Actual canonical intake and accepted stored-form
    diagnostics are joined. Review remains partial because primary literature, current
    external identifiers/taxonomy, assay protocols and independent natural-state authentication
    are unavailable; full QC/OAK also remain unavailable.
  target_ids:
  - naturalproductmech:mibig-f0284afc2a
  evidence_ids:
  - bgc-2474-owner
  - bgc-2474-capture
  - bgc-2474-intake
  - bgc-2474-intake-acceptance
  - bgc-2474-history-owner
  - bgc-2474-diagnostic-reading
  - bgc-2474-diagnostic-acceptance
  - bgc-2474-diagnostic-execution
  - bgc-2474-source-reading
  - bgc-2474-joint-source-notes
  - bgc-2474-source-plan-execution
  - bgc-2474-native-gate-limits
  - bgc-2474-curation-scope
  - bgc-2474-mechanism-absence
  dimensions:
  - name: review_completion
    value: One source concept, two seed-history events and the exact BGC coordinate/grade
      assertions are preserved. No additional source activity or occurrence is inferred.
      The source-versus-model classification distinction remains an explicit limitation,
      with no supported source edit. Actual canonical intake and accepted stored-form
      diagnostics are joined. Review remains partial because primary literature, current
      external identifiers/taxonomy, assay protocols and independent natural-state
      authentication are unavailable; full QC/OAK also remain unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2474-owner
    - bgc-2474-capture
    - bgc-2474-intake
    - bgc-2474-intake-acceptance
    - bgc-2474-history-owner
    - bgc-2474-diagnostic-reading
    - bgc-2474-diagnostic-acceptance
    - bgc-2474-diagnostic-execution
    - bgc-2474-source-reading
    - bgc-2474-joint-source-notes
    - bgc-2474-source-plan-execution
    - bgc-2474-native-gate-limits
    - bgc-2474-curation-scope
    - bgc-2474-mechanism-absence
findings: []
actions: []
limitations:
- Retained local evidence only; fresh primary literature, current authority/taxonomy,
  assay protocols and independent natural identity/stereochemical authentication remain
  unavailable.
- Five local commands passed, while full QC and OAK remain unavailable. All stored-form
  comparisons agree and maps span atom counts, but full_graph_identity_established
  remains false.
- Producer, locus, occurrence, strain and citation tiers remain separate; shared BGCs/CIDs
  and repeated references do not transfer biological claims or establish independent
  experiments.
- Model-family and biosynthetic applicability remain qualified. G1/generic shared-CID
  correspondence is unresolved; AKML structural macrolides do not by themselves validate
  or refute source NRPS attribution.
- No graph, pathway, component-reference or molecular-target root is declared in these
  five. B1/G1 bioactivities and B1 nested target remain explicit; no maintained-reader
  result, natural-state proof or source-edit promotion is claimed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read ten complete forms: 258 atoms and 284 bonds, all strings/scalars/rings/stereo/motifs/maps.
  Indices are diagnostic-local; eight warnings remain global and unassigned.'
- 'Source reading is disjoint: BGC five contexts/45 frames/38 rows/493 fields; ROOT
  six contexts/54 frames/63 rows/615 fields; Support four contexts/36 frames/14 rows/188
  fields. Native 34 cache stanzas and bounded curation receive zero positive-row credit.'
- BGC operated the original collector and composer; Support operated canonical intakes;
  Native operated diagnostic under ROOT delegation. This fragment reads saved artifacts
  only.
- All five reviews remain partial. No supported source-edit finding or action is proposed;
  unresolved exact cross-reference correspondence is retained as an identity limitation.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-248
```
