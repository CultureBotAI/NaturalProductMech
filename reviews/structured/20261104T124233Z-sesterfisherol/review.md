# Local evidence review: sesterfisherol

- Review: 20261104T124233Z-sesterfisherol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T11:41:40.730774Z
- Finished UTC: 2026-11-04T12:42:33.147064Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Sesterfisherol retains exact local ChEBI/full-key grounding and consistent C25H42O forms with eight specified tetrahedral centers and one Z alkene. Its one-step NfSS mechanism explicitly leaves downstream oxidation unexpanded; its one original maintained call is accepted and preserves the complete owner. The Diterpenoids/Fusicoccane model label is a bounded applicability concern, while producer, locus and occurrence roles remain separate.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2395; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:138046 | data/natural_products/terpenoids/sesterfisherol.yaml | generated | sesterfisherol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for sesterfisherol | passed | True | CHEBI:138046 | One original offline maintained call preserved the complete captured owner, graph, pathway and history. Primary mechanism, protein/construct, natural-identity and stereochemical validity are outside this check. |
| strict_ten | passed | True | CHEBI:138046 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:138046 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:138046 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:138046 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:138046 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:138046 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:138046 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:138046 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity/form consistency; natural identity unverified

identity: supported. Targets: CHEBI:138046.

CHEBI:138046 and full key VQMHZILKNHUAMP-AISFCYSSSA-N join the retained three-star ChEBI concept and MIBiG BGC0002162 v3, with NPA032823 preserved. The owner remains EXACT/SEEDED and the structure remains MIBiG-sourced. Both stored forms yield neutral C25H42O and the declared key. The ChEBI definition describes a tetracyclic sesterterpenoid and attributes its production to gene-cluster expression; that is a saved database definition, not fresh primary verification. The related acid and four numbered compounds are not alternate identities.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: CHEBI:138046.

Both complete forms have 26 heavy atoms, 29 bonds, eight specified tetrahedral centers and one specified Z double bond. All ten saved comparisons are true. The methyl-bearing center has an R CIP assignment; comparison to the acid-bearing S center does not itself demonstrate a stereochemical inversion because substitution priorities change. The original one-match atom correspondence covers all atoms but retains full_graph_identity_established:false, and no natural stereoisomer is independently authenticated.

### Separate source producer, locus and curation scope

provenance: supported. Targets: CHEBI:138046.

MIBiG BGC0002162 v3 retains Aspergillus fischeri NRRL 181, NCBITaxon:331117, as SOURCE_ASSERTION. Heterologous expression separately grades DS027698.1:2485363–2490827 as CLUSTER_DEMONSTRATED. A demonstrated heterologous locus does not automatically strengthen native-producer evidence. No applicable correction appears in the bounded implemented-curation scan; the Sodorifen override is unrelated.

### Citation placement and historical attribution

evidence: supported. Targets: CHEBI:138046.

DOI:10.1021/jacs.5b08319 is the MIBiG compound-evidence reference and its uppercase LOTUS variant is occurrence provenance. The historical NfSS pathway/graph attributes primary-experiment snippets to that DOI and separate mappings to retained MIBiG, UniProt and Rhea pages dated 2026-09-30. Reading those saved excerpts and notes does not mean the primary article or live records were freshly opened. Eight edge references plus four step references repeat evidence rather than representing twelve independent experiments.

### Occurrence and retained assay/target scope

evidence: supported. Targets: CHEBI:138046.

The one written LOTUS occurrence is Aspergillus flavus, NCBITaxon:5059, rather than the A. fischeri NRRL 181 producer. The exact ChEBI-origin query for CHEBI:138046 is empty and adds no organism assertion. The owner has no bioactivities, bioactivity_summary or molecular_targets; exact PubChem and BindingDB joins are empty. Source/cache labels preserve these separate roles without fresh taxonomy, production or inactivity inference.

### Versioned model applicability and source distinctions

consistency: concern. Targets: CHEBI:138046.

The retained NPClassifier output at npclassifier.gnps2.org@2026-09-07 is Terpenoids/Diterpenoids/Fusicoccane diterpenoids with is_glycoside:false. The C25 structure, ChEBI sesterterpenoid definition and historically attributed GFPP cyclization expose a bounded applicability concern for the more specific Diterpenoids/Fusicoccane prediction. Faithful model ingestion and broad TERPENOIDS filing are not thereby erroneous, and no replacement prediction is supplied. The nonglycoside flag is compatible with the saved topology.

### Preserved historical biosynthetic mechanism; primary claims unverified

consistency: unknown. Targets: CHEBI:138046.

One three-node/two-edge BIOSYNTHESIS graph and pathway step 1 retain CHEBI:57907 through NfSS/UniProtKB:A1DN30 to CHEBI:138046, with RHEA:54068. The step explicitly leaves downstream NfP450/A1DN29 oxidation to sesterfisheric acid unexpanded; it must not acquire the acid owner’s second step by shared-locus inference. All evidence, optional-field absences and three history events remain part of the local view. The accepted original maintained call returned exactly the complete captured owner, preserving every graph/pathway/evidence/history field and all optional-field absences. It had no components, unexpected denials or errors; the one known socket-construction capability probe was blocked before action. Preservation is not fresh scientific verification.

### Historically attributed protein/construct scope

identity: unknown. Targets: CHEBI:138046.

The retained NfSS mapping joins UniProtKB:A1DN30, NFIA_055500 and GenPept EAW16201.1; its database note describes a reviewed 764-amino-acid protein and a bifunctional synthase/cyclase context. These remain historical attributions, not fresh sequence/domain, construct/tag or accession verification. The saved reaction’s water/diphosphate description does not establish a newly inspected stoichiometric or cofactor experiment.

### Actual evidence coverage and remaining scientific limits

completeness: unknown. Targets: CHEBI:138046.

