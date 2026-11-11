# Local evidence review: frontalamide A

- Review: 20261106T044856Z-frontalamide-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T04:05:40.061645Z
- Finished UTC: 2026-11-06T04:48:56.856845Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Frontalamide A preserves two source entries with different producer and locus grades, while their shared-structure discussion stays OPEN. Local tables support a macrolactam and tetramic region, not an ester-based reading of the computed Macrolides label. Review is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2658; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-09c929043b | data/natural_products/unclassified/frontalamide-a.yaml | generated | frontalamide A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-09c929043b | The original diagnostic parsed both stored forms and preserved all actual comparison flags. Formula, charge, StandardInChI and full key agree within this owner. |
| strict_ten | passed | True | naturalproductmech:mibig-09c929043b | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-09c929043b | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-09c929043b | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-09c929043b | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-09c929043b | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-09c929043b | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-09c929043b | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-09c929043b | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-09c929043b.

Two exact MIBiG source concepts map to the retained full key and owner: BGC0000996 version 5 and BGC0002509 version 3. The OPEN shared-structure discussion remains unresolved; within-owner normalization does not establish that the two source entries identify the same natural compound. The written NPAtlas and PubChem xrefs are retained mappings, and no exact ChEBI structure row was found in the saved query. Both saved forms regenerate the declared StandardInChI and full key, supporting stored mapping without independent natural-identity verification.

### Stored forms and stereochemistry

representation: unknown. Targets: naturalproductmech:mibig-09c929043b.

Both neutral C29H36N2O7 forms contain 38 atoms and 42 bonds. Five reported rings have sizes 5, 5, 16, 5 and 6. The original has four carbonyls, two amides and no ester; the 16-membered ring contains an amide linkage, while a separate five-membered nitrogen ring contains the other amide. Reconstruction retains two carbonyls and presents two C(OH)=N sites with terminal hydroxyl oxygens. Eight specified and two unspecified tetrahedral centers persist, as do one Z and one E alkene. The original enolic C=C is potential Unspecified/STEREONONE; the corresponding reconstructed entry is Unknown/STEREOANY. The new macrocyclic C=N is potential Unspecified; the new five-membered-ring C=N is not listed as potential double stereo. Thus two imidic motifs do not mean two added unspecified-double entries. Local CIP labels and atom indices remain form-specific because the saved map is empty. Formula, charge, StandardInChI and full key agree, but both canonical comparisons are false. This bounded tautomer-consistent correspondence neither proves full fixed-form identity nor resolves the OPEN cross-entry identity discussion. Four original undefined-stereo warnings remain globally unassigned; they are not attached to an individual record.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-09c929043b.

BGC0000996 retains Streptomyces sp. SPB78 (NCBITaxon:591157), BGC_CHARACTERIZED and a separately CLUSTER_DEMONSTRATED link from knock-out studies at GG657742.1 positions 4,892,742–4,909,316. Its classes are NRPS&#124;PKS and subclasses Type I&#124;Iterative type I; completeness is partial. BGC0002509 instead retains Streptomyces sp. (1931), SOURCE_ASSERTION and CLUSTER_UNSTATED at MN817126.1 positions 1–22,084, with blank methods and unknown completeness. Its class is NRPS only and subclass Type I. Both entries have questionable quality. The stronger 0996 grades are not transferred to 2509.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-09c929043b.

BGC0000996 carries ENTRY-level PMID:20547882; BGC0002509 carries ENTRY-level DOI:10.6023/cjoc201912017. LOTUS retains DOI:10.1073/PNAS.1001513107. These source-specific placements and all history remain intact; publication identity and independence are not newly established.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-09c929043b.

The sole LOTUS row names genus-level Streptomyces (NCBITaxon:1883), distinct from the two source-specific producer taxon assertions. One blank-AID sentinel for CID101515037 provides no assay result. BindingDB, related-corpus and written activity/target roots are absent within the saved scope. Shared-BGC companions do not confer activity, producer grades or mechanism.

### Classification and saved topology

consistency: unknown. Targets: naturalproductmech:mibig-09c929043b.

The original 16-membered ring contains an amide rather than an ester, and the separate five-membered nitrogen ring has the local tetramic carbonyl arrangement. This supports bounded macrolactam and tetramic-region topology. The computed Macrolides superclass is retained as model provenance, without claiming a macrolactone or treating the label as proof of an ester. The Macrocyclic tetramic acids family has local topological support, while complete model-family and biosynthetic applicability remain qualified.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-09c929043b.

