# Local evidence review: Yossoside V

- Review: 20261104T192651Z-yossoside-v
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T18:38:45.542493Z
- Finished UTC: 2026-11-04T19:26:51.917323Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Yossoside V retains a consistent exact-key source and stored-form join, with three unresolved tetrahedral centers. Its oxygenated-ring and ester topology supports a glycoside context, while sugar identity, natural stereochemistry and the named model family remain qualified. Producer and locus evidence stay at their retained source grades.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2431; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-928d3a93b2 | data/natural_products/terpenoids/yossoside-v.yaml | generated | Yossoside V |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-928d3a93b2 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-928d3a93b2 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-928d3a93b2 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-928d3a93b2 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-928d3a93b2 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-928d3a93b2 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-928d3a93b2 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-928d3a93b2 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained identity and natural-identity limits

identity: supported. Targets: naturalproductmech:mibig-928d3a93b2.

The minted record joins MIBiG BGC0002402, version 2, compound 5, by full key FJFARKHHKHMNRK-XRNHBKRYSA-N. Both stored forms normalize to neutral C62H96O29 and that key. The saved exact-key ChEBI join is empty; the grounding note remains historical, not a current global absence claim. Yossosides I–IV are distinct-key direct companions, so their structures, stereochemistry and activities are not transferred to V.

### Stored-form and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-928d3a93b2.

Each stored form contains 91 heavy atoms and 100 bonds, with 31 specified and three unspecified tetrahedral centers. The false stereo_complete flag is consistent with those unresolved positions; in the SMILES table they are atoms 12, 17 and 63. All ten comparisons are true with a complete supplied chirality-aware atom match, while full_graph_identity_established remains false. Agreement does not authenticate natural stereochemistry or resolve the question marks in the retained InChI.

### Distinct producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-928d3a93b2.

Spinacia oleracea NCBITaxon:3562 is retained as BGC_CHARACTERIZED, separately from the CLUSTER_DEMONSTRATED locus KQ150485.1:6311–44201. Knock-out studies and heterologous expression are the source locus methods. These database grades do not independently authenticate an experimental specimen, construct or native production in this review.

### Citation tiers and retained history

evidence: supported. Targets: naturalproductmech:mibig-928d3a93b2.

DOI:10.1038/s41589-020-0541-x is retained at MIBiG COMPOUND_EVIDENCE level and repeated in producer and locus evidence. The two seed-history events document regeneration, not two new experiments. The citation is a retained database attribution; no primary text, supplementary structure determination or assay protocol was newly inspected.

### Occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-928d3a93b2.

Both occurrence roots are absent in the complete owner, and the saved LOTUS, cyanobacterial and ChEBI-origin frames are empty for their exact predicates. These scoped negatives neither establish biological absence nor change the separate Spinacia producer/locus assertions.

### Model fidelity and family applicability

consistency: supported. Targets: naturalproductmech:mibig-928d3a93b2.

NPClassifier npclassifier.gnps2.org@2026-09-07 supplies Terpenoids/Triterpenoids/Oleanane triterpenoids and is_glycoside:true. The oxygenated cycles and external oxygen bridges support the glycoside context. Exact Oleanane-family applicability remains a model assertion rather than an independent biosynthetic conclusion. Whole C62 includes attached groups and does not by itself refute a triterpenoid class; MIBiG TERPENE remains a separate source assertion.

### Actual evidence coverage and remaining limits

completeness: unknown. Targets: naturalproductmech:mibig-928d3a93b2.

