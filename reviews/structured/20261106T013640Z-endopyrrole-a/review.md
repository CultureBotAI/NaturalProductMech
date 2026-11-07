# Local evidence review: endopyrrole A

- Review: 20261106T013640Z-endopyrrole-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T00:46:30.121032Z
- Finished UTC: 2026-11-06T01:36:40.581717Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Endopyrrole A retains consistent normalized chemical encodings and a stereospecified cyclic depsipeptide topology. The accepted maintained reader preserves its complete owner, partial EpyD graph and explicitly proposed pathway step. That positive preservation result does not verify the enzyme mechanism or resolve the OPEN shared-structure question spanning two MIBiG entries. The scientific review remains partial.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2634; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-3749610d08 | data/natural_products/unclassified/endopyrrole-a.yaml | generated | endopyrrole A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Complete offline maintained reader for endopyrrole-a | passed | True | naturalproductmech:mibig-3749610d08 | The accepted original reader preserves the complete owner, partial three-node/two-edge graph and explicitly proposed step, including all references and four histories. |
| strict_ten | passed | True | naturalproductmech:mibig-3749610d08 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-3749610d08 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-3749610d08 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-3749610d08 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-3749610d08 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-3749610d08 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-3749610d08 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-3749610d08 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### identity

identity: supported. Targets: naturalproductmech:mibig-3749610d08.

Both saved forms regenerate KRMWEQCPKUMYBI-DKKFUSLWSA-N, C50H67N9O13 and net charge 0. BGC0002048 and BGC0002326 retain the same full key and Standard InChI but distinct source SMILES strings and source concepts. This supports normalized encoding consistency under the MINTED owner identifier. The existing OPEN shared-structure discussion remains unresolved: two database entries do not independently establish the same natural compound or rule out an upstream cross-reference error. Endopyrrole B shares BGC0002048 but has a distinct key and formula.

### representation

representation: supported. Targets: naturalproductmech:mibig-3749610d08.

Both complete tables contain 72 atoms and 76 bonds: a 13-member ester-containing macrocycle, a pyrrole five-member ring, a saturated nitrogen five-member ring and two phenyl rings. Nine specified tetrahedral centers and no undefined tetrahedral centers are retained. Six of eight original amide placements become C(OH)=N motifs with terminal hydroxyl oxygens, while two amides and the ester remain. Six additional unspecified C=N descriptors belong to that reconstruction. Both canonical comparisons are false and the limited atom correspondence is empty; no full graph or natural-identity conclusion is drawn.

### provenance

provenance: unknown. Targets: naturalproductmech:mibig-3749610d08.

BGC0002048 version 3 records Mycetohabitans rhizoxinica HKI 454 (NCBITaxon:882378) on FR687359.1:1835600–1866150; BGC0002326 version 2 records Mycetohabitans rhizoxinica (NCBITaxon:412963) on MN081797.1:1–40068. Both retained producer grades are BGC_CHARACTERIZED and both locus grades CLUSTER_DEMONSTRATED with Knock-out studies. Their NRPS class and Type I subclass remain separate. The rows have questionable entry quality. The strain-specific and broader names are retained as source context without newly verifying rank or ancestry.

### citations

evidence: unknown. Targets: naturalproductmech:mibig-3749610d08.

The two source rows use ENTRY references PMID:21131495 and PMID:31283172. The graph and proposed step additionally retain DOI:10.1021/ACSCHEMBIO.9B00406 and UniProt/GenPept/GenBank references. Six graph and four step reference placements reuse these sources; they are not ten independent experiments. PRIMARY_EXPERIMENT labels and historical sequence/CDS claims are preserved curator annotations, without new primary-paper or sequence access. The LOTUS DOI may refer to the same publication and does not supply established independent evidence.

### occurrence_activity

evidence: unknown. Targets: naturalproductmech:mibig-3749610d08.

The LOTUS occurrence at NCBITaxon:412963 retains the label Burkholderia rhizoxinica, whereas producer assertions use Mycetohabitans names. Cached naming context does not create a fresh taxonomic verification. The occurrence is explicitly distinct from production, and publication independence is unestablished. No actual AID, direct molecular target or activity root was found in this owner scope. The partial biosynthesis graph is not a pharmacological mechanism or an assay result.

### classification

consistency: unknown. Targets: naturalproductmech:mibig-3749610d08.

The ester-containing peptide macrocycle supports broad Cyclic peptides and Depsipeptides descriptions. The saved tables also retain a pyrrole, two phenyl rings and a saturated nitrogen ring; these do not establish enzyme-module assignments. NPClassifier reports Amino acids and Peptides, Polyketides and Oligopeptides, with is_glycoside false. Exact model and polyketide biosynthetic applicability remain bounded, and the proposed EpyD contribution does not complete the entire biosynthetic pathway.

### completion

completeness: unknown. Targets: naturalproductmech:mibig-3749610d08.

All 47 actual input hashes and ownership declarations, the complete owner/history, selected source payloads and both complete molecular forms were reviewed. The one accepted maintained-reader execution preserves the entire owner, graph and proposed step exactly; its typed check is linked to the actual DATA, execution and ROOT acceptance. One expected IPv6 socket-construction probe was denied before action, with no request. Five local gates passed, but full QC, OAK, independent primary-source validation and resolution of the existing identity discussion remain incomplete.

### proposed_EpyD_contribution

graph: supported. Targets: naturalproductmech:mibig-3749610d08.

