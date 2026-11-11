# Local evidence review: beauvericin

- Review: 20261105T071609Z-beauvericin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T06:20:07.694242Z
- Finished UTC: 2026-11-05T07:16:09.391332Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Beauvericin retains a stereochemically unspecified cyclic depsipeptide encoding and 22 source assay placements. Stored structural forms agree in the local diagnostic, while the cell-screen calls, untyped numeric source value and nested target annotations remain qualified by their original assay contexts.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2522; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-4c106eac10 | data/natural_products/unclassified/beauvericin.yaml | generated | beauvericin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-4c106eac10 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-4c106eac10 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-4c106eac10 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-4c106eac10 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-4c106eac10 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-4c106eac10 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-4c106eac10 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-4c106eac10 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-4c106eac10.

The MINTED identifier naturalproductmech:mibig-4c106eac10 retains MIBiG BGC0000313 version 4, PubChem CID 3007984, NPA01888 and full key GYSCAQFHASJXRS-UHFFFAOYSA-N. The exact retained ChEBI join is empty; the historical no-match grounding note is not a current global authority search. All six tetrahedral centers in the saved encoding are unspecified. Consequently, the label and source identifiers do not independently identify an experimental stereoisomer or show that the assay material has exactly the same stereochemical scope as the stored record.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-4c106eac10.

The maintained stereo_complete=false is consistent with six unspecified tetrahedral centers. An unspecified encoding is not evidence for a natural mixture or for any particular absolute configuration. The complete atom-count correspondence and equal canonical strings do not remove this stereochemical limitation, and the review does not assign the six global diagnostic warnings to this owner.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-4c106eac10.

MIBiG BGC0000313 version 4 reports Beauveria bassiana, taxon 176275, as SOURCE_ASSERTION, with genome accession EU886196.1 and a CLUSTER_UNSTATED locus without retained coordinates or locus-method values. The 16 LOTUS row placements cover multiple fungal taxa and references; they are occurrence assertions rather than 16 independent demonstrations of production. The retained Paecilomyces tenuipes label at taxon 45847 is distinct from the cached current name Cordyceps tenuipes and its Paecilomyces/Isaria synonyms. That saved name correspondence does not authorize silently changing source labels or upgrading taxonomic or production evidence.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-4c106eac10.

The MIBiG producer and locus cite DOI:10.1016/s0040-4039(01)88668-8 from COMPOUND_BIOACTIVITY scope. LOTUS repeats some taxon/reference combinations and PubChem repeats seven AIDs in rows with and without target accessions, so 22 assay placements represent 15 distinct AIDs rather than 22 independent experiments. The cytotoxic profiling row retains PMID:31498718; the other assay references retain their AIDs and deposited titles. All four seeding events remain historical provenance. Neither repeated placements nor citation titles establish newly inspected primary evidence or direct target inhibition.

### Source-specific occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-4c106eac10.

The retained LOTUS rows remain separate from the MIBiG producer assertion. All 22 written bioactivity placements are retained: 13 ACTIVE, 3 INACTIVE and 6 NOT_DETERMINED, the latter corresponding to deposited Inconclusive outcomes. The associated CYTOTOXIC and ENZYME_INHIBITOR summary labels derive from active assay-title classifications. In particular, NSD2 WT/mutant cell screens and SYKi-naive/resistant cell-viability screens must retain their cellular context; their titles and five nested target_enzyme fields do not independently establish direct inhibition or binding to those proteins. There is no selected causal graph or molecular-target root, and no BindingDB or AntibioticMech positive join.

### Reported model families and qualified applicability

consistency: supported. Targets: naturalproductmech:mibig-4c106eac10.

NPClassifier npclassifier.gnps2.org@2026-09-07 reports Amino acids and Peptides plus Polyketides, Oligopeptides, and Cyclic peptides and Depsipeptides. The 18-membered ring with three ester and three N-methyl amide units supports the structural cyclic-depsipeptide description. The additional Polyketides pathway output remains a reported model prediction, distinct from MIBiG’s NRPS source label and without a newly established biosynthetic pathway. The false glycoside output agrees with the complete non-sugar ring topology. Multiple predicted pathways explain UNCLASSIFIED filing; the model does not establish stereochemistry, production or the mechanism of the assay results.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-4c106eac10.

