# Local evidence review: trichobrasilenol

- Review: 20261104T174833Z-trichobrasilenol
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T16:43:12.842424Z
- Finished UTC: 2026-11-04T17:48:33.896218Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Trichobrasilenol retains exact ChEBI/MIBiG grounding and consistent stored forms. The accepted maintained reader preserves both distinct historical enzyme graphs and all history. BraB consumption, TaTC6 formation, imported producer and occurrence contexts remain separate; primary and construct verification remain unavailable.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2422; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:167379 | data/natural_products/terpenoids/trichobrasilenol.yaml | generated | trichobrasilenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for trichobrasilenol | passed | True | CHEBI:167379 | One original offline maintained call preserved the complete captured owner, both graphs and all history. Primary mechanism, sequence/construct, natural identity and stereochemical authentication remain outside this check. |
| strict_ten | passed | True | CHEBI:167379 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:167379 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:167379 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:167379 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:167379 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:167379 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:167379 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:167379 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained source join and bounded natural-identity scope

identity: supported. Targets: CHEBI:167379.

CHEBI:167379 and MIBiG BGC0002260 compound 1 join the complete key DJBXKQSFHIRXRM-JRYBIPSHSA-N. The retained ChEBI carbobicyclic/sesquiterpenoid definition names a Trichoderma cyclase context, while the imported MIBiG producer is Annulohypoxylon truncatum. PubChem 146682173 and NPAtlas NPA025694 remain cross-references. Both forms normalize to neutral C15H26O and the declared key. Exact source alignment does not merge organism roles, verify the natural material, or transfer claims from the five distinct-key BGC2260 companions.

### Original stored-form and stereochemical scope

representation: supported. Targets: CHEBI:167379.

Both forms have 16 heavy atoms, 17 bonds, three specified tetrahedral centers and one specified E double bond. All ten saved comparisons are true with a complete supplied chirality-aware atom match. The actual E assignment is SMILES bond 3 C1=C4, corresponding to reconstructed bond 14 C10=C13. full_graph_identity_established remains false; this local consistency is not independent primary stereochemical or natural-identity confirmation.

### Distinct producer, locus and taxon assertions

provenance: supported. Targets: CHEBI:167379.

BGC0002260 v3 compound 1 retains Annulohypoxylon truncatum NCBITaxon:327061 as SOURCE_ASSERTION. Heterologous expression grades the MT383109.1 locus CLUSTER_DEMONSTRATED, a distinct question from native production or strain/construct identity. The Trichoderma occurrence/definition and historical TaTC6 reference context do not place TaTC6 in this BGC or upgrade imported producer evidence.

### Retained citation and history attribution

evidence: supported. Targets: CHEBI:167379.

PMID:32936132 is the imported MIBiG ENTRY citation; DOI:10.1002/ANIE.201907964 is the LOTUS occurrence reference. The two retained graphs contain ten reference placements, including repeated database URLs and historical native-sequence inferences; these are not ten independently read studies. The BraB history records inaccessible primary DOI:10.1039/D0CC03950K, and the TaTC6 history records inaccessible PMID:31418991/DOI:10.1002/anie.201907964 and supplementary information. The two seed events and two curation events remain intact. This review reads those attributions, not fresh primary text.

### Bounded occurrence and no-assay scope

evidence: supported. Targets: CHEBI:167379.

One LOTUS Trichoderma atroviride NCBITaxon:63577 occurrence is retained, separate from Annulohypoxylon truncatum NCBITaxon:327061 producer/locus claims. The exact-key cyanobacterial and ChEBI-origin frames are empty. The cached names support the two retained taxon identities at their local scope; neither occurrence nor a definition authenticates native production or an experimental strain.

### Versioned model fidelity and applicability limits

consistency: supported. Targets: CHEBI:167379.

The versioned NPClassifier output is Terpenoids/Sesquiterpenoids/Tremulane sesquiterpenoids with is_glycoside:false. The C15 carbon-bicyclic alcohol topology supports retaining a non-glycoside structural description. The named Tremulane prediction, ChEBI definition and source TERPENE class remain distinct assertions; faithful retention does not independently establish biosynthetic family or primary structural assignment.

### Complete preserved historical mechanisms; primary limits

consistency: unknown. Targets: CHEBI:167379.

The complete owner retains two inline BIOSYNTHESIS graphs: BraB substrate glycosylation has four nodes and three edges; TaTC6 product formation has three nodes and two edges. There are no pathway, component-reference or molecular-target roots. BraB consumes exact trichobrasilenol; it is not its terpene synthase. TaTC6 formation is a separate database-reported route. The accepted single maintained call returns the entire captured owner exactly, including all seven nodes, five edges, ten reference placements and four histories. One known socket-construction capability probe was denied before action, with no unexpected denial or error. Structural preservation does not independently validate the biological claims.

### Historically attributed native reference and construct limits

identity: unknown. Targets: CHEBI:167379.

The retained BraB mapping identifies native Annulohypoxylon truncatum CBS140778 P9WER1/QOE88884.1, historically compared over 421 amino acids and reverse CDS MT383109.1:2625–3890. The separate TaTC6 mapping identifies native Trichoderma atroviride FKI-3849 A0A5S9I252/BBK61014.1, historically compared over 386 amino acids and a six-exon LC484924.1 CDS. These are attributed historical reference correspondences, not newly checked sequences or complete assayed constructs/tags. Putative UDP-GlcNAc donor, stereochemically incomplete ungrounded Brasilane A, disputed pathway finality, TaTC6 side-product specificity, koraiol phenotype, homodimer and Mg-binding scopes remain qualified or unadopted as written. No kinetics, physical complex, measured donor preference or native-producer upgrade is inferred.

### Actual evidence coverage and remaining scientific limits

completeness: unknown. Targets: CHEBI:167379.

