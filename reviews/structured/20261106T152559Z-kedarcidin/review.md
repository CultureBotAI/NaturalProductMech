# Local evidence review: kedarcidin

- Review: 20261106T152559Z-kedarcidin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T14:21:26.902206Z
- Finished UTC: 2026-11-06T15:25:59.137590Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Kedarcidin retains an enediyne-containing small-molecule scaffold with two O-linked C5O candidate rings and fourteen unspecified tetrahedral centers. Source-strain, genus occurrence and locus grades remain distinct; named sugars, protein-complex identity and natural stereochemistry are not newly established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2725; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-fed5796f29 | data/natural_products/unclassified/kedarcidin.yaml | generated | kedarcidin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-fed5796f29 | Both stored owner forms parsed in the original twenty-attempt diagnostic and share formula, charge, normalized InChI and declared full key. |
| strict_ten | passed | True | naturalproductmech:mibig-fed5796f29 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-fed5796f29 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-fed5796f29 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-fed5796f29 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-fed5796f29 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-fed5796f29 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-fed5796f29 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-fed5796f29 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-fed5796f29.

Kedarcidin retains full key GFTRTMUGNRZABD-IPBVOBEMSA-N, BGC0000081 compound 1 and source CID6477354. The exact selected object is the retained C53H60ClN3O16 small-molecule structure. The name does not expand this review to an associated protein, complex or unrepresented chromophore state.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-fed5796f29.

The stored graph has a nine-membered ring with two C#C bonds and an E C=C, an O-containing three-membered ring, an aromatic N ring bearing chlorine, a fused aromatic carbon system, and two separate saturated C5O candidate cycles. External O7 connects candidate-ring C5 to scaffold C8, and O34 connects scaffold C33 to candidate-ring C35. Ten C-O-C bridges include ring oxygens, ester, epoxide and aromatic ethers; they are not ten glycosidic links. The two disjoint C5O cycles support a bounded glycosylated-topology interpretation but not named sugars, anomeric configuration or complete natural identity. Ten listed ring rows include overlapping 17-membered cycles and are not ten independent biochemical rings. Fourteen tetrahedral centers remain unspecified in both forms; one E double bond is retained and one unspecified C=N appears after reconstruction. No CIP labels occur. The saved small-molecule graph does not demonstrate the identity, composition or function of a protein complex sharing the Kedarcidin name. Both neutral C53H60ClN3O16 forms agree in normalized InChI/key and counts. Stored SMILES has two carbonyls, one amide and one ester; reconstruction retains the ester and replaces the sole amide with terminal C49(O60H)=N55 (N H0). Canonical graphs differ and the one-way map is empty.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-fed5796f29.

Streptoalloteichus sp. ATCC 53650 NCBITaxon:756733 retains SOURCE_ASSERTION producer evidence. LOTUS genus NCBITaxon:2016 occurrences do not establish strain identity or upgrade that grade. BGC0000081 version5 is active/questionable/complete and names JX679499.1 with CLUSTER_DEMONSTRATED / Enzymatic assays, without coordinates. This locus grade does not establish every reaction or upgrade the SOURCE_ASSERTION producer claim.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-fed5796f29.

ENTRY PMID:23360970 retains its MIBiG locus/producer attribution. The two LOTUS rows cite DOI:10.1021/JA00046A071 and DOI:10.1039/C3MB25523A at occurrence grain. Both history events are seeder-attributed; these retained citations are not newly read papers.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-fed5796f29.

Two physical LOTUS rows share the same Streptoalloteichus genus NCBITaxon:2016 and structure Q15426249 but have distinct DOIs. They represent two attributed occurrence rows, not two producer taxa or newly verified independent studies. Six negative source frames provide no retained actual assay, target or ChEBI route. Enediyne topology and the compound name do not establish cytotoxicity, mechanism of action or a pharmacological target in this review.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-fed5796f29.

The two alkynes and adjacent alkene within the nine-membered ring support the Enediynes prediction; the aromatic N ring supports a pyridine-like structural feature. The two O-linked C5O candidate rings support bounded glycosylated topology, not named sugars or anomeric configuration. Cyclic peptides/Oligopeptides remain coarse model outputs: a single amide in this complex scaffold does not establish a conventional peptide sequence. NRPS&#124;PKS/Type I&#124;Iterative type I and Macrolides/Nicotinic acid alkaloids remain attributed annotations. The 3 computed pathway labels are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased classification.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-fed5796f29.

