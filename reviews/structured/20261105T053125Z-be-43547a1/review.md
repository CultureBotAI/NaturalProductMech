# Local evidence review: BE-43547A1

- Review: 20261105T053125Z-be-43547a1
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T04:47:08.820201Z
- Finished UTC: 2026-11-05T05:31:25.777694Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

This unsuffixed BE-43547A1 owner retains BGC0001330 provenance and three unspecified tetrahedral centers. Its connectivity-level stored strings agree with the more specified A1 record, but their full keys and evidence routes differ. A blank PubChem assay row supplies no activity result.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2515; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-7025b12525 | data/natural_products/unclassified/be-43547a1.yaml | generated | BE-43547A1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-7025b12525 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-7025b12525 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-7025b12525 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-7025b12525 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-7025b12525 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-7025b12525 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-7025b12525 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-7025b12525 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: unknown. Targets: naturalproductmech:mibig-7025b12525.

The MINTED naturalproductmech:mibig-7025b12525 in be-43547a1.yaml retains YHMLVTRWZBFDAT-ISLYRVAYSA-N, BGC0001330 version 5 and pubchem:9959574. The separately selected -2 owner retains YHMLVTRWZBFDAT-KLSYSPJQSA-N with three specified tetrahedral centers and BGC0001331 provenance. Their C30H49N3O7 formulas and corresponding nonisomeric saved strings agree, but this owner has no InChI /t layer. The reciprocal input role is an explicit comparison, not an exact-full-key or direct BGC relation between the two A1 owners. This encoding is stereochemically unspecified, not evidence for a natural mixture, an identical isolate or a justified merge.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-7025b12525.

The three unspecified tetrahedral centers support the retained stereo_complete=false. The specified E alkene does not make the record fully stereodefined. Agreement of nonisomeric strings with the -2 A1 owner establishes the compared encoding scope only; it does not supply the missing configurations or justify copying the other owner’s tetrahedral labels.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-7025b12525.

BGC0001330 version 5 assigns Micromonospora sp. RV43, taxon 1661387, as SOURCE_ASSERTION and NZ_LEKG01000004.1:20144–63730 as CLUSTER_UNSTATED, with no locus methods. The separate LOTUS occurrence names Micromonospora cinerea, taxon 292802. The selected -2 owner’s Salinispora CNR107 claim is different source context and does not replace or strengthen this record’s producer claim. Cached labels and synonyms do not bridge named strain and species assertions.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-7025b12525.

The retained producer/locus citation is MIBiG ENTRY PMID:26637117, and the LOTUS occurrence cites DOI:10.1002/ANIE.201509926. Both seeding histories were read. The separate -2 A1 and shared-BGC cohort references remain explicitly attributed; repeated placements do not establish independent experiments or settle OPEN shared-structure questions in other owners.

### Source-specific occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-7025b12525.

One Micromonospora cinerea occurrence is retained. PubChem CID9959574 contributes only a blank-AID no-assay-data sentinel, with empty activity, endpoint, target and reference fields. No BindingDB target, bioactivity root or molecular-target root is declared. Direct cohort contexts and unselected C2 provide bounded source comparison without activity, stereochemical, producer-grade or review-coverage transfer.

### Reported model families and qualified applicability

consistency: supported. Targets: naturalproductmech:mibig-7025b12525.

The versioned model reports Amino acids and Peptides plus Polyketides, Oligopeptides, Cyclic peptides, Depsipeptides and Lipopeptides, with false glycoside. The saved 17-membered three-amide/one-ester macrocycle and long alkyl substituent are compatible with the structural cyclic depsipeptide/lipopeptide labels. Source NRPS/PKS annotations and computed model pathways are distinct from experimentally established biosynthetic mechanisms. The complete topology supports the nonglycoside interpretation without treating the absence of one ring motif as a universal rule; UNCLASSIFIED filing follows multiple model pathway outputs.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-7025b12525.

