# Local evidence review: cacaoidin

- Review: 20261105T113705Z-cacaoidin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T10:22:47.022610Z
- Finished UTC: 2026-11-05T11:37:05.950491Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Cacaoidin retains a coherent standardized encoding of a sulfur-bridged, glycosylated peptide, with one unassigned atom center and substantial amide/imidic representation differences. The producer assertion and demonstrated locus have different evidence grades. The computed depsipeptide label remains an applicability question because no ester is present in the stored form; no source edit is justified by the retained evidence alone.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2541; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1bd1037c43 | data/natural_products/unclassified/cacaoidin.yaml | generated | cacaoidin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-1bd1037c43 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-1bd1037c43 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-1bd1037c43 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-1bd1037c43 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-1bd1037c43 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-1bd1037c43 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-1bd1037c43 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-1bd1037c43 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-1bd1037c43.

The minted MIBiG-derived identifier and NPA031549 cross-reference remain retained database grounding, not fresh authority verification. Both stored forms produce AIRSSZAIEIYYPQ-QBIWCITBSA-N and C108H164N24O32S2 with neutral charge. The full key and standardized InChI agree, but natural identity and the unassigned stereocenter are not independently established. There is no direct companion or mechanism owner in the bounded map.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-1bd1037c43.

Both forms retain thirty-two assigned tetrahedral centers and one unassigned center. The SMILES unassigned C154 lies in a five-membered proline-like ring; the InChI encoding retains the corresponding uncertainty. The false stereo_complete flag is compatible with this atom-center scope. One assigned E double bond remains, while the InChI-derived imidic form exposes twenty additional unspecified imine geometries. These are representation-dependent descriptors, not twenty new experimentally uncertain natural bonds.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-1bd1037c43.

MIBiG row 2495 retains BGC0002130 version 3 as active. Streptomyces cacaoi CA-170360, taxon 1898, is a SOURCE_ASSERTION producer, whereas its locus is CLUSTER_DEMONSTRATED with heterologous-expression evidence. MT210103.1 is retained without declared coordinates. The demonstrated locus grade must not upgrade the separate taxon assertion. Source RIBOSOMAL classification remains distinct from the computed chemical families.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-1bd1037c43.

PMID33917820 is an ENTRY citation, not a compound-specific protocol newly inspected here. Two seeding history entries retain the extraction and augmentation provenance. The complete raw record, exact MIBiG and classifier rows and local rules were read; no historical citation access is inherited as current primary-source verification.

### Source-specific occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-1bd1037c43.

No occurrence or bioactivity root is declared. The complete saved local occurrence, ChEBI-origin, CyanometDB, PubChem, BindingDB and AntibioticMech frames contain no matched activity or organism result for this exact owner scope. This neither expands the producer assertion nor establishes an inactive compound.

### Reported model families and qualified applicability

consistency: unknown. Targets: naturalproductmech:mibig-1bd1037c43.

NPClassifier reports Amino acids and Peptides plus Polyketides, with oligopeptide, cyclic peptide and depsipeptide labels and is_glycoside true. The retained topology supports peptide macrocycles and oxygen-linked saturated rings broadly. The depsipeptide label is not established by these stored tables because no ester motif is present. These are computed labels with separately assessed applicability; multi-pathway filing as UNCLASSIFIED is not a biosynthetic conclusion.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-1bd1037c43.

