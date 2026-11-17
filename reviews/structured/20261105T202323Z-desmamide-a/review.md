# Local evidence review: desmamide A

- Review: 20261105T202323Z-desmamide-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T19:33:20.891242Z
- Finished UTC: 2026-11-05T20:23:23.422835Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Desmamide A retains a reproducible MIBiG mapping and source-level producer and locus claims. Its original saved graph supports a cyclic lipo-depsipeptide-compatible topology with an aryl-linked C5O ring, without assigning a named sugar. Three tetrahedral centers remain unspecified, and the reconstructed imidic form does not establish full graph or natural identity.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2599; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-7bc3610bc0 | data/natural_products/unclassified/desmamide-a.yaml | generated | desmamide A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-7bc3610bc0 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-7bc3610bc0 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-7bc3610bc0 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-7bc3610bc0 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-7bc3610bc0 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-7bc3610bc0 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-7bc3610bc0 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-7bc3610bc0 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-7bc3610bc0.

The minted identifier, label, BGC0002625 compound 1 and full key SGSWMZBFZBNBSH-ONBVFTLRSA-N agree in the complete owner and exact retained MIBiG row. No exact-key ChEBI structure row was returned. Both saved forms regenerate the declared key, supporting reproducible stored mapping without proving natural identity or allowing congener substitution.

### Stored forms and stereochemistry

representation: unknown. Targets: naturalproductmech:mibig-7bc3610bc0.

Both forms give C66H105N11O21, charge 0, 98 atoms and 102 bonds and SGSWMZBFZBNBSH-ONBVFTLRSA-N. The original graph has 14 specified tetrahedral centers and three unspecified centers (9, 11, 13), consistent with stereo_complete=false. Reconstruction preserves those counts but changes nine amide motifs to C(OH)=N and reports nine additional unspecified double bonds. Both canonical SMILES comparisons are false and the one-way map is empty. The C5O-ring configuration is retained as encoded; neither its ring count nor normalization identifies a sugar residue or proves the natural stereochemistry.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-7bc3610bc0.

BGC0002625 v2 is active, of questionable quality and unknown completeness. Desmonostoc muscorum LEGE 12446, NCBITaxon:1828758, remains SOURCE_ASSERTION; JADEXS020000001.1:7046147–7109291 remains CLUSTER_UNSTATED. The raw class column is NRPS&#124;PKS and subclass Type I&#124;Unknown; neither is a complete pathway. Occurrence NCBITaxon:1179 and producer NCBITaxon:1828758 remain distinct. Cached Desmonostoc muscorum and Nostoc muscorum synonym text supports naming context only, not new rank, lineage or strain confirmation.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-7bc3610bc0.

PMID:35793792 is retained with COMPOUND_EVIDENCE scope. LOTUS and CyanoMetDB cite DOI:10.1021/ACS.JNATPROD.2C00162 and DOI:10.1021/acs.jnatprod.2c00162 respectively; letter case does not create separate publications. The CyanoMetDB nmr_used=Yes field is a retained source assertion, not currently read NMR data. Two seeding-history events and the accession remain provenance, with no fresh primary or sequence access.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-7bc3610bc0.

The six positive rows are MIBiG, two LOTUS rows, one CyanoMetDB row, NPClassifier and a PubChem blank-AID sentinel. The two LOTUS organism labels share NCBITaxon:1179 and the same publication but retain different Wikidata organism identifiers; they are not two independent producer experiments. CyanoMetDB retains LEGE 12446 occurrence context. CID 168010362 has an empty AID and supplies no assay result. Target and related-corpus joins are negative within the saved scope; the curation receipt applies no correction.

### Classification and saved topology

consistency: unknown. Targets: naturalproductmech:mibig-7bc3610bc0.

The original graph has a 34-member ester-containing ring, two five-member nitrogen-containing rings, a six-member aromatic ring and a saturated C5O ring, with 11 amide attachments and one ester. An aliphatic chain and aromatic-O-C5O linkage support the retained glycopeptidolipid and computed cyclic/lipo/depsipeptide descriptions only at the encoded-topology level. The C5O ring is not assigned a sugar name or anomer. Compared with B, A lacks the ring O-acetyl branch; the saved correspondence supports a structural difference, not an acetylation pathway. The dual computed biosynthetic pathway remains unverified.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-7bc3610bc0.