The complete retained owner and history, actual canonical intake, saved source frames, cached taxonomy and original molecular diagnostic were reviewed. Five documented local gates passed, but full QC and OAK were unavailable; no primary literature, fresh taxonomy, authoritative structure service, sequence or assay protocol was retrieved. No external requests were made. The review remains partial, and this bounded evidence does not support a record-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2515-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/be-43547a1.yaml; Complete plaintext including every curation_history entry | supports | Complete BE-43547A1 owner and 2 history events; earlier whole reading carries by current identical bytes. |
| bgc-2515-capture | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2515-intake | /private/tmp/npm-review-work/shared-next-batch252/intakes/2515-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, maintained ownership and all 44 input placements joined to the accepted plan and current hashes. |
| bgc-2515-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch252/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/4 | supports | ROOT accepted this original canonical intake and its exact plan, inspection and receipt pins. |
| bgc-2515-grounding-owner | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/label; /records/4/owner_document/chemical_structure; /records/4/owner_document/xrefs; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status; /records/4/owner_document/grounding_notes | supports | Exact retained identifier, structure, cross-references where present, source concepts and grounding fields. Historical annotations do not constitute a fresh authority lookup. |
| bgc-2515-origin-owner | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/producer_taxon_groups; /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, coordinates where declared and citation tiers. |
| bgc-2515-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete owner supplies the retained occurrences and bounded absence of selected bioactivity and molecular-target roots. Absence is not biological inactivity. |
| bgc-2515-classification-owner | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway; /records/4/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing and separate source categories; applicability is assessed separately. |
| bgc-2515-history-owner | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4/owner_document/curation_status; /records/4/owner_document/curation_history | supports | Complete history and status; seeding and historical curation do not imply new primary verification. |
| bgc-2515-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/4/owner_document | supports | Complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets and bioactivities roots; no maintained reader applies to this owner. |
| bgc-2515-chemistry | /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence; /records/4/smiles/computed/formula; /records/4/smiles/computed/formal_charge; /records/4/smiles/computed/standard_inchi; /records/4/smiles/computed/standard_inchi_key; /records/4/smiles/computed/canonical_isomeric_smiles; /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/atom_count; /records/4/smiles/computed/heavy_atom_count; /records/4/smiles/computed/bond_count; /records/4/smiles/computed/element_counts; /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/formula; /records/4/inchi/computed/formal_charge; /records/4/inchi/computed/standard_inchi; /records/4/inchi/computed/standard_inchi_key; /records/4/inchi/computed/canonical_isomeric_smiles; /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/atom_count; /records/4/inchi/computed/heavy_atom_count; /records/4/inchi/computed/bond_count; /records/4/inchi/computed/element_counts; /records/4/inchi/computed/stereo_counts | supports | Both own forms parse as neutral C30H49N3O7 with 40 atoms and 40 bonds and regenerate the same declared InChI and full key. Eight of ten comparisons are true; both canonical SMILES comparisons are false and the direct map is empty. Two secondary-amide to imidic changes explain the observed local representation differences; full_graph_identity_established remains false. |
| bgc-2515-topology | /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings; /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/motifs; /records/4/smiles/computed/fragment_atom_indices; /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/motifs; /records/4/inchi/computed/fragment_atom_indices | supports | The saved SMILES has one 17-membered ring, ester C4(=O5)-O3-C2, N-methyl amide C8(=O9)-N7, secondary amides C15(=O16)-N14 and C19(=O20)-N18, and ketone C22(=O23). The InChI-derived form retains the ester, tertiary amide and ketone but represents the secondary sites as C24(OH33)=N31 and C28(OH37)=N30. The three unspecified tetrahedral centers are SMILES C1, C2 and hydrogen-free C21, and InChI C22, C23 and C29. One carbon-carbon double bond is E, the exocyclic methylene has no E/Z pair, and the normalized imidic form adds two unspecified C=N sites. No saturated C5O cycle is reported. |
| bgc-2515-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-current252-first-five-molecular-intake-reading-001.json; /records/4; /totals; /whole_reading; /raw_and_source_carry; /limits | supports | BGC complete saved first-five molecular and intake reading, with exact per-form table counts and reading attribution; no new parse. |
| bgc-2515-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /readback; /original_exit_code; /original_terminal_chunk; /molecular_parse_attempts; /parsed; /comparisons_true; /comparisons_total; /global_warning_count; /external_requests; /method_scope; /interpretation_boundary; /ROOT_result_reading; /verification; /scientific_verdicts | supports | ROOT accepted the original twenty stored-form diagnostics. Global warning interpretation and method limits remain explicit; no per-record warning assignment is inferred. |
| bgc-2515-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins. |
| bgc-2515-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | Structure stereochemistry and named/versioned computed classification have distinct evidence scopes. |
| bgc-2515-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The maintained stereo_complete calculation uses unassigned molecular chiral centers; it is not a count of literal question marks in InChI. Atom type and double-bond geometry require separate interpretation. |
| bgc-2515-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while exact model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2515-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 126–145; 1318–1382 | supports | Deposited calls, endpoints and values retain their source scope. Activity classes derived from active assay titles do not independently prove mechanisms or direct binding. |
| bgc-2515-source-reading | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-current252-assigned-source-reading-001.json; /partition; /contexts; /reading; /cautions; /attribution | supports | BGC wholly read selected first-five contexts 1–5 and unselected companions 0 and 11: 63 frames, 27 rows and 331 fields, including 19 selected rows/224 fields and eight companion rows/107 fields. Companion rows add no selected review coverage or transferred activity. |
| bgc-2515-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete source reading covers 108 frames, 46 rows and 640 fields: BGC 27 and Support 19 rows. Native taxonomy/curation has zero positive-source-row credit; secondary peer readings add no primary row credit. |
| bgc-2515-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch252/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope | supports | One original composer produced the accepted plan at 421 placements/49 paths, with exact source notes and attributed reading receipts. This fragment consumes saved results only. |
| bgc-2515-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch252/root-target-input-plan-acceptance-001.json; /status; /accepted; /plan; /execution; /source_placements; /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification; /reading | supports | ROOT accepted the exact 421-placement/49-path source plan and original results; no query or input expansion is inferred. |
| bgc-2515-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch252/root-current252-native-gates-acceptance-001.json; /status; /verification; /all_native_gates_passed; /unavailable_required_gates; /scope | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed remains false. Technical checks do not complete scientific verification. |
| bgc-2515-curation-scope | /private/tmp/npm-review-work/shared-next-batch252-tentative/native-prep/native-current252-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | Bounded ignored-inclusive Native applicability review found no matching correction or exclusion; sixteen unrelated Streptomyces-token overlaps do not establish a record correction. There are zero actual AID rows and two blank-AID sentinels, belonging to BE-14106 and the unsuffixed A1 owner. |
| bgc-2515-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/9 | supports | Complete saved cache names and synonyms for this owner’s source IDs; no independent taxonomic rank, strain, occurrence or producer validation. |
| bgc-2515-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/source_taxa; /contexts/5/source_scope_inventory/forward_taxon_merge_matches; /contexts/5/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh taxonomy request. |
| bgc-2515-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch252-tentative/native-prep/native-current252-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /routes; /interpretation | supports | Native read all eleven whole retained stanzas and twelve routes, including the retained 65497 to 2893586 forward route. Source labels, cached names and synonyms do not establish missing strain or biological evidence. |
| bgc-2515-direct-contexts | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-target-input-plan-001.json; /records/4/proposed_companion_paths; /records/4/direct_companion_predicates | supports | Exact immediate owned-BGC context inputs; shared locus/citation is not identity, stereochemistry, assay or mechanism transfer. No transitive or name-based expansion. |
| bgc-2515-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/6/path; /contexts/6/identifier; /contexts/6/label; /contexts/6/standard_inchi_key; /contexts/6/complete_raw_text; /contexts/6/complete_raw_history; /contexts/6/source_scope_inventory; /contexts/7/path; /contexts/7/identifier; /contexts/7/label; /contexts/7/standard_inchi_key; /contexts/7/complete_raw_text; /contexts/7/complete_raw_history; /contexts/7/source_scope_inventory; /contexts/8/path; /contexts/8/identifier; /contexts/8/label; /contexts/8/standard_inchi_key; /contexts/8/complete_raw_text; /contexts/8/complete_raw_history; /contexts/8/source_scope_inventory; /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key; /contexts/9/complete_raw_text; /contexts/9/complete_raw_history; /contexts/9/source_scope_inventory; /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history; /contexts/10/source_scope_inventory; /contexts/11/path; /contexts/11/identifier; /contexts/11/label; /contexts/11/standard_inchi_key; /contexts/11/complete_raw_text; /contexts/11/complete_raw_history; /contexts/11/source_scope_inventory | supports | Complete directly linked companion encodings, histories and saved source frames. Unselected companions are context only; cohort owners remain separately attributed. No activity, stereochemistry, evidence-grade or coverage transfer. |
| bgc-2515-companion-reading | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-current252-two-companion-whole-reading-001.json; /observer; /recorded_at; /status; /census; /originals; /records; /totals; /scope; /actual_source_inventory; /source_row_credit; /review_coverage_credit; /external_requests; /target_invocations | supports | BGC complete plaintext/history reading of Basiliskamide A and BE-43547C2; unselected context only, with no selected coverage or claim transfer. |
| bgc-2515-selected-A1-comparison-owner | /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete separately selected A1 owner, including exact structure, xref presence, source concepts, provenance and history; an explicit bounded comparison, not a census relationship or deduplication instruction. |
| bgc-2515-selected-A1-comparison-strings | /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed/canonical_nonisomeric_smiles; /records/3/smiles/computed/canonical_isomeric_smiles; /records/3/smiles/computed/standard_inchi_key; /records/3/smiles/computed/stereo_counts; /records/3/inchi/computed/canonical_nonisomeric_smiles; /records/3/inchi/computed/canonical_isomeric_smiles; /records/3/inchi/computed/standard_inchi_key; /records/3/inchi/computed/stereo_counts; /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/canonical_isomeric_smiles; /records/4/smiles/computed/standard_inchi_key; /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/canonical_isomeric_smiles; /records/4/inchi/computed/standard_inchi_key; /records/4/inchi/computed/stereo_counts; /records/3/declared_structure; /records/4/declared_structure | supports | Both selected A1 records have identical corresponding nonisomeric strings but distinct full stereochemical keys and three specified versus three unspecified tetrahedral centers. This comparison does not establish identical natural isolates. |
| bgc-2515-selected-A1-comparison-role | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-target-input-plan-001.json; /records/4/identity_comparison_paths; /records/4/additional_context_paths; /records/4/additional_context_roles | supports | Explicit separate reciprocal selected-owner comparison role; no extra source query, direct BGC edge or exact-full-key relationship is inferred. |
| bgc-2515-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2515-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 1557–1557; row_sha256 80b51a60b7c80511800fff7a4e6aabeef77410e2b48b69929c74f5defe5c8f7c | supports | Exact retained compound/version, structure/key, xrefs, producer/locus grades and citation tiers. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2515-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2515-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2515-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 9813–9813; row_sha256 d391c2f1fb4f422300f057fea0d292b5aebff1a4d941661df0bd4d27f290c791 | supports | Exact organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2515-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2515-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2515-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2918–2918; row_sha256 f7881cbe767d0e57144f20283782f5f1c3113275a0d34f95fa12db82a96c212c | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability remains separate. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2515-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2515-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 10135–10135; row_sha256 9a6c8ee093adf164d872f553d57b049c61799482c44a1605ac54307b14baf628 | supports | Exact retained full-key/CID and blank-AID no-assay-data sentinel; not a measured inactive result. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2515-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2515-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2515-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 row placements, exact predicate/query and all fields. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-252/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-252/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-252/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-252/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-252/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- The encoding leaves three tetrahedral centers unspecified and does not establish a natural mixture or equivalence with the other A1 owner.
- Two secondary-amide/imidic changes leave the direct atom map empty despite normalized-key equality.
- The PubChem row is a blank-AID sentinel, and producer/locus evidence remains source-qualified.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five saved molecular forms (406 atom rows and 406 bond rows) and 201 actual intake placements across 49 paths, without new parsing.
- Disjoint source reading: BGC first-five selected plus two companions, 63 frames/27 rows/331 fields; Support last-five, 45 frames/19 rows/309 fields. Native cache/curation receives zero positive-source-row credit.
- BGC operated original collector/composer; Support operated canonical intakes; Native operated the original diagnostic under ROOT delegation. No selected owner requires a maintained reader. These fragments consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T053125Z-be-43547a1
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: BE-43547A1'
started_at: '2026-11-05T04:47:08.820201Z'
finished_at: '2026-11-05T05:31:25.777694Z'
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
summary: This unsuffixed BE-43547A1 owner retains BGC0001330 provenance and three
  unspecified tetrahedral centers. Its connectivity-level stored strings agree with
  the more specified A1 record, but their full keys and evidence routes differ. A
  blank PubChem assay row supplies no activity result.
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
  - path: data/natural_products/unclassified/be-43547a1-2.yaml
    sha256: 841dd8793ce216e51ddb89843f5c7aa964abbbb7e3509dc66c294571639b3e41
    role: context
  - path: data/natural_products/unclassified/be-43547a1.yaml
    sha256: 3058dd754ac5ab9a1fc0f381401a43d92f4ded8d59119f3cd785cfa157c29e81
    role: target
  - path: data/natural_products/unclassified/be-43547a2.yaml
    sha256: 856d15ac37350fb2333737abae44c0178f65b0b385e3909246fbc02493092de2
    role: context
  - path: data/natural_products/unclassified/be-43547b1.yaml
    sha256: d53bebc08a65a1803b231e677c551fac8f458c9aac16e55ff316cb052887a711
    role: context
  - path: data/natural_products/unclassified/be-43547b2.yaml
    sha256: 9f24078559d93f044f7e9186f25023932b9b8ff2204237ca98ac4dd8ebf31e4e
    role: context
  - path: data/natural_products/unclassified/be-43547b3.yaml
    sha256: 622b6a1d6619ce9da40f926c4e0a402fa16e8a9cc14234222bee4cb9bb41c851
    role: context
  - path: data/natural_products/unclassified/be-43547c1.yaml
    sha256: 5d49ca8864379344ecded1f30f00272766d7407872cde8714e025b64c2dd4818
    role: context
  - path: data/natural_products/unclassified/be-43547c2.yaml
    sha256: 36050e64f55762d60a22f08002100e86b8d27653e70f5e4a5b4dbb873200c084
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
  selection: Campaign path order 2515; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-7025b12525