The whole selected owner/history, complete retained source payloads and negative query bounds, both saved molecular forms and actual intake claims have been read. Current input hashes and ownership declarations match the accepted plan. Five local gates passed, but full QC and OAK remain unavailable and no live authority was consulted. No maintained reader applies. Completion remains partial; positive assessments concern retained mapping, source-grade fidelity and bounded local topology.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2658-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/frontalamide-a.yaml; Whole current plaintext including every curation_history entry | supports | Complete personally read selected owner and history; retained contents do not imply fresh source access. |
| support-2658-capture | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete actual captured owner, including all written claims and exact present/absent mechanism and component roots. |
| support-2658-grounding-owner | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/label; /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes | supports | Exact owner-local identifier, structure and grounding/definition fields; retained mapping is distinct from natural-identity proof. |
| support-2658-provenance-owner | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/producer_taxon_groups; /records/7/owner_document/bgc_class | supports | Stored producer and locus grades, coordinates and citations are preserved as distinct assertions. |
| support-2658-citations-history | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document/source_concepts; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/curation_history | supports | Exact retained source concepts, citation grain and complete seeding history; no primary-paper reopening. |
| support-2658-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups; /records/7/owner_document/xrefs | supports | Owner-local occurrence and identifier placements; no causal production inference. |
| support-2658-activity-owner | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete owner has no written bioactivity or molecular-target roots; bounded retained absence only. |
| support-2658-classification-owner | /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/biosynthesis_origin | supports | Owner-local filing and computed classifier values; source class/subclass and local topology are separately evidenced. |
| support-2658-intake | /private/tmp/npm-review-work/shared-next-batch266/intakes-001/2658-inspect-001.json; /status; /source; /targets | supports | Actual inspection-only hashes and target ownership declarations; no scientific reading of entire captured corpus files is implied. |
| support-2658-intake-execution | /private/tmp/npm-review-work/shared-next-batch266/intakes-001/2658-inspect-execution-001.json; /exit_code; /command; /actual_environment; /stdout; /stderr | supports | Original canonical inspection exit 0 and empty stderr for this owner. |
| support-2658-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch266/root-current266-intake-acceptance-001.json; /accepted; /status; /summary; /source_plan_acceptance; /verification | supports | ROOT accepted all ten original inspections and the exact 466 input placements across 66 paths. |
| support-2658-direct-contexts | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates; /records/7/identity_comparison_paths; /records/7/additional_context_paths; /records/7/additional_context_roles; /records/7/reader_implementation_paths; /records/7/proposed_input_paths; /records/7/proposed_input_count | supports | Exact owner-local companion, seven diagnostic/implementation roles and literal reader implementation inputs where applicable. Captured input presence is distinct from positive scientific evidence. |
| support-2658-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch266/root-current266-source-plan-acceptance-001.json; /status; /plan; /verification | supports | ROOT acceptance of the one original operative source plan. |
| support-2658-source-reading | /private/tmp/npm-review-work/shared-next-batch266-tentative/support-prep/support-current266-assigned-source-reading-001.json; /contexts/9 | supports | Personally read every saved frame and full positive row dictionary for this owner; complete companion attribution remains separately scoped. |
| support-2658-raw-reading | /private/tmp/npm-review-work/shared-next-batch266-tentative/support-prep/support-current266-last-five-whole-owner-reading-001.json; /records/2 | supports | Support personally read this whole raw owner and all history entries; no primary source was reopened. |
| support-2658-source-notes | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Attributed reading reconciliation preserves 35 BGC plus 50 Support row placements and zero Native primary row credit; negative and blank boundaries remain explicit. |
| support-2658-taxonomy | /private/tmp/npm-review-work/shared-next-batch266-tentative/native-prep/native-current266-cached-taxonomy-reading-001.json; /context_interpretations/19; /interpretation; /counts | supports | Owner-local cached labels/synonyms and retained routes; no fresh rank, lineage or production authority. |
| support-2658-curation-scope | /private/tmp/npm-review-work/shared-next-batch266-tentative/native-prep/native-current266-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /interpretation; /implementation_scope | supports | Exact implemented-curation and source-identity resolution; lexical matches do not establish an applicable correction or exclusion for this owner. |
| support-2658-chemistry | /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/diagnostic-DATA-001.json; /records/7 | supports | Complete two-form saved molecular tables, scalars, stereo, motifs and comparisons for this owner; normalized equality is not full fixed-form or natural identity proof. |
| support-2658-molecular-reading | /private/tmp/npm-review-work/shared-next-batch266-tentative/support-prep/support-current266-last-five-molecular-intake-reading-001.json; /records/2 | supports | Support personally read every saved atom/bond field and all ring, stereo and motif fields for both forms; no new molecular parse. |
| support-2658-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/root-diagnostic-result-acceptance-001.json; /accepted; /DATA; /execution; /verification; /interpretation_limits | supports | ROOT acceptance of the one original diagnostic, preserving false comparisons and global warning scope. |
| support-2658-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/diagnostic-execution-001.json; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0 with no retries; four undefined-stereo warnings remain global and are not assigned to particular owners. |
| support-2658-stereo-implementation | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–172 | supports | The retained stereo_complete calculation uses FindMolChiralCenters with includeUnassigned=True and useLegacyImplementation=False on source SMILES; reconstructed double-bond potential stereo is outside that calculation. |
| support-2658-native-gates | /private/tmp/npm-review-work/shared-next-batch266/root-native-gates-acceptance-001.json; /accepted; /checks_passed; /all_native_gates_passed; /unavailable_required_gates; /complete_selected_queue_rows | supports | Five local gates passed; full QC and OAK remain unavailable. Queue rows are leads, not scientific verdicts. |
| support-2658-reader-applicability | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | All ten selected owners have no literal mechanism or component roots; no maintained reader applies. |
| support-2658-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame with all 2 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/mibig_compounds/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2658-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/lotus_occurrences/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2658-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/npclassifier/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2658-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/pubchem_bioassay/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2658-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2658-taxon-query-scope | /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json; /contexts/19/source_scope_inventory/source_taxa; /contexts/19/source_scope_inventory/forward_taxon_merge_matches; /contexts/19/source_scope_inventory/nonorganism_matches | supports | Exact owner-local source taxon IDs and retained positive/negative diagnostic routes; companion route placements are not additional independent decisions. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-266/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-266/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-266/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-266/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-266/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained owners and saved source payloads only; no fresh primary-paper, taxonomy, sequence or external identifier resolution.
- Friulimicin C/D and Frontalamide A/B have unequal canonical representations and empty saved maps. Fujikurin B has a complete limited map, but all five full-identity flags remain false and unresolved stereochemistry is preserved.
- Four original undefined-stereo warnings remain globally unassigned. Full QC and OAK are unavailable; source grades, OPEN discussions and computed-family limitations remain explicit.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete selected owners/history and ten saved molecular forms: 552 atom rows, 576 bond rows and 34 reported ring rows. Selected source coverage is 45 frames, 19 positive placements and 253 fields; the primary partition including eight companions is 117 frames, 50 placements and 620 fields. Other contexts retain separate primary attribution.
- Verified 234 actual input placements across 56 paths and their target ownership declarations. Input hashes do not imply scientific reading of whole corpus files. No generated record, native status or history was edited, and no outbound request was sent.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T044856Z-frontalamide-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: frontalamide A'
started_at: '2026-11-06T04:05:40.061645Z'
finished_at: '2026-11-06T04:48:56.856845Z'
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
summary: Frontalamide A preserves two source entries with different producer and locus
  grades, while their shared-structure discussion stays OPEN. Local tables support
  a macrolactam and tetramic region, not an ester-based reading of the computed Macrolides
  label. Review is partial.
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
  - path: data/natural_products/unclassified/capsimycin.yaml
    sha256: 3cc5878ae15000c984164edd5a16a53e528913346554fa75ac7243cb5560093c
    role: context
  - path: data/natural_products/unclassified/clifednamide-a.yaml
    sha256: 443ecbef7e9c595a5401b48e006958f8ddb456744ee99c4950ca1dd7a55cab74
    role: context
  - path: data/natural_products/unclassified/combamide-a.yaml
    sha256: 26fc2eb57f4a41da87e98ac7d4427b15b5e403911c4682656a4de94e00dbf98e
    role: context
  - path: data/natural_products/unclassified/frontalamide-a.yaml
    sha256: cc2f0d9ea13c0fa5e44679634ea8711d3a85a6543430a09aa621de1765453b25
    role: target
  - path: data/natural_products/unclassified/frontalamide-b.yaml
    sha256: bd720f1d4dae473fb459d5c145803ad3bf888c8ede91ae868216c46d2ea40c22
    role: context
  - path: data/natural_products/unclassified/montamide-a.yaml
    sha256: 9c47ee9d30a974645cedc4beb4db3b9724da28a1e6fe0b922e1221f7da46e038
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2658; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-09c929043b
targets:
- target_id: naturalproductmech:mibig-09c929043b
  path: data/natural_products/unclassified/frontalamide-a.yaml
  label: frontalamide A
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/diagnose266-001.py
    e46ebf46caa5d67b93140ebdfb540fdc1e1c372d0f0ea97ce62d1710c4eba2af 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
    fa98eca1b1e385f78f104dc0bb8248126a9b5c7ac974744a29f423c0758ad4d6
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The original diagnostic parsed both stored forms and preserved all actual
    comparison flags. Formula, charge, StandardInChI and full key agree within this
    owner.
  scope_note: Original shared twenty-form execution; no rerun. False canonical comparisons,
    empty maps and unspecified stereochemistry remain explicit. This passed execution
    check does not certify full graph or natural identity.
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-chemistry
  - support-2658-diagnostic-acceptance
  - support-2658-diagnostic-execution
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-09c929043b
  command: just validate-strict data/natural_products/unclassified/fr900359-2.yaml
    data/natural_products/unclassified/fr900359.yaml data/natural_products/unclassified/frankobactin-a2.yaml
    data/natural_products/unclassified/frankobactin-b2.yaml data/natural_products/unclassified/frederiksenibactin.yaml
    data/natural_products/unclassified/friulimicin-c.yaml data/natural_products/unclassified/friulimicin-d.yaml
    data/natural_products/unclassified/frontalamide-a.yaml data/natural_products/unclassified/frontalamide-b.yaml
    data/natural_products/unclassified/fujikurin-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-266/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-09c929043b
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-266/validate-all-001.tsv
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
  - naturalproductmech:mibig-09c929043b
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
  - naturalproductmech:mibig-09c929043b
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
  - naturalproductmech:mibig-09c929043b
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-266/review-queue-001.tsv
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
  - naturalproductmech:mibig-09c929043b
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-09c929043b
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-09c929043b
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2658-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/frontalamide-a.yaml
  locator: Whole current plaintext including every curation_history entry
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete personally read selected owner and history; retained contents
    do not imply fresh source access.
  snapshot_sha256: cc2f0d9ea13c0fa5e44679634ea8711d3a85a6543430a09aa621de1765453b25
