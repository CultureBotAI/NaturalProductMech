# Local evidence review: stipitatic acid

- Review: 20261103T133012Z-stipitatic-acid
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-03T13:02:50.364588Z
- Finished UTC: 2026-11-03T13:30:12.761867Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Stipitatic acid has coherent exact-key, knockout-graded locus and occurrence provenance in the retained evidence. Its seven-membered tropolone topology limits the applicability of the computed C6-C1 phenolic-acid label. No source identity defect is established; the review remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2223; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-8460498c49 | data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml | generated | stipitatic acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-8460498c49 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-8460498c49 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-8460498c49 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-8460498c49 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-8460498c49 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-8460498c49 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-8460498c49 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-8460498c49 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Identity

identity: supported. Targets: naturalproductmech:mibig-8460498c49.

The minted owner matches the single BGC0000154 v4 source compound, full key ZGKNMKBZOSTFCB-UHFFFAOYSA-N, and both saved molecular forms. The exact retained ChEBI query is empty, so the local minted grounding is preserved. There are no direct companion records in the admitted one-hop scope. PubChem20501 is a retained xref, not a freshly verified independent structure authority.

### Representation

representation: supported. Targets: naturalproductmech:mibig-8460498c49.

Both forms give neutral C8H6O5, 13 atoms and 13 bonds with one seven-carbon ring and no potential stereoelements reported. All ten comparisons are true and the saved correspondence is complete. The true source stereochemistry flag is consistent with this encoded representation; it does not establish a preferred tautomer, protonation state in solution or experimental sample identity. The saved aromatic representation is kept distinct from an experimental electronic-structure claim.

### Origin

provenance: supported. Targets: naturalproductmech:mibig-8460498c49.

BGC0000154 v4 names Talaromyces stipitatus ATCC10500 (441959), BGC_CHARACTERIZED, with knockout-based CLUSTER_DEMONSTRATED locus support. Its source entry is active/questionable/complete and retains EQ962655.1 coordinates 1805625–1837759. Two LOTUS assertions refer to species 28564, distinct from the strain-level producer claim. The cached species stanza carries Penicillium stipitatum as a synonym; this is retained local name continuity, not a fresh taxonomic verification or a forward-merge route.

### Citations

evidence: unknown. Targets: naturalproductmech:mibig-8460498c49.

PMID:22508998 is an entry-level MIBiG citation. The two species-level LOTUS assertions retain DOI:10.1006/BIOO.1995.1011 and DOI:10.1038/155050B0. Their roles are preserved without claiming three independent experiments or freshly confirming the publications. Producer, locus and occurrence claims remain separately graded.

### Bioactivity

evidence: supported. Targets: naturalproductmech:mibig-8460498c49.

The record writes two cited occurrences for species 28564 and no assays, activity summary, targets or mechanisms. The one PubChem match at physical line 11239 is a blank-AID no-assay-data sentinel for CID20501. It does not mean inactivity. Exact BindingDB and sibling-activity joins are empty within the saved scope; no biological absence is inferred.

### Classification

consistency: unknown. Targets: naturalproductmech:mibig-8460498c49.

The complete atom and ring tables show seven carbons in the ring, a ring ketone, two hydroxyl substituents and a carboxylic acid: a tropolone-type scaffold. There is no six-carbon benzene ring or candidate sugar ring. NPClassifier nevertheless stores Phenolic acids (C6-C1)/Simple phenolic acids. This is an explicit model-applicability limitation, not a reason to overwrite the faithfully retained computed field or infer wrong compound identity. The source PKS/iterative-type-I classification and demonstrated locus support remain separate from the model filing.

### Completion

completeness: unknown. Targets: naturalproductmech:mibig-8460498c49.

