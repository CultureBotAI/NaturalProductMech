# Local evidence review: burnettramic acid A

- Review: 20261105T092954Z-burnettramic-acid-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T08:20:00.304910Z
- Finished UTC: 2026-11-05T09:29:54.152021Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Burnettramic acid A has mutually consistent stored forms at the encoded stereochemical resolution. Heterologous locus evidence, the source-asserted native producer and genus-level occurrence remain separate. Cached naming and four undefined tetrahedral centers limit interpretation; coverage is partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2539; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-d33eb5850b | data/natural_products/unclassified/burnettramic-acid-a.yaml | generated | burnettramic acid A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-d33eb5850b | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-d33eb5850b | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-d33eb5850b | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-d33eb5850b | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-d33eb5850b | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-d33eb5850b | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-d33eb5850b | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-d33eb5850b | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and source grounding

identity: supported. Targets: naturalproductmech:mibig-d33eb5850b.

The MINTED identifier naturalproductmech:mibig-d33eb5850b, full key MGYSOSIDALEBDU-KOYWNODBSA-N and label burnettramic acid A agree with the retained MIBiG BGC0001857 version 4 row. Both stored forms reproduce the declared Standard InChI/key, C41H71NO12 and charge 0. The exact retained ChEBI frame is empty, so the historical minted-identity rationale is supported only within that bounded inventory. No fresh naming, glycoside-residue or natural-identity determination is made.

### Encoded stereochemistry and oxygenated topology

representation: supported. Targets: naturalproductmech:mibig-d33eb5850b.

Both forms contain 54 atoms and 56 bonds; all ten comparisons are true and the chirality-aware substructure match covers 54 atoms. This remains a local correspondence rather than independently established full graph or natural identity. Both forms have seven specified and four unspecified tetrahedral centers, with two specified double-bond geometries; stereo_complete=false is preserved. The topology includes an oxygenated long chain, a saturated six-membered C5O ring and a fused five-membered nitrogen-containing system with two carbonyls and an exocyclic enol. The C5O motif is a candidate sugar ring; it does not by itself assign a named sugar, biochemical position or anomer.

### Heterologous locus evidence and native producer scope

provenance: supported. Targets: naturalproductmech:mibig-d33eb5850b.

The MIBiG producer Aspergillus sp. CLMG-2019a (NCBITaxon:209559) remains SOURCE_ASSERTION. BGC0001857 version 4 separately carries CLUSTER_DEMONSTRATED through Heterologous expression at MK425157.1:1–28117. Demonstrating a locus in a heterologous system does not upgrade the named native producer or identify individual catalytic functions. The saved cache names 209559 Aspergillus alliaceus and includes Aspergillus burnettii/Petromyces synonyms; this retained naming relationship does not independently validate the source strain or fresh accepted taxonomy.

### Citation tier and naming provenance

evidence: supported. Targets: naturalproductmech:mibig-d33eb5850b.

The exact retained MIBiG row uses PMID:30735051 at ENTRY scope, repeated as DATABASE_ASSERTION on producer and locus. The LOTUS occurrence cites DOI:10.1021/ACS.ORGLETT.8B04042. These stable strings and their claim placements were read locally; original publication text and experimental details were not newly inspected. Two complete seed histories document import provenance. Cached synonyms do not supply an additional experiment or reconcile source strain naming by themselves.

### Genus occurrence and activity boundaries

evidence: supported. Targets: naturalproductmech:mibig-d33eb5850b.

The LOTUS occurrence is at Aspergillus genus NCBITaxon:5052 and does not independently establish CLMG-2019a or biosynthesis by taxon 209559. The complete owner has no bioactivity, molecular target, pathway or causal graph. Its saved exact-key assay/target frames are empty, a bounded inventory result rather than proof of inactivity. The separately retained producer and heterologous locus assertions are not replaced or broadened by that absence.

### Computed classification and observed motifs

consistency: supported. Targets: naturalproductmech:mibig-d33eb5850b.

NPClassifier predicts Amino acids and Peptides/Polyketides, Linear polyketides and 3-acyl tetramic acids, with is_glycoside=true. The long carbon chain, carbonyl-containing nitrogen ring and oxygen-linked C5O candidate ring make broad polyketide/tetramic/glycoside compatibility plausible at a topology level. The enol representation and partial stereochemistry limit any narrower chemical assignment, and the model labels do not establish biosynthetic provenance or named sugar identity. Source BGC OTHER/NRPS/PKS and pinned UNCLASSIFIED filing remain separate assertions.

### Review completion

completeness: supported. Targets: naturalproductmech:mibig-d33eb5850b.

