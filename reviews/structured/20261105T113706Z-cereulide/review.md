# Local evidence review: cereulide

- Review: 20261105T113706Z-cereulide
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T10:22:47.054920Z
- Finished UTC: 2026-11-05T11:37:06.053509Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

cereulide: retained identity, source grades and representation limits assessed; cyclic-depsipeptide topology retained without a pharmacological inference.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2550; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5ab77d877b | data/natural_products/unclassified/cereulide.yaml | generated | cereulide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-5ab77d877b | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5ab77d877b | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5ab77d877b | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5ab77d877b | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5ab77d877b | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5ab77d877b | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5ab77d877b | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5ab77d877b | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and congener boundaries

identity: supported. Targets: naturalproductmech:mibig-5ab77d877b.

The MINTED owner naturalproductmech:mibig-5ab77d877b retains the exact full key JWWAHGUHYLWQCQ-UHZBFKKDSA-N and MIBiG source label cereulide. Both saved forms reproduce the declared Standard InChI and key, without proving the natural compound or a unique fixed tautomer. The exact retained ChEBI frame is empty; this bounds the historical minted-identity rationale without a fresh authority lookup. The retained npatlas:NPA01776 pointer adds no newly accessed atlas evidence. Neither parseability nor the compound name establishes toxicity, ion binding or a pharmacological mechanism.

### Stored forms and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-5ab77d877b.

Both saved forms have C57H96N6O18 at net charge 0, 81 atoms and 81 bonds, with one 36-membered ring. Eight normalized comparisons are true, while both canonical SMILES comparisons are false and the direct atom map is empty. The SMILES contains six ester and six amide linkages; the InChI-derived form retains the esters and expresses six C(O)=N motifs. All twelve potential tetrahedral centers are specified, consistent with the stored stereo_complete=true flag at that bounded scope. Six unspecified double bonds in the InChI-derived form arise from the imidic representation and do not independently show missing natural stereochemistry. No terminal carboxylic acid, phosphate or candidate sugar ring is present in these saved forms; neither full fixed-graph nor natural identity is established.

### Separate producer and locus evidence

provenance: supported. Targets: naturalproductmech:mibig-5ab77d877b.

MIBiG BGC0000320 version 5 retains Bacillus cereus (NCBITaxon:1396) as BGC_CHARACTERIZED and separately grades its NRPS locus CLUSTER_DEMONSTRATED, citing Knock-out studies and Enzymatic assays. Genome accession DQ360825.1 is retained, while the source locus bounds are blank and no coordinates are supplied by this review. Active/complete source status and questionable source quality remain distinct from the producer and locus grades. This species-level assertion does not establish a specific producing isolate or a complete enzyme-by-enzyme route.

### Citation tier and retained history

evidence: supported. Targets: naturalproductmech:mibig-5ab77d877b.

PMID:15640177 is retained at ENTRY scope on the MIBiG producer/locus assertions. Four LOTUS rows cite DOI:10.1016/0378-1097(95)00119-P, DOI:10.1039/P19950000765, DOI:10.1128/AEM.71.1.105-113.2005 and DOI:10.1246/CL.1995.791. These are database-retained references without new paper access or a claim of four independent production experiments. The NPA01776 xref is only a retained pointer. All three history events are seeding events; no historical mechanism curation is invented.

### Occurrence and bounded activity absence

evidence: supported. Targets: naturalproductmech:mibig-5ab77d877b.

Four retained LOTUS rows use Bacillus cereus (NCBITaxon:1396). Their explicit occurrence scope remains separate from the MIBiG producer claim even though the taxon matches, and publication independence is unestablished. The complete owner has no causal graph, pathway, bioactivity or molecular-target root. The exact retained PubChem, BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin frames are empty; no inactivity, toxicity, ionophore or universal literature-absence conclusion follows. Three supplemental diagnostic-only input roles create no assay evidence.

### Applicability of computed labels

consistency: supported. Targets: naturalproductmech:mibig-5ab77d877b.

NPClassifier version npclassifier.gnps2.org@2026-09-07 predicts Amino acids and Peptides/Polyketides, Oligopeptides, and Cyclic peptides/Depsipeptides, with is_glycoside=false. The stored ring with amide and ester linkages is compatible with the broad cyclic-depsipeptide description, and no candidate sugar ring is present. Model pathway labels do not independently prove biosynthetic origin, enzyme functions or a polyketide route. MIBiG NRPS classification and UNCLASSIFIED filing remain separate assertions.

### Review completion

completeness: supported. Targets: naturalproductmech:mibig-5ab77d877b.

