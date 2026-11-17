# Local evidence review: andalusicin A

- Review: 20261105T004623Z-andalusicin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T23:57:06.234856Z
- Finished UTC: 2026-11-05T00:46:23.106367Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Andalusicin A retains a thioether-containing, unsaturated peptide encoding and a characterized BGC association. Fifteen unresolved tetrahedral centers and extensive representation-dependent amide/imidic differences prevent a complete stereochemical or natural-state conclusion; local evidence does not supply a native assay or independently verify the source strain and biosynthetic experiments.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2481; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1d37bf9b31 | data/natural_products/unclassified/andalusicin-a.yaml | generated | andalusicin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-1d37bf9b31 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-1d37bf9b31 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-1d37bf9b31 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-1d37bf9b31 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-1d37bf9b31 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-1d37bf9b31 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-1d37bf9b31 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-1d37bf9b31 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-1d37bf9b31.

The retained MIBiG BGC0002111 version 3 structure, full key HNFCMZRTSDWBCX-FFVXNQHYSA-N and C107H147N27O26S agree with the two saved normalized InChI results. That agreement preserves the deposited identity correspondence, not independent natural identity or a unique tautomer. ChEBI/full-key and assay joins are bounded to their saved frames. No direct one-hop companion was found by the declared census predicates; this does not establish chemical uniqueness.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-1d37bf9b31.

Both saved forms are neutral, with 161 atoms and 166 bonds; normalized InChI/full key and formula agree while both canonical SMILES comparisons are false and the direct atom map is empty. The stored SMILES has 24 carbonyl-amide sites; the regenerated InChI form has 23 C(OH)=N sites and retains one tertiary amide. These are explicit representation differences, not evidence of a source-ingestion error or the natural tautomer. Both forms retain 15 unspecified tetrahedral centers. Nine specified C=C elements in the SMILES coexist with four additional specified C=N elements and 19 unspecified C=N potentials in the regenerated form; those extra descriptors do not establish new experimental geometry. The literal stereo_complete:false remains appropriate.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-1d37bf9b31.

BGC0002111 version 3 records producer NCBITaxon:257985 with BGC_CHARACTERIZED and a separately CLUSTER_DEMONSTRATED locus at CP035727.2:3149977–3156657, with knockout, enzymatic, heterologous-expression and expression-correlation methods retained. The source label includes Bacillus thuringiensis serovar andalousiensis NRRL B-23139, while the saved cache name for257985 is the serovar without independently authenticating that strain label. The LOTUS Bacillus thuringiensis species occurrence at1428 remains separate. Database quality/complete flags and these method labels are retained evidence tiers, not a fresh review of experiments.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-1d37bf9b31.

The MIBiG ENTRY PMID34113822 and LOTUS DOI10.1016/J.ISCI.2021.102480 retain their entry and occurrence roles; overlapping article identity does not make their placements independent experiments. Both SEEDED_FROM_SOURCES events are read and preserved. There is no fresh primary-paper, isolate, sequence or experimental-protocol verification.

### Source-specific occurrence and assay assertions

evidence: supported. Targets: naturalproductmech:mibig-1d37bf9b31.

The retained LOTUS occurrence is detection context at the reported taxon and citation, not an additional causal producer assertion. The complete owner has no native bioactivity, causal graph, pathway, component-reference or molecular-target root, and the saved PubChem/BindingDB frames supply no actual assay. This bounded absence does not mean inactivity or absence of biological effects.

### Reported model families and bounded structural compatibility

consistency: supported. Targets: naturalproductmech:mibig-1d37bf9b31.

The versioned NPClassifier Amino acids and Peptides/Polyketides pathway arrays and Oligopeptides/RiPPs-Lanthipeptides labels remain model outputs, distinct from the source RIBOSOMAL category and UNCLASSIFIED filing. The sulfur-linked unsaturated peptide topology is compatible with a lanthipeptide-oriented interpretation, but motif compatibility does not independently establish the detailed biosynthesis or the model family. Exact source and model arrays remain separately cited.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-1d37bf9b31.