Whole owner/history, all nine saved query frames (4 positive rows/44 fields) and both complete saved molecular forms were personally read. The 44 actual input hashes and explicit ownership declarations were verified; this does not claim whole-corpus semantic reading. Five required local native commands passed, while full QC/OAK, live authority and independent primary verification remain unavailable. No selected graph/pathway/component or molecular-target root requires a maintained reader for this owner. Corrections belong in maintained inputs, implemented curation tables, extractors or the seeder; no record edit is proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2725-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kedarcidin.yaml; Complete plaintext and all curation_history entries | supports | Whole current owner/history was personally read; source assertions and curated mechanism annotations remain attributed. |
| bgc-2725-identity | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/4/owner_document/identifier; /records/4/owner_document/chemical_structure; /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status | supports | Kedarcidin retains full key GFTRTMUGNRZABD-IPBVOBEMSA-N, BGC0000081 compound 1 and source CID6477354. The exact selected object is the retained C53H60ClN3O16 small-molecule structure. The name does not expand this review to an associated protein, complex or unrepresented chromophore state. |
| bgc-2725-history | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/4/owner_document/curation_history | supports | ENTRY PMID:23360970 retains its MIBiG locus/producer attribution. The two LOTUS rows cite DOI:10.1021/JA00046A071 and DOI:10.1039/C3MB25523A at occurrence grain. Both history events are seeder-attributed; these retained citations are not newly read papers. |
| bgc-2725-provenance | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters | supports | Streptoalloteichus sp. ATCC 53650 NCBITaxon:756733 retains SOURCE_ASSERTION producer evidence. LOTUS genus NCBITaxon:2016 occurrences do not establish strain identity or upgrade that grade. BGC0000081 version5 is active/questionable/complete and names JX679499.1 with CLUSTER_DEMONSTRATED / Enzymatic assays, without coordinates. This locus grade does not establish every reaction or upgrade the SOURCE_ASSERTION producer claim. |
| bgc-2725-classification | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway; /records/4/owner_document/bgc_class | supports | The two alkynes and adjacent alkene within the nine-membered ring support the Enediynes prediction; the aromatic N ring supports a pyridine-like structural feature. The two O-linked C5O candidate rings support bounded glycosylated topology, not named sugars or anomeric configuration. Cyclic peptides/Oligopeptides remain coarse model outputs: a single amide in this complex scaffold does not establish a conventional peptide sequence. NRPS&#124;PKS/Type I&#124;Iterative type I and Macrolides/Nicotinic acid alkaloids remain attributed annotations. The 3 computed pathway labels are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased classification. |
| bgc-2725-roots | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/complete_root_keys; /contexts/7/declared_mechanism_roots_literal; /contexts/7/literal_bioactivities_root | context_only | Whole captured root set has no declared mechanism, component or measured bioactivity/target root. |
| bgc-2725-chemistry | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-DATA-001.json; /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons; /records/4/atom_correspondence; /records/4/literal_InChI_layers | supports | The stored graph has a nine-membered ring with two C#C bonds and an E C=C, an O-containing three-membered ring, an aromatic N ring bearing chlorine, a fused aromatic carbon system, and two separate saturated C5O candidate cycles. External O7 connects candidate-ring C5 to scaffold C8, and O34 connects scaffold C33 to candidate-ring C35. Ten C-O-C bridges include ring oxygens, ester, epoxide and aromatic ethers; they are not ten glycosidic links. The two disjoint C5O cycles support a bounded glycosylated-topology interpretation but not named sugars, anomeric configuration or complete natural identity. Ten listed ring rows include overlapping 17-membered cycles and are not ten independent biochemical rings. Fourteen tetrahedral centers remain unspecified in both forms; one E double bond is retained and one unspecified C=N appears after reconstruction. No CIP labels occur. The saved small-molecule graph does not demonstrate the identity, composition or function of a protein complex sharing the Kedarcidin name. Both neutral C53H60ClN3O16 forms agree in normalized InChI/key and counts. Stored SMILES has two carbonyls, one amide and one ester; reconstruction retains the ester and replaces the sole amide with terminal C49(O60H)=N55 (N H0). Canonical graphs differ and the one-way map is empty. |
| bgc-2725-molecular-reading | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-first-five-molecular-intake-reading-001.json; /records/4; /scope; /warnings_scope | supports | Complete saved atom/bond/ring/stereo/motif and mapping reading is independently attributed here; no new parse or primary source row credit. |
| bgc-2725-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /full_graph_identity_established | supports | ROOT accepted the one original twenty-form diagnostic; full graph identity remains false. |
| bgc-2725-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Exact original command and zero exit are retained without executing it again. |
| bgc-2725-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-original-001.stderr; Complete original stderr; four nonempty warning lines | context_only | Four omitted-undefined-stereo warnings are preserved globally without assigning them to any owner. |
| bgc-2725-intake | /private/tmp/npm-review-work/shared-next-batch273/intakes-001/2725-inspect-001.json; /targets; /source/inputs | supports | One exact target, 44 current input hashes and explicit maintained ownership declarations. |
| bgc-2725-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch273/root-intake-acceptance-001.json; /status; /accepted; /input_placements; /unique_input_paths | supports | ROOT accepted the ten actual canonical inspections with468 input placements/60 unique paths. |
| bgc-2725-plan | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-target-input-plan-001.json; /records/4 | supports | Current accepted exact input and direct-companion scope; presence alone confers no scientific proof. |
| bgc-2725-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch273/root-current273-source-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepted the original plan after attributed source reading. |
| bgc-2725-gates | /private/tmp/npm-native-checks/batch-273/root-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_snapshot | context_only | Five local native commands passed; full QC/OAK remain unavailable and queue entries are leads only. |
| bgc-2725-source-reading | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-assigned-source-reading-001.json; /contexts/7; /totals; /row_attribution | supports | Complete assigned saved dictionaries, physical rows and negative predicates were personally read; final molecular/reader meanings are supplied by the later actual artifacts. |
| bgc-2725-source-notes | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-scope-notes-001.json; /totals; /reading_reconciliation; /cautions | context_only | Disjoint source credit is23 BGC plus24 Support rows and zero Native/ROOT primary rows; this review uses its exact selected subset. |
| bgc-2725-taxonomy | /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-cached-taxonomy-reading-001.json; /scope; /interpretation; /context_interpretations | context_only | Eleven retained stanzas and fifteen exact routes were read, with no forward merge/nonorganism/unmatched route. Generic and strain labels remain separate. |
| bgc-2725-curation | /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Nine substantive tables/3422 rows yield zero lexical candidates and zero applicable exact predicates. Census-only extra tables confer no scientific input credit. |
| bgc-2725-assay-curation | /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json; /assay_scope | context_only | Six negative source frames provide no retained actual assay, target or ChEBI route. Enediyne topology and the compound name do not establish cytotoxicity, mechanism of action or a pharmacological target in this review. |
| bgc-2725-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines165-172: FindMolChiralCenters includeUnassigned | context_only | The MIBiG stereo_complete flag tests unassigned atom-centered chirality; reconstructed imidic-double geometry is a separate representation issue. |
| bgc-2725-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines295-306: choose_pathway | context_only | The 3 computed pathway labels are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased classification. |
| bgc-2725-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 108-108; raw record sha256 54563887f682f1ec8dc3057ca7be88bb9eb9eb98f687e738f992ef9dcf5cf630 | supports | All 25 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2725-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 2 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 2092-2092; raw record sha256 a3062a1bbfdf634a8ca900d60b59b058210f106586af133f0fa9bb4198185716 | supports | All 6 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2725-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 2093-2093; raw record sha256 396ee7aa9fec452949fbd655b49d09767144ea3fff37c9c7edc12a76efd21099 | supports | All 6 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2725-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 671-671; raw record sha256 d4fdd3174357968cd9c4bf35bffbc71e7f5075916c8e4cb41b8a2c98946a1214 | supports | All 7 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2725-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2725-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-273/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-273/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-273/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-273/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-273/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained source rows, grades and history were read; cited primary papers and live identity/taxonomy resources were not newly verified. Full QC and OAK remain unavailable under the no-outbound hold.
- Both neutral C53H60ClN3O16 forms agree in normalized InChI/key and counts. Stored SMILES has two carbonyls, one amide and one ester; reconstruction retains the ester and replaces the sole amide with terminal C49(O60H)=N55 (N H0). Canonical graphs differ and the one-way map is empty. Four original omitted-undefined-stereo warnings remain globally unassigned.
- Ring, amide, ester and C5O/bridge predicates provide local topology; they do not assign natural residues, all stereochemical details, enzyme functions or assay activity.
- The selected small-molecule representation does not establish a protein complex or named sugar/anomeric identities; fourteen tetrahedral centers are explicitly unassigned.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All current conclusions are scoped to this exact owner and its captured inputs; retained source status remains unchanged.
- No repair, source mutation, external request or new molecular parse was performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T152559Z-kedarcidin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: kedarcidin'
started_at: '2026-11-06T14:21:26.902206Z'
finished_at: '2026-11-06T15:25:59.137590Z'
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
summary: Kedarcidin retains an enediyne-containing small-molecule scaffold with two
  O-linked C5O candidate rings and fourteen unspecified tetrahedral centers. Source-strain,
  genus occurrence and locus grades remain distinct; named sugars, protein-complex
  identity and natural stereochemistry are not newly established.
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
  - path: data/natural_products/unclassified/kedarcidin.yaml
    sha256: 0d7d2c1f8a3d48e531c4f4fafddde9bac5b3d4492210af1387a07e9a66836fd5
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
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2725; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-fed5796f29
targets:
- target_id: naturalproductmech:mibig-fed5796f29
  path: data/natural_products/unclassified/kedarcidin.yaml
  label: kedarcidin
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
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnose273-001.py
    eef60eba394bf43b8ac3d4ed93ea024d47f231ec4dd051d571c8a865b7b78261 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
    92c35f8754f5db35ac73a3bf2f48f63b286fd6378e915892bbbabdd17fba19f7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored owner forms parsed in the original twenty-attempt diagnostic
    and share formula, charge, normalized InChI and declared full key.
  scope_note: Both neutral C53H60ClN3O16 forms agree in normalized InChI/key and counts.
    Stored SMILES has two carbonyls, one amide and one ester; reconstruction retains
    the ester and replaces the sole amide with terminal C49(O60H)=N55 (N H0). Canonical
    graphs differ and the one-way map is empty. Four original omitted-undefined-stereo
    warnings remain globally unassigned. No exact full graph, natural identity or
    primary biological certification follows.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-chemistry
  - bgc-2725-diagnostic-acceptance
  - bgc-2725-diagnostic-execution
  - bgc-2725-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  command: just validate-strict data/natural_products/unclassified/jamaicamide-c.yaml
    data/natural_products/unclassified/jessenipeptin.yaml data/natural_products/unclassified/keanumycin-a.yaml
    data/natural_products/unclassified/keanumycin-b.yaml data/natural_products/unclassified/kedarcidin.yaml
    data/natural_products/unclassified/kirromycin.yaml data/natural_products/unclassified/kitacinnamycin-a.yaml
    data/natural_products/unclassified/kitacinnamycin-b.yaml data/natural_products/unclassified/kitacinnamycin-c.yaml
    data/natural_products/unclassified/kitacinnamycin-d.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-273/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-fed5796f29
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-273/validate-all-001.tsv
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
  - naturalproductmech:mibig-fed5796f29
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
  - naturalproductmech:mibig-fed5796f29
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
  - naturalproductmech:mibig-fed5796f29
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-273/review-queue-001.tsv
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
  - naturalproductmech:mibig-fed5796f29
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2725-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kedarcidin.yaml
  locator: Complete plaintext and all curation_history entries
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Whole current owner/history was personally read; source assertions and
    curated mechanism annotations remain attributed.
  snapshot_sha256: 0d7d2c1f8a3d48e531c4f4fafddde9bac5b3d4492210af1387a07e9a66836fd5