Complete owner/history, canonical intake, retained positive source payloads and empty frames, and both original molecular forms have been read. All four mechanism roots are absent, so no maintained-mechanism reader applies. The owner remains MINTED and SEEDED with 2 unchanged history events. Source seeder/extractor/model ownership remains distinct from curator-owned mechanism/history where present. The ignored-inclusive bounded curation scan found no applicable correction or exclusion. Full QC/OAK, fresh primary, taxonomy, assay/construct verification, and independent natural identity/stereochemistry remain unavailable. This is a partial review with no supported source-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2431-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-v.yaml; Complete plaintext including every curation_history entry | supports | Complete Yossoside V owner with all 2 history events; MINTED/SEEDED unchanged. Prior complete raw/history reading carries. |
| bgc-2431-capture | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0 | supports | Actual complete owner and any ordered component captures, metadata and exact root presence; capture fidelity is not independent scientific verification. |
| bgc-2431-intake | /private/tmp/npm-review-work/shared-next-batch244/intakes/2431-inspect-001.json; /status; /repository; /source; /targets | supports | Actual target and ownership roles with all 41 current input placements, joined to the accepted plan. |
| bgc-2431-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch244/root-intake-acceptance-001.json; /status; /summary | supports | ROOT accepted ten original canonical intakes; this owner’s complete target/ownership/input evidence is linked separately. |
| bgc-2431-grounding-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/grounding_notes | supports | Exact retained identifier, label, structure, source concepts and grounding status and grounding notes. |
| bgc-2431-origin-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Exact producer/locus grades, methods, accession and citation tiers, with coordinates only where supplied. Native production, strain identity and locus evidence remain distinct. |
| bgc-2431-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0/owner_document | supports | The complete owner lacks both occurrence roots, bioactivities, bioactivity_summary and molecular_targets. This is owner scope, not a biological absence claim. |
| bgc-2431-classification-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, pathway filing and source classes. Fidelity does not independently establish applicability. |
| bgc-2431-history-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0/owner_document/curation_status; /records/0/owner_document/curation_history | supports | Every retained history event and SEEDED status remain unchanged. |
| bgc-2431-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/0/owner_document | supports | Whole owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets; no maintained reader applies. |
| bgc-2431-chemistry | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge; /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key; /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles; /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count; /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge; /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key; /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles; /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count; /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts; /records/0/inchi/computed/stereo_counts | supports | All ten stored-form comparisons are true with a complete supplied chirality-aware match at its stated scope. full_graph_identity_established remains false; natural identity is unverified. |
| bgc-2431-topology | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs; /records/0/inchi/computed/fragment_atom_indices | supports | The SMILES table contains four saturated C5O six-membered cycles and a separate oxygenated all-carbon six-membered cycle. External oxygen linkages, two carboxylic acids and two ester groups are retained; the ester bridges include C26–O27–C28 and C56–O55–C54. The all-carbon cycle is not another C5O ring. This supports an oxygenated glycosidic context without assigning sugar names, anomers, biochemical linkage positions or a natural residue count from the compound label. |
| bgc-2431-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-current244-first-five-diagnostic-reading-001.json; /records/0; /coverage; /lossless_reading_method; /readings; /limits | supports | BGC personally read all ten first-five forms: 372 atom rows and 398 bond rows, including every scalar/string/ring/stereo/motif/map field through exact lossless factoring. No reparse. |
| bgc-2431-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/0; /global_warning_count; /warning_attribution; /method_scope; /interpretation_boundary | supports | ROOT accepted the one original twenty-form diagnostic; this owner’s true comparisons and complete atom-match flag are located. Six global stderr warnings remain unassigned. |
| bgc-2431-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original execution timestamps, exit status, source pin and stdout/stderr pins. |
| bgc-2431-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–430 | supports | The schema distinguishes undefined stereo from fabricated assignments and defines computed classification as named/versioned model output, never a source assertion. |
| bgc-2431-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | The extractor defines stereo_complete through FindMolChiralCenters including unassigned centers; it does not test independent natural truth or complete double-bond geometry. |
| bgc-2431-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Source structure/stereo and classifier arrays are retained with model-based filing. Retention and applicability remain different questions. |
| bgc-2431-source-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-current244-source-reading-001.json; /scope; /reading; /division; /verification; /cautions | supports | BGC personally read nine contexts/81 frames/412 complete positive rows/2854 fields, including these five and four Yossoside companions. Full current raw/history/component carries remain explicitly attributed. |
| bgc-2431-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations | supports | Actual full source scope: BGC 412 rows, Support 18 rows, Native 298 cache stanzas and bounded curation scan. Historical author-time fields stay distinct from later earned acceptances. |
| bgc-2431-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch244/root-source-plan-acceptance-001.json; /status | supports | ROOT accepted the original composed source plan and exact input maps; no source query is replayed. |
| bgc-2431-curation-scope | /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-implemented-curation-scan-001.json; /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions; /assays; /guidance | supports | Ignored-inclusive bounded scan retained 60 lexical hits and found no applicable correction/exclusion. Identity tuples govern applicability; shared AID alone does not exclude an assay. No-exclusion is not identity or protocol validation. |
| bgc-2431-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/41 | supports | Exact retained cached names/synonyms for available source-taxon stanzas. Historical routes, species/strain and producer/occurrence roles remain distinct. |
| bgc-2431-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/source_taxa; /contexts/4/source_scope_inventory/forward_taxon_merge_matches; /contexts/4/source_scope_inventory/nonorganism_matches | supports | Complete saved source-taxon IDs and forwarding/nonorganism routes, including any empty route sets; no fresh taxonomy resolution. |
| bgc-2431-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-cached-taxonomy-reading-001.json; /scope; /taxonomy; /assays; /reading_outputs; /limitations | supports | Native personally read all 298 complete stanzas and retained routes. Five unmatched IDs have saved forward merges. This review carries that attribution without duplicate positive-row credit or fresh taxonomy claims. |
| bgc-2431-direct-contexts | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-target-input-plan-001.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | supports | Exact direct companions and literal predicates; shared BGC membership does not transfer identity, stereo, activity or mechanism. |
| bgc-2431-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/0/path; /contexts/0/identifier; /contexts/0/label; /contexts/0/standard_inchi_key; /contexts/0/owned_bgc_ids; /contexts/1/path; /contexts/1/identifier; /contexts/1/label; /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/2/path; /contexts/2/identifier; /contexts/2/label; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/3/path; /contexts/3/identifier; /contexts/3/label; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids | supports | Distinct full keys and labels remain explicit within direct shared-BGC context. |
| bgc-2431-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame contains 1 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2955–2955; row_sha256 dc607d65465a48639e5340e6f2bd97e61c8d4cb4538c7615a339f3f7f2eb43dd | supports | Exact full-key/version/compound index and source producer/locus/citation-tier fields. BGC complete source-row reading carries. |
| bgc-2431-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame contains 1 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 552–552; row_sha256 7c9fa5370f72412361181666611e63c797f8390ce2006112154bedc4338b7e4a | supports | Exact named/versioned model arrays and glycoside flag; applicability remains separate. BGC complete source-row reading carries. |
| bgc-2431-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| bgc-2431-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame contains 0 placements. Exact predicates, query and complete row fields define its finite scope. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-244/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-244/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-244/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-244/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-244/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only. Fresh primary papers, taxonomy, assay protocols and independent natural identity/stereochemical authentication remain unavailable.
- Full QC and complete OAK coverage remain unavailable. Saved normalized forms, motifs and atom matches do not establish independent full-graph or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain distinct. Shared loci and repeated references do not transfer biological claims or establish independent experiments.
- Model fidelity is separate from applicability; qualified named-family concerns do not establish source-ingestion defects or authorize source replacement.
- No graph, pathway, component-reference or molecular-target root occurs in the complete owner. No maintained-reader result or source status/history change is claimed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five molecular forms: 372 atom rows and 398 bond rows, plus complete scalar/string/ring/stereo/motif/map fields. Indices are zero-based diagnostic indices, not biochemical locants. Six global warnings remain unassigned.
- Disjoint source reading: BGC nine contexts/81 frames/412 rows/2854 fields; Support six contexts/54 frames/18 rows/228 fields. Native read 298 complete cache stanzas and the bounded ignored-inclusive curation scan, with zero positive-source-row credit. Whole raw/history and component reading attribution carries.
- BGC operated the original local collector and composer; Support operated canonical intakes; Native operated the original diagnostic and maintained reader under ROOT delegation. Separate method/dependency/descriptor peers are attributed; fragment authoring invokes no target.
- All five scientific outcomes remain partial; no supported source-edit finding or action is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T192651Z-yossoside-v
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Yossoside V'
started_at: '2026-11-04T18:38:45.542493Z'
finished_at: '2026-11-04T19:26:51.917323Z'
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
summary: Yossoside V retains a consistent exact-key source and stored-form join, with
  three unresolved tetrahedral centers. Its oxygenated-ring and ester topology supports
  a glycoside context, while sugar identity, natural stereochemistry and the named
  model family remain qualified. Producer and locus evidence stay at their retained
  source grades.
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
  - path: data/natural_products/terpenoids/yossoside-i.yaml
    sha256: c6713b478c05ee63949bb427cd6febd92cde60d5504a0df6c02e566656107ae7
    role: context
  - path: data/natural_products/terpenoids/yossoside-ii.yaml
    sha256: e3dca931c852f1781bf2d187ce80b8169bfa56da7c91abbf320950038c115f04
    role: context
  - path: data/natural_products/terpenoids/yossoside-iii.yaml
    sha256: d0623e4ce00c6e96d6b72795619c1ee221555398275e6983aee42cf2b41698aa
    role: context
  - path: data/natural_products/terpenoids/yossoside-iv.yaml
    sha256: 41e425e86f42463c53d7285f1ea7937112cb26700ca674c229e450385125c552
    role: context
  - path: data/natural_products/terpenoids/yossoside-v.yaml
    sha256: f0f1eed9d896500698c0bfc6f2e187ea7d6082ee45f5a751ff2d4bb791a4f48b
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
  selection: Campaign path order 2431; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-928d3a93b2