- evidence_id: support-2658-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete actual captured owner, including all written claims and exact
    present/absent mechanism and component roots.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/label;
    /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts;
    /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Exact owner-local identifier, structure and grounding/definition fields;
    retained mapping is distinct from natural-identity proof.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-provenance-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/producer_taxon_groups; /records/7/owner_document/bgc_class
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Stored producer and locus grades, coordinates and citations are preserved
    as distinct assertions.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-citations-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document/source_concepts; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/curation_history
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Exact retained source concepts, citation grain and complete seeding history;
    no primary-paper reopening.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups;
    /records/7/owner_document/xrefs
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Owner-local occurrence and identifier placements; no causal production
    inference.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete owner has no written bioactivity or molecular-target roots; bounded
    retained absence only.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/biosynthesis_origin
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Owner-local filing and computed classifier values; source class/subclass
    and local topology are separately evidenced.
  snapshot_sha256: 1213643e3463555de428cf1ebde3425096654ed63ce9b519e271f7a2279f7526
- evidence_id: support-2658-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/intakes-001/2658-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Actual inspection-only hashes and target ownership declarations; no scientific
    reading of entire captured corpus files is implied.
  snapshot_sha256: 5cb30c0a20806d87063aa67b645c5184c619fb70760c12652fdb4ab0d9ae5bb7
