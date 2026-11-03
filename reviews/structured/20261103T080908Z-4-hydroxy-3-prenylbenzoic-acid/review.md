# Local evidence review: 4-hydroxy-3-prenylbenzoic acid

- Review: 20261103T080908Z-4-hydroxy-3-prenylbenzoic-acid
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T07:43:36.010074Z
- Finished UTC: 2026-11-03T08:09:08.447934Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The minted record retains exact key LBSJJNAMGVDGCU-UHFFFAOYSA-N and REVIEW_NEEDED because two retained ChEBI concepts share that key. CHEBI:1845 describes a generic polyprenyl benzoic-acid concept, whereas CHEBI:31111 specifies the dimethylallyl structure. EXACT is already withheld. The generic zwitterion explanation in the note does not resolve this concept-scope collision, and the prior sibling finding is not transferred to this owner. Both saved forms give neutral C12H14O3, 15 atoms and 15 bonds; all ten comparisons are true. Complete rows show a phenolic benzoic acid with one C5 prenyl side chain. Neither form reports potential stereo: one alkene carbon has two methyl substituents, so the literal slash syntax does not establish an E/Z assignment. Agreement does not settle ChEBI concept scope or natural identity. Local evidence supports a qualified partial review within the stated limits; no confirmed actionable defect is established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2173; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b4ad51fa2f | data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml | generated | 4-hydroxy-3-prenylbenzoic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-b4ad51fa2f | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b4ad51fa2f | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b4ad51fa2f | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b4ad51fa2f | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b4ad51fa2f | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b4ad51fa2f | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b4ad51fa2f | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b4ad51fa2f | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

The minted record retains exact key LBSJJNAMGVDGCU-UHFFFAOYSA-N and REVIEW_NEEDED because two retained ChEBI concepts share that key. CHEBI:1845 describes a generic polyprenyl benzoic-acid concept, whereas CHEBI:31111 specifies the dimethylallyl structure. EXACT is already withheld. The generic zwitterion explanation in the note does not resolve this concept-scope collision, and the prior sibling finding is not transferred to this owner.

### Representation

representation: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

Both saved forms give neutral C12H14O3, 15 atoms and 15 bonds; all ten comparisons are true. Complete rows show a phenolic benzoic acid with one C5 prenyl side chain. Neither form reports potential stereo: one alkene carbon has two methyl substituents, so the literal slash syntax does not establish an E/Z assignment. Agreement does not settle ChEBI concept scope or natural identity.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

Biscogniauxia sp. NCBITaxon:1896107 is retained as SOURCE_ASSERTION. BGC0002290 v2 has a distinct CLUSTER_DEMONSTRATED grade from heterologous-expression evidence, not a demonstrated native producer or complete enzyme pathway. Eight LOTUS occurrences and one ChEBI origin assertion are separate from this locus claim. Eleven direct companions have distinct keys and do not transfer activity, identity or stereochemistry.

### Citations

evidence: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

MIBiG ENTRY PMID:32364293 is retained as the locus-linked database citation. The Rubia yunnanensis ChEBI origin cites PMID:21973054 and the corresponding LOTUS assertion uses DOI:10.1021/NP2002918; citation spelling and source duplication do not establish independent publications. The other seven LOTUS rows retain their own taxon/citation claims. No primary text was fetched or adjacent BGC2290 result transferred. Both written occurrence labels and cached NCBITaxon:1650721 retain Rubia yunnanensis; no alternate-name equivalence is asserted.

### Bioactivity

evidence: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

The complete owner has no written bioactivities, bioactivity_summary or molecular_targets, and its retained exact full-key assay/target/sibling-activity queries are empty. Nine occurrence assertions and BGC2290 companion evidence do not establish pharmacology or inactivity. Compound 15 bioactivity citation roles elsewhere in the directly read context are not this compound’s assays.

### Classification

consistency: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

NPClassifier retains Phenolic acids (C6-C1), Shikimic acids and derivatives, and Simple phenolic acids with is_glycoside=false. The complete saved graph supports the narrow phenolic-carboxylic-acid/prenyl description, not a demonstrated shikimate pathway. MIBiG OTHER and heterologous locus evidence are separate axes. Computed labels do not resolve the CHEBI:1845/CHEBI:31111 collision.

### Completion

completeness: supported. Targets: naturalproductmech:mibig-b4ad51fa2f.