All source frames for this owner, both complete molecular forms, the canonical intake, raw owner/history and relevant cache stanzas are read. The four global diagnostic warnings are unassigned; no per-owner warning inference is made. Current retained evidence supports a partial review with unresolved stereochemistry and unavailable fresh primary/authority verification, without a demonstrated source-edit defect.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2481-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/andalusicin-a.yaml; Complete plaintext including every curation_history entry | supports | Complete andalusicin A owner with 2 history events; prior complete raw reading carries with current identical bytes. No source/status/history edit. |
| bgc-2481-capture | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2481-intake | /private/tmp/npm-review-work/shared-next-batch249/intakes/2481-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, ownership and all 37 input placements joined to current plan hashes. |
| bgc-2481-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/0 | supports | ROOT accepted the original canonical intake and exact supplemental plan; this owner’s actual inspection and receipt pins are located. |
| bgc-2481-grounding-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/grounding_notes | supports | Exact retained identifier, structure, source concepts, definition where present, cross-references and grounding fields. Historical annotations are not fresh authority searches. |
| bgc-2481-origin-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, declared coordinates and citation tiers; absent fields are not filled. |
| bgc-2481-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete owner supplies exact occurrence, activity and nested target assertions or bounded absence. Detection does not prove production; absent assays do not mean inactivity. |
| bgc-2481-classification-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | Exact named/versioned model arrays, glycoside flag, filing and separate source categories; retention fidelity is not biological-family or biosynthetic proof. |
| bgc-2481-history-owner | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0/owner_document/curation_status; /records/0/owner_document/curation_history | supports | All history events and status are preserved; seeding/import remains distinct from fresh primary verification. |
| bgc-2481-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets roots; no maintained reader applies. Its 0 native bioactivities and any nested target annotations remain separately retained. |
| bgc-2481-chemistry | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge; /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key; /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles; /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count; /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge; /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key; /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles; /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count; /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts; /records/0/inchi/computed/stereo_counts | supports | Eight of ten comparisons are true: normalized InChI/full key, formula, charge and atom/bond counts agree, but both canonical SMILES comparisons are false and direct atom correspondence is empty. Natural identity, tautomer preference and complete stereochemistry are not established by these booleans. |
| bgc-2481-topology | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs; /records/0/inchi/computed/fragment_atom_indices | supports | Complete paired tables contain 322 atom and 332 bond rows. The SMILES ring basis has sizes 5,6,11,13,5,6, with two indole systems, a thioether sulfur at atom41 bonded to carbons40 and42, 24 carbonyl-amide sites and no ester motif. The InChI form contains 23 C(OH)=N motifs; its remaining carbonyls include a tertiary amide and carboxylic acid. No saturated C5O six-cycle is detected. These exact topology observations support a sulfur-containing constrained peptide description but do not assign natural stereochemistry, biosynthetic enzyme action or a unique tautomer. |
| bgc-2481-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-first-five-diagnostic-reading-001.json; /records/0; /read_scope; /totals; /representation; /reading_caveats; /reader | supports | BGC personally read all ten complete first-five forms:604 atom and636 bond rows and all191 intake placements/47 paths. Whole Anditomin graph/history meanings factor to exact actual full-owner preservation; saved-result limits and display recovery are recorded. |
| bgc-2481-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/0; /molecular_parse_attempts; /parsed; /global_warning_count; /method_scope; /interpretation_boundary | supports | ROOT accepted the original twenty stored forms. This owner’s actual comparison scope is located; four warnings remain global and unassigned. No alternate parse or normalization repair is inferred. |
| bgc-2481-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins; stream interpretation is supplied separately. |
| bgc-2481-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–433 | supports | Undefined stereocenters remain explicit; named/versioned computed classification is never a source assertion. |
| bgc-2481-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines165–173 | supports | The maintained stereo_complete flag tests unassigned tetrahedral centers; natural identity and double-bond geometry need their separate evidence scopes. |
| bgc-2481-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines295–306;988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2481-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines126–145;1318–1382 | supports | Source assay calls, endpoint values and target accessions are retained. Activity classes use assay-name matching on active rows and summaries derive from written classes; these are not independent potency measurements or protocol validation. |
| bgc-2481-source-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-assigned-source-reading-001.json; /selected_indices; /reading; /counts; /frames; /cautions | supports | BGC personally read contexts0–3:36 complete frames/22 rows/225 fields, including the Anditomin blank-AID sentinel. This does not claim ROOT’s Antimycin source-row credit. |
| bgc-2481-root-source-reading | /private/tmp/npm-review-work/shared-next-batch249/root-current249-source-row-reading-001.json; /context_indices; /named_query_frames; /positive_row_placements; /positive_row_fields; /whole_payload_readings; /scientific_cautions | supports | ROOT personally read Antimycin A context4:9 complete frames/185 rows/1990 fields, including all172 assay rows. Attribution remains ROOT; no duplicate source-row credit. |
| bgc-2481-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Complete disjoint source reading covers90 frames/222 rows/2415 fields: BGC22, ROOT185 and Support15 rows. Native cache/curation has zero positive-row credit; overlapping readings add none. |
| bgc-2481-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch249/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /notes; /verification; /supplement_scope | supports | One original composer produced historical plan001 at379 placements/51 paths. Inventory and original source counts remain unchanged; the separate accepted supplement adds three A1B rule/transform inputs only. |
| bgc-2481-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch249/root-target-input-plan-acceptance-001.json; /status; /accepted; /plan; /original_plan; /supplement_derivation; /source_placements; /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification | supports | ROOT accepted supplemental plan002 at382 placements/54 paths. Only2486 gains three rule/transform inputs; no source query, context or positive-row count is added. |
| bgc-2481-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch249/root-current249-native-gates-acceptance-001.json; /status; /counts; /all_native_gates_passed; /unavailable | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed is false. Local validation does not complete scientific verification. |
| bgc-2481-curation-scope | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | The bounded Native scan found no applicable implemented correction/exclusion and26 unrelated lexical hits. No exact assay exclusion applies among172 retained tuples; one blank sentinel remains separate. |
| bgc-2481-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/17 | supports | Complete saved cache names and synonyms for this owner’s source taxon IDs. They do not independently validate taxonomic rank, source strain labels, occurrence or production; no fresh taxonomy lookup. |
| bgc-2481-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/source_taxa; /contexts/0/source_scope_inventory/forward_taxon_merge_matches; /contexts/0/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and saved forwarding/nonorganism routes for this owner; no fresh taxonomy request. |
| bgc-2481-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /forward_routes; /interpretation | supports | Native personally read all26 saved cache stanzas/10 routes, including67295→1911. Cached names/synonyms and routes do not upgrade species, strain, occurrence or producer evidence. |
| bgc-2481-direct-contexts | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | supports | Exact declared one-hop direct map is empty for this batch. Selected Antimycin identity comparison is separate; no transitive expansion or biological claim transfer is inferred. |
| bgc-2481-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2481-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines 2455–2455; row_sha256 02ea0543e4ee492c0cd86dadb8da2d1228240da9b6096182956df4283455b252 | supports | Exact compound/version, structure/key, database IDs, producer/locus grades and citation tiers. BGC complete source reading and current physical bytes are joined. |
| bgc-2481-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2481-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2481-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line1; physical lines 2524–2524; row_sha256 87bd55d4b4e211669fd2b561b6c1aad65b0ab681b4f035b4af5afc57683c50fd | supports | Complete organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. BGC complete source reading and current physical bytes are joined. |
| bgc-2481-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2481-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame has 1 placements with exact query, predicate and all matched fields. |
| bgc-2481-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines 864–864; row_sha256 7a013e76ce73e5416e8974820aa4ad91640daed096bf0dabf127575d8262f8fa | supports | Exact named/versioned model arrays and glycoside flag; applicability is assessed separately. BGC complete source reading and current physical bytes are joined. |
| bgc-2481-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2481-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2481-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame has 0 placements with exact query, predicate and all matched fields. |
| bgc-2481-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json; /contexts/0/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame has 0 placements with exact query, predicate and all matched fields. |
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
- All source frames for this owner, both complete molecular forms, the canonical intake, raw owner/history and relevant cache stanzas are read. The four global diagnostic warnings are unassigned; no per-owner warning inference is made. Current retained evidence supports a partial review with unresolved stereochemistry and unavailable fresh primary/authority verification, without a demonstrated source-edit defect.
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
review_id: 20261105T004623Z-andalusicin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: andalusicin A'
started_at: '2026-11-04T23:57:06.234856Z'
finished_at: '2026-11-05T00:46:23.106367Z'
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
summary: Andalusicin A retains a thioether-containing, unsaturated peptide encoding
  and a characterized BGC association. Fifteen unresolved tetrahedral centers and
  extensive representation-dependent amide/imidic differences prevent a complete stereochemical
  or natural-state conclusion; local evidence does not supply a native assay or independently
  verify the source strain and biosynthetic experiments.
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
  - path: data/natural_products/unclassified/andalusicin-a.yaml
    sha256: 5d0cc2f77e6b73be87229a9b72530dbc66b80c8cf4bcb089393545712e824e16
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
  selection: Campaign path order 2481; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1d37bf9b31
