# Local evidence review: 14-hydroxypaspalinine

- Review: 20261104T203214Z-14-hydroxypaspalinine
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T20:02:03.829781Z
- Finished UTC: 2026-11-04T20:32:14.306738Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

14-hydroxypaspalinine retains its exact C27H31NO5 identity, seven specified tetrahedral centers and characterized BGC2149 producer/locus assertions. Its PubChem row is a blank-AID sentinel, not an assay. Broad indole-terpenoid context is supported locally while the named Penitrem model family and natural identity remain qualified; review is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2443; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-eb3a34d0e2 | data/natural_products/unclassified/14-hydroxypaspalinine.yaml | generated | 14-hydroxypaspalinine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-eb3a34d0e2 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-eb3a34d0e2 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-eb3a34d0e2 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-eb3a34d0e2 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-eb3a34d0e2 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-eb3a34d0e2 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-eb3a34d0e2 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-eb3a34d0e2 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained identity and bounded correspondence

identity: supported. Targets: naturalproductmech:mibig-eb3a34d0e2.

The exact full key JNHPMJVSUJKCKH-KCCNSQSLSA-N and minted identifier naturalproductmech:mibig-eb3a34d0e2 belong to BGC0002149 version 2 compound 3. Both saved encodings normalize to that key, C27H31NO5 and zero formal charge, with ten true comparisons and a complete supplied 33-atom match at its stated scope. PubChem:10072409 is a retained cross-reference. The neighboring leucyloxy and dimethylleucyloxy records have distinct keys and formulas; names and a common locus do not make them equivalent identities or demonstrate a reaction sequence.

### Stored-form stereochemistry and topology limits

representation: supported. Targets: naturalproductmech:mibig-eb3a34d0e2.

Both saved forms report seven specified tetrahedral centers and no unresolved potential stereo, consistent with the stored true flag at the maintained extractor’s chiral-center scope. The fused aromatic N-containing system, carbonyl and oxygen bridges remain explicit in the complete tables. All ten comparisons agree, but full_graph_identity_established remains false and no natural stereochemical authentication is inferred. No biochemical atom numbering or named substituent position is assigned solely from zero-based diagnostic indices.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-eb3a34d0e2.

The retained MIBiG record identifies Aspergillus alliaceus ATCC 20738, NCBITaxon:209559, at BGC_CHARACTERIZED. Its separately graded CLUSTER_DEMONSTRATED locus is OK546695.1:1–40000, with Knock-out studies, Heterologous expression and Correlated expression listed. These source assertions are preserved without upgrading them to a fresh independent strain/construct verification. There is no retained occurrence assertion to substitute for producer evidence, and common BGC2149 membership does not transfer results between the three selected compounds.

### Citation tiers and seed-history scope

evidence: supported. Targets: naturalproductmech:mibig-eb3a34d0e2.

PMID:35315670 is explicitly ENTRY evidence for the MIBiG source placement, not a retained compound-specific activity report. It repeats across the three BGC2149 owners and is not counted as three independent studies. The two SEEDED_FROM_SOURCES events establish inventory provenance rather than primary experimental review. No primary text was freshly accessed and no status promotion follows from the cited database grades.

### Finite occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-eb3a34d0e2.

LOTUS, ChEBI-origin and CyanoMetDB frames are empty for this exact identity and there are no owner occurrence roots. The one PubChem row for CID10072409 has a blank AID and is explicitly a no-assay sentinel, not an inactive call or measured potency. BindingDB and related-corpus joins are empty. No biological inactivity, target, congener activity or molecular mechanism is inferred.

### Model fidelity with specific family applicability unverified

consistency: unknown. Targets: naturalproductmech:mibig-eb3a34d0e2.

NPClassifier version 2026-09-07 retains Alkaloids and Terpenoids, Tryptophan alkaloids and Indole-Diterpenoid alkaloids (Penitrems), glycoside false. The NRPS/TERPENE BGC classes are separate source metadata; the source compound-class list is empty. The aromatic N-containing fused framework supports broad indole-terpenoid compatibility, while the specific parenthetical Penitrem family is not independently established by the retained source or local motifs. Multiple model labels explain UNCLASSIFIED filing. This applicability uncertainty is not an established source-ingestion defect.

### Actual evidence coverage and remaining limits

completeness: unknown. Targets: naturalproductmech:mibig-eb3a34d0e2.