Complete local whole-owner/source and both saved molecular forms were reviewed with claim-level limits. Five native checks passed; full QC/OAK and external primary, xref and taxonomy verification remain unavailable. No confirmed actionable defect is established by these bounded inputs. The existing minted REVIEW_NEEDED state remains unresolved; no wrong-EXACT finding is imported from the previously reviewed BGC2290 sibling. The appropriate completion is partial and the local verdict is qualified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2173-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml; Whole current owner and complete curation_history | supports | Complete plaintext owner and all 2 history events personally read. This evidence identifies the preserved written content; no record edit or new YAML parse. |
| bgc-2173-capture | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete actual captured owner preserves all written structure, grounding, source, occurrence, classification and history fields. |
| bgc-2173-intake | /private/tmp/npm-review-work/shared-next-batch218/intakes/2173-inspect-001.json; /targets/0; /source/inputs | supports | Actual canonical inspection records this target, its maintained owners and all 48 current source inputs. Inspection is provenance, not proof of scientific truth. |
| bgc-2173-source-plan | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2 | supports | Complete selected raw/history/source copy and all nine saved query frames with their full positive payloads. Admission uses exact root ID/full key/direct owned BGC scope, without name or recursive expansion. |
| bgc-2173-grounding-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes | supports | Literal structure, source-concept and grounding fields, including retained definitions/xrefs/notes where written. This snapshot alone does not verify external identity. |
| bgc-2173-origin-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/bgc_class | supports | Complete written producer and locus objects, including grades, methods, accessions, coordinates where present, and attached evidence roles. |
| bgc-2173-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups | supports | All 9 written occurrence objects and literal occurrence_taxon_groups, preserving attached citations, notes and the displayed scope. This snapshot does not independently verify lineage or source identity. |
| bgc-2173-citation-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document/source_concepts; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/occurrences; /records/2/owner_document/curation_history | supports | Complete written source-concept, locus and occurrence citations plus history are retained in their original claim roles, without a primary-source refresh. |
| bgc-2173-classification-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class; /records/2/owner_document/np_pathway; /records/2/owner_document/biosynthesis_origin | supports | Literal retained classification: {"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":["Shikimates and Phenylpropanoids"],"superclass_results":["Phenolic acids (C6-C1)"],"class_results":["Shikimic acids and derivatives","Simple phenolic acids"],"is_glycoside":false}; source bgc_class=["OTHER"]. Computed labels and source classes are distinct assertions. |
| bgc-2173-assay-owner | /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json; /records/2/owner_document | partial | The complete captured owner has no written bioactivities, bioactivity_summary or molecular_targets. This bounded owner observation does not establish inactivity. |
| bgc-2173-chemistry | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/smiles/computed; /records/2/inchi/computed; /records/2/comparisons; /records/2/atom_correspondence | partial | Saved paired forms: C12H14O3, formal charge 0, 15 atoms/15 bonds in each; SMILES stereo {}, InChI-form stereo {}. All ten comparisons are true; full_graph_identity_established remains false. The written stereo_complete=true is preserved. No natural-identity or primary stereochemical proof is inferred. |
| bgc-2173-topology | /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/motifs; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings; /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs | supports | The saved SMILES form has an aromatic ring with phenolic OH7 and carboxyl C11(O12)=O13. Its side chain is ring-C4-C3=C1(C0)(C2); the two methyl groups at C1 preclude an E/Z distinction at that double bond. Both forms preserve the same bounded aromatic acid/prenyl topology; no saturated C5O candidate is reported. |
| bgc-2173-diagnostic-root | /private/tmp/npm-review-work/shared-next-batch218/root-diagnostic-acceptance-001.json; / | partial | ROOT accepts the one saved diagnostic execution and its integrity evidence: 20 forms parsed, all 100 comparison flags true, and two global undefined-stereo warnings remain unassigned. This does not supply a per-record warning attribution or scientific verdict. |
| bgc-2173-native-root | /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json; / | partial | ROOT accepts the five original passed native checks while full QC/OAK remain unavailable. Local validation/reproduction does not establish scientific accuracy; unavailable checks remain explicit. |
| bgc-2173-plan-root | /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json; / | supports | ROOT accepts the original source plan with 392 source placements/67 paths and its exact original ten-intake join. It is historical provenance and does not incorporate the later 2174 supplemental taxonomy input. |
| bgc-2173-intake-root | /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json; / | supports | ROOT accepts all ten original canonical intakes and exact original 392/67 maps. The later 2174 supplemental snapshot is separately cited rather than substituted into this historical acceptance. |
| bgc-2173-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/mibig_compounds | supports | Exact saved mibig_compounds predicate/query and 1 complete matching payload. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical TSV lines 2774 | supports | Complete exact full-key MIBiG payloads preserve compound structures, source concepts, producer/locus evidence grades and citation roles; retained database assertions are not refreshed primary experiments. |
| bgc-2173-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/chebi_structures | supports | Exact saved chebi_structures predicate/query and 2 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-source-chebi_structures | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv; physical TSV lines 191,7842 | supports | Complete exact full-key ChEBI payloads preserve the distinct identifiers, names and definitions in the retained crosswalk; equal keys do not make differently scoped concepts interchangeable. |
| bgc-2173-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/lotus_occurrences | supports | Exact saved lotus_occurrences predicate/query and 8 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical TSV lines 3799,3800,3801,3802,3803,3804,3805,3806 | supports | Complete exact full-key LOTUS payloads retain each taxon, name and citation assertion. These are occurrence records, not a count of independent producer experiments. |
| bgc-2173-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/cyanometdb_occurrences | partial | Exact saved cyanometdb_occurrences predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/npclassifier | supports | Exact saved npclassifier predicate/query and 1 complete matching payload. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical TSV lines 1325 | supports | Exact full-key NPClassifier payload preserves predicted pathway, superclass, class and glycoside fields with retained version; it is computed classification, not direct biosynthetic evidence. |
| bgc-2173-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/pubchem_bioassay | partial | Exact saved pubchem_bioassay predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/bindingdb_targets | partial | Exact saved bindingdb_targets predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/antibioticmech_inchikeys | partial | Exact saved antibioticmech_inchikeys predicate/query and 0 complete matching payloads. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /records/2/source_scope_inventory/joins/chebi_origins | supports | Exact saved chebi_origins predicate/query and 1 complete matching payload. Empty results are bounded to this retained inventory and exact selector, not a global absence claim. |
| bgc-2173-source-chebi_origins | /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv; physical TSV lines 4563 | supports | Complete matched ChEBI origin payloads preserve original taxon, source and citation fields; no primary-publication independence is assumed. |
| bgc-2173-taxonomy-cache | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/20; /cached_taxonomy/whole_stanzas/34; /cached_taxonomy/whole_stanzas/42; /cached_taxonomy/whole_stanzas/55; /cached_taxonomy/whole_stanzas/56; /cached_taxonomy/whole_stanzas/59; /cached_taxonomy/whole_stanzas/62; /cached_taxonomy/whole_stanzas/63 | partial | Complete retained cached stanzas for this selected source-taxon scope: NCBITaxon:3755, NCBITaxon:42229, NCBITaxon:130401, NCBITaxon:215128, NCBITaxon:582712, NCBITaxon:697043, NCBITaxon:857094, NCBITaxon:1650721, NCBITaxon:1896107. Names and synonyms remain saved cache assertions; they do not prove ancestry, intended homonym, cultivation or publication independence. |
| bgc-2173-direct-contexts | /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json; /raw_unselected_companions/6; /raw_unselected_companions/7; /raw_unselected_companions/8; /raw_unselected_companions/10; /raw_unselected_companions/11; /raw_unselected_companions/12; /raw_unselected_companions/13; /raw_unselected_companions/14; /raw_unselected_companions/15; /raw_unselected_companions/16; /raw_unselected_companions/17 | context_only | All 11 direct owned-BGC companion raw/history/source copies, each with its own full key and exact source claims. Their shared locus does not establish identity, stereochemistry, activity or independent experiments for the selected owner. Reading attribution is stated separately. |
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
- The existing minted REVIEW_NEEDED state remains unresolved; no wrong-EXACT finding is imported from the previously reviewed BGC2290 sibling.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read every selected raw/history and current capture, all nine saved selected query frames and full positive source payloads, and every atom/bond/ring/stereo/motif/scalar/map field in both assigned saved forms. No new source-query, YAML or molecular execution. Source collector/composer and first-five review authorship overlap is explicit.
- Current direct-context reading: seven BGC2167 bodies/histories personally read; current BGC2290 scope carries ten exact-pinned ROOT prior whole companion reads and one prior-selected/current-companion body personally read. These scopes were rejoined to current bytes and are not claimed to be an identical old eleven-member set.
- The assigned 112 complete source-row payloads/207 query frames were personally read and physically rejoined. Support independently read the complementary 70 rows/45 frames and 22 cached stanzas; BGC read the remaining 45 cached stanzas. Local curation absence is not used as a first-five scientific claim, and the supplemental PubChem exclusion table is not imported into these targets.
- ROOT executed/accepted the original diagnostic; Native provided saved-result integrity review. This author independently interpreted complete saved forms. Native gates are represented by their actual accepted receipts, with unavailable QC/OAK preserved.
- No source record, native status, history, Git or LIVE mutation; no assembly/canonical/reader invocation or outbound active, queued, scheduled or retrying under this author.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T080908Z-4-hydroxy-3-prenylbenzoic-acid
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 4-hydroxy-3-prenylbenzoic acid'
started_at: '2026-11-03T07:43:36.010074Z'
finished_at: '2026-11-03T08:09:08.447934Z'
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
summary: 'The minted record retains exact key LBSJJNAMGVDGCU-UHFFFAOYSA-N and REVIEW_NEEDED
  because two retained ChEBI concepts share that key. CHEBI:1845 describes a generic
  polyprenyl benzoic-acid concept, whereas CHEBI:31111 specifies the dimethylallyl
  structure. EXACT is already withheld. The generic zwitterion explanation in the
  note does not resolve this concept-scope collision, and the prior sibling finding
  is not transferred to this owner. Both saved forms give neutral C12H14O3, 15 atoms
  and 15 bonds; all ten comparisons are true. Complete rows show a phenolic benzoic
  acid with one C5 prenyl side chain. Neither form reports potential stereo: one alkene
  carbon has two methyl substituents, so the literal slash syntax does not establish
  an E/Z assignment. Agreement does not settle ChEBI concept scope or natural identity.
  Local evidence supports a qualified partial review within the stated limits; no
  confirmed actionable defect is established.'
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
    role: target
  - path: data/natural_products/shikimates_and_phenylpropanoids/compound-7.yaml
    sha256: 5b2493967d1774d28d023edd8500fbf16a14cfbe5139e0ff65abb0d471302e56
    role: context
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
  selection: Campaign path order 2173; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