The complete retained owner and history, actual canonical intake, assigned full source frames, saved taxonomy and original molecular tables were reviewed. Five local gates passed, while full QC and OAK remained unavailable. No primary literature, fresh taxonomy, external structure authority or assay protocol was requested. All first-five owners lack declared causal graphs, pathways, components and molecular-target roots, so no maintained reader applies to them; Beauvericin’s assay observations are preserved separately. This is a partial review. The bounded evidence supports the qualified assessment but does not establish a source-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2522-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/beauvericin.yaml; Complete plaintext including every curation_history entry | supports | Complete beauvericin owner and 4 history events; earlier whole reading carries by current identical bytes. |
| bgc-2522-capture | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2522-intake | /private/tmp/npm-review-work/shared-next-batch253/intakes/2522-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, maintained ownership and all 39 input placements joined to the accepted plan and current hashes. |
| bgc-2522-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch253/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/1 | supports | ROOT accepted this original canonical intake and its exact plan, inspection and receipt pins. |
| bgc-2522-grounding-owner | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/label; /records/1/owner_document/chemical_structure; /records/1/owner_document/xrefs; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status; /records/1/owner_document/grounding_notes | supports | Exact retained identifier, structure, cross-references where present, source concepts and grounding fields. Historical annotations do not constitute a fresh authority lookup. |
| bgc-2522-origin-owner | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups; /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, coordinates where declared and citation tiers. |
| bgc-2522-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete owner supplies retained occurrences, definitions and all bioactivities where present, with their source-specific fields and notes. Missing observations are not biological inactivity. |
| bgc-2522-classification-owner | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing and separate source categories; applicability is assessed separately. |
| bgc-2522-history-owner | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1/owner_document/curation_status; /records/1/owner_document/curation_history | supports | Complete history and status; seeding and historical curation do not imply new primary verification. |
| bgc-2522-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway, components and molecular_targets roots; no maintained reader applies to this owner. Beauvericin bioactivities and their nested target annotations are separately preserved, not treated as root mechanism graphs. |
| bgc-2522-chemistry | /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/formula; /records/1/smiles/computed/formal_charge; /records/1/smiles/computed/standard_inchi; /records/1/smiles/computed/standard_inchi_key; /records/1/smiles/computed/canonical_isomeric_smiles; /records/1/smiles/computed/canonical_nonisomeric_smiles; /records/1/smiles/computed/atom_count; /records/1/smiles/computed/heavy_atom_count; /records/1/smiles/computed/bond_count; /records/1/smiles/computed/element_counts; /records/1/smiles/computed/stereo_counts; /records/1/inchi/computed/formula; /records/1/inchi/computed/formal_charge; /records/1/inchi/computed/standard_inchi; /records/1/inchi/computed/standard_inchi_key; /records/1/inchi/computed/canonical_isomeric_smiles; /records/1/inchi/computed/canonical_nonisomeric_smiles; /records/1/inchi/computed/atom_count; /records/1/inchi/computed/heavy_atom_count; /records/1/inchi/computed/bond_count; /records/1/inchi/computed/element_counts; /records/1/inchi/computed/stereo_counts | supports | Both stored forms parse as neutral C45H57N3O9 with 57 atoms and 60 bonds, and all ten comparisons are true, including canonical isomeric and nonisomeric strings, Standard InChI and the full key. The saved correspondence covers all 57 atoms by the diagnostic’s mapping check, but full_graph_identity_established remains false. This agreement supports the two stored representations within the local method; it does not supply independent natural identity, stereochemical assignment or assay-material verification. |
| bgc-2522-topology | /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds; /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo; /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices; /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings; /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs; /records/1/inchi/computed/fragment_atom_indices | supports | The complete tables show an 18-membered depsipeptide ring and three six-membered phenyl rings. The three ester linkages are C5(=O6)-O4-C3, C21(=O22)-O20-C19 and C37(=O38)-O36-C35. Three tertiary N-methyl amides join C17-N15, C33-N31 and C49-N47; each nitrogen has degree 3 and no attached hydrogen. All six carbonyls are retained in the InChI-derived form. Six potential tetrahedral sites are unspecified: SMILES C3, C7, C19, C23, C35 and C39, corresponding to six unspecified sites C33–C38 in the reconstructed form. No amide-to-imidic shift, saturated C5O cycle, free primary amine or N-acetyl motif is reported. |
| bgc-2522-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-current253-first-five-molecular-intake-reading-001.json; /records/1; /counts; /reading_scope; /intake_reading; /source_reading; /limits | supports | BGC complete saved first-five molecular and intake reading, with exact per-form table counts and reading attribution; no new parse. |
| bgc-2522-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /readback; /original_exit_code; /original_terminal_chunk; /molecular_parse_attempts; /parsed; /comparisons_true; /comparisons_total; /global_warning_count; /external_requests; /method_scope; /interpretation_boundary; /ROOT_result_reading; /verification; /scientific_verdicts | supports | ROOT accepted the original twenty stored-form diagnostics. Global warning interpretation and method limits remain explicit; no per-record warning assignment is inferred. |
| bgc-2522-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins. |
| bgc-2522-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | Structure stereochemistry and named/versioned computed classification have distinct evidence scopes. |
| bgc-2522-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The maintained stereo_complete calculation uses unassigned molecular chiral centers; it is not a count of literal question marks in InChI. Atom type and double-bond geometry require separate interpretation. |
| bgc-2522-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while exact model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2522-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 126–145; 1318–1382 | supports | Deposited calls, endpoints and values retain their source scope. Activity classes derived from active assay titles do not independently prove mechanisms or direct binding. |
| bgc-2522-source-reading | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-current253-assigned-source-reading-001.json; /primary_scope; /contexts; /raw_history_carries; /whole_reading_terminals; /remaining_attribution; /verification | supports | BGC wholly read contexts 2–13: seven unselected BE cohort companions and the selected first five, totaling 108 frames, 82 rows and 963 fields. The selected five account for 56 rows and 567 fields. Companion rows add no selected review coverage or transferred activity; these are retained-source readings, not newly inspected primary publications. |
| bgc-2522-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete retained-source reading covers 171 frames, 110 rows and 1281 fields: BGC 82 rows and Support 28 rows. Native taxonomy/curation has zero positive-source-row credit; secondary peer readings add no disjoint row credit. |
| bgc-2522-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch253/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope | supports | One original composer produced the accepted plan at 391 placements across 59 paths, with exact source notes and attributed reading receipts. This fragment consumes saved results only. |
| bgc-2522-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch253/root-target-input-plan-acceptance-001.json; /status; /accepted; /plan; /execution; /source_placements; /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification; /reading | supports | ROOT accepted the exact 391-placement/59-path source plan and original results; no query or input expansion is inferred. |
| bgc-2522-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch253/root-current253-five-gates-acceptance-001.json; /status; /verification; /all_native_gates_passed; /limits; /execution | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed remains false. Technical checks do not complete scientific verification. |
| bgc-2522-curation-scope | /private/tmp/npm-review-work/shared-next-batch253-tentative/native-prep/native-current253-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | Bounded ignored-inclusive Native applicability review found zero lexical or applicable curation matches and no assay exclusion. Across the complete inventory, 22 Beauvericin assay rows represent 15 distinct full-key/CID/AID tuples, with three blank-AID sentinels on other owners. Untyped source endpoints do not imply absence of numeric source values. |
| bgc-2522-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/8; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/14 | supports | Complete saved cache names and synonyms for this owner’s source IDs; no independent taxonomic rank, strain, occurrence or producer validation. |
| bgc-2522-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/source_taxa; /contexts/10/source_scope_inventory/forward_taxon_merge_matches; /contexts/10/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh taxonomy request. |
| bgc-2522-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch253-tentative/native-prep/native-current253-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /routes; /interpretation | supports | Native read all 23 whole retained stanzas and 19 routes, with no unmatched, forward-merge or nonorganism entry in this exact scope. Source labels, cached names and synonyms do not establish strain equivalence, taxonomic rank or biological production. |
| bgc-2522-direct-contexts | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-target-input-plan-001.json; /records/1/proposed_companion_paths; /records/1/direct_companion_predicates | supports | Exact immediate owned-BGC context inputs; shared locus/citation is not identity, stereochemistry, assay or mechanism transfer. No transitive or name-based expansion. |
| bgc-2522-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2522-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 422–422; row_sha256 6a3308b76116f448b0bb45a8bd657803f9a06d8097c9db0b38958530d4bfdf04 | supports | Exact retained compound/version, structure/key, xrefs, producer/locus grades and citation tiers. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2522-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2522-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 16 row placements, exact predicate/query and all fields. |
| bgc-2522-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 2219–2219; row_sha256 8133eaefba7a3e4c2152c7298e7d2985fe75b5453d7de1ca553197baa9460dea; physical lines 2220–2220; row_sha256 bf0ef12cfe490f712c74bb9d4bd6ae32e07371799a6b1384bf2c19e6b123a44c; physical lines 2221–2221; row_sha256 fca0207de9dea7c474b6c6e83b2cf6df54aa77ba3da8681aecec4aa25e712dd2; physical lines 2222–2222; row_sha256 c573fd2f3a6fe4e6e38d3e7686783ddc4d570ed3dbcd05076bd0759423be4de2; physical lines 2223–2223; row_sha256 e27f1dd3fbd856edb988cae6032d1c139b7e8621b29f3f81a1fab436f360c297; physical lines 2224–2224; row_sha256 2a30eeafa75ef47b09eac51fa7633a43d604bd5b49b1c0d1e31f44d998826e1d; physical lines 2225–2225; row_sha256 9476c63904d2adacca145e25dfeed1bc789500f7f06ad242f1a0d5f5fa7872b4; physical lines 2226–2226; row_sha256 94a9d5d87cf1f4f7e843644a55d08cebbc6772785b750619cac4aed99c484887; physical lines 2227–2227; row_sha256 3b0a8be6900e2cdb0146b7f177eceef035b55f450495d24012ee75c314ab86ec; physical lines 2228–2228; row_sha256 d823c20d5ef7d153d438463bfe1717bf9f82fa74b39a61d44abfc64727abe11d; physical lines 2229–2229; row_sha256 6a8029f465d013aba32124d788caf8d5645013c775496522399b460f2c9790cc; physical lines 2230–2230; row_sha256 8e71b91407fd642a744da7f1d39cb930077ea142d32126361caa8703d1e01d22; physical lines 2231–2231; row_sha256 58595c71ff2a2a9a91cbc3bc60cc7b13634817d56097e122cf1a94b3b9adb86d; physical lines 2232–2232; row_sha256 577a323554b9aa9aa240586947b05f8f590d1c2169d6f5ad6660c35f1004997e; physical lines 2233–2233; row_sha256 a7a4bddc2ce1121af10eec3bcfeae19bb215d332eda8b80fa5369340ec9cc0b8; physical lines 2234–2234; row_sha256 f4d12d930fbcbde7da43650a62aa9e0fc6c85aac8d5e2e32ebf5aab081634ddf | supports | Exact organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2522-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2522-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2522-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 771–771; row_sha256 dc68eeb43bd0f44fe3251a6d6a3df3860f804b7a8d1aa63edd73954cc7a3f6d7 | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability remains separate. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2522-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 22 row placements, exact predicate/query and all fields. |
| bgc-2522-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 1810–1810; row_sha256 78ecd07d2fea9a96b3eeae1c1fcd7ba98b288822baf7cd08b0a796ef1ea06a15; physical lines 1811–1811; row_sha256 437d8ccdae94cc92519eb9297e75d266282e80a446ea85271f3df2b35fe30379; physical lines 1812–1812; row_sha256 2dc45c1f149d5640d1be65a9c1de9cd6b5a1dd757132c878cb96a6cf8e34303d; physical lines 1813–1813; row_sha256 ec7a78665931e43657c6f02311f4f031e45604e56bb2cd998e3a65999f2dd04c; physical lines 1814–1814; row_sha256 426b99ff5eacf9e0623da42ac90c961d78fd87882cfb1136487d976b019fcadd; physical lines 1815–1815; row_sha256 fb72bbdb9d60560cc8209a413e6636af678e0663e53b8d0c26ec2c91a540b121; physical lines 1816–1816; row_sha256 9c20e45c79a216de3608babce7486ee5c4a7bbcdbf4860d02f6673cb06ee637d; physical lines 1817–1817; row_sha256 ef0e9c1877cc722b04ccb1de32c4cd69227ad3a0c230e6f53458bc9fcaf8cf18; physical lines 1818–1818; row_sha256 430a6f44b00559f741109f81f46fc1cdd00663d35694b9b3c2b76c9ce181643b; physical lines 1819–1819; row_sha256 47a0407867f2a1b48deebe49cca682aae32cb66fa1931901cea67ba21d3252ed; physical lines 1820–1820; row_sha256 c45dda10041733eeb840dd80e0ad28650d003f370080722ee1506234309d9d20; physical lines 1821–1821; row_sha256 48a166b4e7d564d4e3ca826568f05d4da6b423bee11fd172702735184e96a061; physical lines 1822–1822; row_sha256 94c2fb9735794a4bfcbe213b2043c54c6945a67f47c8ed10cec001166c230f92; physical lines 1823–1823; row_sha256 56b7176c6c8c82b7e99f0d1746f02b8a24ac3e704829410fac7f5814f3738b48; physical lines 1824–1824; row_sha256 2b196597fd3e72b882178955ccbf14567918f36f158e92b79d4521891cf18361; physical lines 1825–1825; row_sha256 601995b168f4f507d1de2628342b441dfd5d4b1f98e757aa7b1e3c3fafab0531; physical lines 1826–1826; row_sha256 cb32c68f3906554f72f34f3496c64bccbfb90dc16967c715c26fe348180f4ccd; physical lines 1827–1827; row_sha256 632ff4ac06093782530e09c80c61c4aa6a49997e01da52f8b8ea46df9482b71a; physical lines 1828–1828; row_sha256 daea0f9e545553aafc715e42b605f597786369f1de48ad2eef8ee3ab299c4461; physical lines 1829–1829; row_sha256 e34376b55989272de121ed60a6a6f148d0fadbb57254b733a355ad73f92bbefa; physical lines 1830–1830; row_sha256 77c931062185f2df36743b9b03155cb646372bc0da89f26b3e9130a5c477339f; physical lines 1831–1831; row_sha256 84af635d7ce28ea9a7ecc20eb2b4a0d1e6d06ecd8c633a77d84191743e5656af | supports | Exact retained full-key/CID/AID assay rows, deposited calls, endpoint names, numerical fields, titles and target accessions. Repeated placements are not independent experiments; an empty endpoint name does not mean a numeric source value is absent. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2522-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2522-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2522-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 row placements, exact predicate/query and all fields. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-253/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-253/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-253/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-253/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-253/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Six tetrahedral centers are unspecified and assay-material stereochemistry was not independently verified.
- Cell-screen activity classes and nested targets do not establish direct protein inhibition or binding.
- AID 1345084 has a retained numeric source value but no endpoint name; other Potency values are not IC50 or affinity constants.
- Repeated rows, database citation metadata and historical cache labels do not constitute fresh primary or taxonomic verification.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five saved molecular forms (416 atom rows and 428 bond rows) and 198 actual intake placements across 52 paths, without new parsing.
- Disjoint retained-source reading: BGC first-five selected plus seven BE cohort companions, 108 frames/82 rows/963 fields; Support last-five plus two mallei companions, 63 frames/28 rows/318 fields. Native cache/curation receives zero positive-source-row credit.
- BGC operated original collector/composer; Support operated canonical intakes; Native operated the original diagnostic under ROOT delegation. No owner in these first-five fragments requires a maintained reader. The separately selected Bicozamycin reader is outside this fragment scope. These fragments consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T071609Z-beauvericin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: beauvericin'
started_at: '2026-11-05T06:20:07.694242Z'
finished_at: '2026-11-05T07:16:09.391332Z'
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
summary: Beauvericin retains a stereochemically unspecified cyclic depsipeptide encoding
  and 22 source assay placements. Stored structural forms agree in the local diagnostic,
  while the cell-screen calls, untyped numeric source value and nested target annotations
  remain qualified by their original assay contexts.
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
  - path: data/natural_products/unclassified/beauvericin.yaml
    sha256: 0c840bfe607de732a3c6ec84672490e666761e9ed1835034cbff55666087d51b
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
  selection: Campaign path order 2522; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-4c106eac10