The review covers the entire owner and two histories, accepted 37-input inspection, nine source frames with three positive rows, relevant complete cached stanzas and both complete saved molecular forms. No mechanism-reader call applies because the owner lacks those roots. The retained source grades and encoded structure are internally consistent at this scope. Primary experiments, exact native strain identity, fresh taxonomy and complete stereochemistry remain unverified; full QC and complete OAK coverage are unavailable. No source or status edit is made.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2539-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/burnettramic-acid-a.yaml; Whole current plaintext including complete curation_history | supports | Complete current selected owner and all 2 history events; no native record/status/history changes. |
| support-2539-capture | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete captured owner and every present root. Root presence and absence are retained exactly for this owner. |
| support-2539-grounding-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Exact retained identifier, full key, source structure and present source/grounding fields; no fresh natural identity validation. |
| support-2539-origin-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/producer_taxon_groups | supports | Complete producer and locus claims with separate evidence grades, methods, coordinates and source classes. |
| support-2539-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete owner preserves exact occurrence, activity, target and mechanism root presence or absence; production context is distinct from pharmacological activity. |
| support-2539-classification-owner | /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin | supports | Versioned model output, source BGC classes and UNCLASSIFIED filing remain separate assertions. |
| support-2539-direct-contexts | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates; /records/8/identity_comparison_paths; /records/8/additional_context_roles | context_only | Exact admitted direct-BGC context links and additional input roles; no extra selected-identity comparison roles. Companion facts do not become selected coverage. |
| support-2539-intake | /private/tmp/npm-review-work/shared-next-batch254/intakes/2539-inspect-001.json; /targets; /source | supports | Actual canonical target, source inputs and maintained ownership are retained. |
| support-2539-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch254/root-intake-acceptance-001.json; /status; /records/8; /source_plan; /verification | supports | ROOT accepts this original canonical intake and its exact source-plan/input joins. |
| support-2539-intake-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-last-five-molecular-intake-reading-001.json; /reading; /records/3/target; /records/3/intake; /coverage | supports | Support personally read all last-five canonical target/ownership documents; 192 current input placements across 46 paths are preserved. |
| support-2539-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch254/root-current254-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; this is not primary-paper verification. |
| support-2539-plan | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-target-input-plan-001.json; /records/8/proposed_input_paths; /records/8/proposed_input_count | supports | The accepted input map agrees exactly with this canonical intake. |
| support-2539-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch254/root-current254-source-plan-acceptance-001.json; /status; /verification | supports | ROOT accepts the actual254 plan and its current source-input joins. |
| support-2539-source-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-assigned-source-reading-002.json; /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows; /cautions; /reading_method | supports | Support read all five selected contexts: 45 frames, 16 rows and 196 fields. BGC reads the other seven contexts including two unselected companions; these retained database payloads do not confer primary-literature verification. |
| support-2539-source-notes | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes retain disjoint BGC 23/Support 16/Native 0 retained-row reading attribution, exact bounded interpretations and separately attributed cache/curation work. |
| support-2539-molecular-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/3; /representation_notes; /limits | supports | Support personally read all ten complete saved forms: 346 atom rows and 364 bond rows, all stereo/motif/map fields, and 192 assigned canonical input placements across 46 paths. No new molecular parse. |
| support-2539-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/6 | context_only | Complete relevant retained cache stanzas preserve names and synonyms; these do not prove native production, strain identity or fresh taxonomy. |
| support-2539-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation; /routes | context_only | Native complete cache and route interpretation remains attributed; owner-local retained stanzas carry only their exact saved fields. |
| support-2539-curation-scope | /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | The bounded implemented-table scan found no applicable exact replacement for these owners; unrelated lexical hits are not imported as owner evidence. |
| support-2539-chemistry | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope; /records/8/comparisons; /records/8/atom_correspondence | supports | All ten stored-form comparisons are true, with a complete-count chirality-aware substructure match. Full graph and natural identity remain expressly unestablished. |
| support-2539-topology | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles; /records/8/inchi | supports | Complete saved atom/bond/ring/stereo/motif tables retain representation-specific counts and stereochemical assignments; no new parse or natural-state claim. |
| support-2539-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /limits | supports | ROOT accepts the original stored-form diagnostic, preserving false canonical pairs for Burkholdac A/B in this assigned scope. Six warnings remain global and unattributed; no scientific identity upgrade follows. |
| support-2539-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, terminal exit and stream pins; no retry or external request. |
| support-2539-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Six retained undefined-stereo warnings remain global and unassigned to individual records. |
| support-2539-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2539-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2539-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2539-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2539-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained physical row 2183, all 25 fields: BGC0001857 version 4; Aspergillus sp. CLMG-2019a, producer SOURCE_ASSERTION, locus CLUSTER_DEMONSTRATED; PMID:30735051 at ENTRY scope. Source structure, methods and classes remain exact. |
| support-2539-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 2183 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2539-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained physical row 4406, all 6 fields: Aspergillus (NCBITaxon:5052), DOI:10.1021/ACS.ORGLETT.8B04042; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2539-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 4406 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2539-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained physical row 1479, all 7 fields: npclassifier.gnps2.org@2026-09-07: Amino acids and Peptides&#124;Polyketides/Linear polyketides/3-acyl tetramic acids; glycoside=true, model assertion only. |
| support-2539-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1479 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2539-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2539-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-254/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-254/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-254/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-254/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-254/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; original literature, fresh taxonomy/strain/sequence and natural-identity validation were not performed.
- Standardized agreement and substructure correspondence do not establish full natural graph identity or a uniquely fixed tautomer. Six diagnostic warnings remain global and unattributed.
- Source producer, occurrence, locus and computational classification assertions retain separate evidence grades and scopes.
- Full QC and complete OAK authority coverage remain unavailable; no source, native status or history edit was made.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete selected owners/history and ten saved molecular forms: 346 atom rows and 364 bond rows. Assigned retained-source reading covers 45 frames, 16 rows and 196 fields; BGC other-context and Native cache/curation work remain separately attributed.
- The accepted last-five canonical input scope is 192 placements across 46 paths. Source observations are retained database payloads, not newly inspected primary literature.
- No requests, source replays, molecular reparses or record edits were performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T092954Z-burnettramic-acid-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: burnettramic acid A'
started_at: '2026-11-05T08:20:00.304910Z'
finished_at: '2026-11-05T09:29:54.152021Z'
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
summary: Burnettramic acid A has mutually consistent stored forms at the encoded stereochemical
  resolution. Heterologous locus evidence, the source-asserted native producer and
  genus-level occurrence remain separate. Cached naming and four undefined tetrahedral
  centers limit interpretation; coverage is partial.
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
  - path: data/natural_products/unclassified/burnettramic-acid-a.yaml
    sha256: 2f6890eca5d2b4076214728b940212bbdef2b45b9f01a96c49c4872ebb684e3f
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
  selection: Campaign path order 2539; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-d33eb5850b