targets:
- target_id: naturalproductmech:mibig-928d3a93b2
  path: data/natural_products/terpenoids/yossoside-v.yaml
  label: Yossoside V
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
  - naturalproductmech:mibig-928d3a93b2
  command: just validate-strict data/natural_products/terpenoids/yossoside-v.yaml
    data/natural_products/terpenoids/zealexin-a1.yaml data/natural_products/terpenoids/zealexin-b3.yaml
    data/natural_products/terpenoids/zealexin-c2.yaml data/natural_products/terpenoids/zeaxanthin.yaml
    data/natural_products/unclassified/10-epi-3-deoh-hsaf.yaml data/natural_products/unclassified/10-epi-fi-2.yaml
    data/natural_products/unclassified/10-epi-hsaf.yaml data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml
    data/natural_products/unclassified/10-epi-maltophilin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-244/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-928d3a93b2
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-244/validate-all-001.tsv
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
  - naturalproductmech:mibig-928d3a93b2
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
  - naturalproductmech:mibig-928d3a93b2
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
  - naturalproductmech:mibig-928d3a93b2
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-244/review-queue-001.tsv
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
  - naturalproductmech:mibig-928d3a93b2
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2431-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/yossoside-v.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete Yossoside V owner with all 2 history events; MINTED/SEEDED unchanged.
    Prior complete raw/history reading carries.
  snapshot_sha256: f0f1eed9d896500698c0bfc6f2e187ea7d6082ee45f5a751ff2d4bb791a4f48b