targets:
- target_id: naturalproductmech:mibig-4c106eac10
  path: data/natural_products/unclassified/beauvericin.yaml
  label: beauvericin
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
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
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
  - naturalproductmech:mibig-4c106eac10
  command: just validate-strict data/natural_products/unclassified/be-43547c2.yaml
    data/natural_products/unclassified/beauvericin.yaml data/natural_products/unclassified/beauveriolide-i.yaml
    data/natural_products/unclassified/beauveriolide-iii.yaml data/natural_products/unclassified/beauverolide-ba.yaml
    data/natural_products/unclassified/beauverolide-ca.yaml data/natural_products/unclassified/beauverolide-ka.yaml
    data/natural_products/unclassified/bicozamycin.yaml data/natural_products/unclassified/bii-rafflesfungin.yaml
    data/natural_products/unclassified/bis-malleicyprol.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-253/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-4c106eac10
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-253/validate-all-001.tsv
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
  - naturalproductmech:mibig-4c106eac10
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
  - naturalproductmech:mibig-4c106eac10
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
  - naturalproductmech:mibig-4c106eac10
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-253/review-queue-001.tsv
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
  - naturalproductmech:mibig-4c106eac10
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2522-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/beauvericin.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Complete beauvericin owner and 4 history events; earlier whole reading
    carries by current identical bytes.
  snapshot_sha256: 0c840bfe607de732a3c6ec84672490e666761e9ed1835034cbff55666087d51b
