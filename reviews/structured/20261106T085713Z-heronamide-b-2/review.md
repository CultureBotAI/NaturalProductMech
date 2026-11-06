# Local evidence review: heronamide B

- Review: 20261106T085713Z-heronamide-b-2
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T08:02:41.513629Z
- Finished UTC: 2026-11-06T08:57:13.255041Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The heronamide-b-2 owner retains its own full key and BGC0001349 source route. Its five E and one Z double bonds distinguish it from the separate six-E Heronamide B owner. The stored forms normalize together but differ by an amide/imidic-OH representation; source and experimental limits keep completion partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2688; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b2ae90066f | data/natural_products/unclassified/heronamide-b-2.yaml | generated | heronamide B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-b2ae90066f | The original diagnostic parsed both stored forms; formula, charge, StandardInChI and full key agree within this owner. |
| strict_ten | passed | True | naturalproductmech:mibig-b2ae90066f | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b2ae90066f | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b2ae90066f | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b2ae90066f | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b2ae90066f | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b2ae90066f | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b2ae90066f | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b2ae90066f | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-b2ae90066f.

The heronamide-b-2 owner preserves full key SBSRDDBYEIPHHD-IVCUCATHSA-N, BGC0001349 version 5 compound 2 and PubChem 102257462. The separate heronamide-b owner has SBSRDDBYEIPHHD-DBJJYDABSA-N. Matching name, formula and first key block do not justify merging them: the saved geometry differs. This owner has only its BGC0001349 source route; the other owner's CMB producer, occurrence and xref are not transferred. Both original stored forms regenerate the declared StandardInChI and full key; that supports retained mapping without independent natural-identity proof.

### Stored forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-b2ae90066f.

Both forms retain C29H39NO3, 33 atoms and 35 bonds, zero atom charges and reported rings of 6, 12 and 6 members. Seven tetrahedral centres and six double-bond entries are specified, with five E and one Z in both forms. The source C13=C14 Z bond is retained as a Z entry in the reconstructed form; local atom labels are form-specific because the saved cross-form map is empty. Source C26=O27/N28-H becomes reconstructed C28(OH)=N29, with terminal O32 of degree 1/H1. Thus one carbonyl/amide becomes one hydroxyl-imine motif. Both canonical SMILES comparisons are false; the other eight flags, including formula, charge, StandardInChI and full key, are true. The new six-membered-ring C=N is not listed as potential double-bond stereo. No ester or candidate C5O sugar ring is recorded. This is a tautomer-consistent local representation difference, not proved fixed-graph identity. Eight warnings in the original shared stderr stream are globally unassigned; none is attributed to this owner.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-b2ae90066f.

The sole producer is the source label Streptomyces sp. SCSIO 03032, NCBITaxon:2878388, with SOURCE_ASSERTION evidence. The cache instead labels this ID Streptomyces marincola; the retained evidence does not independently resolve strain equivalence. BGC0001349 remains CLUSTER_UNSTATED at genbank:KP742963.1, with blank coordinates and no locus-evidence methods. Active/questionable/unknown-completeness, NRPS&#124;PKS and Type I&#124;Unknown metadata remain source annotations. No CMB-0406 route is present for this owner.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-b2ae90066f.

PMID:26194087 is retained at ENTRY grain for BGC0001349, not upgraded to a compound-specific experiment. No LOTUS occurrence citation is present. The complete source/history attribution is preserved without reopening the primary article or importing the other Heronamide B owner's references.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-b2ae90066f.

The saved LOTUS and CyanoMetDB frames are empty and the captured owner has no occurrence root. PubChem physical row 6959 is a blank-AID sentinel for CID 102257462, not an activity, inactivity or target observation. BindingDB and related-corpus frames are also empty within their exact predicates. No applicable exact exclusion or qualification is established; no occurrence or assay claim is transferred from the separate B owner.

### Classification and saved topology

consistency: unknown. Targets: naturalproductmech:mibig-b2ae90066f.

The MIBiG compound-class cell is blank. NPClassifier retains the two predicted pathways Amino acids and Peptides and Polyketides, Macrolides superclass and Macrolide lactams class, with is_glycoside false. A cyclic amide is visible in the source representation and an imidic-OH form in the reconstruction; neither form contains a carbonyl ester. These local facts do not independently validate the model family or biosynthetic route and do not make faithful prediction retention a record defect. Two pathway labels explicitly produce UNCLASSIFIED filing.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-b2ae90066f.

