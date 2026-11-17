# Local evidence review: tiancilactone B

- Review: 20261104T160009Z-tiancilactone-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T15:07:30.128036Z
- Finished UTC: 2026-11-04T16:00:09.612086Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Tiancilactone B retains consistent original stored forms and distinct strain/locus versus genus-occurrence assertions. One tetrahedral center remains unspecified. The faithful glycoside prediction has unresolved applicability to the observed lactone topology; no source correction or assay mechanism is established.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2413; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5a982ded92 | data/natural_products/terpenoids/tiancilactone-b.yaml | generated | tiancilactone B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-5a982ded92 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5a982ded92 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5a982ded92 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5a982ded92 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5a982ded92 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5a982ded92 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5a982ded92 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5a982ded92 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identifier and normalized-form consistency; natural identity unverified

identity: supported. Targets: naturalproductmech:mibig-5a982ded92.

The minted identifier naturalproductmech:mibig-5a982ded92 retains the full key CWPRIGWHYUKIHW-NHLPTZDRSA-N from its MIBiG structure. The saved exact-key ChEBI join is empty; the grounding note is a historical explanation of minting, not a current universal ChEBI absence claim. PubChem 156582165 is a cross-reference. The seven other Tiancilactones are same-locus context with distinct full keys; a shared locus, formula or citation does not establish interchangeable identities. Both original forms normalize to C32H45NO8, charge 0 and the declared complete key. This supports the retained identifier/normalized-form join while leaving natural identity unverified.

### Original stored-form and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-5a982ded92.

Both original forms are neutral C32H45NO8 with 41 heavy atoms and 45 bonds. All ten comparison flags are true, and the supplied chirality-aware atom match covers the full atom count; full_graph_identity_established remains false. Each form has nine specified tetrahedral centers and one unspecified center at SMILES atom 20/reconstructed atom 27, consistent with the retained false flag. No configuration is filled from a congener. Atom indices are local diagnostic indices, not natural-product locants.

### Separate producer, locus and taxonomic claims

provenance: supported. Targets: naturalproductmech:mibig-5a982ded92.

BGC0002019 v3 compound 2 retains Streptomyces sp. CB03234 NCBITaxon:1703937 as SOURCE_ASSERTION. BK010469.1 remains CLUSTER_UNSTATED, with no coordinates or locus evidence methods supplied. The genus-level occurrence under NCBITaxon:1883 cannot independently identify that strain or upgrade production or locus evidence.

### Retained citation roles and attribution

evidence: supported. Targets: naturalproductmech:mibig-5a982ded92.

DOI:10.1002/cbic.201800285 is selected from MIBiG COMPOUND_BIOACTIVITY provenance and repeated on producer and locus. The upper-case LOTUS DOI:10.1002/CBIC.201800285 is an occurrence citation to the same DOI after case normalization, not independent experimental support. A bioactivity-tier citation supplies no actual assay endpoint, value or target here; no primary text was newly read.

### Bounded occurrence and no-assay evidence

evidence: supported. Targets: naturalproductmech:mibig-5a982ded92.

The owner retains one LOTUS occurrence at the Streptomyces genus, NCBITaxon:1883. It is distinct from the CB03234 strain-level producer assertion. The saved exact-key cyanobacterial and ChEBI-origin joins return no additional occurrence within these retained inventories; this is not absence from all literature.

### Versioned model fidelity and bounded applicability

consistency: concern. Targets: naturalproductmech:mibig-5a982ded92.

NPClassifier npclassifier.gnps2.org@2026-09-07 faithfully supplies Terpenoids, empty superclass/class arrays and is_glycoside:true. The complete encoding instead shows the unsaturated five-membered lactone described above, with an OH-bearing hemiacetal carbon and no assigned sugar residue or glycosidic linkage. This creates a bounded model-applicability concern; absence of a C5O motif alone would not exclude every sugar form, and no proved ingestion defect or record edit follows. The total 32 carbons include substituents and do not by themselves assign a terpenoid subclass.

### Actual evidence coverage and scientific limits

completeness: unknown. Targets: naturalproductmech:mibig-5a982ded92.