targets:
- target_id: naturalproductmech:mibig-7025b12525
  path: data/natural_products/unclassified/be-43547a1.yaml
  label: BE-43547A1
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
    path: data/raw/pubchem_bioassay.tsv
    role: Retained assay rows or empty-assay sentinels; source outcome and title alone
      do not establish mechanism.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/be-43547a1-2.yaml
    role: Explicit ROOT-requested already-selected encoded identity comparison only;
      not a census companion or extra source-query context.
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
  - naturalproductmech:mibig-7025b12525
  command: just validate-strict data/natural_products/unclassified/basiliskamide-b.yaml
    data/natural_products/unclassified/bassianolide.yaml data/natural_products/unclassified/be-14106.yaml
    data/natural_products/unclassified/be-43547a1-2.yaml data/natural_products/unclassified/be-43547a1.yaml
    data/natural_products/unclassified/be-43547a2.yaml data/natural_products/unclassified/be-43547b1.yaml
    data/natural_products/unclassified/be-43547b2.yaml data/natural_products/unclassified/be-43547b3.yaml
    data/natural_products/unclassified/be-43547c1.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-252/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-7025b12525
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-252/validate-all-001.tsv
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
  - naturalproductmech:mibig-7025b12525
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
  - naturalproductmech:mibig-7025b12525
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
  - naturalproductmech:mibig-7025b12525
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-252/review-queue-001.tsv
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
  - naturalproductmech:mibig-7025b12525
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-7025b12525
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-7025b12525
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2515-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/be-43547a1.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete BE-43547A1 owner and 2 history events; earlier whole reading carries
    by current identical bytes.
  snapshot_sha256: 3058dd754ac5ab9a1fc0f381401a43d92f4ded8d59119f3cd785cfa157c29e81