targets:
- target_id: naturalproductmech:mibig-d33eb5850b
  path: data/natural_products/unclassified/burnettramic-acid-a.yaml
  label: burnettramic acid A
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
  - naturalproductmech:mibig-d33eb5850b
  command: just validate-strict data/natural_products/unclassified/bolagladin-b.yaml
    data/natural_products/unclassified/bombyxamycin-a.yaml data/natural_products/unclassified/bombyxamycin-b.yaml
    data/natural_products/unclassified/brasiliamide-a.yaml data/natural_products/unclassified/brasiliamide-b.yaml
    data/natural_products/unclassified/brasiliamide-d.yaml data/natural_products/unclassified/burkholdac-a.yaml
    data/natural_products/unclassified/burkholdac-b.yaml data/natural_products/unclassified/burnettramic-acid-a.yaml
    data/natural_products/unclassified/caboxamycin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-254/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-d33eb5850b
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-254/validate-all-001.tsv
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
  - naturalproductmech:mibig-d33eb5850b
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
  - naturalproductmech:mibig-d33eb5850b
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
  - naturalproductmech:mibig-d33eb5850b
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-254/review-queue-001.tsv
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
  - naturalproductmech:mibig-d33eb5850b
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2539-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/burnettramic-acid-a.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Complete current selected owner and all 2 history events; no native record/status/history
    changes.
  snapshot_sha256: 2f6890eca5d2b4076214728b940212bbdef2b45b9f01a96c49c4872ebb684e3f
- evidence_id: support-2539-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Complete captured owner and every present root. Root presence and absence
    are retained exactly for this owner.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: support-2539-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Exact retained identifier, full key, source structure and present source/grounding
    fields; no fresh natural identity validation.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: support-2539-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/producer_taxon_groups
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Complete producer and locus claims with separate evidence grades, methods,
    coordinates and source classes.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: support-2539-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Complete owner preserves exact occurrence, activity, target and mechanism
    root presence or absence; production context is distinct from pharmacological
    activity.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: support-2539-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Versioned model output, source BGC classes and UNCLASSIFIED filing remain
    separate assertions.
  snapshot_sha256: 0d6d953ed1697c71964b21cd30e15cd3282875ed15517f3086bf7e9371adad7b
- evidence_id: support-2539-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates;
    /records/8/identity_comparison_paths; /records/8/additional_context_roles
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Exact admitted direct-BGC context links and additional input roles; no
    extra selected-identity comparison roles. Companion facts do not become selected
    coverage.
  snapshot_sha256: a3befc1a2429cf92f217bfdcb48cf72dda39597d5bcef98901a61c6b4bf6a8cb
- evidence_id: support-2539-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/intakes/2539-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Actual canonical target, source inputs and maintained ownership are retained.
  snapshot_sha256: 491458e5a3403d0be19ce475c9a549281cd66558cb91b219a01e9f16b524503d
- evidence_id: support-2539-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/root-intake-acceptance-001.json
  locator: /status; /records/8; /source_plan; /verification
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: ROOT accepts this original canonical intake and its exact source-plan/input
    joins.
  snapshot_sha256: 3d01634e3cce9bed07e36a8432d302136d52eccdbb824359475ecf6f1212fe4a
