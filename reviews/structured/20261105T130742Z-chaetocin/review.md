# Local evidence review: chaetocin

- Review: 20261105T130742Z-chaetocin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T12:18:03.343792Z
- Finished UTC: 2026-11-05T13:07:42.295405Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Chaetocin has internally concordant stored encodings with eight unspecified atom centers. Its retained assay inventory is broader than the 25 written observations and preserves conflicting deposited tissue titles, blank quantitative endpoints and an ungrounded target accession. Producer, locus, model and assay claims remain separately qualified; no source edit is justified by these local results alone.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2551; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-18e3a7edca | data/natural_products/unclassified/chaetocin.yaml | generated | chaetocin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-18e3a7edca | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-18e3a7edca | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-18e3a7edca | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-18e3a7edca | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-18e3a7edca | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-18e3a7edca | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-18e3a7edca | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-18e3a7edca | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-18e3a7edca.

Chaetocin retains the complete key PZPPOCZWRGNKIR-UHFFFAOYSA-N, MIBiG BGC0000321 version 4 and the content-derived record identifier. Both stored forms produce that same standard InChI and key, and the saved full-key source query returns the retained CID 161591 rows. This supports local encoding and provenance correspondence. The record deliberately lacks specified stereochemistry, so neither the CID cross-reference nor the shared name establishes equivalence to a particular naturally isolated stereoisomer. The empty retained exact-key ChEBI query bounds that inventory; the historical grounding note is not a new global ChEBI search.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-18e3a7edca.

Each saved form contains 46 atoms and 55 bonds in one neutral connected component. Both expose eight unspecified tetrahedral centers; the false stereo_complete flag is consistent with the maintained atom-center implementation. The original SMILES centers are 4, 6, 7, 11, 23, 25, 29 and 33. These are internal diagnostic indices, not biochemical atom numbering. No stereochemical assignment, mixture composition or natural configuration was inferred.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-18e3a7edca.

The retained MIBiG row names Collariella virescens, NCBITaxon:1934374, with SOURCE_ASSERTION producer evidence and a separately graded CLUSTER_UNSTATED locus. BGC0000321 is version 4, active with questionable quality and unknown completeness; KF496217.1 and the NRPS category remain source assertions without freshly inspected sequence or experiments. The retained OBO stanza for the same ID names Achaetomiella virescens and lists Collariella virescens as a synonym. This is a saved label relationship, not a newly verified taxonomic rank, lineage or reassignment. No first-five forward-merge or non-organism match is present.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-18e3a7edca.

The locus/producer reference DOI:10.1002/hlca.19700530521 is stored with COMPOUND_BIOACTIVITY reference_basis. Its repetition does not independently establish a gene-cluster or producer experiment. The two written IUPHAR-DB observations share AID 1346062 and target accession NP_001269095 but cite PMID:16408017 and PMID:23416387 separately; these are two retained reference placements for one assay identity. All three history entries record seeding. No original paper, sequence or live authority was newly inspected, and no historical access is inherited as current primary-source verification.

### Source-specific occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-18e3a7edca.

The complete owner contains 25 written ACTIVE bioactivity placements, representing 24 AIDs, and a derived CYTOTOXIC summary. The saved full-key PubChem frame contains 118 physical Active rows and 117 distinct full-key/CID/AID tuples: 57 Confirmatory, 59 Screening and two Other rows. The other exact-key occurrence/target inventories are empty in this bounded search. Written truncation and the historical note about 93 additional results do not make the omitted rows independent assays or create new written claims. No graph, pathway, root molecular-target or component applies, so no maintained-reader check is required.

### Reported model families and qualified applicability

consistency: supported. Targets: naturalproductmech:mibig-18e3a7edca.

NPClassifier version npclassifier.gnps2.org@2026-09-07 reports Alkaloids and Amino acids and Peptides, Peptide alkaloids and Indole diketopiperazine alkaloids (L-Trp, L-Ala), with is_glycoside false. The nitrogen-rich paired diketopiperazine/indoline topology and absence of a candidate sugar ring support broad structural compatibility. The named L-residue precursor interpretation and natural stereochemistry are not established by this unspecified stored form. The two model pathways explain UNCLASSIFIED filing under the maintained seeder; the model, source NRPS label and experimental biosynthesis remain separate evidence categories.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-18e3a7edca.