The actual maintained view preserves one BIOSYNTHESIS graph with three nodes and two contributes-to edges, plus numbered pathway step 1 with proposed:true. EpyD is grounded to UniProtKB:A0A6G7BMN0; the NRPS assembly process remains ungrounded and the compound node uses the exact owner identifier. The whole view matches the captured owner, including all references and four histories. This supports faithful representation of a partial proposed contribution, not an experimentally established complete reaction sequence. Individual module substrates and products remain unexpanded.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2634-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/endopyrrole-a.yaml; Complete plaintext including every curation_history entry | supports | Complete current owner and all 4 history entries were personally read. Historical curator assertions do not confer fresh source-access credit. |
| bgc-2634-capture | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3 | supports | Actual complete owner capture preserves current local content; it is not an independent scientific validation. |
| bgc-2634-identity | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3/owner_document/identifier; /records/3/owner_document/label; /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts; /records/3/owner_document/grounding_status | supports | Exact stored identity, source concepts, grounding and chemical encodings; natural identity is assessed separately. |
| bgc-2634-history | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3/owner_document/curation_history | supports | All 4 current history entries retain their original source and curation scope; no inherited paper access is claimed. |
| bgc-2634-provenance | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters; /records/3/owner_document/source_concepts | supports | Owner-specific producer, locus and source-concept assertions preserve their distinct grades and references. |
| bgc-2634-activity-owner | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3/owner_document/occurrences; /records/3/owner_document/xrefs | supports | Current owner occurrence and cross-reference assertions are retained at their recorded granularity; neither occurrence nor a cross-reference establishes production, activity or molecular mechanism. |
| bgc-2634-classification-owner | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3/owner_document/np_pathway; /records/3/owner_document/biosynthesis_origin; /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class | supports | Recorded classification/model labels and BGC class content; exact source subclasses remain separately visible in the retained MIBiG row. |
| bgc-2634-mechanism-scope | /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json; /records/3/owner_document/causal_graphs; /records/3/owner_document/biosynthetic_pathway; /records/3/owner_document/discussions | supports | The complete captured owner retains one partial biosynthesis graph, one explicitly proposed numbered step and the OPEN shared-structure discussion; no complete experimental pathway is inferred. |
| bgc-2634-reader-DATA | /private/tmp/npm-review-work/shared-next-batch264/native-current264-endopyrrole-a-maintained-reader-DATA-001.json; /resolved_view; /counts; /returned_view_equals_expected_complete_owner; /denials; /limitations | supports | The actual maintained view was personally read in full, including every graph, step, reference and history field. Exact preservation is distinct from biological or sequence verification. |
| bgc-2634-reader-execution | /private/tmp/npm-review-work/shared-next-batch264/native-current264-endopyrrole-a-reader-execution-001.json; /command; /exit_code; /stdout; /stderr; /original_tools; /handle_closed | supports | The original maintained-reader execution closed once with exit 0 and preserved genuine stdout/stderr and terminal objects. |
| bgc-2634-reader-acceptance | /private/tmp/npm-review-work/shared-next-batch264/root-native-reader-2634-acceptance-001.json; /accepted; /DATA; /execution; /verification; /review_check_contract; /scope | supports | ROOT accepted this exact positive reader result. One expected IPv6 socket-construction probe was denied before action; no request was sent. |
| bgc-2634-reader-reading | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-current264-Endopyrrole-A-maintained-view-reading-001.json; /complete_owner_read; /counts; /interpretations; /limits | supports | Independent scientific reading of the complete maintained owner preserves the partial, proposed graph and citation limits. |
| bgc-2634-intake | /private/tmp/npm-review-work/shared-next-batch264/intakes-001/2634-inspect-001.json; /targets; /source | supports | Actual canonical inspection captures 47 current input hashes and complete target ownership declarations. Hash capture does not imply whole scientific reading of each input table. |
| bgc-2634-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch264/root-intakes-acceptance-001.json; /accepted; /status; /summary | supports | ROOT accepted the ten actual canonical inspections and their exact 447-input/58-path scope. |
| bgc-2634-plan | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-target-input-plan-001.json; /records/3; /source_placement_count; /unique_source_path_count | supports | This owner has 47 exact planned inputs, now matched to its accepted actual canonical inspection; the full plan has 447 placements/58 paths. |
| bgc-2634-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch264/root-source-plan-acceptance-001.json; /accepted; /status; /plan | supports | ROOT accepted the original local composed input plan; all current input paths and roles are preserved. |
| bgc-2634-chemistry | /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/diagnostic-DATA-001.json; /records/3 | supports | Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons and limited atom correspondence were personally read. No alternative parse was performed. |
| bgc-2634-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/root-diagnostic-acceptance-001.json; /accepted; /status; /DATA; /execution | supports | ROOT accepted the once-only offline diagnostic execution and saved outputs; this does not establish natural identity or full graph equivalence. |
| bgc-2634-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/diagnostic-execution-001.json; /exit_code; /stdout; /stderr | supports | Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr; no diagnostic replay was made. |
| bgc-2634-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/diagnostic-original-001.stderr; Complete original stderr | context_only | The original diagnostic stderr contains six undefined-stereo and two charge-rearrangement warning blocks. They remain global and are not attributed to a particular owner or stored form. |
| bgc-2634-molecular-reading | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-current264-first-five-molecular-intake-reading-001.json; /records/3; /reading_method; /warning_scope; /limitations | supports | Owner-specific complete saved-table reading and interpretation, with normalized identifiers distinguished from canonical correspondence and natural identity. |
| bgc-2634-gates | /private/tmp/npm-review-work/shared-next-batch264/root-native-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /records | supports | Five local checks passed. Full QC and OAK remain unavailable, so native completion and scientific completion are not promoted. |
| bgc-2634-source-reading | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-current264-assigned-source-reading-001.json; /records/6; /full_meaning_scope; /boundaries | supports | Assigned retained-row meanings and all query metadata for this owner were read. References remain retained database assertions rather than newly inspected primary papers. |
| bgc-2634-source-notes | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /reading_boundaries | supports | Original 447-input/58-path source notes preserve disjoint positive-row reading credit 32 BGC + 20 Support + 0 Native. Actual intake acceptance is supported separately. |
| bgc-2634-taxonomy | /private/tmp/npm-review-work/shared-next-batch264-tentative/native-prep/native-current264-cached-taxonomy-reading-001.json; /context_interpretations/6; /interpretation | partial | Owner-local retained taxonomy routes, names and synonyms, with no current rank, lineage or freshness verification. |
| bgc-2634-curation | /private/tmp/npm-review-work/shared-next-batch264-tentative/native-prep/native-current264-implemented-curation-scan-001.json; /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope; /interpretation | context_only | Ignored-inclusive retained curation scope found no exact applicable correction. The producer-strain and row-digest implementation readings retain their bounded scope. |
| bgc-2634-assay-curation | /private/tmp/npm-review-work/shared-next-batch264-tentative/native-prep/native-current264-implemented-curation-scan-001.json; /assay_scope | context_only | The receipt-wide scan has one actual Enterobactin AID placement and two blank-AID sentinels. This first-five owner has no actual AID; Enduracidin A retains one blank sentinel. Fifteen exact exclusions yielded no applicable tuple. The other-owner assay and same-AID exclusion with a different full key/CID are not transferred. |
| bgc-2634-stereo-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 392-396: stereo_complete description | context_only | The maintained flag describes undefined stereocentres; it does not by itself establish full double-bond geometric resolution. |
| bgc-2634-stereo-extractor | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172: FindMolChiralCenters and undefined-tag predicate | context_only | The maintained extractor computes stereo_complete from unassigned tetrahedral chiral-centre tags. No extractor or molecule was rerun for this reading. |
| bgc-2634-stereo-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; line 995: direct stereo_complete copy | context_only | The maintained seeder copies the retained atom-centred boolean without independently resolving geometric stereochemistry. |
| bgc-2634-stereo-policy | /private/tmp/npm-record-reviews-20261021/docs/HARMONIZATION.md; lines 99-104: stereochemical completeness | context_only | The documented retained stereocentre scope is separated from unknown original bond geometry and reconstruction-derived imine descriptors. |
| bgc-2634-delegated-context-reading | /private/tmp/npm-review-work/shared-next-batch264-tentative/support-prep/support-current264-assigned-source-reading-001.json; /contexts | context_only | Support personally read the five complementary selected contexts, including Enduracidin B and the sole actual Enterobactin assay. This preserves attribution without adding BGC primary source-row credit or transferring activity between owners. |
| bgc-2634-direct-contexts | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-target-input-plan-001.json; /records/3/proposed_companion_paths; /records/3/direct_companion_predicates | context_only | This owner has 1 immediate shared-BGC context input(s); the exact predicates do not establish equivalent identity, independent experimental evidence or source transfer. |
| bgc-2634-companion-0 | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/0 | context_only | The exact immediate companion raw/history and query context are retained. Primary readings of contexts 0–7 belong to BGC; contexts 8–12 belong to Support. Only the literal shared-BGC relation is used, with no identity, activity or source-grade transfer. |
| bgc-2634-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds query frame: 2 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2634-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2344-2344; raw record sha256 a611a5632902f246ffb5c38374b2238c99e628a251d15ac49e387dcf56d5c27a | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2634-row-mibig_compounds-1 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 2828-2828; raw record sha256 18d22dc37de080c61bdafba4cb942e692028eb10ab3fda65f8a6e5cfed974a67 | supports | Assigned retained-row reading of all 25 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2634-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2634-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2634-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 3679-3679; raw record sha256 8498ee96a687ab6dce62f61e39e08034e3e1e12fdbc4fb91bf5b02ed39bc2fd3 | supports | Assigned retained-row reading of all 6 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2634-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2634-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier query frame: 1 retained row placement(s), with every field read. Source grain, blank cells and repeated placements remain explicit. |
| bgc-2634-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 1289-1289; raw record sha256 4682b71ca7342c9f64092397c4c00df2b059ec8efdba63efbda7e4552b15d56d | supports | Assigned retained-row reading of all 7 fields at this exact physical record. This row is not newly accessed primary-paper evidence. |
| bgc-2634-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | context_only | Complete saved pubchem_bioassay query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2634-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2634-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2634-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins query frame: 0 retained row placement(s), with every field read. The negative result is restricted to this exact predicate and retained snapshot. |
| bgc-2634-additional-0 | /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained exclusion-table diagnostic context captured for every review; applicable exact assay exclusions and biological rows must be derived from actual retained inventory, not file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-1 | /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained unresolved-taxon diagnostic context used by the bounded curation scan; no fresh taxonomy, forward-merge decision or producer confirmation.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-2 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained explicit forward-merge table used by positive and negative taxon queries for each owner; historical route evidence only, no fresh taxonomy.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-3 | /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Retained non-organism table used by positive and negative taxon queries for each owner; diagnostic scope only, not a taxon verdict from file presence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-4 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Maintained exclusion identity, source-row digest and attributed-rationale implementation context; no execution or new assay evidence.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-5 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py; load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer lines 65-68; _append_evidence lines 78-89 | context_only | Captured additional input role: Maintained producer-strain qualification implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-6 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py; row_digest lines 19-23 only | context_only | Captured additional input role: Maintained row_digest implementation used by qualification guards: sorted ensure_ascii JSON digest only; input presence does not claim an audit or application of other structure-correction behavior.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-7 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/graph_components.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Future maintained complete-owner reader implementation; not invoked in this plan.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| bgc-2634-additional-8 | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/validation/write_validated.py; Exact retained canonical input; bounded use described by source notes and Native curation/taxonomy receipts | context_only | Captured additional input role: Future maintained complete-owner reader implementation; not invoked in this plan.. File presence itself confers no positive source-row, AID, taxon-rank or correction applicability credit. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-264/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-264/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-264/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-264/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-264/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- The complete stored forms were read from the accepted saved diagnostic, without reparsing. Equal normalized identifiers, formula and net charge do not establish complete graph correspondence or natural identity.
- The diagnostic attempts a limited chirality-aware substructure match. Its full_graph_identity_established flag remains false for every record, including a complete one-way match when present.
- Six undefined-stereo and two charge-rearrangement warnings belong to the original global stderr. They are not attributed to a particular owner or form.
- Retained source rows, database references and historical curator annotations were read locally. No primary publication, sequence, live taxonomy authority or external database was newly accessed.
- Cached taxonomy stanzas supply IDs, names and synonyms, without independently verified rank, lineage or current freshness. Occurrence is distinct from production.
- All captured input hashes and ownership declarations were verified; selected source payloads were read within the recorded query scope. This is not a claim to have scientifically read every row of every input table.
- Five local checks passed, but full QC and OAK remain unavailable. Scientific and overall completion therefore remain partial.
- The accepted maintained view preserves the proposed EpyD contribution; it does not independently verify protein grounding, module substrates/products, assembly order or the natural compound.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- The existing OPEN shared-structure discussion is preserved without guessing a replacement identity.
- Endopyrrole B provides direct shared-BGC context only; its compound identity and source claims are not transferred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T013640Z-endopyrrole-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: endopyrrole A'
started_at: '2026-11-06T00:46:30.121032Z'
finished_at: '2026-11-06T01:36:40.581717Z'
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
summary: Endopyrrole A retains consistent normalized chemical encodings and a stereospecified
  cyclic depsipeptide topology. The accepted maintained reader preserves its complete
  owner, partial EpyD graph and explicitly proposed pathway step. That positive preservation
  result does not verify the enzyme mechanism or resolve the OPEN shared-structure
  question spanning two MIBiG entries. The scientific review remains partial.
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
  - path: data/natural_products/amino_acids_and_peptides/endopyrrole-b.yaml
    sha256: 304cecc0a32ce4dabd5d21cc64dc45361761df949d401bf6cbd43e9dda8ca026
    role: context
  - path: data/natural_products/unclassified/endopyrrole-a.yaml
    sha256: 7d884a2049869ab3e300d0dd95e5b89ce2b9fc8e06d9b48377a062bf990936f0
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
  selection: Campaign path order 2634; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-3749610d08