The actual canonical intake and original local diagnostic are accepted. All assigned raw histories and retained source frames were read. Five local gates passed, but full QC and OAK are unavailable and all_native_gates_passed remains false. No external literature, taxonomy, protein, sequence or assay protocol was retrieved. This is a partial scientific review; database absence, standardization and reader fidelity do not establish biological inactivity, natural stereochemistry or a complete pathway.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2541-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/cacaoidin.yaml; Complete plaintext including every curation_history entry | supports | Complete cacaoidin owner and 2 history events; earlier whole reading carries by current identical bytes. |
| bgc-2541-capture | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2541-intake | /private/tmp/npm-review-work/shared-next-batch255/intakes/2541-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, maintained ownership and all 40 input placements joined to the accepted plan and current hashes. |
| bgc-2541-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch255/root-intake-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /admission; /source; /binding_handoff; /binding_peer; /source_plan_acceptance; /source_plan; /selection; /capture; /capture_acceptance; /environment; /intake_summary; /original_tools; /author_readback; /intakes; /native_gate_acceptance; /verification; /ROOT_readings; /scope; /user_outbound_hold; /external_requests; /retries; /diagnostic_result; /maintained_reader_results; /scientific_verdicts | supports | ROOT accepted this original canonical intake and its exact plan, inspection and receipt pins. |
| bgc-2541-grounding-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/grounding_notes | supports | Exact retained identifier, structure, cross-references where present, source concepts and grounding fields. Historical annotations do not constitute a fresh authority lookup. |
| bgc-2541-origin-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, coordinates where declared and citation tiers. |
| bgc-2541-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete owner supplies retained occurrences, definitions and all bioactivities where present, with their source-specific fields and notes. Missing observations are not biological inactivity. |
| bgc-2541-classification-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing and separate source categories; applicability is assessed separately. |
| bgc-2541-history-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0/owner_document/curation_status; /records/0/owner_document/curation_history | supports | Complete history and status; seeding and historical curation do not imply new primary verification. |
| bgc-2541-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/0/owner_document | supports | The complete owner has no graph, graph-reference, component, pathway, molecular-target or bioactivity root. No maintained reader applies; bounded root absence is not inactivity. |
| bgc-2541-chemistry | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge; /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key; /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles; /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count; /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge; /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key; /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles; /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count; /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts; /records/0/inchi/computed/stereo_counts | supports | Both accepted stored forms have 166 atoms and 173 bonds, the same formula, charge, full standard InChI and key. Canonical isomeric and nonisomeric strings differ through twenty amide-to-imidic shifts; the carbonyl count changes from twenty-two to two and the amide count from twenty-one to one. The direct atom correspondence is empty and full graph identity is explicitly unestablished. These normalization observations do not by themselves identify a record defect. |
| bgc-2541-topology | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs; /records/0/inchi/computed/fragment_atom_indices | supports | Complete atom and bond tables show one connected component with eight rings, including two sulfur-bridged macrocycles of sixteen and nineteen members and two saturated six-membered rings each containing five carbons and one oxygen. The aryl C31–O32–C33 connection and C39–O40–C41 inter-ring connection in the stored SMILES support a glycoside interpretation without proving natural sugar identities, linkage numbering or anomeric configuration. The two thioether bridges are C9–S10–C11 and C136–S137–C138. No ester C(=O)–O–C motif is present. |
| bgc-2541-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-current255-first-five-molecular-intake-reading-001.json; /records/0; /counts; /reading_scope; /intake_reading; /source_reading; /limits | supports | BGC complete saved first-five molecular and intake reading, with exact per-form table counts and reading attribution; no new parse. |
| bgc-2541-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /readback; /independent_peer; /intake_acceptance; /verification; /scope; /ROOT_reading; /external_requests | supports | ROOT accepted the original twenty stored-form diagnostics. The exact original stderr is empty, with no warning count inherited from an earlier batch. Method limits remain explicit. |
| bgc-2541-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins. |
| bgc-2541-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | Structure stereochemistry and named/versioned computed classification have distinct evidence scopes. |
| bgc-2541-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The maintained stereo_complete calculation uses unassigned molecular chiral centers; it is not a count of literal question marks in InChI. Atom type and double-bond geometry require separate interpretation. |
| bgc-2541-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while exact model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2541-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 126–145; 1318–1382 | supports | Deposited calls, endpoints and values retain their source scope. Activity classes derived from active assay titles do not independently prove mechanisms or direct binding. |
| bgc-2541-source-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-current255-assigned-source-reading-001.json; /primary_scope; /contexts; /raw_history_carries; /whole_reading_terminals; /remaining_attribution; /verification | supports | BGC wholly read contexts 0–5 and 11–14: the selected first five plus five unselected companions, totaling 90 frames, 37 rows and 456 fields. The selected five account for 19 rows and 219 fields; eighteen companion rows add no selected coverage or transferred activity. These are retained database-row readings, not newly inspected primary publications. |
| bgc-2541-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete retained-source reading covers 135 frames, 58 rows and 701 fields: BGC 37 rows and Support 21 rows. Native taxonomy/curation has zero positive-source-row credit; overlapping readings add no disjoint row credit. |
| bgc-2541-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch255/bgc-source-plan-execution-001.json; /observer; /operator; /delegated_by; /recorded_at; /status; /admission; /source; /installation; /command; /cwd; /login; /sandbox_permissions; /original_tools; /plan; /derivation; /notes; /readback; /original_tool_objects; /empty_original_objects; /terminal_chunk_id; /exit_code; /live_handle; /tool_wall_time_seconds; /stream_scope; /actual_invocations; /retries; /source_placements; /unique_source_paths; /external_requests; /source_edits; /scientific_verdicts | supports | One original composer produced the immutable original plan at 417 placements across 53 paths. This exact execution receipt preserves the original source, arguments, streams, plan and derivation; it is not the later supplemental-plan adoption. |
| bgc-2541-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch255/root-source-plan-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /plan; /original_plan; /original_plan_acceptance; /derivation; /full_diff; /supplement_handoff; /independent_peer; /inventory; /inventory_acceptance; /source_reading_acceptance; /notes; /original_composer_execution; /original_composer_tools; /verification; /ROOT_readings; /scope; /canonical_intakes; /diagnostic; /maintained_readers; /scientific_verdicts; /external_requests; /target_invocations | supports | ROOT accepted the operative 447-placement/56-path plan, retaining the original 417/53 plan and explicit thirty-placement/three-path diagnostic provenance supplement. No extra physical source-row or AID credit is inferred. |
| bgc-2541-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch255/root-current255-five-gates-acceptance-001.json; /status; /verification; /all_native_gates_passed; /unavailable_required_gates; /execution | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed remains false. Technical checks do not complete scientific verification. |
| bgc-2541-curation-scope | /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | The bounded ignored-inclusive Native scan found seventeen lexical rows and zero exact applicable implemented corrections or exclusions. The inventory has zero actual AIDs and three blank-AID sentinels; no assay exclusion or biological inactivity follows. |
| bgc-2541-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3 | supports | Complete saved cache names and synonyms for this owner’s source IDs; no independent taxonomic rank, strain, occurrence or producer validation. |
| bgc-2541-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/source_taxa; /contexts/1/source_scope_inventory/forward_taxon_merge_matches; /contexts/1/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh taxonomy request. |
| bgc-2541-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /routes; /interpretation | supports | Native read all eight whole retained stanzas and fifteen routes, with no unmatched, forward-merge or nonorganism entry in this exact scope. Source labels, cached names and synonyms do not establish strain equivalence, taxonomic rank or biological production. |
| bgc-2541-direct-contexts | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-target-input-plan-002.proposed.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | supports | Exact immediate owned-BGC context inputs; shared locus/citation is not identity, stereochemistry, assay or mechanism transfer. No transitive or name-based expansion. |
| bgc-2541-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2541-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2495–2495; row_sha256 6bf9ada698b2bcf190fe279c54256bcfc4ab4203022ed322ab472cd24f49a912 | supports | Exact retained compound/version, structure/key, xrefs, producer/locus grades and citation tiers. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2541-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2541-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 50–50; row_sha256 0d3774b3078dbcb85a75d14c0645c75f73c59facfa5f9edd00f274b9183b152e | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability remains separate. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2541-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2541-exclusion-table | /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; Complete retained diagnostic/implementation input; exact scope interpreted in the pinned Native curation receipt | supports | The exact retained exclusion table is captured as diagnostic provenance. No actual AID occurs in this inventory and no applicable exclusion is asserted. |
| bgc-2541-exclusion-implementation | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py; Complete retained diagnostic/implementation input; exact scope interpreted in the pinned Native curation receipt | supports | The retained exclusion implementation requires exact identity/source attribution checks and preserves provenance; its capture does not create an assay or a correction. |
| bgc-2541-unresolved-taxa | /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; Complete retained diagnostic/implementation input; exact scope interpreted in the pinned Native curation receipt | supports | The exact unresolved-taxa diagnostic table is captured. Its retained lexical matches are not exact applicable taxon corrections or fresh taxonomy evidence. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-255/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-255/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-255/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-255/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-255/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- One tetrahedral center remains unspecified; natural stereochemistry was not independently verified.
- The twenty amide/imidic shifts prevent a direct stored-form atom map in the saved diagnostic.
- Computed depsipeptide applicability remains unresolved; no automatic classifier correction is proposed.
- No fresh paper, taxonomy or complete biosynthetic pathway verification; full QC and OAK unavailable.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five stored molecular forms (892 atom rows and 944 bond rows) and 219 actual intake placements across 55 paths, without new parsing.
- Disjoint retained-source reading: BGC first-five selected plus five companions, 90 frames/37 rows/456 fields; Support last-five selected, 45 frames/21 rows/245 fields. Native cache/curation receives zero positive-source-row credit.
- BGC operated the original collector/composer; Support operated canonical intakes; Native operated the diagnostic and maintained readers under ROOT delegation. Only orders 2544 and 2545 require a reader in this fragment scope. Historical paper/sequence access is not inherited as current verification.
- The original plan remains 417 placements/53 paths. The separately adopted diagnostic-input supplement supplies the operative 447/56 scope without new source-row, AID or query credit.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T113705Z-cacaoidin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: cacaoidin'
started_at: '2026-11-05T10:22:47.022610Z'
finished_at: '2026-11-05T11:37:05.950491Z'
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
summary: Cacaoidin retains a coherent standardized encoding of a sulfur-bridged, glycosylated
  peptide, with one unassigned atom center and substantial amide/imidic representation
  differences. The producer assertion and demonstrated locus have different evidence
  grades. The computed depsipeptide label remains an applicability question because
  no ester is present in the stored form; no source edit is justified by the retained
  evidence alone.
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
  - path: data/natural_products/unclassified/cacaoidin.yaml
    sha256: 0f9d8ce893eb4cffcd24846f91d330fcd644a76f2a3983cbd059d7161703e823
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
  selection: Campaign path order 2541; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1bd1037c43
