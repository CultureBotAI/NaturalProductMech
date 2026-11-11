# Local evidence review: 6-hydroxymellein

- Review: 20261103T080908Z-6-hydroxymellein
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T07:43:36.013448Z
- Finished UTC: 2026-11-03T08:09:08.460300Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The retained MIBiG structure and exact-key ChEBI row identify the local CHEBI:16368 6-hydroxymellein concept, DHLPMLVSBRRUGA-RXMQYKEDSA-N. The ChEBI definition specifies mellein with an additional hydroxyl at position 6. PubChem:172675 is a retained xref, not a freshly resolved authority. The supplemental taxonomy snapshot leaves this owner and its original molecular evidence unchanged. Both saved forms give neutral C10H10O4, 14 atoms and 15 bonds, with all ten comparisons true. Complete rows show an aromatic six-membered ring fused to a six-membered lactone ring, two phenolic OH groups and one specified R tetrahedral center (SMILES C1; InChI-form C4). The stored true stereo flag agrees locally, without proving the natural absolute configuration from primary evidence. Local evidence supports a qualified partial review within the stated limits; no confirmed actionable defect is established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2174; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:16368 | data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml | generated | 6-hydroxymellein |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | CHEBI:16368 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | CHEBI:16368 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | CHEBI:16368 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | CHEBI:16368 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | CHEBI:16368 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | CHEBI:16368 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | CHEBI:16368 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | CHEBI:16368 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: CHEBI:16368.

The retained MIBiG structure and exact-key ChEBI row identify the local CHEBI:16368 6-hydroxymellein concept, DHLPMLVSBRRUGA-RXMQYKEDSA-N. The ChEBI definition specifies mellein with an additional hydroxyl at position 6. PubChem:172675 is a retained xref, not a freshly resolved authority. The supplemental taxonomy snapshot leaves this owner and its original molecular evidence unchanged.

### Representation

representation: supported. Targets: CHEBI:16368.

Both saved forms give neutral C10H10O4, 14 atoms and 15 bonds, with all ten comparisons true. Complete rows show an aromatic six-membered ring fused to a six-membered lactone ring, two phenolic OH groups and one specified R tetrahedral center (SMILES C1; InChI-form C4). The stored true stereo flag agrees locally, without proving the natural absolute configuration from primary evidence.

### Origin

provenance: supported. Targets: CHEBI:16368.

Cladonia uncialis subsp. uncialis NCBITaxon:180999 remains a SOURCE_ASSERTION producer for BGC0001489 v3, with PKS class and CLUSTER_UNSTATED locus evidence. Thirteen LOTUS occurrences are separate source assertions. The MOLLUSK facet is reproduced from retained NCBITaxon:2109287 after the recorded 1582468 merge; the name-only Discula cache does not establish whether the intended organism/homonym was grounded correctly. The other retained facets likewise remain source mappings, not fresh lineage verification.

### Citations

evidence: supported. Targets: CHEBI:16368.

The locus citation DOI:10.1016/j.bfopcu.2017.03.001 is explicitly taken from compound bioactivity evidence in MIBiG. That role is not a newly inspected assay or a producer experiment. Thirteen LOTUS rows retain their individual citations; repeated DOI/taxon strings and taxonomic synonyms do not prove publication independence. None of the underlying articles was fetched.

### Bioactivity

evidence: supported. Targets: CHEBI:16368.

This owner has no written bioactivities, bioactivity_summary or molecular_targets. Its exact retained PubChem, BindingDB and AntibioticMech queries are empty. The COMPOUND_BIOACTIVITY citation role cannot be converted into a measured endpoint, and the occurrence list is not evidence for demonstrated production or activity. No inactivity claim follows.

### Classification

consistency: supported. Targets: CHEBI:16368.

NPClassifier predicts Coumarins / Isocoumarins under Shikimates and Phenylpropanoids, while MIBiG retains a PKS locus class. Saved fused-lactone topology supports the narrow structural applicability of an isocoumarin description; these two source axes do not establish biosynthetic origin. The admitted supplemental taxon_groups/seeder evidence explains the displayed MOLLUSK facet internally but cannot resolve the biological identity behind the Discula taxon mapping.

### Completion

completeness: supported. Targets: CHEBI:16368.