- evidence_id: bgc-2515-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/intakes/2515-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Actual canonical target, maintained ownership and all 44 input placements
    joined to the accepted plan and current hashes.
  snapshot_sha256: c93afd34323aec71d63f1695fa2fdc036e7ebe61de02bbd5aca8f93075ecd76b
- evidence_id: bgc-2515-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/4
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: ROOT accepted this original canonical intake and its exact plan, inspection
    and receipt pins.
  snapshot_sha256: d1eced0a9fb6432033f2e2411abe9d8b69c207007d9f7b60a04eef789bc79ac6
- evidence_id: bgc-2515-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/label;
    /records/4/owner_document/chemical_structure; /records/4/owner_document/xrefs;
    /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status;
    /records/4/owner_document/grounding_notes
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact retained identifier, structure, cross-references where present, source
    concepts and grounding fields. Historical annotations do not constitute a fresh
    authority lookup.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/producer_taxon_groups;
    /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, coordinates
    where declared and citation tiers.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete owner supplies the retained occurrences and bounded absence of
    selected bioactivity and molecular-target roots. Absence is not biological inactivity.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway;
    /records/4/owner_document/bgc_class
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing and separate
    source categories; applicability is assessed separately.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4/owner_document/curation_status; /records/4/owner_document/curation_history
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete history and status; seeding and historical curation do not imply
    new primary verification.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/4/owner_document
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway,
    molecular_targets and bioactivities roots; no maintained reader applies to this
    owner.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Both own forms parse as neutral C30H49N3O7 with 40 atoms and 40 bonds and
    regenerate the same declared InChI and full key. Eight of ten comparisons are
    true; both canonical SMILES comparisons are false and the direct map is empty.
    Two secondary-amide to imidic changes explain the observed local representation
    differences; full_graph_identity_established remains false.
  snapshot_sha256: f736c36efdbd17008ea3c47fd3e0acb8b8ce07e1fcebb63cdbfd2bb2e2102435
- evidence_id: bgc-2515-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds;
    /records/4/smiles/computed/rings; /records/4/smiles/computed/potential_stereo;
    /records/4/smiles/computed/motifs; /records/4/smiles/computed/fragment_atom_indices;
    /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings;
    /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/motifs;
    /records/4/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: The saved SMILES has one 17-membered ring, ester C4(=O5)-O3-C2, N-methyl
    amide C8(=O9)-N7, secondary amides C15(=O16)-N14 and C19(=O20)-N18, and ketone
    C22(=O23). The InChI-derived form retains the ester, tertiary amide and ketone
    but represents the secondary sites as C24(OH33)=N31 and C28(OH37)=N30. The three
    unspecified tetrahedral centers are SMILES C1, C2 and hydrogen-free C21, and InChI
    C22, C23 and C29. One carbon-carbon double bond is E, the exocyclic methylene
    has no E/Z pair, and the normalized imidic form adds two unspecified C=N sites.
    No saturated C5O cycle is reported.
  snapshot_sha256: f736c36efdbd17008ea3c47fd3e0acb8b8ce07e1fcebb63cdbfd2bb2e2102435
- evidence_id: bgc-2515-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-current252-first-five-molecular-intake-reading-001.json
  locator: /records/4; /totals; /whole_reading; /raw_and_source_carry; /limits
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: BGC complete saved first-five molecular and intake reading, with exact
    per-form table counts and reading attribution; no new parse.
  snapshot_sha256: 625c9ab7df77ad137eb0f068d235bddebe1a95efe643ac7c5712697dd01d7cdd
- evidence_id: bgc-2515-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /readback; /original_exit_code; /original_terminal_chunk; /molecular_parse_attempts;
    /parsed; /comparisons_true; /comparisons_total; /global_warning_count; /external_requests;
    /method_scope; /interpretation_boundary; /ROOT_result_reading; /verification;
    /scientific_verdicts
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostics. Global warning
    interpretation and method limits remain explicit; no per-record warning assignment
    is inferred.
  snapshot_sha256: d3bcf81096c4a493fd5c8563a934283d29a39f1a7e793b417c8870a29a608b78
- evidence_id: bgc-2515-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins.
  snapshot_sha256: 88ce1437523bedffcf83ce83d267212dbb4f0e4c923bb2a2526290e2ad075a64
- evidence_id: bgc-2515-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Structure stereochemistry and named/versioned computed classification have
    distinct evidence scopes.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2515-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: The maintained stereo_complete calculation uses unassigned molecular chiral
    centers; it is not a count of literal question marks in InChI. Atom type and double-bond
    geometry require separate interpretation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2515-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while exact model
    arrays remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2515-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 126–145; 1318–1382
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Deposited calls, endpoints and values retain their source scope. Activity
    classes derived from active assay titles do not independently prove mechanisms
    or direct binding.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2515-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-current252-assigned-source-reading-001.json
  locator: /partition; /contexts; /reading; /cautions; /attribution
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'BGC wholly read selected first-five contexts 1–5 and unselected companions
    0 and 11: 63 frames, 27 rows and 331 fields, including 19 selected rows/224 fields
    and eight companion rows/107 fields. Companion rows add no selected review coverage
    or transferred activity.'
  snapshot_sha256: 8ae373562f2426b673cafdc6e5c033c75b46eb1969effec429ecc47ce82a26d7
- evidence_id: bgc-2515-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Disjoint complete source reading covers 108 frames, 46 rows and 640 fields:
    BGC 27 and Support 19 rows. Native taxonomy/curation has zero positive-source-row
    credit; secondary peer readings add no primary row credit.'
  snapshot_sha256: de8e3254910c790625a3d0b4cc29d93b5e0a569fe7015b48e0d7ee03899c3e24
- evidence_id: bgc-2515-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /terminal_chunk; /original_exit_code;
    /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: One original composer produced the accepted plan at 421 placements/49 paths,
    with exact source notes and attributed reading receipts. This fragment consumes
    saved results only.
  snapshot_sha256: 694f875c352073039ec588191a4ebe9f9e6ee91fdc9806528e7f834e2341e652
- evidence_id: bgc-2515-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/root-target-input-plan-acceptance-001.json
  locator: /status; /accepted; /plan; /execution; /source_placements; /unique_source_paths;
    /original_source_inventory_counts; /per_order_counts; /verification; /reading
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: ROOT accepted the exact 421-placement/49-path source plan and original
    results; no query or input expansion is inferred.
  snapshot_sha256: 3137a5ac1b8ffb197d77798d319c2321e791ae512f97de8a443b5c61a82b470f