- evidence_id: bgc-2431-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Actual complete owner and any ordered component captures, metadata and
    exact root presence; capture fidelity is not independent scientific verification.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/intakes/2431-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Actual target and ownership roles with all 41 current input placements,
    joined to the accepted plan.
  snapshot_sha256: 35180d12a33af9a0b1470b19b53b4a1b8b60adbd337422eb170c06520d2bc9c7
- evidence_id: bgc-2431-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/root-intake-acceptance-001.json
  locator: /status; /summary
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: ROOT accepted ten original canonical intakes; this owner’s complete target/ownership/input
    evidence is linked separately.
  snapshot_sha256: 69a4e9caf203d1856dab3941056fb7e1f009a566d9d557e0c9beb3e805610f86
- evidence_id: bgc-2431-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/source_concepts;
    /records/0/owner_document/grounding_status; /records/0/owner_document/grounding_notes
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact retained identifier, label, structure, source concepts and grounding
    status and grounding notes.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups;
    /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact producer/locus grades, methods, accession and citation tiers, with
    coordinates only where supplied. Native production, strain identity and locus
    evidence remain distinct.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: The complete owner lacks both occurrence roots, bioactivities, bioactivity_summary
    and molecular_targets. This is owner scope, not a biological absence claim.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, pathway filing and
    source classes. Fidelity does not independently establish applicability.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_status; /records/0/owner_document/curation_history
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Every retained history event and SEEDED status remain unchanged.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Whole owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets; no maintained reader applies.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: bgc-2431-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge;
    /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key;
    /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles;
    /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count;
    /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts;
    /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge;
    /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key;
    /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles;
    /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count;
    /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts;
    /records/0/inchi/computed/stereo_counts
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: All ten stored-form comparisons are true with a complete supplied chirality-aware
    match at its stated scope. full_graph_identity_established remains false; natural
    identity is unverified.
  snapshot_sha256: c810c4c63bf70013c7fb4bf8700ed8117add6af2d237e661c258fcd2be909ff2
- evidence_id: bgc-2431-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds;
    /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices;
    /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings;
    /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs;
    /records/0/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: The SMILES table contains four saturated C5O six-membered cycles and a
    separate oxygenated all-carbon six-membered cycle. External oxygen linkages, two
    carboxylic acids and two ester groups are retained; the ester bridges include
    C26–O27–C28 and C56–O55–C54. The all-carbon cycle is not another C5O ring. This
    supports an oxygenated glycosidic context without assigning sugar names, anomers,
    biochemical linkage positions or a natural residue count from the compound label.
  snapshot_sha256: c810c4c63bf70013c7fb4bf8700ed8117add6af2d237e661c258fcd2be909ff2
- evidence_id: bgc-2431-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-current244-first-five-diagnostic-reading-001.json
  locator: /records/0; /coverage; /lossless_reading_method; /readings; /limits
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: 'BGC personally read all ten first-five forms: 372 atom rows and 398 bond
    rows, including every scalar/string/ring/stereo/motif/map field through exact
    lossless factoring. No reparse.'
  snapshot_sha256: 3ae0c3ca3e7572d4ff66849dbfa962fcc98d13f7f2196ceaefba26ce9ee2ba93
- evidence_id: bgc-2431-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/0; /global_warning_count; /warning_attribution;
    /method_scope; /interpretation_boundary
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: ROOT accepted the one original twenty-form diagnostic; this owner’s true
    comparisons and complete atom-match flag are located. Six global stderr warnings
    remain unassigned.
  snapshot_sha256: f8bce250d5b3e962bc2964d58ee8b7bc9aaa1df654eedef5972fcd2bb0cf28ca
- evidence_id: bgc-2431-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact original execution timestamps, exit status, source pin and stdout/stderr
    pins.
  snapshot_sha256: b2711a19d2e5b81af976c5a9ed111e490efe49be1e8633349337f10e211d3b45
- evidence_id: bgc-2431-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–430
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: The schema distinguishes undefined stereo from fabricated assignments and
    defines computed classification as named/versioned model output, never a source
    assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2431-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: The extractor defines stereo_complete through FindMolChiralCenters including
    unassigned centers; it does not test independent natural truth or complete double-bond
    geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2431-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Source structure/stereo and classifier arrays are retained with model-based
    filing. Retention and applicability remain different questions.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2431-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-current244-source-reading-001.json
  locator: /scope; /reading; /division; /verification; /cautions
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: BGC personally read nine contexts/81 frames/412 complete positive rows/2854
    fields, including these five and four Yossoside companions. Full current raw/history/component
    carries remain explicitly attributed.
  snapshot_sha256: bba064bdffddda3c83f7afe7176ac1cbf532a34e6fd78a4793dca59800c8986d
- evidence_id: bgc-2431-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: 'Actual full source scope: BGC 412 rows, Support 18 rows, Native 298 cache
    stanzas and bounded curation scan. Historical author-time fields stay distinct
    from later earned acceptances.'
  snapshot_sha256: d09da1ec6355073c7b1b30869949f4d2602befa1edd7a0df98841b298c80b516
