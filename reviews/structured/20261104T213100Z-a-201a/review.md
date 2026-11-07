# Local evidence review: A-201A

- Review: 20261104T213100Z-a-201a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T21:03:15.535000Z
- Finished UTC: 2026-11-04T21:31:00.194669Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

A-201A retains its BGC0873 minted identity and a stereochemical encoding distinct from selected a201a. The accepted diagnostic preserves one amide/imidic representation difference, two false canonical SMILES comparisons and an empty direct atom map. Source-asserted producer and unstated locus evidence remain bounded; no source edit is supported.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2456; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-ee9664cae0 | data/natural_products/unclassified/a-201a.yaml | generated | A-201A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-ee9664cae0 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-ee9664cae0 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-ee9664cae0 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-ee9664cae0 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-ee9664cae0 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-ee9664cae0 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-ee9664cae0 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-ee9664cae0 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and exact source correspondence

identity: supported. Targets: naturalproductmech:mibig-ee9664cae0.

The retained minted identifier naturalproductmech:mibig-ee9664cae0 and full key HELPZWNRUYNCJQ-WYPDLKSPSA-N join MIBiG BGC0000873 and PubChem CID76900419. Selected a201a has a different minted identifier, BGC1138 and full key HELPZWNRUYNCJQ-KLBOBXLXSA-N. Their literal InChI t26+ versus t26- and different isomeric canonical strings preserve an encoded stereochemical distinction despite the shared formula/connectivity block. Reciprocal raw inputs support comparison, not name-based deduplication, natural equivalence or a source-error finding. No exact retained ChEBI structure match was found.

### Stored forms and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-ee9664cae0.

Both original forms parse as neutral C37H50N6O14, 57 atoms/62 bonds; eight comparisons are true and both canonical SMILES comparisons are false, with no direct atom correspondence. The SMILES amide C25(=O26)-N27H becomes reconstructed C33(O48H)=N40, consistent with a bounded amide/imidic representation difference. Both forms retain 12 specified tetrahedral centres and two specified double bonds; reconstruction adds one unspecified C=N candidate. The source stereo_complete=true flag concerns the extractor’s tetrahedral test, not every double bond or natural stereochemistry. One saturated C5O ring and additional O-containing five-membered rings are encoded; motif counts do not assign sugar residues. Full-graph identity was not established.

### Producer and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-ee9664cae0.

MIBiG BGC0873 version 3 is active/questionable with unknown completeness. Saccharothrix mutabilis subsp. capreolus NCBITaxon:66854 is SOURCE_ASSERTION, while X84374.3 is CLUSTER_UNSTATED with no retained coordinates or locus-evidence methods. These are separate grades. Cached Nocardia capreola and Streptomyces capreolus synonyms do not establish current taxonomy or transfer the characterized Marinactinospora/BGC1138 evidence from the other selected A201 owner.

### Citation tier and history scope

evidence: supported. Targets: naturalproductmech:mibig-ee9664cae0.

PMID7737149 is an ENTRY-level database citation, not personally verified compound-specific primary evidence. The two complete seed-history events record ingestion, not independent experiments. PubChem and source concepts retain their database attribution; the unresolved queue is a lead, not an additional source or finding.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-ee9664cae0.

No occurrences, bioactivities, molecular_targets or mechanism roots are declared in this complete owner. The exact PubChem row 1979 is a blank-AID no-assay-data sentinel, not inactivity. Recorded LOTUS, ChEBI-origin, CyanoMetDB, BindingDB and AntibioticMech queries are empty within their retained predicates; this is not global biological absence. The other A201 owner’s LOTUS occurrence and producer grade do not transfer.

### Versioned classification applicability

consistency: unknown. Targets: naturalproductmech:mibig-ee9664cae0.

NPClassifier retains empty pathway/superclass/class arrays and is_glycoside=true. The O-linked saturated C5O ring plus O-containing five-membered rings and N-linked heterocycle are compatible with a glycosylated/nucleoside-like topology, but the bounded pattern output does not identify exact sugar residues or independently assign a family. Empty family arrays are not evidence of a source-ingestion defect.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-ee9664cae0.

