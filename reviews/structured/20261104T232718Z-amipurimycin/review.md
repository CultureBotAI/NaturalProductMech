# Local evidence review: amipurimycin

- Review: 20261104T232718Z-amipurimycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T22:54:09.217744Z
- Finished UTC: 2026-11-04T23:27:18.177199Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The stereo-unspecified amipurimycin entry retains its distinct full key and weaker source-locus grades. Tautomer-sensitive canonical mismatches and the bounded N-glycosidic topology/model-flag concern do not support a source edit or name-based merge.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2480; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-87448967a3 | data/natural_products/unclassified/amipurimycin.yaml | generated | amipurimycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-87448967a3 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-87448967a3 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-87448967a3 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-87448967a3 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-87448967a3 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-87448967a3 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-87448967a3 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-87448967a3 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and exact source correspondence

identity: supported. Targets: naturalproductmech:mibig-87448967a3.

Minted naturalproductmech:mibig-87448967a3, full key BHAUQSKSOITMND-UHFFFAOYSA-N and CID162956 correspond to BGC0001957 compound 1. The selected BGC0002054 entry shares the name and first key block but has KVKUBTPSSA stereochemistry. Exact reciprocal saved comparison shows eight unspecified tetrahedra here versus eight specified there, with matching nonisomeric strings within each representation. Natural equivalence, duplicate status and transfer of evidence are not established.

### Stored forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-87448967a3.

Both forms parse as neutral C20H29N7O8, 35 atoms/38 bonds. Eight comparisons agree, both canonical SMILES comparisons are false and the direct atom map is empty. Amide→C(OH)=N and heteroaromatic amino/imino changes account for bounded representation differences; reconstruction adds two unspecified double-bond candidates. All eight tetrahedral candidates remain unspecified, consistent with retained stereo_complete=false. The terminal acid and saturated C5O ring persist. Shared normalized identifiers do not prove a fixed microstate, full-graph or natural identity.

### Producer and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-87448967a3.

BGC0001957 version 4 retains S. novoguineensis (2586640) as SOURCE_ASSERTION and MH534949.1 as CLUSTER_UNSTATED, with no owner locus coordinates or evidence methods. Source PKS class is retained. The other selected amipurimycin locus has stronger characterized/demonstrated grades and different classes; those claims are not transferred to this entry.

### Citation tier and history scope

evidence: supported. Targets: naturalproductmech:mibig-87448967a3.

DOI10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS uppercase spelling is the same DOI and cannot be counted as an independent producer/occurrence publication. An entry-level citation supplies neither an assay measurement nor a stronger locus grade. All three history events are seed provenance; no fresh primary study was examined.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-87448967a3.

One S. novoguineensis LOTUS occurrence is retained independently of the producer-evidence field. The owner has no bioactivities or molecular_targets, and the exact retained assay/target frames are empty. These predicates establish bounded inventory absence only. The stereospecified companion supplies comparison context, not transferable biological activity or proof of native identity.

### Versioned classification applicability

consistency: concern. Targets: naturalproductmech:mibig-87448967a3.

The versioned classifier has empty family arrays and is_glycoside=false. The saved hydroxylated C5O ring has the same direct carbon 14–heteroaromatic N16 linkage as the stereospecified selected entry, supporting a bounded N-glycosidic topology concern when interpreting the flag. No sugar identity, anomer or natural configuration is assigned from this partially specified structure. Model applicability remains separate from source correctness.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-87448967a3.

