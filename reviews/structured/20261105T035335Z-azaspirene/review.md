# Local evidence review: azaspirene

- Review: 20261105T035335Z-azaspirene
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T02:59:53.426433Z
- Finished UTC: 2026-11-05T03:53:35.118309Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Azaspirene retains the exact source structure and a preserved, explicitly partial Af293 reconstitution graph. A one-site lactam/lactim representation difference is bounded; PsoG accession and full constructs remain unresolved. Shared-BGC Pseurotin assays are context only. This review remains partial without new sequence, primary or assay claims.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2502; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-a469ae857b | data/natural_products/unclassified/azaspirene.yaml | generated | azaspirene |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for azaspirene | passed | True | naturalproductmech:mibig-a469ae857b | One original offline maintained call preserved the complete Azaspirene owner: one graph, eight nodes, eight edges and three histories, with no pathway or components. This does not independently validate historical scientific or protein assertions. |
| strict_ten | passed | True | naturalproductmech:mibig-a469ae857b | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-a469ae857b | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-a469ae857b | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-a469ae857b | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-a469ae857b | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-a469ae857b | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-a469ae857b | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-a469ae857b | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained encoding and bounded identity correspondence

identity: supported. Targets: naturalproductmech:mibig-a469ae857b.

The minted naturalproductmech:mibig-a469ae857b owner retains QLKGRMRPKQNCRR-XXPFWKOGSA-N, C21H23NO5 and NPA06799 from MIBiG BGC0001037 version 5. Both forms regenerate the declared key/Standard InChI but canonical strings differ at the ring lactam/lactim site. The exact local ChEBI full-key frame is empty. Pseurotin SLYDIPAXCVVRNY-BBJHAQHQSA-N is a distinct C22H25NO8 encoding with incomplete stereochemistry; the shared BGC does not establish equivalence or transfer xrefs, absolute configuration or activity.

### Stored-form topology and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-a469ae857b.

The single lactam/lactim bond-and-hydrogen shift is directly visible in the complete saved tables. Both forms retain three specified tetrahedral centers and two specified E double bonds, consistent with the scoped stereo_complete=true flag. Empty direct atom correspondence and false canonical comparisons remain explicit. Historical Figure1/structure agreement in the discussion is retained attribution, not a new absolute-configuration experiment.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-a469ae857b.

MIBiG BGC0001037 version 5 retains Af293 taxon 330879 as BGC_CHARACTERIZED producer and CM000176.1:115218–134016 as CLUSTER_DEMONSTRATED locus, with knockout, enzymatic-assay and heterologous-expression method labels. These database grades remain separate from the precise historical graph claims. The Neosartorya 36629 LOTUS occurrence is genus-labelled and does not identify Af293 or add a strain-specific production experiment. The exact Pseurotin companion shares the locus and grades but cannot strengthen Azaspirene-specific identity, substrate specificity or activity.

### Citation tiers and complete history scope

evidence: supported. Targets: naturalproductmech:mibig-a469ae857b.

MIBiG PMID:25494235 is ENTRY attribution; LOTUS DOI:10.1021/OL020104+ is a separate occurrence assertion. The graph has twelve edge-reference placements, including eight placements of DOI:10.1021/ol503179v and four historical curator-inference references for three proteins and the PsoG nucleotide context. Repeated placements are not independent experiments. The three-event history includes two seedings and the 2026-10-12 curator graph event. The old uninspected supercluster paper failure remains historical; it was not retried or used to add methods claims.

### Source-specific occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-a469ae857b.

The selected owner retains one Neosartorya occurrence and no bioactivities or molecular_targets. Unselected Pseurotin alone has three deposited PubChem rows: AID:1845221 and 2202548 are Inconclusive with source Potency 11.6129 and 12.5893 micromolar, represented as OTHER rather than inferred IC50/EC50; AID:2202377 is Active with an ALDH3A1 inhibitor-screen title, no numeric endpoint and no grounded target. These rows neither establish anti-cancer/thiol/direct-binding mechanisms nor transfer to Azaspirene. Pseurotin’s Pseudeurotium ovale occurrence likewise remains its own source assertion.

### Reported model families and qualified applicability

consistency: supported. Targets: naturalproductmech:mibig-a469ae857b.

The versioned model reports Amino acids and Peptides&#124;Polyketides, Cyclic polyketides, no class result and is_glycoside=false. The spiro oxygen/nitrogen heterocycles are compatible with a cyclic mixed-origin scaffold, while the exact biosynthetic interpretation relies on the separately qualified source and graph evidence. Empty class results are retained without inventing a named subtype. Source NRPS/PKS and model-derived UNCLASSIFIED filing remain distinct axes; structural motifs alone do not prove enzyme sequence or natural pathway completion.

### Actual evidence coverage and remaining limitations

completeness: unknown. Targets: naturalproductmech:mibig-a469ae857b.

The whole raw/captured/expected/resolved owner, complete graph/history, 42-input canonical intake, nine selected source frames and nine Pseurotin context frames, and both full molecular forms were read. The maintained reader supplies preservation/topology evidence, not independent primary, sequence, producer or natural-identity validation. Open PsoG/construct/intermediate questions and current external verification remain unresolved, so completion is partial and SEEDED status is retained.

### Preserved reconstitution graph and bounded historical evidence

consistency: supported. Targets: naturalproductmech:mibig-a469ae857b.

The accepted maintained reader preserves one BIOSYNTHESIS graph with eight nodes, eight edges, twelve edge-reference placements and three history events; no ordered pathway or external component is declared. Four encoded-membership edges belong to the successful four-gene yeast BJ5464-NpgA reconstruction; detected product matching does not demonstrate isolated-enzyme sufficiency, a physical complex or native essentiality. PsoA priming and propionyl-CoA preference are scoped to historical in-vitro/competition evidence, not exclusive substrate use or complete in-vitro synthesis. PsoG omission changed peaks 7/8 whose structures were not determined; it does not establish a purified hydroxylation reaction. The graph explicitly excludes Pseurotin transfer and direct PsoB catalytic assignment.

### Historical enzyme references and unresolved construct limits

identity: unknown. Targets: naturalproductmech:mibig-a469ae857b.

