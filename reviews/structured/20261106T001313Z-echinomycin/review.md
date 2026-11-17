# Local evidence review: echinomycin

- Review: 20261106T001313Z-echinomycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-05T23:31:36.900809Z
- Finished UTC: 2026-11-06T00:13:13.880449Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Echinomycin needs curation because AID1259334 is assigned an enzyme-specific class without enzyme-specific support in the retained signaling counterscreen. Its active call and measurement are accurately copied, and other enzyme-named assays separately support the overall summary. Local cyclic depsipeptide topology is supported; assay variants, incomplete stereochemistry and source grades remain qualified.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2628; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-0b86a253f1 | data/natural_products/unclassified/echinomycin.yaml | generated | echinomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-0b86a253f1 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-0b86a253f1 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-0b86a253f1 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-0b86a253f1 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-0b86a253f1 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-0b86a253f1 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-0b86a253f1 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-0b86a253f1 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identity and grounding

identity: supported. Targets: naturalproductmech:mibig-0b86a253f1.

Echinomycin retains its minted identifier, full key AUJXLBOHYWTPFV-CVLRASHMSA-N and MIBiG BGC0000339 source representation. The owner keeps PubChem cross-references 458034 and 3197; all 293 retained assay rows in the exact-key query use CID3197. These identifier placements do not by themselves resolve compound identity beyond the retained mapping. Both saved forms regenerate the declared StandardInChI and full key, supporting stored mapping without independent natural-identity verification.

### Stored forms and stereochemistry

representation: unknown. Targets: naturalproductmech:mibig-0b86a253f1.

Both neutral C51H64N12O12S2 forms retain 77 atoms and 82 bonds. The saved original ring basis has two 17-membered cycles and four aromatic six-membered rings; its eight amides and two esters support a local cyclic depsipeptide description. The two sulfur atoms are not a disulfide: S7 joins C6 and C8, while S74 joins C8 and methyl C75; the shared C8 is the sole unspecified tetrahedral center. Eight other tetrahedral centers are specified (six R and two S). Four original NH amide patterns become C(OH)=N in the reconstruction, while four N-substituted amides and both esters remain. Four reconstructed unspecified C=N entries do not add original biological stereochemistry gaps. Model Tetramate alkaloids and other family labels remain computation-specific rather than all established by these motifs. This chemistry assessment is separate from the confirmed unsupported enzyme-specific assay class. Both canonical SMILES comparisons are false and the one-way map is empty. The original atom-center flag retains the source calculation; the two global warnings are not individually assigned.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-0b86a253f1.

MIBiG BGC0000339 version 5 retains Streptomyces lasaliensis (NCBITaxon:324833) as SOURCE_ASSERTION and the AB211309.1 locus as CLUSTER_UNSTATED, with no recorded coordinate or experimental-method support. The source class is NRPS and the separate subclass is Type I. Cached Streptomyces lasalocidi with the lasaliensis synonym is nomenclatural context only. The entry remains questionable and of unknown completeness.

### Citation and history scope

evidence: supported. Targets: naturalproductmech:mibig-0b86a253f1.

ENTRY PMID:16799553 and LOTUS DOI:10.1002/HLCA.19590420127 retain distinct source roles. Assay evidence includes AID identifiers and the repeated PMID:35787375 for the AID651635 variants. Repeated rows and repeated citations are not independent experiments; no primary protocol or protein function has been freshly verified.

### Occurrence, assay and target boundaries

evidence: concern. Targets: naturalproductmech:mibig-0b86a253f1.

LOTUS occurrence in Streptomyces echinatus (NCBITaxon:67293) is distinct from the source-asserted producer. The complete retained query has 293 assay placements, 227 exact full-key/CID/AID tuples and 233 distinct full dictionaries. The owner writes 25 activities covering 24 AIDs and records the 268-result cap; omission is not inactivity. No exact retained exclusion applies. AID1259334 is a TNFa signaling counterscreen with a blank target: its ACTIVE call and 0.0005 uM AC50 are faithfully retained as OTHER with an endpoint note, but ENZYME_INHIBITOR adds unsupported specificity through a generic title rule. Other written ACTIVE FEN1 and polymerase assays remain separate backing for the overall ENZYME_INHIBITOR summary; that summary is not removed solely because this one annotation is unsupported. AID651635 retains two inconclusive 39.8107 uM Potency variants, one with Q99700 and one without. The target_enzyme field is copied on accession syntax alone; no function or enzyme mechanism is established. A tuple-only exclusion cannot satisfy the exactly-one-source-row guard for that pair.

### Classification and saved topology

consistency: unknown. Targets: naturalproductmech:mibig-0b86a253f1.

The saved original has two 17-membered cycles, four aromatic six-membered rings, eight amides and two esters, supporting a bounded cyclic depsipeptide description. Its sulfur atoms form a shared carbon-centered linkage rather than a disulfide. Computed Tetramate alkaloids and other family labels are not all validated by these motifs. Model pathways establish neither enzyme action nor biosynthesis, and the assay-class finding is assessed separately.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-0b86a253f1.

The whole selected owner/history, complete retained selected source payloads and negative query boundaries, both saved molecular forms and actual intake metadata have been read. All captured input hashes and ownership declarations agree with the accepted plan; this does not imply scientific reading of entire TSV corpora. Five local gates passed, but full QC and OAK remain unavailable and no live authority was consulted. No maintained reader applies. Completion remains partial.

## Findings

### support-2628-unsupported-enzyme-class: A signaling counterscreen is labeled as enzyme inhibition without supporting target evidence

major / open / confirmed; issue key: echinomycin-aid1259334-unsupported-enzyme-class.

The retained TNFa signaling counterscreen AID1259334 has no target accession. Its title and active AC50 observation support a signaling-assay result, but the generic inhibition-of title rule writes ENZYME_INHIBITOR to bioactivities[0].activity_class. The narrower enzyme-specific assertion is unsupported by the retained evidence. The ACTIVE call, OTHER measurement with the exact AC50 endpoint note, 0.0005 value and uM units are correctly copied and remain valid source observations. Other written ACTIVE enzyme-named assays must be assessed separately when retaining the overall activity summary. This is a bounded evidence-scope defect, not an identity or measurement defect.

Disposition: Propose a bounded maintained-seeder class-inference correction and regression coverage. Preserve raw assays and current generated records during this review.

## Recommended Actions And Acceptance Checks

### support-2628-bound-activity-class-inference