The complete owner and three history events, all nine selected source frames, 38 accepted canonical input placements including reciprocal comparison, and both original molecular forms were read. No maintained-reader route applies. Review remains partial/pass_with_limitations because full QC/OAK and fresh primary/taxonomic/natural-state verification are unavailable; no finding, action or source/status/history edit is supported.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2480-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/amipurimycin.yaml; Whole current plaintext including complete curation_history | supports | Complete owner and all 3 history events personally read; current exact bytes retained. |
| support-2480-capture | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete raw captured owner and history; graph, pathway, component, molecular-target and bioactivity roots are absent. |
| support-2480-grounding-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/9/owner_document/identifier; /records/9/owner_document/label; /records/9/owner_document/chemical_structure; /records/9/owner_document/source_concepts; /records/9/owner_document/xrefs; /records/9/owner_document/grounding_status; /records/9/owner_document/grounding_notes | supports | Retained identifier, full key, source structure and exact present grounding/cross-reference/discussion fields; fresh identity verification is not implied. |
| support-2480-origin-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/9/owner_document/producer_organisms; /records/9/owner_document/biosynthetic_gene_clusters; /records/9/owner_document/producer_taxon_groups | supports | Complete current producer/locus assertions, separate grades and coordinates/methods where present. The implemented-curation scope is separately evidenced. |
| support-2480-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete occurrence assertions and absent bioactivities/molecular_targets; any locus methods or biosynthetic mechanism are separate from pharmacological activity. |
| support-2480-classification-owner | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/9/owner_document/np_pathway; /records/9/owner_document/np_classification; /records/9/owner_document/bgc_class; /records/9/owner_document/biosynthesis_origin | supports | Versioned model output and UNCLASSIFIED filing are separate from retained source BGC or compound-class assertions. |
| support-2480-direct-contexts | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-target-input-plan-001.json; /records/9/proposed_companion_paths; /records/9/direct_companion_predicates; /records/9/identity_comparison_paths; /records/9/additional_context_roles | context_only | Exact direct-BGC context and separately labelled selected-owner comparison roles. A shared locus/name does not establish identity or transfer evidence. |
| support-2480-intake | /private/tmp/npm-review-work/shared-next-batch248/intakes/2480-inspect-001.json; /targets; /source | supports | Actual canonical target, input roles and ownership are preserved. |
| support-2480-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch248/root-intake-acceptance-001.json; /status; /records/9; /source_plan; /verification | supports | ROOT accepts this original intake and its exact composed source plan. |
| support-2480-intake-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/support-prep/support-current248-last-five-molecular-intake-reading-001.json; /reading; /records/4/target; /records/4/intake; /coverage | supports | Support personally read all five target/ownership documents and 192 input placements across 45 paths. |
| support-2480-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch248/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local source inventory; extraction is not primary verification. |
| support-2480-plan | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-target-input-plan-001.json; /records/9/proposed_input_paths; /records/9/proposed_input_count | supports | Actual input map agrees with this canonical intake. |
| support-2480-plan-execution | /private/tmp/npm-review-work/shared-next-batch248/bgc-source-plan-execution-001.json; /plan; /exit_code; /original_terminal; /original_tools | supports | Original composer exited zero once; exact plan authority is separately retained. |
| support-2480-source-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/support-prep/support-current248-assigned-source-reading-001.json; /scope; /contexts; /reading; /cautions; /verification; /limits | supports | Support personally read contexts 11–14: 36 frames, 14 positive rows and 188 fields, with exact physical/current joins. Other partitions remain attributed. |
| support-2480-ROOT-source-reading | /private/tmp/npm-review-work/shared-next-batch248/root-current248-source-row-reading-001.json; /context_indices; /context_paths; /named_query_frames; /positive_row_placements; /positive_row_fields; /whole_payload_readings; /scientific_cautions | context_only | ROOT personally read contexts 0–4 and 10, including all Albonoursin payloads: 54 frames/63 rows/615 fields. Retained source labels, raw grades and curation overlay remain distinct. |
| support-2480-source-notes | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes preserve disjoint BGC 38/ROOT 63/Support 14/Native 0 positive-row credits and exact source/curation boundaries. |
| support-2480-molecular-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/support-prep/support-current248-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/4; /representation_notes; /limits | supports | Support personally read all ten forms: 326 atom rows/352 bond rows, all stereo/motif/map fields and 192 intake placements. Four canonical mismatch pairs and empty maps are retained; no reparse. |
| support-2480-selected-identity-comparison | /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json; /records/8/owner_document; /records/9/owner_document | context_only | The two selected amipurimycins retain distinct full keys/stereo and distinct BGC source/producer/locus/citation grades; exact comparison does not establish natural equivalence. |
| support-2480-encoded-pair-comparison | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/smiles; /records/8/inchi; /records/9/declared_structure; /records/9/smiles; /records/9/inchi | context_only | Complete saved tables show equal nonisomeric strings and bond tables within each representation, with eight specified versus eight unspecified tetrahedral atom labels. No new parse or natural equivalence is asserted. |
| support-2480-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/32 | context_only | Complete relevant retained cache stanzas preserve taxon names and synonyms; they do not independently establish a producing strain or fresh taxonomy. |
| support-2480-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation | context_only | Native whole-cache/route reading remains attributed; Support separately read nine relevant complete selected stanzas. |
| support-2480-curation-scope | /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | Native exact scan identifies the existing Albonoursin locus override only. Other lexical hits are unrelated; assay exclusions do not apply to the retained tuples/sentinel. |
| support-2480-chemistry | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope; /records/9/comparisons; /records/9/atom_correspondence | supports | Eight true comparisons, two false canonical SMILES comparisons and an empty direct atom map; normalized identifiers do not establish fixed-form identity. |
| support-2480-topology | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence | supports | Both forms parse as neutral C20H29N7O8, 35 atoms/38 bonds. Eight comparisons agree, both canonical SMILES comparisons are false and the direct atom map is empty. Amide→C(OH)=N and heteroaromatic amino/imino changes account for bounded representation differences; reconstruction adds two unspecified double-bond candidates. All eight tetrahedral candidates remain unspecified, consistent with retained stereo_complete=false. The terminal acid and saturated C5O ring persist. Shared normalized identifiers do not prove a fixed microstate, full-graph or natural identity. |
| support-2480-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/9; /global_warning_count; /interpretation_boundary | supports | ROOT accepts this actual original diagnostic result with false comparisons where present and eight global unassigned warnings. |
| support-2480-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, zero exit and streams, no retry or external request. |
| support-2480-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Eight original undefined-stereo warnings are retained globally, unassigned to individual records. |
| support-2480-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2480-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2480-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2480-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2480-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame contains 1 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Physical row 2268: BGC0001957 version 4, amipurimycin; Streptomyces novoguineensis SOURCE_ASSERTION, locus CLUSTER_UNSTATED; DOI:10.1021/jacs.9b03021 at ENTRY scope. Complete retained structure, coordinates, methods and classes remain in this exact raw row. |
| support-2480-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 2268 | context_only | Every retained field joins these current physical table rows; primary reading credit remains disjoint. |
| support-2480-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame contains 0 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame contains 1 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Physical row 518: Streptomyces novoguineensis (NCBITaxon:2586640), DOI:10.1021/JACS.9B03021; occurrence, not demonstrated production or independent-study proof. |
| support-2480-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 518 | context_only | Every retained field joins these current physical table rows; primary reading credit remains disjoint. |
| support-2480-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame contains 0 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame contains 1 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/npclassifier/matches/0 | supports | Physical row 171: npclassifier.gnps2.org@2026-09-07: //, glycoside=false; model assertion only. |
| support-2480-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 171 | context_only | Every retained field joins these current physical table rows; primary reading credit remains disjoint. |
| support-2480-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame contains 0 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame contains 0 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame contains 0 positive placements; any zero is bounded to its retained exact predicate. |
| support-2480-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame contains 0 positive placements; any zero is bounded to its retained exact predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-248/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-248/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-248/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-248/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-248/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; primary papers, fresh taxonomy, native sequences/constructs and natural stereochemistry were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. Both canonical SMILES comparisons are false and the direct atom map is empty; representation-specific motifs and any unspecified stereo remain explicit.
- Eight undefined-stereo warnings are global and unassigned. Producer, occurrence, locus, citation, model and assay scopes remain distinct; no source/status/history edit is proposed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole selected raw/history and complete paired molecular tables were personally read. Support source credit14/188/36 remains distinct from ROOT63/615/54 and BGC38/493/45; Native0 source rows.
- Support read all192 selected input placements45paths and nine complete relevant cache stanzas. Native cache/curation routes and ROOT companion/Albonoursin payload readings remain attributed.
- Support operated canonical intakes; Native operated original diagnostic/reader under ROOT delegation. Historical execution observer labels do not change attribution. All evidence timestamps use literal UTC Z.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T232718Z-amipurimycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: amipurimycin'
started_at: '2026-11-04T22:54:09.217744Z'
finished_at: '2026-11-04T23:27:18.177199Z'
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
summary: The stereo-unspecified amipurimycin entry retains its distinct full key and
  weaker source-locus grades. Tautomer-sensitive canonical mismatches and the bounded
  N-glycosidic topology/model-flag concern do not support a source edit or name-based
  merge.
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
  - path: data/natural_products/unclassified/amipurimycin-2.yaml
    sha256: 5a54e1132fd290f3ce55e9c462e243a4324207f11736a4f9c54f51bf91966c29
    role: context
  - path: data/natural_products/unclassified/amipurimycin.yaml
    sha256: 6148ccbdd0371f4ffbfd052ea2b731da6eb25ec189802f730e1232bb846f58ac
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
  selection: Campaign path order 2480; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-87448967a3
