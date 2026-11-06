# Local evidence review: Kutzneride 2

- Review: 20261106T170757Z-kutzneride-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T16:14:29.024610Z
- Finished UTC: 2026-11-06T17:07:57.263428Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Kutzneride 2 retains its third aliphatic chlorine and ten specified atom centres. The maintained KtzQ/R annotations describe precursor chlorination, not the extra aliphatic event or complete congener assembly; source grades and representation limits remain explicit.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2735; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-c7ae5d3088 | data/natural_products/unclassified/kutzneride-2.yaml | generated | Kutzneride 2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-c7ae5d3088 | Both stored forms parsed in the original twenty-attempt diagnostic; formula, charge, normalized InChI and complete key agree. |
| Complete offline maintained reader for kutzneride-2 | passed | True | naturalproductmech:mibig-c7ae5d3088 | One original maintained reader preserved the complete Kutzneride 2 owner, all graph/pathway evidence and history, with zero components. |
| strict_ten | passed | True | naturalproductmech:mibig-c7ae5d3088 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-c7ae5d3088 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-c7ae5d3088 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-c7ae5d3088 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-c7ae5d3088 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-c7ae5d3088 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-c7ae5d3088 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-c7ae5d3088 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

Kutzneride 2 retains exact owner naturalproductmech:mibig-c7ae5d3088, full key GOUIVYIRLLTNCF-JJMZTBTASA-N, C37H48Cl3N7O12 and BGC0000378 compound 2. The third, aliphatic chlorine and tenth specified atom centre distinguish it from 1. NPAtlas NPA015447 and shared precursor annotations do not merge congener identities.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

Each saved form has59 atoms/64 bonds and cycle sizes3,18,6,5,5,6. One ester, COOH and methoxy ether remain. Two chlorines are aromatic and the additional chlorine is aliphatic in the N-N six-ring. This locates the structural distinction without assigning its biosynthetic enzyme. Both forms report ten specified tetrahedral centres, including the chlorinated aliphatic centre, and the InChI form adds three unspecified C=N potentials. Source stereo_complete:true does not certify all reconstructed double-bond geometry or independently verify natural configuration. Three NH amides become terminal C(OH)=N sites while two tertiary amides remain; carbonyl7 to4 and strict amide5 to2. All atom charges remain zero. Matching formula, charge, standard InChI and full key is consistent with mobile-H/tautomer normalization, not net protonation change or exact fixed-form identity: both canonical comparisons are false, the one-way map is empty and full_graph_identity_established is false.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

Kutzneria sp. 744 NCBITaxon:345341 retains SOURCE_ASSERTION producer evidence from MIBiG version5. Genus-level NCBITaxon:43356 occurrences remain separate, and precursor-enzyme evidence does not demonstrate complete production of this congener. BGC0000378 version5 is active/questionable with unknown completeness. EU074211.1 retains CLUSTER_UNSTATED and no source coordinates or methods. Shared KtzQ/R precursor annotations do not prove the complete congener-specific assembly or the extra aliphatic chlorination.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

MIBiG COMPOUND_EVIDENCE DOI:10.1021/np050378g duplicates the LOTUS NP050378G DOI by case, while NP0604331 is an additional occurrence citation. Four histories comprise two seeding and two codex KtzQ/R curation events. Historical primary and sequence references are retained annotations, not newly repeated or fetched verification.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

Two physical LOTUS rows retain Kutzneria genus NCBITaxon:43356 and NP050378G/NP0604331. The shared source DOI is not an independent confirmation, and genus occurrence does not identify strain744 or prove this congener's production. The exact retained source queries contain no actual AID, blank assay sentinel, BindingDB target or AntibioticMech row. The owner has no measured bioactivity or pharmacological-target root. This bounded local absence does not establish inactivity, potency or therapeutic action; biosynthetic enzymes are not pharmacological targets.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

The 18-membered ester-containing macrocycle and amides support Cyclic peptides/Depsipeptides locally. The third chlorine does not identify a tailoring enzyme. Absence of a saturated C5O candidate ring is compatible with glycoside=false at this limited scope; blank source class and NRPS/Type I labels remain source/model assertions rather than complete assembly evidence. Both computed pathways (Amino acids and Peptides and Polyketides) are retained while choose_pathway files the owner UNCLASSIFIED. This is consistent multi-label filing, not missing classification or biological absence.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-c7ae5d3088.

Whole owner/history and all nine saved query frames (4 positive rows/44 fields) were personally read. Native independently read all atom/bond/ring/stereo/motif rows of both saved molecular forms; this author read their complete interpretations and critical topology/stereo summaries. All 53 actual input hashes and ownership declarations were verified, without claiming whole-corpus semantic reading. Five local native commands passed; full QC/OAK, live source authorities and independent primary confirmation remain unavailable. The complete accepted maintained owner view and its graph/pathway/history were personally read; biological claims remain qualified. Generated assertions belong to maintained source inputs, applicable curation tables, extractors and seeder; curated graph/history edits require the maintained writer and attributed curation. No edit is proposed.

### Precursor KtzQ/R chemistry, distinct pathway forms and congener-specific limits

graph: supported. Targets: naturalproductmech:mibig-c7ae5d3088.