The complete owner and two histories, accepted 39-input canonical intake, all nine selected source frames including the blank-AID row, full paired tables and two distinct selected BGC peers are covered. No mechanism/component/target root is declared and no maintained-reader result is needed. Primary literature, natural identity, named Penitrem applicability, full QC and complete OAK remain unavailable; review remains partial with no source-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2443-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/14-hydroxypaspalinine.yaml; Complete plaintext including every curation_history entry | supports | Complete 14-hydroxypaspalinine owner and both seed-history events; MINTED/SEEDED unchanged. Prior complete raw/history reading carries with current identical bytes. |
| bgc-2443-capture | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2 | supports | Complete actual owner capture, metadata, root presence and empty component captures; preservation is not independent scientific validation. |
| bgc-2443-intake | /private/tmp/npm-review-work/shared-next-batch245/intakes/2443-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, ownership declarations and all 39 current input placements joined to the exact plan. |
| bgc-2443-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch245/root-intake-acceptance-001.json; /status; /summary; /source_plan; /intakes/2 | supports | ROOT accepted the original canonical intake and exact source plan; this record’s intake, execution and target-spec pins are preserved. |
| bgc-2443-grounding-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/xrefs; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes | supports | Exact retained identifier, structure, source concepts and grounding fields; cross-references only where present. Historical grounding notes are not fresh external searches. |
| bgc-2443-origin-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts | supports | Exact producer and locus grades, experimental methods, accession/coordinates and source citation tiers; organism/strain and locus evidence remain separate. |
| bgc-2443-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete owner lacks occurrence, activity, target and mechanism roots; absence is owner-local and not inactivity evidence. |
| bgc-2443-classification-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2/owner_document/np_classification; /records/2/owner_document/np_pathway; /records/2/owner_document/bgc_class | supports | Named/versioned classifier arrays and glycoside flag, UNCLASSIFIED filing and separately retained source classes; fidelity does not establish specific family applicability. |
| bgc-2443-history-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2/owner_document/curation_status; /records/2/owner_document/curation_history | supports | Both complete seed-history entries and unchanged SEEDED status; seeding is not primary experimental verification. |
| bgc-2443-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/2/owner_document | supports | Whole selected owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets. No maintained-reader result applies to this record. |
| bgc-2443-chemistry | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence; /records/2/smiles/computed/formula; /records/2/smiles/computed/formal_charge; /records/2/smiles/computed/standard_inchi; /records/2/smiles/computed/standard_inchi_key; /records/2/smiles/computed/canonical_isomeric_smiles; /records/2/smiles/computed/canonical_nonisomeric_smiles; /records/2/smiles/computed/atom_count; /records/2/smiles/computed/heavy_atom_count; /records/2/smiles/computed/bond_count; /records/2/smiles/computed/element_counts; /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/formula; /records/2/inchi/computed/formal_charge; /records/2/inchi/computed/standard_inchi; /records/2/inchi/computed/standard_inchi_key; /records/2/inchi/computed/canonical_isomeric_smiles; /records/2/inchi/computed/canonical_nonisomeric_smiles; /records/2/inchi/computed/atom_count; /records/2/inchi/computed/heavy_atom_count; /records/2/inchi/computed/bond_count; /records/2/inchi/computed/element_counts; /records/2/inchi/computed/stereo_counts | supports | All ten comparisons are true and the supplied chirality-aware atom match is complete at its stated scope. Full graph and natural identity remain unestablished. The explicit full_graph_identity_established flag remains false. |
| bgc-2443-topology | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/motifs; /records/2/smiles/computed/fragment_atom_indices; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings; /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs; /records/2/inchi/computed/fragment_atom_indices | supports | Both forms contain 33 heavy atoms, 39 bonds and seven reported rings. They show the fused aromatic N-containing system, one carbonyl, two C-O-C bridge oxygens and no saturated six-membered C5O cycle or amide. Seven tetrahedral centers are specified; the supplied 33-atom map is complete only within its stated chirality-aware matching scope. |
| bgc-2443-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-first-five-diagnostic-reading-001.json; /records/2; /read_scope; /totals; /representation; /reading_caveats | supports | BGC personally read every field of all ten first-five forms, 370 atom rows and 420 bond rows, and all 201 intake placements/51 paths. Exact lossless reconstruction and original reading objects are retained; no reparse. |
| bgc-2443-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/2; /molecular_parse_attempts; /parsed; /global_warning_count; /method_scope; /interpretation_boundary | supports | ROOT accepted the original twenty stored-form diagnostic; this owner’s actual comparison/correspondence scope is located. Global warning count is zero; no alternative normalization repair is inferred. |
| bgc-2443-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and stream pins; stderr is empty as its zero-byte pin records. |
| bgc-2443-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–430 | supports | Undefined stereo is retained rather than fabricated; computed classifications are named/versioned model results, never source assertions. |
| bgc-2443-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | stereo_complete is computed with FindMolChiralCenters including unassigned centers; it does not independently verify natural identity or all double-bond geometry. |
| bgc-2443-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Multiple classifier pathways yield UNCLASSIFIED filing while arrays are retained. Filing and model fidelity do not establish biological applicability. |
| bgc-2443-source-reading | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-assigned-source-reading-001.json; /scope; /reading; /records; /cautions; /physical_verification | supports | BGC personally read ten assigned contexts, 90 frames, 28 positive rows and 373 fields; selected five account for 45 frames/13 rows/183 fields. Prior companion whole-body readings remain explicitly attributed. |
| bgc-2443-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete source reading totals 225 frames/120 rows/1294 fields: BGC 28 rows, ROOT 60, Support 32; Native taxonomy/curation credit is separate. Preferred corrected ROOT CPA002 is retained without transferring its precursor claims. |
| bgc-2443-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch245/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /original_terminal; /exit_code; /plan; /derivation; /inventory; /notes; /verification | supports | The one original local composer produced the exact 400-placement/66-path plan with 31 verified derivation operations. Actual intake acceptance separately binds this plan; historical conditional fields remain unchanged. |
| bgc-2443-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch245/root-native-five-gates-acceptance-001.json; /status; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five local commands passed; full QC and complete OAK remain unavailable. Passing local syntax/reproduction checks does not complete scientific verification. |
| bgc-2443-curation-scope | /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | Native’s bounded ignored-inclusive scan found one applicable BGC0977 override for selected order2447, outside these first five; none applies to this owner. No assay exclusion is borrowed by shared names or locus alone. |
| bgc-2443-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/20 | supports | Complete retained cache stanzas for this owner’s source taxon IDs. Names/synonyms are cached context, not a fresh taxonomic or strain determination. |
| bgc-2443-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/source_taxa; /contexts/8/source_scope_inventory/forward_taxon_merge_matches; /contexts/8/source_scope_inventory/nonorganism_matches | supports | All saved taxon IDs and forwarding/nonorganism routes for this selected source context, including empty routes; no fresh taxonomy request. |
| bgc-2443-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /forward_routes; /interpretation | supports | Native personally read all 32 complete cached stanzas and four saved forwarding routes across the full batch context. This attribution does not duplicate positive-row credit or transfer species/strain roles. |
| bgc-2443-direct-contexts | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-target-input-plan-001.json; /records/2/proposed_companion_paths; /records/2/direct_companion_predicates | supports | Literal one-hop shared-BGC predicates and exact direct companion paths only; no transitive expansion or transfer of identity, stereochemistry, activity or mechanism. |
| bgc-2443-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key; /contexts/9/owned_bgc_ids; /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids | supports | Distinct full keys, identities, labels and owned loci define the selected owner’s direct context; shared BGC membership is not identity equivalence. |
| bgc-2443-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame contains 1 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2519–2519; row_sha256 05077574bcac56dd576b2376e02b472fe81acda7075fdfab80ec4a7d81dc42b5 | supports | Exact full-key/version/compound-index, producer/locus grades and citation-tier fields. BGC complete selected source-row reading and current physical bytes are joined. |
| bgc-2443-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame contains 1 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1139–1139; row_sha256 f3302cffe2a2262bcdaa4dc8380b67b1ad96e3118ba4c32699fde972a4e9c27f | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability is not guaranteed by retention. BGC complete selected source-row reading and current physical bytes are joined. |
| bgc-2443-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame contains 1 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 3359–3359; row_sha256 d261d00704c3f8921245dc4ce5b69e68a19f193128a2755a3e022b7634e9b077 | supports | Exact CID10072409 blank-AID/no-assay sentinel, with no activity measurement or inactive result. BGC complete selected source-row reading and current physical bytes are joined. |
| bgc-2443-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2443-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/8/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-245/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-245/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-245/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-245/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-245/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only. Fresh primary literature, current taxonomy, assay protocols and independent natural identity/stereochemical authentication remain unavailable.
- Five local native commands passed, but full QC and complete OAK remain unavailable. Saved normalized forms and atom matches do not establish independent full graph or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain separate. Shared BGC membership and repeated references do not transfer biological claims or establish independent experiments.
- Named model-family applicability is explicitly unverified; retention fidelity and broad structural compatibility do not establish a specific biosynthetic family or a source-ingestion defect.
- The complete selected owner has no graph, pathway, component reference or molecular-target root. No maintained-reader result, source edit or status/history promotion is claimed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read ten first-five saved forms: 370 atom rows and 420 bond rows, complete strings/scalars/rings/stereo/motifs/maps; indices are diagnostic-local. The original diagnostic stderr was empty. No reparse occurred during review.
- Disjoint source reading: BGC 10 contexts/90 frames/28 rows/373 fields; ROOT 7 contexts/63 frames/60 rows/558 fields; Support 8 contexts/72 frames/32 rows/363 fields. Native read 32 cached stanzas and bounded curation, with zero positive-row credit. Prior raw/history readings and preferred ROOT CPA002 remain attributed.
- BGC operated the original local collector and composer; Support operated canonical intakes; Native operated the original molecular diagnostic under ROOT delegation. Final report authoring only reads saved evidence and writes review artifacts.
- All first-five reviews remain partial. No supported source-edit finding or action is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T203214Z-14-hydroxypaspalinine
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 14-hydroxypaspalinine'
started_at: '2026-11-04T20:02:03.829781Z'
finished_at: '2026-11-04T20:32:14.306738Z'
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
summary: 14-hydroxypaspalinine retains its exact C27H31NO5 identity, seven specified
  tetrahedral centers and characterized BGC2149 producer/locus assertions. Its PubChem
  row is a blank-AID sentinel, not an assay. Broad indole-terpenoid context is supported
  locally while the named Penitrem model family and natural identity remain qualified;
  review is partial.
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
  - path: data/natural_products/unclassified/14-hydroxypaspalinine.yaml
    sha256: 4d37e50fb7d26c4ebc805d7da259a483beba36f68a65d383edfc040690104539
    role: target
  - path: data/natural_products/unclassified/14-leucyloxy-paspalinine.yaml
    sha256: f7d27d82a387c5382c3c90f14fc1a92f84dbc2a79c82487ea63b7e9401f7d1f9
    role: context
  - path: data/natural_products/unclassified/14-n-n-dimethylleucyloxy-paspalinine.yaml
    sha256: 9ae8f2b3ac0b8b01223221be6e30e65a5e081b45e70a164869917a246869a5ef
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
  selection: Campaign path order 2443; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