targets:
- target_id: naturalproductmech:mibig-b4ad51fa2f
  path: data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
  label: 4-hydroxy-3-prenylbenzoic acid
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
    path: data/raw/chebi_origins.tsv
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
  - naturalproductmech:mibig-b4ad51fa2f
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
  - naturalproductmech:mibig-b4ad51fa2f
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
  - naturalproductmech:mibig-b4ad51fa2f
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
  - naturalproductmech:mibig-b4ad51fa2f
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
  - naturalproductmech:mibig-b4ad51fa2f
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
  - naturalproductmech:mibig-b4ad51fa2f
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2173-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/4-hydroxy-3-prenylbenzoic-acid.yaml
  locator: Whole current owner and complete curation_history
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete plaintext owner and all 2 history events personally read. This
    evidence identifies the preserved written content; no record edit or new YAML
    parse.
  snapshot_sha256: 7ea7276c7e9cd0e4510ea28aa8076911d173a70ec9b80bd3ae7803749a5b53de
- evidence_id: bgc-2173-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete actual captured owner preserves all written structure, grounding,
    source, occurrence, classification and history fields.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2173-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/intakes/2173-inspect-001.json
  locator: /targets/0; /source/inputs
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Actual canonical inspection records this target, its maintained owners
    and all 48 current source inputs. Inspection is provenance, not proof of scientific
    truth.
  snapshot_sha256: 063566bbc02cd2870ac489f0b3552c84b48e815929e38e06a587dc87963188a9
