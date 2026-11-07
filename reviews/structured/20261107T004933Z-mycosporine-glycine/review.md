# Local evidence review: mycosporine glycine

- Review: 20261107T004933Z-mycosporine-glycine
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T23:53:39.609939Z
- Finished UTC: 2026-11-07T00:49:33.509663Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Mycosporine glycine has internally agreeing saved molecular forms and a faithfully returned downstream Ava_3855 mechanism. Its sole biosynthetic_pathway step consumes the owner to form shinorine, conflicting with the current owner-centred PathwayStep meaning and affecting queue/render interpretation. This unresolved major scope issue warrants needs_curation, with partial completion; it does not establish false reaction chemistry.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2797; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-00a364fe41 | data/natural_products/unclassified/mycosporine-glycine.yaml | generated | mycosporine glycine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-00a364fe41 | Both stored forms parsed and retain declared normalized keys; Both canonical SMILES comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established remains false. |
| Complete offline maintained reader for mycosporine-glycine | passed | True | naturalproductmech:mibig-00a364fe41 | One original complete offline maintained reader returned the exact captured owner. |
| strict_ten | passed | True | naturalproductmech:mibig-00a364fe41 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-00a364fe41 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-00a364fe41 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-00a364fe41 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-00a364fe41 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-00a364fe41 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-00a364fe41 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-00a364fe41 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-00a364fe41.

The exact XZQILKYKJYHEHD-JTQLQIEISA-N grouping is BGC0000427 version 5, compound index 3, naturalproductmech:mibig-00a364fe41. The explicit Shinorine and 4-deoxygadusol companions remain distinct owners, not alternate structures or merged identities.

### Saved molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-00a364fe41.

Both saved forms contain 17 atoms, 17 bonds, neutral C10H15NO6 and one six-carbon ring. All ten comparison flags agree, including both canonical SMILES strings, and the limited chirality-aware map contains all 17 atom indices. The diagnostic nevertheless explicitly leaves full_graph_identity_established false; this is not experimental identity or pathway validation. The ring contains a ketone and an unsaturated amino/methoxy-substituted segment; the substituent carries a carboxylic acid and a secondary amino linkage. The saved ketone is S1=O0/I6=O12 and the carboxyl carbon S8/I7. The methoxy bridge S3/I16 is not a sugar linkage. Strict amide, ester, nonamide primary-amine and saturated C5O-ring predicates are empty. The sole configured centre is S12/I9, both S. Both canonical SMILES comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established remains false. Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.

### Compound-specific producer, locus and taxon

provenance: supported. Targets: naturalproductmech:mibig-00a364fe41.

Trichormus variabilis ATCC 29413 (240292) remains SOURCE_ASSERTION. Enzymatic assays and heterologous expression grade the BGC link, not the producer claim. Chlorogloeopsis occurrences are separate roles and strains. BGC0000427 version 5, CP000117.1:4798900-4805360, retains active/questionable/complete metadata and CLUSTER_DEMONSTRATED with Enzymatic assays and Heterologous expression. ENTRY PMID:20813918 is not newly read compound-specific primary proof.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-00a364fe41.

The owner has two seeding events and one deliberate 2026-10-23 downstream-curation event. The step and each of three graph edges retain DOI:10.1126/science.1193637, a BGC0000427.5 URL and UniProtKB:Q3M6C6 attribution: 12 placements of three repeated references, not 12 independent studies. The source PMID and stored DOI are not treated as independently verified publications. Primary-experiment labels, HPLC claims, exact protein identity and strain equivalences remain historical attributed assertions.

### Occurrence and assay limits

evidence: supported. Targets: naturalproductmech:mibig-00a364fe41.

Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759, DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used yes and PMID:26286672. These records do not establish equivalence to the MIBiG strain or publication independence. Saved PubChem, BindingDB and AntibioticMech exact-key frames are negative. The retained enzyme-coupling annotation is biosynthetic context, not a measured compound potency or molecular-target assertion. No inactivity or universal assay absence is inferred.

### Source classes, model labels and filing

consistency: supported. Targets: naturalproductmech:mibig-00a364fe41.

Mycosporine derivatives and Mycosporine and Mycosporine-like amino acids are retained model labels, consistent with a qualified amino-substituted cyclohexenone description. The model has Amino acids and Peptides plus Shikimates and Phenylpropanoids, so choose_pathway retains UNCLASSIFIED. Molecular agreement does not adjudicate pathway field ownership.

### Complete retained mechanism and owner scope

consistency: concern. Targets: naturalproductmech:mibig-00a364fe41.

The accepted complete view preserves one BIOSYNTHESIS graph with four nodes and three edges, one step numbered 4 with proposed absent, three histories, and no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates; Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product. The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis is inferred. PathwayStep is defined as an enzymatic step in biosynthesis of this compound. Intermediate steps need not individually produce the owner, but this sole terminal step explicitly consumes the owner and produces a different compound. Its full step block is already present in the Shinorine product owner. Deliberate downstream history and the broader causal-graph definition are material competing context, yet do not provide an explicit exception for the narrower field. The current queue omits this owner from biosynthesis despite one demonstrated locus because the field is nonempty; the renderer labels it curated Biosynthesis. These are material scope/representation consequences. The clearly directed downstream graph may remain as qualified context; the finding concerns pathway placement, not asserted enzyme chemistry or a blanket rejection of that graph. The policy interpretation remains provisional pending curator resolution.

### Earned work and unavailable authority

completeness: concern. Targets: naturalproductmech:mibig-00a364fe41.

Complete assigned raw/source/intake and both saved molecular forms were read. The required original maintained reader returned the complete owner; preservation does not verify mechanism science. The provisional major pathway-owner finding remains open. Five local native commands pass; full QC, complete OAK and fresh primary verification remain unavailable. Completion is partial, native SEEDED status unchanged.

## Findings

### support-2797-downstream-pathway-owner-scope: Downstream shinorine synthesis occupies the precursor owner biosynthesis field

major / open / provisional; issue key: mycosporine-glycine-downstream-pathway-owner-scope.

PathwayStep is defined as an enzymatic step in biosynthesis of this compound. Intermediate steps need not individually produce the owner, but this sole terminal step explicitly consumes the owner and produces a different compound. Its full step block is already present in the Shinorine product owner. Deliberate downstream history and the broader causal-graph definition are material competing context, yet do not provide an explicit exception for the narrower field. The current queue omits this owner from biosynthesis despite one demonstrated locus because the field is nonempty; the renderer labels it curated Biosynthesis. These are material scope/representation consequences. The clearly directed downstream graph may remain as qualified context; the finding concerns pathway placement, not asserted enzyme chemistry or a blanket rejection of that graph. The policy interpretation remains provisional pending curator resolution.

## Recommended Actions And Acceptance Checks

### support-2797-resolve-pathway-owner-placement

Use the validated curator-owned record workflow to remove or relocate the downstream-only pathway step from the precursor owner, preserving the explicitly directed downstream graph, evidence and append-only history. The identical terminal step already exists in Shinorine. Alternatively resolve the model ambiguity through an explicit maintained schema/documentation/consumer policy change; a note alone does not change current queue behavior. Do not invent upstream steps, renumber step 4, or add proposed:true as a placement fix.