The complete current owner and all 2 history events, exact selected source frames, 38 accepted canonical input placements and both original molecular forms were read. No mechanism roots are declared, so no maintained-reader call is applicable to this owner. The review is partial/pass_with_limitations: full QC/OAK and fresh primary, taxonomy and natural-state verification remain unavailable under the outbound hold. Queue leads remain unresolved without a supported correction; no finding, action or source/status/history edit is proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2456-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/a-201a.yaml; Whole current plaintext including complete curation_history | supports | Complete owner and all 2 history events personally read; current exact bytes retained. |
| support-2456-capture | /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json; /records/5/owner_document | supports | Complete raw captured owner, including exact root absence and history. No graph, pathway, external component or molecular-target root is declared. |
| support-2456-grounding-owner | /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json; /records/5/owner_document/identifier; /records/5/owner_document/label; /records/5/owner_document/chemical_structure; /records/5/owner_document/source_concepts; /records/5/owner_document/xrefs; /records/5/owner_document/grounding_status; /records/5/owner_document/grounding_notes | supports | Retained minted identifier, full key, source structure, source concepts and grounding text. Any present cross-reference remains a retained assertion, not fresh external identity verification. |
| support-2456-origin-owner | /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json; /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters; /records/5/owner_document/producer_taxon_groups | supports | Complete current producer/locus assertions, distinct grades, coordinates and methods where present; source and implemented-curation scopes remain separate. |
| support-2456-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json; /records/5/owner_document | supports | Complete owner supplies bounded occurrence/activity/target presence or absence; historical graph notes are not silently promoted to a measured pharmacological assay. |
| support-2456-classification-owner | /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json; /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification; /records/5/owner_document/bgc_class; /records/5/owner_document/biosynthesis_origin | supports | Versioned model output and pinned filing are retained separately from source BGC/compound-class assertions. |
| support-2456-direct-contexts | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-target-input-plan-001.json; /records/5/proposed_companion_paths; /records/5/direct_companion_predicates; /records/5/identity_comparison_paths; /records/5/additional_context_roles | context_only | Direct BGC companion paths are empty for this owner. The separately named identity-comparison role, if present, compares the two selected A201 encodings without asserting a census relation, deduplication or transfer of biological evidence. |
| support-2456-intake | /private/tmp/npm-review-work/shared-next-batch246/intakes/2456-inspect-001.json; /targets; /source | supports | Actual canonical intake preserves the single target, input roles and future correction ownership. |
| support-2456-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch246/root-intake-acceptance-001.json; /status; /intakes; /source_plan; /verification | supports | ROOT accepts the ten original canonical intakes and this exact composed plan. |
| support-2456-intake-reading | /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-last-five-molecular-intake-reading-001.json; /reading; /records/0/target; /records/0/intake; /coverage | supports | Support personally read all five actual target/ownership documents and 187 input placements across 41 paths. |
| support-2456-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch246/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; extraction is not fresh primary verification. |
| support-2456-plan | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-target-input-plan-001.json; /records/5/proposed_input_paths; /records/5/proposed_input_count | supports | Actual input map agrees with this canonical intake. |
| support-2456-plan-execution | /private/tmp/npm-review-work/shared-next-batch246/bgc-source-plan-execution-001.json; /plan; /exit_code; /original_terminal; /original_tools | supports | Original composer exited0 once; ROOT intake acceptance supplies the exact plan authority. |
| support-2456-source-reading | /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-source-reading-001.json; /partition; /per_context; /reading_scope; /physical_join_verification; /cautions | supports | Support personally read 30 positive placements/356 fields and 72 complete frames, including all 45 selected frames/18 rows/223 fields. The three isodomoic companions are separately credited; ROOT read the selected CPA context. No duplicated positive-row credit. |
| support-2456-source-notes | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Joint notes preserve disjoint BGC/ROOT/Support source credit and Native cache/curation interpretation. |
| support-2456-molecular-reading | /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/0; /representation_notes; /limits; /A201_comparison | supports | Support personally read all ten paired forms: 600 atom rows and 642 bond rows, every stereo/motif/map field and all 187 actual intake roles. Saved representations remain distinct where canonical comparisons fail; no reparse. |
| support-2456-a201-comparison | /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-last-five-molecular-intake-reading-001.json; /A201_comparison; /records/0; /records/2 | context_only | Exact saved reciprocal comparison preserves distinct full keys and t26 encodings. In the reconstructed tables the atom/bond-field difference is the atom 25 tetrahedral tag/CIP; this is encoded distinction, not natural identity or a correction finding. |
| support-2456-a201-both-owners | /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json; /records/5/owner_document; /records/7/owner_document | context_only | Both complete selected A201 owners retain their distinct source identity, BGC, producer/locus, occurrence and history assertions; no evidence is transferred between them. |
| support-2456-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/9 | context_only | Relevant complete cached taxon stanzas preserve names and synonyms. Cached names do not independently establish producing strains or fresh taxonomy. |
| support-2456-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch246-tentative/native-prep/native-current246-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation | context_only | Native complete cache/merge reading remains explicitly attributed; Support separately read the six relevant selected stanzas. |
| support-2456-curation-scope | /private/tmp/npm-review-work/shared-next-batch246-tentative/native-prep/native-current246-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Native exact implemented scan has one applicable override for the unselected 2-oxo CPA context; none applies to these five identities. Unrelated lexical matches do not become corrections. |
| support-2456-chemistry | /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/formula_comparison_scope; /records/5/comparisons; /records/5/atom_correspondence | supports | Eight true and two false canonical SMILES comparisons, with empty direct atom map; normalized key/formula agreement does not prove fixed-form identity. |
| support-2456-topology | /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/smiles; /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence | supports | Both original forms parse as neutral C37H50N6O14, 57 atoms/62 bonds; eight comparisons are true and both canonical SMILES comparisons are false, with no direct atom correspondence. The SMILES amide C25(=O26)-N27H becomes reconstructed C33(O48H)=N40, consistent with a bounded amide/imidic representation difference. Both forms retain 12 specified tetrahedral centres and two specified double bonds; reconstruction adds one unspecified C=N candidate. One saturated C5O ring and additional O-containing five-membered rings are encoded; motif counts do not assign sugar residues. Full-graph identity was not established. |
| support-2456-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/5; /global_warning_count; /interpretation_boundary | supports | ROOT accepts this original diagnostic outcome, preserving any false canonical comparisons and the four global undefined-stereo warnings without assigning them to individual records. |
| support-2456-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic command, source, exit0 and exact streams, with no retry or external request. |
| support-2456-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | Four original undefined-stereo warning lines are retained globally. No warning is assigned to an individual owner. |
| support-2456-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2456-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2456-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2456-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2456-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Physical row 950: BGC0000873 version 3, A-201A; Saccharothrix mutabilis subsp. capreolus SOURCE_ASSERTION, locus CLUSTER_UNSTATED; PMID:7737149 at ENTRY scope. All retained structure, coordinates, methods and source classes remain in the exact row. |
| support-2456-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 950 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2456-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/npclassifier/matches/0 | supports | Physical row 805: npclassifier.gnps2.org@2026-09-07: //, glycoside=true; model assertion only. |
| support-2456-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 805 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2456-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 1 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-source-pubchem_bioassay-0 | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/pubchem_bioassay/matches/0 | supports | Physical row 1979: CID76900419, blank AID and no assay data; no activity/inactivity or measurement. |
| support-2456-physical-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 1979 | context_only | All fields in these positive placements join the current physical retained table. |
| support-2456-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| support-2456-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json; /contexts/10/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; any zero result is bounded to its exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-246/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-246/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-246/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-246/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-246/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; primary papers, fresh taxonomy, sequence/construct identity and natural stereochemistry were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. Both canonical SMILES comparisons are false and the direct atom map is empty for this owner; representation-specific motifs and any unspecified stereo are preserved.
- Four undefined-stereo warnings are global and unassigned to individual records. Producer, occurrence, locus, citation, classifier and assay scopes remain distinct; no source/status/history edit is proposed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support whole selected owners/history and three isodomoic companions carry exact current bytes. Source credit is BGC 26 + ROOT 17 + Support 30 + Native 0 positive placements; no duplicate row credit.
- Support personally read all ten saved last-five forms: 600 atom rows/642 bond rows, complete fields and maps, plus 187 intake placements across 41 paths. A201 reciprocal raw inputs preserve distinct encoded identities without a name-based deduplication inference.
- Support operated canonical intakes; Native operated the diagnostic under ROOT delegation. Historical execution observer labels do not change operator attribution. No selected last-five owner has an applicable maintained-reader route.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T213100Z-a-201a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: A-201A'
started_at: '2026-11-04T21:03:15.535000Z'
finished_at: '2026-11-04T21:31:00.194669Z'
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
summary: A-201A retains its BGC0873 minted identity and a stereochemical encoding
  distinct from selected a201a. The accepted diagnostic preserves one amide/imidic
  representation difference, two false canonical SMILES comparisons and an empty direct
  atom map. Source-asserted producer and unstated locus evidence remain bounded; no
  source edit is supported.
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
  - path: data/natural_products/unclassified/a-201a.yaml
    sha256: dedd8584d61f4b391d6a286561cba8c93d862e16117061fa7d50242ddc3dde5a
    role: target
  - path: data/natural_products/unclassified/a201a.yaml
    sha256: 303e37bb67617cdc91de1860651914ef45cecb404e12b91f36d8a934bd8ab4bf
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2456; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-ee9664cae0
targets:
- target_id: naturalproductmech:mibig-ee9664cae0
  path: data/natural_products/unclassified/a-201a.yaml
  label: A-201A
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
    path: data/natural_products/unclassified/a201a.yaml
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
  - naturalproductmech:mibig-ee9664cae0
  command: just validate-strict data/natural_products/unclassified/4-oxomacrophorin-a.yaml
    data/natural_products/unclassified/5-epimacrophorin-b.yaml data/natural_products/unclassified/5-isoprenylindole-3-carboxylate-d-glycosyl-ester.yaml
    data/natural_products/unclassified/6ar-11as-11br-10-acetyl-11-hydroxy-7-7-dimethyl-2-6-6a-7-11a-11b-hexahydro-9h-py.yaml
    data/natural_products/unclassified/7-carboxyn-geranyl-l-glutamic-acid.yaml data/natural_products/unclassified/a-201a.yaml
    data/natural_products/unclassified/a-94964.yaml data/natural_products/unclassified/a201a.yaml
    data/natural_products/unclassified/abt1.yaml data/natural_products/unclassified/acetylaranotin.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-246/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-ee9664cae0
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-246/validate-all-001.tsv
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
  - naturalproductmech:mibig-ee9664cae0
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
  - naturalproductmech:mibig-ee9664cae0
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
  - naturalproductmech:mibig-ee9664cae0
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-246/review-queue-001.tsv
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
  - naturalproductmech:mibig-ee9664cae0
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2456-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/a-201a.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Complete owner and all 2 history events personally read; current exact
    bytes retained.
  snapshot_sha256: dedd8584d61f4b391d6a286561cba8c93d862e16117061fa7d50242ddc3dde5a