- evidence_id: bgc-2725-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/4/owner_document/identifier; /records/4/owner_document/chemical_structure;
    /records/4/owner_document/source_concepts; /records/4/owner_document/grounding_status
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Kedarcidin retains full key GFTRTMUGNRZABD-IPBVOBEMSA-N, BGC0000081 compound
    1 and source CID6477354. The exact selected object is the retained C53H60ClN3O16
    small-molecule structure. The name does not expand this review to an associated
    protein, complex or unrepresented chromophore state.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2725-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/4/owner_document/curation_history
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ENTRY PMID:23360970 retains its MIBiG locus/producer attribution. The two
    LOTUS rows cite DOI:10.1021/JA00046A071 and DOI:10.1039/C3MB25523A at occurrence
    grain. Both history events are seeder-attributed; these retained citations are
    not newly read papers.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2725-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/4/owner_document/producer_organisms; /records/4/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Streptoalloteichus sp. ATCC 53650 NCBITaxon:756733 retains SOURCE_ASSERTION
    producer evidence. LOTUS genus NCBITaxon:2016 occurrences do not establish strain
    identity or upgrade that grade. BGC0000081 version5 is active/questionable/complete
    and names JX679499.1 with CLUSTER_DEMONSTRATED / Enzymatic assays, without coordinates.
    This locus grade does not establish every reaction or upgrade the SOURCE_ASSERTION
    producer claim.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2725-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/4/owner_document/np_classification; /records/4/owner_document/np_pathway;
    /records/4/owner_document/bgc_class
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'The two alkynes and adjacent alkene within the nine-membered ring support
    the Enediynes prediction; the aromatic N ring supports a pyridine-like structural
    feature. The two O-linked C5O candidate rings support bounded glycosylated topology,
    not named sugars or anomeric configuration. Cyclic peptides/Oligopeptides remain
    coarse model outputs: a single amide in this complex scaffold does not establish
    a conventional peptide sequence. NRPS|PKS/Type I|Iterative type I and Macrolides/Nicotinic
    acid alkaloids remain attributed annotations. The 3 computed pathway labels are
    retained while choose_pathway files this owner UNCLASSIFIED. This is consistent
    filing, not biological absence or an erased classification.'
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2725-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/complete_root_keys; /contexts/7/declared_mechanism_roots_literal;
    /contexts/7/literal_bioactivities_root
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Whole captured root set has no declared mechanism, component or measured
    bioactivity/target root.
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: Exact whole current owner root set; no activity or mechanism transfer
    from companion records.