- evidence_id: support-2539-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/3/target; /records/3/intake; /coverage
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Support personally read all last-five canonical target/ownership documents;
    192 current input placements across 46 paths are preserved.
  snapshot_sha256: 24263713faf057395ec120af4286edecf6bbf392f6794a852d20e6e7e236e603
- evidence_id: support-2539-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/root-current254-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; this is not primary-paper
    verification.
  snapshot_sha256: ad4ce7f150c84932c203e46eb1a8aafad8016743ba4546ff5bc9484073d8a9a7
- evidence_id: support-2539-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-target-input-plan-001.json
  locator: /records/8/proposed_input_paths; /records/8/proposed_input_count
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: The accepted input map agrees exactly with this canonical intake.
  snapshot_sha256: a3befc1a2429cf92f217bfdcb48cf72dda39597d5bcef98901a61c6b4bf6a8cb
- evidence_id: support-2539-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/root-current254-source-plan-acceptance-001.json
  locator: /status; /verification
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: ROOT accepts the actual254 plan and its current source-input joins.
  snapshot_sha256: e1594023691731921ba30963fa0f4932281c6be5fd035aed39ff598a31f47e17
- evidence_id: support-2539-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-assigned-source-reading-002.json
  locator: /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows;
    /cautions; /reading_method
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: 'Support read all five selected contexts: 45 frames, 16 rows and 196 fields.
    BGC reads the other seven contexts including two unselected companions; these
    retained database payloads do not confer primary-literature verification.'
  snapshot_sha256: e7abc92530d744a395431cdbe65ec63f635830a000567cf6a4591fb43fa60044
- evidence_id: support-2539-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Joint notes retain disjoint BGC 23/Support 16/Native 0 retained-row reading
    attribution, exact bounded interpretations and separately attributed cache/curation
    work.
  snapshot_sha256: c4d71e9cc9feadeff58f0fc9381158cfb4104f7fdd285c7e4b90f63329e3d39a
- evidence_id: support-2539-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/support-prep/support-current254-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/3; /representation_notes; /limits
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: 'Support personally read all ten complete saved forms: 346 atom rows and
    364 bond rows, all stereo/motif/map fields, and 192 assigned canonical input placements
    across 46 paths. No new molecular parse.'
  snapshot_sha256: 24263713faf057395ec120af4286edecf6bbf392f6794a852d20e6e7e236e603
- evidence_id: support-2539-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/6
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve names and synonyms; these
    do not prove native production, strain identity or fresh taxonomy.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: support-2539-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation; /routes
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Native complete cache and route interpretation remains attributed; owner-local
    retained stanzas carry only their exact saved fields.
  snapshot_sha256: e800f0a3c08f18400a2cfe4155fa0172bf6395fd5df8425c6b7fab66333b7c6d
- evidence_id: support-2539-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/native-prep/native-current254-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: The bounded implemented-table scan found no applicable exact replacement
    for these owners; unrelated lexical hits are not imported as owner evidence.
  snapshot_sha256: eaab179e607165b23f47bdb4c8b4ca8cb1d86120bde0c2a65ceb9e7168438d5f
  search_scope: '{"selected_identifier": "naturalproductmech:mibig-d33eb5850b", "full_key":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "scope": "Eleven enumerated retained curation tables,
    nine implemented tables and exact predicates; ignored-file-independent inspection
    is bounded, not universal absence."}'
- evidence_id: support-2539-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope;
    /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: All ten stored-form comparisons are true, with a complete-count chirality-aware
    substructure match. Full graph and natural identity remain expressly unestablished.
  snapshot_sha256: 6d253472dfe91844e124611b6d35a253691ac62122bafe126fd25c6a10abc9e5
- evidence_id: support-2539-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles; /records/8/inchi
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif tables retain representation-specific
    counts and stereochemical assignments; no new parse or natural-state claim.
  snapshot_sha256: 6d253472dfe91844e124611b6d35a253691ac62122bafe126fd25c6a10abc9e5
- evidence_id: support-2539-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /limits
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: ROOT accepts the original stored-form diagnostic, preserving false canonical
    pairs for Burkholdac A/B in this assigned scope. Six warnings remain global and
    unattributed; no scientific identity upgrade follows.
  snapshot_sha256: 79eaee81115f631249c5c505fd5c06b17e54a99cf34d9887c4a841fdcfba8f0d
- evidence_id: support-2539-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Exact original diagnostic command/source, terminal exit and stream pins;
    no retry or external request.
  snapshot_sha256: bccd14404151f3fca2e384b55178c2eadc18bc707e81a6ee87b54875428e321b
- evidence_id: support-2539-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch254/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Six retained undefined-stereo warnings remain global and unassigned to
    individual records.
  snapshot_sha256: 3a36b094aa77adb4884fbc21954442cbcd91b83c56fc842e83043188b0c136e4