- evidence_id: bgc-2173-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete selected raw/history/source copy and all nine saved query frames
    with their full positive payloads. Admission uses exact root ID/full key/direct
    owned BGC scope, without name or recursive expansion.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
- evidence_id: bgc-2173-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Literal structure, source-concept and grounding fields, including retained
    definitions/xrefs/notes where written. This snapshot alone does not verify external
    identity.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2173-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete written producer and locus objects, including grades, methods,
    accessions, coordinates where present, and attached evidence roles.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2173-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences; /records/2/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: All 9 written occurrence objects and literal occurrence_taxon_groups, preserving
    attached citations, notes and the displayed scope. This snapshot does not independently
    verify lineage or source identity.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2173-citation-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document/source_concepts; /records/2/owner_document/biosynthetic_gene_clusters;
    /records/2/owner_document/occurrences; /records/2/owner_document/curation_history
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete written source-concept, locus and occurrence citations plus history
    are retained in their original claim roles, without a primary-source refresh.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2173-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class;
    /records/2/owner_document/np_pathway; /records/2/owner_document/biosynthesis_origin
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: 'Literal retained classification: {"tool":"NPClassifier","tool_version":"npclassifier.gnps2.org@2026-09-07","pathway_results":["Shikimates
    and Phenylpropanoids"],"superclass_results":["Phenolic acids (C6-C1)"],"class_results":["Shikimic
    acids and derivatives","Simple phenolic acids"],"is_glycoside":false}; source
    bgc_class=["OTHER"]. Computed labels and source classes are distinct assertions.'
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
- evidence_id: bgc-2173-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: The complete captured owner has no written bioactivities, bioactivity_summary
    or molecular_targets. This bounded owner observation does not establish inactivity.
  snapshot_sha256: 111c8ab76adff18f87f09f85986dc5108a336fb3802a5dfa9dad09abdf9407df
  search_scope: Complete saved selected owner only; no external or congener absence
    inference.
- evidence_id: bgc-2173-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/smiles/computed; /records/2/inchi/computed;
    /records/2/comparisons; /records/2/atom_correspondence
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: 'Saved paired forms: C12H14O3, formal charge 0, 15 atoms/15 bonds in each;
    SMILES stereo {}, InChI-form stereo {}. All ten comparisons are true; full_graph_identity_established
    remains false. The written stereo_complete=true is preserved. No natural-identity
    or primary stereochemical proof is inferred.'
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: bgc-2173-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings;
    /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/motifs;
    /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings;
    /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: The saved SMILES form has an aromatic ring with phenolic OH7 and carboxyl
    C11(O12)=O13. Its side chain is ring-C4-C3=C1(C0)(C2); the two methyl groups at
    C1 preclude an E/Z distinction at that double bond. Both forms preserve the same
    bounded aromatic acid/prenyl topology; no saturated C5O candidate is reported.
  snapshot_sha256: 4e71336f0142da26d4b24905132c2acb742b3252da930bfd5b6bc483129f1330