targets:
- target_id: naturalproductmech:mibig-1bd1037c43
  path: data/natural_products/unclassified/cacaoidin.yaml
  label: cacaoidin
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
    role: 'Retained exclusion-table diagnostic scope: zero actual AID tuples and three
      blank sentinels remain separate from biological assay evidence.'
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic table included in the bounded implemented-curation
      scan; no fresh taxonomy or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Implementation context for the retained exclusion identity, row-digest and
      attributed-rationale guards; no execution or new assay evidence.
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
  - naturalproductmech:mibig-1bd1037c43
  command: just validate-strict data/natural_products/unclassified/cacaoidin.yaml
    data/natural_products/unclassified/camporidine-a.yaml data/natural_products/unclassified/capsimycin.yaml
    data/natural_products/unclassified/cda1b.yaml data/natural_products/unclassified/cda2a.yaml
    data/natural_products/unclassified/cda2b.yaml data/natural_products/unclassified/cda3a.yaml
    data/natural_products/unclassified/cda3b.yaml data/natural_products/unclassified/cda4a.yaml
    data/natural_products/unclassified/cereulide.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-255/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-1bd1037c43
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-255/validate-all-001.tsv
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
  - naturalproductmech:mibig-1bd1037c43
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
  - naturalproductmech:mibig-1bd1037c43
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
  - naturalproductmech:mibig-1bd1037c43
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-255/review-queue-001.tsv
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
  - naturalproductmech:mibig-1bd1037c43
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2541-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/cacaoidin.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Complete cacaoidin owner and 2 history events; earlier whole reading carries
    by current identical bytes.
  snapshot_sha256: 0f9d8ce893eb4cffcd24846f91d330fcd644a76f2a3983cbd059d7161703e823
- evidence_id: bgc-2541-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/intakes/2541-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Actual canonical target, maintained ownership and all 40 input placements
    joined to the accepted plan and current hashes.
  snapshot_sha256: ba3b23a483c5cae6159a69273b4102d512cf511d8f097e0bb5f47d0fcc5c20f0
- evidence_id: bgc-2541-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/root-intake-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /admission; /source; /binding_handoff;
    /binding_peer; /source_plan_acceptance; /source_plan; /selection; /capture; /capture_acceptance;
    /environment; /intake_summary; /original_tools; /author_readback; /intakes; /native_gate_acceptance;
    /verification; /ROOT_readings; /scope; /user_outbound_hold; /external_requests;
    /retries; /diagnostic_result; /maintained_reader_results; /scientific_verdicts
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: ROOT accepted this original canonical intake and its exact plan, inspection
    and receipt pins.
  snapshot_sha256: 88c29293963b153618761b4d9f3fea6b57709472904f83988a48b1a243f110f3