PsoA Q4WAZ9/4007 aa, PsoB Q4WAZ8/445 aa and PsoF Q4WAZ0/905 aa remain historical Af293 reference associations, distinct from the complete tagged experimental inserts. The N-FLAG/C-His6 PsoA, bacterial N-His6 proteins and separate yeast vector contexts are preserved. PsoG remains accession-unresolved; the neighboring AFUA_8G00430/Q4WAY9/EAL85123.1 157-aa protein is explicitly excluded. Historical primer matching to nucleotide coordinates is not a validated splice model or exact assayed protein sequence. Earlier sequence/CDS/UniProt claims were not repeated here. The graph’s propionyl-starter preference versus database acetyl-starter statement remains an attributed conflict with its stated evidence priority.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2502-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/azaspirene.yaml; Complete plaintext including every curation_history entry | supports | Complete azaspirene owner and 3 history events; earlier whole reading carries by current identical bytes. |
| bgc-2502-capture | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1 | supports | Complete actual owner capture and metadata; preservation is not independent scientific validation. |
| bgc-2502-intake | /private/tmp/npm-review-work/shared-next-batch251/intakes/2502-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, maintained ownership and all 42 input placements joined to the accepted plan and current hashes. |
| bgc-2502-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch251/root-intake-acceptance-001.json; /status; /summary; /source_plan; /records/1 | supports | ROOT accepted this original canonical intake and its exact plan, inspection and receipt pins. |
| bgc-2502-grounding-owner | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/label; /records/1/owner_document/chemical_structure; /records/1/owner_document/xrefs; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status; /records/1/owner_document/grounding_notes; /records/1/owner_document/discussions | supports | Exact retained identifier, structure, cross-references where present, source concepts and grounding fields. Historical annotations do not constitute a fresh authority lookup. |
| bgc-2502-origin-owner | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups; /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts | supports | Exact separate producer/locus grades, methods, accessions, coordinates where declared and citation tiers. |
| bgc-2502-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1/owner_document | supports | Complete owner supplies the retained occurrences and bounded absence of selected bioactivity and molecular-target roots. Absence is not biological inactivity. |
| bgc-2502-classification-owner | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing and separate source categories; applicability is assessed separately. |
| bgc-2502-history-owner | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1/owner_document/curation_status; /records/1/owner_document/curation_history | supports | Complete history and status; seeding and historical curation do not imply new primary verification. |
| bgc-2502-mechanism-owner | /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json; /records/1/owner_document | supports | The accepted maintained reader preserves one BIOSYNTHESIS graph with eight nodes, eight edges, twelve edge-reference placements and three history events; no ordered pathway or external component is declared. Four encoded-membership edges belong to the successful four-gene yeast BJ5464-NpgA reconstruction; detected product matching does not demonstrate isolated-enzyme sufficiency, a physical complex or native essentiality. PsoA priming and propionyl-CoA preference are scoped to historical in-vitro/competition evidence, not exclusive substrate use or complete in-vitro synthesis. PsoG omission changed peaks 7/8 whose structures were not determined; it does not establish a purified hydroxylation reaction. The graph explicitly excludes Pseurotin transfer and direct PsoB catalytic assignment. PsoA Q4WAZ9/4007 aa, PsoB Q4WAZ8/445 aa and PsoF Q4WAZ0/905 aa remain historical Af293 reference associations, distinct from the complete tagged experimental inserts. The N-FLAG/C-His6 PsoA, bacterial N-His6 proteins and separate yeast vector contexts are preserved. PsoG remains accession-unresolved; the neighboring AFUA_8G00430/Q4WAY9/EAL85123.1 157-aa protein is explicitly excluded. Historical primer matching to nucleotide coordinates is not a validated splice model or exact assayed protein sequence. Earlier sequence/CDS/UniProt claims were not repeated here. The graph’s propionyl-starter preference versus database acetyl-starter statement remains an attributed conflict with its stated evidence priority. |
| bgc-2502-reader-result | /private/tmp/npm-review-work/shared-next-batch251/native-current251-azaspirene-maintained-reader-DATA-001.json; /status; /reader_call_count; /review_check_metadata; /raw_owner; /expected_view; /resolved_view; /counts; /returned_view_equals_expected_complete_owner; /view_mismatches; /errors; /denials; /unexpected_denials; /external_requests; /molecular_parses; /retries; /limitations | supports | One accepted maintained call preserved complete Azaspirene raw/captured/expected/resolved equality: one graph, eight nodes, eight edges, three histories and no components/pathway/targets. Historical science and protein limits remain attributed; the known capability probe was denied before action. |
| bgc-2502-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch251/root-native-reader-2502-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /order; /DATA; /execution; /original_tools; /process; /native_readback; /verification; /review_check_contract; /ROOT_result_reading; /network_boundary; /environment_boundary; /science_boundary; /external_requests | supports | ROOT accepted the exact original zero-exit reader and complete owner equality, with its review-check contract and scientific/network boundaries. |
| bgc-2502-reader-execution | /private/tmp/npm-review-work/shared-next-batch251/native-current251-azaspirene-reader-execution-001.json; /command; /cwd; /started_at; /finished_at; /exit_code; /stdout; /stderr; /DATA; /operator; /delegated_by | supports | Exact Native-operated command, zero exit, clocks and DATA/stream pins under ROOT delegation. |
| bgc-2502-chemistry | /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/formula; /records/1/smiles/computed/formal_charge; /records/1/smiles/computed/standard_inchi; /records/1/smiles/computed/standard_inchi_key; /records/1/smiles/computed/canonical_isomeric_smiles; /records/1/smiles/computed/canonical_nonisomeric_smiles; /records/1/smiles/computed/atom_count; /records/1/smiles/computed/heavy_atom_count; /records/1/smiles/computed/bond_count; /records/1/smiles/computed/element_counts; /records/1/smiles/computed/stereo_counts; /records/1/inchi/computed/formula; /records/1/inchi/computed/formal_charge; /records/1/inchi/computed/standard_inchi; /records/1/inchi/computed/standard_inchi_key; /records/1/inchi/computed/canonical_isomeric_smiles; /records/1/inchi/computed/canonical_nonisomeric_smiles; /records/1/inchi/computed/atom_count; /records/1/inchi/computed/heavy_atom_count; /records/1/inchi/computed/bond_count; /records/1/inchi/computed/element_counts; /records/1/inchi/computed/stereo_counts | supports | Eight of ten saved-form comparisons are true: formula, charge, Standard InChI, full key, atom/bond counts and declared-key checks agree. Canonical isomeric and nonisomeric SMILES differ, and the saved direct atom map is empty with full_graph_identity_established=false. The particular bond/hydrogen changes below support a bounded tautomer interpretation; they do not establish an independent complete graph correspondence, a preferred natural tautomer or experimental identity. |
| bgc-2502-topology | /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/diagnostic-DATA-001.json; /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons; /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds; /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo; /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices; /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings; /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs; /records/1/inchi/computed/fragment_atom_indices | supports | Each form contains 27 atoms and 29 bonds at charge 0, with two five-member rings sharing the spiro carbon and a six-member aromatic ring. SMILES N24-C25(=O26) in the N-containing ring is represented as InChI C18(OH24)=N21, while the other ketone persists. The O-containing five-member ring is unsaturated; there is no saturated C5O motif or ester linkage. Three tetrahedral sites and two E-configured chain double bonds are specified in both forms. The spiro carbon CIP label changes from S at SMILES atom 11 to R at InChI atom 20 as the lactam environment changes; this is not an independently demonstrated stereochemical inversion. |
| bgc-2502-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-current251-first-five-molecular-intake-reading-001.json; /records/1; /totals; /whole_reading; /raw_and_source_carry; /limits | supports | BGC complete saved first-five molecular and intake reading, with exact per-form table counts and reading attribution; no new parse. |
| bgc-2502-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/root-diagnostic-acceptance-001.json; /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools; /readback; /original_exit_code; /original_terminal_chunk; /molecular_parse_attempts; /parsed; /comparisons_true; /comparisons_total; /global_warning_count; /external_requests; /method_scope; /interpretation_boundary; /ROOT_result_reading; /verification; /scientific_verdicts | supports | ROOT accepted the original twenty stored-form diagnostics. Global warning interpretation and method limits remain explicit; no per-record warning assignment is inferred. |
| bgc-2502-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and source/stream pins. |
| bgc-2502-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–433 | supports | Structure stereochemistry and named/versioned computed classification have distinct evidence scopes. |
| bgc-2502-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines165–173 | supports | The maintained stereo_complete calculation uses unassigned molecular chiral centers; it is not a count of literal question marks in InChI. Atom type and double-bond geometry require separate interpretation. |
| bgc-2502-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines295–306;988–1022 | supports | Zero or multiple classifier pathways file as UNCLASSIFIED while exact model arrays remain retained; filing is distinct from scientific applicability. |
| bgc-2502-bioactivity-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines126–145;1318–1382 | supports | Deposited calls, endpoints and values retain their source scope. Activity classes derived from active assay titles do not independently prove mechanisms or direct binding. |
| bgc-2502-source-reading | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-current251-assigned-source-reading-001.json; /partition; /contexts; /reading; /cautions; /attribution | supports | BGC wholly read first-five selected contexts0–4 and unselected Pseurotin10:54 frames/22 rows/272 fields, including16 selected rows/201 fields and6 companion rows/71 fields. Companion rows add no review coverage or transferred activity. |
| bgc-2502-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete source reading covers99 frames/36 rows/456 fields: BGC22 and Support14 rows. Native taxonomy/curation has zero positive-source-row credit. |
| bgc-2502-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch251/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /terminal_chunk; /original_exit_code; /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope | supports | One original composer produced the accepted plan at393 placements/51 paths, with exact source notes and attributed reading receipts. This fragment consumes saved results only. |
| bgc-2502-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch251/root-target-input-plan-acceptance-001.json; /status; /accepted; /plan; /execution; /source_placements; /unique_source_paths; /original_source_inventory_counts; /per_order_counts; /verification; /reading | supports | ROOT accepted the exact393-placement/51-path source plan and original results; no query or input expansion is inferred. |
| bgc-2502-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch251/root-current251-native-gates-acceptance-001.json; /status; /verification; /all_native_gates_passed; /unavailable_required_gates; /scope | supports | Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed remains false. Technical checks do not complete scientific verification. |
| bgc-2502-curation-scope | /private/tmp/npm-review-work/shared-next-batch251-tentative/native-prep/native-current251-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | Bounded ignored-inclusive Native applicability review found no matching correction/exclusion; sixteen unrelated Streptomyces-token hits do not establish a record correction. Three actual assay tuples belong only to Pseurotin; Azinomycin contributes a blank-AID sentinel. |
| bgc-2502-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/8 | supports | Complete saved cache names and synonyms for this owner’s source IDs; no independent taxonomic rank, strain, occurrence or producer validation. |
| bgc-2502-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/source_taxa; /contexts/1/source_scope_inventory/forward_taxon_merge_matches; /contexts/1/source_scope_inventory/nonorganism_matches | supports | Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh taxonomy request. |
| bgc-2502-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch251-tentative/native-prep/native-current251-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /routes; /interpretation | supports | Native read all ten whole retained stanzas and eleven routes; no unmatched IDs or forward merges. Names and synonyms do not establish missing strain or biological evidence. |
| bgc-2502-direct-contexts | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-target-input-plan-001.json; /records/1/proposed_companion_paths; /records/1/direct_companion_predicates | supports | Exact immediate owned-BGC context inputs; shared locus/citation is not identity, stereochemistry, assay or mechanism transfer. No transitive or name-based expansion. |
| bgc-2502-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key; /contexts/10/complete_raw_text; /contexts/10/complete_raw_history; /contexts/10/source_scope_inventory | supports | Complete directly linked companion encodings, histories and saved source frames. Pseurotin is unselected context only; Bananamide peers remain distinct full-key/formula records. No activity, stereochemistry, evidence-grade or coverage transfer. |
| bgc-2502-companion-reading | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-pseurotin-whole-reading-001.json; /observer; /recorded_at; /status; /scope; /owner; /literal_counts; /direct_context; /whole_reading; /bounded_cautions; /bounded_union; /actual251_roles; /final250_checkpoint; /external_requests; /active_queued_retrying_scheduled_outbound_work; /target_invocations; /YAML_molecular_project_imports; /source_table_queries; /source_branch_campaign_mutations | supports | BGC complete Pseurotin plaintext/history reading preserves its distinct structure and three source-specific assays; none is an Azaspirene result. |
| bgc-2502-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2502-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line1; physical lines 1183–1183; row_sha256 012fbf4e1d35fb982935a3b8e79d4b24dd58bfebbbc8caa11fd1d91f0a9995b5 | supports | Exact retained compound/version, structure/key, xrefs, producer/locus grades and citation tiers. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2502-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2502-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2502-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line1; physical lines 7287–7287; row_sha256 89dd3a9486b8bf4c1f0836cfad9dc8bc65b4d79e32763d68b2ff825d01eb880e | supports | Exact organism/reference occurrence assertions; detection and repeated citations do not establish production or independent experiments. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2502-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2502-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 row placements, exact predicate/query and all fields. |
| bgc-2502-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line1; physical lines 2007–2007; row_sha256 931241e00de2385aad5a2498fd09f36823bef2b6ca71ac311fb4ee9f12eb86dc | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability remains separate. BGC whole saved-source reading and current physical bytes are joined. |
| bgc-2502-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2502-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2502-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame: 0 row placements, exact predicate/query and all fields. |
| bgc-2502-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json; /contexts/1/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame: 0 row placements, exact predicate/query and all fields. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-251/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-251/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-251/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-251/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-251/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Only retained local evidence and the accepted original offline results were assessed. Fresh primary literature, current external authority/taxonomy, assay protocols and independent natural identity remain unavailable under the no-request hold.
- All five first-half stored-form pairs have different canonical isomeric and nonisomeric SMILES and empty direct atom maps. Normalized identifiers and counts alone are not full graph identity proof. Fourteen diagnostic warnings are global and are not assigned to individual records.
- Five local gate commands passed; full QC and OAK remain unavailable. Review completion remains partial and native SEEDED status/history are unchanged.
- The whole raw/captured/expected/resolved owner, complete graph/history, 42-input canonical intake, nine selected source frames and nine Pseurotin context frames, and both full molecular forms were read. The maintained reader supplies preservation/topology evidence, not independent primary, sequence, producer or natural-identity validation. Open PsoG/construct/intermediate questions and current external verification remain unresolved, so completion is partial and SEEDED status is retained.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all first-five saved molecular forms and 194 actual intake placements/47 paths, without new parsing.
- Disjoint source reading: BGC first-five selected plus Pseurotin 54 frames/22 rows/272 fields; Support last-five 45 frames/14 rows/184 fields. Native cache/curation receives zero positive-source-row credit.
- BGC operated original collector/composer; Support operated canonical intakes; Native operated diagnostic and sole Azaspirene reader under ROOT delegation. These fragments consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T035335Z-azaspirene
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: azaspirene'
started_at: '2026-11-05T02:59:53.426433Z'
finished_at: '2026-11-05T03:53:35.118309Z'
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
summary: Azaspirene retains the exact source structure and a preserved, explicitly
  partial Af293 reconstitution graph. A one-site lactam/lactim representation difference
  is bounded; PsoG accession and full constructs remain unresolved. Shared-BGC Pseurotin
  assays are context only. This review remains partial without new sequence, primary
  or assay claims.
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
  - path: data/natural_products/unclassified/azaspirene.yaml
    sha256: c68f3940c77cf076fd528e73e6abed34ea93189210c8fabff64aa53ddc64349a
    role: target
  - path: data/natural_products/unclassified/pseurotin.yaml
    sha256: 87b2dd21fa891a5c991fc60d3462edd13ec52cd0223d610289a679dbf2ef1456
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
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
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
  selection: Campaign path order 2502; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-a469ae857b