- evidence_id: bgc-2515-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/root-current252-native-gates-acceptance-001.json
  locator: /status; /verification; /all_native_gates_passed; /unavailable_required_gates;
    /scope
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    remains false. Technical checks do not complete scientific verification.
  snapshot_sha256: e64eafcdc698f9e009f9d5c75fcbccc19d1b49851990b9b0b193a9b4175daa91
- evidence_id: bgc-2515-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/native-prep/native-current252-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Bounded ignored-inclusive Native applicability review found no matching
    correction or exclusion; sixteen unrelated Streptomyces-token overlaps do not
    establish a record correction. There are zero actual AID rows and two blank-AID
    sentinels, belonging to BE-14106 and the unsuffixed A1 owner.
  snapshot_sha256: 8dedf4044be81498ada51ade65adb16a2343bbb16fefac0e9356c8dd67eb798d
  search_scope: Twelve exact retained contexts across eleven enumerated curation TSVs
    including ignored files; nine eligible tables and 3422 rows, with exact retained
    owner/source/BGC/full-key/assay/occurrence predicates. This is not global absence
    or protocol validation.
- evidence_id: bgc-2515-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/5; /cached_taxonomy/whole_stanzas/9
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source IDs; no
    independent taxonomic rank, strain, occurrence or producer validation.
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
- evidence_id: bgc-2515-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/source_taxa; /contexts/5/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/5/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh
    taxonomy request.
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
- evidence_id: bgc-2515-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/native-prep/native-current252-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /routes; /interpretation
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Native read all eleven whole retained stanzas and twelve routes, including
    the retained 65497 to 2893586 forward route. Source labels, cached names and synonyms
    do not establish missing strain or biological evidence.
  snapshot_sha256: 20129ae28e3be14c7cceb9a96292d8c5844a845bcf898394e15d8a2c8db806ab
- evidence_id: bgc-2515-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-target-input-plan-001.json
  locator: /records/4/proposed_companion_paths; /records/4/direct_companion_predicates
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact immediate owned-BGC context inputs; shared locus/citation is not
    identity, stereochemistry, assay or mechanism transfer. No transitive or name-based
    expansion.
  snapshot_sha256: bffdeb5caf198ac9f1fa9950711bab4f94e00f19cc0ced38c698c3a55188ea2f
- evidence_id: bgc-2515-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/6/path; /contexts/6/identifier; /contexts/6/label; /contexts/6/standard_inchi_key;
    /contexts/6/complete_raw_text; /contexts/6/complete_raw_history; /contexts/6/source_scope_inventory;
    /contexts/7/path; /contexts/7/identifier; /contexts/7/label; /contexts/7/standard_inchi_key;
    /contexts/7/complete_raw_text; /contexts/7/complete_raw_history; /contexts/7/source_scope_inventory;
    /contexts/8/path; /contexts/8/identifier; /contexts/8/label; /contexts/8/standard_inchi_key;
    /contexts/8/complete_raw_text; /contexts/8/complete_raw_history; /contexts/8/source_scope_inventory;
    /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key;
    /contexts/9/complete_raw_text; /contexts/9/complete_raw_history; /contexts/9/source_scope_inventory;
    /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key;
    /contexts/10/complete_raw_text; /contexts/10/complete_raw_history; /contexts/10/source_scope_inventory;
    /contexts/11/path; /contexts/11/identifier; /contexts/11/label; /contexts/11/standard_inchi_key;
    /contexts/11/complete_raw_text; /contexts/11/complete_raw_history; /contexts/11/source_scope_inventory
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete directly linked companion encodings, histories and saved source
    frames. Unselected companions are context only; cohort owners remain separately
    attributed. No activity, stereochemistry, evidence-grade or coverage transfer.
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
- evidence_id: bgc-2515-companion-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-current252-two-companion-whole-reading-001.json
  locator: /observer; /recorded_at; /status; /census; /originals; /records; /totals;
    /scope; /actual_source_inventory; /source_row_credit; /review_coverage_credit;
    /external_requests; /target_invocations
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: BGC complete plaintext/history reading of Basiliskamide A and BE-43547C2;
    unselected context only, with no selected coverage or claim transfer.
  snapshot_sha256: bf42ce24e5fec8915bedb8c96d973a5503f81d2815c0e7e97c18f546bb20dd5b
- evidence_id: bgc-2515-selected-A1-comparison-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Complete separately selected A1 owner, including exact structure, xref
    presence, source concepts, provenance and history; an explicit bounded comparison,
    not a census relationship or deduplication instruction.
  snapshot_sha256: f6184b2c9664f13725cc30bb1fad93b956753ff8ab5209649e75a8621030c7b5
- evidence_id: bgc-2515-selected-A1-comparison-strings
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed/canonical_nonisomeric_smiles; /records/3/smiles/computed/canonical_isomeric_smiles;
    /records/3/smiles/computed/standard_inchi_key; /records/3/smiles/computed/stereo_counts;
    /records/3/inchi/computed/canonical_nonisomeric_smiles; /records/3/inchi/computed/canonical_isomeric_smiles;
    /records/3/inchi/computed/standard_inchi_key; /records/3/inchi/computed/stereo_counts;
    /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/canonical_isomeric_smiles;
    /records/4/smiles/computed/standard_inchi_key; /records/4/smiles/computed/stereo_counts;
    /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/canonical_isomeric_smiles;
    /records/4/inchi/computed/standard_inchi_key; /records/4/inchi/computed/stereo_counts;
    /records/3/declared_structure; /records/4/declared_structure
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Both selected A1 records have identical corresponding nonisomeric strings
    but distinct full stereochemical keys and three specified versus three unspecified
    tetrahedral centers. This comparison does not establish identical natural isolates.
  snapshot_sha256: f736c36efdbd17008ea3c47fd3e0acb8b8ce07e1fcebb63cdbfd2bb2e2102435
- evidence_id: bgc-2515-selected-A1-comparison-role
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-target-input-plan-001.json
  locator: /records/4/identity_comparison_paths; /records/4/additional_context_paths;
    /records/4/additional_context_roles
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Explicit separate reciprocal selected-owner comparison role; no extra source
    query, direct BGC edge or exact-full-key relationship is inferred.
  snapshot_sha256: bffdeb5caf198ac9f1fa9950711bab4f94e00f19cc0ced38c698c3a55188ea2f
