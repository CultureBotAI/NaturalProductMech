# Local evidence review: 10-epi-xanthobaccin C

- Review: 20261104T203214Z-10-epi-xanthobaccin-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T20:02:03.826368Z
- Finished UTC: 2026-11-04T20:32:14.282688Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

10-epi-xanthobaccin C retains its exact MIBiG identity, partial stereochemistry and source-qualified BGC2365 provenance. The accepted local forms agree in normalized InChI/key, formula and charge but differ at two amide/imidic representations; natural identity and specific classifier-family applicability remain unverified. Local review is partial, with no supported source-edit finding.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2441; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-9606620456 | data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml | generated | 10-epi-xanthobaccin C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-9606620456 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-9606620456 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-9606620456 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-9606620456 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-9606620456 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-9606620456 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-9606620456 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-9606620456 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained identity and bounded correspondence

identity: supported. Targets: naturalproductmech:mibig-9606620456.

The minted identifier naturalproductmech:mibig-9606620456 and full key DAZWHCJBSRQVSC-LQXARYHSSA-N belong to the retained MIBiG BGC0002365 compound 4, not to the five related BGC congeners. Both saved forms reproduce this full key and C29H38N2O5 with zero formal charge. Their canonical strings differ and the supplied atom map is empty, so normalized agreement does not prove full graph or natural-state identity. NPA026680 is a retained cross-reference; the bounded exact-key ChEBI join is empty, not a fresh database-wide absence claim.

### Stored-form stereochemistry and topology limits

representation: supported. Targets: naturalproductmech:mibig-9606620456.

The stored false stereo flag is consistent with eight specified and one unspecified tetrahedral center in each saved form. The SMILES table also has two specified alkene geometries and one unspecified double bond. The reconstructed InChI form retains an unknown double bond and adds an unspecified C=N potential center. SMILES amides C17/N19 and C25/N24 instead appear as C-single-O/double-N sites C28/N30/O35 and C23/N29/O33 in the reconstructed form; their N-H/O-H and bond-order differences are representation-specific. Neither encoding is selected as the natural tautomer or rewritten.

### Separate producer, locus and taxon assertions

provenance: supported. Targets: naturalproductmech:mibig-9606620456.

MIBiG BGC0002365 version 2 associates the compound with Streptomyces sp. NCBITaxon:1931 at SOURCE_ASSERTION. Its MN234160.1 locus spans 1–17258, remains CLUSTER_UNSTATED and supplies no experimental locus-method list. The LOTUS genus-level Streptomyces NCBITaxon:1883 occurrence has a different evidential role and does not supply a strain or upgrade production. Shared locus membership with five related owners does not transfer their stereochemistry or activity.

### Citation tiers and seed-history scope

evidence: supported. Targets: naturalproductmech:mibig-9606620456.

The MIBiG PMID:31775228 reference is explicitly ENTRY evidence. The separate LOTUS DOI:10.3390/MD17120663 supports the retained occurrence assertion, without proving independent experiments or the MIBiG strain. Neither primary publication was freshly accessed. The two SEEDED_FROM_SOURCES events document inventory seeding, not experimental verification, and the record remains MINTED/SEEDED.

### Finite occurrence and assay scope

evidence: supported. Targets: naturalproductmech:mibig-9606620456.

One exact-key LOTUS row and the matching retained owner occurrence concern Streptomyces at genus scope. The saved ChEBI-origin and CyanoMetDB joins are empty, as are PubChem BioAssay and BindingDB; this owner has no activity, molecular-target or mechanism roots. These bounded local absences do not show biological inactivity or absence from other sources. No congener assay is transferred.

### Model fidelity with specific family applicability unverified

consistency: unknown. Targets: naturalproductmech:mibig-9606620456.

NPClassifier version 2026-09-07 retains both Amino acids and Peptides and Polyketides, Macrolides and Macrocyclic tetramic acids, with glycoside false. The seeder deliberately files multiple pathway labels as UNCLASSIFIED rather than discarding either label. The N-containing macrocycle and carbonyl-bearing five-membered ring are compatible with a mixed peptide/polyketide context, but the specific named model families remain model assertions, not independently established biosynthetic or natural-identity conclusions. Tautomer-dependent amide counts do not by themselves demonstrate classifier or source-ingestion error.

### Actual evidence coverage and remaining limits

completeness: unknown. Targets: naturalproductmech:mibig-9606620456.