- evidence_id: bgc-2173-diagnostic-root
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
- evidence_id: bgc-2173-native-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-native-gates-acceptance-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: ROOT accepts the five original passed native checks while full QC/OAK remain
    unavailable. Local validation/reproduction does not establish scientific accuracy;
    unavailable checks remain explicit.
  snapshot_sha256: 57138741c14dfd03efcb91097dad031f0dc2209cb36d90f08c3b8796ae6f17b5
- evidence_id: bgc-2173-plan-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/root-conditional218-input-plan-acceptance-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: ROOT accepts the original source plan with 392 source placements/67 paths
    and its exact original ten-intake join. It is historical provenance and does not
    incorporate the later 2174 supplemental taxonomy input.
  snapshot_sha256: 938383f6b986f11823252b0a936784870aac1edd32b51ca4eea8c01b059af7ed
- evidence_id: bgc-2173-intake-root
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch218/root-intake-ready-001.json
  locator: /
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: ROOT accepts all ten original canonical intakes and exact original 392/67
    maps. The later 2174 supplemental snapshot is separately cited rather than substituted
    into this historical acceptance.
  snapshot_sha256: 4d19c500387ec2c243eb986a2e00c596a04a9fa2e4f1879d15165d0fcd2ac0cd
- evidence_id: bgc-2173-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved mibig_compounds predicate/query and 1 complete matching payload.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained mibig_compounds only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical TSV lines 2774
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete exact full-key MIBiG payloads preserve compound structures, source
    concepts, producer/locus evidence grades and citation roles; retained database
    assertions are not refreshed primary experiments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2173-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved chebi_structures predicate/query and 2 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained chebi_structures only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-source-chebi_structures
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_structures.tsv
  locator: physical TSV lines 191,7842
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete exact full-key ChEBI payloads preserve the distinct identifiers,
    names and definitions in the retained crosswalk; equal keys do not make differently
    scoped concepts interchangeable.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: bgc-2173-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved lotus_occurrences predicate/query and 8 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained lotus_occurrences only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical TSV lines 3799,3800,3801,3802,3803,3804,3805,3806
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete exact full-key LOTUS payloads retain each taxon, name and citation
    assertion. These are occurrence records, not a count of independent producer experiments.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2173-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved cyanometdb_occurrences predicate/query and 0 complete matching
    payloads. Empty results are bounded to this retained inventory and exact selector,
    not a global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained cyanometdb_occurrences only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved npclassifier predicate/query and 1 complete matching payload.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained npclassifier only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical TSV lines 1325
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact full-key NPClassifier payload preserves predicted pathway, superclass,
    class and glycoside fields with retained version; it is computed classification,
    not direct biosynthetic evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2173-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved pubchem_bioassay predicate/query and 0 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained pubchem_bioassay only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved bindingdb_targets predicate/query and 0 complete matching payloads.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained bindingdb_targets only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: Exact saved antibioticmech_inchikeys predicate/query and 0 complete matching
    payloads. Empty results are bounded to this retained inventory and exact selector,
    not a global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained antibioticmech_inchikeys only; exact complete standard_inchi_key
    equality; query="LBSJJNAMGVDGCU-UHFFFAOYSA-N"; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Exact saved chebi_origins predicate/query and 1 complete matching payload.
    Empty results are bounded to this retained inventory and exact selector, not a
    global absence claim.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
  search_scope: Current retained chebi_origins only; exact chebi_id from exact full-key
    structure rows; query=["CHEBI:1845","CHEBI:31111"]; no name, first-block or recursive
    expansion.
- evidence_id: bgc-2173-source-chebi_origins
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/chebi_origins.tsv
  locator: physical TSV lines 4563
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: supports
  summary: Complete matched ChEBI origin payloads preserve original taxon, source
    and citation fields; no primary-publication independence is assumed.
  snapshot_sha256: fcd43cf439851fcbed2398088cb8e53cc2c37f546fcccba4149b3af1837e78d8
- evidence_id: bgc-2173-taxonomy-cache
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/7; /cached_taxonomy/whole_stanzas/20; /cached_taxonomy/whole_stanzas/34;
    /cached_taxonomy/whole_stanzas/42; /cached_taxonomy/whole_stanzas/55; /cached_taxonomy/whole_stanzas/56;
    /cached_taxonomy/whole_stanzas/59; /cached_taxonomy/whole_stanzas/62; /cached_taxonomy/whole_stanzas/63
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: partial
  summary: 'Complete retained cached stanzas for this selected source-taxon scope:
    NCBITaxon:3755, NCBITaxon:42229, NCBITaxon:130401, NCBITaxon:215128, NCBITaxon:582712,
    NCBITaxon:697043, NCBITaxon:857094, NCBITaxon:1650721, NCBITaxon:1896107. Names
    and synonyms remain saved cache assertions; they do not prove ancestry, intended
    homonym, cultivation or publication independence.'
  snapshot_sha256: edc2e9c98e618d5d71a47c7ee5e0cd2053a1708f67466ad0b99b4e4cb33465f5