Complete local whole-owner/source and both saved molecular forms were reviewed with claim-level limits. Five native checks passed; full QC/OAK and external primary, xref and taxonomy verification remain unavailable. No confirmed actionable defect is established by these bounded inputs. The retained 1582468→2109287 merge and MOLLUSK table assignment are internally traceable, but local name-only Discula cache evidence cannot confirm or refute the intended organism. No unsupported facet or homonym defect is asserted. The appropriate completion is partial and the local verdict is qualified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2174-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml; Whole current owner and complete curation_history | supports | Complete plaintext owner and all 2 history events personally read. This evidence identifies the preserved written content; no record edit or new YAML parse. |
| bgc-2174-capture | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document | supports | Complete actual captured owner preserves all written structure, grounding, source, occurrence, classification and history fields. |
| bgc-2174-intake | /private/tmp/npm-review-work/shared-next-batch218/intakes/2174-inspect-002.json; /targets/0; /source/inputs | supports | Actual supplemental canonical inspection records this exact target, its maintained-owner attribution, and 39 source inputs including taxon_groups.tsv. Comparison with the original snapshot is separately supported by the ROOT supplemental acceptance. |
| bgc-2174-source-plan | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3 | supports | Complete selected raw/history/source copy and all nine saved query frames with their full positive payloads. Admission uses exact root ID/full key/direct owned BGC scope, without name or recursive expansion. |
| bgc-2174-grounding-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status; /records/3/owner_document/definition; /records/3/owner_document/definition_source; /records/3/owner_document/xrefs | supports | Literal structure, source-concept and grounding fields, including retained definitions/xrefs/notes where written. This snapshot alone does not verify external identity. |
| bgc-2174-origin-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/bgc_class | supports | Complete written producer and locus objects, including grades, methods, accessions, coordinates where present, and attached evidence roles. |
| bgc-2174-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document/occurrences; /records/3/owner_document/occurrence_taxon_groups | supports | All 13 written occurrence objects and literal occurrence_taxon_groups, preserving attached citations, notes and the displayed scope. This snapshot does not independently verify lineage or source identity. |
| bgc-2174-citation-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document/source_concepts; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/occurrences; /records/3/owner_document/curation_history | supports | Complete written source-concept, locus and occurrence citations plus history are retained in their original claim roles, without a primary-source refresh. |
| bgc-2174-classification-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class; /records/3/owner_document/np_pathway; /records/3/owner_document/biosynthesis_origin | supports | Literal retained classification: {"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":["Shikimates and Phenylpropanoids"],"superclass_results":["Coumarins"],"class_results":["Isocoumarins"],"is_glycoside":false}; source bgc_class=["PKS"]. Computed labels and source classes are distinct assertions. |
| bgc-2174-assay-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/3/owner_document | partial | The complete captured owner has no written bioactivities, bioactivity_summary or molecular_targets. This bounded owner observation does not establish inactivity. |
| bgc-2174-chemistry | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/3/declared_structure; /records/3/smiles/computed; /records/3/inchi/computed; /records/3/comparisons; /records/3/atom_correspondence | partial | Saved paired forms: C10H10O4, formal charge 0, 14 atoms/15 bonds in each; SMILES stereo {"Atom_Tetrahedral:Specified":1}, InChI-form stereo {"Atom_Tetrahedral:Specified":1}. All ten comparisons are true; full_graph_identity_established remains false. The written stereo_complete=true is preserved. No natural-identity or primary stereochemical proof is inferred. |
| bgc-2174-topology | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/3/smiles/computed/atoms; /records/3/smiles/computed/bonds; /records/3/smiles/computed/rings; /records/3/smiles/computed/potential_stereo; /records/3/smiles/computed/motifs; /records/3/inchi/computed/atoms; /records/3/inchi/computed/bonds; /records/3/inchi/computed/rings; /records/3/inchi/computed/potential_stereo; /records/3/inchi/computed/motifs | supports | The complete saved graphs contain a fused benzene/lactone system, two phenolic hydroxyls and a methyl substituent. SMILES lactone C9-O11-C1 belongs to the oxygen-containing ring; the aromatic ring and ester linkage support a bounded dihydroisocoumarin description. No saturated C5O sugar candidate is reported. |
| bgc-2174-diagnostic-root | /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json; / | partial | ROOT accepts the one saved diagnostic execution and its integrity evidence: 20 forms parsed, all 100 comparison flags true, and two global undefined-stereo warnings remain unassigned. This does not supply a per-record warning attribution or scientific verdict. |
| bgc-2174-native-root | /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json; / | partial | ROOT accepts the five original passed native checks while full QC/OAK remain unavailable. Local validation/reproduction does not establish scientific accuracy; unavailable checks remain explicit. |
| bgc-2174-plan-root | /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json; / | supports | ROOT accepts the original source plan with 392 source placements/67 paths and its exact original ten-intake join. It is historical provenance and does not incorporate the later 2174 supplemental taxonomy input. |
| bgc-2174-intake-root | /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json; / | supports | ROOT accepts all ten original canonical intakes and exact original 392/67 maps. The later 2174 supplemental snapshot is separately cited rather than substituted into this historical acceptance. |
| bgc-2174-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/mibig_compounds | supports | Exact saved mibig_compounds predicate/query and 1 complete matching payload. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical TSV lines 1802 | supports | Complete exact full-key MIBiG payloads preserve compound structures, source concepts, producer/locus evidence grades and citation roles; retained database assertions are not refreshed primary experiments. |
| bgc-2174-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/chebi_structures | supports | Exact saved chebi_structures predicate/query and 1 complete matching payload. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; physical TSV lines 3110 | supports | Complete exact full-key ChEBI payloads preserve the distinct identifiers, names and definitions in the retained crosswalk; equal keys do not make differently scoped concepts interchangeable. |
| bgc-2174-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/lotus_occurrences | supports | Exact saved lotus_occurrences predicate/query and 13 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical TSV lines 1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087 | supports | Complete exact full-key LOTUS payloads retain each taxon, name and citation assertion. These are occurrence records, not a count of independent producer experiments. |
| bgc-2174-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/cyanometdb_occurrences | partial | Exact saved cyanometdb_occurrences predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/npclassifier | supports | Exact saved npclassifier predicate/query and 1 complete matching payload. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical TSV lines 416 | supports | Exact full-key NPClassifier payload preserves predicted pathway, superclass, class and glycoside fields with retained version; it is computed classification, not direct biosynthetic evidence. |
| bgc-2174-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/pubchem_bioassay | partial | Exact saved pubchem_bioassay predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/bindingdb_targets | partial | Exact saved bindingdb_targets predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/antibioticmech_inchikeys | partial | Exact saved antibioticmech_inchikeys predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/joins/chebi_origins | partial | Exact saved chebi_origins predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2174-taxonomy-cache | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/16; /cached_taxonomy/whole_stanzas/27; /cached_taxonomy/whole_stanzas/37; /cached_taxonomy/whole_stanzas/38; /cached_taxonomy/whole_stanzas/50; /cached_taxonomy/whole_stanzas/51; /cached_taxonomy/whole_stanzas/52; /cached_taxonomy/whole_stanzas/60; /cached_taxonomy/whole_stanzas/64; /cached_taxonomy/whole_stanzas/65 | partial | Complete retained cached stanzas for this selected source-taxon scope: NCBITaxon:1883, NCBITaxon:33178, NCBITaxon:78140, NCBITaxon:180101, NCBITaxon:180999, NCBITaxon:346999, NCBITaxon:397620, NCBITaxon:429701, NCBITaxon:1194331, NCBITaxon:2109287, NCBITaxon:2137241. Names and synonyms remain saved cache assertions; they do not prove ancestry, intended homonym, cultivation or publication independence. |
| bgc-2174-taxon-routes | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/3/source_scope_inventory/forward_taxon_merge_matches; /records/3/source_scope_inventory/nonorganism_matches | supports | Exact saved forward taxon-merge frames and nonorganism query result. Original and replacement identifiers remain distinct provenance; this is not new external taxonomy verification. |
| bgc-2174-source-taxon_merged | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; physical TSV lines 310,496 | partial | Complete retained old-ID to replacement-ID mappings for this owner. The mappings do not independently establish biological identity or lineage. |
| bgc-2174-taxonomy-supplement | /private/tmp/npm-review-work/shared-next-batch218/root-current218-2174-taxon-group-evidence-001.json; /query; /matches; /unmatched_ids; /maintained_source_spans; /stored_occurrence_groups; /stored_occurrence_taxa; /scope | partial | The admitted supplemental trace contains 11 exact taxon-group rows for 13 selected source/replacement IDs, with the two old merged IDs unmatched. NCBITaxon:2109287 alone maps MOLLUSK; the seeder derives facets from these nested IDs. Intended Discula organism/homonym correctness is not established. |
| bgc-2174-source-taxon_groups | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_groups.tsv; physical TSV lines 450,2773,7032,12244,12311,17718,18958,19509,25800,30993,31027 | partial | Complete 11 retained exact-ID taxon-group rows; physical 30993 assigns NCBITaxon:2109287 to MOLLUSK. These table assignments do not independently prove intended organism identity or current lineage. |
| bgc-2174-facet-owner | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 271-282; 862-873; 1296-1311; 1478-1490 | supports | Maintained seeder text looks up taxon_groups by nested taxon_id and emits the deduplicated display facets. No seeder module was invoked; lineage correctness is outside this implementation observation. |
| bgc-2174-original-intake | /private/tmp/npm-review-work/shared-next-batch218/root-current218-2174-supplemental-intake-acceptance-001.json; /original_intake; /intake; /added_input; /unchanged_original_owner_and_inputs; /scope | supports | ROOT accepts the supplemental 39-input 2174 snapshot, records its exact original 38-input predecessor and added taxon_groups context, and confirms unchanged original owner/inputs. The original diagnostic/gate provenance is explicitly preserved. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-218/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-218/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-218/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-218/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-218/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-218/native-current218-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Zero outbound: primary papers, database xrefs and taxonomy authorities were not fetched or refreshed.
- Full QC and ontology/OAK are unavailable; local validation and reproduction are not scientific proof.
- Saved full_graph_identity_established remains false; normalized equality is not independent natural-identity or exhaustive stereo proof.
- The two original undefined-stereo warnings are global and unassigned; no per-owner warning attribution.
- Computed classes, bounded empty queries and local motifs do not independently establish biosynthesis, glycosylation, activity or inactivity.
- The retained 1582468→2109287 merge and MOLLUSK table assignment are internally traceable, but local name-only Discula cache evidence cannot confirm or refute the intended organism. No unsupported facet or homonym defect is asserted.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read every selected raw/history and current capture, all nine saved selected query frames and full positive source payloads, and every atom/bond/ring/stereo/motif/scalar/map field in both assigned saved forms. No new source-query, YAML or molecular execution. Source collector/composer and first-five review authorship overlap is explicit.
- Current direct-context reading: seven BGC2167 bodies/histories personally read; current BGC2290 scope carries ten exact-pinned ROOT prior whole companion reads and one prior-selected/current-companion body personally read. These scopes were rejoined to current bytes and are not claimed to be an identical old eleven-member set.
- The assigned 112 complete source-row payloads/207 query frames were personally read and physically rejoined. Support independently read the complementary 70 rows/45 frames and 22 cached stanzas; BGC read the remaining 45 cached stanzas. Local curation absence is not used as a first-five scientific claim, and the supplemental PubChem exclusion table is not imported into these targets.
- ROOT executed/accepted the original diagnostic; Native provided saved-result integrity review. This author independently interpreted complete saved forms. Native gates are represented by their actual accepted receipts, with unavailable QC/OAK preserved.
- No source record, native status, history, Git or LIVE mutation; no assembly/canonical/reader invocation or outbound active, queued, scheduled or retrying under this author.
- ROOT separately captured the supplemental 39-input intake and exact taxon-group table/seeder trace; BGC wholly read that trace ee9afd and the intake owner-path delta29e2ae. Original 38-input plan/intake/diagnostic remain unchanged historical evidence. The supplemental table explains the displayed facet but cannot confirm or refute the intended Discula homonym.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T080908Z-6-hydroxymellein
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 6-hydroxymellein'
started_at: '2026-11-03T07:43:36.013448Z'
finished_at: '2026-11-03T08:09:08.460300Z'
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
summary: The retained MIBiG structure and exact-key ChEBI row identify the local CHEBI:16368
  6-hydroxymellein concept, DHLPMLVSBRRUGA-RXMQYKEDSA-N. The ChEBI definition specifies
  mellein with an additional hydroxyl at position 6. PubChem:172675 is a retained
  xref, not a freshly resolved authority. The supplemental taxonomy snapshot leaves
  this owner and its original molecular evidence unchanged. Both saved forms give
  neutral C10H10O4, 14 atoms and 15 bonds, with all ten comparisons true. Complete
  rows show an aromatic six-membered ring fused to a six-membered lactone ring, two
  phenolic OH groups and one specified R tetrahedral center (SMILES C1; InChI-form
  C4). The stored true stereo flag agrees locally, without proving the natural absolute
  configuration from primary evidence. Local evidence supports a qualified partial
  review within the stated limits; no confirmed actionable defect is established.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml
    sha256: 7cb1d4966cb1ea308c982eb486fa78eea1125bf8f3673b2ad856ff74f3bc0391
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
  - path: data/raw/taxon_groups.tsv
    sha256: f73f228d57d79a1d85a1441efa6829917b1ffecac08cb7bdd4fc855046255f8f
    role: context
  - path: data/raw/taxon_merged.tsv
    sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
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
  selection: Campaign path order 2174; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:16368