The complete owner and both seed histories, accepted 42-input canonical intake, all nine selected saved source frames, full paired molecular tables and direct shared-BGC context have been reviewed. No graph, pathway, component reference or molecular target is declared, so a maintained-reader check does not apply. Fresh primary evidence, independent natural stereochemistry, full QC and complete OAK coverage remain unavailable; this is a partial review without a source/status/history edit.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2441-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml; Complete plaintext including every curation_history entry | supports | Complete 10-epi-xanthobaccin C owner and both seed-history events; MINTED/SEEDED unchanged. Prior complete raw/history reading carries with current identical bytes. |
| bgc-2441-capture | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0 | supports | Complete actual owner capture, metadata, root presence and empty component captures; preservation is not independent scientific validation. |
| bgc-2441-intake | /private/tmp/npm-review-work/shared-next-batch245/intakes/2441-inspect-001.json; /status; /repository; /source; /targets | supports | Actual canonical target, ownership declarations and all 42 current input placements joined to the exact plan. |
| bgc-2441-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch245/root-intake-acceptance-001.json; /status; /summary; /source_plan; /intakes/0 | supports | ROOT accepted the original canonical intake and exact source plan; this record’s intake, execution and target-spec pins are preserved. |
| bgc-2441-grounding-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0/owner_document/identifier; /records/0/owner_document/label; /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs; /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status; /records/0/owner_document/grounding_notes | supports | Exact retained identifier, structure, source concepts and grounding fields; cross-references only where present. Historical grounding notes are not fresh external searches. |
| bgc-2441-origin-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups; /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts | supports | Exact producer and locus grades, experimental methods, accession/coordinates and source citation tiers; organism/strain and locus evidence remain separate. |
| bgc-2441-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0/owner_document | supports | Complete owner occurrence and absence of activity/target/mechanism roots; finite owner scope only. |
| bgc-2441-classification-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway; /records/0/owner_document/bgc_class | supports | Named/versioned classifier arrays and glycoside flag, UNCLASSIFIED filing and separately retained source classes; fidelity does not establish specific family applicability. |
| bgc-2441-history-owner | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0/owner_document/curation_status; /records/0/owner_document/curation_history | supports | Both complete seed-history entries and unchanged SEEDED status; seeding is not primary experimental verification. |
| bgc-2441-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json; /records/0/owner_document | supports | Whole selected owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets. No maintained-reader result applies to this record. |
| bgc-2441-chemistry | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/formula; /records/0/smiles/computed/formal_charge; /records/0/smiles/computed/standard_inchi; /records/0/smiles/computed/standard_inchi_key; /records/0/smiles/computed/canonical_isomeric_smiles; /records/0/smiles/computed/canonical_nonisomeric_smiles; /records/0/smiles/computed/atom_count; /records/0/smiles/computed/heavy_atom_count; /records/0/smiles/computed/bond_count; /records/0/smiles/computed/element_counts; /records/0/smiles/computed/stereo_counts; /records/0/inchi/computed/formula; /records/0/inchi/computed/formal_charge; /records/0/inchi/computed/standard_inchi; /records/0/inchi/computed/standard_inchi_key; /records/0/inchi/computed/canonical_isomeric_smiles; /records/0/inchi/computed/canonical_nonisomeric_smiles; /records/0/inchi/computed/atom_count; /records/0/inchi/computed/heavy_atom_count; /records/0/inchi/computed/bond_count; /records/0/inchi/computed/element_counts; /records/0/inchi/computed/stereo_counts | supports | Eight comparisons agree, two canonical-string comparisons are false, and the supplied atom correspondence is empty. Normalized equality does not establish fixed-form graph or natural identity. The explicit full_graph_identity_established flag remains false. |
| bgc-2441-topology | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json; /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons; /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds; /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo; /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices; /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings; /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs; /records/0/inchi/computed/fragment_atom_indices | supports | Both saved forms contain 36 heavy atoms, 40 bonds and five reported rings. The SMILES form has four carbonyl sites and two amides; the InChI reconstruction has two carbonyl sites and two C-single-O/double-N sites, with exact differing hydrogen/bond neighborhoods retained. Neither form reports a saturated six-membered C5O cycle or phosphorus. The original chirality-aware correspondence is empty and full_graph_identity_established is false. |
| bgc-2441-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-first-five-diagnostic-reading-001.json; /records/0; /read_scope; /totals; /representation; /reading_caveats | supports | BGC personally read every field of all ten first-five forms, 370 atom rows and 420 bond rows, and all 201 intake placements/51 paths. Exact lossless reconstruction and original reading objects are retained; no reparse. |
| bgc-2441-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/0; /molecular_parse_attempts; /parsed; /global_warning_count; /method_scope; /interpretation_boundary | supports | ROOT accepted the original twenty stored-form diagnostic; this owner’s actual comparison/correspondence scope is located. Global warning count is zero; no alternative normalization repair is inferred. |
| bgc-2441-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-execution-001.json; /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original diagnostic command, times, zero exit and stream pins; stderr is empty as its zero-byte pin records. |
| bgc-2441-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines 392–430 | supports | Undefined stereo is retained rather than fabricated; computed classifications are named/versioned model results, never source assertions. |
| bgc-2441-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines 165–173 | supports | stereo_complete is computed with FindMolChiralCenters including unassigned centers; it does not independently verify natural identity or all double-bond geometry. |
| bgc-2441-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines 295–306; 988–1022 | supports | Multiple classifier pathways yield UNCLASSIFIED filing while arrays are retained. Filing and model fidelity do not establish biological applicability. |
| bgc-2441-source-reading | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-assigned-source-reading-001.json; /scope; /reading; /records; /cautions; /physical_verification | supports | BGC personally read ten assigned contexts, 90 frames, 28 positive rows and 373 fields; selected five account for 45 frames/13 rows/183 fields. Prior companion whole-body readings remain explicitly attributed. |
| bgc-2441-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts; /reading_boundaries | supports | Disjoint complete source reading totals 225 frames/120 rows/1294 fields: BGC 28 rows, ROOT 60, Support 32; Native taxonomy/curation credit is separate. Preferred corrected ROOT CPA002 is retained without transferring its precursor claims. |
| bgc-2441-source-plan-execution | /private/tmp/npm-review-work/shared-next-batch245/bgc-source-plan-execution-001.json; /status; /source; /original_tools; /original_terminal; /exit_code; /plan; /derivation; /inventory; /notes; /verification | supports | The one original local composer produced the exact 400-placement/66-path plan with 31 verified derivation operations. Actual intake acceptance separately binds this plan; historical conditional fields remain unchanged. |
| bgc-2441-native-gate-limits | /private/tmp/npm-review-work/shared-next-batch245/root-native-five-gates-acceptance-001.json; /status; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates | supports | Five local commands passed; full QC and complete OAK remain unavailable. Passing local syntax/reproduction checks does not complete scientific verification. |
| bgc-2441-curation-scope | /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-implemented-curation-scan-001.json; /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation | supports | Native’s bounded ignored-inclusive scan found one applicable BGC0977 override for selected order2447, outside these first five; none applies to this owner. No assay exclusion is borrowed by shared names or locus alone. |
| bgc-2441-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/2 | supports | Complete retained cache stanzas for this owner’s source taxon IDs. Names/synonyms are cached context, not a fresh taxonomic or strain determination. |
| bgc-2441-taxonomy-routes | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/source_taxa; /contexts/6/source_scope_inventory/forward_taxon_merge_matches; /contexts/6/source_scope_inventory/nonorganism_matches | supports | All saved taxon IDs and forwarding/nonorganism routes for this selected source context, including empty routes; no fresh taxonomy request. |
| bgc-2441-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-cached-taxonomy-reading-001.json; /scope; /counts; /complete_readings; /forward_routes; /interpretation | supports | Native personally read all 32 complete cached stanzas and four saved forwarding routes across the full batch context. This attribution does not duplicate positive-row credit or transfer species/strain roles. |
| bgc-2441-direct-contexts | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-target-input-plan-001.json; /records/0/proposed_companion_paths; /records/0/direct_companion_predicates | supports | Literal one-hop shared-BGC predicates and exact direct companion paths only; no transitive expansion or transfer of identity, stereochemistry, activity or mechanism. |
| bgc-2441-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/1/path; /contexts/1/identifier; /contexts/1/label; /contexts/1/standard_inchi_key; /contexts/1/owned_bgc_ids; /contexts/2/path; /contexts/2/identifier; /contexts/2/label; /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/3/path; /contexts/3/identifier; /contexts/3/label; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids; /contexts/4/path; /contexts/4/identifier; /contexts/4/label; /contexts/4/standard_inchi_key; /contexts/4/owned_bgc_ids; /contexts/5/path; /contexts/5/identifier; /contexts/5/label; /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids | supports | Distinct full keys, identities, labels and owned loci define the selected owner’s direct context; shared BGC membership is not identity equivalence. |
| bgc-2441-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame contains 1 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2902–2902; row_sha256 ce34c93f6331ac9ab077ad29e4f673bec891ca686f854dde002c73d7ee6f3437 | supports | Exact full-key/version/compound-index, producer/locus grades and citation-tier fields. BGC complete selected source-row reading and current physical bytes are joined. |
| bgc-2441-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame contains 1 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 1007–1007; row_sha256 cdb6607c3d70c48cdd2f080f825f0fe768a802472eafd202ded121c1f9c04b7b | supports | Complete retained organism/reference occurrence assertion, with species/genus scope separate from source strain; repeated citations do not prove independent studies. BGC complete selected source-row reading and current physical bytes are joined. |
| bgc-2441-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame contains 1 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 377–377; row_sha256 38b1f71c6b3014d5a0bd9501da1de4b416f80178d487a943065808f3519e9204 | supports | Exact named/versioned model arrays and glycoside flag; scientific applicability is not guaranteed by retention. BGC complete selected source-row reading and current physical bytes are joined. |
| bgc-2441-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| bgc-2441-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json; /contexts/6/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame contains 0 placements; its exact predicate, query and all fields define the bounded result. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-245/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-245/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-245/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-245/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-245/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only. Fresh primary literature, current taxonomy, assay protocols and independent natural identity/stereochemical authentication remain unavailable.
- Five local native commands passed, but full QC and complete OAK remain unavailable. Saved normalized forms and atom matches do not establish independent full graph or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain separate. Shared BGC membership and repeated references do not transfer biological claims or establish independent experiments.
- Named model-family applicability is explicitly unverified; retention fidelity and broad structural compatibility do not establish a specific biosynthetic family or a source-ingestion defect.
- The complete selected owner has no graph, pathway, component reference or molecular-target root. No maintained-reader result, source edit or status/history promotion is claimed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read ten first-five saved forms: 370 atom rows and 420 bond rows, complete strings/scalars/rings/stereo/motifs/maps; indices are diagnostic-local. The original diagnostic stderr was empty. No reparse occurred during review.
- Disjoint source reading: BGC 10 contexts/90 frames/28 rows/373 fields; ROOT 7 contexts/63 frames/60 rows/558 fields; Support 8 contexts/72 frames/32 rows/363 fields. Native read 32 cached stanzas and bounded curation, with zero positive-row credit. Prior raw/history readings and preferred ROOT CPA002 remain attributed.
- BGC operated the original local collector and composer; Support operated canonical intakes; Native operated the original molecular diagnostic under ROOT delegation. Final report authoring only reads saved evidence and writes review artifacts.
- All first-five reviews remain partial. No supported source-edit finding or action is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T203214Z-10-epi-xanthobaccin-c
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 10-epi-xanthobaccin C'
started_at: '2026-11-04T20:02:03.826368Z'
finished_at: '2026-11-04T20:32:14.282688Z'
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
summary: 10-epi-xanthobaccin C retains its exact MIBiG identity, partial stereochemistry
  and source-qualified BGC2365 provenance. The accepted local forms agree in normalized
  InChI/key, formula and charge but differ at two amide/imidic representations; natural
  identity and specific classifier-family applicability remain unverified. Local review
  is partial, with no supported source-edit finding.
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
  - path: data/natural_products/unclassified/10-epi-3-deoh-hsaf.yaml
    sha256: 90eca40cfa9209661ebc3590955fde9290a1ae92609a6d937285f8131545c9d0
    role: context
  - path: data/natural_products/unclassified/10-epi-fi-2.yaml
    sha256: 6f4336cecf8df43458b865a47296f614c21e6eb828fd59ffb6380b22b2a339e2
    role: context
  - path: data/natural_products/unclassified/10-epi-hsaf.yaml
    sha256: eeaab19285b49ab8db440d2a956bf43aeba58bf61b13600fcf0b8b451357a604
    role: context
  - path: data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml
    sha256: 40aac5575689675dbe8b183adac018c571d568ed58f532da74761f5b2658707a
    role: context
  - path: data/natural_products/unclassified/10-epi-maltophilin.yaml
    sha256: 046fa4ed6b2a5d9119994bde1849ec0b83c3981155b86d393a48dadb9ee8f006
    role: context
  - path: data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml
    sha256: a3bb47cd5f301033a5ba375388e5966dce77323ed82dbcaed63b85b960d4e383
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
  selection: Campaign path order 2441; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-9606620456