- evidence_id: bgc-2173-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch218-tentative/bgc-prep/bgc-conditional218-target-input-plan-001.json
  locator: /raw_unselected_companions/6; /raw_unselected_companions/7; /raw_unselected_companions/8;
    /raw_unselected_companions/10; /raw_unselected_companions/11; /raw_unselected_companions/12;
    /raw_unselected_companions/13; /raw_unselected_companions/14; /raw_unselected_companions/15;
    /raw_unselected_companions/16; /raw_unselected_companions/17
  accessed_at: '2026-11-03T08:00:51.519507Z'
  support: context_only
  summary: All 11 direct owned-BGC companion raw/history/source copies, each with
    its own full key and exact source claims. Their shared locus does not establish
    identity, stereochemistry, activity or independent experiments for the selected
    owner. Reading attribution is stated separately.
  snapshot_sha256: aaf42729452d321d4ecd04f5c235e6b0edd5b3e6da8a853294180d2376980f39
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
- assessment_id: bgc-2173-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted record retains exact key LBSJJNAMGVDGCU-UHFFFAOYSA-N and REVIEW_NEEDED
    because two retained ChEBI concepts share that key. CHEBI:1845 describes a generic
    polyprenyl benzoic-acid concept, whereas CHEBI:31111 specifies the dimethylallyl
    structure. EXACT is already withheld. The generic zwitterion explanation in the
    note does not resolve this concept-scope collision, and the prior sibling finding
    is not transferred to this owner.
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-owner
  - bgc-2173-capture
  - bgc-2173-intake
  - bgc-2173-grounding-owner
  - bgc-2173-source-plan
  - bgc-2173-query-chebi_structures
  - bgc-2173-chemistry
  - bgc-2173-source-mibig_compounds
  - bgc-2173-source-chebi_structures
  - bgc-2173-direct-contexts
  dimensions:
  - name: standard_inchi_key
    value: LBSJJNAMGVDGCU-UHFFFAOYSA-N
    definition: Exact complete key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2173-owner
    - bgc-2173-capture
    - bgc-2173-intake
    - bgc-2173-grounding-owner
    - bgc-2173-source-plan
    - bgc-2173-query-chebi_structures
    - bgc-2173-chemistry
    - bgc-2173-source-mibig_compounds
    - bgc-2173-source-chebi_structures
    - bgc-2173-direct-contexts
  - name: grounding_scope
    value: REVIEW_NEEDED; minted identifier retained; CHEBI:1845 versus CHEBI:31111
      scope conflict unresolved and no EXACT assertion selected.
    definition: Local grounding fidelity and unresolved concept scope are separated
      from natural-identity verification.
    evidence_ids:
    - bgc-2173-owner
    - bgc-2173-capture
    - bgc-2173-intake
    - bgc-2173-grounding-owner
    - bgc-2173-source-plan
    - bgc-2173-query-chebi_structures
    - bgc-2173-chemistry
    - bgc-2173-source-mibig_compounds
    - bgc-2173-source-chebi_structures
    - bgc-2173-direct-contexts
- assessment_id: bgc-2173-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: 'Both saved forms give neutral C12H14O3, 15 atoms and 15 bonds; all ten
    comparisons are true. Complete rows show a phenolic benzoic acid with one C5 prenyl
    side chain. Neither form reports potential stereo: one alkene carbon has two methyl
    substituents, so the literal slash syntax does not establish an E/Z assignment.
    Agreement does not settle ChEBI concept scope or natural identity.'
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-chemistry
  - bgc-2173-topology
  - bgc-2173-diagnostic-root
  - bgc-2173-grounding-owner
  dimensions:
  - name: stereochemistry_scope
    value: No potential stereo elements reported; the prenyl alkene has two methyl
      substituents at one end. Literal slash syntax is not an E/Z assignment.
    definition: Interpretation of complete saved stereo/atom/bond tables, not a new
      parse or primary assignment.
    evidence_ids:
    - bgc-2173-chemistry
    - bgc-2173-topology
    - bgc-2173-diagnostic-root
    - bgc-2173-grounding-owner
  - name: representation_correspondence
    value: All ten saved comparison flags true; full_graph_identity_established=false.
      The saved SMILES form has an aromatic ring with phenolic OH7 and carboxyl C11(O12)=O13.
      Its side chain is ring-C4-C3=C1(C0)(C2); the two methyl groups at C1 preclude
      an E/Z distinction at that double bond. Both forms preserve the same bounded
      aromatic acid/prenyl topology; no saturated C5O candidate is reported.
    definition: Representation agreement is bounded to the saved computational result;
      topology does not prove natural identity.
    evidence_ids:
    - bgc-2173-chemistry
    - bgc-2173-topology
    - bgc-2173-diagnostic-root
    - bgc-2173-grounding-owner