- evidence_id: support-2456-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Complete raw captured owner, including exact root absence and history.
    No graph, pathway, external component or molecular-target root is declared.
  snapshot_sha256: 688cf182ab3c72e7f423eb13bff77ec3a20bfb7faa7e7a611e35c7f76bef21a2
- evidence_id: support-2456-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json
  locator: /records/5/owner_document/identifier; /records/5/owner_document/label;
    /records/5/owner_document/chemical_structure; /records/5/owner_document/source_concepts;
    /records/5/owner_document/xrefs; /records/5/owner_document/grounding_status; /records/5/owner_document/grounding_notes
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Retained minted identifier, full key, source structure, source concepts
    and grounding text. Any present cross-reference remains a retained assertion,
    not fresh external identity verification.
  snapshot_sha256: 688cf182ab3c72e7f423eb13bff77ec3a20bfb7faa7e7a611e35c7f76bef21a2
- evidence_id: support-2456-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json
  locator: /records/5/owner_document/producer_organisms; /records/5/owner_document/biosynthetic_gene_clusters;
    /records/5/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Complete current producer/locus assertions, distinct grades, coordinates
    and methods where present; source and implemented-curation scopes remain separate.
  snapshot_sha256: 688cf182ab3c72e7f423eb13bff77ec3a20bfb7faa7e7a611e35c7f76bef21a2
- evidence_id: support-2456-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json
  locator: /records/5/owner_document
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Complete owner supplies bounded occurrence/activity/target presence or
    absence; historical graph notes are not silently promoted to a measured pharmacological
    assay.
  snapshot_sha256: 688cf182ab3c72e7f423eb13bff77ec3a20bfb7faa7e7a611e35c7f76bef21a2