targets:
- target_id: naturalproductmech:mibig-87448967a3
  path: data/natural_products/unclassified/amipurimycin.yaml
  label: amipurimycin
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
    path: data/natural_products/unclassified/amipurimycin-2.yaml
    role: Explicit ROOT-requested already-selected encoded identity comparison only;
      not a census companion or extra source-query context.
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
  - naturalproductmech:mibig-87448967a3
  command: just validate-strict data/natural_products/unclassified/aflatoxin-b1.yaml
    data/natural_products/unclassified/aflatoxin-g1.yaml data/natural_products/unclassified/aflatoxin.yaml
    data/natural_products/unclassified/akml-a.yaml data/natural_products/unclassified/akml-b.yaml
    data/natural_products/unclassified/albonoursin.yaml data/natural_products/unclassified/alchivemycin-b.yaml
    data/natural_products/unclassified/althiomycin.yaml data/natural_products/unclassified/amipurimycin-2.yaml
    data/natural_products/unclassified/amipurimycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-248/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-87448967a3
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-248/validate-all-001.tsv
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
  - naturalproductmech:mibig-87448967a3
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
  - naturalproductmech:mibig-87448967a3
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
  - naturalproductmech:mibig-87448967a3
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-248/review-queue-001.tsv
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
  - naturalproductmech:mibig-87448967a3
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-87448967a3
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-87448967a3
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2480-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/amipurimycin.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Complete owner and all 3 history events personally read; current exact
    bytes retained.
  snapshot_sha256: 6148ccbdd0371f4ffbfd052ea2b731da6eb25ec189802f730e1232bb846f58ac
- evidence_id: support-2480-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Complete raw captured owner and history; graph, pathway, component, molecular-target
    and bioactivity roots are absent.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: support-2480-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/9/owner_document/identifier; /records/9/owner_document/label;
    /records/9/owner_document/chemical_structure; /records/9/owner_document/source_concepts;
    /records/9/owner_document/xrefs; /records/9/owner_document/grounding_status; /records/9/owner_document/grounding_notes
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Retained identifier, full key, source structure and exact present grounding/cross-reference/discussion
    fields; fresh identity verification is not implied.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: support-2480-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/9/owner_document/producer_organisms; /records/9/owner_document/biosynthetic_gene_clusters;
    /records/9/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Complete current producer/locus assertions, separate grades and coordinates/methods
    where present. The implemented-curation scope is separately evidenced.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: support-2480-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Complete occurrence assertions and absent bioactivities/molecular_targets;
    any locus methods or biosynthetic mechanism are separate from pharmacological
    activity.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: support-2480-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/9/owner_document/np_pathway; /records/9/owner_document/np_classification;
    /records/9/owner_document/bgc_class; /records/9/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Versioned model output and UNCLASSIFIED filing are separate from retained
    source BGC or compound-class assertions.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: support-2480-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-target-input-plan-001.json
  locator: /records/9/proposed_companion_paths; /records/9/direct_companion_predicates;
    /records/9/identity_comparison_paths; /records/9/additional_context_roles
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Exact direct-BGC context and separately labelled selected-owner comparison
    roles. A shared locus/name does not establish identity or transfer evidence.
  snapshot_sha256: 0c3bd623561801ca680bca9af98bbd1e21a2f7dc5ca0bc13a2e8e8654159d436