- evidence_id: bgc-2522-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/intakes/2522-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Actual canonical target, maintained ownership and all 39 input placements
    joined to the accepted plan and current hashes.
  snapshot_sha256: 0fc1a89069cfff392f48b4593fb42d7da9670f3c00c3d0f710625302c11d3465
- evidence_id: bgc-2522-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/1
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: ROOT accepted this original canonical intake and its exact plan, inspection
    and receipt pins.
  snapshot_sha256: 44060e251527e4e9515ede8842209dbfef98f9c36a745a30be60e59288cd35e5
- evidence_id: bgc-2522-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/label;
    /records/1/owner_document/chemical_structure; /records/1/owner_document/xrefs;
    /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status;
    /records/1/owner_document/grounding_notes
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact retained identifier, structure, cross-references where present, source
    concepts and grounding fields. Historical annotations do not constitute a fresh
    authority lookup.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups;
    /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, coordinates
    where declared and citation tiers.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Complete owner supplies retained occurrences, definitions and all bioactivities
    where present, with their source-specific fields and notes. Missing observations
    are not biological inactivity.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing and separate
    source categories; applicability is assessed separately.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1/owner_document/curation_status; /records/1/owner_document/curation_history
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Complete history and status; seeding and historical curation do not imply
    new primary verification.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Complete owner lacks causal_graphs, causal_graph_refs, biosynthetic_pathway,
    components and molecular_targets roots; no maintained reader applies to this owner.
    Beauvericin bioactivities and their nested target annotations are separately preserved,
    not treated as root mechanism graphs.
  snapshot_sha256: f9d77d0d1c38d5310f131c723ff1bdb0a7542b261c87ce933d2d4e529dbdee46
- evidence_id: bgc-2522-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Both stored forms parse as neutral C45H57N3O9 with 57 atoms and 60 bonds,
    and all ten comparisons are true, including canonical isomeric and nonisomeric
    strings, Standard InChI and the full key. The saved correspondence covers all
    57 atoms by the diagnostic’s mapping check, but full_graph_identity_established
    remains false. This agreement supports the two stored representations within the
    local method; it does not supply independent natural identity, stereochemical
    assignment or assay-material verification.
  snapshot_sha256: f82c3a981b2d6f549faa5196357e19cf22f3e49eeca32f5bd9754523161ceecf
- evidence_id: bgc-2522-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds;
    /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo;
    /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices;
    /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings;
    /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs;
    /records/1/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'The complete tables show an 18-membered depsipeptide ring and three six-membered
    phenyl rings. The three ester linkages are C5(=O6)-O4-C3, C21(=O22)-O20-C19 and
    C37(=O38)-O36-C35. Three tertiary N-methyl amides join C17-N15, C33-N31 and C49-N47;
    each nitrogen has degree 3 and no attached hydrogen. All six carbonyls are retained
    in the InChI-derived form. Six potential tetrahedral sites are unspecified: SMILES
    C3, C7, C19, C23, C35 and C39, corresponding to six unspecified sites C33–C38
    in the reconstructed form. No amide-to-imidic shift, saturated C5O cycle, free
    primary amine or N-acetyl motif is reported.'
  snapshot_sha256: f82c3a981b2d6f549faa5196357e19cf22f3e49eeca32f5bd9754523161ceecf
- evidence_id: bgc-2522-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-current253-first-five-molecular-intake-reading-001.json
  locator: /records/1; /counts; /reading_scope; /intake_reading; /source_reading;
    /limits
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: BGC complete saved first-five molecular and intake reading, with exact
    per-form table counts and reading attribution; no new parse.
  snapshot_sha256: ed4036233e9d65a475d4b1f7d16942bf21af52b1ae8512ba4be15651f8ca5462
- evidence_id: bgc-2522-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /readback; /original_exit_code; /original_terminal_chunk; /molecular_parse_attempts;
    /parsed; /comparisons_true; /comparisons_total; /global_warning_count; /external_requests;
    /method_scope; /interpretation_boundary; /ROOT_result_reading; /verification;
    /scientific_verdicts
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostics. Global warning
    interpretation and method limits remain explicit; no per-record warning assignment
    is inferred.
  snapshot_sha256: 74bae2df6c422a75e3a2251ff96b9671825b2b283a324e2036559251fa903459
- evidence_id: bgc-2522-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins.
  snapshot_sha256: e90651455af90c2f4f367c261abda584f8bada9d9f497896419fed15152e902a
- evidence_id: bgc-2522-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Structure stereochemistry and named/versioned computed classification have
    distinct evidence scopes.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2522-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: The maintained stereo_complete calculation uses unassigned molecular chiral
    centers; it is not a count of literal question marks in InChI. Atom type and double-bond
    geometry require separate interpretation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2522-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while exact model
    arrays remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2522-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 126–145; 1318–1382
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Deposited calls, endpoints and values retain their source scope. Activity
    classes derived from active assay titles do not independently prove mechanisms
    or direct binding.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2522-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-current253-assigned-source-reading-001.json
  locator: /primary_scope; /contexts; /raw_history_carries; /whole_reading_terminals;
    /remaining_attribution; /verification
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'BGC wholly read contexts 2–13: seven unselected BE cohort companions and
    the selected first five, totaling 108 frames, 82 rows and 963 fields. The selected
    five account for 56 rows and 567 fields. Companion rows add no selected review
    coverage or transferred activity; these are retained-source readings, not newly
    inspected primary publications.'
  snapshot_sha256: d261b78f166d89fa3dbcbb8ec3a936fb99e4326d8b94b6d0b70de4121a21a7ba
- evidence_id: bgc-2522-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Disjoint complete retained-source reading covers 171 frames, 110 rows
    and 1281 fields: BGC 82 rows and Support 28 rows. Native taxonomy/curation has
    zero positive-source-row credit; secondary peer readings add no disjoint row credit.'
  snapshot_sha256: ac7a180d944c2f29010494494fca003366ae7bdc7e1c543ee8c961c9bf45da4f
- evidence_id: bgc-2522-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /terminal_chunk; /original_exit_code;
    /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: One original composer produced the accepted plan at 391 placements across
    59 paths, with exact source notes and attributed reading receipts. This fragment
    consumes saved results only.
  snapshot_sha256: eb35682e759f1c9d746c61ced7ffc6693605a9d7ab21fd8f70bf30c963b84f15
- evidence_id: bgc-2522-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/root-target-input-plan-acceptance-001.json
  locator: /status; /accepted; /plan; /execution; /source_placements; /unique_source_paths;
    /original_source_inventory_counts; /per_order_counts; /verification; /reading
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: ROOT accepted the exact 391-placement/59-path source plan and original
    results; no query or input expansion is inferred.
  snapshot_sha256: 5bf1a7ac8990d0a881eeafe4f3aec0aa299de678ee8b781b3f5418fbbb152d5a
- evidence_id: bgc-2522-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253/root-current253-five-gates-acceptance-001.json
  locator: /status; /verification; /all_native_gates_passed; /limits; /execution
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    remains false. Technical checks do not complete scientific verification.
  snapshot_sha256: a735727447d6467e44140365ebf2200e9cec7b5ea30472ead2919db0c5f4afe2