- The selected owner no longer represents a different product terminal step as its own biosynthesis unless a documented maintained policy explicitly authorizes it.
- Preserve chemical structures, producer/locus grades, downstream direction, evidence, graph qualifiers and all existing history; append a new curation event for a future edit.
- Avoid duplicating the existing Shinorine annotation or inventing unverified upstream chemistry.
- In a separately authorized correction workflow, validate through the maintained writer and verify queue/render/reproduction behavior with focused regressions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2797-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/mycosporine-glycine.yaml; complete file: chemical_structure, source_concepts, producer_organisms, biosynthetic_gene_clusters, classification, mechanisms and curation_history | supports | Complete current owner retained; generated facts and curator-owned mechanisms remain distinct. |
| support-2797-capture | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/6/owner_document; /records/6/component_captures | supports | Whole accepted owner capture; no component or target transfer. |
| support-2797-source | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-assigned-source-reading-001.json; /contexts/4; /selected_counts; /counts; /global_cautions | supports | Complete assigned saved source context. Own selected credit totals 18 rows/239 fields/45 frames/31 negatives; five companions have separate context-only credit. |
| support-2797-plan | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json; /records/6; /source_placement_count; /unique_source_path_count | supports | Actual 463-placement/72-path plan; this owner has 55 captured inputs. |
| support-2797-planaccept | /private/tmp/npm-review-work/shared-next-batch280/root-current280-input-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepted this original current source plan. |
| support-2797-notes | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Current notes retain the disjoint source and Native taxonomy/curation interpretations; no added primary credit. |
| support-2797-intake | /private/tmp/npm-review-work/shared-next-batch280/intakes-001/2797-inspect-001.json; /status; /source; /targets | supports | Actual intake fixes generated target, maintained owners and current relative input hashes. |
| support-2797-intakeaccept | /private/tmp/npm-review-work/shared-next-batch280/root-current280-intake-acceptance-001.json; /status; /accepted; /intake_summary | supports | ROOT accepted all ten original intakes, all exit zero with empty stderr. |
| support-2797-data | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence; /records/6/literal_InChI_layers; /records/6/formula_comparison_scope | supports | Both saved forms contain 17 atoms, 17 bonds, neutral C10H15NO6 and one six-carbon ring. All ten comparison flags agree, including both canonical SMILES strings, and the limited chirality-aware map contains all 17 atom indices. The diagnostic nevertheless explicitly leaves full_graph_identity_established false; this is not experimental identity or pathway validation. Both canonical SMILES comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established remains false. |
| support-2797-stereo | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed/atoms; /records/6/smiles/computed/potential_stereo; /records/6/smiles/computed/bonds; /records/6/inchi/computed/atoms; /records/6/inchi/computed/potential_stereo; /records/6/inchi/computed/bonds | supports | One specified S tetrahedral centre and no unspecified potential tetrahedral or double-bond candidate are recorded in either form. The source atom-stereo flag and complete limited map do not establish natural absolute stereochemistry or independent full graph identity. |
| support-2797-motifs | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json; /records/6/smiles/computed/motifs; /records/6/smiles/computed/rings; /records/6/smiles/computed/bonds; /records/6/smiles/computed/atoms; /records/6/inchi/computed/motifs; /records/6/inchi/computed/rings; /records/6/inchi/computed/bonds; /records/6/inchi/computed/atoms | supports | The ring contains a ketone and an unsaturated amino/methoxy-substituted segment; the substituent carries a carboxylic acid and a secondary amino linkage. The saved ketone is S1=O0/I6=O12 and the carboxyl carbon S8/I7. The methoxy bridge S3/I16 is not a sugar linkage. Strict amide, ester, nonamide primary-amine and saturated C5O-ring predicates are empty. The sole configured centre is S12/I9, both S. |
| support-2797-molecularreading | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-molecular-intake-reading-001.json; /records/1; /counts; /warnings | supports | Complete ten saved forms personally read; no molecular replay. Four original undefined-stereo warning lines and two proton-addition/removal warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2797-execution | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | Single original diagnostic command and retained streams; no replay. |
| support-2797-diagaccept | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/root-current280-diagnostic-acceptance-001.json; /status; /accepted; /diagnostic; /execution | supports | ROOT accepted the original stored-form diagnostic. |
| support-2797-stderr | /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-original-001.stderr; complete six original warning lines | supports | Four original undefined-stereo warning lines and two proton-addition/removal warning lines remain globally unassigned; none is assigned to an individual owner. |
| support-2797-taxonomy | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-cached-taxonomy-reading-001.json; /context_interpretations/13; /physical_negative_query_scopes/13; /whole_stanzas | supports | The source producer Trichormus variabilis ATCC 29413 (240292), BGC0000427:3/CP000117.1, remains separate from three Chlorogloeopsis (1123) LOTUS occurrences and CyanoMetDB Chlorogloeopsis sp. (28069), literal PCC 6912 context. Cached historical names do not equate those strains. Preserving downstream step 4 is not an adjudication of pathway-owner semantics. |
| support-2797-curation | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | No current exact applicable maintained correction; lexical names and unrelated BGC rows do not transfer decisions. |
| support-2797-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete method grading table | supports | Producer evidence and locus methods answer different questions; unstated methods retain their grade. |
| support-2797-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 165-172, atom-centre completeness predicate | supports | Retained stereo_complete checks unassigned atom centres, not all geometry or natural identity. |
| support-2797-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306, choose_pathway | supports | One supported normalized pathway selects filing; multiple, none or unsupported values retain UNCLASSIFIED. |
| support-2797-gates | /private/tmp/npm-review-work/shared-next-batch280/root-current280-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /selected_queue_rows; /selected_queue_counts/2797; /unavailable_required_gates | supports | Five local gates pass, with required QC/OAK unavailable. Actual queue entries are diagnostic leads, not automatic scientific findings. |
| support-2797-history | /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json; /records/6/owner_document/curation_history; /records/6/owner_document/source_concepts | supports | The owner has two seeding events and one deliberate 2026-10-23 downstream-curation event. The step and each of three graph edges retain DOI:10.1126/science.1193637, a BGC0000427.5 URL and UniProtKB:Q3M6C6 attribution: 12 placements of three repeated references, not 12 independent studies. The source PMID and stored DOI are not treated as independently verified publications. Primary-experiment labels, HPLC claims, exact protein identity and strain equivalences remain historical attributed assertions. |
| support-2797-scope | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json; /records/6/complete_root_keys; /records/6/declared_mechanism_roots_literal; /records/6/component_paths; /records/6/complete_raw_mechanism_sections | supports | The accepted complete view preserves one BIOSYNTHESIS graph with four nodes and three edges, one step numbered 4 with proposed absent, three histories, and no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates; Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product. The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis is inferred. |
| support-2797-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame with 1 positive placements read. |
| support-2797-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 590, raw UTF-8 row SHA-256 e3c09a2334a41ff210c268dbe7418bd91c0cd8fe0f6bb5959c1731976588ea0c | supports | The exact XZQILKYKJYHEHD-JTQLQIEISA-N grouping is BGC0000427 version 5, compound index 3, naturalproductmech:mibig-00a364fe41. The explicit Shinorine and 4-deoxygadusol companions remain distinct owners, not alternate structures or merged identities. Trichormus variabilis ATCC 29413 (240292) remains SOURCE_ASSERTION. Enzymatic assays and heterologous expression grade the BGC link, not the producer claim. Chlorogloeopsis occurrences are separate roles and strains. BGC0000427 version 5, CP000117.1:4798900-4805360, retains active/questionable/complete metadata and CLUSTER_DEMONSTRATED with Enzymatic assays and Heterologous expression. ENTRY PMID:20813918 is not newly read compound-specific primary proof. |
| support-2797-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_structures | supports | Complete saved chebi_structures frame with 0 positive placements read. |
| support-2797-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame with 3 positive placements read. |
| support-2797-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 9720, raw UTF-8 row SHA-256 0696ac49968f3f7192c579b9590ea7d47e95d1a806ad34e0332433c2f75ebe45; physical line 9721, raw UTF-8 row SHA-256 ab229854d291fe61a8918c115ef83382d1f5649e1839ea5b90eef751b4955070; physical line 9722, raw UTF-8 row SHA-256 fa803cd1cdf67953c3b529d171028637d02b86128e42e8c52c1a5976c51bda7b | supports | Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759, DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used yes and PMID:26286672. These records do not establish equivalence to the MIBiG strain or publication independence. |
| support-2797-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences | supports | Complete saved cyanometdb_occurrences frame with 1 positive placements read. |
| support-2797-table-cyanometdb_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/cyanometdb_occurrences.tsv; physical line 90, raw UTF-8 row SHA-256 fe6d73a49b91dad410b8106ba6c0c7c28b1e1f1ab4c90fca2d160a754ebb9b98 | supports | Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759, DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used yes and PMID:26286672. These records do not establish equivalence to the MIBiG strain or publication independence. |
| support-2797-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame with 1 positive placements read. |
| support-2797-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 2872, raw UTF-8 row SHA-256 7f97193be5da2a9691ef8b5bfb57db40af9ef7aa944c54cdde3ccff8a43b2f69 | supports | Mycosporine derivatives and Mycosporine and Mycosporine-like amino acids are retained model labels, consistent with a qualified amino-substituted cyclohexenone description. The model has Amino acids and Peptides plus Shikimates and Phenylpropanoids, so choose_pathway retains UNCLASSIFIED. Molecular agreement does not adjudicate pathway field ownership. |
| support-2797-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame with 0 positive placements read. |
| support-2797-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/bindingdb_targets | supports | Complete saved bindingdb_targets frame with 0 positive placements read. |
| support-2797-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Complete saved antibioticmech_inchikeys frame with 0 positive placements read. |
| support-2797-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json; /contexts/13/source_scope_inventory/joins/chebi_origins | supports | Complete saved chebi_origins frame with 0 positive placements read. |
| support-2797-reader-data | /private/tmp/npm-review-work/shared-next-batch280/native-current280-mycosporine-glycine-maintained-reader-DATA-001.json; /raw_owner; /resolved_view; /expected_view; /counts; /reader_call_count; /denials; /unexpected_denials; /errors | supports | The accepted complete view preserves one BIOSYNTHESIS graph with four nodes and three edges, one step numbered 4 with proposed absent, three histories, and no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates; Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product. The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis is inferred. Whole returned owner equals accepted capture; no primary or scientific validation follows. |
| support-2797-reader-execution | /private/tmp/npm-review-work/shared-next-batch280/native-current280-mycosporine-glycine-reader-execution-001.json; /command; /exit_code; /stdout; /stderr; /retries | supports | One original offline maintained call, zero exit and stderr; known socket construction denied before action, no requests. |
| support-2797-reader-accept | /private/tmp/npm-review-work/shared-next-batch280/root-current280-mycosporine-glycine-reader-acceptance-001.json; /status; /accepted; /DATA; /execution; /review_check_contract; /limits | supports | ROOT accepted the complete returned owner and exact check contract; interpretation remains separate. |
| support-2797-reader-reading | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-maintained-reader-reading-001.json; /records/0 | supports | review_support read every returned owner, graph, node, edge, evidence, pathway and history value. |
| support-2797-placement | /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-2797-pathway-placement-assessment-001.json; /conclusion; /reconciliation; /retained_schema_and_consumer_excerpts; /complete_actual_reader; /prior_bounded_ignored_inclusive_search | supports | PathwayStep is defined as an enzymatic step in biosynthesis of this compound. Intermediate steps need not individually produce the owner, but this sole terminal step explicitly consumes the owner and produces a different compound. Its full step block is already present in the Shinorine product owner. Deliberate downstream history and the broader causal-graph definition are material competing context, yet do not provide an explicit exception for the narrower field. The current queue omits this owner from biosynthesis despite one demonstrated locus because the field is nonempty; the renderer labels it curated Biosynthesis. These are material scope/representation consequences. The clearly directed downstream graph may remain as qualified context; the finding concerns pathway placement, not asserted enzyme chemistry or a blanket rejection of that graph. The policy interpretation remains provisional pending curator resolution. |
| support-2797-native-semantic | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-2797-pathway-owner-independent-semantic-reading-001.json; /conclusion; /normative_reasoning; /competing_context_and_limits; /provisional_finding; /bounded_curator_action | supports | Native independently reaches the same provisional major owner-scope concern; review_support independently read the underlying excerpts and actual returned owner. |
| support-2797-semantic-schema_parent | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 259-270 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-schema_step | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 593-625 | supports | PathwayStep describes biosynthesis of this compound. |
| support-2797-semantic-schema_graph_scope | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 1137-1142 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-owner_step | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/mycosporine-glycine.yaml; lines 113-144 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-owner_history | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/mycosporine-glycine.yaml; lines 250-266 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-counterpart_step | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/shinorine.yaml; lines 146-177 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-counterpart_history | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/shinorine.yaml; lines 283-297 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-queue_consumer | /private/tmp/npm-record-reviews-20261021/scripts/curation_worklist.py; lines 175-192 | supports | Nonempty pathway bypasses the biosynthesis queue before locus grading. |
| support-2797-semantic-queue_test | /private/tmp/npm-record-reviews-20261021/tests/test_curation_worklist.py; lines 57-75 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-render_steps | /private/tmp/npm-record-reviews-20261021/scripts/render_pages.py; lines 208-215 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-render_template | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/templates/record.html; lines 109-128 | supports | Populated pathway is presented as curated Biosynthesis. |
| support-2797-semantic-review_owner_boundary | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; lines 35-56 | supports | Exact current retained owner-policy/consumer excerpt; endpoint direction and deliberate historical scope are preserved. |
| support-2797-semantic-search | /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-conditional280-pathway-owner-semantics-001.json; /search_scope | supports | Native bounded maintained-text search found no explicit downstream-owner exception; scope is not universal. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-280/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-280/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-280/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-280/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized key/formula agreement and a successful local process do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established remains false. One specified S tetrahedral centre and no unspecified potential tetrahedral or double-bond candidate are recorded in either form. The source atom-stereo flag and complete limited map do not establish natural absolute stereochemistry or independent full graph identity.
- Four original undefined-stereo warning lines and two proton-addition/removal warning lines remain globally unassigned; none is assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh current 280 evidence and judgments; prior batches provide interface logic only.
- No source row, record, campaign or native status was changed; no query, molecular parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks; only orders 2797 and 2798 in this fragment receive actual maintained-reader checks.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T004933Z-mycosporine-glycine
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: mycosporine glycine'
started_at: '2026-11-06T23:53:39.609939Z'
finished_at: '2026-11-07T00:49:33.509663Z'
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
summary: Mycosporine glycine has internally agreeing saved molecular forms and a faithfully
  returned downstream Ava_3855 mechanism. Its sole biosynthetic_pathway step consumes
  the owner to form shinorine, conflicting with the current owner-centred PathwayStep
  meaning and affecting queue/render interpretation. This unresolved major scope issue
  warrants needs_curation, with partial completion; it does not establish false reaction
  chemistry.