The original maintained reader preserves two graphs, six node placements, four edges,20 graph evidence placements, two numbered pathway steps/10 evidence placements and four history events. KtzQ (UniProtKB:A8CF75) and KtzR (A8CF74) are separately attributed precursor halogenation annotations: graph CHEBI:16828 to47356 to140086, with the reduced-flavin partner KtzS outside the Q graph. Numbered pathway steps1/2 retain RHEA:26494/55904 and different substrate/product identifiers CHEBI:57912 to58713 to139336 plus recorded cofactors/products; graph and pathway forms are not silently equated. The raw proposed field is absent, so no proposed flag is invented. PRIMARY_EXPERIMENT DOI:10.1021/ja806467a, MITE0000029/30, UniProt/NCBIProtein and historical sequence notes remain attributed evidence, not newly fetched primary or sequence verification. Curator-inferred shared-BGC placement is not demonstrated complete congener assembly or proof for every chlorine. No KtzA/D graphs are present in this owner. The two aromatic chlorines are compatible with this bounded precursor context, but the additional aliphatic chlorine and complete mature product are not mechanistically assigned by these two reactions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2735-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kutzneride-2.yaml; Complete plaintext and all curation_history entries | supports | The complete current owner/history was personally read; all source assertions and curated annotations remain attributed. |
| bgc-2735-identity | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/chemical_structure; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status | supports | Kutzneride 2 retains exact owner naturalproductmech:mibig-c7ae5d3088, full key GOUIVYIRLLTNCF-JJMZTBTASA-N, C37H48Cl3N7O12 and BGC0000378 compound 2. The third, aliphatic chlorine and tenth specified atom centre distinguish it from 1. NPAtlas NPA015447 and shared precursor annotations do not merge congener identities. |
| bgc-2735-history | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/4/owner_document/curation_history | supports | MIBiG COMPOUND_EVIDENCE DOI:10.1021/np050378g duplicates the LOTUS NP050378G DOI by case, while NP0604331 is an additional occurrence citation. Four histories comprise two seeding and two codex KtzQ/R curation events. Historical primary and sequence references are retained annotations, not newly repeated or fetched verification. |
| bgc-2735-provenance | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters | supports | Kutzneria sp. 744 NCBITaxon:345341 retains SOURCE_ASSERTION producer evidence from MIBiG version5. Genus-level NCBITaxon:43356 occurrences remain separate, and precursor-enzyme evidence does not demonstrate complete production of this congener. BGC0000378 version5 is active/questionable with unknown completeness. EU074211.1 retains CLUSTER_UNSTATED and no source coordinates or methods. Shared KtzQ/R precursor annotations do not prove the complete congener-specific assembly or the extra aliphatic chlorination. |
| bgc-2735-classification | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway; /records/4/owner_document/bgc_class | supports | The 18-membered ester-containing macrocycle and amides support Cyclic peptides/Depsipeptides locally. The third chlorine does not identify a tailoring enzyme. Absence of a saturated C5O candidate ring is compatible with glycoside=false at this limited scope; blank source class and NRPS/Type I labels remain source/model assertions rather than complete assembly evidence. Both computed pathways (Amino acids and Peptides and Polyketides) are retained while choose_pathway files the owner UNCLASSIFIED. This is consistent multi-label filing, not missing classification or biological absence. |
| bgc-2735-roots | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/complete_root_keys; /contexts/9/declared_mechanism_roots_literal; /contexts/9/literal_bioactivities_root | context_only | The whole owner retains the explicitly scoped mechanism/pathway, with no pharmacological target or measured bioactivity root. |
| bgc-2735-chemistry | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons; /records/4/atom_correspondence; /records/4/literal_InChI_layers | supports | Each saved form has59 atoms/64 bonds and cycle sizes3,18,6,5,5,6. One ester, COOH and methoxy ether remain. Two chlorines are aromatic and the additional chlorine is aliphatic in the N-N six-ring. This locates the structural distinction without assigning its biosynthetic enzyme. Both forms report ten specified tetrahedral centres, including the chlorinated aliphatic centre, and the InChI form adds three unspecified C=N potentials. Source stereo_complete:true does not certify all reconstructed double-bond geometry or independently verify natural configuration. Three NH amides become terminal C(OH)=N sites while two tertiary amides remain; carbonyl7 to4 and strict amide5 to2. All atom charges remain zero. Matching formula, charge, standard InChI and full key is consistent with mobile-H/tautomer normalization, not net protonation change or exact fixed-form identity: both canonical comparisons are false, the one-way map is empty and full_graph_identity_established is false. |
| bgc-2735-molecular-reading | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-first-five-molecular-intake-reading-001.json; /records/4; /scope_orders; /original_stderr; /method_limits | supports | Native personally read the complete saved atom/bond/ring/stereo/motif tables. This author read the complete attributed interpretations and critical summaries; no new parse or duplicate primary source-row credit. |
| bgc-2735-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /full_graph_identity_established | supports | ROOT accepted one original twenty-form diagnostic. All fixed-form canonical comparisons remain false and full graph identity is not established. |
| bgc-2735-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Exact original ROOT command and zero exit; this command is evidence, not a replay. |
| bgc-2735-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-original-001.stderr; Complete original stderr; two nonempty warning lines | context_only | Two omitted-undefined-stereo warnings remain globally unassigned. |
| bgc-2735-intake | /private/tmp/npm-review-work/shared-next-batch274/intakes-001/2735-inspect-001.json; /targets; /source/inputs | supports | One exact target, 53 current input hashes and explicit maintained ownership declarations. |
| bgc-2735-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch274/root-intake-acceptance-001.json; /status; /accepted; /input_placements; /unique_input_paths | supports | ROOT accepted ten actual canonical inspections with513 input placements/60 unique paths. |
| bgc-2735-plan | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-target-input-plan-001.json; /records/4 | supports | Current accepted input and direct-companion scope; input presence alone confers no scientific proof. |
| bgc-2735-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch274/root-current274-source-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepted the original plan after attributed current source readings. |
| bgc-2735-gates | /private/tmp/npm-native-checks/batch-274/root-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_snapshot | context_only | Five required local commands passed; full QC/OAK remain unavailable. Queue entries remain leads. |
| bgc-2735-source-reading | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-current274-assigned-source-reading-001.json; /contexts/8; /counts; /reading_attribution | supports | All assigned saved dictionaries, physical rows and negative predicates were personally read; the selected subset is exact and separate from later molecular/reader results. |
| bgc-2735-source-notes | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-scope-notes-001.json; /totals; /reading_reconciliation; /cautions | context_only | Disjoint current primary credit is29 BGC plus20 Support rows; Native/ROOT credit0. This record uses its exact selected subset. |
| bgc-2735-taxonomy | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-cached-taxonomy-reading-001.json; /scope; /interpretation; /context_interpretations | context_only | Six complete cached stanzas and fifteen routes retain genus/species/strain distinctions, with zero missing/forward-merge/nonorganism matches. |
| bgc-2735-curation | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Nine substantive tables/3422 rows and125 current tokens yield zero lexical or exact applicable decisions. Two census-only tables remain outside scientific input scope. |
| bgc-2735-assay-curation | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-implemented-curation-scan-001.json; /assay_scope | context_only | The exact retained source queries contain no actual AID, blank assay sentinel, BindingDB target or AntibioticMech row. The owner has no measured bioactivity or pharmacological-target root. This bounded local absence does not establish inactivity, potency or therapeutic action; biosynthetic enzymes are not pharmacological targets. |
| bgc-2735-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines165-172: FindMolChiralCenters includeUnassigned | context_only | The retained stereo_complete flag tests unassigned atom-centred chirality; reconstructed imidic double-bond geometry is a separate representation issue. |
| bgc-2735-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines295-306: choose_pathway | context_only | Both computed pathways (Amino acids and Peptides and Polyketides) are retained while choose_pathway files the owner UNCLASSIFIED. This is consistent multi-label filing, not missing classification or biological absence. |
| bgc-2735-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 508-508; raw record sha256 8104f77d00eedc8b0bdb6204cf7fe60762dd100376b8a7aa41349ea7d7c57249 | supports | All 25 retained fields were personally read and physically joined; source grade/citation grain and blanks remain literal. |
| bgc-2735-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 2 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 2155-2155; raw record sha256 496cfa6ab5085a825b8db39b1137236ce265448d9e80dac2267fbc98cbbe96ba | supports | All 6 retained fields were personally read and physically joined; source grade/citation grain and blanks remain literal. |
| bgc-2735-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 2156-2156; raw record sha256 4265aeea3707b33c2e11f1b380f7d513018464bad5aee5b4cfe07b1efc382d71 | supports | All 6 retained fields were personally read and physically joined; source grade/citation grain and blanks remain literal. |
| bgc-2735-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 724-724; raw record sha256 c5e792453068208eeb98a6ca154ad4d91f2b8824028a63fc1d8af541dfe644e7 | supports | All 7 retained fields were personally read and physically joined; source grade/citation grain and blanks remain literal. |
| bgc-2735-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements; all returned fields and bounded negative predicates were personally read. |
| bgc-2735-congener-context | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kutzneride-1.yaml; Complete chemical_structure and source_concepts | context_only | The captured counterpart retains a different complete key/formula and atom-centre count; no identity, configuration, production or pathway transfer. |
| bgc-2735-congener-comparison | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-first-five-molecular-intake-reading-001.json; /records/3/declared_structure; /records/3/forms; /records/3/interpretation | context_only | Native-attributed complete saved counterpart facts support the stated congener distinction; no new atom correspondence or biological equivalence. |
| bgc-2735-reader-DATA | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-2-maintained-reader-DATA-001.json; /resolved_view; /returned_view_equals_expected_complete_owner; /counts; /limitations | supports | The original maintained reader preserves two graphs, six node placements, four edges,20 graph evidence placements, two numbered pathway steps/10 evidence placements and four history events. KtzQ (UniProtKB:A8CF75) and KtzR (A8CF74) are separately attributed precursor halogenation annotations: graph CHEBI:16828 to47356 to140086, with the reduced-flavin partner KtzS outside the Q graph. Numbered pathway steps1/2 retain RHEA:26494/55904 and different substrate/product identifiers CHEBI:57912 to58713 to139336 plus recorded cofactors/products; graph and pathway forms are not silently equated. The raw proposed field is absent, so no proposed flag is invented. PRIMARY_EXPERIMENT DOI:10.1021/ja806467a, MITE0000029/30, UniProt/NCBIProtein and historical sequence notes remain attributed evidence, not newly fetched primary or sequence verification. Curator-inferred shared-BGC placement is not demonstrated complete congener assembly or proof for every chlorine. No KtzA/D graphs are present in this owner. The two aromatic chlorines are compatible with this bounded precursor context, but the additional aliphatic chlorine and complete mature product are not mechanistically assigned by these two reactions. |
| bgc-2735-reader-execution | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-2-reader-execution-001.json; /command; /exit_code | supports | One original ROOT maintained-reader call, exit0; one expected capability probe blocked before socket construction and zero outbound requests. |
| bgc-2735-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch274/root-native-reader-2735-acceptance-001.json; /status; /accepted; /verification; /review_check_contract | supports | ROOT accepted complete current owner preservation and recorded runtime dependency pins; scientific interpretation remains bounded. |
| bgc-2735-graph | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-2-maintained-reader-DATA-001.json; /resolved_view/causal_graphs; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history | supports | The original maintained reader preserves two graphs, six node placements, four edges,20 graph evidence placements, two numbered pathway steps/10 evidence placements and four history events. KtzQ (UniProtKB:A8CF75) and KtzR (A8CF74) are separately attributed precursor halogenation annotations: graph CHEBI:16828 to47356 to140086, with the reduced-flavin partner KtzS outside the Q graph. Numbered pathway steps1/2 retain RHEA:26494/55904 and different substrate/product identifiers CHEBI:57912 to58713 to139336 plus recorded cofactors/products; graph and pathway forms are not silently equated. The raw proposed field is absent, so no proposed flag is invented. PRIMARY_EXPERIMENT DOI:10.1021/ja806467a, MITE0000029/30, UniProt/NCBIProtein and historical sequence notes remain attributed evidence, not newly fetched primary or sequence verification. Curator-inferred shared-BGC placement is not demonstrated complete congener assembly or proof for every chlorine. No KtzA/D graphs are present in this owner. The two aromatic chlorines are compatible with this bounded precursor context, but the additional aliphatic chlorine and complete mature product are not mechanistically assigned by these two reactions. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-274/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-274/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-274/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-274/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-274/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained source assertions, grades and histories are attributed; live identity/taxonomy authorities and cited primary papers were not independently verified. Full QC/OAK remain unavailable under the no-outbound hold.
- Three NH amides become terminal C(OH)=N sites while two tertiary amides remain; carbonyl7 to4 and strict amide5 to2. All atom charges remain zero. Matching formula, charge, standard InChI and full key is consistent with mobile-H/tautomer normalization, not net protonation change or exact fixed-form identity: both canonical comparisons are false, the one-way map is empty and full_graph_identity_established is false. Two original omitted-undefined-stereo warnings remain globally unassigned.
- Local topology predicates do not assign natural residues, every stereochemical detail, biosynthetic enzymes, assay activity or complete assembly.
- The maintained reader verifies complete view preservation and structural consistency. KtzQ/R precursor evidence, differing graph/pathway forms and historical sequence claims remain limited; no complete congener assembly is established.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Conclusions apply only to this exact owner and its captured current inputs; retained source status is unchanged.
- No source mutation, external request or new molecular/maintained-reader invocation was performed by this author.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T170757Z-kutzneride-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Kutzneride 2'
started_at: '2026-11-06T16:14:29.024610Z'
finished_at: '2026-11-06T17:07:57.263428Z'
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
summary: Kutzneride 2 retains its third aliphatic chlorine and ten specified atom
  centres. The maintained KtzQ/R annotations describe precursor chlorination, not
  the extra aliphatic event or complete congener assembly; source grades and representation
  limits remain explicit.
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
  - path: data/natural_products/amino_acids_and_peptides/kutzneride-6.yaml
    sha256: e9cd3bb0da0f378d8e964317eb9b5e0a3021b2f8dcc9341a9c9b12ada4559fd9
    role: context
  - path: data/natural_products/unclassified/kutzneride-1.yaml
    sha256: 2954407c141acbf2283eb99515c4f0973598b059ed2e215f82cbb3aa56f57aca
    role: context
  - path: data/natural_products/unclassified/kutzneride-2.yaml
    sha256: 26175cd1432d7580995f6852ca74fdb044c7466f8e5e54c6c88e33a4cf3d6749
    role: target
  - path: data/natural_products/unclassified/kutzneride-3.yaml
    sha256: b96bf6b28895c444556b57bf37db2a95e0a310ad2c797eef0b8348bd40cee853
    role: context
  - path: data/natural_products/unclassified/kutzneride-4.yaml
    sha256: 7cb271590a269d6dba7dbd49a2ba7b4b664bd47a9f9e894a62f5c4ce3e765ac6
    role: context
  - path: data/natural_products/unclassified/kutzneride-5.yaml
    sha256: 5ac0ba9f549d8eaf7b98f8fd4cfe5680867c92e3d0f5c82b6928d02754c83890
    role: context
  - path: data/natural_products/unclassified/kutzneride-7.yaml
    sha256: 6bd2a0ecf7dc600204cd4cb84b8db53ad7e77e772ed4631f619465c969e2a8fa
    role: context
  - path: data/natural_products/unclassified/kutzneride-8.yaml
    sha256: a67c6066e5671ca70c5c28062095db4f862dbd02e2d4b48a2a15abe999feed5a
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
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
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
  selection: Campaign path order 2735; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-c7ae5d3088
