# Local evidence review: citrulassin A

- Review: 20261105T130742Z-citrulassin-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T12:18:03.364380Z
- Finished UTC: 2026-11-05T13:07:42.386476Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

citrulassin A: retained identity, source-specific grades, taxonomy and representation limits assessed; computed labels remain separately qualified.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2560; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-1ea8852cad | data/natural_products/unclassified/citrulassin-a.yaml | generated | citrulassin A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-1ea8852cad | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-1ea8852cad | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-1ea8852cad | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-1ea8852cad | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-1ea8852cad | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-1ea8852cad | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-1ea8852cad | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-1ea8852cad | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding scope

identity: supported. Targets: naturalproductmech:mibig-1ea8852cad.

The MINTED owner naturalproductmech:mibig-1ea8852cad retains the exact full key JYSBHGIINWQTOH-JHTNTUONSA-N, MIBiG source label citrulassin A and declared source structure. Both saved forms reproduce the declared Standard InChI and full key. The exact retained ChEBI structure frame is empty, which bounds the historical minted-identifier rationale without a fresh authority search. No name-only, first-block, congener or external natural-identity substitution is made. False canonical comparisons and an empty direct atom map remain explicit; normalized identifier agreement does not establish a unique fixed tautomer or natural identity.

### Stored forms and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-1ea8852cad.

Both saved forms have C69H120N20O21, net charge 0, 110 atoms and 110 bonds. Eight comparisons are true, while both canonical SMILES comparisons are false and the direct atom map is empty. The source SMILES has a 25-member amide macrocycle and an extended peptide portion. Eighteen distinct amide-bearing carbonyl carbons include a urea carbon with two nitrogen attachments, giving nineteen amide C-N motif pairs; a separate terminal carboxylic acid brings the total to nineteen carbonyl carbons. No ester or carbon-O-carbon bridge is present. The InChI-derived form has eighteen C(O)=N motifs and the retained acid carbonyl. Thirteen tetrahedral centers are specified in both forms, consistent with the stored true flag at this scope. Eighteen undefined imidic double bonds are representation-specific, not new biological stereo gaps. Neither the graph nor its normalized identifiers establish spatial lasso entrapment or natural identity.

### Separate producer, locus and cached naming evidence

provenance: supported. Targets: naturalproductmech:mibig-1ea8852cad.

MIBiG BGC0001548 version 4 retains Streptomyces albulus (NCBITaxon:1971), SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades, LWBU01000091.1:108186–111640, and ribosomal/RiPP classes. Active status, questionable quality and unknown entry completeness are distinct from these grades. The saved cache names 1971 S. noursei and lists S. albulus as a synonym; the historical 68570→1971 route is retained separately. Neither these labels nor the locus coordinates newly verifies taxonomy, rank, ancestry, producer identity or a complete RiPP pathway.

### Citation tier and retained history

evidence: supported. Targets: naturalproductmech:mibig-1ea8852cad.

PMID:28244986 has exact ENTRY scope in MIBiG and appears on producer and locus assertions. LOTUS supplies DOI:10.1038/NCHEMBIO.2319. Independence is not established from these identifier strings, and no original publication was newly accessed. Three seeding histories remain unchanged.

### Occurrence, assay and mechanism scope

evidence: supported. Targets: naturalproductmech:mibig-1ea8852cad.

The LOTUS row retains source taxon 68570 and its historical route to 1971, whose current owner label is S. albulus. Shared naming with the producer does not merge occurrence and production evidence. PubChem CID124080860 is a blank-AID no-data sentinel with activity, target and reference fields blank. The owner has no bioactivity, target or declared mechanism root. Empty BindingDB and other negative frames do not establish inactivity or global absence of evidence.

### Applicability of computed labels

consistency: unknown. Targets: naturalproductmech:mibig-1ea8852cad.

NPClassifier version npclassifier.gnps2.org@2026-09-07 predicts Amino acids and Peptides/Polyketides, Oligopeptides and Cyclic peptides/Depsipeptides/Lipopeptides, with is_glycoside=false. The stored graph supports an amide-rich cyclic peptide, but it has no ester motif and no separate fatty-acyl chain; applicability of the Depsipeptides and Lipopeptides predictions is therefore not established. The labels remain attributed model output, with no automatic source edit. Source RIBOSOMAL/RiPP, computational pathway labels and UNCLASSIFIED filing are distinct. A two-dimensional molecular graph alone does not establish lasso entrapment or a complete biosynthetic pathway.

### Review completion

completeness: supported. Targets: naturalproductmech:mibig-1ea8852cad.