targets:
- target_id: naturalproductmech:mibig-9606620456
  path: data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml
  label: 10-epi-xanthobaccin C
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
  - naturalproductmech:mibig-9606620456
  command: just validate-strict data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml
    data/natural_products/unclassified/13-epi-higginsianin-c.yaml data/natural_products/unclassified/14-hydroxypaspalinine.yaml
    data/natural_products/unclassified/14-leucyloxy-paspalinine.yaml data/natural_products/unclassified/14-n-n-dimethylleucyloxy-paspalinine.yaml
    data/natural_products/unclassified/2-methoxy-5-methyl-6-13-methyltetradecyl-1-4-benzoquinone.yaml
    data/natural_products/unclassified/2-oxocyclopiazonic-acid.yaml data/natural_products/unclassified/21-22-diprenylated-paxilline.yaml
    data/natural_products/unclassified/2r-3s-4s-5-fluoro-2-3-4-trihydroxypentanoic-acid.yaml
    data/natural_products/unclassified/4-deoxygadusol.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-245/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-9606620456
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-245/validate-all-001.tsv
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
  - naturalproductmech:mibig-9606620456
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
  - naturalproductmech:mibig-9606620456
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
  - naturalproductmech:mibig-9606620456
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-245/review-queue-001.tsv
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
  - naturalproductmech:mibig-9606620456
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-9606620456
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-9606620456
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2441-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml
  locator: Complete plaintext including every curation_history entry
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete 10-epi-xanthobaccin C owner and both seed-history events; MINTED/SEEDED
    unchanged. Prior complete raw/history reading carries with current identical bytes.
  snapshot_sha256: a3bb47cd5f301033a5ba375388e5966dce77323ed82dbcaed63b85b960d4e383