targets:
- target_id: naturalproductmech:mibig-c7ae5d3088
  path: data/natural_products/unclassified/kutzneride-2.yaml
  label: Kutzneride 2
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
    role: Retained exclusion-table diagnostic context captured for every review; applicable
      exact assay exclusions and biological rows must be derived from actual retained
      inventory, not file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic context used by the bounded curation
      scan; no fresh taxonomy, forward-merge decision or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Retained explicit forward-merge table used by positive and negative taxon
      queries for each owner; historical route evidence only, no fresh taxonomy.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism table used by positive and negative taxon queries
      for each owner; diagnostic scope only, not a taxon verdict from file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained exclusion identity, source-row digest and attributed-rationale
      implementation context; no execution or new assay evidence.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/producer_strains.py
    role: 'Maintained producer-strain qualification implementation: source-row and
      digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency,
      no execution or grade/taxon upgrade.'
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: 'Maintained row_digest implementation used by qualification guards: sorted
      ensure_ascii JSON digest only; input presence does not claim an audit or application
      of other structure-correction behavior.'
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/kutzneride-2.yaml
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
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnose274-001.py
    12549d68400aa9861f680ef37c41c182318bcf0d07247b93dcf43f66da0eaa0e 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
    ce78cc5fde09a6c9a7c6416bbf4aad680efff7f9414040b475e81a26c9a05f61
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed in the original twenty-attempt diagnostic; formula,
    charge, normalized InChI and complete key agree.
  scope_note: 'Three NH amides become terminal C(OH)=N sites while two tertiary amides
    remain; carbonyl7 to4 and strict amide5 to2. All atom charges remain zero. Matching
    formula, charge, standard InChI and full key is consistent with mobile-H/tautomer
    normalization, not net protonation change or exact fixed-form identity: both canonical
    comparisons are false, the one-way map is empty and full_graph_identity_established
    is false. Two original omitted-undefined-stereo warnings remain globally unassigned.
    No natural identity or primary biological certification follows.'
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-chemistry
  - bgc-2735-diagnostic-acceptance
  - bgc-2735-diagnostic-execution
  - bgc-2735-diagnostic-stderr
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for kutzneride-2
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch274/read-selected-mechanism-guarded-001.py
    2735 ce78cc5fde09a6c9a7c6416bbf4aad680efff7f9414040b475e81a26c9a05f61 1deb507efd02d920caa748b2404d84ced2f4a3e09465798723c57af273829c8e
    207b9ecac890a6753cbe5ba79997dacaf2b9c818f28fb2e58539b9e55415c2e8 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
    12549d68400aa9861f680ef37c41c182318bcf0d07247b93dcf43f66da0eaa0e
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: One original maintained reader preserved the complete Kutzneride 2 owner,
    all graph/pathway evidence and history, with zero components.
  scope_note: Preservation and structural consistency only; precursor, historical
    sequence and primary evidence remain attributed. Graph/pathway forms stay distinct;
    no complete assembly or catalytic upgrade. One expected IPv6 capability probe
    was blocked before action; no request was sent.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-reader-DATA
  - bgc-2735-reader-execution
  - bgc-2735-reader-acceptance
  - bgc-2735-graph
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  command: just validate-strict data/natural_products/unclassified/kitacinnamycin-e.yaml
    data/natural_products/unclassified/kitacinnamycin-f.yaml data/natural_products/unclassified/kk-1.yaml
    data/natural_products/unclassified/kutzneride-1.yaml data/natural_products/unclassified/kutzneride-2.yaml
    data/natural_products/unclassified/kutzneride-3.yaml data/natural_products/unclassified/kutzneride-4.yaml
    data/natural_products/unclassified/kutzneride-5.yaml data/natural_products/unclassified/kutzneride-7.yaml
    data/natural_products/unclassified/kutzneride-8.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-274/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-c7ae5d3088
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-274/validate-all-001.tsv
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
  - naturalproductmech:mibig-c7ae5d3088
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
  - naturalproductmech:mibig-c7ae5d3088
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
  - naturalproductmech:mibig-c7ae5d3088
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-274/review-queue-001.tsv
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
  - naturalproductmech:mibig-c7ae5d3088
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2735-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kutzneride-2.yaml
  locator: Complete plaintext and all curation_history entries
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: The complete current owner/history was personally read; all source assertions
    and curated annotations remain attributed.
  snapshot_sha256: 26175cd1432d7580995f6852ca74fdb044c7466f8e5e54c6c88e33a4cf3d6749