Complete owner/history, actual canonical intake, retained source rows and negative frames, and both original molecular forms have been read. All four mechanism roots are absent in this captured owner, so no maintained-mechanism reader applies. The record remains MINTED and SEEDED with 2 retained seed-history events. Its canonical intake identifies the maintained seeder, MIBiG extraction/table, classifier and occurrence/assay inventories as owners of distinct fields. Review authoring does not rewrite the generated record or promote its status. The ignored-inclusive local curation scan reports no applicable correction in its declared scope. Full QC/OAK, fresh primary and taxonomy/assay verification, and independent natural identity or stereochemical authentication remain unavailable. This is a partial review with no supported record-edit finding.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2413-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/tiancilactone-b.yaml; Complete plaintext including all curation_history entries | supports | Complete tiancilactone B owner and 2 seed-history events; retained MINTED/SEEDED status. Prior personal whole plaintext/history reading carries. |
| bgc-2413-capture | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2 | supports | Exact actual whole owner capture, metadata and history; a faithful capture is not independent scientific verification. |
| bgc-2413-intake | /private/tmp/npm-review-work/shared-next-batch242/intakes/2413-inspect-001.json; /status; /repository; /source; /targets | supports | Actual target, complete six-role ownership map and all 44 current input placements, joined to the accepted plan. |
| bgc-2413-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch242/root-intake-acceptance-001.json; /status; /accepted; /summary | supports | ROOT accepted the original ten canonical intakes; this owner’s complete input and ownership details are linked separately. |
| bgc-2413-grounding-owner | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2/owner_document/identifier; /records/2/owner_document/label; /records/2/owner_document/chemical_structure; /records/2/owner_document/xrefs; /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status; /records/2/owner_document/grounding_notes | supports | Exact minted identifier, full stored structure, cross-references and historical grounding explanation. The note is not a new universal database-absence assertion. |
| bgc-2413-origin-owner | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2/owner_document/producer_organisms; /records/2/owner_document/producer_taxon_groups; /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts | supports | Complete retained producer and locus grades, methods, citations and any supplied genome/coordinates. Taxon support and locus support remain distinct. |
| bgc-2413-occurrence-owner | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2/owner_document | supports | The complete owner retains one LOTUS occurrence and lacks bioactivities, bioactivity_summary and molecular_targets. Producer/locus assertions and citation tiers remain separate owner fields. |
| bgc-2413-classification-owner | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2/owner_document/np_classification; /records/2/owner_document/np_pathway; /records/2/owner_document/bgc_class | supports | Exact named/versioned model arrays and glycoside flag, filing pathway and any source class fields; applicability is distinct from faithful retention. |
| bgc-2413-history-owner | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2/owner_document/curation_status; /records/2/owner_document/curation_history | supports | Complete original seed history and SEEDED status; no review-induced source status or history edit. |
| bgc-2413-mechanism-absence | /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json; /records/2/owner_document | supports | Whole captured owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs and molecular_targets. No maintained-mechanism reader applies to this owner. |
| bgc-2413-chemistry | /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence; /records/2/smiles/computed/formula; /records/2/smiles/computed/formal_charge; /records/2/smiles/computed/standard_inchi; /records/2/smiles/computed/standard_inchi_key; /records/2/smiles/computed/canonical_isomeric_smiles; /records/2/smiles/computed/canonical_nonisomeric_smiles; /records/2/smiles/computed/atom_count; /records/2/smiles/computed/heavy_atom_count; /records/2/smiles/computed/bond_count; /records/2/smiles/computed/element_counts; /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/formula; /records/2/inchi/computed/formal_charge; /records/2/inchi/computed/standard_inchi; /records/2/inchi/computed/standard_inchi_key; /records/2/inchi/computed/canonical_isomeric_smiles; /records/2/inchi/computed/canonical_nonisomeric_smiles; /records/2/inchi/computed/atom_count; /records/2/inchi/computed/heavy_atom_count; /records/2/inchi/computed/bond_count; /records/2/inchi/computed/element_counts; /records/2/inchi/computed/stereo_counts | supports | All ten comparison flags are true and the supplied match covers all atoms. full_graph_identity_established remains false; normalization does not authenticate natural identity. |
| bgc-2413-topology | /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/diagnostic-DATA-001.json; /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons; /records/2/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds; /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo; /records/2/smiles/computed/motifs; /records/2/smiles/computed/fragment_atom_indices; /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings; /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs; /records/2/inchi/computed/fragment_atom_indices | supports | The complete tables show three fused six-membered carbocycles, one aromatic ring and a five-membered oxygen-containing lactone (SMILES atoms 15,16,17,19,20). Its C15=C16, C17=O18 and ring O19 identify an unsaturated C4O ring, not a saturated C5O sugar ring. The N-methylamino aromatic group is unchlorinated. Its ester joins CH2 atom 25/O26 to C27=O28; core atom 8 retains OH37. Lactone carbon 20 bears OH21 and is unspecified. No saturated six-membered C5O candidate or carbonyl amide is reported; ether/ester bridges are interpreted in their complete graph context. |
| bgc-2413-diagnostic-reading | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-current242-first-five-diagnostic-reading-001.json; /records/2; /coverage; /lossless_reading_method; /readings; /limits | supports | BGC personally read every field of the ten first-five forms: 404 atom rows and 444 bond rows. Exact constant-column factoring is reversible; no new parsing occurred. |
| bgc-2413-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /warning_count; /warning_record_attribution; /limits; /stderr | supports | ROOT accepted one original twenty-form local diagnostic with empty stderr. This owner’s exact comparisons are cited separately; the receipt does not authenticate natural identity. |
| bgc-2413-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/diagnostic-execution-001.json; /started_at; /finished_at; /exit_code; /source; /stdout; /stderr | supports | Exact original execution and stream pins; review authoring does not reparse the stored forms. |
| bgc-2413-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines392–430 | supports | The schema distinguishes undefined stereocenters from fabricated assignments and defines computed classification as named/versioned model output, never a source assertion. |
| bgc-2413-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines165–173 | supports | The exact extractor flag checks FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False) for unassigned centers; it does not test double-bond completeness or natural stereochemical truth. |
| bgc-2413-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines295–306;988–1022 | supports | The maintained seeder retains source structure/stereo and exact classifier arrays, with filing from the pathway array. Fidelity does not decide model applicability. |
| bgc-2413-source-reading | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-current242-source-reading-001.json; /scope; /reading; /division; /verification; /cautions | supports | BGC personally read ten assigned contexts: 90 complete frames, 54 positive rows and 556 fields. The scope comprises the five selected owners and five unselected BGC1140 companions of Thioplatensimycin. Prior complete raw/history carries remain attributed. |
| bgc-2413-joint-source-notes | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-scope-notes-001.json; /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations | supports | Actual 15-context scope combines BGC 54 rows with Support 26 rows and Native 8 complete cache stanzas/curation scan. |
| bgc-2413-source-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch242/root-source-plan-acceptance-001.json; /status | supports | ROOT accepted the original source-plan result and exact current input maps; source-stage conditional wording is not a substitute for earned runtime receipts. |
| bgc-2413-curation-scope | /private/tmp/npm-review-work/shared-next-batch242-tentative/native-prep/native-current242-implemented-curation-scan-001.json; /scope; /ignored_files_included; /table_pins; /scanned_tables; /lexical_positive_rows; /applicable_rows; /conclusion; /assay_exclusion_scope; /reserved_files; /limitations | supports | Ignored-inclusive bounded scan of nine tables from eleven enumerated TSVs has 16 broad Streptomyces lexical hits, all unrelated, and zero applicable correction/exclusion. All ten PubChem sentinel rows have blank AIDs; no actual assay tuple is validated by this absence. |
| bgc-2413-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/0; /cached_taxonomy/whole_stanzas/7 | supports | Complete retained NCBITaxon:1883 and NCBITaxon:1703937 stanzas give cached Streptomyces genus and Streptomyces sp. CB03234 strain names/synonyms. Their distinct scopes do not establish production or fresh taxonomy. |
| bgc-2413-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch242-tentative/native-prep/native-current242-cached-taxonomy-reading-001.json; /scope; /counts; /readings; /cautions | supports | Native personally read all eight inventory stanzas. The complete saved reading is delegated and attributed; no new lookup or duplicate disjoint-source credit. |
| bgc-2413-direct-contexts | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-target-input-plan-001.json; /records/2/proposed_companion_paths; /records/2/direct_companion_predicates | supports | Exact one-hop owned-BGC context membership; shared locus membership does not transfer full-key identity, stereochemistry, activity or producer claims. |
| bgc-2413-companion-boundaries | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/6/path; /contexts/6/identifier; /contexts/6/label; /contexts/6/standard_inchi_key; /contexts/6/owned_bgc_ids; /contexts/8/path; /contexts/8/identifier; /contexts/8/label; /contexts/8/standard_inchi_key; /contexts/8/owned_bgc_ids; /contexts/9/path; /contexts/9/identifier; /contexts/9/label; /contexts/9/standard_inchi_key; /contexts/9/owned_bgc_ids; /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key; /contexts/10/owned_bgc_ids; /contexts/11/path; /contexts/11/identifier; /contexts/11/label; /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/12/path; /contexts/12/identifier; /contexts/12/label; /contexts/12/standard_inchi_key; /contexts/12/owned_bgc_ids; /contexts/13/path; /contexts/13/identifier; /contexts/13/label; /contexts/13/standard_inchi_key; /contexts/13/owned_bgc_ids | supports | Each direct companion retains its own label, full key, identifier and explicit owned BGC. These compact identity boundaries support context comparison only, not claim transfer. |
| bgc-2413-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame has 1 matching placement with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-source-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Header line 1; physical lines 2304–2304; row_sha256 cffc5b9525b4cd1dfe8d4ef36abb5b917ee47cc1da6d33c6a44ab6981491a0de | supports | Exact full-key compound/version/index, producer/locus grades, genome/coordinate/method fields and citation tier. BGC complete selected source-row reading carries. |
| bgc-2413-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame has 0 matching placements with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame has 1 matching placement with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-source-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Header line 1; physical lines 925–925; row_sha256 b8fe9910ecbda90ffb38d5888a5081ee908544f48d2580b882bac99d972fce63 | supports | Complete organism/reference occurrence assertion, distinct from production and independent experiments. BGC complete selected source-row reading carries. |
| bgc-2413-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame has 0 matching placements with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame has 1 matching placement with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-source-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Header line 1; physical lines 353–353; row_sha256 dbc2a55feed3099a808c029b9c3d84a107efeaf16ef1f902a8caa5a5fbcf7fd9 | supports | Exact named/versioned model arrays and glycoside flag; retention does not establish applicability. BGC complete selected source-row reading carries. |
| bgc-2413-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame has 1 matching placement with all fields and exact predicate/query. Its blank-AID row is a no-assay sentinel. |
| bgc-2413-source-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; Header line 1; physical lines 918–918; row_sha256 9f01b14fc498c56bd9045c36d904efda10f1d0b1bff7cb169b5d05d63edc0029 | supports | Exact owner full-key/CID sentinel with blank AID, assay_name '(no assay data)', and blank outcome/measurement/target/reference fields. No actual assay observation. BGC complete selected source-row reading carries. |
| bgc-2413-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame has 0 matching placements with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame has 0 matching placements with all fields and exact predicate/query. Database scope is limited to this retained join. |
| bgc-2413-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json; /contexts/7/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame has 0 matching placements with all fields and exact predicate/query. Database scope is limited to this retained join. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-242/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-242/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-242/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-242/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-242/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; fresh primary literature, taxonomy, assay protocols and independent natural identity or stereochemistry remain unverified.
- Full QC and complete OAK coverage remain unavailable. Local normalization, motif descriptions and supplied atom matches are not independent full-graph or natural-state proof.
- Producer, locus, occurrence, strain and citation tiers remain distinct; repeated references and congeners do not transfer claims or experimental independence.
- Versioned model fidelity is assessable; the stated applicability concerns do not prove an ingestion defect or justify a source replacement.
- The complete owner has no graph/pathway/component/target roots. No maintained-mechanism result or source status/history edit is claimed.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- BGC personally read all ten first-five forms: 404 atom rows and 444 bond rows, all strings/scalars/rings/stereo/motifs/maps. Diagnostic indices are zero-based and are not biochemical locants; original stderr is empty.
- Disjoint source meanings: BGC ten contexts/54 rows/556 fields/90 frames; Support five contexts/26 rows/278 fields/45 frames. Native read all 8 cache stanzas and the ignored-inclusive curation scan; BGC additionally read three unique first-five stanzas. Prior companion raw/history carries remain attributed.
- BGC operated the admitted local source collector/composer. Support operated the ten canonical intakes; ROOT operated the original molecular diagnostic. Native authored/audited the diagnostic and supplied cache/curation reading. Review authoring invokes no target.
- All outcomes remain partial with no supported edit finding or action; missing fresh verification or model concern alone is not a defect.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T160009Z-tiancilactone-b
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: tiancilactone B'
started_at: '2026-11-04T15:07:30.128036Z'
finished_at: '2026-11-04T16:00:09.612086Z'
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
summary: Tiancilactone B retains consistent original stored forms and distinct strain/locus
  versus genus-occurrence assertions. One tetrahedral center remains unspecified.
  The faithful glycoside prediction has unresolved applicability to the observed lactone
  topology; no source correction or assay mechanism is established.
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
  - path: data/natural_products/terpenoids/tiancilactone-a.yaml
    sha256: 567bc7c127591ff7590d88b2b69e8cf0e4db7fb58bb720b6bb4bc69ebc3186f9
    role: context
  - path: data/natural_products/terpenoids/tiancilactone-b.yaml
    sha256: e1f6d777dd11e4dc8b4c7ed925f2b0eed310efbe767511e54ffb00301b6fddaf
    role: target
  - path: data/natural_products/terpenoids/tiancilactone-c.yaml
    sha256: 8cd026270eb3bd74affc4521f8e3687c2957fec6f71414b71b17585398122f0b
    role: context
  - path: data/natural_products/terpenoids/tiancilactone-d.yaml
    sha256: 25c061f69f218d804fe06c2bd1970b6eb5812c3e55cdbc5c7b7ad54fc6668e35
    role: context
  - path: data/natural_products/terpenoids/tiancilactone-e.yaml
    sha256: d9a4d7379e082f94b173919d01e71d8afc46bbadf55372e062f7f0049ec5baf2
    role: context
  - path: data/natural_products/terpenoids/tiancilactone-f.yaml
    sha256: 0b1c4039e001300d8bd4681174bea86e1c2647a3ff6a1895cef1971c356488cb
    role: context
  - path: data/natural_products/terpenoids/tiancilactone-g.yaml
    sha256: b02d396c67bf4dc4a4601b4e560751a34aabe56c58b42edec10e6ae141ad823c
    role: context
  - path: data/natural_products/terpenoids/tiancilactone-h.yaml
    sha256: cfab25fb803078ea45c813027fb1c8f5509f19a91a40d4ffc664435e92639b43
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
  selection: Campaign path order 2413; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5a982ded92