Complete owner/history, actual canonical intake, retained source payloads and empty frames, and both original molecular forms have been read. The accepted single maintained call also preserves both complete graphs and all four histories. The owner remains EXACT and SEEDED with 4 unchanged history events. Its intake identifies source seeder/extractor/classifier ownership separately from curator-owned mechanism/history where present. The ignored-inclusive bounded curation scan reports no applicable correction. Full QC/OAK, fresh primary, taxonomy, assay and construct verification, and independent natural identity or stereochemistry remain unavailable. This is a partial review with no supported source-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2422-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/trichobrasilenol.yaml; Complete plaintext including every curation_history entry | supports | Complete trichobrasilenol owner and 4 unchanged history entries. Grounding EXACT and native status SEEDED are retained; prior personal whole raw/history reading carries. |
| bgc-2422-capture | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1 | supports | Actual complete owner capture, metadata, history and exact root presence; capture fidelity is not independent scientific verification. |
| bgc-2422-intake | /private/tmp/npm-review-work/shared-next-batch243/intakes/2422-inspect-001.json; /status; /repository; /source; /targets | supports | Actual target and ownership roles with all 44 current input placements, joined to the accepted plan. |
| bgc-2422-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch243/root-intake-acceptance-001.json; /status; /summary | supports | ROOT accepted the ten original canonical intakes; this owner’s exact targets/ownership and complete inputs are linked separately. |
| bgc-2422-grounding-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/label; /records/1/owner_document/chemical_structure; /records/1/owner_document/definition; /records/1/owner_document/definition_source; /records/1/owner_document/xrefs; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status | supports | Complete retained identifier, stored structure, cross-references and source concepts, with any definition or historical grounding note actually present; no current global database-absence claim. |
| bgc-2422-origin-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups; /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts | supports | Exact producer and locus support grades, methods, accession, citations and any coordinate fields actually supplied; native production and locus support remain distinct. |
| bgc-2422-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1/owner_document | supports | One retained LOTUS occurrence is distinct from production. The complete owner lacks bioactivities, bioactivity_summary and molecular_targets; these are owner-only observations. |
| bgc-2422-classification-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing pathway and retained source classes. Retention does not establish applicability. |
| bgc-2422-history-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1/owner_document/curation_status; /records/1/owner_document/curation_history | supports | All retained history events and SEEDED status remain unchanged; review validation does not promote source status. |
| bgc-2422-mechanism-owner | /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json; /records/1/owner_document/causal_graphs; /records/1/owner_document/curation_history | supports | Both complete historical graph assertions and all histories: two inline graphs, seven nodes, five edges and ten edge-reference placements. Native sequence and inaccessible-primary claims remain historically attributed. |
| bgc-2422-chemistry | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/formula; /records/1/smiles/computed/formal_charge; /records/1/smiles/computed/standard_inchi; /records/1/smiles/computed/standard_inchi_key; /records/1/smiles/computed/canonical_isomeric_smiles; /records/1/smiles/computed/canonical_nonisomeric_smiles; /records/1/smiles/computed/atom_count; /records/1/smiles/computed/heavy_atom_count; /records/1/smiles/computed/bond_count; /records/1/smiles/computed/element_counts; /records/1/smiles/computed/stereo_counts; /records/1/inchi/computed/formula; /records/1/inchi/computed/formal_charge; /records/1/inchi/computed/standard_inchi; /records/1/inchi/computed/standard_inchi_key; /records/1/inchi/computed/canonical_isomeric_smiles; /records/1/inchi/computed/canonical_nonisomeric_smiles; /records/1/inchi/computed/atom_count; /records/1/inchi/computed/heavy_atom_count; /records/1/inchi/computed/bond_count; /records/1/inchi/computed/element_counts; /records/1/inchi/computed/stereo_counts | supports | All ten stored-form comparisons are true with a complete supplied chirality-aware atom match; full_graph_identity_established remains false and natural identity is unverified. |
| bgc-2422-topology | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds; /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo; /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices; /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings; /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs; /records/1/inchi/computed/fragment_atom_indices | supports | The stored forms retain fused carbon-only six- and five-membered cycles and one alcohol; the SMILES alcohol O3 attaches to C2. No C5O ring, carbonyl or C–O–C bridge is detected. This local topology is consistent with retaining the non-glycoside flag, without independently verifying the named scaffold family or either enzyme reaction. |
| bgc-2422-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-current243-first-five-diagnostic-reading-001.json; /records/1; /coverage; /lossless_reading_method; /readings; /limits | supports | BGC personally read all ten first-five forms: 420 atom rows and 438 bond rows, including every scalar/string/ring/stereo/motif/map field. Exact common-value and constant-column factoring was reconstructed losslessly; no reparse. |
| bgc-2422-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /scalar_results/1; /warnings; /limitations | supports | ROOT accepted one original twenty-form diagnostic. This owner’s scalar results are explicit; four global stderr warnings remain unassigned to records. Natural identity and claim-specific interpretation remain separate. |
| bgc-2422-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original execution, source and stdout/stderr pins. |
| bgc-2422-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–430 | supports | The schema distinguishes undefined stereo from fabricated assignments and defines computed classification as named/versioned model output, never a source assertion. |
| bgc-2422-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False) defines the stored flag via unassigned centers. It does not test double-bond completeness or natural stereochemical truth. |
| bgc-2422-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | The maintained seeder retains source structure/stereo and classifier arrays, with pathway filing from the model; faithful retention is distinct from applicability. |
| bgc-2422-source-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-current243-source-reading-001.json; /scope; /reading; /division; /physical_join_verification; /cautions | supports | BGC personally read contexts 0–8: 81 complete frames, 31 positive rows and 396 fields, including these five owners and four unselected Brasilane contexts. Prior raw/history carries remain attributed. |
| bgc-2422-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations | supports | Actual fifteen-context scope combines BGC 31 rows, Support 15 rows and Native eight cache stanzas plus curation scan. Historical conditional fields remain distinct from later earned runtime acceptances. |
| bgc-2422-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch243/root-source-plan-acceptance-001.json; /status | supports | ROOT accepted the original composed source plan and exact input maps; no source-table query is replayed for this review. |
| bgc-2422-curation-scope | /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-implemented-curation-scan-001.json; /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions; /assays; /guidance | supports | Ignored-inclusive scan of eight implemented tables and unresolved-taxonomy diagnostics found four inapplicable lexical matches, no applicable correction or exclusion. No actual AID is present; absence of an exclusion does not validate assay or natural identity. |
| bgc-2422-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/5 | supports | Complete retained taxon stanzas locate exact cached names/synonyms for this source context. Strain, species and producer/occurrence roles are not collapsed or freshly resolved. |
| bgc-2422-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-cached-taxonomy-reading-001.json; /scope; /taxonomy; /cached_names; /interpretation; /reading_outputs; /limitations | supports | Native personally read all eight saved stanzas and every route. BGC carries that explicit attribution; no fresh taxonomy lookup or duplicate positive-source-row credit. |
| bgc-2422-direct-contexts | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-target-input-plan-001.json; /records/1/proposed_companion_paths; /records/1/direct_companion_predicates | supports | Exact direct-context paths and literal predicates; shared owned-BGC context does not transfer identity, stereo, mechanism or activity. |
| bgc-2422-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/0/path; /contexts/0/identifier; /contexts/0/label; /contexts/0/standard_inchi_key; /contexts/0/owned_bgc_ids; /contexts/1/path; /contexts/1/identifier; /contexts/1/label; /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/2/path; /contexts/2/identifier; /contexts/2/label; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/3/path; /contexts/3/identifier; /contexts/3/label; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/8/path; /contexts/8/identifier; /contexts/8/label; /contexts/8/standard_inchi_key; /contexts/8/owned_bgc_ids | supports | Direct companions retain distinct full keys and labels under their explicit BGC ownership. Compact identity context is not claim transfer. |
| bgc-2422-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2716–2716; row_sha256 7f57bbb0b46f83655aa0963d2d635c1d7d43f5f9c0073b0a177f643f227f4162 | supports | Exact full-key/version/compound-index and all source producer/locus/citation-tier fields. BGC complete source-row reading carries. |
| bgc-2422-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 1 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; Header line 1; physical lines 43374–43374; row_sha256 c17d6b71acd65bae107c9a1a815a8fd31680dc46193f5ebdb80fe7a901f7797a | supports | Exact retained ChEBI identifier, full structure key and definition. BGC complete source-row reading carries. |
| bgc-2422-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 1113–1113; row_sha256 2f3eda34012601e2c192b2588e446314cb779179e7b0435cbb87f2035d3af1f5 | supports | Complete organism/reference occurrence assertion, not producer or independent-study proof. BGC complete source-row reading carries. |
| bgc-2422-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 431–431; row_sha256 b063d22be2f099daf9cf150409ccb9ac3bd1c367c73ae0aa486783172742c20f | supports | Exact named/versioned classifier arrays and glycoside flag; applicability is a separate assessment. BGC complete source-row reading carries. |
| bgc-2422-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 1 matching placements with exact predicate/query and all fields. Its blank-AID row is a no-assay sentinel. |
| bgc-2422-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 1453–1453; row_sha256 46f821136f2429659d8d1d362d6668a490183cfe611bc649916b4765e1024b37 | supports | Exact full-key/CID sentinel with blank AID and no assay outcome, measurement, target or reference; not inactivity. BGC complete source-row reading carries. |
| bgc-2422-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json; /contexts/5/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 matching placements with exact predicate/query and all fields. Negative scope is limited to this retained join. |
| bgc-2422-reader-DATA | /private/tmp/npm-review-work/shared-next-batch243/native-current243-trichobrasilenol-maintained-reader-DATA-001.json; /status; /reader_call_count; /raw_owner; /expected_view; /resolved_view; /component_captures; /returned_view_equals_expected_complete_owner; /view_mismatches; /counts; /denials; /unexpected_denials; /errors; /post_pin_failures; /limitations | supports | One original maintained call preserves the complete owner, two graphs, ten edge-reference placements and four histories exactly. The known socket-construction probe was denied before action; no unexpected denial or error. Biological and primary-source limits remain explicit. |
| bgc-2422-reader-execution | /private/tmp/npm-review-work/shared-next-batch243/native-current243-trichobrasilenol-reader-execution-001.json; /command; /started_at; /finished_at; /exit_code; /actual_environment; /stdout; /stderr; /DATA; /original_process_receipt; /original_tool_file; /original_start_tool; /original_tool; /operator | supports | BGC operated the single admitted original reader launch; one empty start object and genuine terminal 0 are preserved. Controller observer attribution remains distinct from operator. |
| bgc-2422-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch243/root-current243-trichobrasilenol-reader-acceptance-001.json; /status; /order; /DATA; /execution; /verification; /review_check_contract; /runtime_environment_delta; /limitations | supports | ROOT accepted the exact original reader and typed review check contract, complete-owner equality and positive content. Runtime-added __CF_USER_TEXT_ENCODING is explicit, without changing the launch environment. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-243/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-243/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-243/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-243/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-243/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only. Fresh primary papers, taxonomy, assay protocols and independent natural identity/stereochemical authentication remain unavailable.
- Full QC and complete OAK coverage remain unavailable. Saved normalized forms, motifs and atom matches do not establish independent full graph or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain distinct. Shared loci and repeated references do not transfer biological claims or establish independent experiments.
- Versioned model fidelity is assessed separately from applicability; the stated concerns do not prove source-ingestion defects or authorize record replacement.
- The accepted reader preserves complete historical graph and native-reference assertions without freshly verifying primary experiments, sequences, constructs, kinetics or physical complexes.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five molecular forms: 420 atom rows and 438 bond rows, plus every scalar/string/ring/stereo/motif/map field. Diagnostic indices are zero-based, not biochemical locants; four global stderr warnings remain unassigned.
- Disjoint source reading: BGC nine contexts/81 frames/31 rows/396 fields; Support six contexts/54 frames/15 rows/215 fields. Native read all eight complete cache stanzas and the ignored-inclusive curation scan, with zero positive-source-row credit. Prior whole raw/history carries remain attributed.
- ROOT operated the local collector, composer and canonical intakes; Native operated the original molecular diagnostic. BGC operated the sole original maintained reader; Native and Support supplied the separately attributed method, dependency, descriptor and binding peers. No new target is invoked by fragment authoring.
- All scientific outcomes remain partial; no supported source-record edit finding or action is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T174833Z-trichobrasilenol
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: trichobrasilenol'
started_at: '2026-11-04T16:43:12.842424Z'
finished_at: '2026-11-04T17:48:33.896218Z'
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
summary: Trichobrasilenol retains exact ChEBI/MIBiG grounding and consistent stored
  forms. The accepted maintained reader preserves both distinct historical enzyme
  graphs and all history. BraB consumption, TaTC6 formation, imported producer and
  occurrence contexts remain separate; primary and construct verification remain unavailable.
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
  - path: data/natural_products/terpenoids/brasilane-a.yaml
    sha256: ad9d6c81134c14e495ce5b385b3cdf3581740b9d3e1318770cc5dfeec5951261
    role: context
  - path: data/natural_products/terpenoids/brasilane-d.yaml
    sha256: 9e708a2e090dbc1260666cd78393c9d1afc462d65a73b9c694c0e218b3290495
    role: context
  - path: data/natural_products/terpenoids/brasilane-e.yaml
    sha256: f341965e6fc5cee18d52eeabca4eed2d8b87d2c78b475c0a45bb9952f3f54517
    role: context
  - path: data/natural_products/terpenoids/brasilane-f.yaml
    sha256: eba2703e50c44d7c8069d5e3c19f577b1e88e3d6e4e2588d009bae1f891048cc
    role: context
  - path: data/natural_products/terpenoids/trichobrasilenol.yaml
    sha256: 2ec4a7287c9776fe96c0b325e89b8dba8f54f41d50b9ea57698aa5190417eaf1
    role: target
  - path: data/natural_products/terpenoids/xylarenic-acid-b.yaml
    sha256: 706e8b2a674d3191d483cefe3f2adc1b45d7af822b968c4f78b0c3d890bd07ca
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
  selection: Campaign path order 2422; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:167379