- evidence_id: bgc-2522-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/native-prep/native-current253-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Bounded ignored-inclusive Native applicability review found zero lexical
    or applicable curation matches and no assay exclusion. Across the complete inventory,
    22 Beauvericin assay rows represent 15 distinct full-key/CID/AID tuples, with
    three blank-AID sentinels on other owners. Untyped source endpoints do not imply
    absence of numeric source values.
  snapshot_sha256: 6b2c6ace79bfb8fbb0f722d8f7c7a431b9ca8e065faa57458e691cdcc7ae01c1
  search_scope: Nineteen exact retained contexts across eleven enumerated curation
    TSVs including ignored files; nine eligible tables and 3422 rows, with exact retained
    owner/source/BGC/full-key/assay/occurrence predicates. This is not global absence
    or protocol validation.
- evidence_id: bgc-2522-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/7;
    /cached_taxonomy/whole_stanzas/8; /cached_taxonomy/whole_stanzas/11; /cached_taxonomy/whole_stanzas/14
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source IDs; no
    independent taxonomic rank, strain, occurrence or producer validation.
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
- evidence_id: bgc-2522-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/source_taxa; /contexts/10/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/10/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh
    taxonomy request.
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
- evidence_id: bgc-2522-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/native-prep/native-current253-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /routes; /interpretation
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Native read all 23 whole retained stanzas and 19 routes, with no unmatched,
    forward-merge or nonorganism entry in this exact scope. Source labels, cached
    names and synonyms do not establish strain equivalence, taxonomic rank or biological
    production.
  snapshot_sha256: 2a79d177ff697affc57bd647af4791fdd94dfddfbf4caee0e61d56de8a46e791
- evidence_id: bgc-2522-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-target-input-plan-001.json
  locator: /records/1/proposed_companion_paths; /records/1/direct_companion_predicates
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact immediate owned-BGC context inputs; shared locus/citation is not
    identity, stereochemistry, assay or mechanism transfer. No transitive or name-based
    expansion.
  snapshot_sha256: 2e727499fcd002f904a6efb5c7cc66d09d8fad6cd7dce9bef65f5e31b9ce1c74
- evidence_id: bgc-2522-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 422–422; row_sha256 6a3308b76116f448b0bb45a8bd657803f9a06d8097c9db0b38958530d4bfdf04
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact retained compound/version, structure/key, xrefs, producer/locus grades
    and citation tiers. BGC whole saved-source reading and current physical bytes
    are joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2522-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 16 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 2219–2219; row_sha256 8133eaefba7a3e4c2152c7298e7d2985fe75b5453d7de1ca553197baa9460dea;
    physical lines 2220–2220; row_sha256 bf0ef12cfe490f712c74bb9d4bd6ae32e07371799a6b1384bf2c19e6b123a44c;
    physical lines 2221–2221; row_sha256 fca0207de9dea7c474b6c6e83b2cf6df54aa77ba3da8681aecec4aa25e712dd2;
    physical lines 2222–2222; row_sha256 c573fd2f3a6fe4e6e38d3e7686783ddc4d570ed3dbcd05076bd0759423be4de2;
    physical lines 2223–2223; row_sha256 e27f1dd3fbd856edb988cae6032d1c139b7e8621b29f3f81a1fab436f360c297;
    physical lines 2224–2224; row_sha256 2a30eeafa75ef47b09eac51fa7633a43d604bd5b49b1c0d1e31f44d998826e1d;
    physical lines 2225–2225; row_sha256 9476c63904d2adacca145e25dfeed1bc789500f7f06ad242f1a0d5f5fa7872b4;
    physical lines 2226–2226; row_sha256 94a9d5d87cf1f4f7e843644a55d08cebbc6772785b750619cac4aed99c484887;
    physical lines 2227–2227; row_sha256 3b0a8be6900e2cdb0146b7f177eceef035b55f450495d24012ee75c314ab86ec;
    physical lines 2228–2228; row_sha256 d823c20d5ef7d153d438463bfe1717bf9f82fa74b39a61d44abfc64727abe11d;
    physical lines 2229–2229; row_sha256 6a8029f465d013aba32124d788caf8d5645013c775496522399b460f2c9790cc;
    physical lines 2230–2230; row_sha256 8e71b91407fd642a744da7f1d39cb930077ea142d32126361caa8703d1e01d22;
    physical lines 2231–2231; row_sha256 58595c71ff2a2a9a91cbc3bc60cc7b13634817d56097e122cf1a94b3b9adb86d;
    physical lines 2232–2232; row_sha256 577a323554b9aa9aa240586947b05f8f590d1c2169d6f5ad6660c35f1004997e;
    physical lines 2233–2233; row_sha256 a7a4bddc2ce1121af10eec3bcfeae19bb215d332eda8b80fa5369340ec9cc0b8;
    physical lines 2234–2234; row_sha256 f4d12d930fbcbde7da43650a62aa9e0fc6c85aac8d5e2e32ebf5aab081634ddf
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. BGC whole saved-source
    reading and current physical bytes are joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2522-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: bgc-2522-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 771–771; row_sha256 dc68eeb43bd0f44fe3251a6d6a3df3860f804b7a8d1aa63edd73954cc7a3f6d7
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    remains separate. BGC whole saved-source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2522-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 22 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 1810–1810; row_sha256 78ecd07d2fea9a96b3eeae1c1fcd7ba98b288822baf7cd08b0a796ef1ea06a15;
    physical lines 1811–1811; row_sha256 437d8ccdae94cc92519eb9297e75d266282e80a446ea85271f3df2b35fe30379;
    physical lines 1812–1812; row_sha256 2dc45c1f149d5640d1be65a9c1de9cd6b5a1dd757132c878cb96a6cf8e34303d;
    physical lines 1813–1813; row_sha256 ec7a78665931e43657c6f02311f4f031e45604e56bb2cd998e3a65999f2dd04c;
    physical lines 1814–1814; row_sha256 426b99ff5eacf9e0623da42ac90c961d78fd87882cfb1136487d976b019fcadd;
    physical lines 1815–1815; row_sha256 fb72bbdb9d60560cc8209a413e6636af678e0663e53b8d0c26ec2c91a540b121;
    physical lines 1816–1816; row_sha256 9c20e45c79a216de3608babce7486ee5c4a7bbcdbf4860d02f6673cb06ee637d;
    physical lines 1817–1817; row_sha256 ef0e9c1877cc722b04ccb1de32c4cd69227ad3a0c230e6f53458bc9fcaf8cf18;
    physical lines 1818–1818; row_sha256 430a6f44b00559f741109f81f46fc1cdd00663d35694b9b3c2b76c9ce181643b;
    physical lines 1819–1819; row_sha256 47a0407867f2a1b48deebe49cca682aae32cb66fa1931901cea67ba21d3252ed;
    physical lines 1820–1820; row_sha256 c45dda10041733eeb840dd80e0ad28650d003f370080722ee1506234309d9d20;
    physical lines 1821–1821; row_sha256 48a166b4e7d564d4e3ca826568f05d4da6b423bee11fd172702735184e96a061;
    physical lines 1822–1822; row_sha256 94c2fb9735794a4bfcbe213b2043c54c6945a67f47c8ed10cec001166c230f92;
    physical lines 1823–1823; row_sha256 56b7176c6c8c82b7e99f0d1746f02b8a24ac3e704829410fac7f5814f3738b48;
    physical lines 1824–1824; row_sha256 2b196597fd3e72b882178955ccbf14567918f36f158e92b79d4521891cf18361;
    physical lines 1825–1825; row_sha256 601995b168f4f507d1de2628342b441dfd5d4b1f98e757aa7b1e3c3fafab0531;
    physical lines 1826–1826; row_sha256 cb32c68f3906554f72f34f3496c64bccbfb90dc16967c715c26fe348180f4ccd;
    physical lines 1827–1827; row_sha256 632ff4ac06093782530e09c80c61c4aa6a49997e01da52f8b8ea46df9482b71a;
    physical lines 1828–1828; row_sha256 daea0f9e545553aafc715e42b605f597786369f1de48ad2eef8ee3ab299c4461;
    physical lines 1829–1829; row_sha256 e34376b55989272de121ed60a6a6f148d0fadbb57254b733a355ad73f92bbefa;
    physical lines 1830–1830; row_sha256 77c931062185f2df36743b9b03155cb646372bc0da89f26b3e9130a5c477339f;
    physical lines 1831–1831; row_sha256 84af635d7ce28ea9a7ecc20eb2b4a0d1e6d06ecd8c633a77d84191743e5656af
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: Exact retained full-key/CID/AID assay rows, deposited calls, endpoint names,
    numerical fields, titles and target accessions. Repeated placements are not independent
    experiments; an empty endpoint name does not mean a numeric source value is absent.
    BGC whole saved-source reading and current physical bytes are joined.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2522-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 row placements, exact
    predicate/query and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "GYSCAQFHASJXRS-UHFFFAOYSA-N". Complete
    matched payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2522-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch253-tentative/bgc-prep/bgc-conditional253-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T07:06:32.953612Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 0c3a6c4e2f7caf8870e953effb2821d44b8a19dba44bb357c2a4534cc1342d24
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-253/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json
  accessed_at: '2026-11-05T06:27:02.849151Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 46cb08f982c93bba72097f39db75d5069b591b82c6d077be0d14ba465c027379
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-253/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json
  accessed_at: '2026-11-05T06:27:28.614687Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: f46b9d063dfe84b6f9c999d240dd8fca46a98b462ff83992528b451d8914fafb
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-253/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json
  accessed_at: '2026-11-05T06:27:48.271430Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-253/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json
  accessed_at: '2026-11-05T06:28:22.768847Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-253/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-253/native-current253-five-gates-execution-001.json
  accessed_at: '2026-11-05T06:28:34.515014Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 7ce8a3ca06e25c7154714db8f8d22f619791d956b49fe0ecc17973aa6b71c157