targets:
- target_id: CHEBI:16368
  path: data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml
  label: 6-hydroxymellein
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
    path: data/raw/chebi_structures.tsv
    role: Retained ChEBI identifiers, definitions and exact chemical forms.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Retained cited occurrence assertions, distinct from demonstrated production.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_merged.tsv
    role: Exact retained selected/direct taxon decision; no fresh authority.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_groups.tsv
    role: Retained taxonomic group assignments used by the maintained seeder for occurrence/producer
      facets; no fresh taxonomy verification.
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
  - CHEBI:16368
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
  - CHEBI:16368
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
  - CHEBI:16368
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
  - CHEBI:16368
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
  - CHEBI:16368
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
  - CHEBI:16368
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - CHEBI:16368
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - CHEBI:16368
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2174-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/6-hydroxymellein.yaml
  locator: Whole current owner and complete curation_history
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete plaintext owner and all 2 history events personally read. This
    evidence identifies the preserved written content; no record edit or new YAML
    parse.
  snapshot_sha256: 7cb1d4966cb1ea308c982eb486fa78eea1125bf8f3673b2ad856ff74f3bc0391
- evidence_id: bgc-2174-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete actual captured owner preserves all written structure, grounding,
    source, occurrence, classification and history fields.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2174-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/intakes/2174-inspect-002.json
  locator: /targets/0; /source/inputs
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Actual supplemental canonical inspection records this exact target, its
    maintained-owner attribution, and 39 source inputs including taxon_groups.tsv.
    Comparison with the original snapshot is separately supported by the ROOT supplemental
    acceptance.
  snapshot_sha256: 1132a0953387134bbc3c57c2fbe86bb9002aa566f5fd948523faaf60d9418948