targets:
- target_id: naturalproductmech:mibig-eb3a34d0e2
  path: data/natural_products/unclassified/14-hydroxypaspalinine.yaml
  label: 14-hydroxypaspalinine
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
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
  - naturalproductmech:mibig-eb3a34d0e2
  command: just validate-strict data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml
    data/natural_products/unclassified/13-epi-higginsianin-c.yaml data/natural_products/unclassified/14-hydroxypaspalinine.yaml
    data/natural_products/unclassified/14-leucyloxy-paspalinine.yaml data/natural_products/unclassified/14-n-n-dimethylleucyloxy-paspalinine.yaml
    data/natural_products/unclassified/2-methoxy-5-methyl-6-13-methyltetradecyl-1-4-benzoquinone.yaml
    data/natural_products/unclassified/2-oxocyclopiazonic-acid.yaml data/natural_products/unclassified/21-22-diprenylated-paxilline.yaml
    data/natural_products/unclassified/2r-3s-4s-5-fluoro-2-3-4-trihydroxypentanoic-acid.yaml
    data/natural_products/unclassified/4-deoxygadusol.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-245/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-eb3a34d0e2
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-245/validate-all-001.tsv
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
  - naturalproductmech:mibig-eb3a34d0e2
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
  - naturalproductmech:mibig-eb3a34d0e2
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
  - naturalproductmech:mibig-eb3a34d0e2
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-245/review-queue-001.tsv
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
  - naturalproductmech:mibig-eb3a34d0e2
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2443-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/14-hydroxypaspalinine.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete 14-hydroxypaspalinine owner and both seed-history events; MINTED/SEEDED
    unchanged. Prior complete raw/history reading carries with current identical bytes.
  snapshot_sha256: 4d37e50fb7d26c4ebc805d7da259a483beba36f68a65d383edfc040690104539