The complete selected owner/history, all selected retained source rows and query boundaries, both full saved molecular forms and actual intake metadata have been read. The input hashes and ownership declarations agree with the accepted plan; that is not scientific reading of every captured corpus file. Five local gates passed, but full QC and OAK are unavailable and fresh source verification is prohibited. No applicable maintained-reader scope exists. Completion remains partial; no record, native status or history edit is proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2599-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/desmamide-a.yaml; Whole current plaintext including all curation_history entries | supports | Complete selected owner and all 2 seeding-history events; retained content only. |
| support-2599-capture | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/8/owner_document | supports | Complete captured owner, including present claims and literal absence of mechanism, target and component roots. |
| support-2599-grounding-owner | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Exact retained identifier, label, complete structure and minted source grounding; no natural-identity verification. |
| support-2599-provenance-owner | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/producer_taxon_groups; /records/8/owner_document/bgc_class | supports | Owner-local producer, locus and BGC assertions with their distinct stored grades. |
| support-2599-classification-owner | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/biosynthesis_origin; /records/8/owner_document/compound_classes | supports | Retained source classes and computed classification outputs; their presence is distinct from biological mechanism support. |
| support-2599-citations-history | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/source_concepts; /records/8/owner_document/curation_history | supports | Owner-local retained references, source concepts and complete history; no primary-paper or sequence access. |
| support-2599-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json; /records/8/owner_document/occurrences; /records/8/owner_document/occurrence_taxon_groups; /records/8/owner_document/xrefs | supports | Complete retained occurrence/xref context, or literal absence in the complete owner; not a production or activity experiment. |
| support-2599-intake | /private/tmp/npm-review-work/shared-next-batch260/intakes-001/2599-inspect-001.json; /status; /source; /targets | supports | Actual inspection-only input hashes and complete target ownership declarations; this is not a scientific reading of all captured corpus files. |
| support-2599-intake-execution | /private/tmp/npm-review-work/shared-next-batch260/intakes-001/2599-inspect-execution-001.json; /exit_code; /command; /actual_environment; /stdout; /stderr | supports | Original canonical inspect receipt for this owner, with exit 0 and empty stderr. |
| support-2599-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch260/root-intake-acceptance-001.json; /accepted; /status; /summary; /plan; /source_placements; /unique_source_paths | supports | ROOT acceptance of the original ten inspections and exact 455 placements across 63 paths. |
| support-2599-direct-contexts | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates; /records/8/identity_comparison_paths; /records/8/additional_context_paths; /records/8/additional_context_roles; /records/8/reader_implementation_paths; /records/8/proposed_input_paths; /records/8/proposed_input_count | supports | Exact owner-local companion, comparison and additional-input roles. Seven diagnostic/query or implementation inputs are captured for this owner; no maintained-reader role applies. Capture does not confer positive scientific support. |
| support-2599-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch260/root-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT acceptance of the actual original source plan used by this intake. |
| support-2599-source-reading | /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-assigned-source-reading-001.json; /contexts/6 | supports | Personally read all nine saved query frames and all 6 positive row placements/63 fields for this selected owner; broader companion coverage is separately attributed. |
| support-2599-raw-reading | /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-assigned-source-reading-001.json; /raw_reading | supports | Receipt for Support whole selected raw-owner/history reading and separately pinned six-companion reading; no primary-source reopening. |
| support-2599-companion-reading | /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-six-companion-whole-reading-001.json; /scope | supports | Support personally read six complete companion records/history. Their different keys, grades and source scope remain separate from the selected owner. |
| support-2599-source-notes | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Attributed source-reading reconciliation: 55 BGC plus 42 Support row placements and zero Native source-row credit. Notes preserve source, cache and curation scope separately. |
| support-2599-taxonomy | /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-cached-taxonomy-reading-001.json; /context_interpretations/11; /interpretation; /counts | supports | Cached name/synonym interpretation for this owner. No rank, lineage, freshness or producer confirmation is supplied. |
| support-2599-curation-scope | /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /interpretation; /implementation_scope | supports | Retained implemented-curation resolution reports no applicable selected correction. Native scope is table/implementation-specific, including only row_digest from structure_corrections.py. |
| support-2599-chemistry | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-DATA-001.json; /records/8 | supports | Complete two-form saved molecular result for this owner, including every atom, bond, stereo annotation, motif, false comparison and empty one-way map; no natural-identity proof. |
| support-2599-molecular-reading | /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-last-five-molecular-intake-reading-001.json; /records/3 | supports | Support personally read both complete saved atom/bond tables and all scalar, ring, stereo and motif fields for this owner; interpretations preserve fixed-form limitations. |
| support-2599-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /scope; /warnings | supports | ROOT acceptance of the one original diagnostic, including false comparisons and unassigned original warnings. |
| support-2599-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-execution-001.json; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0 with zero retries; four charge-rearrangement warnings remain global. |
| support-2599-native-gates | /private/tmp/npm-review-work/shared-next-batch260/root-native-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five local checks passed; required full QC and OAK remain unavailable. Technical validation is distinct from scientific proof. |
| support-2599-queue-reading | /private/tmp/npm-review-work/shared-next-batch260/root-native-queue-reading-001.json; /selected_rows | supports | ROOT personally read the current selected queue rows. Queue labels are review leads rather than automatic scientific defects. |
| support-2599-reader-applicability | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | Exact selected profile has no mechanism-owner or maintained-reader applicability; no reader check is invented. |
| support-2599-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/mibig_compounds | supports | Complete retained mibig_compounds frame: 1 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-source-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 3351-3351; complete parsed row at /contexts/11/source_scope_inventory/joins/mibig_compounds/matches/0/row in the pinned inventory | supports | Complete retained MIBiG row, including distinct producer/locus/reference grades, entry qualifiers and literal class/subclass columns. |
| support-2599-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/chebi_structures | supports | Complete retained chebi_structures frame: 0 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained lotus_occurrences frame: 2 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-source-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8371-8371; complete parsed row at /contexts/11/source_scope_inventory/joins/lotus_occurrences/matches/0/row in the pinned inventory | supports | Complete cited occurrence row; source labels and database placements are not independent causal production evidence. |
| support-2599-source-lotus_occurrences-1 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 8372-8372; complete parsed row at /contexts/11/source_scope_inventory/joins/lotus_occurrences/matches/1/row in the pinned inventory | supports | Complete cited occurrence row; source labels and database placements are not independent causal production evidence. |
| support-2599-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained cyanometdb_occurrences frame: 1 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-source-cyanometdb_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/cyanometdb_occurrences.tsv; physical lines 67-67; complete parsed row at /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences/matches/0/row in the pinned inventory | supports | Complete cited CyanoMetDB occurrence and nmr_used metadata; no current NMR access. |
| support-2599-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/npclassifier | supports | Complete retained npclassifier frame: 1 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-source-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2241-2241; complete parsed row at /contexts/11/source_scope_inventory/joins/npclassifier/matches/0/row in the pinned inventory | supports | Complete retained computed classifier row; pathway and family predictions retain model provenance. |
| support-2599-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained pubchem_bioassay frame: 1 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-source-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6966-6966; complete parsed row at /contexts/11/source_scope_inventory/joins/pubchem_bioassay/matches/0/row in the pinned inventory | supports | Complete blank-AID sentinel. Compound/CID presence is not an assay result or biological activity. |
| support-2599-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained bindingdb_targets frame: 0 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained antibioticmech_inchikeys frame: 0 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/chebi_origins | supports | Complete retained chebi_origins frame: 0 matched row placements. Negative results are bounded by this saved predicate and inventory. |
| support-2599-taxon-query-scope | /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/source_taxa; /contexts/11/source_scope_inventory/forward_taxon_merge_matches; /contexts/11/source_scope_inventory/nonorganism_matches | supports | Exact saved source-taxon IDs and negative merge/non-organism table matches for this owner; no fresh taxonomy decision. |
| support-2599-desmamide-comparison | /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-DATA-001.json; /records/8/smiles/computed; /records/9/smiles/computed | supports | Both complete original saved forms support the encoded A/B O-acetyl comparison; no new parse, natural identity, sugar-name or enzyme inference. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-260/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-260/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-260/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-260/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-260/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained current owner/history, saved source rows and local diagnostic only; no fresh primary-paper, sequence or taxonomy verification.
- Both canonical SMILES comparisons are false and the one-way map is empty. Normalized identifiers do not establish full graph or natural identity; reconstructed imidic stereo is not promoted to an original-structure defect.
- Four global charge-rearrangement warnings remain unassigned. Full QC and OAK remain unavailable; computed pathway applicability and source-level biological limits remain explicit.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete selected owners/history and ten saved molecular forms (768 atom rows, 802 bond rows, 44 rings), plus 99 retained query frames/42 positive row placements/503 fields across eleven assigned contexts. The selected five contribute 45 frames/20 rows/234 fields; companion reading remains separate.
- Verified 229 actual input placements across 54 paths and all 63 assigned ownership declarations. Hash capture is not scientific reading of entire TSV corpora. No record/status/history edit or outbound request was made.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T202323Z-desmamide-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: desmamide A'
started_at: '2026-11-05T19:33:20.891242Z'
finished_at: '2026-11-05T20:23:23.422835Z'
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
summary: Desmamide A retains a reproducible MIBiG mapping and source-level producer
  and locus claims. Its original saved graph supports a cyclic lipo-depsipeptide-compatible
  topology with an aryl-linked C5O ring, without assigning a named sugar. Three tetrahedral
  centers remain unspecified, and the reconstructed imidic form does not establish
  full graph or natural identity.
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
  - path: data/natural_products/unclassified/desmamide-a.yaml
    sha256: fbadbcffc00becf2937dac79204a36f53f21bc7b2f3299036d0ce9ea9fc750ee
    role: target
  - path: data/natural_products/unclassified/desmamide-b.yaml
    sha256: 58a89942f80460152e4469df7f9b1966b4c59ae718b260125fc6aeef99ef46cb
    role: context
  - path: data/natural_products/unclassified/desmamide-c.yaml
    sha256: fd7ba1cddf6863d2beca6d2ecafaf6f0286a219643133074733c7c843af7a6d4
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
  selection: Campaign path order 2599; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-7bc3610bc0