Complete raw/history, retained source payloads, actual intake, both molecular forms and the actual maintained-reader result have been read. The accepted original call preserves the complete single-step mechanism and all three history events. Full QC/OAK, fresh primary/source, protein/construct and taxonomic verification, and independent natural-identity confirmation remain unavailable. This is a partial review with no supported record-edit finding; the model-applicability concern does not authorize replacing a faithful prediction.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2395-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/sesterfisherol.yaml; Whole current plaintext and complete curation_history | supports | Complete sesterfisherol owner and 3 history events, with the unchanged native EXACT/SEEDED statuses. Prior full raw reading is carried; no record edit. |
| bgc-2395-capture | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4 | supports | Complete actual captured owner, exact root presence, mechanism projection and history; no scientific claim is inferred solely from counts. |
| bgc-2395-intake | /private/tmp/npm-review-work/shared-next-batch240/intakes/2395-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, all 44 source placements and complete ownership roles. Generated records/pages are not independent correction owners. |
| bgc-2395-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch240/root-intake-acceptance-001.json; /status | supports | ROOT acceptance of the actual ten canonical intakes; complete per-owner inputs are separately linked in this record intake. |
| bgc-2395-grounding-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/label; /records/4/owner_document/chemical_structure; /records/4/owner_document/grounding_status; /records/4/owner_document/definition; /records/4/owner_document/definition_source; /records/4/owner_document/xrefs; /records/4/owner_document/source_concepts; /records/4/owner_document | supports | Retained identifier, label, exact structure, grounding/source concepts and present cross-references; definition is present as a ChEBI attribution. |
| bgc-2395-origin-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4/owner_document/biosynthesis_origin; /records/4/owner_document/producer_taxon_groups; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters; /records/4/owner_document/source_concepts | supports | Exact owner producer/locus/source concepts and separate evidence grades, reference placements and available coordinate fields; no fresh source validation. |
| bgc-2395-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4/owner_document/occurrences; /records/4/owner_document/occurrence_taxon_groups; /records/4/owner_document | supports | The owner retains 1 occurrence placements. Bioactivities, bioactivity_summary and molecular_targets are absent. This owner-only evidence makes no saved-query or curation claim. |
| bgc-2395-classification-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4/owner_document/np_pathway; /records/4/owner_document/np_classification; /records/4/owner_document/bgc_class; /records/4/owner_document | supports | Exact retained model version/pathway/superclass/class/glycoside output and separate source BGC class fields; computed specificity is not independently validated here. |
| bgc-2395-history-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4/owner_document/curation_status; /records/4/owner_document/curation_history | supports | Complete unchanged curation_status and curation_history, including seeded and any historically curated events; review status is not promoted. |
| bgc-2395-mechanism-owner | /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json; /records/4/owner_document/causal_graphs; /records/4/owner_document/biosynthetic_pathway; /records/4/owner_document | supports | Complete retained graph/pathway semantics and optional-field absences. |
| bgc-2395-chemistry | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json; /records/4/declared_structure; /records/4/literal_InChI_layers; /records/4/comparisons; /records/4/atom_correspondence; /records/4/smiles/computed/formula; /records/4/smiles/computed/formal_charge; /records/4/smiles/computed/standard_inchi; /records/4/smiles/computed/standard_inchi_key; /records/4/smiles/computed/canonical_isomeric_smiles; /records/4/smiles/computed/canonical_nonisomeric_smiles; /records/4/smiles/computed/atom_count; /records/4/smiles/computed/heavy_atom_count; /records/4/smiles/computed/bond_count; /records/4/smiles/computed/element_counts; /records/4/smiles/computed/stereo_counts; /records/4/inchi/computed/formula; /records/4/inchi/computed/formal_charge; /records/4/inchi/computed/standard_inchi; /records/4/inchi/computed/standard_inchi_key; /records/4/inchi/computed/canonical_isomeric_smiles; /records/4/inchi/computed/canonical_nonisomeric_smiles; /records/4/inchi/computed/atom_count; /records/4/inchi/computed/heavy_atom_count; /records/4/inchi/computed/bond_count; /records/4/inchi/computed/element_counts; /records/4/inchi/computed/stereo_counts | supports | Both complete saved representations preserve the exact formula/charge/full key/canonical forms and stereo counts. All ten comparison flags are true; original full_graph_identity_established remains false. |
| bgc-2395-topology | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings; /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/motifs; /records/4/smiles/computed/fragment_atom_indices; /records/4/inchi/computed/atoms; /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/potential_stereo; /records/4/inchi/computed/motifs; /records/4/inchi/computed/fragment_atom_indices | supports | The saved graph contains four independent carbocyclic rings with path sizes 8, 5, 6 and 5 and a single tertiary alcohol. It has no carbonyl, ether bridge or candidate sugar cycle. These features are compatible with the retained tetracyclic alcohol description, without independently establishing the natural skeleton, enzymatic product or biochemical atom numbering. |
| bgc-2395-congener-stereo-context | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed/atoms; /records/3/inchi/computed/atoms; /records/4/smiles/computed/atoms; /records/4/inchi/computed/atoms | supports | Complete saved acid/alcohol atom tables retain the distinct S acid-bearing and R methyl-bearing CIP labels; a congener letter contrast alone is not an epimerization witness. |
| bgc-2395-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-current240-first-five-diagnostic-reading-001.json; /records/4; /coverage; /lossless_reading_method; /limits | supports | BGC personally read every assigned stored-form field, all 234 atom and 254 bond rows across the first five, with exact shared-value/constant-column factoring and bounded original atom maps. |
| bgc-2395-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /warning_count; /warning_record_attribution; /limits | supports | Accepted one original diagnostic; four charge-rearrangement warnings remain global/unassigned and limitations remain explicit. |
| bgc-2395-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Original diagnostic execution, source and exact saved output streams; no new parse or runtime is performed by scientific authoring. |
| bgc-2395-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 381–430 | supports | Schema distinguishes retained exact-key/structure stereochemistry and versioned computed classification; model values are not source assertions. |
| bgc-2395-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 155–173 | supports | Maintained extractor derives the saved flag from unassigned chiral centers in its original molecular input. The flag is not fresh experimental stereochemical validation. |
| bgc-2395-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1019 | supports | Maintained seeder preserves the chosen source structure/flag and exact named/versioned classifier outputs; filing follows its result-array rule. |
| bgc-2395-source-reading | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-current240-source-reading-001.json; /scope; /reading; /finite; /cautions | supports | BGC complete assigned 30-context reading covers 123 positive placements and 270 frames. Existing whole raw/history carries and physical joins are explicitly attributed; these five selected owner query sets belong to that slice. |
| bgc-2395-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations | supports | Complete actual source scope combines BGC 123 rows, Support 42 rows, Native 22 cached stanzas and the bounded implemented-curation scan, preserving exact authorship and source limitations. |
| bgc-2395-curation-scope | /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-implemented-curation-scan-001.json; /scope; /ignored_files_included; /table_pins; /scanned_tables; /lexical_positive_rows; /applicable_rows; /applicable_curation; /unrelated_lexical_hits; /conclusion; /exclusion_conclusion; /reserved_files; /limitations | supports | Bounded ignored-inclusive scan has one applicable Sodorifen/BGC1361 override outside this owner and sixteen generic Streptomyces-only unrelated hits. No applicable correction/exclusion is transferred to this owner. Reserved decisions/source queue are excluded. |
| bgc-2395-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/11 | supports | Complete retained taxonomy stanzas for this owner’s source identifiers preserve names and exact synonyms only. They do not freshly establish lineage, producer identity or strain equivalence. |
| bgc-2395-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-cached-taxonomy-reading-001.json; /status; /scope; /counts; /readings; /cautions | supports | Native personally read all 22 whole stanzas; this is delegated taxonomy evidence, separate from BGC source-row reading and without a live lookup. |
| bgc-2395-direct-contexts | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-target-input-plan-001.json; /records/4/proposed_companion_paths; /records/4/direct_companion_predicates | supports | Exact direct same-locus context membership and predicates; no transitive expansion or identity, mechanism or activity transfer. |
| bgc-2395-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/21; /contexts/22; /contexts/23; /contexts/24; /contexts/34 | supports | Complete raw/history/source contexts for the direct companions retain distinct full keys, source roles and historical mechanisms; their claims are not automatically inherited by this owner. |
| bgc-2395-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2529–2529, row_sha256 208eeb09c242f07c41cfb4f5d1af53453a210d89d5441d4556601443798abe20 | supports | Complete exact-key compound/source/version, producer/locus grades and citation-level fields. BGC complete assigned source reading carries. |
| bgc-2395-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 39031–39031, row_sha256 a2e08a1d3efe3318bdbe607d9fec76c6d781c4477fbeff153b16cf187b7bc2bc | supports | Complete exact-key ChEBI structure/concept/definition fields; database grounding is not fresh natural-identity authentication. BGC complete assigned source reading carries. |
| bgc-2395-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 9086–9086, row_sha256 d42941173e2266666b94980e2dee653b46917b850acfee656ec03407f0b4221b | supports | Complete source organism/reference assertions, separate from demonstrated production or independent experiments. BGC complete assigned source reading carries. |
| bgc-2395-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 2560–2560, row_sha256 4ef2e91835767b87d143ceeda7b3eacc4015e0c7a36e4258c510af0cc62fb8bd | supports | Exact named/versioned computed classification and glycoside prediction, not an experimentally established scaffold. BGC complete assigned source reading carries. |
| bgc-2395-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys query: exact predicate exact complete standard_inchi_key equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json; /contexts/35/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins query: exact predicate exact chebi_id from exact full-key structure rows; exact query value ["CHEBI:138046"]; all 0 matches or complete empty result retained. Blank AID rows, if present, are no-assay sentinels. |
| bgc-2395-reader-DATA | /private/tmp/npm-review-work/shared-next-batch240/native-current240-sesterfisherol-maintained-reader-DATA-001.json; /status; /review_check_metadata; /raw_owner; /resolved_view; /expected_view; /component_captures; /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials; /errors; /limitations | supports | One actual maintained call returned the complete owner exactly, including every graph, pathway, evidence and history field. No components or unexpected errors/denials; known capability probe blocked before action. This does not authenticate the historical biology. |
| bgc-2395-reader-execution | /private/tmp/npm-review-work/shared-next-batch240/native-current240-sesterfisherol-reader-execution-001.json; /order; /command; /started_at; /finished_at; /exit_code; /DATA; /stdout; /stderr; /original_process_receipt; /original_tool_file | supports | Original one-call execution, exact DATA/output pins and closed original process; no retry or new execution by this review. |
| bgc-2395-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch240/root-native-reader-2395-acceptance-001.json; /status; /order; /DATA; /execution; /verification; /review_check_contract; /positive_content_scope; /runtime_environment_addition; /expected_socket_probe_blocked_before_action | supports | ROOT accepted this exact original owner result and typed check contract. Runtime-only CF environment addition is explicit; launch equality is not misreported as runtime equality. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-240/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-240/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-240/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-240/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-240/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- All evidence is retained locally; no fresh publication, taxonomy, assay, protein or natural-stereochemistry verification occurred.
- Full QC and complete OAK coverage remain unavailable. Saved-form consistency is not exact natural identity or an independent full-graph proof.
- Producer, locus, occurrence and citation roles remain separate. Shared taxa, BGCs, references and congeners do not transfer identity, activity or experimental independence.
- Four original charge-rearrangement warnings remain global and unassigned. Original comparison/map and optional-field semantics are preserved.
- No source status, history or record edit is proposed; any future supported correction belongs to the maintained owners in the actual intake.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five forms: 234 atom rows and 254 bond rows, with every scalar/ring/stereo/motif/map field. Diagnostic indices are zero-based, not biochemical locants.
- Actual source meanings retain disjoint attribution: BGC 123 complete rows/270 frames, Support 42 rows/99 frames, Native 22 complete cached stanzas and bounded ignored-inclusive curation. Exact prior whole raw/history carries are retained in accepted notes.
- BGC operated the sole admitted source collector and composer and authored these assessments. Support operated actual canonical intakes; ROOT operated the original diagnostic. ROOT operated the original per-owner maintained-reader launch wrappers; Native authored preparation and independently audited the saved results. Only sesterfisheric acid and sesterfisherol require maintained readers in this first-five scope.
- No finding/action is inferred solely from model applicability concerns, unavailable fresh verification or local diagnostic success.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T124233Z-sesterfisherol
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: sesterfisherol'
started_at: '2026-11-04T11:41:40.730774Z'
finished_at: '2026-11-04T12:42:33.147064Z'
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
summary: Sesterfisherol retains exact local ChEBI/full-key grounding and consistent
  C25H42O forms with eight specified tetrahedral centers and one Z alkene. Its one-step
  NfSS mechanism explicitly leaves downstream oxidation unexpanded; its one original
  maintained call is accepted and preserves the complete owner. The Diterpenoids/Fusicoccane
  model label is a bounded applicability concern, while producer, locus and occurrence
  roles remain separate.
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
  - path: data/natural_products/terpenoids/compound-5.yaml
    sha256: 87a02823400a7a21bad4687966e6079abd6b1f681848c2bfbb274189d69cc4f3
    role: context
  - path: data/natural_products/terpenoids/compound-6-2.yaml
    sha256: ff4b7f43512cb99d35e43bb8305b6615fa396a62bce5b4a88d29df4bc3ef5c94
    role: context
  - path: data/natural_products/terpenoids/compound-7a.yaml
    sha256: b679d2615a1acbce2e472a8fc5d34ebfdac5943973222e7d7cd378d9652aec75
    role: context
  - path: data/natural_products/terpenoids/compound-8-2.yaml
    sha256: 68403d95a9ea9be2728367fae51a04a8bccd310a91f1cf91c2fe25deca39ed99
    role: context
  - path: data/natural_products/terpenoids/sesterfisheric-acid.yaml
    sha256: 6335b2898a1d612945320f2dbc948c28f61d311ff280fb118065cf67e49d55e7
    role: context
  - path: data/natural_products/terpenoids/sesterfisherol.yaml
    sha256: 04a0bb1a0a35f53248d39401d8d3b24121d9c36a1010a7da3ced52fb4be71ed7
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
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2395; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:138046
targets:
- target_id: CHEBI:138046
  path: data/natural_products/terpenoids/sesterfisherol.yaml
  label: sesterfisherol
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
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/sesterfisherol.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for sesterfisherol
  required: true
  status: passed
  summary: One original offline maintained call preserved the complete captured owner,
    graph, pathway and history. Primary mechanism, protein/construct, natural-identity
    and stereochemical validity are outside this check.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-reader-DATA
  - bgc-2395-reader-execution
  - bgc-2395-reader-acceptance
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch240/read-selected-mechanism-guarded-001.py
    2395 404809cc80667a481bff31ecb717ad1c1abb2449f137a4c53a6a36215dc30fdb 29ef01ec3c00517302398203c0efa9db85eaa687a86990dcd3b63ab7f87aa331
    34cf7036b49c50a22b33b25135e3980718d171e0950a40cc5706c02a4c59983b bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
    25fca7a0e0dc63367ff9e0e49bf9dd5e26598663615a68a6e62a1109d9b857bf
  exit_code: 0
  expected_exit_code: 0
  scope_note: Complete owner preservation and maintained topology; only the expected
    capability probe was blocked before action. No component call, retry or external
    request.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:138046
  command: just validate-strict data/natural_products/terpenoids/secobotrytriendiol.yaml
    data/natural_products/terpenoids/secobotrytriene-10-12-15-triol.yaml data/natural_products/terpenoids/sespenine.yaml
    data/natural_products/terpenoids/sesterfisheric-acid.yaml data/natural_products/terpenoids/sesterfisherol.yaml
    data/natural_products/terpenoids/snf4435c.yaml data/natural_products/terpenoids/snf4435d.yaml
    data/natural_products/terpenoids/sodorifen.yaml data/natural_products/terpenoids/sordaricin-b.yaml
    data/natural_products/terpenoids/sordarin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-240/validate-strict-selected10-001.tsv
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
  - CHEBI:138046
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-240/validate-all-001.tsv
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
  - CHEBI:138046
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
  - CHEBI:138046
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
  - CHEBI:138046
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-240/review-queue-001.tsv
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
  - CHEBI:138046
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:138046
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:138046
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2395-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/sesterfisherol.yaml
  locator: Whole current plaintext and complete curation_history
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete sesterfisherol owner and 3 history events, with the unchanged
    native EXACT/SEEDED statuses. Prior full raw reading is carried; no record edit.
  snapshot_sha256: 04a0bb1a0a35f53248d39401d8d3b24121d9c36a1010a7da3ced52fb4be71ed7