source:
  git_revision: ce6a5498df5be51116bd5e0c119023ee62bb5464
  state: working_tree
  inputs:
  - path: .claude/skills/add-proteins-to-graphs/SKILL.md
    sha256: 139a65a4e3404ceae275a01a724c43f85062de86a19d1772eea52fb54e52735a
    role: context
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
  - path: data/natural_products/unclassified/4-deoxygadusol.yaml
    sha256: 207fd06afecc3931ae3bd06c26f6a34e0ecc9955cb440c736c274c29ea76992b
    role: context
  - path: data/natural_products/unclassified/mycosporine-glycine.yaml
    sha256: a633697a3f5f44f2947951f4f17e934a3812cc63c602d40540468d63104b64b0
    role: target
  - path: data/natural_products/unclassified/shinorine.yaml
    sha256: eb3991e3cea604c58583a38d6ba53538302bce8c9329b229957f83d3989ff582
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
  - path: scripts/curation_worklist.py
    sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
    role: context
  - path: scripts/extract_chebi.py
    sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/render_pages.py
    sha256: e3dc205d44111813cc02439caff895e30e8c06756d74a7675acbe15d84cf14ab
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
  - path: src/naturalproductmech/templates/record.html
    sha256: 4c5143ae98b51531c3b708cf73590decd50f3e222e375d91288a54ef767e7893
    role: context
  - path: src/naturalproductmech/validation/write_validated.py
    sha256: 4b7648fc5d2e7a5d26ad8bb168dbcae609aaa2694434a8ed5cfcb33fb66ff80a
    role: context
  - path: tests/test_curation_worklist.py
    sha256: fd6171c4533ef20b8cffc1f73d57fd081e32060ca672ab647c7034e4394984f6
    role: context
  - path: tests/test_render_pages.py
    sha256: c294d3f879b917963c22347a52fffb9b7c2bee110164c2fbcd48e35ad1e3e951
    role: context
  - path: tests/test_schema.py
    sha256: 9bb9579bc83285d270d8e0d6944329fd975234cc728e65458e5edbd868ba4859
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2797; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-00a364fe41
targets:
- target_id: naturalproductmech:mibig-00a364fe41
  path: data/natural_products/unclassified/mycosporine-glycine.yaml
  label: mycosporine glycine
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
    path: .claude/skills/add-proteins-to-graphs/SKILL.md
    role: 'Order 2797 only: retained curation guidance for pathway ordering, exact
      endpoints, evidence and proposed flags; policy context for the open owner-scope
      question, not a downstream exception or primary scientific verification.'
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
    role: Exact retained selected/direct/comparison taxon decision; no fresh authority.
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/taxon_non_organism.tsv
    role: Retained non-organism table used by positive and negative taxon queries
      for each owner; diagnostic scope only, not a taxon verdict from file presence.
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/curation_worklist.py
    role: 'Order 2797 only: maintained queue consumer skips records with a nonempty
      biosynthetic_pathway; supports assessment of field-presence impact, not correctness
      of the stored biological direction.'
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/render_pages.py
    role: 'Order 2797 only: retained renderer projects singular or plural pathway
      endpoints and labels; supports interpretation of displayed downstream context
      without validating owner-product direction.'
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
    path: src/naturalproductmech/templates/record.html
    role: 'Order 2797 only: retained template labels a populated pathway as curated
      biosynthesis and displays substrate-to-product steps; presentation impact only,
      not primary mechanism proof.'
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/validation/write_validated.py
    role: Future maintained complete-owner reader implementation; not invoked in this
      plan.
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_curation_worklist.py
    role: 'Order 2797 only: retained test documents the queue exclusion for an existing
      pathway; plaintext consumer-contract evidence only, no test execution or biological
      validation.'
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_render_pages.py
    role: 'Order 2797 only: retained rendering tests cover ungrounded endpoints and
      an absent step number; they do not establish an exception to owner-centered
      pathway semantics or execute here.'
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_schema.py
    role: 'Order 2797 only: retained PathwayStep evidence-requirement test supplies
      bounded schema-contract context; it is not biochemical validation or an owner-direction
      exception.'
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/mycosporine-glycine.yaml
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
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnose280-001.py
    2ba99053ef31c5bdddb405acb0108a92720b8a4af71d98f5b032ccd0adfb11b7 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
    df0120607515dc9243bfa92b39622a3bb842fd0bd3d1eb18d29677b785fd591b
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed and retain declared normalized keys; Both canonical
    SMILES comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established
    remains false.
  scope_note: Both saved forms contain 17 atoms, 17 bonds, neutral C10H15NO6 and one
    six-carbon ring. All ten comparison flags agree, including both canonical SMILES
    strings, and the limited chirality-aware map contains all 17 atom indices. The
    diagnostic nevertheless explicitly leaves full_graph_identity_established false;
    this is not experimental identity or pathway validation. One specified S tetrahedral
    centre and no unspecified potential tetrahedral or double-bond candidate are recorded
    in either form. The source atom-stereo flag and complete limited map do not establish
    natural absolute stereochemistry or independent full graph identity. Four original
    undefined-stereo warning lines and two proton-addition/removal warning lines remain
    globally unassigned; none is assigned to an individual owner.
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-data
  - support-2797-execution
  - support-2797-diagaccept