targets:
- target_id: naturalproductmech:mibig-7bc3610bc0
  path: data/natural_products/unclassified/desmamide-a.yaml
  label: desmamide A
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
    path: data/raw/cyanometdb_occurrences.tsv
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
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  command: just validate-strict data/natural_products/unclassified/cystobactamid-919-1.yaml
    data/natural_products/unclassified/cystobactamid-919-2.yaml data/natural_products/unclassified/cystothiazole-a.yaml
    data/natural_products/unclassified/daptomycin.yaml data/natural_products/unclassified/dehydrodidemnin-b-aplidine.yaml
    data/natural_products/unclassified/deoxyhangtaimycin.yaml data/natural_products/unclassified/depsibosamycin-d.yaml
    data/natural_products/unclassified/deschlorosvetamycin-a.yaml data/natural_products/unclassified/desmamide-a.yaml
    data/natural_products/unclassified/desmamide-b.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-260/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-7bc3610bc0
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-260/validate-all-001.tsv
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
  - naturalproductmech:mibig-7bc3610bc0
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
  - naturalproductmech:mibig-7bc3610bc0
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
  - naturalproductmech:mibig-7bc3610bc0
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-260/review-queue-001.tsv
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
  - naturalproductmech:mibig-7bc3610bc0
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2599-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/desmamide-a.yaml
  locator: Whole current plaintext including all curation_history entries
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete selected owner and all 2 seeding-history events; retained content
    only.
  snapshot_sha256: fbadbcffc00becf2937dac79204a36f53f21bc7b2f3299036d0ce9ea9fc750ee