- evidence_id: support-2658-intake-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/intakes-001/2658-inspect-execution-001.json
  locator: /exit_code; /command; /actual_environment; /stdout; /stderr
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Original canonical inspection exit 0 and empty stderr for this owner.
  snapshot_sha256: 56aa93bbcdaddb9d202566057f6b848780a8edd6779a188f0b8b300f9d031712
- evidence_id: support-2658-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/root-current266-intake-acceptance-001.json
  locator: /accepted; /status; /summary; /source_plan_acceptance; /verification
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: ROOT accepted all ten original inspections and the exact 466 input placements
    across 66 paths.
  snapshot_sha256: 765e490e331f1532a48a852f419b6b189ed4dcf79c925bebb4d2ba6fe5c9df40
- evidence_id: support-2658-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates;
    /records/7/identity_comparison_paths; /records/7/additional_context_paths; /records/7/additional_context_roles;
    /records/7/reader_implementation_paths; /records/7/proposed_input_paths; /records/7/proposed_input_count
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Exact owner-local companion, seven diagnostic/implementation roles and
    literal reader implementation inputs where applicable. Captured input presence
    is distinct from positive scientific evidence.
  snapshot_sha256: ce93dbe0de3ce7dd26ec25c66225980ab91feedb2756ae146c866b183070d40e
- evidence_id: support-2658-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/root-current266-source-plan-acceptance-001.json
  locator: /status; /plan; /verification
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: ROOT acceptance of the one original operative source plan.
  snapshot_sha256: 8ed76d5d89e051b30302b866483f9c8c2ffc9b09d7f9b555cf44c96c2016e4a7
- evidence_id: support-2658-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/support-prep/support-current266-assigned-source-reading-001.json
  locator: /contexts/9
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Personally read every saved frame and full positive row dictionary for
    this owner; complete companion attribution remains separately scoped.
  snapshot_sha256: f78a11f180fc489947c726dbbfe3146bb29c81b4e14be91805f99456dbc6c228
- evidence_id: support-2658-raw-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/support-prep/support-current266-last-five-whole-owner-reading-001.json
  locator: /records/2
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Support personally read this whole raw owner and all history entries; no
    primary source was reopened.
  snapshot_sha256: 6b88e700b9a676feca13ef0fc87e56cd6249b34fd873a92116511aff41767489
- evidence_id: support-2658-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Attributed reading reconciliation preserves 35 BGC plus 50 Support row
    placements and zero Native primary row credit; negative and blank boundaries remain
    explicit.
  snapshot_sha256: 0729b9729d54d9a7558967a0b6a214929dafd3a4eb1051d9bfe79c7b59395137
- evidence_id: support-2658-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/native-prep/native-current266-cached-taxonomy-reading-001.json
  locator: /context_interpretations/19; /interpretation; /counts
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Owner-local cached labels/synonyms and retained routes; no fresh rank,
    lineage or production authority.
  snapshot_sha256: aa52cce9dbed42a2b3d6b7e7caff16f397dfcf50ff7e4d44ec0d1d1551f1cb80