- evidence_id: bgc-2441-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete actual owner capture, metadata, root presence and empty component
    captures; preservation is not independent scientific validation.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/intakes/2441-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Actual canonical target, ownership declarations and all 42 current input
    placements joined to the exact plan.
  snapshot_sha256: b97903a72b12cacf47b5f3e936bdf5b30e168bed1eb3dac9f452c489d9150f3b
- evidence_id: bgc-2441-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/root-intake-acceptance-001.json
  locator: /status; /summary; /source_plan; /intakes/0
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: ROOT accepted the original canonical intake and exact source plan; this
    record’s intake, execution and target-spec pins are preserved.
  snapshot_sha256: b5e9b8a29b2595e6870fb8f9ccc97a7ac56051767c54f32ccb565669667ad062
- evidence_id: bgc-2441-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0/owner_document/identifier; /records/0/owner_document/label;
    /records/0/owner_document/chemical_structure; /records/0/owner_document/xrefs;
    /records/0/owner_document/source_concepts; /records/0/owner_document/grounding_status;
    /records/0/owner_document/grounding_notes
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact retained identifier, structure, source concepts and grounding fields;
    cross-references only where present. Historical grounding notes are not fresh
    external searches.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0/owner_document/producer_organisms; /records/0/owner_document/producer_taxon_groups;
    /records/0/owner_document/biosynthetic_gene_clusters; /records/0/owner_document/source_concepts
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact producer and locus grades, experimental methods, accession/coordinates
    and source citation tiers; organism/strain and locus evidence remain separate.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete owner occurrence and absence of activity/target/mechanism roots;
    finite owner scope only.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0/owner_document/np_classification; /records/0/owner_document/np_pathway;
    /records/0/owner_document/bgc_class
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Named/versioned classifier arrays and glycoside flag, UNCLASSIFIED filing
    and separately retained source classes; fidelity does not establish specific family
    applicability.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0/owner_document/curation_status; /records/0/owner_document/curation_history
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Both complete seed-history entries and unchanged SEEDED status; seeding
    is not primary experimental verification.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/owner-capture-DATA-001.json
  locator: /records/0/owner_document
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Whole selected owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets. No maintained-reader result applies to this record.
  snapshot_sha256: 73dda5dacd4cc4cfd75083e5bee7a1323f7e82f41cd8cc9b9486b5cd7d11415e
- evidence_id: bgc-2441-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json
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
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Eight comparisons agree, two canonical-string comparisons are false, and
    the supplied atom correspondence is empty. Normalized equality does not establish
    fixed-form graph or natural identity. The explicit full_graph_identity_established
    flag remains false.
  snapshot_sha256: 6850baa8fbfc54cf5ad8aa70b91f3565712bfc851de94725684972e0480db98c
- evidence_id: bgc-2441-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-DATA-001.json
  locator: /records/0/declared_structure; /records/0/literal_InChI_layers; /records/0/comparisons;
    /records/0/atom_correspondence; /records/0/smiles/computed/atoms; /records/0/smiles/computed/bonds;
    /records/0/smiles/computed/rings; /records/0/smiles/computed/potential_stereo;
    /records/0/smiles/computed/motifs; /records/0/smiles/computed/fragment_atom_indices;
    /records/0/inchi/computed/atoms; /records/0/inchi/computed/bonds; /records/0/inchi/computed/rings;
    /records/0/inchi/computed/potential_stereo; /records/0/inchi/computed/motifs;
    /records/0/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Both saved forms contain 36 heavy atoms, 40 bonds and five reported rings.
    The SMILES form has four carbonyl sites and two amides; the InChI reconstruction
    has two carbonyl sites and two C-single-O/double-N sites, with exact differing
    hydrogen/bond neighborhoods retained. Neither form reports a saturated six-membered
    C5O cycle or phosphorus. The original chirality-aware correspondence is empty
    and full_graph_identity_established is false.
  snapshot_sha256: 6850baa8fbfc54cf5ad8aa70b91f3565712bfc851de94725684972e0480db98c
- evidence_id: bgc-2441-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-first-five-diagnostic-reading-001.json
  locator: /records/0; /read_scope; /totals; /representation; /reading_caveats
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: BGC personally read every field of all ten first-five forms, 370 atom rows
    and 420 bond rows, and all 201 intake placements/51 paths. Exact lossless reconstruction
    and original reading objects are retained; no reparse.
  snapshot_sha256: 421e98636ba662d3b80856bd203a17f6d4821b1d26478e98cfb2f4c5983c3263
- evidence_id: bgc-2441-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/0; /molecular_parse_attempts; /parsed;
    /global_warning_count; /method_scope; /interpretation_boundary
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: ROOT accepted the original twenty stored-form diagnostic; this owner’s
    actual comparison/correspondence scope is located. Global warning count is zero;
    no alternative normalization repair is inferred.
  snapshot_sha256: 53cfc82e0782adcaf6fa89a1f348882ed503e70b4f238ecea56ce4b6e454792e
- evidence_id: bgc-2441-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/chemistry-local/diagnostic-execution-001.json
  locator: /command; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact original diagnostic command, times, zero exit and stream pins; stderr
    is empty as its zero-byte pin records.
  snapshot_sha256: a8e429b538e8b4bb210b03462f44fed28d75a036c4254b0b9a23fa933362e886
- evidence_id: bgc-2441-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines 392–430
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Undefined stereo is retained rather than fabricated; computed classifications
    are named/versioned model results, never source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2441-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines 165–173
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: stereo_complete is computed with FindMolChiralCenters including unassigned
    centers; it does not independently verify natural identity or all double-bond
    geometry.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2441-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines 295–306; 988–1022
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Multiple classifier pathways yield UNCLASSIFIED filing while arrays are
    retained. Filing and model fidelity do not establish biological applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2441-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-current245-assigned-source-reading-001.json
  locator: /scope; /reading; /records; /cautions; /physical_verification
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: BGC personally read ten assigned contexts, 90 frames, 28 positive rows
    and 373 fields; selected five account for 45 frames/13 rows/183 fields. Prior
    companion whole-body readings remain explicitly attributed.
  snapshot_sha256: bbd532f2feb60267a5f06722b7f019a9dc82f0140df14c12347a59fa8032c159