- evidence_id: support-2539-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2539-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2539-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2539-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2539-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/mibig_compounds",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: 'Complete retained physical row 2183, all 25 fields: BGC0001857 version
    4; Aspergillus sp. CLMG-2019a, producer SOURCE_ASSERTION, locus CLUSTER_DEMONSTRATED;
    PMID:30735051 at ENTRY scope. Source structure, methods and classes remain exact.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: support-2539-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 2183
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2539-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/chebi_structures",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved lotus_occurrences frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: 'Complete retained physical row 4406, all 6 fields: Aspergillus (NCBITaxon:5052),
    DOI:10.1021/ACS.ORGLETT.8B04042; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: support-2539-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 4406
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2539-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; a zero is
    bounded to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; a zero is bounded to
    its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/npclassifier",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: 'Complete retained physical row 1479, all 7 fields: npclassifier.gnps2.org@2026-09-07:
    Amino acids and Peptides|Polyketides/Linear polyketides/3-acyl tetramic acids;
    glycoside=true, model assertion only.'
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
- evidence_id: support-2539-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1479
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2539-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; a zero
    is bounded to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "MGYSOSIDALEBDU-KOYWNODBSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2539-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch254-tentative/bgc-prep/bgc-conditional254-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T09:17:03.804706Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: ac0f8ca1ade64a0e1414797cb8d98e9bd24ca2a57b7fb6a30a59deb9358a66e2
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/10/source_scope_inventory/joins/chebi_origins",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:25:53.433020Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: abde76276283777c27ca8f8cb3e993c54849c791d6c4c50a2b4b752ad4d63a34
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:26:19.438483Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 58288e3a0e8e1f4d32b86499befb70e491856d1d31f9ed7c4e9cdecd80cce987
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:26:39.349503Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:27:14.003223Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-254/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-254/native-current254-five-gates-execution-001.json
  accessed_at: '2026-11-05T08:27:26.021174Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: dcdc0438cb99a1ca1e0474633939a0e21f52b5ed7eed5055db8a09a5f824442f
assessments:
- area: identity
  topic: Retained identity and source grounding
  outcome: supported
  summary: The MINTED identifier naturalproductmech:mibig-d33eb5850b, full key MGYSOSIDALEBDU-KOYWNODBSA-N
    and label burnettramic acid A agree with the retained MIBiG BGC0001857 version
    4 row. Both stored forms reproduce the declared Standard InChI/key, C41H71NO12
    and charge 0. The exact retained ChEBI frame is empty, so the historical minted-identity
    rationale is supported only within that bounded inventory. No fresh naming, glycoside-residue
    or natural-identity determination is made.
  assessment_id: support-2539-identity
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-grounding-owner
  - support-2539-chemistry
  - support-2539-topology
  - support-2539-direct-contexts
  - support-2539-source-reading
  - support-2539-query-chebi_structures
  - support-2539-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: MGYSOSIDALEBDU-KOYWNODBSA-N; retained full key, not independently established
      natural identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2539-grounding-owner
    - support-2539-chemistry
    - support-2539-topology
    - support-2539-direct-contexts
    - support-2539-source-reading
    - support-2539-query-chebi_structures
    - support-2539-source-mibig_compounds-0
  - name: grounding_scope
    value: The MINTED identifier naturalproductmech:mibig-d33eb5850b, full key MGYSOSIDALEBDU-KOYWNODBSA-N
      and label burnettramic acid A agree with the retained MIBiG BGC0001857 version
      4 row. Both stored forms reproduce the declared Standard InChI/key, C41H71NO12
      and charge 0. The exact retained ChEBI frame is empty, so the historical minted-identity
      rationale is supported only within that bounded inventory. No fresh naming,
      glycoside-residue or natural-identity determination is made.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2539-grounding-owner
    - support-2539-chemistry
    - support-2539-topology
    - support-2539-direct-contexts
    - support-2539-source-reading
    - support-2539-query-chebi_structures
    - support-2539-source-mibig_compounds-0