- evidence_id: support-2480-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/intakes/2480-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Actual canonical target, input roles and ownership are preserved.
  snapshot_sha256: 671d2426f0ba496ad34b45c4264e9b3280d23448ad1f4f043c889ba238852abc
- evidence_id: support-2480-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-intake-acceptance-001.json
  locator: /status; /records/9; /source_plan; /verification
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: ROOT accepts this original intake and its exact composed source plan.
  snapshot_sha256: f87f72eb2a281d4f80f9b05b6da75a212ac84262eb85a2c7deda4880bf4cb3ac
- evidence_id: support-2480-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/support-prep/support-current248-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/4/target; /records/4/intake; /coverage
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Support personally read all five target/ownership documents and 192 input
    placements across 45 paths.
  snapshot_sha256: b774464c7cf9acc47211a52a04105b9d1dbdc4bcfe4019f410d2b9f310d7eb2d
- evidence_id: support-2480-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: ROOT accepts the original retained local source inventory; extraction is
    not primary verification.
  snapshot_sha256: a34291d2ddf9b4f2e37d581987153174963345d545fd7de0e33c10c431be803d
- evidence_id: support-2480-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-target-input-plan-001.json
  locator: /records/9/proposed_input_paths; /records/9/proposed_input_count
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Actual input map agrees with this canonical intake.
  snapshot_sha256: 0c3bd623561801ca680bca9af98bbd1e21a2f7dc5ca0bc13a2e8e8654159d436
- evidence_id: support-2480-plan-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/bgc-source-plan-execution-001.json
  locator: /plan; /exit_code; /original_terminal; /original_tools
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Original composer exited zero once; exact plan authority is separately
    retained.
  snapshot_sha256: d40c3e02d03edac5e9b1db9d96b102c645797330a4a7337c53b8cbb9f3e24fce
- evidence_id: support-2480-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/support-prep/support-current248-assigned-source-reading-001.json
  locator: /scope; /contexts; /reading; /cautions; /verification; /limits
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: 'Support personally read contexts 11–14: 36 frames, 14 positive rows and
    188 fields, with exact physical/current joins. Other partitions remain attributed.'
  snapshot_sha256: c996430b58d01cbad9459a509a40ea8f9f240de9c819ca5efd6a0bfd3d6ae3eb
- evidence_id: support-2480-ROOT-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/root-current248-source-row-reading-001.json
  locator: /context_indices; /context_paths; /named_query_frames; /positive_row_placements;
    /positive_row_fields; /whole_payload_readings; /scientific_cautions
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: 'ROOT personally read contexts 0–4 and 10, including all Albonoursin payloads:
    54 frames/63 rows/615 fields. Retained source labels, raw grades and curation
    overlay remain distinct.'
  snapshot_sha256: b03407dab38283949dfdecd53d2a3308b5b7e0d4fafcb1fb22adb26c4ad1277d
- evidence_id: support-2480-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Joint notes preserve disjoint BGC 38/ROOT 63/Support 14/Native 0 positive-row
    credits and exact source/curation boundaries.
  snapshot_sha256: 677fa47e38b38fd68d1bcf303c6c209b2f27162b6297c48aafdaf6faabdcd759
- evidence_id: support-2480-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/support-prep/support-current248-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/4; /representation_notes; /limits
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: 'Support personally read all ten forms: 326 atom rows/352 bond rows, all
    stereo/motif/map fields and 192 intake placements. Four canonical mismatch pairs
    and empty maps are retained; no reparse.'
  snapshot_sha256: b774464c7cf9acc47211a52a04105b9d1dbdc4bcfe4019f410d2b9f310d7eb2d
- evidence_id: support-2480-selected-identity-comparison
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248/owner-capture-DATA-001.json
  locator: /records/8/owner_document; /records/9/owner_document
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: The two selected amipurimycins retain distinct full keys/stereo and distinct
    BGC source/producer/locus/citation grades; exact comparison does not establish
    natural equivalence.
  snapshot_sha256: 3c6968de9a5f894cbd520a4e4890ecccd8eb0360df6238b8996bd8394401352c
- evidence_id: support-2480-encoded-pair-comparison
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/smiles; /records/8/inchi; /records/9/declared_structure;
    /records/9/smiles; /records/9/inchi
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Complete saved tables show equal nonisomeric strings and bond tables within
    each representation, with eight specified versus eight unspecified tetrahedral
    atom labels. No new parse or natural equivalence is asserted.
  snapshot_sha256: fe37d4f7a6c507b5efcc54c9e6513c21060d9243d2794faa75d700b3b100ee3b
- evidence_id: support-2480-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/32
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve taxon names and synonyms;
    they do not independently establish a producing strain or fresh taxonomy.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: support-2480-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Native whole-cache/route reading remains attributed; Support separately
    read nine relevant complete selected stanzas.
  snapshot_sha256: a707cc6012faf88e8edeaddd6023fcb24a8468c3cad108257ee28d4b602e0bf6