- evidence_id: bgc-2541-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status;
    /records/0/owner_document/grounding_notes
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact retained identifier, structure, cross-references where present, source
    concepts and grounding fields. Historical annotations do not constitute a fresh
    authority lookup.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups;
    /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, coordinates
    where declared and citation tiers.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Complete owner supplies retained occurrences, definitions and all bioactivities
    where present, with their source-specific fields and notes. Missing observations
    are not biological inactivity.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing and separate
    source categories; applicability is assessed separately.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_status; /records/0/owner_document/curation_history
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Complete history and status; seeding and historical curation do not imply
    new primary verification.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: The complete owner has no graph, graph-reference, component, pathway, molecular-target
    or bioactivity root. No maintained reader applies; bounded root absence is not
    inactivity.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: bgc-2541-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge;
    /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key;
    /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles;
    /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count;
    /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts;
    /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge;
    /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key;
    /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles;
    /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count;
    /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts;
    /records/0/inchi/computed/stereo_counts
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Both accepted stored forms have 166 atoms and 173 bonds, the same formula,
    charge, full standard InChI and key. Canonical isomeric and nonisomeric strings
    differ through twenty amide-to-imidic shifts; the carbonyl count changes from
    twenty-two to two and the amide count from twenty-one to one. The direct atom
    correspondence is empty and full graph identity is explicitly unestablished. These
    normalization observations do not by themselves identify a record defect.
  snapshot_sha256: 8aca4e34df21753ab142a768460f4a6bee6ee1ff4fd9c63a175c1e0aed5d6483
- evidence_id: bgc-2541-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds;
    /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices;
    /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings;
    /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs;
    /records/0/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Complete atom and bond tables show one connected component with eight rings,
    including two sulfur-bridged macrocycles of sixteen and nineteen members and two
    saturated six-membered rings each containing five carbons and one oxygen. The
    aryl C31–O32–C33 connection and C39–O40–C41 inter-ring connection in the stored
    SMILES support a glycoside interpretation without proving natural sugar identities,
    linkage numbering or anomeric configuration. The two thioether bridges are C9–S10–C11
    and C136–S137–C138. No ester C(=O)–O–C motif is present.
  snapshot_sha256: 8aca4e34df21753ab142a768460f4a6bee6ee1ff4fd9c63a175c1e0aed5d6483
- evidence_id: bgc-2541-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-current255-first-five-molecular-intake-reading-001.json
  locator: /records/0; /counts; /reading_scope; /intake_reading; /source_reading;
    /limits
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: BGC complete saved first-five molecular and intake reading, with exact
    per-form table counts and reading attribution; no new parse.
  snapshot_sha256: 83ab9e5c19d00e28c7d1678e1ac8f2ed1bf339326498db9dca53a770972746e5
- evidence_id: bgc-2541-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /readback; /independent_peer; /intake_acceptance; /verification; /scope; /ROOT_reading;
    /external_requests
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostics. The exact original
    stderr is empty, with no warning count inherited from an earlier batch. Method
    limits remain explicit.
  snapshot_sha256: f10a2276d9c19ae550fc9c927710f9d11c8b4f32896a2b260e7b4115cd6652d5
- evidence_id: bgc-2541-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins.
  snapshot_sha256: bb2ed399af53bcac08ccf13bf71e36d5b6767e189508fe1d9ff9994f15868eba
- evidence_id: bgc-2541-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Structure stereochemistry and named/versioned computed classification have
    distinct evidence scopes.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2541-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: The maintained stereo_complete calculation uses unassigned molecular chiral
    centers; it is not a count of literal question marks in InChI. Atom type and double-bond
    geometry require separate interpretation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2541-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while exact model
    arrays remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2541-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 126–145; 1318–1382
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Deposited calls, endpoints and values retain their source scope. Activity
    classes derived from active assay titles do not independently prove mechanisms
    or direct binding.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2541-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-current255-assigned-source-reading-001.json
  locator: /primary_scope; /contexts; /raw_history_carries; /whole_reading_terminals;
    /remaining_attribution; /verification
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'BGC wholly read contexts 0–5 and 11–14: the selected first five plus five
    unselected companions, totaling 90 frames, 37 rows and 456 fields. The selected
    five account for 19 rows and 219 fields; eighteen companion rows add no selected
    coverage or transferred activity. These are retained database-row readings, not
    newly inspected primary publications.'
  snapshot_sha256: ddf9aec83c6e61320fcd44007252865a94ec0b69f1022fa0a4b4ababfb44417a
- evidence_id: bgc-2541-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Disjoint complete retained-source reading covers 135 frames, 58 rows and
    701 fields: BGC 37 rows and Support 21 rows. Native taxonomy/curation has zero
    positive-source-row credit; overlapping readings add no disjoint row credit.'
  snapshot_sha256: dd29263b6b480a6ea0d9f608aabfb045ec6ab5a8dcfb47220f21e112dadb4ce0