- evidence_id: support-2456-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json
  locator: /records/5/owner_document/np_pathway; /records/5/owner_document/np_classification;
    /records/5/owner_document/bgc_class; /records/5/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Versioned model output and pinned filing are retained separately from source
    BGC/compound-class assertions.
  snapshot_sha256: 688cf182ab3c72e7f423eb13bff77ec3a20bfb7faa7e7a611e35c7f76bef21a2
- evidence_id: support-2456-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-target-input-plan-001.json
  locator: /records/5/proposed_companion_paths; /records/5/direct_companion_predicates;
    /records/5/identity_comparison_paths; /records/5/additional_context_roles
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Direct BGC companion paths are empty for this owner. The separately named
    identity-comparison role, if present, compares the two selected A201 encodings
    without asserting a census relation, deduplication or transfer of biological evidence.
  snapshot_sha256: 24eb44c19003762fec70fdd9ebaecafeba03b3a979c088aa26d90ca90807e28f
- evidence_id: support-2456-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/intakes/2456-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Actual canonical intake preserves the single target, input roles and future
    correction ownership.
  snapshot_sha256: a3bc872c2e8d9bcc0b3e280c6b61602578e6329c4a38328dc3b4f7dbedffb291
- evidence_id: support-2456-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/root-intake-acceptance-001.json
  locator: /status; /intakes; /source_plan; /verification
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: ROOT accepts the ten original canonical intakes and this exact composed
    plan.
  snapshot_sha256: 091c4706eb2ab31fcf5d43c36b04a9fdbd350b59c9b51308370d635dc77ef7e1
- evidence_id: support-2456-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/0/target; /records/0/intake; /coverage
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Support personally read all five actual target/ownership documents and
    187 input placements across 41 paths.
  snapshot_sha256: bb8f1f92de7eda1c2960090a3191516d76bebac874caea7fbf029310173c57ba
- evidence_id: support-2456-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; extraction is not fresh
    primary verification.
  snapshot_sha256: 661d2c93bd6b71abfbcaac03c2c6bee2810a1c475b854da79920fa5d5425dd82
- evidence_id: support-2456-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-target-input-plan-001.json
  locator: /records/5/proposed_input_paths; /records/5/proposed_input_count
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Actual input map agrees with this canonical intake.
  snapshot_sha256: 24eb44c19003762fec70fdd9ebaecafeba03b3a979c088aa26d90ca90807e28f
- evidence_id: support-2456-plan-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/bgc-source-plan-execution-001.json
  locator: /plan; /exit_code; /original_terminal; /original_tools
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Original composer exited0 once; ROOT intake acceptance supplies the exact
    plan authority.
  snapshot_sha256: 5719eba596ef36196b39d182fd05babe5bf21b43b4a81fcf21110884364f4199
- evidence_id: support-2456-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-source-reading-001.json
  locator: /partition; /per_context; /reading_scope; /physical_join_verification;
    /cautions
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Support personally read 30 positive placements/356 fields and 72 complete
    frames, including all 45 selected frames/18 rows/223 fields. The three isodomoic
    companions are separately credited; ROOT read the selected CPA context. No duplicated
    positive-row credit.
  snapshot_sha256: 9a68c0e169a43abc671c2e30d87aec9772d910322249f7e1b1ae61051cb50076
- evidence_id: support-2456-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Joint notes preserve disjoint BGC/ROOT/Support source credit and Native
    cache/curation interpretation.
  snapshot_sha256: f2d50686d4f5025330324d746a12fb2f58bdbf31ff885fd08a63fd1bcbe5d475
- evidence_id: support-2456-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/0; /representation_notes; /limits; /A201_comparison
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: 'Support personally read all ten paired forms: 600 atom rows and 642 bond
    rows, every stereo/motif/map field and all 187 actual intake roles. Saved representations
    remain distinct where canonical comparisons fail; no reparse.'
  snapshot_sha256: bb8f1f92de7eda1c2960090a3191516d76bebac874caea7fbf029310173c57ba
- evidence_id: support-2456-a201-comparison
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/support-prep/support-current246-last-five-molecular-intake-reading-001.json
  locator: /A201_comparison; /records/0; /records/2
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Exact saved reciprocal comparison preserves distinct full keys and t26
    encodings. In the reconstructed tables the atom/bond-field difference is the atom
    25 tetrahedral tag/CIP; this is encoded distinction, not natural identity or a
    correction finding.
  snapshot_sha256: bb8f1f92de7eda1c2960090a3191516d76bebac874caea7fbf029310173c57ba
- evidence_id: support-2456-a201-both-owners
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246/owner-capture-DATA-001.json
  locator: /records/5/owner_document; /records/7/owner_document
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Both complete selected A201 owners retain their distinct source identity,
    BGC, producer/locus, occurrence and history assertions; no evidence is transferred
    between them.
  snapshot_sha256: 688cf182ab3c72e7f423eb13bff77ec3a20bfb7faa7e7a611e35c7f76bef21a2
- evidence_id: support-2456-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/9
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Relevant complete cached taxon stanzas preserve names and synonyms. Cached
    names do not independently establish producing strains or fresh taxonomy.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
- evidence_id: support-2456-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/native-prep/native-current246-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Native complete cache/merge reading remains explicitly attributed; Support
    separately read the six relevant selected stanzas.
  snapshot_sha256: fc07c051c0d96be27e7a4eb5a7899530a138b691d326b7e27c47bf9cff1ead0e