- evidence_id: bgc-2443-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete actual owner capture, metadata, root presence and empty component
    captures; preservation is not independent scientific validation.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/intakes/2443-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Actual canonical target, ownership declarations and all 39 current input
    placements joined to the exact plan.
  snapshot_sha256: 0e4d464d1cf1e1815b3bdc9175a903765d709eb742f99e3bf7d9dc327b5ffe82
- evidence_id: bgc-2443-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /intakes/2
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: ROOT accepted the original canonical intake and exact source plan; this
    record’s intake, execution and target-spec pins are preserved.
  snapshot_sha256: b5e9b8a29b2595e6870fb8f9ccc97a7ac56051767c54f32ccb565669667ad062
- evidence_id: bgc-2443-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/xrefs;
    /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status;
    /records/2/owner_document/grounding_notes
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact retained identifier, structure, source concepts and grounding fields;
    cross-references only where present. Historical grounding notes are not fresh
    external searches.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/producer_taxon_groups;
    /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact producer and locus grades, experimental methods, accession/coordinates
    and source citation tiers; organism/strain and locus evidence remain separate.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete owner lacks occurrence, activity, target and mechanism roots;
    absence is owner-local and not inactivity evidence.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_classification; /records/2/owner_document/np_pathway;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Named/versioned classifier arrays and glycoside flag, UNCLASSIFIED filing
    and separately retained source classes; fidelity does not establish specific family
    applicability.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2/owner_document/curation_status; /records/2/owner_document/curation_history
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Both complete seed-history entries and unchanged SEEDED status; seeding
    is not primary experimental verification.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Whole selected owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets. No maintained-reader result applies to this record.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2443-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: All ten comparisons are true and the supplied chirality-aware atom match
    is complete at its stated scope. Full graph and natural identity remain unestablished.
    The explicit full_graph_identity_established flag remains false.
  snapshot_sha256: 6850baa8fbfc54cf5ad8aa70b91f3565712bfc851de94725684972e0480db98c
- evidence_id: bgc-2443-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons;
    /records/2/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds;
    /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo;
    /records/2/smiles/computed/motifs; /records/2/smiles/computed/fragment_atom_indices;
    /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings;
    /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs;
    /records/2/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Both forms contain 33 heavy atoms, 39 bonds and seven reported rings. They
    show the fused aromatic N-containing system, one carbonyl, two C-O-C bridge oxygens
    and no saturated six-membered C5O cycle or amide. Seven tetrahedral centers are
    specified; the supplied 33-atom map is complete only within its stated chirality-aware
    matching scope.
  snapshot_sha256: 6850baa8fbfc54cf5ad8aa70b91f3565712bfc851de94725684972e0480db98c
- evidence_id: bgc-2443-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-first-five-diagnostic-reading-001.json
  locator: /records/2; /read_scope; /totals; /representation; /reading_caveats
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: BGC personally read every field of all ten first-five forms, 370 atom rows
    and 420 bond rows, and all 201 intake placements/51 paths. Exact lossless reconstruction
    and original reading objects are retained; no reparse.
  snapshot_sha256: 421e98636ba662d3b80856bd203a17f6d4821b1d26478e98cfb2f4c5983c3263
- evidence_id: bgc-2443-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/2; /molecular_parse_attempts; /parsed;
    /global_warning_count; /method_scope; /interpretation_boundary
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostic; this owner’s
    actual comparison/correspondence scope is located. Global warning count is zero;
    no alternative normalization repair is inferred.
  snapshot_sha256: 53cfc82e0782adcaf6fa89a1f348882ed503e70b4f238ecea56ce4b6e454792e
- evidence_id: bgc-2443-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and stream pins; stderr
    is empty as its zero-byte pin records.
  snapshot_sha256: a8e429b538e8b4bb210b03462f44fed28d75a036c4254b0b9a23fa933362e886
- evidence_id: bgc-2443-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–430
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Undefined stereo is retained rather than fabricated; computed classifications
    are named/versioned model results, never source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2443-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: stereo_complete is computed with FindMolChiralCenters including unassigned
    centers; it does not independently verify natural identity or all double-bond
    geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2443-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Multiple classifier pathways yield UNCLASSIFIED filing while arrays are
    retained. Filing and model fidelity do not establish biological applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2443-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-assigned-source-reading-001.json
  locator: /scope; /reading; /records; /cautions; /physical_verification
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: BGC personally read ten assigned contexts, 90 frames, 28 positive rows
    and 373 fields; selected five account for 45 frames/13 rows/183 fields. Prior
    companion whole-body readings remain explicitly attributed.
  snapshot_sha256: bbd532f2feb60267a5f06722b7f019a9dc82f0140df14c12347a59fa8032c159
- evidence_id: bgc-2443-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: 'Disjoint complete source reading totals 225 frames/120 rows/1294 fields:
    BGC 28 rows, ROOT 60, Support 32; Native taxonomy/curation credit is separate.
    Preferred corrected ROOT CPA002 is retained without transferring its precursor
    claims.'
  snapshot_sha256: f1ff457f0b365650b471d3899f218f22149798ceb6c718ce3b4ca4381f3999b4