The review covers the whole owner and 3 seeding histories, its accepted 42-input canonical intake, all nine assigned source frames with 4 positive row placements, relevant complete cached stanzas and both complete saved molecular forms. No declared graph, pathway, component or root molecular target is present, so no maintained-reader check applies. Five local native gates passed, while full QC and complete OAK authority coverage remain unavailable; primary publications and fresh authorities were not accessed. Completion is partial, and no owner, native status or history is changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2560-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/citrulassin-a.yaml; Whole current plaintext including complete curation_history | supports | Complete current selected owner and all 3 history events; no native record/status/history changes. |
| support-2560-capture | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete captured owner and every present root. Root presence and absence are retained exactly for this owner. |
| support-2560-grounding-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/9/owner_document/identifier; /records/9/owner_document/label; /records/9/owner_document/chemical_structure; /records/9/owner_document/source_concepts; /records/9/owner_document/xrefs; /records/9/owner_document/grounding_status; /records/9/owner_document/grounding_notes | supports | Exact retained identifier, full key, source structure and present source/grounding fields; no fresh natural identity validation. |
| support-2560-origin-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/9/owner_document/producer_organisms; /records/9/owner_document/biosynthetic_gene_clusters; /records/9/owner_document/producer_taxon_groups | supports | Complete producer and locus claims with separate evidence grades, methods, coordinates and source classes. |
| support-2560-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/9/owner_document | supports | Complete owner preserves exact occurrence, activity, target and mechanism root presence or absence; production context is distinct from pharmacological activity. |
| support-2560-classification-owner | /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json; /records/9/owner_document/np_pathway; /records/9/owner_document/np_classification; /records/9/owner_document/bgc_class; /records/9/owner_document/biosynthesis_origin | supports | Versioned model output, source BGC classes and UNCLASSIFIED filing remain separate assertions. |
| support-2560-direct-contexts | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-target-input-plan-003.proposed.json; /records/9/proposed_companion_paths; /records/9/direct_companion_predicates; /records/9/identity_comparison_paths; /records/9/additional_context_roles | context_only | Exact admitted owner-local context roles include three curation diagnostic inputs and two taxonomy-query inputs. These last-five owners have no direct companion or maintained-reader roles; input capture is distinct from positive evidence. |
| support-2560-intake | /private/tmp/npm-review-work/shared-next-batch256/intakes/2560-inspect-001.json; /targets; /source | supports | Actual canonical target, source inputs and maintained ownership are retained. |
| support-2560-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch256/root-intake-acceptance-001.json; /status; /intakes/9; /source_plan; /verification | supports | ROOT accepts this original canonical intake and its exact source-plan/input joins. |
| support-2560-intake-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-last-five-molecular-intake-reading-001.json; /reading; /records/4/target; /records/4/intake; /coverage | supports | Support personally read all five canonical target and ownership documents; 210 current input placements across 46 paths are preserved. |
| support-2560-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch256/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory; /verification | supports | ROOT accepts the original retained local inventory; this is not primary-paper verification. |
| support-2560-plan | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-target-input-plan-003.proposed.json; /records/9/proposed_input_paths; /records/9/proposed_input_count | supports | The accepted input map agrees exactly with this canonical intake. |
| support-2560-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch256/root-source-plan-acceptance-001.json; /status; /verification | supports | ROOT accepts the operative 426-placement, 51-path plan, including all-owner taxonomy-query inputs; original inventory scope remains separate. |
| support-2560-source-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-assigned-source-reading-001.json; /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows; /cautions; /reading_method | supports | Support read all five assigned contexts: 45 frames, 23 rows and 248 fields, with four historical taxon-merge rows separately recorded. BGC owns the other five contexts; retained database reading does not confer primary-literature verification. |
| support-2560-source-notes | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | context_only | Historical joint notes retain disjoint BGC 136/Support 23/Native 0 retained-row reading attribution and the original 410-placement, 50-path inventory. Their taxonomy-query supplement was pending at creation; later operative authority is cited separately. |
| support-2560-molecular-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-last-five-molecular-intake-reading-001.json; /reading; /coverage; /records/4; /representation_notes; /limits | supports | Support personally read all ten complete saved forms: 650 atom rows and 680 bond rows, complete stereo, motif and correspondence fields, and 210 assigned canonical input placements across 46 paths. No new molecular parse. |
| support-2560-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/2 | context_only | Complete relevant retained cache stanzas preserve identifiers, names and synonyms only. They contain no explicit rank or lineage fields and do not prove ancestry, strain equivalence, native production or fresh taxonomy. |
| support-2560-taxonomy-query-routes | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/source_taxa; /contexts/9/source_scope_inventory/forward_taxon_merge_matches; /contexts/9/source_scope_inventory/nonorganism_matches | context_only | Complete retained source taxon IDs and saved forward-merge/non-organism results; historical merge routes are distinct from current nomenclatural, rank or ancestry verification. |
| support-2560-raw-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-last-five-whole-owner-reading-001.json; /records; /totals; /reading; /limits | context_only | Support personally read these five whole current owners and all 13 history events; this receipt credits plaintext reading, not original literature or fresh external verification. |
| support-2560-required-gates | /private/tmp/npm-review-work/shared-next-batch256/root-current256-five-gates-acceptance-001.json; /status; /verification; /unavailable_required_gates | supports | ROOT accepts five local gate results; the required QC and OAK checks remain unavailable, so completion is partial. |
| support-2560-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-cached-taxonomy-reading-001.json; /scope; /complete_readings; /counts; /interpretation; /routes | context_only | Native complete cache and route interpretation remains attributed; owner-local retained stanzas carry only their exact saved fields. |
| support-2560-curation-scope | /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation; /assay_scope | context_only | The bounded implemented-table scan found no applicable exact replacement for these owners; unrelated lexical hits are not imported as owner evidence. |
| support-2560-chemistry | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json; /records/9/declared_structure; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope; /records/9/comparisons; /records/9/atom_correspondence | supports | Eight comparisons are true; canonical isomeric and nonisomeric SMILES comparisons are false, and the direct atom map is empty. Amide/imidic representation differences preserve normalized identifiers, formula and charge without fixed-graph or natural-identity proof. |
| support-2560-topology | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles; /records/9/inchi | supports | Complete saved atom/bond/ring/stereo/motif tables retain representation-specific counts and stereochemical assignments; no new parse or natural-state claim. |
| support-2560-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /verification; /scope | supports | ROOT accepts the single original stored-form diagnostic and its exact outputs. Three of these five canonical pairs differ despite normalized identifier, formula and charge agreement; complete molecular reading is separately attributed. |
| support-2560-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Exact original diagnostic command/source, terminal exit and stream pins; no retry or external request. |
| support-2560-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-original-001.stderr; Whole original stderr | supports | The original stderr contains four omitted-undefined-stereo warnings. They remain global and are not assigned to an owner or form. |
| support-2560-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2560-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2560-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2560-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2560-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Complete retained physical row 1859, all 25 fields: BGC0001548 version 4; Streptomyces albulus, producer SOURCE_ASSERTION, locus CLUSTER_UNSTATED; PMID:28244986 at ENTRY scope. Source structure, methods and classes remain exact. |
| support-2560-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 1859 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2560-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Complete retained physical row 3542, all 6 fields: Streptomyces albulus (NCBITaxon:68570), DOI:10.1038/NCHEMBIO.2319; occurrence is distinct from demonstrated production and independent-study corroboration. |
| support-2560-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 3542 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2560-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/npclassifier/matches/0 | supports | Complete retained physical row 1198, all 7 fields: npclassifier.gnps2.org@2026-09-07: Amino acids and Peptides&#124;Polyketides/Oligopeptides/Cyclic peptides&#124;Depsipeptides&#124;Lipopeptides; glycoside=false, model assertion only. |
| support-2560-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1198 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2560-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame has 1 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-source-pubchem_bioassay-0 | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/pubchem_bioassay/matches/0 | supports | Complete retained physical row 3380, all 11 fields: Blank-AID no-data sentinel; not a measured activity or inactive assay. |
| support-2560-physical-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 3380 | context_only | Every complete retained field joins the exact current physical rows; retained-source reading attribution remains disjoint. |
| support-2560-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| support-2560-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json; /contexts/9/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame has 0 positive placements; a zero is bounded to its exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-256/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-256/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-256/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-256/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-256/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only: original publications, fresh taxonomy and independent natural-identity verification were not accessed.
- Formula, normalized identifiers, canonical strings and substructure mappings retain their separate scopes; no full graph identity is inferred. Four global undefined-stereo warnings are preserved without owner attribution.
- Cached OBO IDs, names and synonyms do not provide freshly verified rank, lineage, ancestry or strain equivalence. Producer, locus and occurrence claims retain distinct evidence grades.
- Full QC, complete OAK authority coverage and primary-source cross-checking remain unavailable. No record, native status or history edit was made.
- Computed class applicability remains explicitly uncertain for labels not established by the stored topology; this is not an automatic source-error finding.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five whole owners and all 13 histories, ten complete saved molecular forms with 650 atom rows and 680 bond rows, and all assigned retained-source payloads: 45 frames, 23 rows and 248 fields. Four historical merge rows and 12 relevant complete cached stanzas remain separately scoped.
- Actual last-five canonical inputs comprise 210 placements across 46 paths. Original source inventory scope remains 410/50; the accepted taxonomy-query supplement and successful intakes establish operative 426/51 globally without adding positive source rows.
- No requests, source replays, molecular reparses or owner edits were performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T130742Z-citrulassin-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: citrulassin A'
started_at: '2026-11-05T12:18:03.364380Z'
finished_at: '2026-11-05T13:07:42.386476Z'
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
summary: 'citrulassin A: retained identity, source-specific grades, taxonomy and representation
  limits assessed; computed labels remain separately qualified.'
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
  - path: data/natural_products/unclassified/citrulassin-a.yaml
    sha256: 757950a666e87a20b0f9536e1252255dc02436e01388f4f4403b1f637993970f
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2560; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-1ea8852cad
targets:
- target_id: naturalproductmech:mibig-1ea8852cad
  path: data/natural_products/unclassified/citrulassin-a.yaml
  label: citrulassin A
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
    role: Exact retained selected/direct taxon decision; no fresh authority.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism query and negative-query diagnostic context for every
      selected owner. Input presence does not assert a non-organism classification
      or fresh taxonomy.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/bioassay_exclusions.py
    role: Maintained exclusion identity, source-row digest and attributed-rationale
      implementation context; no execution or new assay evidence.
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
  - naturalproductmech:mibig-1ea8852cad
  command: just validate-strict data/natural_products/unclassified/chaetocin.yaml
    data/natural_products/unclassified/chaetolivacine-a.yaml data/natural_products/unclassified/chaetolivacine-b.yaml
    data/natural_products/unclassified/chaetolivacine-c.yaml data/natural_products/unclassified/chevalone-e.yaml
    data/natural_products/unclassified/chondramide-a.yaml data/natural_products/unclassified/chrodrimanin-b.yaml
    data/natural_products/unclassified/cinnapeptin.yaml data/natural_products/unclassified/citreohybridonol.yaml
    data/natural_products/unclassified/citrulassin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-256/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-1ea8852cad
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-256/validate-all-001.tsv
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
  - naturalproductmech:mibig-1ea8852cad
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
  - naturalproductmech:mibig-1ea8852cad
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
  - naturalproductmech:mibig-1ea8852cad
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-256/review-queue-001.tsv
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
  - naturalproductmech:mibig-1ea8852cad
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2560-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/citrulassin-a.yaml
  locator: Whole current plaintext including complete curation_history
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Complete current selected owner and all 3 history events; no native record/status/history
    changes.
  snapshot_sha256: 757950a666e87a20b0f9536e1252255dc02436e01388f4f4403b1f637993970f
