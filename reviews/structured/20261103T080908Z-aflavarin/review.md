# Local evidence review: aflavarin

- Review: 20261103T080908Z-aflavarin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T07:43:36.026237Z
- Finished UTC: 2026-11-03T08:09:08.493418Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

aflavarin: qualified partial review preserving exact identity, source grades and bounded representation/activity claims.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2177; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-7f9f9bacb5 | data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml | generated | aflavarin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-7f9f9bacb5 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-7f9f9bacb5 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-7f9f9bacb5 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-7f9f9bacb5 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-7f9f9bacb5 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-7f9f9bacb5 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-7f9f9bacb5 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-7f9f9bacb5 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact identity and grounding scope

identity: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

The minted aflavarin owner retains PQHCPIZEGQBDDY-UHFFFAOYSA-N and C24H22O9. Its exact retained ChEBI frame is empty. Active BGC0001304 version 3 compound 1 and PubChem44584646 remain source assertions; entry quality is questionable and completeness unknown. No direct companion is admitted. Encoded identity is internally concordant, without proving an unencoded natural axial state.

### Paired representations and stereochemistry limits

representation: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

Both saved forms parse as neutral C24H22O9 (33 atoms/36 bonds), agree on all ten saved comparisons and retain a complete atom map with full_graph_identity_established:false. Both saved forms have no detected potential tetrahedral or double-bond stereoelements and literal stereo_complete:true. The coupled aromatic units have a connecting single bond (SMILES C4–C14; InChI C19–C20), but this saved diagnostic does not test stable atropisomerism or establish a natural axial assignment. The atom-centered flag must not be read as an exhaustive axial-stereochemistry certificate. Two original global warnings remain unassigned.

### Producer, occurrence and locus grades

provenance: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

Aspergillus flavus NRRL3357 (NCBITaxon:332952) remains a SOURCE_ASSERTION producer; BGC0001304 is CLUSTER_UNSTATED with no locus method stated. EQ963475.1 coordinates 1142161–1157254 are retained. Two species-level LOTUS Aspergillus flavus5059 assertions do not establish two producer experiments or transfer strain resolution.

### Claim-level citation support

evidence: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

DOI:10.1021/np50086a008 is explicitly MIBiG COMPOUND_BIOACTIVITY citation scope, not newly inspected locus evidence. LOTUS cites the same DOI in uppercase and DOI:10.1128/EC.00092-15; shared identifiers/case variants do not establish independent publications or new assay observations. No original article was inspected.

### Occurrence and assay boundaries

scope: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

Two retained LOTUS Aspergillus flavus5059 citation assertions; producer strain 332952 remains distinct. The owner has no bioactivities, molecular targets or bioactivity summary. Exact retained PubChem, BindingDB and AntibioticMech frames contain no rows or blank-AID sentinel. A MIBiG compound-bioactivity citation alone supplies no assay endpoint, potency or target in this record; no inactivity claim is made.

### Computed classification and topology applicability

other: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

NPClassifier reports Shikimates and Phenylpropanoids / Coumarins / Simple coumarins, is_glycoside=false (npclassifier.gnps2.org@2026-09-07). NPClassifier Simple coumarins is a model family label for a coupled coumarin-containing structure, not a claim that the molecule is a single simple ring or a verified biosynthetic route. PKS source class remains separate. The saved structure contains four six-membered rings in two coupled bicyclic units, connected by the C4–C14 single bond. Carbonyls C9=O10 and C27=O28, aromatic ring oxygens O11/O26, four methoxy oxygens O12/O24/O29/O31, and hydroxymethyl C22–O23 are explicit in the SMILES tables. Aromaticized cyclic esters are not detected by the narrow SINGLE-bond ester motif; no saturated C5O candidate sugar ring is present.

### Partial completion and maintained ownership

completeness: supported. Targets: naturalproductmech:mibig-7f9f9bacb5.