targets:
- target_id: naturalproductmech:mibig-3749610d08
  path: data/natural_products/unclassified/endopyrrole-a.yaml
  label: endopyrrole A
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
    path: data/natural_products/unclassified/endopyrrole-a.yaml
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
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for endopyrrole-a
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch264/read-selected-mechanism-guarded-001.py
    2634 56c03860ba6de66b5e9d7a5fd8df4828e771dc2feb791174ae1b7426207ceb7a 978efb99a073cf9ba96541ef52f2348037f25f089b24d6766efc68f7760c14ca
    6a3b06c6c039569b8337930b1dcdf176bf9ba4744948533aecda6b53b4dcc59f bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
    0659efede4e7ef6ed61ce8853ae18bbd5fba31157707a00a04df4528c7d0ea6a
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: The accepted original reader preserves the complete owner, partial three-node/two-edge
    graph and explicitly proposed step, including all references and four histories.
  scope_note: One expected IPv6 socket-construction probe was denied before action;
    no request was sent. Complete preservation does not independently validate protein
    grounding, publications, natural identity or a full biosynthetic sequence.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-reader-DATA
  - bgc-2634-reader-execution
  - bgc-2634-reader-acceptance
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  command: just validate-strict data/natural_products/unclassified/emericellamide-b.yaml
    data/natural_products/unclassified/emeridone-f.yaml data/natural_products/unclassified/empedopeptin.yaml
    data/natural_products/unclassified/endopyrrole-a.yaml data/natural_products/unclassified/enduracidin-a.yaml
    data/natural_products/unclassified/enduracidin-b.yaml data/natural_products/unclassified/enniatin.yaml
    data/natural_products/unclassified/enterobactin.yaml data/natural_products/unclassified/enteromycin.yaml
    data/natural_products/unclassified/epi-aszonalenin-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-264/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-3749610d08
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-264/validate-all-001.tsv
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
  - naturalproductmech:mibig-3749610d08
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
  - naturalproductmech:mibig-3749610d08
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
  - naturalproductmech:mibig-3749610d08
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-264/review-queue-001.tsv
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
  - naturalproductmech:mibig-3749610d08
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-3749610d08
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-3749610d08
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2634-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/endopyrrole-a.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Complete current owner and all 4 history entries were personally read.
    Historical curator assertions do not confer fresh source-access credit.
  snapshot_sha256: 7d884a2049869ab3e300d0dd95e5b89ce2b9fc8e06d9b48377a062bf990936f0