Revise the maintained activity-class inference so generic cell-signaling inhibition titles do not, by themselves, produce ENZYME_INHIBITOR. Preserve the raw AID1259334 row, active call, numeric observation, units, endpoint note and provenance. Evaluate other enzyme-specific observations separately before changing any overall summary. No source or generated-record edit is performed by this review.

- Demonstrate that the retained AID1259334 row no longer receives an enzyme-specific class solely from the generic inhibition wording, while its ACTIVE call, AC50 endpoint note and 0.0005 uM observation remain exact.
- Retain independently supported enzyme-specific written observations and recompute the overall summary from their individual backing; do not blanket-remove ENZYME_INHIBITOR.
- Preserve both AID651635 variants, their NOT_DETERMINED calls and source annotations; do not invent a protein function or use an invalid tuple-only exclusion.
- If a generator change is separately authorized, add focused regression coverage for unsupported generic signaling titles and supported enzyme-specific assays, preserve deterministic cap/provenance behavior, and run the documented strict, corpus and reproduction checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2628-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/echinomycin.yaml; Whole current plaintext including every curation_history entry | supports | Complete personally read selected owner and history; retained contents do not imply fresh source access. |
| support-2628-capture | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document | supports | Complete actual captured owner, including all written claims and absent mechanism/component roots. |
| support-2628-grounding-owner | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/identifier; /records/7/owner_document/label; /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts; /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes | supports | Exact owner-local identifier, structure and grounding/definition fields; retained mapping is distinct from natural-identity proof. |
| support-2628-provenance-owner | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/producer_taxon_groups; /records/7/owner_document/bgc_class | supports | Stored producer and locus grades, coordinates and citations are preserved as distinct assertions. |
| support-2628-citations-history | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/source_concepts; /records/7/owner_document/biosynthetic_gene_clusters; /records/7/owner_document/curation_history | supports | Exact retained source concepts, citation grain and complete seeding history; no primary-paper reopening. |
| support-2628-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups; /records/7/owner_document/xrefs | supports | Owner-local occurrence and identifier placements; no causal production inference. |
| support-2628-activity-owner | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/bioactivities; /records/7/owner_document/bioactivity_summary | supports | Complete 25 written activities and their summary, including both AID651635 variants and the retained cap note. |
| support-2628-classification-owner | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification; /records/7/owner_document/biosynthesis_origin | supports | Owner-local filing and computed classifier values; source class/subclass and local topology are separately evidenced. |
| support-2628-intake | /private/tmp/npm-review-work/shared-next-batch263/intakes-001/2628-inspect-001.json; /status; /source; /targets | supports | Actual inspection-only hashes and target ownership declarations; no scientific reading of entire captured corpus files is implied. |
| support-2628-intake-execution | /private/tmp/npm-review-work/shared-next-batch263/intakes-001/2628-inspect-execution-001.json; /exit_code; /command; /actual_environment; /stdout; /stderr | supports | Original canonical inspection exit 0 and empty stderr for this owner. |
| support-2628-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch263/root-intakes-acceptance-001.json; /accepted; /status; /summary; /source_plan_acceptance; /source_placements; /unique_source_paths | supports | ROOT accepted all ten original inspections and the exact 513 input placements across 61 paths. |
| support-2628-direct-contexts | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-target-input-plan-001.json; /records/7/proposed_companion_paths; /records/7/direct_companion_predicates; /records/7/identity_comparison_paths; /records/7/additional_context_paths; /records/7/additional_context_roles; /records/7/reader_implementation_paths; /records/7/proposed_input_paths; /records/7/proposed_input_count | supports | Exact owner-local companion and seven additional query/implementation input roles; no maintained reader applies. Capture is distinct from positive scientific evidence. |
| support-2628-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch263/root-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT acceptance of the one original operative source plan. |
| support-2628-source-reading | /private/tmp/npm-review-work/shared-next-batch263-tentative/support-prep/support-current263-assigned-source-reading-001.json; /contexts/2 | supports | Personally read every saved frame and full positive row dictionary for this owner; complete companion attribution remains separately scoped. |
| support-2628-raw-reading | /private/tmp/npm-review-work/shared-next-batch263-tentative/support-prep/support-current263-last-five-whole-owner-reading-001.json; /records/2 | supports | Support personally read this whole raw owner and all history entries; no primary source was reopened. |
| support-2628-source-notes | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Attributed reading reconciliation preserves 35 BGC plus 316 Support row placements and zero Native primary row credit, with negative, blank, cap and merge boundaries. |
| support-2628-taxonomy | /private/tmp/npm-review-work/shared-next-batch263-tentative/native-prep/native-current263-cached-taxonomy-reading-001.json; /context_interpretations/14; /interpretation; /counts | supports | Owner-local cached labels/synonyms and retained routes; no fresh rank, lineage or production authority. |
| support-2628-curation-scope | /private/tmp/npm-review-work/shared-next-batch263-tentative/native-prep/native-current263-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /interpretation; /implementation_scope | supports | Exact implemented-curation and source-identity resolution; no applicable Echinomycin exclusion or automatic correction is inferred from a lexical match. |
| support-2628-chemistry | /private/tmp/npm-review-work/shared-next-batch263/chemistry-local/diagnostic-DATA-001.json; /records/7 | supports | Complete two-form saved molecular tables, scalars, stereo, motifs and comparisons for this owner; normalized equality is not full fixed-form or natural identity proof. |
| support-2628-molecular-reading | /private/tmp/npm-review-work/shared-next-batch263-tentative/support-prep/support-current263-last-five-molecular-intake-reading-001.json; /records/2 | supports | Support personally read every saved atom/bond field and all ring, stereo and motif fields for both forms; no new molecular parse. |
| support-2628-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch263/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /scope; /denied_events | supports | ROOT acceptance of the one original diagnostic, preserving false comparisons and global warning scope. |
| support-2628-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch263/chemistry-local/diagnostic-execution-001.json; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic exit 0 with no retries; two undefined-stereo warnings remain global and are not assigned to particular owners. |
| support-2628-stereo-implementation | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142–172 | supports | The retained stereo_complete calculation uses FindMolChiralCenters with includeUnassigned=True and useLegacyImplementation=False on source SMILES; reconstructed double-bond potential stereo is outside that calculation. |
| support-2628-native-gates | /private/tmp/npm-review-work/shared-next-batch263/root-native-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | supports | Five local gates passed; full QC and OAK remain unavailable. Queue rows are leads, not scientific verdicts. |
| support-2628-reader-applicability | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-selected-mechanism-profile-001.json; /mechanisms; /selected_reader_orders | supports | Literal mechanism applicability is empty; no maintained-reader check is invented. |
| support-2628-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/mibig_compounds/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2628-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/lotus_occurrences/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2628-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame with all 1 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/npclassifier/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2628-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay query frame with all 293 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches in the pinned inventory; individual physical_line/last_physical_line/row_sha256 fields are preserved there | supports | Original retained table backing the complete saved positive payloads; detailed physical-byte and dictionary joins are in the personally read source receipt. |
| support-2628-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins query frame with all 0 row placements and full fields. A negative frame is limited to its recorded predicate; repeated rows are not independent experiments. |
| support-2628-taxon-query-scope | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/source_taxa; /contexts/14/source_scope_inventory/forward_taxon_merge_matches; /contexts/14/source_scope_inventory/nonorganism_matches | supports | Exact owner-local source taxon IDs and retained positive/negative diagnostic routes; companion route placements are not additional independent decisions. |
| support-2628-focal-assay-owner | /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json; /records/7/owner_document/bioactivities/0; /records/7/owner_document/bioactivities/13; /records/7/owner_document/bioactivities/14; /records/7/owner_document/bioactivity_summary | supports | AID1259334 class, correct observation/call, both AID651635 target-annotation variants and the separate overall summary are retained without conflation. |
| support-2628-focal-assay-row-345 | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches/28 | supports | Complete focal source row with exact title, blank or syntax-only target annotation, call, endpoint, value, units and citation; not an independent experiment inferred from row multiplicity. |
| support-2628-focal-assay-row-536 | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches/219 | supports | Complete focal source row with exact title, blank or syntax-only target annotation, call, endpoint, value, units and citation; not an independent experiment inferred from row multiplicity. |
| support-2628-focal-assay-row-537 | /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches/220 | supports | Complete focal source row with exact title, blank or syntax-only target annotation, call, endpoint, value, units and citation; not an independent experiment inferred from row multiplicity. |
| support-2628-assay-implementation | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 96–181; lines 1254–1383 | supports | Generic inhibition wording can assign ENZYME_INHIBITOR to active rows; UniProt-looking accessions populate target_enzyme on syntax. The cap, measurements and source observations remain separately preserved. |
| support-2628-assay-curation-resolution | /private/tmp/npm-review-work/shared-next-batch263-tentative/native-prep/native-current263-implemented-curation-scan-001.json; /assay_scope; /interpretation; /exact_applicability_resolution | supports | All 293 placements yield 227 tuples/233 dictionaries; no exact Echinomycin exclusion applies. The two AID651635 variants fail a tuple-only unique-source-row decision guard. |
| support-2628-activity-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; BioactivityObservation.target_enzyme and BioactivityClassEnum declarations | supports | Every activity-class value must be backed by evidence; a CURIE-shaped target field alone does not establish enzyme function. |
| support-2628-severity-rubric | /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md; lines 150–163 | supports | The retained review rubric classifies unsupported evidence and scope inflation as major; no identity or numeric-measurement defect is asserted. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-263/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-263/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-263/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-263/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-263/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained current owners, saved source payloads and the one original diagnostic only; no fresh primary-paper, sequence, protein-function or taxonomy authority.
- Both canonical comparisons are false and one-way atom maps are empty. Local amide/imidic correspondence and normalized equality do not establish full fixed-form or natural identity.
- Two original undefined-stereo warnings remain globally unassigned. Full QC and OAK are unavailable; source grades and model-family applicability remain explicit.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five complete selected owners/history and all ten saved molecular forms: 620 atom rows, 636 bond rows and 26 reported ring rows. The six assigned source contexts comprise 54 frames, 316 positive row placements and 3,486 fields; the five selected contexts contribute 311 rows and 3,436 fields. Companion and delegated context readings remain separately attributed.
- Verified 233 actual input placements across 61 paths and their target ownership declarations. Captured hashes are not scientific reading of entire underlying corpus files. No generated record, native status or history was edited and no outbound request was sent.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T001313Z-echinomycin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: echinomycin'
started_at: '2026-11-05T23:31:36.900809Z'
finished_at: '2026-11-06T00:13:13.880449Z'
reviewer:
  identity: Codex root with native_checks, bgc_science and review_support peer agents
  kind: agent
  independence: independent
  independence_basis: This review team inspected existing owner and retained source
    bytes without editing them; scientific fragments were cross-checked separately
    from their author. Local validation is not treated as scientific proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Echinomycin needs curation because AID1259334 is assigned an enzyme-specific
  class without enzyme-specific support in the retained signaling counterscreen. Its
  active call and measurement are accurately copied, and other enzyme-named assays
  separately support the overall summary. Local cyclic depsipeptide topology is supported;
  assay variants, incomplete stereochemistry and source grades remain qualified.
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
  - path: data/natural_products/unclassified/echinomycin.yaml
    sha256: 04b8b9fd7182bfcce506c48e00e5ffe7e367bc4d74401887f4a68b2f7d7683c1
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
  selection: Campaign path order 2628; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-0b86a253f1