- evidence_id: support-2560-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Complete captured owner and every present root. Root presence and absence
    are retained exactly for this owner.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: support-2560-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/9/owner_document/identifier; /records/9/owner_document/label;
    /records/9/owner_document/chemical_structure; /records/9/owner_document/source_concepts;
    /records/9/owner_document/xrefs; /records/9/owner_document/grounding_status; /records/9/owner_document/grounding_notes
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Exact retained identifier, full key, source structure and present source/grounding
    fields; no fresh natural identity validation.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: support-2560-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/9/owner_document/producer_organisms; /records/9/owner_document/biosynthetic_gene_clusters;
    /records/9/owner_document/producer_taxon_groups
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Complete producer and locus claims with separate evidence grades, methods,
    coordinates and source classes.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: support-2560-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Complete owner preserves exact occurrence, activity, target and mechanism
    root presence or absence; production context is distinct from pharmacological
    activity.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: support-2560-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256/owner-capture-DATA-001.json
  locator: /records/9/owner_document/np_pathway; /records/9/owner_document/np_classification;
    /records/9/owner_document/bgc_class; /records/9/owner_document/biosynthesis_origin
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Versioned model output, source BGC classes and UNCLASSIFIED filing remain
    separate assertions.
  snapshot_sha256: bd0be284ec3c904300b1e2a021e226e364cc76dfa06dca0677788e8f363980c9
- evidence_id: support-2560-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-target-input-plan-003.proposed.json
  locator: /records/9/proposed_companion_paths; /records/9/direct_companion_predicates;
    /records/9/identity_comparison_paths; /records/9/additional_context_roles
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Exact admitted owner-local context roles include three curation diagnostic
    inputs and two taxonomy-query inputs. These last-five owners have no direct companion
    or maintained-reader roles; input capture is distinct from positive evidence.
  snapshot_sha256: c196eea90a6145f1e90684b4169ae2dbfa0e7ffcc94722af4ddc95fecb798b44