- evidence_id: bgc-2634-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Actual complete owner capture preserves current local content; it is not
    an independent scientific validation.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3/owner_document/identifier; /records/3/owner_document/label;
    /records/3/owner_document/chemical_structure; /records/3/owner_document/source_concepts;
    /records/3/owner_document/grounding_status
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Exact stored identity, source concepts, grounding and chemical encodings;
    natural identity is assessed separately.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3/owner_document/curation_history
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: All 4 current history entries retain their original source and curation
    scope; no inherited paper access is claimed.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3/owner_document/producer_organisms; /records/3/owner_document/biosynthetic_gene_clusters;
    /records/3/owner_document/source_concepts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Owner-specific producer, locus and source-concept assertions preserve their
    distinct grades and references.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3/owner_document/occurrences; /records/3/owner_document/xrefs
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Current owner occurrence and cross-reference assertions are retained at
    their recorded granularity; neither occurrence nor a cross-reference establishes
    production, activity or molecular mechanism.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3/owner_document/np_pathway; /records/3/owner_document/biosynthesis_origin;
    /records/3/owner_document/np_classification; /records/3/owner_document/bgc_class
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Recorded classification/model labels and BGC class content; exact source
    subclasses remain separately visible in the retained MIBiG row.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-mechanism-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264/owner-capture-DATA-001.json
  locator: /records/3/owner_document/causal_graphs; /records/3/owner_document/biosynthetic_pathway;
    /records/3/owner_document/discussions
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: The complete captured owner retains one partial biosynthesis graph, one
    explicitly proposed numbered step and the OPEN shared-structure discussion; no
    complete experimental pathway is inferred.
  snapshot_sha256: bab7f5d5859678ecdd1df66714f3a457aa37bac4a360e8f98fde0040a18f56a7
- evidence_id: bgc-2634-reader-DATA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/native-current264-endopyrrole-a-maintained-reader-DATA-001.json
  locator: /resolved_view; /counts; /returned_view_equals_expected_complete_owner;
    /denials; /limitations
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: The actual maintained view was personally read in full, including every
    graph, step, reference and history field. Exact preservation is distinct from
    biological or sequence verification.
  snapshot_sha256: ea3282c7c5cec30261b635029ec0c3c989025a67434aaec72adc78b66b813fbb
- evidence_id: bgc-2634-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/native-current264-endopyrrole-a-reader-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /original_tools; /handle_closed
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: The original maintained-reader execution closed once with exit 0 and preserved
    genuine stdout/stderr and terminal objects.
  snapshot_sha256: cc601605b072496bd7a6a0ce4824c711ac9e9a074f971c9e7a713c7a32b31813
- evidence_id: bgc-2634-reader-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/root-native-reader-2634-acceptance-001.json
  locator: /accepted; /DATA; /execution; /verification; /review_check_contract; /scope
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: ROOT accepted this exact positive reader result. One expected IPv6 socket-construction
    probe was denied before action; no request was sent.
  snapshot_sha256: 284b60640a47dc4ae2eb09fcff4811ba37c26e5eb320d0a21634cfb0e38e755e
- evidence_id: bgc-2634-reader-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-current264-Endopyrrole-A-maintained-view-reading-001.json
  locator: /complete_owner_read; /counts; /interpretations; /limits
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Independent scientific reading of the complete maintained owner preserves
    the partial, proposed graph and citation limits.
  snapshot_sha256: 7ca0a0592f4b8972132e4d2b2cf56df984908dfb7071eb91457d6accd2c32a00
- evidence_id: bgc-2634-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/intakes-001/2634-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Actual canonical inspection captures 47 current input hashes and complete
    target ownership declarations. Hash capture does not imply whole scientific reading
    of each input table.
  snapshot_sha256: 978efb99a073cf9ba96541ef52f2348037f25f089b24d6766efc68f7760c14ca
- evidence_id: bgc-2634-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/root-intakes-acceptance-001.json
  locator: /accepted; /status; /summary
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: ROOT accepted the ten actual canonical inspections and their exact 447-input/58-path
    scope.
  snapshot_sha256: aa74ecbf61f31d81529aa45af3d633a31a881c7cb2c854e9af858ad0dc6fecb4
- evidence_id: bgc-2634-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-target-input-plan-001.json
  locator: /records/3; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: This owner has 47 exact planned inputs, now matched to its accepted actual
    canonical inspection; the full plan has 447 placements/58 paths.
  snapshot_sha256: 2705226b5c430928c2851cf11438025ccd351e57b780dcbf8cf274890f7b0d9f
- evidence_id: bgc-2634-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/root-source-plan-acceptance-001.json
  locator: /accepted; /status; /plan
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: ROOT accepted the original local composed input plan; all current input
    paths and roles are preserved.
  snapshot_sha256: 723e3816c8f8f8d7c161d70ec3ea3cb9d831a16b912baa52d1439811b368b00f
- evidence_id: bgc-2634-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/diagnostic-DATA-001.json
  locator: /records/3
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Both complete saved forms, all atom/bond/ring/motif/stereo fields, comparisons
    and limited atom correspondence were personally read. No alternative parse was
    performed.
  snapshot_sha256: 1e3b29a3fc36f2e087e0663c82a6b467b6a5531f944145cae2e1a503e5ca6d50
- evidence_id: bgc-2634-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /accepted; /status; /DATA; /execution
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: ROOT accepted the once-only offline diagnostic execution and saved outputs;
    this does not establish natural identity or full graph equivalence.
  snapshot_sha256: faca5f66ce045ddc74917b68ae747e21812436aaf482944f95a57a0f856ced53
- evidence_id: bgc-2634-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/diagnostic-execution-001.json
  locator: /exit_code; /stdout; /stderr
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Actual diagnostic execution closed with exit 0 and preserved original stdout/stderr;
    no diagnostic replay was made.
  snapshot_sha256: 0495063e54fb070bd45781db49bba5c9bced62b25afb7cc49c070a5b01379df6
- evidence_id: bgc-2634-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The original diagnostic stderr contains six undefined-stereo and two charge-rearrangement
    warning blocks. They remain global and are not attributed to a particular owner
    or stored form.
  snapshot_sha256: a19b73bfc5c524fffb0be731ef03d0e5079407ba1930272132a84089b2b7eae4
- evidence_id: bgc-2634-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-current264-first-five-molecular-intake-reading-001.json
  locator: /records/3; /reading_method; /warning_scope; /limitations
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Owner-specific complete saved-table reading and interpretation, with normalized
    identifiers distinguished from canonical correspondence and natural identity.
  snapshot_sha256: 2e0a472463b34ee6b6a079dc62d8f13d7b8ff3a1e217cf32150b138585da560c
- evidence_id: bgc-2634-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264/root-native-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /records
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Five local checks passed. Full QC and OAK remain unavailable, so native
    completion and scientific completion are not promoted.
  snapshot_sha256: baf93bf8099bff68913668dc6b5e2b751f83316192943d0d10795d716227c2d7
- evidence_id: bgc-2634-source-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-current264-assigned-source-reading-001.json
  locator: /records/6; /full_meaning_scope; /boundaries
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Assigned retained-row meanings and all query metadata for this owner were
    read. References remain retained database assertions rather than newly inspected
    primary papers.
  snapshot_sha256: 1532fbe7c55f60e1579a04c9ca0ac66903a34c4cc751438593096609c31855c6