targets:
- target_id: naturalproductmech:mibig-0b86a253f1
  path: data/natural_products/unclassified/echinomycin.yaml
  label: echinomycin
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
    role: Exact assay identity exclusion decisions for selected/direct/comparison
      source context.
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
    role: Maintained source-row identity/digest guard; text-only dependency.
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
  - naturalproductmech:mibig-0b86a253f1
  command: just validate-strict data/natural_products/unclassified/dkxanthene-548.yaml
    data/natural_products/unclassified/dkxanthene-556.yaml data/natural_products/unclassified/dkxanthene-560.yaml
    data/natural_products/unclassified/dkxanthene-574.yaml data/natural_products/unclassified/dkxanthene-586.yaml
    data/natural_products/unclassified/dkxanthene.yaml data/natural_products/unclassified/dudomycin-a.yaml
    data/natural_products/unclassified/echinomycin.yaml data/natural_products/unclassified/ecumicin.yaml
    data/natural_products/unclassified/emericellamide-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-263/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-0b86a253f1
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-263/validate-all-001.tsv
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
  - naturalproductmech:mibig-0b86a253f1
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
  - naturalproductmech:mibig-0b86a253f1
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
  - naturalproductmech:mibig-0b86a253f1
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-263/review-queue-001.tsv
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
  - naturalproductmech:mibig-0b86a253f1
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2628-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/echinomycin.yaml
  locator: Whole current plaintext including every curation_history entry
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete personally read selected owner and history; retained contents
    do not imply fresh source access.
  snapshot_sha256: 04b8b9fd7182bfcce506c48e00e5ffe7e367bc4d74401887f4a68b2f7d7683c1