assessments:
- assessment_id: bgc-2522-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: The MINTED identifier naturalproductmech:mibig-4c106eac10 retains MIBiG
    BGC0000313 version 4, PubChem CID 3007984, NPA01888 and full key GYSCAQFHASJXRS-UHFFFAOYSA-N.
    The exact retained ChEBI join is empty; the historical no-match grounding note
    is not a current global authority search. All six tetrahedral centers in the saved
    encoding are unspecified. Consequently, the label and source identifiers do not
    independently identify an experimental stereoisomer or show that the assay material
    has exactly the same stereochemical scope as the stored record.
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-grounding-owner
  - bgc-2522-chemistry
  - bgc-2522-source-mibig_compounds
  - bgc-2522-query-chebi_structures
  - bgc-2522-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: GYSCAQFHASJXRS-UHFFFAOYSA-N; retained key, not independent natural-identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2522-grounding-owner
    - bgc-2522-chemistry
    - bgc-2522-source-mibig_compounds
    - bgc-2522-query-chebi_structures
    - bgc-2522-direct-contexts
  - name: grounding_scope
    value: The MINTED identifier naturalproductmech:mibig-4c106eac10 retains MIBiG
      BGC0000313 version 4, PubChem CID 3007984, NPA01888 and full key GYSCAQFHASJXRS-UHFFFAOYSA-N.
      The exact retained ChEBI join is empty; the historical no-match grounding note
      is not a current global authority search. All six tetrahedral centers in the
      saved encoding are unspecified. Consequently, the label and source identifiers
      do not independently identify an experimental stereoisomer or show that the
      assay material has exactly the same stereochemical scope as the stored record.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2522-grounding-owner
    - bgc-2522-chemistry
    - bgc-2522-source-mibig_compounds
    - bgc-2522-query-chebi_structures
    - bgc-2522-direct-contexts
- assessment_id: bgc-2522-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: The maintained stereo_complete=false is consistent with six unspecified
    tetrahedral centers. An unspecified encoding is not evidence for a natural mixture
    or for any particular absolute configuration. The complete atom-count correspondence
    and equal canonical strings do not remove this stereochemical limitation, and
    the review does not assign the six global diagnostic warnings to this owner.
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-grounding-owner
  - bgc-2522-chemistry
  - bgc-2522-topology
  - bgc-2522-diagnostic-reading
  - bgc-2522-diagnostic-acceptance
  - bgc-2522-structure-schema
  - bgc-2522-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: The maintained stereo_complete=false is consistent with six unspecified
      tetrahedral centers. An unspecified encoding is not evidence for a natural mixture
      or for any particular absolute configuration. The complete atom-count correspondence
      and equal canonical strings do not remove this stereochemical limitation, and
      the review does not assign the six global diagnostic warnings to this owner.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2522-grounding-owner
    - bgc-2522-chemistry
    - bgc-2522-topology
    - bgc-2522-diagnostic-reading
    - bgc-2522-diagnostic-acceptance
    - bgc-2522-structure-schema
    - bgc-2522-stereo-method
  - name: representation_correspondence
    value: Both stored forms parse as neutral C45H57N3O9 with 57 atoms and 60 bonds,
      and all ten comparisons are true, including canonical isomeric and nonisomeric
      strings, Standard InChI and the full key. The saved correspondence covers all
      57 atoms by the diagnostic’s mapping check, but full_graph_identity_established
      remains false. This agreement supports the two stored representations within
      the local method; it does not supply independent natural identity, stereochemical
      assignment or assay-material verification.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2522-grounding-owner
    - bgc-2522-chemistry
    - bgc-2522-topology
    - bgc-2522-diagnostic-reading
    - bgc-2522-diagnostic-acceptance
    - bgc-2522-structure-schema
    - bgc-2522-stereo-method