- evidence_id: support-2599-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete captured owner, including present claims and literal absence of
    mechanism, target and component roots.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: support-2599-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Exact retained identifier, label, complete structure and minted source
    grounding; no natural-identity verification.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: support-2599-provenance-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/producer_taxon_groups; /records/8/owner_document/bgc_class
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Owner-local producer, locus and BGC assertions with their distinct stored
    grades.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: support-2599-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/biosynthesis_origin; /records/8/owner_document/compound_classes
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Retained source classes and computed classification outputs; their presence
    is distinct from biological mechanism support.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: support-2599-citations-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/source_concepts;
    /records/8/owner_document/curation_history
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Owner-local retained references, source concepts and complete history;
    no primary-paper or sequence access.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: support-2599-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/owner-capture-DATA-001.json
  locator: /records/8/owner_document/occurrences; /records/8/owner_document/occurrence_taxon_groups;
    /records/8/owner_document/xrefs
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete retained occurrence/xref context, or literal absence in the complete
    owner; not a production or activity experiment.
  snapshot_sha256: 2e2e8fb7b85daae766641584163c34e6ff88fbf94291430fa380e294fa8bee19
- evidence_id: support-2599-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/intakes-001/2599-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Actual inspection-only input hashes and complete target ownership declarations;
    this is not a scientific reading of all captured corpus files.
  snapshot_sha256: 7b84d6b6a36aad184a82218465788737c25039ccda4b1e571dda2004b279637d
- evidence_id: support-2599-intake-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/intakes-001/2599-inspect-execution-001.json
  locator: /exit_code; /command; /actual_environment; /stdout; /stderr
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Original canonical inspect receipt for this owner, with exit 0 and empty
    stderr.
  snapshot_sha256: 62f73c61e3ce27cd9c1b35188b853864b3cd181a984130defd15bde8d97cc624
- evidence_id: support-2599-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-intake-acceptance-001.json
  locator: /accepted; /status; /summary; /plan; /source_placements; /unique_source_paths
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: ROOT acceptance of the original ten inspections and exact 455 placements
    across 63 paths.
  snapshot_sha256: 48c0dd3874d34a3fe56e6f43d6ecc044efb43d0fed97cf8713507ed05d70ed41
- evidence_id: support-2599-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates;
    /records/8/identity_comparison_paths; /records/8/additional_context_paths; /records/8/additional_context_roles;
    /records/8/reader_implementation_paths; /records/8/proposed_input_paths; /records/8/proposed_input_count
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Exact owner-local companion, comparison and additional-input roles. Seven
    diagnostic/query or implementation inputs are captured for this owner; no maintained-reader
    role applies. Capture does not confer positive scientific support.
  snapshot_sha256: 31543a1f8d8477dfd89c147a1d95a836b39146176a2f6d6f0887c064b79dacc3
- evidence_id: support-2599-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: ROOT acceptance of the actual original source plan used by this intake.
  snapshot_sha256: 32343815aa82a0d56f226d32975ee77e9ab34c667376058dcf1b53d881b61295
- evidence_id: support-2599-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-assigned-source-reading-001.json
  locator: /contexts/6
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Personally read all nine saved query frames and all 6 positive row placements/63
    fields for this selected owner; broader companion coverage is separately attributed.
  snapshot_sha256: 7d00e3fb98c209a6669e540c00f2dbca78e619dea13ad9219e5f3778fb1ab9e6
- evidence_id: support-2599-raw-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-assigned-source-reading-001.json
  locator: /raw_reading
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Receipt for Support whole selected raw-owner/history reading and separately
    pinned six-companion reading; no primary-source reopening.
  snapshot_sha256: 7d00e3fb98c209a6669e540c00f2dbca78e619dea13ad9219e5f3778fb1ab9e6
- evidence_id: support-2599-companion-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-six-companion-whole-reading-001.json
  locator: /scope
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Support personally read six complete companion records/history. Their different
    keys, grades and source scope remain separate from the selected owner.
  snapshot_sha256: 3e3789e8c14a142318c02e8a988aaf4e8b9f0ebd077473de6c074571a77271f8
- evidence_id: support-2599-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Attributed source-reading reconciliation: 55 BGC plus 42 Support row placements
    and zero Native source-row credit. Notes preserve source, cache and curation scope
    separately.'
  snapshot_sha256: 740dbb3ff3e48483ca7251ca1d6c0e98d5fb0c1994a38c71045fdcd84d071dc0
- evidence_id: support-2599-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-cached-taxonomy-reading-001.json
  locator: /context_interpretations/11; /interpretation; /counts
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Cached name/synonym interpretation for this owner. No rank, lineage, freshness
    or producer confirmation is supplied.
  snapshot_sha256: 341eb459cc59fbcb70393b278b9b5de0cdcf48817d9641c97f49d08ee6e4da50