All owner fields and three histories, all 42 actual canonical input placements, the complete saved molecular pair, 118 assay rows and the remaining retained source frames were read. The operative intake captures both taxonomy-query tables and all three curation/implementation diagnostics; the original collector/composer/notes remain historical 410/50 scope. Review completion is partial because full QC, complete ontology authority coverage, fresh external verification and natural stereochemical identity are unavailable. No record edit, new exclusion, native promotion or unsupported finding follows from the retained evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2551-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/chaetocin.yaml; Complete plaintext including every curation_history entry | supports | Complete chaetocin owner and all 3 history events, carried from actual whole reading by identical current bytes. |
| bgc-2551-capture | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0 | supports | Complete actual owner capture and its metadata; preservation is distinct from independent scientific validation. |
| bgc-2551-intake | /private/tmp/npm-review-work/shared-next-batch256/intakes/2551-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, maintained ownership and all 42 input placements joined to the accepted plan and current hashes. |
| bgc-2551-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch256/root-intake-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /source; /source_plan_acceptance; /source_plan; /selection; /capture; /capture_acceptance; /environment; /intake_summary; /original_tools; /intakes; /native_gate_acceptance; /verification; /scope; /passive_observer_recovery; /user_outbound_hold; /external_requests; /retries; /diagnostic_result; /maintained_reader_results; /scientific_verdicts | supports | ROOT accepted the original ten canonical intakes at 426 placements across 51 paths, including the planned taxonomy-query inputs. This owner is assessed only after its actual inspection. |
| bgc-2551-grounding-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/grounding_notes | supports | Exact retained identifier, full structure key, source concepts and grounding fields, including cross-references where present. No fresh authority lookup or natural-identity verification is inferred. |
| bgc-2551-origin-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, coordinates and citation tiers as declared. Different evidence grades are not transferred between claims. |
| bgc-2551-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete owner supplies retained occurrence assertions and every written bioactivity where present. An absent observation is not biological inactivity. |
| bgc-2551-classification-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | Exact named/versioned model arrays, glycoside flag, filing and separate source BGC categories; scientific applicability is assessed independently. |
| bgc-2551-history-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0/owner_document/curation_status; /records/0/owner_document/curation_history | supports | Complete owner history and status. Historical seeding and curation do not supply fresh primary-publication access. |
| bgc-2551-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/0/owner_document | supports | The complete owner has no declared graph, graph-reference, component, biosynthetic-pathway or root molecular-target field. No maintained reader applies. Its 25 written bioactivities remain present and require their own assay-context interpretation. |
| bgc-2551-chemistry | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge; /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key; /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles; /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count; /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge; /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key; /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles; /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count; /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts; /records/0/inchi/computed/stereo_counts | supports | All ten saved comparison flags are true, including formula C30H28N6O6S4, zero charge, standard InChI, complete key and both canonical SMILES strings. One chirality-aware match covers all 46 atoms. The diagnostic nevertheless explicitly leaves independent full-graph identity unestablished; a match between two stored encodings does not establish experimental natural identity. The four warnings belong to the original whole-batch stderr and cannot be assigned to this owner. |
| bgc-2551-topology | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs; /records/0/inchi/computed/fragment_atom_indices | supports | The complete saved tables contain four amide carbonyls and two six-member nitrogen diketopiperazine rings, with two sulfur-sulfur bridges joining substituted ring carbons. Two indoline-like fused halves are joined by a carbon-carbon bond, and two hydroxymethyl substituents remain. No ester, phosphorus or candidate saturated C5O sugar cycle is present. These are observations of the stored graph, not a deduction of an enzymatic sulfur-insertion mechanism, precursor origin or absolute configuration. |
| bgc-2551-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-current256-first-five-molecular-intake-reading-001.json; /records/0; /counts; /reading_scope; /intake_reading; /source_reading; /limits | supports | BGC completely read all first-five saved molecular tables and the corresponding actual intake fields: 352 atom rows, 396 bond rows and 216 input placements. No new parse was performed. |
| bgc-2551-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /readback; /independent_peer; /last_five_reading; /intake_acceptance; /verification; /whole_molecular_reading; /scope; /ROOT_reading; /actual_operator; /external_requests | supports | ROOT accepted the original twenty stored-form diagnostics, with 88 of 100 comparison flags true and four global undefined-stereochemistry warnings preserved. Warnings are not attributed to individual owners. Full-graph identity remains unestablished by this method for every owner, without an automatic defect inference. |
| bgc-2551-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, clocks, zero exit and source/stream pins. The original stderr retains four warning blocks; no alternate parse was used. |
| bgc-2551-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–433 | supports | The schema distinguishes structure stereochemistry from named/versioned computed classification and its evidence scope. |
| bgc-2551-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The maintained stereo_complete calculation checks unassigned molecular chiral centers. It does not count all literal InChI question marks or assert complete double-bond geometry. |
| bgc-2551-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Zero or multiple model pathways produce UNCLASSIFIED filing while exact model arrays remain retained; filing does not decide model applicability. |
| bgc-2551-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 126–145; 1318–1382 | supports | The seeder retains deposited activity calls, adds numerical measurements only with both a name and value, grounds only recognized protein identifiers and caps written activities. Title-derived activity classes are not independent target or mechanism evidence. |
| bgc-2551-source-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-current256-assigned-source-reading-001.json; /contexts; /counts; /reading_terminals; /whole_owner_reading; /finite_verification; /cautions; /assay_scope; /search_scope; /attribution | supports | BGC wholly read the five selected contexts: 45 query frames, 136 retained physical row placements and all 1506 fields. These include 118 assay row placements representing 117 distinct full-key/CID/AID tuples, with no blank AID or merge row in this partition. Credit is retained database-row reading, not new primary-publication inspection. |
| bgc-2551-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries; /required_input_supplement | supports | The notes preserve original inventory/composer scope of 410 placements across 50 paths and disjoint readings of 159 rows/1754 fields: BGC 136, Support 23 and Native zero positive rows. Four taxonomy merge rows are separate. The notes record the then-pending taxonomy-input supplement; current operative intake authority is cited separately. |
| bgc-2551-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch256/bgc-source-plan-execution-001.json; /observer; /delegated_by; /recorded_at; /status; /source; /installation; /binding_handoff; /binding_peer; /original_tools; /arguments; /terminal_chunk_id; /exit_code; /original_objects; /empty_objects; /live_handle; /complete_original_output; /inventory; /notes; /plan; /derivation; /actual_invocations; /retries; /readback; /required_taxonomy_supplement; /external_requests; /source_query_replays; /scientific_verdicts | supports | One original composer produced the immutable 410-placement/50-path plan. This execution receipt does not itself establish the later supplemented input scope. |
| bgc-2551-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch256/root-source-plan-acceptance-001.json; /observer; /recorded_at; /accepted; /status; /plan; /original_plan; /independent_peer; /supplement_handoff; /inventory; /inventory_acceptance; /source_reading_acceptance; /notes; /original_composer_execution; /original_composer_tools; /verification; /scope; /canonical_intakes; /diagnostic; /scientific_verdicts; /external_requests | supports | ROOT accepted the operative 426-placement/51-path plan. Six missing merged-taxon placements and ten nonorganism-table placements were added without another collector query or additional positive-row/AID credit. Original 410/50 provenance is preserved. |
| bgc-2551-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch256/root-current256-five-gates-acceptance-001.json; /status; /verification; /unavailable_required_gates; /execution | supports | Five documented local commands passed. Full QC and OAK remain unavailable, with all_native_gates_passed false. Selected queue leads are not scientific findings and local success does not complete the review. |
| bgc-2551-curation-scope | /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation; /implementation_pins | supports | The bounded retained curation scan found 100 lexical matches but zero exact applicable corrections or exclusions. Its 118 actual assay row placements resolve 117 distinct full-key/CID/AID tuples; two blank sentinels belong to other selected owners. The exact exclusion table and implementation were inspected without applying an exclusion. This receipt retains its original input scope and author-time pending plan status. |
| bgc-2551-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/15 | supports | Complete retained cache stanzas for this owner’s source IDs provide names, identifiers and synonyms only. They do not verify rank, lineage, strain equivalence, occurrence or production. |
| bgc-2551-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/source_taxa; /contexts/0/source_scope_inventory/forward_taxon_merge_matches; /contexts/0/source_scope_inventory/nonorganism_matches | supports | This owner’s exact source IDs and saved forwarding/nonorganism results; no fresh taxonomy request or newly verified ancestry. |
| bgc-2551-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /routes; /interpretation; /forward_routes | supports | Native wholly read seventeen cached stanzas and ten context routes. Four historical unmatched IDs elsewhere in the selected set have explicit retained forwarding routes. Names and synonyms do not supply rank or lineage verification, and Native receives zero positive inventory-row credit. |
| bgc-2551-direct-contexts | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-target-input-plan-003.proposed.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | supports | Exact immediate owned-BGC context inputs. Shared loci or citations do not transfer identity, stereochemistry, assays, producer grades or mechanism claims; no transitive or name-based expansion was used. |
| bgc-2551-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 436–436; row_sha256 f362f2715d76dbd2a6de1c0b45ed3711c918242ca8ac2b441868e202eb32a57e | supports | Exact compound/version, retained structure/key, cross-references, separate producer/locus grades and citation tiers. Whole retained-row reading and exact current physical bytes are joined. |
| bgc-2551-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 0 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 0 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 1955–1955; row_sha256 aade694dadfc73dcf712c6dc6feeb26e6aaf2b35fc5612d0c829afe5a898f877 | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability remains separately assessed. Whole retained-row reading and exact current physical bytes are joined. |
| bgc-2551-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 118 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 5428–5428; row_sha256 7f5eb0367ac72639ddf8ebc0de641b42733c656e8169c64216cc7fda906e9f19; physical lines 5429–5429; row_sha256 ffe8c904ae7e9a6eec8916faae802a203732a72c67754066e207325113ba3a59; physical lines 5430–5430; row_sha256 f51a0dea32bda355f6160f708273ad9f7b15e0db67190c64b9a39ef5b07df2c5; physical lines 5431–5431; row_sha256 58f2f2965ee1083564c32c99dd2b51d7152fd83d7b2b5c52b8fa04fead66c28c; physical lines 5432–5432; row_sha256 78f4a8935875a5c8698fb2a20e700ee08176d8c0dd63b98e07770c2eb78dc4e8; physical lines 5433–5433; row_sha256 021a9fc9239ca51be062a5fc50705cdcd0e6f5fd86087202d4321c7146f84fd4; physical lines 5434–5434; row_sha256 bde4d5e1fa5ccf08e4bda94d2f9fe5b45554ae643bef8d5d727776a5c9b436c5; physical lines 5435–5435; row_sha256 48bdbd75ca4f56be80e72c5863e4db0abe7052f9ef04c82b59ae5f882ec4a5c5; physical lines 5436–5436; row_sha256 3302ecf765966dbf1cc04336b9375770ac31a206c419ad6b2ad6c27c04d4e555; physical lines 5437–5437; row_sha256 1812870110782ab391e740b3d5ad85cff65714b96eaa83a76d71f593bc6e6380; physical lines 5438–5438; row_sha256 aa2d1f01a930a1dc6c759c9dc4102fef54ee4faca1ae79d31b6860f00a1be727; physical lines 5439–5439; row_sha256 0e6861550b8b206fb9398fd106d62feebdee13562dfa51e4e9fad78244fbb3fa; physical lines 5440–5440; row_sha256 b2357965cc1549803cb9ca3d607a4609dc1675966cb29684b075d891d9e56254; physical lines 5441–5441; row_sha256 af00d55258e993039c1bfcff3f08d2e25c93afa01131c02ebe8dab8ca63cbc43; physical lines 5442–5442; row_sha256 5dc02c0a017d4f0e6970079f9db9c1c64a8675adc17edff2a25aec2afe13d6b0; physical lines 5443–5443; row_sha256 ef6634495441bc8902e335d6cdbe99c2ae04fb78a82f45193fa3f298effb953b; physical lines 5444–5444; row_sha256 e5a81cb1b6ac4ad729216324b64abf371a9c3ec91b343af3d3e7b2634c331d7c; physical lines 5445–5445; row_sha256 8731fb4d9383e714c65ab0595d14ab177082ae4587689a9c3e5847e3427afabd; physical lines 5446–5446; row_sha256 cfe70d659f81412fc82082880d7f3db026d7fe8b2c2eceddcb7bd94b4fc00a1c; physical lines 5447–5447; row_sha256 9d4efa0c5f1dd78c73d770acbd6fa4b19a5e876c8d4ec6f867801508b0a49375; physical lines 5448–5448; row_sha256 8e918902b42cfe644c11b266d842c8e1eacaf5920a4fefa1a7aa7ee14d60ad3c; physical lines 5449–5449; row_sha256 ffb72326e817ca843b6afcddbb7faad77caa0d51a1f1035925cc113a347be3cd; physical lines 5450–5450; row_sha256 7affd891b49b5a9293fcf8fd05744af863a421fe7ff4e3e7586f846861807c99; physical lines 5451–5451; row_sha256 26593eab033abc67c7de063506f600579b8c193dc91520e2456fc76c1ef1922b; physical lines 5452–5452; row_sha256 28b64c8f08fe7fb848ee741e27efab4947f9ad391fc8a0f58b6fa81d69b09ac7; physical lines 5453–5453; row_sha256 4680a27a580ebd41b34b785f16748656d99d43f80ab763e8a67ac19ac02cb634; physical lines 5454–5454; row_sha256 478677a4ba3bf8abb8637bab7ff1e91d2f94bac46b1771cebae48d4c25ca8524; physical lines 5455–5455; row_sha256 c49af1b1904b7077366011af358213cc332f283f2a36b2ff795c8e2486f1bf2c; physical lines 5456–5456; row_sha256 c17fe761287f704298b48062cb8a1badcf2279858301c78423b619a91ecce0fe; physical lines 5457–5457; row_sha256 58b0d30d991e2883a4c7ffbc06b3db791290fa208ad40a4dc6085f31bbbef2a0; physical lines 5458–5458; row_sha256 c32e34c498635fb28720d41064846e9d11e7091327978aa9192e2b70282244d6; physical lines 5459–5459; row_sha256 71849d93983c6ed79f4b72499faad449bc2d8eafd6193477673a371c97984b76; physical lines 5460–5460; row_sha256 dee4bcc7e17d8f9d8bbdf6d4570f217a52d3c6f4099d1fb8b06f19efdef43f95; physical lines 5461–5461; row_sha256 070626fdfac23a8daf4cd01a22ee790be2951c99662b9970414e0ffaa8ba2dd2; physical lines 5462–5462; row_sha256 24cf62065b9a3f3495b18e0a4ea4251b67daedc103c2c4dacc8b615d87090d14; physical lines 5463–5463; row_sha256 5b8e739765aa51191f378545218e744b1f1485b599a219e8684c8d8eb11e4a87; physical lines 5464–5464; row_sha256 e0514ca3956ef6d2ee7d16c3e6c11627f4eea2548a5bfe938c83517e2f79f87e; physical lines 5465–5465; row_sha256 09e1ce17284d1f9f77c995bf44eb8ae8447b322341192026ae0a9e7b32d85fc9; physical lines 5466–5466; row_sha256 66bfb99a20dc382efe08becb0e0033f67eb91a1f94589094fbbaacb4a4e71aa8; physical lines 5467–5467; row_sha256 741d9fe5740159ca61bf493e4d711ac92b391dad59e34556ebec96cccd84e762; physical lines 5468–5468; row_sha256 d5368105e02207004ebd6baa5ec9ed90a2e448d9a44f68802bcaf66d2f9a945c; physical lines 5469–5469; row_sha256 9a017796f1a2e6d4e560af7d5bb74ca58d15bf066149f03be3754a7df0e6615e; physical lines 5470–5470; row_sha256 4349c031066b73f28b5f83d2237752f2ca3edd9cc1f6ed5861a59d7b0de8e161; physical lines 5471–5471; row_sha256 8acaddfcf5cf1bf7cbfdd6d250b4cd9cbaf9d662054d59ad2453f9020116dd3e; physical lines 5472–5472; row_sha256 ab0d26d544f8dea7b550a550972df09ab66e3ec7487683fabbe749d6660ed563; physical lines 5473–5473; row_sha256 ea8e1f5e0ae4812245014397b9dffb63046b941482a0a9a25e6db5558d8e8ab0; physical lines 5474–5474; row_sha256 a6e4125aa925d9a71a6931743a62a4b07c594148974581ce25fe9dccc643707d; physical lines 5475–5475; row_sha256 cf083a1b04a228bda8ea25e2681d8e240ab22ec3d73a9a05b6fbec29e5f7e84d; physical lines 5476–5476; row_sha256 b11816009cda8c3c5612f69771014311eb4c3f199ae28e0a4a5dbd2f35b8aef3; physical lines 5477–5477; row_sha256 70be311193b45dc44ee51ddbdb2a254c62a0cb2d5cf4ece8cd80835a981b4e84; physical lines 5478–5478; row_sha256 562d1253504645acf32251f30276bf6f5b80309f8b67f097f0fef66c1e2f7132; physical lines 5479–5479; row_sha256 cbbde43ed2f800e64ee56cc41511e5894f5c8f87318e910352421f1a751a3ef5; physical lines 5480–5480; row_sha256 f7dcf4e96224b21092e9d2f911ae9391e91ee2b33c2119ac99938a5b3dff92cd; physical lines 5481–5481; row_sha256 311bc07b7f755ed9189fb6020d8ad6361c8efe8f3a0320169daf7e8028d5bb55; physical lines 5482–5482; row_sha256 e9bfbb71fdb3ec400aaa40f61c429be4c60b778f3c7e8eb46a9cfa7bd13d3279; physical lines 5483–5483; row_sha256 2b24ec13b0cf9a77d2a549117f24d23cfd3e4f9079eb02a55fe5add2e0358cec; physical lines 5484–5484; row_sha256 a5d0f981ed9bf7f1c1840d350030e6107ad89453de6fbd1192ef083f9a71e997; physical lines 5485–5485; row_sha256 0597b9f0076fac829de1704c4bde2b74bcfe3d062cde44326e7c3e917ca3c7ff; physical lines 5486–5486; row_sha256 cb19b99014080a06e2f2315fe78da308c859f8fdd362a1b88e73014ee48930bf; physical lines 5487–5487; row_sha256 fd60c67644b0a04373c3127e8851606467a101c305ed23305bebba9533b8cc4c; physical lines 5488–5488; row_sha256 58860b6a5e7bf9acd4ec2ddd176202cfe09d441dfc24c5946ad16d813e4a53e3; physical lines 5489–5489; row_sha256 27ac515817ea6d31e668bbfc06f21fed9e31c48acccc16b67cbb10ca25ec361a; physical lines 5490–5490; row_sha256 3a21db8a0353ab395f3ab3a8ecbbf53e064dda0ada897f9dd86900b182876cdf; physical lines 5491–5491; row_sha256 ed5d9ab32ffe979e013affd4b151820522808f5bc11cf75d1a82e009c9f2b232; physical lines 5492–5492; row_sha256 6cf13c4573e1893722a1b611077a0a1b9d2d2d0d7389a0174e88531e4e761768; physical lines 5493–5493; row_sha256 4bba8c5ac3456649e4d507c480455ef70921a1a5e2550b80cd9ab84b579ee287; physical lines 5494–5494; row_sha256 b3f7ef0cbace4c1cc1a88bae908e571e24daf06256b96330e64680466f950a17; physical lines 5495–5495; row_sha256 08871b25bf9b80b0f321cddfccf9a00c3b56b9aecd5fc93097ea68602ab720cc; physical lines 5496–5496; row_sha256 b6a45e3d1861a3e0dce618d6af0d3808bd31bf6b51b24c698285555495dc3d86; physical lines 5497–5497; row_sha256 8e29f5c77a79c82c281bcb7c706f4e6485ee84d32bcd0ac025f0192226f5c763; physical lines 5498–5498; row_sha256 8e7910624041b8f6f00bf9bdfa94ddc493281e2533c99b0b332bd0534fb57275; physical lines 5499–5499; row_sha256 c7c9857bc26ed9a34116bf9feb509fe8ffcde95c8d62cea540d4d165b70fba55; physical lines 5500–5500; row_sha256 4f8a59c5404642cd69f932ec9d56fc998832f3b77d56e69db1491f34e1569758; physical lines 5501–5501; row_sha256 847275bcbf98e90fd00f5c8f7aaff740d7bab9a2cf0ae014c1ff5931f6c012d8; physical lines 5502–5502; row_sha256 951c2f4da948fc4acc4610d98552baa45b4394a46d91b900632dee9b2e293a19; physical lines 5503–5503; row_sha256 ac254a4fcae866de9cba515f4bc0d13e251f3513d3f62bda3405b295506c6516; physical lines 5504–5504; row_sha256 f558224628e2672e15aae77bbfbbb3a0a2df3fa41ce96c0a20e3a3ad0e834803; physical lines 5505–5505; row_sha256 1d95a8b64bddbc0ff01f058309600ebcdbd68a52d86c9371b763c5c8ff430187; physical lines 5506–5506; row_sha256 144b7a7862cb8c15048076e576e4aaeec01012ea1fb0828ee1f5a0e51a69e40b; physical lines 5507–5507; row_sha256 48fc69bfc314ba6809f68297dbf124326e808abba4b02bb36063dacb64a4a15b; physical lines 5508–5508; row_sha256 5b363c98cf2f087a32c70598574981d977ee672ea1c91ee6c84cba6e8485ae86; physical lines 5509–5509; row_sha256 3dbe2fba1f99b18c061f03bc9b9633791adafb28e444ea5d522a41bce7565edc; physical lines 5510–5510; row_sha256 d917f5b621a756efb7d0f38c425ac8541e450ebbb5df52b9fb8c2d9b6b4e3df9; physical lines 5511–5511; row_sha256 039863964d7e7ef40c3067eb4cdf3eff6c331732c1145c2df070e96739ca9d8b; physical lines 5512–5512; row_sha256 8654705bff9566d32ecd9c35a1871bd40b7cbda52a3f1c9e6fdfe9df699c4446; physical lines 5513–5513; row_sha256 475fead6571ef57901eae9bf4bf76139ddc674d2e387d616fd17f3303808a0cd; physical lines 5514–5514; row_sha256 2bdd467bd32cd89fbfb1779f4d6ec969c369e9c7c22e376b44f48cc3aa64712f; physical lines 5515–5515; row_sha256 abf81252df88749fe53a9402489e7f099847630ebdb7d40f54b93967df689d60; physical lines 5516–5516; row_sha256 c487b44204ab2b8e9234b00f468e2a2c8e3eed423ee4037e438a06f815986ccf; physical lines 5517–5517; row_sha256 926601a7c593eeccaf3b557dd28baa8558f411d6d1861fc7498bc4ec5c3290fa; physical lines 5518–5518; row_sha256 b5f436cbd6412dcae02bc7b4d1764081a3be6c08a27704dc9edd68f00a1e0eb6; physical lines 5519–5519; row_sha256 e7c89cd28b865f266bd109b42e58091e350d93d83287f08a7b9026f2dd451840; physical lines 5520–5520; row_sha256 ce9f84783992c2182389c570f9f2a3a9a748f5e6fd19339ad7a421f51838980e; physical lines 5521–5521; row_sha256 65c1ceb638f7b81db594158e7e2286f7d0c763fac4bb24f12d5eb04b1d2c4956; physical lines 5522–5522; row_sha256 3f3a8ece2816a444ddbdbdfe939019aae0a381f073db00de54ecc2cf8b185a2e; physical lines 5523–5523; row_sha256 7777d0aecdfd0dceae3f46fb103cffe5d36d87aefcadf19fb6ee4871e5a18230; physical lines 5524–5524; row_sha256 040e7c93570c2e2ce3162f28c826dd94695e06cf5f067c3c4028528b10de87ac; physical lines 5525–5525; row_sha256 3c2e2a3bbc4d6fe0d366d0d699475e2b96687b47975635d9c44d18dc97e8a931; physical lines 5526–5526; row_sha256 90fd0ae949519ed9e87e081a5a585b2ea67a5b978d36f3dddbcc087e271cfe70; physical lines 5527–5527; row_sha256 fb3f84b4b27e8d958e1ae5d4b1aa091a8a31382a39f68fa1cd3321e9022e7b9e; physical lines 5528–5528; row_sha256 ce57c5b12fa6c93026a71216c1ff8e5d08f51b38fad17a9347988383be92799d; physical lines 5529–5529; row_sha256 408eddaed3d5e190d9affc4929c448e188c6ad4005123e75d2492d523a1cc2f0; physical lines 5530–5530; row_sha256 4908b8958f2a28505ce481b231fdb94ee2be917b4c1a3f8f23bb2e5d8c40477e; physical lines 5531–5531; row_sha256 816ed4be89a6bbf40ca5cb0f9f37c6e3a34c2298ea313e25813984550f071d98; physical lines 5532–5532; row_sha256 f8005ec22fd9f4bb0c2f3cf23cbedaaf8a45aa4c1a15114fcfb477d73e6e8008; physical lines 5533–5533; row_sha256 d18362953816d2b671ba79a85aaf93e837b814df6ef5fe35ca81795fc4b02095; physical lines 5534–5534; row_sha256 89da67dad51ec121fb458907c738775a319dc007842f2dcdea085ae2f63bd28c; physical lines 5535–5535; row_sha256 807accd9cefde2a6e7eba3c054ecc8fadf5bcbcc354a176823171b4e6f6a1089; physical lines 5536–5536; row_sha256 4fae227481c851f541487d4b5a0516933bab8f7b6df649e4573d82df2611b24d; physical lines 5537–5537; row_sha256 28c4862ebcb701a4356777a6ff407a6c19b9eb4c3021ba6ac4440b1e43a67c29; physical lines 5538–5538; row_sha256 45e400425f7e80def199fde2e83f191e46cb4799686006a28c67b34c9357b912; physical lines 5539–5539; row_sha256 08ccb2f5413fd092abeaace9aeb01e75a5e1cdfd05ed4546082c6b2cd5cfa93d; physical lines 5540–5540; row_sha256 b0a4467750024a81c54acde0b114a50dee5e7efeec82e6506b7dd3d7b69e30c4; physical lines 5541–5541; row_sha256 2dd807c27e329ca76319fc6d10401afc44777ad1f0f6815dc11b1e49ff8807d8; physical lines 5542–5542; row_sha256 a9275f2cb382638193167a5c8f361bf63955b4047bc613335ca2b7f76b2095a9; physical lines 5543–5543; row_sha256 27b20a2ceab8e3ef83690298dd7988c52f2371596b88781e4da14492fa251ca6; physical lines 5544–5544; row_sha256 58a7a2c730b7c1b722fa146ab5cee26de5c46d75f01c1bd16820ea1010a0c261; physical lines 5545–5545; row_sha256 25b6671ea014ecbf35ea739d2a20e5d74b704e8fd53a0bd5a517385c1e6c78b3 | supports | All 118 exact Chaetocin assay row placements, including both placements of AID1346062 with different references. All deposited calls are Active; endpoint names and numerical values are empty. Screening/Confirmatory/Other titles, conflicting tissue labels and ungrounded target accessions remain literal, without silently normalizing them or inferring direct target inhibition. Whole retained-row reading and exact current physical bytes are joined. |
| bgc-2551-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 retained row placements with the exact predicate, query and all fields. |
| bgc-2551-exclusion-table | /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; Complete retained diagnostic/implementation input; interpretation bounded by the saved owner query and pinned Native receipt | supports | Retained exclusion diagnostic input captured in this actual intake. Native inspected all fifteen rows and found no exact applicable match to the saved assay identity tuples; no exclusion is applied. |
| bgc-2551-exclusion-implementation | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py; Complete retained diagnostic/implementation input; interpretation bounded by the saved owner query and pinned Native receipt | supports | Retained implementation input captured in this actual intake; exact identity/source-attribution guards and provenance preservation do not create an assay or a correction. |
| bgc-2551-unresolved-taxa | /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; Complete retained diagnostic/implementation input; interpretation bounded by the saved owner query and pinned Native receipt | supports | Retained unresolved-taxon diagnostic input captured in this actual intake. Lexical matches are not exact applicable corrections or fresh taxonomy evidence. |
| bgc-2551-taxon-merged-input | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; Complete retained diagnostic/implementation input; interpretation bounded by the saved owner query and pinned Native receipt | supports | The retained merged-taxon table is included in this actual intake to capture the saved query and its negative scope as well as any explicit forwarding result. Capture does not infer a new route. |
| bgc-2551-taxon-nonorganism-input | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv; Complete retained diagnostic/implementation input; interpretation bounded by the saved owner query and pinned Native receipt | supports | The retained nonorganism table is included in this actual intake for the saved query and its negative scope. No nonorganism result or biological conclusion is invented. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-256/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-256/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-256/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-256/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-256/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Eight atom centers remain unspecified; the natural stereoisomer and external CID representations were not independently verified.
- The 118 active retained rows have no numeric endpoint and include unresolved deposited tissue-title conflicts; activity does not establish direct target inhibition.
- Retained taxonomy labels/synonyms and source grades do not establish fresh lineage, producer experiments or a complete biosynthetic pathway.
- Full QC, OAK and external primary/database verification remain unavailable.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five stored molecular forms (352 atom rows and 396 bond rows) and 216 actual intake placements across 46 paths. No new molecular parse was performed.
- Disjoint retained-source reading: BGC first five, 45 frames/136 rows/1506 fields; Support last five, 45 frames/23 rows/248 fields. Four taxonomy merge rows remain separate. Native cache/curation receives zero positive inventory-row credit.
- BGC operated the original collector/composer; Support operated canonical intakes; Native operated the original diagnostic under ROOT delegation. No maintained reader applies to these owners. Historical source access is not inherited as current primary verification.
- The original inventory/composer scope remains 410 placements/50 paths. The accepted taxonomy-query supplement and actual canonical intakes establish the operative 426/51 scope without another source query or extra positive-row/AID credit.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T130742Z-chaetocin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: chaetocin'
started_at: '2026-11-05T12:18:03.343792Z'
finished_at: '2026-11-05T13:07:42.295405Z'
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
summary: Chaetocin has internally concordant stored encodings with eight unspecified
  atom centers. Its retained assay inventory is broader than the 25 written observations
  and preserves conflicting deposited tissue titles, blank quantitative endpoints
  and an ungrounded target accession. Producer, locus, model and assay claims remain
  separately qualified; no source edit is justified by these local results alone.
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
  - path: data/natural_products/unclassified/chaetocin.yaml
    sha256: 7ed72be67fbb9cc624571cda7a24a19b283b845d30d51f2ae974bad161987b0d
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2551; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-18e3a7edca
targets:
- target_id: naturalproductmech:mibig-18e3a7edca
  path: data/natural_products/unclassified/chaetocin.yaml
  label: chaetocin
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
  - repository: CultureBotAI/NaturalProductMech
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Retained taxon-merge query and negative-query diagnostic context for every
      selected owner; exact positive historical routes remain separately attributed.
      Input presence does not assert a merge, fresh taxonomy or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism query and negative-query diagnostic context for every
      selected owner. Input presence does not assert a non-organism classification
      or fresh taxonomy.
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
  - naturalproductmech:mibig-18e3a7edca
  command: just validate-strict data/natural_products/unclassified/chaetocin.yaml
    data/natural_products/unclassified/chaetolivacine-a.yaml data/natural_products/unclassified/chaetolivacine-b.yaml
    data/natural_products/unclassified/chaetolivacine-c.yaml data/natural_products/unclassified/chevalone-e.yaml
    data/natural_products/unclassified/chondramide-a.yaml data/natural_products/unclassified/chrodrimanin-b.yaml
    data/natural_products/unclassified/cinnapeptin.yaml data/natural_products/unclassified/citreohybridonol.yaml
    data/natural_products/unclassified/citrulassin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-256/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-18e3a7edca
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-256/validate-all-001.tsv
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
  - naturalproductmech:mibig-18e3a7edca
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
  - naturalproductmech:mibig-18e3a7edca
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
  - naturalproductmech:mibig-18e3a7edca
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-256/review-queue-001.tsv
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
  - naturalproductmech:mibig-18e3a7edca
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2551-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/chaetocin.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Complete chaetocin owner and all 3 history events, carried from actual
    whole reading by identical current bytes.
  snapshot_sha256: 7ed72be67fbb9cc624571cda7a24a19b283b845d30d51f2ae974bad161987b0d