- evidence_id: bgc-2174-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete selected raw/history/source copy and all nine saved query frames
    with their full positive payloads. Admission uses exact root ID/full key/direct
    owned BGC scope, without name or recursive expansion.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: bgc-2174-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts;
    /records/3/owner_document/grounding_status; /records/3/owner_document/definition;
    /records/3/owner_document/definition_source; /records/3/owner_document/xrefs
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Literal structure, source-concept and grounding fields, including retained
    definitions/xrefs/notes where written. This snapshot alone does not verify external
    identity.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2174-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters;
    /records/3/owner_document/bgc_class
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete written producer and locus objects, including grades, methods,
    accessions, coordinates where present, and attached evidence roles.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2174-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document/occurrences; /records/3/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: All 13 written occurrence objects and literal occurrence_taxon_groups,
    preserving attached citations, notes and the displayed scope. This snapshot does
    not independently verify lineage or source identity.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2174-citation-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document/source_concepts; /records/3/owner_document/biosynthetic_gene_clusters;
    /records/3/owner_document/occurrences; /records/3/owner_document/curation_history
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete written source-concept, locus and occurrence citations plus history
    are retained in their original claim roles, without a primary-source refresh.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2174-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class;
    /records/3/owner_document/np_pathway; /records/3/owner_document/biosynthesis_origin
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: 'Literal retained classification: {"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":["Shikimates
    and Phenylpropanoids"],"superclass_results":["Coumarins"],"class_results":["Isocoumarins"],"is_glycoside":false};
    source bgc_class=["PKS"]. Computed labels and source classes are distinct assertions.'
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2174-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/3/owner_document
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: The complete captured owner has no written bioactivities, bioactivity_summary
    or molecular_targets. This bounded owner observation does not establish inactivity.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
  search_scope: Complete saved selected owner only; no external or congener absence
    inference.
- evidence_id: bgc-2174-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/declared_structure; /records/3/smiles/computed; /records/3/inchi/computed;
    /records/3/comparisons; /records/3/atom_correspondence
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: 'Saved paired forms: C10H10O4, formal charge 0, 14 atoms/15 bonds in each;
    SMILES stereo {"Atom_Tetrahedral:Specified":1}, InChI-form stereo {"Atom_Tetrahedral:Specified":1}.
    All ten comparisons are true; full_graph_identity_established remains false. The
    written stereo_complete=true is preserved. No natural-identity or primary stereochemical
    proof is inferred.'
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: bgc-2174-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3/smiles/computed/atoms; /records/3/smiles/computed/bonds; /records/3/smiles/computed/rings;
    /records/3/smiles/computed/potential_stereo; /records/3/smiles/computed/motifs;
    /records/3/inchi/computed/atoms; /records/3/inchi/computed/bonds; /records/3/inchi/computed/rings;
    /records/3/inchi/computed/potential_stereo; /records/3/inchi/computed/motifs
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: The complete saved graphs contain a fused benzene/lactone system, two phenolic
    hydroxyls and a methyl substituent. SMILES lactone C9-O11-C1 belongs to the oxygen-containing
    ring; the aromatic ring and ester linkage support a bounded dihydroisocoumarin
    description. No saturated C5O sugar candidate is reported.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: bgc-2174-diagnostic-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: 'ROOT accepts the one saved diagnostic execution and its integrity evidence:
    20 forms parsed, all 100 comparison flags true, and two global undefined-stereo
    warnings remain unassigned. This does not supply a per-record warning attribution
    or scientific verdict.'
  snapshot_sha256: 0f1c218ef2948f88c16e3ae0c830644e13e2d397ea05a9e4604a715e8da98443
- evidence_id: bgc-2174-native-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: ROOT accepts the five original passed native checks while full QC/OAK remain
    unavailable. Local validation/reproduction does not establish scientific accuracy;
    unavailable checks remain explicit.
  snapshot_sha256: 57138741c14dfd03efcb91097dad031f0dc2209cb36d90f08c3b8796ae6f17b5