The whole selected owner/history, every saved source payload and negative frame, both complete saved molecular forms and actual intake claims have been read. Input hashes and ownership declarations match the accepted plan; this is distinct from reading entire corpus files. Positive conclusions concern retained mapping, source-grade fidelity and bounded encoded topology. Five local checks passed, but full QC/OAK and live authorities are unavailable. No maintained reader applies, so completion remains partial.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2688-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/heronamide-b-2.yaml; Whole current plaintext, including all curation_history entries | supports | Personally read the complete current owner and history; no fresh primary-source access. |
| support-2688-capture | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete actual owner with all written claims and absent mechanism/activity roots. |
| support-2688-grounding-owner | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/label; /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes; /records/7/owner_document/xrefs | supports | Exact owner-local full identity, source mappings and any OPEN discussion; no independent natural-identity proof. |
| support-2688-provenance-owner | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/producer_taxon_groups; /records/7/owner_document/bgc_class | supports | Producer and compound-specific locus assertions retain distinct grades, source routes and citation grain. |
| support-2688-citations-history | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document/source_concepts; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/curation_history | supports | All retained source concepts, citation-bearing locus fields and whole seeding history. |
| support-2688-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document/xrefs | supports | Exact written occurrence and xref placements; absence and occurrence are distinct from production. |
| support-2688-activity-owner | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete captured owner has no written bioactivity or molecular-target root; bounded retained absence only. |
| support-2688-classification-owner | /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/biosynthesis_origin; /records/7/owner_document/bgc_class | supports | Literal filing, model predictions and any asserted source compound class are preserved separately. |
| support-2688-intake | /private/tmp/npm-review-work/shared-next-batch269/intakes-001/2688-inspect-001.json; /status; /source; /targets | supports | Original inspection-only input hashes and target ownership declarations; input presence does not imply whole corpus reading. |
| support-2688-intake-execution | /private/tmp/npm-review-work/shared-next-batch269/intakes-001/2688-inspect-execution-001.json; /exit_code; /command; /actual_environment; /stdout; /stderr | supports | Original owner inspection exit 0 with empty stderr. |
| support-2688-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch269/root-intake-acceptance-001.json; /accepted; /summary; /exact_plan_maps; /all_stderr_empty | supports | ROOT accepted the ten original intakes and exact 464 placements across 59 paths. |
| support-2688-direct-contexts | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates; /records/7/identity_comparison_paths; /records/7/additional_context_paths; /records/7/additional_context_roles; /records/7/reader_implementation_paths; /records/7/proposed_input_paths; /records/7/proposed_input_count | supports | Owner-local direct contexts and seven additional diagnostic/implementation roles; no transfer of another owner's source assertions. |
| support-2688-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch269/root-current269-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT accepted the one original operative source plan. |
| support-2688-source-reading | /private/tmp/npm-review-work/shared-next-batch269-tentative/support-prep/support-current269-assigned-source-reading-001.json; /contexts/5; /selected_source_to_owner_reconciliation; /raw_owner_reading | supports | Personally read this complete saved frame set and all positive dictionaries; current source-to-owner placements reconciled without extra primary credit. |
| support-2688-source-notes | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Disjoint 19 BGC plus 39 Support primary rows and zero Native source-row credit; blank and negative scope remain explicit. |
| support-2688-taxonomy | /private/tmp/npm-review-work/shared-next-batch269-tentative/native-prep/native-current269-cached-taxonomy-reading-001.json; /context_interpretations/10; /interpretation; /counts | supports | Owner-local cached labels and unresolved strain-spelling scope; no fresh taxonomy or producer authority. |
| support-2688-curation-scope | /private/tmp/npm-review-work/shared-next-batch269-tentative/native-prep/native-current269-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /interpretation; /implementation_scope | supports | Exact retained identity/digest predicates establish no applicable correction, exclusion or qualification for this owner; lexical candidates are separate. |
| support-2688-chemistry | /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnostic-DATA-001.json; /records/7 | supports | Complete saved two-form atom/bond/ring/stereo/motif tables, comparisons and existing map for this owner; normalized equality is not natural identity. |
| support-2688-molecular-reading | /private/tmp/npm-review-work/shared-next-batch269-tentative/support-prep/support-current269-last-five-molecular-intake-reading-001.json; /records/2 | supports | Personal whole saved-table reading and form-specific interpretation; no new molecular parse or map. |
| support-2688-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /warnings; /denied_events | supports | ROOT accepted the original twenty-form diagnostic; eight undefined-stereo warnings remain globally unassigned. |
| support-2688-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0, eight unassigned stderr warnings, no retries or external requests. |
| support-2688-stereo-implementation | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–172 | supports | stereo_complete is computed from source-SMILES FindMolChiralCenters(includeUnassigned=True, useLegacyImplementation=False); it does not certify all double-bond geometry. |
| support-2688-producer-grade-policy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; lines 1–40 | supports | Maintained grade table separates cluster-only heterologous/enzymatic evidence from organism-and-cluster correlation evidence. |
| support-2688-filing-implementation | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306 | supports | choose_pathway returns UNCLASSIFIED for zero or multiple model pathway labels; a single supported label is the separate branch. |
| support-2688-native-gates | /private/tmp/npm-review-work/shared-next-batch269/root-native-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_required_native_gates_passed; /unavailable_required_gates; /queue | supports | Five local child commands passed once; the earlier controller stopped before children. Full QC/OAK are unavailable and queue rows remain leads. |
| support-2688-reader-applicability | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | No literal selected mechanism/component roots and no maintained reader applies. |
| support-2688-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds predicate and full payloads for 1 placements; negatives are finite and rows are not independent experiments. |
| support-2688-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Complete physical row chunks/dictionaries at /contexts/10/source_scope_inventory/joins/mibig_compounds/matches in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved there | supports | Retained table backing all personally read positive fields; exact physical joins are retained in the source-reading receipt. |
| support-2688-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2688-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2688-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2688-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier predicate and full payloads for 1 placements; negatives are finite and rows are not independent experiments. |
| support-2688-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Complete physical row chunks/dictionaries at /contexts/10/source_scope_inventory/joins/npclassifier/matches in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved there | supports | Retained table backing all personally read positive fields; exact physical joins are retained in the source-reading receipt. |
| support-2688-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay predicate and full payloads for 1 placements; negatives are finite and rows are not independent experiments. |
| support-2688-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Complete physical row chunks/dictionaries at /contexts/10/source_scope_inventory/joins/pubchem_bioassay/matches in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved there | supports | Retained table backing all personally read positive fields; exact physical joins are retained in the source-reading receipt. |
| support-2688-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2688-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2688-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins predicate and full payloads for 0 placements; negatives are finite and rows are not independent experiments. |
| support-2688-taxon-query-scope | /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/source_taxa; /contexts/10/source_scope_inventory/forward_taxon_merge_matches; /contexts/10/source_scope_inventory/nonorganism_matches | supports | Exact owner-local taxon routes and retained diagnostic negatives; no companion route or independent decision is inferred. |
| support-2688-B-variant-saved-geometry | /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnostic-DATA-001.json; /records/7/declared_structure; /records/7/smiles/computed/potential_stereo; /records/7/inchi/computed/potential_stereo; /records/8/declared_structure; /records/8/smiles/computed/potential_stereo; /records/8/inchi/computed/potential_stereo | supports | Separately saved B-2 and B forms retain distinct full keys and five-E/one-Z versus six-E geometry. Comparative reading does not add a counterpart owner to this target's input provenance. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-269/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-269/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-269/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-269/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-269/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained owner, source rows and saved diagnostics only; no fresh primary-paper, taxonomy, sequence or external identifier resolution.
- The heronamide-b-2 and heronamide-b owners retain different full keys and opposite geometry at one encoded alkene. The empty cross-form map and amide/imidic representation difference do not authorize identity collapse or source transfer.
- Eight undefined-stereo warnings remain unassigned to owners. Full QC and OAK are unavailable; recorded grades, citation grain, model predictions and existing source discussions retain their stated limits.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The complete owner/history, both saved molecular tables and all owner-local saved query frames were personally read. Physical row placements are not independent experiments and input hash verification is not whole-corpus scientific reading.
- This review proposes no source, generated record, curation status or history edit. No outbound request, new molecular parse or target execution was performed in this authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T085713Z-heronamide-b-2
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: heronamide B'
started_at: '2026-11-06T08:02:41.513629Z'
finished_at: '2026-11-06T08:57:13.255041Z'
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
summary: The heronamide-b-2 owner retains its own full key and BGC0001349 source route.
  Its five E and one Z double bonds distinguish it from the separate six-E Heronamide
  B owner. The stored forms normalize together but differ by an amide/imidic-OH representation;
  source and experimental limits keep completion partial.
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
  - path: data/natural_products/unclassified/heronamide-a.yaml
    sha256: 1fd30cc8e305d8c273489aafd9ac770b0d2151c1d3b01ae63fd7ae31ac57392c
    role: context
  - path: data/natural_products/unclassified/heronamide-b-2.yaml
    sha256: d14d6be54599a34145f1b1cf6f6bbe09daa704fba9a23f647c53be86bf0c21a4
    role: target
  - path: data/natural_products/unclassified/heronamide-c.yaml
    sha256: 250e53de9241ca14915fa62f3c38867d92b3afa2139b5a50aaf1d970f70cd4fd
    role: context
  - path: data/natural_products/unclassified/heronamide-d.yaml
    sha256: dbe3f04ce3b688115ec0d9e6d07b490c028a09535b513872ce412fb272dcfdc3
    role: context
  - path: data/natural_products/unclassified/heronamide-e.yaml
    sha256: 3e86ab7c283ceba70cd0609108ad291b419a1bee46170d8cc7bd606259ee5bd3
    role: context
  - path: data/natural_products/unclassified/heronamide-f.yaml
    sha256: eab7bb0a45740b7e36ab2465f80ec88063bc2dd2da2de9bec9d5c5fc017e5176
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
  selection: Campaign path order 2688; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b2ae90066f