- evidence_id: support-2456-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/native-prep/native-current246-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Native exact implemented scan has one applicable override for the unselected
    2-oxo CPA context; none applies to these five identities. Unrelated lexical matches
    do not become corrections.
  snapshot_sha256: 4ea934fac919b3937992c02f507c3ef0c133fdca93d44deed9d8b062cbc522fb
  search_scope: '{"whole_ignored_inclusive_scan": "/private/tmp/npm-review-work/shared-next-batch246-tentative/native-prep/native-current246-implemented-curation-scan-001.json",
    "selected_identifier": "naturalproductmech:mibig-ee9664cae0", "selected_full_key":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "scope": "Retained implemented tables and exact
    applicability, not universal evidence absence."}'
- evidence_id: support-2456-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/formula_comparison_scope;
    /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Eight true and two false canonical SMILES comparisons, with empty direct
    atom map; normalized key/formula agreement does not prove fixed-form identity.
  snapshot_sha256: 2057affe416fc50cfd5fa881ae590c5a8eb68aa001177411bc2c2262696c2bf6
- evidence_id: support-2456-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/smiles; /records/5/inchi; /records/5/comparisons;
    /records/5/atom_correspondence
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Both original forms parse as neutral C37H50N6O14, 57 atoms/62 bonds; eight
    comparisons are true and both canonical SMILES comparisons are false, with no
    direct atom correspondence. The SMILES amide C25(=O26)-N27H becomes reconstructed
    C33(O48H)=N40, consistent with a bounded amide/imidic representation difference.
    Both forms retain 12 specified tetrahedral centres and two specified double bonds;
    reconstruction adds one unspecified C=N candidate. One saturated C5O ring and
    additional O-containing five-membered rings are encoded; motif counts do not assign
    sugar residues. Full-graph identity was not established.
  snapshot_sha256: 2057affe416fc50cfd5fa881ae590c5a8eb68aa001177411bc2c2262696c2bf6
- evidence_id: support-2456-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/5; /global_warning_count; /interpretation_boundary
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: ROOT accepts this original diagnostic outcome, preserving any false canonical
    comparisons and the four global undefined-stereo warnings without assigning them
    to individual records.
  snapshot_sha256: 6a602d3ed33b573f8dc753d82febcf527f82dd68695d4ad4a7346fb9c4dac348
- evidence_id: support-2456-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Original diagnostic command, source, exit0 and exact streams, with no retry
    or external request.
  snapshot_sha256: cca547eef58e3295b88aa5015a7149e72af11b936cf7919e8a2faa2f5617f060
- evidence_id: support-2456-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch246/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Four original undefined-stereo warning lines are retained globally. No
    warning is assigned to an individual owner.
  snapshot_sha256: 6db5d0c7e4c4e4100a356c59de2dc4ad9dfeea23300b31c8a7a31f77b69dda6b
- evidence_id: support-2456-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2456-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2456-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2456-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2456-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/mibig_compounds",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: 'Physical row 950: BGC0000873 version 3, A-201A; Saccharothrix mutabilis
    subsp. capreolus SOURCE_ASSERTION, locus CLUSTER_UNSTATED; PMID:7737149 at ENTRY
    scope. All retained structure, coordinates, methods and source classes remain
    in the exact row.'
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
- evidence_id: support-2456-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 950
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2456-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/chebi_structures",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved lotus_occurrences frame has 0 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; any zero
    result is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; any zero result is
    bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/npclassifier",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: 'Physical row 805: npclassifier.gnps2.org@2026-09-07: //, glycoside=true;
    model assertion only.'
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
- evidence_id: support-2456-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 805
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2456-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 1 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-source-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/pubchem_bioassay/matches/0
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: 'Physical row 1979: CID76900419, blank AID and no assay data; no activity/inactivity
    or measurement.'
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
- evidence_id: support-2456-physical-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 1979
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: context_only
  summary: All fields in these positive placements join the current physical retained
    table.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2456-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; any zero result
    is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; any zero
    result is bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "HELPZWNRUYNCJQ-WYPDLKSPSA-N", "saved_frame": "/contexts/10/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: support-2456-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch246-tentative/bgc-prep/bgc-conditional246-source-inventory-DATA-001.json
  locator: /contexts/10/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T21:25:09.412435Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; any zero result is
    bounded to its exact retained predicate.
  snapshot_sha256: ce12c8c3d90615fbcdfef14a27f9c360d055872f0e7663f49e6b187c40ae0585
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/10/source_scope_inventory/joins/chebi_origins",
    "scope": "Immutable local retained source; no replay or universal absence claim."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-246/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json
  accessed_at: '2026-11-04T21:07:49.197100Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: a98abc30fa3cd51029e1829adf321a91fa45b5ff95fb566663f15cb38ee1c1fa
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-246/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json
  accessed_at: '2026-11-04T21:08:15.452126Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: d70739603e27733c2c52efde9e3e6c84a88a5bc0146ae905dbd2fac6ac74250d
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-246/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json
  accessed_at: '2026-11-04T21:08:36.136196Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-246/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json
  accessed_at: '2026-11-04T21:09:11.854678Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-246/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-246/native-current246-five-gates-execution-001.json
  accessed_at: '2026-11-04T21:09:24.158160Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: bca7ad7e8e20f1a311f2bc857314b8127ac370ba73d0bf4edddc4909f8c8753e
