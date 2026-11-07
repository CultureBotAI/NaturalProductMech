# Local evidence review: Kutzneride 4

- Review: 20261106T170757Z-kutzneride-4
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T16:14:29.039088Z
- Finished UTC: 2026-11-06T17:07:57.291845Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Kutzneride4 retains its distinct unsaturated congener identity and source-specific provenance. Two precursor chlorination steps are faithfully resolved, but do not establish full assembly. Three amide/imidic differences, empty correspondence and unavailable external checks keep this qualified pass partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2737; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-8e920fa3c9 | data/natural_products/unclassified/kutzneride-4.yaml | generated | Kutzneride 4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-8e920fa3c9 | Original stored-form parsing succeeded with formula, charge, StandardInChI and declared full-key agreement. |
| Complete offline maintained reader for kutzneride-4 | passed | True | naturalproductmech:mibig-8e920fa3c9 | One original offline maintained call preserved the complete owner: two graphs, six nodes, four edges, two numbered steps, thirty evidence placements and four histories; no components. |
| strict_ten | passed | True | naturalproductmech:mibig-8e920fa3c9 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-8e920fa3c9 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-8e920fa3c9 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-8e920fa3c9 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-8e920fa3c9 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-8e920fa3c9 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-8e920fa3c9 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-8e920fa3c9 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained congener identity and grounding

identity: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

MIBiG BGC0000378 version5 compound-4 preserves Kutzneride 4, full key IURQCOHKGOZHQD-QLXFUGDFSA-N and npatlas:NPA007816. The empty retained exact-key ChEBI query supports only this captured MINTED route; it does not establish universal absence or verified natural identity. Its unsaturated N–N side ring and two fewer hydrogens distinguish it from Kutzneride3; the common stereochemical key suffix does not merge these full keys.

### Stored forms and stereochemical limits

representation: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

Both stored forms regenerate the declared StandardInChI/full key and neutral formula C37H47Cl2N7O12, with 58 atoms and 63 bonds each. Every saved atom has formal charge zero and no isotopic label. Both canonical isomeric and nonisomeric comparisons are false; the limited map is empty, complete_atom_count_match is false and full_graph_identity_established remains false. Seven carbonyls and five strict amides in the SMILES become four carbonyls and two strict amides, with three terminal C(OH)=N motifs in the reconstructed form (each O has degree1 and H1). The one macrocyclic ester and terminal carboxylic acid persist. Nine specified tetrahedral centres in each form; three reconstructed C=N entries are unspecified. The pre-existing C=N in the six-member N–N ring is not listed as potential double-bond stereo. The source-form cyclic C=N at bond15 (C15–N16) persists as a separate motif from the three newly represented imines; its corresponding reconstructed bond is14 (C11–N39). Those form-specific indices are not an atom map. Relative to Kutzneride3, the formula contains two fewer hydrogens and the full key differs. Two stderr warnings belong to the shared run and are not assigned to this record.

### Producer, taxonomy and locus grades

provenance: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

The producer Kutzneria sp. 744 / NCBITaxon:345341 remains SOURCE_ASSERTION, while its BGC0000378 v5 / genbank:EU074211.1 association separately remains CLUSTER_UNSTATED. The exact MIBiG row is active/questionable with unknown completeness, blank locus coordinates and no stated locus evidence methods. Shared cluster membership and curated precursor-enzyme annotations do not upgrade either grade or establish congener-specific production. Cached labels corroborate retained ID/name routes only; current strain, lineage and sequence identity were not independently verified.

### Citation grain and historical authority

evidence: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

DOI:10.1021/np050378g is the COMPOUND_EVIDENCE citation retained for the MIBiG producer/locus claim. Occurrence citations retain their own row grain. Four history events comprise two seeder events (2026-09-10 and2026-09-25) and two Codex precursor graph/pathway curations (2026-10-02 or03). Historical PRIMARY_EXPERIMENT labels, quotations and 2026-10-02 retrieval dates for KtzQ/R are attributed annotations. The DOI:10.1021/ja806467a paper and MITE/UniProt/GenPept/GenBank bodies were not independently inspected in this offline review, so no new primary, sequence or database authority is claimed.

### Occurrence, assay and target boundaries

evidence: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

Two LOTUS placements report genus Kutzneria / NCBITaxon:43356, with DOI:10.1021/NP050378G and DOI:10.1021/NP0604331. These are distinct occurrence/reference rows, not two strain-level production experiments; the producer remains the separate Kutzneria sp.744 /345341 source claim. All saved exact-key PubChem BioAssay, BindingDB, CyanometDB and related AntibioticMech queries are empty, with no actual AID and no blank-AID sentinel. ChEBI origins has an empty predicate list because no ChEBI structure matched. These bounds do not establish inactivity or a complete biological-target survey; no molecular-target root is present.

### Classification and encoded topology

consistency: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

The blank MIBiG compound_classes field is faithfully retained; it is not automatically a required-class defect. Source NRPS and separate Type I subclass text are not a new PKS assertion. NPClassifier predicts Oligopeptides, Cyclic peptides and Depsipeptides with is_glycoside:false. Its two pathways, Amino acids and Peptides plus Polyketides, intentionally produce UNCLASSIFIED filing under choose_pathway295–306. The source-form amides and ester within the 18-member macrocycle support a broad cyclic depsipeptide topology. Both forms have ring sizes3,5,5,6,6,18; no C5O candidate sugar ring is reported. Two broad carbon–O–carbon bridges include the ester and an ether and do not imply two glycosidic links. These encoded motifs qualify the model output without proving a biosynthetic pathway, residue names or natural identity.

### Precursor enzyme mechanism and complete reader scope

graph: supported. Targets: naturalproductmech:mibig-8e920fa3c9.

The actual maintained call preserves two inline BIOSYNTHESIS graphs (six nodes/four edges/twenty evidence placements), two numbered pathway steps (ten evidence placements), and all four histories, with no components or molecular targets. Their bounded meaning is sequential free-tryptophan precursor chlorination: KtzQ / UniProtKB:A8CF75 / GenPept ABV56597.1 / MITE0000029 at RHEA:26494, followed by KtzR / A8CF74 / ABV56598.1 / MITE0000030 at RHEA:55904. KtzS is expressly outside the KtzQ-specific graph. Graph chemical IDs CHEBI:16828→47356→140086 and pathway forms CHEBI:57912→58713→139336 are distinct retained representations, not synonyms or newly verified charge-form equivalences; pathway cofactors/products also remain intact. The repeated DOI:10.1021/ja806467a and historical database references support the attributed precursor narrative only at its recorded scope. No full-congener assembly, fresh enzyme sequence/construct attribution, independent PRIMARY_EXPERIMENT verification or complete ontology grounding is established by the reader. KtzA/D material from Kutzneride1 is not imported into this owner.