- assessment_id: bgc-2522-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: MIBiG BGC0000313 version 4 reports Beauveria bassiana, taxon 176275, as
    SOURCE_ASSERTION, with genome accession EU886196.1 and a CLUSTER_UNSTATED locus
    without retained coordinates or locus-method values. The 16 LOTUS row placements
    cover multiple fungal taxa and references; they are occurrence assertions rather
    than 16 independent demonstrations of production. The retained Paecilomyces tenuipes
    label at taxon 45847 is distinct from the cached current name Cordyceps tenuipes
    and its Paecilomyces/Isaria synonyms. That saved name correspondence does not
    authorize silently changing source labels or upgrading taxonomic or production
    evidence.
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-origin-owner
  - bgc-2522-occurrence-owner
  - bgc-2522-source-mibig_compounds
  - bgc-2522-cached-taxonomy
  - bgc-2522-taxonomy-routes
  - bgc-2522-curation-scope
  - bgc-2522-direct-contexts
  - bgc-2522-source-lotus_occurrences
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0000313 version 4 reports Beauveria bassiana, taxon 176275, as
      SOURCE_ASSERTION, with genome accession EU886196.1 and a CLUSTER_UNSTATED locus
      without retained coordinates or locus-method values. The 16 LOTUS row placements
      cover multiple fungal taxa and references; they are occurrence assertions rather
      than 16 independent demonstrations of production. The retained Paecilomyces
      tenuipes label at taxon 45847 is distinct from the cached current name Cordyceps
      tenuipes and its Paecilomyces/Isaria synonyms. That saved name correspondence
      does not authorize silently changing source labels or upgrading taxonomic or
      production evidence.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2522-origin-owner
    - bgc-2522-occurrence-owner
    - bgc-2522-source-mibig_compounds
    - bgc-2522-cached-taxonomy
    - bgc-2522-taxonomy-routes
    - bgc-2522-curation-scope
    - bgc-2522-direct-contexts
    - bgc-2522-source-lotus_occurrences
  - name: producer_evidence
    value: MIBiG BGC0000313 version 4 reports Beauveria bassiana, taxon 176275, as
      SOURCE_ASSERTION, with genome accession EU886196.1 and a CLUSTER_UNSTATED locus
      without retained coordinates or locus-method values. The 16 LOTUS row placements
      cover multiple fungal taxa and references; they are occurrence assertions rather
      than 16 independent demonstrations of production. The retained Paecilomyces
      tenuipes label at taxon 45847 is distinct from the cached current name Cordyceps
      tenuipes and its Paecilomyces/Isaria synonyms. That saved name correspondence
      does not authorize silently changing source labels or upgrading taxonomic or
      production evidence.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2522-origin-owner
    - bgc-2522-occurrence-owner
    - bgc-2522-source-mibig_compounds
    - bgc-2522-cached-taxonomy
    - bgc-2522-taxonomy-routes
    - bgc-2522-curation-scope
    - bgc-2522-direct-contexts
    - bgc-2522-source-lotus_occurrences
  - name: locus_evidence
    value: MIBiG BGC0000313 version 4 reports Beauveria bassiana, taxon 176275, as
      SOURCE_ASSERTION, with genome accession EU886196.1 and a CLUSTER_UNSTATED locus
      without retained coordinates or locus-method values. The 16 LOTUS row placements
      cover multiple fungal taxa and references; they are occurrence assertions rather
      than 16 independent demonstrations of production. The retained Paecilomyces
      tenuipes label at taxon 45847 is distinct from the cached current name Cordyceps
      tenuipes and its Paecilomyces/Isaria synonyms. That saved name correspondence
      does not authorize silently changing source labels or upgrading taxonomic or
      production evidence.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2522-origin-owner
    - bgc-2522-occurrence-owner
    - bgc-2522-source-mibig_compounds
    - bgc-2522-cached-taxonomy
    - bgc-2522-taxonomy-routes
    - bgc-2522-curation-scope
    - bgc-2522-direct-contexts
    - bgc-2522-source-lotus_occurrences
- assessment_id: bgc-2522-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: The MIBiG producer and locus cite DOI:10.1016/s0040-4039(01)88668-8 from
    COMPOUND_BIOACTIVITY scope. LOTUS repeats some taxon/reference combinations and
    PubChem repeats seven AIDs in rows with and without target accessions, so 22 assay
    placements represent 15 distinct AIDs rather than 22 independent experiments.
    The cytotoxic profiling row retains PMID:31498718; the other assay references
    retain their AIDs and deposited titles. All four seeding events remain historical
    provenance. Neither repeated placements nor citation titles establish newly inspected
    primary evidence or direct target inhibition.
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-owner
  - bgc-2522-history-owner
  - bgc-2522-origin-owner
  - bgc-2522-occurrence-owner
  - bgc-2522-source-mibig_compounds
  - bgc-2522-source-reading
  - bgc-2522-source-lotus_occurrences
  - bgc-2522-source-pubchem_bioassay
  dimensions:
  - name: citation_scope
    value: The MIBiG producer and locus cite DOI:10.1016/s0040-4039(01)88668-8 from
      COMPOUND_BIOACTIVITY scope. LOTUS repeats some taxon/reference combinations
      and PubChem repeats seven AIDs in rows with and without target accessions, so
      22 assay placements represent 15 distinct AIDs rather than 22 independent experiments.
      The cytotoxic profiling row retains PMID:31498718; the other assay references
      retain their AIDs and deposited titles. All four seeding events remain historical
      provenance. Neither repeated placements nor citation titles establish newly
      inspected primary evidence or direct target inhibition.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2522-owner
    - bgc-2522-history-owner
    - bgc-2522-origin-owner
    - bgc-2522-occurrence-owner
    - bgc-2522-source-mibig_compounds
    - bgc-2522-source-reading
    - bgc-2522-source-lotus_occurrences
    - bgc-2522-source-pubchem_bioassay
- assessment_id: bgc-2522-occurrence
  area: evidence
  topic: Source-specific occurrence and assay boundaries
  outcome: supported
  summary: 'The retained LOTUS rows remain separate from the MIBiG producer assertion.
    All 22 written bioactivity placements are retained: 13 ACTIVE, 3 INACTIVE and
    6 NOT_DETERMINED, the latter corresponding to deposited Inconclusive outcomes.
    The associated CYTOTOXIC and ENZYME_INHIBITOR summary labels derive from active
    assay-title classifications. In particular, NSD2 WT/mutant cell screens and SYKi-naive/resistant
    cell-viability screens must retain their cellular context; their titles and five
    nested target_enzyme fields do not independently establish direct inhibition or
    binding to those proteins. There is no selected causal graph or molecular-target
    root, and no BindingDB or AntibioticMech positive join.'
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-occurrence-owner
  - bgc-2522-mechanism-absence
  - bgc-2522-query-lotus_occurrences
  - bgc-2522-query-chebi_origins
  - bgc-2522-query-cyanometdb_occurrences
  - bgc-2522-query-pubchem_bioassay
  - bgc-2522-query-bindingdb_targets
  - bgc-2522-query-antibioticmech_inchikeys
  - bgc-2522-cached-taxonomy
  - bgc-2522-taxonomy-routes
  - bgc-2522-taxonomy-reading
  - bgc-2522-curation-scope
  - bgc-2522-bioactivity-seeder
  - bgc-2522-source-reading
  - bgc-2522-source-lotus_occurrences
  - bgc-2522-source-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    value: 'The retained LOTUS rows remain separate from the MIBiG producer assertion.
      All 22 written bioactivity placements are retained: 13 ACTIVE, 3 INACTIVE and
      6 NOT_DETERMINED, the latter corresponding to deposited Inconclusive outcomes.
      The associated CYTOTOXIC and ENZYME_INHIBITOR summary labels derive from active
      assay-title classifications. In particular, NSD2 WT/mutant cell screens and
      SYKi-naive/resistant cell-viability screens must retain their cellular context;
      their titles and five nested target_enzyme fields do not independently establish
      direct inhibition or binding to those proteins. There is no selected causal
      graph or molecular-target root, and no BindingDB or AntibioticMech positive
      join.'
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2522-occurrence-owner
    - bgc-2522-mechanism-absence
    - bgc-2522-query-lotus_occurrences
    - bgc-2522-query-chebi_origins
    - bgc-2522-query-cyanometdb_occurrences
    - bgc-2522-query-pubchem_bioassay
    - bgc-2522-query-bindingdb_targets
    - bgc-2522-query-antibioticmech_inchikeys
    - bgc-2522-cached-taxonomy
    - bgc-2522-taxonomy-routes
    - bgc-2522-taxonomy-reading
    - bgc-2522-curation-scope
    - bgc-2522-bioactivity-seeder
    - bgc-2522-source-reading
    - bgc-2522-source-lotus_occurrences
    - bgc-2522-source-pubchem_bioassay
  - name: assay_target_scope
    value: Potency values remain OTHER measurements in µM rather than IC50 or affinity
      constants. The raw AID 1345084 row has numeric activity_value_um=7.9433 but
      an empty activity_name; the inspected seeder writes a typed measurement only
      when both fields are nonempty, so its generated observation retains the active
      call without that numeric measurement. The source number is therefore acknowledged
      without inventing an endpoint. Other retained examples include NSD2 mutant/WT
      values 6.8169/4.826 µM, SYKi-naive/resistant viability values 3.8524/5.4417
      µM, and P-glycoprotein substrate-screen value 4.8499 µM. Inactive thiol-artifact
      and CAR HepG2 calls and inconclusive GPX1, redox, SNCA viability and delta133p53alpha
      screens are not converted into positive mechanisms. P07203, O96028 and P43405
      remain assay target annotations; non-UniProt accessions NP_001119587 and ADZ17385
      remain explicitly ungrounded in their source notes. No assay protocol or target-causality
      experiment was newly checked.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2522-occurrence-owner
    - bgc-2522-mechanism-absence
    - bgc-2522-query-lotus_occurrences
    - bgc-2522-query-chebi_origins
    - bgc-2522-query-cyanometdb_occurrences
    - bgc-2522-query-pubchem_bioassay
    - bgc-2522-query-bindingdb_targets
    - bgc-2522-query-antibioticmech_inchikeys
    - bgc-2522-cached-taxonomy
    - bgc-2522-taxonomy-routes
    - bgc-2522-taxonomy-reading
    - bgc-2522-curation-scope
    - bgc-2522-bioactivity-seeder
    - bgc-2522-source-reading
    - bgc-2522-source-lotus_occurrences
    - bgc-2522-source-pubchem_bioassay