- evidence_id: bgc-2441-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /source_receipts;
    /reading_boundaries
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: 'Disjoint complete source reading totals 225 frames/120 rows/1294 fields:
    BGC 28 rows, ROOT 60, Support 32; Native taxonomy/curation credit is separate.
    Preferred corrected ROOT CPA002 is retained without transferring its precursor
    claims.'
  snapshot_sha256: f1ff457f0b365650b471d3899f218f22149798ceb6c718ce3b4ca4381f3999b4
- evidence_id: bgc-2441-source-plan-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/bgc-source-plan-execution-001.json
  locator: /status; /source; /original_tools; /original_terminal; /exit_code; /plan;
    /derivation; /inventory; /notes; /verification
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: The one original local composer produced the exact 400-placement/66-path
    plan with 31 verified derivation operations. Actual intake acceptance separately
    binds this plan; historical conditional fields remain unchanged.
  snapshot_sha256: cb6bb69a0d55063a04f1c655cf745f18397fc6504458f8c4e463145c33f93c80
- evidence_id: bgc-2441-native-gate-limits
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245/root-native-five-gates-acceptance-001.json
  locator: /status; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Five local commands passed; full QC and complete OAK remain unavailable.
    Passing local syntax/reproduction checks does not complete scientific verification.
  snapshot_sha256: 96136a2f222716e1d3f662e48e6dc859f6672faad8d32454d56b161c97b1dcff
- evidence_id: bgc-2441-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-implemented-curation-scan-001.json
  locator: /scope; /counts; /table_inventory; /applied_rows; /assay_scope; /interpretation
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Native’s bounded ignored-inclusive scan found one applicable BGC0977 override
    for selected order2447, outside these first five; none applies to this owner.
    No assay exclusion is borrowed by shared names or locus alone.
  snapshot_sha256: 5dc21625a5090a65de13d121ec91c99ee12146f14405c52e5e642caefc880eca
  search_scope: Current 25-context scope, 242 literal tokens and all 11 enumerated
    TSVs including ignored files; nine eligible tables/3422 rows examined, with exact
    applied/unrelated identities retained. This does not claim a global external absence
    or validate assay protocols.
- evidence_id: bgc-2441-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/1; /cached_taxonomy/whole_stanzas/2
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete retained cache stanzas for this owner’s source taxon IDs. Names/synonyms
    are cached context, not a fresh taxonomic or strain determination.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
- evidence_id: bgc-2441-taxonomy-routes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/source_taxa; /contexts/6/source_scope_inventory/forward_taxon_merge_matches;
    /contexts/6/source_scope_inventory/nonorganism_matches
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: All saved taxon IDs and forwarding/nonorganism routes for this selected
    source context, including empty routes; no fresh taxonomy request.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
- evidence_id: bgc-2441-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/native-prep/native-current245-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /complete_readings; /forward_routes; /interpretation
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Native personally read all 32 complete cached stanzas and four saved forwarding
    routes across the full batch context. This attribution does not duplicate positive-row
    credit or transfer species/strain roles.
  snapshot_sha256: f806240f1ff8a94ab163860a370a55b75d773a8f648573732831e9d207b61242
- evidence_id: bgc-2441-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-target-input-plan-001.json
  locator: /records/0/proposed_companion_paths; /records/0/direct_companion_predicates
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Literal one-hop shared-BGC predicates and exact direct companion paths
    only; no transitive expansion or transfer of identity, stereochemistry, activity
    or mechanism.
  snapshot_sha256: d8a44564b39627c62877f3b0921e0b13011b120098db5d35d33f5a2bc3d6a1df
- evidence_id: bgc-2441-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/1/path; /contexts/1/identifier; /contexts/1/label; /contexts/1/standard_inchi_key;
    /contexts/1/owned_bgc_ids; /contexts/2/path; /contexts/2/identifier; /contexts/2/label;
    /contexts/2/standard_inchi_key; /contexts/2/owned_bgc_ids; /contexts/3/path; /contexts/3/identifier;
    /contexts/3/label; /contexts/3/standard_inchi_key; /contexts/3/owned_bgc_ids;
    /contexts/4/path; /contexts/4/identifier; /contexts/4/label; /contexts/4/standard_inchi_key;
    /contexts/4/owned_bgc_ids; /contexts/5/path; /contexts/5/identifier; /contexts/5/label;
    /contexts/5/standard_inchi_key; /contexts/5/owned_bgc_ids
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Distinct full keys, identities, labels and owned loci define the selected
    owner’s direct context; shared BGC membership is not identity equivalence.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
- evidence_id: bgc-2441-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved mibig_compounds frame contains 1 placements; its exact predicate,
    query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory mibig_compounds: literal predicate exact complete
    standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2441-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2902–2902; row_sha256 ce34c93f6331ac9ab077ad29e4f673bec891ca686f854dde002c73d7ee6f3437
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact full-key/version/compound-index, producer/locus grades and citation-tier
    fields. BGC complete selected source-row reading and current physical bytes are
    joined.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2441-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved chebi_structures frame contains 0 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory chebi_structures: literal predicate exact complete
    standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2441-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved lotus_occurrences frame contains 1 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory lotus_occurrences: literal predicate exact
    complete standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete
    matching payloads or empty result frame retained. No external lookup or query
    replay.'
- evidence_id: bgc-2441-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 1007–1007; row_sha256 cdb6607c3d70c48cdd2f080f825f0fe768a802472eafd202ded121c1f9c04b7b
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete retained organism/reference occurrence assertion, with species/genus
    scope separate from source strain; repeated citations do not prove independent
    studies. BGC complete selected source-row reading and current physical bytes are
    joined.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2441-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame contains 0 placements; its
    exact predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory cyanometdb_occurrences: literal predicate exact
    complete standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete
    matching payloads or empty result frame retained. No external lookup or query
    replay.'
- evidence_id: bgc-2441-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved npclassifier frame contains 1 placements; its exact predicate,
    query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory npclassifier: literal predicate exact complete
    standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2441-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 377–377; row_sha256 38b1f71c6b3014d5a0bd9501da1de4b416f80178d487a943065808f3519e9204
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; scientific applicability
    is not guaranteed by retention. BGC complete selected source-row reading and current
    physical bytes are joined.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2441-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame contains 0 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory pubchem_bioassay: literal predicate exact complete
    standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete matching
    payloads or empty result frame retained. No external lookup or query replay.'
- evidence_id: bgc-2441-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved bindingdb_targets frame contains 0 placements; its exact
    predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory bindingdb_targets: literal predicate exact
    complete standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N". Complete
    matching payloads or empty result frame retained. No external lookup or query
    replay.'