The review covers the complete owner and three histories, the accepted 40-input canonical intake, all nine assigned source frames and 6 positive rows, relevant retained cache stanzas, and both complete saved molecular forms. No maintained-reader check applies because mechanism roots are absent. All retained evidence remains usable within its stated scope, while natural identity, primary experimental verification and full authority coverage remain limited. Full QC, complete OAK authority coverage and primary-source cross-checking remain unavailable, so review completion is partial. No record, status or history is edited.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2550-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/cereulide.yaml; Whole current plaintext including complete curation_history | supports | Complete current selected owner and all 3 history events; no native record/status/history changes. |
| support-2550-capture | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete captured owner and every present root. Root presence and absence are retained exactly for this owner. |
| support-2550-grounding-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/9/owner_document/identifier; /records/9/owner_document/label; /records/9/owner_document/chemical_structure; /records/9/owner_document/source_concepts; /records/9/owner_document/xrefs; /records/9/owner_document/grounding_status; /records/9/owner_document/grounding_notes | supports | Exact retained identifier, full key, source structure and present source/grounding fields; no fresh natural identity validation. |
| support-2550-origin-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/9/owner_document/producer_organisms; /records/9/owner_document/biosynthetic_gene_clusters; /records/9/owner_document/producer_taxon_groups | supports | Complete producer and locus claims with separate evidence grades, methods, coordinates and source classes. |
| support-2550-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete owner preserves exact occurrence, activity, target and mechanism root presence or absence; production context is distinct from pharmacological activity. |
| support-2550-classification-owner | /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json; /records/9/owner_document/np_pathway; /records/9/owner_document/np_classification; /records/9/owner_document/bgc_class; /records/9/owner_document/biosynthesis_origin | supports | Versioned model output, source BGC classes and UNCLASSIFIED filing remain separate assertions. |
| support-2550-direct-contexts | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-target-input-plan-002.proposed.json; /records/9/proposed_companion_paths; /records/9/direct_companion_predicates; /records/9/identity_comparison_paths; /records/9/additional_context_roles | context_only | Exact admitted direct-BGC context links and additional input roles, including the three diagnostic-only supplement roles. No separate selected-identity comparison roles or added assay outcomes follow. |
| support-2550-intake | /private/tmp/npm-review-work/shared-next-batch255/intakes/2550-inspect-001.json; /targets; /source | supports | Actual canonical target, source inputs and maintained ownership are retained. |
| support-2550-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch255/root-intake-acceptance-001.json; /status; /intakes/9; /source_plan; /verification | supports | ROOT accepts this original canonical intake and its exact source-plan/input joins. |
| support-2550-intake-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/support-prep/support-current255-last-five-molecular-intake-reading-001.json; /reading; /records/4/target; /records/4/intake; /coverage | supports | Support personally read all last-five canonical target/ownership documents; 228 current input placements across 48 paths are preserved. |
| support-2550-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch255/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; this is not primary-paper verification. |
| support-2550-plan | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-target-input-plan-002.proposed.json; /records/9/proposed_input_paths; /records/9/proposed_input_count | supports | The accepted input map agrees exactly with this canonical intake. |
| support-2550-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch255/root-source-plan-acceptance-001.json; /status; /verification | supports | ROOT accepts the actual255 plan and its current source-input joins. |
| support-2550-source-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/support-prep/support-current255-assigned-source-reading-001.json; /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows; /cautions; /reading_method | supports | Support read all five selected contexts: 45 frames, 21 rows and 245 fields. BGC reads the other ten contexts including five unselected companions; these retained database payloads do not confer primary-literature verification. |
| support-2550-source-notes | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes retain disjoint BGC 37, Support 21 and Native 0 retained-row reading attribution, with original 417-placement/53-path source scope and the recorded reading cautions and boundaries. These notes add no assay evidence or new source-row credit. |
| support-2550-molecular-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/support-prep/support-current255-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/4; /representation_notes; /limits | supports | Support personally read all ten complete saved forms: 1,022 atom rows and 1,070 bond rows, all stereo/motif/map fields, and 228 assigned canonical input placements across 48 paths. No new molecular parse. |
| support-2550-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/0 | context_only | Complete relevant retained cache stanzas preserve names and synonyms; these do not prove native production, strain identity or fresh taxonomy. |
| support-2550-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation; /routes | context_only | Native complete cache and route interpretation remains attributed; owner-local retained stanzas carry only their exact saved fields. |
| support-2550-curation-scope | /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | The bounded implemented-table scan found no applicable exact replacement for these owners; unrelated lexical hits are not imported as owner evidence. |
| support-2550-chemistry | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope; /records/9/comparisons; /records/9/atom_correspondence | supports | Eight normalized comparisons are true, while both canonical SMILES comparisons are false and the direct atom map is empty. Amide/imidic representation differences retain normalized identifiers without fixed-graph or natural-identity proof. |
| support-2550-topology | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles; /records/9/inchi | supports | Complete saved atom/bond/ring/stereo/motif tables retain representation-specific counts and stereochemical assignments; no new parse or natural-state claim. |
| support-2550-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /scope | supports | ROOT accepts the original stored-form diagnostic: all five assigned canonical pairs remain unequal despite normalized identity agreement. The original stderr is empty; no natural identity upgrade follows. |
| support-2550-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, terminal exit and stream pins; no retry or external request. |
| support-2550-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Original diagnostic stderr is empty; no warnings are imported from another batch. |
| support-2550-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2550-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2550-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2550-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2550-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained physical row 435, all 25 fields: BGC0000320 version 5; Bacillus cereus, producer BGC_CHARACTERIZED, locus CLUSTER_DEMONSTRATED; PMID:15640177 at ENTRY scope. Source structure, methods and classes remain exact. |
| support-2550-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 435 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2550-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 4 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained physical row 3531, all 6 fields: Bacillus cereus (NCBITaxon:1396), DOI:10.1016/0378-1097(95)00119-P; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2550-source-lotus_occurrences-1 | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/1 | supports | Complete retained physical row 3532, all 6 fields: Bacillus cereus (NCBITaxon:1396), DOI:10.1039/P19950000765; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2550-source-lotus_occurrences-2 | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/2 | supports | Complete retained physical row 3533, all 6 fields: Bacillus cereus (NCBITaxon:1396), DOI:10.1128/AEM.71.1.105-113.2005; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2550-source-lotus_occurrences-3 | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/3 | supports | Complete retained physical row 3534, all 6 fields: Bacillus cereus (NCBITaxon:1396), DOI:10.1246/CL.1995.791; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2550-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 3531, 3532, 3533, 3534 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2550-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained physical row 1190, all 7 fields: npclassifier.gnps2.org@2026-09-07: Amino acids and Peptides&#124;Polyketides/Oligopeptides/Cyclic peptides&#124;Depsipeptides; glycoside=false, model assertion only. |
| support-2550-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1190 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2550-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2550-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-255/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-255/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-255/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-255/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-255/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only: original publications, fresh taxonomy, sequences and natural-identity verification were not accessed.
- Matching normalized identifiers do not establish a unique fixed graph or tautomer. False canonical comparisons and empty direct atom maps remain explicit; original diagnostic stderr is empty.
- Producer, locus, occurrence and computational classification claims retain separate evidence grades; historical curator access is not current primary-source verification.
- Full QC, complete OAK authority coverage and primary-source cross-checking remain unavailable. No source, native status or history edit was made.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete selected owners/history and ten saved molecular forms: 1,022 atom rows and 1,070 bond rows. Assigned retained-source reading covers 45 frames, 21 rows and 245 fields; BGC other-context and Native cache/curation work remain separately attributed.
- The accepted last-five canonical input scope is 228 placements across 48 paths. Original inventory scope was 417/53; the explicit diagnostic-only supplement gives operative 447/56 globally without adding assay outcomes.
- No requests, source replays, molecular reparses or owner edits were performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T113706Z-cereulide
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: cereulide'
started_at: '2026-11-05T10:22:47.054920Z'
finished_at: '2026-11-05T11:37:06.053509Z'
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
summary: 'cereulide: retained identity, source grades and representation limits assessed;
  cyclic-depsipeptide topology retained without a pharmacological inference.'
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
  - path: data/natural_products/unclassified/cereulide.yaml
    sha256: eec699c528a4f57f1431baf57ecf35952076af61144c7bfaf4cea1919eb5b2a8
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
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
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
  selection: Campaign path order 2550; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5ab77d877b