targets:
- target_id: naturalproductmech:mibig-a469ae857b
  path: data/natural_products/unclassified/azaspirene.yaml
  label: azaspirene
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
    path: curation/pubchem_bioassay_exclusions.tsv
    role: Exact assay identity exclusion decisions for selected/direct source context.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained source-row identity/digest guard; text-only dependency.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/azaspirene.yaml
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
  name: Complete offline maintained reader for azaspirene
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch251/read-selected-mechanism-guarded-001.py
    2502 bdd5f095e686087bb61d45f47b787c8b13f9dab13ce4d7a92117b47644008c16 dc19158b80abcca1707f4aea86e8cf6de57d935c04f39d482982de81bd68145c
    77aa1e1d5d0826e0c069ce645a3b334cf37ba553a464930915c3aa68bacf170c 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
    302ee4eb8e4426a9fe10249cfaf6374cbf03b7c3b3c881c024cd2cda05e57ef0
  exit_code: 0
  expected_exit_code: 0
  status: passed
  required: true
  summary: 'One original offline maintained call preserved the complete Azaspirene
    owner: one graph, eight nodes, eight edges and three histories, with no pathway
    or components. This does not independently validate historical scientific or protein
    assertions.'
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-reader-result
  - bgc-2502-reader-execution
  - bgc-2502-reader-acceptance
  scope_note: Complete owner preservation and maintained topology check. Known capability
    probe denied before action; no additional molecular parse or reader call.
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  command: just validate-strict data/natural_products/unclassified/aurantimycin-a.yaml
    data/natural_products/unclassified/azaspirene.yaml data/natural_products/unclassified/azinomycin-b.yaml
    data/natural_products/unclassified/bananamide-1.yaml data/natural_products/unclassified/bananamide-2.yaml
    data/natural_products/unclassified/bananamide-3.yaml data/natural_products/unclassified/bananamide-d.yaml
    data/natural_products/unclassified/bananamide-e.yaml data/natural_products/unclassified/bananamide-f.yaml
    data/natural_products/unclassified/bananamide-g.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-251/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-a469ae857b
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-251/validate-all-001.tsv
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
  - naturalproductmech:mibig-a469ae857b
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
  - naturalproductmech:mibig-a469ae857b
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
  - naturalproductmech:mibig-a469ae857b
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-251/review-queue-001.tsv
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
  - naturalproductmech:mibig-a469ae857b
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2502-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/azaspirene.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Complete azaspirene owner and 3 history events; earlier whole reading carries
    by current identical bytes.
  snapshot_sha256: c68f3940c77cf076fd528e73e6abed34ea93189210c8fabff64aa53ddc64349a