targets:
- target_id: naturalproductmech:mibig-1d37bf9b31
  path: data/natural_products/unclassified/andalusicin-a.yaml
  label: andalusicin A
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
  - naturalproductmech:mibig-1d37bf9b31
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
  - naturalproductmech:mibig-1d37bf9b31
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
  - naturalproductmech:mibig-1d37bf9b31
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
  - naturalproductmech:mibig-1d37bf9b31
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
  - naturalproductmech:mibig-1d37bf9b31
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
  - naturalproductmech:mibig-1d37bf9b31
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2481-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/andalusicin-a.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete andalusicin A owner with 2 history events; prior complete raw
    reading carries with current identical bytes. No source/status/history edit.
  snapshot_sha256: 5d0cc2f77e6b73be87229a9b72530dbc66b80c8cf4bcb089393545712e824e16
- evidence_id: bgc-2481-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/intakes/2481-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Actual canonical target, ownership and all 37 input placements joined to
    current plan hashes.
  snapshot_sha256: b356155fe9d8afc9a638e0b8afd95e26fc4081d83e2ae5fe50e38d32e71de2a8
- evidence_id: bgc-2481-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/0
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted the original canonical intake and exact supplemental plan;
    this owner’s actual inspection and receipt pins are located.
  snapshot_sha256: f4ee1f9dc4160c60cc3201b9246bb2ee1bd3ec750d96493dccd37dbd1725a6e5