targets:
- target_id: naturalproductmech:mibig-5ab77d877b
  path: data/natural_products/unclassified/cereulide.yaml
  label: cereulide
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
    role: 'Retained exclusion-table diagnostic scope: zero actual AID tuples and three
      blank sentinels remain separate from biological assay evidence.'
  - repository: CultureBotAI/NaturalProductMech
    path: curation/unresolved_taxa.tsv
    role: Retained unresolved-taxon diagnostic table included in the bounded implemented-curation
      scan; no fresh taxonomy or producer confirmation.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Implementation context for the retained exclusion identity, row-digest and
      attributed-rationale guards; no execution or new assay evidence.
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
  - naturalproductmech:mibig-5ab77d877b
  command: just validate-strict data/natural_products/unclassified/cacaoidin.yaml
    data/natural_products/unclassified/camporidine-a.yaml data/natural_products/unclassified/capsimycin.yaml
    data/natural_products/unclassified/cda1b.yaml data/natural_products/unclassified/cda2a.yaml
    data/natural_products/unclassified/cda2b.yaml data/natural_products/unclassified/cda3a.yaml
    data/natural_products/unclassified/cda3b.yaml data/natural_products/unclassified/cda4a.yaml
    data/natural_products/unclassified/cereulide.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-255/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-5ab77d877b
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-255/validate-all-001.tsv
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
  - naturalproductmech:mibig-5ab77d877b
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
  - naturalproductmech:mibig-5ab77d877b
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
  - naturalproductmech:mibig-5ab77d877b
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-255/review-queue-001.tsv
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
  - naturalproductmech:mibig-5ab77d877b
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2550-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/cereulide.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Complete current selected owner and all 3 history events; no native record/status/history
    changes.
  snapshot_sha256: eec699c528a4f57f1431baf57ecf35952076af61144c7bfaf4cea1919eb5b2a8
- evidence_id: support-2550-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Complete captured owner and every present root. Root presence and absence
    are retained exactly for this owner.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: support-2550-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/9/owner_document/identifier; /records/9/owner_document/label;
    /records/9/owner_document/chemical_structure; /records/9/owner_document/source_concepts;
    /records/9/owner_document/xrefs; /records/9/owner_document/grounding_status; /records/9/owner_document/grounding_notes
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Exact retained identifier, full key, source structure and present source/grounding
    fields; no fresh natural identity validation.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: support-2550-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/9/owner_document/producer_organisms; /records/9/owner_document/biosynthetic_gene_clusters;
    /records/9/owner_document/producer_taxon_groups
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Complete producer and locus claims with separate evidence grades, methods,
    coordinates and source classes.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: support-2550-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Complete owner preserves exact occurrence, activity, target and mechanism
    root presence or absence; production context is distinct from pharmacological
    activity.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: support-2550-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255/owner-capture-DATA-001.json
  locator: /records/9/owner_document/np_pathway; /records/9/owner_document/np_classification;
    /records/9/owner_document/bgc_class; /records/9/owner_document/biosynthesis_origin
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Versioned model output, source BGC classes and UNCLASSIFIED filing remain
    separate assertions.
  snapshot_sha256: 9c4c9dd4fafd0504a926a72da222acd9c5bd5022cda900cbdd428eaed2bb8f5e
- evidence_id: support-2550-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-target-input-plan-002.proposed.json
  locator: /records/9/proposed_companion_paths; /records/9/direct_companion_predicates;
    /records/9/identity_comparison_paths; /records/9/additional_context_roles
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Exact admitted direct-BGC context links and additional input roles, including
    the three diagnostic-only supplement roles. No separate selected-identity comparison
    roles or added assay outcomes follow.
  snapshot_sha256: 4def32a9c6c5c2e785a4aa93cd25501a68aac8f22e70ac34e9148b633fa6ac79