- area: representation
  topic: Encoded stereochemistry and oxygenated topology
  outcome: supported
  summary: Both forms contain 54 atoms and 56 bonds; all ten comparisons are true
    and the chirality-aware substructure match covers 54 atoms. This remains a local
    correspondence rather than independently established full graph or natural identity.
    Both forms have seven specified and four unspecified tetrahedral centers, with
    two specified double-bond geometries; stereo_complete=false is preserved. The
    topology includes an oxygenated long chain, a saturated six-membered C5O ring
    and a fused five-membered nitrogen-containing system with two carbonyls and an
    exocyclic enol. The C5O motif is a candidate sugar ring; it does not by itself
    assign a named sugar, biochemical position or anomer.
  assessment_id: support-2539-representation
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-grounding-owner
  - support-2539-chemistry
  - support-2539-topology
  - support-2539-molecular-reading
  - support-2539-diagnostic-acceptance
  - support-2539-structure-schema
  - support-2539-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both forms contain 54 atoms and 56 bonds; all ten comparisons are true
      and the chirality-aware substructure match covers 54 atoms. This remains a local
      correspondence rather than independently established full graph or natural identity.
      Both forms have seven specified and four unspecified tetrahedral centers, with
      two specified double-bond geometries; stereo_complete=false is preserved. The
      topology includes an oxygenated long chain, a saturated six-membered C5O ring
      and a fused five-membered nitrogen-containing system with two carbonyls and
      an exocyclic enol. The C5O motif is a candidate sugar ring; it does not by itself
      assign a named sugar, biochemical position or anomer.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2539-grounding-owner
    - support-2539-chemistry
    - support-2539-topology
    - support-2539-molecular-reading
    - support-2539-diagnostic-acceptance
    - support-2539-structure-schema
    - support-2539-stereo-method
  - name: representation_correspondence
    value: Both forms contain 54 atoms and 56 bonds; all ten comparisons are true
      and the chirality-aware substructure match covers 54 atoms. This remains a local
      correspondence rather than independently established full graph or natural identity.
      Both forms have seven specified and four unspecified tetrahedral centers, with
      two specified double-bond geometries; stereo_complete=false is preserved. The
      topology includes an oxygenated long chain, a saturated six-membered C5O ring
      and a fused five-membered nitrogen-containing system with two carbonyls and
      an exocyclic enol. The C5O motif is a candidate sugar ring; it does not by itself
      assign a named sugar, biochemical position or anomer.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2539-grounding-owner
    - support-2539-chemistry
    - support-2539-topology
    - support-2539-molecular-reading
    - support-2539-diagnostic-acceptance
    - support-2539-structure-schema
    - support-2539-stereo-method
- area: provenance
  topic: Heterologous locus evidence and native producer scope
  outcome: supported
  summary: The MIBiG producer Aspergillus sp. CLMG-2019a (NCBITaxon:209559) remains
    SOURCE_ASSERTION. BGC0001857 version 4 separately carries CLUSTER_DEMONSTRATED
    through Heterologous expression at MK425157.1:1–28117. Demonstrating a locus in
    a heterologous system does not upgrade the named native producer or identify individual
    catalytic functions. The saved cache names 209559 Aspergillus alliaceus and includes
    Aspergillus burnettii/Petromyces synonyms; this retained naming relationship does
    not independently validate the source strain or fresh accepted taxonomy.
  assessment_id: support-2539-provenance
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-origin-owner
  - support-2539-source-reading
  - support-2539-direct-contexts
  - support-2539-cached-taxonomy
  - support-2539-taxonomy-reading
  - support-2539-curation-scope
  - support-2539-source-mibig_compounds-0
  - support-2539-source-lotus_occurrences-0
  dimensions:
  - name: taxon_scope
    value: The MIBiG producer Aspergillus sp. CLMG-2019a (NCBITaxon:209559) remains
      SOURCE_ASSERTION. BGC0001857 version 4 separately carries CLUSTER_DEMONSTRATED
      through Heterologous expression at MK425157.1:1–28117. Demonstrating a locus
      in a heterologous system does not upgrade the named native producer or identify
      individual catalytic functions. The saved cache names 209559 Aspergillus alliaceus
      and includes Aspergillus burnettii/Petromyces synonyms; this retained naming
      relationship does not independently validate the source strain or fresh accepted
      taxonomy.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2539-origin-owner
    - support-2539-source-reading
    - support-2539-direct-contexts
    - support-2539-cached-taxonomy
    - support-2539-taxonomy-reading
    - support-2539-curation-scope
    - support-2539-source-mibig_compounds-0
    - support-2539-source-lotus_occurrences-0
  - name: producer_evidence
    value: The MIBiG producer Aspergillus sp. CLMG-2019a (NCBITaxon:209559) remains
      SOURCE_ASSERTION. BGC0001857 version 4 separately carries CLUSTER_DEMONSTRATED
      through Heterologous expression at MK425157.1:1–28117. Demonstrating a locus
      in a heterologous system does not upgrade the named native producer or identify
      individual catalytic functions. The saved cache names 209559 Aspergillus alliaceus
      and includes Aspergillus burnettii/Petromyces synonyms; this retained naming
      relationship does not independently validate the source strain or fresh accepted
      taxonomy.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2539-origin-owner
    - support-2539-source-reading
    - support-2539-direct-contexts
    - support-2539-cached-taxonomy
    - support-2539-taxonomy-reading
    - support-2539-curation-scope
    - support-2539-source-mibig_compounds-0
    - support-2539-source-lotus_occurrences-0
  - name: locus_evidence
    value: The MIBiG producer Aspergillus sp. CLMG-2019a (NCBITaxon:209559) remains
      SOURCE_ASSERTION. BGC0001857 version 4 separately carries CLUSTER_DEMONSTRATED
      through Heterologous expression at MK425157.1:1–28117. Demonstrating a locus
      in a heterologous system does not upgrade the named native producer or identify
      individual catalytic functions. The saved cache names 209559 Aspergillus alliaceus
      and includes Aspergillus burnettii/Petromyces synonyms; this retained naming
      relationship does not independently validate the source strain or fresh accepted
      taxonomy.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2539-origin-owner
    - support-2539-source-reading
    - support-2539-direct-contexts
    - support-2539-cached-taxonomy
    - support-2539-taxonomy-reading
    - support-2539-curation-scope
    - support-2539-source-mibig_compounds-0
    - support-2539-source-lotus_occurrences-0