- evidence_id: bgc-2481-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status;
    /records/0/owner_document/grounding_notes
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact retained identifier, structure, source concepts, definition where
    present, cross-references and grounding fields. Historical annotations are not
    fresh authority searches.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups;
    /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, declared coordinates
    and citation tiers; absent fields are not filled.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete owner supplies exact occurrence, activity and nested target assertions
    or bounded absence. Detection does not prove production; absent assays do not
    mean inactivity.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact named/versioned model arrays, glycoside flag, filing and separate
    source categories; retention fidelity is not biological-family or biosynthetic
    proof.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_status; /records/0/owner_document/curation_history
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: All history events and status are preserved; seeding/import remains distinct
    from fresh primary verification.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets roots; no maintained reader applies. Its 0 native bioactivities
    and any nested target annotations remain separately retained.
  snapshot_sha256: 91f3ee5d770560a302542def29139583ba13b4e3234fd3120bc02adeb3039ff6
- evidence_id: bgc-2481-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: 'Eight of ten comparisons are true: normalized InChI/full key, formula,
    charge and atom/bond counts agree, but both canonical SMILES comparisons are false
    and direct atom correspondence is empty. Natural identity, tautomer preference
    and complete stereochemistry are not established by these booleans.'
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2481-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds;
    /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices;
    /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings;
    /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs;
    /records/0/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete paired tables contain 322 atom and 332 bond rows. The SMILES ring
    basis has sizes 5,6,11,13,5,6, with two indole systems, a thioether sulfur at
    atom41 bonded to carbons40 and42, 24 carbonyl-amide sites and no ester motif.
    The InChI form contains 23 C(OH)=N motifs; its remaining carbonyls include a tertiary
    amide and carboxylic acid. No saturated C5O six-cycle is detected. These exact
    topology observations support a sulfur-containing constrained peptide description
    but do not assign natural stereochemistry, biosynthetic enzyme action or a unique
    tautomer.
  snapshot_sha256: 352a767f6e142ac6b3ecad138717d8d108483f61c6631a3480518d2a833285e5
- evidence_id: bgc-2481-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-first-five-diagnostic-reading-001.json
  locator: /records/0; /read_scope; /totals; /representation; /reading_caveats; /reader
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: BGC personally read all ten complete first-five forms:604 atom and636 bond
    rows and all191 intake placements/47 paths. Whole Anditomin graph/history meanings
    factor to exact actual full-owner preservation; saved-result limits and display
    recovery are recorded.
  snapshot_sha256: 8f02ce5ed547abe9ee3e3738e23cec650136884c62b12e64de9dc31dfa480a63
- evidence_id: bgc-2481-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/0; /molecular_parse_attempts; /parsed;
    /global_warning_count; /method_scope; /interpretation_boundary
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: ROOT accepted the original twenty stored forms. This owner’s actual comparison
    scope is located; four warnings remain global and unassigned. No alternate parse
    or normalization repair is inferred.
  snapshot_sha256: 85f657ea1d785c1aca4e78bdcf54056041799b0913a9df5155fb43b6ed51e491
- evidence_id: bgc-2481-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins;
    stream interpretation is supplied separately.
  snapshot_sha256: 7955c4e94046cc4fedde2ebda7bd56f32eb9cb544f5367b1955b30ae11d58c88
- evidence_id: bgc-2481-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–433
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Undefined stereocenters remain explicit; named/versioned computed classification
    is never a source assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2481-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines165–173
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: The maintained stereo_complete flag tests unassigned tetrahedral centers;
    natural identity and double-bond geometry need their separate evidence scopes.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2481-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines295–306;988–1022
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while model arrays
    remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2481-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines126–145;1318–1382
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Source assay calls, endpoint values and target accessions are retained.
    Activity classes use assay-name matching on active rows and summaries derive from
    written classes; these are not independent potency measurements or protocol validation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2481-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-current249-assigned-source-reading-001.json
  locator: /selected_indices; /reading; /counts; /frames; /cautions
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: BGC personally read contexts0–3:36 complete frames/22 rows/225 fields,
    including the Anditomin blank-AID sentinel. This does not claim ROOT’s Antimycin
    source-row credit.
  snapshot_sha256: 8204ce76b856283f97da2268d1a5738b9616c5da78d6a2996ffb2b5bfce43737
- evidence_id: bgc-2481-root-source-reading
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
- evidence_id: bgc-2481-joint-source-notes
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
- evidence_id: bgc-2481-source-plan-execution
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
- evidence_id: bgc-2481-source-plan-acceptance
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
- evidence_id: bgc-2481-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249/root-current249-native-gates-acceptance-001.json
  locator: /status; /counts; /all_native_gates_passed; /unavailable
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    is false. Local validation does not complete scientific verification.
  snapshot_sha256: 7c4057fa2e4c45bd5339590edd15f460011ae95df0211342b097be1e9b76b94a