- evidence_id: bgc-2174-plan-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: ROOT accepts the original source plan with 392 source placements/67 paths
    and its exact original ten-intake join. It is historical provenance and does not
    incorporate the later 2174 supplemental taxonomy input.
  snapshot_sha256: 938383f6b986f11823252b0a936784870aac1edd32b51ca4eea8c01b059af7ed
- evidence_id: bgc-2174-intake-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes and exact original 392/67
    maps. The later 2174 supplemental snapshot is separately cited rather than substituted
    into this historical acceptance.
  snapshot_sha256: 4d19c500387ec2c243eb986a2e00c596a04a9fa2e4f1879d15165d0fcd2ac0cd
- evidence_id: bgc-2174-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved mibig_compounds predicate/query and 1 complete matching payload.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained mibig_compounds only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical TSV lines 1802
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete exact full-key MIBiG payloads preserve compound structures, source
    concepts, producer/locus evidence grades and citation roles; retained database
    assertions are not refreshed primary experiments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2174-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved chebi_structures predicate/query and 1 complete matching payload.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained chebi_structures only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: physical TSV lines 3110
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete exact full-key ChEBI payloads preserve the distinct identifiers,
    names and definitions in the retained crosswalk; equal keys do not make differently
    scoped concepts interchangeable.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2174-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved lotus_occurrences predicate/query and 13 complete matching
    payloads. Empty results are bounded to this retained inventory and exact selector,
    not a global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained lotus_occurrences only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical TSV lines 1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete exact full-key LOTUS payloads retain each taxon, name and citation
    assertion. These are occurrence records, not a count of independent producer experiments.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2174-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved cyanometdb_occurrences predicate/query and 0 complete matching
    payloads. Empty results are bounded to this retained inventory and exact selector,
    not a global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained cyanometdb_occurrences only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved npclassifier predicate/query and 1 complete matching payload.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained npclassifier only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical TSV lines 416
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact full-key NPClassifier payload preserves predicted pathway, superclass,
    class and glycoside fields with retained version; it is computed classification,
    not direct biosynthetic evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2174-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved pubchem_bioassay predicate/query and 0 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained pubchem_bioassay only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved bindingdb_targets predicate/query and 0 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained bindingdb_targets only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved antibioticmech_inchikeys predicate/query and 0 complete matching
    payloads. Empty results are bounded to this retained inventory and exact selector,
    not a global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained antibioticmech_inchikeys only; exact complete standard_inchi_key
    equality; query="DHLPMLVSBRRUGA-RXMQYKEDSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2174-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved chebi_origins predicate/query and 0 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained chebi_origins only; exact chebi_id from exact full-key
    structure rows; query=["CHEBI:16368"]; no name, first-block or recursive expansion.
- evidence_id: bgc-2174-taxonomy-cache
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/2; /cached_taxonomy/whole_stanzas/16; /cached_taxonomy/whole_stanzas/27;
    /cached_taxonomy/whole_stanzas/37; /cached_taxonomy/whole_stanzas/38; /cached_taxonomy/whole_stanzas/50;
    /cached_taxonomy/whole_stanzas/51; /cached_taxonomy/whole_stanzas/52; /cached_taxonomy/whole_stanzas/60;
    /cached_taxonomy/whole_stanzas/64; /cached_taxonomy/whole_stanzas/65
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: 'Complete retained cached stanzas for this selected source-taxon scope:
    NCBITaxon:1883, NCBITaxon:33178, NCBITaxon:78140, NCBITaxon:180101, NCBITaxon:180999,
    NCBITaxon:346999, NCBITaxon:397620, NCBITaxon:429701, NCBITaxon:1194331, NCBITaxon:2109287,
    NCBITaxon:2137241. Names and synonyms remain saved cache assertions; they do not
    prove ancestry, intended homonym, cultivation or publication independence.'
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: bgc-2174-taxon-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/3/source_scope_inventory/forward_taxon_merge_matches; /records/3/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved forward taxon-merge frames and nonorganism query result. Original
    and replacement identifiers remain distinct provenance; this is not new external
    taxonomy verification.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: bgc-2174-source-taxon_merged
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv
  locator: physical TSV lines 310,496
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Complete retained old-ID to replacement-ID mappings for this owner. The
    mappings do not independently establish biological identity or lineage.
  snapshot_sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
- evidence_id: bgc-2174-taxonomy-supplement
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-current218-2174-taxon-group-evidence-001.json
  locator: /query; /matches; /unmatched_ids; /maintained_source_spans; /stored_occurrence_groups;
    /stored_occurrence_taxa; /scope
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: The admitted supplemental trace contains 11 exact taxon-group rows for
    13 selected source/replacement IDs, with the two old merged IDs unmatched. NCBITaxon:2109287
    alone maps MOLLUSK; the seeder derives facets from these nested IDs. Intended
    Discula organism/homonym correctness is not established.
  snapshot_sha256: 16724b70d2360fcb6b7c5c001854c22d13cca21698b70f2f7fefe03bbaf7395c
- evidence_id: bgc-2174-source-taxon_groups
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_groups.tsv
  locator: physical TSV lines 450,2773,7032,12244,12311,17718,18958,19509,25800,30993,31027
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Complete 11 retained exact-ID taxon-group rows; physical 30993 assigns
    NCBITaxon:2109287 to MOLLUSK. These table assignments do not independently prove
    intended organism identity or current lineage.
  snapshot_sha256: f73f228d57d79a1d85a1441efa6829917b1ffecac08cb7bdd4fc855046255f8f