targets:
- target_id: CHEBI:167379
  path: data/natural_products/terpenoids/trichobrasilenol.yaml
  label: trichobrasilenol
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
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/terpenoids/trichobrasilenol.yaml
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
  name: Complete offline maintained reader for trichobrasilenol
  required: true
  status: passed
  summary: One original offline maintained call preserved the complete captured owner,
    both graphs and all history. Primary mechanism, sequence/construct, natural identity
    and stereochemical authentication remain outside this check.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-reader-DATA
  - bgc-2422-reader-execution
  - bgc-2422-reader-acceptance
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch243/read-selected-mechanism-guarded-001.py
    2422 98a87b1c3c77621707cf5c2342e6791a97ef46ca9f4d3b880586cf3f4dbdd320 a0f2611123c29e687ee310160eead110acf54156046a751d8edfa1798541234f
    34cf7036b49c50a22b33b25135e3980718d171e0950a40cc5706c02a4c59983b 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
    9d9144549bb93ca99de4542e849e13663d22fe1983d13df9463c71daadd71160
  exit_code: 0
  expected_exit_code: 0
  scope_note: Complete owner preservation and maintained topology. The known socket
    capability probe was blocked before action; no components, retry, external request
    or additional molecular parse.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - CHEBI:167379
  command: just validate-strict data/natural_products/terpenoids/trehangelin.yaml
    data/natural_products/terpenoids/trichobrasilenol.yaml data/natural_products/terpenoids/viguiepinol.yaml
    data/natural_products/terpenoids/xanthan.yaml data/natural_products/terpenoids/xylarenic-acid-b.yaml
    data/natural_products/terpenoids/yanuthone-d.yaml data/natural_products/terpenoids/yossoside-i.yaml
    data/natural_products/terpenoids/yossoside-ii.yaml data/natural_products/terpenoids/yossoside-iii.yaml
    data/natural_products/terpenoids/yossoside-iv.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-243/validate-strict-selected10-001.tsv
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
  - CHEBI:167379
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-243/validate-all-001.tsv
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
  - CHEBI:167379
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
  - CHEBI:167379
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
  - CHEBI:167379
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-243/review-queue-001.tsv
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
  - CHEBI:167379
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:167379
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:167379
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2422-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/trichobrasilenol.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Complete trichobrasilenol owner and 4 unchanged history entries. Grounding
    EXACT and native status SEEDED are retained; prior personal whole raw/history
    reading carries.
  snapshot_sha256: 2ec4a7287c9776fe96c0b325e89b8dba8f54f41d50b9ea57698aa5190417eaf1
- evidence_id: bgc-2422-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Actual complete owner capture, metadata, history and exact root presence;
    capture fidelity is not independent scientific verification.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/intakes/2422-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Actual target and ownership roles with all 44 current input placements,
    joined to the accepted plan.
  snapshot_sha256: a0f2611123c29e687ee310160eead110acf54156046a751d8edfa1798541234f