- evidence_id: bgc-2634-source-notes
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /reading_boundaries
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Original 447-input/58-path source notes preserve disjoint positive-row
    reading credit 32 BGC + 20 Support + 0 Native. Actual intake acceptance is supported
    separately.
  snapshot_sha256: 22d7924e186376d5bd7ba145f0c91033f78d75b9aa8ef1227307afec2b669505
- evidence_id: bgc-2634-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/native-prep/native-current264-cached-taxonomy-reading-001.json
  locator: /context_interpretations/6; /interpretation
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: partial
  summary: Owner-local retained taxonomy routes, names and synonyms, with no current
    rank, lineage or freshness verification.
  snapshot_sha256: 2445775091a3eba203f2d599b79a3cf3955ac557c7ff4ca9d2766a78732adae0
- evidence_id: bgc-2634-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/native-prep/native-current264-implemented-curation-scan-001.json
  locator: /scope; /counts; /exact_predicates; /exact_applicability_resolution; /implementation_scope;
    /interpretation
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: Ignored-inclusive retained curation scope found no exact applicable correction.
    The producer-strain and row-digest implementation readings retain their bounded
    scope.
  snapshot_sha256: ad8a36ff78376d48b61603dfa108557a065ad7c666d015385f1e698fd97afa98
  search_scope: Nine implemented curation/diagnostic tables among eleven enumerated;
    decisions/source_queue excluded. Exact current context predicates applied after
    broad lexical screening; no general absence claim.
- evidence_id: bgc-2634-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/native-prep/native-current264-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The receipt-wide scan has one actual Enterobactin AID placement and two
    blank-AID sentinels. This first-five owner has no actual AID; Enduracidin A retains
    one blank sentinel. Fifteen exact exclusions yielded no applicable tuple. The
    other-owner assay and same-AID exclusion with a different full key/CID are not
    transferred.
  snapshot_sha256: ad8a36ff78376d48b61603dfa108557a065ad7c666d015385f1e698fd97afa98
  search_scope: All fifteen retained exclusion decisions under the implemented exact
    full-key/CID/AID/source-provenance guards; owner assay counts are recorded in
    its own saved query frame.
- evidence_id: bgc-2634-stereo-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: 'lines 392-396: stereo_complete description'
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The maintained flag describes undefined stereocentres; it does not by itself
    establish full double-bond geometric resolution.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2634-stereo-extractor
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines 165-172: FindMolChiralCenters and undefined-tag predicate'
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The maintained extractor computes stereo_complete from unassigned tetrahedral
    chiral-centre tags. No extractor or molecule was rerun for this reading.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2634-stereo-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'line 995: direct stereo_complete copy'
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The maintained seeder copies the retained atom-centred boolean without
    independently resolving geometric stereochemistry.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2634-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/HARMONIZATION.md
  locator: 'lines 99-104: stereochemical completeness'
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The documented retained stereocentre scope is separated from unknown original
    bond geometry and reconstruction-derived imine descriptors.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: bgc-2634-delegated-context-reading
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/support-prep/support-current264-assigned-source-reading-001.json
  locator: /contexts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: Support personally read the five complementary selected contexts, including
    Enduracidin B and the sole actual Enterobactin assay. This preserves attribution
    without adding BGC primary source-row credit or transferring activity between
    owners.
  snapshot_sha256: a9e1476859f45ace2131fd6b4d0d7cf1315815bf8e7b0187c7d3d83491370e45
- evidence_id: bgc-2634-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-target-input-plan-001.json
  locator: /records/3/proposed_companion_paths; /records/3/direct_companion_predicates
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: This owner has 1 immediate shared-BGC context input(s); the exact predicates
    do not establish equivalent identity, independent experimental evidence or source
    transfer.
  snapshot_sha256: 2705226b5c430928c2851cf11438025ccd351e57b780dcbf8cf274890f7b0d9f
- evidence_id: bgc-2634-companion-0
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/0
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: The exact immediate companion raw/history and query context are retained.
    Primary readings of contexts 0–7 belong to BGC; contexts 8–12 belong to Support.
    Only the literal shared-BGC relation is used, with no identity, activity or source-grade
    transfer.
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
- evidence_id: bgc-2634-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: 'Complete saved mibig_compounds query frame: 2 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
- evidence_id: bgc-2634-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2344-2344; raw record sha256 a611a5632902f246ffb5c38374b2238c99e628a251d15ac49e387dcf56d5c27a
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2634-row-mibig_compounds-1
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 2828-2828; raw record sha256 18d22dc37de080c61bdafba4cb942e692028eb10ab3fda65f8a6e5cfed974a67
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Assigned retained-row reading of all 25 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2634-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Complete saved chebi_structures query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
  search_scope: '{"context_path": "data/natural_products/unclassified/endopyrrole-a.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "KRMWEQCPKUMYBI-DKKFUSLWSA-N", "table": "chebi_structures"}'
- evidence_id: bgc-2634-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: 'Complete saved lotus_occurrences query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
- evidence_id: bgc-2634-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 3679-3679; raw record sha256 8498ee96a687ab6dce62f61e39e08034e3e1e12fdbc4fb91bf5b02ed39bc2fd3
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Assigned retained-row reading of all 6 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2634-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
  search_scope: '{"context_path": "data/natural_products/unclassified/endopyrrole-a.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "KRMWEQCPKUMYBI-DKKFUSLWSA-N", "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2634-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: 'Complete saved npclassifier query frame: 1 retained row placement(s),
    with every field read. Source grain, blank cells and repeated placements remain
    explicit.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
- evidence_id: bgc-2634-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 1289-1289; raw record sha256 4682b71ca7342c9f64092397c4c00df2b059ec8efdba63efbda7e4552b15d56d
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: supports
  summary: Assigned retained-row reading of all 7 fields at this exact physical record.
    This row is not newly accessed primary-paper evidence.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2634-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Complete saved pubchem_bioassay query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
  search_scope: '{"context_path": "data/natural_products/unclassified/endopyrrole-a.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "KRMWEQCPKUMYBI-DKKFUSLWSA-N", "table": "pubchem_bioassay"}'
- evidence_id: bgc-2634-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
  search_scope: '{"context_path": "data/natural_products/unclassified/endopyrrole-a.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "KRMWEQCPKUMYBI-DKKFUSLWSA-N", "table": "bindingdb_targets"}'
- evidence_id: bgc-2634-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
  search_scope: '{"context_path": "data/natural_products/unclassified/endopyrrole-a.yaml",
    "matches": 0, "predicate": "exact complete standard_inchi_key equality", "query":
    "KRMWEQCPKUMYBI-DKKFUSLWSA-N", "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2634-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch264-tentative/bgc-prep/bgc-conditional264-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Complete saved chebi_origins query frame: 0 retained row placement(s),
    with every field read. The negative result is restricted to this exact predicate
    and retained snapshot.'
  snapshot_sha256: c177f1e2c93c3ea2fc3093ed8652c06b2ec1ca6457e4e25b62453f888220ea60
  search_scope: '{"context_path": "data/natural_products/unclassified/endopyrrole-a.yaml",
    "matches": 0, "predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "table": "chebi_origins"}'
