# Local evidence review: compound 7

- Review: 20261103T103427Z-compound-7
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T09:59:30.239577Z
- Finished UTC: 2026-11-03T10:34:27.876493Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

compound 7: qualified partial review of exact structure, retained evidence grades, source boundaries and saved computation.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2196; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-92c7bb9c67 | data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml | generated | compound 7 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-92c7bb9c67 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-92c7bb9c67 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-92c7bb9c67 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-92c7bb9c67 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-92c7bb9c67 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-92c7bb9c67 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-92c7bb9c67 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-92c7bb9c67 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact structure concept and grounding scope

identity: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

Compound 7 resolves to the single MIBiG-derived structure ITBNIRGMDWCANJ-UHFFFAOYSA-N, neutral C12H14O4, with source compound_index=8 within active BGC0002290 version 2. The label is the paper's compound number, and the existing OPEN needs-a-name discussion remains unresolved. The retained exact-key ChEBI query is empty, supporting the MINTED status only within this saved inventory. Eleven directly shared-BGC companions have distinct full keys. In particular, the generic CHEBI:64921 concept belongs to a different-key companion; its unresolved generic/exact grounding issue does not become a finding on this owner.

### Paired molecular representations and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

Both stored forms parse with equal standardized InChI, full key, formula, charge, canonical isomeric and nonisomeric strings, atom and bond counts. The saved chirality-aware mapping covers all 16 atoms, while full_graph_identity_established remains false. No potential atom or double-bond stereo is reported in either saved form. The source's stereo_complete true is compatible with this local calculation, but neither calculation nor the flag verifies natural identity, axial stereochemistry or an experimental stereochemical assignment.

### Producer, occurrence and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

The producer is Biscogniauxia sp. NCBITaxon:1896107 with SOURCE_ASSERTION, whereas the BGC0002290 link is CLUSTER_DEMONSTRATED from retained heterologous-expression evidence. Those grades answer different questions and are preserved. MT109335.1 coordinates 1–37984 describe the source locus. The cached taxon label and source organism agree at this saved scope; heterologous expression does not turn the native taxon claim into demonstrated production or identify an unreported host/strain.

### Citation placement and historical verification scope

evidence: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

PMID:32364293 is retained as an ENTRY-level DATABASE_ASSERTION in the MIBiG-derived producer and locus evidence. It is not a freshly inspected original experiment. No primary article or current identifier service was inspected for this review. The companions retain their own citation roles, including compound 15's distinct COMPOUND_BIOACTIVITY reference DOI:10.1016/j.phytol.2020.07.016. Shared BGC membership does not independently verify every compound's production, activity or structure, or resolve the paper-number name.

### Occurrence, assay and companion boundaries

scope: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

All nine retained owner source queries were inspected. There are no matching owner LOTUS, ChEBI-origin, PubChem assay, BindingDB or AntibioticMech rows in those exact saved query frames, and the captured owner has no occurrence or bioactivity root. This is bounded missing evidence, not proof of biological inactivity or absence from other sources. Companion species, activities, generic identities and open grounding discussions are contextual only. The eight-table scan found no matching exact cohort token; that statement is limited to the 142-token, 101-physical-line scan recorded in source notes.

### Computed classification and full-table topology limits

other: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

NPClassifier's pinned model reports Shikimates and Phenylpropanoids, Phenolic acids (C6-C1), Simple phenolic acids and is_glycoside false; the source cluster's OTHER class remains a separate axis. Saved atoms show a substituted phenyl ring, one phenolic OH, a terminal carboxylic acid and a side-chain ketone next to an isopropyl group. In the SMILES form these are phenol O6, carboxyl C10(=O12)–O11H and ketone C2=O14. No C5O candidate ring is reported. These observations support a bounded topology interpretation, not a biosynthetic pathway inferred from the filing label.

### Partial scientific completion and maintained ownership

completeness: supported. Targets: naturalproductmech:mibig-92c7bb9c67.