### Scientific completion and ownership

completeness: unknown. Targets: naturalproductmech:mibig-8e920fa3c9.

The complete current owner/history, every assigned saved source query and positive dictionary, both complete saved molecular forms, and actual maintained returned view were personally read. All53 owned input hashes and exact ownership match the accepted plan; hash checks are distinct from whole-corpus reading. Five original local native commands passed, but full QC, complete OAK grounding and fresh primary/database verification remain unavailable. The reader establishes complete local view preservation, not all scientific authorities. Completion therefore remains partial, scientific_review:true and all_native_gates_passed:false.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2737-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kutzneride-4.yaml; Complete current owner, all fields and four history events | supports | Whole current owner personally read; byte pin is unchanged and scientific claims retain their source limits. |
| support-2737-capture | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/6 | supports | Complete accepted owner capture; not a substitute for actual maintained execution. |
| support-2737-identity | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/6/owner_document/identifier; /records/6/owner_document/chemical_structure; /records/6/owner_document/source_concepts; /records/6/owner_document/xrefs; /records/6/owner_document/grounding_status; /records/6/owner_document/grounding_notes | supports | Exact congener full key and retained source/grounding route; no natural-sample equivalence inferred. |
| support-2737-producer-locus | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters; /records/6/owner_document/producer_taxon_groups; /records/6/owner_document/bgc_class | supports | SOURCE_ASSERTION producer and separate CLUSTER_UNSTATED locus grades remain unchanged. |
| support-2737-history-citations | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/6/owner_document/curation_history; /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters | supports | Two seeding events and two graph/pathway curations; source citations are not new primary verification. |
| support-2737-occurrence | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups | supports | Exact owner occurrence content; omission and bounded negative queries do not establish biological absence. |
| support-2737-classification | /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json; /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification; /records/6/owner_document/biosynthesis_origin; /records/6/owner_document/bgc_class | supports | Source BGC class and separate model outputs, including intentional multi-label UNCLASSIFIED filing. |
| support-2737-intake | /private/tmp/npm-review-work/shared-next-batch274/intakes-001/2737-inspect-001.json; /status; /source; /targets | supports | Actual canonical intake and exact owner input ownership; no final scientific result inferred from inspection. |
| support-2737-intake-original | /private/tmp/npm-review-work/shared-next-batch274/intakes-001/intake-summary-001.json; /receipts/6 | supports | Original intake command and outcome, with empty stderr; no replay. |
| support-2737-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch274/root-intake-acceptance-001.json; /accepted; /summary; /all_expected_maps_exact; /all_stderr_empty | supports | ROOT acceptance of the original ten intakes and exact current input maps. |
| support-2737-source-plan | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-target-input-plan-001.json; /records/6 | supports | Actual per-owner direct companion and implementation scope; shared BGC does not transfer congener evidence. |
| support-2737-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch274/root-current274-source-plan-acceptance-001.json; /accepted; /plan | supports | Accepted actual source plan with current inputs. |
| support-2737-source-reading | /private/tmp/npm-review-work/shared-next-batch274-tentative/support-prep/support-current274-assigned-source-reading-001.json; /contexts/2; /counts; /selected_counts; /primary_context_indices | supports | All assigned positive row dictionaries and exact negative frames personally read; selected and unselected credits remain separate. |
| support-2737-notes | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /reading_boundaries | supports | Disjoint current source reading and explicitly attributed cached/curation interpretations. |
| support-2737-taxonomy | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-cached-taxonomy-reading-001.json; /context_interpretations/11; /interpretation | supports | Cached exact ID/label routes only; no fresh lineage, rank, strain or taxon equivalence. |
| support-2737-curation | /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-implemented-curation-scan-001.json; /counts; /exact_applicability_resolution; /implementation_scope; /interpretation | supports | No applicable exact correction in the inspected substantive retained tables; no broader primary-source conclusion. |
| support-2737-molecular-DATA | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-DATA-001.json; /records/6 | supports | Both complete saved molecular forms and all false canonical/empty-map/full-identity flags; no new parse. |
| support-2737-molecular-reading | /private/tmp/npm-review-work/shared-next-batch274-tentative/support-prep/support-current274-last-five-saved-molecular-reading-001.json; /records/1 | supports | Personally read complete atom/bond/ring/stereo/motif tables and bounded form-specific interpretation. |
| support-2737-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /data; /execution; /all_canonical_smiles_comparisons_false; /all_atom_correspondence_maps_empty; /full_graph_identity_established; /unassigned_stderr_warning_count | supports | Accepted original twenty-form diagnostic; two global warnings remain unassigned. |
| support-2737-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-execution-001.json; /exit_code; /command; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic command and streams, zero exit and no retry/request. |
| support-2737-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165–172 | supports | Atom-centred extraction policy for stereo_complete; no promise of all bond geometry or natural stereochemistry. |
| support-2737-grade-policy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; lines 23–28 | supports | No-stated-method case keeps source producer assertion separate from an unstated locus grade. |
| support-2737-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295–306 | supports | Multiple NPClassifier pathway labels intentionally map to UNCLASSIFIED. |
| support-2737-local-gates | /private/tmp/npm-native-checks/batch-274/root-five-gates-acceptance-001.json; /accepted; /execution; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_rows | supports | Five original local commands passed; full required gate completion remains false. |
| support-2737-reader-DATA | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-maintained-reader-DATA-001.json; /order; /status; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner; /counts; /denials; /unexpected_denials; /limitations | supports | Actual complete maintained view, two precursor graphs, two numbered steps and four histories; one blocked capability probe, no request. |
| support-2737-reader-execution | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-reader-execution-001.json; /order; /command; /exit_code; /stdout; /stderr; /retries; /external_requests | supports | The actual single reader process and empty stderr; no new execution in this review lane. |
| support-2737-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch274/root-native-reader-2737-acceptance-001.json; /accepted; /DATA; /execution; /verification; /review_check_contract; /scope | supports | ROOT accepted actual complete view equality and exact review check contract; source science is not newly verified. |
| support-2737-precursor-graphs | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-maintained-reader-DATA-001.json; /resolved_view/causal_graphs | supports | All six nodes, four edges and twenty reference placements personally read; graphs are precursor-scoped and retain historical evidence attribution. |
| support-2737-precursor-pathway | /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-maintained-reader-DATA-001.json; /resolved_view/biosynthetic_pathway; /resolved_view/curation_history | supports | Both numbered reactions, ten reference placements and four history events; chemical forms are preserved separately from graph identifiers. |
| support-2737-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/mibig_compounds | supports | Complete retained mibig_compounds query: 1 positive placements, exact predicate and full rows retained. |
| support-2737-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 510; complete header/dictionaries in pinned inventory /contexts/11/source_scope_inventory/joins/mibig_compounds/matches | supports | Whole retained physical rows and every field, including blanks; row placements are not independent experiments. |
| support-2737-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/chebi_structures | supports | Complete retained chebi_structures query: 0 positive placements, exact predicate and full rows retained. |
| support-2737-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/lotus_occurrences | supports | Complete retained lotus_occurrences query: 2 positive placements, exact predicate and full rows retained. |
| support-2737-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 2855, 2856; complete header/dictionaries in pinned inventory /contexts/11/source_scope_inventory/joins/lotus_occurrences/matches | supports | Whole retained physical rows and every field, including blanks; row placements are not independent experiments. |
| support-2737-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete retained cyanometdb_occurrences query: 0 positive placements, exact predicate and full rows retained. |
| support-2737-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/npclassifier | supports | Complete retained npclassifier query: 1 positive placements, exact predicate and full rows retained. |
| support-2737-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 1041; complete header/dictionaries in pinned inventory /contexts/11/source_scope_inventory/joins/npclassifier/matches | supports | Whole retained physical rows and every field, including blanks; row placements are not independent experiments. |
| support-2737-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/pubchem_bioassay | supports | Complete retained pubchem_bioassay query: 0 positive placements, exact predicate and full rows retained. |
| support-2737-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/bindingdb_targets | supports | Complete retained bindingdb_targets query: 0 positive placements, exact predicate and full rows retained. |
| support-2737-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete retained antibioticmech_inchikeys query: 0 positive placements, exact predicate and full rows retained. |
| support-2737-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/joins/chebi_origins | supports | Complete retained chebi_origins query: 0 positive placements, exact predicate and full rows retained. |
| support-2737-taxon-predicates | /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json; /contexts/11/source_scope_inventory/source_taxa; /contexts/11/source_scope_inventory/forward_taxon_merge_matches; /contexts/11/source_scope_inventory/nonorganism_matches | supports | Exact owner source taxa and retained merge/nonorganism query results; no fresh taxonomy. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-274/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-274/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-274/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-274/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-274/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Only retained owner/source rows and accepted original local outputs were used. Current publications, database records, sequences, taxon authorities and complete ontology grounding were not independently verified.
- The source-form cyclic C=N at bond15 (C15–N16) persists as a separate motif from the three newly represented imines; its corresponding reconstructed bond is14 (C11–N39). Those form-specific indices are not an atom map. Relative to Kutzneride3, the formula contains two fewer hydrogens and the full key differs. Both canonical comparisons and full identity remain false; empty maps do not resolve the three amide/imidic differences. Nine specified tetrahedral centres in each form; three reconstructed C=N entries are unspecified. The pre-existing C=N in the six-member N–N ring is not listed as potential double-bond stereo.
- KtzQ/R annotations concern two precursor steps, with distinct graph/pathway chemical identifiers. Historical evidence labels and reader success do not establish all congener-specific synthesis. Two diagnostic warnings are globally unassigned; full QC/OAK/live primary checks remain unavailable.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Whole owner, full saved source payloads, molecular tables and actual returned view personally read. Primary-row attribution remains Support18 selected rows/208 fields plus separate Kutzneride6 context2 rows/32 fields; repeated references and placements are not independent experiments.
- No native curation status, record, source table or history was edited; no new parse, target execution or outbound request occurred in this authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T170757Z-kutzneride-4
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: Kutzneride 4'
started_at: '2026-11-06T16:14:29.039088Z'
finished_at: '2026-11-06T17:07:57.291845Z'
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
summary: Kutzneride4 retains its distinct unsaturated congener identity and source-specific
  provenance. Two precursor chlorination steps are faithfully resolved, but do not
  establish full assembly. Three amide/imidic differences, empty correspondence and
  unavailable external checks keep this qualified pass partial.
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
  - path: data/natural_products/amino_acids_and_peptides/kutzneride-6.yaml
    sha256: e9cd3bb0da0f378d8e964317eb9b5e0a3021b2f8dcc9341a9c9b12ada4559fd9
    role: context
  - path: data/natural_products/unclassified/kutzneride-1.yaml
    sha256: 2954407c141acbf2283eb99515c4f0973598b059ed2e215f82cbb3aa56f57aca
    role: context
  - path: data/natural_products/unclassified/kutzneride-2.yaml
    sha256: 26175cd1432d7580995f6852ca74fdb044c7466f8e5e54c6c88e33a4cf3d6749
    role: context
  - path: data/natural_products/unclassified/kutzneride-3.yaml
    sha256: b96bf6b28895c444556b57bf37db2a95e0a310ad2c797eef0b8348bd40cee853
    role: context
  - path: data/natural_products/unclassified/kutzneride-4.yaml
    sha256: 7cb271590a269d6dba7dbd49a2ba7b4b664bd47a9f9e894a62f5c4ce3e765ac6
    role: target
  - path: data/natural_products/unclassified/kutzneride-5.yaml
    sha256: 5ac0ba9f549d8eaf7b98f8fd4cfe5680867c92e3d0f5c82b6928d02754c83890
    role: context
  - path: data/natural_products/unclassified/kutzneride-7.yaml
    sha256: 6bd2a0ecf7dc600204cd4cb84b8db53ad7e77e772ed4631f619465c969e2a8fa
    role: context
  - path: data/natural_products/unclassified/kutzneride-8.yaml
    sha256: a67c6066e5671ca70c5c28062095db4f862dbd02e2d4b48a2a15abe999feed5a
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
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2737; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-8e920fa3c9
targets:
- target_id: naturalproductmech:mibig-8e920fa3c9
  path: data/natural_products/unclassified/kutzneride-4.yaml
  label: Kutzneride 4
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
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/graph_components.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/kutzneride-4.yaml
    role: Curator-owned declared graphs, graph references, pathway steps and history;
      imported molecular-target assertions and other seeded fields retain inventory
      ownership. Curated graph/pathway changes require the validated writer and a
      curation event.
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners. This mechanism-bearing owner requires separately
    authorized complete maintained resolution before scientific assessment and draft
    assembly. Raw owner capture is not a maintained resolved view.