targets:
- target_id: naturalproductmech:mibig-5a982ded92
  path: data/natural_products/terpenoids/tiancilactone-b.yaml
  label: tiancilactone B
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
  - naturalproductmech:mibig-5a982ded92
  command: just validate-strict data/natural_products/terpenoids/thioplatensimycin.yaml
    data/natural_products/terpenoids/tiancilactone-a.yaml data/natural_products/terpenoids/tiancilactone-b.yaml
    data/natural_products/terpenoids/tiancilactone-c.yaml data/natural_products/terpenoids/tiancilactone-d.yaml
    data/natural_products/terpenoids/tiancilactone-e.yaml data/natural_products/terpenoids/tiancilactone-f.yaml
    data/natural_products/terpenoids/tiancilactone-g.yaml data/natural_products/terpenoids/tiancilactone-h.yaml
    data/natural_products/terpenoids/tirucalla-7-24-dien-3-ol.yaml --workers 1 --out
    /private/tmp/npm-native-checks/batch-242/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-5a982ded92
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-242/validate-all-001.tsv
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
  - naturalproductmech:mibig-5a982ded92
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
  - naturalproductmech:mibig-5a982ded92
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
  - naturalproductmech:mibig-5a982ded92
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-242/review-queue-001.tsv
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
  - naturalproductmech:mibig-5a982ded92
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2413-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/terpenoids/tiancilactone-b.yaml
  locator: Complete plaintext including all curation_history entries
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete tiancilactone B owner and 2 seed-history events; retained MINTED/SEEDED
    status. Prior personal whole plaintext/history reading carries.
  snapshot_sha256: e1f6d777dd11e4dc8b4c7ed925f2b0eed310efbe767511e54ffb00301b6fddaf