targets:
- target_id: naturalproductmech:mibig-b2ae90066f
  path: data/natural_products/unclassified/heronamide-b-2.yaml
  label: heronamide B
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnose269-001.py
    1838554543323855b8d9a8242692545cffb4e70091b18d2ff00c929204dac10b 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
    f1128b31e703b4d75afdcee3a5686aa799cd60d4dbe4d9c8408d51039483c9f7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The original diagnostic parsed both stored forms; formula, charge, StandardInChI
    and full key agree within this owner.
  scope_note: Original shared twenty-form execution, no rerun. Both owner canonical
    SMILES comparison flags are false; the other eight are true, with an empty saved
    map and an amide/imidic-OH representation difference. The full-identity flag remains
    false and eight stderr warnings are globally unassigned. A passed execution does
    not establish full graph or natural identity.
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-chemistry
  - support-2688-diagnostic-acceptance
  - support-2688-diagnostic-execution
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  command: just validate-strict data/natural_products/unclassified/harzianopyridone.yaml
    data/natural_products/unclassified/hassallidin-c.yaml data/natural_products/unclassified/hassallidin-d.yaml
    data/natural_products/unclassified/heat-stable-antifungal-factor.yaml data/natural_products/unclassified/hectochlorin.yaml
    data/natural_products/unclassified/heptyltyrazolone.yaml data/natural_products/unclassified/heronamide-a.yaml
    data/natural_products/unclassified/heronamide-b-2.yaml data/natural_products/unclassified/heronamide-b.yaml
    data/natural_products/unclassified/heronamide-c.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-269/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-b2ae90066f
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-269/validate-all-001.tsv
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
  - naturalproductmech:mibig-b2ae90066f
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
  - naturalproductmech:mibig-b2ae90066f
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
  - naturalproductmech:mibig-b2ae90066f
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-269/review-queue-001.tsv
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
  - naturalproductmech:mibig-b2ae90066f
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2688-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/heronamide-b-2.yaml
  locator: Whole current plaintext, including all curation_history entries
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Personally read the complete current owner and history; no fresh primary-source
    access.
  snapshot_sha256: d14d6be54599a34145f1b1cf6f6bbe09daa704fba9a23f647c53be86bf0c21a4