- evidence_id: bgc-2725-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-DATA-001.json
  locator: /records/4/smiles/computed; /records/4/inchi/computed; /records/4/comparisons;
    /records/4/atom_correspondence; /records/4/literal_InChI_layers
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: The stored graph has a nine-membered ring with two C#C bonds and an E C=C,
    an O-containing three-membered ring, an aromatic N ring bearing chlorine, a fused
    aromatic carbon system, and two separate saturated C5O candidate cycles. External
    O7 connects candidate-ring C5 to scaffold C8, and O34 connects scaffold C33 to
    candidate-ring C35. Ten C-O-C bridges include ring oxygens, ester, epoxide and
    aromatic ethers; they are not ten glycosidic links. The two disjoint C5O cycles
    support a bounded glycosylated-topology interpretation but not named sugars, anomeric
    configuration or complete natural identity. Ten listed ring rows include overlapping
    17-membered cycles and are not ten independent biochemical rings. Fourteen tetrahedral
    centers remain unspecified in both forms; one E double bond is retained and one
    unspecified C=N appears after reconstruction. No CIP labels occur. The saved small-molecule
    graph does not demonstrate the identity, composition or function of a protein
    complex sharing the Kedarcidin name. Both neutral C53H60ClN3O16 forms agree in
    normalized InChI/key and counts. Stored SMILES has two carbonyls, one amide and
    one ester; reconstruction retains the ester and replaces the sole amide with terminal
    C49(O60H)=N55 (N H0). Canonical graphs differ and the one-way map is empty.
  snapshot_sha256: 0458568ea55f029d20f51b75bae21b1e1be822c1a62c95bf0764118349b3b024
- evidence_id: bgc-2725-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-first-five-molecular-intake-reading-001.json
  locator: /records/4; /scope; /warnings_scope
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif and mapping reading is independently
    attributed here; no new parse or primary source row credit.
  snapshot_sha256: 8f5b3160d02aef0a71df7a89cc19ec3ef32d0d6542c3c11fb881ae1334ba18c4