- evidence_id: support-2560-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/intakes/2560-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Actual canonical target, source inputs and maintained ownership are retained.
  snapshot_sha256: 6440bfb1f769497c94aff1981096a0620c81a736b9ce8f0a3b8375fc16a5c517
- evidence_id: support-2560-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-intake-acceptance-001.json
  locator: /status; /intakes/9; /source_plan; /verification
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: ROOT accepts this original canonical intake and its exact source-plan/input
    joins.
  snapshot_sha256: 1604fe3b3542aae03b17b7316b5d14b03ead1f6ab5d0eb05f3eb4154b1660d3b
- evidence_id: support-2560-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-last-five-molecular-intake-reading-001.json
  locator: /reading; /records/4/target; /records/4/intake; /coverage
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Support personally read all five canonical target and ownership documents;
    210 current input placements across 46 paths are preserved.
  snapshot_sha256: 647d17aa27b3634d6d7e14174df0145d0852dac519d13c33e1db05b3fd6e46b5
- evidence_id: support-2560-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory; /verification
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: ROOT accepts the original retained local inventory; this is not primary-paper
    verification.
  snapshot_sha256: b5998813909f43f1aca6f34f99775e6a33ed12c916795acf3a3dce76b1d0d879
- evidence_id: support-2560-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-target-input-plan-003.proposed.json
  locator: /records/9/proposed_input_paths; /records/9/proposed_input_count
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: The accepted input map agrees exactly with this canonical intake.
  snapshot_sha256: c196eea90a6145f1e90684b4169ae2dbfa0e7ffcc94722af4ddc95fecb798b44
- evidence_id: support-2560-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-source-plan-acceptance-001.json
  locator: /status; /verification
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: ROOT accepts the operative 426-placement, 51-path plan, including all-owner
    taxonomy-query inputs; original inventory scope remains separate.
  snapshot_sha256: ac7d6ad5a59b920608dd3f690213af2011c8f81333acb1292dc24e49b9012b13
- evidence_id: support-2560-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-assigned-source-reading-001.json
  locator: /contexts; /totals; /raw_reading; /whole_reading_original_chunks; /physical_rows;
    /cautions; /reading_method
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: 'Support read all five assigned contexts: 45 frames, 23 rows and 248 fields,
    with four historical taxon-merge rows separately recorded. BGC owns the other
    five contexts; retained database reading does not confer primary-literature verification.'
  snapshot_sha256: c68f7d60017a7247ad7b6af661f51d42f9b89269574bd5818d78473a94d1a6c2
- evidence_id: support-2560-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Historical joint notes retain disjoint BGC 136/Support 23/Native 0 retained-row
    reading attribution and the original 410-placement, 50-path inventory. Their taxonomy-query
    supplement was pending at creation; later operative authority is cited separately.
  snapshot_sha256: 1e1fb894d0fe150d27cd92b637788e782ad886fd0786882126672059c5528ca5
- evidence_id: support-2560-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-last-five-molecular-intake-reading-001.json
  locator: /reading; /coverage; /records/4; /representation_notes; /limits
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: 'Support personally read all ten complete saved forms: 650 atom rows and
    680 bond rows, complete stereo, motif and correspondence fields, and 210 assigned
    canonical input placements across 46 paths. No new molecular parse.'
  snapshot_sha256: 647d17aa27b3634d6d7e14174df0145d0852dac519d13c33e1db05b3fd6e46b5
- evidence_id: support-2560-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/2
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Complete relevant retained cache stanzas preserve identifiers, names and
    synonyms only. They contain no explicit rank or lineage fields and do not prove
    ancestry, strain equivalence, native production or fresh taxonomy.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: support-2560-taxonomy-query-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/source_taxa; /contexts/9/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/9/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Complete retained source taxon IDs and saved forward-merge/non-organism
    results; historical merge routes are distinct from current nomenclatural, rank
    or ancestry verification.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: support-2560-raw-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/support-prep/support-current256-last-five-whole-owner-reading-001.json
  locator: /records; /totals; /reading; /limits
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Support personally read these five whole current owners and all 13 history
    events; this receipt credits plaintext reading, not original literature or fresh
    external verification.
  snapshot_sha256: d02bf94c204088e0ccee0498ba5ec8ea44ad8ae0a1a6bf73d23e2ef872107de4
- evidence_id: support-2560-required-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/root-current256-five-gates-acceptance-001.json
  locator: /status; /verification; /unavailable_required_gates
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: ROOT accepts five local gate results; the required QC and OAK checks remain
    unavailable, so completion is partial.
  snapshot_sha256: 319f0cd4fa76e6ca46dc31ba74652ba42b527e1ff8a5bb4b3e49c395a8af0bd7
- evidence_id: support-2560-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-cached-taxonomy-reading-001.json
  locator: /scope; /complete_readings; /counts; /interpretation; /routes
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Native complete cache and route interpretation remains attributed; owner-local
    retained stanzas carry only their exact saved fields.
  snapshot_sha256: a2cc30e7383daa4c5a8b571e68ea4eb106ef6fd05e880955e8fa25b958d23c43
- evidence_id: support-2560-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/native-prep/native-current256-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation; /assay_scope
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: The bounded implemented-table scan found no applicable exact replacement
    for these owners; unrelated lexical hits are not imported as owner evidence.
  snapshot_sha256: fafc422df141040e1168a039350961c7f34d19f470409f46ca719a442767589b
  search_scope: '{"selected_identifier": "naturalproductmech:mibig-1ea8852cad", "full_key":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "scope": "Eleven enumerated retained curation tables,
    nine implemented tables and exact predicates; ignored-file-independent inspection
    is bounded, not universal absence."}'