- evidence_id: support-2658-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/native-prep/native-current266-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /interpretation; /implementation_scope
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Exact implemented-curation and source-identity resolution; lexical matches
    do not establish an applicable correction or exclusion for this owner.
  snapshot_sha256: 98f4e92faa9e248d6fcb077ca1fcdc62813caecabe5b6e69ff3cfc0d4385a689
  search_scope: '{"owner": "data/natural_products/unclassified/frontalamide-a.yaml",
    "primary_source_row_credit": 0, "scope": "Retained exact identity/digest predicates;
    lexical candidates remain separate"}'
- evidence_id: support-2658-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete two-form saved molecular tables, scalars, stereo, motifs and comparisons
    for this owner; normalized equality is not full fixed-form or natural identity
    proof.
  snapshot_sha256: 920f9aa6995b2c16a2204c152bcd2068dc2b0d1699e8ea514f207e5b2125df6b
- evidence_id: support-2658-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/support-prep/support-current266-last-five-molecular-intake-reading-001.json
  locator: /records/2
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Support personally read every saved atom/bond field and all ring, stereo
    and motif fields for both forms; no new molecular parse.
  snapshot_sha256: 19114635222840485ebe9d3288b8ec9e9e0802895498c78696005292adf545a4
- evidence_id: support-2658-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/root-diagnostic-result-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /interpretation_limits
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: ROOT acceptance of the one original diagnostic, preserving false comparisons
    and global warning scope.
  snapshot_sha256: 9ce2ac94c51ea81860ade7e782c7c157c7b5c6d4db25b3f98def0488a11f0d4e
- evidence_id: support-2658-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Original diagnostic exit 0 with no retries; four undefined-stereo warnings
    remain global and are not assigned to particular owners.
  snapshot_sha256: a1661417137ee1b0ac645876214207107e6114cac8d6e0e7c000d50a15e92594
- evidence_id: support-2658-stereo-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–172
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: The retained stereo_complete calculation uses FindMolChiralCenters with
    includeUnassigned=True and useLegacyImplementation=False on source SMILES; reconstructed
    double-bond potential stereo is outside that calculation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2658-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch266/root-native-gates-acceptance-001.json
  locator: /accepted; /checks_passed; /all_native_gates_passed; /unavailable_required_gates;
    /complete_selected_queue_rows
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Five local gates passed; full QC and OAK remain unavailable. Queue rows
    are leads, not scientific verdicts.
  snapshot_sha256: ec2f7485bf1db286f354883da4b5bdca77fcd173501f711c856f1d9ddd54e3ee
- evidence_id: support-2658-reader-applicability
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: All ten selected owners have no literal mechanism or component roots; no
    maintained reader applies.
  snapshot_sha256: d81831a5a715fba911c9ba3e8e25c83babd744879bcc2fa85c6ad00f201d97cc
- evidence_id: support-2658-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved mibig_compounds query frame with all 2 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 2, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/mibig_compounds/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2658-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved chebi_structures query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved lotus_occurrences query frame with all 1 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/lotus_occurrences/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2658-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved npclassifier query frame with all 1 row placements and full
    fields. A negative frame is limited to its recorded predicate; repeated rows are
    not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/npclassifier/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2658-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved pubchem_bioassay query frame with all 1 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/19/source_scope_inventory/joins/pubchem_bioassay/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2658-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved bindingdb_targets query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "FZFGBLTUJOOTPO-QRHYNJGYSA-N"}'
- evidence_id: support-2658-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Complete saved chebi_origins query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"matched_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2658-taxon-query-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch266-tentative/bgc-prep/bgc-conditional266-source-inventory-DATA-001.json
  locator: /contexts/19/source_scope_inventory/source_taxa; /contexts/19/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/19/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T04:40:29.807041Z'
  support: supports
  summary: Exact owner-local source taxon IDs and retained positive/negative diagnostic
    routes; companion route placements are not additional independent decisions.
  snapshot_sha256: 83c51ec779acab5eb3a8ef439d0bf65584ca748443899426709502b96230ac3b
  search_scope: '{"forward_merge_placements": 0, "nonorganism_placements": 0, "predicate":
    "Exact retained taxon IDs against both captured diagnostic tables", "source_taxa":
    ["NCBITaxon:1883", "NCBITaxon:1931", "NCBITaxon:591157"]}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-266/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json
  accessed_at: '2026-11-06T04:09:24.184233Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: f5ffa97dd28f712666cfe79a3e22e6439e15c4df44edb453afeb9a98794aaa2b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-266/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json
  accessed_at: '2026-11-06T04:09:48.537907Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 42dbb541817cadbff2f100ebfef01033d9bb4fe24a6480a15bdf11b504868ef4
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-266/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json
  accessed_at: '2026-11-06T04:10:07.806177Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-266/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json
  accessed_at: '2026-11-06T04:10:41.587497Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-266/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-266/native-current266-five-gates-execution-001.json
  accessed_at: '2026-11-06T04:10:53.099686Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f37906f56b62745ee2cb703d1a5509bb3961ff444f0b5af93df0487dd2909cdf