- evidence_id: bgc-2413-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact actual whole owner capture, metadata and history; a faithful capture
    is not independent scientific verification.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-intake
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/intakes/2413-inspect-001.json
  locator: /status; /repository; /source; /targets
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Actual target, complete six-role ownership map and all 44 current input
    placements, joined to the accepted plan.
  snapshot_sha256: 0d0f1538f639f38c9403e6fcdf961d6fdae99c2a77412d5b4f1eaf77ec0d9a37
- evidence_id: bgc-2413-intake-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/root-intake-acceptance-001.json
  locator: /status; /accepted; /summary
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: ROOT accepted the original ten canonical intakes; this owner’s complete
    input and ownership details are linked separately.
  snapshot_sha256: 81ea91a4e55c5d283f44c697954180b8db583f1164c4aa1c94c68b3fce5b9aee
- evidence_id: bgc-2413-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2/owner_document/identifier; /records/2/owner_document/label;
    /records/2/owner_document/chemical_structure; /records/2/owner_document/xrefs;
    /records/2/owner_document/source_concepts; /records/2/owner_document/grounding_status;
    /records/2/owner_document/grounding_notes
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact minted identifier, full stored structure, cross-references and historical
    grounding explanation. The note is not a new universal database-absence assertion.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2/owner_document/producer_organisms; /records/2/owner_document/producer_taxon_groups;
    /records/2/owner_document/biosynthetic_gene_clusters; /records/2/owner_document/source_concepts
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete retained producer and locus grades, methods, citations and any
    supplied genome/coordinates. Taxon support and locus support remain distinct.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-occurrence-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: The complete owner retains one LOTUS occurrence and lacks bioactivities,
    bioactivity_summary and molecular_targets. Producer/locus assertions and citation
    tiers remain separate owner fields.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2/owner_document/np_classification; /records/2/owner_document/np_pathway;
    /records/2/owner_document/bgc_class
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag, filing pathway and
    any source class fields; applicability is distinct from faithful retention.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-history-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2/owner_document/curation_status; /records/2/owner_document/curation_history
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete original seed history and SEEDED status; no review-induced source
    status or history edit.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-mechanism-absence
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/owner-capture-DATA-001.json
  locator: /records/2/owner_document
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Whole captured owner lacks causal_graphs, biosynthetic_pathway, causal_graph_refs
    and molecular_targets. No maintained-mechanism reader applies to this owner.
  snapshot_sha256: 7d18f761e81e959a9c6621b00efafda055d612738a82aff090c7a532242d43c3
- evidence_id: bgc-2413-chemistry
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons;
    /records/2/atom_correspondence; /records/2/smiles/computed/formula; /records/2/smiles/computed/formal_charge;
    /records/2/smiles/computed/standard_inchi; /records/2/smiles/computed/standard_inchi_key;
    /records/2/smiles/computed/canonical_isomeric_smiles; /records/2/smiles/computed/canonical_nonisomeric_smiles;
    /records/2/smiles/computed/atom_count; /records/2/smiles/computed/heavy_atom_count;
    /records/2/smiles/computed/bond_count; /records/2/smiles/computed/element_counts;
    /records/2/smiles/computed/stereo_counts; /records/2/inchi/computed/formula; /records/2/inchi/computed/formal_charge;
    /records/2/inchi/computed/standard_inchi; /records/2/inchi/computed/standard_inchi_key;
    /records/2/inchi/computed/canonical_isomeric_smiles; /records/2/inchi/computed/canonical_nonisomeric_smiles;
    /records/2/inchi/computed/atom_count; /records/2/inchi/computed/heavy_atom_count;
    /records/2/inchi/computed/bond_count; /records/2/inchi/computed/element_counts;
    /records/2/inchi/computed/stereo_counts
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: All ten comparison flags are true and the supplied match covers all atoms.
    full_graph_identity_established remains false; normalization does not authenticate
    natural identity.
  snapshot_sha256: 1b4a4a0d8ab1da100e77f176c1a99556871c4a3a7e7e1f91e81b0a7b40265962
- evidence_id: bgc-2413-topology
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/diagnostic-DATA-001.json
  locator: /records/2/declared_structure; /records/2/literal_InChI_layers; /records/2/comparisons;
    /records/2/atom_correspondence; /records/2/smiles/computed/atoms; /records/2/smiles/computed/bonds;
    /records/2/smiles/computed/rings; /records/2/smiles/computed/potential_stereo;
    /records/2/smiles/computed/motifs; /records/2/smiles/computed/fragment_atom_indices;
    /records/2/inchi/computed/atoms; /records/2/inchi/computed/bonds; /records/2/inchi/computed/rings;
    /records/2/inchi/computed/potential_stereo; /records/2/inchi/computed/motifs;
    /records/2/inchi/computed/fragment_atom_indices
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: The complete tables show three fused six-membered carbocycles, one aromatic
    ring and a five-membered oxygen-containing lactone (SMILES atoms 15,16,17,19,20).
    Its C15=C16, C17=O18 and ring O19 identify an unsaturated C4O ring, not a saturated
    C5O sugar ring. The N-methylamino aromatic group is unchlorinated. Its ester joins
    CH2 atom 25/O26 to C27=O28; core atom 8 retains OH37. Lactone carbon 20 bears
    OH21 and is unspecified. No saturated six-membered C5O candidate or carbonyl amide
    is reported; ether/ester bridges are interpreted in their complete graph context.
  snapshot_sha256: 1b4a4a0d8ab1da100e77f176c1a99556871c4a3a7e7e1f91e81b0a7b40265962
- evidence_id: bgc-2413-diagnostic-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-current242-first-five-diagnostic-reading-001.json
  locator: /records/2; /coverage; /lossless_reading_method; /readings; /limits
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: 'BGC personally read every field of the ten first-five forms: 404 atom
    rows and 444 bond rows. Exact constant-column factoring is reversible; no new
    parsing occurred.'
  snapshot_sha256: 3393f1921a5f018b12efeec78026c795aebf38812040456615602d3f4c5045a7
- evidence_id: bgc-2413-diagnostic-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /warning_count; /warning_record_attribution;
    /limits; /stderr
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: ROOT accepted one original twenty-form local diagnostic with empty stderr.
    This owner’s exact comparisons are cited separately; the receipt does not authenticate
    natural identity.
  snapshot_sha256: 3218b288de8f7de9ac715b4a76bf5056a499e3920837c878ec4aff83bae31bc2
- evidence_id: bgc-2413-diagnostic-execution
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/chemistry-local/diagnostic-execution-001.json
  locator: /started_at; /finished_at; /exit_code; /source; /stdout; /stderr
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact original execution and stream pins; review authoring does not reparse
    the stored forms.
  snapshot_sha256: f58a5ea78bf178adcd11f6f385ee98228add898ee87d715518fc81ddb48396a8