- assessment_id: bgc-2522-classification
  area: consistency
  topic: Reported model families and qualified applicability
  outcome: supported
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 reports Amino acids and
    Peptides plus Polyketides, Oligopeptides, and Cyclic peptides and Depsipeptides.
    The 18-membered ring with three ester and three N-methyl amide units supports
    the structural cyclic-depsipeptide description. The additional Polyketides pathway
    output remains a reported model prediction, distinct from MIBiG’s NRPS source
    label and without a newly established biosynthetic pathway. The false glycoside
    output agrees with the complete non-sugar ring topology. Multiple predicted pathways
    explain UNCLASSIFIED filing; the model does not establish stereochemistry, production
    or the mechanism of the assay results.
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-classification-owner
  - bgc-2522-source-npclassifier
  - bgc-2522-chemistry
  - bgc-2522-topology
  - bgc-2522-structure-schema
  - bgc-2522-classification-seeder
  - bgc-2522-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 reports Amino acids and
      Peptides plus Polyketides, Oligopeptides, and Cyclic peptides and Depsipeptides.
      The 18-membered ring with three ester and three N-methyl amide units supports
      the structural cyclic-depsipeptide description. The additional Polyketides pathway
      output remains a reported model prediction, distinct from MIBiG’s NRPS source
      label and without a newly established biosynthetic pathway. The false glycoside
      output agrees with the complete non-sugar ring topology. Multiple predicted
      pathways explain UNCLASSIFIED filing; the model does not establish stereochemistry,
      production or the mechanism of the assay results.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2522-classification-owner
    - bgc-2522-source-npclassifier
    - bgc-2522-chemistry
    - bgc-2522-topology
    - bgc-2522-structure-schema
    - bgc-2522-classification-seeder
    - bgc-2522-source-mibig_compounds
- assessment_id: bgc-2522-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: The complete retained owner and history, actual canonical intake, assigned
    full source frames, saved taxonomy and original molecular tables were reviewed.
    Five local gates passed, while full QC and OAK remained unavailable. No primary
    literature, fresh taxonomy, external structure authority or assay protocol was
    requested. All first-five owners lack declared causal graphs, pathways, components
    and molecular-target roots, so no maintained reader applies to them; Beauvericin’s
    assay observations are preserved separately. This is a partial review. The bounded
    evidence supports the qualified assessment but does not establish a source-edit
    finding.
  target_ids:
  - naturalproductmech:mibig-4c106eac10
  evidence_ids:
  - bgc-2522-owner
  - bgc-2522-capture
  - bgc-2522-intake
  - bgc-2522-intake-acceptance
  - bgc-2522-history-owner
  - bgc-2522-diagnostic-reading
  - bgc-2522-diagnostic-acceptance
  - bgc-2522-diagnostic-execution
  - bgc-2522-source-reading
  - bgc-2522-joint-source-notes
  - bgc-2522-source-plan-execution
  - bgc-2522-source-plan-acceptance
  - bgc-2522-native-gate-limits
  - bgc-2522-curation-scope
  - bgc-2522-mechanism-absence
  dimensions:
  - name: review_completion
    value: The complete retained owner and history, actual canonical intake, assigned
      full source frames, saved taxonomy and original molecular tables were reviewed.
      Five local gates passed, while full QC and OAK remained unavailable. No primary
      literature, fresh taxonomy, external structure authority or assay protocol was
      requested. All first-five owners lack declared causal graphs, pathways, components
      and molecular-target roots, so no maintained reader applies to them; Beauvericin’s
      assay observations are preserved separately. This is a partial review. The bounded
      evidence supports the qualified assessment but does not establish a source-edit
      finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2522-owner
    - bgc-2522-capture
    - bgc-2522-intake
    - bgc-2522-intake-acceptance
    - bgc-2522-history-owner
    - bgc-2522-diagnostic-reading
    - bgc-2522-diagnostic-acceptance
    - bgc-2522-diagnostic-execution
    - bgc-2522-source-reading
    - bgc-2522-joint-source-notes
    - bgc-2522-source-plan-execution
    - bgc-2522-source-plan-acceptance
    - bgc-2522-native-gate-limits
    - bgc-2522-curation-scope
    - bgc-2522-mechanism-absence
findings: []
actions: []
limitations:
- Six tetrahedral centers are unspecified and assay-material stereochemistry was not
  independently verified.
- Cell-screen activity classes and nested targets do not establish direct protein
  inhibition or binding.
- AID 1345084 has a retained numeric source value but no endpoint name; other Potency
  values are not IC50 or affinity constants.
- Repeated rows, database citation metadata and historical cache labels do not constitute
  fresh primary or taxonomic verification.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all ten first-five saved molecular forms (416 atom rows and
  428 bond rows) and 198 actual intake placements across 52 paths, without new parsing.
- 'Disjoint retained-source reading: BGC first-five selected plus seven BE cohort
  companions, 108 frames/82 rows/963 fields; Support last-five plus two mallei companions,
  63 frames/28 rows/318 fields. Native cache/curation receives zero positive-source-row
  credit.'
- BGC operated original collector/composer; Support operated canonical intakes; Native
  operated the original diagnostic under ROOT delegation. No owner in these first-five
  fragments requires a maintained reader. The separately selected Bicozamycin reader
  is outside this fragment scope. These fragments consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-253
```