assessments:
- area: identity
  topic: Retained identity and grounding
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key; no prefix or name substitution.
    value: FZFGBLTUJOOTPO-QRHYNJGYSA-N
    evidence_ids:
    - support-2658-grounding-owner
    - support-2658-chemistry
    - support-2658-query-mibig_compounds
    - support-2658-query-chebi_structures
    - support-2658-direct-contexts
    - support-2658-source-reading
  - name: grounding_scope
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    value: MINTED retained mapping; no independent natural-identity proof
    evidence_ids:
    - support-2658-grounding-owner
    - support-2658-chemistry
    - support-2658-query-mibig_compounds
    - support-2658-query-chebi_structures
    - support-2658-direct-contexts
    - support-2658-source-reading
  assessment_id: support-2658-identity
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-grounding-owner
  - support-2658-chemistry
  - support-2658-query-mibig_compounds
  - support-2658-query-chebi_structures
  - support-2658-direct-contexts
  - support-2658-source-reading
  outcome: supported
  summary: 'Two exact MIBiG source concepts map to the retained full key and owner:
    BGC0000996 version 5 and BGC0002509 version 3. The OPEN shared-structure discussion
    remains unresolved; within-owner normalization does not establish that the two
    source entries identify the same natural compound. The written NPAtlas and PubChem
    xrefs are retained mappings, and no exact ChEBI structure row was found in the
    saved query. Both saved forms regenerate the declared StandardInChI and full key,
    supporting stored mapping without independent natural-identity verification.'
- area: representation
  topic: Stored forms and stereochemistry
  dimensions:
  - name: stereochemistry_scope
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    value: 8 specified and 2 unspecified tetrahedral centers; one E and one Z alkene
    evidence_ids:
    - support-2658-grounding-owner
    - support-2658-chemistry
    - support-2658-molecular-reading
    - support-2658-diagnostic-acceptance
    - support-2658-diagnostic-execution
    - support-2658-stereo-implementation
  - name: representation_correspondence
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    value: 8 of 10 flags; two imidic motifs; enolic Unknown and macrocyclic imine
      Unspecified
    evidence_ids:
    - support-2658-grounding-owner
    - support-2658-chemistry
    - support-2658-molecular-reading
    - support-2658-diagnostic-acceptance
    - support-2658-diagnostic-execution
    - support-2658-stereo-implementation
  assessment_id: support-2658-representation
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-grounding-owner
  - support-2658-chemistry
  - support-2658-molecular-reading
  - support-2658-diagnostic-acceptance
  - support-2658-diagnostic-execution
  - support-2658-stereo-implementation
  outcome: unknown
  summary: Both neutral C29H36N2O7 forms contain 38 atoms and 42 bonds. Five reported
    rings have sizes 5, 5, 16, 5 and 6. The original has four carbonyls, two amides
    and no ester; the 16-membered ring contains an amide linkage, while a separate
    five-membered nitrogen ring contains the other amide. Reconstruction retains two
    carbonyls and presents two C(OH)=N sites with terminal hydroxyl oxygens. Eight
    specified and two unspecified tetrahedral centers persist, as do one Z and one
    E alkene. The original enolic C=C is potential Unspecified/STEREONONE; the corresponding
    reconstructed entry is Unknown/STEREOANY. The new macrocyclic C=N is potential
    Unspecified; the new five-membered-ring C=N is not listed as potential double
    stereo. Thus two imidic motifs do not mean two added unspecified-double entries.
    Local CIP labels and atom indices remain form-specific because the saved map is
    empty. Formula, charge, StandardInChI and full key agree, but both canonical comparisons
    are false. This bounded tautomer-consistent correspondence neither proves full
    fixed-form identity nor resolves the OPEN cross-entry identity discussion. Four
    original undefined-stereo warnings remain globally unassigned; they are not attached
    to an individual record.