- evidence_id: support-2688-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete actual owner with all written claims and absent mechanism/activity
    roots.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/label;
    /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts;
    /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes;
    /records/7/owner_document/xrefs
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Exact owner-local full identity, source mappings and any OPEN discussion;
    no independent natural-identity proof.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-provenance-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/producer_taxon_groups; /records/7/owner_document/bgc_class
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Producer and compound-specific locus assertions retain distinct grades,
    source routes and citation grain.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-citations-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document/source_concepts; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/curation_history
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: All retained source concepts, citation-bearing locus fields and whole seeding
    history.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document/xrefs
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Exact written occurrence and xref placements; absence and occurrence are
    distinct from production.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete captured owner has no written bioactivity or molecular-target
    root; bounded retained absence only.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/biosynthesis_origin; /records/7/owner_document/bgc_class
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Literal filing, model predictions and any asserted source compound class
    are preserved separately.
  snapshot_sha256: 2f669dc88707463c0779c810e60c6f078d5c768e0fa411fd53d8522cdfd53b48
- evidence_id: support-2688-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/intakes-001/2688-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Original inspection-only input hashes and target ownership declarations;
    input presence does not imply whole corpus reading.
  snapshot_sha256: 8a294991a54e9f60b40b86e14c3691dd5e8a771ee1ad1861f1f9d0cce25f7848
- evidence_id: support-2688-intake-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/intakes-001/2688-inspect-execution-001.json
  locator: /exit_code; /command; /actual_environment; /stdout; /stderr
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Original owner inspection exit 0 with empty stderr.
  snapshot_sha256: a04cf4cef96281a02276ec440119391bf45884ec6cec980004212ecf4e14f7cf
- evidence_id: support-2688-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/root-intake-acceptance-001.json
  locator: /accepted; /summary; /exact_plan_maps; /all_stderr_empty
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: ROOT accepted the ten original intakes and exact 464 placements across
    59 paths.
  snapshot_sha256: 6c38d99b6d497dac528fc48cb08f0c0a604187d9d0d32ff98725d95812980c7b
- evidence_id: support-2688-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates;
    /records/7/identity_comparison_paths; /records/7/additional_context_paths; /records/7/additional_context_roles;
    /records/7/reader_implementation_paths; /records/7/proposed_input_paths; /records/7/proposed_input_count
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Owner-local direct contexts and seven additional diagnostic/implementation
    roles; no transfer of another owner's source assertions.
  snapshot_sha256: 7307ae5798b9a1a3e0942dc91ac785ed00acfb2e70f69f08b3ef4f63fe547d65
- evidence_id: support-2688-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/root-current269-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: ROOT accepted the one original operative source plan.
  snapshot_sha256: 80d54c34c42b90b32d1c908229956235e5bf6734534703923b5fac065f407511
- evidence_id: support-2688-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/support-prep/support-current269-assigned-source-reading-001.json
  locator: /contexts/5; /selected_source_to_owner_reconciliation; /raw_owner_reading
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Personally read this complete saved frame set and all positive dictionaries;
    current source-to-owner placements reconciled without extra primary credit.
  snapshot_sha256: f280355289d880e24f67126e17b0135ffcdc9f14a2d80e6a27e8c2e12305a804
- evidence_id: support-2688-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Disjoint 19 BGC plus 39 Support primary rows and zero Native source-row
    credit; blank and negative scope remain explicit.
  snapshot_sha256: 8c79cdc34e2a575469bd81da5b79b331dbb8cf07013197696db0f4def206a71b
- evidence_id: support-2688-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/native-prep/native-current269-cached-taxonomy-reading-001.json
  locator: /context_interpretations/10; /interpretation; /counts
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Owner-local cached labels and unresolved strain-spelling scope; no fresh
    taxonomy or producer authority.
  snapshot_sha256: f14fa9e57e3e68706d6ab3f299777563917c32edf4cfb1e6da61f25eba4b2dcd