All seven core areas and twelve dimensions were assessed against the actual intake, complete raw/history, retained source rows/cache and both saved chemical forms. Five local commands passed; full QC/OAK and external verification remain unavailable. This owner declares no mechanism roots/components and needs no maintained reader. The pinned source assertions and local structure are positively supported within that scope; no concrete contradiction requiring a finding was established. SEEDED status/history and all source records remain unchanged.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2177-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml; Complete raw owner, lines 1-100. | supports | Whole selected raw owner and 2 complete history events personally read; exact bytes retained. |
| support-2177-capture | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/6/owner_document; /records/6/owner_pin; /records/6/read_started_at; /records/6/read_finished_at | supports | Actual captured complete owner, current raw pin and original access clocks. |
| support-2177-intake | /private/tmp/npm-review-work/shared-next-batch218/intakes/2177-inspect-001.json; /status; /source; /targets/0 | supports | Original inspection-only intake with 37 current admitted inputs and explicit maintained owner paths. |
| support-2177-source-plan | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/6; /source_placement_count; /unique_source_path_count | supports | Exact selected raw/history/source frames and input map match accepted inventory and actual intake. Whole cohort 392placements67 paths; no future scientific authority inferred. |
| support-2177-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json; /accepted; /plan; /inventory; /per_order_counts | supports | ROOT accepts the exact saved plan and joins all actual intake maps; no scientific verdict is conferred. |
| support-2177-history | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/complete_raw_history; /contexts/13/history_count | supports | All 2 complete history events retained unchanged. |
| support-2177-direct-contexts | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/6/proposed_companion_paths; /records/6/direct_companion_predicates; /records/6/declared_mechanism_roots_literal; /records/6/component_paths | supports | No direct companions, four mechanism roots or components are admitted for this selected owner; no maintained reader applies. |
| support-2177-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/mibig_compounds | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 1 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical TSV line 1537. | supports | Retained row only, row SHA256 1d45758f1d8fbf430fc537785370317f9ab81f62bfd4f6d186428878abfa5c4b: {"bgc_classes": "PKS", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name": "aflavarin", "database_ids": "pubchem:44584646", "entry_completeness": "unknown", "entry_quality": "questionable", "entry_status": "active", "entry_version": "3", "genome_accession": "EQ963475.1", "locus_evidence_methods": "", "locus_from": "1142161", "locus_to": "1157254", "mibig_accession": "BGC0001304", "primary_reference": "DOI:10.1021/np50086a008", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "COMPOUND_BIOACTIVITY", "smiles": "CC1=CC(=C(C2=C1C(=CC(=O)O2)OC)C3=C(C4=C(C=C(C=C4CO)OC)OC3=O)OC)OC", "standard_inchi": "InChI=1S/C24H22O9/c1-11-6-14(29-3)20(23-18(11)15(30-4)9-17(26)33-23)21-22(31-5)19-12(10-25)7-13(28-2)8-16(19)32-24(21)27/h6-9,25H,10H2,1-5H3", "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:332952", "taxon_label": "Aspergillus flavus NRRL3357"} |
| support-2177-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_structures | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/lotus_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 2 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 7097. | supports | Retained row only, row SHA256 79157a8f62db36dc002d9e412fa6b8b4b8947b90ed600f2425e10b9c5e35e4ce: {"organism_name": "Aspergillus flavus", "organism_wikidata": "http://www.wikidata.org/entity/Q137096", "reference_doi": "10.1021/NP50086A008", "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27269537", "taxon_id": "NCBITaxon:5059"} |
| support-2177-row-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical TSV line 7098. | supports | Retained row only, row SHA256 3925737a06a3d9291e13006c179e7208b582290d515928bc7cf35c654b9784dc: {"organism_name": "Aspergillus flavus", "organism_wikidata": "http://www.wikidata.org/entity/Q137096", "reference_doi": "10.1128/EC.00092-15", "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27269537", "taxon_id": "NCBITaxon:5059"} |
| support-2177-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/npclassifier | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 1 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical TSV line 1917. | supports | Retained row only, row SHA256 369551f750f53f283c72188862d4231707e135f14157a8ff7bdb2beda6bcd16e: {"class_results": "Simple coumarins", "is_glycoside": "false", "model_version": "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Shikimates and Phenylpropanoids", "smiles": "CC1=CC(=C(C2=C1C(=CC(=O)O2)OC)C3=C(C4=C(C=C(C=C4CO)OC)OC3=O)OC)OC", "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N", "superclass_results": "Coumarins"} |
| support-2177-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/pubchem_bioassay | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/bindingdb_targets | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N"; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_origins | supports | Saved predicate exact chebi_id from exact full-key structure rows; query []; 0 retained rows. Empty results describe only this pinned scope, not inactivity or literature absence. |
| support-2177-taxon-routes | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/source_taxa; /contexts/13/source_scope_inventory/forward_taxon_merge_matches; /contexts/13/source_scope_inventory/nonorganism_matches | supports | Exact source taxa NCBITaxon:332952, NCBITaxon:5059; no retained forward merge or nonorganism matches. Cached labels do not establish production or fresh taxonomic authority. |
| support-2177-taxon-332952 | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/48; /cached_taxonomy/input | supports | Whole cached stanza for NCBITaxon:332952 names Aspergillus flavus NRRL3357 at OBO line 83767. Source/historical labels and any synonyms remain scoped; no live taxonomy or production proof. |
| support-2177-taxon-5059 | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/input | supports | Whole cached stanza for NCBITaxon:5059 names Aspergillus flavus at OBO line 7866. Source/historical labels and any synonyms remain scoped; no live taxonomy or production proof. |
| support-2177-chemistry | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/smiles/computed; /records/6/inchi/computed; /records/6/comparisons; /records/6/atom_correspondence; /records/6/literal_InChI_layers | supports | Both saved forms parse as neutral C24H22O9 with 33 atoms/36 bonds; all ten comparisons true and complete chirality-aware atom map. full_graph_identity_established:false; no fresh parse or proof of natural identity. |
| support-2177-topology | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed; /records/6/inchi/computed | supports | The saved structure contains four six-membered rings in two coupled bicyclic units, connected by the C4–C14 single bond. Carbonyls C9=O10 and C27=O28, aromatic ring oxygens O11/O26, four methoxy oxygens O12/O24/O29/O31, and hydroxymethyl C22–O23 are explicit in the SMILES tables. Aromaticized cyclic esters are not detected by the narrow SINGLE-bond ester motif; no saturated C5O candidate sugar ring is present. |
| support-2177-stereo | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/6/declared_structure; /records/6/smiles/computed/potential_stereo; /records/6/inchi/computed/potential_stereo; /records/6/smiles/computed/stereo_counts; /records/6/inchi/computed/stereo_counts; /records/6/smiles/computed/atoms; /records/6/inchi/computed/atoms; /records/6/smiles/computed/bonds; /records/6/inchi/computed/bonds | supports | Both saved forms have no detected potential tetrahedral or double-bond stereoelements and literal stereo_complete:true. The coupled aromatic units have a connecting single bond (SMILES C4–C14; InChI C19–C20), but this saved diagnostic does not test stable atropisomerism or establish a natural axial assignment. No axial-stereochemistry conclusion is established by these saved tables. |
| support-2177-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165-172. | supports | Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters results; no independent axial/all-natural-stereo claim. |
| support-2177-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-execution-001.json; /exit_code; /target_invocations; /retries; /DATA; /stderr | supports | Original ROOT diagnostic exit0, one target invocation/no retries; exact DATA and stderr pins. |
| support-2177-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json; /accepted; /verification; /limits; /DATA | supports | ROOT accepts 20 parsed forms/all 100 comparisons true. Two original global stereo warnings remain unassigned; natural identity and complete stereochemistry are not established. |
| support-2177-warnings | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-stderr-001.log; Complete original stderr, lines 1-4. | supports | Two original global omitted-undefined-stereo warnings with blank separators; not assigned to any one owner. |
| support-2177-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json; /status; /input_placements; /unique_input_paths; /input_counts; /reader_orders | supports | ROOT accepts all 10 original inspection-only intakes 392placements67 paths with no selected readers. |
| support-2177-native-acceptance | /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json; /results; /unavailable_required_gates; /all_native_gates_passed; /selected_queue_rows | supports | Five actual local commands passed; strict selected 10/full 3116 zero errors and 3116 byte-identical reproduction. Only 14 selected queue rows and 12 group counts are read here; full QC/OAK unavailable and all_native_gates_passed:false. |
| support-2177-source-ownership | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 950-1005; lines 1252-1308; lines 1310-1381; lines 1438-1468. | supports | Maintained exact-key grounding, literal stereo-source carry, occurrence deduplication/cap, written ACTIVE assay summary and coarse same-key sibling summary derivation; generator read as text only. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-218/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-218/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-218/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-218/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- No external requests, original-paper reading or live ontology/taxonomy/accession/sibling verification. Imported identifiers and quotations retain their source scope.
- All ten saved comparisons agree, but full_graph_identity_established remains false. The two original global stereo warnings are unassigned; natural identity and unmeasured stereochemistry are not proved.
- Full QC/OAK remain unavailable. Local gate success and selected queue rows do not establish scientific completeness.
- Empty retained query frames apply only to the exact pinned key/query; no inactivity, literature absence or congener-transfer inference. Curation reading is limited to the admitted seven baseline tables; the eighth assay table was supplemental preparation only.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole selected raw/history and both complete saved molecular tables personally read. BGC owns collector/composer and other source partitions; Support owns this target's retained payloads and relevant cached stanzas.
- No source, status or history edits, additional molecular/YAML parses, maintained-reader/gate/assembly/canonical invocation or outbound activity.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T080908Z-aflavarin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: aflavarin'
started_at: '2026-11-03T07:43:36.026237Z'
finished_at: '2026-11-03T08:09:08.493418Z'
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
summary: 'aflavarin: qualified partial review preserving exact identity, source grades
  and bounded representation/activity claims.'
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml
    sha256: 5b0698aabb047b9660c92ea6cac054b5ba0c5b1592b606ff681faccfd5b9f2e6
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
  selection: Campaign path order 2177; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
targets:
- target_id: naturalproductmech:mibig-7f9f9bacb5
  path: data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml
  label: aflavarin
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
  - naturalproductmech:mibig-7f9f9bacb5
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/3-5-dibromo-p-anisic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/3-p-hydroxyphenyl-1-2-propanediol.yaml
    data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml data/natural_products/shikimates_and_phenylpropanoids/6-methylsalicylic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/8-methyldiaporthin.yaml
    data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml data/natural_products/shikimates_and_phenylpropanoids/ajudazol-a.yaml
    data/natural_products/shikimates_and_phenylpropanoids/alternariol.yaml data/natural_products/shikimates_and_phenylpropanoids/aspulvinone-e.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-7f9f9bacb5
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-218/validate-all-001.tsv
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
  - naturalproductmech:mibig-7f9f9bacb5
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
  - naturalproductmech:mibig-7f9f9bacb5
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
  - naturalproductmech:mibig-7f9f9bacb5
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-218/review-queue-001.tsv
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
  - naturalproductmech:mibig-7f9f9bacb5
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2177-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/aflavarin.yaml
  locator: Complete raw owner, lines 1-100.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole selected raw owner and 2 complete history events personally read;
    exact bytes retained.
  snapshot_sha256: 5b0698aabb047b9660c92ea6cac054b5ba0c5b1592b606ff681faccfd5b9f2e6
- evidence_id: support-2177-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/6/owner_document; /records/6/owner_pin; /records/6/read_started_at;
    /records/6/read_finished_at
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Actual captured complete owner, current raw pin and original access clocks.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: support-2177-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/intakes/2177-inspect-001.json
  locator: /status; /source; /targets/0
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Original inspection-only intake with 37 current admitted inputs and explicit
    maintained owner paths.
  snapshot_sha256: 0a6cda2fb0f3507e088479a664d00c2633a13315a0c0010aff9e90883b526991
- evidence_id: support-2177-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/6; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Exact selected raw/history/source frames and input map match accepted inventory
    and actual intake. Whole cohort 392placements67 paths; no future scientific authority
    inferred.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: support-2177-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json
  locator: /accepted; /plan; /inventory; /per_order_counts
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: ROOT accepts the exact saved plan and joins all actual intake maps; no
    scientific verdict is conferred.
  snapshot_sha256: 938383f6b986f11823252b0a936784870aac1edd32b51ca4eea8c01b059af7ed
- evidence_id: support-2177-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/complete_raw_history; /contexts/13/history_count
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: All 2 complete history events retained unchanged.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/6/proposed_companion_paths; /records/6/direct_companion_predicates;
    /records/6/declared_mechanism_roots_literal; /records/6/component_paths
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: No direct companions, four mechanism roots or components are admitted for
    this selected owner; no maintained reader applies.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: support-2177-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    1 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-row-mibig_compounds-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical TSV line 1537.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 1d45758f1d8fbf430fc537785370317f9ab81f62bfd4f6d186428878abfa5c4b:
    {"bgc_classes": "PKS", "bgc_subclasses": "Unknown", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "1", "compound_name":
    "aflavarin", "database_ids": "pubchem:44584646", "entry_completeness": "unknown",
    "entry_quality": "questionable", "entry_status": "active", "entry_version": "3",
    "genome_accession": "EQ963475.1", "locus_evidence_methods": "", "locus_from":
    "1142161", "locus_to": "1157254", "mibig_accession": "BGC0001304", "primary_reference":
    "DOI:10.1021/np50086a008", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "COMPOUND_BIOACTIVITY", "smiles": "CC1=CC(=C(C2=C1C(=CC(=O)O2)OC)C3=C(C4=C(C=C(C=C4CO)OC)OC3=O)OC)OC",
    "standard_inchi": "InChI=1S/C24H22O9/c1-11-6-14(29-3)20(23-18(11)15(30-4)9-17(26)33-23)21-22(31-5)19-12(10-25)7-13(28-2)8-16(19)32-24(21)27/h6-9,25H,10H2,1-5H3",
    "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:332952", "taxon_label": "Aspergillus flavus NRRL3357"}'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2177-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    2 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-row-lotus_occurrences-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 7097.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 79157a8f62db36dc002d9e412fa6b8b4b8947b90ed600f2425e10b9c5e35e4ce:
    {"organism_name": "Aspergillus flavus", "organism_wikidata": "http://www.wikidata.org/entity/Q137096",
    "reference_doi": "10.1021/NP50086A008", "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27269537", "taxon_id":
    "NCBITaxon:5059"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2177-row-lotus_occurrences-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical TSV line 7098.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 3925737a06a3d9291e13006c179e7208b582290d515928bc7cf35c654b9784dc:
    {"organism_name": "Aspergillus flavus", "organism_wikidata": "http://www.wikidata.org/entity/Q137096",
    "reference_doi": "10.1128/EC.00092-15", "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27269537", "taxon_id":
    "NCBITaxon:5059"}'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2177-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    1 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-row-npclassifier-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical TSV line 1917.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: 'Retained row only, row SHA256 369551f750f53f283c72188862d4231707e135f14157a8ff7bdb2beda6bcd16e:
    {"class_results": "Simple coumarins", "is_glycoside": "false", "model_version":
    "npclassifier.gnps2.org@2026-09-07", "pathway_results": "Shikimates and Phenylpropanoids",
    "smiles": "CC1=CC(=C(C2=C1C(=CC(=O)O2)OC)C3=C(C4=C(C=C(C=C4CO)OC)OC3=O)OC)OC",
    "standard_inchi_key": "PQHCPIZEGQBDDY-UHFFFAOYSA-N", "superclass_results": "Coumarins"}'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2177-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact complete standard_inchi_key equality; query "PQHCPIZEGQBDDY-UHFFFAOYSA-N";
    0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Saved predicate exact chebi_id from exact full-key structure rows; query
    []; 0 retained rows. Empty results describe only this pinned scope, not inactivity
    or literature absence.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/source_taxa; /contexts/13/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/13/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Exact source taxa NCBITaxon:332952, NCBITaxon:5059; no retained forward
    merge or nonorganism matches. Cached labels do not establish production or fresh
    taxonomic authority.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-taxon-332952
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/48; /cached_taxonomy/input
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole cached stanza for NCBITaxon:332952 names Aspergillus flavus NRRL3357
    at OBO line 83767. Source/historical labels and any synonyms remain scoped; no
    live taxonomy or production proof.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-taxon-5059
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/10; /cached_taxonomy/input
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Whole cached stanza for NCBITaxon:5059 names Aspergillus flavus at OBO
    line 7866. Source/historical labels and any synonyms remain scoped; no live taxonomy
    or production proof.
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: support-2177-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/smiles/computed; /records/6/inchi/computed;
    /records/6/comparisons; /records/6/atom_correspondence; /records/6/literal_InChI_layers
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Both saved forms parse as neutral C24H22O9 with 33 atoms/36 bonds; all
    ten comparisons true and complete chirality-aware atom map. full_graph_identity_established:false;
    no fresh parse or proof of natural identity.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: support-2177-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed; /records/6/inchi/computed
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: The saved structure contains four six-membered rings in two coupled bicyclic
    units, connected by the C4–C14 single bond. Carbonyls C9=O10 and C27=O28, aromatic
    ring oxygens O11/O26, four methoxy oxygens O12/O24/O29/O31, and hydroxymethyl
    C22–O23 are explicit in the SMILES tables. Aromaticized cyclic esters are not
    detected by the narrow SINGLE-bond ester motif; no saturated C5O candidate sugar
    ring is present.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: support-2177-stereo
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/declared_structure; /records/6/smiles/computed/potential_stereo;
    /records/6/inchi/computed/potential_stereo; /records/6/smiles/computed/stereo_counts;
    /records/6/inchi/computed/stereo_counts; /records/6/smiles/computed/atoms; /records/6/inchi/computed/atoms;
    /records/6/smiles/computed/bonds; /records/6/inchi/computed/bonds
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Both saved forms have no detected potential tetrahedral or double-bond
    stereoelements and literal stereo_complete:true. The coupled aromatic units have
    a connecting single bond (SMILES C4–C14; InChI C19–C20), but this saved diagnostic
    does not test stable atropisomerism or establish a natural axial assignment. No
    axial-stereochemistry conclusion is established by these saved tables.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: support-2177-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165-172.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Maintained stereo_complete derives from unassigned atom-centered FindMolChiralCenters
    results; no independent axial/all-natural-stereo claim.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2177-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /target_invocations; /retries; /DATA; /stderr
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Original ROOT diagnostic exit0, one target invocation/no retries; exact
    DATA and stderr pins.
  snapshot_sha256: 2ef21bfab2aa20e8c198737cd65814fabc3cf91a51eb09cb617abb548c80cc06
- evidence_id: support-2177-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json
  locator: /accepted; /verification; /limits; /DATA
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: ROOT accepts 20 parsed forms/all 100 comparisons true. Two original global
    stereo warnings remain unassigned; natural identity and complete stereochemistry
    are not established.
  snapshot_sha256: 0f1c218ef2948f88c16e3ae0c830644e13e2d397ea05a9e4604a715e8da98443
- evidence_id: support-2177-warnings
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-stderr-001.log
  locator: Complete original stderr, lines 1-4.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Two original global omitted-undefined-stereo warnings with blank separators;
    not assigned to any one owner.
  snapshot_sha256: 836c9e40af7d808b240d363bb89b8b73c826451b24292cbfa9509297a4b6c480
- evidence_id: support-2177-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json
  locator: /status; /input_placements; /unique_input_paths; /input_counts; /reader_orders
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: ROOT accepts all 10 original inspection-only intakes 392placements67 paths
    with no selected readers.
  snapshot_sha256: 4d19c500387ec2c243eb986a2e00c596a04a9fa2e4f1879d15165d0fcd2ac0cd
- evidence_id: support-2177-native-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json
  locator: /results; /unavailable_required_gates; /all_native_gates_passed; /selected_queue_rows
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Five actual local commands passed; strict selected 10/full 3116 zero errors
    and 3116 byte-identical reproduction. Only 14 selected queue rows and 12 group
    counts are read here; full QC/OAK unavailable and all_native_gates_passed:false.
  snapshot_sha256: 57138741c14dfd03efcb91097dad031f0dc2209cb36d90f08c3b8796ae6f17b5
- evidence_id: support-2177-source-ownership
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 950-1005; lines 1252-1308; lines 1310-1381; lines 1438-1468.
  accessed_at: '2026-11-03T07:56:30.757326Z'
  support: supports
  summary: Maintained exact-key grounding, literal stereo-source carry, occurrence
    deduplication/cap, written ACTIVE assay summary and coarse same-key sibling summary
    derivation; generator read as text only.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:45:15.668585Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 35b181876d50c61aae3d6d9f47dda6fb34ee6cde4034660f8fc4f331a26db38d
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:45:43.691892Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 9a21ff2483495ee3c3d0e1631a10c4dd5cf399ea7f3f5838778bf6c4104dd10d
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:46:05.559629Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:46:42.649455Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-218/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json
  accessed_at: '2026-11-03T07:46:55.530300Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cf9808fb82c82233d73dbf69f7483bb393c3341686b96881f6fc8137b53cdbaa
assessments:
- assessment_id: support-2177-A1
  area: identity
  topic: Exact identity and grounding scope
  outcome: supported
  summary: The minted aflavarin owner retains PQHCPIZEGQBDDY-UHFFFAOYSA-N and C24H22O9.
    Its exact retained ChEBI frame is empty. Active BGC0001304 version 3 compound
    1 and PubChem44584646 remain source assertions; entry quality is questionable
    and completeness unknown. No direct companion is admitted. Encoded identity is
    internally concordant, without proving an unencoded natural axial state.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-direct-contexts
  - support-2177-query-chebi_structures
  - support-2177-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: PQHCPIZEGQBDDY-UHFFFAOYSA-N
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-direct-contexts
    - support-2177-query-chebi_structures
    - support-2177-row-mibig_compounds-0
  - name: grounding_scope
    value: MINTED; no retained exact-key ChEBI hit
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-direct-contexts
    - support-2177-query-chebi_structures
    - support-2177-row-mibig_compounds-0
- assessment_id: support-2177-A2
  area: representation
  topic: Paired representations and stereochemistry limits
  outcome: supported
  summary: Both saved forms parse as neutral C24H22O9 (33 atoms/36 bonds), agree on
    all ten saved comparisons and retain a complete atom map with full_graph_identity_established:false.
    Both saved forms have no detected potential tetrahedral or double-bond stereoelements
    and literal stereo_complete:true. The coupled aromatic units have a connecting
    single bond (SMILES C4–C14; InChI C19–C20), but this saved diagnostic does not
    test stable atropisomerism or establish a natural axial assignment. The atom-centered
    flag must not be read as an exhaustive axial-stereochemistry certificate. Two
    original global warnings remain unassigned.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-chemistry
  - support-2177-stereo
  - support-2177-stereo-method
  - support-2177-diagnostic-execution
  - support-2177-diagnostic-acceptance
  - support-2177-warnings
  dimensions:
  - name: stereochemical_resolution
    value: Both saved forms have no detected potential tetrahedral or double-bond
      stereoelements and literal stereo_complete:true. The coupled aromatic units
      have a connecting single bond (SMILES C4–C14; InChI C19–C20), but this saved
      diagnostic does not test stable atropisomerism or establish a natural axial
      assignment. The atom-centered flag must not be read as an exhaustive axial-stereochemistry
      certificate.
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-chemistry
    - support-2177-stereo
    - support-2177-stereo-method
    - support-2177-diagnostic-execution
    - support-2177-diagnostic-acceptance
    - support-2177-warnings
  - name: representation_correspondence
    value: Ten comparisons true; complete chirality-aware map; full_graph_identity_established:false
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-chemistry
    - support-2177-stereo
    - support-2177-stereo-method
    - support-2177-diagnostic-execution
    - support-2177-diagnostic-acceptance
    - support-2177-warnings
- assessment_id: support-2177-A3
  area: provenance
  topic: Producer, occurrence and locus grades
  outcome: supported
  summary: Aspergillus flavus NRRL3357 (NCBITaxon:332952) remains a SOURCE_ASSERTION
    producer; BGC0001304 is CLUSTER_UNSTATED with no locus method stated. EQ963475.1
    coordinates 1142161–1157254 are retained. Two species-level LOTUS Aspergillus
    flavus5059 assertions do not establish two producer experiments or transfer strain
    resolution.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-row-mibig_compounds-0
  - support-2177-row-lotus_occurrences-0
  - support-2177-row-lotus_occurrences-1
  - support-2177-taxon-routes
  - support-2177-taxon-332952
  - support-2177-taxon-5059
  dimensions:
  - name: taxon_and_strain_scope
    value: NCBITaxon:332952; NCBITaxon:5059; source/cached labels only
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-row-mibig_compounds-0
    - support-2177-row-lotus_occurrences-0
    - support-2177-row-lotus_occurrences-1
    - support-2177-taxon-routes
    - support-2177-taxon-332952
    - support-2177-taxon-5059
  - name: producer_evidence_tier
    value: SOURCE_ASSERTION
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-row-mibig_compounds-0
    - support-2177-row-lotus_occurrences-0
    - support-2177-row-lotus_occurrences-1
    - support-2177-taxon-routes
    - support-2177-taxon-332952
    - support-2177-taxon-5059
  - name: locus_evidence_tier
    value: CLUSTER_UNSTATED; no locus method stated
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-row-mibig_compounds-0
    - support-2177-row-lotus_occurrences-0
    - support-2177-row-lotus_occurrences-1
    - support-2177-taxon-routes
    - support-2177-taxon-332952
    - support-2177-taxon-5059
- assessment_id: support-2177-A4
  area: evidence
  topic: Claim-level citation support
  outcome: supported
  summary: DOI:10.1021/np50086a008 is explicitly MIBiG COMPOUND_BIOACTIVITY citation
    scope, not newly inspected locus evidence. LOTUS cites the same DOI in uppercase
    and DOI:10.1128/EC.00092-15; shared identifiers/case variants do not establish
    independent publications or new assay observations. No original article was inspected.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-history
  - support-2177-row-mibig_compounds-0
  - support-2177-row-lotus_occurrences-0
  - support-2177-row-lotus_occurrences-1
  dimensions:
  - name: citation_scope
    value: MIBiG COMPOUND_BIOACTIVITY DOI10.1021/np50086a008; LOTUS same DOI and 10.1128/EC.00092-15
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-history
    - support-2177-row-mibig_compounds-0
    - support-2177-row-lotus_occurrences-0
    - support-2177-row-lotus_occurrences-1
- assessment_id: support-2177-A5
  area: scope
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: Two retained LOTUS Aspergillus flavus5059 citation assertions; producer
    strain 332952 remains distinct. The owner has no bioactivities, molecular targets
    or bioactivity summary. Exact retained PubChem, BindingDB and AntibioticMech frames
    contain no rows or blank-AID sentinel. A MIBiG compound-bioactivity citation alone
    supplies no assay endpoint, potency or target in this record; no inactivity claim
    is made.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-query-lotus_occurrences
  - support-2177-query-cyanometdb_occurrences
  - support-2177-query-pubchem_bioassay
  - support-2177-query-bindingdb_targets
  - support-2177-query-antibioticmech_inchikeys
  - support-2177-query-chebi_origins
  - support-2177-row-lotus_occurrences-0
  - support-2177-row-lotus_occurrences-1
  dimensions:
  - name: occurrence_scope
    value: Two retained LOTUS Aspergillus flavus5059 citation assertions; producer
      strain 332952 remains distinct.
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-query-lotus_occurrences
    - support-2177-query-cyanometdb_occurrences
    - support-2177-query-pubchem_bioassay
    - support-2177-query-bindingdb_targets
    - support-2177-query-antibioticmech_inchikeys
    - support-2177-query-chebi_origins
    - support-2177-row-lotus_occurrences-0
    - support-2177-row-lotus_occurrences-1
  - name: assay_scope
    value: No retained assay/target/sibling rows; compound citation is not a measured
      endpoint
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-query-lotus_occurrences
    - support-2177-query-cyanometdb_occurrences
    - support-2177-query-pubchem_bioassay
    - support-2177-query-bindingdb_targets
    - support-2177-query-antibioticmech_inchikeys
    - support-2177-query-chebi_origins
    - support-2177-row-lotus_occurrences-0
    - support-2177-row-lotus_occurrences-1
- assessment_id: support-2177-A6
  area: other
  topic: Computed classification and topology applicability
  outcome: supported
  summary: NPClassifier reports Shikimates and Phenylpropanoids / Coumarins / Simple
    coumarins, is_glycoside=false (npclassifier.gnps2.org@2026-09-07). NPClassifier
    Simple coumarins is a model family label for a coupled coumarin-containing structure,
    not a claim that the molecule is a single simple ring or a verified biosynthetic
    route. PKS source class remains separate. The saved structure contains four six-membered
    rings in two coupled bicyclic units, connected by the C4–C14 single bond. Carbonyls
    C9=O10 and C27=O28, aromatic ring oxygens O11/O26, four methoxy oxygens O12/O24/O29/O31,
    and hydroxymethyl C22–O23 are explicit in the SMILES tables. Aromaticized cyclic
    esters are not detected by the narrow SINGLE-bond ester motif; no saturated C5O
    candidate sugar ring is present.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-topology
  - support-2177-chemistry
  - support-2177-row-npclassifier-0
  - support-2177-row-mibig_compounds-0
  dimensions:
  - name: computed_classification
    value: Shikimates and Phenylpropanoids / Coumarins / Simple coumarins; glycoside=false;
      npclassifier.gnps2.org@2026-09-07
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-topology
    - support-2177-chemistry
    - support-2177-row-npclassifier-0
    - support-2177-row-mibig_compounds-0
- assessment_id: support-2177-A7
  area: completeness
  topic: Partial completion and maintained ownership
  outcome: supported
  summary: All seven core areas and twelve dimensions were assessed against the actual
    intake, complete raw/history, retained source rows/cache and both saved chemical
    forms. Five local commands passed; full QC/OAK and external verification remain
    unavailable. This owner declares no mechanism roots/components and needs no maintained
    reader. The pinned source assertions and local structure are positively supported
    within that scope; no concrete contradiction requiring a finding was established.
    SEEDED status/history and all source records remain unchanged.
  target_ids:
  - naturalproductmech:mibig-7f9f9bacb5
  evidence_ids:
  - support-2177-owner
  - support-2177-capture
  - support-2177-intake
  - support-2177-source-plan
  - support-2177-plan-acceptance
  - support-2177-history
  - support-2177-direct-contexts
  - support-2177-intake-acceptance
  - support-2177-native-acceptance
  - support-2177-diagnostic-acceptance
  - support-2177-source-ownership
  dimensions:
  - name: review_completion
    value: partial; QC/OAK/external unavailable; native source/status/history unchanged
    definition: Exact inspected scope; retained assertions, computed facts and fresh
      experimental verification remain distinct.
    evidence_ids:
    - support-2177-owner
    - support-2177-capture
    - support-2177-intake
    - support-2177-source-plan
    - support-2177-plan-acceptance
    - support-2177-history
    - support-2177-direct-contexts
    - support-2177-intake-acceptance
    - support-2177-native-acceptance
    - support-2177-diagnostic-acceptance
    - support-2177-source-ownership
findings: []
actions: []
limitations:
- No external requests, original-paper reading or live ontology/taxonomy/accession/sibling
  verification. Imported identifiers and quotations retain their source scope.
- All ten saved comparisons agree, but full_graph_identity_established remains false.
  The two original global stereo warnings are unassigned; natural identity and unmeasured
  stereochemistry are not proved.
- Full QC/OAK remain unavailable. Local gate success and selected queue rows do not
  establish scientific completeness.
- Empty retained query frames apply only to the exact pinned key/query; no inactivity,
  literature absence or congener-transfer inference. Curation reading is limited to
  the admitted seven baseline tables; the eighth assay table was supplemental preparation
  only.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole selected raw/history and both complete saved molecular tables personally read.
  BGC owns collector/composer and other source partitions; Support owns this target's
  retained payloads and relevant cached stanzas.
- No source, status or history edits, additional molecular/YAML parses, maintained-reader/gate/assembly/canonical
  invocation or outbound activity.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-218
```