- evidence_id: bgc-2431-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/root-source-plan-acceptance-001.json
  locator: /status
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: ROOT accepted the original composed source plan and exact input maps; no
    source query is replayed.
  snapshot_sha256: 644539ce2aa9af2ccc4419d3516227d61c3e8c05f5fa73d2ac35c5748fbcd9e7
- evidence_id: bgc-2431-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-implemented-curation-scan-001.json
  locator: /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions;
    /assays; /guidance
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Ignored-inclusive bounded scan retained 60 lexical hits and found no applicable
    correction/exclusion. Identity tuples govern applicability; shared AID alone does
    not exclude an assay. No-exclusion is not identity or protocol validation.
  snapshot_sha256: 2cc4f7732f69d5e3697664af9e42b1d14330dca0c1afd999c028f7a47f33b708
  search_scope: Exact current 15-context scan of 745 literal tokens across eight implemented
    tables (93 rows) plus unresolved-taxonomy diagnostics (3329 rows); all 11 TSVs
    enumerated including ignored files, decisions/source_queue excluded from effective
    corrections. Full predicates and hits retained in the cited scope.
- evidence_id: bgc-2431-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/41
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact retained cached names/synonyms for available source-taxon stanzas.
    Historical routes, species/strain and producer/occurrence roles remain distinct.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: bgc-2431-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/source_taxa; /contexts/4/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/4/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved source-taxon IDs and forwarding/nonorganism routes, including
    any empty route sets; no fresh taxonomy resolution.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: bgc-2431-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-cached-taxonomy-reading-001.json
  locator: /scope; /taxonomy; /assays; /reading_outputs; /limitations
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Native personally read all 298 complete stanzas and retained routes. Five
    unmatched IDs have saved forward merges. This review carries that attribution
    without duplicate positive-row credit or fresh taxonomy claims.
  snapshot_sha256: 490df5d6fb436d89d8d181011b8ec2a4c8310aac830b3254df0667330b5d4e61
- evidence_id: bgc-2431-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-target-input-plan-001.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact direct companions and literal predicates; shared BGC membership does
    not transfer identity, stereo, activity or mechanism.
  snapshot_sha256: dccfa62e7ebea5087b254368b8b36da0f0233f06f61fc60a45298ef4983bd85d
- evidence_id: bgc-2431-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/0/path; /contexts/0/identifier; /contexts/0/label; /contexts/0/standard_inchi_key;
    /contexts/0/owned_bgc_ids; /contexts/1/path; /contexts/1/identifier; /contexts/1/label;
    /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/2/path; /contexts/2/identifier;
    /contexts/2/label; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids;
    /contexts/3/path; /contexts/3/identifier; /contexts/3/label; /contexts/3/standard_inchi_key;
    /contexts/3/owned_bgc_ids
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Distinct full keys and labels remain explicit within direct shared-BGC
    context.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: bgc-2431-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved mibig_compounds frame contains 1 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: mibig_compounds, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2955–2955; row_sha256 dc607d65465a48639e5340e6f2bd97e61c8d4cb4538c7615a339f3f7f2eb43dd
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact full-key/version/compound index and source producer/locus/citation-tier
    fields. BGC complete source-row reading carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2431-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved chebi_structures frame contains 0 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: chebi_structures, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved lotus_occurrences frame contains 0 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: lotus_occurrences, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame contains 0 placements. Exact
    predicates, query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: cyanometdb_occurrences, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved npclassifier frame contains 1 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: npclassifier, exact predicate exact
    complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N". All
    matching payloads or the complete empty frame retained; no external lookup or
    query replay.'
- evidence_id: bgc-2431-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 552–552; row_sha256 7c9fa5370f72412361181666611e63c797f8390ce2006112154bedc4338b7e4a
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; applicability remains
    separate. BGC complete source-row reading carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2431-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame contains 0 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: pubchem_bioassay, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved bindingdb_targets frame contains 0 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: bindingdb_targets, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame contains 0 placements. Exact
    predicates, query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: antibioticmech_inchikeys, exact predicate
    exact complete standard_inchi_key equality, query "FJFARKHHKHMNRK-XRNHBKRYSA-N".
    All matching payloads or the complete empty frame retained; no external lookup
    or query replay.'