- evidence_id: bgc-2551-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Complete actual owner capture and its metadata; preservation is distinct
    from independent scientific validation.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/intakes/2551-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Actual canonical target, maintained ownership and all 42 input placements
    joined to the accepted plan and current hashes.
  snapshot_sha256: c0c426f5dae648175a543ae60fecd9f5c57f168debbf2ba450674fb678e0eede
- evidence_id: bgc-2551-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-intake-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /source; /source_plan_acceptance;
    /source_plan; /selection; /capture; /capture_acceptance; /environment; /intake_summary;
    /original_tools; /intakes; /native_gate_acceptance; /verification; /scope; /passive_observer_recovery;
    /user_outbound_hold; /external_requests; /retries; /diagnostic_result; /maintained_reader_results;
    /scientific_verdicts
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: ROOT accepted the original ten canonical intakes at 426 placements across
    51 paths, including the planned taxonomy-query inputs. This owner is assessed
    only after its actual inspection.
  snapshot_sha256: 1604fe3b3542aae03b17b7316b5d14b03ead1f6ab5d0eb05f3eb4154b1660d3b
- evidence_id: bgc-2551-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status;
    /records/0/owner_document/grounding_notes
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact retained identifier, full structure key, source concepts and grounding
    fields, including cross-references where present. No fresh authority lookup or
    natural-identity verification is inferred.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups;
    /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, coordinates
    and citation tiers as declared. Different evidence grades are not transferred
    between claims.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Complete owner supplies retained occurrence assertions and every written
    bioactivity where present. An absent observation is not biological inactivity.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact named/versioned model arrays, glycoside flag, filing and separate
    source BGC categories; scientific applicability is assessed independently.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_status; /records/0/owner_document/curation_history
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Complete owner history and status. Historical seeding and curation do not
    supply fresh primary-publication access.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The complete owner has no declared graph, graph-reference, component, biosynthetic-pathway
    or root molecular-target field. No maintained reader applies. Its 25 written bioactivities
    remain present and require their own assay-context interpretation.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: bgc-2551-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: All ten saved comparison flags are true, including formula C30H28N6O6S4,
    zero charge, standard InChI, complete key and both canonical SMILES strings. One
    chirality-aware match covers all 46 atoms. The diagnostic nevertheless explicitly
    leaves independent full-graph identity unestablished; a match between two stored
    encodings does not establish experimental natural identity. The four warnings
    belong to the original whole-batch stderr and cannot be assigned to this owner.
  snapshot_sha256: 5ed67154a557428a9822cd74c0955c82fa6591381965e375d5f9b6a2df7c1c12