- evidence_id: support-2560-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/declared_structure; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope;
    /records/9/comparisons; /records/9/atom_correspondence
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Eight comparisons are true; canonical isomeric and nonisomeric SMILES comparisons
    are false, and the direct atom map is empty. Amide/imidic representation differences
    preserve normalized identifiers, formula and charge without fixed-graph or natural-identity
    proof.
  snapshot_sha256: 5ed67154a557428a9822cd74c0955c82fa6591381965e375d5f9b6a2df7c1c12
- evidence_id: support-2560-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles; /records/9/inchi
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif tables retain representation-specific
    counts and stereochemical assignments; no new parse or natural-state claim.
  snapshot_sha256: 5ed67154a557428a9822cd74c0955c82fa6591381965e375d5f9b6a2df7c1c12
- evidence_id: support-2560-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /verification; /scope
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: ROOT accepts the single original stored-form diagnostic and its exact outputs.
    Three of these five canonical pairs differ despite normalized identifier, formula
    and charge agreement; complete molecular reading is separately attributed.
  snapshot_sha256: ce8d094e6dccc0f7bf5c4e7317dbd4e80953c45036d1a8594af631904a831ed0
- evidence_id: support-2560-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Exact original diagnostic command/source, terminal exit and stream pins;
    no retry or external request.
  snapshot_sha256: 907e344f01ce09ca03c2340c5f78750840e75de01b571f7d3aa193c9e8423497
- evidence_id: support-2560-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch256/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: The original stderr contains four omitted-undefined-stereo warnings. They
    remain global and are not assigned to an owner or form.
  snapshot_sha256: 1eb7190b0fa9a4a670db0f828bd9324aa0df207c3b03cdda7586725f21bcb09e
- evidence_id: support-2560-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2560-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2560-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2560-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2560-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved mibig_compounds frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/mibig_compounds",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: 'Complete retained physical row 1859, all 25 fields: BGC0001548 version
    4; Streptomyces albulus, producer SOURCE_ASSERTION, locus CLUSTER_UNSTATED; PMID:28244986
    at ENTRY scope. Source structure, methods and classes remain exact.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: support-2560-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 1859
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2560-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved chebi_structures frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/chebi_structures",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved lotus_occurrences frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: 'Complete retained physical row 3542, all 6 fields: Streptomyces albulus
    (NCBITaxon:68570), DOI:10.1038/NCHEMBIO.2319; occurrence is distinct from demonstrated
    production and independent-study corroboration.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: support-2560-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 3542
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2560-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved cyanometdb_occurrences frame has 0 positive placements; a zero is
    bounded to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved npclassifier frame has 1 positive placements; a zero is bounded to
    its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/npclassifier",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: 'Complete retained physical row 1198, all 7 fields: npclassifier.gnps2.org@2026-09-07:
    Amino acids and Peptides|Polyketides/Oligopeptides/Cyclic peptides|Depsipeptides|Lipopeptides;
    glycoside=false, model assertion only.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: support-2560-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1198
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2560-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved pubchem_bioassay frame has 1 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-source-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/pubchem_bioassay/matches/0
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: 'Complete retained physical row 3380, all 11 fields: Blank-AID no-data
    sentinel; not a measured activity or inactive assay.'
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
- evidence_id: support-2560-physical-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 3380
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: context_only
  summary: Every complete retained field joins the exact current physical rows; retained-source
    reading attribution remains disjoint.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2560-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved bindingdb_targets frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved antibioticmech_inchikeys frame has 0 positive placements; a zero
    is bounded to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "JYSBHGIINWQTOH-JHTNTUONSA-N", "saved_frame": "/contexts/9/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: support-2560-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch256-tentative/bgc-prep/bgc-conditional256-source-inventory-DATA-001.json
  locator: /contexts/9/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T13:02:17.881814Z'
  support: supports
  summary: Saved chebi_origins frame has 0 positive placements; a zero is bounded
    to its exact retained predicate.
  snapshot_sha256: 9dcad0f5f1adb19508420f23d54218c8817e02d7d45ee9c31df43a733757a7b1
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/9/source_scope_inventory/joins/chebi_origins",
    "scope": "Saved local query only; no replay or universal absence inference."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:24:35.238925Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 726c23bfb5cf1d35406050521ce748bed31e1a54f2b059ace62708d240b0ec6f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:24:59.093466Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: abaf52c1a3174650333c90f46b94c837bc28699d7d7910c26ef650fa6173c043
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:25:17.770846Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:25:50.262912Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-256/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-256/native-current256-five-gates-execution-001.json
  accessed_at: '2026-11-05T12:26:01.626059Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 4eb94433e8671f2d0089684950fba7aef697542150201403ac54f25d798445e2
assessments:
- area: identity
  topic: Retained identity and grounding scope
  outcome: supported
  summary: The MINTED owner naturalproductmech:mibig-1ea8852cad retains the exact
    full key JYSBHGIINWQTOH-JHTNTUONSA-N, MIBiG source label citrulassin A and declared
    source structure. Both saved forms reproduce the declared Standard InChI and full
    key. The exact retained ChEBI structure frame is empty, which bounds the historical
    minted-identifier rationale without a fresh authority search. No name-only, first-block,
    congener or external natural-identity substitution is made. False canonical comparisons
    and an empty direct atom map remain explicit; normalized identifier agreement
    does not establish a unique fixed tautomer or natural identity.
  assessment_id: support-2560-identity
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-grounding-owner
  - support-2560-chemistry
  - support-2560-topology
  - support-2560-direct-contexts
  - support-2560-source-reading
  - support-2560-query-chebi_structures
  - support-2560-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: JYSBHGIINWQTOH-JHTNTUONSA-N; retained full key, not independently established
      natural identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2560-grounding-owner
    - support-2560-chemistry
    - support-2560-topology
    - support-2560-direct-contexts
    - support-2560-source-reading
    - support-2560-query-chebi_structures
    - support-2560-source-mibig_compounds-0
  - name: grounding_scope
    value: The MINTED owner naturalproductmech:mibig-1ea8852cad retains the exact
      full key JYSBHGIINWQTOH-JHTNTUONSA-N, MIBiG source label citrulassin A and declared
      source structure. Both saved forms reproduce the declared Standard InChI and
      full key. The exact retained ChEBI structure frame is empty, which bounds the
      historical minted-identifier rationale without a fresh authority search. No
      name-only, first-block, congener or external natural-identity substitution is
      made. False canonical comparisons and an empty direct atom map remain explicit;
      normalized identifier agreement does not establish a unique fixed tautomer or
      natural identity.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2560-grounding-owner
    - support-2560-chemistry
    - support-2560-topology
    - support-2560-direct-contexts
    - support-2560-source-reading
    - support-2560-query-chebi_structures
    - support-2560-source-mibig_compounds-0