- evidence_id: bgc-2443-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /original_terminal; /exit_code; /plan;
    /derivation; /inventory; /notes; /verification
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: The one original local composer produced the exact 400-placement/66-path
    plan with 31 verified derivation operations. Actual intake acceptance separately
    binds this plan; historical conditional fields remain unchanged.
  snapshot_sha256: cb6bb69a0d55063a04f1c655cf745f18397fc6504458f8c4e463145c33f93c80
- evidence_id: bgc-2443-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/root-native-five-gates-acceptance-001.json
  locator: /status; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Five local commands passed; full QC and complete OAK remain unavailable.
    Passing local syntax/reproduction checks does not complete scientific verification.
  snapshot_sha256: 96136a2f222716e1d3f662e48e6dc859f6672faad8d32454d56b161c97b1dcff
- evidence_id: bgc-2443-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Native’s bounded ignored-inclusive scan found one applicable BGC0977 override
    for selected order2447, outside these first five; none applies to this owner.
    No assay exclusion is borrowed by shared names or locus alone.
  snapshot_sha256: 5dc21625a5090a65de13d121ec91c99ee12146f14405c52e5e642caefc880eca
  search_scope: Current 25-context scope, 242 literal tokens and all 11 enumerated
    TSVs including ignored files; nine eligible tables/3422 rows examined, with exact
    applied/unrelated identities retained. This does not claim a global external absence
    or validate assay protocols.
- evidence_id: bgc-2443-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/20
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete retained cache stanzas for this owner’s source taxon IDs. Names/synonyms
    are cached context, not a fresh taxonomic or strain determination.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
- evidence_id: bgc-2443-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/source_taxa; /contexts/8/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/8/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: All saved taxon IDs and forwarding/nonorganism routes for this selected
    source context, including empty routes; no fresh taxonomy request.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
- evidence_id: bgc-2443-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /forward_routes; /interpretation
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Native personally read all 32 complete cached stanzas and four saved forwarding
    routes across the full batch context. This attribution does not duplicate positive-row
    credit or transfer species/strain roles.
  snapshot_sha256: f806240f1ff8a94ab163860a370a55b75d773a8f648573732831e9d207b61242
- evidence_id: bgc-2443-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-target-input-plan-001.json
  locator: /records/2/proposed_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Literal one-hop shared-BGC predicates and exact direct companion paths
    only; no transitive expansion or transfer of identity, stereochemistry, activity
    or mechanism.
  snapshot_sha256: d8a44564b39627c62877f3b0921e0b13011b120098db5d35d33f5a2bc3d6a1df
- evidence_id: bgc-2443-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key;
    /contexts/9/owned_bgc_ids; /contexts/10/path; /contexts/10/identifier; /contexts/10/label;
    /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Distinct full keys, identities, labels and owned loci define the selected
    owner’s direct context; shared BGC membership is not identity equivalence.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
- evidence_id: bgc-2443-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved mibig_compounds frame contains 1 placements; its exact predicate,
    query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory mibig_compounds: literal predicate exact complete
    standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2443-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2519–2519; row_sha256 05077574bcac56dd576b2376e02b472fe81acda7075fdfab80ec4a7d81dc42b5
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact full-key/version/compound-index, producer/locus grades and citation-tier
    fields. BGC complete selected source-row reading and current physical bytes are
    joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2443-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved chebi_structures frame contains 0 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory chebi_structures: literal predicate exact complete
    standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2443-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved lotus_occurrences frame contains 0 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory lotus_occurrences: literal predicate exact
    complete standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete
    matching payloads or empty result frame retained. No external lookup or query
    replay.'
- evidence_id: bgc-2443-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame contains 0 placements; its
    exact predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory cyanometdb_occurrences: literal predicate exact
    complete standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete
    matching payloads or empty result frame retained. No external lookup or query
    replay.'
- evidence_id: bgc-2443-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved npclassifier frame contains 1 placements; its exact predicate,
    query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory npclassifier: literal predicate exact complete
    standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2443-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1139–1139; row_sha256 f3302cffe2a2262bcdaa4dc8380b67b1ad96e3118ba4c32699fde972a4e9c27f
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    is not guaranteed by retention. BGC complete selected source-row reading and current
    physical bytes are joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2443-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame contains 1 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory pubchem_bioassay: literal predicate exact complete
    standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2443-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 3359–3359; row_sha256 d261d00704c3f8921245dc4ce5b69e68a19f193128a2755a3e022b7634e9b077
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact CID10072409 blank-AID/no-assay sentinel, with no activity measurement
    or inactive result. BGC complete selected source-row reading and current physical
    bytes are joined.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2443-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved bindingdb_targets frame contains 0 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory bindingdb_targets: literal predicate exact
    complete standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N". Complete
    matching payloads or empty result frame retained. No external lookup or query
    replay.'
- evidence_id: bgc-2443-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame contains 0 placements; its
    exact predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory antibioticmech_inchikeys: literal predicate
    exact complete standard_inchi_key equality; query "JNHPMJVSUJKCKH-KCCNSQSLSA-N".
    Complete matching payloads or empty result frame retained. No external lookup
    or query replay.'