- evidence_id: bgc-2395-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete actual captured owner, exact root presence, mechanism projection
    and history; no scientific claim is inferred solely from counts.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/intakes/2395-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Actual canonical target, all 44 source placements and complete ownership
    roles. Generated records/pages are not independent correction owners.
  snapshot_sha256: 29ef01ec3c00517302398203c0efa9db85eaa687a86990dcd3b63ab7f87aa331
- evidence_id: bgc-2395-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/root-intake-acceptance-001.json
  locator: /status
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: ROOT acceptance of the actual ten canonical intakes; complete per-owner
    inputs are separately linked in this record intake.
  snapshot_sha256: 39665ad64e8c5ac43677a515dec2d8ff754b14f46840f107070fba7f9c20fe80
- evidence_id: bgc-2395-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/label;
    /records/4/owner_document/chemical_structure; /records/4/owner_document/grounding_status;
    /records/4/owner_document/definition; /records/4/owner_document/definition_source;
    /records/4/owner_document/xrefs; /records/4/owner_document/source_concepts; /records/4/owner_document
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Retained identifier, label, exact structure, grounding/source concepts
    and present cross-references; definition is present as a ChEBI attribution.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4/owner_document/biosynthesis_origin; /records/4/owner_document/producer_taxon_groups;
    /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters;
    /records/4/owner_document/source_concepts
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Exact owner producer/locus/source concepts and separate evidence grades,
    reference placements and available coordinate fields; no fresh source validation.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4/owner_document/occurrences; /records/4/owner_document/occurrence_taxon_groups;
    /records/4/owner_document
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: The owner retains 1 occurrence placements. Bioactivities, bioactivity_summary
    and molecular_targets are absent. This owner-only evidence makes no saved-query
    or curation claim.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_pathway; /records/4/owner_document/np_classification;
    /records/4/owner_document/bgc_class; /records/4/owner_document
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Exact retained model version/pathway/superclass/class/glycoside output
    and separate source BGC class fields; computed specificity is not independently
    validated here.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4/owner_document/curation_status; /records/4/owner_document/curation_history
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete unchanged curation_status and curation_history, including seeded
    and any historically curated events; review status is not promoted.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-mechanism-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/owner-capture-DATA-001.json
  locator: /records/4/owner_document/causal_graphs; /records/4/owner_document/biosynthetic_pathway;
    /records/4/owner_document
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete retained graph/pathway semantics and optional-field absences.
  snapshot_sha256: bad78941d881846251ff3dacec3c38227e42b7c1de7a9142554e8d9d15663edd