- area: provenance
  topic: Producer, taxonomy and locus grades
  dimensions:
  - name: taxon_scope
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    value: 591157 and 1931 producers; 1883 occurrence; cached scope
    evidence_ids:
    - support-2658-provenance-owner
    - support-2658-taxonomy
    - support-2658-taxon-query-scope
    - support-2658-curation-scope
    - support-2658-query-mibig_compounds
  - name: producer_evidence
    definition: Retained producer grade, not inferred from occurrence or locus association.
    value: 0996 BGC_CHARACTERIZED; 2509 SOURCE_ASSERTION
    evidence_ids:
    - support-2658-provenance-owner
    - support-2658-taxonomy
    - support-2658-taxon-query-scope
    - support-2658-curation-scope
    - support-2658-query-mibig_compounds
  - name: locus_evidence
    definition: Retained compound-specific cluster-link grade and source methods.
    value: 0996 CLUSTER_DEMONSTRATED; 2509 CLUSTER_UNSTATED
    evidence_ids:
    - support-2658-provenance-owner
    - support-2658-taxonomy
    - support-2658-taxon-query-scope
    - support-2658-curation-scope
    - support-2658-query-mibig_compounds
  assessment_id: support-2658-provenance
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-provenance-owner
  - support-2658-taxonomy
  - support-2658-taxon-query-scope
  - support-2658-curation-scope
  - support-2658-query-mibig_compounds
  outcome: supported
  summary: BGC0000996 retains Streptomyces sp. SPB78 (NCBITaxon:591157), BGC_CHARACTERIZED
    and a separately CLUSTER_DEMONSTRATED link from knock-out studies at GG657742.1
    positions 4,892,742–4,909,316. Its classes are NRPS|PKS and subclasses Type I|Iterative
    type I; completeness is partial. BGC0002509 instead retains Streptomyces sp. (1931),
    SOURCE_ASSERTION and CLUSTER_UNSTATED at MN817126.1 positions 1–22,084, with blank
    methods and unknown completeness. Its class is NRPS only and subclass Type I.
    Both entries have questionable quality. The stronger 0996 grades are not transferred
    to 2509.
- area: evidence
  topic: Citation and history scope
  dimensions:
  - name: citation_scope
    definition: Exact retained citation basis; no implied new primary-source access.
    value: Two ENTRY-level source citations plus separate LOTUS DOI
    evidence_ids:
    - support-2658-citations-history
    - support-2658-source-reading
    - support-2658-source-notes
    - support-2658-source-mibig_compounds
    - support-2658-source-lotus_occurrences
    - support-2658-source-npclassifier
    - support-2658-source-pubchem_bioassay
    - support-2658-query-mibig_compounds
    - support-2658-query-chebi_structures
    - support-2658-query-lotus_occurrences
    - support-2658-query-cyanometdb_occurrences
    - support-2658-query-npclassifier
    - support-2658-query-pubchem_bioassay
    - support-2658-query-bindingdb_targets
    - support-2658-query-antibioticmech_inchikeys
    - support-2658-query-chebi_origins
  assessment_id: support-2658-citations
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-citations-history
  - support-2658-source-reading
  - support-2658-source-notes
  - support-2658-source-mibig_compounds
  - support-2658-source-lotus_occurrences
  - support-2658-source-npclassifier
  - support-2658-source-pubchem_bioassay
  - support-2658-query-mibig_compounds
  - support-2658-query-chebi_structures
  - support-2658-query-lotus_occurrences
  - support-2658-query-cyanometdb_occurrences
  - support-2658-query-npclassifier
  - support-2658-query-pubchem_bioassay
  - support-2658-query-bindingdb_targets
  - support-2658-query-antibioticmech_inchikeys
  - support-2658-query-chebi_origins
  outcome: supported
  summary: BGC0000996 carries ENTRY-level PMID:20547882; BGC0002509 carries ENTRY-level
    DOI:10.6023/cjoc201912017. LOTUS retains DOI:10.1073/PNAS.1001513107. These source-specific
    placements and all history remain intact; publication identity and independence
    are not newly established.
- area: evidence
  topic: Occurrence, assay and target boundaries
  dimensions:
  - name: occurrence_scope
    definition: Source placements and shared citations are not independent production
      experiments.
    value: One genus-level LOTUS placement; no grade transfer
    evidence_ids:
    - support-2658-occurrence-owner
    - support-2658-activity-owner
    - support-2658-source-reading
    - support-2658-curation-scope
    - support-2658-taxon-query-scope
    - support-2658-source-mibig_compounds
    - support-2658-source-lotus_occurrences
    - support-2658-source-npclassifier
    - support-2658-source-pubchem_bioassay
    - support-2658-query-mibig_compounds
    - support-2658-query-chebi_structures
    - support-2658-query-lotus_occurrences
    - support-2658-query-cyanometdb_occurrences
    - support-2658-query-npclassifier
    - support-2658-query-pubchem_bioassay
    - support-2658-query-bindingdb_targets
    - support-2658-query-antibioticmech_inchikeys
    - support-2658-query-chebi_origins
  - name: assay_target_scope
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    value: Zero actual AIDs; one blank sentinel; no target transfer
    evidence_ids:
    - support-2658-occurrence-owner
    - support-2658-activity-owner
    - support-2658-source-reading
    - support-2658-curation-scope
    - support-2658-taxon-query-scope
    - support-2658-source-mibig_compounds
    - support-2658-source-lotus_occurrences
    - support-2658-source-npclassifier
    - support-2658-source-pubchem_bioassay
    - support-2658-query-mibig_compounds
    - support-2658-query-chebi_structures
    - support-2658-query-lotus_occurrences
    - support-2658-query-cyanometdb_occurrences
    - support-2658-query-npclassifier
    - support-2658-query-pubchem_bioassay
    - support-2658-query-bindingdb_targets
    - support-2658-query-antibioticmech_inchikeys
    - support-2658-query-chebi_origins
  assessment_id: support-2658-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-occurrence-owner
  - support-2658-activity-owner
  - support-2658-source-reading
  - support-2658-curation-scope
  - support-2658-taxon-query-scope
  - support-2658-source-mibig_compounds
  - support-2658-source-lotus_occurrences
  - support-2658-source-npclassifier
  - support-2658-source-pubchem_bioassay
  - support-2658-query-mibig_compounds
  - support-2658-query-chebi_structures
  - support-2658-query-lotus_occurrences
  - support-2658-query-cyanometdb_occurrences
  - support-2658-query-npclassifier
  - support-2658-query-pubchem_bioassay
  - support-2658-query-bindingdb_targets
  - support-2658-query-antibioticmech_inchikeys
  - support-2658-query-chebi_origins
  outcome: supported
  summary: The sole LOTUS row names genus-level Streptomyces (NCBITaxon:1883), distinct
    from the two source-specific producer taxon assertions. One blank-AID sentinel
    for CID101515037 provides no assay result. BindingDB, related-corpus and written
    activity/target roots are absent within the saved scope. Shared-BGC companions
    do not confer activity, producer grades or mechanism.