checks:
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnose274-001.py
    12549d68400aa9861f680ef37c41c182318bcf0d07247b93dcf43f66da0eaa0e 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
    ce78cc5fde09a6c9a7c6416bbf4aad680efff7f9414040b475e81a26c9a05f61
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Original stored-form parsing succeeded with formula, charge, StandardInChI
    and declared full-key agreement.
  scope_note: Both canonical comparisons are false, map empty, complete correspondence
    and full identity false; three amide/imidic changes persist. Nine specified tetrahedral
    centres in each form; three reconstructed C=N entries are unspecified. The pre-existing
    C=N in the six-member N–N ring is not listed as potential double-bond stereo.
    Two shared-run warnings remain globally unassigned; no natural-identity or experimental-stereo
    claim.
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-molecular-DATA
  - support-2737-diagnostic-acceptance
  - support-2737-diagnostic-execution
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for kutzneride-4
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch274/read-selected-mechanism-guarded-001.py
    2737 ce78cc5fde09a6c9a7c6416bbf4aad680efff7f9414040b475e81a26c9a05f61 88c44c3470bb813b439eec5a260bf4a8bb52d3f0e2d416070a597b0c143611a5
    207b9ecac890a6753cbe5ba79997dacaf2b9c818f28fb2e58539b9e55415c2e8 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
    12549d68400aa9861f680ef37c41c182318bcf0d07247b93dcf43f66da0eaa0e
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: 'One original offline maintained call preserved the complete owner: two
    graphs, six nodes, four edges, two numbered steps, thirty evidence placements
    and four histories; no components.'
  scope_note: Complete capture=expected=returned view, zero unexpected denials/empty
    stderr. One urllib3 IPv6 socket-construction probe was blocked before action;
    no request was sent. Preserved historical evidence labels and precursor topology
    do not newly verify primary publications, sequences, ontology grounding or complete
    congener biosynthesis.
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-reader-DATA
  - support-2737-reader-execution
  - support-2737-reader-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  command: just validate-strict data/natural_products/unclassified/kitacinnamycin-e.yaml
    data/natural_products/unclassified/kitacinnamycin-f.yaml data/natural_products/unclassified/kk-1.yaml
    data/natural_products/unclassified/kutzneride-1.yaml data/natural_products/unclassified/kutzneride-2.yaml
    data/natural_products/unclassified/kutzneride-3.yaml data/natural_products/unclassified/kutzneride-4.yaml
    data/natural_products/unclassified/kutzneride-5.yaml data/natural_products/unclassified/kutzneride-7.yaml
    data/natural_products/unclassified/kutzneride-8.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-274/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-8e920fa3c9
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-274/validate-all-001.tsv
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
  - naturalproductmech:mibig-8e920fa3c9
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
  - naturalproductmech:mibig-8e920fa3c9
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
  - naturalproductmech:mibig-8e920fa3c9
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-274/review-queue-001.tsv
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
  - naturalproductmech:mibig-8e920fa3c9
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2737-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/kutzneride-4.yaml
  locator: Complete current owner, all fields and four history events
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Whole current owner personally read; byte pin is unchanged and scientific
    claims retain their source limits.
  snapshot_sha256: 7cb271590a269d6dba7dbd49a2ba7b4b664bd47a9f9e894a62f5c4ce3e765ac6