- evidence_id: bgc-2481-curation-scope
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
- evidence_id: bgc-2481-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/17
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source taxon IDs.
    They do not independently validate taxonomic rank, source strain labels, occurrence
    or production; no fresh taxonomy lookup.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2481-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/source_taxa; /contexts/0/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/0/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact source taxon IDs and saved forwarding/nonorganism routes for this
    owner; no fresh taxonomy request.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
- evidence_id: bgc-2481-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/native-prep/native-current249-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /forward_routes; /interpretation
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Native personally read all26 saved cache stanzas/10 routes, including67295→1911.
    Cached names/synonyms and routes do not upgrade species, strain, occurrence or
    producer evidence.
  snapshot_sha256: 781f62e73b1694225f8ccdca96b95bbc58bea281997f4ef1152a7ccf2d5ecc88
- evidence_id: bgc-2481-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-target-input-plan-002.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact declared one-hop direct map is empty for this batch. Selected Antimycin
    identity comparison is separate; no transitive expansion or biological claim transfer
    is inferred.
  snapshot_sha256: 4c92dba7f8c9b89c7fe05a9e64e3721282d76814855c144975ff46e930b901b0
- evidence_id: bgc-2481-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved mibig_compounds frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines 2455–2455; row_sha256 02ea0543e4ee492c0cd86dadb8da2d1228240da9b6096182956df4283455b252
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact compound/version, structure/key, database IDs, producer/locus grades
    and citation tiers. BGC complete source reading and current physical bytes are
    joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2481-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved chebi_structures frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved lotus_occurrences frame has 1 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line1; physical lines 2524–2524; row_sha256 87bd55d4b4e211669fd2b561b6c1aad65b0ab681b4f035b4af5afc57683c50fd
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. BGC complete
    source reading and current physical bytes are joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2481-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved npclassifier frame has 1 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching payload or the empty
    frame is retained; no query replay.
- evidence_id: bgc-2481-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines 864–864; row_sha256 7a013e76ce73e5416e8974820aa4ad91640daed096bf0dabf127575d8262f8fa
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; applicability is
    assessed separately. BGC complete source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2481-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved bindingdb_targets frame has 0 placements with exact query,
    predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every matching
    payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame has 0 placements with exact
    query, predicate and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "HNFCMZRTSDWBCX-FFVXNQHYSA-N". Every
    matching payload or the empty frame is retained; no query replay.
- evidence_id: bgc-2481-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch249-tentative/bgc-prep/bgc-conditional249-source-inventory-DATA-001.json
  locator: /contexts/0/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T00:35:04.253743Z'
  support: supports
  summary: Complete saved chebi_origins frame has 0 placements with exact query, predicate
    and all matched fields.
  snapshot_sha256: be580601c6c6f02f9af67de677ebe33ad891e74cb2aabd86ef75435bc77ba434
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Every matching payload or the empty frame
    is retained; no query replay.
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
- assessment_id: bgc-2481-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: The retained MIBiG BGC0002111 version 3 structure, full key HNFCMZRTSDWBCX-FFVXNQHYSA-N
    and C107H147N27O26S agree with the two saved normalized InChI results. That agreement
    preserves the deposited identity correspondence, not independent natural identity
    or a unique tautomer. ChEBI/full-key and assay joins are bounded to their saved
    frames. No direct one-hop companion was found by the declared census predicates;
    this does not establish chemical uniqueness.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-grounding-owner
  - bgc-2481-chemistry
  - bgc-2481-source-mibig_compounds
  - bgc-2481-query-chebi_structures
  - bgc-2481-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: HNFCMZRTSDWBCX-FFVXNQHYSA-N; retained key, not natural-identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2481-grounding-owner
    - bgc-2481-chemistry
    - bgc-2481-source-mibig_compounds
    - bgc-2481-query-chebi_structures
    - bgc-2481-direct-contexts
  - name: grounding_scope
    value: The retained MIBiG BGC0002111 version 3 structure, full key HNFCMZRTSDWBCX-FFVXNQHYSA-N
      and C107H147N27O26S agree with the two saved normalized InChI results. That
      agreement preserves the deposited identity correspondence, not independent natural
      identity or a unique tautomer. ChEBI/full-key and assay joins are bounded to
      their saved frames. No direct one-hop companion was found by the declared census
      predicates; this does not establish chemical uniqueness.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2481-grounding-owner
    - bgc-2481-chemistry
    - bgc-2481-source-mibig_compounds
    - bgc-2481-query-chebi_structures
    - bgc-2481-direct-contexts