- area: consistency
  topic: Classification and saved topology
  dimensions:
  - name: classification_applicability
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    value: 16-membered macrolactam; zero esters; Macrolides model label qualified
    evidence_ids:
    - support-2658-classification-owner
    - support-2658-chemistry
    - support-2658-molecular-reading
    - support-2658-query-npclassifier
    - support-2658-query-mibig_compounds
  assessment_id: support-2658-classification
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-classification-owner
  - support-2658-chemistry
  - support-2658-molecular-reading
  - support-2658-query-npclassifier
  - support-2658-query-mibig_compounds
  outcome: unknown
  summary: The original 16-membered ring contains an amide rather than an ester, and
    the separate five-membered nitrogen ring has the local tetramic carbonyl arrangement.
    This supports bounded macrolactam and tetramic-region topology. The computed Macrolides
    superclass is retained as model provenance, without claiming a macrolactone or
    treating the label as proof of an ester. The Macrocyclic tetramic acids family
    has local topological support, while complete model-family and biosynthetic applicability
    remain qualified.
- area: completeness
  topic: Scientific completion and ownership
  dimensions:
  - name: review_completion
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    value: partial; five local gates passed; QC/OAK unavailable; no applicable reader
    evidence_ids:
    - support-2658-owner
    - support-2658-capture
    - support-2658-intake
    - support-2658-intake-execution
    - support-2658-intake-acceptance
    - support-2658-plan-acceptance
    - support-2658-source-reading
    - support-2658-raw-reading
    - support-2658-source-notes
    - support-2658-diagnostic-acceptance
    - support-2658-molecular-reading
    - support-2658-native-gates
    - support-2658-reader-applicability
  assessment_id: support-2658-completion
  target_ids:
  - naturalproductmech:mibig-09c929043b
  evidence_ids:
  - support-2658-owner
  - support-2658-capture
  - support-2658-intake
  - support-2658-intake-execution
  - support-2658-intake-acceptance
  - support-2658-plan-acceptance
  - support-2658-source-reading
  - support-2658-raw-reading
  - support-2658-source-notes
  - support-2658-diagnostic-acceptance
  - support-2658-molecular-reading
  - support-2658-native-gates
  - support-2658-reader-applicability
  outcome: unknown
  summary: The whole selected owner/history, complete retained source payloads and
    negative query bounds, both saved molecular forms and actual intake claims have
    been read. Current input hashes and ownership declarations match the accepted
    plan. Five local gates passed, but full QC and OAK remain unavailable and no live
    authority was consulted. No maintained reader applies. Completion remains partial;
    positive assessments concern retained mapping, source-grade fidelity and bounded
    local topology.
findings: []
actions: []
limitations:
- Retained owners and saved source payloads only; no fresh primary-paper, taxonomy,
  sequence or external identifier resolution.
- Friulimicin C/D and Frontalamide A/B have unequal canonical representations and
  empty saved maps. Fujikurin B has a complete limited map, but all five full-identity
  flags remain false and unresolved stereochemistry is preserved.
- Four original undefined-stereo warnings remain globally unassigned. Full QC and
  OAK are unavailable; source grades, OPEN discussions and computed-family limitations
  remain explicit.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Support personally read five complete selected owners/history and ten saved molecular
  forms: 552 atom rows, 576 bond rows and 34 reported ring rows. Selected source coverage
  is 45 frames, 19 positive placements and 253 fields; the primary partition including
  eight companions is 117 frames, 50 placements and 620 fields. Other contexts retain
  separate primary attribution.'
- Verified 234 actual input placements across 56 paths and their target ownership
  declarations. Input hashes do not imply scientific reading of whole corpus files.
  No generated record, native status or history was edited, and no outbound request
  was sent.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-266
```