- evidence_id: support-2550-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/intakes/2550-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Actual canonical target, source inputs and maintained ownership are retained.
  snapshot_sha256: a58e8f5348eb92fa024e7c69b54d74903c489caf8f769218997543ebc790137a
- evidence_id: support-2550-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/root-intake-acceptance-001.json
  locator: /status; /intakes/9; /source_plan; /verification
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: ROOT accepts this original canonical intake and its exact source-plan/input
    joins.
  snapshot_sha256: 88c29293963b153618761b4d9f3fea6b57709472904f83988a48b1a243f110f3
- evidence_id: support-2550-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/support-prep/support-current255-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/4/target; /records/4/intake; /coverage
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Support personally read all last-five canonical target/ownership documents;
    228 current input placements across 48 paths are preserved.
  snapshot_sha256: 37b2704a69beaa2f8053f043a2a56f840809a36afcc1a4369408596a737da99d
- evidence_id: support-2550-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; this is not primary-paper
    verification.
  snapshot_sha256: e88b11c77a4bded10730616c541000fd4b3c93dcab7689dd0d512b6a372514b2
- evidence_id: support-2550-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-target-input-plan-002.proposed.json
  locator: /records/9/proposed_input_paths; /records/9/proposed_input_count
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: The accepted input map agrees exactly with this canonical intake.
  snapshot_sha256: 4def32a9c6c5c2e785a4aa93cd25501a68aac8f22e70ac34e9148b633fa6ac79
- evidence_id: support-2550-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/root-source-plan-acceptance-001.json
  locator: /status; /verification
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: ROOT accepts the actual255 plan and its current source-input joins.
  snapshot_sha256: b28770e21370105fdd17012b97c866489df36ee86a94449afc88472045732b66
- evidence_id: support-2550-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/support-prep/support-current255-assigned-source-reading-001.json
  locator: /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows;
    /cautions; /reading_method
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Support read all five selected contexts: 45 frames, 21 rows and 245 fields.
    BGC reads the other ten contexts including five unselected companions; these retained
    database payloads do not confer primary-literature verification.'
  snapshot_sha256: e0316420c43895dafa53910bfeafbb235f307c1ca994f6ec5146bbc885f1a12c
- evidence_id: support-2550-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Joint notes retain disjoint BGC 37, Support 21 and Native 0 retained-row
    reading attribution, with original 417-placement/53-path source scope and the
    recorded reading cautions and boundaries. These notes add no assay evidence or
    new source-row credit.
  snapshot_sha256: dd29263b6b480a6ea0d9f608aabfb045ec6ab5a8dcfb47220f21e112dadb4ce0
- evidence_id: support-2550-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/support-prep/support-current255-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/4; /representation_notes; /limits
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Support personally read all ten complete saved forms: 1,022 atom rows
    and 1,070 bond rows, all stereo/motif/map fields, and 228 assigned canonical input
    placements across 48 paths. No new molecular parse.'
  snapshot_sha256: 37b2704a69beaa2f8053f043a2a56f840809a36afcc1a4369408596a737da99d
- evidence_id: support-2550-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/0
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve names and synonyms; these
    do not prove native production, strain identity or fresh taxonomy.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation; /routes
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Native complete cache and route interpretation remains attributed; owner-local
    retained stanzas carry only their exact saved fields.
  snapshot_sha256: e80799a40def631e8e5224442cb193c264b78522fe4fe62a0316c4995d329a55
- evidence_id: support-2550-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/native-prep/native-current255-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: The bounded implemented-table scan found no applicable exact replacement
    for these owners; unrelated lexical hits are not imported as owner evidence.
  snapshot_sha256: c1dbdf1c6aa0c9dcf29d1e127250afb13ba3123717af90247f53dd0922cdef96
  search_scope: '{"selected_identifier": "naturalproductmech:mibig-5ab77d877b", "full_key":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "scope": "Eleven enumerated retained curation tables,
    nine implemented tables and exact predicates; ignored-file-independent inspection
    is bounded, not universal absence."}'
- evidence_id: support-2550-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope;
    /records/9/comparisons; /records/9/atom_correspondence
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Eight normalized comparisons are true, while both canonical SMILES comparisons
    are false and the direct atom map is empty. Amide/imidic representation differences
    retain normalized identifiers without fixed-graph or natural-identity proof.
  snapshot_sha256: 8aca4e34df21753ab142a768460f4a6bee6ee1ff4fd9c63a175c1e0aed5d6483
- evidence_id: support-2550-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles; /records/9/inchi
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif tables retain representation-specific
    counts and stereochemical assignments; no new parse or natural-state claim.
  snapshot_sha256: 8aca4e34df21753ab142a768460f4a6bee6ee1ff4fd9c63a175c1e0aed5d6483
- evidence_id: support-2550-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /scope
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'ROOT accepts the original stored-form diagnostic: all five assigned canonical
    pairs remain unequal despite normalized identity agreement. The original stderr
    is empty; no natural identity upgrade follows.'
  snapshot_sha256: f10a2276d9c19ae550fc9c927710f9d11c8b4f32896a2b260e7b4115cd6652d5
- evidence_id: support-2550-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Exact original diagnostic command/source, terminal exit and stream pins;
    no retry or external request.
  snapshot_sha256: bb2ed399af53bcac08ccf13bf71e36d5b6767e189508fe1d9ff9994f15868eba