- evidence_id: bgc-2551-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds;
    /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices;
    /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings;
    /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs;
    /records/0/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The complete saved tables contain four amide carbonyls and two six-member
    nitrogen diketopiperazine rings, with two sulfur-sulfur bridges joining substituted
    ring carbons. Two indoline-like fused halves are joined by a carbon-carbon bond,
    and two hydroxymethyl substituents remain. No ester, phosphorus or candidate saturated
    C5O sugar cycle is present. These are observations of the stored graph, not a
    deduction of an enzymatic sulfur-insertion mechanism, precursor origin or absolute
    configuration.
  snapshot_sha256: 5ed67154a557428a9822cd74c0955c82fa6591381965e375d5f9b6a2df7c1c12
- evidence_id: bgc-2551-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-current256-first-five-molecular-intake-reading-001.json
  locator: /records/0; /counts; /reading_scope; /intake_reading; /source_reading;
    /limits
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'BGC completely read all first-five saved molecular tables and the corresponding
    actual intake fields: 352 atom rows, 396 bond rows and 216 input placements. No
    new parse was performed.'
  snapshot_sha256: 35b3971d1c27a1b60b28a64f0d977ab5ba8a2da75ed0dfb32c8a606f38250d58
- evidence_id: bgc-2551-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /readback; /independent_peer; /last_five_reading; /intake_acceptance; /verification;
    /whole_molecular_reading; /scope; /ROOT_reading; /actual_operator; /external_requests
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostics, with 88 of 100
    comparison flags true and four global undefined-stereochemistry warnings preserved.
    Warnings are not attributed to individual owners. Full-graph identity remains
    unestablished by this method for every owner, without an automatic defect inference.
  snapshot_sha256: ce8d094e6dccc0f7bf5c4e7317dbd4e80953c45036d1a8594af631904a831ed0
- evidence_id: bgc-2551-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact original diagnostic command, clocks, zero exit and source/stream
    pins. The original stderr retains four warning blocks; no alternate parse was
    used.
  snapshot_sha256: 907e344f01ce09ca03c2340c5f78750840e75de01b571f7d3aa193c9e8423497
- evidence_id: bgc-2551-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–433
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The schema distinguishes structure stereochemistry from named/versioned
    computed classification and its evidence scope.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2551-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The maintained stereo_complete calculation checks unassigned molecular
    chiral centers. It does not count all literal InChI question marks or assert complete
    double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2551-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Zero or multiple model pathways produce UNCLASSIFIED filing while exact
    model arrays remain retained; filing does not decide model applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2551-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 126–145; 1318–1382
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The seeder retains deposited activity calls, adds numerical measurements
    only with both a name and value, grounds only recognized protein identifiers and
    caps written activities. Title-derived activity classes are not independent target
    or mechanism evidence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2551-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-current256-assigned-source-reading-001.json
  locator: /contexts; /counts; /reading_terminals; /whole_owner_reading; /finite_verification;
    /cautions; /assay_scope; /search_scope; /attribution
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'BGC wholly read the five selected contexts: 45 query frames, 136 retained
    physical row placements and all 1506 fields. These include 118 assay row placements
    representing 117 distinct full-key/CID/AID tuples, with no blank AID or merge
    row in this partition. Credit is retained database-row reading, not new primary-publication
    inspection.'
  snapshot_sha256: 776629fd4a495399bb1406da0ffb4ba8282c73c20d51531dfd242e261a78011e
- evidence_id: bgc-2551-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries; /required_input_supplement
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'The notes preserve original inventory/composer scope of 410 placements
    across 50 paths and disjoint readings of 159 rows/1754 fields: BGC 136, Support
    23 and Native zero positive rows. Four taxonomy merge rows are separate. The notes
    record the then-pending taxonomy-input supplement; current operative intake authority
    is cited separately.'
  snapshot_sha256: 1e1fb894d0fe150d27cd92b637788e782ad886fd0786882126672059c5528ca5
- evidence_id: bgc-2551-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/bgc-source-plan-execution-001.json
  locator: /observer; /delegated_by; /recorded_at; /status; /source; /installation;
    /binding_handoff; /binding_peer; /original_tools; /arguments; /terminal_chunk_id;
    /exit_code; /original_objects; /empty_objects; /live_handle; /complete_original_output;
    /inventory; /notes; /plan; /derivation; /actual_invocations; /retries; /readback;
    /required_taxonomy_supplement; /external_requests; /source_query_replays; /scientific_verdicts
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: One original composer produced the immutable 410-placement/50-path plan.
    This execution receipt does not itself establish the later supplemented input
    scope.
  snapshot_sha256: 29e2e7c1d5fddb57b91173a4e61af51ca06b89d87bb4153f275f120681f31f67
- evidence_id: bgc-2551-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-source-plan-acceptance-001.json
  locator: /observer; /recorded_at; /accepted; /status; /plan; /original_plan; /independent_peer;
    /supplement_handoff; /inventory; /inventory_acceptance; /source_reading_acceptance;
    /notes; /original_composer_execution; /original_composer_tools; /verification;
    /scope; /canonical_intakes; /diagnostic; /scientific_verdicts; /external_requests
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: ROOT accepted the operative 426-placement/51-path plan. Six missing merged-taxon
    placements and ten nonorganism-table placements were added without another collector
    query or additional positive-row/AID credit. Original 410/50 provenance is preserved.
  snapshot_sha256: ac7d6ad5a59b920608dd3f690213af2011c8f81333acb1292dc24e49b9012b13