- assessment_id: bgc-2481-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: Both saved forms are neutral, with 161 atoms and 166 bonds; normalized
    InChI/full key and formula agree while both canonical SMILES comparisons are false
    and the direct atom map is empty. The stored SMILES has 24 carbonyl-amide sites;
    the regenerated InChI form has 23 C(OH)=N sites and retains one tertiary amide.
    These are explicit representation differences, not evidence of a source-ingestion
    error or the natural tautomer. Both forms retain 15 unspecified tetrahedral centers.
    Nine specified C=C elements in the SMILES coexist with four additional specified
    C=N elements and 19 unspecified C=N potentials in the regenerated form; those
    extra descriptors do not establish new experimental geometry. The literal stereo_complete:false
    remains appropriate.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-grounding-owner
  - bgc-2481-chemistry
  - bgc-2481-topology
  - bgc-2481-diagnostic-reading
  - bgc-2481-diagnostic-acceptance
  - bgc-2481-structure-schema
  - bgc-2481-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms are neutral, with 161 atoms and 166 bonds; normalized
      InChI/full key and formula agree while both canonical SMILES comparisons are
      false and the direct atom map is empty. The stored SMILES has 24 carbonyl-amide
      sites; the regenerated InChI form has 23 C(OH)=N sites and retains one tertiary
      amide. These are explicit representation differences, not evidence of a source-ingestion
      error or the natural tautomer. Both forms retain 15 unspecified tetrahedral
      centers. Nine specified C=C elements in the SMILES coexist with four additional
      specified C=N elements and 19 unspecified C=N potentials in the regenerated
      form; those extra descriptors do not establish new experimental geometry. The
      literal stereo_complete:false remains appropriate.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2481-grounding-owner
    - bgc-2481-chemistry
    - bgc-2481-topology
    - bgc-2481-diagnostic-reading
    - bgc-2481-diagnostic-acceptance
    - bgc-2481-structure-schema
    - bgc-2481-stereo-method
  - name: representation_correspondence
    value: 'Eight of ten comparisons are true: normalized InChI/full key, formula,
      charge and atom/bond counts agree, but both canonical SMILES comparisons are
      false and direct atom correspondence is empty. Natural identity, tautomer preference
      and complete stereochemistry are not established by these booleans.'
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2481-grounding-owner
    - bgc-2481-chemistry
    - bgc-2481-topology
    - bgc-2481-diagnostic-reading
    - bgc-2481-diagnostic-acceptance
    - bgc-2481-structure-schema
    - bgc-2481-stereo-method
- assessment_id: bgc-2481-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: BGC0002111 version 3 records producer NCBITaxon:257985 with BGC_CHARACTERIZED
    and a separately CLUSTER_DEMONSTRATED locus at CP035727.2:3149977–3156657, with
    knockout, enzymatic, heterologous-expression and expression-correlation methods
    retained. The source label includes Bacillus thuringiensis serovar andalousiensis
    NRRL B-23139, while the saved cache name for257985 is the serovar without independently
    authenticating that strain label. The LOTUS Bacillus thuringiensis species occurrence
    at1428 remains separate. Database quality/complete flags and these method labels
    are retained evidence tiers, not a fresh review of experiments.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-origin-owner
  - bgc-2481-occurrence-owner
  - bgc-2481-source-mibig_compounds
  - bgc-2481-cached-taxonomy
  - bgc-2481-taxonomy-routes
  - bgc-2481-curation-scope
  - bgc-2481-direct-contexts
  - bgc-2481-source-lotus_occurrences
  dimensions:
  - name: taxon_scope
    value: BGC0002111 version 3 records producer NCBITaxon:257985 with BGC_CHARACTERIZED
      and a separately CLUSTER_DEMONSTRATED locus at CP035727.2:3149977–3156657, with
      knockout, enzymatic, heterologous-expression and expression-correlation methods
      retained. The source label includes Bacillus thuringiensis serovar andalousiensis
      NRRL B-23139, while the saved cache name for257985 is the serovar without independently
      authenticating that strain label. The LOTUS Bacillus thuringiensis species occurrence
      at1428 remains separate. Database quality/complete flags and these method labels
      are retained evidence tiers, not a fresh review of experiments.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2481-origin-owner
    - bgc-2481-occurrence-owner
    - bgc-2481-source-mibig_compounds
    - bgc-2481-cached-taxonomy
    - bgc-2481-taxonomy-routes
    - bgc-2481-curation-scope
    - bgc-2481-direct-contexts
    - bgc-2481-source-lotus_occurrences
  - name: producer_evidence
    value: BGC0002111 version 3 records producer NCBITaxon:257985 with BGC_CHARACTERIZED
      and a separately CLUSTER_DEMONSTRATED locus at CP035727.2:3149977–3156657, with
      knockout, enzymatic, heterologous-expression and expression-correlation methods
      retained. The source label includes Bacillus thuringiensis serovar andalousiensis
      NRRL B-23139, while the saved cache name for257985 is the serovar without independently
      authenticating that strain label. The LOTUS Bacillus thuringiensis species occurrence
      at1428 remains separate. Database quality/complete flags and these method labels
      are retained evidence tiers, not a fresh review of experiments.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2481-origin-owner
    - bgc-2481-occurrence-owner
    - bgc-2481-source-mibig_compounds
    - bgc-2481-cached-taxonomy
    - bgc-2481-taxonomy-routes
    - bgc-2481-curation-scope
    - bgc-2481-direct-contexts
    - bgc-2481-source-lotus_occurrences
  - name: locus_evidence
    value: BGC0002111 version 3 records producer NCBITaxon:257985 with BGC_CHARACTERIZED
      and a separately CLUSTER_DEMONSTRATED locus at CP035727.2:3149977–3156657, with
      knockout, enzymatic, heterologous-expression and expression-correlation methods
      retained. The source label includes Bacillus thuringiensis serovar andalousiensis
      NRRL B-23139, while the saved cache name for257985 is the serovar without independently
      authenticating that strain label. The LOTUS Bacillus thuringiensis species occurrence
      at1428 remains separate. Database quality/complete flags and these method labels
      are retained evidence tiers, not a fresh review of experiments.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2481-origin-owner
    - bgc-2481-occurrence-owner
    - bgc-2481-source-mibig_compounds
    - bgc-2481-cached-taxonomy
    - bgc-2481-taxonomy-routes
    - bgc-2481-curation-scope
    - bgc-2481-direct-contexts
    - bgc-2481-source-lotus_occurrences