- evidence_id: support-2550-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch255/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Original diagnostic stderr is empty; no warnings are imported from another
    batch.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: support-2550-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2550-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2550-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2550-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2550-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/mibig_compounds",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Complete retained physical row 435, all 25 fields: BGC0000320 version
    5; Bacillus cereus, producer BGC_CHARACTERIZED, locus CLUSTER_DEMONSTRATED; PMID:15640177
    at ENTRY scope. Source structure, methods and classes remain exact.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 435
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2550-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/chebi_structures",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved lotus_occurrences frame has 4 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Complete retained physical row 3531, all 6 fields: Bacillus cereus (NCBITaxon:1396),
    DOI:10.1016/0378-1097(95)00119-P; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-source-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/1
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Complete retained physical row 3532, all 6 fields: Bacillus cereus (NCBITaxon:1396),
    DOI:10.1039/P19950000765; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-source-lotus_occurrences-2
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/2
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Complete retained physical row 3533, all 6 fields: Bacillus cereus (NCBITaxon:1396),
    DOI:10.1128/AEM.71.1.105-113.2005; occurrence is distinct from demonstrated production
    and independent-study corroboration.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-source-lotus_occurrences-3
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences/matches/3
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Complete retained physical row 3534, all 6 fields: Bacillus cereus (NCBITaxon:1396),
    DOI:10.1246/CL.1995.791; occurrence is distinct from demonstrated production and
    independent-study corroboration.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 3531, 3532, 3533, 3534
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2550-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; a zero is
    bounded to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; a zero is bounded to
    its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/npclassifier",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: 'Complete retained physical row 1190, all 7 fields: npclassifier.gnps2.org@2026-09-07:
    Amino acids and Peptides|Polyketides/Oligopeptides/Cyclic peptides|Depsipeptides;
    glycoside=false, model assertion only.'
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
- evidence_id: support-2550-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1190
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2550-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; a zero
    is bounded to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JWWAHGUHYLWQCQ-UHZBFKKDSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2550-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch255-tentative/bgc-prep/bgc-conditional255-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T11:26:16.566219Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 206eee8785e1cd1814a33625d8780fecd72df38794947886651d42019ca8e928
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/10/source_scope_inventory/joins/chebi_origins",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:33:23.740807Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 8cb8777463815d064d8d6a8debcddee05dcd1cf93d48611f7881e2ed321ce0b0
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:33:47.513574Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 200d5cffe7b8a89613f5bd36389b83452a7611ea40cb1e6b7805eb3531c9523b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:34:06.425956Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:34:39.110237Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-255/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-255/native-current255-five-gates-execution-001.json
  accessed_at: '2026-11-05T10:34:50.404426Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 98f13f2c35ba807bae8831fae9d0256cfeea0b6181f83aaceddb47e61f71cbd5
assessments:
- area: identity
  topic: Retained identity and congener boundaries
  outcome: supported
  summary: The MINTED owner naturalproductmech:mibig-5ab77d877b retains the exact
    full key JWWAHGUHYLWQCQ-UHZBFKKDSA-N and MIBiG source label cereulide. Both saved
    forms reproduce the declared Standard InChI and key, without proving the natural
    compound or a unique fixed tautomer. The exact retained ChEBI frame is empty;
    this bounds the historical minted-identity rationale without a fresh authority
    lookup. The retained npatlas:NPA01776 pointer adds no newly accessed atlas evidence.
    Neither parseability nor the compound name establishes toxicity, ion binding or
    a pharmacological mechanism.
  assessment_id: support-2550-identity
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-grounding-owner
  - support-2550-chemistry
  - support-2550-topology
  - support-2550-direct-contexts
  - support-2550-source-reading
  - support-2550-query-chebi_structures
  - support-2550-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: JWWAHGUHYLWQCQ-UHZBFKKDSA-N; retained full key, not independently established
      natural identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2550-grounding-owner
    - support-2550-chemistry
    - support-2550-topology
    - support-2550-direct-contexts
    - support-2550-source-reading
    - support-2550-query-chebi_structures
    - support-2550-source-mibig_compounds-0
  - name: grounding_scope
    value: The MINTED owner naturalproductmech:mibig-5ab77d877b retains the exact
      full key JWWAHGUHYLWQCQ-UHZBFKKDSA-N and MIBiG source label cereulide. Both
      saved forms reproduce the declared Standard InChI and key, without proving the
      natural compound or a unique fixed tautomer. The exact retained ChEBI frame
      is empty; this bounds the historical minted-identity rationale without a fresh
      authority lookup. The retained npatlas:NPA01776 pointer adds no newly accessed
      atlas evidence. Neither parseability nor the compound name establishes toxicity,
      ion binding or a pharmacological mechanism.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2550-grounding-owner
    - support-2550-chemistry
    - support-2550-topology
    - support-2550-direct-contexts
    - support-2550-source-reading
    - support-2550-query-chebi_structures
    - support-2550-source-mibig_compounds-0