- evidence_id: bgc-2551-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-current256-five-gates-acceptance-001.json
  locator: /status; /verification; /unavailable_required_gates; /execution
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Five documented local commands passed. Full QC and OAK remain unavailable,
    with all_native_gates_passed false. Selected queue leads are not scientific findings
    and local success does not complete the review.
  snapshot_sha256: 319f0cd4fa76e6ca46dc31ba74652ba42b527e1ff8a5bb4b3e49c395a8af0bd7
- evidence_id: bgc-2551-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation;
    /implementation_pins
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The bounded retained curation scan found 100 lexical matches but zero exact
    applicable corrections or exclusions. Its 118 actual assay row placements resolve
    117 distinct full-key/CID/AID tuples; two blank sentinels belong to other selected
    owners. The exact exclusion table and implementation were inspected without applying
    an exclusion. This receipt retains its original input scope and author-time pending
    plan status.
  snapshot_sha256: fafc422df141040e1168a039350961c7f34d19f470409f46ca719a442767589b
  search_scope: Ten exact retained contexts; eleven enumerated curation tables including
    ignored files, of which nine implemented tables contain 3422 rows. All 93 correction-table
    and seven unresolved-taxon lexical matches, plus fifteen exclusion rows, were
    read under exact identity/source/assay applicability predicates. Reserved decisions/source_queue
    tables are not effective overrides. No global absence or assay-protocol claim
    follows.
- evidence_id: bgc-2551-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/15
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Complete retained cache stanzas for this owner’s source IDs provide names,
    identifiers and synonyms only. They do not verify rank, lineage, strain equivalence,
    occurrence or production.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: bgc-2551-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/source_taxa; /contexts/0/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/0/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: This owner’s exact source IDs and saved forwarding/nonorganism results;
    no fresh taxonomy request or newly verified ancestry.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: bgc-2551-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /routes; /interpretation; /forward_routes
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Native wholly read seventeen cached stanzas and ten context routes. Four
    historical unmatched IDs elsewhere in the selected set have explicit retained
    forwarding routes. Names and synonyms do not supply rank or lineage verification,
    and Native receives zero positive inventory-row credit.
  snapshot_sha256: a2cc30e7383daa4c5a8b571e68ea4eb106ef6fd05e880955e8fa25b958d23c43
- evidence_id: bgc-2551-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-target-input-plan-003.proposed.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact immediate owned-BGC context inputs. Shared loci or citations do not
    transfer identity, stereochemistry, assays, producer grades or mechanism claims;
    no transitive or name-based expansion was used.
  snapshot_sha256: c196eea90a6145f1e90684b4169ae2dbfa0e7ffcc94722af4ddc95fecb798b44
- evidence_id: bgc-2551-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 retained row placements with the
    exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched
    payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 436–436; row_sha256 f362f2715d76dbd2a6de1c0b45ed3711c918242ca8ac2b441868e202eb32a57e
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact compound/version, retained structure/key, cross-references, separate
    producer/locus grades and citation tiers. Whole retained-row reading and exact
    current physical bytes are joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2551-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 0 retained row placements with
    the exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched
    payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 0 retained row placements with
    the exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched
    payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 retained row placements
    with the exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched
    payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 retained row placements with the
    exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched payload or explicit
    empty frame, without a query replay.