- assessment_id: bgc-2481-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: The MIBiG ENTRY PMID34113822 and LOTUS DOI10.1016/J.ISCI.2021.102480 retain
    their entry and occurrence roles; overlapping article identity does not make their
    placements independent experiments. Both SEEDED_FROM_SOURCES events are read and
    preserved. There is no fresh primary-paper, isolate, sequence or experimental-protocol
    verification.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-owner
  - bgc-2481-history-owner
  - bgc-2481-origin-owner
  - bgc-2481-occurrence-owner
  - bgc-2481-source-mibig_compounds
  - bgc-2481-source-reading
  - bgc-2481-root-source-reading
  - bgc-2481-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: The MIBiG ENTRY PMID34113822 and LOTUS DOI10.1016/J.ISCI.2021.102480 retain
      their entry and occurrence roles; overlapping article identity does not make
      their placements independent experiments. Both SEEDED_FROM_SOURCES events are
      read and preserved. There is no fresh primary-paper, isolate, sequence or experimental-protocol
      verification.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2481-owner
    - bgc-2481-history-owner
    - bgc-2481-origin-owner
    - bgc-2481-occurrence-owner
    - bgc-2481-source-mibig_compounds
    - bgc-2481-source-reading
    - bgc-2481-root-source-reading
    - bgc-2481-source-lotus_occurrences
- assessment_id: bgc-2481-occurrence
  area: evidence
  topic: Source-specific occurrence and assay assertions
  outcome: supported
  summary: The retained LOTUS occurrence is detection context at the reported taxon
    and citation, not an additional causal producer assertion. The complete owner
    has no native bioactivity, causal graph, pathway, component-reference or molecular-target
    root, and the saved PubChem/BindingDB frames supply no actual assay. This bounded
    absence does not mean inactivity or absence of biological effects.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-occurrence-owner
  - bgc-2481-mechanism-absence
  - bgc-2481-query-lotus_occurrences
  - bgc-2481-query-chebi_origins
  - bgc-2481-query-cyanometdb_occurrences
  - bgc-2481-query-pubchem_bioassay
  - bgc-2481-query-bindingdb_targets
  - bgc-2481-query-antibioticmech_inchikeys
  - bgc-2481-cached-taxonomy
  - bgc-2481-taxonomy-routes
  - bgc-2481-taxonomy-reading
  - bgc-2481-curation-scope
  - bgc-2481-bioactivity-seeder
  - bgc-2481-root-source-reading
  - bgc-2481-source-lotus_occurrences
  dimensions:
  - name: occurrence_scope
    value: The retained LOTUS occurrence is detection context at the reported taxon
      and citation, not an additional causal producer assertion. The complete owner
      has no native bioactivity, causal graph, pathway, component-reference or molecular-target
      root, and the saved PubChem/BindingDB frames supply no actual assay. This bounded
      absence does not mean inactivity or absence of biological effects.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2481-occurrence-owner
    - bgc-2481-mechanism-absence
    - bgc-2481-query-lotus_occurrences
    - bgc-2481-query-chebi_origins
    - bgc-2481-query-cyanometdb_occurrences
    - bgc-2481-query-pubchem_bioassay
    - bgc-2481-query-bindingdb_targets
    - bgc-2481-query-antibioticmech_inchikeys
    - bgc-2481-cached-taxonomy
    - bgc-2481-taxonomy-routes
    - bgc-2481-taxonomy-reading
    - bgc-2481-curation-scope
    - bgc-2481-bioactivity-seeder
    - bgc-2481-root-source-reading
    - bgc-2481-source-lotus_occurrences
  - name: assay_target_scope
    value: No native assay or exact saved AID/BindingDB match is available for this
      selected owner. Activity, potency and targets are not transferred from the BGC,
      a taxonomic label or a peptide-family expectation.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2481-occurrence-owner
    - bgc-2481-mechanism-absence
    - bgc-2481-query-lotus_occurrences
    - bgc-2481-query-chebi_origins
    - bgc-2481-query-cyanometdb_occurrences
    - bgc-2481-query-pubchem_bioassay
    - bgc-2481-query-bindingdb_targets
    - bgc-2481-query-antibioticmech_inchikeys
    - bgc-2481-cached-taxonomy
    - bgc-2481-taxonomy-routes
    - bgc-2481-taxonomy-reading
    - bgc-2481-curation-scope
    - bgc-2481-bioactivity-seeder
    - bgc-2481-root-source-reading
    - bgc-2481-source-lotus_occurrences