- evidence_id: bgc-2541-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/bgc-source-plan-execution-001.json
  locator: /observer; /operator; /delegated_by; /recorded_at; /status; /admission;
    /source; /installation; /command; /cwd; /login; /sandbox_permissions; /original_tools;
    /plan; /derivation; /notes; /readback; /original_tool_objects; /empty_original_objects;
    /terminal_chunk_id; /exit_code; /live_handle; /tool_wall_time_seconds; /stream_scope;
    /actual_invocations; /retries; /source_placements; /unique_source_paths; /external_requests;
    /source_edits; /scientific_verdicts
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: One original composer produced the immutable original plan at 417 placements
    across 53 paths. This exact execution receipt preserves the original source, arguments,
    streams, plan and derivation; it is not the later supplemental-plan adoption.
  snapshot_sha256: a038c4f320e46721a42acc6d333a568dd819902672713c1c8692150201ceef76
- evidence_id: bgc-2541-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/root-source-plan-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /plan; /original_plan; /original_plan_acceptance;
    /derivation; /full_diff; /supplement_handoff; /independent_peer; /inventory; /inventory_acceptance;
    /source_reading_acceptance; /notes; /original_composer_execution; /original_composer_tools;
    /verification; /ROOT_readings; /scope; /canonical_intakes; /diagnostic; /maintained_readers;
    /scientific_verdicts; /external_requests; /target_invocations
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: ROOT accepted the operative 447-placement/56-path plan, retaining the original
    417/53 plan and explicit thirty-placement/three-path diagnostic provenance supplement.
    No extra physical source-row or AID credit is inferred.
  snapshot_sha256: b28770e21370105fdd17012b97c866489df36ee86a94449afc88472045732b66
- evidence_id: bgc-2541-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/root-current255-five-gates-acceptance-001.json
  locator: /status; /verification; /all_native_gates_passed; /unavailable_required_gates;
    /execution
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    remains false. Technical checks do not complete scientific verification.
  snapshot_sha256: 2b0c5e5dc4bfabc24ccbb56c7916bbef7126d33440557b668d47436a949befb5
- evidence_id: bgc-2541-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: The bounded ignored-inclusive Native scan found seventeen lexical rows
    and zero exact applicable implemented corrections or exclusions. The inventory
    has zero actual AIDs and three blank-AID sentinels; no assay exclusion or biological
    inactivity follows.
  snapshot_sha256: c1dbdf1c6aa0c9dcf29d1e127250afb13ba3123717af90247f53dd0922cdef96
  search_scope: Fifteen exact retained contexts across eleven enumerated curation
    TSVs including ignored files; nine implemented tables and 3422 rows, using exact
    owner/source/BGC/full-key/assay/occurrence predicates. Reserved decisions/source_queue
    inputs are not effective overrides. This is not a global absence or assay-protocol
    claim.
- evidence_id: bgc-2541-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source IDs; no
    independent taxonomic rank, strain, occurrence or producer validation.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: bgc-2541-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/source_taxa; /contexts/1/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/1/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh
    taxonomy request.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: bgc-2541-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /routes; /interpretation
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Native read all eight whole retained stanzas and fifteen routes, with no
    unmatched, forward-merge or nonorganism entry in this exact scope. Source labels,
    cached names and synonyms do not establish strain equivalence, taxonomic rank
    or biological production.
  snapshot_sha256: e80799a40def631e8e5224442cb193c264b78522fe4fe62a0316c4995d329a55
- evidence_id: bgc-2541-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-target-input-plan-002.proposed.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact immediate owned-BGC context inputs; shared locus/citation is not
    identity, stereochemistry, assay or mechanism transfer. No transitive or name-based
    expansion.
  snapshot_sha256: 4def32a9c6c5c2e785a4aa93cd25501a68aac8f22e70ac34e9148b633fa6ac79
- evidence_id: bgc-2541-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2495–2495; row_sha256 6bf9ada698b2bcf190fe279c54256bcfc4ab4203022ed322ab472cd24f49a912
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact retained compound/version, structure/key, xrefs, producer/locus grades
    and citation tiers. BGC whole saved-source reading and current physical bytes
    are joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2541-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: bgc-2541-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 50–50; row_sha256 0d3774b3078dbcb85a75d14c0645c75f73c59facfa5f9edd00f274b9183b152e
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    remains separate. BGC whole saved-source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2541-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 row placements, exact
    predicate/query and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "AIRSSZAIEIYYPQ-QBIWCITBSA-N". Complete
    matched payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2541-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: bgc-2541-exclusion-table
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: Complete retained diagnostic/implementation input; exact scope interpreted
    in the pinned Native curation receipt
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: The exact retained exclusion table is captured as diagnostic provenance.
    No actual AID occurs in this inventory and no applicable exclusion is asserted.
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: bgc-2541-exclusion-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Complete retained diagnostic/implementation input; exact scope interpreted
    in the pinned Native curation receipt
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: The retained exclusion implementation requires exact identity/source attribution
    checks and preserves provenance; its capture does not create an assay or a correction.
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: bgc-2541-unresolved-taxa
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv
  locator: Complete retained diagnostic/implementation input; exact scope interpreted
    in the pinned Native curation receipt
  accessed_at: '2026-11-05T11:30:24.545747Z'
  support: supports
  summary: The exact unresolved-taxa diagnostic table is captured. Its retained lexical
    matches are not exact applicable taxon corrections or fresh taxonomy evidence.
  snapshot_sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:33:23.740807Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8cb8777463815d064d8d6a8debcddee05dcd1cf93d48611f7881e2ed321ce0b0
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:33:47.513574Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 200d5cffe7b8a89613f5bd36389b83452a7611ea40cb1e6b7805eb3531c9523b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:34:06.425956Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:34:39.110237Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:34:50.404426Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 98f13f2c35ba807bae8831fae9d0256cfeea0b6181f83aaceddb47e61f71cbd5
assessments:
- assessment_id: bgc-2541-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: The minted MIBiG-derived identifier and NPA031549 cross-reference remain
    retained database grounding, not fresh authority verification. Both stored forms
    produce AIRSSZAIEIYYPQ-QBIWCITBSA-N and C108H164N24O32S2 with neutral charge.
    The full key and standardized InChI agree, but natural identity and the unassigned
    stereocenter are not independently established. There is no direct companion or
    mechanism owner in the bounded map.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-grounding-owner
  - bgc-2541-chemistry
  - bgc-2541-source-mibig_compounds
  - bgc-2541-query-chebi_structures
  - bgc-2541-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: AIRSSZAIEIYYPQ-QBIWCITBSA-N; retained key, not independent natural-identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2541-grounding-owner
    - bgc-2541-chemistry
    - bgc-2541-source-mibig_compounds
    - bgc-2541-query-chebi_structures
    - bgc-2541-direct-contexts
  - name: grounding_scope
    value: The minted MIBiG-derived identifier and NPA031549 cross-reference remain
      retained database grounding, not fresh authority verification. Both stored forms
      produce AIRSSZAIEIYYPQ-QBIWCITBSA-N and C108H164N24O32S2 with neutral charge.
      The full key and standardized InChI agree, but natural identity and the unassigned
      stereocenter are not independently established. There is no direct companion
      or mechanism owner in the bounded map.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2541-grounding-owner
    - bgc-2541-chemistry
    - bgc-2541-source-mibig_compounds
    - bgc-2541-query-chebi_structures
    - bgc-2541-direct-contexts