assessments:
- area: identity
  topic: Retained identity and exact source correspondence
  outcome: supported
  summary: The retained minted identifier naturalproductmech:mibig-ee9664cae0 and
    full key HELPZWNRUYNCJQ-WYPDLKSPSA-N join MIBiG BGC0000873 and PubChem CID76900419.
    Selected a201a has a different minted identifier, BGC1138 and full key HELPZWNRUYNCJQ-KLBOBXLXSA-N.
    Their literal InChI t26+ versus t26- and different isomeric canonical strings
    preserve an encoded stereochemical distinction despite the shared formula/connectivity
    block. Reciprocal raw inputs support comparison, not name-based deduplication,
    natural equivalence or a source-error finding. No exact retained ChEBI structure
    match was found.
  assessment_id: support-2456-identity
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-grounding-owner
  - support-2456-chemistry
  - support-2456-direct-contexts
  - support-2456-query-chebi_structures
  - support-2456-source-mibig_compounds-0
  - support-2456-a201-comparison
  - support-2456-a201-both-owners
  - support-2456-source-reading
  dimensions:
  - name: standard_inchi_key
    value: HELPZWNRUYNCJQ-WYPDLKSPSA-N; retained full key, not independent natural
      identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2456-grounding-owner
    - support-2456-chemistry
    - support-2456-direct-contexts
    - support-2456-query-chebi_structures
    - support-2456-source-mibig_compounds-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
  - name: grounding_scope
    value: The retained minted identifier naturalproductmech:mibig-ee9664cae0 and
      full key HELPZWNRUYNCJQ-WYPDLKSPSA-N join MIBiG BGC0000873 and PubChem CID76900419.
      Selected a201a has a different minted identifier, BGC1138 and full key HELPZWNRUYNCJQ-KLBOBXLXSA-N.
      Their literal InChI t26+ versus t26- and different isomeric canonical strings
      preserve an encoded stereochemical distinction despite the shared formula/connectivity
      block. Reciprocal raw inputs support comparison, not name-based deduplication,
      natural equivalence or a source-error finding. No exact retained ChEBI structure
      match was found.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2456-grounding-owner
    - support-2456-chemistry
    - support-2456-direct-contexts
    - support-2456-query-chebi_structures
    - support-2456-source-mibig_compounds-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
- area: representation
  topic: Stored forms and stereochemistry
  outcome: supported
  summary: Both original forms parse as neutral C37H50N6O14, 57 atoms/62 bonds; eight
    comparisons are true and both canonical SMILES comparisons are false, with no
    direct atom correspondence. The SMILES amide C25(=O26)-N27H becomes reconstructed
    C33(O48H)=N40, consistent with a bounded amide/imidic representation difference.
    Both forms retain 12 specified tetrahedral centres and two specified double bonds;
    reconstruction adds one unspecified C=N candidate. The source stereo_complete=true
    flag concerns the extractor’s tetrahedral test, not every double bond or natural
    stereochemistry. One saturated C5O ring and additional O-containing five-membered
    rings are encoded; motif counts do not assign sugar residues. Full-graph identity
    was not established.
  assessment_id: support-2456-representation
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-grounding-owner
  - support-2456-chemistry
  - support-2456-topology
  - support-2456-molecular-reading
  - support-2456-diagnostic-acceptance
  - support-2456-structure-schema
  - support-2456-stereo-method
  - support-2456-a201-comparison
  - support-2456-a201-both-owners
  - support-2456-source-reading
  dimensions:
  - name: stereochemistry_scope
    value: Both original forms parse as neutral C37H50N6O14, 57 atoms/62 bonds; eight
      comparisons are true and both canonical SMILES comparisons are false, with no
      direct atom correspondence. The SMILES amide C25(=O26)-N27H becomes reconstructed
      C33(O48H)=N40, consistent with a bounded amide/imidic representation difference.
      Both forms retain 12 specified tetrahedral centres and two specified double
      bonds; reconstruction adds one unspecified C=N candidate. The source stereo_complete=true
      flag concerns the extractor’s tetrahedral test, not every double bond or natural
      stereochemistry. One saturated C5O ring and additional O-containing five-membered
      rings are encoded; motif counts do not assign sugar residues. Full-graph identity
      was not established.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2456-grounding-owner
    - support-2456-chemistry
    - support-2456-topology
    - support-2456-molecular-reading
    - support-2456-diagnostic-acceptance
    - support-2456-structure-schema
    - support-2456-stereo-method
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
  - name: representation_correspondence
    value: Both original forms parse as neutral C37H50N6O14, 57 atoms/62 bonds; eight
      comparisons are true and both canonical SMILES comparisons are false, with no
      direct atom correspondence. The SMILES amide C25(=O26)-N27H becomes reconstructed
      C33(O48H)=N40, consistent with a bounded amide/imidic representation difference.
      Both forms retain 12 specified tetrahedral centres and two specified double
      bonds; reconstruction adds one unspecified C=N candidate. The source stereo_complete=true
      flag concerns the extractor’s tetrahedral test, not every double bond or natural
      stereochemistry. One saturated C5O ring and additional O-containing five-membered
      rings are encoded; motif counts do not assign sugar residues. Full-graph identity
      was not established.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2456-grounding-owner
    - support-2456-chemistry
    - support-2456-topology
    - support-2456-molecular-reading
    - support-2456-diagnostic-acceptance
    - support-2456-structure-schema
    - support-2456-stereo-method
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: MIBiG BGC0873 version 3 is active/questionable with unknown completeness.
    Saccharothrix mutabilis subsp. capreolus NCBITaxon:66854 is SOURCE_ASSERTION,
    while X84374.3 is CLUSTER_UNSTATED with no retained coordinates or locus-evidence
    methods. These are separate grades. Cached Nocardia capreola and Streptomyces
    capreolus synonyms do not establish current taxonomy or transfer the characterized
    Marinactinospora/BGC1138 evidence from the other selected A201 owner.
  assessment_id: support-2456-provenance
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-origin-owner
  - support-2456-source-reading
  - support-2456-direct-contexts
  - support-2456-cached-taxonomy
  - support-2456-taxonomy-reading
  - support-2456-curation-scope
  - support-2456-source-mibig_compounds-0
  - support-2456-a201-comparison
  - support-2456-a201-both-owners
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0873 version 3 is active/questionable with unknown completeness.
      Saccharothrix mutabilis subsp. capreolus NCBITaxon:66854 is SOURCE_ASSERTION,
      while X84374.3 is CLUSTER_UNSTATED with no retained coordinates or locus-evidence
      methods. These are separate grades. Cached Nocardia capreola and Streptomyces
      capreolus synonyms do not establish current taxonomy or transfer the characterized
      Marinactinospora/BGC1138 evidence from the other selected A201 owner.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2456-origin-owner
    - support-2456-source-reading
    - support-2456-direct-contexts
    - support-2456-cached-taxonomy
    - support-2456-taxonomy-reading
    - support-2456-curation-scope
    - support-2456-source-mibig_compounds-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
  - name: producer_evidence
    value: MIBiG BGC0873 version 3 is active/questionable with unknown completeness.
      Saccharothrix mutabilis subsp. capreolus NCBITaxon:66854 is SOURCE_ASSERTION,
      while X84374.3 is CLUSTER_UNSTATED with no retained coordinates or locus-evidence
      methods. These are separate grades. Cached Nocardia capreola and Streptomyces
      capreolus synonyms do not establish current taxonomy or transfer the characterized
      Marinactinospora/BGC1138 evidence from the other selected A201 owner.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2456-origin-owner
    - support-2456-source-reading
    - support-2456-direct-contexts
    - support-2456-cached-taxonomy
    - support-2456-taxonomy-reading
    - support-2456-curation-scope
    - support-2456-source-mibig_compounds-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
  - name: locus_evidence
    value: MIBiG BGC0873 version 3 is active/questionable with unknown completeness.
      Saccharothrix mutabilis subsp. capreolus NCBITaxon:66854 is SOURCE_ASSERTION,
      while X84374.3 is CLUSTER_UNSTATED with no retained coordinates or locus-evidence
      methods. These are separate grades. Cached Nocardia capreola and Streptomyces
      capreolus synonyms do not establish current taxonomy or transfer the characterized
      Marinactinospora/BGC1138 evidence from the other selected A201 owner.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2456-origin-owner
    - support-2456-source-reading
    - support-2456-direct-contexts
    - support-2456-cached-taxonomy
    - support-2456-taxonomy-reading
    - support-2456-curation-scope
    - support-2456-source-mibig_compounds-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