- evidence_id: bgc-2413-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines392–430
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: The schema distinguishes undefined stereocenters from fabricated assignments
    and defines computed classification as named/versioned model output, never a source
    assertion.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: bgc-2413-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines165–173
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: The exact extractor flag checks FindMolChiralCenters(includeUnassigned=True,useLegacyImplementation=False)
    for unassigned centers; it does not test double-bond completeness or natural stereochemical
    truth.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2413-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines295–306;988–1022
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: The maintained seeder retains source structure/stereo and exact classifier
    arrays, with filing from the pathway array. Fidelity does not decide model applicability.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2413-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-current242-source-reading-001.json
  locator: /scope; /reading; /division; /verification; /cautions
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: 'BGC personally read ten assigned contexts: 90 complete frames, 54 positive
    rows and 556 fields. The scope comprises the five selected owners and five unselected
    BGC1140 companions of Thioplatensimycin. Prior complete raw/history carries remain
    attributed.'
  snapshot_sha256: d484a11a0ba1fcaf73332484bf4bdb8279f7e310f484fc9927f6bbcb6279e171
- evidence_id: bgc-2413-joint-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-scope-notes-001.json
  locator: /totals; /reading; /reading_reconciliation; /cautions; /curation; /limitations
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Actual 15-context scope combines BGC 54 rows with Support 26 rows and Native
    8 complete cache stanzas/curation scan.
  snapshot_sha256: 9f7355393ff5cc3b85496f73563b45ef77bdb0d69550b3ca3b58f9464e0a922a
- evidence_id: bgc-2413-source-plan-acceptance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242/root-source-plan-acceptance-001.json
  locator: /status
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: ROOT accepted the original source-plan result and exact current input maps;
    source-stage conditional wording is not a substitute for earned runtime receipts.
  snapshot_sha256: 5edb42cd18330fb573f111ddbc271299532a12800669ee68c01719157db70003
- evidence_id: bgc-2413-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/native-prep/native-current242-implemented-curation-scan-001.json
  locator: /scope; /ignored_files_included; /table_pins; /scanned_tables; /lexical_positive_rows;
    /applicable_rows; /conclusion; /assay_exclusion_scope; /reserved_files; /limitations
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Ignored-inclusive bounded scan of nine tables from eleven enumerated TSVs
    has 16 broad Streptomyces lexical hits, all unrelated, and zero applicable correction/exclusion.
    All ten PubChem sentinel rows have blank AIDs; no actual assay tuple is validated
    by this absence.
  snapshot_sha256: fb88e8fe80e9ac6c4cc8a41f21a911bd812f36a2a81968d0935bc7494fc62a5b
  search_scope: All15 current context owner/source identifiers, full keys, owned BGC
    accessions, labels/slugs, taxa/chemical IDs and15 exact BGC:compound IDs;126 case-insensitive
    literal tokens. Complete9-table rows scanned via ignored-inclusive Path.rglob
    enumeration of all11 curation TSVs. All saved source rows used only for token/identity
    scope; no source-query replay.
- evidence_id: bgc-2413-cached-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/0; /cached_taxonomy/whole_stanzas/7
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete retained NCBITaxon:1883 and NCBITaxon:1703937 stanzas give cached
    Streptomyces genus and Streptomyces sp. CB03234 strain names/synonyms. Their distinct
    scopes do not establish production or fresh taxonomy.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
- evidence_id: bgc-2413-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/native-prep/native-current242-cached-taxonomy-reading-001.json
  locator: /scope; /counts; /readings; /cautions
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Native personally read all eight inventory stanzas. The complete saved
    reading is delegated and attributed; no new lookup or duplicate disjoint-source
    credit.
  snapshot_sha256: ba2cfcbc29e2def53103af238be8a37841b7fbe5ba22c73aef7a893abe7acb5e
- evidence_id: bgc-2413-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-target-input-plan-001.json
  locator: /records/2/proposed_companion_paths; /records/2/direct_companion_predicates
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact one-hop owned-BGC context membership; shared locus membership does
    not transfer full-key identity, stereochemistry, activity or producer claims.
  snapshot_sha256: 7776327261e7d5450ef8c6bb6401d3130de51f1ee913314ce19fbb46ae920994
- evidence_id: bgc-2413-companion-boundaries
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/6/path; /contexts/6/identifier; /contexts/6/label; /contexts/6/standard_inchi_key;
    /contexts/6/owned_bgc_ids; /contexts/8/path; /contexts/8/identifier; /contexts/8/label;
    /contexts/8/standard_inchi_key; /contexts/8/owned_bgc_ids; /contexts/9/path; /contexts/9/identifier;
    /contexts/9/label; /contexts/9/standard_inchi_key; /contexts/9/owned_bgc_ids;
    /contexts/10/path; /contexts/10/identifier; /contexts/10/label; /contexts/10/standard_inchi_key;
    /contexts/10/owned_bgc_ids; /contexts/11/path; /contexts/11/identifier; /contexts/11/label;
    /contexts/11/standard_inchi_key; /contexts/11/owned_bgc_ids; /contexts/12/path;
    /contexts/12/identifier; /contexts/12/label; /contexts/12/standard_inchi_key;
    /contexts/12/owned_bgc_ids; /contexts/13/path; /contexts/13/identifier; /contexts/13/label;
    /contexts/13/standard_inchi_key; /contexts/13/owned_bgc_ids
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Each direct companion retains its own label, full key, identifier and explicit
    owned BGC. These compact identity boundaries support context comparison only,
    not claim transfer.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
- evidence_id: bgc-2413-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved mibig_compounds frame has 1 matching placement with all
    fields and exact predicate/query. Database scope is limited to this retained join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact mibig_compounds predicate
    exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-source-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Header line 1; physical lines 2304–2304; row_sha256 cffc5b9525b4cd1dfe8d4ef36abb5b917ee47cc1da6d33c6a44ab6981491a0de
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact full-key compound/version/index, producer/locus grades, genome/coordinate/method
    fields and citation tier. BGC complete selected source-row reading carries.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2413-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved chebi_structures frame has 0 matching placements with all
    fields and exact predicate/query. Database scope is limited to this retained join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact chebi_structures predicate
    exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved lotus_occurrences frame has 1 matching placement with all
    fields and exact predicate/query. Database scope is limited to this retained join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact lotus_occurrences predicate
    exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-source-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Header line 1; physical lines 925–925; row_sha256 b8fe9910ecbda90ffb38d5888a5081ee908544f48d2580b882bac99d972fce63
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete organism/reference occurrence assertion, distinct from production
    and independent experiments. BGC complete selected source-row reading carries.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2413-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame has 0 matching placements with
    all fields and exact predicate/query. Database scope is limited to this retained
    join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact cyanometdb_occurrences
    predicate exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved npclassifier frame has 1 matching placement with all fields
    and exact predicate/query. Database scope is limited to this retained join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact npclassifier predicate
    exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-source-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Header line 1; physical lines 353–353; row_sha256 dbc2a55feed3099a808c029b9c3d84a107efeaf16ef1f902a8caa5a5fbcf7fd9
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact named/versioned model arrays and glycoside flag; retention does not
    establish applicability. BGC complete selected source-row reading carries.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2413-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame has 1 matching placement with all
    fields and exact predicate/query. Its blank-AID row is a no-assay sentinel.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact pubchem_bioassay predicate
    exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-source-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: Header line 1; physical lines 918–918; row_sha256 9f01b14fc498c56bd9045c36d904efda10f1d0b1bff7cb169b5d05d63edc0029
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Exact owner full-key/CID sentinel with blank AID, assay_name '(no assay
    data)', and blank outcome/measurement/target/reference fields. No actual assay
    observation. BGC complete selected source-row reading carries.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2413-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved bindingdb_targets frame has 0 matching placements with all
    fields and exact predicate/query. Database scope is limited to this retained join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact bindingdb_targets predicate
    exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame has 0 matching placements
    with all fields and exact predicate/query. Database scope is limited to this retained
    join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact antibioticmech_inchikeys
    predicate exact complete standard_inchi_key equality; query "CWPRIGWHYUKIHW-NHLPTZDRSA-N".
    Full matched rows or the complete empty result are retained. No replay/external
    lookup.