- evidence_id: bgc-2431-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T19:20:38.074199Z'
  support: supports
  summary: Complete saved chebi_origins frame contains 0 placements. Exact predicates,
    query and complete row fields define its finite scope.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: 'Original saved local inventory: chebi_origins, exact predicate exact
    chebi_id from exact full-key structure rows, query []. All matching payloads or
    the complete empty frame retained; no external lookup or query replay.'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:43:43.930616Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 7bb4ad4e0fc89a85a446b5527c39990074b4b39615edd9f0921661f38f9d769f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:44:08.281786Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: ddb5ae59e1880322ba67c16aed40fe6d92c5c1fa277fbcc27fd28114ab658231
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:44:27.128430Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:45:02.008522Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:45:14.089345Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 8023a9f2ce97c6d100e6a428e98eddc81efb4bc4be6fd5b45fe050798b28612a
assessments:
- assessment_id: bgc-2431-identity
  area: identity
  topic: Exact retained identity and natural-identity limits
  outcome: supported
  summary: The minted record joins MIBiG BGC0002402, version 2, compound 5, by full
    key FJFARKHHKHMNRK-XRNHBKRYSA-N. Both stored forms normalize to neutral C62H96O29
    and that key. The saved exact-key ChEBI join is empty; the grounding note remains
    historical, not a current global absence claim. Yossosides I–IV are distinct-key
    direct companions, so their structures, stereochemistry and activities are not
    transferred to V.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-grounding-owner
  - bgc-2431-chemistry
  - bgc-2431-source-mibig_compounds
  - bgc-2431-query-chebi_structures
  - bgc-2431-direct-contexts
  - bgc-2431-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: FJFARKHHKHMNRK-XRNHBKRYSA-N; exact retained key, not natural identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2431-grounding-owner
    - bgc-2431-chemistry
    - bgc-2431-source-mibig_compounds
    - bgc-2431-query-chebi_structures
    - bgc-2431-direct-contexts
    - bgc-2431-companion-boundaries
  - name: grounding_scope
    value: The minted record joins MIBiG BGC0002402, version 2, compound 5, by full
      key FJFARKHHKHMNRK-XRNHBKRYSA-N. Both stored forms normalize to neutral C62H96O29
      and that key. The saved exact-key ChEBI join is empty; the grounding note remains
      historical, not a current global absence claim. Yossosides I–IV are distinct-key
      direct companions, so their structures, stereochemistry and activities are not
      transferred to V.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2431-grounding-owner
    - bgc-2431-chemistry
    - bgc-2431-source-mibig_compounds
    - bgc-2431-query-chebi_structures
    - bgc-2431-direct-contexts
    - bgc-2431-companion-boundaries
- assessment_id: bgc-2431-representation
  area: representation
  topic: Stored-form and stereochemical scope
  outcome: supported
  summary: Each stored form contains 91 heavy atoms and 100 bonds, with 31 specified
    and three unspecified tetrahedral centers. The false stereo_complete flag is consistent
    with those unresolved positions; in the SMILES table they are atoms 12, 17 and
    63. All ten comparisons are true with a complete supplied chirality-aware atom
    match, while full_graph_identity_established remains false. Agreement does not
    authenticate natural stereochemistry or resolve the question marks in the retained
    InChI.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-grounding-owner
  - bgc-2431-chemistry
  - bgc-2431-topology
  - bgc-2431-diagnostic-reading
  - bgc-2431-diagnostic-acceptance
  - bgc-2431-structure-schema
  - bgc-2431-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Each stored form contains 91 heavy atoms and 100 bonds, with 31 specified
      and three unspecified tetrahedral centers. The false stereo_complete flag is
      consistent with those unresolved positions; in the SMILES table they are atoms
      12, 17 and 63. All ten comparisons are true with a complete supplied chirality-aware
      atom match, while full_graph_identity_established remains false. Agreement does
      not authenticate natural stereochemistry or resolve the question marks in the
      retained InChI.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2431-grounding-owner
    - bgc-2431-chemistry
    - bgc-2431-topology
    - bgc-2431-diagnostic-reading
    - bgc-2431-diagnostic-acceptance
    - bgc-2431-structure-schema
    - bgc-2431-stereo-method
  - name: representation_correspondence
    value: All ten comparisons are true and the supplied atom match is complete at
      its stated scope; full_graph_identity_established remains false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2431-grounding-owner
    - bgc-2431-chemistry
    - bgc-2431-topology
    - bgc-2431-diagnostic-reading
    - bgc-2431-diagnostic-acceptance
    - bgc-2431-structure-schema
    - bgc-2431-stereo-method
- assessment_id: bgc-2431-provenance
  area: provenance
  topic: Distinct producer, locus and taxon assertions
  outcome: supported
  summary: Spinacia oleracea NCBITaxon:3562 is retained as BGC_CHARACTERIZED, separately
    from the CLUSTER_DEMONSTRATED locus KQ150485.1:6311–44201. Knock-out studies and
    heterologous expression are the source locus methods. These database grades do
    not independently authenticate an experimental specimen, construct or native production
    in this review.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-origin-owner
  - bgc-2431-occurrence-owner
  - bgc-2431-source-mibig_compounds
  - bgc-2431-cached-taxonomy
  - bgc-2431-curation-scope
  - bgc-2431-direct-contexts
  dimensions:
  - name: taxon_scope
    value: Spinacia oleracea NCBITaxon:3562 is retained as BGC_CHARACTERIZED, separately
      from the CLUSTER_DEMONSTRATED locus KQ150485.1:6311–44201. Knock-out studies
      and heterologous expression are the source locus methods. These database grades
      do not independently authenticate an experimental specimen, construct or native
      production in this review.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2431-origin-owner
    - bgc-2431-occurrence-owner
    - bgc-2431-source-mibig_compounds
    - bgc-2431-cached-taxonomy
    - bgc-2431-curation-scope
    - bgc-2431-direct-contexts
  - name: producer_evidence
    value: Spinacia oleracea NCBITaxon:3562 is retained as BGC_CHARACTERIZED, separately
      from the CLUSTER_DEMONSTRATED locus KQ150485.1:6311–44201. Knock-out studies
      and heterologous expression are the source locus methods. These database grades
      do not independently authenticate an experimental specimen, construct or native
      production in this review.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2431-origin-owner
    - bgc-2431-occurrence-owner
    - bgc-2431-source-mibig_compounds
    - bgc-2431-cached-taxonomy
    - bgc-2431-curation-scope
    - bgc-2431-direct-contexts
  - name: locus_evidence
    value: Spinacia oleracea NCBITaxon:3562 is retained as BGC_CHARACTERIZED, separately
      from the CLUSTER_DEMONSTRATED locus KQ150485.1:6311–44201. Knock-out studies
      and heterologous expression are the source locus methods. These database grades
      do not independently authenticate an experimental specimen, construct or native
      production in this review.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2431-origin-owner
    - bgc-2431-occurrence-owner
    - bgc-2431-source-mibig_compounds
    - bgc-2431-cached-taxonomy
    - bgc-2431-curation-scope
    - bgc-2431-direct-contexts