- evidence_id: bgc-2395-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Both complete saved representations preserve the exact formula/charge/full
    key/canonical forms and stereo counts. All ten comparison flags are true; original
    full_graph_identity_established remains false.
  snapshot_sha256: df6a2b945015b15d512b8fe44d459381e89edf2ba59bc2c68e2f4c3af5c3e25c
- evidence_id: bgc-2395-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed/atoms; /records/4/smiles/computed/bonds; /records/4/smiles/computed/rings;
    /records/4/smiles/computed/potential_stereo; /records/4/smiles/computed/motifs;
    /records/4/smiles/computed/fragment_atom_indices; /records/4/inchi/computed/atoms;
    /records/4/inchi/computed/bonds; /records/4/inchi/computed/rings; /records/4/inchi/computed/potential_stereo;
    /records/4/inchi/computed/motifs; /records/4/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: The saved graph contains four independent carbocyclic rings with path sizes
    8, 5, 6 and 5 and a single tertiary alcohol. It has no carbonyl, ether bridge
    or candidate sugar cycle. These features are compatible with the retained tetracyclic
    alcohol description, without independently establishing the natural skeleton,
    enzymatic product or biochemical atom numbering.
  snapshot_sha256: df6a2b945015b15d512b8fe44d459381e89edf2ba59bc2c68e2f4c3af5c3e25c
- evidence_id: bgc-2395-congener-stereo-context
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed/atoms; /records/3/inchi/computed/atoms; /records/4/smiles/computed/atoms;
    /records/4/inchi/computed/atoms
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete saved acid/alcohol atom tables retain the distinct S acid-bearing
    and R methyl-bearing CIP labels; a congener letter contrast alone is not an epimerization
    witness.
  snapshot_sha256: df6a2b945015b15d512b8fe44d459381e89edf2ba59bc2c68e2f4c3af5c3e25c
- evidence_id: bgc-2395-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-current240-first-five-diagnostic-reading-001.json
  locator: /records/4; /coverage; /lossless_reading_method; /limits
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: BGC personally read every assigned stored-form field, all 234 atom and
    254 bond rows across the first five, with exact shared-value/constant-column factoring
    and bounded original atom maps.
  snapshot_sha256: 0d313ed4944076cf0d041a40fb91be9a432dc2e488a7726568dcdac7fccbf1f3