- check_id: maintained-mechanism-reader
  name: Complete offline maintained reader for mycosporine-glycine
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -B /private/tmp/npm-review-work/shared-next-batch280/read-selected-mechanism-guarded-001.py
    2797 df0120607515dc9243bfa92b39622a3bb842fd0bd3d1eb18d29677b785fd591b 36cccfc5add051ebc91a6a3725e9e247982bb4985092c423e9caf13319d1f91f
    a44b8239212154b11705bb659af9577a9ea6c7a94ca560b4a804f10dc48b84aa 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
    2ba99053ef31c5bdddb405acb0108a92720b8a4af71d98f5b032ccd0adfb11b7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: One original complete offline maintained reader returned the exact captured
    owner.
  scope_note: The accepted complete view preserves one BIOSYNTHESIS graph with four
    nodes and three edges, one step numbered 4 with proposed absent, three histories,
    and no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates;
    Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product.
    The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No
    renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis
    is inferred. Reader success is preservation and topology evidence, not scientific
    field-placement or primary-source validation.
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-reader-data
  - support-2797-reader-execution
  - support-2797-reader-accept
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  command: just validate-strict data/natural_products/unclassified/ml-449.yaml data/natural_products/unclassified/montamide-a.yaml
    data/natural_products/unclassified/montanastatin.yaml data/natural_products/unclassified/muscoride-b.yaml
    data/natural_products/unclassified/mutanocyclin.yaml data/natural_products/unclassified/mycobactin.yaml
    data/natural_products/unclassified/mycosporine-glycine.yaml data/natural_products/unclassified/myxarylin.yaml
    data/natural_products/unclassified/myxochromide-b.yaml data/natural_products/unclassified/myxochromide-c.yaml
    --workers 1 --out /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-00a364fe41
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-280/validate-all-001.tsv
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
  - naturalproductmech:mibig-00a364fe41
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
  - naturalproductmech:mibig-00a364fe41
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
  - naturalproductmech:mibig-00a364fe41
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-280/review-queue-001.tsv
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
  - naturalproductmech:mibig-00a364fe41
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2797-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/mycosporine-glycine.yaml
  locator: 'complete file: chemical_structure, source_concepts, producer_organisms,
    biosynthetic_gene_clusters, classification, mechanisms and curation_history'
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete current owner retained; generated facts and curator-owned mechanisms
    remain distinct.
  snapshot_sha256: a633697a3f5f44f2947951f4f17e934a3812cc63c602d40540468d63104b64b0
- evidence_id: support-2797-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/6/owner_document; /records/6/component_captures
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Whole accepted owner capture; no component or target transfer.
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: support-2797-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-assigned-source-reading-001.json
  locator: /contexts/4; /selected_counts; /counts; /global_cautions
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete assigned saved source context. Own selected credit totals 18 rows/239
    fields/45 frames/31 negatives; five companions have separate context-only credit.
  snapshot_sha256: 585a5127b5ae32d25e5558b6d6299bb5da1cdf7584de93d3f093bd410ea4b5b0
- evidence_id: support-2797-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json
  locator: /records/6; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Actual 463-placement/72-path plan; this owner has 55 captured inputs.
  snapshot_sha256: d6777f8dea91c7542347ffaf26f8bc8cc03d93b08032d32861abac52335c3fa3
- evidence_id: support-2797-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-input-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted this original current source plan.
  snapshot_sha256: 0e8c34013ec3794cfaa30bcb060b8a8717b99a038f5ba349a893ae7fbc47c2ce
- evidence_id: support-2797-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Current notes retain the disjoint source and Native taxonomy/curation interpretations;
    no added primary credit.
  snapshot_sha256: e5b80095d288105ec28103716a87da06b65c083b79bf0fbbac86dc83773a08d4
- evidence_id: support-2797-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/intakes-001/2797-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Actual intake fixes generated target, maintained owners and current relative
    input hashes.
  snapshot_sha256: 36cccfc5add051ebc91a6a3725e9e247982bb4985092c423e9caf13319d1f91f
- evidence_id: support-2797-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-intake-acceptance-001.json
  locator: /status; /accepted; /intake_summary
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted all ten original intakes, all exit zero with empty stderr.
  snapshot_sha256: e11e8f952eeb308c816112881974c56ec907ec0a5ee8935ee308347ab2e2d871
- evidence_id: support-2797-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles; /records/6/inchi; /records/6/comparisons; /records/6/atom_correspondence;
    /records/6/literal_InChI_layers; /records/6/formula_comparison_scope
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Both saved forms contain 17 atoms, 17 bonds, neutral C10H15NO6 and one
    six-carbon ring. All ten comparison flags agree, including both canonical SMILES
    strings, and the limited chirality-aware map contains all 17 atom indices. The
    diagnostic nevertheless explicitly leaves full_graph_identity_established false;
    this is not experimental identity or pathway validation. Both canonical SMILES
    comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established
    remains false.
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: support-2797-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed/atoms; /records/6/smiles/computed/potential_stereo;
    /records/6/smiles/computed/bonds; /records/6/inchi/computed/atoms; /records/6/inchi/computed/potential_stereo;
    /records/6/inchi/computed/bonds
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: One specified S tetrahedral centre and no unspecified potential tetrahedral
    or double-bond candidate are recorded in either form. The source atom-stereo flag
    and complete limited map do not establish natural absolute stereochemistry or
    independent full graph identity.
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: support-2797-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-DATA-001.json
  locator: /records/6/smiles/computed/motifs; /records/6/smiles/computed/rings; /records/6/smiles/computed/bonds;
    /records/6/smiles/computed/atoms; /records/6/inchi/computed/motifs; /records/6/inchi/computed/rings;
    /records/6/inchi/computed/bonds; /records/6/inchi/computed/atoms
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The ring contains a ketone and an unsaturated amino/methoxy-substituted
    segment; the substituent carries a carboxylic acid and a secondary amino linkage.
    The saved ketone is S1=O0/I6=O12 and the carboxyl carbon S8/I7. The methoxy bridge
    S3/I16 is not a sugar linkage. Strict amide, ester, nonamide primary-amine and
    saturated C5O-ring predicates are empty. The sole configured centre is S12/I9,
    both S.
  snapshot_sha256: c1725a2a201004679fb5a6b60a3124217de57850698749040b40e46d316502d8
- evidence_id: support-2797-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-molecular-intake-reading-001.json
  locator: /records/1; /counts; /warnings
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete ten saved forms personally read; no molecular replay. Four original
    undefined-stereo warning lines and two proton-addition/removal warning lines remain
    globally unassigned; none is assigned to an individual owner.
  snapshot_sha256: f5ca966135e76b0744ac3f920329e18329eb3fa3c4b384b3606068946a6ac3aa
- evidence_id: support-2797-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Single original diagnostic command and retained streams; no replay.
  snapshot_sha256: fe6b12cc17cb942787983efb14216babe8b2ee52b81adaca8ffaed0d29142fd6