- evidence_id: bgc-2634-additional-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/pubchem_bioassay_exclusions.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Retained exclusion-table diagnostic context
    captured for every review; applicable exact assay exclusions and biological rows
    must be derived from actual retained inventory, not file presence.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
- evidence_id: bgc-2634-additional-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/curation/unresolved_taxa.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Retained unresolved-taxon diagnostic context
    used by the bounded curation scan; no fresh taxonomy, forward-merge decision or
    producer confirmation.. File presence itself confers no positive source-row, AID,
    taxon-rank or correction applicability credit.'
  snapshot_sha256: 86efbda9c09388723a4f24da35e18404032f1549a9088192fbd2020cb846fa43
- evidence_id: bgc-2634-additional-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_merged.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Retained explicit forward-merge table
    used by positive and negative taxon queries for each owner; historical route evidence
    only, no fresh taxonomy.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 97b3efa66d4fc1679ab65ae547e78b2f627f37bc8e45ae33f2719008fe3863bb
- evidence_id: bgc-2634-additional-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/taxon_non_organism.tsv
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Retained non-organism table used by positive
    and negative taxon queries for each owner; diagnostic scope only, not a taxon
    verdict from file presence.. File presence itself confers no positive source-row,
    AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: f2c1ee257bbbcb0854528196ab1f809d658c27f1c7b2036f7f71f088b52935bb
- evidence_id: bgc-2634-additional-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/bioassay_exclusions.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Maintained exclusion identity, source-row
    digest and attributed-rationale implementation context; no execution or new assay
    evidence.. File presence itself confers no positive source-row, AID, taxon-rank
    or correction applicability credit.'
  snapshot_sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
- evidence_id: bgc-2634-additional-5
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/producer_strains.py
  locator: load_producer_strains lines 12-17; _load_qualifications lines 28-62; qualify_producer
    lines 65-68; _append_evidence lines 78-89
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Maintained producer-strain qualification
    implementation: source-row and digest predicate, strain-only CURATOR_INFERENCE
    scope; plaintext dependency, no execution or grade/taxon upgrade.. File presence
    itself confers no positive source-row, AID, taxon-rank or correction applicability
    credit.'
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: bgc-2634-additional-6
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py
  locator: row_digest lines 19-23 only
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Maintained row_digest implementation used
    by qualification guards: sorted ensure_ascii JSON digest only; input presence
    does not claim an audit or application of other structure-correction behavior..
    File presence itself confers no positive source-row, AID, taxon-rank or correction
    applicability credit.'
  snapshot_sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
- evidence_id: bgc-2634-additional-7
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/graph_components.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Future maintained complete-owner reader
    implementation; not invoked in this plan.. File presence itself confers no positive
    source-row, AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
- evidence_id: bgc-2634-additional-8
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/validation/write_validated.py
  locator: Exact retained canonical input; bounded use described by source notes and
    Native curation/taxonomy receipts
  accessed_at: '2026-11-06T01:28:39.183795Z'
  support: context_only
  summary: 'Captured additional input role: Future maintained complete-owner reader
    implementation; not invoked in this plan.. File presence itself confers no positive
    source-row, AID, taxon-rank or correction applicability credit.'
  snapshot_sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-264/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json
  accessed_at: '2026-11-06T00:53:07.954186Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 59158b4b2b9d2978bf7a9241fc9441589e4060465788f328c8504f0f181c447a
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-264/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json
  accessed_at: '2026-11-06T00:53:34.577071Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 80fddbc4b855754348aacc812708d7cd44dfd60aff64cde9afe4aeec57488421
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-264/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json
  accessed_at: '2026-11-06T00:53:56.182166Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-264/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json
  accessed_at: '2026-11-06T00:54:32.434256Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-264/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-264/native-current264-five-gates-execution-001.json
  accessed_at: '2026-11-06T00:54:44.876230Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: f40d70b647e2e355873c7c8c76963d60f4aa3f8a258e15f24910085fb8ea83ba
assessments:
- assessment_id: bgc-2634-identity
  area: identity
  topic: identity
  outcome: supported
  summary: 'Both saved forms regenerate KRMWEQCPKUMYBI-DKKFUSLWSA-N, C50H67N9O13 and
    net charge 0. BGC0002048 and BGC0002326 retain the same full key and Standard
    InChI but distinct source SMILES strings and source concepts. This supports normalized
    encoding consistency under the MINTED owner identifier. The existing OPEN shared-structure
    discussion remains unresolved: two database entries do not independently establish
    the same natural compound or rule out an upstream cross-reference error. Endopyrrole
    B shares BGC0002048 but has a distinct key and formula.'
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-identity
  - bgc-2634-chemistry
  - bgc-2634-diagnostic-acceptance
  - bgc-2634-query-mibig_compounds
  - bgc-2634-query-chebi_structures
  - bgc-2634-query-antibioticmech_inchikeys
  - bgc-2634-direct-contexts
  - bgc-2634-row-mibig_compounds-0
  - bgc-2634-row-mibig_compounds-1
  - bgc-2634-companion-0
  - bgc-2634-reader-DATA
  - bgc-2634-reader-execution
  - bgc-2634-reader-acceptance
  - bgc-2634-reader-reading
  - bgc-2634-delegated-context-reading
  dimensions:
  - name: standard_inchi_key
    value: KRMWEQCPKUMYBI-DKKFUSLWSA-N; both normalized regenerations agree
    definition: Literal retained full key and accepted saved regeneration scope.
    evidence_ids:
    - bgc-2634-identity
    - bgc-2634-chemistry
    - bgc-2634-diagnostic-acceptance
    - bgc-2634-query-mibig_compounds
    - bgc-2634-query-chebi_structures
    - bgc-2634-query-antibioticmech_inchikeys
    - bgc-2634-direct-contexts
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-companion-0
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
    - bgc-2634-delegated-context-reading
  - name: grounding_scope
    value: MINTED; existing OPEN shared-structure question unresolved
    definition: Recorded grounding category, separated from independent natural identity.
    evidence_ids:
    - bgc-2634-identity
    - bgc-2634-chemistry
    - bgc-2634-diagnostic-acceptance
    - bgc-2634-query-mibig_compounds
    - bgc-2634-query-chebi_structures
    - bgc-2634-query-antibioticmech_inchikeys
    - bgc-2634-direct-contexts
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-companion-0
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
    - bgc-2634-delegated-context-reading