- assessment_id: bgc-2541-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: Both forms retain thirty-two assigned tetrahedral centers and one unassigned
    center. The SMILES unassigned C154 lies in a five-membered proline-like ring;
    the InChI encoding retains the corresponding uncertainty. The false stereo_complete
    flag is compatible with this atom-center scope. One assigned E double bond remains,
    while the InChI-derived imidic form exposes twenty additional unspecified imine
    geometries. These are representation-dependent descriptors, not twenty new experimentally
    uncertain natural bonds.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-grounding-owner
  - bgc-2541-chemistry
  - bgc-2541-topology
  - bgc-2541-diagnostic-reading
  - bgc-2541-diagnostic-acceptance
  - bgc-2541-structure-schema
  - bgc-2541-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms retain thirty-two assigned tetrahedral centers and one unassigned
      center. The SMILES unassigned C154 lies in a five-membered proline-like ring;
      the InChI encoding retains the corresponding uncertainty. The false stereo_complete
      flag is compatible with this atom-center scope. One assigned E double bond remains,
      while the InChI-derived imidic form exposes twenty additional unspecified imine
      geometries. These are representation-dependent descriptors, not twenty new experimentally
      uncertain natural bonds.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2541-grounding-owner
    - bgc-2541-chemistry
    - bgc-2541-topology
    - bgc-2541-diagnostic-reading
    - bgc-2541-diagnostic-acceptance
    - bgc-2541-structure-schema
    - bgc-2541-stereo-method
  - name: representation_correspondence
    value: Both accepted stored forms have 166 atoms and 173 bonds, the same formula,
      charge, full standard InChI and key. Canonical isomeric and nonisomeric strings
      differ through twenty amide-to-imidic shifts; the carbonyl count changes from
      twenty-two to two and the amide count from twenty-one to one. The direct atom
      correspondence is empty and full graph identity is explicitly unestablished.
      These normalization observations do not by themselves identify a record defect.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2541-grounding-owner
    - bgc-2541-chemistry
    - bgc-2541-topology
    - bgc-2541-diagnostic-reading
    - bgc-2541-diagnostic-acceptance
    - bgc-2541-structure-schema
    - bgc-2541-stereo-method
- assessment_id: bgc-2541-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: MIBiG row 2495 retains BGC0002130 version 3 as active. Streptomyces cacaoi
    CA-170360, taxon 1898, is a SOURCE_ASSERTION producer, whereas its locus is CLUSTER_DEMONSTRATED
    with heterologous-expression evidence. MT210103.1 is retained without declared
    coordinates. The demonstrated locus grade must not upgrade the separate taxon
    assertion. Source RIBOSOMAL classification remains distinct from the computed
    chemical families.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-origin-owner
  - bgc-2541-occurrence-owner
  - bgc-2541-source-mibig_compounds
  - bgc-2541-cached-taxonomy
  - bgc-2541-taxonomy-routes
  - bgc-2541-curation-scope
  - bgc-2541-direct-contexts
  - bgc-2541-exclusion-table
  - bgc-2541-exclusion-implementation
  - bgc-2541-unresolved-taxa
  dimensions:
  - name: taxon_scope
    value: MIBiG row 2495 retains BGC0002130 version 3 as active. Streptomyces cacaoi
      CA-170360, taxon 1898, is a SOURCE_ASSERTION producer, whereas its locus is
      CLUSTER_DEMONSTRATED with heterologous-expression evidence. MT210103.1 is retained
      without declared coordinates. The demonstrated locus grade must not upgrade
      the separate taxon assertion. Source RIBOSOMAL classification remains distinct
      from the computed chemical families.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2541-origin-owner
    - bgc-2541-occurrence-owner
    - bgc-2541-source-mibig_compounds
    - bgc-2541-cached-taxonomy
    - bgc-2541-taxonomy-routes
    - bgc-2541-curation-scope
    - bgc-2541-direct-contexts
    - bgc-2541-exclusion-table
    - bgc-2541-exclusion-implementation
    - bgc-2541-unresolved-taxa
  - name: producer_evidence
    value: MIBiG row 2495 retains BGC0002130 version 3 as active. Streptomyces cacaoi
      CA-170360, taxon 1898, is a SOURCE_ASSERTION producer, whereas its locus is
      CLUSTER_DEMONSTRATED with heterologous-expression evidence. MT210103.1 is retained
      without declared coordinates. The demonstrated locus grade must not upgrade
      the separate taxon assertion. Source RIBOSOMAL classification remains distinct
      from the computed chemical families.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2541-origin-owner
    - bgc-2541-occurrence-owner
    - bgc-2541-source-mibig_compounds
    - bgc-2541-cached-taxonomy
    - bgc-2541-taxonomy-routes
    - bgc-2541-curation-scope
    - bgc-2541-direct-contexts
    - bgc-2541-exclusion-table
    - bgc-2541-exclusion-implementation
    - bgc-2541-unresolved-taxa
  - name: locus_evidence
    value: MIBiG row 2495 retains BGC0002130 version 3 as active. Streptomyces cacaoi
      CA-170360, taxon 1898, is a SOURCE_ASSERTION producer, whereas its locus is
      CLUSTER_DEMONSTRATED with heterologous-expression evidence. MT210103.1 is retained
      without declared coordinates. The demonstrated locus grade must not upgrade
      the separate taxon assertion. Source RIBOSOMAL classification remains distinct
      from the computed chemical families.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2541-origin-owner
    - bgc-2541-occurrence-owner
    - bgc-2541-source-mibig_compounds
    - bgc-2541-cached-taxonomy
    - bgc-2541-taxonomy-routes
    - bgc-2541-curation-scope
    - bgc-2541-direct-contexts
    - bgc-2541-exclusion-table
    - bgc-2541-exclusion-implementation
    - bgc-2541-unresolved-taxa