- evidence_id: bgc-2551-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 1955–1955; row_sha256 aade694dadfc73dcf712c6dc6feeb26e6aaf2b35fc5612d0c829afe5a898f877
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    remains separately assessed. Whole retained-row reading and exact current physical
    bytes are joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2551-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 118 retained row placements with
    the exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched
    payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 5428–5428; row_sha256 7f5eb0367ac72639ddf8ebc0de641b42733c656e8169c64216cc7fda906e9f19;
    physical lines 5429–5429; row_sha256 ffe8c904ae7e9a6eec8916faae802a203732a72c67754066e207325113ba3a59;
    physical lines 5430–5430; row_sha256 f51a0dea32bda355f6160f708273ad9f7b15e0db67190c64b9a39ef5b07df2c5;
    physical lines 5431–5431; row_sha256 58f2f2965ee1083564c32c99dd2b51d7152fd83d7b2b5c52b8fa04fead66c28c;
    physical lines 5432–5432; row_sha256 78f4a8935875a5c8698fb2a20e700ee08176d8c0dd63b98e07770c2eb78dc4e8;
    physical lines 5433–5433; row_sha256 021a9fc9239ca51be062a5fc50705cdcd0e6f5fd86087202d4321c7146f84fd4;
    physical lines 5434–5434; row_sha256 bde4d5e1fa5ccf08e4bda94d2f9fe5b45554ae643bef8d5d727776a5c9b436c5;
    physical lines 5435–5435; row_sha256 48bdbd75ca4f56be80e72c5863e4db0abe7052f9ef04c82b59ae5f882ec4a5c5;
    physical lines 5436–5436; row_sha256 3302ecf765966dbf1cc04336b9375770ac31a206c419ad6b2ad6c27c04d4e555;
    physical lines 5437–5437; row_sha256 1812870110782ab391e740b3d5ad85cff65714b96eaa83a76d71f593bc6e6380;
    physical lines 5438–5438; row_sha256 aa2d1f01a930a1dc6c759c9dc4102fef54ee4faca1ae79d31b6860f00a1be727;
    physical lines 5439–5439; row_sha256 0e6861550b8b206fb9398fd106d62feebdee13562dfa51e4e9fad78244fbb3fa;
    physical lines 5440–5440; row_sha256 b2357965cc1549803cb9ca3d607a4609dc1675966cb29684b075d891d9e56254;
    physical lines 5441–5441; row_sha256 af00d55258e993039c1bfcff3f08d2e25c93afa01131c02ebe8dab8ca63cbc43;
    physical lines 5442–5442; row_sha256 5dc02c0a017d4f0e6970079f9db9c1c64a8675adc17edff2a25aec2afe13d6b0;
    physical lines 5443–5443; row_sha256 ef6634495441bc8902e335d6cdbe99c2ae04fb78a82f45193fa3f298effb953b;
    physical lines 5444–5444; row_sha256 e5a81cb1b6ac4ad729216324b64abf371a9c3ec91b343af3d3e7b2634c331d7c;
    physical lines 5445–5445; row_sha256 8731fb4d9383e714c65ab0595d14ab177082ae4587689a9c3e5847e3427afabd;
    physical lines 5446–5446; row_sha256 cfe70d659f81412fc82082880d7f3db026d7fe8b2c2eceddcb7bd94b4fc00a1c;
    physical lines 5447–5447; row_sha256 9d4efa0c5f1dd78c73d770acbd6fa4b19a5e876c8d4ec6f867801508b0a49375;
    physical lines 5448–5448; row_sha256 8e918902b42cfe644c11b266d842c8e1eacaf5920a4fefa1a7aa7ee14d60ad3c;
    physical lines 5449–5449; row_sha256 ffb72326e817ca843b6afcddbb7faad77caa0d51a1f1035925cc113a347be3cd;
    physical lines 5450–5450; row_sha256 7affd891b49b5a9293fcf8fd05744af863a421fe7ff4e3e7586f846861807c99;
    physical lines 5451–5451; row_sha256 26593eab033abc67c7de063506f600579b8c193dc91520e2456fc76c1ef1922b;
    physical lines 5452–5452; row_sha256 28b64c8f08fe7fb848ee741e27efab4947f9ad391fc8a0f58b6fa81d69b09ac7;
    physical lines 5453–5453; row_sha256 4680a27a580ebd41b34b785f16748656d99d43f80ab763e8a67ac19ac02cb634;
    physical lines 5454–5454; row_sha256 478677a4ba3bf8abb8637bab7ff1e91d2f94bac46b1771cebae48d4c25ca8524;
    physical lines 5455–5455; row_sha256 c49af1b1904b7077366011af358213cc332f283f2a36b2ff795c8e2486f1bf2c;
    physical lines 5456–5456; row_sha256 c17fe761287f704298b48062cb8a1badcf2279858301c78423b619a91ecce0fe;
    physical lines 5457–5457; row_sha256 58b0d30d991e2883a4c7ffbc06b3db791290fa208ad40a4dc6085f31bbbef2a0;
    physical lines 5458–5458; row_sha256 c32e34c498635fb28720d41064846e9d11e7091327978aa9192e2b70282244d6;
    physical lines 5459–5459; row_sha256 71849d93983c6ed79f4b72499faad449bc2d8eafd6193477673a371c97984b76;
    physical lines 5460–5460; row_sha256 dee4bcc7e17d8f9d8bbdf6d4570f217a52d3c6f4099d1fb8b06f19efdef43f95;
    physical lines 5461–5461; row_sha256 070626fdfac23a8daf4cd01a22ee790be2951c99662b9970414e0ffaa8ba2dd2;
    physical lines 5462–5462; row_sha256 24cf62065b9a3f3495b18e0a4ea4251b67daedc103c2c4dacc8b615d87090d14;
    physical lines 5463–5463; row_sha256 5b8e739765aa51191f378545218e744b1f1485b599a219e8684c8d8eb11e4a87;
    physical lines 5464–5464; row_sha256 e0514ca3956ef6d2ee7d16c3e6c11627f4eea2548a5bfe938c83517e2f79f87e;
    physical lines 5465–5465; row_sha256 09e1ce17284d1f9f77c995bf44eb8ae8447b322341192026ae0a9e7b32d85fc9;
    physical lines 5466–5466; row_sha256 66bfb99a20dc382efe08becb0e0033f67eb91a1f94589094fbbaacb4a4e71aa8;
    physical lines 5467–5467; row_sha256 741d9fe5740159ca61bf493e4d711ac92b391dad59e34556ebec96cccd84e762;
    physical lines 5468–5468; row_sha256 d5368105e02207004ebd6baa5ec9ed90a2e448d9a44f68802bcaf66d2f9a945c;
    physical lines 5469–5469; row_sha256 9a017796f1a2e6d4e560af7d5bb74ca58d15bf066149f03be3754a7df0e6615e;
    physical lines 5470–5470; row_sha256 4349c031066b73f28b5f83d2237752f2ca3edd9cc1f6ed5861a59d7b0de8e161;
    physical lines 5471–5471; row_sha256 8acaddfcf5cf1bf7cbfdd6d250b4cd9cbaf9d662054d59ad2453f9020116dd3e;
    physical lines 5472–5472; row_sha256 ab0d26d544f8dea7b550a550972df09ab66e3ec7487683fabbe749d6660ed563;
    physical lines 5473–5473; row_sha256 ea8e1f5e0ae4812245014397b9dffb63046b941482a0a9a25e6db5558d8e8ab0;
    physical lines 5474–5474; row_sha256 a6e4125aa925d9a71a6931743a62a4b07c594148974581ce25fe9dccc643707d;
    physical lines 5475–5475; row_sha256 cf083a1b04a228bda8ea25e2681d8e240ab22ec3d73a9a05b6fbec29e5f7e84d;
    physical lines 5476–5476; row_sha256 b11816009cda8c3c5612f69771014311eb4c3f199ae28e0a4a5dbd2f35b8aef3;
    physical lines 5477–5477; row_sha256 70be311193b45dc44ee51ddbdb2a254c62a0cb2d5cf4ece8cd80835a981b4e84;
    physical lines 5478–5478; row_sha256 562d1253504645acf32251f30276bf6f5b80309f8b67f097f0fef66c1e2f7132;
    physical lines 5479–5479; row_sha256 cbbde43ed2f800e64ee56cc41511e5894f5c8f87318e910352421f1a751a3ef5;
    physical lines 5480–5480; row_sha256 f7dcf4e96224b21092e9d2f911ae9391e91ee2b33c2119ac99938a5b3dff92cd;
    physical lines 5481–5481; row_sha256 311bc07b7f755ed9189fb6020d8ad6361c8efe8f3a0320169daf7e8028d5bb55;
    physical lines 5482–5482; row_sha256 e9bfbb71fdb3ec400aaa40f61c429be4c60b778f3c7e8eb46a9cfa7bd13d3279;
    physical lines 5483–5483; row_sha256 2b24ec13b0cf9a77d2a549117f24d23cfd3e4f9079eb02a55fe5add2e0358cec;
    physical lines 5484–5484; row_sha256 a5d0f981ed9bf7f1c1840d350030e6107ad89453de6fbd1192ef083f9a71e997;
    physical lines 5485–5485; row_sha256 0597b9f0076fac829de1704c4bde2b74bcfe3d062cde44326e7c3e917ca3c7ff;
    physical lines 5486–5486; row_sha256 cb19b99014080a06e2f2315fe78da308c859f8fdd362a1b88e73014ee48930bf;
    physical lines 5487–5487; row_sha256 fd60c67644b0a04373c3127e8851606467a101c305ed23305bebba9533b8cc4c;
    physical lines 5488–5488; row_sha256 58860b6a5e7bf9acd4ec2ddd176202cfe09d441dfc24c5946ad16d813e4a53e3;
    physical lines 5489–5489; row_sha256 27ac515817ea6d31e668bbfc06f21fed9e31c48acccc16b67cbb10ca25ec361a;
    physical lines 5490–5490; row_sha256 3a21db8a0353ab395f3ab3a8ecbbf53e064dda0ada897f9dd86900b182876cdf;
    physical lines 5491–5491; row_sha256 ed5d9ab32ffe979e013affd4b151820522808f5bc11cf75d1a82e009c9f2b232;
    physical lines 5492–5492; row_sha256 6cf13c4573e1893722a1b611077a0a1b9d2d2d0d7389a0174e88531e4e761768;
    physical lines 5493–5493; row_sha256 4bba8c5ac3456649e4d507c480455ef70921a1a5e2550b80cd9ab84b579ee287;
    physical lines 5494–5494; row_sha256 b3f7ef0cbace4c1cc1a88bae908e571e24daf06256b96330e64680466f950a17;
    physical lines 5495–5495; row_sha256 08871b25bf9b80b0f321cddfccf9a00c3b56b9aecd5fc93097ea68602ab720cc;
    physical lines 5496–5496; row_sha256 b6a45e3d1861a3e0dce618d6af0d3808bd31bf6b51b24c698285555495dc3d86;
    physical lines 5497–5497; row_sha256 8e29f5c77a79c82c281bcb7c706f4e6485ee84d32bcd0ac025f0192226f5c763;
    physical lines 5498–5498; row_sha256 8e7910624041b8f6f00bf9bdfa94ddc493281e2533c99b0b332bd0534fb57275;
    physical lines 5499–5499; row_sha256 c7c9857bc26ed9a34116bf9feb509fe8ffcde95c8d62cea540d4d165b70fba55;
    physical lines 5500–5500; row_sha256 4f8a59c5404642cd69f932ec9d56fc998832f3b77d56e69db1491f34e1569758;
    physical lines 5501–5501; row_sha256 847275bcbf98e90fd00f5c8f7aaff740d7bab9a2cf0ae014c1ff5931f6c012d8;
    physical lines 5502–5502; row_sha256 951c2f4da948fc4acc4610d98552baa45b4394a46d91b900632dee9b2e293a19;
    physical lines 5503–5503; row_sha256 ac254a4fcae866de9cba515f4bc0d13e251f3513d3f62bda3405b295506c6516;
    physical lines 5504–5504; row_sha256 f558224628e2672e15aae77bbfbbb3a0a2df3fa41ce96c0a20e3a3ad0e834803;
    physical lines 5505–5505; row_sha256 1d95a8b64bddbc0ff01f058309600ebcdbd68a52d86c9371b763c5c8ff430187;
    physical lines 5506–5506; row_sha256 144b7a7862cb8c15048076e576e4aaeec01012ea1fb0828ee1f5a0e51a69e40b;
    physical lines 5507–5507; row_sha256 48fc69bfc314ba6809f68297dbf124326e808abba4b02bb36063dacb64a4a15b;
    physical lines 5508–5508; row_sha256 5b363c98cf2f087a32c70598574981d977ee672ea1c91ee6c84cba6e8485ae86;
    physical lines 5509–5509; row_sha256 3dbe2fba1f99b18c061f03bc9b9633791adafb28e444ea5d522a41bce7565edc;
    physical lines 5510–5510; row_sha256 d917f5b621a756efb7d0f38c425ac8541e450ebbb5df52b9fb8c2d9b6b4e3df9;
    physical lines 5511–5511; row_sha256 039863964d7e7ef40c3067eb4cdf3eff6c331732c1145c2df070e96739ca9d8b;
    physical lines 5512–5512; row_sha256 8654705bff9566d32ecd9c35a1871bd40b7cbda52a3f1c9e6fdfe9df699c4446;
    physical lines 5513–5513; row_sha256 475fead6571ef57901eae9bf4bf76139ddc674d2e387d616fd17f3303808a0cd;
    physical lines 5514–5514; row_sha256 2bdd467bd32cd89fbfb1779f4d6ec969c369e9c7c22e376b44f48cc3aa64712f;
    physical lines 5515–5515; row_sha256 abf81252df88749fe53a9402489e7f099847630ebdb7d40f54b93967df689d60;
    physical lines 5516–5516; row_sha256 c487b44204ab2b8e9234b00f468e2a2c8e3eed423ee4037e438a06f815986ccf;
    physical lines 5517–5517; row_sha256 926601a7c593eeccaf3b557dd28baa8558f411d6d1861fc7498bc4ec5c3290fa;
    physical lines 5518–5518; row_sha256 b5f436cbd6412dcae02bc7b4d1764081a3be6c08a27704dc9edd68f00a1e0eb6;
    physical lines 5519–5519; row_sha256 e7c89cd28b865f266bd109b42e58091e350d93d83287f08a7b9026f2dd451840;
    physical lines 5520–5520; row_sha256 ce9f84783992c2182389c570f9f2a3a9a748f5e6fd19339ad7a421f51838980e;
    physical lines 5521–5521; row_sha256 65c1ceb638f7b81db594158e7e2286f7d0c763fac4bb24f12d5eb04b1d2c4956;
    physical lines 5522–5522; row_sha256 3f3a8ece2816a444ddbdbdfe939019aae0a381f073db00de54ecc2cf8b185a2e;
    physical lines 5523–5523; row_sha256 7777d0aecdfd0dceae3f46fb103cffe5d36d87aefcadf19fb6ee4871e5a18230;
    physical lines 5524–5524; row_sha256 040e7c93570c2e2ce3162f28c826dd94695e06cf5f067c3c4028528b10de87ac;
    physical lines 5525–5525; row_sha256 3c2e2a3bbc4d6fe0d366d0d699475e2b96687b47975635d9c44d18dc97e8a931;
    physical lines 5526–5526; row_sha256 90fd0ae949519ed9e87e081a5a585b2ea67a5b978d36f3dddbcc087e271cfe70;
    physical lines 5527–5527; row_sha256 fb3f84b4b27e8d958e1ae5d4b1aa091a8a31382a39f68fa1cd3321e9022e7b9e;
    physical lines 5528–5528; row_sha256 ce57c5b12fa6c93026a71216c1ff8e5d08f51b38fad17a9347988383be92799d;
    physical lines 5529–5529; row_sha256 408eddaed3d5e190d9affc4929c448e188c6ad4005123e75d2492d523a1cc2f0;
    physical lines 5530–5530; row_sha256 4908b8958f2a28505ce481b231fdb94ee2be917b4c1a3f8f23bb2e5d8c40477e;
    physical lines 5531–5531; row_sha256 816ed4be89a6bbf40ca5cb0f9f37c6e3a34c2298ea313e25813984550f071d98;
    physical lines 5532–5532; row_sha256 f8005ec22fd9f4bb0c2f3cf23cbedaaf8a45aa4c1a15114fcfb477d73e6e8008;
    physical lines 5533–5533; row_sha256 d18362953816d2b671ba79a85aaf93e837b814df6ef5fe35ca81795fc4b02095;
    physical lines 5534–5534; row_sha256 89da67dad51ec121fb458907c738775a319dc007842f2dcdea085ae2f63bd28c;
    physical lines 5535–5535; row_sha256 807accd9cefde2a6e7eba3c054ecc8fadf5bcbcc354a176823171b4e6f6a1089;
    physical lines 5536–5536; row_sha256 4fae227481c851f541487d4b5a0516933bab8f7b6df649e4573d82df2611b24d;
    physical lines 5537–5537; row_sha256 28c4862ebcb701a4356777a6ff407a6c19b9eb4c3021ba6ac4440b1e43a67c29;
    physical lines 5538–5538; row_sha256 45e400425f7e80def199fde2e83f191e46cb4799686006a28c67b34c9357b912;
    physical lines 5539–5539; row_sha256 08ccb2f5413fd092abeaace9aeb01e75a5e1cdfd05ed4546082c6b2cd5cfa93d;
    physical lines 5540–5540; row_sha256 b0a4467750024a81c54acde0b114a50dee5e7efeec82e6506b7dd3d7b69e30c4;
    physical lines 5541–5541; row_sha256 2dd807c27e329ca76319fc6d10401afc44777ad1f0f6815dc11b1e49ff8807d8;
    physical lines 5542–5542; row_sha256 a9275f2cb382638193167a5c8f361bf63955b4047bc613335ca2b7f76b2095a9;
    physical lines 5543–5543; row_sha256 27b20a2ceab8e3ef83690298dd7988c52f2371596b88781e4da14492fa251ca6;
    physical lines 5544–5544; row_sha256 58a7a2c730b7c1b722fa146ab5cee26de5c46d75f01c1bd16820ea1010a0c261;
    physical lines 5545–5545; row_sha256 25b6671ea014ecbf35ea739d2a20e5d74b704e8fd53a0bd5a517385c1e6c78b3
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: All 118 exact Chaetocin assay row placements, including both placements
    of AID1346062 with different references. All deposited calls are Active; endpoint
    names and numerical values are empty. Screening/Confirmatory/Other titles, conflicting
    tissue labels and ungrounded target accessions remain literal, without silently
    normalizing them or inferring direct target inhibition. Whole retained-row reading
    and exact current physical bytes are joined.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2551-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 retained row placements with
    the exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete matched
    payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 retained row placements
    with the exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "PZPPOCZWRGNKIR-UHFFFAOYSA-N". Complete
    matched payload or explicit empty frame, without a query replay.
- evidence_id: bgc-2551-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 retained row placements with the
    exact predicate, query and all fields.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Complete matched payload or explicit
    empty frame, without a query replay.