- area: representation
  topic: Stored forms and stereochemical limits
  outcome: supported
  summary: Both saved forms have C57H96N6O18 at net charge 0, 81 atoms and 81 bonds,
    with one 36-membered ring. Eight normalized comparisons are true, while both canonical
    SMILES comparisons are false and the direct atom map is empty. The SMILES contains
    six ester and six amide linkages; the InChI-derived form retains the esters and
    expresses six C(O)=N motifs. All twelve potential tetrahedral centers are specified,
    consistent with the stored stereo_complete=true flag at that bounded scope. Six
    unspecified double bonds in the InChI-derived form arise from the imidic representation
    and do not independently show missing natural stereochemistry. No terminal carboxylic
    acid, phosphate or candidate sugar ring is present in these saved forms; neither
    full fixed-graph nor natural identity is established.
  assessment_id: support-2550-representation
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-grounding-owner
  - support-2550-chemistry
  - support-2550-topology
  - support-2550-molecular-reading
  - support-2550-diagnostic-acceptance
  - support-2550-structure-schema
  - support-2550-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms have C57H96N6O18 at net charge 0, 81 atoms and 81 bonds,
      with one 36-membered ring. Eight normalized comparisons are true, while both
      canonical SMILES comparisons are false and the direct atom map is empty. The
      SMILES contains six ester and six amide linkages; the InChI-derived form retains
      the esters and expresses six C(O)=N motifs. All twelve potential tetrahedral
      centers are specified, consistent with the stored stereo_complete=true flag
      at that bounded scope. Six unspecified double bonds in the InChI-derived form
      arise from the imidic representation and do not independently show missing natural
      stereochemistry. No terminal carboxylic acid, phosphate or candidate sugar ring
      is present in these saved forms; neither full fixed-graph nor natural identity
      is established.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2550-grounding-owner
    - support-2550-chemistry
    - support-2550-topology
    - support-2550-molecular-reading
    - support-2550-diagnostic-acceptance
    - support-2550-structure-schema
    - support-2550-stereo-method
  - name: representation_correspondence
    value: Both saved forms have C57H96N6O18 at net charge 0, 81 atoms and 81 bonds,
      with one 36-membered ring. Eight normalized comparisons are true, while both
      canonical SMILES comparisons are false and the direct atom map is empty. The
      SMILES contains six ester and six amide linkages; the InChI-derived form retains
      the esters and expresses six C(O)=N motifs. All twelve potential tetrahedral
      centers are specified, consistent with the stored stereo_complete=true flag
      at that bounded scope. Six unspecified double bonds in the InChI-derived form
      arise from the imidic representation and do not independently show missing natural
      stereochemistry. No terminal carboxylic acid, phosphate or candidate sugar ring
      is present in these saved forms; neither full fixed-graph nor natural identity
      is established.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2550-grounding-owner
    - support-2550-chemistry
    - support-2550-topology
    - support-2550-molecular-reading
    - support-2550-diagnostic-acceptance
    - support-2550-structure-schema
    - support-2550-stereo-method
- area: provenance
  topic: Separate producer and locus evidence
  outcome: supported
  summary: MIBiG BGC0000320 version 5 retains Bacillus cereus (NCBITaxon:1396) as
    BGC_CHARACTERIZED and separately grades its NRPS locus CLUSTER_DEMONSTRATED, citing
    Knock-out studies and Enzymatic assays. Genome accession DQ360825.1 is retained,
    while the source locus bounds are blank and no coordinates are supplied by this
    review. Active/complete source status and questionable source quality remain distinct
    from the producer and locus grades. This species-level assertion does not establish
    a specific producing isolate or a complete enzyme-by-enzyme route.
  assessment_id: support-2550-provenance
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-origin-owner
  - support-2550-source-reading
  - support-2550-direct-contexts
  - support-2550-cached-taxonomy
  - support-2550-taxonomy-reading
  - support-2550-curation-scope
  - support-2550-source-mibig_compounds-0
  - support-2550-source-lotus_occurrences-0
  - support-2550-source-lotus_occurrences-1
  - support-2550-source-lotus_occurrences-2
  - support-2550-source-lotus_occurrences-3
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0000320 version 5 retains Bacillus cereus (NCBITaxon:1396) as
      BGC_CHARACTERIZED and separately grades its NRPS locus CLUSTER_DEMONSTRATED,
      citing Knock-out studies and Enzymatic assays. Genome accession DQ360825.1 is
      retained, while the source locus bounds are blank and no coordinates are supplied
      by this review. Active/complete source status and questionable source quality
      remain distinct from the producer and locus grades. This species-level assertion
      does not establish a specific producing isolate or a complete enzyme-by-enzyme
      route.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2550-origin-owner
    - support-2550-source-reading
    - support-2550-direct-contexts
    - support-2550-cached-taxonomy
    - support-2550-taxonomy-reading
    - support-2550-curation-scope
    - support-2550-source-mibig_compounds-0
    - support-2550-source-lotus_occurrences-0
    - support-2550-source-lotus_occurrences-1
    - support-2550-source-lotus_occurrences-2
    - support-2550-source-lotus_occurrences-3
  - name: producer_evidence
    value: MIBiG BGC0000320 version 5 retains Bacillus cereus (NCBITaxon:1396) as
      BGC_CHARACTERIZED and separately grades its NRPS locus CLUSTER_DEMONSTRATED,
      citing Knock-out studies and Enzymatic assays. Genome accession DQ360825.1 is
      retained, while the source locus bounds are blank and no coordinates are supplied
      by this review. Active/complete source status and questionable source quality
      remain distinct from the producer and locus grades. This species-level assertion
      does not establish a specific producing isolate or a complete enzyme-by-enzyme
      route.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2550-origin-owner
    - support-2550-source-reading
    - support-2550-direct-contexts
    - support-2550-cached-taxonomy
    - support-2550-taxonomy-reading
    - support-2550-curation-scope
    - support-2550-source-mibig_compounds-0
    - support-2550-source-lotus_occurrences-0
    - support-2550-source-lotus_occurrences-1
    - support-2550-source-lotus_occurrences-2
    - support-2550-source-lotus_occurrences-3
  - name: locus_evidence
    value: MIBiG BGC0000320 version 5 retains Bacillus cereus (NCBITaxon:1396) as
      BGC_CHARACTERIZED and separately grades its NRPS locus CLUSTER_DEMONSTRATED,
      citing Knock-out studies and Enzymatic assays. Genome accession DQ360825.1 is
      retained, while the source locus bounds are blank and no coordinates are supplied
      by this review. Active/complete source status and questionable source quality
      remain distinct from the producer and locus grades. This species-level assertion
      does not establish a specific producing isolate or a complete enzyme-by-enzyme
      route.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2550-origin-owner
    - support-2550-source-reading
    - support-2550-direct-contexts
    - support-2550-cached-taxonomy
    - support-2550-taxonomy-reading
    - support-2550-curation-scope
    - support-2550-source-mibig_compounds-0
    - support-2550-source-lotus_occurrences-0
    - support-2550-source-lotus_occurrences-1
    - support-2550-source-lotus_occurrences-2
    - support-2550-source-lotus_occurrences-3