- evidence_id: support-2688-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/native-prep/native-current269-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /interpretation; /implementation_scope
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Exact retained identity/digest predicates establish no applicable correction,
    exclusion or qualification for this owner; lexical candidates are separate.
  snapshot_sha256: d9dbfc539d6cdf6359969ead203c38e747770a9e823f399a26785180b1205e76
  search_scope: '{"owner": "data/natural_products/unclassified/heronamide-b-2.yaml",
    "primary_source_rows": 0, "scope": "Retained finite identity/digest and source-row
    predicates; no new source query"}'
- evidence_id: support-2688-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved two-form atom/bond/ring/stereo/motif tables, comparisons
    and existing map for this owner; normalized equality is not natural identity.
  snapshot_sha256: 4dd8e73e6764e4e52bc73ecb64a688c7976a78482e7b601efaf0b45a9e8306b7
- evidence_id: support-2688-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/support-prep/support-current269-last-five-molecular-intake-reading-001.json
  locator: /records/2
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Personal whole saved-table reading and form-specific interpretation; no
    new molecular parse or map.
  snapshot_sha256: 1793270bc12352821a39fd8e9360e8893e7dca2f94434d3ae000e1de132c8136
- evidence_id: support-2688-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /warnings; /denied_events
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: ROOT accepted the original twenty-form diagnostic; eight undefined-stereo
    warnings remain globally unassigned.
  snapshot_sha256: 8081bf92400fb9ad8f3cfd0ca24daa87a4f38f7a92451c09eaa857db5098f134
- evidence_id: support-2688-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Original diagnostic exit 0, eight unassigned stderr warnings, no retries
    or external requests.
  snapshot_sha256: 98d95ac143562fafa8534c3501e071c2a53c6119331902335b998738a8bbf033
- evidence_id: support-2688-stereo-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–172
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: stereo_complete is computed from source-SMILES FindMolChiralCenters(includeUnassigned=True,
    useLegacyImplementation=False); it does not certify all double-bond geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2688-producer-grade-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: lines 1–40
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Maintained grade table separates cluster-only heterologous/enzymatic evidence
    from organism-and-cluster correlation evidence.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2688-filing-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295–306
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: choose_pathway returns UNCLASSIFIED for zero or multiple model pathway
    labels; a single supported label is the separate branch.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2688-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch269/root-native-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /all_required_native_gates_passed;
    /unavailable_required_gates; /queue
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Five local child commands passed once; the earlier controller stopped before
    children. Full QC/OAK are unavailable and queue rows remain leads.
  snapshot_sha256: a9277f0df17e85554007515ad147a5ca7d2f53490933b2dc4086f8bfa1205bf2
- evidence_id: support-2688-reader-applicability
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: No literal selected mechanism/component roots and no maintained reader
    applies.
  snapshot_sha256: a5ec0576da093eb38998c4fccabc4aaf39ed0928eb1e930612c75586c05799dc
- evidence_id: support-2688-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved mibig_compounds predicate and full payloads for 1 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Complete physical row chunks/dictionaries at /contexts/10/source_scope_inventory/joins/mibig_compounds/matches
    in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved
    there
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Retained table backing all personally read positive fields; exact physical
    joins are retained in the source-reading receipt.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2688-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved chebi_structures predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved lotus_occurrences predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences predicate and full payloads for 0
    placements; negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved npclassifier predicate and full payloads for 1 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Complete physical row chunks/dictionaries at /contexts/10/source_scope_inventory/joins/npclassifier/matches
    in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved
    there
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Retained table backing all personally read positive fields; exact physical
    joins are retained in the source-reading receipt.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2688-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved pubchem_bioassay predicate and full payloads for 1 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Complete physical row chunks/dictionaries at /contexts/10/source_scope_inventory/joins/pubchem_bioassay/matches
    in the pinned inventory; physical_line, last_physical_line and row_sha256 preserved
    there
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Retained table backing all personally read positive fields; exact physical
    joins are retained in the source-reading receipt.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2688-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved bindingdb_targets predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys predicate and full payloads for
    0 placements; negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SBSRDDBYEIPHHD-IVCUCATHSA-N"}'
- evidence_id: support-2688-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Complete saved chebi_origins predicate and full payloads for 0 placements;
    negatives are finite and rows are not independent experiments.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"matched_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2688-taxon-query-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch269-tentative/bgc-prep/bgc-conditional269-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/source_taxa; /contexts/10/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/10/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Exact owner-local taxon routes and retained diagnostic negatives; no companion
    route or independent decision is inferred.
  snapshot_sha256: 2a2927d893a9297c5c46d964561057b92cc8450c6d5dad7d4bc8fdced7d8ee92
  search_scope: '{"forward_merge_placements": 0, "nonorganism_placements": 0, "source_taxa":
    ["NCBITaxon:2878388"]}'