- evidence_id: bgc-2502-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Complete actual owner capture and metadata; preservation is not independent
    scientific validation.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/intakes/2502-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Actual canonical target, maintained ownership and all 42 input placements
    joined to the accepted plan and current hashes.
  snapshot_sha256: dc19158b80abcca1707f4aea86e8cf6de57d935c04f39d482982de81bd68145c
- evidence_id: bgc-2502-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /records/1
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: ROOT accepted this original canonical intake and its exact plan, inspection
    and receipt pins.
  snapshot_sha256: f8d44265377e6f34e956f611649fa9f82e8d53ba0a8114e8bcd7aa30c2b4d084
- evidence_id: bgc-2502-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/label;
    /records/1/owner_document/chemical_structure; /records/1/owner_document/xrefs;
    /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status;
    /records/1/owner_document/grounding_notes; /records/1/owner_document/discussions
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact retained identifier, structure, cross-references where present, source
    concepts and grounding fields. Historical annotations do not constitute a fresh
    authority lookup.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/producer_taxon_groups;
    /records/1/owner_document/biosynthetic_gene_clusters; /records/1/owner_document/source_concepts
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact separate producer/locus grades, methods, accessions, coordinates
    where declared and citation tiers.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Complete owner supplies the retained occurrences and bounded absence of
    selected bioactivity and molecular-target roots. Absence is not biological inactivity.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing and separate
    source categories; applicability is assessed separately.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1/owner_document/curation_status; /records/1/owner_document/curation_history
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Complete history and status; seeding and historical curation do not imply
    new primary verification.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-mechanism-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/owner-capture-DATA-001.json
  locator: /records/1/owner_document
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: The accepted maintained reader preserves one BIOSYNTHESIS graph with eight
    nodes, eight edges, twelve edge-reference placements and three history events;
    no ordered pathway or external component is declared. Four encoded-membership
    edges belong to the successful four-gene yeast BJ5464-NpgA reconstruction; detected
    product matching does not demonstrate isolated-enzyme sufficiency, a physical
    complex or native essentiality. PsoA priming and propionyl-CoA preference are
    scoped to historical in-vitro/competition evidence, not exclusive substrate use
    or complete in-vitro synthesis. PsoG omission changed peaks 7/8 whose structures
    were not determined; it does not establish a purified hydroxylation reaction.
    The graph explicitly excludes Pseurotin transfer and direct PsoB catalytic assignment.
    PsoA Q4WAZ9/4007 aa, PsoB Q4WAZ8/445 aa and PsoF Q4WAZ0/905 aa remain historical
    Af293 reference associations, distinct from the complete tagged experimental inserts.
    The N-FLAG/C-His6 PsoA, bacterial N-His6 proteins and separate yeast vector contexts
    are preserved. PsoG remains accession-unresolved; the neighboring AFUA_8G00430/Q4WAY9/EAL85123.1
    157-aa protein is explicitly excluded. Historical primer matching to nucleotide
    coordinates is not a validated splice model or exact assayed protein sequence.
    Earlier sequence/CDS/UniProt claims were not repeated here. The graph’s propionyl-starter
    preference versus database acetyl-starter statement remains an attributed conflict
    with its stated evidence priority.
  snapshot_sha256: 5c5156d45104fe87d48c6b658a92a645ba4712c082ba6113ac8e07e6552b59a9
- evidence_id: bgc-2502-reader-result
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/native-current251-azaspirene-maintained-reader-DATA-001.json
  locator: /status; /reader_call_count; /review_check_metadata; /raw_owner; /expected_view;
    /resolved_view; /counts; /returned_view_equals_expected_complete_owner; /view_mismatches;
    /errors; /denials; /unexpected_denials; /external_requests; /molecular_parses;
    /retries; /limitations
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'One accepted maintained call preserved complete Azaspirene raw/captured/expected/resolved
    equality: one graph, eight nodes, eight edges, three histories and no components/pathway/targets.
    Historical science and protein limits remain attributed; the known capability
    probe was denied before action.'
  snapshot_sha256: cf30d9557db73865ab3eeda7bbcd33a57a1c8ac4c8d96d6ca60f5baaef163825
- evidence_id: bgc-2502-reader-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/root-native-reader-2502-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /order; /DATA; /execution;
    /original_tools; /process; /native_readback; /verification; /review_check_contract;
    /ROOT_result_reading; /network_boundary; /environment_boundary; /science_boundary;
    /external_requests
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: ROOT accepted the exact original zero-exit reader and complete owner equality,
    with its review-check contract and scientific/network boundaries.
  snapshot_sha256: 45be3c3ff103ba81fa6217f94286f4680b1df3156130d6859297602b181e7450
- evidence_id: bgc-2502-reader-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/native-current251-azaspirene-reader-execution-001.json
  locator: /command; /cwd; /started_at; /finished_at; /exit_code; /stdout; /stderr;
    /DATA; /operator; /delegated_by
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact Native-operated command, zero exit, clocks and DATA/stream pins under
    ROOT delegation.
  snapshot_sha256: f9538291e6b18803391d812638fb4142245f8c7716fc9896ebe304e0b8021c20
- evidence_id: bgc-2502-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Eight of ten saved-form comparisons are true: formula, charge, Standard
    InChI, full key, atom/bond counts and declared-key checks agree. Canonical isomeric
    and nonisomeric SMILES differ, and the saved direct atom map is empty with full_graph_identity_established=false.
    The particular bond/hydrogen changes below support a bounded tautomer interpretation;
    they do not establish an independent complete graph correspondence, a preferred
    natural tautomer or experimental identity.'
  snapshot_sha256: a58820e2b3b1509e707954a1c157394f10a694304860cd0874508747ee537090
- evidence_id: bgc-2502-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/declared_structure; /records/1/literal_InChI_layers; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/smiles/computed/atoms; /records/1/smiles/computed/bonds;
    /records/1/smiles/computed/rings; /records/1/smiles/computed/potential_stereo;
    /records/1/smiles/computed/motifs; /records/1/smiles/computed/fragment_atom_indices;
    /records/1/inchi/computed/atoms; /records/1/inchi/computed/bonds; /records/1/inchi/computed/rings;
    /records/1/inchi/computed/potential_stereo; /records/1/inchi/computed/motifs;
    /records/1/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Each form contains 27 atoms and 29 bonds at charge 0, with two five-member
    rings sharing the spiro carbon and a six-member aromatic ring. SMILES N24-C25(=O26)
    in the N-containing ring is represented as InChI C18(OH24)=N21, while the other
    ketone persists. The O-containing five-member ring is unsaturated; there is no
    saturated C5O motif or ester linkage. Three tetrahedral sites and two E-configured
    chain double bonds are specified in both forms. The spiro carbon CIP label changes
    from S at SMILES atom 11 to R at InChI atom 20 as the lactam environment changes;
    this is not an independently demonstrated stereochemical inversion.
  snapshot_sha256: a58820e2b3b1509e707954a1c157394f10a694304860cd0874508747ee537090
- evidence_id: bgc-2502-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-current251-first-five-molecular-intake-reading-001.json
  locator: /records/1; /totals; /whole_reading; /raw_and_source_carry; /limits
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: BGC complete saved first-five molecular and intake reading, with exact
    per-form table counts and reading attribution; no new parse.
  snapshot_sha256: b91e60fafde925b602b23168899cccaa508b2122963db9817c340dfd76971842