- evidence_id: support-2737-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Complete accepted owner capture; not a substitute for actual maintained
    execution.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: support-2737-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/6/owner_document/identifier; /records/6/owner_document/chemical_structure;
    /records/6/owner_document/source_concepts; /records/6/owner_document/xrefs; /records/6/owner_document/grounding_status;
    /records/6/owner_document/grounding_notes
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Exact congener full key and retained source/grounding route; no natural-sample
    equivalence inferred.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: support-2737-producer-locus
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/6/owner_document/producer_organisms; /records/6/owner_document/biosynthetic_gene_clusters;
    /records/6/owner_document/producer_taxon_groups; /records/6/owner_document/bgc_class
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: SOURCE_ASSERTION producer and separate CLUSTER_UNSTATED locus grades remain
    unchanged.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: support-2737-history-citations
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/6/owner_document/curation_history; /records/6/owner_document/producer_organisms;
    /records/6/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Two seeding events and two graph/pathway curations; source citations are
    not new primary verification.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: support-2737-occurrence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/6/owner_document/occurrences; /records/6/owner_document/occurrence_taxon_groups
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Exact owner occurrence content; omission and bounded negative queries do
    not establish biological absence.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: support-2737-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/owner-capture-DATA-001.json
  locator: /records/6/owner_document/np_pathway; /records/6/owner_document/np_classification;
    /records/6/owner_document/biosynthesis_origin; /records/6/owner_document/bgc_class
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Source BGC class and separate model outputs, including intentional multi-label
    UNCLASSIFIED filing.
  snapshot_sha256: 97fb52f35b4b50edc88009193d6edfb04416b1b12675ceb4d2b6a2d3e92b67d0
- evidence_id: support-2737-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/intakes-001/2737-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Actual canonical intake and exact owner input ownership; no final scientific
    result inferred from inspection.
  snapshot_sha256: 88c44c3470bb813b439eec5a260bf4a8bb52d3f0e2d416070a597b0c143611a5
- evidence_id: support-2737-intake-original
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/intakes-001/intake-summary-001.json
  locator: /receipts/6
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Original intake command and outcome, with empty stderr; no replay.
  snapshot_sha256: ce78cc5fde09a6c9a7c6416bbf4aad680efff7f9414040b475e81a26c9a05f61
- evidence_id: support-2737-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/root-intake-acceptance-001.json
  locator: /accepted; /summary; /all_expected_maps_exact; /all_stderr_empty
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: ROOT acceptance of the original ten intakes and exact current input maps.
  snapshot_sha256: 44e8e110bef4b892fba9024b09cab57eef2ed34c5977f1d8db37176b2db6418f
- evidence_id: support-2737-source-plan
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-target-input-plan-001.json
  locator: /records/6
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Actual per-owner direct companion and implementation scope; shared BGC
    does not transfer congener evidence.
  snapshot_sha256: 83af42d96827a5af436bb7aca0ccb952527ad886bf06d40a18c2ec1a0c770708
- evidence_id: support-2737-source-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/root-current274-source-plan-acceptance-001.json
  locator: /accepted; /plan
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Accepted actual source plan with current inputs.
  snapshot_sha256: 15c392305536f94216a1174abce9db3443ca92c3467358e2e2c2f629f7a40f06