- assessment_id: bgc-2541-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: PMID33917820 is an ENTRY citation, not a compound-specific protocol newly
    inspected here. Two seeding history entries retain the extraction and augmentation
    provenance. The complete raw record, exact MIBiG and classifier rows and local
    rules were read; no historical citation access is inherited as current primary-source
    verification.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-owner
  - bgc-2541-history-owner
  - bgc-2541-origin-owner
  - bgc-2541-occurrence-owner
  - bgc-2541-source-mibig_compounds
  - bgc-2541-source-reading
  dimensions:
  - name: citation_scope
    value: PMID33917820 is an ENTRY citation, not a compound-specific protocol newly
      inspected here. Two seeding history entries retain the extraction and augmentation
      provenance. The complete raw record, exact MIBiG and classifier rows and local
      rules were read; no historical citation access is inherited as current primary-source
      verification.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2541-owner
    - bgc-2541-history-owner
    - bgc-2541-origin-owner
    - bgc-2541-occurrence-owner
    - bgc-2541-source-mibig_compounds
    - bgc-2541-source-reading
- assessment_id: bgc-2541-occurrence
  area: evidence
  topic: Source-specific occurrence and assay boundaries
  outcome: supported
  summary: No occurrence or bioactivity root is declared. The complete saved local
    occurrence, ChEBI-origin, CyanometDB, PubChem, BindingDB and AntibioticMech frames
    contain no matched activity or organism result for this exact owner scope. This
    neither expands the producer assertion nor establishes an inactive compound.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-occurrence-owner
  - bgc-2541-mechanism-absence
  - bgc-2541-query-lotus_occurrences
  - bgc-2541-query-chebi_origins
  - bgc-2541-query-cyanometdb_occurrences
  - bgc-2541-query-pubchem_bioassay
  - bgc-2541-query-bindingdb_targets
  - bgc-2541-query-antibioticmech_inchikeys
  - bgc-2541-cached-taxonomy
  - bgc-2541-taxonomy-routes
  - bgc-2541-taxonomy-reading
  - bgc-2541-curation-scope
  - bgc-2541-bioactivity-seeder
  - bgc-2541-source-reading
  - bgc-2541-exclusion-table
  - bgc-2541-exclusion-implementation
  - bgc-2541-unresolved-taxa
  dimensions:
  - name: occurrence_scope
    value: No occurrence or bioactivity root is declared. The complete saved local
      occurrence, ChEBI-origin, CyanometDB, PubChem, BindingDB and AntibioticMech
      frames contain no matched activity or organism result for this exact owner scope.
      This neither expands the producer assertion nor establishes an inactive compound.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2541-occurrence-owner
    - bgc-2541-mechanism-absence
    - bgc-2541-query-lotus_occurrences
    - bgc-2541-query-chebi_origins
    - bgc-2541-query-cyanometdb_occurrences
    - bgc-2541-query-pubchem_bioassay
    - bgc-2541-query-bindingdb_targets
    - bgc-2541-query-antibioticmech_inchikeys
    - bgc-2541-cached-taxonomy
    - bgc-2541-taxonomy-routes
    - bgc-2541-taxonomy-reading
    - bgc-2541-curation-scope
    - bgc-2541-bioactivity-seeder
    - bgc-2541-source-reading
    - bgc-2541-exclusion-table
    - bgc-2541-exclusion-implementation
    - bgc-2541-unresolved-taxa
  - name: assay_target_scope
    value: The exact saved full-key source joins contain no actual AID, BindingDB
      target or grounded molecular-target result for this owner. Empty local frames
      are bounded search results, not negative experiments. The added exclusion table,
      exclusion implementation and unresolved-taxa table are captured diagnostic inputs;
      their presence adds no assay or source-row credit.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2541-occurrence-owner
    - bgc-2541-mechanism-absence
    - bgc-2541-query-lotus_occurrences
    - bgc-2541-query-chebi_origins
    - bgc-2541-query-cyanometdb_occurrences
    - bgc-2541-query-pubchem_bioassay
    - bgc-2541-query-bindingdb_targets
    - bgc-2541-query-antibioticmech_inchikeys
    - bgc-2541-cached-taxonomy
    - bgc-2541-taxonomy-routes
    - bgc-2541-taxonomy-reading
    - bgc-2541-curation-scope
    - bgc-2541-bioactivity-seeder
    - bgc-2541-source-reading
    - bgc-2541-exclusion-table
    - bgc-2541-exclusion-implementation
    - bgc-2541-unresolved-taxa