- evidence_id: bgc-2735-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/chemical_structure;
    /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: Kutzneride 2 retains exact owner naturalproductmech:mibig-c7ae5d3088, full
    key GOUIVYIRLLTNCF-JJMZTBTASA-N, C37H48Cl3N7O12 and BGC0000378 compound 2. The
    third, aliphatic chlorine and tenth specified atom centre distinguish it from
    1. NPAtlas NPA015447 and shared precursor annotations do not merge congener identities.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: bgc-2735-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/4/owner_document/curation_history
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: MIBiG COMPOUND_EVIDENCE DOI:10.1021/np050378g duplicates the LOTUS NP050378G
    DOI by case, while NP0604331 is an additional occurrence citation. Four histories
    comprise two seeding and two codex KtzQ/R curation events. Historical primary
    and sequence references are retained annotations, not newly repeated or fetched
    verification.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: bgc-2735-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: Kutzneria sp. 744 NCBITaxon:345341 retains SOURCE_ASSERTION producer evidence
    from MIBiG version5. Genus-level NCBITaxon:43356 occurrences remain separate,
    and precursor-enzyme evidence does not demonstrate complete production of this
    congener. BGC0000378 version5 is active/questionable with unknown completeness.
    EU074211.1 retains CLUSTER_UNSTATED and no source coordinates or methods. Shared
    KtzQ/R precursor annotations do not prove the complete congener-specific assembly
    or the extra aliphatic chlorination.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: bgc-2735-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway;
    /records/4/owner_document/bgc_class
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: The 18-membered ester-containing macrocycle and amides support Cyclic peptides/Depsipeptides
    locally. The third chlorine does not identify a tailoring enzyme. Absence of a
    saturated C5O candidate ring is compatible with glycoside=false at this limited
    scope; blank source class and NRPS/Type I labels remain source/model assertions
    rather than complete assembly evidence. Both computed pathways (Amino acids and
    Peptides and Polyketides) are retained while choose_pathway files the owner UNCLASSIFIED.
    This is consistent multi-label filing, not missing classification or biological
    absence.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: bgc-2735-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/complete_root_keys; /contexts/9/declared_mechanism_roots_literal;
    /contexts/9/literal_bioactivities_root
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: The whole owner retains the explicitly scoped mechanism/pathway, with no
    pharmacological target or measured bioactivity root.
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: Exact complete current owner root set only; no congener or activity
    transfer.
- evidence_id: bgc-2735-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/literal_InChI_layers
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: 'Each saved form has59 atoms/64 bonds and cycle sizes3,18,6,5,5,6. One
    ester, COOH and methoxy ether remain. Two chlorines are aromatic and the additional
    chlorine is aliphatic in the N-N six-ring. This locates the structural distinction
    without assigning its biosynthetic enzyme. Both forms report ten specified tetrahedral
    centres, including the chlorinated aliphatic centre, and the InChI form adds three
    unspecified C=N potentials. Source stereo_complete:true does not certify all reconstructed
    double-bond geometry or independently verify natural configuration. Three NH amides
    become terminal C(OH)=N sites while two tertiary amides remain; carbonyl7 to4
    and strict amide5 to2. All atom charges remain zero. Matching formula, charge,
    standard InChI and full key is consistent with mobile-H/tautomer normalization,
    not net protonation change or exact fixed-form identity: both canonical comparisons
    are false, the one-way map is empty and full_graph_identity_established is false.'
  snapshot_sha256: 968b394137ace1559551b48880dc4f4860d58cd338562129d08ad6037ce4ccb6