- evidence_id: bgc-2551-exclusion-table
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: Complete retained diagnostic/implementation input; interpretation bounded
    by the saved owner query and pinned Native receipt
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Retained exclusion diagnostic input captured in this actual intake. Native
    inspected all fifteen rows and found no exact applicable match to the saved assay
    identity tuples; no exclusion is applied.
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: bgc-2551-exclusion-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Complete retained diagnostic/implementation input; interpretation bounded
    by the saved owner query and pinned Native receipt
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Retained implementation input captured in this actual intake; exact identity/source-attribution
    guards and provenance preservation do not create an assay or a correction.
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: bgc-2551-unresolved-taxa
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv
  locator: Complete retained diagnostic/implementation input; interpretation bounded
    by the saved owner query and pinned Native receipt
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: Retained unresolved-taxon diagnostic input captured in this actual intake.
    Lexical matches are not exact applicable corrections or fresh taxonomy evidence.
  snapshot_sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
- evidence_id: bgc-2551-taxon-merged-input
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv
  locator: Complete retained diagnostic/implementation input; interpretation bounded
    by the saved owner query and pinned Native receipt
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The retained merged-taxon table is included in this actual intake to capture
    the saved query and its negative scope as well as any explicit forwarding result.
    Capture does not infer a new route.
  snapshot_sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
- evidence_id: bgc-2551-taxon-nonorganism-input
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv
  locator: Complete retained diagnostic/implementation input; interpretation bounded
    by the saved owner query and pinned Native receipt
  accessed_at: '2026-11-05T13:03:39.485780Z'
  support: supports
  summary: The retained nonorganism table is included in this actual intake for the
    saved query and its negative scope. No nonorganism result or biological conclusion
    is invented.
  snapshot_sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:24:35.238925Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 726c23bfb5cf1d35406050521ce748bed31e1a54f2b059ace62708d240b0ec6f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:24:59.093466Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: abaf52c1a3174650333c90f46b94c837bc28699d7d7910c26ef650fa6173c043
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:25:17.770846Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:25:50.262912Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:26:01.626059Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 4eb94433e8671f2d0089684950fba7aef697542150201403ac54f25d798445e2
assessments:
- assessment_id: bgc-2551-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: Chaetocin retains the complete key PZPPOCZWRGNKIR-UHFFFAOYSA-N, MIBiG BGC0000321
    version 4 and the content-derived record identifier. Both stored forms produce
    that same standard InChI and key, and the saved full-key source query returns
    the retained CID 161591 rows. This supports local encoding and provenance correspondence.
    The record deliberately lacks specified stereochemistry, so neither the CID cross-reference
    nor the shared name establishes equivalence to a particular naturally isolated
    stereoisomer. The empty retained exact-key ChEBI query bounds that inventory;
    the historical grounding note is not a new global ChEBI search.
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-grounding-owner
  - bgc-2551-chemistry
  - bgc-2551-source-mibig_compounds
  - bgc-2551-query-chebi_structures
  - bgc-2551-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: PZPPOCZWRGNKIR-UHFFFAOYSA-N; retained full key, not independent natural-identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2551-grounding-owner
    - bgc-2551-chemistry
    - bgc-2551-source-mibig_compounds
    - bgc-2551-query-chebi_structures
    - bgc-2551-direct-contexts
  - name: grounding_scope
    value: Chaetocin retains the complete key PZPPOCZWRGNKIR-UHFFFAOYSA-N, MIBiG BGC0000321
      version 4 and the content-derived record identifier. Both stored forms produce
      that same standard InChI and key, and the saved full-key source query returns
      the retained CID 161591 rows. This supports local encoding and provenance correspondence.
      The record deliberately lacks specified stereochemistry, so neither the CID
      cross-reference nor the shared name establishes equivalence to a particular
      naturally isolated stereoisomer. The empty retained exact-key ChEBI query bounds
      that inventory; the historical grounding note is not a new global ChEBI search.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2551-grounding-owner
    - bgc-2551-chemistry
    - bgc-2551-source-mibig_compounds
    - bgc-2551-query-chebi_structures
    - bgc-2551-direct-contexts
- assessment_id: bgc-2551-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: Each saved form contains 46 atoms and 55 bonds in one neutral connected
    component. Both expose eight unspecified tetrahedral centers; the false stereo_complete
    flag is consistent with the maintained atom-center implementation. The original
    SMILES centers are 4, 6, 7, 11, 23, 25, 29 and 33. These are internal diagnostic
    indices, not biochemical atom numbering. No stereochemical assignment, mixture
    composition or natural configuration was inferred.
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-grounding-owner
  - bgc-2551-chemistry
  - bgc-2551-topology
  - bgc-2551-diagnostic-reading
  - bgc-2551-diagnostic-acceptance
  - bgc-2551-structure-schema
  - bgc-2551-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Each saved form contains 46 atoms and 55 bonds in one neutral connected
      component. Both expose eight unspecified tetrahedral centers; the false stereo_complete
      flag is consistent with the maintained atom-center implementation. The original
      SMILES centers are 4, 6, 7, 11, 23, 25, 29 and 33. These are internal diagnostic
      indices, not biochemical atom numbering. No stereochemical assignment, mixture
      composition or natural configuration was inferred.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2551-grounding-owner
    - bgc-2551-chemistry
    - bgc-2551-topology
    - bgc-2551-diagnostic-reading
    - bgc-2551-diagnostic-acceptance
    - bgc-2551-structure-schema
    - bgc-2551-stereo-method
  - name: representation_correspondence
    value: All ten saved comparison flags are true, including formula C30H28N6O6S4,
      zero charge, standard InChI, complete key and both canonical SMILES strings.
      One chirality-aware match covers all 46 atoms. The diagnostic nevertheless explicitly
      leaves independent full-graph identity unestablished; a match between two stored
      encodings does not establish experimental natural identity. The four warnings
      belong to the original whole-batch stderr and cannot be assigned to this owner.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2551-grounding-owner
    - bgc-2551-chemistry
    - bgc-2551-topology
    - bgc-2551-diagnostic-reading
    - bgc-2551-diagnostic-acceptance
    - bgc-2551-structure-schema
    - bgc-2551-stereo-method
- assessment_id: bgc-2551-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: The retained MIBiG row names Collariella virescens, NCBITaxon:1934374,
    with SOURCE_ASSERTION producer evidence and a separately graded CLUSTER_UNSTATED
    locus. BGC0000321 is version 4, active with questionable quality and unknown completeness;
    KF496217.1 and the NRPS category remain source assertions without freshly inspected
    sequence or experiments. The retained OBO stanza for the same ID names Achaetomiella
    virescens and lists Collariella virescens as a synonym. This is a saved label
    relationship, not a newly verified taxonomic rank, lineage or reassignment. No
    first-five forward-merge or non-organism match is present.
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-origin-owner
  - bgc-2551-occurrence-owner
  - bgc-2551-source-mibig_compounds
  - bgc-2551-cached-taxonomy
  - bgc-2551-taxonomy-routes
  - bgc-2551-curation-scope
  - bgc-2551-direct-contexts
  - bgc-2551-exclusion-table
  - bgc-2551-exclusion-implementation
  - bgc-2551-unresolved-taxa
  - bgc-2551-taxon-merged-input
  - bgc-2551-taxon-nonorganism-input
  dimensions:
  - name: taxon_scope
    value: The retained MIBiG row names Collariella virescens, NCBITaxon:1934374,
      with SOURCE_ASSERTION producer evidence and a separately graded CLUSTER_UNSTATED
      locus. BGC0000321 is version 4, active with questionable quality and unknown
      completeness; KF496217.1 and the NRPS category remain source assertions without
      freshly inspected sequence or experiments. The retained OBO stanza for the same
      ID names Achaetomiella virescens and lists Collariella virescens as a synonym.
      This is a saved label relationship, not a newly verified taxonomic rank, lineage
      or reassignment. No first-five forward-merge or non-organism match is present.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2551-origin-owner
    - bgc-2551-occurrence-owner
    - bgc-2551-source-mibig_compounds
    - bgc-2551-cached-taxonomy
    - bgc-2551-taxonomy-routes
    - bgc-2551-curation-scope
    - bgc-2551-direct-contexts
    - bgc-2551-exclusion-table
    - bgc-2551-exclusion-implementation
    - bgc-2551-unresolved-taxa
    - bgc-2551-taxon-merged-input
    - bgc-2551-taxon-nonorganism-input
  - name: producer_evidence
    value: The retained MIBiG row names Collariella virescens, NCBITaxon:1934374,
      with SOURCE_ASSERTION producer evidence and a separately graded CLUSTER_UNSTATED
      locus. BGC0000321 is version 4, active with questionable quality and unknown
      completeness; KF496217.1 and the NRPS category remain source assertions without
      freshly inspected sequence or experiments. The retained OBO stanza for the same
      ID names Achaetomiella virescens and lists Collariella virescens as a synonym.
      This is a saved label relationship, not a newly verified taxonomic rank, lineage
      or reassignment. No first-five forward-merge or non-organism match is present.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2551-origin-owner
    - bgc-2551-occurrence-owner
    - bgc-2551-source-mibig_compounds
    - bgc-2551-cached-taxonomy
    - bgc-2551-taxonomy-routes
    - bgc-2551-curation-scope
    - bgc-2551-direct-contexts
    - bgc-2551-exclusion-table
    - bgc-2551-exclusion-implementation
    - bgc-2551-unresolved-taxa
    - bgc-2551-taxon-merged-input
    - bgc-2551-taxon-nonorganism-input
  - name: locus_evidence
    value: The retained MIBiG row names Collariella virescens, NCBITaxon:1934374,
      with SOURCE_ASSERTION producer evidence and a separately graded CLUSTER_UNSTATED
      locus. BGC0000321 is version 4, active with questionable quality and unknown
      completeness; KF496217.1 and the NRPS category remain source assertions without
      freshly inspected sequence or experiments. The retained OBO stanza for the same
      ID names Achaetomiella virescens and lists Collariella virescens as a synonym.
      This is a saved label relationship, not a newly verified taxonomic rank, lineage
      or reassignment. No first-five forward-merge or non-organism match is present.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2551-origin-owner
    - bgc-2551-occurrence-owner
    - bgc-2551-source-mibig_compounds
    - bgc-2551-cached-taxonomy
    - bgc-2551-taxonomy-routes
    - bgc-2551-curation-scope
    - bgc-2551-direct-contexts
    - bgc-2551-exclusion-table
    - bgc-2551-exclusion-implementation
    - bgc-2551-unresolved-taxa
    - bgc-2551-taxon-merged-input
    - bgc-2551-taxon-nonorganism-input
- assessment_id: bgc-2551-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: The locus/producer reference DOI:10.1002/hlca.19700530521 is stored with
    COMPOUND_BIOACTIVITY reference_basis. Its repetition does not independently establish
    a gene-cluster or producer experiment. The two written IUPHAR-DB observations
    share AID 1346062 and target accession NP_001269095 but cite PMID:16408017 and
    PMID:23416387 separately; these are two retained reference placements for one
    assay identity. All three history entries record seeding. No original paper, sequence
    or live authority was newly inspected, and no historical access is inherited as
    current primary-source verification.
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-owner
  - bgc-2551-history-owner
  - bgc-2551-origin-owner
  - bgc-2551-occurrence-owner
  - bgc-2551-source-mibig_compounds
  - bgc-2551-source-reading
  - bgc-2551-source-pubchem_bioassay
  dimensions:
  - name: citation_scope
    value: The locus/producer reference DOI:10.1002/hlca.19700530521 is stored with
      COMPOUND_BIOACTIVITY reference_basis. Its repetition does not independently
      establish a gene-cluster or producer experiment. The two written IUPHAR-DB observations
      share AID 1346062 and target accession NP_001269095 but cite PMID:16408017 and
      PMID:23416387 separately; these are two retained reference placements for one
      assay identity. All three history entries record seeding. No original paper,
      sequence or live authority was newly inspected, and no historical access is
      inherited as current primary-source verification.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2551-owner
    - bgc-2551-history-owner
    - bgc-2551-origin-owner
    - bgc-2551-occurrence-owner
    - bgc-2551-source-mibig_compounds
    - bgc-2551-source-reading
    - bgc-2551-source-pubchem_bioassay