- assessment_id: bgc-2634-representation
  area: representation
  topic: representation
  outcome: supported
  summary: 'Both complete tables contain 72 atoms and 76 bonds: a 13-member ester-containing
    macrocycle, a pyrrole five-member ring, a saturated nitrogen five-member ring
    and two phenyl rings. Nine specified tetrahedral centers and no undefined tetrahedral
    centers are retained. Six of eight original amide placements become C(OH)=N motifs
    with terminal hydroxyl oxygens, while two amides and the ester remain. Six additional
    unspecified C=N descriptors belong to that reconstruction. Both canonical comparisons
    are false and the limited atom correspondence is empty; no full graph or natural-identity
    conclusion is drawn.'
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-identity
  - bgc-2634-chemistry
  - bgc-2634-molecular-reading
  - bgc-2634-diagnostic-acceptance
  - bgc-2634-diagnostic-stderr
  - bgc-2634-row-mibig_compounds-0
  - bgc-2634-row-mibig_compounds-1
  - bgc-2634-stereo-schema
  - bgc-2634-stereo-extractor
  - bgc-2634-stereo-seeder
  - bgc-2634-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    value: 9 specified tetrahedra; 0 undefined; 6 reconstructed unspecified C=N descriptors
    definition: Specified original centers and bond geometry, separated from reconstructed
      imine descriptors.
    evidence_ids:
    - bgc-2634-identity
    - bgc-2634-chemistry
    - bgc-2634-molecular-reading
    - bgc-2634-diagnostic-acceptance
    - bgc-2634-diagnostic-stderr
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-stereo-schema
    - bgc-2634-stereo-extractor
    - bgc-2634-stereo-seeder
    - bgc-2634-stereo-policy
  - name: representation_correspondence
    value: Both canonical comparisons false; empty limited match
    definition: Saved canonical comparisons and limited atom-match result; normalized
      identifiers are not full graph proof.
    evidence_ids:
    - bgc-2634-identity
    - bgc-2634-chemistry
    - bgc-2634-molecular-reading
    - bgc-2634-diagnostic-acceptance
    - bgc-2634-diagnostic-stderr
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-stereo-schema
    - bgc-2634-stereo-extractor
    - bgc-2634-stereo-seeder
    - bgc-2634-stereo-policy
- assessment_id: bgc-2634-provenance
  area: provenance
  topic: provenance
  outcome: unknown
  summary: BGC0002048 version 3 records Mycetohabitans rhizoxinica HKI 454 (NCBITaxon:882378)
    on FR687359.1:1835600–1866150; BGC0002326 version 2 records Mycetohabitans rhizoxinica
    (NCBITaxon:412963) on MN081797.1:1–40068. Both retained producer grades are BGC_CHARACTERIZED
    and both locus grades CLUSTER_DEMONSTRATED with Knock-out studies. Their NRPS
    class and Type I subclass remain separate. The rows have questionable entry quality.
    The strain-specific and broader names are retained as source context without newly
    verifying rank or ancestry.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-owner
  - bgc-2634-provenance
  - bgc-2634-query-mibig_compounds
  - bgc-2634-query-lotus_occurrences
  - bgc-2634-taxonomy
  - bgc-2634-curation
  - bgc-2634-direct-contexts
  - bgc-2634-row-mibig_compounds-0
  - bgc-2634-row-mibig_compounds-1
  - bgc-2634-row-lotus_occurrences-0
  - bgc-2634-companion-0
  - bgc-2634-reader-DATA
  - bgc-2634-reader-execution
  - bgc-2634-reader-acceptance
  - bgc-2634-reader-reading
  - bgc-2634-delegated-context-reading
  dimensions:
  - name: taxon_scope
    value: 882378 and 412963 retained; strain/name context is not new lineage verification
    definition: Retained names, IDs and synonyms; current rank and ancestry are not
      independently established.
    evidence_ids:
    - bgc-2634-owner
    - bgc-2634-provenance
    - bgc-2634-query-mibig_compounds
    - bgc-2634-query-lotus_occurrences
    - bgc-2634-taxonomy
    - bgc-2634-curation
    - bgc-2634-direct-contexts
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-row-lotus_occurrences-0
    - bgc-2634-companion-0
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
    - bgc-2634-delegated-context-reading
  - name: producer_evidence
    value: Both BGC_CHARACTERIZED
    definition: Literal source grade for the compound producer assertion.
    evidence_ids:
    - bgc-2634-owner
    - bgc-2634-provenance
    - bgc-2634-query-mibig_compounds
    - bgc-2634-query-lotus_occurrences
    - bgc-2634-taxonomy
    - bgc-2634-curation
    - bgc-2634-direct-contexts
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-row-lotus_occurrences-0
    - bgc-2634-companion-0
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
    - bgc-2634-delegated-context-reading
  - name: locus_evidence
    value: 'BGC0002048 and BGC0002326: CLUSTER_DEMONSTRATED; Knock-out studies'
    definition: Literal source grade for the locus-to-compound assertion.
    evidence_ids:
    - bgc-2634-owner
    - bgc-2634-provenance
    - bgc-2634-query-mibig_compounds
    - bgc-2634-query-lotus_occurrences
    - bgc-2634-taxonomy
    - bgc-2634-curation
    - bgc-2634-direct-contexts
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-row-lotus_occurrences-0
    - bgc-2634-companion-0
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
    - bgc-2634-delegated-context-reading
- assessment_id: bgc-2634-citations
  area: evidence
  topic: citations
  outcome: unknown
  summary: The two source rows use ENTRY references PMID:21131495 and PMID:31283172.
    The graph and proposed step additionally retain DOI:10.1021/ACSCHEMBIO.9B00406
    and UniProt/GenPept/GenBank references. Six graph and four step reference placements
    reuse these sources; they are not ten independent experiments. PRIMARY_EXPERIMENT
    labels and historical sequence/CDS claims are preserved curator annotations, without
    new primary-paper or sequence access. The LOTUS DOI may refer to the same publication
    and does not supply established independent evidence.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-provenance
  - bgc-2634-query-mibig_compounds
  - bgc-2634-query-lotus_occurrences
  - bgc-2634-query-chebi_origins
  - bgc-2634-source-reading
  - bgc-2634-history
  - bgc-2634-row-mibig_compounds-0
  - bgc-2634-row-mibig_compounds-1
  - bgc-2634-row-lotus_occurrences-0
  - bgc-2634-companion-0
  - bgc-2634-reader-DATA
  - bgc-2634-reader-execution
  - bgc-2634-reader-acceptance
  - bgc-2634-reader-reading
  - bgc-2634-delegated-context-reading
  dimensions:
  - name: citation_scope
    value: Two ENTRY PMIDs; graph/step references retain historical source labels
    definition: Reference grain in the retained source rows; no inherited primary-paper
      access.
    evidence_ids:
    - bgc-2634-provenance
    - bgc-2634-query-mibig_compounds
    - bgc-2634-query-lotus_occurrences
    - bgc-2634-query-chebi_origins
    - bgc-2634-source-reading
    - bgc-2634-history
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
    - bgc-2634-row-lotus_occurrences-0
    - bgc-2634-companion-0
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
    - bgc-2634-delegated-context-reading