- area: evidence
  topic: Citation tier and history scope
  outcome: supported
  summary: PMID7737149 is an ENTRY-level database citation, not personally verified
    compound-specific primary evidence. The two complete seed-history events record
    ingestion, not independent experiments. PubChem and source concepts retain their
    database attribution; the unresolved queue is a lead, not an additional source
    or finding.
  assessment_id: support-2456-citations
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-owner
  - support-2456-origin-owner
  - support-2456-occurrence-activity-owner
  - support-2456-source-reading
  - support-2456-direct-contexts
  - support-2456-source-mibig_compounds-0
  - support-2456-source-npclassifier-0
  - support-2456-source-pubchem_bioassay-0
  - support-2456-a201-comparison
  - support-2456-a201-both-owners
  dimensions:
  - name: citation_scope
    value: PMID7737149 is an ENTRY-level database citation, not personally verified
      compound-specific primary evidence. The two complete seed-history events record
      ingestion, not independent experiments. PubChem and source concepts retain their
      database attribution; the unresolved queue is a lead, not an additional source
      or finding.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2456-owner
    - support-2456-origin-owner
    - support-2456-occurrence-activity-owner
    - support-2456-source-reading
    - support-2456-direct-contexts
    - support-2456-source-mibig_compounds-0
    - support-2456-source-npclassifier-0
    - support-2456-source-pubchem_bioassay-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
- area: evidence
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: No occurrences, bioactivities, molecular_targets or mechanism roots are
    declared in this complete owner. The exact PubChem row 1979 is a blank-AID no-assay-data
    sentinel, not inactivity. Recorded LOTUS, ChEBI-origin, CyanoMetDB, BindingDB
    and AntibioticMech queries are empty within their retained predicates; this is
    not global biological absence. The other A201 owner’s LOTUS occurrence and producer
    grade do not transfer.
  assessment_id: support-2456-occurrence
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-occurrence-activity-owner
  - support-2456-direct-contexts
  - support-2456-cached-taxonomy
  - support-2456-curation-scope
  - support-2456-query-lotus_occurrences
  - support-2456-query-chebi_origins
  - support-2456-query-cyanometdb_occurrences
  - support-2456-query-pubchem_bioassay
  - support-2456-query-bindingdb_targets
  - support-2456-query-antibioticmech_inchikeys
  - support-2456-source-pubchem_bioassay-0
  - support-2456-a201-comparison
  - support-2456-a201-both-owners
  - support-2456-source-reading
  dimensions:
  - name: occurrence_scope
    value: No occurrences, bioactivities, molecular_targets or mechanism roots are
      declared in this complete owner. The exact PubChem row 1979 is a blank-AID no-assay-data
      sentinel, not inactivity. Recorded LOTUS, ChEBI-origin, CyanoMetDB, BindingDB
      and AntibioticMech queries are empty within their retained predicates; this
      is not global biological absence. The other A201 owner’s LOTUS occurrence and
      producer grade do not transfer.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2456-occurrence-activity-owner
    - support-2456-direct-contexts
    - support-2456-cached-taxonomy
    - support-2456-curation-scope
    - support-2456-query-lotus_occurrences
    - support-2456-query-chebi_origins
    - support-2456-query-cyanometdb_occurrences
    - support-2456-query-pubchem_bioassay
    - support-2456-query-bindingdb_targets
    - support-2456-query-antibioticmech_inchikeys
    - support-2456-source-pubchem_bioassay-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
  - name: assay_target_scope
    value: No owner assay or target root; one blank-AID PubChem sentinel. No activity
      or mechanism is transferred from the distinct selected a201a owner.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2456-occurrence-activity-owner
    - support-2456-direct-contexts
    - support-2456-cached-taxonomy
    - support-2456-curation-scope
    - support-2456-query-lotus_occurrences
    - support-2456-query-chebi_origins
    - support-2456-query-cyanometdb_occurrences
    - support-2456-query-pubchem_bioassay
    - support-2456-query-bindingdb_targets
    - support-2456-query-antibioticmech_inchikeys
    - support-2456-source-pubchem_bioassay-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