- evidence_id: bgc-2441-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame contains 0 placements; its
    exact predicate, query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory antibioticmech_inchikeys: literal predicate
    exact complete standard_inchi_key equality; query "DAZWHCJBSRQVSC-LQXARYHSSA-N".
    Complete matching payloads or empty result frame retained. No external lookup
    or query replay.'
- evidence_id: bgc-2441-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch245-tentative/bgc-prep/bgc-conditional245-source-inventory-DATA-001.json
  locator: /contexts/6/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T20:22:56.421652Z'
  support: supports
  summary: Complete saved chebi_origins frame contains 0 placements; its exact predicate,
    query and all fields define the bounded result.
  snapshot_sha256: 379e491d34bf872bb3154ba1e6aface0afd0382090f3bf9fca93abec0ad16b33
  search_scope: 'Saved local inventory chebi_origins: literal predicate exact chebi_id
    from exact full-key structure rows; query []. Complete matching payloads or empty
    result frame retained. No external lookup or query replay.'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:04:58.745110Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 7eb06a6ca3ba46a89e3143ba4577e69ee5f15cb4b210d94eacb75cb403730549
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:05:23.400080Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 9fd4e3ad709d6047c757bb93f69289bf8689e934def523093fad81695b2f8718
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:05:42.956098Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:06:17.242880Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-245/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-245/native-current245-five-gates-execution-001.json
  accessed_at: '2026-11-04T20:06:28.919996Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b64dd93ae78a663114393f190e69f05eacc19b62d12eeb842aa8b0aae78f76c5
assessments:
- assessment_id: bgc-2441-identity
  area: identity
  topic: Exact retained identity and bounded correspondence
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-9606620456 and full key
    DAZWHCJBSRQVSC-LQXARYHSSA-N belong to the retained MIBiG BGC0002365 compound 4,
    not to the five related BGC congeners. Both saved forms reproduce this full key
    and C29H38N2O5 with zero formal charge. Their canonical strings differ and the
    supplied atom map is empty, so normalized agreement does not prove full graph
    or natural-state identity. NPA026680 is a retained cross-reference; the bounded
    exact-key ChEBI join is empty, not a fresh database-wide absence claim.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-grounding-owner
  - bgc-2441-chemistry
  - bgc-2441-source-mibig_compounds
  - bgc-2441-query-chebi_structures
  - bgc-2441-direct-contexts
  - bgc-2441-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: DAZWHCJBSRQVSC-LQXARYHSSA-N; exact retained key, not natural identity proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2441-grounding-owner
    - bgc-2441-chemistry
    - bgc-2441-source-mibig_compounds
    - bgc-2441-query-chebi_structures
    - bgc-2441-direct-contexts
    - bgc-2441-companion-boundaries
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-9606620456 and full key
      DAZWHCJBSRQVSC-LQXARYHSSA-N belong to the retained MIBiG BGC0002365 compound
      4, not to the five related BGC congeners. Both saved forms reproduce this full
      key and C29H38N2O5 with zero formal charge. Their canonical strings differ and
      the supplied atom map is empty, so normalized agreement does not prove full
      graph or natural-state identity. NPA026680 is a retained cross-reference; the
      bounded exact-key ChEBI join is empty, not a fresh database-wide absence claim.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2441-grounding-owner
    - bgc-2441-chemistry
    - bgc-2441-source-mibig_compounds
    - bgc-2441-query-chebi_structures
    - bgc-2441-direct-contexts
    - bgc-2441-companion-boundaries
- assessment_id: bgc-2441-representation
  area: representation
  topic: Stored-form stereochemistry and topology limits
  outcome: supported
  summary: The stored false stereo flag is consistent with eight specified and one
    unspecified tetrahedral center in each saved form. The SMILES table also has two
    specified alkene geometries and one unspecified double bond. The reconstructed
    InChI form retains an unknown double bond and adds an unspecified C=N potential
    center. SMILES amides C17/N19 and C25/N24 instead appear as C-single-O/double-N
    sites C28/N30/O35 and C23/N29/O33 in the reconstructed form; their N-H/O-H and
    bond-order differences are representation-specific. Neither encoding is selected
    as the natural tautomer or rewritten.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-grounding-owner
  - bgc-2441-chemistry
  - bgc-2441-topology
  - bgc-2441-diagnostic-reading
  - bgc-2441-diagnostic-acceptance
  - bgc-2441-structure-schema
  - bgc-2441-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: The stored false stereo flag is consistent with eight specified and one
      unspecified tetrahedral center in each saved form. The SMILES table also has
      two specified alkene geometries and one unspecified double bond. The reconstructed
      InChI form retains an unknown double bond and adds an unspecified C=N potential
      center. SMILES amides C17/N19 and C25/N24 instead appear as C-single-O/double-N
      sites C28/N30/O35 and C23/N29/O33 in the reconstructed form; their N-H/O-H and
      bond-order differences are representation-specific. Neither encoding is selected
      as the natural tautomer or rewritten.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2441-grounding-owner
    - bgc-2441-chemistry
    - bgc-2441-topology
    - bgc-2441-diagnostic-reading
    - bgc-2441-diagnostic-acceptance
    - bgc-2441-structure-schema
    - bgc-2441-stereo-method
  - name: representation_correspondence
    value: Eight comparisons agree, two canonical-string comparisons are false, and
      the supplied atom correspondence is empty. Normalized equality does not establish
      fixed-form graph or natural identity. full_graph_identity_established remains
      false.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2441-grounding-owner
    - bgc-2441-chemistry
    - bgc-2441-topology
    - bgc-2441-diagnostic-reading
    - bgc-2441-diagnostic-acceptance
    - bgc-2441-structure-schema
    - bgc-2441-stereo-method