- evidence_id: support-2797-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/root-current280-diagnostic-acceptance-001.json
  locator: /status; /accepted; /diagnostic; /execution
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted the original stored-form diagnostic.
  snapshot_sha256: 409fc03abfaba0325bf25149704a554a7c7d5fc80f2dd056cca027cd008797c5
- evidence_id: support-2797-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/chemistry-local/diagnostic-original-001.stderr
  locator: complete six original warning lines
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Four original undefined-stereo warning lines and two proton-addition/removal
    warning lines remain globally unassigned; none is assigned to an individual owner.
  snapshot_sha256: f6a74ef31a1d327a6a483c87de5d2671dedd256b334e08156260de25ee0a95be
- evidence_id: support-2797-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-cached-taxonomy-reading-001.json
  locator: /context_interpretations/13; /physical_negative_query_scopes/13; /whole_stanzas
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The source producer Trichormus variabilis ATCC 29413 (240292), BGC0000427:3/CP000117.1,
    remains separate from three Chlorogloeopsis (1123) LOTUS occurrences and CyanoMetDB
    Chlorogloeopsis sp. (28069), literal PCC 6912 context. Cached historical names
    do not equate those strains. Preserving downstream step 4 is not an adjudication
    of pathway-owner semantics.
  snapshot_sha256: 7b3133d38f9f774b7be03c70880701cccf97fa8b6968bb2278462c34f3c47fe0
- evidence_id: support-2797-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-implemented-curation-scan-002.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: No current exact applicable maintained correction; lexical names and unrelated
    BGC rows do not transfer decisions.
  snapshot_sha256: 6ad28a5dd301fac51ee52e70ca0789cd040a1906660932acedd202703d786e11
  search_scope: Native complete nine-table/3422-row bounded scan, exact owner/full-key/BGC/occurrence/assay
    predicates; no new query or universal absence.
- evidence_id: support-2797-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete method grading table
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Producer evidence and locus methods answer different questions; unstated
    methods retain their grade.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2797-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 165-172, atom-centre completeness predicate
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Retained stereo_complete checks unassigned atom centres, not all geometry
    or natural identity.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2797-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306, choose_pathway
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: One supported normalized pathway selects filing; multiple, none or unsupported
    values retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2797-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /selected_queue_rows;
    /selected_queue_counts/2797; /unavailable_required_gates
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Five local gates pass, with required QC/OAK unavailable. Actual queue entries
    are diagnostic leads, not automatic scientific findings.
  snapshot_sha256: 7e6f44be6a38a56ec60db94569abcb6d4b76d33133e329930db626e8bbb3f0b8
- evidence_id: support-2797-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280/owner-capture-DATA-001.json
  locator: /records/6/owner_document/curation_history; /records/6/owner_document/source_concepts
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: 'The owner has two seeding events and one deliberate 2026-10-23 downstream-curation
    event. The step and each of three graph edges retain DOI:10.1126/science.1193637,
    a BGC0000427.5 URL and UniProtKB:Q3M6C6 attribution: 12 placements of three repeated
    references, not 12 independent studies. The source PMID and stored DOI are not
    treated as independently verified publications. Primary-experiment labels, HPLC
    claims, exact protein identity and strain equivalences remain historical attributed
    assertions.'
  snapshot_sha256: 1977ebb464dbe0b842f442a47d5cb3c78fb1d147b3c73b041e6edad6465bc2a8
- evidence_id: support-2797-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-target-input-plan-001.json
  locator: /records/6/complete_root_keys; /records/6/declared_mechanism_roots_literal;
    /records/6/component_paths; /records/6/complete_raw_mechanism_sections
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The accepted complete view preserves one BIOSYNTHESIS graph with four nodes
    and three edges, one step numbered 4 with proposed absent, three histories, and
    no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates;
    Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product.
    The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No
    renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis
    is inferred.
  snapshot_sha256: d6777f8dea91c7542347ffaf26f8bc8cc03d93b08032d32861abac52335c3fa3
- evidence_id: support-2797-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved mibig_compounds frame with 1 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 590, raw UTF-8 row SHA-256 e3c09a2334a41ff210c268dbe7418bd91c0cd8fe0f6bb5959c1731976588ea0c
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The exact XZQILKYKJYHEHD-JTQLQIEISA-N grouping is BGC0000427 version 5,
    compound index 3, naturalproductmech:mibig-00a364fe41. The explicit Shinorine
    and 4-deoxygadusol companions remain distinct owners, not alternate structures
    or merged identities. Trichormus variabilis ATCC 29413 (240292) remains SOURCE_ASSERTION.
    Enzymatic assays and heterologous expression grade the BGC link, not the producer
    claim. Chlorogloeopsis occurrences are separate roles and strains. BGC0000427
    version 5, CP000117.1:4798900-4805360, retains active/questionable/complete metadata
    and CLUSTER_DEMONSTRATED with Enzymatic assays and Heterologous expression. ENTRY
    PMID:20813918 is not newly read compound-specific primary proof.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2797-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved chebi_structures frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved lotus_occurrences frame with 3 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 9720, raw UTF-8 row SHA-256 0696ac49968f3f7192c579b9590ea7d47e95d1a806ad34e0332433c2f75ebe45;
    physical line 9721, raw UTF-8 row SHA-256 ab229854d291fe61a8918c115ef83382d1f5649e1839ea5b90eef751b4955070;
    physical line 9722, raw UTF-8 row SHA-256 fa803cd1cdf67953c3b529d171028637d02b86128e42e8c52c1a5976c51bda7b
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759,
    DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately
    names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used
    yes and PMID:26286672. These records do not establish equivalence to the MIBiG
    strain or publication independence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2797-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved cyanometdb_occurrences frame with 1 positive placements
    read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-table-cyanometdb_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/cyanometdb_occurrences.tsv
  locator: physical line 90, raw UTF-8 row SHA-256 fe6d73a49b91dad410b8106ba6c0c7c28b1e1f1ab4c90fca2d160a754ebb9b98
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759,
    DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately
    names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used
    yes and PMID:26286672. These records do not establish equivalence to the MIBiG
    strain or publication independence.
  snapshot_sha256: f81900edaaaceb1472c0d8100a17b6ca51ccd0c913e4f0aebf24b010b7bb92b8
- evidence_id: support-2797-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved npclassifier frame with 1 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 2872, raw UTF-8 row SHA-256 7f97193be5da2a9691ef8b5bfb57db40af9ef7aa944c54cdde3ccff8a43b2f69
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Mycosporine derivatives and Mycosporine and Mycosporine-like amino acids
    are retained model labels, consistent with a qualified amino-substituted cyclohexenone
    description. The model has Amino acids and Peptides plus Shikimates and Phenylpropanoids,
    so choose_pathway retains UNCLASSIFIED. Molecular agreement does not adjudicate
    pathway field ownership.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2797-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved pubchem_bioassay frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved bindingdb_targets frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved antibioticmech_inchikeys frame with 0 positive placements
    read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact complete standard_inchi_key equality
    and query "XZQILKYKJYHEHD-JTQLQIEISA-N" only; no source replay or universal absence.
- evidence_id: support-2797-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/bgc-prep/bgc-conditional280-source-inventory-DATA-001.json
  locator: /contexts/13/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Complete saved chebi_origins frame with 0 positive placements read.
  snapshot_sha256: 85f8198e450e78a14d329a5da9d9d83f0a5490042af3e0e407fedbed9bb0912b
  search_scope: Retained uncapped predicate exact chebi_id from exact full-key structure
    rows and query [] only; no source replay or universal absence.
- evidence_id: support-2797-reader-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-mycosporine-glycine-maintained-reader-DATA-001.json
  locator: /raw_owner; /resolved_view; /expected_view; /counts; /reader_call_count;
    /denials; /unexpected_denials; /errors
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: The accepted complete view preserves one BIOSYNTHESIS graph with four nodes
    and three edges, one step numbered 4 with proposed absent, three histories, and
    no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates;
    Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product.
    The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No
    renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis
    is inferred. Whole returned owner equals accepted capture; no primary or scientific
    validation follows.
  snapshot_sha256: 84f8bbd254631c3b416a17740428b8338d9fc40e52af0e49ad40cf1c76759a07
- evidence_id: support-2797-reader-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/native-current280-mycosporine-glycine-reader-execution-001.json
  locator: /command; /exit_code; /stdout; /stderr; /retries
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: One original offline maintained call, zero exit and stderr; known socket
    construction denied before action, no requests.
  snapshot_sha256: 9b5797ac833525b96c439c8c719ea56656a2fc1eedb8265be06788c8c3b7ef94