- evidence_id: support-2480-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/native-prep/native-current248-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Native exact scan identifies the existing Albonoursin locus override only.
    Other lexical hits are unrelated; assay exclusions do not apply to the retained
    tuples/sentinel.
  snapshot_sha256: 74baac5175595ad8100603064c8b260f4478e6f3df17e0e3bd7a5f882a763638
  search_scope: '{"selected_identifier": "naturalproductmech:mibig-87448967a3", "selected_full_key":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "scope": "Implemented retained tables/exact predicates,
    not universal absence."}'
- evidence_id: support-2480-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope;
    /records/9/comparisons; /records/9/atom_correspondence
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Eight true comparisons, two false canonical SMILES comparisons and an empty
    direct atom map; normalized identifiers do not establish fixed-form identity.
  snapshot_sha256: fe37d4f7a6c507b5efcc54c9e6513c21060d9243d2794faa75d700b3b100ee3b
- evidence_id: support-2480-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/smiles; /records/9/inchi; /records/9/comparisons;
    /records/9/atom_correspondence
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Both forms parse as neutral C20H29N7O8, 35 atoms/38 bonds. Eight comparisons
    agree, both canonical SMILES comparisons are false and the direct atom map is
    empty. Amide→C(OH)=N and heteroaromatic amino/imino changes account for bounded
    representation differences; reconstruction adds two unspecified double-bond candidates.
    All eight tetrahedral candidates remain unspecified, consistent with retained
    stereo_complete=false. The terminal acid and saturated C5O ring persist. Shared
    normalized identifiers do not prove a fixed microstate, full-graph or natural
    identity.
  snapshot_sha256: fe37d4f7a6c507b5efcc54c9e6513c21060d9243d2794faa75d700b3b100ee3b
- evidence_id: support-2480-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/9; /global_warning_count; /interpretation_boundary
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: ROOT accepts this actual original diagnostic result with false comparisons
    where present and eight global unassigned warnings.
  snapshot_sha256: 41385e734709ffb4be37d705ba14138074f919e8ec530b5fe226af2a54f084a3
- evidence_id: support-2480-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Exact original diagnostic command/source, zero exit and streams, no retry
    or external request.
  snapshot_sha256: 50e6d82d0a03ece4185009e6997df38fc53c2ee4a2e5ee4731557c1554fcffbe
- evidence_id: support-2480-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch248/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Eight original undefined-stereo warnings are retained globally, unassigned
    to individual records.
  snapshot_sha256: 891b2e757b4f1083afca55d3a26a0b5f6d0e4357ada06900ea0b41d78d619592
- evidence_id: support-2480-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2480-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2480-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2480-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2480-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved mibig_compounds frame contains 1 positive placements; any zero is
    bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/mibig_compounds",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: 'Physical row 2268: BGC0001957 version 4, amipurimycin; Streptomyces novoguineensis
    SOURCE_ASSERTION, locus CLUSTER_UNSTATED; DOI:10.1021/jacs.9b03021 at ENTRY scope.
    Complete retained structure, coordinates, methods and classes remain in this exact
    raw row.'
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: support-2480-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 2268
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Every retained field joins these current physical table rows; primary reading
    credit remains disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2480-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved chebi_structures frame contains 0 positive placements; any zero is
    bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/chebi_structures",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved lotus_occurrences frame contains 1 positive placements; any zero
    is bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: 'Physical row 518: Streptomyces novoguineensis (NCBITaxon:2586640), DOI:10.1021/JACS.9B03021;
    occurrence, not demonstrated production or independent-study proof.'
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: support-2480-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 518
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Every retained field joins these current physical table rows; primary reading
    credit remains disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2480-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame contains 0 positive placements; any
    zero is bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved npclassifier frame contains 1 positive placements; any zero is bounded
    to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/npclassifier",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: 'Physical row 171: npclassifier.gnps2.org@2026-09-07: //, glycoside=false;
    model assertion only.'
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
- evidence_id: support-2480-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 171
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: context_only
  summary: Every retained field joins these current physical table rows; primary reading
    credit remains disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2480-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved pubchem_bioassay frame contains 0 positive placements; any zero is
    bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved bindingdb_targets frame contains 0 positive placements; any zero
    is bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame contains 0 positive placements; any
    zero is bounded to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "BHAUQSKSOITMND-UHFFFAOYSA-N", "saved_frame": "/contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: support-2480-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch248-tentative/bgc-prep/bgc-conditional248-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T23:20:10.471363Z'
  support: supports
  summary: Saved chebi_origins frame contains 0 positive placements; any zero is bounded
    to its retained exact predicate.
  snapshot_sha256: d1650c0bd0f80538126f9bcd863b5b67bedfa93269faaee75adfd76e151abc00
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/14/source_scope_inventory/joins/chebi_origins",
    "scope": "Retained local inventory, no replay or universal absence claim."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:00:05.428362Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 05f7ff44ff39609faa785f7d8316778db38b3e466a7b42ac04af854d325189d9
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:00:29.630261Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 573bb35b53b63fe06f28e8a2fde2228099a315c85116ab728b231cb78ca10e31
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:00:48.761900Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:01:22.418928Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-248/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-248/native-current248-five-gates-execution-001.json
  accessed_at: '2026-11-04T23:01:34.024377Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: aa37a5e7f7dca8035ff37f45b3abcecacfe21927b7db12caf18af4a107e9a98d