- assessment_id: bgc-2173-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: Biscogniauxia sp. NCBITaxon:1896107 is retained as SOURCE_ASSERTION. BGC0002290
    v2 has a distinct CLUSTER_DEMONSTRATED grade from heterologous-expression evidence,
    not a demonstrated native producer or complete enzyme pathway. Eight LOTUS occurrences
    and one ChEBI origin assertion are separate from this locus claim. Eleven direct
    companions have distinct keys and do not transfer activity, identity or stereochemistry.
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-origin-owner
  - bgc-2173-occurrence-owner
  - bgc-2173-source-plan
  - bgc-2173-taxonomy-cache
  - bgc-2173-source-mibig_compounds
  - bgc-2173-source-lotus_occurrences
  - bgc-2173-source-chebi_origins
  - bgc-2173-direct-contexts
  dimensions:
  - name: taxon_scope
    value: 'Nine written occurrence assertions: eight LOTUS rows plus one ChEBI Rubia
      yunnanensis root-extract origin. Repeated taxon/source citations are not independent
      producer experiments. Biscogniauxia sp. NCBITaxon:1896107: SOURCE_ASSERTION;
      locus demonstration does not upgrade native producer evidence.'
    definition: Producer, occurrence, cache and forward-merge scopes remain distinct;
      no fresh ancestry claim.
    evidence_ids:
    - bgc-2173-origin-owner
    - bgc-2173-occurrence-owner
    - bgc-2173-source-plan
    - bgc-2173-taxonomy-cache
    - bgc-2173-source-mibig_compounds
    - bgc-2173-source-lotus_occurrences
    - bgc-2173-source-chebi_origins
    - bgc-2173-direct-contexts
  - name: producer_evidence
    value: 'Biscogniauxia sp. NCBITaxon:1896107: SOURCE_ASSERTION; locus demonstration
      does not upgrade native producer evidence.'
    definition: Producer evidence is assessed independently of occurrence and locus
      evidence.
    evidence_ids:
    - bgc-2173-origin-owner
    - bgc-2173-occurrence-owner
    - bgc-2173-source-plan
    - bgc-2173-taxonomy-cache
    - bgc-2173-source-mibig_compounds
    - bgc-2173-source-lotus_occurrences
    - bgc-2173-source-chebi_origins
    - bgc-2173-direct-contexts
  - name: locus_evidence
    value: BGC0002290 v2, MT109335.1:1..37984, OTHER; CLUSTER_DEMONSTRATED with Heterologous
      expression; ENTRY PMID:32364293.
    definition: Locus grade/method and citation role are retained without promotion
      to a complete pathway.
    evidence_ids:
    - bgc-2173-origin-owner
    - bgc-2173-occurrence-owner
    - bgc-2173-source-plan
    - bgc-2173-taxonomy-cache
    - bgc-2173-source-mibig_compounds
    - bgc-2173-source-lotus_occurrences
    - bgc-2173-source-chebi_origins
    - bgc-2173-direct-contexts
- assessment_id: bgc-2173-citations
  area: evidence
  topic: Citations
  outcome: supported
  summary: MIBiG ENTRY PMID:32364293 is retained as the locus-linked database citation.
    The Rubia yunnanensis ChEBI origin cites PMID:21973054 and the corresponding LOTUS
    assertion uses DOI:10.1021/NP2002918; citation spelling and source duplication
    do not establish independent publications. The other seven LOTUS rows retain their
    own taxon/citation claims. No primary text was fetched or adjacent BGC2290 result
    transferred. Both written occurrence labels and cached NCBITaxon:1650721 retain
    Rubia yunnanensis; no alternate-name equivalence is asserted.
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-citation-owner
  - bgc-2173-grounding-owner
  - bgc-2173-source-mibig_compounds
  - bgc-2173-source-lotus_occurrences
  - bgc-2173-source-chebi_origins
  - bgc-2173-source-chebi_structures
  - bgc-2173-direct-contexts
  - bgc-2173-taxonomy-cache
  dimensions:
  - name: citation_scope
    value: MIBiG ENTRY PMID:32364293 is retained as the locus-linked database citation.
      The Rubia yunnanensis ChEBI origin cites PMID:21973054 and the corresponding
      LOTUS assertion uses DOI:10.1021/NP2002918; citation spelling and source duplication
      do not establish independent publications. The other seven LOTUS rows retain
      their own taxon/citation claims. No primary text was fetched or adjacent BGC2290
      result transferred. Both written occurrence labels and cached NCBITaxon:1650721
      retain Rubia yunnanensis; no alternate-name equivalence is asserted.
    definition: References support their recorded assertion roles; no publication
      independence or fresh primary access is assumed.
    evidence_ids:
    - bgc-2173-citation-owner
    - bgc-2173-grounding-owner
    - bgc-2173-source-mibig_compounds
    - bgc-2173-source-lotus_occurrences
    - bgc-2173-source-chebi_origins
    - bgc-2173-source-chebi_structures
    - bgc-2173-direct-contexts
    - bgc-2173-taxonomy-cache