- evidence_id: support-2797-reader-accept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280/root-current280-mycosporine-glycine-reader-acceptance-001.json
  locator: /status; /accepted; /DATA; /execution; /review_check_contract; /limits
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: ROOT accepted the complete returned owner and exact check contract; interpretation
    remains separate.
  snapshot_sha256: b710e8498a1ce49886b7c5ec8ce0ee6d6b3505ce9a1c4fc905fb384b1773b6d7
- evidence_id: support-2797-reader-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-last-five-maintained-reader-reading-001.json
  locator: /records/0
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: review_support read every returned owner, graph, node, edge, evidence,
    pathway and history value.
  snapshot_sha256: 3fa3bc413bd887941dbb4e55bd97ee4600bee153f430a46fb015b886843cf832
- evidence_id: support-2797-placement
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/support-prep/support-current280-2797-pathway-placement-assessment-001.json
  locator: /conclusion; /reconciliation; /retained_schema_and_consumer_excerpts; /complete_actual_reader;
    /prior_bounded_ignored_inclusive_search
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: PathwayStep is defined as an enzymatic step in biosynthesis of this compound.
    Intermediate steps need not individually produce the owner, but this sole terminal
    step explicitly consumes the owner and produces a different compound. Its full
    step block is already present in the Shinorine product owner. Deliberate downstream
    history and the broader causal-graph definition are material competing context,
    yet do not provide an explicit exception for the narrower field. The current queue
    omits this owner from biosynthesis despite one demonstrated locus because the
    field is nonempty; the renderer labels it curated Biosynthesis. These are material
    scope/representation consequences. The clearly directed downstream graph may remain
    as qualified context; the finding concerns pathway placement, not asserted enzyme
    chemistry or a blanket rejection of that graph. The policy interpretation remains
    provisional pending curator resolution.
  snapshot_sha256: 94fc5c0f08e582989cff9c8974fe129289999cb5582397295b833e04167aeaa2
- evidence_id: support-2797-native-semantic
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-current280-2797-pathway-owner-independent-semantic-reading-001.json
  locator: /conclusion; /normative_reasoning; /competing_context_and_limits; /provisional_finding;
    /bounded_curator_action
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Native independently reaches the same provisional major owner-scope concern;
    review_support independently read the underlying excerpts and actual returned
    owner.
  snapshot_sha256: 358f9ca5d24837d35dc03905dfdf70b14fbd35e3154ca1f704055e32ec356faa
- evidence_id: support-2797-semantic-schema_parent
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 259-270
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2797-semantic-schema_step
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 593-625
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: PathwayStep describes biosynthesis of this compound.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2797-semantic-schema_graph_scope
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 1137-1142
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2797-semantic-owner_step
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/mycosporine-glycine.yaml
  locator: lines 113-144
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: a633697a3f5f44f2947951f4f17e934a3812cc63c602d40540468d63104b64b0
- evidence_id: support-2797-semantic-owner_history
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/mycosporine-glycine.yaml
  locator: lines 250-266
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: a633697a3f5f44f2947951f4f17e934a3812cc63c602d40540468d63104b64b0
- evidence_id: support-2797-semantic-counterpart_step
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/shinorine.yaml
  locator: lines 146-177
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: eb3991e3cea604c58583a38d6ba53538302bce8c9329b229957f83d3989ff582
- evidence_id: support-2797-semantic-counterpart_history
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/shinorine.yaml
  locator: lines 283-297
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: eb3991e3cea604c58583a38d6ba53538302bce8c9329b229957f83d3989ff582
- evidence_id: support-2797-semantic-queue_consumer
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/curation_worklist.py
  locator: lines 175-192
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Nonempty pathway bypasses the biosynthesis queue before locus grading.
  snapshot_sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
- evidence_id: support-2797-semantic-queue_test
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/tests/test_curation_worklist.py
  locator: lines 57-75
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: fd6171c4533ef20b8cffc1f73d57fd081e32060ca672ab647c7034e4394984f6
- evidence_id: support-2797-semantic-render_steps
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/render_pages.py
  locator: lines 208-215
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: e3dc205d44111813cc02439caff895e30e8c06756d74a7675acbe15d84cf14ab
- evidence_id: support-2797-semantic-render_template
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/templates/record.html
  locator: lines 109-128
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Populated pathway is presented as curated Biosynthesis.
  snapshot_sha256: 4c5143ae98b51531c3b708cf73590decd50f3e222e375d91288a54ef767e7893
- evidence_id: support-2797-semantic-review_owner_boundary
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: lines 35-56
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Exact current retained owner-policy/consumer excerpt; endpoint direction
    and deliberate historical scope are preserved.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2797-semantic-search
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch280-tentative/native-prep/native-conditional280-pathway-owner-semantics-001.json
  locator: /search_scope
  accessed_at: '2026-11-07T00:35:30.465187Z'
  support: supports
  summary: Native bounded maintained-text search found no explicit downstream-owner
    exception; scope is not universal.
  snapshot_sha256: 9d142ed1130e08c15926e620111e0d71cb393397ba4db91955ed3773c3487488
  search_scope: Ignored and hidden files included in named maintained roots; exact
    two recorded regexes, textual search only; no fresh search or external lookup.
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:58:35.720629Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 11c07976d94801b8044a911f854cef59d220d80dafabd86673396f6a1ee54ae4
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:58:59.871180Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 54b4e29921ed94b48337f9938b95ac8c403d840bd704ec9c7c3c6fe215016937
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:59:19.061941Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-06T23:59:52.340365Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-280/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-280/native-current280-five-gates-execution-001.json
  accessed_at: '2026-11-07T00:00:03.873381Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: b0c41dbce9d0cef868a144aadc058261eb329ecea06a3affb0e50465adf478e0
assessments:
- assessment_id: support-2797-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: The exact XZQILKYKJYHEHD-JTQLQIEISA-N grouping is BGC0000427 version 5,
    compound index 3, naturalproductmech:mibig-00a364fe41. The explicit Shinorine
    and 4-deoxygadusol companions remain distinct owners, not alternate structures
    or merged identities.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-owner
  - support-2797-capture
  - support-2797-source
  - support-2797-intake
  - support-2797-curation
  - support-2797-table-mibig_compounds
  - support-2797-table-lotus_occurrences
  - support-2797-table-cyanometdb_occurrences
  - support-2797-table-npclassifier
  dimensions:
  - name: standard_inchi_key
    definition: Full key rather than label matching.
    value: XZQILKYKJYHEHD-JTQLQIEISA-N
    evidence_ids:
    - support-2797-owner
    - support-2797-capture
    - support-2797-source
    - support-2797-intake
    - support-2797-curation
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
  - name: grounding_scope
    definition: Retained source identity is distinct from natural identity.
    value: The exact XZQILKYKJYHEHD-JTQLQIEISA-N grouping is BGC0000427 version 5,
      compound index 3, naturalproductmech:mibig-00a364fe41. The explicit Shinorine
      and 4-deoxygadusol companions remain distinct owners, not alternate structures
      or merged identities.
    evidence_ids:
    - support-2797-owner
    - support-2797-capture
    - support-2797-source
    - support-2797-intake
    - support-2797-curation
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
- assessment_id: support-2797-representation-assessment
  area: representation
  topic: Saved molecular forms and stereochemical scope
  summary: Both saved forms contain 17 atoms, 17 bonds, neutral C10H15NO6 and one
    six-carbon ring. All ten comparison flags agree, including both canonical SMILES
    strings, and the limited chirality-aware map contains all 17 atom indices. The
    diagnostic nevertheless explicitly leaves full_graph_identity_established false;
    this is not experimental identity or pathway validation. The ring contains a ketone
    and an unsaturated amino/methoxy-substituted segment; the substituent carries
    a carboxylic acid and a secondary amino linkage. The saved ketone is S1=O0/I6=O12
    and the carboxyl carbon S8/I7. The methoxy bridge S3/I16 is not a sugar linkage.
    Strict amide, ester, nonamide primary-amine and saturated C5O-ring predicates
    are empty. The sole configured centre is S12/I9, both S. Both canonical SMILES
    comparisons agree and the limited 17-atom map is complete, while full_graph_identity_established
    remains false. Normalized key/formula agreement and a successful local process
    do not establish independent full graph identity, natural-sample identity, experimental
    absolute stereochemistry, primary mechanism validation or a native status promotion.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-data
  - support-2797-stereo
  - support-2797-motifs
  - support-2797-molecularreading
  - support-2797-execution
  - support-2797-diagaccept
  - support-2797-stereopolicy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified atom centres and representation-dependent candidates remain
      distinct.
    value: One specified S tetrahedral centre and no unspecified potential tetrahedral
      or double-bond candidate are recorded in either form. The source atom-stereo
      flag and complete limited map do not establish natural absolute stereochemistry
      or independent full graph identity.
    evidence_ids:
    - support-2797-data
    - support-2797-stereo
    - support-2797-motifs
    - support-2797-molecularreading
    - support-2797-execution
    - support-2797-diagaccept
    - support-2797-stereopolicy
  - name: representation_correspondence
    definition: Saved limited comparison, not full identity.
    value: Both canonical SMILES comparisons agree and the limited 17-atom map is
      complete, while full_graph_identity_established remains false. Normalized key/formula
      agreement and a successful local process do not establish independent full graph
      identity, natural-sample identity, experimental absolute stereochemistry, primary
      mechanism validation or a native status promotion.
    evidence_ids:
    - support-2797-data
    - support-2797-stereo
    - support-2797-motifs
    - support-2797-molecularreading
    - support-2797-execution
    - support-2797-diagaccept
    - support-2797-stereopolicy