assessments:
- area: identity
  topic: Retained identity and exact source correspondence
  outcome: supported
  summary: Minted naturalproductmech:mibig-87448967a3, full key BHAUQSKSOITMND-UHFFFAOYSA-N
    and CID162956 correspond to BGC0001957 compound 1. The selected BGC0002054 entry
    shares the name and first key block but has KVKUBTPSSA stereochemistry. Exact
    reciprocal saved comparison shows eight unspecified tetrahedra here versus eight
    specified there, with matching nonisomeric strings within each representation.
    Natural equivalence, duplicate status and transfer of evidence are not established.
  assessment_id: support-2480-identity
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-grounding-owner
  - support-2480-chemistry
  - support-2480-direct-contexts
  - support-2480-source-reading
  - support-2480-ROOT-source-reading
  - support-2480-query-chebi_structures
  - support-2480-source-mibig_compounds-0
  - support-2480-selected-identity-comparison
  - support-2480-encoded-pair-comparison
  dimensions:
  - name: standard_inchi_key
    value: BHAUQSKSOITMND-UHFFFAOYSA-N; retained full key, not independent natural
      identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2480-grounding-owner
    - support-2480-chemistry
    - support-2480-direct-contexts
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-query-chebi_structures
    - support-2480-source-mibig_compounds-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
  - name: grounding_scope
    value: Minted naturalproductmech:mibig-87448967a3, full key BHAUQSKSOITMND-UHFFFAOYSA-N
      and CID162956 correspond to BGC0001957 compound 1. The selected BGC0002054 entry
      shares the name and first key block but has KVKUBTPSSA stereochemistry. Exact
      reciprocal saved comparison shows eight unspecified tetrahedra here versus eight
      specified there, with matching nonisomeric strings within each representation.
      Natural equivalence, duplicate status and transfer of evidence are not established.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2480-grounding-owner
    - support-2480-chemistry
    - support-2480-direct-contexts
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-query-chebi_structures
    - support-2480-source-mibig_compounds-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
- area: representation
  topic: Stored forms and stereochemistry
  outcome: supported
  summary: Both forms parse as neutral C20H29N7O8, 35 atoms/38 bonds. Eight comparisons
    agree, both canonical SMILES comparisons are false and the direct atom map is
    empty. Amide→C(OH)=N and heteroaromatic amino/imino changes account for bounded
    representation differences; reconstruction adds two unspecified double-bond candidates.
    All eight tetrahedral candidates remain unspecified, consistent with retained
    stereo_complete=false. The terminal acid and saturated C5O ring persist. Shared
    normalized identifiers do not prove a fixed microstate, full-graph or natural
    identity.
  assessment_id: support-2480-representation
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-grounding-owner
  - support-2480-chemistry
  - support-2480-topology
  - support-2480-molecular-reading
  - support-2480-diagnostic-acceptance
  - support-2480-structure-schema
  - support-2480-stereo-method
  - support-2480-selected-identity-comparison
  - support-2480-encoded-pair-comparison
  dimensions:
  - name: stereochemistry_scope
    value: Both forms parse as neutral C20H29N7O8, 35 atoms/38 bonds. Eight comparisons
      agree, both canonical SMILES comparisons are false and the direct atom map is
      empty. Amide→C(OH)=N and heteroaromatic amino/imino changes account for bounded
      representation differences; reconstruction adds two unspecified double-bond
      candidates. All eight tetrahedral candidates remain unspecified, consistent
      with retained stereo_complete=false. The terminal acid and saturated C5O ring
      persist. Shared normalized identifiers do not prove a fixed microstate, full-graph
      or natural identity.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2480-grounding-owner
    - support-2480-chemistry
    - support-2480-topology
    - support-2480-molecular-reading
    - support-2480-diagnostic-acceptance
    - support-2480-structure-schema
    - support-2480-stereo-method
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
  - name: representation_correspondence
    value: Both forms parse as neutral C20H29N7O8, 35 atoms/38 bonds. Eight comparisons
      agree, both canonical SMILES comparisons are false and the direct atom map is
      empty. Amide→C(OH)=N and heteroaromatic amino/imino changes account for bounded
      representation differences; reconstruction adds two unspecified double-bond
      candidates. All eight tetrahedral candidates remain unspecified, consistent
      with retained stereo_complete=false. The terminal acid and saturated C5O ring
      persist. Shared normalized identifiers do not prove a fixed microstate, full-graph
      or natural identity.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2480-grounding-owner
    - support-2480-chemistry
    - support-2480-topology
    - support-2480-molecular-reading
    - support-2480-diagnostic-acceptance
    - support-2480-structure-schema
    - support-2480-stereo-method
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: BGC0001957 version 4 retains S. novoguineensis (2586640) as SOURCE_ASSERTION
    and MH534949.1 as CLUSTER_UNSTATED, with no owner locus coordinates or evidence
    methods. Source PKS class is retained. The other selected amipurimycin locus has
    stronger characterized/demonstrated grades and different classes; those claims
    are not transferred to this entry.
  assessment_id: support-2480-provenance
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-origin-owner
  - support-2480-source-reading
  - support-2480-ROOT-source-reading
  - support-2480-direct-contexts
  - support-2480-cached-taxonomy
  - support-2480-taxonomy-reading
  - support-2480-curation-scope
  - support-2480-source-mibig_compounds-0
  - support-2480-source-lotus_occurrences-0
  - support-2480-selected-identity-comparison
  - support-2480-encoded-pair-comparison
  dimensions:
  - name: taxon_scope
    value: BGC0001957 version 4 retains S. novoguineensis (2586640) as SOURCE_ASSERTION
      and MH534949.1 as CLUSTER_UNSTATED, with no owner locus coordinates or evidence
      methods. Source PKS class is retained. The other selected amipurimycin locus
      has stronger characterized/demonstrated grades and different classes; those
      claims are not transferred to this entry.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2480-origin-owner
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-direct-contexts
    - support-2480-cached-taxonomy
    - support-2480-taxonomy-reading
    - support-2480-curation-scope
    - support-2480-source-mibig_compounds-0
    - support-2480-source-lotus_occurrences-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
  - name: producer_evidence
    value: BGC0001957 version 4 retains S. novoguineensis (2586640) as SOURCE_ASSERTION
      and MH534949.1 as CLUSTER_UNSTATED, with no owner locus coordinates or evidence
      methods. Source PKS class is retained. The other selected amipurimycin locus
      has stronger characterized/demonstrated grades and different classes; those
      claims are not transferred to this entry.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2480-origin-owner
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-direct-contexts
    - support-2480-cached-taxonomy
    - support-2480-taxonomy-reading
    - support-2480-curation-scope
    - support-2480-source-mibig_compounds-0
    - support-2480-source-lotus_occurrences-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
  - name: locus_evidence
    value: BGC0001957 version 4 retains S. novoguineensis (2586640) as SOURCE_ASSERTION
      and MH534949.1 as CLUSTER_UNSTATED, with no owner locus coordinates or evidence
      methods. Source PKS class is retained. The other selected amipurimycin locus
      has stronger characterized/demonstrated grades and different classes; those
      claims are not transferred to this entry.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2480-origin-owner
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-direct-contexts
    - support-2480-cached-taxonomy
    - support-2480-taxonomy-reading
    - support-2480-curation-scope
    - support-2480-source-mibig_compounds-0
    - support-2480-source-lotus_occurrences-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