- evidence_id: bgc-2413-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch242-tentative/bgc-prep/bgc-conditional242-source-inventory-DATA-001.json
  locator: /contexts/7/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T15:48:40.370129Z'
  support: supports
  summary: Complete saved chebi_origins frame has 0 matching placements with all fields
    and exact predicate/query. Database scope is limited to this retained join.
  snapshot_sha256: 191b0e02721677b1156568242d485fc6fe58728f7f39f4d80a304f77966f34cc
  search_scope: Saved original local inventory only; exact chebi_origins predicate
    exact chebi_id from exact full-key structure rows; query []. Full matched rows
    or the complete empty result are retained. No replay/external lookup.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-242/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json
  accessed_at: '2026-11-04T15:14:15.534175Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 4716bbaef605acd509094f305d7449e615f0ca81f39a5664c2e4e0ddb25312b8
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-242/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json
  accessed_at: '2026-11-04T15:14:39.560929Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: b3b364375db71493f634201256cb5ef99d77c7df33a99ecc27778c0a15b5fea2
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-242/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json
  accessed_at: '2026-11-04T15:14:58.507530Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-242/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json
  accessed_at: '2026-11-04T15:15:31.306920Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-242/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-242/native-current242-five-gates-execution-001.json
  accessed_at: '2026-11-04T15:15:42.697838Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 5703b18c537e13d5d626dac20c1f6673e9c64544ebf3ec5f7fe06d446c579352
assessments:
- assessment_id: bgc-2413-identity
  area: identity
  topic: Retained identifier and normalized-form consistency; natural identity unverified
  outcome: supported
  summary: The minted identifier naturalproductmech:mibig-5a982ded92 retains the full
    key CWPRIGWHYUKIHW-NHLPTZDRSA-N from its MIBiG structure. The saved exact-key
    ChEBI join is empty; the grounding note is a historical explanation of minting,
    not a current universal ChEBI absence claim. PubChem 156582165 is a cross-reference.
    The seven other Tiancilactones are same-locus context with distinct full keys;
    a shared locus, formula or citation does not establish interchangeable identities.
    Both original forms normalize to C32H45NO8, charge 0 and the declared complete
    key. This supports the retained identifier/normalized-form join while leaving
    natural identity unverified.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-grounding-owner
  - bgc-2413-chemistry
  - bgc-2413-source-mibig_compounds
  - bgc-2413-query-chebi_structures
  - bgc-2413-direct-contexts
  - bgc-2413-companion-boundaries
  dimensions:
  - name: standard_inchi_key
    value: CWPRIGWHYUKIHW-NHLPTZDRSA-N; exact retained full key, not natural identity
      proof.
    definition: Exact full key; no name, first-block or congener substitution.
    evidence_ids:
    - bgc-2413-grounding-owner
    - bgc-2413-chemistry
    - bgc-2413-source-mibig_compounds
    - bgc-2413-query-chebi_structures
    - bgc-2413-direct-contexts
    - bgc-2413-companion-boundaries
  - name: grounding_scope
    value: The minted identifier naturalproductmech:mibig-5a982ded92 retains the full
      key CWPRIGWHYUKIHW-NHLPTZDRSA-N from its MIBiG structure. The saved exact-key
      ChEBI join is empty; the grounding note is a historical explanation of minting,
      not a current universal ChEBI absence claim. PubChem 156582165 is a cross-reference.
      The seven other Tiancilactones are same-locus context with distinct full keys;
      a shared locus, formula or citation does not establish interchangeable identities.
      Both original forms normalize to C32H45NO8, charge 0 and the declared complete
      key. This supports the retained identifier/normalized-form join while leaving
      natural identity unverified.
    definition: Local grounding fidelity is distinct from fresh natural-identity verification.
    evidence_ids:
    - bgc-2413-grounding-owner
    - bgc-2413-chemistry
    - bgc-2413-source-mibig_compounds
    - bgc-2413-query-chebi_structures
    - bgc-2413-direct-contexts
    - bgc-2413-companion-boundaries
- assessment_id: bgc-2413-representation
  area: representation
  topic: Original stored-form and stereochemical scope
  outcome: supported
  summary: Both original forms are neutral C32H45NO8 with 41 heavy atoms and 45 bonds.
    All ten comparison flags are true, and the supplied chirality-aware atom match
    covers the full atom count; full_graph_identity_established remains false. Each
    form has nine specified tetrahedral centers and one unspecified center at SMILES
    atom 20/reconstructed atom 27, consistent with the retained false flag. No configuration
    is filled from a congener. Atom indices are local diagnostic indices, not natural-product
    locants.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-grounding-owner
  - bgc-2413-chemistry
  - bgc-2413-topology
  - bgc-2413-diagnostic-reading
  - bgc-2413-diagnostic-acceptance
  - bgc-2413-structure-schema
  - bgc-2413-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: Both original forms are neutral C32H45NO8 with 41 heavy atoms and 45 bonds.
      All ten comparison flags are true, and the supplied chirality-aware atom match
      covers the full atom count; full_graph_identity_established remains false. Each
      form has nine specified tetrahedral centers and one unspecified center at SMILES
      atom 20/reconstructed atom 27, consistent with the retained false flag. No configuration
      is filled from a congener. Atom indices are local diagnostic indices, not natural-product
      locants.
    definition: Saved complete stereo/atom/bond interpretation, not an experimental
      assignment or a new parse.
    evidence_ids:
    - bgc-2413-grounding-owner
    - bgc-2413-chemistry
    - bgc-2413-topology
    - bgc-2413-diagnostic-reading
    - bgc-2413-diagnostic-acceptance
    - bgc-2413-structure-schema
    - bgc-2413-stereo-method
  - name: representation_correspondence
    value: All ten comparison flags are true and the supplied atom match is complete
      at this method’s scope. full_graph_identity_established remains false; no natural
      identity authentication.
    definition: Normalized identifier agreement does not establish explicit full-graph
      or natural-form identity.
    evidence_ids:
    - bgc-2413-grounding-owner
    - bgc-2413-chemistry
    - bgc-2413-topology
    - bgc-2413-diagnostic-reading
    - bgc-2413-diagnostic-acceptance
    - bgc-2413-structure-schema
    - bgc-2413-stereo-method