- area: representation
  topic: Stored forms and stereochemical limits
  outcome: supported
  summary: Both saved forms have C69H120N20O21, net charge 0, 110 atoms and 110 bonds.
    Eight comparisons are true, while both canonical SMILES comparisons are false
    and the direct atom map is empty. The source SMILES has a 25-member amide macrocycle
    and an extended peptide portion. Eighteen distinct amide-bearing carbonyl carbons
    include a urea carbon with two nitrogen attachments, giving nineteen amide C-N
    motif pairs; a separate terminal carboxylic acid brings the total to nineteen
    carbonyl carbons. No ester or carbon-O-carbon bridge is present. The InChI-derived
    form has eighteen C(O)=N motifs and the retained acid carbonyl. Thirteen tetrahedral
    centers are specified in both forms, consistent with the stored true flag at this
    scope. Eighteen undefined imidic double bonds are representation-specific, not
    new biological stereo gaps. Neither the graph nor its normalized identifiers establish
    spatial lasso entrapment or natural identity.
  assessment_id: support-2560-representation
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-grounding-owner
  - support-2560-chemistry
  - support-2560-topology
  - support-2560-molecular-reading
  - support-2560-diagnostic-acceptance
  - support-2560-structure-schema
  - support-2560-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both saved forms have C69H120N20O21, net charge 0, 110 atoms and 110 bonds.
      Eight comparisons are true, while both canonical SMILES comparisons are false
      and the direct atom map is empty. The source SMILES has a 25-member amide macrocycle
      and an extended peptide portion. Eighteen distinct amide-bearing carbonyl carbons
      include a urea carbon with two nitrogen attachments, giving nineteen amide C-N
      motif pairs; a separate terminal carboxylic acid brings the total to nineteen
      carbonyl carbons. No ester or carbon-O-carbon bridge is present. The InChI-derived
      form has eighteen C(O)=N motifs and the retained acid carbonyl. Thirteen tetrahedral
      centers are specified in both forms, consistent with the stored true flag at
      this scope. Eighteen undefined imidic double bonds are representation-specific,
      not new biological stereo gaps. Neither the graph nor its normalized identifiers
      establish spatial lasso entrapment or natural identity.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2560-grounding-owner
    - support-2560-chemistry
    - support-2560-topology
    - support-2560-molecular-reading
    - support-2560-diagnostic-acceptance
    - support-2560-structure-schema
    - support-2560-stereo-method
  - name: representation_correspondence
    value: Both saved forms have C69H120N20O21, net charge 0, 110 atoms and 110 bonds.
      Eight comparisons are true, while both canonical SMILES comparisons are false
      and the direct atom map is empty. The source SMILES has a 25-member amide macrocycle
      and an extended peptide portion. Eighteen distinct amide-bearing carbonyl carbons
      include a urea carbon with two nitrogen attachments, giving nineteen amide C-N
      motif pairs; a separate terminal carboxylic acid brings the total to nineteen
      carbonyl carbons. No ester or carbon-O-carbon bridge is present. The InChI-derived
      form has eighteen C(O)=N motifs and the retained acid carbonyl. Thirteen tetrahedral
      centers are specified in both forms, consistent with the stored true flag at
      this scope. Eighteen undefined imidic double bonds are representation-specific,
      not new biological stereo gaps. Neither the graph nor its normalized identifiers
      establish spatial lasso entrapment or natural identity.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2560-grounding-owner
    - support-2560-chemistry
    - support-2560-topology
    - support-2560-molecular-reading
    - support-2560-diagnostic-acceptance
    - support-2560-structure-schema
    - support-2560-stereo-method
- area: provenance
  topic: Separate producer, locus and cached naming evidence
  outcome: supported
  summary: MIBiG BGC0001548 version 4 retains Streptomyces albulus (NCBITaxon:1971),
    SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades, LWBU01000091.1:108186–111640,
    and ribosomal/RiPP classes. Active status, questionable quality and unknown entry
    completeness are distinct from these grades. The saved cache names 1971 S. noursei
    and lists S. albulus as a synonym; the historical 68570→1971 route is retained
    separately. Neither these labels nor the locus coordinates newly verifies taxonomy,
    rank, ancestry, producer identity or a complete RiPP pathway.
  assessment_id: support-2560-provenance
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-origin-owner
  - support-2560-source-reading
  - support-2560-direct-contexts
  - support-2560-cached-taxonomy
  - support-2560-taxonomy-query-routes
  - support-2560-taxonomy-reading
  - support-2560-curation-scope
  - support-2560-source-mibig_compounds-0
  - support-2560-source-lotus_occurrences-0
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0001548 version 4 retains Streptomyces albulus (NCBITaxon:1971),
      SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades, LWBU01000091.1:108186–111640,
      and ribosomal/RiPP classes. Active status, questionable quality and unknown
      entry completeness are distinct from these grades. The saved cache names 1971
      S. noursei and lists S. albulus as a synonym; the historical 68570→1971 route
      is retained separately. Neither these labels nor the locus coordinates newly
      verifies taxonomy, rank, ancestry, producer identity or a complete RiPP pathway.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2560-origin-owner
    - support-2560-source-reading
    - support-2560-direct-contexts
    - support-2560-cached-taxonomy
    - support-2560-taxonomy-query-routes
    - support-2560-taxonomy-reading
    - support-2560-curation-scope
    - support-2560-source-mibig_compounds-0
    - support-2560-source-lotus_occurrences-0
  - name: producer_evidence
    value: MIBiG BGC0001548 version 4 retains Streptomyces albulus (NCBITaxon:1971),
      SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades, LWBU01000091.1:108186–111640,
      and ribosomal/RiPP classes. Active status, questionable quality and unknown
      entry completeness are distinct from these grades. The saved cache names 1971
      S. noursei and lists S. albulus as a synonym; the historical 68570→1971 route
      is retained separately. Neither these labels nor the locus coordinates newly
      verifies taxonomy, rank, ancestry, producer identity or a complete RiPP pathway.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2560-origin-owner
    - support-2560-source-reading
    - support-2560-direct-contexts
    - support-2560-cached-taxonomy
    - support-2560-taxonomy-query-routes
    - support-2560-taxonomy-reading
    - support-2560-curation-scope
    - support-2560-source-mibig_compounds-0
    - support-2560-source-lotus_occurrences-0
  - name: locus_evidence
    value: MIBiG BGC0001548 version 4 retains Streptomyces albulus (NCBITaxon:1971),
      SOURCE_ASSERTION producer and CLUSTER_UNSTATED locus grades, LWBU01000091.1:108186–111640,
      and ribosomal/RiPP classes. Active status, questionable quality and unknown
      entry completeness are distinct from these grades. The saved cache names 1971
      S. noursei and lists S. albulus as a synonym; the historical 68570→1971 route
      is retained separately. Neither these labels nor the locus coordinates newly
      verifies taxonomy, rank, ancestry, producer identity or a complete RiPP pathway.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2560-origin-owner
    - support-2560-source-reading
    - support-2560-direct-contexts
    - support-2560-cached-taxonomy
    - support-2560-taxonomy-query-routes
    - support-2560-taxonomy-reading
    - support-2560-curation-scope
    - support-2560-source-mibig_compounds-0
    - support-2560-source-lotus_occurrences-0