- evidence_id: support-2628-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete actual captured owner, including all written claims and absent
    mechanism/component roots.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/identifier; /records/7/owner_document/label;
    /records/7/owner_document/chemical_structure; /records/7/owner_document/source_concepts;
    /records/7/owner_document/grounding_status; /records/7/owner_document/grounding_notes
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Exact owner-local identifier, structure and grounding/definition fields;
    retained mapping is distinct from natural-identity proof.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-provenance-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/producer_organisms; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/producer_taxon_groups; /records/7/owner_document/bgc_class
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Stored producer and locus grades, coordinates and citations are preserved
    as distinct assertions.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-citations-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/source_concepts; /records/7/owner_document/biosynthetic_gene_clusters;
    /records/7/owner_document/curation_history
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Exact retained source concepts, citation grain and complete seeding history;
    no primary-paper reopening.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/occurrences; /records/7/owner_document/occurrence_taxon_groups;
    /records/7/owner_document/xrefs
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Owner-local occurrence and identifier placements; no causal production
    inference.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/bioactivities; /records/7/owner_document/bioactivity_summary
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete 25 written activities and their summary, including both AID651635
    variants and the retained cap note.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/np_pathway; /records/7/owner_document/np_classification;
    /records/7/owner_document/biosynthesis_origin
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Owner-local filing and computed classifier values; source class/subclass
    and local topology are separately evidenced.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/intakes-001/2628-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Actual inspection-only hashes and target ownership declarations; no scientific
    reading of entire captured corpus files is implied.
  snapshot_sha256: 1df29d74bb60048fcc66229c40c895fefdba9682328e711619f5ad725ab2845e
- evidence_id: support-2628-intake-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/intakes-001/2628-inspect-execution-001.json
  locator: /exit_code; /command; /actual_environment; /stdout; /stderr
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Original canonical inspection exit 0 and empty stderr for this owner.
  snapshot_sha256: cd33fbc8c3ee9b2be22ddeb5300f0fb8a5c780e178ba49c0f215e572a122bda8
- evidence_id: support-2628-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/root-intakes-acceptance-001.json
  locator: /accepted; /status; /summary; /source_plan_acceptance; /source_placements;
    /unique_source_paths
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: ROOT accepted all ten original inspections and the exact 513 input placements
    across 61 paths.
  snapshot_sha256: 0d8b4d8a4ce3b6ea417c140b1361c3398d4d3da2c82447db19dd95a360b7c83b
- evidence_id: support-2628-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-target-input-plan-001.json
  locator: /records/7/proposed_companion_paths; /records/7/direct_companion_predicates;
    /records/7/identity_comparison_paths; /records/7/additional_context_paths; /records/7/additional_context_roles;
    /records/7/reader_implementation_paths; /records/7/proposed_input_paths; /records/7/proposed_input_count
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Exact owner-local companion and seven additional query/implementation input
    roles; no maintained reader applies. Capture is distinct from positive scientific
    evidence.
  snapshot_sha256: 42ce0b14d9eb7443e5518a25a35359668afb149a80e73281d561ccc2b3dba214
- evidence_id: support-2628-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: ROOT acceptance of the one original operative source plan.
  snapshot_sha256: 3cf994e1587536042cef579865e43ed724f1944581b95445f5574ebc72ad63b9
- evidence_id: support-2628-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/support-prep/support-current263-assigned-source-reading-001.json
  locator: /contexts/2
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Personally read every saved frame and full positive row dictionary for
    this owner; complete companion attribution remains separately scoped.
  snapshot_sha256: 16d9469a8fb245a90ee0db935a7e48152bf5b830615e9c6607518d0ec5a5ae93
- evidence_id: support-2628-raw-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/support-prep/support-current263-last-five-whole-owner-reading-001.json
  locator: /records/2
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Support personally read this whole raw owner and all history entries; no
    primary source was reopened.
  snapshot_sha256: 1ecb42dc617a04f3c6bdeeaf089d29de9cae8ecf26a7a4280df38f52db94f1ee
- evidence_id: support-2628-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Attributed reading reconciliation preserves 35 BGC plus 316 Support row
    placements and zero Native primary row credit, with negative, blank, cap and merge
    boundaries.
  snapshot_sha256: 958ce6ca56fa280953d232599313e76b916354016bf7361b393b1f6c065a21a2
- evidence_id: support-2628-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/native-prep/native-current263-cached-taxonomy-reading-001.json
  locator: /context_interpretations/14; /interpretation; /counts
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Owner-local cached labels/synonyms and retained routes; no fresh rank,
    lineage or production authority.
  snapshot_sha256: f3d919a870d2983afabae8745a0bc44b3c6ab9801b8e9fb1221c5f8f75939578
- evidence_id: support-2628-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/native-prep/native-current263-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /interpretation; /implementation_scope
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Exact implemented-curation and source-identity resolution; no applicable
    Echinomycin exclusion or automatic correction is inferred from a lexical match.
  snapshot_sha256: 0eb9b07541b1658a2044c4af3115e90a4f28c665c89dd390acec7161f451f8ac
  search_scope: '{"owner": "data/natural_products/unclassified/echinomycin.yaml",
    "primary_source_row_credit": 0, "scope": "Retained exact identity/digest predicates;
    lexical candidates remain separate"}'
- evidence_id: support-2628-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/chemistry-local/diagnostic-DATA-001.json
  locator: /records/7
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete two-form saved molecular tables, scalars, stereo, motifs and comparisons
    for this owner; normalized equality is not full fixed-form or natural identity
    proof.
  snapshot_sha256: 27b46c3b911d92a8fae9bef5171b15880ef1cfcb89abee0ae33f78e437a2ba65
- evidence_id: support-2628-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/support-prep/support-current263-last-five-molecular-intake-reading-001.json
  locator: /records/2
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Support personally read every saved atom/bond field and all ring, stereo
    and motif fields for both forms; no new molecular parse.
  snapshot_sha256: a82fc654f71907d619b9fea9b6eabda93cbcc2a768993539b866ef45bb2c7902
- evidence_id: support-2628-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /scope; /denied_events
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: ROOT acceptance of the one original diagnostic, preserving false comparisons
    and global warning scope.
  snapshot_sha256: 6d96c20dfd550d6b6656e6eb4943ad3f8e1ce96a1324d0f9a14a3980171664f6