- evidence_id: bgc-2174-facet-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 271-282; 862-873; 1296-1311; 1478-1490
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Maintained seeder text looks up taxon_groups by nested taxon_id and emits
    the deduplicated display facets. No seeder module was invoked; lineage correctness
    is outside this implementation observation.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2174-original-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-current218-2174-supplemental-intake-acceptance-001.json
  locator: /original_intake; /intake; /added_input; /unchanged_original_owner_and_inputs;
    /scope
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: ROOT accepts the supplemental 39-input 2174 snapshot, records its exact
    original 38-input predecessor and added taxon_groups context, and confirms unchanged
    original owner/inputs. The original diagnostic/gate provenance is explicitly preserved.
  snapshot_sha256: b5d028c5d9f04aa81266c11ad07e260efb6b6234abcef8642381bd72ca901870
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
- assessment_id: bgc-2174-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The retained MIBiG structure and exact-key ChEBI row identify the local
    CHEBI:16368 6-hydroxymellein concept, DHLPMLVSBRRUGA-RXMQYKEDSA-N. The ChEBI definition
    specifies mellein with an additional hydroxyl at position 6. PubChem:172675 is
    a retained xref, not a freshly resolved authority. The supplemental taxonomy snapshot
    leaves this owner and its original molecular evidence unchanged.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-owner
  - bgc-2174-capture
  - bgc-2174-intake
  - bgc-2174-grounding-owner
  - bgc-2174-source-plan
  - bgc-2174-query-chebi_structures
  - bgc-2174-chemistry
  - bgc-2174-source-mibig_compounds
  - bgc-2174-source-chebi_structures
  dimensions:
  - name: standard_inchi_key
    value: DHLPMLVSBRRUGA-RXMQYKEDSA-N
    definition: Exact complete key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2174-owner
    - bgc-2174-capture
    - bgc-2174-intake
    - bgc-2174-grounding-owner
    - bgc-2174-source-plan
    - bgc-2174-query-chebi_structures
    - bgc-2174-chemistry
    - bgc-2174-source-mibig_compounds
    - bgc-2174-source-chebi_structures
  - name: grounding_scope
    value: EXACT CHEBI:16368 in the retained local crosswalk; pubchem:172675 unrefreshed.
      This is not independent natural-identity confirmation.
    definition: Local grounding fidelity and unresolved concept scope are separated
      from natural-identity verification.
    evidence_ids:
    - bgc-2174-owner
    - bgc-2174-capture
    - bgc-2174-intake
    - bgc-2174-grounding-owner
    - bgc-2174-source-plan
    - bgc-2174-query-chebi_structures
    - bgc-2174-chemistry
    - bgc-2174-source-mibig_compounds
    - bgc-2174-source-chebi_structures
- assessment_id: bgc-2174-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both saved forms give neutral C10H10O4, 14 atoms and 15 bonds, with all
    ten comparisons true. Complete rows show an aromatic six-membered ring fused to
    a six-membered lactone ring, two phenolic OH groups and one specified R tetrahedral
    center (SMILES C1; InChI-form C4). The stored true stereo flag agrees locally,
    without proving the natural absolute configuration from primary evidence.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-chemistry
  - bgc-2174-topology
  - bgc-2174-diagnostic-root
  - bgc-2174-grounding-owner
  dimensions:
  - name: stereochemistry_scope
    value: One specified R tetrahedral center in each saved form; stored stereo_complete=true.
      Natural absolute configuration was not freshly verified.
    definition: Interpretation of complete saved stereo/atom/bond tables, not a new
      parse or primary assignment.
    evidence_ids:
    - bgc-2174-chemistry
    - bgc-2174-topology
    - bgc-2174-diagnostic-root
    - bgc-2174-grounding-owner
  - name: representation_correspondence
    value: All ten saved comparison flags true; full_graph_identity_established=false.
      The complete saved graphs contain a fused benzene/lactone system, two phenolic
      hydroxyls and a methyl substituent. SMILES lactone C9-O11-C1 belongs to the
      oxygen-containing ring; the aromatic ring and ester linkage support a bounded
      dihydroisocoumarin description. No saturated C5O sugar candidate is reported.
    definition: Representation agreement is bounded to the saved computational result;
      topology does not prove natural identity.
    evidence_ids:
    - bgc-2174-chemistry
    - bgc-2174-topology
    - bgc-2174-diagnostic-root
    - bgc-2174-grounding-owner