- area: evidence
  topic: Citation tier and naming provenance
  outcome: supported
  summary: The exact retained MIBiG row uses PMID:30735051 at ENTRY scope, repeated
    as DATABASE_ASSERTION on producer and locus. The LOTUS occurrence cites DOI:10.1021/ACS.ORGLETT.8B04042.
    These stable strings and their claim placements were read locally; original publication
    text and experimental details were not newly inspected. Two complete seed histories
    document import provenance. Cached synonyms do not supply an additional experiment
    or reconcile source strain naming by themselves.
  assessment_id: support-2539-citations
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-owner
  - support-2539-origin-owner
  - support-2539-occurrence-activity-owner
  - support-2539-source-reading
  - support-2539-direct-contexts
  - support-2539-source-mibig_compounds-0
  - support-2539-source-lotus_occurrences-0
  - support-2539-source-npclassifier-0
  dimensions:
  - name: citation_scope
    value: The exact retained MIBiG row uses PMID:30735051 at ENTRY scope, repeated
      as DATABASE_ASSERTION on producer and locus. The LOTUS occurrence cites DOI:10.1021/ACS.ORGLETT.8B04042.
      These stable strings and their claim placements were read locally; original
      publication text and experimental details were not newly inspected. Two complete
      seed histories document import provenance. Cached synonyms do not supply an
      additional experiment or reconcile source strain naming by themselves.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2539-owner
    - support-2539-origin-owner
    - support-2539-occurrence-activity-owner
    - support-2539-source-reading
    - support-2539-direct-contexts
    - support-2539-source-mibig_compounds-0
    - support-2539-source-lotus_occurrences-0
    - support-2539-source-npclassifier-0
- area: evidence
  topic: Genus occurrence and activity boundaries
  outcome: supported
  summary: The LOTUS occurrence is at Aspergillus genus NCBITaxon:5052 and does not
    independently establish CLMG-2019a or biosynthesis by taxon 209559. The complete
    owner has no bioactivity, molecular target, pathway or causal graph. Its saved
    exact-key assay/target frames are empty, a bounded inventory result rather than
    proof of inactivity. The separately retained producer and heterologous locus assertions
    are not replaced or broadened by that absence.
  assessment_id: support-2539-occurrence
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-occurrence-activity-owner
  - support-2539-direct-contexts
  - support-2539-cached-taxonomy
  - support-2539-taxonomy-reading
  - support-2539-curation-scope
  - support-2539-source-reading
  - support-2539-query-lotus_occurrences
  - support-2539-query-chebi_origins
  - support-2539-query-cyanometdb_occurrences
  - support-2539-query-pubchem_bioassay
  - support-2539-query-bindingdb_targets
  - support-2539-query-antibioticmech_inchikeys
  - support-2539-source-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: The LOTUS occurrence is at Aspergillus genus NCBITaxon:5052 and does not
      independently establish CLMG-2019a or biosynthesis by taxon 209559. The complete
      owner has no bioactivity, molecular target, pathway or causal graph. Its saved
      exact-key assay/target frames are empty, a bounded inventory result rather than
      proof of inactivity. The separately retained producer and heterologous locus
      assertions are not replaced or broadened by that absence.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2539-occurrence-activity-owner
    - support-2539-direct-contexts
    - support-2539-cached-taxonomy
    - support-2539-taxonomy-reading
    - support-2539-curation-scope
    - support-2539-source-reading
    - support-2539-query-lotus_occurrences
    - support-2539-query-chebi_origins
    - support-2539-query-cyanometdb_occurrences
    - support-2539-query-pubchem_bioassay
    - support-2539-query-bindingdb_targets
    - support-2539-query-antibioticmech_inchikeys
    - support-2539-source-lotus_occurrences-0
  - name: assay_target_scope
    value: The LOTUS occurrence is at Aspergillus genus NCBITaxon:5052 and does not
      independently establish CLMG-2019a or biosynthesis by taxon 209559. The complete
      owner has no bioactivity, molecular target, pathway or causal graph. Its saved
      exact-key assay/target frames are empty, a bounded inventory result rather than
      proof of inactivity. The separately retained producer and heterologous locus
      assertions are not replaced or broadened by that absence.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2539-occurrence-activity-owner
    - support-2539-direct-contexts
    - support-2539-cached-taxonomy
    - support-2539-taxonomy-reading
    - support-2539-curation-scope
    - support-2539-source-reading
    - support-2539-query-lotus_occurrences
    - support-2539-query-chebi_origins
    - support-2539-query-cyanometdb_occurrences
    - support-2539-query-pubchem_bioassay
    - support-2539-query-bindingdb_targets
    - support-2539-query-antibioticmech_inchikeys
    - support-2539-source-lotus_occurrences-0