- evidence_id: support-2737-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/support-prep/support-current274-assigned-source-reading-001.json
  locator: /contexts/2; /counts; /selected_counts; /primary_context_indices
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: All assigned positive row dictionaries and exact negative frames personally
    read; selected and unselected credits remain separate.
  snapshot_sha256: 26ed1a8183e0ec67fb8c8d866c8c943ae690822b1e5ab1cf52bf9b6dac8e4918
- evidence_id: support-2737-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /reading_boundaries
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Disjoint current source reading and explicitly attributed cached/curation
    interpretations.
  snapshot_sha256: ccb81806b7d50db41cfc2aaaeb638f9df68733017a6e847ab3c72bf2d0fedf94
- evidence_id: support-2737-taxonomy
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-cached-taxonomy-reading-001.json
  locator: /context_interpretations/11; /interpretation
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Cached exact ID/label routes only; no fresh lineage, rank, strain or taxon
    equivalence.
  snapshot_sha256: ab95bb0dcc77d16661eb24f6b3d9d07b99215275ece984f359f75775d0947596
- evidence_id: support-2737-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/native-prep/native-current274-implemented-curation-scan-001.json
  locator: /counts; /exact_applicability_resolution; /implementation_scope; /interpretation
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: No applicable exact correction in the inspected substantive retained tables;
    no broader primary-source conclusion.
  snapshot_sha256: 204d96aa0c5d6a835ef6e361ffc70af374d6cdce738af90d1e81ce141502e289
  search_scope: Ignored-inclusive 11-table census, nine substantive retained correction/diagnostic
    tables and context-specific exact predicates; census-only decisions/source-queue
    extras are not operative correction tables.
- evidence_id: support-2737-molecular-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Both complete saved molecular forms and all false canonical/empty-map/full-identity
    flags; no new parse.
  snapshot_sha256: 968b394137ace1559551b48880dc4f4860d58cd338562129d08ad6037ce4ccb6
- evidence_id: support-2737-molecular-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/support-prep/support-current274-last-five-saved-molecular-reading-001.json
  locator: /records/1
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Personally read complete atom/bond/ring/stereo/motif tables and bounded
    form-specific interpretation.
  snapshot_sha256: d43d7c44f4ab7bfda9e185690f5ff75088655c487af9eae80f8c80a654cf4b16
- evidence_id: support-2737-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /data; /execution; /all_canonical_smiles_comparisons_false;
    /all_atom_correspondence_maps_empty; /full_graph_identity_established; /unassigned_stderr_warning_count
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Accepted original twenty-form diagnostic; two global warnings remain unassigned.
  snapshot_sha256: 0c8c7b7e8d27b7373931eb6d60bb04c0bd41e089410a3ae0d1e15b2ad101a345
- evidence_id: support-2737-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /command; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Original diagnostic command and streams, zero exit and no retry/request.
  snapshot_sha256: dcbf2e358a8b2141865d7795f53402e4c5b4dcd9a4ea92ef690eafdc89d1a4b3
- evidence_id: support-2737-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165–172
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Atom-centred extraction policy for stereo_complete; no promise of all bond
    geometry or natural stereochemistry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2737-grade-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: lines 23–28
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: No-stated-method case keeps source producer assertion separate from an
    unstated locus grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2737-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295–306
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Multiple NPClassifier pathway labels intentionally map to UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2737-local-gates
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/root-five-gates-acceptance-001.json
  locator: /accepted; /execution; /five_local_commands_passed; /all_native_gates_passed;
    /unavailable_required_gates; /selected_queue_rows
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Five original local commands passed; full required gate completion remains
    false.
  snapshot_sha256: 70c72a46f5d647646262e080f7a03cac5b3deb9fd8ea34dbc344262115b876fc
- evidence_id: support-2737-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-maintained-reader-DATA-001.json
  locator: /order; /status; /resolved_view; /expected_view; /returned_view_equals_expected_complete_owner;
    /counts; /denials; /unexpected_denials; /limitations
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Actual complete maintained view, two precursor graphs, two numbered steps
    and four histories; one blocked capability probe, no request.
  snapshot_sha256: 0546bc4aadb44f0e99c8a0767f5c4efb67692c282f432d53b26b737d387d2f58
- evidence_id: support-2737-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-reader-execution-001.json
  locator: /order; /command; /exit_code; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: The actual single reader process and empty stderr; no new execution in
    this review lane.
  snapshot_sha256: 93d28fd28daae7a8d6624920c12e6c46af977eb8e64c3f0928957dd117aa34a1
- evidence_id: support-2737-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch274/root-native-reader-2737-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /review_check_contract; /scope
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: ROOT accepted actual complete view equality and exact review check contract;
    source science is not newly verified.
  snapshot_sha256: d0afa571a84204fc3d154758eddbd61a26bcb17eb7b171a8e1625eccdbcd2613
- evidence_id: support-2737-precursor-graphs
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-maintained-reader-DATA-001.json
  locator: /resolved_view/causal_graphs
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: All six nodes, four edges and twenty reference placements personally read;
    graphs are precursor-scoped and retain historical evidence attribution.
  snapshot_sha256: 0546bc4aadb44f0e99c8a0767f5c4efb67692c282f432d53b26b737d387d2f58
- evidence_id: support-2737-precursor-pathway
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch274/native-current274-kutzneride-4-maintained-reader-DATA-001.json
  locator: /resolved_view/biosynthetic_pathway; /resolved_view/curation_history
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Both numbered reactions, ten reference placements and four history events;
    chemical forms are preserved separately from graph identifiers.
  snapshot_sha256: 0546bc4aadb44f0e99c8a0767f5c4efb67692c282f432d53b26b737d387d2f58
- evidence_id: support-2737-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained mibig_compounds query: 1 positive placements, exact
    predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "mibig_compounds"}'
- evidence_id: support-2737-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 510; complete header/dictionaries in pinned inventory
    /contexts/11/source_scope_inventory/joins/mibig_compounds/matches
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Whole retained physical rows and every field, including blanks; row placements
    are not independent experiments.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2737-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained chebi_structures query: 0 positive placements, exact
    predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "chebi_structures"}'
- evidence_id: support-2737-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained lotus_occurrences query: 2 positive placements, exact
    predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 2, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "lotus_occurrences"}'
- evidence_id: support-2737-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 2855, 2856; complete header/dictionaries in pinned inventory
    /contexts/11/source_scope_inventory/joins/lotus_occurrences/matches
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Whole retained physical rows and every field, including blanks; row placements
    are not independent experiments.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2737-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained cyanometdb_occurrences query: 0 positive placements,
    exact predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "cyanometdb_occurrences"}'