- evidence_id: support-2599-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/native-prep/native-current260-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /interpretation; /implementation_scope
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Retained implemented-curation resolution reports no applicable selected
    correction. Native scope is table/implementation-specific, including only row_digest
    from structure_corrections.py.
  snapshot_sha256: 1f7fd8a5c9f7bc3fd10d464aa2b443adad2dfc5faf417010b98d0dda8f87b8e8
  search_scope: '{"scope": "Retained implemented exact-identity and row-digest predicates;
    lexical hits distinguished from applicable decisions", "selected_owner": "data/natural_products/unclassified/desmamide-a.yaml",
    "source_row_credit": 0}'
- evidence_id: support-2599-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete two-form saved molecular result for this owner, including every
    atom, bond, stereo annotation, motif, false comparison and empty one-way map;
    no natural-identity proof.
  snapshot_sha256: e9c8abdeb50c79ef4be2bbec545f99015ee724587ba4f9892b51b2e5f0e16258
- evidence_id: support-2599-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/support-prep/support-current260-last-five-molecular-intake-reading-001.json
  locator: /records/3
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Support personally read both complete saved atom/bond tables and all scalar,
    ring, stereo and motif fields for this owner; interpretations preserve fixed-form
    limitations.
  snapshot_sha256: 18b82d7ddda54d41218ea5f83a64186b45e5e8ab3a0b75ebde70bb698efe8a6d
- evidence_id: support-2599-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /scope; /warnings
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: ROOT acceptance of the one original diagnostic, including false comparisons
    and unassigned original warnings.
  snapshot_sha256: b394d34147477dca214f38d6a5bb7bc193b47109faa3869755d34a87bacde21d
- evidence_id: support-2599-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Original diagnostic exit 0 with zero retries; four charge-rearrangement
    warnings remain global.
  snapshot_sha256: 06354cc95be3de2c172fc46d09cd63e24d02d4078f16df4fd7497ab7ab70f79b
- evidence_id: support-2599-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-native-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Five local checks passed; required full QC and OAK remain unavailable.
    Technical validation is distinct from scientific proof.
  snapshot_sha256: 20997a8aa70b4d2ffd564963e2dd1e8d9de39018545b1226b31f26f6bf984bb4
- evidence_id: support-2599-queue-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260/root-native-queue-reading-001.json
  locator: /selected_rows
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: ROOT personally read the current selected queue rows. Queue labels are
    review leads rather than automatic scientific defects.
  snapshot_sha256: 30cbca9fd4bc81345edfcd263e9628b900992c1f8bcb851a6d91ad89efcbac27
- evidence_id: support-2599-reader-applicability
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Exact selected profile has no mechanism-owner or maintained-reader applicability;
    no reader check is invented.
  snapshot_sha256: f935f62c48ce92be06a533503bea2db993330c4cafdf6d0dac68b5bd23083e58
- evidence_id: support-2599-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained mibig_compounds frame: 1 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 3351-3351; complete parsed row at /contexts/11/source_scope_inventory/joins/mibig_compounds/matches/0/row
    in the pinned inventory
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete retained MIBiG row, including distinct producer/locus/reference
    grades, entry qualifiers and literal class/subclass columns.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2599-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained chebi_structures frame: 0 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained lotus_occurrences frame: 2 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 2, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8371-8371; complete parsed row at /contexts/11/source_scope_inventory/joins/lotus_occurrences/matches/0/row
    in the pinned inventory
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete cited occurrence row; source labels and database placements are
    not independent causal production evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2599-source-lotus_occurrences-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 8372-8372; complete parsed row at /contexts/11/source_scope_inventory/joins/lotus_occurrences/matches/1/row
    in the pinned inventory
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete cited occurrence row; source labels and database placements are
    not independent causal production evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2599-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained cyanometdb_occurrences frame: 1 matched row placements.
    Negative results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-source-cyanometdb_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/cyanometdb_occurrences.tsv
  locator: physical lines 67-67; complete parsed row at /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences/matches/0/row
    in the pinned inventory
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete cited CyanoMetDB occurrence and nmr_used metadata; no current
    NMR access.
  snapshot_sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
- evidence_id: support-2599-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained npclassifier frame: 1 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2241-2241; complete parsed row at /contexts/11/source_scope_inventory/joins/npclassifier/matches/0/row
    in the pinned inventory
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete retained computed classifier row; pathway and family predictions
    retain model provenance.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2599-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained pubchem_bioassay frame: 1 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-source-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6966-6966; complete parsed row at /contexts/11/source_scope_inventory/joins/pubchem_bioassay/matches/0/row
    in the pinned inventory
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Complete blank-AID sentinel. Compound/CID presence is not an assay result
    or biological activity.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2599-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained bindingdb_targets frame: 0 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained antibioticmech_inchikeys frame: 0 matched row placements.
    Negative results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "SGSWMZBFZBNBSH-ONBVFTLRSA-N"}'