- evidence_id: bgc-2515-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 1557–1557; row_sha256 80b51a60b7c80511800fff7a4e6aabeef77410e2b48b69929c74f5defe5c8f7c
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact retained compound/version, structure/key, xrefs, producer/locus grades
    and citation tiers. BGC whole saved-source reading and current physical bytes
    are joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2515-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 9813–9813; row_sha256 d391c2f1fb4f422300f057fea0d292b5aebff1a4d941661df0bd4d27f290c791
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. BGC whole saved-source
    reading and current physical bytes are joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2515-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: bgc-2515-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2918–2918; row_sha256 f7881cbe767d0e57144f20283782f5f1c3113275a0d34f95fa12db82a96c212c
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    remains separate. BGC whole saved-source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2515-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 10135–10135; row_sha256 9a6c8ee093adf164d872f553d57b049c61799482c44a1605ac54307b14baf628
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: Exact retained full-key/CID and blank-AID no-assay-data sentinel; not a
    measured inactive result. BGC whole saved-source reading and current physical
    bytes are joined.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2515-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 row placements, exact
    predicate/query and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "YHMLVTRWZBFDAT-ISLYRVAYSA-N". Complete
    matched payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2515-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch252-tentative/bgc-prep/bgc-conditional252-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T05:22:07.299790Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 754d419d4cf2ac1bafa351937c4e8692d3e8ebfee2ef4c8de5c96032527fa481
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-252/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json
  accessed_at: '2026-11-05T04:51:25.936788Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 9e841aab0d723628d7e251d55ffc2268fbc1bddf21d4a763a14e9bd61bd05afb
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-252/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json
  accessed_at: '2026-11-05T04:51:50.249957Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: fa6aa098821ce85b56a5d62775fa75f94d48f23b54d651f37a96628ed2693368
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-252/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json
  accessed_at: '2026-11-05T04:52:09.485891Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-252/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json
  accessed_at: '2026-11-05T04:52:42.749497Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-252/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-252/native-current252-five-gates-execution-001.json
  accessed_at: '2026-11-05T04:52:54.413588Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: ed9ae8ede1f0dbc861272fdefcb10cc468fd4c19a2af9a47e3fb89f1170c270d