- evidence_id: support-2628-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Original diagnostic exit 0 with no retries; two undefined-stereo warnings
    remain global and are not assigned to particular owners.
  snapshot_sha256: 5872bb04df87d6f73e974dbc8a91154adb3e74459df7fb151de8bc7ffe856952
- evidence_id: support-2628-stereo-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142–172
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: The retained stereo_complete calculation uses FindMolChiralCenters with
    includeUnassigned=True and useLegacyImplementation=False on source SMILES; reconstructed
    double-bond potential stereo is outside that calculation.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2628-native-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch263/root-native-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_rows
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Five local gates passed; full QC and OAK remain unavailable. Queue rows
    are leads, not scientific verdicts.
  snapshot_sha256: 09ad392a719242a0dc5085e3214db69ccb97662d3eef472dcd8a9253beb14cbf
- evidence_id: support-2628-reader-applicability
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-selected-mechanism-profile-001.json
  locator: /mechanisms; /selected_reader_orders
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Literal mechanism applicability is empty; no maintained-reader check is
    invented.
  snapshot_sha256: 403fc8c2ed67df460ffd35c4e48b87127311b8ce891f611d4d768981ed394b90
- evidence_id: support-2628-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved mibig_compounds query frame with all 1 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/mibig_compounds/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2628-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved chebi_structures query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved lotus_occurrences query frame with all 1 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/lotus_occurrences/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2628-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved npclassifier query frame with all 1 row placements and full
    fields. A negative frame is limited to its recorded predicate; repeated rows are
    not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/npclassifier/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2628-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved pubchem_bioassay query frame with all 293 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 293, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Complete selected physical row chunks and dictionaries retained at /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches
    in the pinned inventory; individual physical_line/last_physical_line/row_sha256
    fields are preserved there
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Original retained table backing the complete saved positive payloads; detailed
    physical-byte and dictionary joins are in the personally read source receipt.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2628-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved bindingdb_targets query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys query frame with all 0 row placements
    and full fields. A negative frame is limited to its recorded predicate; repeated
    rows are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "AUJXLBOHYWTPFV-CVLRASHMSA-N"}'
- evidence_id: support-2628-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete saved chebi_origins query frame with all 0 row placements and
    full fields. A negative frame is limited to its recorded predicate; repeated rows
    are not independent experiments.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"matched_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": []}'
- evidence_id: support-2628-taxon-query-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/source_taxa; /contexts/14/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/14/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Exact owner-local source taxon IDs and retained positive/negative diagnostic
    routes; companion route placements are not additional independent decisions.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
  search_scope: '{"forward_merge_placements": 0, "nonorganism_placements": 0, "predicate":
    "Exact retained taxon IDs against both captured diagnostic tables", "source_taxa":
    ["NCBITaxon:324833", "NCBITaxon:67293"]}'
- evidence_id: support-2628-focal-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263/owner-capture-DATA-001.json
  locator: /records/7/owner_document/bioactivities/0; /records/7/owner_document/bioactivities/13;
    /records/7/owner_document/bioactivities/14; /records/7/owner_document/bioactivity_summary
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: AID1259334 class, correct observation/call, both AID651635 target-annotation
    variants and the separate overall summary are retained without conflation.
  snapshot_sha256: 1597e94741ee1b16f7aad6240dd408c7f664aaa08014a4e530afb4b654117dd0
- evidence_id: support-2628-focal-assay-row-345
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches/28
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete focal source row with exact title, blank or syntax-only target
    annotation, call, endpoint, value, units and citation; not an independent experiment
    inferred from row multiplicity.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
- evidence_id: support-2628-focal-assay-row-536
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches/219
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete focal source row with exact title, blank or syntax-only target
    annotation, call, endpoint, value, units and citation; not an independent experiment
    inferred from row multiplicity.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
- evidence_id: support-2628-focal-assay-row-537
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/bgc-prep/bgc-conditional263-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay/matches/220
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Complete focal source row with exact title, blank or syntax-only target
    annotation, call, endpoint, value, units and citation; not an independent experiment
    inferred from row multiplicity.
  snapshot_sha256: 33b56385b9bcce8867a19dcd4dacaefdff38365f5976f4e45e28bff2023c7966
- evidence_id: support-2628-assay-implementation
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 96–181; lines 1254–1383
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Generic inhibition wording can assign ENZYME_INHIBITOR to active rows;
    UniProt-looking accessions populate target_enzyme on syntax. The cap, measurements
    and source observations remain separately preserved.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2628-assay-curation-resolution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch263-tentative/native-prep/native-current263-implemented-curation-scan-001.json
  locator: /assay_scope; /interpretation; /exact_applicability_resolution
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: All 293 placements yield 227 tuples/233 dictionaries; no exact Echinomycin
    exclusion applies. The two AID651635 variants fail a tuple-only unique-source-row
    decision guard.
  snapshot_sha256: 0eb9b07541b1658a2044c4af3115e90a4f28c665c89dd390acec7161f451f8ac
- evidence_id: support-2628-activity-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: BioactivityObservation.target_enzyme and BioactivityClassEnum declarations
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: Every activity-class value must be backed by evidence; a CURIE-shaped target
    field alone does not establish enzyme function.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2628-severity-rubric
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/.claude/skills/review-yaml-record/SKILL.md
  locator: lines 150–163
  accessed_at: '2026-11-06T00:08:25.876016Z'
  support: supports
  summary: The retained review rubric classifies unsupported evidence and scope inflation
    as major; no identity or numeric-measurement defect is asserted.
  snapshot_sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-263/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json
  accessed_at: '2026-11-05T23:37:07.979176Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: f0099bfc6141966d1735f2f4c523cd1d334b8ac2a30815971aafca3d432a1f25
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-263/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json
  accessed_at: '2026-11-05T23:37:33.931844Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 18b28cb1da9e42e0325539f2b40add91511b2366ff5b5f029471f34697e12ceb
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-263/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json
  accessed_at: '2026-11-05T23:37:54.471670Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-263/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json
  accessed_at: '2026-11-05T23:38:29.513844Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-263/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-263/native-current263-five-gates-execution-001.json
  accessed_at: '2026-11-05T23:38:41.503684Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f24874c6c441edace808e210d5021ad11f9ded18d17a5af6b331a0076a835dc2