- evidence_id: bgc-2735-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-first-five-molecular-intake-reading-001.json
  locator: /records/4; /scope_orders; /original_stderr; /method_limits
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: Native personally read the complete saved atom/bond/ring/stereo/motif tables.
    This author read the complete attributed interpretations and critical summaries;
    no new parse or duplicate primary source-row credit.
  snapshot_sha256: 2eec74f11381aa8efadbf50fdd6a0db29ffb12f8497be9b12238ba17be077813
- evidence_id: bgc-2735-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /full_graph_identity_established
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: ROOT accepted one original twenty-form diagnostic. All fixed-form canonical
    comparisons remain false and full graph identity is not established.
  snapshot_sha256: 0c8c7b7e8d27b7373931eb6d60bb04c0bd41e089410a3ae0d1e15b2ad101a345
- evidence_id: bgc-2735-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: Exact original ROOT command and zero exit; this command is evidence, not
    a replay.
  snapshot_sha256: dcbf2e358a8b2141865d7795f53402e4c5b4dcd9a4ea92ef690eafdc89d1a4b3
- evidence_id: bgc-2735-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr; two nonempty warning lines
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Two omitted-undefined-stereo warnings remain globally unassigned.
  snapshot_sha256: 9028daa403fda9b7a6e810495102e0b067e7651420fd532f30578816b98a6147
- evidence_id: bgc-2735-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/intakes-001/2735-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: One exact target, 53 current input hashes and explicit maintained ownership
    declarations.
  snapshot_sha256: 1deb507efd02d920caa748b2404d84ced2f4a3e09465798723c57af273829c8e
- evidence_id: bgc-2735-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/root-intake-acceptance-001.json
  locator: /status; /accepted; /input_placements; /unique_input_paths
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: ROOT accepted ten actual canonical inspections with513 input placements/60
    unique paths.
  snapshot_sha256: 44e8e110bef4b892fba9024b09cab57eef2ed34c5977f1d8db37176b2db6418f
- evidence_id: bgc-2735-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-target-input-plan-001.json
  locator: /records/4
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: Current accepted input and direct-companion scope; input presence alone
    confers no scientific proof.
  snapshot_sha256: 83af42d96827a5af436bb7aca0ccb952527ad886bf06d40a18c2ec1a0c770708
- evidence_id: bgc-2735-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/root-current274-source-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: ROOT accepted the original plan after attributed current source readings.
  snapshot_sha256: 15c392305536f94216a1174abce9db3443ca92c3467358e2e2c2f629f7a40f06
- evidence_id: bgc-2735-gates
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/root-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_snapshot
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Five required local commands passed; full QC/OAK remain unavailable. Queue
    entries remain leads.
  snapshot_sha256: 70c72a46f5d647646262e080f7a03cac5b3deb9fd8ea34dbc344262115b876fc
- evidence_id: bgc-2735-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-current274-assigned-source-reading-001.json
  locator: /contexts/8; /counts; /reading_attribution
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: All assigned saved dictionaries, physical rows and negative predicates
    were personally read; the selected subset is exact and separate from later molecular/reader
    results.
  snapshot_sha256: cf0247f6de846a4d494fb851234b47deecc6fffd12a17dc9bbebfdaa011ddb84
- evidence_id: bgc-2735-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /cautions
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Disjoint current primary credit is29 BGC plus20 Support rows; Native/ROOT
    credit0. This record uses its exact selected subset.
  snapshot_sha256: ccb81806b7d50db41cfc2aaaeb638f9df68733017a6e847ab3c72bf2d0fedf94
- evidence_id: bgc-2735-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-cached-taxonomy-reading-001.json
  locator: /scope; /interpretation; /context_interpretations
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Six complete cached stanzas and fifteen routes retain genus/species/strain
    distinctions, with zero missing/forward-merge/nonorganism matches.
  snapshot_sha256: ab95bb0dcc77d16661eb24f6b3d9d07b99215275ece984f359f75775d0947596
  search_scope: Current exact retained route predicates only; no new live taxonomic
    rank/lineage/strain or OAK validation.
- evidence_id: bgc-2735-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Nine substantive tables/3422 rows and125 current tokens yield zero lexical
    or exact applicable decisions. Two census-only tables remain outside scientific
    input scope.
  snapshot_sha256: 204d96aa0c5d6a835ef6e361ffc70af374d6cdce738af90d1e81ce141502e289
  search_scope: Current274 bounded tokens and implemented exact predicates only; no
    external correction-absence claim.
- evidence_id: bgc-2735-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: The exact retained source queries contain no actual AID, blank assay sentinel,
    BindingDB target or AntibioticMech row. The owner has no measured bioactivity
    or pharmacological-target root. This bounded local absence does not establish
    inactivity, potency or therapeutic action; biosynthetic enzymes are not pharmacological
    targets.
  snapshot_sha256: 204d96aa0c5d6a835ef6e361ffc70af374d6cdce738af90d1e81ce141502e289
  search_scope: Zero actual AIDs and zero blank sentinels in current saved scope;
    all15 retained exclusion decisions require exact full predicates and none applies.
- evidence_id: bgc-2735-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines165-172: FindMolChiralCenters includeUnassigned'
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: The retained stereo_complete flag tests unassigned atom-centred chirality;
    reconstructed imidic double-bond geometry is a separate representation issue.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2735-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines295-306: choose_pathway'
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Both computed pathways (Amino acids and Peptides and Polyketides) are retained
    while choose_pathway files the owner UNCLASSIFIED. This is consistent multi-label
    filing, not missing classification or biological absence.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2735-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
- evidence_id: bgc-2735-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 508-508; raw record sha256 8104f77d00eedc8b0bdb6204cf7fe60762dd100376b8a7aa41349ea7d7c57249
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: All 25 retained fields were personally read and physically joined; source
    grade/citation grain and blanks remain literal.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2735-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kutzneride-2.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GOUIVYIRLLTNCF-JJMZTBTASA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2735-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 2 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
- evidence_id: bgc-2735-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 2155-2155; raw record sha256 496cfa6ab5085a825b8db39b1137236ce265448d9e80dac2267fbc98cbbe96ba
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: All 6 retained fields were personally read and physically joined; source
    grade/citation grain and blanks remain literal.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2735-row-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 2156-2156; raw record sha256 4265aeea3707b33c2e11f1b380f7d513018464bad5aee5b4cfe07b1efc382d71
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: All 6 retained fields were personally read and physically joined; source
    grade/citation grain and blanks remain literal.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2735-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements; all
    returned fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kutzneride-2.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GOUIVYIRLLTNCF-JJMZTBTASA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2735-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
- evidence_id: bgc-2735-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 724-724; raw record sha256 c5e792453068208eeb98a6ca154ad4d91f2b8824028a63fc1d8af541dfe644e7
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: All 7 retained fields were personally read and physically joined; source
    grade/citation grain and blanks remain literal.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2735-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kutzneride-2.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GOUIVYIRLLTNCF-JJMZTBTASA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2735-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kutzneride-2.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GOUIVYIRLLTNCF-JJMZTBTASA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2735-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements;
    all returned fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kutzneride-2.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GOUIVYIRLLTNCF-JJMZTBTASA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2735-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements; all returned
    fields and bounded negative predicates were personally read.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kutzneride-2.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: bgc-2735-congener-context
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kutzneride-1.yaml
  locator: Complete chemical_structure and source_concepts
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: The captured counterpart retains a different complete key/formula and atom-centre
    count; no identity, configuration, production or pathway transfer.
  snapshot_sha256: 2954407c141acbf2283eb99515c4f0973598b059ed2e215f82cbb3aa56f57aca