- area: evidence
  topic: Citation tier and retained history
  outcome: supported
  summary: PMID:15640177 is retained at ENTRY scope on the MIBiG producer/locus assertions.
    Four LOTUS rows cite DOI:10.1016/0378-1097(95)00119-P, DOI:10.1039/P19950000765,
    DOI:10.1128/AEM.71.1.105-113.2005 and DOI:10.1246/CL.1995.791. These are database-retained
    references without new paper access or a claim of four independent production
    experiments. The NPA01776 xref is only a retained pointer. All three history events
    are seeding events; no historical mechanism curation is invented.
  assessment_id: support-2550-citations
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-owner
  - support-2550-origin-owner
  - support-2550-occurrence-activity-owner
  - support-2550-source-reading
  - support-2550-direct-contexts
  - support-2550-source-mibig_compounds-0
  - support-2550-source-lotus_occurrences-0
  - support-2550-source-lotus_occurrences-1
  - support-2550-source-lotus_occurrences-2
  - support-2550-source-lotus_occurrences-3
  - support-2550-source-npclassifier-0
  dimensions:
  - name: citation_scope
    value: PMID:15640177 is retained at ENTRY scope on the MIBiG producer/locus assertions.
      Four LOTUS rows cite DOI:10.1016/0378-1097(95)00119-P, DOI:10.1039/P19950000765,
      DOI:10.1128/AEM.71.1.105-113.2005 and DOI:10.1246/CL.1995.791. These are database-retained
      references without new paper access or a claim of four independent production
      experiments. The NPA01776 xref is only a retained pointer. All three history
      events are seeding events; no historical mechanism curation is invented.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2550-owner
    - support-2550-origin-owner
    - support-2550-occurrence-activity-owner
    - support-2550-source-reading
    - support-2550-direct-contexts
    - support-2550-source-mibig_compounds-0
    - support-2550-source-lotus_occurrences-0
    - support-2550-source-lotus_occurrences-1
    - support-2550-source-lotus_occurrences-2
    - support-2550-source-lotus_occurrences-3
    - support-2550-source-npclassifier-0
- area: evidence
  topic: Occurrence and bounded activity absence
  outcome: supported
  summary: Four retained LOTUS rows use Bacillus cereus (NCBITaxon:1396). Their explicit
    occurrence scope remains separate from the MIBiG producer claim even though the
    taxon matches, and publication independence is unestablished. The complete owner
    has no causal graph, pathway, bioactivity or molecular-target root. The exact
    retained PubChem, BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin frames
    are empty; no inactivity, toxicity, ionophore or universal literature-absence
    conclusion follows. Three supplemental diagnostic-only input roles create no assay
    evidence.
  assessment_id: support-2550-occurrence
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-occurrence-activity-owner
  - support-2550-direct-contexts
  - support-2550-cached-taxonomy
  - support-2550-taxonomy-reading
  - support-2550-curation-scope
  - support-2550-source-reading
  - support-2550-query-lotus_occurrences
  - support-2550-query-chebi_origins
  - support-2550-query-cyanometdb_occurrences
  - support-2550-query-pubchem_bioassay
  - support-2550-query-bindingdb_targets
  - support-2550-query-antibioticmech_inchikeys
  - support-2550-source-lotus_occurrences-0
  - support-2550-source-lotus_occurrences-1
  - support-2550-source-lotus_occurrences-2
  - support-2550-source-lotus_occurrences-3
  dimensions:
  - name: occurrence_scope
    value: Four retained LOTUS rows use Bacillus cereus (NCBITaxon:1396). Their explicit
      occurrence scope remains separate from the MIBiG producer claim even though
      the taxon matches, and publication independence is unestablished. The complete
      owner has no causal graph, pathway, bioactivity or molecular-target root. The
      exact retained PubChem, BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin
      frames are empty; no inactivity, toxicity, ionophore or universal literature-absence
      conclusion follows. Three supplemental diagnostic-only input roles create no
      assay evidence.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2550-occurrence-activity-owner
    - support-2550-direct-contexts
    - support-2550-cached-taxonomy
    - support-2550-taxonomy-reading
    - support-2550-curation-scope
    - support-2550-source-reading
    - support-2550-query-lotus_occurrences
    - support-2550-query-chebi_origins
    - support-2550-query-cyanometdb_occurrences
    - support-2550-query-pubchem_bioassay
    - support-2550-query-bindingdb_targets
    - support-2550-query-antibioticmech_inchikeys
    - support-2550-source-lotus_occurrences-0
    - support-2550-source-lotus_occurrences-1
    - support-2550-source-lotus_occurrences-2
    - support-2550-source-lotus_occurrences-3
  - name: assay_target_scope
    value: Four retained LOTUS rows use Bacillus cereus (NCBITaxon:1396). Their explicit
      occurrence scope remains separate from the MIBiG producer claim even though
      the taxon matches, and publication independence is unestablished. The complete
      owner has no causal graph, pathway, bioactivity or molecular-target root. The
      exact retained PubChem, BindingDB, AntibioticMech, CyanoMetDB and ChEBI-origin
      frames are empty; no inactivity, toxicity, ionophore or universal literature-absence
      conclusion follows. Three supplemental diagnostic-only input roles create no
      assay evidence.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2550-occurrence-activity-owner
    - support-2550-direct-contexts
    - support-2550-cached-taxonomy
    - support-2550-taxonomy-reading
    - support-2550-curation-scope
    - support-2550-source-reading
    - support-2550-query-lotus_occurrences
    - support-2550-query-chebi_origins
    - support-2550-query-cyanometdb_occurrences
    - support-2550-query-pubchem_bioassay
    - support-2550-query-bindingdb_targets
    - support-2550-query-antibioticmech_inchikeys
    - support-2550-source-lotus_occurrences-0
    - support-2550-source-lotus_occurrences-1
    - support-2550-source-lotus_occurrences-2
    - support-2550-source-lotus_occurrences-3