assessments:
- area: identity
  topic: Retained identity and grounding
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key; no prefix or name substitution.
    value: AUJXLBOHYWTPFV-CVLRASHMSA-N
    evidence_ids:
    - support-2628-grounding-owner
    - support-2628-chemistry
    - support-2628-query-mibig_compounds
    - support-2628-query-chebi_structures
    - support-2628-direct-contexts
    - support-2628-source-reading
  - name: grounding_scope
    definition: Stored grounding fidelity is distinct from fresh natural-identity
      verification.
    value: MINTED retained mapping; no independent natural-identity proof
    evidence_ids:
    - support-2628-grounding-owner
    - support-2628-chemistry
    - support-2628-query-mibig_compounds
    - support-2628-query-chebi_structures
    - support-2628-direct-contexts
    - support-2628-source-reading
  assessment_id: support-2628-identity
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-grounding-owner
  - support-2628-chemistry
  - support-2628-query-mibig_compounds
  - support-2628-query-chebi_structures
  - support-2628-direct-contexts
  - support-2628-source-reading
  outcome: supported
  summary: Echinomycin retains its minted identifier, full key AUJXLBOHYWTPFV-CVLRASHMSA-N
    and MIBiG BGC0000339 source representation. The owner keeps PubChem cross-references
    458034 and 3197; all 293 retained assay rows in the exact-key query use CID3197.
    These identifier placements do not by themselves resolve compound identity beyond
    the retained mapping. Both saved forms regenerate the declared StandardInChI and
    full key, supporting stored mapping without independent natural-identity verification.
- area: representation
  topic: Stored forms and stereochemistry
  dimensions:
  - name: stereochemistry_scope
    definition: Saved original atom-center and double-bond scope; no natural stereochemistry
      proof.
    value: 8 specified (6 R/2 S) + 1 unspecified tetrahedral center
    evidence_ids:
    - support-2628-grounding-owner
    - support-2628-chemistry
    - support-2628-molecular-reading
    - support-2628-diagnostic-acceptance
    - support-2628-diagnostic-execution
    - support-2628-stereo-implementation
  - name: representation_correspondence
    definition: Normalized InChI/key agreement does not prove full fixed-form graph
      equivalence.
    value: 8/10 flags; 4 imidic changes; unequal canonical strings/empty map
    evidence_ids:
    - support-2628-grounding-owner
    - support-2628-chemistry
    - support-2628-molecular-reading
    - support-2628-diagnostic-acceptance
    - support-2628-diagnostic-execution
    - support-2628-stereo-implementation
  assessment_id: support-2628-representation
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-grounding-owner
  - support-2628-chemistry
  - support-2628-molecular-reading
  - support-2628-diagnostic-acceptance
  - support-2628-diagnostic-execution
  - support-2628-stereo-implementation
  outcome: unknown
  summary: 'Both neutral C51H64N12O12S2 forms retain 77 atoms and 82 bonds. The saved
    original ring basis has two 17-membered cycles and four aromatic six-membered
    rings; its eight amides and two esters support a local cyclic depsipeptide description.
    The two sulfur atoms are not a disulfide: S7 joins C6 and C8, while S74 joins
    C8 and methyl C75; the shared C8 is the sole unspecified tetrahedral center. Eight
    other tetrahedral centers are specified (six R and two S). Four original NH amide
    patterns become C(OH)=N in the reconstruction, while four N-substituted amides
    and both esters remain. Four reconstructed unspecified C=N entries do not add
    original biological stereochemistry gaps. Model Tetramate alkaloids and other
    family labels remain computation-specific rather than all established by these
    motifs. This chemistry assessment is separate from the confirmed unsupported enzyme-specific
    assay class. Both canonical SMILES comparisons are false and the one-way map is
    empty. The original atom-center flag retains the source calculation; the two global
    warnings are not individually assigned.'
- area: provenance
  topic: Producer, taxonomy and locus grades
  dimensions:
  - name: taxon_scope
    definition: Cached IDs/names/synonyms are distinct from verified rank, lineage
      or strain identity.
    value: 324833 producer; 67293 occurrence; cached synonym context only
    evidence_ids:
    - support-2628-provenance-owner
    - support-2628-taxonomy
    - support-2628-taxon-query-scope
    - support-2628-curation-scope
    - support-2628-query-mibig_compounds
  - name: producer_evidence
    definition: Retained producer grade, not inferred from occurrence or locus association.
    value: SOURCE_ASSERTION; BGC0000339 v5
    evidence_ids:
    - support-2628-provenance-owner
    - support-2628-taxonomy
    - support-2628-taxon-query-scope
    - support-2628-curation-scope
    - support-2628-query-mibig_compounds
  - name: locus_evidence
    definition: Retained compound-specific cluster-link grade and source methods.
    value: CLUSTER_UNSTATED; AB211309.1; coordinates/methods blank
    evidence_ids:
    - support-2628-provenance-owner
    - support-2628-taxonomy
    - support-2628-taxon-query-scope
    - support-2628-curation-scope
    - support-2628-query-mibig_compounds
  assessment_id: support-2628-provenance
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-provenance-owner
  - support-2628-taxonomy
  - support-2628-taxon-query-scope
  - support-2628-curation-scope
  - support-2628-query-mibig_compounds
  outcome: supported
  summary: MIBiG BGC0000339 version 5 retains Streptomyces lasaliensis (NCBITaxon:324833)
    as SOURCE_ASSERTION and the AB211309.1 locus as CLUSTER_UNSTATED, with no recorded
    coordinate or experimental-method support. The source class is NRPS and the separate
    subclass is Type I. Cached Streptomyces lasalocidi with the lasaliensis synonym
    is nomenclatural context only. The entry remains questionable and of unknown completeness.