- assessment_id: bgc-2441-provenance
  area: provenance
  topic: Separate producer, locus and taxon assertions
  outcome: supported
  summary: MIBiG BGC0002365 version 2 associates the compound with Streptomyces sp.
    NCBITaxon:1931 at SOURCE_ASSERTION. Its MN234160.1 locus spans 1–17258, remains
    CLUSTER_UNSTATED and supplies no experimental locus-method list. The LOTUS genus-level
    Streptomyces NCBITaxon:1883 occurrence has a different evidential role and does
    not supply a strain or upgrade production. Shared locus membership with five related
    owners does not transfer their stereochemistry or activity.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-origin-owner
  - bgc-2441-occurrence-owner
  - bgc-2441-source-mibig_compounds
  - bgc-2441-cached-taxonomy
  - bgc-2441-curation-scope
  - bgc-2441-direct-contexts
  - bgc-2441-companion-boundaries
  - bgc-2441-source-lotus_occurrences
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0002365 version 2 associates the compound with Streptomyces sp.
      NCBITaxon:1931 at SOURCE_ASSERTION. Its MN234160.1 locus spans 1–17258, remains
      CLUSTER_UNSTATED and supplies no experimental locus-method list. The LOTUS genus-level
      Streptomyces NCBITaxon:1883 occurrence has a different evidential role and does
      not supply a strain or upgrade production. Shared locus membership with five
      related owners does not transfer their stereochemistry or activity.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2441-origin-owner
    - bgc-2441-occurrence-owner
    - bgc-2441-source-mibig_compounds
    - bgc-2441-cached-taxonomy
    - bgc-2441-curation-scope
    - bgc-2441-direct-contexts
    - bgc-2441-companion-boundaries
    - bgc-2441-source-lotus_occurrences
  - name: producer_evidence
    value: MIBiG BGC0002365 version 2 associates the compound with Streptomyces sp.
      NCBITaxon:1931 at SOURCE_ASSERTION. Its MN234160.1 locus spans 1–17258, remains
      CLUSTER_UNSTATED and supplies no experimental locus-method list. The LOTUS genus-level
      Streptomyces NCBITaxon:1883 occurrence has a different evidential role and does
      not supply a strain or upgrade production. Shared locus membership with five
      related owners does not transfer their stereochemistry or activity.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2441-origin-owner
    - bgc-2441-occurrence-owner
    - bgc-2441-source-mibig_compounds
    - bgc-2441-cached-taxonomy
    - bgc-2441-curation-scope
    - bgc-2441-direct-contexts
    - bgc-2441-companion-boundaries
    - bgc-2441-source-lotus_occurrences
  - name: locus_evidence
    value: MIBiG BGC0002365 version 2 associates the compound with Streptomyces sp.
      NCBITaxon:1931 at SOURCE_ASSERTION. Its MN234160.1 locus spans 1–17258, remains
      CLUSTER_UNSTATED and supplies no experimental locus-method list. The LOTUS genus-level
      Streptomyces NCBITaxon:1883 occurrence has a different evidential role and does
      not supply a strain or upgrade production. Shared locus membership with five
      related owners does not transfer their stereochemistry or activity.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2441-origin-owner
    - bgc-2441-occurrence-owner
    - bgc-2441-source-mibig_compounds
    - bgc-2441-cached-taxonomy
    - bgc-2441-curation-scope
    - bgc-2441-direct-contexts
    - bgc-2441-companion-boundaries
    - bgc-2441-source-lotus_occurrences
- assessment_id: bgc-2441-citations
  area: evidence
  topic: Citation tiers and seed-history scope
  outcome: supported
  summary: The MIBiG PMID:31775228 reference is explicitly ENTRY evidence. The separate
    LOTUS DOI:10.3390/MD17120663 supports the retained occurrence assertion, without
    proving independent experiments or the MIBiG strain. Neither primary publication
    was freshly accessed. The two SEEDED_FROM_SOURCES events document inventory seeding,
    not experimental verification, and the record remains MINTED/SEEDED.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-owner
  - bgc-2441-history-owner
  - bgc-2441-origin-owner
  - bgc-2441-occurrence-owner
  - bgc-2441-source-mibig_compounds
  - bgc-2441-source-reading
  - bgc-2441-source-lotus_occurrences
  dimensions:
  - name: citation_scope
    value: The MIBiG PMID:31775228 reference is explicitly ENTRY evidence. The separate
      LOTUS DOI:10.3390/MD17120663 supports the retained occurrence assertion, without
      proving independent experiments or the MIBiG strain. Neither primary publication
      was freshly accessed. The two SEEDED_FROM_SOURCES events document inventory
      seeding, not experimental verification, and the record remains MINTED/SEEDED.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2441-owner
    - bgc-2441-history-owner
    - bgc-2441-origin-owner
    - bgc-2441-occurrence-owner
    - bgc-2441-source-mibig_compounds
    - bgc-2441-source-reading
    - bgc-2441-source-lotus_occurrences
- assessment_id: bgc-2441-occurrence
  area: evidence
  topic: Finite occurrence and assay scope
  outcome: supported
  summary: One exact-key LOTUS row and the matching retained owner occurrence concern
    Streptomyces at genus scope. The saved ChEBI-origin and CyanoMetDB joins are empty,
    as are PubChem BioAssay and BindingDB; this owner has no activity, molecular-target
    or mechanism roots. These bounded local absences do not show biological inactivity
    or absence from other sources. No congener assay is transferred.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-occurrence-owner
  - bgc-2441-mechanism-absence
  - bgc-2441-query-lotus_occurrences
  - bgc-2441-query-chebi_origins
  - bgc-2441-query-cyanometdb_occurrences
  - bgc-2441-query-pubchem_bioassay
  - bgc-2441-query-bindingdb_targets
  - bgc-2441-query-antibioticmech_inchikeys
  - bgc-2441-cached-taxonomy
  - bgc-2441-taxonomy-routes
  - bgc-2441-taxonomy-reading
  - bgc-2441-curation-scope
  - bgc-2441-source-lotus_occurrences
  dimensions:
  - name: occurrence_scope
    value: One exact-key LOTUS row and the matching retained owner occurrence concern
      Streptomyces at genus scope. The saved ChEBI-origin and CyanoMetDB joins are
      empty, as are PubChem BioAssay and BindingDB; this owner has no activity, molecular-target
      or mechanism roots. These bounded local absences do not show biological inactivity
      or absence from other sources. No congener assay is transferred.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2441-occurrence-owner
    - bgc-2441-mechanism-absence
    - bgc-2441-query-lotus_occurrences
    - bgc-2441-query-chebi_origins
    - bgc-2441-query-cyanometdb_occurrences
    - bgc-2441-query-pubchem_bioassay
    - bgc-2441-query-bindingdb_targets
    - bgc-2441-query-antibioticmech_inchikeys
    - bgc-2441-cached-taxonomy
    - bgc-2441-taxonomy-routes
    - bgc-2441-taxonomy-reading
    - bgc-2441-curation-scope
    - bgc-2441-source-lotus_occurrences
  - name: assay_target_scope
    value: No actual assay row or blank-AID sentinel occurs for this selected identity.
      Empty retained PubChem/BindingDB joins and absent owner activity/target roots
      do not establish inactivity, potency or a molecular mechanism.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2441-occurrence-owner
    - bgc-2441-mechanism-absence
    - bgc-2441-query-lotus_occurrences
    - bgc-2441-query-chebi_origins
    - bgc-2441-query-cyanometdb_occurrences
    - bgc-2441-query-pubchem_bioassay
    - bgc-2441-query-bindingdb_targets
    - bgc-2441-query-antibioticmech_inchikeys
    - bgc-2441-cached-taxonomy
    - bgc-2441-taxonomy-routes
    - bgc-2441-taxonomy-reading
    - bgc-2441-curation-scope
    - bgc-2441-source-lotus_occurrences