- evidence_id: bgc-2422-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/root-intake-acceptance-001.json
  locator: /status; /summary
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: ROOT accepted the ten original canonical intakes; this owner’s exact targets/ownership
    and complete inputs are linked separately.
  snapshot_sha256: b147ca209359c57adf20c4cd992acef2e7e20a63a82f6736763f7bcc4f9ba609
- evidence_id: bgc-2422-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/label;
    /records/1/owner_document/chemical_structure; /records/1/owner_document/definition;
    /records/1/owner_document/definition_source; /records/1/owner_document/xrefs;
    /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Complete retained identifier, stored structure, cross-references and source
    concepts, with any definition or historical grounding note actually present; no
    current global database-absence claim.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups;
    /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact producer and locus support grades, methods, accession, citations
    and any coordinate fields actually supplied; native production and locus support
    remain distinct.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: One retained LOTUS occurrence is distinct from production. The complete
    owner lacks bioactivities, bioactivity_summary and molecular_targets; these are
    owner-only observations.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing pathway and
    retained source classes. Retention does not establish applicability.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1/owner_document/curation_status; /records/1/owner_document/curation_history
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: All retained history events and SEEDED status remain unchanged; review
    validation does not promote source status.
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-mechanism-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/owner-capture-DATA-001.json
  locator: /records/1/owner_document/causal_graphs; /records/1/owner_document/curation_history
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Both complete historical graph assertions and all histories: two inline
    graphs, seven nodes, five edges and ten edge-reference placements. Native sequence
    and inaccessible-primary claims remain historically attributed.'
  snapshot_sha256: 7bbab67b7e48ef9ff76642ea6f9df2483f985271b02d04ba13a689d1db4fff0b
- evidence_id: bgc-2422-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: All ten stored-form comparisons are true with a complete supplied chirality-aware
    atom match; full_graph_identity_established remains false and natural identity
    is unverified.
  snapshot_sha256: 69a149d2f7c4a56aecea9a32f5ae0456c00a18f05bc12f14b0a0fbd95911976f
- evidence_id: bgc-2422-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds;
    /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo;
    /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices;
    /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings;
    /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs;
    /records/1/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: The stored forms retain fused carbon-only six- and five-membered cycles
    and one alcohol; the SMILES alcohol O3 attaches to C2. No C5O ring, carbonyl or
    C–O–C bridge is detected. This local topology is consistent with retaining the
    non-glycoside flag, without independently verifying the named scaffold family
    or either enzyme reaction.
  snapshot_sha256: 69a149d2f7c4a56aecea9a32f5ae0456c00a18f05bc12f14b0a0fbd95911976f
- evidence_id: bgc-2422-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-current243-first-five-diagnostic-reading-001.json
  locator: /records/1; /coverage; /lossless_reading_method; /readings; /limits
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'BGC personally read all ten first-five forms: 420 atom rows and 438 bond
    rows, including every scalar/string/ring/stereo/motif/map field. Exact common-value
    and constant-column factoring was reconstructed losslessly; no reparse.'
  snapshot_sha256: 24aa659950e9a1e06cc35d7aca13b02fc01e8f346760124c7c0cb97ab2930758
- evidence_id: bgc-2422-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /scalar_results/1; /warnings;
    /limitations
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: ROOT accepted one original twenty-form diagnostic. This owner’s scalar
    results are explicit; four global stderr warnings remain unassigned to records.
    Natural identity and claim-specific interpretation remain separate.
  snapshot_sha256: a93e9d5429154ef3e54a1049299fd86065e7551df82beb9c49e91b848fa65787
- evidence_id: bgc-2422-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact original execution, source and stdout/stderr pins.
  snapshot_sha256: 0129f39cb4f9773ffa73ced786859b7d33905900d2c1d092d54ed2839f17d6d4
- evidence_id: bgc-2422-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–430
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: The schema distinguishes undefined stereo from fabricated assignments and
    defines computed classification as named/versioned model output, never a source
    assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2422-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False)
    defines the stored flag via unassigned centers. It does not test double-bond completeness
    or natural stereochemical truth.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2422-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: The maintained seeder retains source structure/stereo and classifier arrays,
    with pathway filing from the model; faithful retention is distinct from applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2422-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-current243-source-reading-001.json
  locator: /scope; /reading; /division; /physical_join_verification; /cautions
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'BGC personally read contexts 0–8: 81 complete frames, 31 positive rows
    and 396 fields, including these five owners and four unselected Brasilane contexts.
    Prior raw/history carries remain attributed.'
  snapshot_sha256: eed62a3a5970b9689ab38d5732cc9749bff0fc7e36bfc4f7561c1ba939f47422
- evidence_id: bgc-2422-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Actual fifteen-context scope combines BGC 31 rows, Support 15 rows and
    Native eight cache stanzas plus curation scan. Historical conditional fields remain
    distinct from later earned runtime acceptances.
  snapshot_sha256: f9cb956d084c97bd6e0eda881981ffd6089e8271792437c1b94188d8afd65a40
- evidence_id: bgc-2422-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/root-source-plan-acceptance-001.json
  locator: /status
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: ROOT accepted the original composed source plan and exact input maps; no
    source-table query is replayed for this review.
  snapshot_sha256: 3654dc31a31787379bb3afc90c454264eead72eb18553e3b753539911bb06391