- evidence_id: bgc-2725-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /full_graph_identity_established
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ROOT accepted the one original twenty-form diagnostic; full graph identity
    remains false.
  snapshot_sha256: 4958a99eeb26cfffbd8c333ef1c3ee720875ff468d51026a3b08590c9cfce39e
- evidence_id: bgc-2725-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Exact original command and zero exit are retained without executing it
    again.
  snapshot_sha256: 19f0309e060cd114e107dee98d301154b18130d166db4b12f2f1fc1ecce48cf6
- evidence_id: bgc-2725-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr; four nonempty warning lines
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Four omitted-undefined-stereo warnings are preserved globally without assigning
    them to any owner.
  snapshot_sha256: 1983ffbdc45b00739a943c2031ce64f65d27e1b5c9e3a058936e4d4ec2ddc57a
- evidence_id: bgc-2725-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/intakes-001/2725-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: One exact target, 44 current input hashes and explicit maintained ownership
    declarations.
  snapshot_sha256: 3cca3da35e69b35fc0575765e588cdabf56c887ea4181f7634c29a499412799d
- evidence_id: bgc-2725-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/root-intake-acceptance-001.json
  locator: /status; /accepted; /input_placements; /unique_input_paths
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ROOT accepted the ten actual canonical inspections with468 input placements/60
    unique paths.
  snapshot_sha256: a68ca1cf0788a294ae06506515c973dcebe06ce4d0d280cdbce713be0a0f2278
- evidence_id: bgc-2725-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-target-input-plan-001.json
  locator: /records/4
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Current accepted exact input and direct-companion scope; presence alone
    confers no scientific proof.
  snapshot_sha256: 37a2529c76339bea20b2c862c7a09ce11dd909d4a69623ba4f8914026c771cf4
- evidence_id: bgc-2725-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/root-current273-source-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ROOT accepted the original plan after attributed source reading.
  snapshot_sha256: 678b0919f00212e2f1140491aa5ce980685261662e4f336d19fb01fb46d1ed26
- evidence_id: bgc-2725-gates
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/root-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_snapshot
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Five local native commands passed; full QC/OAK remain unavailable and queue
    entries are leads only.
  snapshot_sha256: a98bb4066024289ac97d3274aadccfb96d4d4068f9a6168c3ba9e2ff7b39ca6b
- evidence_id: bgc-2725-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-assigned-source-reading-001.json
  locator: /contexts/7; /totals; /row_attribution
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Complete assigned saved dictionaries, physical rows and negative predicates
    were personally read; final molecular/reader meanings are supplied by the later
    actual artifacts.
  snapshot_sha256: 3b530e67d54edcc3b5a56f3ca7bc7d25e642f8d44e73d5db22b00202a1a0d175
- evidence_id: bgc-2725-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /cautions
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Disjoint source credit is23 BGC plus24 Support rows and zero Native/ROOT
    primary rows; this review uses its exact selected subset.
  snapshot_sha256: 7d3af448ee3538d1c078e1f22263097ac13a4d83d3f4192854724c31d6a8eb86
- evidence_id: bgc-2725-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-cached-taxonomy-reading-001.json
  locator: /scope; /interpretation; /context_interpretations
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Eleven retained stanzas and fifteen exact routes were read, with no forward
    merge/nonorganism/unmatched route. Generic and strain labels remain separate.
  snapshot_sha256: 6f4cd7f16a6f8b2e82152f6a274f5b9b139808f8a7845e8912ac4e4538bb7b26
  search_scope: Current cached source labels and exact route predicates only; no fresh
    rank, lineage, strain or OAK result.
- evidence_id: bgc-2725-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Nine substantive tables/3422 rows yield zero lexical candidates and zero
    applicable exact predicates. Census-only extra tables confer no scientific input
    credit.
  snapshot_sha256: 61175b3c187b89ef171b28e839d743a6f7e58bddaf5e67dfb64864d62653c966
  search_scope: Current273 bounded identity/source tokens and retained implemented
    predicates; no decision applied.
- evidence_id: bgc-2725-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Six negative source frames provide no retained actual assay, target or
    ChEBI route. Enediyne topology and the compound name do not establish cytotoxicity,
    mechanism of action or a pharmacological target in this review.
  snapshot_sha256: 61175b3c187b89ef171b28e839d743a6f7e58bddaf5e67dfb64864d62653c966
  search_scope: Zero actual AIDs; batch has two blank sentinels, Jessenipeptin and
    Kirromycin. Exact fifteen exclusion decisions cannot transfer without their full
    predicates.