The complete owner and its two history events, all direct companion contexts, retained source frames and paired molecular tables were read. The structure is positively assessed at the stated saved-source scope, with the naming discussion and producer evidence limit retained. Five original local gates passed, but full QC, complete ontology authority coverage and external source verification remain unavailable. The review is partial; it does not promote SEEDED status, close a naming issue, or edit generated fields. Any future correction belongs in maintained inventories, implemented overlays, extractors or the seeder.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2196-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml; Complete raw owner, lines 1-83. | supports | Complete owner and all 2 history events personally read; exact current bytes preserved. |
| support-2196-capture | /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json; /records/5/owner_document; /records/5/owner_pin; /records/5/read_started_at; /records/5/read_finished_at | supports | Actual complete captured owner, source pin and original read clocks; component resolution is separate. |
| support-2196-intake | /private/tmp/npm-review-work/shared-next-batch220/intakes/2196-inspect-001.json; /status; /source; /targets/0 | supports | Original inspection-only intake, 48 current inputs, exact target and maintained ownership. |
| support-2196-intake-ready | /private/tmp/npm-review-work/shared-next-batch220/root-intake-ready-001.json; /status; /records/5; /source_placements; /unique_source_paths; /external_requests | supports | ROOT acceptance of the original ten intakes and exact 455/123 source maps. |
| support-2196-source-plan | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5 | supports | Complete owner source plan: raw/history, all nine query frames, positive payloads, route sets, direct companions and input paths. |
| support-2196-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-source-plan-acceptance-001.json; /status; /plan; /source_notes; /actual_intake_ready; /verified | supports | ROOT joins the earned source plan to the accepted inventory and actual intake maps. |
| support-2196-source-notes | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json; /reading; /cautions; /totals | supports | Complete-source-reading attribution and retained source cautions; no new primary verification is asserted. |
| support-2196-curation-scope | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json; /curation | supports | Completed 142-literal-token scan over eight explicitly opened tables including ignored files: 101 physical lines/93 data rows, zero matches within that exact scope. |
| support-2196-chemistry | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json; /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/smiles; /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence | supports | Complete saved paired molecular computations, literal source stereo flag, exact comparisons and atom-map limits. No additional molecule was parsed. |
| support-2196-topology | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json; /records/5/smiles/computed; /records/5/inchi/computed | supports | Both complete atom/bond/ring/stereo/motif tables personally read: 16 atoms and 16 bonds per form. Topology motifs are not natural-identity proof. |
| support-2196-chemistry-execution | /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /stdout; /stderr; /output; /external_requests | supports | Original twenty-form diagnostic exited 0 with empty original stderr; no new parse, retry or owner-specific warning assignment. |
| support-2196-chemistry-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-chemistry-acceptance-001.json; /status; /data; /execution; /records/5; /scope | supports | ROOT accepts the saved original diagnostic while preserving false comparisons and scientific limits. |
| support-2196-native-acceptance | /private/tmp/npm-review-work/shared-next-batch220/root-native-gates-acceptance-001.json; /status; /ledger; /outcomes; /reading | supports | Five original local gates passed; full QC and ontology consistency/OAK remain unavailable. Selected queue rows are diagnostic leads. |
| support-2196-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-172. | supports | Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters output; it is not universal geometric, axial or natural stereochemical completeness. |
| support-2196-source-ownership | /private/tmp/npm-review-work/shared-next-batch220/intakes/2196-inspect-001.json; /targets/0/owner_paths; /targets/0/ownership_note | supports | Generated fields belong to retained inventories/extractors/seeder; curated mechanism owner/components and their histories have separately stated validated-writer ownership. |
| support-2196-taxon-1896107 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /cached_taxonomy/whole_stanzas/56 | supports | Complete cached stanza for NCBITaxon:1896107; literal labels/synonyms, not fresh taxonomy authority. |
| support-2196-taxon-routes | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/source_taxa; /records/5/source_scope_inventory/forward_taxon_merge_matches; /records/5/source_scope_inventory/nonorganism_matches | supports | Exact saved taxon route sets; no forward merge/non-organism hit for this selected owner. |
| support-2196-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/mibig_compounds | supports | Complete retained mibig_compounds predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2196-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical lines 2778-2778; exact complete TSV record SHA256 38eda8cdb3809c4e14be14bc7f3db3eed3dfb3f1dc1fbf3d54cd92d49cf1ad80. | supports | Retained row fields: {"mibig_accession":"BGC0002290","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"compound 7","compound_index":"8","smiles":"CC(C(CC1=C(O)C=CC(C(O)=O)=C1)=O)C","standard_inchi":"InChI=1S/C12H14O4/c1-7(2)11(14)6-9-5-8(12(15)16)3-4-10(9)13/h3-5,7,13H,6H2,1-2H3,(H,15,16)","standard_inchi_key":"ITBNIRGMDWCANJ-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1896107","taxon_label":"Biscogniauxia sp.","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"MT109335.1","locus_from":"1","locus_to":"37984","locus_evidence_methods":"Heterologous expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:32364293","reference_basis":"ENTRY"} |
| support-2196-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/chebi_structures | supports | Complete retained chebi_structures predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained lotus_occurrences predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained cyanometdb_occurrences predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/npclassifier | supports | Complete retained npclassifier predicate/query and all 1 matches; empty results refer only to this frozen query. |
| support-2196-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical lines 1028-1028; exact complete TSV record SHA256 eb9a033edbb3bb74b18712c2002a4513b939f048c53aa6607a8664909e1a78f7. | supports | Retained row fields: {"standard_inchi_key":"ITBNIRGMDWCANJ-UHFFFAOYSA-N","smiles":"CC(C(CC1=C(O)C=CC(C(O)=O)=C1)=O)C","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Simple phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"} |
| support-2196-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained pubchem_bioassay predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained bindingdb_targets predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained antibioticmech_inchikeys predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json; /records/5/source_scope_inventory/joins/chebi_origins | supports | Complete retained chebi_origins predicate/query and all 0 matches; empty results refer only to this frozen query. |
| support-2196-companion-1 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/1/complete_raw_text; /contexts/1/complete_raw_history; /contexts/1/source_scope_inventory | supports | Complete direct companion 3,4-dihydroxy-5-polyprenylbenzoic acid (CHEBI:64921, NMAKQSXJWYBYRF-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-2 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/2/complete_raw_text; /contexts/2/complete_raw_history; /contexts/2/source_scope_inventory | supports | Complete direct companion 4-hydroxy-3-prenylbenzoic acid (naturalproductmech:mibig-b4ad51fa2f, LBSJJNAMGVDGCU-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-9 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/9/complete_raw_text; /contexts/9/complete_raw_history; /contexts/9/source_scope_inventory | supports | Complete direct companion compound 8 (naturalproductmech:mibig-007406ddf9, HHJKLMAAAQXSLU-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-19 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/19/complete_raw_text; /contexts/19/complete_raw_history; /contexts/19/source_scope_inventory | supports | Complete direct companion prenylhydroquinone (naturalproductmech:mibig-8029a6a4d2, RPIWRSVHAHNACM-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-20 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/20/complete_raw_text; /contexts/20/complete_raw_history; /contexts/20/source_scope_inventory | supports | Complete direct companion biscognienyne B (CHEBI:167050, UAAPCPSYCUMTPM-LVQVYYBASA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-21 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/21/complete_raw_text; /contexts/21/complete_raw_history; /contexts/21/source_scope_inventory | supports | Complete direct companion compound 11 (naturalproductmech:mibig-21c4af6890, XRWGLEWIDBKJHA-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-22 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/22/complete_raw_text; /contexts/22/complete_raw_history; /contexts/22/source_scope_inventory | supports | Complete direct companion compound 12 (naturalproductmech:mibig-5cc4b239f3, IAAUFTNAVRJTIR-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-23 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/23/complete_raw_text; /contexts/23/complete_raw_history; /contexts/23/source_scope_inventory | supports | Complete direct companion compound 15 (naturalproductmech:mibig-fb29c28c86, DYVDEFLXDOLVQF-HOTGVXAUSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-24 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/24/complete_raw_text; /contexts/24/complete_raw_history; /contexts/24/source_scope_inventory | supports | Complete direct companion compound 6 (naturalproductmech:mibig-c9721b757b, LMSXLLMHAAGBSJ-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-25 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/25/complete_raw_text; /contexts/25/complete_raw_history; /contexts/25/source_scope_inventory | supports | Complete direct companion eutypinic acid (naturalproductmech:mibig-a75acad16f, HFSFSKBQIGXUEY-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| support-2196-companion-26 | /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json; /contexts/26/complete_raw_text; /contexts/26/complete_raw_history; /contexts/26/source_scope_inventory | supports | Complete direct companion pestalodiol E (naturalproductmech:mibig-2b8aee01b5, XLJZQTJROGTDLX-UHFFFAOYSA-N), raw/history and exact retained source frames. Context only; no identity, producer, activity or stereochemical transfer. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-220/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-220/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-220/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-220/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Full QC and complete ontology authority coverage/OAK were unavailable; passing local gates do not establish scientific completeness.
- No external requests, primary-article retrieval or live taxonomy/identifier/protein queries were performed. These assessments use the original saved owner-form computations, with no additional molecular parses during fragment authoring.
- Source citations, database labels, model predictions and historical annotations retain their stated evidence types; no publication independence or natural-identity proof is inferred from matching keys.
- No source record, component or curation history was edited by this review. Canonical review persistence and campaign publication are separate ROOT-owned operations.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Raw/source/cache/curation and molecular reading attribution is preserved in the fragment metadata and source-scope notes.
- No finding in this bounded review closes an existing issue or proves absence of uncertainty outside the inspected scope.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T103427Z-compound-7
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: compound 7'
started_at: '2026-11-03T09:59:30.239577Z'
finished_at: '2026-11-03T10:34:27.876493Z'
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
summary: 'compound 7: qualified partial review of exact structure, retained evidence
  grades, source boundaries and saved computation.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/3-4-dihydroxy-5-polyprenylbenzoic-acid.yaml
    sha256: 81e523462ebb0540e1de3b9eb19f88bc87266f0c7a4dcabbacae3556ccbdb91d
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
    sha256: 7ea7276c7e9cd0e4510ea28aa8076911d173a70ec9b80bd3ae7803749a5b53de
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml
    sha256: 5b2493967d1774d28d023edd8500fbf16a14cfbe5139e0ff65abb0d471302e56
    role: target
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-8.yaml
    sha256: 996d80d8c8f8eb32b5ee5a074da9d5390601d56585fbacde28b84e3315a246c9
    role: context
  - path: data/natural_products/shikimates_and_phenylpropanoids/prenylhydroquinone.yaml
    sha256: 9e180def1be87dc17c2f604712ad8ce85162e4fb8ef3af415887e619dc1dd6ac
    role: context
  - path: data/natural_products/terpenoids/biscognienyne-b.yaml
    sha256: ed9704a4411299b7c325c3ed9017a2aeabe6cfcb5600f5a13d923adc8361e3df
    role: context
  - path: data/natural_products/terpenoids/compound-11.yaml
    sha256: c6b1144ed2ccd49b3eb15d81e70c396bee614094e11074ed50076687ec64a29a
    role: context
  - path: data/natural_products/terpenoids/compound-12.yaml
    sha256: 68523e625132f3a958ba5ad4f2bad5984bfbc7d33f8a0f73e46e9ec109b21fd9
    role: context
  - path: data/natural_products/terpenoids/compound-15.yaml
    sha256: 86ed50b1cb3aeb1170f1e40e4c1d365b90cf94937cb27d36376882cda4b327ce
    role: context
  - path: data/natural_products/terpenoids/compound-6.yaml
    sha256: 4db168bf9a510a55403f4087abc00f8eee30b59a886a13a49daa8322eaa3b5cd
    role: context
  - path: data/natural_products/terpenoids/eutypinic-acid.yaml
    sha256: a2fbde14564e24a58cdf68e5c5b12fca09bb50874a8708eaf2904e684cfc6158
    role: context
  - path: data/natural_products/terpenoids/pestalodiol-e.yaml
    sha256: 6ee7a6ba26b1c13ea95adc492d1e200f9aefc45e3f700b3c53608e5960fc4e0b
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
  selection: Campaign path order 2196; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-92c7bb9c67
targets:
- target_id: naturalproductmech:mibig-92c7bb9c67
  path: data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml
  label: compound 7
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
  - naturalproductmech:mibig-92c7bb9c67
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/chartreusin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/chlorflavonin.yaml data/natural_products/shikimates_and_phenylpropanoids/clorobiocin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/colletorin-d-acid.yaml data/natural_products/shikimates_and_phenylpropanoids/collinomycin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml data/natural_products/shikimates_and_phenylpropanoids/coumermycin-a1.yaml
    data/natural_products/shikimates_and_phenylpropanoids/dichlorodiaporthin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/e-n-2-hydroxy-5-oxocyclopent-1-en-1-yl-5-o-tolyl-pent-4-enamide.yaml
    data/natural_products/shikimates_and_phenylpropanoids/echoside-a.yaml --workers
    1 --out /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-92c7bb9c67
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-220/validate-all-001.tsv
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
  - naturalproductmech:mibig-92c7bb9c67
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
  - naturalproductmech:mibig-92c7bb9c67
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
  - naturalproductmech:mibig-92c7bb9c67
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-220/review-queue-001.tsv
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
  - naturalproductmech:mibig-92c7bb9c67
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2196-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml
  locator: Complete raw owner, lines 1-83.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete owner and all 2 history events personally read; exact current
    bytes preserved.
  snapshot_sha256: 5b2493967d1774d28d023edd8500fbf16a14cfbe5139e0ff65abb0d471302e56
- evidence_id: support-2196-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/owner-capture-DATA-001.json
  locator: /records/5/owner_document; /records/5/owner_pin; /records/5/read_started_at;
    /records/5/read_finished_at
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Actual complete captured owner, source pin and original read clocks; component
    resolution is separate.
  snapshot_sha256: 90236bcdb9064859a691606fd163f92576040ab44a954a6323cc0b39871e571d
- evidence_id: support-2196-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/intakes/2196-inspect-001.json
  locator: /status; /source; /targets/0
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Original inspection-only intake, 48 current inputs, exact target and maintained
    ownership.
  snapshot_sha256: 4728c643d7463daaff841003547cda0ef4793e6249eadff3450c4ff660b6bb36
- evidence_id: support-2196-intake-ready
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-intake-ready-001.json
  locator: /status; /records/5; /source_placements; /unique_source_paths; /external_requests
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT acceptance of the original ten intakes and exact 455/123 source maps.
  snapshot_sha256: 0d2b19cf4c0cd15f0c85c8325c71569238160f93ba1db1f2d0f347ca4b659b60
- evidence_id: support-2196-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Complete owner source plan: raw/history, all nine query frames, positive
    payloads, route sets, direct companions and input paths.'
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-source-plan-acceptance-001.json
  locator: /status; /plan; /source_notes; /actual_intake_ready; /verified
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT joins the earned source plan to the accepted inventory and actual
    intake maps.
  snapshot_sha256: 8a51c9303cf8dd7483b2fc282491f294f43ae3adc3a419819b31fe9531b98f6b
- evidence_id: support-2196-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json
  locator: /reading; /cautions; /totals
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete-source-reading attribution and retained source cautions; no new
    primary verification is asserted.
  snapshot_sha256: aabfc3a0d18af5bd7d41acb95f1f89848cfbd06a962b174ef64b76218295ec7d
- evidence_id: support-2196-curation-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-scope-notes-001.json
  locator: /curation
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Completed 142-literal-token scan over eight explicitly opened tables including
    ignored files: 101 physical lines/93 data rows, zero matches within that exact
    scope.'
  snapshot_sha256: aabfc3a0d18af5bd7d41acb95f1f89848cfbd06a962b174ef64b76218295ec7d
- evidence_id: support-2196-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/declared_structure; /records/5/literal_InChI_layers; /records/5/smiles;
    /records/5/inchi; /records/5/comparisons; /records/5/atom_correspondence
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete saved paired molecular computations, literal source stereo flag,
    exact comparisons and atom-map limits. No additional molecule was parsed.
  snapshot_sha256: 7bfd670e8944734f1da87a78ecd6d4cee7c6a8dd8bbb225b260809c176bb3de7
- evidence_id: support-2196-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-DATA-001.json
  locator: /records/5/smiles/computed; /records/5/inchi/computed
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Both complete atom/bond/ring/stereo/motif tables personally read: 16 atoms
    and 16 bonds per form. Topology motifs are not natural-identity proof.'
  snapshot_sha256: 7bfd670e8944734f1da87a78ecd6d4cee7c6a8dd8bbb225b260809c176bb3de7
- evidence_id: support-2196-chemistry-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /stdout; /stderr; /output;
    /external_requests
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Original twenty-form diagnostic exited 0 with empty original stderr; no
    new parse, retry or owner-specific warning assignment.
  snapshot_sha256: 84a2689e8e405cf60782b070279cad53dbf96aadc5499ce50c17bd97650dd6ca
- evidence_id: support-2196-chemistry-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-chemistry-acceptance-001.json
  locator: /status; /data; /execution; /records/5; /scope
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: ROOT accepts the saved original diagnostic while preserving false comparisons
    and scientific limits.
  snapshot_sha256: c7b9547299a849c14093f64f88df2ec128f3806a864554cb39d89a2236dae984
- evidence_id: support-2196-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch220/root-native-gates-acceptance-001.json
  locator: /status; /ledger; /outcomes; /reading
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Five original local gates passed; full QC and ontology consistency/OAK
    remain unavailable. Selected queue rows are diagnostic leads.
  snapshot_sha256: 8ec4e48edaf25db9df0c202f6b8595e07cc7118c8fd24193c839e9c875f2c5c7
- evidence_id: support-2196-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-172.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters
    output; it is not universal geometric, axial or natural stereochemical completeness.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2196-source-ownership
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220/intakes/2196-inspect-001.json
  locator: /targets/0/owner_paths; /targets/0/ownership_note
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Generated fields belong to retained inventories/extractors/seeder; curated
    mechanism owner/components and their histories have separately stated validated-writer
    ownership.
  snapshot_sha256: 4728c643d7463daaff841003547cda0ef4793e6249eadff3450c4ff660b6bb36
- evidence_id: support-2196-taxon-1896107
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /cached_taxonomy/whole_stanzas/56
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete cached stanza for NCBITaxon:1896107; literal labels/synonyms,
    not fresh taxonomy authority.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/source_taxa; /records/5/source_scope_inventory/forward_taxon_merge_matches;
    /records/5/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Exact saved taxon route sets; no forward merge/non-organism hit for this
    selected owner.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained mibig_compounds predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical lines 2778-2778; exact complete TSV record SHA256 38eda8cdb3809c4e14be14bc7f3db3eed3dfb3f1dc1fbf3d54cd92d49cf1ad80.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"mibig_accession":"BGC0002290","entry_version":"2","entry_status":"active","entry_quality":"questionable","entry_completeness":"unknown","compound_name":"compound
    7","compound_index":"8","smiles":"CC(C(CC1=C(O)C=CC(C(O)=O)=C1)=O)C","standard_inchi":"InChI=1S/C12H14O4/c1-7(2)11(14)6-9-5-8(12(15)16)3-4-10(9)13/h3-5,7,13H,6H2,1-2H3,(H,15,16)","standard_inchi_key":"ITBNIRGMDWCANJ-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"","taxon_id":"NCBITaxon:1896107","taxon_label":"Biscogniauxia
    sp.","bgc_classes":"other","bgc_subclasses":"other","genome_accession":"MT109335.1","locus_from":"1","locus_to":"37984","locus_evidence_methods":"Heterologous
    expression","producer_evidence_basis":"SOURCE_ASSERTION","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:32364293","reference_basis":"ENTRY"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2196-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained chebi_structures predicate/query and all 0 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained lotus_occurrences predicate/query and all 0 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained cyanometdb_occurrences predicate/query and all 0 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained npclassifier predicate/query and all 1 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical lines 1028-1028; exact complete TSV record SHA256 eb9a033edbb3bb74b18712c2002a4513b939f048c53aa6607a8664909e1a78f7.
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: 'Retained row fields: {"standard_inchi_key":"ITBNIRGMDWCANJ-UHFFFAOYSA-N","smiles":"CC(C(CC1=C(O)C=CC(C(O)=O)=C1)=O)C","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Simple
    phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2196-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained pubchem_bioassay predicate/query and all 0 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained bindingdb_targets predicate/query and all 0 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained antibioticmech_inchikeys predicate/query and all 0 matches;
    empty results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-target-input-plan-001.json
  locator: /records/5/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete retained chebi_origins predicate/query and all 0 matches; empty
    results refer only to this frozen query.
  snapshot_sha256: 0205469165fcaae0dc2f1de2912fcdc95d75319f33f0fd474495dd54d45b3e92
- evidence_id: support-2196-companion-1
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/1/complete_raw_text; /contexts/1/complete_raw_history; /contexts/1/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion 3,4-dihydroxy-5-polyprenylbenzoic acid (CHEBI:64921,
    NMAKQSXJWYBYRF-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-2
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/2/complete_raw_text; /contexts/2/complete_raw_history; /contexts/2/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion 4-hydroxy-3-prenylbenzoic acid (naturalproductmech:mibig-b4ad51fa2f,
    LBSJJNAMGVDGCU-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-9
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/9/complete_raw_text; /contexts/9/complete_raw_history; /contexts/9/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion compound 8 (naturalproductmech:mibig-007406ddf9,
    HHJKLMAAAQXSLU-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-19
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/19/complete_raw_text; /contexts/19/complete_raw_history; /contexts/19/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion prenylhydroquinone (naturalproductmech:mibig-8029a6a4d2,
    RPIWRSVHAHNACM-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-20
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/20/complete_raw_text; /contexts/20/complete_raw_history; /contexts/20/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion biscognienyne B (CHEBI:167050, UAAPCPSYCUMTPM-LVQVYYBASA-N),
    raw/history and exact retained source frames. Context only; no identity, producer,
    activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-21
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/21/complete_raw_text; /contexts/21/complete_raw_history; /contexts/21/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion compound 11 (naturalproductmech:mibig-21c4af6890,
    XRWGLEWIDBKJHA-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-22
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/22/complete_raw_text; /contexts/22/complete_raw_history; /contexts/22/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion compound 12 (naturalproductmech:mibig-5cc4b239f3,
    IAAUFTNAVRJTIR-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-23
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/23/complete_raw_text; /contexts/23/complete_raw_history; /contexts/23/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion compound 15 (naturalproductmech:mibig-fb29c28c86,
    DYVDEFLXDOLVQF-HOTGVXAUSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-24
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/24/complete_raw_text; /contexts/24/complete_raw_history; /contexts/24/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion compound 6 (naturalproductmech:mibig-c9721b757b,
    LMSXLLMHAAGBSJ-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-25
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/25/complete_raw_text; /contexts/25/complete_raw_history; /contexts/25/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion eutypinic acid (naturalproductmech:mibig-a75acad16f,
    HFSFSKBQIGXUEY-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: support-2196-companion-26
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch220-tentative/bgc-prep/bgc-conditional220-source-inventory-DATA-002.json
  locator: /contexts/26/complete_raw_text; /contexts/26/complete_raw_history; /contexts/26/source_scope_inventory
  accessed_at: '2026-11-03T10:23:18.864450Z'
  support: supports
  summary: Complete direct companion pestalodiol E (naturalproductmech:mibig-2b8aee01b5,
    XLJZQTJROGTDLX-UHFFFAOYSA-N), raw/history and exact retained source frames. Context
    only; no identity, producer, activity or stereochemical transfer.
  snapshot_sha256: d42de14f96cf9d3b71c6aceb591f64629fba0ffde36721db7d37af2a8b594658
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:05:35.934949Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 3eb7a41f227bc3766da4ddb5affcab339127e3eec377a38a928d989861e7bca3
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:00.493115Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: b0fee61c050e78f367a4ad7e88aa28c2e04159e5fc41cb9fdd8c3cc0c524bbf8
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:19.575968Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:06:54.142706Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-220/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-220/native-current220-five-gates-execution-001.json
  accessed_at: '2026-11-03T10:07:06.355777Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 6b8a6b8cb74ddc70b591fb67b612031f05b241b0a0c649cdb0317a6bdeabfb46
assessments:
- assessment_id: support-2196-A1
  area: identity
  topic: Exact structure concept and grounding scope
  outcome: supported
  summary: Compound 7 resolves to the single MIBiG-derived structure ITBNIRGMDWCANJ-UHFFFAOYSA-N,
    neutral C12H14O4, with source compound_index=8 within active BGC0002290 version
    2. The label is the paper's compound number, and the existing OPEN needs-a-name
    discussion remains unresolved. The retained exact-key ChEBI query is empty, supporting
    the MINTED status only within this saved inventory. Eleven directly shared-BGC
    companions have distinct full keys. In particular, the generic CHEBI:64921 concept
    belongs to a different-key companion; its unresolved generic/exact grounding issue
    does not become a finding on this owner.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-capture
  - support-2196-intake
  - support-2196-source-plan
  - support-2196-plan-acceptance
  - support-2196-chemistry
  - support-2196-query-mibig_compounds
  - support-2196-row-mibig_compounds-0
  - support-2196-query-chebi_structures
  - support-2196-companion-1
  - support-2196-companion-2
  - support-2196-companion-9
  - support-2196-companion-19
  - support-2196-companion-20
  - support-2196-companion-21
  - support-2196-companion-22
  - support-2196-companion-23
  - support-2196-companion-24
  - support-2196-companion-25
  - support-2196-companion-26
  dimensions:
  - name: standard_inchi_key
    value: ITBNIRGMDWCANJ-UHFFFAOYSA-N
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-capture
    - support-2196-intake
    - support-2196-source-plan
    - support-2196-plan-acceptance
    - support-2196-chemistry
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
    - support-2196-query-chebi_structures
    - support-2196-companion-1
    - support-2196-companion-2
    - support-2196-companion-9
    - support-2196-companion-19
    - support-2196-companion-20
    - support-2196-companion-21
    - support-2196-companion-22
    - support-2196-companion-23
    - support-2196-companion-24
    - support-2196-companion-25
    - support-2196-companion-26
  - name: grounding_scope
    value: MINTED; saved exact-key ChEBI query empty; paper-number name unresolved
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-capture
    - support-2196-intake
    - support-2196-source-plan
    - support-2196-plan-acceptance
    - support-2196-chemistry
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
    - support-2196-query-chebi_structures
    - support-2196-companion-1
    - support-2196-companion-2
    - support-2196-companion-9
    - support-2196-companion-19
    - support-2196-companion-20
    - support-2196-companion-21
    - support-2196-companion-22
    - support-2196-companion-23
    - support-2196-companion-24
    - support-2196-companion-25
    - support-2196-companion-26
- assessment_id: support-2196-A2
  area: representation
  topic: Paired molecular representations and stereochemical limits
  outcome: supported
  summary: Both stored forms parse with equal standardized InChI, full key, formula,
    charge, canonical isomeric and nonisomeric strings, atom and bond counts. The
    saved chirality-aware mapping covers all 16 atoms, while full_graph_identity_established
    remains false. No potential atom or double-bond stereo is reported in either saved
    form. The source's stereo_complete true is compatible with this local calculation,
    but neither calculation nor the flag verifies natural identity, axial stereochemistry
    or an experimental stereochemical assignment.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-chemistry
  - support-2196-topology
  - support-2196-stereo-method
  - support-2196-chemistry-execution
  - support-2196-chemistry-acceptance
  dimensions:
  - name: stereochemical_resolution
    value: No potential stereo in either saved form; literal flag true
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-chemistry
    - support-2196-topology
    - support-2196-stereo-method
    - support-2196-chemistry-execution
    - support-2196-chemistry-acceptance
  - name: representation_correspondence
    value: All comparisons true;16-atom map;full graph/natural identity unproved
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-chemistry
    - support-2196-topology
    - support-2196-stereo-method
    - support-2196-chemistry-execution
    - support-2196-chemistry-acceptance
- assessment_id: support-2196-A3
  area: provenance
  topic: Producer, occurrence and locus evidence grades
  outcome: supported
  summary: The producer is Biscogniauxia sp. NCBITaxon:1896107 with SOURCE_ASSERTION,
    whereas the BGC0002290 link is CLUSTER_DEMONSTRATED from retained heterologous-expression
    evidence. Those grades answer different questions and are preserved. MT109335.1
    coordinates 1–37984 describe the source locus. The cached taxon label and source
    organism agree at this saved scope; heterologous expression does not turn the
    native taxon claim into demonstrated production or identify an unreported host/strain.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-capture
  - support-2196-taxon-routes
  - support-2196-query-mibig_compounds
  - support-2196-row-mibig_compounds-0
  - support-2196-query-lotus_occurrences
  - support-2196-query-chebi_origins
  - support-2196-taxon-1896107
  dimensions:
  - name: taxon_and_strain_scope
    value: Biscogniauxia sp.1896107
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-capture
    - support-2196-taxon-routes
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
    - support-2196-query-lotus_occurrences
    - support-2196-query-chebi_origins
    - support-2196-taxon-1896107
  - name: producer_evidence_tier
    value: SOURCE_ASSERTION, MIBiG2290v2
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-capture
    - support-2196-taxon-routes
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
    - support-2196-query-lotus_occurrences
    - support-2196-query-chebi_origins
    - support-2196-taxon-1896107
  - name: locus_evidence_tier
    value: CLUSTER_DEMONSTRATED;heterologous expression
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-capture
    - support-2196-taxon-routes
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
    - support-2196-query-lotus_occurrences
    - support-2196-query-chebi_origins
    - support-2196-taxon-1896107
- assessment_id: support-2196-A4
  area: evidence
  topic: Citation placement and historical verification scope
  outcome: supported
  summary: PMID:32364293 is retained as an ENTRY-level DATABASE_ASSERTION in the MIBiG-derived
    producer and locus evidence. It is not a freshly inspected original experiment.
    No primary article or current identifier service was inspected for this review.
    The companions retain their own citation roles, including compound 15's distinct
    COMPOUND_BIOACTIVITY reference DOI:10.1016/j.phytol.2020.07.016. Shared BGC membership
    does not independently verify every compound's production, activity or structure,
    or resolve the paper-number name.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-capture
  - support-2196-taxon-routes
  - support-2196-query-mibig_compounds
  - support-2196-row-mibig_compounds-0
  - support-2196-query-lotus_occurrences
  - support-2196-query-chebi_origins
  - support-2196-taxon-1896107
  - support-2196-source-notes
  - support-2196-companion-23
  dimensions:
  - name: citation_scope
    value: PMID32364293 ENTRY database assertion
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-capture
    - support-2196-taxon-routes
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
    - support-2196-query-lotus_occurrences
    - support-2196-query-chebi_origins
    - support-2196-taxon-1896107
    - support-2196-source-notes
    - support-2196-companion-23
- assessment_id: support-2196-A5
  area: scope
  topic: Occurrence, assay and companion boundaries
  outcome: supported
  summary: All nine retained owner source queries were inspected. There are no matching
    owner LOTUS, ChEBI-origin, PubChem assay, BindingDB or AntibioticMech rows in
    those exact saved query frames, and the captured owner has no occurrence or bioactivity
    root. This is bounded missing evidence, not proof of biological inactivity or
    absence from other sources. Companion species, activities, generic identities
    and open grounding discussions are contextual only. The eight-table scan found
    no matching exact cohort token; that statement is limited to the 142-token, 101-physical-line
    scan recorded in source notes.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-curation-scope
  - support-2196-query-lotus_occurrences
  - support-2196-query-pubchem_bioassay
  - support-2196-query-bindingdb_targets
  - support-2196-query-antibioticmech_inchikeys
  - support-2196-query-chebi_structures
  - support-2196-companion-1
  - support-2196-companion-2
  - support-2196-companion-9
  - support-2196-companion-19
  - support-2196-companion-20
  - support-2196-companion-21
  - support-2196-companion-22
  - support-2196-companion-23
  - support-2196-companion-24
  - support-2196-companion-25
  - support-2196-companion-26
  - support-2196-query-chebi_origins
  dimensions:
  - name: occurrence_scope
    value: No owner occurrence rows within saved joins
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-curation-scope
    - support-2196-query-lotus_occurrences
    - support-2196-query-pubchem_bioassay
    - support-2196-query-bindingdb_targets
    - support-2196-query-antibioticmech_inchikeys
    - support-2196-query-chebi_structures
    - support-2196-companion-1
    - support-2196-companion-2
    - support-2196-companion-9
    - support-2196-companion-19
    - support-2196-companion-20
    - support-2196-companion-21
    - support-2196-companion-22
    - support-2196-companion-23
    - support-2196-companion-24
    - support-2196-companion-25
    - support-2196-companion-26
    - support-2196-query-chebi_origins
  - name: assay_scope
    value: No owner assay/target rows;not inactivity
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-curation-scope
    - support-2196-query-lotus_occurrences
    - support-2196-query-pubchem_bioassay
    - support-2196-query-bindingdb_targets
    - support-2196-query-antibioticmech_inchikeys
    - support-2196-query-chebi_structures
    - support-2196-companion-1
    - support-2196-companion-2
    - support-2196-companion-9
    - support-2196-companion-19
    - support-2196-companion-20
    - support-2196-companion-21
    - support-2196-companion-22
    - support-2196-companion-23
    - support-2196-companion-24
    - support-2196-companion-25
    - support-2196-companion-26
- assessment_id: support-2196-A6
  area: other
  topic: Computed classification and full-table topology limits
  outcome: supported
  summary: NPClassifier's pinned model reports Shikimates and Phenylpropanoids, Phenolic
    acids (C6-C1), Simple phenolic acids and is_glycoside false; the source cluster's
    OTHER class remains a separate axis. Saved atoms show a substituted phenyl ring,
    one phenolic OH, a terminal carboxylic acid and a side-chain ketone next to an
    isopropyl group. In the SMILES form these are phenol O6, carboxyl C10(=O12)–O11H
    and ketone C2=O14. No C5O candidate ring is reported. These observations support
    a bounded topology interpretation, not a biosynthetic pathway inferred from the
    filing label.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-topology
  - support-2196-chemistry
  - support-2196-query-npclassifier
  - support-2196-row-npclassifier-0
  - support-2196-query-mibig_compounds
  - support-2196-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: Pinned Simple phenolic acids;model filing distinct from OTHER BGC
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-topology
    - support-2196-chemistry
    - support-2196-query-npclassifier
    - support-2196-row-npclassifier-0
    - support-2196-query-mibig_compounds
    - support-2196-row-mibig_compounds-0
- assessment_id: support-2196-A7
  area: completeness
  topic: Partial scientific completion and maintained ownership
  outcome: supported
  summary: The complete owner and its two history events, all direct companion contexts,
    retained source frames and paired molecular tables were read. The structure is
    positively assessed at the stated saved-source scope, with the naming discussion
    and producer evidence limit retained. Five original local gates passed, but full
    QC, complete ontology authority coverage and external source verification remain
    unavailable. The review is partial; it does not promote SEEDED status, close a
    naming issue, or edit generated fields. Any future correction belongs in maintained
    inventories, implemented overlays, extractors or the seeder.
  target_ids:
  - naturalproductmech:mibig-92c7bb9c67
  evidence_ids:
  - support-2196-owner
  - support-2196-intake
  - support-2196-intake-ready
  - support-2196-native-acceptance
  - support-2196-source-ownership
  - support-2196-source-notes
  - support-2196-companion-1
  - support-2196-companion-2
  - support-2196-companion-9
  - support-2196-companion-19
  - support-2196-companion-20
  - support-2196-companion-21
  - support-2196-companion-22
  - support-2196-companion-23
  - support-2196-companion-24
  - support-2196-companion-25
  - support-2196-companion-26
  dimensions:
  - name: review_completion
    value: partial;QC/OAK/external verification unavailable
    definition: Exact inspected scope; retained source assertions, saved computation
      and fresh experimental verification remain distinct.
    evidence_ids:
    - support-2196-owner
    - support-2196-intake
    - support-2196-intake-ready
    - support-2196-native-acceptance
    - support-2196-source-ownership
    - support-2196-source-notes
    - support-2196-companion-1
    - support-2196-companion-2
    - support-2196-companion-9
    - support-2196-companion-19
    - support-2196-companion-20
    - support-2196-companion-21
    - support-2196-companion-22
    - support-2196-companion-23
    - support-2196-companion-24
    - support-2196-companion-25
    - support-2196-companion-26
findings: []
actions: []
limitations:
- Full QC and complete ontology authority coverage/OAK were unavailable; passing local
  gates do not establish scientific completeness.
- No external requests, primary-article retrieval or live taxonomy/identifier/protein
  queries were performed. These assessments use the original saved owner-form computations,
  with no additional molecular parses during fragment authoring.
- Source citations, database labels, model predictions and historical annotations
  retain their stated evidence types; no publication independence or natural-identity
  proof is inferred from matching keys.
- No source record, component or curation history was edited by this review. Canonical
  review persistence and campaign publication are separate ROOT-owned operations.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Raw/source/cache/curation and molecular reading attribution is preserved in the
  fragment metadata and source-scope notes.
- No finding in this bounded review closes an existing issue or proves absence of
  uncertainty outside the inspected scope.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-220
```