- assessment_id: bgc-2173-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The complete owner has no written bioactivities, bioactivity_summary or
    molecular_targets, and its retained exact full-key assay/target/sibling-activity
    queries are empty. Nine occurrence assertions and BGC2290 companion evidence do
    not establish pharmacology or inactivity. Compound 15 bioactivity citation roles
    elsewhere in the directly read context are not this compound’s assays.
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-assay-owner
  - bgc-2173-occurrence-owner
  - bgc-2173-query-pubchem_bioassay
  - bgc-2173-query-bindingdb_targets
  - bgc-2173-query-antibioticmech_inchikeys
  - bgc-2173-source-lotus_occurrences
  - bgc-2173-source-chebi_origins
  - bgc-2173-source-mibig_compounds
  - bgc-2173-direct-contexts
  dimensions:
  - name: occurrence_scope
    value: 'Nine written occurrence assertions: eight LOTUS rows plus one ChEBI Rubia
      yunnanensis root-extract origin. Repeated taxon/source citations are not independent
      producer experiments.'
    definition: Occurrence assertion counts and written caps do not count independent
      experiments or producers.
    evidence_ids:
    - bgc-2173-assay-owner
    - bgc-2173-occurrence-owner
    - bgc-2173-query-pubchem_bioassay
    - bgc-2173-query-bindingdb_targets
    - bgc-2173-query-antibioticmech_inchikeys
    - bgc-2173-source-lotus_occurrences
    - bgc-2173-source-chebi_origins
    - bgc-2173-source-mibig_compounds
    - bgc-2173-direct-contexts
  - name: assay_target_scope
    value: No written selected bioactivities/bioactivity_summary/molecular_targets;
      exact retained PubChem, BindingDB and AntibioticMech queries empty. No inactivity
      or companion pharmacology inference.
    definition: Absence is bounded to complete owner plus exact retained source queries;
      no external absence claim.
    evidence_ids:
    - bgc-2173-assay-owner
    - bgc-2173-occurrence-owner
    - bgc-2173-query-pubchem_bioassay
    - bgc-2173-query-bindingdb_targets
    - bgc-2173-query-antibioticmech_inchikeys
    - bgc-2173-source-lotus_occurrences
    - bgc-2173-source-chebi_origins
    - bgc-2173-source-mibig_compounds
    - bgc-2173-direct-contexts
- assessment_id: bgc-2173-classification
  area: consistency
  topic: Classification
  outcome: supported
  summary: NPClassifier retains Phenolic acids (C6-C1), Shikimic acids and derivatives,
    and Simple phenolic acids with is_glycoside=false. The complete saved graph supports
    the narrow phenolic-carboxylic-acid/prenyl description, not a demonstrated shikimate
    pathway. MIBiG OTHER and heterologous locus evidence are separate axes. Computed
    labels do not resolve the CHEBI:1845/CHEBI:31111 collision.
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-classification-owner
  - bgc-2173-source-npclassifier
  - bgc-2173-topology
  - bgc-2173-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: Computed Phenolic acids (C6-C1), Shikimic acids and derivatives, Simple
      phenolic acids; is_glycoside=false. OTHER locus class and unresolved grounding
      remain separate.
    definition: Computed classification, saved graph topology and source biosynthetic
      class are separate evidence axes.
    evidence_ids:
    - bgc-2173-classification-owner
    - bgc-2173-source-npclassifier
    - bgc-2173-topology
    - bgc-2173-source-mibig_compounds
- assessment_id: bgc-2173-completion
  area: completeness
  topic: Completion
  outcome: supported
  summary: Complete local whole-owner/source and both saved molecular forms were reviewed
    with claim-level limits. Five native checks passed; full QC/OAK and external primary,
    xref and taxonomy verification remain unavailable. No confirmed actionable defect
    is established by these bounded inputs. The existing minted REVIEW_NEEDED state
    remains unresolved; no wrong-EXACT finding is imported from the previously reviewed
    BGC2290 sibling. The appropriate completion is partial and the local verdict is
    qualified.
  target_ids:
  - naturalproductmech:mibig-b4ad51fa2f
  evidence_ids:
  - bgc-2173-owner
  - bgc-2173-intake
  - bgc-2173-intake-root
  - bgc-2173-plan-root
  - bgc-2173-source-plan
  - bgc-2173-diagnostic-root
  - bgc-2173-native-root
  dimensions:
  - name: review_completion
    value: partial; qualified local review; external primary/taxonomy/xref verification
      and full QC/OAK unavailable. The existing minted REVIEW_NEEDED state remains
      unresolved; no wrong-EXACT finding is imported from the previously reviewed
      BGC2290 sibling.
    definition: Completion reflects actual evidence access and check coverage, not
      all-native-pass or comprehensive verification.
    evidence_ids:
    - bgc-2173-owner
    - bgc-2173-intake
    - bgc-2173-intake-root
    - bgc-2173-plan-root
    - bgc-2173-source-plan
    - bgc-2173-diagnostic-root
    - bgc-2173-native-root
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
- The existing minted REVIEW_NEEDED state remains unresolved; no wrong-EXACT finding
  is imported from the previously reviewed BGC2290 sibling.
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
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-218
```