- evidence_id: support-2599-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: 'Complete retained chebi_origins frame: 0 matched row placements. Negative
    results are bounded by this saved predicate and inventory.'
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"matched_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2599-taxon-query-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch260-tentative/bgc-prep/bgc-conditional260-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/source_taxa; /contexts/11/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/11/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Exact saved source-taxon IDs and negative merge/non-organism table matches
    for this owner; no fresh taxonomy decision.
  snapshot_sha256: 97cb4a87681b978f4cc4f2c0817cada9bad1dcd677c2aca543c58320057013eb
  search_scope: '{"merge_matches": 0, "nonorganism_matches": 0, "predicate": "exact
    retained taxon ID match against the two pinned diagnostic tables", "source_taxa":
    ["NCBITaxon:1179", "NCBITaxon:1828758"]}'
- evidence_id: support-2599-desmamide-comparison
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch260/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/smiles/computed; /records/9/smiles/computed
  accessed_at: '2026-11-05T20:14:18.638476Z'
  support: supports
  summary: Both complete original saved forms support the encoded A/B O-acetyl comparison;
    no new parse, natural identity, sugar-name or enzyme inference.
  snapshot_sha256: e9c8abdeb50c79ef4be2bbec545f99015ee724587ba4f9892b51b2e5f0e16258
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:35:58.108095Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 6942ae586a37f1f6b0bfb953bb033d936740f6cadc8e55613e9606147d21e0b5
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:36:23.921683Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 1c748ba7fbed98b1a37bc11eeaf650da93dae7b9457394d90018afccdabb0508
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:36:44.647940Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:37:19.990709Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-260/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-260/native-current260-five-gates-execution-001.json
  accessed_at: '2026-11-05T19:37:32.297786Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: d16d92e0251bd183ccd4e5ea14ba7888a14b7eaeb33b2b3635fb5cec93f057b0
assessments:
- area: identity
  topic: Retained identity and grounding
  outcome: supported
  summary: The minted identifier, label, BGC0002625 compound 1 and full key SGSWMZBFZBNBSH-ONBVFTLRSA-N
    agree in the complete owner and exact retained MIBiG row. No exact-key ChEBI structure
    row was returned. Both saved forms regenerate the declared key, supporting reproducible
    stored mapping without proving natural identity or allowing congener substitution.
  assessment_id: support-2599-identity
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-grounding-owner
  - support-2599-chemistry
  - support-2599-direct-contexts
  - support-2599-source-reading
  - support-2599-query-chebi_structures
  - support-2599-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: SGSWMZBFZBNBSH-ONBVFTLRSA-N
    definition: Exact full key; no prefix or name substitution.
    evidence_ids:
    - support-2599-grounding-owner
    - support-2599-chemistry
    - support-2599-direct-contexts
    - support-2599-source-reading
    - support-2599-query-chebi_structures
    - support-2599-source-mibig_compounds-0
  - name: grounding_scope
    value: MINTED retained mapping; natural identity not independently reverified
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2599-grounding-owner
    - support-2599-chemistry
    - support-2599-direct-contexts
    - support-2599-source-reading
    - support-2599-query-chebi_structures
    - support-2599-source-mibig_compounds-0
- area: representation
  topic: Stored forms and stereochemistry
  outcome: unknown
  summary: Both forms give C66H105N11O21, charge 0, 98 atoms and 102 bonds and SGSWMZBFZBNBSH-ONBVFTLRSA-N.
    The original graph has 14 specified tetrahedral centers and three unspecified
    centers (9, 11, 13), consistent with stereo_complete=false. Reconstruction preserves
    those counts but changes nine amide motifs to C(OH)=N and reports nine additional
    unspecified double bonds. Both canonical SMILES comparisons are false and the
    one-way map is empty. The C5O-ring configuration is retained as encoded; neither
    its ring count nor normalization identifies a sugar residue or proves the natural
    stereochemistry.
  assessment_id: support-2599-representation
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-grounding-owner
  - support-2599-chemistry
  - support-2599-molecular-reading
  - support-2599-diagnostic-acceptance
  - support-2599-diagnostic-execution
  - support-2599-source-mibig_compounds-0
  dimensions:
  - name: stereochemistry_scope
    value: 14 specified + 3 unspecified tetrahedral centers; no original undefined
      double bond
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    evidence_ids:
    - support-2599-grounding-owner
    - support-2599-chemistry
    - support-2599-molecular-reading
    - support-2599-diagnostic-acceptance
    - support-2599-diagnostic-execution
    - support-2599-source-mibig_compounds-0
  - name: representation_correspondence
    value: 8/10 comparisons true; canonical strings differ; map empty; 9 imidic shifts
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    evidence_ids:
    - support-2599-grounding-owner
    - support-2599-chemistry
    - support-2599-molecular-reading
    - support-2599-diagnostic-acceptance
    - support-2599-diagnostic-execution
    - support-2599-source-mibig_compounds-0