- evidence_id: bgc-2395-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /warning_count; /warning_record_attribution;
    /limits
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Accepted one original diagnostic; four charge-rearrangement warnings remain
    global/unassigned and limitations remain explicit.
  snapshot_sha256: 7b2df2f605f5811f33a50b322bcb32924d833f122debedde4aade3f1cbb98593
- evidence_id: bgc-2395-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Original diagnostic execution, source and exact saved output streams; no
    new parse or runtime is performed by scientific authoring.
  snapshot_sha256: e8eb39e2c4d3c778bd003e0f6124b4b8fe805c37edfecce886a63b7e6c9db494
- evidence_id: bgc-2395-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 381–430
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Schema distinguishes retained exact-key/structure stereochemistry and versioned
    computed classification; model values are not source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2395-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 155–173
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Maintained extractor derives the saved flag from unassigned chiral centers
    in its original molecular input. The flag is not fresh experimental stereochemical
    validation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2395-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1019
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Maintained seeder preserves the chosen source structure/flag and exact
    named/versioned classifier outputs; filing follows its result-array rule.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2395-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-current240-source-reading-001.json
  locator: /scope; /reading; /finite; /cautions
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: BGC complete assigned 30-context reading covers 123 positive placements
    and 270 frames. Existing whole raw/history carries and physical joins are explicitly
    attributed; these five selected owner query sets belong to that slice.
  snapshot_sha256: f63e970fbb5bfc5376dd478ed535a2e7f072bcf260b511c725242b459db0ec8d
- evidence_id: bgc-2395-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete actual source scope combines BGC 123 rows, Support 42 rows, Native
    22 cached stanzas and the bounded implemented-curation scan, preserving exact
    authorship and source limitations.
  snapshot_sha256: 907d007ae08eaef6f9013847278a95cb5869dc1d040eb84b729c7e11e62f76b5
- evidence_id: bgc-2395-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-implemented-curation-scan-001.json
  locator: /scope; /ignored_files_included; /table_pins; /scanned_tables; /lexical_positive_rows;
    /applicable_rows; /applicable_curation; /unrelated_lexical_hits; /conclusion;
    /exclusion_conclusion; /reserved_files; /limitations
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Bounded ignored-inclusive scan has one applicable Sodorifen/BGC1361 override
    outside this owner and sixteen generic Streptomyces-only unrelated hits. No applicable
    correction/exclusion is transferred to this owner. Reserved decisions/source queue
    are excluded.
  snapshot_sha256: e11b54bb43c56a6f60a0183df7479e707360d3ae3e984dba85792653fd27bab4
  search_scope: All41 current owner/source contexts, fullkeys, IDs, ownedBGCs, labels/slugs,
    taxa, chemical IDs,44 exact BGC:compound IDs and0 actual AID tuples. Case-insensitive
    literal token scan of complete rows in9 relevant curation TSVs; Path.rglob enumerates
    all11 TSVs including ignored files.
- evidence_id: bgc-2395-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/11
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete retained taxonomy stanzas for this owner’s source identifiers
    preserve names and exact synonyms only. They do not freshly establish lineage,
    producer identity or strain equivalence.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
- evidence_id: bgc-2395-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/native-prep/native-current240-cached-taxonomy-reading-001.json
  locator: /status; /scope; /counts; /readings; /cautions
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Native personally read all 22 whole stanzas; this is delegated taxonomy
    evidence, separate from BGC source-row reading and without a live lookup.
  snapshot_sha256: 56fcae4e15e6d6042ddc77c6308f556c8e057c1fcd57af82c36c7f50eb28884c
- evidence_id: bgc-2395-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-target-input-plan-001.json
  locator: /records/4/proposed_companion_paths; /records/4/direct_companion_predicates
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Exact direct same-locus context membership and predicates; no transitive
    expansion or identity, mechanism or activity transfer.
  snapshot_sha256: e52fb36424e9a024531fd104d8039f91d4747645b78c4db4b0654db1e131da52
- evidence_id: bgc-2395-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/21; /contexts/22; /contexts/23; /contexts/24; /contexts/34
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete raw/history/source contexts for the direct companions retain distinct
    full keys, source roles and historical mechanisms; their claims are not automatically
    inherited by this owner.
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
- evidence_id: bgc-2395-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved mibig_compounds query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2529–2529, row_sha256 208eeb09c242f07c41cfb4f5d1af53453a210d89d5441d4556601443798abe20
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete exact-key compound/source/version, producer/locus grades and citation-level
    fields. BGC complete assigned source reading carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2395-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved chebi_structures query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 39031–39031, row_sha256 a2e08a1d3efe3318bdbe607d9fec76c6d781c4477fbeff153b16cf187b7bc2bc
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete exact-key ChEBI structure/concept/definition fields; database
    grounding is not fresh natural-identity authentication. BGC complete assigned
    source reading carries.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2395-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved lotus_occurrences query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 9086–9086, row_sha256 d42941173e2266666b94980e2dee653b46917b850acfee656ec03407f0b4221b
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Complete source organism/reference assertions, separate from demonstrated
    production or independent experiments. BGC complete assigned source reading carries.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2395-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved cyanometdb_occurrences query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved npclassifier query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 1 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 2560–2560, row_sha256 4ef2e91835767b87d143ceeda7b3eacc4015e0c7a36e4258c510af0cc62fb8bd
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Exact named/versioned computed classification and glycoside prediction,
    not an experimentally established scaffold. BGC complete assigned source reading
    carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2395-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved pubchem_bioassay query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved bindingdb_targets query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved antibioticmech_inchikeys query: exact predicate exact complete standard_inchi_key
    equality; exact query value "VQMHZILKNHUAMP-AISFCYSSSA-N"; all 0 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact complete standard_inchi_key
    equality; query: "VQMHZILKNHUAMP-AISFCYSSSA-N"'
- evidence_id: bgc-2395-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch240-tentative/bgc-prep/bgc-conditional240-source-inventory-DATA-001.json
  locator: /contexts/35/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: 'Saved chebi_origins query: exact predicate exact chebi_id from exact full-key
    structure rows; exact query value ["CHEBI:138046"]; all 0 matches or complete
    empty result retained. Blank AID rows, if present, are no-assay sentinels.'
  snapshot_sha256: 52ded90fc82630a030aec28ca249b934f65b09a61a40eb626e497e36accc4f72
  search_scope: 'The complete saved exact predicate/query against the pinned local
    table, including all matches or the complete empty result. No source replay, live
    lookup or universal absence claim. Predicate: exact chebi_id from exact full-key
    structure rows; query: ["CHEBI:138046"]'
- evidence_id: bgc-2395-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/native-current240-sesterfisherol-maintained-reader-DATA-001.json
  locator: /status; /review_check_metadata; /raw_owner; /resolved_view; /expected_view;
    /component_captures; /returned_view_equals_expected_complete_owner; /counts; /denials;
    /unexpected_denials; /errors; /limitations
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: One actual maintained call returned the complete owner exactly, including
    every graph, pathway, evidence and history field. No components or unexpected
    errors/denials; known capability probe blocked before action. This does not authenticate
    the historical biology.
  snapshot_sha256: 9fb0d94458a5af365b102255b0780d50ced5ef7693ae3c5a9e332a315b3352d3