- evidence_id: support-2688-B-variant-saved-geometry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch269/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7/declared_structure; /records/7/smiles/computed/potential_stereo;
    /records/7/inchi/computed/potential_stereo; /records/8/declared_structure; /records/8/smiles/computed/potential_stereo;
    /records/8/inchi/computed/potential_stereo
  accessed_at: '2026-11-06T08:49:16.611921Z'
  support: supports
  summary: Separately saved B-2 and B forms retain distinct full keys and five-E/one-Z
    versus six-E geometry. Comparative reading does not add a counterpart owner to
    this target's input provenance.
  snapshot_sha256: 4dd8e73e6764e4e52bc73ecb64a688c7976a78482e7b601efaf0b45a9e8306b7
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-269/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json
  accessed_at: '2026-11-06T08:16:38.744616Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: e7b0f88d1d452d96e411f7151b0fd1a1bcb78169460707f0c094e1c1328796b3
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-269/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json
  accessed_at: '2026-11-06T08:17:03.444961Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: ec545a3a6411006c286c6c9095cebc77f1528530152ced377d2029ad4a2cd837
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-269/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json
  accessed_at: '2026-11-06T08:17:22.446295Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-269/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json
  accessed_at: '2026-11-06T08:17:55.808877Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-269/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-269/native-current269-five-gates-execution-001.json
  accessed_at: '2026-11-06T08:18:07.361121Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f66ddf51b470f237088289a5ef21e54bde83ebe25ba43e765961ffd92609fc55
assessments:
- area: identity
  topic: Retained identity and grounding
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key; no prefix or name substitution.
    value: SBSRDDBYEIPHHD-IVCUCATHSA-N
    evidence_ids:
    - support-2688-grounding-owner
    - support-2688-chemistry
    - support-2688-query-mibig_compounds
    - support-2688-query-chebi_structures
    - support-2688-direct-contexts
    - support-2688-source-reading
    - support-2688-B-variant-saved-geometry
  - name: grounding_scope
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    value: MINTED retained mapping; no independent natural-identity proof
    evidence_ids:
    - support-2688-grounding-owner
    - support-2688-chemistry
    - support-2688-query-mibig_compounds
    - support-2688-query-chebi_structures
    - support-2688-direct-contexts
    - support-2688-source-reading
    - support-2688-B-variant-saved-geometry
  assessment_id: support-2688-identity
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-grounding-owner
  - support-2688-chemistry
  - support-2688-query-mibig_compounds
  - support-2688-query-chebi_structures
  - support-2688-direct-contexts
  - support-2688-source-reading
  - support-2688-B-variant-saved-geometry
  outcome: supported
  summary: 'The heronamide-b-2 owner preserves full key SBSRDDBYEIPHHD-IVCUCATHSA-N,
    BGC0001349 version 5 compound 2 and PubChem 102257462. The separate heronamide-b
    owner has SBSRDDBYEIPHHD-DBJJYDABSA-N. Matching name, formula and first key block
    do not justify merging them: the saved geometry differs. This owner has only its
    BGC0001349 source route; the other owner''s CMB producer, occurrence and xref
    are not transferred. Both original stored forms regenerate the declared StandardInChI
    and full key; that supports retained mapping without independent natural-identity
    proof.'
- area: representation
  topic: Stored forms and stereochemistry
  dimensions:
  - name: stereochemistry_scope
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    value: Seven specified tetrahedral centres; six specified C=C entries, five E
      and one Z; source atom-centred stereo_complete true
    evidence_ids:
    - support-2688-grounding-owner
    - support-2688-chemistry
    - support-2688-molecular-reading
    - support-2688-diagnostic-acceptance
    - support-2688-diagnostic-execution
    - support-2688-stereo-implementation
    - support-2688-B-variant-saved-geometry
  - name: representation_correspondence
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    value: Eight comparison flags true; both canonical SMILES flags false; empty saved
      map and full-identity false
    evidence_ids:
    - support-2688-grounding-owner
    - support-2688-chemistry
    - support-2688-molecular-reading
    - support-2688-diagnostic-acceptance
    - support-2688-diagnostic-execution
    - support-2688-stereo-implementation
    - support-2688-B-variant-saved-geometry
  assessment_id: support-2688-representation
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-grounding-owner
  - support-2688-chemistry
  - support-2688-molecular-reading
  - support-2688-diagnostic-acceptance
  - support-2688-diagnostic-execution
  - support-2688-stereo-implementation
  - support-2688-B-variant-saved-geometry
  outcome: supported
  summary: Both forms retain C29H39NO3, 33 atoms and 35 bonds, zero atom charges and
    reported rings of 6, 12 and 6 members. Seven tetrahedral centres and six double-bond
    entries are specified, with five E and one Z in both forms. The source C13=C14
    Z bond is retained as a Z entry in the reconstructed form; local atom labels are
    form-specific because the saved cross-form map is empty. Source C26=O27/N28-H
    becomes reconstructed C28(OH)=N29, with terminal O32 of degree 1/H1. Thus one
    carbonyl/amide becomes one hydroxyl-imine motif. Both canonical SMILES comparisons
    are false; the other eight flags, including formula, charge, StandardInChI and
    full key, are true. The new six-membered-ring C=N is not listed as potential double-bond
    stereo. No ester or candidate C5O sugar ring is recorded. This is a tautomer-consistent
    local representation difference, not proved fixed-graph identity. Eight warnings
    in the original shared stderr stream are globally unassigned; none is attributed
    to this owner.