- assessment_id: bgc-2541-classification
  area: consistency
  topic: Reported model families and qualified applicability
  outcome: unknown
  summary: NPClassifier reports Amino acids and Peptides plus Polyketides, with oligopeptide,
    cyclic peptide and depsipeptide labels and is_glycoside true. The retained topology
    supports peptide macrocycles and oxygen-linked saturated rings broadly. The depsipeptide
    label is not established by these stored tables because no ester motif is present.
    These are computed labels with separately assessed applicability; multi-pathway
    filing as UNCLASSIFIED is not a biosynthetic conclusion.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-classification-owner
  - bgc-2541-source-npclassifier
  - bgc-2541-chemistry
  - bgc-2541-topology
  - bgc-2541-structure-schema
  - bgc-2541-classification-seeder
  - bgc-2541-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: NPClassifier reports Amino acids and Peptides plus Polyketides, with oligopeptide,
      cyclic peptide and depsipeptide labels and is_glycoside true. The retained topology
      supports peptide macrocycles and oxygen-linked saturated rings broadly. The
      depsipeptide label is not established by these stored tables because no ester
      motif is present. These are computed labels with separately assessed applicability;
      multi-pathway filing as UNCLASSIFIED is not a biosynthetic conclusion.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2541-classification-owner
    - bgc-2541-source-npclassifier
    - bgc-2541-chemistry
    - bgc-2541-topology
    - bgc-2541-structure-schema
    - bgc-2541-classification-seeder
    - bgc-2541-source-mibig_compounds
- assessment_id: bgc-2541-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: The actual canonical intake and original local diagnostic are accepted.
    All assigned raw histories and retained source frames were read. Five local gates
    passed, but full QC and OAK are unavailable and all_native_gates_passed remains
    false. No external literature, taxonomy, protein, sequence or assay protocol was
    retrieved. This is a partial scientific review; database absence, standardization
    and reader fidelity do not establish biological inactivity, natural stereochemistry
    or a complete pathway.
  target_ids:
  - naturalproductmech:mibig-1bd1037c43
  evidence_ids:
  - bgc-2541-owner
  - bgc-2541-capture
  - bgc-2541-intake
  - bgc-2541-intake-acceptance
  - bgc-2541-history-owner
  - bgc-2541-diagnostic-reading
  - bgc-2541-diagnostic-acceptance
  - bgc-2541-diagnostic-execution
  - bgc-2541-source-reading
  - bgc-2541-joint-source-notes
  - bgc-2541-source-plan-execution
  - bgc-2541-source-plan-acceptance
  - bgc-2541-native-gate-limits
  - bgc-2541-curation-scope
  - bgc-2541-mechanism-absence
  - bgc-2541-exclusion-table
  - bgc-2541-exclusion-implementation
  - bgc-2541-unresolved-taxa
  dimensions:
  - name: review_completion
    value: The actual canonical intake and original local diagnostic are accepted.
      All assigned raw histories and retained source frames were read. Five local
      gates passed, but full QC and OAK are unavailable and all_native_gates_passed
      remains false. No external literature, taxonomy, protein, sequence or assay
      protocol was retrieved. This is a partial scientific review; database absence,
      standardization and reader fidelity do not establish biological inactivity,
      natural stereochemistry or a complete pathway.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2541-owner
    - bgc-2541-capture
    - bgc-2541-intake
    - bgc-2541-intake-acceptance
    - bgc-2541-history-owner
    - bgc-2541-diagnostic-reading
    - bgc-2541-diagnostic-acceptance
    - bgc-2541-diagnostic-execution
    - bgc-2541-source-reading
    - bgc-2541-joint-source-notes
    - bgc-2541-source-plan-execution
    - bgc-2541-source-plan-acceptance
    - bgc-2541-native-gate-limits
    - bgc-2541-curation-scope
    - bgc-2541-mechanism-absence
    - bgc-2541-exclusion-table
    - bgc-2541-exclusion-implementation
    - bgc-2541-unresolved-taxa
findings: []
actions: []
limitations:
- One tetrahedral center remains unspecified; natural stereochemistry was not independently
  verified.
- The twenty amide/imidic shifts prevent a direct stored-form atom map in the saved
  diagnostic.
- Computed depsipeptide applicability remains unresolved; no automatic classifier
  correction is proposed.
- No fresh paper, taxonomy or complete biosynthetic pathway verification; full QC
  and OAK unavailable.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all ten first-five stored molecular forms (892 atom rows and
  944 bond rows) and 219 actual intake placements across 55 paths, without new parsing.
- 'Disjoint retained-source reading: BGC first-five selected plus five companions,
  90 frames/37 rows/456 fields; Support last-five selected, 45 frames/21 rows/245
  fields. Native cache/curation receives zero positive-source-row credit.'
- BGC operated the original collector/composer; Support operated canonical intakes;
  Native operated the diagnostic and maintained readers under ROOT delegation. Only
  orders 2544 and 2545 require a reader in this fragment scope. Historical paper/sequence
  access is not inherited as current verification.
- The original plan remains 417 placements/53 paths. The separately adopted diagnostic-input
  supplement supplies the operative 447/56 scope without new source-row, AID or query
  credit.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-255
```