- evidence_id: support-2737-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained npclassifier query: 1 positive placements, exact predicate
    and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 1, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "npclassifier"}'
- evidence_id: support-2737-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 1041; complete header/dictionaries in pinned inventory
    /contexts/11/source_scope_inventory/joins/npclassifier/matches
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Whole retained physical rows and every field, including blanks; row placements
    are not independent experiments.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2737-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained pubchem_bioassay query: 0 positive placements, exact
    predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "pubchem_bioassay"}'
- evidence_id: support-2737-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained bindingdb_targets query: 0 positive placements, exact
    predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "bindingdb_targets"}'
- evidence_id: support-2737-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained antibioticmech_inchikeys query: 0 positive placements,
    exact predicate and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 0, "predicate": "exact complete standard_inchi_key
    equality", "query": "IURQCOHKGOZHQD-QLXFUGDFSA-N", "scope": "Pinned retained tables
    only; no source-query replay, universal absence or fresh database verification.",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: support-2737-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: 'Complete retained chebi_origins query: 0 positive placements, exact predicate
    and full rows retained.'
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: '{"positive_placements": 0, "predicate": "exact chebi_id from exact
    full-key structure rows", "query": [], "scope": "Pinned retained tables only;
    no source-query replay, universal absence or fresh database verification.", "table":
    "chebi_origins"}'
- evidence_id: support-2737-taxon-predicates
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch274-tentative/bgc-prep/bgc-conditional274-source-inventory-DATA-001.json
  locator: /contexts/11/source_scope_inventory/source_taxa; /contexts/11/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/11/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-06T16:58:16.138236Z'
  support: supports
  summary: Exact owner source taxa and retained merge/nonorganism query results; no
    fresh taxonomy.
  snapshot_sha256: 2d137cc981cee242b81bb2016c78bd3f4ba7d8ad1306b4f58993e1ae432274dd
  search_scope: Only the context’s literal source taxon IDs and pinned forward-merge/nonorganism
    tables, with no reverse-ID or live inference.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:15:09.494074Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: cd7d41117a4f278a0ff9fddf933a24f1419ad0e5c4f6c531afdb8145c64d3a4b
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:15:34.127215Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 9a2b548d7e3e59d3e4b40953a14514daf8c4c59f1d53a6fd2dada6108673dfc9
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:15:53.345460Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:16:26.812981Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-274/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-274/native-current274-five-gates-execution-001.json
  accessed_at: '2026-11-06T16:16:38.263309Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 39cc66beb0fcbfcd1a090de6f99823466c4b7f1a642ff96107c65f51784a3909
assessments:
- assessment_id: support-2737-identity
  area: identity
  topic: Retained congener identity and grounding
  summary: MIBiG BGC0000378 version5 compound-4 preserves Kutzneride 4, full key IURQCOHKGOZHQD-QLXFUGDFSA-N
    and npatlas:NPA007816. The empty retained exact-key ChEBI query supports only
    this captured MINTED route; it does not establish universal absence or verified
    natural identity. Its unsaturated N–N side ring and two fewer hydrogens distinguish
    it from Kutzneride3; the common stereochemical key suffix does not merge these
    full keys.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-identity
  - support-2737-query-mibig_compounds
  - support-2737-query-chebi_structures
  - support-2737-source-plan
  - support-2737-source-reading
  - support-2737-molecular-DATA
  dimensions:
  - name: standard_inchi_key
    definition: Exact full key without prefix or name substitution.
    value: IURQCOHKGOZHQD-QLXFUGDFSA-N
    evidence_ids:
    - support-2737-identity
    - support-2737-query-mibig_compounds
    - support-2737-query-chebi_structures
    - support-2737-source-plan
    - support-2737-source-reading
    - support-2737-molecular-DATA
  - name: grounding_scope
    definition: Retained source grounding is distinct from natural-identity verification.
    value: MINTED exact-key/source route; no newly verified natural identity
    evidence_ids:
    - support-2737-identity
    - support-2737-query-mibig_compounds
    - support-2737-query-chebi_structures
    - support-2737-source-plan
    - support-2737-source-reading
    - support-2737-molecular-DATA
- assessment_id: support-2737-representation
  area: representation
  topic: Stored forms and stereochemical limits
  summary: Both stored forms regenerate the declared StandardInChI/full key and neutral
    formula C37H47Cl2N7O12, with 58 atoms and 63 bonds each. Every saved atom has
    formal charge zero and no isotopic label. Both canonical isomeric and nonisomeric
    comparisons are false; the limited map is empty, complete_atom_count_match is
    false and full_graph_identity_established remains false. Seven carbonyls and five
    strict amides in the SMILES become four carbonyls and two strict amides, with
    three terminal C(OH)=N motifs in the reconstructed form (each O has degree1 and
    H1). The one macrocyclic ester and terminal carboxylic acid persist. Nine specified
    tetrahedral centres in each form; three reconstructed C=N entries are unspecified.
    The pre-existing C=N in the six-member N–N ring is not listed as potential double-bond
    stereo. The source-form cyclic C=N at bond15 (C15–N16) persists as a separate
    motif from the three newly represented imines; its corresponding reconstructed
    bond is14 (C11–N39). Those form-specific indices are not an atom map. Relative
    to Kutzneride3, the formula contains two fewer hydrogens and the full key differs.
    Two stderr warnings belong to the shared run and are not assigned to this record.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-identity
  - support-2737-molecular-DATA
  - support-2737-molecular-reading
  - support-2737-diagnostic-acceptance
  - support-2737-diagnostic-execution
  - support-2737-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Saved atom-centre and bond geometry is distinct from experimental
      assignment.
    value: Nine specified tetrahedral centres in each form; three reconstructed C=N
      entries are unspecified. The pre-existing C=N in the six-member N–N ring is
      not listed as potential double-bond stereo.
    evidence_ids:
    - support-2737-identity
    - support-2737-molecular-DATA
    - support-2737-molecular-reading
    - support-2737-diagnostic-acceptance
    - support-2737-diagnostic-execution
    - support-2737-stereo-policy
  - name: representation_correspondence
    definition: Normalized key equality does not prove fixed-form graph equivalence.
    value: Both canonical comparisons false; map empty; three amide/imidic differences;
      complete map and full identity false.
    evidence_ids:
    - support-2737-identity
    - support-2737-molecular-DATA
    - support-2737-molecular-reading
    - support-2737-diagnostic-acceptance
    - support-2737-diagnostic-execution
    - support-2737-stereo-policy