- evidence_id: bgc-2725-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines165-172: FindMolChiralCenters includeUnassigned'
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: The MIBiG stereo_complete flag tests unassigned atom-centered chirality;
    reconstructed imidic-double geometry is a separate representation issue.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2725-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines295-306: choose_pathway'
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: The 3 computed pathway labels are retained while choose_pathway files this
    owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased
    classification.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2725-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2725-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 108-108; raw record sha256 54563887f682f1ec8dc3057ca7be88bb9eb9eb98f687e738f992ef9dcf5cf630
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 25 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2725-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kedarcidin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GFTRTMUGNRZABD-IPBVOBEMSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2725-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 2 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2725-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 2092-2092; raw record sha256 a3062a1bbfdf634a8ca900d60b59b058210f106586af133f0fa9bb4198185716
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 6 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2725-row-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 2093-2093; raw record sha256 396ee7aa9fec452949fbd655b49d09767144ea3fff37c9c7edc12a76efd21099
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 6 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2725-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements; every
    returned field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kedarcidin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GFTRTMUGNRZABD-IPBVOBEMSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2725-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2725-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 671-671; raw record sha256 d4fdd3174357968cd9c4bf35bffbc71e7f5075916c8e4cb41b8a2c98946a1214
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 7 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2725-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kedarcidin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GFTRTMUGNRZABD-IPBVOBEMSA-N",
    "table": "pubchem_bioassay"}'
- evidence_id: bgc-2725-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kedarcidin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GFTRTMUGNRZABD-IPBVOBEMSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2725-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements;
    every returned field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kedarcidin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "GFTRTMUGNRZABD-IPBVOBEMSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2725-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/kedarcidin.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:27:07.176543Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 43fcdede3e42b4a8cbfdd8d20ede685766c071c094bfffde0b3540840ec32dd5
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:27:32.867288Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 680d286e5b6524c522d17e6143f9f5738389cdf8d006a5de216a5266c72fe77f
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:27:53.047300Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:28:27.995571Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:28:40.232102Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cd75bfb4b51e32cf7d9e268e520b8869e68b5463e2da44f5b1e2f6c68ee26d09
assessments:
- assessment_id: bgc-2725-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: Kedarcidin retains full key GFTRTMUGNRZABD-IPBVOBEMSA-N, BGC0000081 compound
    1 and source CID6477354. The exact selected object is the retained C53H60ClN3O16
    small-molecule structure. The name does not expand this review to an associated
    protein, complex or unrepresented chromophore state.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-identity
  - bgc-2725-chemistry
  - bgc-2725-query-mibig_compounds
  - bgc-2725-query-chebi_structures
  - bgc-2725-plan
  - bgc-2725-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: GFTRTMUGNRZABD-IPBVOBEMSA-N
    evidence_ids:
    - bgc-2725-identity
    - bgc-2725-chemistry
    - bgc-2725-query-mibig_compounds
    - bgc-2725-query-chebi_structures
    - bgc-2725-plan
    - bgc-2725-row-mibig_compounds-0
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: Kedarcidin retains full key GFTRTMUGNRZABD-IPBVOBEMSA-N, BGC0000081 compound
      1 and source CID6477354. The exact selected object is the retained C53H60ClN3O16
      small-molecule structure. The name does not expand this review to an associated
      protein, complex or unrepresented chromophore state.
    evidence_ids:
    - bgc-2725-identity
    - bgc-2725-chemistry
    - bgc-2725-query-mibig_compounds
    - bgc-2725-query-chebi_structures
    - bgc-2725-plan
    - bgc-2725-row-mibig_compounds-0
- assessment_id: bgc-2725-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: The stored graph has a nine-membered ring with two C#C bonds and an E C=C,
    an O-containing three-membered ring, an aromatic N ring bearing chlorine, a fused
    aromatic carbon system, and two separate saturated C5O candidate cycles. External
    O7 connects candidate-ring C5 to scaffold C8, and O34 connects scaffold C33 to
    candidate-ring C35. Ten C-O-C bridges include ring oxygens, ester, epoxide and
    aromatic ethers; they are not ten glycosidic links. The two disjoint C5O cycles
    support a bounded glycosylated-topology interpretation but not named sugars, anomeric
    configuration or complete natural identity. Ten listed ring rows include overlapping
    17-membered cycles and are not ten independent biochemical rings. Fourteen tetrahedral
    centers remain unspecified in both forms; one E double bond is retained and one
    unspecified C=N appears after reconstruction. No CIP labels occur. The saved small-molecule
    graph does not demonstrate the identity, composition or function of a protein
    complex sharing the Kedarcidin name. Both neutral C53H60ClN3O16 forms agree in
    normalized InChI/key and counts. Stored SMILES has two carbonyls, one amide and
    one ester; reconstruction retains the ester and replaces the sole amide with terminal
    C49(O60H)=N55 (N H0). Canonical graphs differ and the one-way map is empty.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-identity
  - bgc-2725-chemistry
  - bgc-2725-molecular-reading
  - bgc-2725-diagnostic-acceptance
  - bgc-2725-diagnostic-stderr
  - bgc-2725-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Fourteen tetrahedral centers remain unspecified in both forms; one E double
      bond is retained and one unspecified C=N appears after reconstruction. No CIP
      labels occur. The saved small-molecule graph does not demonstrate the identity,
      composition or function of a protein complex sharing the Kedarcidin name.
    evidence_ids:
    - bgc-2725-identity
    - bgc-2725-chemistry
    - bgc-2725-molecular-reading
    - bgc-2725-diagnostic-acceptance
    - bgc-2725-diagnostic-stderr
    - bgc-2725-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: Both neutral C53H60ClN3O16 forms agree in normalized InChI/key and counts.
      Stored SMILES has two carbonyls, one amide and one ester; reconstruction retains
      the ester and replaces the sole amide with terminal C49(O60H)=N55 (N H0). Canonical
      graphs differ and the one-way map is empty.
    evidence_ids:
    - bgc-2725-identity
    - bgc-2725-chemistry
    - bgc-2725-molecular-reading
    - bgc-2725-diagnostic-acceptance
    - bgc-2725-diagnostic-stderr
    - bgc-2725-stereo-policy