- area: provenance
  topic: Producer, taxonomy and locus grades
  outcome: supported
  summary: BGC0002625 v2 is active, of questionable quality and unknown completeness.
    Desmonostoc muscorum LEGE 12446, NCBITaxon:1828758, remains SOURCE_ASSERTION;
    JADEXS020000001.1:7046147–7109291 remains CLUSTER_UNSTATED. The raw class column
    is NRPS|PKS and subclass Type I|Unknown; neither is a complete pathway. Occurrence
    NCBITaxon:1179 and producer NCBITaxon:1828758 remain distinct. Cached Desmonostoc
    muscorum and Nostoc muscorum synonym text supports naming context only, not new
    rank, lineage or strain confirmation.
  assessment_id: support-2599-provenance
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-provenance-owner
  - support-2599-taxonomy
  - support-2599-taxon-query-scope
  - support-2599-curation-scope
  - support-2599-direct-contexts
  - support-2599-source-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    value: Producer 1828758; occurrences 1179; cached name/synonyms, no verified lineage
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    evidence_ids:
    - support-2599-provenance-owner
    - support-2599-taxonomy
    - support-2599-taxon-query-scope
    - support-2599-curation-scope
    - support-2599-direct-contexts
    - support-2599-source-mibig_compounds-0
  - name: producer_evidence
    value: SOURCE_ASSERTION
    definition: Retained producer grade, not inferred from occurrence or locus association.
    evidence_ids:
    - support-2599-provenance-owner
    - support-2599-taxonomy
    - support-2599-taxon-query-scope
    - support-2599-curation-scope
    - support-2599-direct-contexts
    - support-2599-source-mibig_compounds-0
  - name: locus_evidence
    value: CLUSTER_UNSTATED; retained genome interval only
    definition: Retained compound-specific cluster-link grade and source methods.
    evidence_ids:
    - support-2599-provenance-owner
    - support-2599-taxonomy
    - support-2599-taxon-query-scope
    - support-2599-curation-scope
    - support-2599-direct-contexts
    - support-2599-source-mibig_compounds-0
- area: evidence
  topic: Citation and history scope
  outcome: supported
  summary: PMID:35793792 is retained with COMPOUND_EVIDENCE scope. LOTUS and CyanoMetDB
    cite DOI:10.1021/ACS.JNATPROD.2C00162 and DOI:10.1021/acs.jnatprod.2c00162 respectively;
    letter case does not create separate publications. The CyanoMetDB nmr_used=Yes
    field is a retained source assertion, not currently read NMR data. Two seeding-history
    events and the accession remain provenance, with no fresh primary or sequence
    access.
  assessment_id: support-2599-citations
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-citations-history
  - support-2599-source-reading
  - support-2599-companion-reading
  - support-2599-source-mibig_compounds-0
  - support-2599-source-lotus_occurrences-0
  - support-2599-source-lotus_occurrences-1
  - support-2599-source-cyanometdb_occurrences-0
  - support-2599-source-npclassifier-0
  - support-2599-source-pubchem_bioassay-0
  dimensions:
  - name: citation_scope
    value: PMID:35793792 [COMPOUND_EVIDENCE]; shared DOI:10.1021/acs.jnatprod.2c00162
    definition: Exact retained citation basis; no implied new primary-source access.
    evidence_ids:
    - support-2599-citations-history
    - support-2599-source-reading
    - support-2599-companion-reading
    - support-2599-source-mibig_compounds-0
    - support-2599-source-lotus_occurrences-0
    - support-2599-source-lotus_occurrences-1
    - support-2599-source-cyanometdb_occurrences-0
    - support-2599-source-npclassifier-0
    - support-2599-source-pubchem_bioassay-0
- area: evidence
  topic: Occurrence, assay and target boundaries
  outcome: supported
  summary: The six positive rows are MIBiG, two LOTUS rows, one CyanoMetDB row, NPClassifier
    and a PubChem blank-AID sentinel. The two LOTUS organism labels share NCBITaxon:1179
    and the same publication but retain different Wikidata organism identifiers; they
    are not two independent producer experiments. CyanoMetDB retains LEGE 12446 occurrence
    context. CID 168010362 has an empty AID and supplies no assay result. Target and
    related-corpus joins are negative within the saved scope; the curation receipt
    applies no correction.
  assessment_id: support-2599-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-occurrence-owner
  - support-2599-curation-scope
  - support-2599-source-reading
  - support-2599-query-mibig_compounds
  - support-2599-query-chebi_structures
  - support-2599-query-lotus_occurrences
  - support-2599-query-cyanometdb_occurrences
  - support-2599-query-npclassifier
  - support-2599-query-pubchem_bioassay
  - support-2599-query-bindingdb_targets
  - support-2599-query-antibioticmech_inchikeys
  - support-2599-query-chebi_origins
  - support-2599-source-mibig_compounds-0
  - support-2599-source-lotus_occurrences-0
  - support-2599-source-lotus_occurrences-1
  - support-2599-source-cyanometdb_occurrences-0
  - support-2599-source-npclassifier-0
  - support-2599-source-pubchem_bioassay-0
  dimensions:
  - name: occurrence_scope
    value: 2 LOTUS + 1 CyanoMetDB rows; shared citation, distinct source contexts
    definition: Source placements and shared citations are not independent production
      experiments.
    evidence_ids:
    - support-2599-occurrence-owner
    - support-2599-curation-scope
    - support-2599-source-reading
    - support-2599-query-mibig_compounds
    - support-2599-query-chebi_structures
    - support-2599-query-lotus_occurrences
    - support-2599-query-cyanometdb_occurrences
    - support-2599-query-npclassifier
    - support-2599-query-pubchem_bioassay
    - support-2599-query-bindingdb_targets
    - support-2599-query-antibioticmech_inchikeys
    - support-2599-query-chebi_origins
    - support-2599-source-mibig_compounds-0
    - support-2599-source-lotus_occurrences-0
    - support-2599-source-lotus_occurrences-1
    - support-2599-source-cyanometdb_occurrences-0
    - support-2599-source-npclassifier-0
    - support-2599-source-pubchem_bioassay-0
  - name: assay_target_scope
    value: 0 AIDs; CID 168010362 blank sentinel; target joins negative
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    evidence_ids:
    - support-2599-occurrence-owner
    - support-2599-curation-scope
    - support-2599-source-reading
    - support-2599-query-mibig_compounds
    - support-2599-query-chebi_structures
    - support-2599-query-lotus_occurrences
    - support-2599-query-cyanometdb_occurrences
    - support-2599-query-npclassifier
    - support-2599-query-pubchem_bioassay
    - support-2599-query-bindingdb_targets
    - support-2599-query-antibioticmech_inchikeys
    - support-2599-query-chebi_origins
    - support-2599-source-mibig_compounds-0
    - support-2599-source-lotus_occurrences-0
    - support-2599-source-lotus_occurrences-1
    - support-2599-source-cyanometdb_occurrences-0
    - support-2599-source-npclassifier-0
    - support-2599-source-pubchem_bioassay-0