- area: consistency
  topic: Computed classification and observed motifs
  outcome: supported
  summary: NPClassifier predicts Amino acids and Peptides/Polyketides, Linear polyketides
    and 3-acyl tetramic acids, with is_glycoside=true. The long carbon chain, carbonyl-containing
    nitrogen ring and oxygen-linked C5O candidate ring make broad polyketide/tetramic/glycoside
    compatibility plausible at a topology level. The enol representation and partial
    stereochemistry limit any narrower chemical assignment, and the model labels do
    not establish biosynthetic provenance or named sugar identity. Source BGC OTHER/NRPS/PKS
    and pinned UNCLASSIFIED filing remain separate assertions.
  assessment_id: support-2539-classification
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-classification-owner
  - support-2539-chemistry
  - support-2539-topology
  - support-2539-classification-seeder
  - support-2539-source-reading
  - support-2539-source-mibig_compounds-0
  - support-2539-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: NPClassifier predicts Amino acids and Peptides/Polyketides, Linear polyketides
      and 3-acyl tetramic acids, with is_glycoside=true. The long carbon chain, carbonyl-containing
      nitrogen ring and oxygen-linked C5O candidate ring make broad polyketide/tetramic/glycoside
      compatibility plausible at a topology level. The enol representation and partial
      stereochemistry limit any narrower chemical assignment, and the model labels
      do not establish biosynthetic provenance or named sugar identity. Source BGC
      OTHER/NRPS/PKS and pinned UNCLASSIFIED filing remain separate assertions.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2539-classification-owner
    - support-2539-chemistry
    - support-2539-topology
    - support-2539-classification-seeder
    - support-2539-source-reading
    - support-2539-source-mibig_compounds-0
    - support-2539-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: supported
  summary: The review covers the entire owner and two histories, accepted 37-input
    inspection, nine source frames with three positive rows, relevant complete cached
    stanzas and both complete saved molecular forms. No mechanism-reader call applies
    because the owner lacks those roots. The retained source grades and encoded structure
    are internally consistent at this scope. Primary experiments, exact native strain
    identity, fresh taxonomy and complete stereochemistry remain unverified; full
    QC and complete OAK coverage are unavailable. No source or status edit is made.
  assessment_id: support-2539-completion
  target_ids:
  - naturalproductmech:mibig-d33eb5850b
  evidence_ids:
  - support-2539-owner
  - support-2539-capture
  - support-2539-intake
  - support-2539-intake-acceptance
  - support-2539-intake-reading
  - support-2539-inventory-acceptance
  - support-2539-plan
  - support-2539-plan-acceptance
  - support-2539-source-reading
  - support-2539-source-notes
  - support-2539-molecular-reading
  - support-2539-diagnostic-acceptance
  - support-2539-diagnostic-execution
  - support-2539-diagnostic-stderr
  - support-2539-review-profile
  dimensions:
  - name: review_completion
    value: The review covers the entire owner and two histories, accepted 37-input
      inspection, nine source frames with three positive rows, relevant complete cached
      stanzas and both complete saved molecular forms. No mechanism-reader call applies
      because the owner lacks those roots. The retained source grades and encoded
      structure are internally consistent at this scope. Primary experiments, exact
      native strain identity, fresh taxonomy and complete stereochemistry remain unverified;
      full QC and complete OAK coverage are unavailable. No source or status edit
      is made.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2539-owner
    - support-2539-capture
    - support-2539-intake
    - support-2539-intake-acceptance
    - support-2539-intake-reading
    - support-2539-inventory-acceptance
    - support-2539-plan
    - support-2539-plan-acceptance
    - support-2539-source-reading
    - support-2539-source-notes
    - support-2539-molecular-reading
    - support-2539-diagnostic-acceptance
    - support-2539-diagnostic-execution
    - support-2539-diagnostic-stderr
    - support-2539-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; original literature, fresh taxonomy/strain/sequence
  and natural-identity validation were not performed.
- Standardized agreement and substructure correspondence do not establish full natural
  graph identity or a uniquely fixed tautomer. Six diagnostic warnings remain global
  and unattributed.
- Source producer, occurrence, locus and computational classification assertions retain
  separate evidence grades and scopes.
- Full QC and complete OAK authority coverage remain unavailable; no source, native
  status or history edit was made.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Support personally read five complete selected owners/history and ten saved molecular
  forms: 346 atom rows and 364 bond rows. Assigned retained-source reading covers
  45 frames, 16 rows and 196 fields; BGC other-context and Native cache/curation work
  remain separately attributed.'
- The accepted last-five canonical input scope is 192 placements across 46 paths.
  Source observations are retained database payloads, not newly inspected primary
  literature.
- No requests, source replays, molecular reparses or record edits were performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-254
```