- assessment_id: bgc-2174-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Cladonia uncialis subsp. uncialis NCBITaxon:180999 remains a SOURCE_ASSERTION
    producer for BGC0001489 v3, with PKS class and CLUSTER_UNSTATED locus evidence.
    Thirteen LOTUS occurrences are separate source assertions. The MOLLUSK facet is
    reproduced from retained NCBITaxon:2109287 after the recorded 1582468 merge; the
    name-only Discula cache does not establish whether the intended organism/homonym
    was grounded correctly. The other retained facets likewise remain source mappings,
    not fresh lineage verification.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-origin-owner
  - bgc-2174-occurrence-owner
  - bgc-2174-source-plan
  - bgc-2174-taxonomy-cache
  - bgc-2174-source-mibig_compounds
  - bgc-2174-source-lotus_occurrences
  - bgc-2174-taxon-routes
  - bgc-2174-source-taxon_merged
  - bgc-2174-taxonomy-supplement
  - bgc-2174-source-taxon_groups
  - bgc-2174-facet-owner
  - bgc-2174-intake
  dimensions:
  - name: taxon_scope
    value: 'Thirteen written LOTUS assertions, including two preserved forward merges.
      Supplemental taxon_groups row 30993 maps NCBITaxon:2109287 to MOLLUSK; intended
      Discula identity/lineage remains unverified. Cladonia uncialis subsp. uncialis
      NCBITaxon:180999: SOURCE_ASSERTION; no inferred characterized producer.'
    definition: Producer, occurrence, cache and forward-merge scopes remain distinct;
      no fresh ancestry claim.
    evidence_ids:
    - bgc-2174-origin-owner
    - bgc-2174-occurrence-owner
    - bgc-2174-source-plan
    - bgc-2174-taxonomy-cache
    - bgc-2174-source-mibig_compounds
    - bgc-2174-source-lotus_occurrences
    - bgc-2174-taxon-routes
    - bgc-2174-source-taxon_merged
    - bgc-2174-taxonomy-supplement
    - bgc-2174-source-taxon_groups
    - bgc-2174-facet-owner
    - bgc-2174-intake
  - name: producer_evidence
    value: 'Cladonia uncialis subsp. uncialis NCBITaxon:180999: SOURCE_ASSERTION;
      no inferred characterized producer.'
    definition: Producer evidence is assessed independently of occurrence and locus
      evidence.
    evidence_ids:
    - bgc-2174-origin-owner
    - bgc-2174-occurrence-owner
    - bgc-2174-source-plan
    - bgc-2174-taxonomy-cache
    - bgc-2174-source-mibig_compounds
    - bgc-2174-source-lotus_occurrences
    - bgc-2174-taxon-routes
    - bgc-2174-source-taxon_merged
    - bgc-2174-taxonomy-supplement
    - bgc-2174-source-taxon_groups
    - bgc-2174-facet-owner
    - bgc-2174-intake
  - name: locus_evidence
    value: BGC0001489 v3; MG777496.1:7141..29885; PKS; CLUSTER_UNSTATED. DOI:10.1016/j.bfopcu.2017.03.001
      is COMPOUND_BIOACTIVITY-level citation provenance.
    definition: Locus grade/method and citation role are retained without promotion
      to a complete pathway.
    evidence_ids:
    - bgc-2174-origin-owner
    - bgc-2174-occurrence-owner
    - bgc-2174-source-plan
    - bgc-2174-taxonomy-cache
    - bgc-2174-source-mibig_compounds
    - bgc-2174-source-lotus_occurrences
    - bgc-2174-taxon-routes
    - bgc-2174-source-taxon_merged
    - bgc-2174-taxonomy-supplement
    - bgc-2174-source-taxon_groups
    - bgc-2174-facet-owner
    - bgc-2174-intake
- assessment_id: bgc-2174-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: The locus citation DOI:10.1016/j.bfopcu.2017.03.001 is explicitly taken
    from compound bioactivity evidence in MIBiG. That role is not a newly inspected
    assay or a producer experiment. Thirteen LOTUS rows retain their individual citations;
    repeated DOI/taxon strings and taxonomic synonyms do not prove publication independence.
    None of the underlying articles was fetched.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-citation-owner
  - bgc-2174-grounding-owner
  - bgc-2174-source-mibig_compounds
  - bgc-2174-source-lotus_occurrences
  - bgc-2174-source-chebi_structures
  dimensions:
  - name: citation_scope
    value: The locus citation DOI:10.1016/j.bfopcu.2017.03.001 is explicitly taken
      from compound bioactivity evidence in MIBiG. That role is not a newly inspected
      assay or a producer experiment. Thirteen LOTUS rows retain their individual
      citations; repeated DOI/taxon strings and taxonomic synonyms do not prove publication
      independence. None of the underlying articles was fetched.
    definition: References support their recorded assertion roles; no publication
      independence or fresh primary access is assumed.
    evidence_ids:
    - bgc-2174-citation-owner
    - bgc-2174-grounding-owner
    - bgc-2174-source-mibig_compounds
    - bgc-2174-source-lotus_occurrences
    - bgc-2174-source-chebi_structures
- assessment_id: bgc-2174-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: This owner has no written bioactivities, bioactivity_summary or molecular_targets.
    Its exact retained PubChem, BindingDB and AntibioticMech queries are empty. The
    COMPOUND_BIOACTIVITY citation role cannot be converted into a measured endpoint,
    and the occurrence list is not evidence for demonstrated production or activity.
    No inactivity claim follows.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-assay-owner
  - bgc-2174-occurrence-owner
  - bgc-2174-query-pubchem_bioassay
  - bgc-2174-query-bindingdb_targets
  - bgc-2174-query-antibioticmech_inchikeys
  - bgc-2174-source-lotus_occurrences
  - bgc-2174-source-mibig_compounds
  - bgc-2174-taxonomy-supplement
  - bgc-2174-source-taxon_groups
  - bgc-2174-taxonomy-cache
  - bgc-2174-taxon-routes
  dimensions:
  - name: occurrence_scope
    value: Thirteen written LOTUS assertions, including two preserved forward merges.
      Supplemental taxon_groups row 30993 maps NCBITaxon:2109287 to MOLLUSK; intended
      Discula identity/lineage remains unverified.
    definition: Occurrence assertion counts and written caps do not count independent
      experiments or producers.
    evidence_ids:
    - bgc-2174-assay-owner
    - bgc-2174-occurrence-owner
    - bgc-2174-query-pubchem_bioassay
    - bgc-2174-query-bindingdb_targets
    - bgc-2174-query-antibioticmech_inchikeys
    - bgc-2174-source-lotus_occurrences
    - bgc-2174-source-mibig_compounds
    - bgc-2174-taxonomy-supplement
    - bgc-2174-source-taxon_groups
    - bgc-2174-taxonomy-cache
    - bgc-2174-taxon-routes
  - name: assay_target_scope
    value: No written selected bioactivities/bioactivity_summary/molecular_targets;
      exact retained PubChem, BindingDB and AntibioticMech queries empty. Compound-bioactivity
      citation role is not a measured assay.
    definition: Absence is bounded to complete owner plus exact retained source queries;
      no external absence claim.
    evidence_ids:
    - bgc-2174-assay-owner
    - bgc-2174-occurrence-owner
    - bgc-2174-query-pubchem_bioassay
    - bgc-2174-query-bindingdb_targets
    - bgc-2174-query-antibioticmech_inchikeys
    - bgc-2174-source-lotus_occurrences
    - bgc-2174-source-mibig_compounds
    - bgc-2174-taxonomy-supplement
    - bgc-2174-source-taxon_groups
    - bgc-2174-taxonomy-cache
    - bgc-2174-taxon-routes