- area: provenance
  topic: Producer, taxonomy and locus grades
  dimensions:
  - name: taxon_scope
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    value: Only source SCSIO 03032/2878388, cached as Streptomyces marincola; no CMB
      or genus-occurrence route
    evidence_ids:
    - support-2688-provenance-owner
    - support-2688-taxonomy
    - support-2688-taxon-query-scope
    - support-2688-curation-scope
    - support-2688-producer-grade-policy
    - support-2688-query-mibig_compounds
  - name: producer_evidence
    definition: Retained producer grade, not inferred from occurrence or locus association.
    value: One SOURCE_ASSERTION producer; no strain-identity upgrade
    evidence_ids:
    - support-2688-provenance-owner
    - support-2688-taxonomy
    - support-2688-taxon-query-scope
    - support-2688-curation-scope
    - support-2688-producer-grade-policy
    - support-2688-query-mibig_compounds
  - name: locus_evidence
    definition: Retained compound-specific cluster-link grade and source methods.
    value: CLUSTER_UNSTATED at KP742963.1; no coordinates or methods
    evidence_ids:
    - support-2688-provenance-owner
    - support-2688-taxonomy
    - support-2688-taxon-query-scope
    - support-2688-curation-scope
    - support-2688-producer-grade-policy
    - support-2688-query-mibig_compounds
  assessment_id: support-2688-provenance
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-provenance-owner
  - support-2688-taxonomy
  - support-2688-taxon-query-scope
  - support-2688-curation-scope
  - support-2688-producer-grade-policy
  - support-2688-query-mibig_compounds
  outcome: supported
  summary: The sole producer is the source label Streptomyces sp. SCSIO 03032, NCBITaxon:2878388,
    with SOURCE_ASSERTION evidence. The cache instead labels this ID Streptomyces
    marincola; the retained evidence does not independently resolve strain equivalence.
    BGC0001349 remains CLUSTER_UNSTATED at genbank:KP742963.1, with blank coordinates
    and no locus-evidence methods. Active/questionable/unknown-completeness, NRPS|PKS
    and Type I|Unknown metadata remain source annotations. No CMB-0406 route is present
    for this owner.
- area: evidence
  topic: Citation and history scope
  dimensions:
  - name: citation_scope
    definition: Exact retained citation basis; no implied new primary-source access.
    value: ENTRY PMID 26194087 only; no occurrence citation
    evidence_ids:
    - support-2688-citations-history
    - support-2688-source-reading
    - support-2688-source-notes
    - support-2688-source-mibig_compounds
    - support-2688-source-npclassifier
    - support-2688-source-pubchem_bioassay
    - support-2688-query-mibig_compounds
    - support-2688-query-chebi_structures
    - support-2688-query-lotus_occurrences
    - support-2688-query-cyanometdb_occurrences
    - support-2688-query-npclassifier
    - support-2688-query-pubchem_bioassay
    - support-2688-query-bindingdb_targets
    - support-2688-query-antibioticmech_inchikeys
    - support-2688-query-chebi_origins
  assessment_id: support-2688-citations
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-citations-history
  - support-2688-source-reading
  - support-2688-source-notes
  - support-2688-source-mibig_compounds
  - support-2688-source-npclassifier
  - support-2688-source-pubchem_bioassay
  - support-2688-query-mibig_compounds
  - support-2688-query-chebi_structures
  - support-2688-query-lotus_occurrences
  - support-2688-query-cyanometdb_occurrences
  - support-2688-query-npclassifier
  - support-2688-query-pubchem_bioassay
  - support-2688-query-bindingdb_targets
  - support-2688-query-antibioticmech_inchikeys
  - support-2688-query-chebi_origins
  outcome: supported
  summary: PMID:26194087 is retained at ENTRY grain for BGC0001349, not upgraded to
    a compound-specific experiment. No LOTUS occurrence citation is present. The complete
    source/history attribution is preserved without reopening the primary article
    or importing the other Heronamide B owner's references.