- area: evidence
  topic: Citation and history scope
  dimensions:
  - name: citation_scope
    definition: Exact retained citation basis; no implied new primary-source access.
    value: PMID:16799553 [ENTRY]; assay references retained, not independent experiments
    evidence_ids:
    - support-2628-citations-history
    - support-2628-source-reading
    - support-2628-source-notes
    - support-2628-source-mibig_compounds
    - support-2628-source-lotus_occurrences
    - support-2628-source-npclassifier
    - support-2628-source-pubchem_bioassay
    - support-2628-query-mibig_compounds
    - support-2628-query-chebi_structures
    - support-2628-query-lotus_occurrences
    - support-2628-query-cyanometdb_occurrences
    - support-2628-query-npclassifier
    - support-2628-query-pubchem_bioassay
    - support-2628-query-bindingdb_targets
    - support-2628-query-antibioticmech_inchikeys
    - support-2628-query-chebi_origins
  assessment_id: support-2628-citations
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-citations-history
  - support-2628-source-reading
  - support-2628-source-notes
  - support-2628-source-mibig_compounds
  - support-2628-source-lotus_occurrences
  - support-2628-source-npclassifier
  - support-2628-source-pubchem_bioassay
  - support-2628-query-mibig_compounds
  - support-2628-query-chebi_structures
  - support-2628-query-lotus_occurrences
  - support-2628-query-cyanometdb_occurrences
  - support-2628-query-npclassifier
  - support-2628-query-pubchem_bioassay
  - support-2628-query-bindingdb_targets
  - support-2628-query-antibioticmech_inchikeys
  - support-2628-query-chebi_origins
  outcome: supported
  summary: ENTRY PMID:16799553 and LOTUS DOI:10.1002/HLCA.19590420127 retain distinct
    source roles. Assay evidence includes AID identifiers and the repeated PMID:35787375
    for the AID651635 variants. Repeated rows and repeated citations are not independent
    experiments; no primary protocol or protein function has been freshly verified.
- area: evidence
  topic: Occurrence, assay and target boundaries
  dimensions:
  - name: occurrence_scope
    definition: Source placements and shared citations are not independent production
      experiments.
    value: 1 LOTUS occurrence; 293 assay rows are not 293 independent experiments
    evidence_ids:
    - support-2628-occurrence-owner
    - support-2628-activity-owner
    - support-2628-source-reading
    - support-2628-curation-scope
    - support-2628-taxon-query-scope
    - support-2628-source-mibig_compounds
    - support-2628-source-lotus_occurrences
    - support-2628-source-npclassifier
    - support-2628-source-pubchem_bioassay
    - support-2628-query-mibig_compounds
    - support-2628-query-chebi_structures
    - support-2628-query-lotus_occurrences
    - support-2628-query-cyanometdb_occurrences
    - support-2628-query-npclassifier
    - support-2628-query-pubchem_bioassay
    - support-2628-query-bindingdb_targets
    - support-2628-query-antibioticmech_inchikeys
    - support-2628-query-chebi_origins
    - support-2628-focal-assay-owner
    - support-2628-focal-assay-row-345
    - support-2628-focal-assay-row-536
    - support-2628-focal-assay-row-537
    - support-2628-assay-implementation
    - support-2628-assay-curation-resolution
    - support-2628-activity-schema
    - support-2628-severity-rubric
  - name: assay_target_scope
    definition: Actual AIDs, blank sentinels and bounded negative target queries remain
      distinct.
    value: 293 rows/227 tuples/233 dictionaries; 25 written; AID1259334 class unsupported
    evidence_ids:
    - support-2628-occurrence-owner
    - support-2628-activity-owner
    - support-2628-source-reading
    - support-2628-curation-scope
    - support-2628-taxon-query-scope
    - support-2628-source-mibig_compounds
    - support-2628-source-lotus_occurrences
    - support-2628-source-npclassifier
    - support-2628-source-pubchem_bioassay
    - support-2628-query-mibig_compounds
    - support-2628-query-chebi_structures
    - support-2628-query-lotus_occurrences
    - support-2628-query-cyanometdb_occurrences
    - support-2628-query-npclassifier
    - support-2628-query-pubchem_bioassay
    - support-2628-query-bindingdb_targets
    - support-2628-query-antibioticmech_inchikeys
    - support-2628-query-chebi_origins
    - support-2628-focal-assay-owner
    - support-2628-focal-assay-row-345
    - support-2628-focal-assay-row-536
    - support-2628-focal-assay-row-537
    - support-2628-assay-implementation
    - support-2628-assay-curation-resolution
    - support-2628-activity-schema
    - support-2628-severity-rubric
  assessment_id: support-2628-occurrence-activity
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-occurrence-owner
  - support-2628-activity-owner
  - support-2628-source-reading
  - support-2628-curation-scope
  - support-2628-taxon-query-scope
  - support-2628-source-mibig_compounds
  - support-2628-source-lotus_occurrences
  - support-2628-source-npclassifier
  - support-2628-source-pubchem_bioassay
  - support-2628-query-mibig_compounds
  - support-2628-query-chebi_structures
  - support-2628-query-lotus_occurrences
  - support-2628-query-cyanometdb_occurrences
  - support-2628-query-npclassifier
  - support-2628-query-pubchem_bioassay
  - support-2628-query-bindingdb_targets
  - support-2628-query-antibioticmech_inchikeys
  - support-2628-query-chebi_origins
  - support-2628-focal-assay-owner
  - support-2628-focal-assay-row-345
  - support-2628-focal-assay-row-536
  - support-2628-focal-assay-row-537
  - support-2628-assay-implementation
  - support-2628-assay-curation-resolution
  - support-2628-activity-schema
  - support-2628-severity-rubric
  outcome: concern
  summary: 'LOTUS occurrence in Streptomyces echinatus (NCBITaxon:67293) is distinct
    from the source-asserted producer. The complete retained query has 293 assay placements,
    227 exact full-key/CID/AID tuples and 233 distinct full dictionaries. The owner
    writes 25 activities covering 24 AIDs and records the 268-result cap; omission
    is not inactivity. No exact retained exclusion applies. AID1259334 is a TNFa signaling
    counterscreen with a blank target: its ACTIVE call and 0.0005 uM AC50 are faithfully
    retained as OTHER with an endpoint note, but ENZYME_INHIBITOR adds unsupported
    specificity through a generic title rule. Other written ACTIVE FEN1 and polymerase
    assays remain separate backing for the overall ENZYME_INHIBITOR summary; that
    summary is not removed solely because this one annotation is unsupported. AID651635
    retains two inconclusive 39.8107 uM Potency variants, one with Q99700 and one
    without. The target_enzyme field is copied on accession syntax alone; no function
    or enzyme mechanism is established. A tuple-only exclusion cannot satisfy the
    exactly-one-source-row guard for that pair.'