- assessment_id: bgc-2634-occurrence_activity
  area: evidence
  topic: occurrence_activity
  outcome: unknown
  summary: The LOTUS occurrence at NCBITaxon:412963 retains the label Burkholderia
    rhizoxinica, whereas producer assertions use Mycetohabitans names. Cached naming
    context does not create a fresh taxonomic verification. The occurrence is explicitly
    distinct from production, and publication independence is unestablished. No actual
    AID, direct molecular target or activity root was found in this owner scope. The
    partial biosynthesis graph is not a pharmacological mechanism or an assay result.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-activity-owner
  - bgc-2634-query-lotus_occurrences
  - bgc-2634-query-chebi_origins
  - bgc-2634-query-cyanometdb_occurrences
  - bgc-2634-query-pubchem_bioassay
  - bgc-2634-query-bindingdb_targets
  - bgc-2634-query-antibioticmech_inchikeys
  - bgc-2634-assay-curation
  - bgc-2634-direct-contexts
  - bgc-2634-row-lotus_occurrences-0
  - bgc-2634-companion-0
  - bgc-2634-delegated-context-reading
  dimensions:
  - name: occurrence_scope
    value: 1 LOTUS placement; independence from producer citations unestablished
    definition: Exact retained occurrence query scope, without production or independence
      transfer.
    evidence_ids:
    - bgc-2634-activity-owner
    - bgc-2634-query-lotus_occurrences
    - bgc-2634-query-chebi_origins
    - bgc-2634-query-cyanometdb_occurrences
    - bgc-2634-query-pubchem_bioassay
    - bgc-2634-query-bindingdb_targets
    - bgc-2634-query-antibioticmech_inchikeys
    - bgc-2634-assay-curation
    - bgc-2634-direct-contexts
    - bgc-2634-row-lotus_occurrences-0
    - bgc-2634-companion-0
    - bgc-2634-delegated-context-reading
  - name: assay_target_scope
    value: 0 actual AID rows; biosynthesis graph is not a pharmacological target claim
    definition: Actual AID, endpoint and direct-target scope, including sentinels
      and exclusions.
    evidence_ids:
    - bgc-2634-activity-owner
    - bgc-2634-query-lotus_occurrences
    - bgc-2634-query-chebi_origins
    - bgc-2634-query-cyanometdb_occurrences
    - bgc-2634-query-pubchem_bioassay
    - bgc-2634-query-bindingdb_targets
    - bgc-2634-query-antibioticmech_inchikeys
    - bgc-2634-assay-curation
    - bgc-2634-direct-contexts
    - bgc-2634-row-lotus_occurrences-0
    - bgc-2634-companion-0
    - bgc-2634-delegated-context-reading
- assessment_id: bgc-2634-classification
  area: consistency
  topic: classification
  outcome: unknown
  summary: The ester-containing peptide macrocycle supports broad Cyclic peptides
    and Depsipeptides descriptions. The saved tables also retain a pyrrole, two phenyl
    rings and a saturated nitrogen ring; these do not establish enzyme-module assignments.
    NPClassifier reports Amino acids and Peptides, Polyketides and Oligopeptides,
    with is_glycoside false. Exact model and polyketide biosynthetic applicability
    remain bounded, and the proposed EpyD contribution does not complete the entire
    biosynthetic pathway.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-classification-owner
  - bgc-2634-query-npclassifier
  - bgc-2634-query-mibig_compounds
  - bgc-2634-chemistry
  - bgc-2634-molecular-reading
  - bgc-2634-row-npclassifier-0
  - bgc-2634-row-mibig_compounds-0
  - bgc-2634-row-mibig_compounds-1
  dimensions:
  - name: classification_applicability
    value: Cyclic depsipeptide topology supported; model and full pathway applicability
      bounded
    definition: Encoded motif support separated from exact computed model-family or
      biosynthesis claims.
    evidence_ids:
    - bgc-2634-classification-owner
    - bgc-2634-query-npclassifier
    - bgc-2634-query-mibig_compounds
    - bgc-2634-chemistry
    - bgc-2634-molecular-reading
    - bgc-2634-row-npclassifier-0
    - bgc-2634-row-mibig_compounds-0
    - bgc-2634-row-mibig_compounds-1
- assessment_id: bgc-2634-completion
  area: completeness
  topic: completion
  outcome: unknown
  summary: All 47 actual input hashes and ownership declarations, the complete owner/history,
    selected source payloads and both complete molecular forms were reviewed. The
    one accepted maintained-reader execution preserves the entire owner, graph and
    proposed step exactly; its typed check is linked to the actual DATA, execution
    and ROOT acceptance. One expected IPv6 socket-construction probe was denied before
    action, with no request. Five local gates passed, but full QC, OAK, independent
    primary-source validation and resolution of the existing identity discussion remain
    incomplete.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-intake
  - bgc-2634-intake-acceptance
  - bgc-2634-plan
  - bgc-2634-plan-acceptance
  - bgc-2634-gates
  - bgc-2634-source-reading
  - bgc-2634-source-notes
  - bgc-2634-molecular-reading
  - bgc-2634-diagnostic-acceptance
  - bgc-2634-mechanism-scope
  - bgc-2634-reader-DATA
  - bgc-2634-reader-execution
  - bgc-2634-reader-acceptance
  - bgc-2634-reader-reading
  dimensions:
  - name: review_completion
    value: Partial; 47 actual inputs, both forms and accepted complete reader reviewed
    definition: Actual local review scope and unavailable required gates.
    evidence_ids:
    - bgc-2634-intake
    - bgc-2634-intake-acceptance
    - bgc-2634-plan
    - bgc-2634-plan-acceptance
    - bgc-2634-gates
    - bgc-2634-source-reading
    - bgc-2634-source-notes
    - bgc-2634-molecular-reading
    - bgc-2634-diagnostic-acceptance
    - bgc-2634-mechanism-scope
    - bgc-2634-reader-DATA
    - bgc-2634-reader-execution
    - bgc-2634-reader-acceptance
    - bgc-2634-reader-reading
- assessment_id: bgc-2634-graph
  area: graph
  topic: proposed_EpyD_contribution
  outcome: supported
  summary: The actual maintained view preserves one BIOSYNTHESIS graph with three
    nodes and two contributes-to edges, plus numbered pathway step 1 with proposed:true.
    EpyD is grounded to UniProtKB:A0A6G7BMN0; the NRPS assembly process remains ungrounded
    and the compound node uses the exact owner identifier. The whole view matches
    the captured owner, including all references and four histories. This supports
    faithful representation of a partial proposed contribution, not an experimentally
    established complete reaction sequence. Individual module substrates and products
    remain unexpanded.
  target_ids:
  - naturalproductmech:mibig-3749610d08
  evidence_ids:
  - bgc-2634-reader-DATA
  - bgc-2634-reader-execution
  - bgc-2634-reader-acceptance
  - bgc-2634-reader-reading
  - bgc-2634-mechanism-scope
  - bgc-2634-provenance
  - bgc-2634-source-reading
  dimensions: []
findings: []
actions: []
limitations:
- The complete stored forms were read from the accepted saved diagnostic, without
  reparsing. Equal normalized identifiers, formula and net charge do not establish
  complete graph correspondence or natural identity.
- The diagnostic attempts a limited chirality-aware substructure match. Its full_graph_identity_established
  flag remains false for every record, including a complete one-way match when present.
- Six undefined-stereo and two charge-rearrangement warnings belong to the original
  global stderr. They are not attributed to a particular owner or form.
- Retained source rows, database references and historical curator annotations were
  read locally. No primary publication, sequence, live taxonomy authority or external
  database was newly accessed.
- Cached taxonomy stanzas supply IDs, names and synonyms, without independently verified
  rank, lineage or current freshness. Occurrence is distinct from production.
- All captured input hashes and ownership declarations were verified; selected source
  payloads were read within the recorded query scope. This is not a claim to have
  scientifically read every row of every input table.
- Five local checks passed, but full QC and OAK remain unavailable. Scientific and
  overall completion therefore remain partial.
- The accepted maintained view preserves the proposed EpyD contribution; it does not
  independently verify protein grounding, module substrates/products, assembly order
  or the natural compound.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- The existing OPEN shared-structure discussion is preserved without guessing a replacement
  identity.
- Endopyrrole B provides direct shared-BGC context only; its compound identity and
  source claims are not transferred.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-264
```