- area: evidence
  topic: Occurrence, assay and target boundaries
  dimensions:
  - name: occurrence_scope
    definition: Source placements and shared citations are not independent production
      experiments.
    value: No saved LOTUS/CyanoMetDB hit or written occurrence; bounded absence only
    evidence_ids:
    - support-2688-occurrence-owner
    - support-2688-activity-owner
    - support-2688-source-reading
    - support-2688-curation-scope
    - support-2688-taxon-query-scope
    - support-2688-source-mibig_compounds
    - support-2688-source-npclassifier
    - support-2688-source-pubchem_bioassay
    - support-2688-query-mibig_compounds
    - support-2688-query-chebi_structures
    - support-2688-query-lotus_occurrences
    - support-2688-query-cyanometdb_occurrences
    - support-2688-query-npclassifier
    - support-2688-query-pubchem_bioassay
    - support-2688-query-bindingdb_targets
    - support-2688-query-antibioticmech_inchikeys
    - support-2688-query-chebi_origins
  - name: assay_target_scope
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    value: CID 102257462 blank-AID sentinel; no actual assay or target-source hit
    evidence_ids:
    - support-2688-occurrence-owner
    - support-2688-activity-owner
    - support-2688-source-reading
    - support-2688-curation-scope
    - support-2688-taxon-query-scope
    - support-2688-source-mibig_compounds
    - support-2688-source-npclassifier
    - support-2688-source-pubchem_bioassay
    - support-2688-query-mibig_compounds
    - support-2688-query-chebi_structures
    - support-2688-query-lotus_occurrences
    - support-2688-query-cyanometdb_occurrences
    - support-2688-query-npclassifier
    - support-2688-query-pubchem_bioassay
    - support-2688-query-bindingdb_targets
    - support-2688-query-antibioticmech_inchikeys
    - support-2688-query-chebi_origins
  assessment_id: support-2688-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-occurrence-owner
  - support-2688-activity-owner
  - support-2688-source-reading
  - support-2688-curation-scope
  - support-2688-taxon-query-scope
  - support-2688-source-mibig_compounds
  - support-2688-source-npclassifier
  - support-2688-source-pubchem_bioassay
  - support-2688-query-mibig_compounds
  - support-2688-query-chebi_structures
  - support-2688-query-lotus_occurrences
  - support-2688-query-cyanometdb_occurrences
  - support-2688-query-npclassifier
  - support-2688-query-pubchem_bioassay
  - support-2688-query-bindingdb_targets
  - support-2688-query-antibioticmech_inchikeys
  - support-2688-query-chebi_origins
  outcome: supported
  summary: The saved LOTUS and CyanoMetDB frames are empty and the captured owner
    has no occurrence root. PubChem physical row 6959 is a blank-AID sentinel for
    CID 102257462, not an activity, inactivity or target observation. BindingDB and
    related-corpus frames are also empty within their exact predicates. No applicable
    exact exclusion or qualification is established; no occurrence or assay claim
    is transferred from the separate B owner.
- area: consistency
  topic: Classification and saved topology
  dimensions:
  - name: classification_applicability
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    value: Blank source class preserved; predicted Macrolides/Macrolide lactams qualified;
      two labels yield UNCLASSIFIED
    evidence_ids:
    - support-2688-classification-owner
    - support-2688-chemistry
    - support-2688-molecular-reading
    - support-2688-filing-implementation
    - support-2688-query-npclassifier
    - support-2688-query-mibig_compounds
  assessment_id: support-2688-classification
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-classification-owner
  - support-2688-chemistry
  - support-2688-molecular-reading
  - support-2688-filing-implementation
  - support-2688-query-npclassifier
  - support-2688-query-mibig_compounds
  outcome: unknown
  summary: The MIBiG compound-class cell is blank. NPClassifier retains the two predicted
    pathways Amino acids and Peptides and Polyketides, Macrolides superclass and Macrolide
    lactams class, with is_glycoside false. A cyclic amide is visible in the source
    representation and an imidic-OH form in the reconstruction; neither form contains
    a carbonyl ester. These local facts do not independently validate the model family
    or biosynthetic route and do not make faithful prediction retention a record defect.
    Two pathway labels explicitly produce UNCLASSIFIED filing.
- area: completeness
  topic: Scientific completion and ownership
  dimensions:
  - name: review_completion
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    value: partial; five local gates passed; QC/OAK and live authorities unavailable;
      no applicable reader
    evidence_ids:
    - support-2688-owner
    - support-2688-capture
    - support-2688-intake
    - support-2688-intake-execution
    - support-2688-intake-acceptance
    - support-2688-plan-acceptance
    - support-2688-source-reading
    - support-2688-source-notes
    - support-2688-diagnostic-acceptance
    - support-2688-molecular-reading
    - support-2688-native-gates
    - support-2688-reader-applicability
  assessment_id: support-2688-completion
  target_ids:
  - naturalproductmech:mibig-b2ae90066f
  evidence_ids:
  - support-2688-owner
  - support-2688-capture
  - support-2688-intake
  - support-2688-intake-execution
  - support-2688-intake-acceptance
  - support-2688-plan-acceptance
  - support-2688-source-reading
  - support-2688-source-notes
  - support-2688-diagnostic-acceptance
  - support-2688-molecular-reading
  - support-2688-native-gates
  - support-2688-reader-applicability
  outcome: unknown
  summary: The whole selected owner/history, every saved source payload and negative
    frame, both complete saved molecular forms and actual intake claims have been
    read. Input hashes and ownership declarations match the accepted plan; this is
    distinct from reading entire corpus files. Positive conclusions concern retained
    mapping, source-grade fidelity and bounded encoded topology. Five local checks
    passed, but full QC/OAK and live authorities are unavailable. No maintained reader
    applies, so completion remains partial.
findings: []
actions: []
limitations:
- Retained owner, source rows and saved diagnostics only; no fresh primary-paper,
  taxonomy, sequence or external identifier resolution.
- The heronamide-b-2 and heronamide-b owners retain different full keys and opposite
  geometry at one encoded alkene. The empty cross-form map and amide/imidic representation
  difference do not authorize identity collapse or source transfer.
- Eight undefined-stereo warnings remain unassigned to owners. Full QC and OAK are
  unavailable; recorded grades, citation grain, model predictions and existing source
  discussions retain their stated limits.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The complete owner/history, both saved molecular tables and all owner-local saved
  query frames were personally read. Physical row placements are not independent experiments
  and input hash verification is not whole-corpus scientific reading.
- This review proposes no source, generated record, curation status or history edit.
  No outbound request, new molecular parse or target execution was performed in this
  authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-269
```