- evidence_id: bgc-2735-congener-comparison
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-first-five-molecular-intake-reading-001.json
  locator: /records/3/declared_structure; /records/3/forms; /records/3/interpretation
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: context_only
  summary: Native-attributed complete saved counterpart facts support the stated congener
    distinction; no new atom correspondence or biological equivalence.
  snapshot_sha256: 2eec74f11381aa8efadbf50fdd6a0db29ffb12f8497be9b12238ba17be077813
- evidence_id: bgc-2735-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-2-maintained-reader-DATA-001.json
  locator: /resolved_view; /returned_view_equals_expected_complete_owner; /counts;
    /limitations
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: 'The original maintained reader preserves two graphs, six node placements,
    four edges,20 graph evidence placements, two numbered pathway steps/10 evidence
    placements and four history events. KtzQ (UniProtKB:A8CF75) and KtzR (A8CF74)
    are separately attributed precursor halogenation annotations: graph CHEBI:16828
    to47356 to140086, with the reduced-flavin partner KtzS outside the Q graph. Numbered
    pathway steps1/2 retain RHEA:26494/55904 and different substrate/product identifiers
    CHEBI:57912 to58713 to139336 plus recorded cofactors/products; graph and pathway
    forms are not silently equated. The raw proposed field is absent, so no proposed
    flag is invented. PRIMARY_EXPERIMENT DOI:10.1021/ja806467a, MITE0000029/30, UniProt/NCBIProtein
    and historical sequence notes remain attributed evidence, not newly fetched primary
    or sequence verification. Curator-inferred shared-BGC placement is not demonstrated
    complete congener assembly or proof for every chlorine. No KtzA/D graphs are present
    in this owner. The two aromatic chlorines are compatible with this bounded precursor
    context, but the additional aliphatic chlorine and complete mature product are
    not mechanistically assigned by these two reactions.'
  snapshot_sha256: cc12c38de33e72afac6f5c6c568f9f15fa22c9d99282b1151a6b69e14a6d0610
- evidence_id: bgc-2735-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-2-reader-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: One original ROOT maintained-reader call, exit0; one expected capability
    probe blocked before socket construction and zero outbound requests.
  snapshot_sha256: 32f4e91fa4f7ed6e8e0bfe66d1aca0b8987f5a4295386bf923d81cedcc0f4d82
- evidence_id: bgc-2735-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/root-native-reader-2735-acceptance-001.json
  locator: /status; /accepted; /verification; /review_check_contract
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: ROOT accepted complete current owner preservation and recorded runtime
    dependency pins; scientific interpretation remains bounded.
  snapshot_sha256: e6d2ca731c7a253c68b537d4fbe2015220748852eb7f5aa87dfa582657eb4a7a
- evidence_id: bgc-2735-graph
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-2-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history
  accessed_at: '2026-11-06T16:57:43.841046Z'
  support: supports
  summary: 'The original maintained reader preserves two graphs, six node placements,
    four edges,20 graph evidence placements, two numbered pathway steps/10 evidence
    placements and four history events. KtzQ (UniProtKB:A8CF75) and KtzR (A8CF74)
    are separately attributed precursor halogenation annotations: graph CHEBI:16828
    to47356 to140086, with the reduced-flavin partner KtzS outside the Q graph. Numbered
    pathway steps1/2 retain RHEA:26494/55904 and different substrate/product identifiers
    CHEBI:57912 to58713 to139336 plus recorded cofactors/products; graph and pathway
    forms are not silently equated. The raw proposed field is absent, so no proposed
    flag is invented. PRIMARY_EXPERIMENT DOI:10.1021/ja806467a, MITE0000029/30, UniProt/NCBIProtein
    and historical sequence notes remain attributed evidence, not newly fetched primary
    or sequence verification. Curator-inferred shared-BGC placement is not demonstrated
    complete congener assembly or proof for every chlorine. No KtzA/D graphs are present
    in this owner. The two aromatic chlorines are compatible with this bounded precursor
    context, but the additional aliphatic chlorine and complete mature product are
    not mechanistically assigned by these two reactions.'
  snapshot_sha256: cc12c38de33e72afac6f5c6c568f9f15fa22c9d99282b1151a6b69e14a6d0610
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:15:09.494074Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: cd7d41117a4f278a0ff9fddf933a24f1419ad0e5c4f6c531afdb8145c64d3a4b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:15:34.127215Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 9a2b548d7e3e59d3e4b40953a14514daf8c4c59f1d53a6fd2dada6108673dfc9
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:15:53.345460Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:16:26.812981Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:16:38.263309Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 39cc66beb0fcbfcd1a090de6f99823466c4b7f1a642ff96107c65f51784a3909
assessments:
- assessment_id: bgc-2735-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: Kutzneride 2 retains exact owner naturalproductmech:mibig-c7ae5d3088, full
    key GOUIVYIRLLTNCF-JJMZTBTASA-N, C37H48Cl3N7O12 and BGC0000378 compound 2. The
    third, aliphatic chlorine and tenth specified atom centre distinguish it from
    1. NPAtlas NPA015447 and shared precursor annotations do not merge congener identities.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-identity
  - bgc-2735-chemistry
  - bgc-2735-query-mibig_compounds
  - bgc-2735-query-chebi_structures
  - bgc-2735-plan
  - bgc-2735-row-mibig_compounds-0
  - bgc-2735-congener-context
  - bgc-2735-congener-comparison
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: GOUIVYIRLLTNCF-JJMZTBTASA-N
    evidence_ids:
    - bgc-2735-identity
    - bgc-2735-chemistry
    - bgc-2735-query-mibig_compounds
    - bgc-2735-query-chebi_structures
    - bgc-2735-plan
    - bgc-2735-row-mibig_compounds-0
    - bgc-2735-congener-context
    - bgc-2735-congener-comparison
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: Kutzneride 2 retains exact owner naturalproductmech:mibig-c7ae5d3088, full
      key GOUIVYIRLLTNCF-JJMZTBTASA-N, C37H48Cl3N7O12 and BGC0000378 compound 2. The
      third, aliphatic chlorine and tenth specified atom centre distinguish it from
      1. NPAtlas NPA015447 and shared precursor annotations do not merge congener
      identities.
    evidence_ids:
    - bgc-2735-identity
    - bgc-2735-chemistry
    - bgc-2735-query-mibig_compounds
    - bgc-2735-query-chebi_structures
    - bgc-2735-plan
    - bgc-2735-row-mibig_compounds-0
    - bgc-2735-congener-context
    - bgc-2735-congener-comparison