The complete owner/history, admitted source context, actual intake and all paired saved molecular tables were reviewed. No supported local curation defect is established within this scope. Five local gates passed, while full QC, OAK and external primary-source/taxonomy/accession verification were unavailable. The review remains partial; no record, native curation status or history was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2223-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml; Whole owner plaintext and complete curation_history | supports | Complete owner and append-only history, personally read as exact saved plaintext and rejoined to this current raw pin. |
| bgc-2223-capture | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/2/owner_pin; /records/2/owner_document | supports | Complete captured owner and its exact source pin; no source fields or native history were edited. |
| bgc-2223-intake | /private/tmp/npm-review-work/shared-next-batch223/intakes/2223-inspect-001.json; /source; /targets | supports | Actual canonical intake source, complete input map and target/maintained-owner scope. |
| bgc-2223-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-intake-ready-001.json; /status; /intake_summary | supports | ROOT acceptance of the original ten canonical intakes, with no replay. |
| bgc-2223-grounding-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status | supports | Written structure, source concepts and grounding decision, without fresh external resolution. |
| bgc-2223-origin-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters | supports | Complete written producer and locus assertions, including evidence grades, source versions, methods and references. |
| bgc-2223-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/2/owner_document/occurrences | supports | Complete written occurrences and their cited scope. |
| bgc-2223-assay-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/2/owner_document | supports | Complete captured owner supports the written assay, summary, target and mechanism fields or their absence; source-query-only facts belong to separate evidence. |
| bgc-2223-classification-owner | /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json; /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class | supports | Named-model prediction and source BGC class are preserved as separate assertions. |
| bgc-2223-source-plan | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2 | supports | Complete admitted selected context, direct companions, raw/history and exact input map. |
| bgc-2223-source-notes | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-scope-notes-001.json; /reading; /curation; /cautions | supports | Complete reading attribution and bounded curation scope: 135 literal tokens across eight explicit files, with five out-of-scope shared-taxon hits rather than zero textual matches. |
| bgc-2223-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-input-plan-acceptance-001.json; /status; /plan; /notes; /inventory; /per_order_counts | supports | ROOT acceptance of this original saved source plan, notes and exact per-order input counts. |
| bgc-2223-chemistry | /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/smiles; /records/2/inchi; /records/2/comparisons; /records/2/atom_correspondence | supports | Both complete saved molecular forms, all comparison flags and literal atom correspondence. All ten comparisons are true for this owner; full_graph_identity_established remains false. |
| bgc-2223-topology | /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings; /records/2/smiles/computed/motifs; /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings; /records/2/inchi/computed/motifs; /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/stereo_counts; /records/2/atom_correspondence; /records/2/declared_structure | supports | Complete indexed topology and stereochemistry in both saved forms. Structural motifs are bounded patterns, not natural-identity or experimental assignments. |
| bgc-2223-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json; /status; /chemistry_DATA; /chemistry_execution; /results; /unavailable | supports | ROOT acceptance of the original ordinary molecular diagnostic, with four globally unassigned warnings; scientific interpretation remains separately scoped. |
| bgc-2223-native-acceptance | /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json; /status; /native_ledger; /results; /unavailable | supports | ROOT acceptance of the five original local gates; full QC and OAK remain unavailable as separately recorded. |
| bgc-2223-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/mibig_compounds | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned mibig_compounds table. No query replay or external lookup. |
| bgc-2223-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 201 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":201,"row_sha256":"7acaf5987f9924f07ac7945f2403baef394c8432aab65c64fd516d53117e9dd1","row":{"mibig_accession":"BGC0000154","entry_version":"4","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"stipitatic acid","compound_index":"1","smiles":"C1=C(C=C(C(=CC1=O)O)O)C(=O)O","standard_inchi":"InChI=1S/C8H6O5/c9-5-1-4(8(12)13)2-6(10)7(11)3-5/h1-3,10-11H,(H,12,13)","standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:20501&#124;chemspider:19955692","taxon_id":"NCBITaxon:441959","taxon_label":"Talaromyces stipitatus ATCC 10500","bgc_classes":"PKS","bgc_subclasses":"Iterative type I","genome_accession":"EQ962655.1","locus_from":"1805625","locus_to":"1837759","locus_evidence_methods":"Knock-out studies","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:22508998","reference_basis":"ENTRY"}}] |
| bgc-2223-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/chebi_structures | supports | Complete saved query frame with 0 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned chebi_structures table. No query replay or external lookup. |
| bgc-2223-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved query frame with 2 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned lotus_occurrences table. No query replay or external lookup. |
| bgc-2223-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 10008,10009 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":10008,"row_sha256":"8458b66149b174315da1da4b43b84c35bf67ac3cd363b6a75112ab5869aad4eb","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","organism_name":"Talaromyces stipitatus","taxon_id":"NCBITaxon:28564","organism_wikidata":"http://www.wikidata.org/entity/Q80855389","reference_doi":"10.1006/BIOO.1995.1011","structure_wikidata":"http://www.wikidata.org/entity/Q105375286"}},{"physical_line":10009,"row_sha256":"6492eb43660599b9d29f07c1ca793af28e4b28fe2521145105e26b8b88f43bbb","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","organism_name":"Talaromyces stipitatus","taxon_id":"NCBITaxon:28564","organism_wikidata":"http://www.wikidata.org/entity/Q80855389","reference_doi":"10.1038/155050B0","structure_wikidata":"http://www.wikidata.org/entity/Q105375286"}}] |
| bgc-2223-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved query frame with 0 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned cyanometdb_occurrences table. No query replay or external lookup. |
| bgc-2223-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/npclassifier | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned npclassifier table. No query replay or external lookup. |
| bgc-2223-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 3026 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":3026,"row_sha256":"15d41d06455b3b47a6f2585194db437aecd66d94cdd7e15426775cab69092215","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","smiles":"C1=C(C=C(C(=CC1=O)O)O)C(=O)O","pathway_results":"Shikimates and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Simple phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}] |
| bgc-2223-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved query frame with 1 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned pubchem_bioassay table. No query replay or external lookup. |
| bgc-2223-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Physical TSV lines 11239 | supports | Complete retained fields, including blanks, and physical frame hashes: [{"physical_line":11239,"row_sha256":"33c2336e631f757ce7ba47b4b6c04377937fc127b5dcc113faaa3e85134d6888","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","cid":"20501","aid":"","assay_name":"(no assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""}}] |
| bgc-2223-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved query frame with 0 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned bindingdb_targets table. No query replay or external lookup. |
| bgc-2223-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved query frame with 0 positive row placements. Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against the exact pinned antibioticmech_inchikeys table. No query replay or external lookup. |
| bgc-2223-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/joins/chebi_origins | supports | Complete saved query frame with 0 positive row placements. Saved exact chebi_id from exact full-key structure rows, query [], against the exact pinned chebi_origins table. No query replay or external lookup. |
| bgc-2223-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/6; /cached_taxonomy/whole_stanzas/17 | supports | Complete personally read retained name/synonym stanzas: [{"id":"NCBITaxon:28564","physical_line":12651,"complete_stanza":"[Term]\nid: NCBITaxon:28564\nname: Talaromyces stipitatus\nsynonym: \"Penicillium stipitatum\" EXACT []\n\n"},{"id":"NCBITaxon:441959","physical_line":94051,"complete_stanza":"[Term]\nid: NCBITaxon:441959\nname: Talaromyces stipitatus ATCC 10500\n\n"}]. No current external taxonomy or ancestry is inferred. |
| bgc-2223-source-routes | /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json; /records/2/source_scope_inventory/source_taxa; /records/2/source_scope_inventory/forward_taxon_merge_matches; /records/2/source_scope_inventory/nonorganism_matches | supports | Exact selected source taxa and forward/nonorganism route sets; both match lists are empty in this saved scope. |
| bgc-2223-review-skill | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Workflow; Output | supports | Claim-level review, immutable records and honest partial completion under actual evidence-access limits. |
| bgc-2223-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Complete maintained review profile | supports | Producer/occurrence distinctions, evidence grades, source ownership and qualified computed classifications. |
| bgc-2223-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 376–432 | supports | Identifier/stereo limitations and the explicit computed-not-source status of NPClassifier fields. |
| bgc-2223-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 632–665; lines 920–947 | supports | Optional observation activity class and coarse backed activity buckets; no dedicated cell-killing definition is supplied. |
| bgc-2223-activity-classifier | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 127–179; lines 1310–1382 | supports | Maintained title classifier, ACTIVE-only class assignment, 25-observation cap and summary derivation from written observations. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-223/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-223/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-223/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-223/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- External identifiers, taxonomy, accessions and primary publications were not refreshed under the absolute no-request instruction; historical and database assertions remain attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and parsing establish their declared mechanical scope only.
- Negative source joins apply only to the exact retained predicates and source snapshots. Shared loci, citations and companion records do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Complete selected source payloads and explicit direct-context reading attribution are preserved in the pinned source notes. All five owner histories, actual intakes and ten paired molecular tables were personally read.
- Four original diagnostic warnings remain global and unassigned; no warning is attributed to an individual owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T133012Z-stipitatic-acid
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: stipitatic acid'
started_at: '2026-11-03T13:02:50.364588Z'
finished_at: '2026-11-03T13:30:12.761867Z'
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
summary: Stipitatic acid has coherent exact-key, knockout-graded locus and occurrence
  provenance in the retained evidence. Its seven-membered tropolone topology limits
  the applicability of the computed C6-C1 phenolic-acid label. No source identity
  defect is established; the review remains partial.
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
  - path: data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml
    sha256: c4f13ee451c35e55f2d3146c0f5984458a44958a964d99ae039c18dfc1556250
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
  selection: Campaign path order 2223; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-8460498c49
targets:
- target_id: naturalproductmech:mibig-8460498c49
  path: data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml
  label: stipitatic acid
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
  - naturalproductmech:mibig-8460498c49
  command: just validate-strict data/natural_products/shikimates_and_phenylpropanoids/s2507.yaml
    data/natural_products/shikimates_and_phenylpropanoids/semivioxanthin.yaml data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/sungeidine-d.yaml data/natural_products/shikimates_and_phenylpropanoids/tropodithietic-acid.yaml
    data/natural_products/shikimates_and_phenylpropanoids/venemycin.yaml data/natural_products/shikimates_and_phenylpropanoids/xenocoumacin-1.yaml
    data/natural_products/shikimates_and_phenylpropanoids/xenocoumacin-ii.yaml data/natural_products/shikimates_and_phenylpropanoids/z-6-undecenyltyrazolone.yaml
    data/natural_products/terpenoids/1-epibotrydial.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-8460498c49
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-223/validate-all-001.tsv
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
  - naturalproductmech:mibig-8460498c49
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
  - naturalproductmech:mibig-8460498c49
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
  - naturalproductmech:mibig-8460498c49
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-223/review-queue-001.tsv
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
  - naturalproductmech:mibig-8460498c49
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-8460498c49
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-8460498c49
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2223-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/shikimates_and_phenylpropanoids/stipitatic-acid.yaml
  locator: Whole owner plaintext and complete curation_history
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete owner and append-only history, personally read as exact saved
    plaintext and rejoined to this current raw pin.
  snapshot_sha256: c4f13ee451c35e55f2d3146c0f5984458a44958a964d99ae039c18dfc1556250
- evidence_id: bgc-2223-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/2/owner_pin; /records/2/owner_document
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete captured owner and its exact source pin; no source fields or native
    history were edited.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2223-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/intakes/2223-inspect-001.json
  locator: /source; /targets
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Actual canonical intake source, complete input map and target/maintained-owner
    scope.
  snapshot_sha256: e888dbcaa2aa8e53328c2ed1891c4ad00fc0dde07f2bf4249ee388050982d4aa
- evidence_id: bgc-2223-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-intake-ready-001.json
  locator: /status; /intake_summary
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of the original ten canonical intakes, with no replay.
  snapshot_sha256: f4a1f4b715e664d404565e45fe7359127911e5c1349b6e9f0df7c7ce4a4519a7
- evidence_id: bgc-2223-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/2/owner_document/chemical_structure; /records/2/owner_document/source_concepts;
    /records/2/owner_document/grounding_status
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Written structure, source concepts and grounding decision, without fresh
    external resolution.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2223-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete written producer and locus assertions, including evidence grades,
    source versions, methods and references.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2223-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/2/owner_document/occurrences
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete written occurrences and their cited scope.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2223-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete captured owner supports the written assay, summary, target and
    mechanism fields or their absence; source-query-only facts belong to separate
    evidence.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2223-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_classification; /records/2/owner_document/bgc_class
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Named-model prediction and source BGC class are preserved as separate assertions.
  snapshot_sha256: c90dd6eef423327441048f2ac656489bafb5327f718ca861e50b54a0f4670df5
- evidence_id: bgc-2223-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete admitted selected context, direct companions, raw/history and
    exact input map.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: bgc-2223-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-scope-notes-001.json
  locator: /reading; /curation; /cautions
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete reading attribution and bounded curation scope: 135 literal tokens
    across eight explicit files, with five out-of-scope shared-taxon hits rather than
    zero textual matches.'
  snapshot_sha256: 589a3b0bfdd9afec556e285580c4102a2e3fa8d9735e3364d7ea42d9827eee41
- evidence_id: bgc-2223-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-input-plan-acceptance-001.json
  locator: /status; /plan; /notes; /inventory; /per_order_counts
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of this original saved source plan, notes and exact per-order
    input counts.
  snapshot_sha256: 4428e2ef161f4bb098750e9bbcdd4dd8841c2332e7bc64b01c75f1cc8aacdaf0
- evidence_id: bgc-2223-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/smiles; /records/2/inchi; /records/2/comparisons;
    /records/2/atom_correspondence
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Both complete saved molecular forms, all comparison flags and literal atom
    correspondence. All ten comparisons are true for this owner; full_graph_identity_established
    remains false.
  snapshot_sha256: 1723f79377c00369ddbb345f4b472f98b3ef855db093e27f59998345d4779937
- evidence_id: bgc-2223-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings;
    /records/2/smiles/computed/motifs; /records/2/smiles/computed/potential_stereo;
    /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds;
    /records/2/inchi/computed/rings; /records/2/inchi/computed/motifs; /records/2/inchi/computed/potential_stereo;
    /records/2/inchi/computed/stereo_counts; /records/2/atom_correspondence; /records/2/declared_structure
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete indexed topology and stereochemistry in both saved forms. Structural
    motifs are bounded patterns, not natural-identity or experimental assignments.
  snapshot_sha256: 1723f79377c00369ddbb345f4b472f98b3ef855db093e27f59998345d4779937
- evidence_id: bgc-2223-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json
  locator: /status; /chemistry_DATA; /chemistry_execution; /results; /unavailable
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of the original ordinary molecular diagnostic, with four
    globally unassigned warnings; scientific interpretation remains separately scoped.
  snapshot_sha256: 05cfab1ce4207e65f6e1a2f6f010bb822ee4db74b3c8277597c5b7707e04fb7a
- evidence_id: bgc-2223-native-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223/root-local-diagnostics-acceptance-001.json
  locator: /status; /native_ledger; /results; /unavailable
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: ROOT acceptance of the five original local gates; full QC and OAK remain
    unavailable as separately recorded.
  snapshot_sha256: 05cfab1ce4207e65f6e1a2f6f010bb822ee4db74b3c8277597c5b7707e04fb7a
- evidence_id: bgc-2223-query-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned mibig_compounds table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned mibig_compounds table. No query replay or external lookup.
- evidence_id: bgc-2223-source-mibig_compounds
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 201
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":201,"row_sha256":"7acaf5987f9924f07ac7945f2403baef394c8432aab65c64fd516d53117e9dd1","row":{"mibig_accession":"BGC0000154","entry_version":"4","entry_status":"active","entry_quality":"questionable","entry_completeness":"complete","compound_name":"stipitatic
    acid","compound_index":"1","smiles":"C1=C(C=C(C(=CC1=O)O)O)C(=O)O","standard_inchi":"InChI=1S/C8H6O5/c9-5-1-4(8(12)13)2-6(10)7(11)3-5/h1-3,10-11H,(H,12,13)","standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","stereo_complete":"true","compound_classes":"","database_ids":"pubchem:20501|chemspider:19955692","taxon_id":"NCBITaxon:441959","taxon_label":"Talaromyces
    stipitatus ATCC 10500","bgc_classes":"PKS","bgc_subclasses":"Iterative type I","genome_accession":"EQ962655.1","locus_from":"1805625","locus_to":"1837759","locus_evidence_methods":"Knock-out
    studies","producer_evidence_basis":"BGC_CHARACTERIZED","cluster_link_evidence_basis":"CLUSTER_DEMONSTRATED","primary_reference":"PMID:22508998","reference_basis":"ENTRY"}}]'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2223-query-chebi_structures
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned chebi_structures table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned chebi_structures table. No query replay or external lookup.
- evidence_id: bgc-2223-query-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 2 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned lotus_occurrences table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned lotus_occurrences table. No query replay or external
    lookup.
- evidence_id: bgc-2223-source-lotus_occurrences
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 10008,10009
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":10008,"row_sha256":"8458b66149b174315da1da4b43b84c35bf67ac3cd363b6a75112ab5869aad4eb","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","organism_name":"Talaromyces
    stipitatus","taxon_id":"NCBITaxon:28564","organism_wikidata":"http://www.wikidata.org/entity/Q80855389","reference_doi":"10.1006/BIOO.1995.1011","structure_wikidata":"http://www.wikidata.org/entity/Q105375286"}},{"physical_line":10009,"row_sha256":"6492eb43660599b9d29f07c1ca793af28e4b28fe2521145105e26b8b88f43bbb","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","organism_name":"Talaromyces
    stipitatus","taxon_id":"NCBITaxon:28564","organism_wikidata":"http://www.wikidata.org/entity/Q80855389","reference_doi":"10.1038/155050B0","structure_wikidata":"http://www.wikidata.org/entity/Q105375286"}}]'
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2223-query-cyanometdb_occurrences
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned cyanometdb_occurrences table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned cyanometdb_occurrences table. No query replay or external
    lookup.
- evidence_id: bgc-2223-query-npclassifier
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned npclassifier table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned npclassifier table. No query replay or external lookup.
- evidence_id: bgc-2223-source-npclassifier
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 3026
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":3026,"row_sha256":"15d41d06455b3b47a6f2585194db437aecd66d94cdd7e15426775cab69092215","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","smiles":"C1=C(C=C(C(=CC1=O)O)O)C(=O)O","pathway_results":"Shikimates
    and Phenylpropanoids","superclass_results":"Phenolic acids (C6-C1)","class_results":"Simple
    phenolic acids","is_glycoside":"false","model_version":"npclassifier.gnps2.org@2026-09-07"}}]'
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2223-query-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 1 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned pubchem_bioassay table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned pubchem_bioassay table. No query replay or external lookup.
- evidence_id: bgc-2223-source-pubchem_bioassay
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Physical TSV lines 11239
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete retained fields, including blanks, and physical frame hashes:
    [{"physical_line":11239,"row_sha256":"33c2336e631f757ce7ba47b4b6c04377937fc127b5dcc113faaa3e85134d6888","row":{"standard_inchi_key":"ZGKNMKBZOSTFCB-UHFFFAOYSA-N","cid":"20501","aid":"","assay_name":"(no
    assay data)","assay_type":"","depositor":"","activity_outcome":"","activity_name":"","activity_value_um":"","target_accession":"","reference":""}}]'
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2223-query-bindingdb_targets
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned bindingdb_targets table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned bindingdb_targets table. No query replay or external
    lookup.
- evidence_id: bgc-2223-query-antibioticmech_inchikeys
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N", against
    the exact pinned antibioticmech_inchikeys table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact complete standard_inchi_key equality, query "ZGKNMKBZOSTFCB-UHFFFAOYSA-N",
    against the exact pinned antibioticmech_inchikeys table. No query replay or external
    lookup.
- evidence_id: bgc-2223-query-chebi_origins
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Complete saved query frame with 0 positive row placements. Saved exact
    chebi_id from exact full-key structure rows, query [], against the exact pinned
    chebi_origins table. No query replay or external lookup.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
  search_scope: Saved exact chebi_id from exact full-key structure rows, query [],
    against the exact pinned chebi_origins table. No query replay or external lookup.
- evidence_id: bgc-2223-cached-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/6; /cached_taxonomy/whole_stanzas/17
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: 'Complete personally read retained name/synonym stanzas: [{"id":"NCBITaxon:28564","physical_line":12651,"complete_stanza":"[Term]\nid:
    NCBITaxon:28564\nname: Talaromyces stipitatus\nsynonym: \"Penicillium stipitatum\"
    EXACT []\n\n"},{"id":"NCBITaxon:441959","physical_line":94051,"complete_stanza":"[Term]\nid:
    NCBITaxon:441959\nname: Talaromyces stipitatus ATCC 10500\n\n"}]. No current external
    taxonomy or ancestry is inferred.'
  snapshot_sha256: 2908ca392787234d35ba65232b790613208e64ba9ee046c5977f3083ca6d2184
- evidence_id: bgc-2223-source-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch223-tentative/bgc-prep/bgc-conditional223-target-input-plan-001.json
  locator: /records/2/source_scope_inventory/source_taxa; /records/2/source_scope_inventory/forward_taxon_merge_matches;
    /records/2/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Exact selected source taxa and forward/nonorganism route sets; both match
    lists are empty in this saved scope.
  snapshot_sha256: a3557cfcaa6392d9aac60b6239f6c82e45bc199192130ebc3ab4c840c9735590
- evidence_id: bgc-2223-review-skill
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Workflow; Output
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Claim-level review, immutable records and honest partial completion under
    actual evidence-access limits.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: bgc-2223-review-profile
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Complete maintained review profile
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Producer/occurrence distinctions, evidence grades, source ownership and
    qualified computed classifications.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: bgc-2223-structure-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 376–432
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Identifier/stereo limitations and the explicit computed-not-source status
    of NPClassifier fields.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2223-activity-schema
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 632–665; lines 920–947
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Optional observation activity class and coarse backed activity buckets;
    no dedicated cell-killing definition is supplied.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2223-activity-classifier
  kind: authority
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 127–179; lines 1310–1382
  accessed_at: '2026-11-03T13:22:18.009910Z'
  support: supports
  summary: Maintained title classifier, ACTIVE-only class assignment, 25-observation
    cap and summary derivation from written observations.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:04:37.883893Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 66324cb2f94b0ce47e3f280f083307555671c644c60bd8f537eca77bd779fb7e
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:05:07.558356Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 57dad69fca1e4915ddaa2cfc5cf058591111722e4e624616dadf9a79e2ddb244
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:05:29.643887Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:06:05.240084Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-223/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-223/native-current223-five-gates-execution-001.json
  accessed_at: '2026-11-03T13:06:18.573110Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cfbaccb0dbd803cbeac03b9148b9355a7e6393913f208ea1a9c6d5c53927cf9b
assessments:
- assessment_id: bgc-2223-identity
  area: identity
  topic: Identity
  outcome: supported
  summary: The minted owner matches the single BGC0000154 v4 source compound, full
    key ZGKNMKBZOSTFCB-UHFFFAOYSA-N, and both saved molecular forms. The exact retained
    ChEBI query is empty, so the local minted grounding is preserved. There are no
    direct companion records in the admitted one-hop scope. PubChem20501 is a retained
    xref, not a freshly verified independent structure authority.
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-grounding-owner
  - bgc-2223-source-plan
  - bgc-2223-plan-acceptance
  - bgc-2223-query-chebi_structures
  - bgc-2223-source-mibig_compounds
  - bgc-2223-chemistry
  dimensions:
  - name: standard_inchi_key
    value: Full key ZGKNMKBZOSTFCB-UHFFFAOYSA-N.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2223-grounding-owner
    - bgc-2223-source-plan
    - bgc-2223-plan-acceptance
    - bgc-2223-query-chebi_structures
    - bgc-2223-source-mibig_compounds
    - bgc-2223-chemistry
  - name: grounding_scope
    value: Minted grounding supported within the exact retained source scope; PubChem
      xref not freshly resolved.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2223-grounding-owner
    - bgc-2223-source-plan
    - bgc-2223-plan-acceptance
    - bgc-2223-query-chebi_structures
    - bgc-2223-source-mibig_compounds
    - bgc-2223-chemistry
- assessment_id: bgc-2223-representation
  area: representation
  topic: Representation
  outcome: supported
  summary: Both forms give neutral C8H6O5, 13 atoms and 13 bonds with one seven-carbon
    ring and no potential stereoelements reported. All ten comparisons are true and
    the saved correspondence is complete. The true source stereochemistry flag is
    consistent with this encoded representation; it does not establish a preferred
    tautomer, protonation state in solution or experimental sample identity. The saved
    aromatic representation is kept distinct from an experimental electronic-structure
    claim.
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-chemistry
  - bgc-2223-topology
  - bgc-2223-diagnostic-acceptance
  - bgc-2223-structure-schema
  dimensions:
  - name: stereochemistry_scope
    value: No potential stereo element in either saved form; no experimental tautomer
      or solution-state claim.
    definition: Saved full stereo/atom/bond interpretation, not an experimental assignment
      or new parse.
    evidence_ids:
    - bgc-2223-chemistry
    - bgc-2223-topology
    - bgc-2223-diagnostic-acceptance
    - bgc-2223-structure-schema
  - name: representation_correspondence
    value: Ten true comparisons and complete saved match, without full natural-identity
      assertion.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2223-chemistry
    - bgc-2223-topology
    - bgc-2223-diagnostic-acceptance
    - bgc-2223-structure-schema
- assessment_id: bgc-2223-origin
  area: provenance
  topic: Origin
  outcome: supported
  summary: BGC0000154 v4 names Talaromyces stipitatus ATCC10500 (441959), BGC_CHARACTERIZED,
    with knockout-based CLUSTER_DEMONSTRATED locus support. Its source entry is active/questionable/complete
    and retains EQ962655.1 coordinates 1805625–1837759. Two LOTUS assertions refer
    to species 28564, distinct from the strain-level producer claim. The cached species
    stanza carries Penicillium stipitatum as a synonym; this is retained local name
    continuity, not a fresh taxonomic verification or a forward-merge route.
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-origin-owner
  - bgc-2223-occurrence-owner
  - bgc-2223-source-mibig_compounds
  - bgc-2223-source-lotus_occurrences
  - bgc-2223-cached-taxonomy
  - bgc-2223-source-routes
  - bgc-2223-review-profile
  dimensions:
  - name: taxon_scope
    value: Producer strain 441959 versus species occurrence 28564; cached synonym
      only.
    definition: Source taxa and cache labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2223-origin-owner
    - bgc-2223-occurrence-owner
    - bgc-2223-source-mibig_compounds
    - bgc-2223-source-lotus_occurrences
    - bgc-2223-cached-taxonomy
    - bgc-2223-source-routes
    - bgc-2223-review-profile
  - name: producer_evidence
    value: BGC_CHARACTERIZED from the retained source evidence grade.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2223-origin-owner
    - bgc-2223-occurrence-owner
    - bgc-2223-source-mibig_compounds
    - bgc-2223-source-lotus_occurrences
    - bgc-2223-cached-taxonomy
    - bgc-2223-source-routes
    - bgc-2223-review-profile
  - name: locus_evidence
    value: BGC0000154 v4 knockout-based CLUSTER_DEMONSTRATED; source quality and version
      retained.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2223-origin-owner
    - bgc-2223-occurrence-owner
    - bgc-2223-source-mibig_compounds
    - bgc-2223-source-lotus_occurrences
    - bgc-2223-cached-taxonomy
    - bgc-2223-source-routes
    - bgc-2223-review-profile
- assessment_id: bgc-2223-citations
  area: evidence
  topic: Citations
  outcome: unknown
  summary: PMID:22508998 is an entry-level MIBiG citation. The two species-level LOTUS
    assertions retain DOI:10.1006/BIOO.1995.1011 and DOI:10.1038/155050B0. Their roles
    are preserved without claiming three independent experiments or freshly confirming
    the publications. Producer, locus and occurrence claims remain separately graded.
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-origin-owner
  - bgc-2223-occurrence-owner
  - bgc-2223-assay-owner
  - bgc-2223-source-mibig_compounds
  - bgc-2223-source-lotus_occurrences
  - bgc-2223-source-pubchem_bioassay
  - bgc-2223-source-notes
  dimensions:
  - name: citation_scope
    value: One entry PMID and two occurrence DOIs; independence and original texts
      unverified.
    definition: Citation roles remain database assertions; no publication independence
      or fresh source access is assumed.
    evidence_ids:
    - bgc-2223-origin-owner
    - bgc-2223-occurrence-owner
    - bgc-2223-assay-owner
    - bgc-2223-source-mibig_compounds
    - bgc-2223-source-lotus_occurrences
    - bgc-2223-source-pubchem_bioassay
    - bgc-2223-source-notes
- assessment_id: bgc-2223-bioactivity
  area: evidence
  topic: Bioactivity
  outcome: supported
  summary: The record writes two cited occurrences for species 28564 and no assays,
    activity summary, targets or mechanisms. The one PubChem match at physical line
    11239 is a blank-AID no-assay-data sentinel for CID20501. It does not mean inactivity.
    Exact BindingDB and sibling-activity joins are empty within the saved scope; no
    biological absence is inferred.
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-assay-owner
  - bgc-2223-occurrence-owner
  - bgc-2223-query-lotus_occurrences
  - bgc-2223-source-lotus_occurrences
  - bgc-2223-query-chebi_origins
  - bgc-2223-query-pubchem_bioassay
  - bgc-2223-source-pubchem_bioassay
  - bgc-2223-query-bindingdb_targets
  - bgc-2223-query-antibioticmech_inchikeys
  - bgc-2223-source-plan
  - bgc-2223-source-routes
  - bgc-2223-cached-taxonomy
  - bgc-2223-activity-classifier
  - bgc-2223-activity-schema
  dimensions:
  - name: occurrence_scope
    value: Two species-level occurrence assertions, not two independent producer experiments.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2223-assay-owner
    - bgc-2223-occurrence-owner
    - bgc-2223-query-lotus_occurrences
    - bgc-2223-source-lotus_occurrences
    - bgc-2223-query-chebi_origins
    - bgc-2223-query-pubchem_bioassay
    - bgc-2223-source-pubchem_bioassay
    - bgc-2223-query-bindingdb_targets
    - bgc-2223-query-antibioticmech_inchikeys
    - bgc-2223-source-plan
    - bgc-2223-source-routes
    - bgc-2223-cached-taxonomy
    - bgc-2223-activity-classifier
    - bgc-2223-activity-schema
  - name: assay_target_scope
    value: One blank-AID sentinel; no written activity or target and no inactivity
      inference.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2223-assay-owner
    - bgc-2223-occurrence-owner
    - bgc-2223-query-lotus_occurrences
    - bgc-2223-source-lotus_occurrences
    - bgc-2223-query-chebi_origins
    - bgc-2223-query-pubchem_bioassay
    - bgc-2223-source-pubchem_bioassay
    - bgc-2223-query-bindingdb_targets
    - bgc-2223-query-antibioticmech_inchikeys
    - bgc-2223-source-plan
    - bgc-2223-source-routes
    - bgc-2223-cached-taxonomy
    - bgc-2223-activity-classifier
    - bgc-2223-activity-schema
- assessment_id: bgc-2223-classification
  area: consistency
  topic: Classification
  outcome: unknown
  summary: 'The complete atom and ring tables show seven carbons in the ring, a ring
    ketone, two hydroxyl substituents and a carboxylic acid: a tropolone-type scaffold.
    There is no six-carbon benzene ring or candidate sugar ring. NPClassifier nevertheless
    stores Phenolic acids (C6-C1)/Simple phenolic acids. This is an explicit model-applicability
    limitation, not a reason to overwrite the faithfully retained computed field or
    infer wrong compound identity. The source PKS/iterative-type-I classification
    and demonstrated locus support remain separate from the model filing.'
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-classification-owner
  - bgc-2223-source-npclassifier
  - bgc-2223-source-mibig_compounds
  - bgc-2223-chemistry
  - bgc-2223-topology
  - bgc-2223-structure-schema
  - bgc-2223-review-profile
  dimensions:
  - name: classification_applicability
    value: Seven-carbon tropolone ring limits computed C6-C1 phenolic-acid applicability;
      raw model field preserved.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2223-classification-owner
    - bgc-2223-source-npclassifier
    - bgc-2223-source-mibig_compounds
    - bgc-2223-chemistry
    - bgc-2223-topology
    - bgc-2223-structure-schema
    - bgc-2223-review-profile
- assessment_id: bgc-2223-completion
  area: completeness
  topic: Completion
  outcome: unknown
  summary: The complete owner/history, admitted source context, actual intake and
    all paired saved molecular tables were reviewed. No supported local curation defect
    is established within this scope. Five local gates passed, while full QC, OAK
    and external primary-source/taxonomy/accession verification were unavailable.
    The review remains partial; no record, native curation status or history was changed.
  target_ids:
  - naturalproductmech:mibig-8460498c49
  evidence_ids:
  - bgc-2223-owner
  - bgc-2223-intake
  - bgc-2223-intake-acceptance
  - bgc-2223-source-notes
  - bgc-2223-native-acceptance
  - bgc-2223-diagnostic-acceptance
  - bgc-2223-source-plan
  - bgc-2223-plan-acceptance
  - bgc-2223-review-skill
  - bgc-2223-review-profile
  dimensions:
  - name: review_completion
    value: Partial; qualified local result with external verification, full QC and
      OAK unavailable.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2223-owner
    - bgc-2223-intake
    - bgc-2223-intake-acceptance
    - bgc-2223-source-notes
    - bgc-2223-native-acceptance
    - bgc-2223-diagnostic-acceptance
    - bgc-2223-source-plan
    - bgc-2223-plan-acceptance
    - bgc-2223-review-skill
    - bgc-2223-review-profile
findings: []
actions: []
limitations:
- External identifiers, taxonomy, accessions and primary publications were not refreshed
  under the absolute no-request instruction; historical and database assertions remain
  attributed.
- Full QC and complete OAK authority coverage were unavailable. Local gates and parsing
  establish their declared mechanical scope only.
- Negative source joins apply only to the exact retained predicates and source snapshots.
  Shared loci, citations and companion records do not transfer compound-specific claims.
- No additional molecular or YAML parse occurred during fragment authoring. Source
  records, raw snapshots, native curation status and histories were not edited.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Complete selected source payloads and explicit direct-context reading attribution
  are preserved in the pinned source notes. All five owner histories, actual intakes
  and ten paired molecular tables were personally read.
- Four original diagnostic warnings remain global and unassigned; no warning is attributed
  to an individual owner.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-223
```