- evidence_id: bgc-2502-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /observer; /recorded_at; /status; /accepted; /DATA; /execution; /original_tools;
    /readback; /original_exit_code; /original_terminal_chunk; /molecular_parse_attempts;
    /parsed; /comparisons_true; /comparisons_total; /global_warning_count; /external_requests;
    /method_scope; /interpretation_boundary; /ROOT_result_reading; /verification;
    /scientific_verdicts
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostics. Global warning
    interpretation and method limits remain explicit; no per-record warning assignment
    is inferred.
  snapshot_sha256: 44804c4922a8371a9433a0b0f567b4bee11ae37cf44a7766e240160b6f50b8ee
- evidence_id: bgc-2502-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and source/stream pins.
  snapshot_sha256: ee56a168ed367f2bd4133deb9ae43a867c68ac72edce6d2d757bfd2c904c2319
- evidence_id: bgc-2502-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–433
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Structure stereochemistry and named/versioned computed classification have
    distinct evidence scopes.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2502-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines165–173
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: The maintained stereo_complete calculation uses unassigned molecular chiral
    centers; it is not a count of literal question marks in InChI. Atom type and double-bond
    geometry require separate interpretation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2502-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines295–306;988–1022
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Zero or multiple classifier pathways file as UNCLASSIFIED while exact model
    arrays remain retained; filing is distinct from scientific applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2502-bioactivity-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines126–145;1318–1382
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Deposited calls, endpoints and values retain their source scope. Activity
    classes derived from active assay titles do not independently prove mechanisms
    or direct binding.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2502-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-current251-assigned-source-reading-001.json
  locator: /partition; /contexts; /reading; /cautions; /attribution
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: BGC wholly read first-five selected contexts0–4 and unselected Pseurotin10:54
    frames/22 rows/272 fields, including16 selected rows/201 fields and6 companion
    rows/71 fields. Companion rows add no review coverage or transferred activity.
  snapshot_sha256: 01b88b133c3d400102e43ecb6a6c6deb91f4e1f3f5eaa93616082193be69c00b
- evidence_id: bgc-2502-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Disjoint complete source reading covers99 frames/36 rows/456 fields: BGC22
    and Support14 rows. Native taxonomy/curation has zero positive-source-row credit.'
  snapshot_sha256: 9600a96028d38ef3d431914089b691eca0df186f436a7bde85a0dc8038a13558
- evidence_id: bgc-2502-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /terminal_chunk; /original_exit_code;
    /plan; /derivation; /inventory; /source_notes; /verification; /source_reading_scope
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: One original composer produced the accepted plan at393 placements/51 paths,
    with exact source notes and attributed reading receipts. This fragment consumes
    saved results only.
  snapshot_sha256: 8b11825cedd73b30b107703adee82e7cab1b069f3f4725f936e96b16353d276c
- evidence_id: bgc-2502-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/root-target-input-plan-acceptance-001.json
  locator: /status; /accepted; /plan; /execution; /source_placements; /unique_source_paths;
    /original_source_inventory_counts; /per_order_counts; /verification; /reading
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: ROOT accepted the exact393-placement/51-path source plan and original results;
    no query or input expansion is inferred.
  snapshot_sha256: ccf6d6a834717b27d9d8dd1073428de035287822a3bd2c2697b69bd91121eacd
- evidence_id: bgc-2502-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251/root-current251-native-gates-acceptance-001.json
  locator: /status; /verification; /all_native_gates_passed; /unavailable_required_gates;
    /scope
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Five local commands passed; full QC and OAK remain unavailable and all_native_gates_passed
    remains false. Technical checks do not complete scientific verification.
  snapshot_sha256: 84a181e1ab9e40bab1f3659965b0fd82fd986b2046d2af9ecb1370ca1e2482fe
- evidence_id: bgc-2502-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/native-prep/native-current251-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Bounded ignored-inclusive Native applicability review found no matching
    correction/exclusion; sixteen unrelated Streptomyces-token hits do not establish
    a record correction. Three actual assay tuples belong only to Pseurotin; Azinomycin
    contributes a blank-AID sentinel.
  snapshot_sha256: bb7018a0be58f6bbb30dbb1aaae81c148f745e637d9c9b7b27a21ba8f68e348e
  search_scope: Eleven current contexts and96 literal tokens across eleven enumerated
    curation TSVs including ignored files; nine eligible tables/3422 rows, with exact
    retained owner/source/BGC/full-key/assay/occurrence predicates. This is not global
    absence or protocol validation.
- evidence_id: bgc-2502-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/4; /cached_taxonomy/whole_stanzas/8
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Complete saved cache names and synonyms for this owner’s source IDs; no
    independent taxonomic rank, strain, occurrence or producer validation.
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
- evidence_id: bgc-2502-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/source_taxa; /contexts/1/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/1/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact source taxon IDs and retained forwarding/nonorganism routes; no fresh
    taxonomy request.
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
- evidence_id: bgc-2502-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/native-prep/native-current251-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /routes; /interpretation
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Native read all ten whole retained stanzas and eleven routes; no unmatched
    IDs or forward merges. Names and synonyms do not establish missing strain or biological
    evidence.
  snapshot_sha256: e490af5ae9104119761ad15fca091a8127ed945a441575641898d09f511ef001
- evidence_id: bgc-2502-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-target-input-plan-001.json
  locator: /records/1/proposed_companion_paths; /records/1/direct_companion_predicates
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact immediate owned-BGC context inputs; shared locus/citation is not
    identity, stereochemistry, assay or mechanism transfer. No transitive or name-based
    expansion.
  snapshot_sha256: 8a02d6639775a3484e740e22b79e1529702a9652cbc6c5e831a407ca0fe8d46d
- evidence_id: bgc-2502-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key;
    /contexts/10/complete_raw_text; /contexts/10/complete_raw_history; /contexts/10/source_scope_inventory
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Complete directly linked companion encodings, histories and saved source
    frames. Pseurotin is unselected context only; Bananamide peers remain distinct
    full-key/formula records. No activity, stereochemistry, evidence-grade or coverage
    transfer.
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
- evidence_id: bgc-2502-companion-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-pseurotin-whole-reading-001.json
  locator: /observer; /recorded_at; /status; /scope; /owner; /literal_counts; /direct_context;
    /whole_reading; /bounded_cautions; /bounded_union; /actual251_roles; /final250_checkpoint;
    /external_requests; /active_queued_retrying_scheduled_outbound_work; /target_invocations;
    /YAML_molecular_project_imports; /source_table_queries; /source_branch_campaign_mutations
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: BGC complete Pseurotin plaintext/history reading preserves its distinct
    structure and three source-specific assays; none is an Azaspirene result.
  snapshot_sha256: 520782068fea68ff2a2a3291ef45b4bcc1e4cf42063cb3b1888b42ef4f3366eb
- evidence_id: bgc-2502-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local mibig_compounds frame; exact predicate exact complete
    standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line1; physical lines 1183–1183; row_sha256 012fbf4e1d35fb982935a3b8e79d4b24dd58bfebbbc8caa11fd1d91f0a9995b5
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact retained compound/version, structure/key, xrefs, producer/locus grades
    and citation tiers. BGC whole saved-source reading and current physical bytes
    are joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2502-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved chebi_structures frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local chebi_structures frame; exact predicate exact complete
    standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local lotus_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line1; physical lines 7287–7287; row_sha256 89dd3a9486b8bf4c1f0836cfad9dc8bc65b4d79e32763d68b2ff825d01eb880e
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact organism/reference occurrence assertions; detection and repeated
    citations do not establish production or independent experiments. BGC whole saved-source
    reading and current physical bytes are joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2502-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved cyanometdb_occurrences frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local cyanometdb_occurrences frame; exact predicate exact complete
    standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local npclassifier frame; exact predicate exact complete standard_inchi_key
    equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: bgc-2502-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line1; physical lines 2007–2007; row_sha256 931241e00de2385aad5a2498fd09f36823bef2b6ca71ac311fb4ee9f12eb86dc
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    remains separate. BGC whole saved-source reading and current physical bytes are
    joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2502-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local pubchem_bioassay frame; exact predicate exact complete
    standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved bindingdb_targets frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local bindingdb_targets frame; exact predicate exact complete
    standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete matched
    payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 row placements, exact
    predicate/query and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local antibioticmech_inchikeys frame; exact predicate exact
    complete standard_inchi_key equality; query "QLKGRMRPKQNCRR-XXPFWKOGSA-N". Complete
    matched payloads or explicit empty frame, without query replay.