- evidence_id: bgc-2395-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/native-current240-sesterfisherol-reader-execution-001.json
  locator: /order; /command; /started_at; /finished_at; /exit_code; /DATA; /stdout;
    /stderr; /original_process_receipt; /original_tool_file
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: Original one-call execution, exact DATA/output pins and closed original
    process; no retry or new execution by this review.
  snapshot_sha256: 723d9f743749cc9778590bb8304b40cf6b7c98888a7b57a7cbe11af47ec22869
- evidence_id: bgc-2395-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch240/root-native-reader-2395-acceptance-001.json
  locator: /status; /order; /DATA; /execution; /verification; /review_check_contract;
    /positive_content_scope; /runtime_environment_addition; /expected_socket_probe_blocked_before_action
  accessed_at: '2026-11-04T12:25:06.940885Z'
  support: supports
  summary: ROOT accepted this exact original owner result and typed check contract.
    Runtime-only CF environment addition is explicit; launch equality is not misreported
    as runtime equality.
  snapshot_sha256: 5f085c36e9bf39023dc930d8864cf5be64601a18040b13d500f511a21a4d1294
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:48:26.886706Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: a3ea4c1642d250ceb04a5ce0d0e63df092fc0b87afdabbbe0b2b7951b0ce3708
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:48:50.739192Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0062770845553872da90b572db6992f46a2ed20f86a684fc1f4021b943a3f384
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:49:09.952157Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:49:43.151899Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-240/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-240/native-current240-five-gates-execution-001.json
  accessed_at: '2026-11-04T11:49:55.198103Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: ef0f483866268632a552451bc3d4ba0368facfa350b47970dd4e1d1f9e3727b9
assessments:
- assessment_id: bgc-2395-identity
  area: identity
  topic: Retained identity/form consistency; natural identity unverified
  outcome: supported
  summary: CHEBI:138046 and full key VQMHZILKNHUAMP-AISFCYSSSA-N join the retained
    three-star ChEBI concept and MIBiG BGC0002162 v3, with NPA032823 preserved. The
    owner remains EXACT/SEEDED and the structure remains MIBiG-sourced. Both stored
    forms yield neutral C25H42O and the declared key. The ChEBI definition describes
    a tetracyclic sesterterpenoid and attributes its production to gene-cluster expression;
    that is a saved database definition, not fresh primary verification. The related
    acid and four numbered compounds are not alternate identities.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-grounding-owner
  - bgc-2395-chemistry
  - bgc-2395-source-mibig_compounds
  - bgc-2395-source-chebi_structures
  - bgc-2395-query-chebi_structures
  - bgc-2395-direct-contexts
  - bgc-2395-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: VQMHZILKNHUAMP-AISFCYSSSA-N; exact retained full key, not a name-only natural-identity
      claim.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2395-grounding-owner
    - bgc-2395-chemistry
    - bgc-2395-source-mibig_compounds
    - bgc-2395-source-chebi_structures
    - bgc-2395-query-chebi_structures
    - bgc-2395-direct-contexts
    - bgc-2395-companion-boundaries
  - name: grounding_scope
    value: CHEBI:138046 and full key VQMHZILKNHUAMP-AISFCYSSSA-N join the retained
      three-star ChEBI concept and MIBiG BGC0002162 v3, with NPA032823 preserved.
      The owner remains EXACT/SEEDED and the structure remains MIBiG-sourced. Both
      stored forms yield neutral C25H42O and the declared key. The ChEBI definition
      describes a tetracyclic sesterterpenoid and attributes its production to gene-cluster
      expression; that is a saved database definition, not fresh primary verification.
      The related acid and four numbered compounds are not alternate identities.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2395-grounding-owner
    - bgc-2395-chemistry
    - bgc-2395-source-mibig_compounds
    - bgc-2395-source-chebi_structures
    - bgc-2395-query-chebi_structures
    - bgc-2395-direct-contexts
    - bgc-2395-companion-boundaries
- assessment_id: bgc-2395-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: Both complete forms have 26 heavy atoms, 29 bonds, eight specified tetrahedral
    centers and one specified Z double bond. All ten saved comparisons are true. The
    methyl-bearing center has an R CIP assignment; comparison to the acid-bearing
    S center does not itself demonstrate a stereochemical inversion because substitution
    priorities change. The original one-match atom correspondence covers all atoms
    but retains full_graph_identity_established:false, and no natural stereoisomer
    is independently authenticated.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-chemistry
  - bgc-2395-topology
  - bgc-2395-congener-stereo-context
  - bgc-2395-diagnostic-reading
  - bgc-2395-diagnostic-acceptance
  - bgc-2395-grounding-owner
  - bgc-2395-structure-schema
  - bgc-2395-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both complete forms have 26 heavy atoms, 29 bonds, eight specified tetrahedral
      centers and one specified Z double bond. All ten saved comparisons are true.
      The methyl-bearing center has an R CIP assignment; comparison to the acid-bearing
      S center does not itself demonstrate a stereochemical inversion because substitution
      priorities change. The original one-match atom correspondence covers all atoms
      but retains full_graph_identity_established:false, and no natural stereoisomer
      is independently authenticated.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2395-chemistry
    - bgc-2395-topology
    - bgc-2395-congener-stereo-context
    - bgc-2395-diagnostic-reading
    - bgc-2395-diagnostic-acceptance
    - bgc-2395-grounding-owner
    - bgc-2395-structure-schema
    - bgc-2395-stereo-method
  - name: representation_correspondence
    value: All ten original comparisons are true; one chirality-aware atom match covers
      the atom count. full_graph_identity_established remains false; no new graph
      or natural-identity proof.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2395-chemistry
    - bgc-2395-topology
    - bgc-2395-congener-stereo-context
    - bgc-2395-diagnostic-reading
    - bgc-2395-diagnostic-acceptance
    - bgc-2395-grounding-owner
    - bgc-2395-structure-schema
    - bgc-2395-stereo-method