- assessment_id: bgc-2725-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: Streptoalloteichus sp. ATCC 53650 NCBITaxon:756733 retains SOURCE_ASSERTION
    producer evidence. LOTUS genus NCBITaxon:2016 occurrences do not establish strain
    identity or upgrade that grade. BGC0000081 version5 is active/questionable/complete
    and names JX679499.1 with CLUSTER_DEMONSTRATED / Enzymatic assays, without coordinates.
    This locus grade does not establish every reaction or upgrade the SOURCE_ASSERTION
    producer claim.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-provenance
  - bgc-2725-query-mibig_compounds
  - bgc-2725-taxonomy
  - bgc-2725-curation
  - bgc-2725-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: Streptoalloteichus sp. ATCC 53650 NCBITaxon:756733 retains SOURCE_ASSERTION
      producer evidence. LOTUS genus NCBITaxon:2016 occurrences do not establish strain
      identity or upgrade that grade.
    evidence_ids:
    - bgc-2725-provenance
    - bgc-2725-query-mibig_compounds
    - bgc-2725-taxonomy
    - bgc-2725-curation
    - bgc-2725-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: Streptoalloteichus sp. ATCC 53650 NCBITaxon:756733 retains SOURCE_ASSERTION
      producer evidence. LOTUS genus NCBITaxon:2016 occurrences do not establish strain
      identity or upgrade that grade.
    evidence_ids:
    - bgc-2725-provenance
    - bgc-2725-query-mibig_compounds
    - bgc-2725-taxonomy
    - bgc-2725-curation
    - bgc-2725-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0000081 version5 is active/questionable/complete and names JX679499.1
      with CLUSTER_DEMONSTRATED / Enzymatic assays, without coordinates. This locus
      grade does not establish every reaction or upgrade the SOURCE_ASSERTION producer
      claim.
    evidence_ids:
    - bgc-2725-provenance
    - bgc-2725-query-mibig_compounds
    - bgc-2725-taxonomy
    - bgc-2725-curation
    - bgc-2725-row-mibig_compounds-0
- assessment_id: bgc-2725-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: ENTRY PMID:23360970 retains its MIBiG locus/producer attribution. The two
    LOTUS rows cite DOI:10.1021/JA00046A071 and DOI:10.1039/C3MB25523A at occurrence
    grain. Both history events are seeder-attributed; these retained citations are
    not newly read papers.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-history
  - bgc-2725-provenance
  - bgc-2725-source-reading
  - bgc-2725-query-mibig_compounds
  - bgc-2725-row-mibig_compounds-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: ENTRY PMID:23360970 retains its MIBiG locus/producer attribution. The two
      LOTUS rows cite DOI:10.1021/JA00046A071 and DOI:10.1039/C3MB25523A at occurrence
      grain. Both history events are seeder-attributed; these retained citations are
      not newly read papers.
    evidence_ids:
    - bgc-2725-history
    - bgc-2725-provenance
    - bgc-2725-source-reading
    - bgc-2725-query-mibig_compounds
    - bgc-2725-row-mibig_compounds-0
- assessment_id: bgc-2725-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: Two physical LOTUS rows share the same Streptoalloteichus genus NCBITaxon:2016
    and structure Q15426249 but have distinct DOIs. They represent two attributed
    occurrence rows, not two producer taxa or newly verified independent studies.
    Six negative source frames provide no retained actual assay, target or ChEBI route.
    Enediyne topology and the compound name do not establish cytotoxicity, mechanism
    of action or a pharmacological target in this review.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-roots
  - bgc-2725-query-lotus_occurrences
  - bgc-2725-query-cyanometdb_occurrences
  - bgc-2725-query-pubchem_bioassay
  - bgc-2725-query-bindingdb_targets
  - bgc-2725-query-antibioticmech_inchikeys
  - bgc-2725-assay-curation
  - bgc-2725-row-lotus_occurrences-0
  - bgc-2725-row-lotus_occurrences-1
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: Two physical LOTUS rows share the same Streptoalloteichus genus NCBITaxon:2016
      and structure Q15426249 but have distinct DOIs. They represent two attributed
      occurrence rows, not two producer taxa or newly verified independent studies.
    evidence_ids:
    - bgc-2725-roots
    - bgc-2725-query-lotus_occurrences
    - bgc-2725-query-cyanometdb_occurrences
    - bgc-2725-query-pubchem_bioassay
    - bgc-2725-query-bindingdb_targets
    - bgc-2725-query-antibioticmech_inchikeys
    - bgc-2725-assay-curation
    - bgc-2725-row-lotus_occurrences-0
    - bgc-2725-row-lotus_occurrences-1
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: Six negative source frames provide no retained actual assay, target or
      ChEBI route. Enediyne topology and the compound name do not establish cytotoxicity,
      mechanism of action or a pharmacological target in this review.
    evidence_ids:
    - bgc-2725-roots
    - bgc-2725-query-lotus_occurrences
    - bgc-2725-query-cyanometdb_occurrences
    - bgc-2725-query-pubchem_bioassay
    - bgc-2725-query-bindingdb_targets
    - bgc-2725-query-antibioticmech_inchikeys
    - bgc-2725-assay-curation
    - bgc-2725-row-lotus_occurrences-0
    - bgc-2725-row-lotus_occurrences-1