- area: consistency
  topic: Versioned classification applicability
  outcome: unknown
  summary: NPClassifier retains empty pathway/superclass/class arrays and is_glycoside=true.
    The O-linked saturated C5O ring plus O-containing five-membered rings and N-linked
    heterocycle are compatible with a glycosylated/nucleoside-like topology, but the
    bounded pattern output does not identify exact sugar residues or independently
    assign a family. Empty family arrays are not evidence of a source-ingestion defect.
  assessment_id: support-2456-classification
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-classification-owner
  - support-2456-chemistry
  - support-2456-topology
  - support-2456-classification-seeder
  - support-2456-source-mibig_compounds-0
  - support-2456-source-npclassifier-0
  - support-2456-a201-comparison
  - support-2456-a201-both-owners
  - support-2456-source-reading
  dimensions:
  - name: classification_applicability
    value: NPClassifier retains empty pathway/superclass/class arrays and is_glycoside=true.
      The O-linked saturated C5O ring plus O-containing five-membered rings and N-linked
      heterocycle are compatible with a glycosylated/nucleoside-like topology, but
      the bounded pattern output does not identify exact sugar residues or independently
      assign a family. Empty family arrays are not evidence of a source-ingestion
      defect.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2456-classification-owner
    - support-2456-chemistry
    - support-2456-topology
    - support-2456-classification-seeder
    - support-2456-source-mibig_compounds-0
    - support-2456-source-npclassifier-0
    - support-2456-a201-comparison
    - support-2456-a201-both-owners
    - support-2456-source-reading
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: 'The complete current owner and all 2 history events, exact selected source
    frames, 38 accepted canonical input placements and both original molecular forms
    were read. No mechanism roots are declared, so no maintained-reader call is applicable
    to this owner. The review is partial/pass_with_limitations: full QC/OAK and fresh
    primary, taxonomy and natural-state verification remain unavailable under the
    outbound hold. Queue leads remain unresolved without a supported correction; no
    finding, action or source/status/history edit is proposed.'
  assessment_id: support-2456-completion
  target_ids:
  - naturalproductmech:mibig-ee9664cae0
  evidence_ids:
  - support-2456-owner
  - support-2456-capture
  - support-2456-intake
  - support-2456-intake-acceptance
  - support-2456-intake-reading
  - support-2456-inventory-acceptance
  - support-2456-plan
  - support-2456-plan-execution
  - support-2456-source-reading
  - support-2456-source-notes
  - support-2456-molecular-reading
  - support-2456-diagnostic-acceptance
  - support-2456-diagnostic-execution
  - support-2456-diagnostic-stderr
  - support-2456-review-profile
  dimensions:
  - name: review_completion
    value: 'The complete current owner and all 2 history events, exact selected source
      frames, 38 accepted canonical input placements and both original molecular forms
      were read. No mechanism roots are declared, so no maintained-reader call is
      applicable to this owner. The review is partial/pass_with_limitations: full
      QC/OAK and fresh primary, taxonomy and natural-state verification remain unavailable
      under the outbound hold. Queue leads remain unresolved without a supported correction;
      no finding, action or source/status/history edit is proposed.'
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2456-owner
    - support-2456-capture
    - support-2456-intake
    - support-2456-intake-acceptance
    - support-2456-intake-reading
    - support-2456-inventory-acceptance
    - support-2456-plan
    - support-2456-plan-execution
    - support-2456-source-reading
    - support-2456-source-notes
    - support-2456-molecular-reading
    - support-2456-diagnostic-acceptance
    - support-2456-diagnostic-execution
    - support-2456-diagnostic-stderr
    - support-2456-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; primary papers, fresh taxonomy, sequence/construct
  identity and natural stereochemistry were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Full-graph identity was not established. Both canonical SMILES comparisons are false
  and the direct atom map is empty for this owner; representation-specific motifs
  and any unspecified stereo are preserved.
- Four undefined-stereo warnings are global and unassigned to individual records.
  Producer, occurrence, locus, citation, classifier and assay scopes remain distinct;
  no source/status/history edit is proposed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support whole selected owners/history and three isodomoic companions carry exact
  current bytes. Source credit is BGC 26 + ROOT 17 + Support 30 + Native 0 positive
  placements; no duplicate row credit.
- 'Support personally read all ten saved last-five forms: 600 atom rows/642 bond rows,
  complete fields and maps, plus 187 intake placements across 41 paths. A201 reciprocal
  raw inputs preserve distinct encoded identities without a name-based deduplication
  inference.'
- Support operated canonical intakes; Native operated the diagnostic under ROOT delegation.
  Historical execution observer labels do not change operator attribution. No selected
  last-five owner has an applicable maintained-reader route.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-246
```