- evidence_id: bgc-2443-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/8/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved chebi_origins frame contains 0 placements; its exact predicate,
    query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory chebi_origins: literal predicate exact chebi_id
    from exact full-key structure rows; query []. Complete matching payloads or empty
    result frame retained. No external lookup or query replay.'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:04:58.745110Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 7eb06a6ca3ba46a89e3143ba4577e69ee5f15cb4b210d94eacb75cb403730549
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:05:23.400080Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 9fd4e3ad709d6047c757bb93f69289bf8689e934def523093fad81695b2f8718
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:05:42.956098Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:06:17.242880Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:06:28.919996Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b64dd93ae78a663114393f190e69f05eacc19b62d12eeb842aa8b0aae78f76c5
assessments:
- assessment_id: bgc-2443-identity
  area: identity
  topic: Exact retained identity and bounded correspondence
  outcome: supported
  summary: The exact full key JNHPMJVSUJKCKH-KCCNSQSLSA-N and minted identifier naturalproductmech:mibig-eb3a34d0e2
    belong to BGC0002149 version 2 compound 3. Both saved encodings normalize to that
    key, C27H31NO5 and zero formal charge, with ten true comparisons and a complete
    supplied 33-atom match at its stated scope. PubChem:10072409 is a retained cross-reference.
    The neighboring leucyloxy and dimethylleucyloxy records have distinct keys and
    formulas; names and a common locus do not make them equivalent identities or demonstrate
    a reaction sequence.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-grounding-owner
  - bgc-2443-chemistry
  - bgc-2443-source-mibig_compounds
  - bgc-2443-query-chebi_structures
  - bgc-2443-direct-contexts
  - bgc-2443-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: JNHPMJVSUJKCKH-KCCNSQSLSA-N; exact retained key, not natural identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2443-grounding-owner
    - bgc-2443-chemistry
    - bgc-2443-source-mibig_compounds
    - bgc-2443-query-chebi_structures
    - bgc-2443-direct-contexts
    - bgc-2443-companion-boundaries
  - name: grounding_scope
    value: The exact full key JNHPMJVSUJKCKH-KCCNSQSLSA-N and minted identifier naturalproductmech:mibig-eb3a34d0e2
      belong to BGC0002149 version 2 compound 3. Both saved encodings normalize to
      that key, C27H31NO5 and zero formal charge, with ten true comparisons and a
      complete supplied 33-atom match at its stated scope. PubChem:10072409 is a retained
      cross-reference. The neighboring leucyloxy and dimethylleucyloxy records have
      distinct keys and formulas; names and a common locus do not make them equivalent
      identities or demonstrate a reaction sequence.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2443-grounding-owner
    - bgc-2443-chemistry
    - bgc-2443-source-mibig_compounds
    - bgc-2443-query-chebi_structures
    - bgc-2443-direct-contexts
    - bgc-2443-companion-boundaries
- assessment_id: bgc-2443-representation
  area: representation
  topic: Stored-form stereochemistry and topology limits
  outcome: supported
  summary: Both saved forms report seven specified tetrahedral centers and no unresolved
    potential stereo, consistent with the stored true flag at the maintained extractor’s
    chiral-center scope. The fused aromatic N-containing system, carbonyl and oxygen
    bridges remain explicit in the complete tables. All ten comparisons agree, but
    full_graph_identity_established remains false and no natural stereochemical authentication
    is inferred. No biochemical atom numbering or named substituent position is assigned
    solely from zero-based diagnostic indices.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-grounding-owner
  - bgc-2443-chemistry
  - bgc-2443-topology
  - bgc-2443-diagnostic-reading
  - bgc-2443-diagnostic-acceptance
  - bgc-2443-structure-schema
  - bgc-2443-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms report seven specified tetrahedral centers and no unresolved
      potential stereo, consistent with the stored true flag at the maintained extractor’s
      chiral-center scope. The fused aromatic N-containing system, carbonyl and oxygen
      bridges remain explicit in the complete tables. All ten comparisons agree, but
      full_graph_identity_established remains false and no natural stereochemical
      authentication is inferred. No biochemical atom numbering or named substituent
      position is assigned solely from zero-based diagnostic indices.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2443-grounding-owner
    - bgc-2443-chemistry
    - bgc-2443-topology
    - bgc-2443-diagnostic-reading
    - bgc-2443-diagnostic-acceptance
    - bgc-2443-structure-schema
    - bgc-2443-stereo-method
  - name: representation_correspondence
    value: All ten comparisons are true and the supplied chirality-aware atom match
      is complete at its stated scope. Full graph and natural identity remain unestablished.
      full_graph_identity_established remains false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2443-grounding-owner
    - bgc-2443-chemistry
    - bgc-2443-topology
    - bgc-2443-diagnostic-reading
    - bgc-2443-diagnostic-acceptance
    - bgc-2443-structure-schema
    - bgc-2443-stereo-method