- assessment_id: bgc-2725-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: 'The two alkynes and adjacent alkene within the nine-membered ring support
    the Enediynes prediction; the aromatic N ring supports a pyridine-like structural
    feature. The two O-linked C5O candidate rings support bounded glycosylated topology,
    not named sugars or anomeric configuration. Cyclic peptides/Oligopeptides remain
    coarse model outputs: a single amide in this complex scaffold does not establish
    a conventional peptide sequence. NRPS|PKS/Type I|Iterative type I and Macrolides/Nicotinic
    acid alkaloids remain attributed annotations. The 3 computed pathway labels are
    retained while choose_pathway files this owner UNCLASSIFIED. This is consistent
    filing, not biological absence or an erased classification.'
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-classification
  - bgc-2725-chemistry
  - bgc-2725-query-npclassifier
  - bgc-2725-query-mibig_compounds
  - bgc-2725-filing-policy
  - bgc-2725-row-npclassifier-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: 'The two alkynes and adjacent alkene within the nine-membered ring support
      the Enediynes prediction; the aromatic N ring supports a pyridine-like structural
      feature. The two O-linked C5O candidate rings support bounded glycosylated topology,
      not named sugars or anomeric configuration. Cyclic peptides/Oligopeptides remain
      coarse model outputs: a single amide in this complex scaffold does not establish
      a conventional peptide sequence. NRPS|PKS/Type I|Iterative type I and Macrolides/Nicotinic
      acid alkaloids remain attributed annotations. The 3 computed pathway labels
      are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent
      filing, not biological absence or an erased classification.'
    evidence_ids:
    - bgc-2725-classification
    - bgc-2725-chemistry
    - bgc-2725-query-npclassifier
    - bgc-2725-query-mibig_compounds
    - bgc-2725-filing-policy
    - bgc-2725-row-npclassifier-0
- assessment_id: bgc-2725-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Whole owner/history, all nine saved query frames (4 positive rows/44 fields)
    and both complete saved molecular forms were personally read. The 44 actual input
    hashes and explicit ownership declarations were verified; this does not claim
    whole-corpus semantic reading. Five required local native commands passed, while
    full QC/OAK, live authority and independent primary verification remain unavailable.
    No selected graph/pathway/component or molecular-target root requires a maintained
    reader for this owner. Corrections belong in maintained inputs, implemented curation
    tables, extractors or the seeder; no record edit is proposed.
  target_ids:
  - naturalproductmech:mibig-fed5796f29
  evidence_ids:
  - bgc-2725-owner
  - bgc-2725-history
  - bgc-2725-intake
  - bgc-2725-intake-acceptance
  - bgc-2725-plan
  - bgc-2725-plan-acceptance
  - bgc-2725-gates
  - bgc-2725-source-reading
  - bgc-2725-source-notes
  - bgc-2725-molecular-reading
  - bgc-2725-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Whole owner/history, all nine saved query frames (4 positive rows/44 fields)
      and both complete saved molecular forms were personally read. The 44 actual
      input hashes and explicit ownership declarations were verified; this does not
      claim whole-corpus semantic reading. Five required local native commands passed,
      while full QC/OAK, live authority and independent primary verification remain
      unavailable. No selected graph/pathway/component or molecular-target root requires
      a maintained reader for this owner. Corrections belong in maintained inputs,
      implemented curation tables, extractors or the seeder; no record edit is proposed.
    evidence_ids:
    - bgc-2725-owner
    - bgc-2725-history
    - bgc-2725-intake
    - bgc-2725-intake-acceptance
    - bgc-2725-plan
    - bgc-2725-plan-acceptance
    - bgc-2725-gates
    - bgc-2725-source-reading
    - bgc-2725-source-notes
    - bgc-2725-molecular-reading
    - bgc-2725-roots
findings: []
actions: []
limitations:
- Retained source rows, grades and history were read; cited primary papers and live
  identity/taxonomy resources were not newly verified. Full QC and OAK remain unavailable
  under the no-outbound hold.
- Both neutral C53H60ClN3O16 forms agree in normalized InChI/key and counts. Stored
  SMILES has two carbonyls, one amide and one ester; reconstruction retains the ester
  and replaces the sole amide with terminal C49(O60H)=N55 (N H0). Canonical graphs
  differ and the one-way map is empty. Four original omitted-undefined-stereo warnings
  remain globally unassigned.
- Ring, amide, ester and C5O/bridge predicates provide local topology; they do not
  assign natural residues, all stereochemical details, enzyme functions or assay activity.
- The selected small-molecule representation does not establish a protein complex
  or named sugar/anomeric identities; fourteen tetrahedral centers are explicitly
  unassigned.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- All current conclusions are scoped to this exact owner and its captured inputs;
  retained source status remains unchanged.
- No repair, source mutation, external request or new molecular parse was performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-273
```