- area: evidence
  topic: Citation tier and retained history
  outcome: supported
  summary: PMID:28244986 has exact ENTRY scope in MIBiG and appears on producer and
    locus assertions. LOTUS supplies DOI:10.1038/NCHEMBIO.2319. Independence is not
    established from these identifier strings, and no original publication was newly
    accessed. Three seeding histories remain unchanged.
  assessment_id: support-2560-citations
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-owner
  - support-2560-raw-reading
  - support-2560-origin-owner
  - support-2560-occurrence-activity-owner
  - support-2560-source-reading
  - support-2560-direct-contexts
  - support-2560-source-mibig_compounds-0
  - support-2560-source-lotus_occurrences-0
  - support-2560-source-npclassifier-0
  - support-2560-source-pubchem_bioassay-0
  dimensions:
  - name: citation_scope
    value: PMID:28244986 has exact ENTRY scope in MIBiG and appears on producer and
      locus assertions. LOTUS supplies DOI:10.1038/NCHEMBIO.2319. Independence is
      not established from these identifier strings, and no original publication was
      newly accessed. Three seeding histories remain unchanged.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2560-owner
    - support-2560-raw-reading
    - support-2560-origin-owner
    - support-2560-occurrence-activity-owner
    - support-2560-source-reading
    - support-2560-direct-contexts
    - support-2560-source-mibig_compounds-0
    - support-2560-source-lotus_occurrences-0
    - support-2560-source-npclassifier-0
    - support-2560-source-pubchem_bioassay-0
- area: evidence
  topic: Occurrence, assay and mechanism scope
  outcome: supported
  summary: The LOTUS row retains source taxon 68570 and its historical route to 1971,
    whose current owner label is S. albulus. Shared naming with the producer does
    not merge occurrence and production evidence. PubChem CID124080860 is a blank-AID
    no-data sentinel with activity, target and reference fields blank. The owner has
    no bioactivity, target or declared mechanism root. Empty BindingDB and other negative
    frames do not establish inactivity or global absence of evidence.
  assessment_id: support-2560-occurrence
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-occurrence-activity-owner
  - support-2560-direct-contexts
  - support-2560-cached-taxonomy
  - support-2560-taxonomy-query-routes
  - support-2560-taxonomy-reading
  - support-2560-curation-scope
  - support-2560-source-reading
  - support-2560-query-lotus_occurrences
  - support-2560-query-chebi_origins
  - support-2560-query-cyanometdb_occurrences
  - support-2560-query-pubchem_bioassay
  - support-2560-query-bindingdb_targets
  - support-2560-query-antibioticmech_inchikeys
  - support-2560-source-lotus_occurrences-0
  - support-2560-source-pubchem_bioassay-0
  dimensions:
  - name: occurrence_scope
    value: The LOTUS row retains source taxon 68570 and its historical route to 1971,
      whose current owner label is S. albulus. Shared naming with the producer does
      not merge occurrence and production evidence. PubChem CID124080860 is a blank-AID
      no-data sentinel with activity, target and reference fields blank. The owner
      has no bioactivity, target or declared mechanism root. Empty BindingDB and other
      negative frames do not establish inactivity or global absence of evidence.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2560-occurrence-activity-owner
    - support-2560-direct-contexts
    - support-2560-cached-taxonomy
    - support-2560-taxonomy-query-routes
    - support-2560-taxonomy-reading
    - support-2560-curation-scope
    - support-2560-source-reading
    - support-2560-query-lotus_occurrences
    - support-2560-query-chebi_origins
    - support-2560-query-cyanometdb_occurrences
    - support-2560-query-pubchem_bioassay
    - support-2560-query-bindingdb_targets
    - support-2560-query-antibioticmech_inchikeys
    - support-2560-source-lotus_occurrences-0
    - support-2560-source-pubchem_bioassay-0
  - name: assay_target_scope
    value: The LOTUS row retains source taxon 68570 and its historical route to 1971,
      whose current owner label is S. albulus. Shared naming with the producer does
      not merge occurrence and production evidence. PubChem CID124080860 is a blank-AID
      no-data sentinel with activity, target and reference fields blank. The owner
      has no bioactivity, target or declared mechanism root. Empty BindingDB and other
      negative frames do not establish inactivity or global absence of evidence.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2560-occurrence-activity-owner
    - support-2560-direct-contexts
    - support-2560-cached-taxonomy
    - support-2560-taxonomy-query-routes
    - support-2560-taxonomy-reading
    - support-2560-curation-scope
    - support-2560-source-reading
    - support-2560-query-lotus_occurrences
    - support-2560-query-chebi_origins
    - support-2560-query-cyanometdb_occurrences
    - support-2560-query-pubchem_bioassay
    - support-2560-query-bindingdb_targets
    - support-2560-query-antibioticmech_inchikeys
    - support-2560-source-lotus_occurrences-0
    - support-2560-source-pubchem_bioassay-0