assessments:
- assessment_id: bgc-2515-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: unknown
  summary: The MINTED naturalproductmech:mibig-7025b12525 in be-43547a1.yaml retains
    YHMLVTRWZBFDAT-ISLYRVAYSA-N, BGC0001330 version 5 and pubchem:9959574. The separately
    selected -2 owner retains YHMLVTRWZBFDAT-KLSYSPJQSA-N with three specified tetrahedral
    centers and BGC0001331 provenance. Their C30H49N3O7 formulas and corresponding
    nonisomeric saved strings agree, but this owner has no InChI /t layer. The reciprocal
    input role is an explicit comparison, not an exact-full-key or direct BGC relation
    between the two A1 owners. This encoding is stereochemically unspecified, not
    evidence for a natural mixture, an identical isolate or a justified merge.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-grounding-owner
  - bgc-2515-chemistry
  - bgc-2515-source-mibig_compounds
  - bgc-2515-query-chebi_structures
  - bgc-2515-direct-contexts
  - bgc-2515-companion-boundaries
  - bgc-2515-companion-reading
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: standard_inchi_key
    value: YHMLVTRWZBFDAT-ISLYRVAYSA-N; retained key, not independent natural-identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2515-grounding-owner
    - bgc-2515-chemistry
    - bgc-2515-source-mibig_compounds
    - bgc-2515-query-chebi_structures
    - bgc-2515-direct-contexts
    - bgc-2515-companion-boundaries
    - bgc-2515-companion-reading
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
  - name: grounding_scope
    value: The MINTED naturalproductmech:mibig-7025b12525 in be-43547a1.yaml retains
      YHMLVTRWZBFDAT-ISLYRVAYSA-N, BGC0001330 version 5 and pubchem:9959574. The separately
      selected -2 owner retains YHMLVTRWZBFDAT-KLSYSPJQSA-N with three specified tetrahedral
      centers and BGC0001331 provenance. Their C30H49N3O7 formulas and corresponding
      nonisomeric saved strings agree, but this owner has no InChI /t layer. The reciprocal
      input role is an explicit comparison, not an exact-full-key or direct BGC relation
      between the two A1 owners. This encoding is stereochemically unspecified, not
      evidence for a natural mixture, an identical isolate or a justified merge.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2515-grounding-owner
    - bgc-2515-chemistry
    - bgc-2515-source-mibig_compounds
    - bgc-2515-query-chebi_structures
    - bgc-2515-direct-contexts
    - bgc-2515-companion-boundaries
    - bgc-2515-companion-reading
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
- assessment_id: bgc-2515-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: The three unspecified tetrahedral centers support the retained stereo_complete=false.
    The specified E alkene does not make the record fully stereodefined. Agreement
    of nonisomeric strings with the -2 A1 owner establishes the compared encoding
    scope only; it does not supply the missing configurations or justify copying the
    other owner’s tetrahedral labels.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-grounding-owner
  - bgc-2515-chemistry
  - bgc-2515-topology
  - bgc-2515-diagnostic-reading
  - bgc-2515-diagnostic-acceptance
  - bgc-2515-structure-schema
  - bgc-2515-stereo-method
  - bgc-2515-companion-boundaries
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: stereochemistry_scope
    value: The three unspecified tetrahedral centers support the retained stereo_complete=false.
      The specified E alkene does not make the record fully stereodefined. Agreement
      of nonisomeric strings with the -2 A1 owner establishes the compared encoding
      scope only; it does not supply the missing configurations or justify copying
      the other owner’s tetrahedral labels.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2515-grounding-owner
    - bgc-2515-chemistry
    - bgc-2515-topology
    - bgc-2515-diagnostic-reading
    - bgc-2515-diagnostic-acceptance
    - bgc-2515-structure-schema
    - bgc-2515-stereo-method
    - bgc-2515-companion-boundaries
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
  - name: representation_correspondence
    value: Both own forms parse as neutral C30H49N3O7 with 40 atoms and 40 bonds and
      regenerate the same declared InChI and full key. Eight of ten comparisons are
      true; both canonical SMILES comparisons are false and the direct map is empty.
      Two secondary-amide to imidic changes explain the observed local representation
      differences; full_graph_identity_established remains false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2515-grounding-owner
    - bgc-2515-chemistry
    - bgc-2515-topology
    - bgc-2515-diagnostic-reading
    - bgc-2515-diagnostic-acceptance
    - bgc-2515-structure-schema
    - bgc-2515-stereo-method
    - bgc-2515-companion-boundaries
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
- assessment_id: bgc-2515-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: BGC0001330 version 5 assigns Micromonospora sp. RV43, taxon 1661387, as
    SOURCE_ASSERTION and NZ_LEKG01000004.1:20144–63730 as CLUSTER_UNSTATED, with no
    locus methods. The separate LOTUS occurrence names Micromonospora cinerea, taxon
    292802. The selected -2 owner’s Salinispora CNR107 claim is different source context
    and does not replace or strengthen this record’s producer claim. Cached labels
    and synonyms do not bridge named strain and species assertions.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-origin-owner
  - bgc-2515-occurrence-owner
  - bgc-2515-source-mibig_compounds
  - bgc-2515-cached-taxonomy
  - bgc-2515-taxonomy-routes
  - bgc-2515-curation-scope
  - bgc-2515-direct-contexts
  - bgc-2515-source-lotus_occurrences
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: taxon_scope
    value: BGC0001330 version 5 assigns Micromonospora sp. RV43, taxon 1661387, as
      SOURCE_ASSERTION and NZ_LEKG01000004.1:20144–63730 as CLUSTER_UNSTATED, with
      no locus methods. The separate LOTUS occurrence names Micromonospora cinerea,
      taxon 292802. The selected -2 owner’s Salinispora CNR107 claim is different
      source context and does not replace or strengthen this record’s producer claim.
      Cached labels and synonyms do not bridge named strain and species assertions.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2515-origin-owner
    - bgc-2515-occurrence-owner
    - bgc-2515-source-mibig_compounds
    - bgc-2515-cached-taxonomy
    - bgc-2515-taxonomy-routes
    - bgc-2515-curation-scope
    - bgc-2515-direct-contexts
    - bgc-2515-source-lotus_occurrences
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
  - name: producer_evidence
    value: BGC0001330 version 5 assigns Micromonospora sp. RV43, taxon 1661387, as
      SOURCE_ASSERTION and NZ_LEKG01000004.1:20144–63730 as CLUSTER_UNSTATED, with
      no locus methods. The separate LOTUS occurrence names Micromonospora cinerea,
      taxon 292802. The selected -2 owner’s Salinispora CNR107 claim is different
      source context and does not replace or strengthen this record’s producer claim.
      Cached labels and synonyms do not bridge named strain and species assertions.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2515-origin-owner
    - bgc-2515-occurrence-owner
    - bgc-2515-source-mibig_compounds
    - bgc-2515-cached-taxonomy
    - bgc-2515-taxonomy-routes
    - bgc-2515-curation-scope
    - bgc-2515-direct-contexts
    - bgc-2515-source-lotus_occurrences
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
  - name: locus_evidence
    value: BGC0001330 version 5 assigns Micromonospora sp. RV43, taxon 1661387, as
      SOURCE_ASSERTION and NZ_LEKG01000004.1:20144–63730 as CLUSTER_UNSTATED, with
      no locus methods. The separate LOTUS occurrence names Micromonospora cinerea,
      taxon 292802. The selected -2 owner’s Salinispora CNR107 claim is different
      source context and does not replace or strengthen this record’s producer claim.
      Cached labels and synonyms do not bridge named strain and species assertions.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2515-origin-owner
    - bgc-2515-occurrence-owner
    - bgc-2515-source-mibig_compounds
    - bgc-2515-cached-taxonomy
    - bgc-2515-taxonomy-routes
    - bgc-2515-curation-scope
    - bgc-2515-direct-contexts
    - bgc-2515-source-lotus_occurrences
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
- assessment_id: bgc-2515-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: The retained producer/locus citation is MIBiG ENTRY PMID:26637117, and
    the LOTUS occurrence cites DOI:10.1002/ANIE.201509926. Both seeding histories
    were read. The separate -2 A1 and shared-BGC cohort references remain explicitly
    attributed; repeated placements do not establish independent experiments or settle
    OPEN shared-structure questions in other owners.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-owner
  - bgc-2515-history-owner
  - bgc-2515-origin-owner
  - bgc-2515-occurrence-owner
  - bgc-2515-source-mibig_compounds
  - bgc-2515-source-reading
  - bgc-2515-source-lotus_occurrences
  - bgc-2515-source-pubchem_bioassay
  - bgc-2515-companion-boundaries
  - bgc-2515-companion-reading
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: citation_scope
    value: The retained producer/locus citation is MIBiG ENTRY PMID:26637117, and
      the LOTUS occurrence cites DOI:10.1002/ANIE.201509926. Both seeding histories
      were read. The separate -2 A1 and shared-BGC cohort references remain explicitly
      attributed; repeated placements do not establish independent experiments or
      settle OPEN shared-structure questions in other owners.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2515-owner
    - bgc-2515-history-owner
    - bgc-2515-origin-owner
    - bgc-2515-occurrence-owner
    - bgc-2515-source-mibig_compounds
    - bgc-2515-source-reading
    - bgc-2515-source-lotus_occurrences
    - bgc-2515-source-pubchem_bioassay
    - bgc-2515-companion-boundaries
    - bgc-2515-companion-reading
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
- assessment_id: bgc-2515-occurrence
  area: evidence
  topic: Source-specific occurrence and assay boundaries
  outcome: supported
  summary: One Micromonospora cinerea occurrence is retained. PubChem CID9959574 contributes
    only a blank-AID no-assay-data sentinel, with empty activity, endpoint, target
    and reference fields. No BindingDB target, bioactivity root or molecular-target
    root is declared. Direct cohort contexts and unselected C2 provide bounded source
    comparison without activity, stereochemical, producer-grade or review-coverage
    transfer.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-occurrence-owner
  - bgc-2515-mechanism-absence
  - bgc-2515-query-lotus_occurrences
  - bgc-2515-query-chebi_origins
  - bgc-2515-query-cyanometdb_occurrences
  - bgc-2515-query-pubchem_bioassay
  - bgc-2515-query-bindingdb_targets
  - bgc-2515-query-antibioticmech_inchikeys
  - bgc-2515-cached-taxonomy
  - bgc-2515-taxonomy-routes
  - bgc-2515-taxonomy-reading
  - bgc-2515-curation-scope
  - bgc-2515-bioactivity-seeder
  - bgc-2515-source-reading
  - bgc-2515-source-lotus_occurrences
  - bgc-2515-source-pubchem_bioassay
  - bgc-2515-companion-boundaries
  - bgc-2515-companion-reading
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: occurrence_scope
    value: One Micromonospora cinerea occurrence is retained. PubChem CID9959574 contributes
      only a blank-AID no-assay-data sentinel, with empty activity, endpoint, target
      and reference fields. No BindingDB target, bioactivity root or molecular-target
      root is declared. Direct cohort contexts and unselected C2 provide bounded source
      comparison without activity, stereochemical, producer-grade or review-coverage
      transfer.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2515-occurrence-owner
    - bgc-2515-mechanism-absence
    - bgc-2515-query-lotus_occurrences
    - bgc-2515-query-chebi_origins
    - bgc-2515-query-cyanometdb_occurrences
    - bgc-2515-query-pubchem_bioassay
    - bgc-2515-query-bindingdb_targets
    - bgc-2515-query-antibioticmech_inchikeys
    - bgc-2515-cached-taxonomy
    - bgc-2515-taxonomy-routes
    - bgc-2515-taxonomy-reading
    - bgc-2515-curation-scope
    - bgc-2515-bioactivity-seeder
    - bgc-2515-source-reading
    - bgc-2515-source-lotus_occurrences
    - bgc-2515-source-pubchem_bioassay
    - bgc-2515-companion-boundaries
    - bgc-2515-companion-reading
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
  - name: assay_target_scope
    value: CID9959574 is a retained xref and no-data row, not an inactive measurement,
      potency or direct-binding assertion. It belongs to this source route and is
      not automatically authority for the more specified A1 encoding.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2515-occurrence-owner
    - bgc-2515-mechanism-absence
    - bgc-2515-query-lotus_occurrences
    - bgc-2515-query-chebi_origins
    - bgc-2515-query-cyanometdb_occurrences
    - bgc-2515-query-pubchem_bioassay
    - bgc-2515-query-bindingdb_targets
    - bgc-2515-query-antibioticmech_inchikeys
    - bgc-2515-cached-taxonomy
    - bgc-2515-taxonomy-routes
    - bgc-2515-taxonomy-reading
    - bgc-2515-curation-scope
    - bgc-2515-bioactivity-seeder
    - bgc-2515-source-reading
    - bgc-2515-source-lotus_occurrences
    - bgc-2515-source-pubchem_bioassay
    - bgc-2515-companion-boundaries
    - bgc-2515-companion-reading
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
- assessment_id: bgc-2515-classification
  area: consistency
  topic: Reported model families and qualified applicability
  outcome: supported
  summary: The versioned model reports Amino acids and Peptides plus Polyketides,
    Oligopeptides, Cyclic peptides, Depsipeptides and Lipopeptides, with false glycoside.
    The saved 17-membered three-amide/one-ester macrocycle and long alkyl substituent
    are compatible with the structural cyclic depsipeptide/lipopeptide labels. Source
    NRPS/PKS annotations and computed model pathways are distinct from experimentally
    established biosynthetic mechanisms. The complete topology supports the nonglycoside
    interpretation without treating the absence of one ring motif as a universal rule;
    UNCLASSIFIED filing follows multiple model pathway outputs.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-classification-owner
  - bgc-2515-source-npclassifier
  - bgc-2515-chemistry
  - bgc-2515-topology
  - bgc-2515-structure-schema
  - bgc-2515-classification-seeder
  - bgc-2515-source-mibig_compounds
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: classification_applicability
    value: The versioned model reports Amino acids and Peptides plus Polyketides,
      Oligopeptides, Cyclic peptides, Depsipeptides and Lipopeptides, with false glycoside.
      The saved 17-membered three-amide/one-ester macrocycle and long alkyl substituent
      are compatible with the structural cyclic depsipeptide/lipopeptide labels. Source
      NRPS/PKS annotations and computed model pathways are distinct from experimentally
      established biosynthetic mechanisms. The complete topology supports the nonglycoside
      interpretation without treating the absence of one ring motif as a universal
      rule; UNCLASSIFIED filing follows multiple model pathway outputs.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2515-classification-owner
    - bgc-2515-source-npclassifier
    - bgc-2515-chemistry
    - bgc-2515-topology
    - bgc-2515-structure-schema
    - bgc-2515-classification-seeder
    - bgc-2515-source-mibig_compounds
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
- assessment_id: bgc-2515-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: The complete retained owner and history, actual canonical intake, saved
    source frames, cached taxonomy and original molecular diagnostic were reviewed.
    Five documented local gates passed, but full QC and OAK were unavailable; no primary
    literature, fresh taxonomy, authoritative structure service, sequence or assay
    protocol was retrieved. No external requests were made. The review remains partial,
    and this bounded evidence does not support a record-edit finding.
  target_ids:
  - naturalproductmech:mibig-7025b12525
  evidence_ids:
  - bgc-2515-owner
  - bgc-2515-capture
  - bgc-2515-intake
  - bgc-2515-intake-acceptance
  - bgc-2515-history-owner
  - bgc-2515-diagnostic-reading
  - bgc-2515-diagnostic-acceptance
  - bgc-2515-diagnostic-execution
  - bgc-2515-source-reading
  - bgc-2515-joint-source-notes
  - bgc-2515-source-plan-execution
  - bgc-2515-source-plan-acceptance
  - bgc-2515-native-gate-limits
  - bgc-2515-curation-scope
  - bgc-2515-mechanism-absence
  - bgc-2515-companion-boundaries
  - bgc-2515-companion-reading
  - bgc-2515-selected-A1-comparison-owner
  - bgc-2515-selected-A1-comparison-strings
  - bgc-2515-selected-A1-comparison-role
  dimensions:
  - name: review_completion
    value: The complete retained owner and history, actual canonical intake, saved
      source frames, cached taxonomy and original molecular diagnostic were reviewed.
      Five documented local gates passed, but full QC and OAK were unavailable; no
      primary literature, fresh taxonomy, authoritative structure service, sequence
      or assay protocol was retrieved. No external requests were made. The review
      remains partial, and this bounded evidence does not support a record-edit finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2515-owner
    - bgc-2515-capture
    - bgc-2515-intake
    - bgc-2515-intake-acceptance
    - bgc-2515-history-owner
    - bgc-2515-diagnostic-reading
    - bgc-2515-diagnostic-acceptance
    - bgc-2515-diagnostic-execution
    - bgc-2515-source-reading
    - bgc-2515-joint-source-notes
    - bgc-2515-source-plan-execution
    - bgc-2515-source-plan-acceptance
    - bgc-2515-native-gate-limits
    - bgc-2515-curation-scope
    - bgc-2515-mechanism-absence
    - bgc-2515-companion-boundaries
    - bgc-2515-companion-reading
    - bgc-2515-selected-A1-comparison-owner
    - bgc-2515-selected-A1-comparison-strings
    - bgc-2515-selected-A1-comparison-role
findings: []
actions: []
limitations:
- The encoding leaves three tetrahedral centers unspecified and does not establish
  a natural mixture or equivalence with the other A1 owner.
- Two secondary-amide/imidic changes leave the direct atom map empty despite normalized-key
  equality.
- The PubChem row is a blank-AID sentinel, and producer/locus evidence remains source-qualified.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all ten first-five saved molecular forms (406 atom rows and
  406 bond rows) and 201 actual intake placements across 49 paths, without new parsing.
- 'Disjoint source reading: BGC first-five selected plus two companions, 63 frames/27
  rows/331 fields; Support last-five, 45 frames/19 rows/309 fields. Native cache/curation
  receives zero positive-source-row credit.'
- BGC operated original collector/composer; Support operated canonical intakes; Native
  operated the original diagnostic under ROOT delegation. No selected owner requires
  a maintained reader. These fragments consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-252
```