- assessment_id: bgc-2551-occurrence
  area: evidence
  topic: Source-specific occurrence and assay boundaries
  outcome: supported
  summary: 'The complete owner contains 25 written ACTIVE bioactivity placements,
    representing 24 AIDs, and a derived CYTOTOXIC summary. The saved full-key PubChem
    frame contains 118 physical Active rows and 117 distinct full-key/CID/AID tuples:
    57 Confirmatory, 59 Screening and two Other rows. The other exact-key occurrence/target
    inventories are empty in this bounded search. Written truncation and the historical
    note about 93 additional results do not make the omitted rows independent assays
    or create new written claims. No graph, pathway, root molecular-target or component
    applies, so no maintained-reader check is required.'
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-occurrence-owner
  - bgc-2551-mechanism-absence
  - bgc-2551-query-lotus_occurrences
  - bgc-2551-query-chebi_origins
  - bgc-2551-query-cyanometdb_occurrences
  - bgc-2551-query-pubchem_bioassay
  - bgc-2551-query-bindingdb_targets
  - bgc-2551-query-antibioticmech_inchikeys
  - bgc-2551-cached-taxonomy
  - bgc-2551-taxonomy-routes
  - bgc-2551-taxonomy-reading
  - bgc-2551-curation-scope
  - bgc-2551-bioactivity-seeder
  - bgc-2551-source-reading
  - bgc-2551-exclusion-table
  - bgc-2551-exclusion-implementation
  - bgc-2551-unresolved-taxa
  - bgc-2551-taxon-merged-input
  - bgc-2551-taxon-nonorganism-input
  - bgc-2551-source-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    value: 'The complete owner contains 25 written ACTIVE bioactivity placements,
      representing 24 AIDs, and a derived CYTOTOXIC summary. The saved full-key PubChem
      frame contains 118 physical Active rows and 117 distinct full-key/CID/AID tuples:
      57 Confirmatory, 59 Screening and two Other rows. The other exact-key occurrence/target
      inventories are empty in this bounded search. Written truncation and the historical
      note about 93 additional results do not make the omitted rows independent assays
      or create new written claims. No graph, pathway, root molecular-target or component
      applies, so no maintained-reader check is required.'
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2551-occurrence-owner
    - bgc-2551-mechanism-absence
    - bgc-2551-query-lotus_occurrences
    - bgc-2551-query-chebi_origins
    - bgc-2551-query-cyanometdb_occurrences
    - bgc-2551-query-pubchem_bioassay
    - bgc-2551-query-bindingdb_targets
    - bgc-2551-query-antibioticmech_inchikeys
    - bgc-2551-cached-taxonomy
    - bgc-2551-taxonomy-routes
    - bgc-2551-taxonomy-reading
    - bgc-2551-curation-scope
    - bgc-2551-bioactivity-seeder
    - bgc-2551-source-reading
    - bgc-2551-exclusion-table
    - bgc-2551-exclusion-implementation
    - bgc-2551-unresolved-taxa
    - bgc-2551-taxon-merged-input
    - bgc-2551-taxon-nonorganism-input
    - bgc-2551-source-pubchem_bioassay
  - name: assay_target_scope
    value: All 118 retained rows have blank activity_name and activity_value_um fields,
      so no quantitative endpoint or potency can be assigned from this inventory.
      The two Other rows name human suppressor of variegation 3-9 homolog 1 and retain
      NP_001269095 ungrounded, without a UniProt target or direct binding proof. The
      remaining rows describe NCI cell-growth contexts; the maintained title classifier
      explains the CYTOTOXIC labels but does not prove a molecular mechanism or clinical
      anticancer effect. Several Screening titles call 786-0, A498 or ACHN Non-Small
      Cell Lung while their Confirmatory titles say Renal; BT-549 likewise has conflicting
      Lung and Breast titles. Both deposited descriptions remain literal and unresolved.
      The retained exclusion scan found no exact applicable tuple; that does not validate
      the biological interpretation or authorize normalization of those tissue labels.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2551-occurrence-owner
    - bgc-2551-mechanism-absence
    - bgc-2551-query-lotus_occurrences
    - bgc-2551-query-chebi_origins
    - bgc-2551-query-cyanometdb_occurrences
    - bgc-2551-query-pubchem_bioassay
    - bgc-2551-query-bindingdb_targets
    - bgc-2551-query-antibioticmech_inchikeys
    - bgc-2551-cached-taxonomy
    - bgc-2551-taxonomy-routes
    - bgc-2551-taxonomy-reading
    - bgc-2551-curation-scope
    - bgc-2551-bioactivity-seeder
    - bgc-2551-source-reading
    - bgc-2551-exclusion-table
    - bgc-2551-exclusion-implementation
    - bgc-2551-unresolved-taxa
    - bgc-2551-taxon-merged-input
    - bgc-2551-taxon-nonorganism-input
    - bgc-2551-source-pubchem_bioassay
- assessment_id: bgc-2551-classification
  area: consistency
  topic: Reported model families and qualified applicability
  outcome: supported
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 reports Alkaloids
    and Amino acids and Peptides, Peptide alkaloids and Indole diketopiperazine alkaloids
    (L-Trp, L-Ala), with is_glycoside false. The nitrogen-rich paired diketopiperazine/indoline
    topology and absence of a candidate sugar ring support broad structural compatibility.
    The named L-residue precursor interpretation and natural stereochemistry are not
    established by this unspecified stored form. The two model pathways explain UNCLASSIFIED
    filing under the maintained seeder; the model, source NRPS label and experimental
    biosynthesis remain separate evidence categories.
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-classification-owner
  - bgc-2551-source-npclassifier
  - bgc-2551-chemistry
  - bgc-2551-topology
  - bgc-2551-structure-schema
  - bgc-2551-classification-seeder
  - bgc-2551-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: NPClassifier version npclassifier.gnps2.org@2026-09-07 reports Alkaloids
      and Amino acids and Peptides, Peptide alkaloids and Indole diketopiperazine
      alkaloids (L-Trp, L-Ala), with is_glycoside false. The nitrogen-rich paired
      diketopiperazine/indoline topology and absence of a candidate sugar ring support
      broad structural compatibility. The named L-residue precursor interpretation
      and natural stereochemistry are not established by this unspecified stored form.
      The two model pathways explain UNCLASSIFIED filing under the maintained seeder;
      the model, source NRPS label and experimental biosynthesis remain separate evidence
      categories.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2551-classification-owner
    - bgc-2551-source-npclassifier
    - bgc-2551-chemistry
    - bgc-2551-topology
    - bgc-2551-structure-schema
    - bgc-2551-classification-seeder
    - bgc-2551-source-mibig_compounds
- assessment_id: bgc-2551-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: All owner fields and three histories, all 42 actual canonical input placements,
    the complete saved molecular pair, 118 assay rows and the remaining retained source
    frames were read. The operative intake captures both taxonomy-query tables and
    all three curation/implementation diagnostics; the original collector/composer/notes
    remain historical 410/50 scope. Review completion is partial because full QC,
    complete ontology authority coverage, fresh external verification and natural
    stereochemical identity are unavailable. No record edit, new exclusion, native
    promotion or unsupported finding follows from the retained evidence.
  target_ids:
  - naturalproductmech:mibig-18e3a7edca
  evidence_ids:
  - bgc-2551-owner
  - bgc-2551-capture
  - bgc-2551-intake
  - bgc-2551-intake-acceptance
  - bgc-2551-history-owner
  - bgc-2551-diagnostic-reading
  - bgc-2551-diagnostic-acceptance
  - bgc-2551-diagnostic-execution
  - bgc-2551-source-reading
  - bgc-2551-joint-source-notes
  - bgc-2551-source-plan-execution
  - bgc-2551-source-plan-acceptance
  - bgc-2551-native-gate-limits
  - bgc-2551-curation-scope
  - bgc-2551-mechanism-absence
  - bgc-2551-exclusion-table
  - bgc-2551-exclusion-implementation
  - bgc-2551-unresolved-taxa
  - bgc-2551-taxon-merged-input
  - bgc-2551-taxon-nonorganism-input
  dimensions:
  - name: review_completion
    value: All owner fields and three histories, all 42 actual canonical input placements,
      the complete saved molecular pair, 118 assay rows and the remaining retained
      source frames were read. The operative intake captures both taxonomy-query tables
      and all three curation/implementation diagnostics; the original collector/composer/notes
      remain historical 410/50 scope. Review completion is partial because full QC,
      complete ontology authority coverage, fresh external verification and natural
      stereochemical identity are unavailable. No record edit, new exclusion, native
      promotion or unsupported finding follows from the retained evidence.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2551-owner
    - bgc-2551-capture
    - bgc-2551-intake
    - bgc-2551-intake-acceptance
    - bgc-2551-history-owner
    - bgc-2551-diagnostic-reading
    - bgc-2551-diagnostic-acceptance
    - bgc-2551-diagnostic-execution
    - bgc-2551-source-reading
    - bgc-2551-joint-source-notes
    - bgc-2551-source-plan-execution
    - bgc-2551-source-plan-acceptance
    - bgc-2551-native-gate-limits
    - bgc-2551-curation-scope
    - bgc-2551-mechanism-absence
    - bgc-2551-exclusion-table
    - bgc-2551-exclusion-implementation
    - bgc-2551-unresolved-taxa
    - bgc-2551-taxon-merged-input
    - bgc-2551-taxon-nonorganism-input
findings: []
actions: []
limitations:
- Eight atom centers remain unspecified; the natural stereoisomer and external CID
  representations were not independently verified.
- The 118 active retained rows have no numeric endpoint and include unresolved deposited
  tissue-title conflicts; activity does not establish direct target inhibition.
- Retained taxonomy labels/synonyms and source grades do not establish fresh lineage,
  producer experiments or a complete biosynthetic pathway.
- Full QC, OAK and external primary/database verification remain unavailable.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all ten first-five stored molecular forms (352 atom rows and
  396 bond rows) and 216 actual intake placements across 46 paths. No new molecular
  parse was performed.
- 'Disjoint retained-source reading: BGC first five, 45 frames/136 rows/1506 fields;
  Support last five, 45 frames/23 rows/248 fields. Four taxonomy merge rows remain
  separate. Native cache/curation receives zero positive inventory-row credit.'
- BGC operated the original collector/composer; Support operated canonical intakes;
  Native operated the original diagnostic under ROOT delegation. No maintained reader
  applies to these owners. Historical source access is not inherited as current primary
  verification.
- The original inventory/composer scope remains 410 placements/50 paths. The accepted
  taxonomy-query supplement and actual canonical intakes establish the operative 426/51
  scope without another source query or extra positive-row/AID credit.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-256
```