- assessment_id: bgc-2431-citations
  area: evidence
  topic: Citation tiers and retained history
  outcome: supported
  summary: DOI:10.1038/s41589-020-0541-x is retained at MIBiG COMPOUND_EVIDENCE level
    and repeated in producer and locus evidence. The two seed-history events document
    regeneration, not two new experiments. The citation is a retained database attribution;
    no primary text, supplementary structure determination or assay protocol was newly
    inspected.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-owner
  - bgc-2431-origin-owner
  - bgc-2431-occurrence-owner
  - bgc-2431-source-mibig_compounds
  - bgc-2431-source-reading
  dimensions:
  - name: citation_scope
    value: DOI:10.1038/s41589-020-0541-x is retained at MIBiG COMPOUND_EVIDENCE level
      and repeated in producer and locus evidence. The two seed-history events document
      regeneration, not two new experiments. The citation is a retained database attribution;
      no primary text, supplementary structure determination or assay protocol was
      newly inspected.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2431-owner
    - bgc-2431-origin-owner
    - bgc-2431-occurrence-owner
    - bgc-2431-source-mibig_compounds
    - bgc-2431-source-reading
- assessment_id: bgc-2431-occurrence
  area: evidence
  topic: Occurrence and assay scope
  outcome: supported
  summary: Both occurrence roots are absent in the complete owner, and the saved LOTUS,
    cyanobacterial and ChEBI-origin frames are empty for their exact predicates. These
    scoped negatives neither establish biological absence nor change the separate
    Spinacia producer/locus assertions.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-occurrence-owner
  - bgc-2431-query-lotus_occurrences
  - bgc-2431-query-chebi_origins
  - bgc-2431-query-cyanometdb_occurrences
  - bgc-2431-query-pubchem_bioassay
  - bgc-2431-query-bindingdb_targets
  - bgc-2431-cached-taxonomy
  - bgc-2431-taxonomy-routes
  - bgc-2431-taxonomy-reading
  - bgc-2431-curation-scope
  dimensions:
  - name: occurrence_scope
    value: Both occurrence roots are absent in the complete owner, and the saved LOTUS,
      cyanobacterial and ChEBI-origin frames are empty for their exact predicates.
      These scoped negatives neither establish biological absence nor change the separate
      Spinacia producer/locus assertions.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2431-occurrence-owner
    - bgc-2431-query-lotus_occurrences
    - bgc-2431-query-chebi_origins
    - bgc-2431-query-cyanometdb_occurrences
    - bgc-2431-query-pubchem_bioassay
    - bgc-2431-query-bindingdb_targets
    - bgc-2431-cached-taxonomy
    - bgc-2431-taxonomy-routes
    - bgc-2431-taxonomy-reading
    - bgc-2431-curation-scope
  - name: assay_target_scope
    value: The complete owner lacks bioactivities, bioactivity_summary and molecular_targets.
      Both retained PubChem assay and BindingDB frames are empty. This is bounded
      local source absence, not evidence of inactivity or absence of published assays.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2431-occurrence-owner
    - bgc-2431-query-lotus_occurrences
    - bgc-2431-query-chebi_origins
    - bgc-2431-query-cyanometdb_occurrences
    - bgc-2431-query-pubchem_bioassay
    - bgc-2431-query-bindingdb_targets
    - bgc-2431-cached-taxonomy
    - bgc-2431-taxonomy-routes
    - bgc-2431-taxonomy-reading
    - bgc-2431-curation-scope