- assessment_id: support-2797-provenance-assessment
  area: provenance
  topic: Compound-specific producer, locus and taxon
  summary: Trichormus variabilis ATCC 29413 (240292) remains SOURCE_ASSERTION. Enzymatic
    assays and heterologous expression grade the BGC link, not the producer claim.
    Chlorogloeopsis occurrences are separate roles and strains. BGC0000427 version
    5, CP000117.1:4798900-4805360, retains active/questionable/complete metadata and
    CLUSTER_DEMONSTRATED with Enzymatic assays and Heterologous expression. ENTRY
    PMID:20813918 is not newly read compound-specific primary proof.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-source
  - support-2797-capture
  - support-2797-taxonomy
  - support-2797-curation
  - support-2797-producerpolicy
  - support-2797-table-mibig_compounds
  - support-2797-table-lotus_occurrences
  - support-2797-table-cyanometdb_occurrences
  - support-2797-table-npclassifier
  dimensions:
  - name: taxon_scope
    definition: Cached names do not establish current lineage or strain equivalence.
    value: The source producer Trichormus variabilis ATCC 29413 (240292), BGC0000427:3/CP000117.1,
      remains separate from three Chlorogloeopsis (1123) LOTUS occurrences and CyanoMetDB
      Chlorogloeopsis sp. (28069), literal PCC 6912 context. Cached historical names
      do not equate those strains. Preserving downstream step 4 is not an adjudication
      of pathway-owner semantics.
    evidence_ids:
    - support-2797-source
    - support-2797-capture
    - support-2797-taxonomy
    - support-2797-curation
    - support-2797-producerpolicy
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
  - name: producer_evidence
    definition: Producer and locus evidence remain separate.
    value: Trichormus variabilis ATCC 29413 (240292) remains SOURCE_ASSERTION. Enzymatic
      assays and heterologous expression grade the BGC link, not the producer claim.
      Chlorogloeopsis occurrences are separate roles and strains.
    evidence_ids:
    - support-2797-source
    - support-2797-capture
    - support-2797-taxonomy
    - support-2797-curation
    - support-2797-producerpolicy
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
  - name: locus_evidence
    definition: Exact source version, endpoints and methods delimit the claim.
    value: BGC0000427 version 5, CP000117.1:4798900-4805360, retains active/questionable/complete
      metadata and CLUSTER_DEMONSTRATED with Enzymatic assays and Heterologous expression.
      ENTRY PMID:20813918 is not newly read compound-specific primary proof.
    evidence_ids:
    - support-2797-source
    - support-2797-capture
    - support-2797-taxonomy
    - support-2797-curation
    - support-2797-producerpolicy
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
- assessment_id: support-2797-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: 'The owner has two seeding events and one deliberate 2026-10-23 downstream-curation
    event. The step and each of three graph edges retain DOI:10.1126/science.1193637,
    a BGC0000427.5 URL and UniProtKB:Q3M6C6 attribution: 12 placements of three repeated
    references, not 12 independent studies. The source PMID and stored DOI are not
    treated as independently verified publications. Primary-experiment labels, HPLC
    claims, exact protein identity and strain equivalences remain historical attributed
    assertions.'
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-owner
  - support-2797-source
  - support-2797-capture
  - support-2797-history
  - support-2797-table-mibig_compounds
  - support-2797-table-lotus_occurrences
  - support-2797-table-cyanometdb_occurrences
  - support-2797-table-npclassifier
  dimensions:
  - name: citation_scope
    definition: Repeated annotations are not independent primary proof.
    value: 'The owner has two seeding events and one deliberate 2026-10-23 downstream-curation
      event. The step and each of three graph edges retain DOI:10.1126/science.1193637,
      a BGC0000427.5 URL and UniProtKB:Q3M6C6 attribution: 12 placements of three
      repeated references, not 12 independent studies. The source PMID and stored
      DOI are not treated as independently verified publications. Primary-experiment
      labels, HPLC claims, exact protein identity and strain equivalences remain historical
      attributed assertions.'
    evidence_ids:
    - support-2797-owner
    - support-2797-source
    - support-2797-capture
    - support-2797-history
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
- assessment_id: support-2797-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay limits
  summary: Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759,
    DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately
    names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used
    yes and PMID:26286672. These records do not establish equivalence to the MIBiG
    strain or publication independence. Saved PubChem, BindingDB and AntibioticMech
    exact-key frames are negative. The retained enzyme-coupling annotation is biosynthetic
    context, not a measured compound potency or molecular-target assertion. No inactivity
    or universal assay absence is inferred.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-source
  - support-2797-taxonomy
  - support-2797-curation
  - support-2797-query-mibig_compounds
  - support-2797-query-chebi_structures
  - support-2797-query-lotus_occurrences
  - support-2797-query-cyanometdb_occurrences
  - support-2797-query-npclassifier
  - support-2797-query-pubchem_bioassay
  - support-2797-query-bindingdb_targets
  - support-2797-query-antibioticmech_inchikeys
  - support-2797-query-chebi_origins
  dimensions:
  - name: occurrence_scope
    definition: Occurrence does not establish production.
    value: Three LOTUS occurrences name Chlorogloeopsis (1123) with DOI:10.1007/S002030050759,
      DOI:10.1016/S0742-8413(96)00135-1 and DOI:10.1021/JO00117A008. CyanoMetDB separately
      names Chlorogloeopsis sp. (28069), literal [Chlorogloeopsis sp.]PCC 6912, nmr_used
      yes and PMID:26286672. These records do not establish equivalence to the MIBiG
      strain or publication independence.
    evidence_ids:
    - support-2797-source
    - support-2797-taxonomy
    - support-2797-curation
    - support-2797-query-mibig_compounds
    - support-2797-query-chebi_structures
    - support-2797-query-lotus_occurrences
    - support-2797-query-cyanometdb_occurrences
    - support-2797-query-npclassifier
    - support-2797-query-pubchem_bioassay
    - support-2797-query-bindingdb_targets
    - support-2797-query-antibioticmech_inchikeys
    - support-2797-query-chebi_origins
  - name: assay_target_scope
    definition: Blank sentinels and bounded negatives are not inactivity.
    value: Saved PubChem, BindingDB and AntibioticMech exact-key frames are negative.
      The retained enzyme-coupling annotation is biosynthetic context, not a measured
      compound potency or molecular-target assertion. No inactivity or universal assay
      absence is inferred.
    evidence_ids:
    - support-2797-source
    - support-2797-taxonomy
    - support-2797-curation
    - support-2797-query-mibig_compounds
    - support-2797-query-chebi_structures
    - support-2797-query-lotus_occurrences
    - support-2797-query-cyanometdb_occurrences
    - support-2797-query-npclassifier
    - support-2797-query-pubchem_bioassay
    - support-2797-query-bindingdb_targets
    - support-2797-query-antibioticmech_inchikeys
    - support-2797-query-chebi_origins
- assessment_id: support-2797-classification-assessment
  area: consistency
  topic: Source classes, model labels and filing
  summary: Mycosporine derivatives and Mycosporine and Mycosporine-like amino acids
    are retained model labels, consistent with a qualified amino-substituted cyclohexenone
    description. The model has Amino acids and Peptides plus Shikimates and Phenylpropanoids,
    so choose_pathway retains UNCLASSIFIED. Molecular agreement does not adjudicate
    pathway field ownership.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-source
  - support-2797-owner
  - support-2797-motifs
  - support-2797-filingpolicy
  - support-2797-gates
  - support-2797-table-mibig_compounds
  - support-2797-table-lotus_occurrences
  - support-2797-table-cyanometdb_occurrences
  - support-2797-table-npclassifier
  dimensions:
  - name: classification_applicability
    definition: Model, source and saved topology are separate evidence.
    value: Mycosporine derivatives and Mycosporine and Mycosporine-like amino acids
      are retained model labels, consistent with a qualified amino-substituted cyclohexenone
      description. The model has Amino acids and Peptides plus Shikimates and Phenylpropanoids,
      so choose_pathway retains UNCLASSIFIED. Molecular agreement does not adjudicate
      pathway field ownership.
    evidence_ids:
    - support-2797-source
    - support-2797-owner
    - support-2797-motifs
    - support-2797-filingpolicy
    - support-2797-gates
    - support-2797-table-mibig_compounds
    - support-2797-table-lotus_occurrences
    - support-2797-table-cyanometdb_occurrences
    - support-2797-table-npclassifier