- area: consistency
  topic: Classification and saved topology
  outcome: unknown
  summary: The original graph has a 34-member ester-containing ring, two five-member
    nitrogen-containing rings, a six-member aromatic ring and a saturated C5O ring,
    with 11 amide attachments and one ester. An aliphatic chain and aromatic-O-C5O
    linkage support the retained glycopeptidolipid and computed cyclic/lipo/depsipeptide
    descriptions only at the encoded-topology level. The C5O ring is not assigned
    a sugar name or anomer. Compared with B, A lacks the ring O-acetyl branch; the
    saved correspondence supports a structural difference, not an acetylation pathway.
    The dual computed biosynthetic pathway remains unverified.
  assessment_id: support-2599-classification
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-classification-owner
  - support-2599-chemistry
  - support-2599-molecular-reading
  - support-2599-source-npclassifier-0
  - support-2599-source-mibig_compounds-0
  - support-2599-desmamide-comparison
  dimensions:
  - name: classification_applicability
    value: 34-member cycle, 11 amides, 1 ester, aryl-linked C5O ring; sugar identity
      unassigned
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    evidence_ids:
    - support-2599-classification-owner
    - support-2599-chemistry
    - support-2599-molecular-reading
    - support-2599-source-npclassifier-0
    - support-2599-source-mibig_compounds-0
    - support-2599-desmamide-comparison
- area: completeness
  topic: Scientific completion and ownership
  outcome: unknown
  summary: The complete selected owner/history, all selected retained source rows
    and query boundaries, both full saved molecular forms and actual intake metadata
    have been read. The input hashes and ownership declarations agree with the accepted
    plan; that is not scientific reading of every captured corpus file. Five local
    gates passed, but full QC and OAK are unavailable and fresh source verification
    is prohibited. No applicable maintained-reader scope exists. Completion remains
    partial; no record, native status or history edit is proposed.
  assessment_id: support-2599-completion
  target_ids:
  - naturalproductmech:mibig-7bc3610bc0
  evidence_ids:
  - support-2599-intake
  - support-2599-intake-execution
  - support-2599-intake-acceptance
  - support-2599-plan-acceptance
  - support-2599-native-gates
  - support-2599-diagnostic-acceptance
  - support-2599-reader-applicability
  - support-2599-source-reading
  - support-2599-molecular-reading
  - support-2599-source-notes
  - support-2599-queue-reading
  dimensions:
  - name: review_completion
    value: partial; 5 local gates passed; full QC/OAK unavailable; zero required readers
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    evidence_ids:
    - support-2599-intake
    - support-2599-intake-execution
    - support-2599-intake-acceptance
    - support-2599-plan-acceptance
    - support-2599-native-gates
    - support-2599-diagnostic-acceptance
    - support-2599-reader-applicability
    - support-2599-source-reading
    - support-2599-molecular-reading
    - support-2599-source-notes
    - support-2599-queue-reading
findings: []
actions: []
limitations:
- Retained current owner/history, saved source rows and local diagnostic only; no
  fresh primary-paper, sequence or taxonomy verification.
- Both canonical SMILES comparisons are false and the one-way map is empty. Normalized
  identifiers do not establish full graph or natural identity; reconstructed imidic
  stereo is not promoted to an original-structure defect.
- Four global charge-rearrangement warnings remain unassigned. Full QC and OAK remain
  unavailable; computed pathway applicability and source-level biological limits remain
  explicit.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read five complete selected owners/history and ten saved molecular
  forms (768 atom rows, 802 bond rows, 44 rings), plus 99 retained query frames/42
  positive row placements/503 fields across eleven assigned contexts. The selected
  five contribute 45 frames/20 rows/234 fields; companion reading remains separate.
- Verified 229 actual input placements across 54 paths and all 63 assigned ownership
  declarations. Hash capture is not scientific reading of entire TSV corpora. No record/status/history
  edit or outbound request was made.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-260
```