- assessment_id: bgc-2431-classification
  area: consistency
  topic: Model fidelity and family applicability
  outcome: supported
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 supplies Terpenoids/Triterpenoids/Oleanane
    triterpenoids and is_glycoside:true. The oxygenated cycles and external oxygen
    bridges support the glycoside context. Exact Oleanane-family applicability remains
    a model assertion rather than an independent biosynthetic conclusion. Whole C62
    includes attached groups and does not by itself refute a triterpenoid class; MIBiG
    TERPENE remains a separate source assertion.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-classification-owner
  - bgc-2431-source-npclassifier
  - bgc-2431-chemistry
  - bgc-2431-topology
  - bgc-2431-structure-schema
  - bgc-2431-classification-seeder
  - bgc-2431-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 supplies Terpenoids/Triterpenoids/Oleanane
      triterpenoids and is_glycoside:true. The oxygenated cycles and external oxygen
      bridges support the glycoside context. Exact Oleanane-family applicability remains
      a model assertion rather than an independent biosynthetic conclusion. Whole
      C62 includes attached groups and does not by itself refute a triterpenoid class;
      MIBiG TERPENE remains a separate source assertion.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2431-classification-owner
    - bgc-2431-source-npclassifier
    - bgc-2431-chemistry
    - bgc-2431-topology
    - bgc-2431-structure-schema
    - bgc-2431-classification-seeder
    - bgc-2431-source-mibig_compounds
- assessment_id: bgc-2431-completion
  area: completeness
  topic: Actual evidence coverage and remaining limits
  outcome: unknown
  summary: Complete owner/history, canonical intake, retained positive source payloads
    and empty frames, and both original molecular forms have been read. All four mechanism
    roots are absent, so no maintained-mechanism reader applies. The owner remains
    MINTED and SEEDED with 2 unchanged history events. Source seeder/extractor/model
    ownership remains distinct from curator-owned mechanism/history where present.
    The ignored-inclusive bounded curation scan found no applicable correction or
    exclusion. Full QC/OAK, fresh primary, taxonomy, assay/construct verification,
    and independent natural identity/stereochemistry remain unavailable. This is a
    partial review with no supported source-edit finding.
  target_ids:
  - naturalproductmech:mibig-928d3a93b2
  evidence_ids:
  - bgc-2431-owner
  - bgc-2431-capture
  - bgc-2431-intake
  - bgc-2431-intake-acceptance
  - bgc-2431-history-owner
  - bgc-2431-diagnostic-reading
  - bgc-2431-diagnostic-acceptance
  - bgc-2431-diagnostic-execution
  - bgc-2431-source-reading
  - bgc-2431-joint-source-notes
  - bgc-2431-source-plan-acceptance
  - bgc-2431-curation-scope
  - bgc-2431-mechanism-absence
  dimensions:
  - name: review_completion
    value: Complete owner/history, canonical intake, retained positive source payloads
      and empty frames, and both original molecular forms have been read. All four
      mechanism roots are absent, so no maintained-mechanism reader applies. The owner
      remains MINTED and SEEDED with 2 unchanged history events. Source seeder/extractor/model
      ownership remains distinct from curator-owned mechanism/history where present.
      The ignored-inclusive bounded curation scan found no applicable correction or
      exclusion. Full QC/OAK, fresh primary, taxonomy, assay/construct verification,
      and independent natural identity/stereochemistry remain unavailable. This is
      a partial review with no supported source-edit finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2431-owner
    - bgc-2431-capture
    - bgc-2431-intake
    - bgc-2431-intake-acceptance
    - bgc-2431-history-owner
    - bgc-2431-diagnostic-reading
    - bgc-2431-diagnostic-acceptance
    - bgc-2431-diagnostic-execution
    - bgc-2431-source-reading
    - bgc-2431-joint-source-notes
    - bgc-2431-source-plan-acceptance
    - bgc-2431-curation-scope
    - bgc-2431-mechanism-absence
findings: []
actions: []
limitations:
- Retained local evidence only. Fresh primary papers, taxonomy, assay protocols and
  independent natural identity/stereochemical authentication remain unavailable.
- Full QC and complete OAK coverage remain unavailable. Saved normalized forms, motifs
  and atom matches do not establish independent full-graph or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain distinct. Shared loci
  and repeated references do not transfer biological claims or establish independent
  experiments.
- Model fidelity is separate from applicability; qualified named-family concerns do
  not establish source-ingestion defects or authorize source replacement.
- No graph, pathway, component-reference or molecular-target root occurs in the complete
  owner. No maintained-reader result or source status/history change is claimed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read all ten first-five molecular forms: 372 atom rows and 398 bond
  rows, plus complete scalar/string/ring/stereo/motif/map fields. Indices are zero-based
  diagnostic indices, not biochemical locants. Six global warnings remain unassigned.'
- 'Disjoint source reading: BGC nine contexts/81 frames/412 rows/2854 fields; Support
  six contexts/54 frames/18 rows/228 fields. Native read 298 complete cache stanzas
  and the bounded ignored-inclusive curation scan, with zero positive-source-row credit.
  Whole raw/history and component reading attribution carries.'
- BGC operated the original local collector and composer; Support operated canonical
  intakes; Native operated the original diagnostic and maintained reader under ROOT
  delegation. Separate method/dependency/descriptor peers are attributed; fragment
  authoring invokes no target.
- All five scientific outcomes remain partial; no supported source-edit finding or
  action is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-244
```