- evidence_id: bgc-2502-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch251-tentative/bgc-prep/bgc-conditional251-source-inventory-DATA-001.json
  locator: /contexts/1/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T03:44:54.458256Z'
  support: supports
  summary: 'Complete saved chebi_origins frame: 0 row placements, exact predicate/query
    and all fields.'
  snapshot_sha256: 4087faa65c4a64afae960b1e39156e31ba66fda0057c2cd22f4ed6761ce5ca93
  search_scope: Saved local chebi_origins frame; exact predicate exact chebi_id from
    exact full-key structure rows; query []. Complete matched payloads or explicit
    empty frame, without query replay.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-251/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json
  accessed_at: '2026-11-05T03:07:39.704448Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 1fc6dc2137395f9ab9f0a57bccaf51646a259ecaeb62f2748c8c79fa67974d75
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-251/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json
  accessed_at: '2026-11-05T03:08:05.678076Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: f4361ec5360bd859b2b6e2f3bbbfa92be18e002cde118d2c31e5f4329a4edc08
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-251/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json
  accessed_at: '2026-11-05T03:08:25.879227Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-251/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json
  accessed_at: '2026-11-05T03:09:00.941119Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-251/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-251/native-current251-five-gates-execution-001.json
  accessed_at: '2026-11-05T03:09:13.133239Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f316f40d4b75824a11091c1c78dc45636ee1654b5640d1d7420933acebe18edc
assessments:
- assessment_id: bgc-2502-identity
  area: identity
  topic: Retained encoding and bounded identity correspondence
  outcome: supported
  summary: The minted naturalproductmech:mibig-a469ae857b owner retains QLKGRMRPKQNCRR-XXPFWKOGSA-N,
    C21H23NO5 and NPA06799 from MIBiG BGC0001037 version 5. Both forms regenerate
    the declared key/Standard InChI but canonical strings differ at the ring lactam/lactim
    site. The exact local ChEBI full-key frame is empty. Pseurotin SLYDIPAXCVVRNY-BBJHAQHQSA-N
    is a distinct C22H25NO8 encoding with incomplete stereochemistry; the shared BGC
    does not establish equivalence or transfer xrefs, absolute configuration or activity.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-grounding-owner
  - bgc-2502-chemistry
  - bgc-2502-source-mibig_compounds
  - bgc-2502-query-chebi_structures
  - bgc-2502-direct-contexts
  - bgc-2502-companion-boundaries
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-result
  - bgc-2502-reader-acceptance
  dimensions:
  - name: standard_inchi_key
    value: QLKGRMRPKQNCRR-XXPFWKOGSA-N; retained key, not independent natural-identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2502-grounding-owner
    - bgc-2502-chemistry
    - bgc-2502-source-mibig_compounds
    - bgc-2502-query-chebi_structures
    - bgc-2502-direct-contexts
    - bgc-2502-companion-boundaries
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
  - name: grounding_scope
    value: The minted naturalproductmech:mibig-a469ae857b owner retains QLKGRMRPKQNCRR-XXPFWKOGSA-N,
      C21H23NO5 and NPA06799 from MIBiG BGC0001037 version 5. Both forms regenerate
      the declared key/Standard InChI but canonical strings differ at the ring lactam/lactim
      site. The exact local ChEBI full-key frame is empty. Pseurotin SLYDIPAXCVVRNY-BBJHAQHQSA-N
      is a distinct C22H25NO8 encoding with incomplete stereochemistry; the shared
      BGC does not establish equivalence or transfer xrefs, absolute configuration
      or activity.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2502-grounding-owner
    - bgc-2502-chemistry
    - bgc-2502-source-mibig_compounds
    - bgc-2502-query-chebi_structures
    - bgc-2502-direct-contexts
    - bgc-2502-companion-boundaries
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
- assessment_id: bgc-2502-representation
  area: representation
  topic: Stored-form topology and stereochemical scope
  outcome: supported
  summary: The single lactam/lactim bond-and-hydrogen shift is directly visible in
    the complete saved tables. Both forms retain three specified tetrahedral centers
    and two specified E double bonds, consistent with the scoped stereo_complete=true
    flag. Empty direct atom correspondence and false canonical comparisons remain
    explicit. Historical Figure1/structure agreement in the discussion is retained
    attribution, not a new absolute-configuration experiment.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-grounding-owner
  - bgc-2502-chemistry
  - bgc-2502-topology
  - bgc-2502-diagnostic-reading
  - bgc-2502-diagnostic-acceptance
  - bgc-2502-structure-schema
  - bgc-2502-stereo-method
  - bgc-2502-companion-boundaries
  dimensions:
  - name: stereochemistry_scope
    value: The single lactam/lactim bond-and-hydrogen shift is directly visible in
      the complete saved tables. Both forms retain three specified tetrahedral centers
      and two specified E double bonds, consistent with the scoped stereo_complete=true
      flag. Empty direct atom correspondence and false canonical comparisons remain
      explicit. Historical Figure1/structure agreement in the discussion is retained
      attribution, not a new absolute-configuration experiment.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2502-grounding-owner
    - bgc-2502-chemistry
    - bgc-2502-topology
    - bgc-2502-diagnostic-reading
    - bgc-2502-diagnostic-acceptance
    - bgc-2502-structure-schema
    - bgc-2502-stereo-method
    - bgc-2502-companion-boundaries
  - name: representation_correspondence
    value: 'Eight of ten saved-form comparisons are true: formula, charge, Standard
      InChI, full key, atom/bond counts and declared-key checks agree. Canonical isomeric
      and nonisomeric SMILES differ, and the saved direct atom map is empty with full_graph_identity_established=false.
      The particular bond/hydrogen changes below support a bounded tautomer interpretation;
      they do not establish an independent complete graph correspondence, a preferred
      natural tautomer or experimental identity.'
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2502-grounding-owner
    - bgc-2502-chemistry
    - bgc-2502-topology
    - bgc-2502-diagnostic-reading
    - bgc-2502-diagnostic-acceptance
    - bgc-2502-structure-schema
    - bgc-2502-stereo-method
    - bgc-2502-companion-boundaries