- assessment_id: bgc-2735-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: 'Each saved form has59 atoms/64 bonds and cycle sizes3,18,6,5,5,6. One
    ester, COOH and methoxy ether remain. Two chlorines are aromatic and the additional
    chlorine is aliphatic in the N-N six-ring. This locates the structural distinction
    without assigning its biosynthetic enzyme. Both forms report ten specified tetrahedral
    centres, including the chlorinated aliphatic centre, and the InChI form adds three
    unspecified C=N potentials. Source stereo_complete:true does not certify all reconstructed
    double-bond geometry or independently verify natural configuration. Three NH amides
    become terminal C(OH)=N sites while two tertiary amides remain; carbonyl7 to4
    and strict amide5 to2. All atom charges remain zero. Matching formula, charge,
    standard InChI and full key is consistent with mobile-H/tautomer normalization,
    not net protonation change or exact fixed-form identity: both canonical comparisons
    are false, the one-way map is empty and full_graph_identity_established is false.'
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-identity
  - bgc-2735-chemistry
  - bgc-2735-molecular-reading
  - bgc-2735-diagnostic-acceptance
  - bgc-2735-diagnostic-stderr
  - bgc-2735-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Both forms report ten specified tetrahedral centres, including the chlorinated
      aliphatic centre, and the InChI form adds three unspecified C=N potentials.
      Source stereo_complete:true does not certify all reconstructed double-bond geometry
      or independently verify natural configuration.
    evidence_ids:
    - bgc-2735-identity
    - bgc-2735-chemistry
    - bgc-2735-molecular-reading
    - bgc-2735-diagnostic-acceptance
    - bgc-2735-diagnostic-stderr
    - bgc-2735-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: 'Three NH amides become terminal C(OH)=N sites while two tertiary amides
      remain; carbonyl7 to4 and strict amide5 to2. All atom charges remain zero. Matching
      formula, charge, standard InChI and full key is consistent with mobile-H/tautomer
      normalization, not net protonation change or exact fixed-form identity: both
      canonical comparisons are false, the one-way map is empty and full_graph_identity_established
      is false.'
    evidence_ids:
    - bgc-2735-identity
    - bgc-2735-chemistry
    - bgc-2735-molecular-reading
    - bgc-2735-diagnostic-acceptance
    - bgc-2735-diagnostic-stderr
    - bgc-2735-stereo-policy
- assessment_id: bgc-2735-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: Kutzneria sp. 744 NCBITaxon:345341 retains SOURCE_ASSERTION producer evidence
    from MIBiG version5. Genus-level NCBITaxon:43356 occurrences remain separate,
    and precursor-enzyme evidence does not demonstrate complete production of this
    congener. BGC0000378 version5 is active/questionable with unknown completeness.
    EU074211.1 retains CLUSTER_UNSTATED and no source coordinates or methods. Shared
    KtzQ/R precursor annotations do not prove the complete congener-specific assembly
    or the extra aliphatic chlorination.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-provenance
  - bgc-2735-query-mibig_compounds
  - bgc-2735-taxonomy
  - bgc-2735-curation
  - bgc-2735-row-mibig_compounds-0
  - bgc-2735-graph
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: Kutzneria sp. 744 NCBITaxon:345341 retains SOURCE_ASSERTION producer evidence
      from MIBiG version5. Genus-level NCBITaxon:43356 occurrences remain separate,
      and precursor-enzyme evidence does not demonstrate complete production of this
      congener.
    evidence_ids:
    - bgc-2735-provenance
    - bgc-2735-query-mibig_compounds
    - bgc-2735-taxonomy
    - bgc-2735-curation
    - bgc-2735-row-mibig_compounds-0
    - bgc-2735-graph
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: Kutzneria sp. 744 NCBITaxon:345341 retains SOURCE_ASSERTION producer evidence
      from MIBiG version5. Genus-level NCBITaxon:43356 occurrences remain separate,
      and precursor-enzyme evidence does not demonstrate complete production of this
      congener.
    evidence_ids:
    - bgc-2735-provenance
    - bgc-2735-query-mibig_compounds
    - bgc-2735-taxonomy
    - bgc-2735-curation
    - bgc-2735-row-mibig_compounds-0
    - bgc-2735-graph
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0000378 version5 is active/questionable with unknown completeness. EU074211.1
      retains CLUSTER_UNSTATED and no source coordinates or methods. Shared KtzQ/R
      precursor annotations do not prove the complete congener-specific assembly or
      the extra aliphatic chlorination.
    evidence_ids:
    - bgc-2735-provenance
    - bgc-2735-query-mibig_compounds
    - bgc-2735-taxonomy
    - bgc-2735-curation
    - bgc-2735-row-mibig_compounds-0
    - bgc-2735-graph
- assessment_id: bgc-2735-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: MIBiG COMPOUND_EVIDENCE DOI:10.1021/np050378g duplicates the LOTUS NP050378G
    DOI by case, while NP0604331 is an additional occurrence citation. Four histories
    comprise two seeding and two codex KtzQ/R curation events. Historical primary
    and sequence references are retained annotations, not newly repeated or fetched
    verification.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-history
  - bgc-2735-provenance
  - bgc-2735-source-reading
  - bgc-2735-query-mibig_compounds
  - bgc-2735-row-mibig_compounds-0
  - bgc-2735-graph
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: MIBiG COMPOUND_EVIDENCE DOI:10.1021/np050378g duplicates the LOTUS NP050378G
      DOI by case, while NP0604331 is an additional occurrence citation. Four histories
      comprise two seeding and two codex KtzQ/R curation events. Historical primary
      and sequence references are retained annotations, not newly repeated or fetched
      verification.
    evidence_ids:
    - bgc-2735-history
    - bgc-2735-provenance
    - bgc-2735-source-reading
    - bgc-2735-query-mibig_compounds
    - bgc-2735-row-mibig_compounds-0
    - bgc-2735-graph
- assessment_id: bgc-2735-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: Two physical LOTUS rows retain Kutzneria genus NCBITaxon:43356 and NP050378G/NP0604331.
    The shared source DOI is not an independent confirmation, and genus occurrence
    does not identify strain744 or prove this congener's production. The exact retained
    source queries contain no actual AID, blank assay sentinel, BindingDB target or
    AntibioticMech row. The owner has no measured bioactivity or pharmacological-target
    root. This bounded local absence does not establish inactivity, potency or therapeutic
    action; biosynthetic enzymes are not pharmacological targets.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-roots
  - bgc-2735-query-lotus_occurrences
  - bgc-2735-query-cyanometdb_occurrences
  - bgc-2735-query-pubchem_bioassay
  - bgc-2735-query-bindingdb_targets
  - bgc-2735-query-antibioticmech_inchikeys
  - bgc-2735-assay-curation
  - bgc-2735-row-lotus_occurrences-0
  - bgc-2735-row-lotus_occurrences-1
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: Two physical LOTUS rows retain Kutzneria genus NCBITaxon:43356 and NP050378G/NP0604331.
      The shared source DOI is not an independent confirmation, and genus occurrence
      does not identify strain744 or prove this congener's production.
    evidence_ids:
    - bgc-2735-roots
    - bgc-2735-query-lotus_occurrences
    - bgc-2735-query-cyanometdb_occurrences
    - bgc-2735-query-pubchem_bioassay
    - bgc-2735-query-bindingdb_targets
    - bgc-2735-query-antibioticmech_inchikeys
    - bgc-2735-assay-curation
    - bgc-2735-row-lotus_occurrences-0
    - bgc-2735-row-lotus_occurrences-1
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: The exact retained source queries contain no actual AID, blank assay sentinel,
      BindingDB target or AntibioticMech row. The owner has no measured bioactivity
      or pharmacological-target root. This bounded local absence does not establish
      inactivity, potency or therapeutic action; biosynthetic enzymes are not pharmacological
      targets.
    evidence_ids:
    - bgc-2735-roots
    - bgc-2735-query-lotus_occurrences
    - bgc-2735-query-cyanometdb_occurrences
    - bgc-2735-query-pubchem_bioassay
    - bgc-2735-query-bindingdb_targets
    - bgc-2735-query-antibioticmech_inchikeys
    - bgc-2735-assay-curation
    - bgc-2735-row-lotus_occurrences-0
    - bgc-2735-row-lotus_occurrences-1