- area: evidence
  topic: Citation tier and history scope
  outcome: supported
  summary: DOI10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS uppercase
    spelling is the same DOI and cannot be counted as an independent producer/occurrence
    publication. An entry-level citation supplies neither an assay measurement nor
    a stronger locus grade. All three history events are seed provenance; no fresh
    primary study was examined.
  assessment_id: support-2480-citations
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-owner
  - support-2480-origin-owner
  - support-2480-occurrence-activity-owner
  - support-2480-source-reading
  - support-2480-ROOT-source-reading
  - support-2480-direct-contexts
  - support-2480-source-mibig_compounds-0
  - support-2480-source-lotus_occurrences-0
  - support-2480-source-npclassifier-0
  - support-2480-selected-identity-comparison
  - support-2480-encoded-pair-comparison
  dimensions:
  - name: citation_scope
    value: DOI10.1021/jacs.9b03021 is ENTRY-level MIBiG attribution. The LOTUS uppercase
      spelling is the same DOI and cannot be counted as an independent producer/occurrence
      publication. An entry-level citation supplies neither an assay measurement nor
      a stronger locus grade. All three history events are seed provenance; no fresh
      primary study was examined.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2480-owner
    - support-2480-origin-owner
    - support-2480-occurrence-activity-owner
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-direct-contexts
    - support-2480-source-mibig_compounds-0
    - support-2480-source-lotus_occurrences-0
    - support-2480-source-npclassifier-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
- area: evidence
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: One S. novoguineensis LOTUS occurrence is retained independently of the
    producer-evidence field. The owner has no bioactivities or molecular_targets,
    and the exact retained assay/target frames are empty. These predicates establish
    bounded inventory absence only. The stereospecified companion supplies comparison
    context, not transferable biological activity or proof of native identity.
  assessment_id: support-2480-occurrence
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-occurrence-activity-owner
  - support-2480-direct-contexts
  - support-2480-cached-taxonomy
  - support-2480-taxonomy-reading
  - support-2480-curation-scope
  - support-2480-source-reading
  - support-2480-ROOT-source-reading
  - support-2480-query-lotus_occurrences
  - support-2480-query-chebi_origins
  - support-2480-query-cyanometdb_occurrences
  - support-2480-query-pubchem_bioassay
  - support-2480-query-bindingdb_targets
  - support-2480-query-antibioticmech_inchikeys
  - support-2480-source-lotus_occurrences-0
  - support-2480-selected-identity-comparison
  - support-2480-encoded-pair-comparison
  dimensions:
  - name: occurrence_scope
    value: One S. novoguineensis LOTUS occurrence is retained independently of the
      producer-evidence field. The owner has no bioactivities or molecular_targets,
      and the exact retained assay/target frames are empty. These predicates establish
      bounded inventory absence only. The stereospecified companion supplies comparison
      context, not transferable biological activity or proof of native identity.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2480-occurrence-activity-owner
    - support-2480-direct-contexts
    - support-2480-cached-taxonomy
    - support-2480-taxonomy-reading
    - support-2480-curation-scope
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-query-lotus_occurrences
    - support-2480-query-chebi_origins
    - support-2480-query-cyanometdb_occurrences
    - support-2480-query-pubchem_bioassay
    - support-2480-query-bindingdb_targets
    - support-2480-query-antibioticmech_inchikeys
    - support-2480-source-lotus_occurrences-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
  - name: assay_target_scope
    value: One S. novoguineensis LOTUS occurrence is retained independently of the
      producer-evidence field. The owner has no bioactivities or molecular_targets,
      and the exact retained assay/target frames are empty. These predicates establish
      bounded inventory absence only. The stereospecified companion supplies comparison
      context, not transferable biological activity or proof of native identity.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2480-occurrence-activity-owner
    - support-2480-direct-contexts
    - support-2480-cached-taxonomy
    - support-2480-taxonomy-reading
    - support-2480-curation-scope
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-query-lotus_occurrences
    - support-2480-query-chebi_origins
    - support-2480-query-cyanometdb_occurrences
    - support-2480-query-pubchem_bioassay
    - support-2480-query-bindingdb_targets
    - support-2480-query-antibioticmech_inchikeys
    - support-2480-source-lotus_occurrences-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