- assessment_id: bgc-2395-provenance
  area: provenance
  topic: Separate source producer, locus and curation scope
  outcome: supported
  summary: MIBiG BGC0002162 v3 retains Aspergillus fischeri NRRL 181, NCBITaxon:331117,
    as SOURCE_ASSERTION. Heterologous expression separately grades DS027698.1:2485363–2490827
    as CLUSTER_DEMONSTRATED. A demonstrated heterologous locus does not automatically
    strengthen native-producer evidence. No applicable correction appears in the bounded
    implemented-curation scan; the Sodorifen override is unrelated.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-origin-owner
  - bgc-2395-source-mibig_compounds
  - bgc-2395-curation-scope
  - bgc-2395-direct-contexts
  - bgc-2395-companion-boundaries
  - bgc-2395-cached-taxonomy
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0002162 v3 retains Aspergillus fischeri NRRL 181, NCBITaxon:331117,
      as SOURCE_ASSERTION. Heterologous expression separately grades DS027698.1:2485363–2490827
      as CLUSTER_DEMONSTRATED. A demonstrated heterologous locus does not automatically
      strengthen native-producer evidence. No applicable correction appears in the
      bounded implemented-curation scan; the Sodorifen override is unrelated.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2395-origin-owner
    - bgc-2395-source-mibig_compounds
    - bgc-2395-curation-scope
    - bgc-2395-direct-contexts
    - bgc-2395-companion-boundaries
    - bgc-2395-cached-taxonomy
  - name: producer_evidence
    value: MIBiG BGC0002162 v3 retains Aspergillus fischeri NRRL 181, NCBITaxon:331117,
      as SOURCE_ASSERTION. Heterologous expression separately grades DS027698.1:2485363–2490827
      as CLUSTER_DEMONSTRATED. A demonstrated heterologous locus does not automatically
      strengthen native-producer evidence. No applicable correction appears in the
      bounded implemented-curation scan; the Sodorifen override is unrelated.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2395-origin-owner
    - bgc-2395-source-mibig_compounds
    - bgc-2395-curation-scope
    - bgc-2395-direct-contexts
    - bgc-2395-companion-boundaries
    - bgc-2395-cached-taxonomy
  - name: locus_evidence
    value: MIBiG BGC0002162 v3 retains Aspergillus fischeri NRRL 181, NCBITaxon:331117,
      as SOURCE_ASSERTION. Heterologous expression separately grades DS027698.1:2485363–2490827
      as CLUSTER_DEMONSTRATED. A demonstrated heterologous locus does not automatically
      strengthen native-producer evidence. No applicable correction appears in the
      bounded implemented-curation scan; the Sodorifen override is unrelated.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2395-origin-owner
    - bgc-2395-source-mibig_compounds
    - bgc-2395-curation-scope
    - bgc-2395-direct-contexts
    - bgc-2395-companion-boundaries
    - bgc-2395-cached-taxonomy
- assessment_id: bgc-2395-citations
  area: evidence
  topic: Citation placement and historical attribution
  outcome: supported
  summary: DOI:10.1021/jacs.5b08319 is the MIBiG compound-evidence reference and its
    uppercase LOTUS variant is occurrence provenance. The historical NfSS pathway/graph
    attributes primary-experiment snippets to that DOI and separate mappings to retained
    MIBiG, UniProt and Rhea pages dated 2026-09-30. Reading those saved excerpts and
    notes does not mean the primary article or live records were freshly opened. Eight
    edge references plus four step references repeat evidence rather than representing
    twelve independent experiments.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-origin-owner
  - bgc-2395-occurrence-owner
  - bgc-2395-mechanism-owner
  - bgc-2395-grounding-owner
  - bgc-2395-source-mibig_compounds
  - bgc-2395-source-lotus_occurrences
  - bgc-2395-source-chebi_structures
  - bgc-2395-source-reading
  dimensions:
  - name: citation_scope
    value: DOI:10.1021/jacs.5b08319 is the MIBiG compound-evidence reference and its
      uppercase LOTUS variant is occurrence provenance. The historical NfSS pathway/graph
      attributes primary-experiment snippets to that DOI and separate mappings to
      retained MIBiG, UniProt and Rhea pages dated 2026-09-30. Reading those saved
      excerpts and notes does not mean the primary article or live records were freshly
      opened. Eight edge references plus four step references repeat evidence rather
      than representing twelve independent experiments.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2395-origin-owner
    - bgc-2395-occurrence-owner
    - bgc-2395-mechanism-owner
    - bgc-2395-grounding-owner
    - bgc-2395-source-mibig_compounds
    - bgc-2395-source-lotus_occurrences
    - bgc-2395-source-chebi_structures
    - bgc-2395-source-reading
- assessment_id: bgc-2395-occurrence
  area: evidence
  topic: Occurrence and retained assay/target scope
  outcome: supported
  summary: The one written LOTUS occurrence is Aspergillus flavus, NCBITaxon:5059,
    rather than the A. fischeri NRRL 181 producer. The exact ChEBI-origin query for
    CHEBI:138046 is empty and adds no organism assertion. The owner has no bioactivities,
    bioactivity_summary or molecular_targets; exact PubChem and BindingDB joins are
    empty. Source/cache labels preserve these separate roles without fresh taxonomy,
    production or inactivity inference.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-occurrence-owner
  - bgc-2395-source-lotus_occurrences
  - bgc-2395-query-lotus_occurrences
  - bgc-2395-query-chebi_origins
  - bgc-2395-cached-taxonomy
  - bgc-2395-taxonomy-reading
  - bgc-2395-query-pubchem_bioassay
  - bgc-2395-query-bindingdb_targets
  dimensions:
  - name: occurrence_scope
    value: The one written LOTUS occurrence is Aspergillus flavus, NCBITaxon:5059,
      rather than the A. fischeri NRRL 181 producer. The exact ChEBI-origin query
      for CHEBI:138046 is empty and adds no organism assertion. The owner has no bioactivities,
      bioactivity_summary or molecular_targets; exact PubChem and BindingDB joins
      are empty. Source/cache labels preserve these separate roles without fresh taxonomy,
      production or inactivity inference.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2395-occurrence-owner
    - bgc-2395-source-lotus_occurrences
    - bgc-2395-query-lotus_occurrences
    - bgc-2395-query-chebi_origins
    - bgc-2395-cached-taxonomy
    - bgc-2395-taxonomy-reading
    - bgc-2395-query-pubchem_bioassay
    - bgc-2395-query-bindingdb_targets
  - name: assay_target_scope
    value: No owner bioactivities, bioactivity_summary or molecular_targets, with
      empty retained PubChem/BindingDB joins. The biosynthetic enzyme account does
      not supply a pharmacological assay or target measurement.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2395-occurrence-owner
    - bgc-2395-source-lotus_occurrences
    - bgc-2395-query-lotus_occurrences
    - bgc-2395-query-chebi_origins
    - bgc-2395-cached-taxonomy
    - bgc-2395-taxonomy-reading
    - bgc-2395-query-pubchem_bioassay
    - bgc-2395-query-bindingdb_targets