- assessment_id: bgc-2174-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: NPClassifier predicts Coumarins / Isocoumarins under Shikimates and Phenylpropanoids,
    while MIBiG retains a PKS locus class. Saved fused-lactone topology supports the
    narrow structural applicability of an isocoumarin description; these two source
    axes do not establish biosynthetic origin. The admitted supplemental taxon_groups/seeder
    evidence explains the displayed MOLLUSK facet internally but cannot resolve the
    biological identity behind the Discula taxon mapping.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-classification-owner
  - bgc-2174-source-npclassifier
  - bgc-2174-topology
  - bgc-2174-source-mibig_compounds
  - bgc-2174-taxonomy-supplement
  - bgc-2174-source-taxon_groups
  - bgc-2174-facet-owner
  - bgc-2174-taxonomy-cache
  dimensions:
  - name: classification_applicability
    value: Computed Coumarins/Isocoumarins and is_glycoside=false; source PKS separate.
      Taxonomic MOLLUSK facet follows retained ID mapping only, with homonym correctness
      unresolved.
    definition: Computed classification, saved graph topology and source biosynthetic
      class are separate evidence axes.
    evidence_ids:
    - bgc-2174-classification-owner
    - bgc-2174-source-npclassifier
    - bgc-2174-topology
    - bgc-2174-source-mibig_compounds
    - bgc-2174-taxonomy-supplement
    - bgc-2174-source-taxon_groups
    - bgc-2174-facet-owner
    - bgc-2174-taxonomy-cache
- assessment_id: bgc-2174-completion
  area: completeness
  topic: Completion
  outcome: supported
  summary: Complete local whole-owner/source and both saved molecular forms were reviewed
    with claim-level limits. Five native checks passed; full QC/OAK and external primary,
    xref and taxonomy verification remain unavailable. No confirmed actionable defect
    is established by these bounded inputs. The retained 1582468→2109287 merge and
    MOLLUSK table assignment are internally traceable, but local name-only Discula
    cache evidence cannot confirm or refute the intended organism. No unsupported
    facet or homonym defect is asserted. The appropriate completion is partial and
    the local verdict is qualified.
  target_ids:
  - CHEBI:16368
  evidence_ids:
  - bgc-2174-owner
  - bgc-2174-intake
  - bgc-2174-intake-root
  - bgc-2174-plan-root
  - bgc-2174-source-plan
  - bgc-2174-diagnostic-root
  - bgc-2174-native-root
  - bgc-2174-taxonomy-supplement
  - bgc-2174-original-intake
  dimensions:
  - name: review_completion
    value: partial; qualified local review; external primary/taxonomy/xref verification
      and full QC/OAK unavailable. The retained 1582468→2109287 merge and MOLLUSK
      table assignment are internally traceable, but local name-only Discula cache
      evidence cannot confirm or refute the intended organism. No unsupported facet
      or homonym defect is asserted.
    definition: Completion reflects actual evidence access and check coverage, not
      all-native-pass or comprehensive verification.
    evidence_ids:
    - bgc-2174-owner
    - bgc-2174-intake
    - bgc-2174-intake-root
    - bgc-2174-plan-root
    - bgc-2174-source-plan
    - bgc-2174-diagnostic-root
    - bgc-2174-native-root
    - bgc-2174-taxonomy-supplement
    - bgc-2174-original-intake
findings: []
actions: []
limitations:
- 'Zero outbound: primary papers, database xrefs and taxonomy authorities were not
  fetched or refreshed.'
- Full QC and ontology/OAK are unavailable; local validation and reproduction are
  not scientific proof.
- Saved full_graph_identity_established remains false; normalized equality is not
  independent natural-identity or exhaustive stereo proof.
- The two original undefined-stereo warnings are global and unassigned; no per-owner
  warning attribution.
- Computed classes, bounded empty queries and local motifs do not independently establish
  biosynthesis, glycosylation, activity or inactivity.
- The retained 1582468→2109287 merge and MOLLUSK table assignment are internally traceable,
  but local name-only Discula cache evidence cannot confirm or refute the intended
  organism. No unsupported facet or homonym defect is asserted.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- BGC personally read every selected raw/history and current capture, all nine saved
  selected query frames and full positive source payloads, and every atom/bond/ring/stereo/motif/scalar/map
  field in both assigned saved forms. No new source-query, YAML or molecular execution.
  Source collector/composer and first-five review authorship overlap is explicit.
- 'Current direct-context reading: seven BGC2167 bodies/histories personally read;
  current BGC2290 scope carries ten exact-pinned ROOT prior whole companion reads
  and one prior-selected/current-companion body personally read. These scopes were
  rejoined to current bytes and are not claimed to be an identical old eleven-member
  set.'
- The assigned 112 complete source-row payloads/207 query frames were personally read
  and physically rejoined. Support independently read the complementary 70 rows/45
  frames and 22 cached stanzas; BGC read the remaining 45 cached stanzas. Local curation
  absence is not used as a first-five scientific claim, and the supplemental PubChem
  exclusion table is not imported into these targets.
- ROOT executed/accepted the original diagnostic; Native provided saved-result integrity
  review. This author independently interpreted complete saved forms. Native gates
  are represented by their actual accepted receipts, with unavailable QC/OAK preserved.
- No source record, native status, history, Git or LIVE mutation; no assembly/canonical/reader
  invocation or outbound active, queued, scheduled or retrying under this author.
- ROOT separately captured the supplemental 39-input intake and exact taxon-group
  table/seeder trace; BGC wholly read that trace ee9afd and the intake owner-path
  delta29e2ae. Original 38-input plan/intake/diagnostic remain unchanged historical
  evidence. The supplemental table explains the displayed facet but cannot confirm
  or refute the intended Discula homonym.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-218
```