- evidence_id: bgc-2422-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-implemented-curation-scan-001.json
  locator: /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions;
    /assays; /guidance
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Ignored-inclusive scan of eight implemented tables and unresolved-taxonomy
    diagnostics found four inapplicable lexical matches, no applicable correction
    or exclusion. No actual AID is present; absence of an exclusion does not validate
    assay or natural identity.
  snapshot_sha256: b6f3bec95f889d74d38d39907c3c311b066e0611ca3512cf3e6e73d719eb4aa7
  search_scope: '{"contexts": 15, "tokens": 120, "owner_pins": [{"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/brasilane-a.yaml",
    "sha256": "ad9d6c81134c14e495ce5b385b3cdf3581740b9d3e1318770cc5dfeec5951261",
    "bytes": 2609}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/brasilane-d.yaml",
    "sha256": "9e708a2e090dbc1260666cd78393c9d1afc462d65a73b9c694c0e218b3290495",
    "bytes": 3479}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/brasilane-e.yaml",
    "sha256": "f341965e6fc5cee18d52eeabca4eed2d8b87d2c78b475c0a45bb9952f3f54517",
    "bytes": 3491}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/brasilane-f.yaml",
    "sha256": "eba2703e50c44d7c8069d5e3c19f577b1e88e3d6e4e2588d009bae1f891048cc",
    "bytes": 3379}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/trehangelin.yaml",
    "sha256": "d712704f8aaf78a965b8b1671b2796ad0a7799df4b085b98051374ce931c3482",
    "bytes": 3422}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/trichobrasilenol.yaml",
    "sha256": "2ec4a7287c9776fe96c0b325e89b8dba8f54f41d50b9ea57698aa5190417eaf1",
    "bytes": 16785}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/viguiepinol.yaml",
    "sha256": "2d8a4d400e714293c16e47cb1c2cc9fa9e19420d12e0dc7a4968faf2996ba8ea",
    "bytes": 2483}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/xanthan.yaml",
    "sha256": "d96e992370ff4b17054a042a4d64e02bb0030424d4e0e7beca61111f17a62ee1",
    "bytes": 3340}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/xylarenic-acid-b.yaml",
    "sha256": "706e8b2a674d3191d483cefe3f2adc1b45d7af822b968c4f78b0c3d890bd07ca",
    "bytes": 3418}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yanuthone-d.yaml",
    "sha256": "31dea0846e8b484b9167ae83114f89cf49415d7f0613eb3e0c4149912b7ba7c9",
    "bytes": 3602}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-i.yaml",
    "sha256": "c6713b478c05ee63949bb427cd6febd92cde60d5504a0df6c02e566656107ae7",
    "bytes": 2981}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-ii.yaml",
    "sha256": "e3dca931c852f1781bf2d187ce80b8169bfa56da7c91abbf320950038c115f04",
    "bytes": 3081}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-iii.yaml",
    "sha256": "d0623e4ce00c6e96d6b72795619c1ee221555398275e6983aee42cf2b41698aa",
    "bytes": 3179}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-iv.yaml",
    "sha256": "41e425e86f42463c53d7285f1ea7937112cb26700ca674c229e450385125c552",
    "bytes": 3261}, {"path": "/private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-v.yaml",
    "sha256": "f0f1eed9d896500698c0bfc6f2e187ea7d6082ee45f5a751ff2d4bb791a4f48b",
    "bytes": 3281}], "exact_source_ids": ["BGC0000170:1", "BGC0000286:1", "BGC0000800:1",
    "BGC0001810:1", "BGC0002260:1", "BGC0002260:2", "BGC0002260:3", "BGC0002260:4",
    "BGC0002260:5", "BGC0002260:6", "BGC0002402:1", "BGC0002402:2", "BGC0002402:3",
    "BGC0002402:4", "BGC0002402:5"], "token_scope": "All context owner IDs/full InChIKeys/explicit
    owned BGCs/labels/slugs and literal source taxa/chemical identifiers, plus actual
    nonblank AID tuples (none); full retained token map in finite DATA /tokens.",
    "ignored_files_included": true, "enumeration": ["/private/tmp/npm-record-reviews-20261021/curation/decisions.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/lotus_occurrence_exclusions.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/mibig_claim_references.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/mibig_locus_evidence_overrides.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/mibig_producer_isolates.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/mibig_producer_strains.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/mibig_structure_corrections.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/mibig_xref_exclusions.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv",
    "/private/tmp/npm-record-reviews-20261021/curation/source_queue.tsv", "/private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv"],
    "implemented_tables": 8, "implemented_rows": 93, "diagnostic_tables": 1, "diagnostic_rows":
    3329, "all_scanned_rows": 3422, "excluded": ["curation/decisions.tsv: reserved
    unimplemented format", "curation/source_queue.tsv: general source-adoption queue"],
    "literal_search": "Case-insensitive substring scan of every field; classify all
    positive lexical matches using exact identity keys, not substring alone."}'
- evidence_id: bgc-2422-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/3; /cached_taxonomy/whole_stanzas/5
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Complete retained taxon stanzas locate exact cached names/synonyms for
    this source context. Strain, species and producer/occurrence roles are not collapsed
    or freshly resolved.
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: bgc-2422-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/native-prep/native-current243-cached-taxonomy-reading-001.json
  locator: /scope; /taxonomy; /cached_names; /interpretation; /reading_outputs; /limitations
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Native personally read all eight saved stanzas and every route. BGC carries
    that explicit attribution; no fresh taxonomy lookup or duplicate positive-source-row
    credit.
  snapshot_sha256: 7eb3dc20b9bb5259d999c82830a794576f16aee4c95cd1b69d0f07145000e7ee
- evidence_id: bgc-2422-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-target-input-plan-001.json
  locator: /records/1/proposed_companion_paths; /records/1/direct_companion_predicates
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact direct-context paths and literal predicates; shared owned-BGC context
    does not transfer identity, stereo, mechanism or activity.
  snapshot_sha256: 91ac3acc1e6264332df09dbaac2293537c6c971feaddfd56c7c06d905026a0cd
- evidence_id: bgc-2422-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/0/path; /contexts/0/identifier; /contexts/0/label; /contexts/0/standard_inchi_key;
    /contexts/0/owned_bgc_ids; /contexts/1/path; /contexts/1/identifier; /contexts/1/label;
    /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/2/path; /contexts/2/identifier;
    /contexts/2/label; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids;
    /contexts/3/path; /contexts/3/identifier; /contexts/3/label; /contexts/3/standard_inchi_key;
    /contexts/3/owned_bgc_ids; /contexts/8/path; /contexts/8/identifier; /contexts/8/label;
    /contexts/8/standard_inchi_key; /contexts/8/owned_bgc_ids
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Direct companions retain distinct full keys and labels under their explicit
    BGC ownership. Compact identity context is not claim transfer.
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
- evidence_id: bgc-2422-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 matching placements with exact
    predicate/query and all fields. Negative scope is limited to this retained join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; mibig_compounds, exact predicate exact
    complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N". All
    matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2716–2716; row_sha256 7f57bbb0b46f83655aa0963d2d635c1d7d43f5f9c0073b0a177f643f227f4162
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact full-key/version/compound-index and all source producer/locus/citation-tier
    fields. BGC complete source-row reading carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2422-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 1 matching placements with exact
    predicate/query and all fields. Negative scope is limited to this retained join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; chebi_structures, exact predicate
    exact complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N".
    All matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: Header line 1; physical lines 43374–43374; row_sha256 c17d6b71acd65bae107c9a1a815a8fd31680dc46193f5ebdb80fe7a901f7797a
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact retained ChEBI identifier, full structure key and definition. BGC
    complete source-row reading carries.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2422-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 matching placements with exact
    predicate/query and all fields. Negative scope is limited to this retained join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; lotus_occurrences, exact predicate
    exact complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N".
    All matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 1113–1113; row_sha256 2f3eda34012601e2c192b2588e446314cb779179e7b0435cbb87f2035d3af1f5
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Complete organism/reference occurrence assertion, not producer or independent-study
    proof. BGC complete source-row reading carries.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2422-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 matching placements with
    exact predicate/query and all fields. Negative scope is limited to this retained
    join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; cyanometdb_occurrences, exact predicate
    exact complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N".
    All matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 matching placements with exact predicate/query
    and all fields. Negative scope is limited to this retained join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; npclassifier, exact predicate exact
    complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N". All
    matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 431–431; row_sha256 b063d22be2f099daf9cf150409ccb9ac3bd1c367c73ae0aa486783172742c20f
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact named/versioned classifier arrays and glycoside flag; applicability
    is a separate assessment. BGC complete source-row reading carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2422-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 1 matching placements with exact
    predicate/query and all fields. Its blank-AID row is a no-assay sentinel.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; pubchem_bioassay, exact predicate
    exact complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N".
    All matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 1453–1453; row_sha256 46f821136f2429659d8d1d362d6668a490183cfe611bc649916b4765e1024b37
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: Exact full-key/CID sentinel with blank AID and no assay outcome, measurement,
    target or reference; not inactivity. BGC complete source-row reading carries.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2422-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 matching placements with exact
    predicate/query and all fields. Negative scope is limited to this retained join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; bindingdb_targets, exact predicate
    exact complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N".
    All matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 matching placements with
    exact predicate/query and all fields. Negative scope is limited to this retained
    join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; antibioticmech_inchikeys, exact predicate
    exact complete standard_inchi_key equality, query "DJBXKQSFHIRXRM-JRYBIPSHSA-N".
    All matching payloads or the complete empty frame are retained. No external lookup
    or query replay.
- evidence_id: bgc-2422-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch243-tentative/bgc-prep/bgc-conditional243-source-inventory-DATA-001.json
  locator: /contexts/5/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 matching placements with exact predicate/query
    and all fields. Negative scope is limited to this retained join.'
  snapshot_sha256: 025dbc1bd5fbb8ae4f9fbd2f05a9cc6c08caf6a21f13b4b88d9563cf399e073f
  search_scope: Original saved local inventory; chebi_origins, exact predicate exact
    chebi_id from exact full-key structure rows, query ["CHEBI:167379"]. All matching
    payloads or the complete empty frame are retained. No external lookup or query
    replay.
- evidence_id: bgc-2422-reader-DATA
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/native-current243-trichobrasilenol-maintained-reader-DATA-001.json
  locator: /status; /reader_call_count; /raw_owner; /expected_view; /resolved_view;
    /component_captures; /returned_view_equals_expected_complete_owner; /view_mismatches;
    /counts; /denials; /unexpected_denials; /errors; /post_pin_failures; /limitations
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: One original maintained call preserves the complete owner, two graphs,
    ten edge-reference placements and four histories exactly. The known socket-construction
    probe was denied before action; no unexpected denial or error. Biological and
    primary-source limits remain explicit.
  snapshot_sha256: bc89c9c96efc748f498252bc6254e8297ee0e725bf3fbbfef8826daab63a89eb
- evidence_id: bgc-2422-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/native-current243-trichobrasilenol-reader-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /actual_environment; /stdout;
    /stderr; /DATA; /original_process_receipt; /original_tool_file; /original_start_tool;
    /original_tool; /operator
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: BGC operated the single admitted original reader launch; one empty start
    object and genuine terminal 0 are preserved. Controller observer attribution remains
    distinct from operator.
  snapshot_sha256: 89736667b6180805a38263e7306893f0ea3aa5913119812c6c84b17ef7eaca73
- evidence_id: bgc-2422-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch243/root-current243-trichobrasilenol-reader-acceptance-001.json
  locator: /status; /order; /DATA; /execution; /verification; /review_check_contract;
    /runtime_environment_delta; /limitations
  accessed_at: '2026-11-04T17:32:57.754027Z'
  support: supports
  summary: ROOT accepted the exact original reader and typed review check contract,
    complete-owner equality and positive content. Runtime-added __CF_USER_TEXT_ENCODING
    is explicit, without changing the launch environment.
  snapshot_sha256: d30514e6a1d299edba6bed73521b2137527992e9e36ebeea567894a09f3ebda8
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:55:02.739193Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: d4bd86d11da0cdff7ea8d2f5e606f7acf91688bd00ade940fd6f64bed0849036
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:55:27.551506Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 0fc23d99fc43282086aac001026995a6b725d41dd7ca97d430a2d4af2e8cad4b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:55:47.023037Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:56:20.820932Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-243/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-243/native-current243-five-gates-execution-001.json
  accessed_at: '2026-11-04T16:56:32.540355Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: c1ffddf8e5ee40c30ec339073c0402934ebfb573993911f7fc890b95e4ac8fe5
assessments:
- assessment_id: bgc-2422-identity
  area: identity
  topic: Exact retained source join and bounded natural-identity scope
  outcome: supported
  summary: CHEBI:167379 and MIBiG BGC0002260 compound 1 join the complete key DJBXKQSFHIRXRM-JRYBIPSHSA-N.
    The retained ChEBI carbobicyclic/sesquiterpenoid definition names a Trichoderma
    cyclase context, while the imported MIBiG producer is Annulohypoxylon truncatum.
    PubChem 146682173 and NPAtlas NPA025694 remain cross-references. Both forms normalize
    to neutral C15H26O and the declared key. Exact source alignment does not merge
    organism roles, verify the natural material, or transfer claims from the five
    distinct-key BGC2260 companions.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-grounding-owner
  - bgc-2422-chemistry
  - bgc-2422-source-mibig_compounds
  - bgc-2422-query-chebi_structures
  - bgc-2422-direct-contexts
  - bgc-2422-companion-boundaries
  - bgc-2422-source-chebi_structures
  dimensions:
  - name: standard_inchi_key
    value: DJBXKQSFHIRXRM-JRYBIPSHSA-N; exact retained key, not natural identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2422-grounding-owner
    - bgc-2422-chemistry
    - bgc-2422-source-mibig_compounds
    - bgc-2422-query-chebi_structures
    - bgc-2422-direct-contexts
    - bgc-2422-companion-boundaries
    - bgc-2422-source-chebi_structures
  - name: grounding_scope
    value: CHEBI:167379 and MIBiG BGC0002260 compound 1 join the complete key DJBXKQSFHIRXRM-JRYBIPSHSA-N.
      The retained ChEBI carbobicyclic/sesquiterpenoid definition names a Trichoderma
      cyclase context, while the imported MIBiG producer is Annulohypoxylon truncatum.
      PubChem 146682173 and NPAtlas NPA025694 remain cross-references. Both forms
      normalize to neutral C15H26O and the declared key. Exact source alignment does
      not merge organism roles, verify the natural material, or transfer claims from
      the five distinct-key BGC2260 companions.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2422-grounding-owner
    - bgc-2422-chemistry
    - bgc-2422-source-mibig_compounds
    - bgc-2422-query-chebi_structures
    - bgc-2422-direct-contexts
    - bgc-2422-companion-boundaries
    - bgc-2422-source-chebi_structures
- assessment_id: bgc-2422-representation
  area: representation
  topic: Original stored-form and stereochemical scope
  outcome: supported
  summary: Both forms have 16 heavy atoms, 17 bonds, three specified tetrahedral centers
    and one specified E double bond. All ten saved comparisons are true with a complete
    supplied chirality-aware atom match. The actual E assignment is SMILES bond 3
    C1=C4, corresponding to reconstructed bond 14 C10=C13. full_graph_identity_established
    remains false; this local consistency is not independent primary stereochemical
    or natural-identity confirmation.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-grounding-owner
  - bgc-2422-chemistry
  - bgc-2422-topology
  - bgc-2422-diagnostic-reading
  - bgc-2422-diagnostic-acceptance
  - bgc-2422-structure-schema
  - bgc-2422-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms have 16 heavy atoms, 17 bonds, three specified tetrahedral centers
      and one specified E double bond. All ten saved comparisons are true with a complete
      supplied chirality-aware atom match. The actual E assignment is SMILES bond
      3 C1=C4, corresponding to reconstructed bond 14 C10=C13. full_graph_identity_established
      remains false; this local consistency is not independent primary stereochemical
      or natural-identity confirmation.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2422-grounding-owner
    - bgc-2422-chemistry
    - bgc-2422-topology
    - bgc-2422-diagnostic-reading
    - bgc-2422-diagnostic-acceptance
    - bgc-2422-structure-schema
    - bgc-2422-stereo-method
  - name: representation_correspondence
    value: All ten comparisons are true and the supplied atom match is complete at
      its stated scope; full_graph_identity_established remains false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2422-grounding-owner
    - bgc-2422-chemistry
    - bgc-2422-topology
    - bgc-2422-diagnostic-reading
    - bgc-2422-diagnostic-acceptance
    - bgc-2422-structure-schema
    - bgc-2422-stereo-method
- assessment_id: bgc-2422-provenance
  area: provenance
  topic: Distinct producer, locus and taxon assertions
  outcome: supported
  summary: BGC0002260 v3 compound 1 retains Annulohypoxylon truncatum NCBITaxon:327061
    as SOURCE_ASSERTION. Heterologous expression grades the MT383109.1 locus CLUSTER_DEMONSTRATED,
    a distinct question from native production or strain/construct identity. The Trichoderma
    occurrence/definition and historical TaTC6 reference context do not place TaTC6
    in this BGC or upgrade imported producer evidence.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-origin-owner
  - bgc-2422-occurrence-owner
  - bgc-2422-source-mibig_compounds
  - bgc-2422-cached-taxonomy
  - bgc-2422-curation-scope
  - bgc-2422-direct-contexts
  - bgc-2422-mechanism-owner
  dimensions:
  - name: taxon_scope
    value: BGC0002260 v3 compound 1 retains Annulohypoxylon truncatum NCBITaxon:327061
      as SOURCE_ASSERTION. Heterologous expression grades the MT383109.1 locus CLUSTER_DEMONSTRATED,
      a distinct question from native production or strain/construct identity. The
      Trichoderma occurrence/definition and historical TaTC6 reference context do
      not place TaTC6 in this BGC or upgrade imported producer evidence.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2422-origin-owner
    - bgc-2422-occurrence-owner
    - bgc-2422-source-mibig_compounds
    - bgc-2422-cached-taxonomy
    - bgc-2422-curation-scope
    - bgc-2422-direct-contexts
    - bgc-2422-mechanism-owner
  - name: producer_evidence
    value: BGC0002260 v3 compound 1 retains Annulohypoxylon truncatum NCBITaxon:327061
      as SOURCE_ASSERTION. Heterologous expression grades the MT383109.1 locus CLUSTER_DEMONSTRATED,
      a distinct question from native production or strain/construct identity. The
      Trichoderma occurrence/definition and historical TaTC6 reference context do
      not place TaTC6 in this BGC or upgrade imported producer evidence.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2422-origin-owner
    - bgc-2422-occurrence-owner
    - bgc-2422-source-mibig_compounds
    - bgc-2422-cached-taxonomy
    - bgc-2422-curation-scope
    - bgc-2422-direct-contexts
    - bgc-2422-mechanism-owner
  - name: locus_evidence
    value: BGC0002260 v3 compound 1 retains Annulohypoxylon truncatum NCBITaxon:327061
      as SOURCE_ASSERTION. Heterologous expression grades the MT383109.1 locus CLUSTER_DEMONSTRATED,
      a distinct question from native production or strain/construct identity. The
      Trichoderma occurrence/definition and historical TaTC6 reference context do
      not place TaTC6 in this BGC or upgrade imported producer evidence.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2422-origin-owner
    - bgc-2422-occurrence-owner
    - bgc-2422-source-mibig_compounds
    - bgc-2422-cached-taxonomy
    - bgc-2422-curation-scope
    - bgc-2422-direct-contexts
    - bgc-2422-mechanism-owner
- assessment_id: bgc-2422-citations
  area: evidence
  topic: Retained citation and history attribution
  outcome: supported
  summary: PMID:32936132 is the imported MIBiG ENTRY citation; DOI:10.1002/ANIE.201907964
    is the LOTUS occurrence reference. The two retained graphs contain ten reference
    placements, including repeated database URLs and historical native-sequence inferences;
    these are not ten independently read studies. The BraB history records inaccessible
    primary DOI:10.1039/D0CC03950K, and the TaTC6 history records inaccessible PMID:31418991/DOI:10.1002/anie.201907964
    and supplementary information. The two seed events and two curation events remain
    intact. This review reads those attributions, not fresh primary text.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-owner
  - bgc-2422-origin-owner
  - bgc-2422-occurrence-owner
  - bgc-2422-source-mibig_compounds
  - bgc-2422-source-reading
  - bgc-2422-source-lotus_occurrences
  - bgc-2422-mechanism-owner
  dimensions:
  - name: citation_scope
    value: PMID:32936132 is the imported MIBiG ENTRY citation; DOI:10.1002/ANIE.201907964
      is the LOTUS occurrence reference. The two retained graphs contain ten reference
      placements, including repeated database URLs and historical native-sequence
      inferences; these are not ten independently read studies. The BraB history records
      inaccessible primary DOI:10.1039/D0CC03950K, and the TaTC6 history records inaccessible
      PMID:31418991/DOI:10.1002/anie.201907964 and supplementary information. The
      two seed events and two curation events remain intact. This review reads those
      attributions, not fresh primary text.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2422-owner
    - bgc-2422-origin-owner
    - bgc-2422-occurrence-owner
    - bgc-2422-source-mibig_compounds
    - bgc-2422-source-reading
    - bgc-2422-source-lotus_occurrences
    - bgc-2422-mechanism-owner
- assessment_id: bgc-2422-occurrence
  area: evidence
  topic: Bounded occurrence and no-assay scope
  outcome: supported
  summary: One LOTUS Trichoderma atroviride NCBITaxon:63577 occurrence is retained,
    separate from Annulohypoxylon truncatum NCBITaxon:327061 producer/locus claims.
    The exact-key cyanobacterial and ChEBI-origin frames are empty. The cached names
    support the two retained taxon identities at their local scope; neither occurrence
    nor a definition authenticates native production or an experimental strain.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-occurrence-owner
  - bgc-2422-source-pubchem_bioassay
  - bgc-2422-query-lotus_occurrences
  - bgc-2422-query-chebi_origins
  - bgc-2422-query-cyanometdb_occurrences
  - bgc-2422-query-pubchem_bioassay
  - bgc-2422-query-bindingdb_targets
  - bgc-2422-cached-taxonomy
  - bgc-2422-taxonomy-reading
  - bgc-2422-curation-scope
  - bgc-2422-source-lotus_occurrences
  dimensions:
  - name: occurrence_scope
    value: One LOTUS Trichoderma atroviride NCBITaxon:63577 occurrence is retained,
      separate from Annulohypoxylon truncatum NCBITaxon:327061 producer/locus claims.
      The exact-key cyanobacterial and ChEBI-origin frames are empty. The cached names
      support the two retained taxon identities at their local scope; neither occurrence
      nor a definition authenticates native production or an experimental strain.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2422-occurrence-owner
    - bgc-2422-source-pubchem_bioassay
    - bgc-2422-query-lotus_occurrences
    - bgc-2422-query-chebi_origins
    - bgc-2422-query-cyanometdb_occurrences
    - bgc-2422-query-pubchem_bioassay
    - bgc-2422-query-bindingdb_targets
    - bgc-2422-cached-taxonomy
    - bgc-2422-taxonomy-reading
    - bgc-2422-curation-scope
    - bgc-2422-source-lotus_occurrences
  - name: assay_target_scope
    value: The complete owner lacks bioactivities, bioactivity_summary and molecular_targets.
      Its exact-key PubChem row has blank AID, the literal assay name (no assay data),
      and blank outcome, quantitative measurement, target and reference fields. It
      is a no-assay sentinel, not an inactive result. The BindingDB join is empty;
      these retained-table limits do not establish absence of published activity.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2422-occurrence-owner
    - bgc-2422-source-pubchem_bioassay
    - bgc-2422-query-lotus_occurrences
    - bgc-2422-query-chebi_origins
    - bgc-2422-query-cyanometdb_occurrences
    - bgc-2422-query-pubchem_bioassay
    - bgc-2422-query-bindingdb_targets
    - bgc-2422-cached-taxonomy
    - bgc-2422-taxonomy-reading
    - bgc-2422-curation-scope
    - bgc-2422-source-lotus_occurrences
- assessment_id: bgc-2422-classification
  area: consistency
  topic: Versioned model fidelity and applicability limits
  outcome: supported
  summary: The versioned NPClassifier output is Terpenoids/Sesquiterpenoids/Tremulane
    sesquiterpenoids with is_glycoside:false. The C15 carbon-bicyclic alcohol topology
    supports retaining a non-glycoside structural description. The named Tremulane
    prediction, ChEBI definition and source TERPENE class remain distinct assertions;
    faithful retention does not independently establish biosynthetic family or primary
    structural assignment.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-classification-owner
  - bgc-2422-source-npclassifier
  - bgc-2422-chemistry
  - bgc-2422-topology
  - bgc-2422-structure-schema
  - bgc-2422-classification-seeder
  - bgc-2422-source-mibig_compounds
  - bgc-2422-grounding-owner
  dimensions:
  - name: classification_applicability
    value: The versioned NPClassifier output is Terpenoids/Sesquiterpenoids/Tremulane
      sesquiterpenoids with is_glycoside:false. The C15 carbon-bicyclic alcohol topology
      supports retaining a non-glycoside structural description. The named Tremulane
      prediction, ChEBI definition and source TERPENE class remain distinct assertions;
      faithful retention does not independently establish biosynthetic family or primary
      structural assignment.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2422-classification-owner
    - bgc-2422-source-npclassifier
    - bgc-2422-chemistry
    - bgc-2422-topology
    - bgc-2422-structure-schema
    - bgc-2422-classification-seeder
    - bgc-2422-source-mibig_compounds
    - bgc-2422-grounding-owner
- assessment_id: bgc-2422-mechanism
  area: consistency
  topic: Complete preserved historical mechanisms; primary limits
  outcome: unknown
  summary: 'The complete owner retains two inline BIOSYNTHESIS graphs: BraB substrate
    glycosylation has four nodes and three edges; TaTC6 product formation has three
    nodes and two edges. There are no pathway, component-reference or molecular-target
    roots. BraB consumes exact trichobrasilenol; it is not its terpene synthase. TaTC6
    formation is a separate database-reported route. The accepted single maintained
    call returns the entire captured owner exactly, including all seven nodes, five
    edges, ten reference placements and four histories. One known socket-construction
    capability probe was denied before action, with no unexpected denial or error.
    Structural preservation does not independently validate the biological claims.'
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-mechanism-owner
  - bgc-2422-reader-DATA
  - bgc-2422-reader-execution
  - bgc-2422-reader-acceptance
  - bgc-2422-origin-owner
  - bgc-2422-occurrence-owner
  - bgc-2422-direct-contexts
  dimensions: []
- assessment_id: bgc-2422-protein
  area: identity
  topic: Historically attributed native reference and construct limits
  outcome: unknown
  summary: The retained BraB mapping identifies native Annulohypoxylon truncatum CBS140778
    P9WER1/QOE88884.1, historically compared over 421 amino acids and reverse CDS
    MT383109.1:2625–3890. The separate TaTC6 mapping identifies native Trichoderma
    atroviride FKI-3849 A0A5S9I252/BBK61014.1, historically compared over 386 amino
    acids and a six-exon LC484924.1 CDS. These are attributed historical reference
    correspondences, not newly checked sequences or complete assayed constructs/tags.
    Putative UDP-GlcNAc donor, stereochemically incomplete ungrounded Brasilane A,
    disputed pathway finality, TaTC6 side-product specificity, koraiol phenotype,
    homodimer and Mg-binding scopes remain qualified or unadopted as written. No kinetics,
    physical complex, measured donor preference or native-producer upgrade is inferred.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-mechanism-owner
  - bgc-2422-reader-DATA
  - bgc-2422-reader-acceptance
  dimensions: []
- assessment_id: bgc-2422-completion
  area: completeness
  topic: Actual evidence coverage and remaining scientific limits
  outcome: unknown
  summary: Complete owner/history, actual canonical intake, retained source payloads
    and empty frames, and both original molecular forms have been read. The accepted
    single maintained call also preserves both complete graphs and all four histories.
    The owner remains EXACT and SEEDED with 4 unchanged history events. Its intake
    identifies source seeder/extractor/classifier ownership separately from curator-owned
    mechanism/history where present. The ignored-inclusive bounded curation scan reports
    no applicable correction. Full QC/OAK, fresh primary, taxonomy, assay and construct
    verification, and independent natural identity or stereochemistry remain unavailable.
    This is a partial review with no supported source-edit finding.
  target_ids:
  - CHEBI:167379
  evidence_ids:
  - bgc-2422-owner
  - bgc-2422-capture
  - bgc-2422-intake
  - bgc-2422-intake-acceptance
  - bgc-2422-history-owner
  - bgc-2422-diagnostic-reading
  - bgc-2422-diagnostic-acceptance
  - bgc-2422-diagnostic-execution
  - bgc-2422-source-reading
  - bgc-2422-joint-source-notes
  - bgc-2422-source-plan-acceptance
  - bgc-2422-curation-scope
  - bgc-2422-mechanism-owner
  - bgc-2422-reader-DATA
  - bgc-2422-reader-execution
  - bgc-2422-reader-acceptance
  dimensions:
  - name: review_completion
    value: Complete owner/history, actual canonical intake, retained source payloads
      and empty frames, and both original molecular forms have been read. The accepted
      single maintained call also preserves both complete graphs and all four histories.
      The owner remains EXACT and SEEDED with 4 unchanged history events. Its intake
      identifies source seeder/extractor/classifier ownership separately from curator-owned
      mechanism/history where present. The ignored-inclusive bounded curation scan
      reports no applicable correction. Full QC/OAK, fresh primary, taxonomy, assay
      and construct verification, and independent natural identity or stereochemistry
      remain unavailable. This is a partial review with no supported source-edit finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2422-owner
    - bgc-2422-capture
    - bgc-2422-intake
    - bgc-2422-intake-acceptance
    - bgc-2422-history-owner
    - bgc-2422-diagnostic-reading
    - bgc-2422-diagnostic-acceptance
    - bgc-2422-diagnostic-execution
    - bgc-2422-source-reading
    - bgc-2422-joint-source-notes
    - bgc-2422-source-plan-acceptance
    - bgc-2422-curation-scope
    - bgc-2422-mechanism-owner
    - bgc-2422-reader-DATA
    - bgc-2422-reader-execution
    - bgc-2422-reader-acceptance
findings: []
actions: []
limitations:
- Retained local evidence only. Fresh primary papers, taxonomy, assay protocols and
  independent natural identity/stereochemical authentication remain unavailable.
- Full QC and complete OAK coverage remain unavailable. Saved normalized forms, motifs
  and atom matches do not establish independent full graph or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain distinct. Shared loci
  and repeated references do not transfer biological claims or establish independent
  experiments.
- Versioned model fidelity is assessed separately from applicability; the stated concerns
  do not prove source-ingestion defects or authorize record replacement.
- The accepted reader preserves complete historical graph and native-reference assertions
  without freshly verifying primary experiments, sequences, constructs, kinetics or
  physical complexes.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read all ten first-five molecular forms: 420 atom rows and 438 bond
  rows, plus every scalar/string/ring/stereo/motif/map field. Diagnostic indices are
  zero-based, not biochemical locants; four global stderr warnings remain unassigned.'
- 'Disjoint source reading: BGC nine contexts/81 frames/31 rows/396 fields; Support
  six contexts/54 frames/15 rows/215 fields. Native read all eight complete cache
  stanzas and the ignored-inclusive curation scan, with zero positive-source-row credit.
  Prior whole raw/history carries remain attributed.'
- ROOT operated the local collector, composer and canonical intakes; Native operated
  the original molecular diagnostic. BGC operated the sole original maintained reader;
  Native and Support supplied the separately attributed method, dependency, descriptor
  and binding peers. No new target is invoked by fragment authoring.
- All scientific outcomes remain partial; no supported source-record edit finding
  or action is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-243
```