- area: consistency
  topic: Versioned classification applicability
  outcome: concern
  summary: The versioned classifier has empty family arrays and is_glycoside=false.
    The saved hydroxylated C5O ring has the same direct carbon 14–heteroaromatic N16
    linkage as the stereospecified selected entry, supporting a bounded N-glycosidic
    topology concern when interpreting the flag. No sugar identity, anomer or natural
    configuration is assigned from this partially specified structure. Model applicability
    remains separate from source correctness.
  assessment_id: support-2480-classification
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-classification-owner
  - support-2480-chemistry
  - support-2480-topology
  - support-2480-classification-seeder
  - support-2480-source-mibig_compounds-0
  - support-2480-source-npclassifier-0
  - support-2480-selected-identity-comparison
  - support-2480-encoded-pair-comparison
  dimensions:
  - name: classification_applicability
    value: The versioned classifier has empty family arrays and is_glycoside=false.
      The saved hydroxylated C5O ring has the same direct carbon 14–heteroaromatic
      N16 linkage as the stereospecified selected entry, supporting a bounded N-glycosidic
      topology concern when interpreting the flag. No sugar identity, anomer or natural
      configuration is assigned from this partially specified structure. Model applicability
      remains separate from source correctness.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2480-classification-owner
    - support-2480-chemistry
    - support-2480-topology
    - support-2480-classification-seeder
    - support-2480-source-mibig_compounds-0
    - support-2480-source-npclassifier-0
    - support-2480-selected-identity-comparison
    - support-2480-encoded-pair-comparison
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: The complete owner and three history events, all nine selected source frames,
    38 accepted canonical input placements including reciprocal comparison, and both
    original molecular forms were read. No maintained-reader route applies. Review
    remains partial/pass_with_limitations because full QC/OAK and fresh primary/taxonomic/natural-state
    verification are unavailable; no finding, action or source/status/history edit
    is supported.
  assessment_id: support-2480-completion
  target_ids:
  - naturalproductmech:mibig-87448967a3
  evidence_ids:
  - support-2480-owner
  - support-2480-capture
  - support-2480-intake
  - support-2480-intake-acceptance
  - support-2480-intake-reading
  - support-2480-inventory-acceptance
  - support-2480-plan
  - support-2480-plan-execution
  - support-2480-source-reading
  - support-2480-ROOT-source-reading
  - support-2480-source-notes
  - support-2480-molecular-reading
  - support-2480-diagnostic-acceptance
  - support-2480-diagnostic-execution
  - support-2480-diagnostic-stderr
  - support-2480-review-profile
  dimensions:
  - name: review_completion
    value: The complete owner and three history events, all nine selected source frames,
      38 accepted canonical input placements including reciprocal comparison, and
      both original molecular forms were read. No maintained-reader route applies.
      Review remains partial/pass_with_limitations because full QC/OAK and fresh primary/taxonomic/natural-state
      verification are unavailable; no finding, action or source/status/history edit
      is supported.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2480-owner
    - support-2480-capture
    - support-2480-intake
    - support-2480-intake-acceptance
    - support-2480-intake-reading
    - support-2480-inventory-acceptance
    - support-2480-plan
    - support-2480-plan-execution
    - support-2480-source-reading
    - support-2480-ROOT-source-reading
    - support-2480-source-notes
    - support-2480-molecular-reading
    - support-2480-diagnostic-acceptance
    - support-2480-diagnostic-execution
    - support-2480-diagnostic-stderr
    - support-2480-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; primary papers, fresh taxonomy, native sequences/constructs
  and natural stereochemistry were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. Both canonical SMILES comparisons are false
  and the direct atom map is empty; representation-specific motifs and any unspecified
  stereo remain explicit.
- Eight undefined-stereo warnings are global and unassigned. Producer, occurrence,
  locus, citation, model and assay scopes remain distinct; no source/status/history
  edit is proposed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole selected raw/history and complete paired molecular tables were personally
  read. Support source credit14/188/36 remains distinct from ROOT63/615/54 and BGC38/493/45;
  Native0 source rows.
- Support read all192 selected input placements45paths and nine complete relevant
  cache stanzas. Native cache/curation routes and ROOT companion/Albonoursin payload
  readings remain attributed.
- Support operated canonical intakes; Native operated original diagnostic/reader under
  ROOT delegation. Historical execution observer labels do not change attribution.
  All evidence timestamps use literal UTC Z.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-248
```