- assessment_id: bgc-2395-classification
  area: consistency
  topic: Versioned model applicability and source distinctions
  outcome: concern
  summary: The retained NPClassifier output at npclassifier.gnps2.org@2026-09-07 is
    Terpenoids/Diterpenoids/Fusicoccane diterpenoids with is_glycoside:false. The
    C25 structure, ChEBI sesterterpenoid definition and historically attributed GFPP
    cyclization expose a bounded applicability concern for the more specific Diterpenoids/Fusicoccane
    prediction. Faithful model ingestion and broad TERPENOIDS filing are not thereby
    erroneous, and no replacement prediction is supplied. The nonglycoside flag is
    compatible with the saved topology.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-classification-owner
  - bgc-2395-source-npclassifier
  - bgc-2395-chemistry
  - bgc-2395-topology
  - bgc-2395-mechanism-owner
  - bgc-2395-grounding-owner
  - bgc-2395-structure-schema
  - bgc-2395-classification-seeder
  dimensions:
  - name: classification_applicability
    value: The retained NPClassifier output at npclassifier.gnps2.org@2026-09-07 is
      Terpenoids/Diterpenoids/Fusicoccane diterpenoids with is_glycoside:false. The
      C25 structure, ChEBI sesterterpenoid definition and historically attributed
      GFPP cyclization expose a bounded applicability concern for the more specific
      Diterpenoids/Fusicoccane prediction. Faithful model ingestion and broad TERPENOIDS
      filing are not thereby erroneous, and no replacement prediction is supplied.
      The nonglycoside flag is compatible with the saved topology.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2395-classification-owner
    - bgc-2395-source-npclassifier
    - bgc-2395-chemistry
    - bgc-2395-topology
    - bgc-2395-mechanism-owner
    - bgc-2395-grounding-owner
    - bgc-2395-structure-schema
    - bgc-2395-classification-seeder
- assessment_id: bgc-2395-mechanism
  area: consistency
  topic: Preserved historical biosynthetic mechanism; primary claims unverified
  outcome: unknown
  summary: One three-node/two-edge BIOSYNTHESIS graph and pathway step 1 retain CHEBI:57907
    through NfSS/UniProtKB:A1DN30 to CHEBI:138046, with RHEA:54068. The step explicitly
    leaves downstream NfP450/A1DN29 oxidation to sesterfisheric acid unexpanded; it
    must not acquire the acid owner’s second step by shared-locus inference. All evidence,
    optional-field absences and three history events remain part of the local view.
    The accepted original maintained call returned exactly the complete captured owner,
    preserving every graph/pathway/evidence/history field and all optional-field absences.
    It had no components, unexpected denials or errors; the one known socket-construction
    capability probe was blocked before action. Preservation is not fresh scientific
    verification.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-mechanism-owner
  - bgc-2395-history-owner
  - bgc-2395-reader-DATA
  - bgc-2395-reader-execution
  - bgc-2395-reader-acceptance
  - bgc-2395-origin-owner
  - bgc-2395-source-mibig_compounds
  - bgc-2395-direct-contexts
  - bgc-2395-companion-boundaries
- assessment_id: bgc-2395-protein
  area: identity
  topic: Historically attributed protein/construct scope
  outcome: unknown
  summary: The retained NfSS mapping joins UniProtKB:A1DN30, NFIA_055500 and GenPept
    EAW16201.1; its database note describes a reviewed 764-amino-acid protein and
    a bifunctional synthase/cyclase context. These remain historical attributions,
    not fresh sequence/domain, construct/tag or accession verification. The saved
    reaction’s water/diphosphate description does not establish a newly inspected
    stoichiometric or cofactor experiment.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-mechanism-owner
  - bgc-2395-reader-DATA
  - bgc-2395-reader-acceptance
  - bgc-2395-origin-owner
- assessment_id: bgc-2395-completion
  area: completeness
  topic: Actual evidence coverage and remaining scientific limits
  outcome: unknown
  summary: Complete raw/history, retained source payloads, actual intake, both molecular
    forms and the actual maintained-reader result have been read. The accepted original
    call preserves the complete single-step mechanism and all three history events.
    Full QC/OAK, fresh primary/source, protein/construct and taxonomic verification,
    and independent natural-identity confirmation remain unavailable. This is a partial
    review with no supported record-edit finding; the model-applicability concern
    does not authorize replacing a faithful prediction.
  target_ids:
  - CHEBI:138046
  evidence_ids:
  - bgc-2395-owner
  - bgc-2395-capture
  - bgc-2395-intake
  - bgc-2395-intake-acceptance
  - bgc-2395-diagnostic-reading
  - bgc-2395-diagnostic-acceptance
  - bgc-2395-diagnostic-execution
  - bgc-2395-source-reading
  - bgc-2395-joint-source-notes
  - bgc-2395-curation-scope
  - bgc-2395-reader-DATA
  - bgc-2395-reader-execution
  - bgc-2395-reader-acceptance
  - bgc-2395-mechanism-owner
  dimensions:
  - name: review_completion
    value: Complete raw/history, retained source payloads, actual intake, both molecular
      forms and the actual maintained-reader result have been read. The accepted original
      call preserves the complete single-step mechanism and all three history events.
      Full QC/OAK, fresh primary/source, protein/construct and taxonomic verification,
      and independent natural-identity confirmation remain unavailable. This is a
      partial review with no supported record-edit finding; the model-applicability
      concern does not authorize replacing a faithful prediction.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2395-owner
    - bgc-2395-capture
    - bgc-2395-intake
    - bgc-2395-intake-acceptance
    - bgc-2395-diagnostic-reading
    - bgc-2395-diagnostic-acceptance
    - bgc-2395-diagnostic-execution
    - bgc-2395-source-reading
    - bgc-2395-joint-source-notes
    - bgc-2395-curation-scope
    - bgc-2395-reader-DATA
    - bgc-2395-reader-execution
    - bgc-2395-reader-acceptance
    - bgc-2395-mechanism-owner
findings: []
actions: []
limitations:
- All evidence is retained locally; no fresh publication, taxonomy, assay, protein
  or natural-stereochemistry verification occurred.
- Full QC and complete OAK coverage remain unavailable. Saved-form consistency is
  not exact natural identity or an independent full-graph proof.
- Producer, locus, occurrence and citation roles remain separate. Shared taxa, BGCs,
  references and congeners do not transfer identity, activity or experimental independence.
- Four original charge-rearrangement warnings remain global and unassigned. Original
  comparison/map and optional-field semantics are preserved.
- No source status, history or record edit is proposed; any future supported correction
  belongs to the maintained owners in the actual intake.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read all ten first-five forms: 234 atom rows and 254 bond rows,
  with every scalar/ring/stereo/motif/map field. Diagnostic indices are zero-based,
  not biochemical locants.'
- 'Actual source meanings retain disjoint attribution: BGC 123 complete rows/270 frames,
  Support 42 rows/99 frames, Native 22 complete cached stanzas and bounded ignored-inclusive
  curation. Exact prior whole raw/history carries are retained in accepted notes.'
- BGC operated the sole admitted source collector and composer and authored these
  assessments. Support operated actual canonical intakes; ROOT operated the original
  diagnostic. ROOT operated the original per-owner maintained-reader launch wrappers;
  Native authored preparation and independently audited the saved results. Only sesterfisheric
  acid and sesterfisherol require maintained readers in this first-five scope.
- No finding/action is inferred solely from model applicability concerns, unavailable
  fresh verification or local diagnostic success.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-240
```