- area: consistency
  topic: Classification and saved topology
  dimensions:
  - name: classification_applicability
    definition: Local encoded topology can support a broad description without validating
      a model-derived pathway or natural identity.
    value: Cyclic depsipeptide topology; 8 amides/2 esters; model families qualified
    evidence_ids:
    - support-2628-classification-owner
    - support-2628-chemistry
    - support-2628-molecular-reading
    - support-2628-query-npclassifier
    - support-2628-query-mibig_compounds
  assessment_id: support-2628-classification
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-classification-owner
  - support-2628-chemistry
  - support-2628-molecular-reading
  - support-2628-query-npclassifier
  - support-2628-query-mibig_compounds
  outcome: unknown
  summary: The saved original has two 17-membered cycles, four aromatic six-membered
    rings, eight amides and two esters, supporting a bounded cyclic depsipeptide description.
    Its sulfur atoms form a shared carbon-centered linkage rather than a disulfide.
    Computed Tetramate alkaloids and other family labels are not all validated by
    these motifs. Model pathways establish neither enzyme action nor biosynthesis,
    and the assay-class finding is assessed separately.
- area: completeness
  topic: Scientific completion and ownership
  dimensions:
  - name: review_completion
    definition: Coverage of a whole record is distinct from all required checks and
      independent external verification.
    value: partial; 5 local gates passed; QC/OAK unavailable; zero readers
    evidence_ids:
    - support-2628-owner
    - support-2628-capture
    - support-2628-intake
    - support-2628-intake-execution
    - support-2628-intake-acceptance
    - support-2628-plan-acceptance
    - support-2628-source-reading
    - support-2628-raw-reading
    - support-2628-source-notes
    - support-2628-diagnostic-acceptance
    - support-2628-molecular-reading
    - support-2628-native-gates
    - support-2628-reader-applicability
  assessment_id: support-2628-completion
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-owner
  - support-2628-capture
  - support-2628-intake
  - support-2628-intake-execution
  - support-2628-intake-acceptance
  - support-2628-plan-acceptance
  - support-2628-source-reading
  - support-2628-raw-reading
  - support-2628-source-notes
  - support-2628-diagnostic-acceptance
  - support-2628-molecular-reading
  - support-2628-native-gates
  - support-2628-reader-applicability
  outcome: unknown
  summary: The whole selected owner/history, complete retained selected source payloads
    and negative query boundaries, both saved molecular forms and actual intake metadata
    have been read. All captured input hashes and ownership declarations agree with
    the accepted plan; this does not imply scientific reading of entire TSV corpora.
    Five local gates passed, but full QC and OAK remain unavailable and no live authority
    was consulted. No maintained reader applies. Completion remains partial.
findings:
- finding_id: support-2628-unsupported-enzyme-class
  issue_key: echinomycin-aid1259334-unsupported-enzyme-class
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: A signaling counterscreen is labeled as enzyme inhibition without supporting
    target evidence
  description: The retained TNFa signaling counterscreen AID1259334 has no target
    accession. Its title and active AC50 observation support a signaling-assay result,
    but the generic inhibition-of title rule writes ENZYME_INHIBITOR to bioactivities[0].activity_class.
    The narrower enzyme-specific assertion is unsupported by the retained evidence.
    The ACTIVE call, OTHER measurement with the exact AC50 endpoint note, 0.0005 value
    and uM units are correctly copied and remain valid source observations. Other
    written ACTIVE enzyme-named assays must be assessed separately when retaining
    the overall activity summary. This is a bounded evidence-scope defect, not an
    identity or measurement defect.
  field_paths:
  - bioactivities[0].activity_class
  rule_id: review-yaml-record:major-unsupported-evidence-scope
  native_severity: major
  normalization_reason: The review rubric treats unsupported evidence and scope inflation
    as major. The enzyme-specific class exceeds the retained cell-signaling evidence;
    identity, measurement and parse integrity are not challenged.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained activity-class inference and generated bioactivity assertions;
      source observations remain preserved.
  disposition_reason: Propose a bounded maintained-seeder class-inference correction
    and regression coverage. Preserve raw assays and current generated records during
    this review.
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  evidence_ids:
  - support-2628-focal-assay-owner
  - support-2628-focal-assay-row-345
  - support-2628-focal-assay-row-536
  - support-2628-focal-assay-row-537
  - support-2628-assay-implementation
  - support-2628-assay-curation-resolution
  - support-2628-activity-schema
  - support-2628-severity-rubric
  - support-2628-activity-owner
  - support-2628-query-pubchem_bioassay
actions:
- action_id: support-2628-bound-activity-class-inference
  description: Revise the maintained activity-class inference so generic cell-signaling
    inhibition titles do not, by themselves, produce ENZYME_INHIBITOR. Preserve the
    raw AID1259334 row, active call, numeric observation, units, endpoint note and
    provenance. Evaluate other enzyme-specific observations separately before changing
    any overall summary. No source or generated-record edit is performed by this review.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained activity-class inference and generated bioactivity assertions;
      source observations remain preserved.
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Demonstrate that the retained AID1259334 row no longer receives an enzyme-specific
    class solely from the generic inhibition wording, while its ACTIVE call, AC50
    endpoint note and 0.0005 uM observation remain exact.
  - Retain independently supported enzyme-specific written observations and recompute
    the overall summary from their individual backing; do not blanket-remove ENZYME_INHIBITOR.
  - Preserve both AID651635 variants, their NOT_DETERMINED calls and source annotations;
    do not invent a protein function or use an invalid tuple-only exclusion.
  - If a generator change is separately authorized, add focused regression coverage
    for unsupported generic signaling titles and supported enzyme-specific assays,
    preserve deterministic cap/provenance behavior, and run the documented strict,
    corpus and reproduction checks.
  target_ids:
  - naturalproductmech:mibig-0b86a253f1
  finding_ids:
  - support-2628-unsupported-enzyme-class
limitations:
- Retained current owners, saved source payloads and the one original diagnostic only;
  no fresh primary-paper, sequence, protein-function or taxonomy authority.
- Both canonical comparisons are false and one-way atom maps are empty. Local amide/imidic
  correspondence and normalized equality do not establish full fixed-form or natural
  identity.
- Two original undefined-stereo warnings remain globally unassigned. Full QC and OAK
  are unavailable; source grades and model-family applicability remain explicit.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'Support personally read five complete selected owners/history and all ten saved
  molecular forms: 620 atom rows, 636 bond rows and 26 reported ring rows. The six
  assigned source contexts comprise 54 frames, 316 positive row placements and 3,486
  fields; the five selected contexts contribute 311 rows and 3,436 fields. Companion
  and delegated context readings remain separately attributed.'
- Verified 233 actual input placements across 61 paths and their target ownership
  declarations. Captured hashes are not scientific reading of entire underlying corpus
  files. No generated record, native status or history was edited and no outbound
  request was sent.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-263
```