- assessment_id: bgc-2481-classification
  area: consistency
  topic: Reported model families and bounded structural compatibility
  outcome: supported
  summary: The versioned NPClassifier Amino acids and Peptides/Polyketides pathway
    arrays and Oligopeptides/RiPPs-Lanthipeptides labels remain model outputs, distinct
    from the source RIBOSOMAL category and UNCLASSIFIED filing. The sulfur-linked
    unsaturated peptide topology is compatible with a lanthipeptide-oriented interpretation,
    but motif compatibility does not independently establish the detailed biosynthesis
    or the model family. Exact source and model arrays remain separately cited.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-classification-owner
  - bgc-2481-source-npclassifier
  - bgc-2481-chemistry
  - bgc-2481-topology
  - bgc-2481-structure-schema
  - bgc-2481-classification-seeder
  - bgc-2481-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: The versioned NPClassifier Amino acids and Peptides/Polyketides pathway
      arrays and Oligopeptides/RiPPs-Lanthipeptides labels remain model outputs, distinct
      from the source RIBOSOMAL category and UNCLASSIFIED filing. The sulfur-linked
      unsaturated peptide topology is compatible with a lanthipeptide-oriented interpretation,
      but motif compatibility does not independently establish the detailed biosynthesis
      or the model family. Exact source and model arrays remain separately cited.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2481-classification-owner
    - bgc-2481-source-npclassifier
    - bgc-2481-chemistry
    - bgc-2481-topology
    - bgc-2481-structure-schema
    - bgc-2481-classification-seeder
    - bgc-2481-source-mibig_compounds
- assessment_id: bgc-2481-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: All source frames for this owner, both complete molecular forms, the canonical
    intake, raw owner/history and relevant cache stanzas are read. The four global
    diagnostic warnings are unassigned; no per-owner warning inference is made. Current
    retained evidence supports a partial review with unresolved stereochemistry and
    unavailable fresh primary/authority verification, without a demonstrated source-edit
    defect.
  target_ids:
  - naturalproductmech:mibig-1d37bf9b31
  evidence_ids:
  - bgc-2481-owner
  - bgc-2481-capture
  - bgc-2481-intake
  - bgc-2481-intake-acceptance
  - bgc-2481-history-owner
  - bgc-2481-diagnostic-reading
  - bgc-2481-diagnostic-acceptance
  - bgc-2481-diagnostic-execution
  - bgc-2481-source-reading
  - bgc-2481-root-source-reading
  - bgc-2481-joint-source-notes
  - bgc-2481-source-plan-execution
  - bgc-2481-source-plan-acceptance
  - bgc-2481-native-gate-limits
  - bgc-2481-curation-scope
  - bgc-2481-mechanism-absence
  dimensions:
  - name: review_completion
    value: All source frames for this owner, both complete molecular forms, the canonical
      intake, raw owner/history and relevant cache stanzas are read. The four global
      diagnostic warnings are unassigned; no per-owner warning inference is made.
      Current retained evidence supports a partial review with unresolved stereochemistry
      and unavailable fresh primary/authority verification, without a demonstrated
      source-edit defect.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2481-owner
    - bgc-2481-capture
    - bgc-2481-intake
    - bgc-2481-intake-acceptance
    - bgc-2481-history-owner
    - bgc-2481-diagnostic-reading
    - bgc-2481-diagnostic-acceptance
    - bgc-2481-diagnostic-execution
    - bgc-2481-source-reading
    - bgc-2481-root-source-reading
    - bgc-2481-joint-source-notes
    - bgc-2481-source-plan-execution
    - bgc-2481-source-plan-acceptance
    - bgc-2481-native-gate-limits
    - bgc-2481-curation-scope
    - bgc-2481-mechanism-absence
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
- All source frames for this owner, both complete molecular forms, the canonical intake,
  raw owner/history and relevant cache stanzas are read. The four global diagnostic
  warnings are unassigned; no per-owner warning inference is made. Current retained
  evidence supports a partial review with unresolved stereochemistry and unavailable
  fresh primary/authority verification, without a demonstrated source-edit defect.
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