- assessment_id: bgc-2735-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: The 18-membered ester-containing macrocycle and amides support Cyclic peptides/Depsipeptides
    locally. The third chlorine does not identify a tailoring enzyme. Absence of a
    saturated C5O candidate ring is compatible with glycoside=false at this limited
    scope; blank source class and NRPS/Type I labels remain source/model assertions
    rather than complete assembly evidence. Both computed pathways (Amino acids and
    Peptides and Polyketides) are retained while choose_pathway files the owner UNCLASSIFIED.
    This is consistent multi-label filing, not missing classification or biological
    absence.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-classification
  - bgc-2735-chemistry
  - bgc-2735-query-npclassifier
  - bgc-2735-query-mibig_compounds
  - bgc-2735-filing-policy
  - bgc-2735-row-npclassifier-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: The 18-membered ester-containing macrocycle and amides support Cyclic peptides/Depsipeptides
      locally. The third chlorine does not identify a tailoring enzyme. Absence of
      a saturated C5O candidate ring is compatible with glycoside=false at this limited
      scope; blank source class and NRPS/Type I labels remain source/model assertions
      rather than complete assembly evidence. Both computed pathways (Amino acids
      and Peptides and Polyketides) are retained while choose_pathway files the owner
      UNCLASSIFIED. This is consistent multi-label filing, not missing classification
      or biological absence.
    evidence_ids:
    - bgc-2735-classification
    - bgc-2735-chemistry
    - bgc-2735-query-npclassifier
    - bgc-2735-query-mibig_compounds
    - bgc-2735-filing-policy
    - bgc-2735-row-npclassifier-0
- assessment_id: bgc-2735-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Whole owner/history and all nine saved query frames (4 positive rows/44
    fields) were personally read. Native independently read all atom/bond/ring/stereo/motif
    rows of both saved molecular forms; this author read their complete interpretations
    and critical topology/stereo summaries. All 53 actual input hashes and ownership
    declarations were verified, without claiming whole-corpus semantic reading. Five
    local native commands passed; full QC/OAK, live source authorities and independent
    primary confirmation remain unavailable. The complete accepted maintained owner
    view and its graph/pathway/history were personally read; biological claims remain
    qualified. Generated assertions belong to maintained source inputs, applicable
    curation tables, extractors and seeder; curated graph/history edits require the
    maintained writer and attributed curation. No edit is proposed.
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-owner
  - bgc-2735-history
  - bgc-2735-intake
  - bgc-2735-intake-acceptance
  - bgc-2735-plan
  - bgc-2735-plan-acceptance
  - bgc-2735-gates
  - bgc-2735-source-reading
  - bgc-2735-source-notes
  - bgc-2735-molecular-reading
  - bgc-2735-roots
  - bgc-2735-reader-DATA
  - bgc-2735-reader-execution
  - bgc-2735-reader-acceptance
  - bgc-2735-graph
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Whole owner/history and all nine saved query frames (4 positive rows/44
      fields) were personally read. Native independently read all atom/bond/ring/stereo/motif
      rows of both saved molecular forms; this author read their complete interpretations
      and critical topology/stereo summaries. All 53 actual input hashes and ownership
      declarations were verified, without claiming whole-corpus semantic reading.
      Five local native commands passed; full QC/OAK, live source authorities and
      independent primary confirmation remain unavailable. The complete accepted maintained
      owner view and its graph/pathway/history were personally read; biological claims
      remain qualified. Generated assertions belong to maintained source inputs, applicable
      curation tables, extractors and seeder; curated graph/history edits require
      the maintained writer and attributed curation. No edit is proposed.
    evidence_ids:
    - bgc-2735-owner
    - bgc-2735-history
    - bgc-2735-intake
    - bgc-2735-intake-acceptance
    - bgc-2735-plan
    - bgc-2735-plan-acceptance
    - bgc-2735-gates
    - bgc-2735-source-reading
    - bgc-2735-source-notes
    - bgc-2735-molecular-reading
    - bgc-2735-roots
    - bgc-2735-reader-DATA
    - bgc-2735-reader-execution
    - bgc-2735-reader-acceptance
    - bgc-2735-graph
- assessment_id: bgc-2735-graph
  area: graph
  topic: Precursor KtzQ/R chemistry, distinct pathway forms and congener-specific
    limits
  outcome: supported
  summary: 'The original maintained reader preserves two graphs, six node placements,
    four edges,20 graph evidence placements, two numbered pathway steps/10 evidence
    placements and four history events. KtzQ (UniProtKB:A8CF75) and KtzR (A8CF74)
    are separately attributed precursor halogenation annotations: graph CHEBI:16828
    to47356 to140086, with the reduced-flavin partner KtzS outside the Q graph. Numbered
    pathway steps1/2 retain RHEA:26494/55904 and different substrate/product identifiers
    CHEBI:57912 to58713 to139336 plus recorded cofactors/products; graph and pathway
    forms are not silently equated. The raw proposed field is absent, so no proposed
    flag is invented. PRIMARY_EXPERIMENT DOI:10.1021/ja806467a, MITE0000029/30, UniProt/NCBIProtein
    and historical sequence notes remain attributed evidence, not newly fetched primary
    or sequence verification. Curator-inferred shared-BGC placement is not demonstrated
    complete congener assembly or proof for every chlorine. No KtzA/D graphs are present
    in this owner. The two aromatic chlorines are compatible with this bounded precursor
    context, but the additional aliphatic chlorine and complete mature product are
    not mechanistically assigned by these two reactions.'
  target_ids:
  - naturalproductmech:mibig-c7ae5d3088
  evidence_ids:
  - bgc-2735-graph
  - bgc-2735-reader-DATA
  - bgc-2735-reader-execution
  - bgc-2735-reader-acceptance
  - bgc-2735-chemistry
  - bgc-2735-query-mibig_compounds
  dimensions: []
findings: []
actions: []
limitations:
- Retained source assertions, grades and histories are attributed; live identity/taxonomy
  authorities and cited primary papers were not independently verified. Full QC/OAK
  remain unavailable under the no-outbound hold.
- 'Three NH amides become terminal C(OH)=N sites while two tertiary amides remain;
  carbonyl7 to4 and strict amide5 to2. All atom charges remain zero. Matching formula,
  charge, standard InChI and full key is consistent with mobile-H/tautomer normalization,
  not net protonation change or exact fixed-form identity: both canonical comparisons
  are false, the one-way map is empty and full_graph_identity_established is false.
  Two original omitted-undefined-stereo warnings remain globally unassigned.'
- Local topology predicates do not assign natural residues, every stereochemical detail,
  biosynthetic enzymes, assay activity or complete assembly.
- The maintained reader verifies complete view preservation and structural consistency.
  KtzQ/R precursor evidence, differing graph/pathway forms and historical sequence
  claims remain limited; no complete congener assembly is established.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Conclusions apply only to this exact owner and its captured current inputs; retained
  source status is unchanged.
- No source mutation, external request or new molecular/maintained-reader invocation
  was performed by this author.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-274
```