- assessment_id: bgc-2502-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: MIBiG BGC0001037 version 5 retains Af293 taxon 330879 as BGC_CHARACTERIZED
    producer and CM000176.1:115218–134016 as CLUSTER_DEMONSTRATED locus, with knockout,
    enzymatic-assay and heterologous-expression method labels. These database grades
    remain separate from the precise historical graph claims. The Neosartorya 36629
    LOTUS occurrence is genus-labelled and does not identify Af293 or add a strain-specific
    production experiment. The exact Pseurotin companion shares the locus and grades
    but cannot strengthen Azaspirene-specific identity, substrate specificity or activity.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-origin-owner
  - bgc-2502-occurrence-owner
  - bgc-2502-source-mibig_compounds
  - bgc-2502-cached-taxonomy
  - bgc-2502-taxonomy-routes
  - bgc-2502-curation-scope
  - bgc-2502-direct-contexts
  - bgc-2502-source-lotus_occurrences
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-result
  - bgc-2502-reader-acceptance
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0001037 version 5 retains Af293 taxon 330879 as BGC_CHARACTERIZED
      producer and CM000176.1:115218–134016 as CLUSTER_DEMONSTRATED locus, with knockout,
      enzymatic-assay and heterologous-expression method labels. These database grades
      remain separate from the precise historical graph claims. The Neosartorya 36629
      LOTUS occurrence is genus-labelled and does not identify Af293 or add a strain-specific
      production experiment. The exact Pseurotin companion shares the locus and grades
      but cannot strengthen Azaspirene-specific identity, substrate specificity or
      activity.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2502-origin-owner
    - bgc-2502-occurrence-owner
    - bgc-2502-source-mibig_compounds
    - bgc-2502-cached-taxonomy
    - bgc-2502-taxonomy-routes
    - bgc-2502-curation-scope
    - bgc-2502-direct-contexts
    - bgc-2502-source-lotus_occurrences
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
  - name: producer_evidence
    value: MIBiG BGC0001037 version 5 retains Af293 taxon 330879 as BGC_CHARACTERIZED
      producer and CM000176.1:115218–134016 as CLUSTER_DEMONSTRATED locus, with knockout,
      enzymatic-assay and heterologous-expression method labels. These database grades
      remain separate from the precise historical graph claims. The Neosartorya 36629
      LOTUS occurrence is genus-labelled and does not identify Af293 or add a strain-specific
      production experiment. The exact Pseurotin companion shares the locus and grades
      but cannot strengthen Azaspirene-specific identity, substrate specificity or
      activity.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2502-origin-owner
    - bgc-2502-occurrence-owner
    - bgc-2502-source-mibig_compounds
    - bgc-2502-cached-taxonomy
    - bgc-2502-taxonomy-routes
    - bgc-2502-curation-scope
    - bgc-2502-direct-contexts
    - bgc-2502-source-lotus_occurrences
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
  - name: locus_evidence
    value: MIBiG BGC0001037 version 5 retains Af293 taxon 330879 as BGC_CHARACTERIZED
      producer and CM000176.1:115218–134016 as CLUSTER_DEMONSTRATED locus, with knockout,
      enzymatic-assay and heterologous-expression method labels. These database grades
      remain separate from the precise historical graph claims. The Neosartorya 36629
      LOTUS occurrence is genus-labelled and does not identify Af293 or add a strain-specific
      production experiment. The exact Pseurotin companion shares the locus and grades
      but cannot strengthen Azaspirene-specific identity, substrate specificity or
      activity.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2502-origin-owner
    - bgc-2502-occurrence-owner
    - bgc-2502-source-mibig_compounds
    - bgc-2502-cached-taxonomy
    - bgc-2502-taxonomy-routes
    - bgc-2502-curation-scope
    - bgc-2502-direct-contexts
    - bgc-2502-source-lotus_occurrences
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
- assessment_id: bgc-2502-citations
  area: evidence
  topic: Citation tiers and complete history scope
  outcome: supported
  summary: MIBiG PMID:25494235 is ENTRY attribution; LOTUS DOI:10.1021/OL020104+ is
    a separate occurrence assertion. The graph has twelve edge-reference placements,
    including eight placements of DOI:10.1021/ol503179v and four historical curator-inference
    references for three proteins and the PsoG nucleotide context. Repeated placements
    are not independent experiments. The three-event history includes two seedings
    and the 2026-10-12 curator graph event. The old uninspected supercluster paper
    failure remains historical; it was not retried or used to add methods claims.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-owner
  - bgc-2502-history-owner
  - bgc-2502-origin-owner
  - bgc-2502-occurrence-owner
  - bgc-2502-source-mibig_compounds
  - bgc-2502-source-reading
  - bgc-2502-source-lotus_occurrences
  - bgc-2502-companion-boundaries
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-result
  - bgc-2502-reader-acceptance
  dimensions:
  - name: citation_scope
    value: MIBiG PMID:25494235 is ENTRY attribution; LOTUS DOI:10.1021/OL020104+ is
      a separate occurrence assertion. The graph has twelve edge-reference placements,
      including eight placements of DOI:10.1021/ol503179v and four historical curator-inference
      references for three proteins and the PsoG nucleotide context. Repeated placements
      are not independent experiments. The three-event history includes two seedings
      and the 2026-10-12 curator graph event. The old uninspected supercluster paper
      failure remains historical; it was not retried or used to add methods claims.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2502-owner
    - bgc-2502-history-owner
    - bgc-2502-origin-owner
    - bgc-2502-occurrence-owner
    - bgc-2502-source-mibig_compounds
    - bgc-2502-source-reading
    - bgc-2502-source-lotus_occurrences
    - bgc-2502-companion-boundaries
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
- assessment_id: bgc-2502-occurrence
  area: evidence
  topic: Source-specific occurrence and assay boundaries
  outcome: supported
  summary: 'The selected owner retains one Neosartorya occurrence and no bioactivities
    or molecular_targets. Unselected Pseurotin alone has three deposited PubChem rows:
    AID:1845221 and 2202548 are Inconclusive with source Potency 11.6129 and 12.5893
    micromolar, represented as OTHER rather than inferred IC50/EC50; AID:2202377 is
    Active with an ALDH3A1 inhibitor-screen title, no numeric endpoint and no grounded
    target. These rows neither establish anti-cancer/thiol/direct-binding mechanisms
    nor transfer to Azaspirene. Pseurotin’s Pseudeurotium ovale occurrence likewise
    remains its own source assertion.'
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-occurrence-owner
  - bgc-2502-reader-result
  - bgc-2502-query-lotus_occurrences
  - bgc-2502-query-chebi_origins
  - bgc-2502-query-cyanometdb_occurrences
  - bgc-2502-query-pubchem_bioassay
  - bgc-2502-query-bindingdb_targets
  - bgc-2502-query-antibioticmech_inchikeys
  - bgc-2502-cached-taxonomy
  - bgc-2502-taxonomy-routes
  - bgc-2502-taxonomy-reading
  - bgc-2502-curation-scope
  - bgc-2502-bioactivity-seeder
  - bgc-2502-source-reading
  - bgc-2502-source-lotus_occurrences
  - bgc-2502-companion-boundaries
  - bgc-2502-companion-reading
  dimensions:
  - name: occurrence_scope
    value: 'The selected owner retains one Neosartorya occurrence and no bioactivities
      or molecular_targets. Unselected Pseurotin alone has three deposited PubChem
      rows: AID:1845221 and 2202548 are Inconclusive with source Potency 11.6129 and
      12.5893 micromolar, represented as OTHER rather than inferred IC50/EC50; AID:2202377
      is Active with an ALDH3A1 inhibitor-screen title, no numeric endpoint and no
      grounded target. These rows neither establish anti-cancer/thiol/direct-binding
      mechanisms nor transfer to Azaspirene. Pseurotin’s Pseudeurotium ovale occurrence
      likewise remains its own source assertion.'
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2502-occurrence-owner
    - bgc-2502-reader-result
    - bgc-2502-query-lotus_occurrences
    - bgc-2502-query-chebi_origins
    - bgc-2502-query-cyanometdb_occurrences
    - bgc-2502-query-pubchem_bioassay
    - bgc-2502-query-bindingdb_targets
    - bgc-2502-query-antibioticmech_inchikeys
    - bgc-2502-cached-taxonomy
    - bgc-2502-taxonomy-routes
    - bgc-2502-taxonomy-reading
    - bgc-2502-curation-scope
    - bgc-2502-bioactivity-seeder
    - bgc-2502-source-reading
    - bgc-2502-source-lotus_occurrences
    - bgc-2502-companion-boundaries
    - bgc-2502-companion-reading
  - name: assay_target_scope
    value: No retained selected-owner potency or target assertion exists. Pseurotin’s
      three exact source tuples are review context only; title-derived ENZYME_INHIBITOR
      annotation is distinct from experimentally resolved target binding and no companion
      assay changes Azaspirene’s absence of assay roots.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2502-occurrence-owner
    - bgc-2502-reader-result
    - bgc-2502-query-lotus_occurrences
    - bgc-2502-query-chebi_origins
    - bgc-2502-query-cyanometdb_occurrences
    - bgc-2502-query-pubchem_bioassay
    - bgc-2502-query-bindingdb_targets
    - bgc-2502-query-antibioticmech_inchikeys
    - bgc-2502-cached-taxonomy
    - bgc-2502-taxonomy-routes
    - bgc-2502-taxonomy-reading
    - bgc-2502-curation-scope
    - bgc-2502-bioactivity-seeder
    - bgc-2502-source-reading
    - bgc-2502-source-lotus_occurrences
    - bgc-2502-companion-boundaries
    - bgc-2502-companion-reading