- assessment_id: support-2797-mechanism-assessment
  area: consistency
  topic: Complete retained mechanism and owner scope
  summary: The accepted complete view preserves one BIOSYNTHESIS graph with four nodes
    and three edges, one step numbered 4 with proposed absent, three histories, and
    no components or targets. Own identifier plus L-serine CHEBI:17115 are substrates;
    Ava_3855 UniProtKB:Q3M6C6 is the enzyme and CHEBI:131712 shinorine is the product.
    The graph clearly labels the owner as PRECURSOR and shinorine as COMPOUND. No
    renumbering, implicit proposed=false, invented Rhea reaction or upstream biosynthesis
    is inferred. PathwayStep is defined as an enzymatic step in biosynthesis of this
    compound. Intermediate steps need not individually produce the owner, but this
    sole terminal step explicitly consumes the owner and produces a different compound.
    Its full step block is already present in the Shinorine product owner. Deliberate
    downstream history and the broader causal-graph definition are material competing
    context, yet do not provide an explicit exception for the narrower field. The
    current queue omits this owner from biosynthesis despite one demonstrated locus
    because the field is nonempty; the renderer labels it curated Biosynthesis. These
    are material scope/representation consequences. The clearly directed downstream
    graph may remain as qualified context; the finding concerns pathway placement,
    not asserted enzyme chemistry or a blanket rejection of that graph. The policy
    interpretation remains provisional pending curator resolution.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-scope
  - support-2797-reader-data
  - support-2797-reader-execution
  - support-2797-reader-accept
  - support-2797-reader-reading
  - support-2797-placement
  - support-2797-native-semantic
  - support-2797-semantic-search
  - support-2797-gates
  - support-2797-semantic-schema_parent
  - support-2797-semantic-schema_step
  - support-2797-semantic-schema_graph_scope
  - support-2797-semantic-owner_step
  - support-2797-semantic-owner_history
  - support-2797-semantic-counterpart_step
  - support-2797-semantic-counterpart_history
  - support-2797-semantic-queue_consumer
  - support-2797-semantic-queue_test
  - support-2797-semantic-render_steps
  - support-2797-semantic-render_template
  - support-2797-semantic-review_owner_boundary
  dimensions: []
- assessment_id: support-2797-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: Complete assigned raw/source/intake and both saved molecular forms were
    read. The required original maintained reader returned the complete owner; preservation
    does not verify mechanism science. The provisional major pathway-owner finding
    remains open. Five local native commands pass; full QC, complete OAK and fresh
    primary verification remain unavailable. Completion is partial, native SEEDED
    status unchanged.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  evidence_ids:
  - support-2797-intake
  - support-2797-intakeaccept
  - support-2797-plan
  - support-2797-planaccept
  - support-2797-notes
  - support-2797-gates
  - support-2797-data
  - support-2797-diagaccept
  - support-2797-scope
  dimensions:
  - name: review_completion
    definition: Local review does not promote native status or substitute for unavailable
      checks.
    value: Complete assigned raw/source/intake and both saved molecular forms were
      read. The required original maintained reader returned the complete owner; preservation
      does not verify mechanism science. The provisional major pathway-owner finding
      remains open. Five local native commands pass; full QC, complete OAK and fresh
      primary verification remain unavailable. Completion is partial, native SEEDED
      status unchanged.
    evidence_ids:
    - support-2797-intake
    - support-2797-intakeaccept
    - support-2797-plan
    - support-2797-planaccept
    - support-2797-notes
    - support-2797-gates
    - support-2797-data
    - support-2797-diagaccept
    - support-2797-scope
findings:
- finding_id: support-2797-downstream-pathway-owner-scope
  issue_key: mycosporine-glycine-downstream-pathway-owner-scope
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Downstream shinorine synthesis occupies the precursor owner biosynthesis
    field
  description: PathwayStep is defined as an enzymatic step in biosynthesis of this
    compound. Intermediate steps need not individually produce the owner, but this
    sole terminal step explicitly consumes the owner and produces a different compound.
    Its full step block is already present in the Shinorine product owner. Deliberate
    downstream history and the broader causal-graph definition are material competing
    context, yet do not provide an explicit exception for the narrower field. The
    current queue omits this owner from biosynthesis despite one demonstrated locus
    because the field is nonempty; the renderer labels it curated Biosynthesis. These
    are material scope/representation consequences. The clearly directed downstream
    graph may remain as qualified context; the finding concerns pathway placement,
    not asserted enzyme chemistry or a blanket rejection of that graph. The policy
    interpretation remains provisional pending curator resolution.
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  field_paths:
  - /biosynthetic_pathway/0
  evidence_ids:
  - support-2797-placement
  - support-2797-native-semantic
  - support-2797-reader-data
  - support-2797-reader-accept
  - support-2797-gates
  - support-2797-semantic-search
  - support-2797-semantic-schema_parent
  - support-2797-semantic-schema_step
  - support-2797-semantic-schema_graph_scope
  - support-2797-semantic-owner_step
  - support-2797-semantic-owner_history
  - support-2797-semantic-counterpart_step
  - support-2797-semantic-counterpart_history
  - support-2797-semantic-queue_consumer
  - support-2797-semantic-queue_test
  - support-2797-semantic-render_steps
  - support-2797-semantic-render_template
  - support-2797-semantic-review_owner_boundary
  ownership_note: This is a curator-owned pathway annotation in the selected YAML.
    The downstream graph and historical evidence are explicit competing context; generated
    source facts and pages are not the repair owner.
actions:
- action_id: support-2797-resolve-pathway-owner-placement
  description: Use the validated curator-owned record workflow to remove or relocate
    the downstream-only pathway step from the precursor owner, preserving the explicitly
    directed downstream graph, evidence and append-only history. The identical terminal
    step already exists in Shinorine. Alternatively resolve the model ambiguity through
    an explicit maintained schema/documentation/consumer policy change; a note alone
    does not change current queue behavior. Do not invent upstream steps, renumber
    step 4, or add proposed:true as a placement fix.
  finding_ids:
  - support-2797-downstream-pathway-owner-scope
  target_ids:
  - naturalproductmech:mibig-00a364fe41
  ownership_note: Proposed curator-owned correction or explicit maintained policy
    resolution only; no YAML, schema, source, renderer or campaign edit is performed
    here.
  acceptance_checks:
  - The selected owner no longer represents a different product terminal step as its
    own biosynthesis unless a documented maintained policy explicitly authorizes it.
  - Preserve chemical structures, producer/locus grades, downstream direction, evidence,
    graph qualifiers and all existing history; append a new curation event for a future
    edit.
  - Avoid duplicating the existing Shinorine annotation or inventing unverified upstream
    chemistry.
  - In a separately authorized correction workflow, validate through the maintained
    writer and verify queue/render/reproduction behavior with focused regressions.
limitations:
- Normalized key/formula agreement and a successful local process do not establish
  independent full graph identity, natural-sample identity, experimental absolute
  stereochemistry, primary mechanism validation or a native status promotion.
- Both canonical SMILES comparisons agree and the limited 17-atom map is complete,
  while full_graph_identity_established remains false. One specified S tetrahedral
  centre and no unspecified potential tetrahedral or double-bond candidate are recorded
  in either form. The source atom-stereo flag and complete limited map do not establish
  natural absolute stereochemistry or independent full graph identity.
- Four original undefined-stereo warning lines and two proton-addition/removal warning
  lines remain globally unassigned; none is assigned to an individual owner.
- Primary publications, spectra, sequences, live taxonomy, full QC and complete OAK
  remain unavailable; source/database claims retain their exact authority.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh current 280 evidence and judgments; prior batches provide interface logic
  only.
- No source row, record, campaign or native status was changed; no query, molecular
  parse, target invocation or outbound request occurred in this lane.
- ROOT appends five actual native checks and three required unavailable checks; only
  orders 2797 and 2798 in this fragment receive actual maintained-reader checks.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-280
```