- area: consistency
  topic: Applicability of computed labels
  outcome: supported
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 predicts Amino acids
    and Peptides/Polyketides, Oligopeptides, and Cyclic peptides/Depsipeptides, with
    is_glycoside=false. The stored ring with amide and ester linkages is compatible
    with the broad cyclic-depsipeptide description, and no candidate sugar ring is
    present. Model pathway labels do not independently prove biosynthetic origin,
    enzyme functions or a polyketide route. MIBiG NRPS classification and UNCLASSIFIED
    filing remain separate assertions.
  assessment_id: support-2550-classification
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-classification-owner
  - support-2550-chemistry
  - support-2550-topology
  - support-2550-classification-seeder
  - support-2550-source-reading
  - support-2550-source-mibig_compounds-0
  - support-2550-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: NPClassifier version npclassifier.gnps2.org@2026-09-07 predicts Amino acids
      and Peptides/Polyketides, Oligopeptides, and Cyclic peptides/Depsipeptides,
      with is_glycoside=false. The stored ring with amide and ester linkages is compatible
      with the broad cyclic-depsipeptide description, and no candidate sugar ring
      is present. Model pathway labels do not independently prove biosynthetic origin,
      enzyme functions or a polyketide route. MIBiG NRPS classification and UNCLASSIFIED
      filing remain separate assertions.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2550-classification-owner
    - support-2550-chemistry
    - support-2550-topology
    - support-2550-classification-seeder
    - support-2550-source-reading
    - support-2550-source-mibig_compounds-0
    - support-2550-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: supported
  summary: The review covers the complete owner and three histories, the accepted
    40-input canonical intake, all nine assigned source frames and 6 positive rows,
    relevant retained cache stanzas, and both complete saved molecular forms. No maintained-reader
    check applies because mechanism roots are absent. All retained evidence remains
    usable within its stated scope, while natural identity, primary experimental verification
    and full authority coverage remain limited. Full QC, complete OAK authority coverage
    and primary-source cross-checking remain unavailable, so review completion is
    partial. No record, status or history is edited.
  assessment_id: support-2550-completion
  target_ids:
  - naturalproductmech:mibig-5ab77d877b
  evidence_ids:
  - support-2550-owner
  - support-2550-capture
  - support-2550-intake
  - support-2550-intake-acceptance
  - support-2550-intake-reading
  - support-2550-inventory-acceptance
  - support-2550-plan
  - support-2550-plan-acceptance
  - support-2550-source-reading
  - support-2550-source-notes
  - support-2550-molecular-reading
  - support-2550-diagnostic-acceptance
  - support-2550-diagnostic-execution
  - support-2550-diagnostic-stderr
  - support-2550-review-profile
  dimensions:
  - name: review_completion
    value: The review covers the complete owner and three histories, the accepted
      40-input canonical intake, all nine assigned source frames and 6 positive rows,
      relevant retained cache stanzas, and both complete saved molecular forms. No
      maintained-reader check applies because mechanism roots are absent. All retained
      evidence remains usable within its stated scope, while natural identity, primary
      experimental verification and full authority coverage remain limited. Full QC,
      complete OAK authority coverage and primary-source cross-checking remain unavailable,
      so review completion is partial. No record, status or history is edited.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2550-owner
    - support-2550-capture
    - support-2550-intake
    - support-2550-intake-acceptance
    - support-2550-intake-reading
    - support-2550-inventory-acceptance
    - support-2550-plan
    - support-2550-plan-acceptance
    - support-2550-source-reading
    - support-2550-source-notes
    - support-2550-molecular-reading
    - support-2550-diagnostic-acceptance
    - support-2550-diagnostic-execution
    - support-2550-diagnostic-stderr
    - support-2550-review-profile
findings: []
actions: []
limitations:
- 'Retained local evidence only: original publications, fresh taxonomy, sequences
  and natural-identity verification were not accessed.'
- Matching normalized identifiers do not establish a unique fixed graph or tautomer.
  False canonical comparisons and empty direct atom maps remain explicit; original
  diagnostic stderr is empty.
- Producer, locus, occurrence and computational classification claims retain separate
  evidence grades; historical curator access is not current primary-source verification.
- Full QC, complete OAK authority coverage and primary-source cross-checking remain
  unavailable. No source, native status or history edit was made.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Support personally read five complete selected owners/history and ten saved molecular
  forms: 1,022 atom rows and 1,070 bond rows. Assigned retained-source reading covers
  45 frames, 21 rows and 245 fields; BGC other-context and Native cache/curation work
  remain separately attributed.'
- The accepted last-five canonical input scope is 228 placements across 48 paths.
  Original inventory scope was 417/53; the explicit diagnostic-only supplement gives
  operative 447/56 globally without adding assay outcomes.
- No requests, source replays, molecular reparses or owner edits were performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-255
```