- assessment_id: bgc-2502-classification
  area: consistency
  topic: Reported model families and qualified applicability
  outcome: supported
  summary: The versioned model reports Amino acids and Peptides|Polyketides, Cyclic
    polyketides, no class result and is_glycoside=false. The spiro oxygen/nitrogen
    heterocycles are compatible with a cyclic mixed-origin scaffold, while the exact
    biosynthetic interpretation relies on the separately qualified source and graph
    evidence. Empty class results are retained without inventing a named subtype.
    Source NRPS/PKS and model-derived UNCLASSIFIED filing remain distinct axes; structural
    motifs alone do not prove enzyme sequence or natural pathway completion.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-classification-owner
  - bgc-2502-source-npclassifier
  - bgc-2502-chemistry
  - bgc-2502-topology
  - bgc-2502-structure-schema
  - bgc-2502-classification-seeder
  - bgc-2502-source-mibig_compounds
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-result
  - bgc-2502-reader-acceptance
  dimensions:
  - name: classification_applicability
    value: The versioned model reports Amino acids and Peptides|Polyketides, Cyclic
      polyketides, no class result and is_glycoside=false. The spiro oxygen/nitrogen
      heterocycles are compatible with a cyclic mixed-origin scaffold, while the exact
      biosynthetic interpretation relies on the separately qualified source and graph
      evidence. Empty class results are retained without inventing a named subtype.
      Source NRPS/PKS and model-derived UNCLASSIFIED filing remain distinct axes;
      structural motifs alone do not prove enzyme sequence or natural pathway completion.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2502-classification-owner
    - bgc-2502-source-npclassifier
    - bgc-2502-chemistry
    - bgc-2502-topology
    - bgc-2502-structure-schema
    - bgc-2502-classification-seeder
    - bgc-2502-source-mibig_compounds
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-result
    - bgc-2502-reader-acceptance
- assessment_id: bgc-2502-completion
  area: completeness
  topic: Actual evidence coverage and remaining limitations
  outcome: unknown
  summary: The whole raw/captured/expected/resolved owner, complete graph/history,
    42-input canonical intake, nine selected source frames and nine Pseurotin context
    frames, and both full molecular forms were read. The maintained reader supplies
    preservation/topology evidence, not independent primary, sequence, producer or
    natural-identity validation. Open PsoG/construct/intermediate questions and current
    external verification remain unresolved, so completion is partial and SEEDED status
    is retained.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-owner
  - bgc-2502-capture
  - bgc-2502-intake
  - bgc-2502-intake-acceptance
  - bgc-2502-history-owner
  - bgc-2502-diagnostic-reading
  - bgc-2502-diagnostic-acceptance
  - bgc-2502-diagnostic-execution
  - bgc-2502-source-reading
  - bgc-2502-joint-source-notes
  - bgc-2502-source-plan-execution
  - bgc-2502-source-plan-acceptance
  - bgc-2502-native-gate-limits
  - bgc-2502-curation-scope
  - bgc-2502-reader-result
  - bgc-2502-companion-boundaries
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-acceptance
  dimensions:
  - name: review_completion
    value: The whole raw/captured/expected/resolved owner, complete graph/history,
      42-input canonical intake, nine selected source frames and nine Pseurotin context
      frames, and both full molecular forms were read. The maintained reader supplies
      preservation/topology evidence, not independent primary, sequence, producer
      or natural-identity validation. Open PsoG/construct/intermediate questions and
      current external verification remain unresolved, so completion is partial and
      SEEDED status is retained.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2502-owner
    - bgc-2502-capture
    - bgc-2502-intake
    - bgc-2502-intake-acceptance
    - bgc-2502-history-owner
    - bgc-2502-diagnostic-reading
    - bgc-2502-diagnostic-acceptance
    - bgc-2502-diagnostic-execution
    - bgc-2502-source-reading
    - bgc-2502-joint-source-notes
    - bgc-2502-source-plan-execution
    - bgc-2502-source-plan-acceptance
    - bgc-2502-native-gate-limits
    - bgc-2502-curation-scope
    - bgc-2502-reader-result
    - bgc-2502-companion-boundaries
    - bgc-2502-mechanism-owner
    - bgc-2502-reader-acceptance
- assessment_id: bgc-2502-mechanism
  area: consistency
  topic: Preserved reconstitution graph and bounded historical evidence
  outcome: supported
  summary: The accepted maintained reader preserves one BIOSYNTHESIS graph with eight
    nodes, eight edges, twelve edge-reference placements and three history events;
    no ordered pathway or external component is declared. Four encoded-membership
    edges belong to the successful four-gene yeast BJ5464-NpgA reconstruction; detected
    product matching does not demonstrate isolated-enzyme sufficiency, a physical
    complex or native essentiality. PsoA priming and propionyl-CoA preference are
    scoped to historical in-vitro/competition evidence, not exclusive substrate use
    or complete in-vitro synthesis. PsoG omission changed peaks 7/8 whose structures
    were not determined; it does not establish a purified hydroxylation reaction.
    The graph explicitly excludes Pseurotin transfer and direct PsoB catalytic assignment.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-result
  - bgc-2502-reader-acceptance
  - bgc-2502-reader-execution
  - bgc-2502-history-owner
  - bgc-2502-origin-owner
  - bgc-2502-companion-boundaries
  dimensions: []
- assessment_id: bgc-2502-proteins
  area: identity
  topic: Historical enzyme references and unresolved construct limits
  outcome: unknown
  summary: PsoA Q4WAZ9/4007 aa, PsoB Q4WAZ8/445 aa and PsoF Q4WAZ0/905 aa remain historical
    Af293 reference associations, distinct from the complete tagged experimental inserts.
    The N-FLAG/C-His6 PsoA, bacterial N-His6 proteins and separate yeast vector contexts
    are preserved. PsoG remains accession-unresolved; the neighboring AFUA_8G00430/Q4WAY9/EAL85123.1
    157-aa protein is explicitly excluded. Historical primer matching to nucleotide
    coordinates is not a validated splice model or exact assayed protein sequence.
    Earlier sequence/CDS/UniProt claims were not repeated here. The graph’s propionyl-starter
    preference versus database acetyl-starter statement remains an attributed conflict
    with its stated evidence priority.
  target_ids:
  - naturalproductmech:mibig-a469ae857b
  evidence_ids:
  - bgc-2502-mechanism-owner
  - bgc-2502-reader-result
  - bgc-2502-reader-acceptance
  - bgc-2502-reader-execution
  - bgc-2502-history-owner
  - bgc-2502-origin-owner
  - bgc-2502-companion-boundaries
  dimensions: []
findings: []
actions: []
limitations:
- Only retained local evidence and the accepted original offline results were assessed.
  Fresh primary literature, current external authority/taxonomy, assay protocols and
  independent natural identity remain unavailable under the no-request hold.
- All five first-half stored-form pairs have different canonical isomeric and nonisomeric
  SMILES and empty direct atom maps. Normalized identifiers and counts alone are not
  full graph identity proof. Fourteen diagnostic warnings are global and are not assigned
  to individual records.
- Five local gate commands passed; full QC and OAK remain unavailable. Review completion
  remains partial and native SEEDED status/history are unchanged.
- The whole raw/captured/expected/resolved owner, complete graph/history, 42-input
  canonical intake, nine selected source frames and nine Pseurotin context frames,
  and both full molecular forms were read. The maintained reader supplies preservation/topology
  evidence, not independent primary, sequence, producer or natural-identity validation.
  Open PsoG/construct/intermediate questions and current external verification remain
  unresolved, so completion is partial and SEEDED status is retained.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read all first-five saved molecular forms and 194 actual intake placements/47
  paths, without new parsing.
- 'Disjoint source reading: BGC first-five selected plus Pseurotin 54 frames/22 rows/272
  fields; Support last-five 45 frames/14 rows/184 fields. Native cache/curation receives
  zero positive-source-row credit.'
- BGC operated original collector/composer; Support operated canonical intakes; Native
  operated diagnostic and sole Azaspirene reader under ROOT delegation. These fragments
  consume saved results only.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-251
```