- assessment_id: support-2737-provenance
  area: provenance
  topic: Producer, taxonomy and locus grades
  summary: The producer Kutzneria sp. 744 / NCBITaxon:345341 remains SOURCE_ASSERTION,
    while its BGC0000378 v5 / genbank:EU074211.1 association separately remains CLUSTER_UNSTATED.
    The exact MIBiG row is active/questionable with unknown completeness, blank locus
    coordinates and no stated locus evidence methods. Shared cluster membership and
    curated precursor-enzyme annotations do not upgrade either grade or establish
    congener-specific production. Cached labels corroborate retained ID/name routes
    only; current strain, lineage and sequence identity were not independently verified.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-producer-locus
  - support-2737-taxonomy
  - support-2737-taxon-predicates
  - support-2737-curation
  - support-2737-grade-policy
  - support-2737-query-mibig_compounds
  dimensions:
  - name: taxon_scope
    definition: Exact cached taxon routes without fresh strain/lineage resolution.
    value: Producer Kutzneria sp.744 /345341; LOTUS genus Kutzneria /43356; cached
      labels only.
    evidence_ids:
    - support-2737-producer-locus
    - support-2737-taxonomy
    - support-2737-taxon-predicates
    - support-2737-curation
    - support-2737-grade-policy
    - support-2737-query-mibig_compounds
  - name: producer_evidence
    definition: Producer grade follows its own source methods.
    value: 'SOURCE_ASSERTION: Kutzneria sp.744 /345341; no upgrade from graphs or
      occurrence.'
    evidence_ids:
    - support-2737-producer-locus
    - support-2737-taxonomy
    - support-2737-taxon-predicates
    - support-2737-curation
    - support-2737-grade-policy
    - support-2737-query-mibig_compounds
  - name: locus_evidence
    definition: Locus association grade remains separate from organism evidence.
    value: CLUSTER_UNSTATED; BGC0000378 v5 /EU074211.1; no stated coordinates/methods,
      completeness unknown.
    evidence_ids:
    - support-2737-producer-locus
    - support-2737-taxonomy
    - support-2737-taxon-predicates
    - support-2737-curation
    - support-2737-grade-policy
    - support-2737-query-mibig_compounds
- assessment_id: support-2737-citations
  area: evidence
  topic: Citation grain and historical authority
  summary: DOI:10.1021/np050378g is the COMPOUND_EVIDENCE citation retained for the
    MIBiG producer/locus claim. Occurrence citations retain their own row grain. Four
    history events comprise two seeder events (2026-09-10 and2026-09-25) and two Codex
    precursor graph/pathway curations (2026-10-02 or03). Historical PRIMARY_EXPERIMENT
    labels, quotations and 2026-10-02 retrieval dates for KtzQ/R are attributed annotations.
    The DOI:10.1021/ja806467a paper and MITE/UniProt/GenPept/GenBank bodies were not
    independently inspected in this offline review, so no new primary, sequence or
    database authority is claimed.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-history-citations
  - support-2737-source-reading
  - support-2737-notes
  - support-2737-precursor-graphs
  - support-2737-precursor-pathway
  - support-2737-table-mibig_compounds
  - support-2737-table-lotus_occurrences
  - support-2737-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Claim-level citation placement does not imply fresh source access.
    value: DOI:10.1021/np050378g at COMPOUND_EVIDENCE grain; four histories; KtzQ/R
      primary/database labels historical and unverified here.
    evidence_ids:
    - support-2737-history-citations
    - support-2737-source-reading
    - support-2737-notes
    - support-2737-precursor-graphs
    - support-2737-precursor-pathway
    - support-2737-table-mibig_compounds
    - support-2737-table-lotus_occurrences
    - support-2737-table-npclassifier
- assessment_id: support-2737-occurrence-activity
  area: evidence
  topic: Occurrence, assay and target boundaries
  summary: Two LOTUS placements report genus Kutzneria / NCBITaxon:43356, with DOI:10.1021/NP050378G
    and DOI:10.1021/NP0604331. These are distinct occurrence/reference rows, not two
    strain-level production experiments; the producer remains the separate Kutzneria
    sp.744 /345341 source claim. All saved exact-key PubChem BioAssay, BindingDB,
    CyanometDB and related AntibioticMech queries are empty, with no actual AID and
    no blank-AID sentinel. ChEBI origins has an empty predicate list because no ChEBI
    structure matched. These bounds do not establish inactivity or a complete biological-target
    survey; no molecular-target root is present.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-occurrence
  - support-2737-source-reading
  - support-2737-curation
  - support-2737-taxon-predicates
  - support-2737-query-mibig_compounds
  - support-2737-query-chebi_structures
  - support-2737-query-lotus_occurrences
  - support-2737-query-cyanometdb_occurrences
  - support-2737-query-npclassifier
  - support-2737-query-pubchem_bioassay
  - support-2737-query-bindingdb_targets
  - support-2737-query-antibioticmech_inchikeys
  - support-2737-query-chebi_origins
  - support-2737-table-mibig_compounds
  - support-2737-table-lotus_occurrences
  - support-2737-table-npclassifier
  dimensions:
  - name: occurrence_scope
    definition: Occurrence rows are distinct from production and independent experiments.
    value: Two genus-level occurrence/reference placements; no production upgrade.
    evidence_ids:
    - support-2737-occurrence
    - support-2737-source-reading
    - support-2737-curation
    - support-2737-taxon-predicates
    - support-2737-query-mibig_compounds
    - support-2737-query-chebi_structures
    - support-2737-query-lotus_occurrences
    - support-2737-query-cyanometdb_occurrences
    - support-2737-query-npclassifier
    - support-2737-query-pubchem_bioassay
    - support-2737-query-bindingdb_targets
    - support-2737-query-antibioticmech_inchikeys
    - support-2737-query-chebi_origins
    - support-2737-table-mibig_compounds
    - support-2737-table-lotus_occurrences
    - support-2737-table-npclassifier
  - name: assay_target_scope
    definition: Actual assays, sentinels and bounded negatives remain distinct.
    value: No saved actual AID or blank sentinel; bounded assay/target/related-corpus
      negatives, not inactivity.
    evidence_ids:
    - support-2737-occurrence
    - support-2737-source-reading
    - support-2737-curation
    - support-2737-taxon-predicates
    - support-2737-query-mibig_compounds
    - support-2737-query-chebi_structures
    - support-2737-query-lotus_occurrences
    - support-2737-query-cyanometdb_occurrences
    - support-2737-query-npclassifier
    - support-2737-query-pubchem_bioassay
    - support-2737-query-bindingdb_targets
    - support-2737-query-antibioticmech_inchikeys
    - support-2737-query-chebi_origins
    - support-2737-table-mibig_compounds
    - support-2737-table-lotus_occurrences
    - support-2737-table-npclassifier