- area: consistency
  topic: Applicability of computed labels
  outcome: unknown
  summary: NPClassifier version npclassifier.gnps2.org@2026-09-07 predicts Amino acids
    and Peptides/Polyketides, Oligopeptides and Cyclic peptides/Depsipeptides/Lipopeptides,
    with is_glycoside=false. The stored graph supports an amide-rich cyclic peptide,
    but it has no ester motif and no separate fatty-acyl chain; applicability of the
    Depsipeptides and Lipopeptides predictions is therefore not established. The labels
    remain attributed model output, with no automatic source edit. Source RIBOSOMAL/RiPP,
    computational pathway labels and UNCLASSIFIED filing are distinct. A two-dimensional
    molecular graph alone does not establish lasso entrapment or a complete biosynthetic
    pathway.
  assessment_id: support-2560-classification
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-classification-owner
  - support-2560-chemistry
  - support-2560-topology
  - support-2560-classification-seeder
  - support-2560-source-reading
  - support-2560-source-mibig_compounds-0
  - support-2560-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: NPClassifier version npclassifier.gnps2.org@2026-09-07 predicts Amino acids
      and Peptides/Polyketides, Oligopeptides and Cyclic peptides/Depsipeptides/Lipopeptides,
      with is_glycoside=false. The stored graph supports an amide-rich cyclic peptide,
      but it has no ester motif and no separate fatty-acyl chain; applicability of
      the Depsipeptides and Lipopeptides predictions is therefore not established.
      The labels remain attributed model output, with no automatic source edit. Source
      RIBOSOMAL/RiPP, computational pathway labels and UNCLASSIFIED filing are distinct.
      A two-dimensional molecular graph alone does not establish lasso entrapment
      or a complete biosynthetic pathway.
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2560-classification-owner
    - support-2560-chemistry
    - support-2560-topology
    - support-2560-classification-seeder
    - support-2560-source-reading
    - support-2560-source-mibig_compounds-0
    - support-2560-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: supported
  summary: The review covers the whole owner and 3 seeding histories, its accepted
    42-input canonical intake, all nine assigned source frames with 4 positive row
    placements, relevant complete cached stanzas and both complete saved molecular
    forms. No declared graph, pathway, component or root molecular target is present,
    so no maintained-reader check applies. Five local native gates passed, while full
    QC and complete OAK authority coverage remain unavailable; primary publications
    and fresh authorities were not accessed. Completion is partial, and no owner,
    native status or history is changed.
  assessment_id: support-2560-completion
  target_ids:
  - naturalproductmech:mibig-1ea8852cad
  evidence_ids:
  - support-2560-owner
  - support-2560-capture
  - support-2560-intake
  - support-2560-intake-acceptance
  - support-2560-intake-reading
  - support-2560-inventory-acceptance
  - support-2560-plan
  - support-2560-plan-acceptance
  - support-2560-source-reading
  - support-2560-source-notes
  - support-2560-molecular-reading
  - support-2560-diagnostic-acceptance
  - support-2560-diagnostic-execution
  - support-2560-diagnostic-stderr
  - support-2560-required-gates
  - support-2560-review-profile
  dimensions:
  - name: review_completion
    value: The review covers the whole owner and 3 seeding histories, its accepted
      42-input canonical intake, all nine assigned source frames with 4 positive row
      placements, relevant complete cached stanzas and both complete saved molecular
      forms. No declared graph, pathway, component or root molecular target is present,
      so no maintained-reader check applies. Five local native gates passed, while
      full QC and complete OAK authority coverage remain unavailable; primary publications
      and fresh authorities were not accessed. Completion is partial, and no owner,
      native status or history is changed.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2560-owner
    - support-2560-capture
    - support-2560-intake
    - support-2560-intake-acceptance
    - support-2560-intake-reading
    - support-2560-inventory-acceptance
    - support-2560-plan
    - support-2560-plan-acceptance
    - support-2560-source-reading
    - support-2560-source-notes
    - support-2560-molecular-reading
    - support-2560-diagnostic-acceptance
    - support-2560-diagnostic-execution
    - support-2560-diagnostic-stderr
    - support-2560-required-gates
    - support-2560-review-profile
findings: []
actions: []
limitations:
- 'Retained local evidence only: original publications, fresh taxonomy and independent
  natural-identity verification were not accessed.'
- Formula, normalized identifiers, canonical strings and substructure mappings retain
  their separate scopes; no full graph identity is inferred. Four global undefined-stereo
  warnings are preserved without owner attribution.
- Cached OBO IDs, names and synonyms do not provide freshly verified rank, lineage,
  ancestry or strain equivalence. Producer, locus and occurrence claims retain distinct
  evidence grades.
- Full QC, complete OAK authority coverage and primary-source cross-checking remain
  unavailable. No record, native status or history edit was made.
- Computed class applicability remains explicitly uncertain for labels not established
  by the stored topology; this is not an automatic source-error finding.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Support personally read five whole owners and all 13 histories, ten complete saved
  molecular forms with 650 atom rows and 680 bond rows, and all assigned retained-source
  payloads: 45 frames, 23 rows and 248 fields. Four historical merge rows and 12 relevant
  complete cached stanzas remain separately scoped.'
- Actual last-five canonical inputs comprise 210 placements across 46 paths. Original
  source inventory scope remains 410/50; the accepted taxonomy-query supplement and
  successful intakes establish operative 426/51 globally without adding positive source
  rows.
- No requests, source replays, molecular reparses or owner edits were performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-256
```