- assessment_id: bgc-2443-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: The retained MIBiG record identifies Aspergillus alliaceus ATCC 20738,
    NCBITaxon:209559, at BGC_CHARACTERIZED. Its separately graded CLUSTER_DEMONSTRATED
    locus is OK546695.1:1–40000, with Knock-out studies, Heterologous expression and
    Correlated expression listed. These source assertions are preserved without upgrading
    them to a fresh independent strain/construct verification. There is no retained
    occurrence assertion to substitute for producer evidence, and common BGC2149 membership
    does not transfer results between the three selected compounds.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-origin-owner
  - bgc-2443-occurrence-owner
  - bgc-2443-source-mibig_compounds
  - bgc-2443-cached-taxonomy
  - bgc-2443-curation-scope
  - bgc-2443-direct-contexts
  - bgc-2443-companion-boundaries
  dimensions:
  - name: taxon_scope
    value: The retained MIBiG record identifies Aspergillus alliaceus ATCC 20738,
      NCBITaxon:209559, at BGC_CHARACTERIZED. Its separately graded CLUSTER_DEMONSTRATED
      locus is OK546695.1:1–40000, with Knock-out studies, Heterologous expression
      and Correlated expression listed. These source assertions are preserved without
      upgrading them to a fresh independent strain/construct verification. There is
      no retained occurrence assertion to substitute for producer evidence, and common
      BGC2149 membership does not transfer results between the three selected compounds.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2443-origin-owner
    - bgc-2443-occurrence-owner
    - bgc-2443-source-mibig_compounds
    - bgc-2443-cached-taxonomy
    - bgc-2443-curation-scope
    - bgc-2443-direct-contexts
    - bgc-2443-companion-boundaries
  - name: producer_evidence
    value: The retained MIBiG record identifies Aspergillus alliaceus ATCC 20738,
      NCBITaxon:209559, at BGC_CHARACTERIZED. Its separately graded CLUSTER_DEMONSTRATED
      locus is OK546695.1:1–40000, with Knock-out studies, Heterologous expression
      and Correlated expression listed. These source assertions are preserved without
      upgrading them to a fresh independent strain/construct verification. There is
      no retained occurrence assertion to substitute for producer evidence, and common
      BGC2149 membership does not transfer results between the three selected compounds.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2443-origin-owner
    - bgc-2443-occurrence-owner
    - bgc-2443-source-mibig_compounds
    - bgc-2443-cached-taxonomy
    - bgc-2443-curation-scope
    - bgc-2443-direct-contexts
    - bgc-2443-companion-boundaries
  - name: locus_evidence
    value: The retained MIBiG record identifies Aspergillus alliaceus ATCC 20738,
      NCBITaxon:209559, at BGC_CHARACTERIZED. Its separately graded CLUSTER_DEMONSTRATED
      locus is OK546695.1:1–40000, with Knock-out studies, Heterologous expression
      and Correlated expression listed. These source assertions are preserved without
      upgrading them to a fresh independent strain/construct verification. There is
      no retained occurrence assertion to substitute for producer evidence, and common
      BGC2149 membership does not transfer results between the three selected compounds.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2443-origin-owner
    - bgc-2443-occurrence-owner
    - bgc-2443-source-mibig_compounds
    - bgc-2443-cached-taxonomy
    - bgc-2443-curation-scope
    - bgc-2443-direct-contexts
    - bgc-2443-companion-boundaries
- assessment_id: bgc-2443-citations
  area: evidence
  topic: Citation tiers and seed-history scope
  outcome: supported
  summary: PMID:35315670 is explicitly ENTRY evidence for the MIBiG source placement,
    not a retained compound-specific activity report. It repeats across the three
    BGC2149 owners and is not counted as three independent studies. The two SEEDED_FROM_SOURCES
    events establish inventory provenance rather than primary experimental review.
    No primary text was freshly accessed and no status promotion follows from the
    cited database grades.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-owner
  - bgc-2443-history-owner
  - bgc-2443-origin-owner
  - bgc-2443-occurrence-owner
  - bgc-2443-source-mibig_compounds
  - bgc-2443-source-reading
  dimensions:
  - name: citation_scope
    value: PMID:35315670 is explicitly ENTRY evidence for the MIBiG source placement,
      not a retained compound-specific activity report. It repeats across the three
      BGC2149 owners and is not counted as three independent studies. The two SEEDED_FROM_SOURCES
      events establish inventory provenance rather than primary experimental review.
      No primary text was freshly accessed and no status promotion follows from the
      cited database grades.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2443-owner
    - bgc-2443-history-owner
    - bgc-2443-origin-owner
    - bgc-2443-occurrence-owner
    - bgc-2443-source-mibig_compounds
    - bgc-2443-source-reading
- assessment_id: bgc-2443-occurrence
  area: evidence
  topic: Finite occurrence and assay scope
  outcome: supported
  summary: LOTUS, ChEBI-origin and CyanoMetDB frames are empty for this exact identity
    and there are no owner occurrence roots. The one PubChem row for CID10072409 has
    a blank AID and is explicitly a no-assay sentinel, not an inactive call or measured
    potency. BindingDB and related-corpus joins are empty. No biological inactivity,
    target, congener activity or molecular mechanism is inferred.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-occurrence-owner
  - bgc-2443-mechanism-absence
  - bgc-2443-query-lotus_occurrences
  - bgc-2443-query-chebi_origins
  - bgc-2443-query-cyanometdb_occurrences
  - bgc-2443-query-pubchem_bioassay
  - bgc-2443-query-bindingdb_targets
  - bgc-2443-query-antibioticmech_inchikeys
  - bgc-2443-cached-taxonomy
  - bgc-2443-taxonomy-routes
  - bgc-2443-taxonomy-reading
  - bgc-2443-curation-scope
  - bgc-2443-source-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    value: LOTUS, ChEBI-origin and CyanoMetDB frames are empty for this exact identity
      and there are no owner occurrence roots. The one PubChem row for CID10072409
      has a blank AID and is explicitly a no-assay sentinel, not an inactive call
      or measured potency. BindingDB and related-corpus joins are empty. No biological
      inactivity, target, congener activity or molecular mechanism is inferred.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2443-occurrence-owner
    - bgc-2443-mechanism-absence
    - bgc-2443-query-lotus_occurrences
    - bgc-2443-query-chebi_origins
    - bgc-2443-query-cyanometdb_occurrences
    - bgc-2443-query-pubchem_bioassay
    - bgc-2443-query-bindingdb_targets
    - bgc-2443-query-antibioticmech_inchikeys
    - bgc-2443-cached-taxonomy
    - bgc-2443-taxonomy-routes
    - bgc-2443-taxonomy-reading
    - bgc-2443-curation-scope
    - bgc-2443-source-pubchem_bioassay
  - name: assay_target_scope
    value: The exact blank-AID sentinel contains no assay identifier or measurement.
      It must not become an inactive result, potency endpoint, target or source of
      assay evidence.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2443-occurrence-owner
    - bgc-2443-mechanism-absence
    - bgc-2443-query-lotus_occurrences
    - bgc-2443-query-chebi_origins
    - bgc-2443-query-cyanometdb_occurrences
    - bgc-2443-query-pubchem_bioassay
    - bgc-2443-query-bindingdb_targets
    - bgc-2443-query-antibioticmech_inchikeys
    - bgc-2443-cached-taxonomy
    - bgc-2443-taxonomy-routes
    - bgc-2443-taxonomy-reading
    - bgc-2443-curation-scope
    - bgc-2443-source-pubchem_bioassay