- assessment_id: support-2737-classification
  area: consistency
  topic: Classification and encoded topology
  summary: The blank MIBiG compound_classes field is faithfully retained; it is not
    automatically a required-class defect. Source NRPS and separate Type I subclass
    text are not a new PKS assertion. NPClassifier predicts Oligopeptides, Cyclic
    peptides and Depsipeptides with is_glycoside:false. Its two pathways, Amino acids
    and Peptides plus Polyketides, intentionally produce UNCLASSIFIED filing under
    choose_pathway295–306. The source-form amides and ester within the 18-member macrocycle
    support a broad cyclic depsipeptide topology. Both forms have ring sizes3,5,5,6,6,18;
    no C5O candidate sugar ring is reported. Two broad carbon–O–carbon bridges include
    the ester and an ether and do not imply two glycosidic links. These encoded motifs
    qualify the model output without proving a biosynthetic pathway, residue names
    or natural identity.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-classification
  - support-2737-molecular-DATA
  - support-2737-molecular-reading
  - support-2737-filing-policy
  - support-2737-query-npclassifier
  - support-2737-query-mibig_compounds
  dimensions:
  - name: classification_applicability
    definition: Structural compatibility can qualify a model output without proving
      biosynthesis.
    value: Two-label UNCLASSIFIED; encoded 18-member depsipeptide macrocycle, no named
      sugar or glycosidic assignment.
    evidence_ids:
    - support-2737-classification
    - support-2737-molecular-DATA
    - support-2737-molecular-reading
    - support-2737-filing-policy
    - support-2737-query-npclassifier
    - support-2737-query-mibig_compounds
- assessment_id: support-2737-mechanism
  area: graph
  topic: Precursor enzyme mechanism and complete reader scope
  summary: 'The actual maintained call preserves two inline BIOSYNTHESIS graphs (six
    nodes/four edges/twenty evidence placements), two numbered pathway steps (ten
    evidence placements), and all four histories, with no components or molecular
    targets. Their bounded meaning is sequential free-tryptophan precursor chlorination:
    KtzQ / UniProtKB:A8CF75 / GenPept ABV56597.1 / MITE0000029 at RHEA:26494, followed
    by KtzR / A8CF74 / ABV56598.1 / MITE0000030 at RHEA:55904. KtzS is expressly outside
    the KtzQ-specific graph. Graph chemical IDs CHEBI:16828→47356→140086 and pathway
    forms CHEBI:57912→58713→139336 are distinct retained representations, not synonyms
    or newly verified charge-form equivalences; pathway cofactors/products also remain
    intact. The repeated DOI:10.1021/ja806467a and historical database references
    support the attributed precursor narrative only at its recorded scope. No full-congener
    assembly, fresh enzyme sequence/construct attribution, independent PRIMARY_EXPERIMENT
    verification or complete ontology grounding is established by the reader. KtzA/D
    material from Kutzneride1 is not imported into this owner.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-reader-DATA
  - support-2737-reader-execution
  - support-2737-reader-acceptance
  - support-2737-precursor-graphs
  - support-2737-precursor-pathway
  - support-2737-source-reading
  - support-2737-producer-locus
  dimensions: []
- assessment_id: support-2737-completion
  area: completeness
  topic: Scientific completion and ownership
  summary: The complete current owner/history, every assigned saved source query and
    positive dictionary, both complete saved molecular forms, and actual maintained
    returned view were personally read. All53 owned input hashes and exact ownership
    match the accepted plan; hash checks are distinct from whole-corpus reading. Five
    original local native commands passed, but full QC, complete OAK grounding and
    fresh primary/database verification remain unavailable. The reader establishes
    complete local view preservation, not all scientific authorities. Completion therefore
    remains partial, scientific_review:true and all_native_gates_passed:false.
  outcome: unknown
  target_ids:
  - naturalproductmech:mibig-8e920fa3c9
  evidence_ids:
  - support-2737-owner
  - support-2737-capture
  - support-2737-intake
  - support-2737-intake-original
  - support-2737-intake-acceptance
  - support-2737-source-plan
  - support-2737-source-plan-acceptance
  - support-2737-source-reading
  - support-2737-molecular-reading
  - support-2737-local-gates
  - support-2737-reader-DATA
  - support-2737-reader-acceptance
  dimensions:
  - name: review_completion
    definition: Full owner coverage is distinct from completing every required external
      check.
    value: partial; five local gates and original diagnostic/reader passed; full QC/OAK/live
      primary unavailable
    evidence_ids:
    - support-2737-owner
    - support-2737-capture
    - support-2737-intake
    - support-2737-intake-original
    - support-2737-intake-acceptance
    - support-2737-source-plan
    - support-2737-source-plan-acceptance
    - support-2737-source-reading
    - support-2737-molecular-reading
    - support-2737-local-gates
    - support-2737-reader-DATA
    - support-2737-reader-acceptance
findings: []
actions: []
limitations:
- Only retained owner/source rows and accepted original local outputs were used. Current
  publications, database records, sequences, taxon authorities and complete ontology
  grounding were not independently verified.
- The source-form cyclic C=N at bond15 (C15–N16) persists as a separate motif from
  the three newly represented imines; its corresponding reconstructed bond is14 (C11–N39).
  Those form-specific indices are not an atom map. Relative to Kutzneride3, the formula
  contains two fewer hydrogens and the full key differs. Both canonical comparisons
  and full identity remain false; empty maps do not resolve the three amide/imidic
  differences. Nine specified tetrahedral centres in each form; three reconstructed
  C=N entries are unspecified. The pre-existing C=N in the six-member N–N ring is
  not listed as potential double-bond stereo.
- KtzQ/R annotations concern two precursor steps, with distinct graph/pathway chemical
  identifiers. Historical evidence labels and reader success do not establish all
  congener-specific synthesis. Two diagnostic warnings are globally unassigned; full
  QC/OAK/live primary checks remain unavailable.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Whole owner, full saved source payloads, molecular tables and actual returned view
  personally read. Primary-row attribution remains Support18 selected rows/208 fields
  plus separate Kutzneride6 context2 rows/32 fields; repeated references and placements
  are not independent experiments.
- No native curation status, record, source table or history was edited; no new parse,
  target execution or outbound request occurred in this authoring lane.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-274
```