- assessment_id: bgc-2413-provenance
  area: provenance
  topic: Separate producer, locus and taxonomic claims
  outcome: supported
  summary: BGC0002019 v3 compound 2 retains Streptomyces sp. CB03234 NCBITaxon:1703937
    as SOURCE_ASSERTION. BK010469.1 remains CLUSTER_UNSTATED, with no coordinates
    or locus evidence methods supplied. The genus-level occurrence under NCBITaxon:1883
    cannot independently identify that strain or upgrade production or locus evidence.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-origin-owner
  - bgc-2413-occurrence-owner
  - bgc-2413-source-mibig_compounds
  - bgc-2413-cached-taxonomy
  - bgc-2413-curation-scope
  - bgc-2413-direct-contexts
  dimensions:
  - name: taxon_scope
    value: BGC0002019 v3 compound 2 retains Streptomyces sp. CB03234 NCBITaxon:1703937
      as SOURCE_ASSERTION. BK010469.1 remains CLUSTER_UNSTATED, with no coordinates
      or locus evidence methods supplied. The genus-level occurrence under NCBITaxon:1883
      cannot independently identify that strain or upgrade production or locus evidence.
    definition: Source taxa and cached labels preserve genus/species/strain scope;
      no fresh ancestry or production inference.
    evidence_ids:
    - bgc-2413-origin-owner
    - bgc-2413-occurrence-owner
    - bgc-2413-source-mibig_compounds
    - bgc-2413-cached-taxonomy
    - bgc-2413-curation-scope
    - bgc-2413-direct-contexts
  - name: producer_evidence
    value: BGC0002019 v3 compound 2 retains Streptomyces sp. CB03234 NCBITaxon:1703937
      as SOURCE_ASSERTION. BK010469.1 remains CLUSTER_UNSTATED, with no coordinates
      or locus evidence methods supplied. The genus-level occurrence under NCBITaxon:1883
      cannot independently identify that strain or upgrade production or locus evidence.
    definition: Producer evidence is assessed separately from occurrence and locus
      support.
    evidence_ids:
    - bgc-2413-origin-owner
    - bgc-2413-occurrence-owner
    - bgc-2413-source-mibig_compounds
    - bgc-2413-cached-taxonomy
    - bgc-2413-curation-scope
    - bgc-2413-direct-contexts
  - name: locus_evidence
    value: BGC0002019 v3 compound 2 retains Streptomyces sp. CB03234 NCBITaxon:1703937
      as SOURCE_ASSERTION. BK010469.1 remains CLUSTER_UNSTATED, with no coordinates
      or locus evidence methods supplied. The genus-level occurrence under NCBITaxon:1883
      cannot independently identify that strain or upgrade production or locus evidence.
    definition: Source version/status/method/grade does not establish a complete pathway
      or fresh primary support.
    evidence_ids:
    - bgc-2413-origin-owner
    - bgc-2413-occurrence-owner
    - bgc-2413-source-mibig_compounds
    - bgc-2413-cached-taxonomy
    - bgc-2413-curation-scope
    - bgc-2413-direct-contexts
- assessment_id: bgc-2413-citations
  area: evidence
  topic: Retained citation roles and attribution
  outcome: supported
  summary: DOI:10.1002/cbic.201800285 is selected from MIBiG COMPOUND_BIOACTIVITY
    provenance and repeated on producer and locus. The upper-case LOTUS DOI:10.1002/CBIC.201800285
    is an occurrence citation to the same DOI after case normalization, not independent
    experimental support. A bioactivity-tier citation supplies no actual assay endpoint,
    value or target here; no primary text was newly read.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-origin-owner
  - bgc-2413-occurrence-owner
  - bgc-2413-source-mibig_compounds
  - bgc-2413-source-lotus_occurrences
  - bgc-2413-source-reading
  dimensions:
  - name: citation_scope
    value: DOI:10.1002/cbic.201800285 is selected from MIBiG COMPOUND_BIOACTIVITY
      provenance and repeated on producer and locus. The upper-case LOTUS DOI:10.1002/CBIC.201800285
      is an occurrence citation to the same DOI after case normalization, not independent
      experimental support. A bioactivity-tier citation supplies no actual assay endpoint,
      value or target here; no primary text was newly read.
    definition: Distinguish retained database provenance, entry-level and compound-specific
      citations, occurrence references and any historical primary-experiment attribution.
      Repeated placements do not establish independent studies or fresh primary access.
    evidence_ids:
    - bgc-2413-origin-owner
    - bgc-2413-occurrence-owner
    - bgc-2413-source-mibig_compounds
    - bgc-2413-source-lotus_occurrences
    - bgc-2413-source-reading
- assessment_id: bgc-2413-occurrence
  area: evidence
  topic: Bounded occurrence and no-assay evidence
  outcome: supported
  summary: The owner retains one LOTUS occurrence at the Streptomyces genus, NCBITaxon:1883.
    It is distinct from the CB03234 strain-level producer assertion. The saved exact-key
    cyanobacterial and ChEBI-origin joins return no additional occurrence within these
    retained inventories; this is not absence from all literature.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-occurrence-owner
  - bgc-2413-source-lotus_occurrences
  - bgc-2413-source-pubchem_bioassay
  - bgc-2413-query-lotus_occurrences
  - bgc-2413-query-chebi_origins
  - bgc-2413-query-cyanometdb_occurrences
  - bgc-2413-query-pubchem_bioassay
  - bgc-2413-query-bindingdb_targets
  - bgc-2413-cached-taxonomy
  - bgc-2413-taxonomy-reading
  - bgc-2413-curation-scope
  - bgc-2413-mechanism-absence
  dimensions:
  - name: occurrence_scope
    value: The owner retains one LOTUS occurrence at the Streptomyces genus, NCBITaxon:1883.
      It is distinct from the CB03234 strain-level producer assertion. The saved exact-key
      cyanobacterial and ChEBI-origin joins return no additional occurrence within
      these retained inventories; this is not absence from all literature.
    definition: Occurrence assertions are not counts of independent experiments or
      producers.
    evidence_ids:
    - bgc-2413-occurrence-owner
    - bgc-2413-source-lotus_occurrences
    - bgc-2413-source-pubchem_bioassay
    - bgc-2413-query-lotus_occurrences
    - bgc-2413-query-chebi_origins
    - bgc-2413-query-cyanometdb_occurrences
    - bgc-2413-query-pubchem_bioassay
    - bgc-2413-query-bindingdb_targets
    - bgc-2413-cached-taxonomy
    - bgc-2413-taxonomy-reading
    - bgc-2413-curation-scope
    - bgc-2413-mechanism-absence
  - name: assay_target_scope
    value: The complete owner lacks bioactivities, bioactivity_summary and molecular_targets.
      Its PubChem row has blank AID, the literal assay_name '(no assay data)', and
      blank outcome, numeric measurement, target and reference fields. It is a no-assay
      sentinel, not an inactive result. The saved BindingDB join is empty; these bounded
      negatives do not establish inactivity or absence of published assays.
    definition: Written claims and exact retained assay/target routes are bounded;
      no global biological absence claim.
    evidence_ids:
    - bgc-2413-occurrence-owner
    - bgc-2413-source-lotus_occurrences
    - bgc-2413-source-pubchem_bioassay
    - bgc-2413-query-lotus_occurrences
    - bgc-2413-query-chebi_origins
    - bgc-2413-query-cyanometdb_occurrences
    - bgc-2413-query-pubchem_bioassay
    - bgc-2413-query-bindingdb_targets
    - bgc-2413-cached-taxonomy
    - bgc-2413-taxonomy-reading
    - bgc-2413-curation-scope
    - bgc-2413-mechanism-absence