- assessment_id: bgc-2441-classification
  area: consistency
  topic: Model fidelity with specific family applicability unverified
  outcome: unknown
  summary: NPClassifier version 2026-09-07 retains both Amino acids and Peptides and
    Polyketides, Macrolides and Macrocyclic tetramic acids, with glycoside false.
    The seeder deliberately files multiple pathway labels as UNCLASSIFIED rather than
    discarding either label. The N-containing macrocycle and carbonyl-bearing five-membered
    ring are compatible with a mixed peptide/polyketide context, but the specific
    named model families remain model assertions, not independently established biosynthetic
    or natural-identity conclusions. Tautomer-dependent amide counts do not by themselves
    demonstrate classifier or source-ingestion error.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-classification-owner
  - bgc-2441-source-npclassifier
  - bgc-2441-chemistry
  - bgc-2441-topology
  - bgc-2441-structure-schema
  - bgc-2441-classification-seeder
  - bgc-2441-source-mibig_compounds
  dimensions:
  - name: classification_applicability
    value: NPClassifier version 2026-09-07 retains both Amino acids and Peptides and
      Polyketides, Macrolides and Macrocyclic tetramic acids, with glycoside false.
      The seeder deliberately files multiple pathway labels as UNCLASSIFIED rather
      than discarding either label. The N-containing macrocycle and carbonyl-bearing
      five-membered ring are compatible with a mixed peptide/polyketide context, but
      the specific named model families remain model assertions, not independently
      established biosynthetic or natural-identity conclusions. Tautomer-dependent
      amide counts do not by themselves demonstrate classifier or source-ingestion
      error.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2441-classification-owner
    - bgc-2441-source-npclassifier
    - bgc-2441-chemistry
    - bgc-2441-topology
    - bgc-2441-structure-schema
    - bgc-2441-classification-seeder
    - bgc-2441-source-mibig_compounds
- assessment_id: bgc-2441-completion
  area: completeness
  topic: Actual evidence coverage and remaining limits
  outcome: unknown
  summary: The complete owner and both seed histories, accepted 42-input canonical
    intake, all nine selected saved source frames, full paired molecular tables and
    direct shared-BGC context have been reviewed. No graph, pathway, component reference
    or molecular target is declared, so a maintained-reader check does not apply.
    Fresh primary evidence, independent natural stereochemistry, full QC and complete
    OAK coverage remain unavailable; this is a partial review without a source/status/history
    edit.
  target_ids:
  - naturalproductmech:mibig-9606620456
  evidence_ids:
  - bgc-2441-owner
  - bgc-2441-capture
  - bgc-2441-intake
  - bgc-2441-intake-acceptance
  - bgc-2441-history-owner
  - bgc-2441-diagnostic-reading
  - bgc-2441-diagnostic-acceptance
  - bgc-2441-diagnostic-execution
  - bgc-2441-source-reading
  - bgc-2441-joint-source-notes
  - bgc-2441-source-plan-execution
  - bgc-2441-native-gate-limits
  - bgc-2441-curation-scope
  - bgc-2441-mechanism-absence
  dimensions:
  - name: review_completion
    value: The complete owner and both seed histories, accepted 42-input canonical
      intake, all nine selected saved source frames, full paired molecular tables
      and direct shared-BGC context have been reviewed. No graph, pathway, component
      reference or molecular target is declared, so a maintained-reader check does
      not apply. Fresh primary evidence, independent natural stereochemistry, full
      QC and complete OAK coverage remain unavailable; this is a partial review without
      a source/status/history edit.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2441-owner
    - bgc-2441-capture
    - bgc-2441-intake
    - bgc-2441-intake-acceptance
    - bgc-2441-history-owner
    - bgc-2441-diagnostic-reading
    - bgc-2441-diagnostic-acceptance
    - bgc-2441-diagnostic-execution
    - bgc-2441-source-reading
    - bgc-2441-joint-source-notes
    - bgc-2441-source-plan-execution
    - bgc-2441-native-gate-limits
    - bgc-2441-curation-scope
    - bgc-2441-mechanism-absence
findings: []
actions: []
limitations:
- Retained local evidence only. Fresh primary literature, current taxonomy, assay
  protocols and independent natural identity/stereochemical authentication remain
  unavailable.
- Five local native commands passed, but full QC and complete OAK remain unavailable.
  Saved normalized forms and atom matches do not establish independent full graph
  or natural-state identity.
- Producer, locus, occurrence, strain and citation tiers remain separate. Shared BGC
  membership and repeated references do not transfer biological claims or establish
  independent experiments.
- Named model-family applicability is explicitly unverified; retention fidelity and
  broad structural compatibility do not establish a specific biosynthetic family or
  a source-ingestion defect.
- The complete selected owner has no graph, pathway, component reference or molecular-target
  root. No maintained-reader result, source edit or status/history promotion is claimed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read ten first-five saved forms: 370 atom rows and 420 bond rows,
  complete strings/scalars/rings/stereo/motifs/maps; indices are diagnostic-local.
  The original diagnostic stderr was empty. No reparse occurred during review.'
- 'Disjoint source reading: BGC 10 contexts/90 frames/28 rows/373 fields; ROOT 7 contexts/63
  frames/60 rows/558 fields; Support 8 contexts/72 frames/32 rows/363 fields. Native
  read 32 cached stanzas and bounded curation, with zero positive-row credit. Prior
  raw/history readings and preferred ROOT CPA002 remain attributed.'
- BGC operated the original local collector and composer; Support operated canonical
  intakes; Native operated the original molecular diagnostic under ROOT delegation.
  Final report authoring only reads saved evidence and writes review artifacts.
- All first-five reviews remain partial. No supported source-edit finding or action
  is asserted.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-245
```