- assessment_id: bgc-2443-classification
  area: consistency
  topic: Model fidelity with specific family applicability unverified
  outcome: unknown
  summary: NPClassifier version 2026-09-07 retains Alkaloids and Terpenoids, Tryptophan
    alkaloids and Indole-Diterpenoid alkaloids (Penitrems), glycoside false. The NRPS/TERPENE
    BGC classes are separate source metadata; the source compound-class list is empty.
    The aromatic N-containing fused framework supports broad indole-terpenoid compatibility,
    while the specific parenthetical Penitrem family is not independently established
    by the retained source or local motifs. Multiple model labels explain UNCLASSIFIED
    filing. This applicability uncertainty is not an established source-ingestion
    defect.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-classification-owner
  - bgc-2443-source-npclassifier
  - bgc-2443-chemistry
  - bgc-2443-topology
  - bgc-2443-structure-schema
  - bgc-2443-classification-seeder
  - bgc-2443-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: NPClassifier version 2026-09-07 retains Alkaloids and Terpenoids, Tryptophan
      alkaloids and Indole-Diterpenoid alkaloids (Penitrems), glycoside false. The
      NRPS/TERPENE BGC classes are separate source metadata; the source compound-class
      list is empty. The aromatic N-containing fused framework supports broad indole-terpenoid
      compatibility, while the specific parenthetical Penitrem family is not independently
      established by the retained source or local motifs. Multiple model labels explain
      UNCLASSIFIED filing. This applicability uncertainty is not an established source-ingestion
      defect.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2443-classification-owner
    - bgc-2443-source-npclassifier
    - bgc-2443-chemistry
    - bgc-2443-topology
    - bgc-2443-structure-schema
    - bgc-2443-classification-seeder
    - bgc-2443-source-mibig_compounds
- assessment_id: bgc-2443-completion
  area: completeness
  topic: Actual evidence coverage and remaining limits
  outcome: unknown
  summary: The complete owner and two histories, accepted 39-input canonical intake,
    all nine selected source frames including the blank-AID row, full paired tables
    and two distinct selected BGC peers are covered. No mechanism/component/target
    root is declared and no maintained-reader result is needed. Primary literature,
    natural identity, named Penitrem applicability, full QC and complete OAK remain
    unavailable; review remains partial with no source-edit finding.
  target_ids:
  - naturalproductmech:mibig-eb3a34d0e2
  evidence_ids:
  - bgc-2443-owner
  - bgc-2443-capture
  - bgc-2443-intake
  - bgc-2443-intake-acceptance
  - bgc-2443-history-owner
  - bgc-2443-diagnostic-reading
  - bgc-2443-diagnostic-acceptance
  - bgc-2443-diagnostic-execution
  - bgc-2443-source-reading
  - bgc-2443-joint-source-notes
  - bgc-2443-source-plan-execution
  - bgc-2443-native-gate-limits
  - bgc-2443-curation-scope
  - bgc-2443-mechanism-absence
  dimensions:
  - name: review_completion
    value: The complete owner and two histories, accepted 39-input canonical intake,
      all nine selected source frames including the blank-AID row, full paired tables
      and two distinct selected BGC peers are covered. No mechanism/component/target
      root is declared and no maintained-reader result is needed. Primary literature,
      natural identity, named Penitrem applicability, full QC and complete OAK remain
      unavailable; review remains partial with no source-edit finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2443-owner
    - bgc-2443-capture
    - bgc-2443-intake
    - bgc-2443-intake-acceptance
    - bgc-2443-history-owner
    - bgc-2443-diagnostic-reading
    - bgc-2443-diagnostic-acceptance
    - bgc-2443-diagnostic-execution
    - bgc-2443-source-reading
    - bgc-2443-joint-source-notes
    - bgc-2443-source-plan-execution
    - bgc-2443-native-gate-limits
    - bgc-2443-curation-scope
    - bgc-2443-mechanism-absence
findings: []
actions: []
limitations:
- Retained local evidence only. Fresh primary literature, current taxonomy, assay
  protocols and independent natural identity/stereochemical authentication remain
  unavailable.
- Five local native commands passed, but full QC and complete OAK remain unavailable.
  Saved normalized forms and atom matches do not establish independent full graph
  or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain separate. Shared BGC
  membership and repeated references do not transfer biological claims or establish
  independent experiments.
- Named model-family applicability is explicitly unverified; retention fidelity and
  broad structural compatibility do not establish a specific biosynthetic family or
  a source-ingestion defect.
- The complete selected owner has no graph, pathway, component reference or molecular-target
  root. No maintained-reader result, source edit or status/history promotion is claimed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read ten first-five saved forms: 370 atom rows and 420 bond rows,
  complete strings/scalars/rings/stereo/motifs/maps; indices are diagnostic-local.
  The original diagnostic stderr was empty. No reparse occurred during review.'
- 'Disjoint source reading: BGC 10 contexts/90 frames/28 rows/373 fields; ROOT 7 contexts/63
  frames/60 rows/558 fields; Support 8 contexts/72 frames/32 rows/363 fields. Native
  read 32 cached stanzas and bounded curation, with zero positive-row credit. Prior
  raw/history readings and preferred ROOT CPA002 remain attributed.'
- BGC operated the original local collector and composer; Support operated canonical
  intakes; Native operated the original molecular diagnostic under ROOT delegation.
  Final report authoring only reads saved evidence and writes review artifacts.
- All first-five reviews remain partial. No supported source-edit finding or action
  is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-245
```