- assessment_id: bgc-2413-classification
  area: consistency
  topic: Versioned model fidelity and bounded applicability
  outcome: concern
  summary: NPClassifier npclassifier.gnps2.org@2026-09-07 faithfully supplies Terpenoids,
    empty superclass/class arrays and is_glycoside:true. The complete encoding instead
    shows the unsaturated five-membered lactone described above, with an OH-bearing
    hemiacetal carbon and no assigned sugar residue or glycosidic linkage. This creates
    a bounded model-applicability concern; absence of a C5O motif alone would not
    exclude every sugar form, and no proved ingestion defect or record edit follows.
    The total 32 carbons include substituents and do not by themselves assign a terpenoid
    subclass.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-classification-owner
  - bgc-2413-source-npclassifier
  - bgc-2413-chemistry
  - bgc-2413-topology
  - bgc-2413-structure-schema
  - bgc-2413-classification-seeder
  dimensions:
  - name: classification_applicability
    value: NPClassifier npclassifier.gnps2.org@2026-09-07 faithfully supplies Terpenoids,
      empty superclass/class arrays and is_glycoside:true. The complete encoding instead
      shows the unsaturated five-membered lactone described above, with an OH-bearing
      hemiacetal carbon and no assigned sugar residue or glycosidic linkage. This
      creates a bounded model-applicability concern; absence of a C5O motif alone
      would not exclude every sugar form, and no proved ingestion defect or record
      edit follows. The total 32 carbons include substituents and do not by themselves
      assign a terpenoid subclass.
    definition: Model filing labels, observed topology and source BGC classes remain
      distinct axes.
    evidence_ids:
    - bgc-2413-classification-owner
    - bgc-2413-source-npclassifier
    - bgc-2413-chemistry
    - bgc-2413-topology
    - bgc-2413-structure-schema
    - bgc-2413-classification-seeder
- assessment_id: bgc-2413-completion
  area: completeness
  topic: Actual evidence coverage and scientific limits
  outcome: unknown
  summary: Complete owner/history, actual canonical intake, retained source rows and
    negative frames, and both original molecular forms have been read. All four mechanism
    roots are absent in this captured owner, so no maintained-mechanism reader applies.
    The record remains MINTED and SEEDED with 2 retained seed-history events. Its
    canonical intake identifies the maintained seeder, MIBiG extraction/table, classifier
    and occurrence/assay inventories as owners of distinct fields. Review authoring
    does not rewrite the generated record or promote its status. The ignored-inclusive
    local curation scan reports no applicable correction in its declared scope. Full
    QC/OAK, fresh primary and taxonomy/assay verification, and independent natural
    identity or stereochemical authentication remain unavailable. This is a partial
    review with no supported record-edit finding.
  target_ids:
  - naturalproductmech:mibig-5a982ded92
  evidence_ids:
  - bgc-2413-owner
  - bgc-2413-capture
  - bgc-2413-intake
  - bgc-2413-intake-acceptance
  - bgc-2413-history-owner
  - bgc-2413-diagnostic-reading
  - bgc-2413-diagnostic-acceptance
  - bgc-2413-diagnostic-execution
  - bgc-2413-source-reading
  - bgc-2413-joint-source-notes
  - bgc-2413-source-plan-acceptance
  - bgc-2413-curation-scope
  - bgc-2413-mechanism-absence
  dimensions:
  - name: review_completion
    value: Complete owner/history, actual canonical intake, retained source rows and
      negative frames, and both original molecular forms have been read. All four
      mechanism roots are absent in this captured owner, so no maintained-mechanism
      reader applies. The record remains MINTED and SEEDED with 2 retained seed-history
      events. Its canonical intake identifies the maintained seeder, MIBiG extraction/table,
      classifier and occurrence/assay inventories as owners of distinct fields. Review
      authoring does not rewrite the generated record or promote its status. The ignored-inclusive
      local curation scan reports no applicable correction in its declared scope.
      Full QC/OAK, fresh primary and taxonomy/assay verification, and independent
      natural identity or stereochemical authentication remain unavailable. This is
      a partial review with no supported record-edit finding.
    definition: Completion reflects actual evidence access and check coverage; parsing
      and gate success are not scientific proof.
    evidence_ids:
    - bgc-2413-owner
    - bgc-2413-capture
    - bgc-2413-intake
    - bgc-2413-intake-acceptance
    - bgc-2413-history-owner
    - bgc-2413-diagnostic-reading
    - bgc-2413-diagnostic-acceptance
    - bgc-2413-diagnostic-execution
    - bgc-2413-source-reading
    - bgc-2413-joint-source-notes
    - bgc-2413-source-plan-acceptance
    - bgc-2413-curation-scope
    - bgc-2413-mechanism-absence
findings: []
actions: []
limitations:
- Retained local evidence only; fresh primary literature, taxonomy, assay protocols
  and independent natural identity or stereochemistry remain unverified.
- Full QC and complete OAK coverage remain unavailable. Local normalization, motif
  descriptions and supplied atom matches are not independent full-graph or natural-state
  proof.
- Producer, locus, occurrence, strain and citation tiers remain distinct; repeated
  references and congeners do not transfer claims or experimental independence.
- Versioned model fidelity is assessable; the stated applicability concerns do not
  prove an ingestion defect or justify a source replacement.
- The complete owner has no graph/pathway/component/target roots. No maintained-mechanism
  result or source status/history edit is claimed.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- 'BGC personally read all ten first-five forms: 404 atom rows and 444 bond rows,
  all strings/scalars/rings/stereo/motifs/maps. Diagnostic indices are zero-based
  and are not biochemical locants; original stderr is empty.'
- 'Disjoint source meanings: BGC ten contexts/54 rows/556 fields/90 frames; Support
  five contexts/26 rows/278 fields/45 frames. Native read all 8 cache stanzas and
  the ignored-inclusive curation scan; BGC additionally read three unique first-five
  stanzas. Prior companion raw/history carries remain attributed.'
- BGC operated the admitted local source collector/composer. Support operated the
  ten canonical intakes; ROOT operated the original molecular diagnostic. Native authored/audited
  the diagnostic and supplied cache/curation reading. Review authoring invokes no
  target.
- All outcomes remain partial with no supported edit finding or action; missing fresh
  verification or model concern alone is not a defect.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-242
```
