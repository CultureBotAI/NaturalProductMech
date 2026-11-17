# Local evidence review: penitrem A

- Review: 20261107T092129Z-penitrem-a
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-07T08:46:40.707055Z
- Finished UTC: 2026-11-07T09:21:29.979955Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Penitrem A has consistent saved molecular forms and thirteen specified atom centres. Its retained assay observations remain useful source evidence, but the generated ENZYME_INHIBITOR classification overstates at least the Lassa-virus binding/entry assay. This confirmed local classification issue is major and open; the partial review requires curation.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2870; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-5942c19a89 | data/natural_products/unclassified/penitrem-a.yaml | generated | penitrem A |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-5942c19a89 | Both stored forms parsed with declared key/formula agreement. Both canonical SMILES comparisons are true and the saved chirality-aware map covers all atoms, but it is one limited substructure comparison. In every case full_graph_identity_established remains false. |
| strict_ten | passed | True | naturalproductmech:mibig-5942c19a89 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-5942c19a89 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-5942c19a89 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-5942c19a89 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-5942c19a89 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-5942c19a89 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-5942c19a89 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-5942c19a89 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact retained compound grounding

identity: supported. Targets: naturalproductmech:mibig-5942c19a89.

BGC0001375 version 4 compound index 1 grounds penitrem A, full key JDUWHZOLEDOQSR-JKPSMKLGSA-N and PubChem CID 6610243. The complete key/CID joins source assays; label similarity does not transfer companion results.

### Saved forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-5942c19a89.

Both saved forms are neutral C37H44ClNO6 with 45 atoms and 54 bonds. Ten ring rows agree with independent cycle rank ten. The polycyclic indole-containing scaffold, chlorine, epoxide, four-membered carbocycle, two terminal methylenes, three alcohols and three ether oxygens persist. No carbonyl, strict amide, ester or imidic motif is present. The epoxide is SMILES C5-C6-O7 and InChI C30-C36-O44. The four-membered carbocycle is source C23-C24-C25-C26 and InChI C12-C21-C35-C18. Terminal methylenes are source C1=C2 and C34=C35, retained as InChI C14=C0 and C15=C2. The saturated C5O predicate finds an embedded scaffold ring, not an assigned sugar; it does not contradict the nonglycoside model flag. No metal, phosphorus or free primary amine is present. Both canonical SMILES comparisons are true and the saved chirality-aware map covers all atoms, but it is one limited substructure comparison. In every case full_graph_identity_established remains false. Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.

### Producer, locus and taxon claim grain

provenance: supported. Targets: naturalproductmech:mibig-5942c19a89.

Penicillium simplicissimum NCBITaxon:69488 remains SOURCE_ASSERTION. A matching occurrence is not independent causal producer evidence. BGC0001375 is active with questionable quality and unknown completeness. LC027937.1 and TERPENE/Unknown are retained, but blank locus bounds/methods leave CLUSTER_UNSTATED. No graph, pathway or complete enzyme sequence is supplied.

### Citation grain and retained history

evidence: supported. Targets: naturalproductmech:mibig-5942c19a89.

DOI:10.1021/jf020983e has COMPOUND_BIOACTIVITY scope, not causal-production or route scope. The 22 LOTUS rows retain individual DOI/Wikidata pointers; five seed histories do not add independent experiments. Assay metadata has its own source provenance and does not establish primary sample verification.

### Occurrence and assay boundaries

evidence: concern. Targets: naturalproductmech:mibig-5942c19a89.

LOTUS physical rows 2977-2998 retain 22 occurrence assertions across twelve taxon IDs. Penicillium 5073 is genus-only; Mucor irregularis 1290454 has cached label Mucor irregularis B50 without a synonym proving strain equivalence. Penicillium janthinellum 5079 and P. ianthinellum 545233 remain distinct IDs. Row multiplicity and matching producer taxon do not establish publication independence. The 22 retained PubChem rows represent eighteen unique AIDs, with paired target-presence variants for 1645877, 1645876, 1963824 and 1963823. Four source Active calls remain ACTIVE; eighteen Inconclusive calls remain NOT_DETERMINED, not inactive. The active thiol-reactivity artifact screen 1845221 has no activity class. Generic Potency values remain OTHER, not IC50/EC50; AID 2330 has no numeric endpoint. Target accession shape is not protein grounding. AID 720533 describes viral binding/entry, so its generated ENZYME_INHIBITOR assertion is unsupported by that retained evidence. Cellular TDP1 AID 686978 and STK33 AID 2330 titles also do not independently establish direct biochemical inhibition. Preserve calls, measurements and target variants while correcting or qualifying class inference.

### Source/model classes and generated activity classification

consistency: concern. Targets: naturalproductmech:mibig-5942c19a89.

NPClassifier retains Alkaloids plus Terpenoids, Tryptophan alkaloids and Indole-Diterpenoid alkaloids (Penitrems), is_glycoside:false and date 2026-09-07. These chemical-model labels are distinct from the generated bioactivity_summary ENZYME_INHIBITOR. The maintained generic inhibition/binding fallback makes an overbroad mechanistic assertion for the Lassa binding/entry observation and propagates it to the summary; this requires curation. No finding asserts that all retained effects are false or that Penitrem A never inhibits an enzyme.

### Earned work and unavailable authority

completeness: concern. Targets: naturalproductmech:mibig-5942c19a89.

The complete owner, assigned source payloads, original intake and both saved forms were read. The complete owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets or components; no maintained reader applies. It retains 22 bioactivity observations and a generated activity summary, which are assessed separately. The separate Paxilline reader supplies no authority for this owner. One major open classification finding requires maintained-source curation. Five local gates pass; full QC, complete OAK and fresh primary/external verification are unavailable. Completion is partial and native SEEDED status is unchanged.

## Findings

### support-2870-assay-classification: Generic assay-title inference overstates enzyme inhibition

major / open / confirmed; issue key: penitrem-a-generic-inhibition-classification.

AID 720533 is a retained active Lassa-virus binding/entry assay, but bioactivities[17].activity_class asserts ENZYME_INHIBITOR without an enzyme endpoint or grounded target. The maintained fallback classifies generic inhibition/binding wording and propagates active classes into bioactivity_summary, despite its own unambiguous-evidence policy. Cellular TDP1 AID 686978 and STK33 AID 2330 likewise require evidence-specific class review rather than a title-only direct biochemical mechanism. The confirmed defect is the local class inference, not the truth of source activity calls or a claim that Penitrem A never inhibits enzymes. Preserve all 22 observations, target variants, measurements and source provenance.

## Recommended Actions And Acceptance Checks

### support-2870-correct-class-inference

Replace generic inhibition/binding-title promotion to ENZYME_INHIBITOR with evidence-specific classification in the maintained seeder. Keep valid binding/entry and cellular observations, source calls, Potency/OTHER values, absent numeric endpoints, target-presence variants and artifact-screen context. Leave activity_class unassigned or use an existing evidence-supported enum under policy; do not invent BINDING. Recompute the generated summary through the maintained regeneration workflow after curator review.

- AID 720533 no longer asserts ENZYME_INHIBITOR solely from its viral binding/entry title; any retained class has appropriate evidence.
- AIDs 686978 and 2330 receive explicit evidence-scoped review without treating cellular titles alone as direct biochemical inhibition.
- All 22 source observations and 18 unique AIDs remain attributable; four duplicated-AID target variants are not counted as independent assays.
- Four ACTIVE and eighteen NOT_DETERMINED calls remain intact; the reactive-artifact screen is retained with its scope, generic Potency stays OTHER and AID 2330 gains no invented endpoint/value.
- Generated activity summary reflects only justified classes; current schema and canonical review checks pass after authorized regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2870-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-a.yaml; complete file: identity, structures, source concepts, producer/locus/occurrence, activity fields when present and history | supports | Complete current generated owner; source assertions and native SEEDED status preserved. |
| support-2870-capture | /private/tmp/npm-review-work/shared-next-batch287/owner-capture-DATA-001.json; /records/9/owner_document | supports | Original whole owner capture, including all retained histories and source assertions. |
| support-2870-source | /private/tmp/npm-review-work/shared-next-batch287-tentative/support-prep/support-current287-assigned-source-reading-001.json; /contexts/8; /selected_counts; /companion_counts; /global_cautions | supports | Own selected-five reading: 61 row placements, 576 fields, 45 frames, 29 negatives and 17 histories. Separate companion credit is not added to selected primary credit. |
| support-2870-plan | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-target-input-plan-001.json; /records/9; /source_placement_count; /unique_source_path_count | supports | Accepted 488-placement/73-path plan; 49 actual inputs for this owner. |
| support-2870-planaccept | /private/tmp/npm-review-work/shared-next-batch287/root-current287-source-plan-acceptance-001.json; /accepted; /plan; /status | supports | ROOT accepted the original current plan. |
| support-2870-notes | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /curation | supports | Disjoint BGC 44 plus Support 124 row placements total 168 rows and 1551 fields across 21 contexts. Native taxonomy/curation adds no primary-row credit. |
| support-2870-intake | /private/tmp/npm-review-work/shared-next-batch287/intakes-001/2870-inspect-001.json; /status; /source; /targets | supports | Original intake fixes current hashes and exact maintained owner roles. |
| support-2870-intakeaccept | /private/tmp/npm-review-work/shared-next-batch287/root-current287-intake-acceptance-001.json; /accepted; /status; /intake_summary; /records | supports | Ten original intakes passed with exact current input maps. |
| support-2870-data | /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence; /records/9/literal_InChI_layers; /records/9/formula_comparison_scope | supports | Both saved forms are neutral C37H44ClNO6 with 45 atoms and 54 bonds. Ten ring rows agree with independent cycle rank ten. The polycyclic indole-containing scaffold, chlorine, epoxide, four-membered carbocycle, two terminal methylenes, three alcohols and three ether oxygens persist. No carbonyl, strict amide, ester or imidic motif is present. Both canonical SMILES comparisons are true and the saved chirality-aware map covers all atoms, but it is one limited substructure comparison. In every case full_graph_identity_established remains false. |
| support-2870-stereo | /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/potential_stereo; /records/9/smiles/computed/stereo_counts; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds; /records/9/inchi/computed/potential_stereo; /records/9/inchi/computed/stereo_counts | supports | Both forms retain thirteen specified tetrahedral candidates and no other potential-stereo entry. The two terminal methylenes cannot carry ordinary E/Z assignment. The true source atom-centre flag and canonical agreement do not prove natural absolute stereochemistry or validate activity classification. |
| support-2870-motifs | /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-DATA-001.json; /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/rings; /records/9/smiles/computed/motifs; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds; /records/9/inchi/computed/rings; /records/9/inchi/computed/motifs | supports | The epoxide is SMILES C5-C6-O7 and InChI C30-C36-O44. The four-membered carbocycle is source C23-C24-C25-C26 and InChI C12-C21-C35-C18. Terminal methylenes are source C1=C2 and C34=C35, retained as InChI C14=C0 and C15=C2. The saturated C5O predicate finds an embedded scaffold ring, not an assigned sugar; it does not contradict the nonglycoside model flag. No metal, phosphorus or free primary amine is present. |
| support-2870-molecularreading | /private/tmp/npm-review-work/shared-next-batch287-tentative/support-prep/support-current287-last-five-molecular-intake-reading-001.json; /records/4; /counts; /interpretations/2870; /warnings | supports | All ten saved forms personally read: 444 atoms, 490 bonds, 62 ring rows and 99 potential-stereo entries; no reparse. |
| support-2870-execution | /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /retries; /stderr | supports | One original diagnostic exited zero with no retry. |
| support-2870-diagaccept | /private/tmp/npm-review-work/shared-next-batch287/root-current287-diagnostic-acceptance-001.json; /accepted; /DATA; /execution; /scope | supports | ROOT accepted original technical outputs without a scientific identity claim. |
| support-2870-stderr | /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-original-001.stderr; complete original 368-byte stderr stream | supports | Eight undefined-stereochemistry warning lines occur in the original 368-byte stderr. They are globally unattributed and are not assigned to any owner or form. |
| support-2870-taxonomy | /private/tmp/npm-review-work/shared-next-batch287-tentative/native-prep/native-current287-cached-taxonomy-reading-001.json; /context_interpretations/14; /physical_negative_query_scopes/14; /whole_stanzas | supports | Attributed Native retained-cache reading: NCBITaxon:121612 = Penicillium janczewskii, NCBITaxon:1290454 = Mucor irregularis B50, NCBITaxon:36656 = Penicillium crustosum, NCBITaxon:434487 = Penicillium novae-zeelandiae, NCBITaxon:5073 = Penicillium, NCBITaxon:5079 = Penicillium janthinellum, NCBITaxon:5083 = Penicillium canescens, NCBITaxon:545233 = Penicillium ianthinellum, NCBITaxon:60171 = Penicillium verrucosum, NCBITaxon:60172 = Penicillium solitum, NCBITaxon:69488 = Penicillium simplicissimum, NCBITaxon:69779 = Penicillium melinii. Names/synonyms do not establish fresh rank/lineage, strain equivalence or experimental production. Exact forward-merge and nonorganism predicates are negative. The source Mucor irregularis label does not independently establish equivalence to cached B50; the two janthinellum/ianthinellum IDs remain distinct. |
| support-2870-curation | /private/tmp/npm-review-work/shared-next-batch287-tentative/native-prep/native-current287-implemented-curation-scan-001.json; /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows; /interpretation | supports | No exact applicable implemented decision changes these current owner/source/assay claims. Generic lexical matches do not apply a correction. |
| support-2870-producerpolicy | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; complete retained source-method grading table | supports | SOURCE_ASSERTION producer and the recorded locus grade have separate scopes; no upgrade from occurrence or shared BGC. |
| support-2870-stereopolicy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines 142-173 structure_fields, specifically 165-172 atom-centre predicate | supports | FindMolChiralCenters unknown atom tags determine stereo_complete; E/Z completeness and natural configuration are not certified. |
| support-2870-filingpolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 295-306 choose_pathway | supports | Exactly one supported model pathway files a record; multiple, absent or unsupported results retain UNCLASSIFIED. |
| support-2870-gates | /private/tmp/npm-review-work/shared-next-batch287/root-current287-five-gates-acceptance-001.json; /accepted; /five_local_commands_passed; /counts; /unavailable_required_gates; /all_native_gates_passed | supports | Five local gates pass; full QC and complete OAK remain unavailable. Queue leads are not scientific findings. |
| support-2870-history | /private/tmp/npm-review-work/shared-next-batch287/owner-capture-DATA-001.json; /records/9/owner_document/curation_history; /records/9/owner_document/source_concepts | supports | DOI:10.1021/jf020983e has COMPOUND_BIOACTIVITY scope, not causal-production or route scope. The 22 LOTUS rows retain individual DOI/Wikidata pointers; five seed histories do not add independent experiments. Assay metadata has its own source provenance and does not establish primary sample verification. |
| support-2870-scope | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-target-input-plan-001.json; /records/9/complete_root_keys; /records/9/declared_mechanism_roots_literal; /records/9/component_paths | supports | The complete owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway, molecular_targets or components; no maintained reader applies. It retains 22 bioactivity observations and a generated activity summary, which are assessed separately. The separate Paxilline reader supplies no authority for this owner. |
| support-2870-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/mibig_compounds | supports | Whole saved mibig_compounds frame: 1 positive placements. |
| support-2870-table-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical line 1660, raw UTF-8 row SHA-256 edd30e86e4d7e3b7e604cde2f4fe8a4ffd873917b99e90190ca00ea698dae974 | supports | BGC0001375 version 4 compound index 1 grounds penitrem A, full key JDUWHZOLEDOQSR-JKPSMKLGSA-N and PubChem CID 6610243. The complete key/CID joins source assays; label similarity does not transfer companion results. Penicillium simplicissimum NCBITaxon:69488 remains SOURCE_ASSERTION. A matching occurrence is not independent causal producer evidence. BGC0001375 is active with questionable quality and unknown completeness. LC027937.1 and TERPENE/Unknown are retained, but blank locus bounds/methods leave CLUSTER_UNSTATED. No graph, pathway or complete enzyme sequence is supplied. |
| support-2870-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_structures | supports | Whole saved chebi_structures frame: 0 positive placements. |
| support-2870-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/lotus_occurrences | supports | Whole saved lotus_occurrences frame: 22 positive placements. |
| support-2870-table-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical line 2977, raw UTF-8 row SHA-256 1fd94b56acd93b37a660a3c2a4e2a151dd751a98746a00f1a07647dcdd2d9921; physical line 2978, raw UTF-8 row SHA-256 536f5ba12b76de1587c26ac5c29eddec204e0a06e9e7e73b69ead9a673acf8f5; physical line 2979, raw UTF-8 row SHA-256 ea4e28fbb134ffdd65cda58572a082199fed297395148305c24d90967d3ddb2f; physical line 2980, raw UTF-8 row SHA-256 f34bdc9a84c2bb04b60eb29b1ffb7f71dfe41886ed4f75faf936a88b3d5dfbcf; physical line 2981, raw UTF-8 row SHA-256 a360812162cb0c8b918b75c792b5d258153fcb841a2176f018d88486ff9cdbca; physical line 2982, raw UTF-8 row SHA-256 bcb50554661b2383b2f51b760e7f611163040cd733f5dc134e76a0af19e87447; physical line 2983, raw UTF-8 row SHA-256 cfcaa8115b1e7652d86af80907042ab801f576d898776ebc8572d0471ed7c680; physical line 2984, raw UTF-8 row SHA-256 f1e4cb5791ddeb5ecf8c1dad5f71b67680750806ab2374ff87cd7d772ae10a57; physical line 2985, raw UTF-8 row SHA-256 229d1dc24bc2d3017e8e4146e123ce0db986549ac69b979ff15991822bb5008b; physical line 2986, raw UTF-8 row SHA-256 d61aae1de9002c6c7f1566cf6cb90aa59256a7ca707ecf06c750738e8df1635b; physical line 2987, raw UTF-8 row SHA-256 ffcbbca4337f8d87b2f048cc4a7d67988b12ae2a0a1c743e169577d69e7f0360; physical line 2988, raw UTF-8 row SHA-256 62d3f7df632208a947e18c668cd620683b38622d629849dd5eb2d011f4ee7ba3; physical line 2989, raw UTF-8 row SHA-256 47b93d511dac0a7fbc8203a3c99ffd2fdf6008be0515dc5c33de3bf90cd50bfc; physical line 2990, raw UTF-8 row SHA-256 18ff65be848b05fffd0a8350b4295b8a7d82ff12c88416110c8c775c14ab2229; physical line 2991, raw UTF-8 row SHA-256 f97f32547864a43eeb348c0beedfe12440057fd3ee5594c43b760af0c2798d51; physical line 2992, raw UTF-8 row SHA-256 d5d5478573bc90b52129b416d508d813e2c6820c9beae1c81a299b493657dcd9; physical line 2993, raw UTF-8 row SHA-256 39854070fad6b624a17749dee368e1e67aeda553750e3b29f7d388f756416a11; physical line 2994, raw UTF-8 row SHA-256 e91d2af558d3540091204a83859d33cd3f48b3e22f4ba814ed15d6ac8ed5b957; physical line 2995, raw UTF-8 row SHA-256 fc87c64167d5987f7887da174e2f879d7cf60883db74085be03f0f7d58d75966; physical line 2996, raw UTF-8 row SHA-256 c06b3621a737db89ce5467421bc1001248738261ee65d3e0869365271948714b; physical line 2997, raw UTF-8 row SHA-256 acd4c44a10455eec2adcf55fafb953b60a7eb7e6f7096e0fc0a9730a6c3a997d; physical line 2998, raw UTF-8 row SHA-256 d78e2d51d7b6b855f07948fa4030dba9abf0bd37478b61299cdb0dd4c02d06d5 | supports | LOTUS physical rows 2977-2998 retain 22 occurrence assertions across twelve taxon IDs. Penicillium 5073 is genus-only; Mucor irregularis 1290454 has cached label Mucor irregularis B50 without a synonym proving strain equivalence. Penicillium janthinellum 5079 and P. ianthinellum 545233 remain distinct IDs. Row multiplicity and matching producer taxon do not establish publication independence. |
| support-2870-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences | supports | Whole saved cyanometdb_occurrences frame: 0 positive placements. |
| support-2870-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/npclassifier | supports | Whole saved npclassifier frame: 1 positive placements. |
| support-2870-table-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical line 1090, raw UTF-8 row SHA-256 d535392eca41b2a49ef3f7e538c3e8b23930ba43d9fd3d0d9785aac4dede726e | supports | NPClassifier retains Alkaloids plus Terpenoids, Tryptophan alkaloids and Indole-Diterpenoid alkaloids (Penitrems), is_glycoside:false and date 2026-09-07. These chemical-model labels are distinct from the generated bioactivity_summary ENZYME_INHIBITOR. The maintained generic inhibition/binding fallback makes an overbroad mechanistic assertion for the Lassa binding/entry observation and propagates it to the summary; this requires curation. No finding asserts that all retained effects are false or that Penitrem A never inhibits an enzyme. |
| support-2870-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/pubchem_bioassay | supports | Whole saved pubchem_bioassay frame: 22 positive placements. |
| support-2870-table-pubchem_bioassay | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical line 3072, raw UTF-8 row SHA-256 85ce40500cf176854294c3a5d0176a5b2fa22735054caca43ed75e1f0ace1293; physical line 3073, raw UTF-8 row SHA-256 7f6224c21925356cd9728abafad0bc48f513256f2091cf1a7244f7b41b96a822; physical line 3074, raw UTF-8 row SHA-256 38addb5c78bb58fa04e1f1d7328ca6f97f2fe1dec987c4047e54d6749780255e; physical line 3075, raw UTF-8 row SHA-256 93806f5a0aaaafbcd9ab2fc085a0435108933341991349075c9112eef80769b5; physical line 3076, raw UTF-8 row SHA-256 c973902466350dcbf4c8eee18be0462f231929844f7b86f6eb33d746ed88b20c; physical line 3077, raw UTF-8 row SHA-256 3f711fff2f4c5cea3e0098c9eb340a36b8c6a214d895009af02575f8c551e580; physical line 3078, raw UTF-8 row SHA-256 267b521fc161b1f412e47ac2bf6e3fe0da4f6aab96cee396660892a6e0c4ed35; physical line 3079, raw UTF-8 row SHA-256 f9ec0b8e2061ed200938b54fb1a3da0ab1d52a2c55da03d0e8081ace347b1643; physical line 3080, raw UTF-8 row SHA-256 68c3400a7c7fcaa98324973b7f704112e4f4bb430e99fcc57a3d832d8944c92d; physical line 3081, raw UTF-8 row SHA-256 a50b8e866c5d0ac058dbdcc8610391c6eb06e7231b1f516ce47b12612e49da75; physical line 3082, raw UTF-8 row SHA-256 1429e22b6233bf0b2c7587a452a6e2586ad3b8c01b21fd5abff3978e38afdbf7; physical line 3083, raw UTF-8 row SHA-256 4f74e7044ba1861bac9cfef28cae01d40266cb99db5f2716945a9426e667e2ee; physical line 3084, raw UTF-8 row SHA-256 1416cadf9cb5759c01bd61a35fd21494dbc95da590c164ffb2f18d6c6bec76f6; physical line 3085, raw UTF-8 row SHA-256 a4248aa9a7fc741763c04765a4a5057431837548e5b47428ba342a932b3314fa; physical line 3086, raw UTF-8 row SHA-256 483c46a553af414a0f480340a4b4a21d7a5b2ba72548d6e5dcfedf4a8fc22dfa; physical line 3087, raw UTF-8 row SHA-256 5e58d9104a5f3dfe2e9f6b6c02ec2d3e3396fd3102a0eb761915114482e875e3; physical line 3088, raw UTF-8 row SHA-256 369f94aa7b69dc9474261a6095e939c1118f57564824ed90a780359771ea97a2; physical line 3089, raw UTF-8 row SHA-256 21ff2d5e98fbd928bd3e19a938f9dd1b054de67f008e795ab1261f4f3ef6e504; physical line 3090, raw UTF-8 row SHA-256 ef2a87b6294308b0fa707434a731a5e8b1e3a11a3c8280995dd987d9e50818a4; physical line 3091, raw UTF-8 row SHA-256 223decdfa0a7fd0635db7c3f659fe0d8dd686a2899abc2d2e65fd396f82060b3; physical line 3092, raw UTF-8 row SHA-256 3609de85b28a3d73bdc478c67dd32d1227b19c1c38fca7c990cb23a4752997fc; physical line 3093, raw UTF-8 row SHA-256 d9707c96cd1c027c6a4b9f91c9a350d015268a18820241a84126e547104b58f7 | supports | The 22 retained PubChem rows represent eighteen unique AIDs, with paired target-presence variants for 1645877, 1645876, 1963824 and 1963823. Four source Active calls remain ACTIVE; eighteen Inconclusive calls remain NOT_DETERMINED, not inactive. The active thiol-reactivity artifact screen 1845221 has no activity class. Generic Potency values remain OTHER, not IC50/EC50; AID 2330 has no numeric endpoint. Target accession shape is not protein grounding. AID 720533 describes viral binding/entry, so its generated ENZYME_INHIBITOR assertion is unsupported by that retained evidence. Cellular TDP1 AID 686978 and STK33 AID 2330 titles also do not independently establish direct biochemical inhibition. Preserve calls, measurements and target variants while correcting or qualifying class inference. |
| support-2870-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/bindingdb_targets | supports | Whole saved bindingdb_targets frame: 0 positive placements. |
| support-2870-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Whole saved antibioticmech_inchikeys frame: 0 positive placements. |
| support-2870-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json; /contexts/14/source_scope_inventory/joins/chebi_origins | supports | Whole saved chebi_origins frame: 0 positive placements. |
| support-2870-companion-0 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-b.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Exact direct companion context retains its own full key and claim grades. No identity, configuration, assay, producer or pathway transfer; source credit is assigned once per owner. |
| support-2870-companion-1 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-c.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Exact direct companion context retains its own full key and claim grades. No identity, configuration, assay, producer or pathway transfer; source credit is assigned once per owner. |
| support-2870-companion-2 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-d.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Exact direct companion context retains its own full key and claim grades. No identity, configuration, assay, producer or pathway transfer; source credit is assigned once per owner. |
| support-2870-companion-3 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-e.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Exact direct companion context retains its own full key and claim grades. No identity, configuration, assay, producer or pathway transfer; source credit is assigned once per owner. |
| support-2870-companion-4 | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-f.yaml; complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters; whole raw reading attributed in current source scope | supports | Exact direct companion context retains its own full key and claim grades. No identity, configuration, assay, producer or pathway transfer; source credit is assigned once per owner. |
| support-2870-assay-owner | /private/tmp/npm-review-work/shared-next-batch287/owner-capture-DATA-001.json; /records/9/owner_document/bioactivities; /records/9/owner_document/bioactivity_summary | supports | All 22 retained observations and generated summary, including the exact classification fields at indices 17, 19 and 21. |
| support-2870-activitypolicy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines 128-142 classification policy/patterns; 160-178 classify_activity; 181-185 endpoint mapping; 208-214 accession-shape check; 1313-1359 assay emission; 1376-1381 summary emission | supports | The unambiguous-class policy conflicts with generic inhibition/binding fallback: ACTIVE rows receive inferred ENZYME_INHIBITOR and seed the summary. Calls, generic Potency/OTHER and target shape have distinct scopes. |
| support-2870-activityschema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; lines 631-664 BioactivityObservation; 920-949 BioactivityClassEnum; 973-978 ActivityCallEnum | supports | Observation activity_class is optional and each class must be evidence-backed. OTHER/UNKNOWN exist; no BINDING enum is invented. NOT_DETERMINED is distinct from inactive. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-287/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-287/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-287/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-287/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-287/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Normalized identifiers, formula agreement and local parsing do not establish independent full graph identity, natural-sample identity, experimental absolute stereochemistry or primary biological validation.
- Both canonical SMILES comparisons are true and the saved chirality-aware map covers all atoms, but it is one limited substructure comparison. In every case full_graph_identity_established remains false. Both forms retain thirteen specified tetrahedral candidates and no other potential-stereo entry. The two terminal methylenes cannot carry ordinary E/Z assignment. The true source atom-centre flag and canonical agreement do not prove natural absolute stereochemistry or validate activity classification.
- Eight undefined-stereochemistry warning lines occur in the original 368-byte stderr. They are globally unattributed and are not assigned to any owner or form.
- Primary publications, spectra, sequence/function experiments, live taxonomy, full QC and complete OAK remain unavailable. Source grades are not upgraded.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Fresh batch 287 evidence and judgments; batch 286 supplies structural interface only.
- No record, native status or history was edited; no source query, molecular parse, target invocation or external request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks. No maintained-reader check applies to these five owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T092129Z-penitrem-a
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: penitrem A'
started_at: '2026-11-07T08:46:40.707055Z'
finished_at: '2026-11-07T09:21:29.979955Z'
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
summary: Penitrem A has consistent saved molecular forms and thirteen specified atom
  centres. Its retained assay observations remain useful source evidence, but the
  generated ENZYME_INHIBITOR classification overstates at least the Lassa-virus binding/entry
  assay. This confirmed local classification issue is major and open; the partial
  review requires curation.
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
  - path: data/natural_products/unclassified/penitrem-a.yaml
    sha256: 598e0e7d65eadf82c374be9a39e88df35751e4301b6f881c202ded7135066b5c
    role: target
  - path: data/natural_products/unclassified/penitrem-b.yaml
    sha256: 47e66539eee4427d7b8cfdc50c4c3bb8ef05d4e5ef1570b5b454c5bf776c347c
    role: context
  - path: data/natural_products/unclassified/penitrem-c.yaml
    sha256: d41dc3c749e9ebd827e4bdc623630694aa7ec0080f3b4371206ac9195191f342
    role: context
  - path: data/natural_products/unclassified/penitrem-d.yaml
    sha256: 734aac2628691ae3defcb3c04ec88fb868064c92614a9d7c3f81469a01c76e28
    role: context
  - path: data/natural_products/unclassified/penitrem-e.yaml
    sha256: 06aba97ca03087eecc0ad6cccdf2554285ae170bb0b9f28133facb4317db2fdb
    role: context
  - path: data/natural_products/unclassified/penitrem-f.yaml
    sha256: 7aa7495c4c24f3e2999a591bf1a324fa834a06cd0fcbb0b808fd4ded79f7594e
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete NaturalProductRecord, including all present scientific
    claims, history and declared mechanisms; external verification remains unavailable.
  selection: Campaign path order 2870; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-5942c19a89
targets:
- target_id: naturalproductmech:mibig-5942c19a89
  path: data/natural_products/unclassified/penitrem-a.yaml
  label: penitrem A
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
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnose287-001.py
    36dad27dc204f7fd83bf2a8e18c654b35e2fce3809b5cbff1a8003ac002ccd60 a985a5a088430c5f67d4e6f344e489fc4ce05f537524273d80e4fd736ca1be2c
    14915667af9b084b32754d03f2fdcd66d372cc4f471504637f6ad97383766816
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored forms parsed with declared key/formula agreement. Both canonical
    SMILES comparisons are true and the saved chirality-aware map covers all atoms,
    but it is one limited substructure comparison. In every case full_graph_identity_established
    remains false.
  scope_note: Both saved forms are neutral C37H44ClNO6 with 45 atoms and 54 bonds.
    Ten ring rows agree with independent cycle rank ten. The polycyclic indole-containing
    scaffold, chlorine, epoxide, four-membered carbocycle, two terminal methylenes,
    three alcohols and three ether oxygens persist. No carbonyl, strict amide, ester
    or imidic motif is present. Both forms retain thirteen specified tetrahedral candidates
    and no other potential-stereo entry. The two terminal methylenes cannot carry
    ordinary E/Z assignment. The true source atom-centre flag and canonical agreement
    do not prove natural absolute stereochemistry or validate activity classification.
    Eight undefined-stereochemistry warning lines occur in the original 368-byte stderr.
    They are globally unattributed and are not assigned to any owner or form.
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-data
  - support-2870-execution
  - support-2870-diagaccept
  - support-2870-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  command: just validate-strict data/natural_products/unclassified/paraherquonin.yaml
    data/natural_products/unclassified/paxilline.yaml data/natural_products/unclassified/pelgipeptin-a.yaml
    data/natural_products/unclassified/pelgipeptin-b.yaml data/natural_products/unclassified/pelgipeptin-c.yaml
    data/natural_products/unclassified/pelgipeptin-d.yaml data/natural_products/unclassified/penigainamide-a.yaml
    data/natural_products/unclassified/penigainamide-b.yaml data/natural_products/unclassified/penigainamide-c.yaml
    data/natural_products/unclassified/penitrem-a.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-287/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-5942c19a89
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-287/validate-all-001.tsv
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
  - naturalproductmech:mibig-5942c19a89
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
  - naturalproductmech:mibig-5942c19a89
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
  - naturalproductmech:mibig-5942c19a89
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-287/review-queue-001.tsv
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
  - naturalproductmech:mibig-5942c19a89
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2870-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-a.yaml
  locator: 'complete file: identity, structures, source concepts, producer/locus/occurrence,
    activity fields when present and history'
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Complete current generated owner; source assertions and native SEEDED status
    preserved.
  snapshot_sha256: 598e0e7d65eadf82c374be9a39e88df35751e4301b6f881c202ded7135066b5c
- evidence_id: support-2870-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch287/owner-capture-DATA-001.json
  locator: /records/9/owner_document
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Original whole owner capture, including all retained histories and source
    assertions.
  snapshot_sha256: a985a5a088430c5f67d4e6f344e489fc4ce05f537524273d80e4fd736ca1be2c
- evidence_id: support-2870-source
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/support-prep/support-current287-assigned-source-reading-001.json
  locator: /contexts/8; /selected_counts; /companion_counts; /global_cautions
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Own selected-five reading: 61 row placements, 576 fields, 45 frames, 29
    negatives and 17 histories. Separate companion credit is not added to selected
    primary credit.'
  snapshot_sha256: 1cdf8c7d8e59ad31d45c58e4bbfbd7cfb42daed81426d64e394b143048235112
- evidence_id: support-2870-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-target-input-plan-001.json
  locator: /records/9; /source_placement_count; /unique_source_path_count
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Accepted 488-placement/73-path plan; 49 actual inputs for this owner.
  snapshot_sha256: 1165d631c0773cfdfbe684528295d0699636d97d00732801dd825b5bb72c334b
- evidence_id: support-2870-planaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/root-current287-source-plan-acceptance-001.json
  locator: /accepted; /plan; /status
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: ROOT accepted the original current plan.
  snapshot_sha256: 431fc70c7d259fbf19ce95367ab9f5f0d49f92232e903f5b3682c09809180acd
- evidence_id: support-2870-notes
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /curation
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Disjoint BGC 44 plus Support 124 row placements total 168 rows and 1551
    fields across 21 contexts. Native taxonomy/curation adds no primary-row credit.
  snapshot_sha256: 82e556ef3c4e0b85dfb36e2dc1df36faddb17a09eec16369c1a0ae78c88988d5
- evidence_id: support-2870-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/intakes-001/2870-inspect-001.json
  locator: /status; /source; /targets
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Original intake fixes current hashes and exact maintained owner roles.
  snapshot_sha256: ae711b7dcba33fc5b4025bda8822503bd333ec92aaf54a36499a257ed5fda250
- evidence_id: support-2870-intakeaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/root-current287-intake-acceptance-001.json
  locator: /accepted; /status; /intake_summary; /records
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Ten original intakes passed with exact current input maps.
  snapshot_sha256: a383fac0a7c326954b67870b2a7e09fe5a60f70242856a2d64235a5c5cce07ae
- evidence_id: support-2870-data
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles; /records/9/inchi; /records/9/comparisons; /records/9/atom_correspondence;
    /records/9/literal_InChI_layers; /records/9/formula_comparison_scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Both saved forms are neutral C37H44ClNO6 with 45 atoms and 54 bonds. Ten
    ring rows agree with independent cycle rank ten. The polycyclic indole-containing
    scaffold, chlorine, epoxide, four-membered carbocycle, two terminal methylenes,
    three alcohols and three ether oxygens persist. No carbonyl, strict amide, ester
    or imidic motif is present. Both canonical SMILES comparisons are true and the
    saved chirality-aware map covers all atoms, but it is one limited substructure
    comparison. In every case full_graph_identity_established remains false.
  snapshot_sha256: 48dcf8ad84d3fc15e89ffcf92069a740c448d8106aeb28a4029e3a744d7b5334
- evidence_id: support-2870-stereo
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/potential_stereo;
    /records/9/smiles/computed/stereo_counts; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds;
    /records/9/inchi/computed/potential_stereo; /records/9/inchi/computed/stereo_counts
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Both forms retain thirteen specified tetrahedral candidates and no other
    potential-stereo entry. The two terminal methylenes cannot carry ordinary E/Z
    assignment. The true source atom-centre flag and canonical agreement do not prove
    natural absolute stereochemistry or validate activity classification.
  snapshot_sha256: 48dcf8ad84d3fc15e89ffcf92069a740c448d8106aeb28a4029e3a744d7b5334
- evidence_id: support-2870-motifs
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-DATA-001.json
  locator: /records/9/smiles/computed/atoms; /records/9/smiles/computed/bonds; /records/9/smiles/computed/rings;
    /records/9/smiles/computed/motifs; /records/9/inchi/computed/atoms; /records/9/inchi/computed/bonds;
    /records/9/inchi/computed/rings; /records/9/inchi/computed/motifs
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: The epoxide is SMILES C5-C6-O7 and InChI C30-C36-O44. The four-membered
    carbocycle is source C23-C24-C25-C26 and InChI C12-C21-C35-C18. Terminal methylenes
    are source C1=C2 and C34=C35, retained as InChI C14=C0 and C15=C2. The saturated
    C5O predicate finds an embedded scaffold ring, not an assigned sugar; it does
    not contradict the nonglycoside model flag. No metal, phosphorus or free primary
    amine is present.
  snapshot_sha256: 48dcf8ad84d3fc15e89ffcf92069a740c448d8106aeb28a4029e3a744d7b5334
- evidence_id: support-2870-molecularreading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/support-prep/support-current287-last-five-molecular-intake-reading-001.json
  locator: /records/4; /counts; /interpretations/2870; /warnings
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'All ten saved forms personally read: 444 atoms, 490 bonds, 62 ring rows
    and 99 potential-stereo entries; no reparse.'
  snapshot_sha256: e74cc3754a9ebee745bd378c0a92d20f4a8ccbe3f87efd52a12ade110e6a821d
- evidence_id: support-2870-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /retries; /stderr
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: One original diagnostic exited zero with no retry.
  snapshot_sha256: 377411b920205ffc5a37e84f943fb114f92fe9341314fd2f2f56cb98ae7b684c
- evidence_id: support-2870-diagaccept
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/root-current287-diagnostic-acceptance-001.json
  locator: /accepted; /DATA; /execution; /scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: ROOT accepted original technical outputs without a scientific identity
    claim.
  snapshot_sha256: 9345f03e05866a000a91d5a3f97c9f9beefd713fa777d02937a01400ab449511
- evidence_id: support-2870-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/chemistry-local/diagnostic-original-001.stderr
  locator: complete original 368-byte stderr stream
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Eight undefined-stereochemistry warning lines occur in the original 368-byte
    stderr. They are globally unattributed and are not assigned to any owner or form.
  snapshot_sha256: 57dc500932332b50528feb40ed8a93e8ee8555facf35d24a6bcdb921545fe583
- evidence_id: support-2870-taxonomy
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/native-prep/native-current287-cached-taxonomy-reading-001.json
  locator: /context_interpretations/14; /physical_negative_query_scopes/14; /whole_stanzas
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Attributed Native retained-cache reading: NCBITaxon:121612 = Penicillium
    janczewskii, NCBITaxon:1290454 = Mucor irregularis B50, NCBITaxon:36656 = Penicillium
    crustosum, NCBITaxon:434487 = Penicillium novae-zeelandiae, NCBITaxon:5073 = Penicillium,
    NCBITaxon:5079 = Penicillium janthinellum, NCBITaxon:5083 = Penicillium canescens,
    NCBITaxon:545233 = Penicillium ianthinellum, NCBITaxon:60171 = Penicillium verrucosum,
    NCBITaxon:60172 = Penicillium solitum, NCBITaxon:69488 = Penicillium simplicissimum,
    NCBITaxon:69779 = Penicillium melinii. Names/synonyms do not establish fresh rank/lineage,
    strain equivalence or experimental production. Exact forward-merge and nonorganism
    predicates are negative. The source Mucor irregularis label does not independently
    establish equivalence to cached B50; the two janthinellum/ianthinellum IDs remain
    distinct.'
  snapshot_sha256: 90f49809ae1b579750a53f4bf77575320e4d42c10a7d2fef0268578e7f2671fb
- evidence_id: support-2870-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/native-prep/native-current287-implemented-curation-scan-001.json
  locator: /counts; /exact_predicates; /exact_applicability_resolution; /applied_rows;
    /interpretation
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: No exact applicable implemented decision changes these current owner/source/assay
    claims. Generic lexical matches do not apply a correction.
  snapshot_sha256: 58d2a7e2a96f650dd9de2f036dbaab3d2ec99635269bea770963577f29750601
  search_scope: Attributed ignored-inclusive nine-table/3422-row scan using exact
    owner/source/BGC/key/occurrence/assay predicates; no replay or universal absence.
- evidence_id: support-2870-producerpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: complete retained source-method grading table
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: SOURCE_ASSERTION producer and the recorded locus grade have separate scopes;
    no upgrade from occurrence or shared BGC.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: support-2870-stereopolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: lines 142-173 structure_fields, specifically 165-172 atom-centre predicate
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: FindMolChiralCenters unknown atom tags determine stereo_complete; E/Z completeness
    and natural configuration are not certified.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2870-filingpolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 295-306 choose_pathway
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Exactly one supported model pathway files a record; multiple, absent or
    unsupported results retain UNCLASSIFIED.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2870-gates
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch287/root-current287-five-gates-acceptance-001.json
  locator: /accepted; /five_local_commands_passed; /counts; /unavailable_required_gates;
    /all_native_gates_passed
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Five local gates pass; full QC and complete OAK remain unavailable. Queue
    leads are not scientific findings.
  snapshot_sha256: 24cd4f6efbc5a2b13255c0a1388ce930ff9734c4dcd984462a942bf5a9931e82
- evidence_id: support-2870-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch287/owner-capture-DATA-001.json
  locator: /records/9/owner_document/curation_history; /records/9/owner_document/source_concepts
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: DOI:10.1021/jf020983e has COMPOUND_BIOACTIVITY scope, not causal-production
    or route scope. The 22 LOTUS rows retain individual DOI/Wikidata pointers; five
    seed histories do not add independent experiments. Assay metadata has its own
    source provenance and does not establish primary sample verification.
  snapshot_sha256: a985a5a088430c5f67d4e6f344e489fc4ce05f537524273d80e4fd736ca1be2c
- evidence_id: support-2870-scope
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-target-input-plan-001.json
  locator: /records/9/complete_root_keys; /records/9/declared_mechanism_roots_literal;
    /records/9/component_paths
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: The complete owner has no causal_graphs, causal_graph_refs, biosynthetic_pathway,
    molecular_targets or components; no maintained reader applies. It retains 22 bioactivity
    observations and a generated activity summary, which are assessed separately.
    The separate Paxilline reader supplies no authority for this owner.
  snapshot_sha256: 1165d631c0773cfdfbe684528295d0699636d97d00732801dd825b5bb72c334b
- evidence_id: support-2870-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved mibig_compounds frame: 1 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-table-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical line 1660, raw UTF-8 row SHA-256 edd30e86e4d7e3b7e604cde2f4fe8a4ffd873917b99e90190ca00ea698dae974
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: BGC0001375 version 4 compound index 1 grounds penitrem A, full key JDUWHZOLEDOQSR-JKPSMKLGSA-N
    and PubChem CID 6610243. The complete key/CID joins source assays; label similarity
    does not transfer companion results. Penicillium simplicissimum NCBITaxon:69488
    remains SOURCE_ASSERTION. A matching occurrence is not independent causal producer
    evidence. BGC0001375 is active with questionable quality and unknown completeness.
    LC027937.1 and TERPENE/Unknown are retained, but blank locus bounds/methods leave
    CLUSTER_UNSTATED. No graph, pathway or complete enzyme sequence is supplied.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2870-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved chebi_structures frame: 0 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved lotus_occurrences frame: 22 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-table-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical line 2977, raw UTF-8 row SHA-256 1fd94b56acd93b37a660a3c2a4e2a151dd751a98746a00f1a07647dcdd2d9921;
    physical line 2978, raw UTF-8 row SHA-256 536f5ba12b76de1587c26ac5c29eddec204e0a06e9e7e73b69ead9a673acf8f5;
    physical line 2979, raw UTF-8 row SHA-256 ea4e28fbb134ffdd65cda58572a082199fed297395148305c24d90967d3ddb2f;
    physical line 2980, raw UTF-8 row SHA-256 f34bdc9a84c2bb04b60eb29b1ffb7f71dfe41886ed4f75faf936a88b3d5dfbcf;
    physical line 2981, raw UTF-8 row SHA-256 a360812162cb0c8b918b75c792b5d258153fcb841a2176f018d88486ff9cdbca;
    physical line 2982, raw UTF-8 row SHA-256 bcb50554661b2383b2f51b760e7f611163040cd733f5dc134e76a0af19e87447;
    physical line 2983, raw UTF-8 row SHA-256 cfcaa8115b1e7652d86af80907042ab801f576d898776ebc8572d0471ed7c680;
    physical line 2984, raw UTF-8 row SHA-256 f1e4cb5791ddeb5ecf8c1dad5f71b67680750806ab2374ff87cd7d772ae10a57;
    physical line 2985, raw UTF-8 row SHA-256 229d1dc24bc2d3017e8e4146e123ce0db986549ac69b979ff15991822bb5008b;
    physical line 2986, raw UTF-8 row SHA-256 d61aae1de9002c6c7f1566cf6cb90aa59256a7ca707ecf06c750738e8df1635b;
    physical line 2987, raw UTF-8 row SHA-256 ffcbbca4337f8d87b2f048cc4a7d67988b12ae2a0a1c743e169577d69e7f0360;
    physical line 2988, raw UTF-8 row SHA-256 62d3f7df632208a947e18c668cd620683b38622d629849dd5eb2d011f4ee7ba3;
    physical line 2989, raw UTF-8 row SHA-256 47b93d511dac0a7fbc8203a3c99ffd2fdf6008be0515dc5c33de3bf90cd50bfc;
    physical line 2990, raw UTF-8 row SHA-256 18ff65be848b05fffd0a8350b4295b8a7d82ff12c88416110c8c775c14ab2229;
    physical line 2991, raw UTF-8 row SHA-256 f97f32547864a43eeb348c0beedfe12440057fd3ee5594c43b760af0c2798d51;
    physical line 2992, raw UTF-8 row SHA-256 d5d5478573bc90b52129b416d508d813e2c6820c9beae1c81a299b493657dcd9;
    physical line 2993, raw UTF-8 row SHA-256 39854070fad6b624a17749dee368e1e67aeda553750e3b29f7d388f756416a11;
    physical line 2994, raw UTF-8 row SHA-256 e91d2af558d3540091204a83859d33cd3f48b3e22f4ba814ed15d6ac8ed5b957;
    physical line 2995, raw UTF-8 row SHA-256 fc87c64167d5987f7887da174e2f879d7cf60883db74085be03f0f7d58d75966;
    physical line 2996, raw UTF-8 row SHA-256 c06b3621a737db89ce5467421bc1001248738261ee65d3e0869365271948714b;
    physical line 2997, raw UTF-8 row SHA-256 acd4c44a10455eec2adcf55fafb953b60a7eb7e6f7096e0fc0a9730a6c3a997d;
    physical line 2998, raw UTF-8 row SHA-256 d78e2d51d7b6b855f07948fa4030dba9abf0bd37478b61299cdb0dd4c02d06d5
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: LOTUS physical rows 2977-2998 retain 22 occurrence assertions across twelve
    taxon IDs. Penicillium 5073 is genus-only; Mucor irregularis 1290454 has cached
    label Mucor irregularis B50 without a synonym proving strain equivalence. Penicillium
    janthinellum 5079 and P. ianthinellum 545233 remain distinct IDs. Row multiplicity
    and matching producer taxon do not establish publication independence.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2870-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved cyanometdb_occurrences frame: 0 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved npclassifier frame: 1 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-table-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical line 1090, raw UTF-8 row SHA-256 d535392eca41b2a49ef3f7e538c3e8b23930ba43d9fd3d0d9785aac4dede726e
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: NPClassifier retains Alkaloids plus Terpenoids, Tryptophan alkaloids and
    Indole-Diterpenoid alkaloids (Penitrems), is_glycoside:false and date 2026-09-07.
    These chemical-model labels are distinct from the generated bioactivity_summary
    ENZYME_INHIBITOR. The maintained generic inhibition/binding fallback makes an
    overbroad mechanistic assertion for the Lassa binding/entry observation and propagates
    it to the summary; this requires curation. No finding asserts that all retained
    effects are false or that Penitrem A never inhibits an enzyme.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2870-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved pubchem_bioassay frame: 22 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-table-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical line 3072, raw UTF-8 row SHA-256 85ce40500cf176854294c3a5d0176a5b2fa22735054caca43ed75e1f0ace1293;
    physical line 3073, raw UTF-8 row SHA-256 7f6224c21925356cd9728abafad0bc48f513256f2091cf1a7244f7b41b96a822;
    physical line 3074, raw UTF-8 row SHA-256 38addb5c78bb58fa04e1f1d7328ca6f97f2fe1dec987c4047e54d6749780255e;
    physical line 3075, raw UTF-8 row SHA-256 93806f5a0aaaafbcd9ab2fc085a0435108933341991349075c9112eef80769b5;
    physical line 3076, raw UTF-8 row SHA-256 c973902466350dcbf4c8eee18be0462f231929844f7b86f6eb33d746ed88b20c;
    physical line 3077, raw UTF-8 row SHA-256 3f711fff2f4c5cea3e0098c9eb340a36b8c6a214d895009af02575f8c551e580;
    physical line 3078, raw UTF-8 row SHA-256 267b521fc161b1f412e47ac2bf6e3fe0da4f6aab96cee396660892a6e0c4ed35;
    physical line 3079, raw UTF-8 row SHA-256 f9ec0b8e2061ed200938b54fb1a3da0ab1d52a2c55da03d0e8081ace347b1643;
    physical line 3080, raw UTF-8 row SHA-256 68c3400a7c7fcaa98324973b7f704112e4f4bb430e99fcc57a3d832d8944c92d;
    physical line 3081, raw UTF-8 row SHA-256 a50b8e866c5d0ac058dbdcc8610391c6eb06e7231b1f516ce47b12612e49da75;
    physical line 3082, raw UTF-8 row SHA-256 1429e22b6233bf0b2c7587a452a6e2586ad3b8c01b21fd5abff3978e38afdbf7;
    physical line 3083, raw UTF-8 row SHA-256 4f74e7044ba1861bac9cfef28cae01d40266cb99db5f2716945a9426e667e2ee;
    physical line 3084, raw UTF-8 row SHA-256 1416cadf9cb5759c01bd61a35fd21494dbc95da590c164ffb2f18d6c6bec76f6;
    physical line 3085, raw UTF-8 row SHA-256 a4248aa9a7fc741763c04765a4a5057431837548e5b47428ba342a932b3314fa;
    physical line 3086, raw UTF-8 row SHA-256 483c46a553af414a0f480340a4b4a21d7a5b2ba72548d6e5dcfedf4a8fc22dfa;
    physical line 3087, raw UTF-8 row SHA-256 5e58d9104a5f3dfe2e9f6b6c02ec2d3e3396fd3102a0eb761915114482e875e3;
    physical line 3088, raw UTF-8 row SHA-256 369f94aa7b69dc9474261a6095e939c1118f57564824ed90a780359771ea97a2;
    physical line 3089, raw UTF-8 row SHA-256 21ff2d5e98fbd928bd3e19a938f9dd1b054de67f008e795ab1261f4f3ef6e504;
    physical line 3090, raw UTF-8 row SHA-256 ef2a87b6294308b0fa707434a731a5e8b1e3a11a3c8280995dd987d9e50818a4;
    physical line 3091, raw UTF-8 row SHA-256 223decdfa0a7fd0635db7c3f659fe0d8dd686a2899abc2d2e65fd396f82060b3;
    physical line 3092, raw UTF-8 row SHA-256 3609de85b28a3d73bdc478c67dd32d1227b19c1c38fca7c990cb23a4752997fc;
    physical line 3093, raw UTF-8 row SHA-256 d9707c96cd1c027c6a4b9f91c9a350d015268a18820241a84126e547104b58f7
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: The 22 retained PubChem rows represent eighteen unique AIDs, with paired
    target-presence variants for 1645877, 1645876, 1963824 and 1963823. Four source
    Active calls remain ACTIVE; eighteen Inconclusive calls remain NOT_DETERMINED,
    not inactive. The active thiol-reactivity artifact screen 1845221 has no activity
    class. Generic Potency values remain OTHER, not IC50/EC50; AID 2330 has no numeric
    endpoint. Target accession shape is not protein grounding. AID 720533 describes
    viral binding/entry, so its generated ENZYME_INHIBITOR assertion is unsupported
    by that retained evidence. Cellular TDP1 AID 686978 and STK33 AID 2330 titles
    also do not independently establish direct biochemical inhibition. Preserve calls,
    measurements and target variants while correcting or qualifying class inference.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: support-2870-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved bindingdb_targets frame: 0 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved antibioticmech_inchikeys frame: 0 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact complete standard_inchi_key equality; query
    "JDUWHZOLEDOQSR-JKPSMKLGSA-N". No replay or wider absence claim.
- evidence_id: support-2870-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch287-tentative/bgc-prep/bgc-conditional287-source-inventory-DATA-001.json
  locator: /contexts/14/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'Whole saved chebi_origins frame: 0 positive placements.'
  snapshot_sha256: b46d10e4ad545844fc39ce82785db690ee89c23c537b3708cab7a8bb3a453b2e
  search_scope: Saved predicate exact chebi_id from exact full-key structure rows;
    query []. No replay or wider absence claim.
- evidence_id: support-2870-companion-0
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-b.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Exact direct companion context retains its own full key and claim grades.
    No identity, configuration, assay, producer or pathway transfer; source credit
    is assigned once per owner.
  snapshot_sha256: 47e66539eee4427d7b8cfdc50c4c3bb8ef05d4e5ef1570b5b454c5bf776c347c
- evidence_id: support-2870-companion-1
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-c.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Exact direct companion context retains its own full key and claim grades.
    No identity, configuration, assay, producer or pathway transfer; source credit
    is assigned once per owner.
  snapshot_sha256: d41dc3c749e9ebd827e4bdc623630694aa7ec0080f3b4371206ac9195191f342
- evidence_id: support-2870-companion-2
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-d.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Exact direct companion context retains its own full key and claim grades.
    No identity, configuration, assay, producer or pathway transfer; source credit
    is assigned once per owner.
  snapshot_sha256: 734aac2628691ae3defcb3c04ec88fb868064c92614a9d7c3f81469a01c76e28
- evidence_id: support-2870-companion-3
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-e.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Exact direct companion context retains its own full key and claim grades.
    No identity, configuration, assay, producer or pathway transfer; source credit
    is assigned once per owner.
  snapshot_sha256: 06aba97ca03087eecc0ad6cccdf2554285ae170bb0b9f28133facb4317db2fdb
- evidence_id: support-2870-companion-4
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/penitrem-f.yaml
  locator: complete identifier, chemical_structure, source_concepts and biosynthetic_gene_clusters;
    whole raw reading attributed in current source scope
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Exact direct companion context retains its own full key and claim grades.
    No identity, configuration, assay, producer or pathway transfer; source credit
    is assigned once per owner.
  snapshot_sha256: 7aa7495c4c24f3e2999a591bf1a324fa834a06cd0fcbb0b808fd4ded79f7594e
- evidence_id: support-2870-assay-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch287/owner-capture-DATA-001.json
  locator: /records/9/owner_document/bioactivities; /records/9/owner_document/bioactivity_summary
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: All 22 retained observations and generated summary, including the exact
    classification fields at indices 17, 19 and 21.
  snapshot_sha256: a985a5a088430c5f67d4e6f344e489fc4ce05f537524273d80e4fd736ca1be2c
- evidence_id: support-2870-activitypolicy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: lines 128-142 classification policy/patterns; 160-178 classify_activity;
    181-185 endpoint mapping; 208-214 accession-shape check; 1313-1359 assay emission;
    1376-1381 summary emission
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: 'The unambiguous-class policy conflicts with generic inhibition/binding
    fallback: ACTIVE rows receive inferred ENZYME_INHIBITOR and seed the summary.
    Calls, generic Potency/OTHER and target shape have distinct scopes.'
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2870-activityschema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: lines 631-664 BioactivityObservation; 920-949 BioactivityClassEnum; 973-978
    ActivityCallEnum
  accessed_at: '2026-11-07T09:11:36.396404Z'
  support: supports
  summary: Observation activity_class is optional and each class must be evidence-backed.
    OTHER/UNKNOWN exist; no BINDING enum is invented. NOT_DETERMINED is distinct from
    inactive.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-287/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json
  accessed_at: '2026-11-07T08:47:39.161933Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 306fe10ce3730b943a10632b593bdea3366989c1ebf9f49d2c03b1d04bcb9ab2
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-287/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json
  accessed_at: '2026-11-07T08:48:05.047091Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 71144670a006c4f55f97c48c026fb5c12f680b74e4e5c9de67113b582f58b53b
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-287/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json
  accessed_at: '2026-11-07T08:48:25.689447Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-287/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json
  accessed_at: '2026-11-07T08:49:01.011283Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-287/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-287/native-current287-five-gates-execution-001.json
  accessed_at: '2026-11-07T08:49:13.170979Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 2eeda82207b939968ae9df33f999891b585e01f9169b01796fad13018a82c0fa
assessments:
- assessment_id: support-2870-identity-assessment
  area: identity
  topic: Exact retained compound grounding
  summary: BGC0001375 version 4 compound index 1 grounds penitrem A, full key JDUWHZOLEDOQSR-JKPSMKLGSA-N
    and PubChem CID 6610243. The complete key/CID joins source assays; label similarity
    does not transfer companion results.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-owner
  - support-2870-capture
  - support-2870-source
  - support-2870-intake
  - support-2870-curation
  - support-2870-plan
  - support-2870-table-mibig_compounds
  - support-2870-table-lotus_occurrences
  - support-2870-table-npclassifier
  - support-2870-table-pubchem_bioassay
  - support-2870-companion-0
  - support-2870-companion-1
  - support-2870-companion-2
  - support-2870-companion-3
  - support-2870-companion-4
  dimensions:
  - name: standard_inchi_key
    definition: Complete source key, not label-only identity.
    value: JDUWHZOLEDOQSR-JKPSMKLGSA-N
    evidence_ids:
    - support-2870-owner
    - support-2870-capture
    - support-2870-source
    - support-2870-intake
    - support-2870-curation
    - support-2870-plan
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
    - support-2870-companion-0
    - support-2870-companion-1
    - support-2870-companion-2
    - support-2870-companion-3
    - support-2870-companion-4
  - name: grounding_scope
    definition: Retained source identity versus independent natural identity.
    value: BGC0001375 version 4 compound index 1 grounds penitrem A, full key JDUWHZOLEDOQSR-JKPSMKLGSA-N
      and PubChem CID 6610243. The complete key/CID joins source assays; label similarity
      does not transfer companion results.
    evidence_ids:
    - support-2870-owner
    - support-2870-capture
    - support-2870-source
    - support-2870-intake
    - support-2870-curation
    - support-2870-plan
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
    - support-2870-companion-0
    - support-2870-companion-1
    - support-2870-companion-2
    - support-2870-companion-3
    - support-2870-companion-4
- assessment_id: support-2870-representation-assessment
  area: representation
  topic: Saved forms and stereochemical scope
  summary: Both saved forms are neutral C37H44ClNO6 with 45 atoms and 54 bonds. Ten
    ring rows agree with independent cycle rank ten. The polycyclic indole-containing
    scaffold, chlorine, epoxide, four-membered carbocycle, two terminal methylenes,
    three alcohols and three ether oxygens persist. No carbonyl, strict amide, ester
    or imidic motif is present. The epoxide is SMILES C5-C6-O7 and InChI C30-C36-O44.
    The four-membered carbocycle is source C23-C24-C25-C26 and InChI C12-C21-C35-C18.
    Terminal methylenes are source C1=C2 and C34=C35, retained as InChI C14=C0 and
    C15=C2. The saturated C5O predicate finds an embedded scaffold ring, not an assigned
    sugar; it does not contradict the nonglycoside model flag. No metal, phosphorus
    or free primary amine is present. Both canonical SMILES comparisons are true and
    the saved chirality-aware map covers all atoms, but it is one limited substructure
    comparison. In every case full_graph_identity_established remains false. Normalized
    identifiers, formula agreement and local parsing do not establish independent
    full graph identity, natural-sample identity, experimental absolute stereochemistry
    or primary biological validation.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-data
  - support-2870-stereo
  - support-2870-motifs
  - support-2870-molecularreading
  - support-2870-execution
  - support-2870-diagaccept
  - support-2870-stereopolicy
  dimensions:
  - name: stereochemistry_scope
    definition: Saved atom/bond assignments and topology-specific candidates.
    value: Both forms retain thirteen specified tetrahedral candidates and no other
      potential-stereo entry. The two terminal methylenes cannot carry ordinary E/Z
      assignment. The true source atom-centre flag and canonical agreement do not
      prove natural absolute stereochemistry or validate activity classification.
    evidence_ids:
    - support-2870-data
    - support-2870-stereo
    - support-2870-motifs
    - support-2870-molecularreading
    - support-2870-execution
    - support-2870-diagaccept
    - support-2870-stereopolicy
  - name: representation_correspondence
    definition: Limited matching is distinct from full identity.
    value: Both canonical SMILES comparisons are true and the saved chirality-aware
      map covers all atoms, but it is one limited substructure comparison. In every
      case full_graph_identity_established remains false. Normalized identifiers,
      formula agreement and local parsing do not establish independent full graph
      identity, natural-sample identity, experimental absolute stereochemistry or
      primary biological validation.
    evidence_ids:
    - support-2870-data
    - support-2870-stereo
    - support-2870-motifs
    - support-2870-molecularreading
    - support-2870-execution
    - support-2870-diagaccept
    - support-2870-stereopolicy
- assessment_id: support-2870-provenance-assessment
  area: provenance
  topic: Producer, locus and taxon claim grain
  summary: Penicillium simplicissimum NCBITaxon:69488 remains SOURCE_ASSERTION. A
    matching occurrence is not independent causal producer evidence. BGC0001375 is
    active with questionable quality and unknown completeness. LC027937.1 and TERPENE/Unknown
    are retained, but blank locus bounds/methods leave CLUSTER_UNSTATED. No graph,
    pathway or complete enzyme sequence is supplied.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-source
  - support-2870-capture
  - support-2870-taxonomy
  - support-2870-curation
  - support-2870-producerpolicy
  - support-2870-table-mibig_compounds
  - support-2870-table-lotus_occurrences
  - support-2870-table-npclassifier
  - support-2870-table-pubchem_bioassay
  dimensions:
  - name: taxon_scope
    definition: Cached names do not establish live taxonomy or strain equivalence.
    value: 'Attributed Native retained-cache reading: NCBITaxon:121612 = Penicillium
      janczewskii, NCBITaxon:1290454 = Mucor irregularis B50, NCBITaxon:36656 = Penicillium
      crustosum, NCBITaxon:434487 = Penicillium novae-zeelandiae, NCBITaxon:5073 =
      Penicillium, NCBITaxon:5079 = Penicillium janthinellum, NCBITaxon:5083 = Penicillium
      canescens, NCBITaxon:545233 = Penicillium ianthinellum, NCBITaxon:60171 = Penicillium
      verrucosum, NCBITaxon:60172 = Penicillium solitum, NCBITaxon:69488 = Penicillium
      simplicissimum, NCBITaxon:69779 = Penicillium melinii. Names/synonyms do not
      establish fresh rank/lineage, strain equivalence or experimental production.
      Exact forward-merge and nonorganism predicates are negative. The source Mucor
      irregularis label does not independently establish equivalence to cached B50;
      the two janthinellum/ianthinellum IDs remain distinct.'
    evidence_ids:
    - support-2870-source
    - support-2870-capture
    - support-2870-taxonomy
    - support-2870-curation
    - support-2870-producerpolicy
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
  - name: producer_evidence
    definition: Producer grade remains separate from locus and occurrence.
    value: Penicillium simplicissimum NCBITaxon:69488 remains SOURCE_ASSERTION. A
      matching occurrence is not independent causal producer evidence.
    evidence_ids:
    - support-2870-source
    - support-2870-capture
    - support-2870-taxonomy
    - support-2870-curation
    - support-2870-producerpolicy
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
  - name: locus_evidence
    definition: Entry quality, completeness and methods delimit evidence.
    value: BGC0001375 is active with questionable quality and unknown completeness.
      LC027937.1 and TERPENE/Unknown are retained, but blank locus bounds/methods
      leave CLUSTER_UNSTATED. No graph, pathway or complete enzyme sequence is supplied.
    evidence_ids:
    - support-2870-source
    - support-2870-capture
    - support-2870-taxonomy
    - support-2870-curation
    - support-2870-producerpolicy
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
- assessment_id: support-2870-citations-assessment
  area: evidence
  topic: Citation grain and retained history
  summary: DOI:10.1021/jf020983e has COMPOUND_BIOACTIVITY scope, not causal-production
    or route scope. The 22 LOTUS rows retain individual DOI/Wikidata pointers; five
    seed histories do not add independent experiments. Assay metadata has its own
    source provenance and does not establish primary sample verification.
  outcome: supported
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-owner
  - support-2870-source
  - support-2870-capture
  - support-2870-history
  - support-2870-table-mibig_compounds
  - support-2870-table-lotus_occurrences
  - support-2870-table-npclassifier
  - support-2870-table-pubchem_bioassay
  dimensions:
  - name: citation_scope
    definition: Pointers and seed events are not independent experimental proof.
    value: DOI:10.1021/jf020983e has COMPOUND_BIOACTIVITY scope, not causal-production
      or route scope. The 22 LOTUS rows retain individual DOI/Wikidata pointers; five
      seed histories do not add independent experiments. Assay metadata has its own
      source provenance and does not establish primary sample verification.
    evidence_ids:
    - support-2870-owner
    - support-2870-source
    - support-2870-capture
    - support-2870-history
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
- assessment_id: support-2870-occurrence-assay-assessment
  area: evidence
  topic: Occurrence and assay boundaries
  summary: LOTUS physical rows 2977-2998 retain 22 occurrence assertions across twelve
    taxon IDs. Penicillium 5073 is genus-only; Mucor irregularis 1290454 has cached
    label Mucor irregularis B50 without a synonym proving strain equivalence. Penicillium
    janthinellum 5079 and P. ianthinellum 545233 remain distinct IDs. Row multiplicity
    and matching producer taxon do not establish publication independence. The 22
    retained PubChem rows represent eighteen unique AIDs, with paired target-presence
    variants for 1645877, 1645876, 1963824 and 1963823. Four source Active calls remain
    ACTIVE; eighteen Inconclusive calls remain NOT_DETERMINED, not inactive. The active
    thiol-reactivity artifact screen 1845221 has no activity class. Generic Potency
    values remain OTHER, not IC50/EC50; AID 2330 has no numeric endpoint. Target accession
    shape is not protein grounding. AID 720533 describes viral binding/entry, so its
    generated ENZYME_INHIBITOR assertion is unsupported by that retained evidence.
    Cellular TDP1 AID 686978 and STK33 AID 2330 titles also do not independently establish
    direct biochemical inhibition. Preserve calls, measurements and target variants
    while correcting or qualifying class inference.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-source
  - support-2870-taxonomy
  - support-2870-curation
  - support-2870-plan
  - support-2870-assay-owner
  - support-2870-activitypolicy
  - support-2870-activityschema
  - support-2870-query-mibig_compounds
  - support-2870-query-chebi_structures
  - support-2870-query-lotus_occurrences
  - support-2870-query-cyanometdb_occurrences
  - support-2870-query-npclassifier
  - support-2870-query-pubchem_bioassay
  - support-2870-query-bindingdb_targets
  - support-2870-query-antibioticmech_inchikeys
  - support-2870-query-chebi_origins
  - support-2870-table-mibig_compounds
  - support-2870-table-lotus_occurrences
  - support-2870-table-npclassifier
  - support-2870-table-pubchem_bioassay
  dimensions:
  - name: occurrence_scope
    definition: Occurrence is distinct from causal production.
    value: LOTUS physical rows 2977-2998 retain 22 occurrence assertions across twelve
      taxon IDs. Penicillium 5073 is genus-only; Mucor irregularis 1290454 has cached
      label Mucor irregularis B50 without a synonym proving strain equivalence. Penicillium
      janthinellum 5079 and P. ianthinellum 545233 remain distinct IDs. Row multiplicity
      and matching producer taxon do not establish publication independence.
    evidence_ids:
    - support-2870-source
    - support-2870-taxonomy
    - support-2870-curation
    - support-2870-plan
    - support-2870-assay-owner
    - support-2870-activitypolicy
    - support-2870-activityschema
    - support-2870-query-mibig_compounds
    - support-2870-query-chebi_structures
    - support-2870-query-lotus_occurrences
    - support-2870-query-cyanometdb_occurrences
    - support-2870-query-npclassifier
    - support-2870-query-pubchem_bioassay
    - support-2870-query-bindingdb_targets
    - support-2870-query-antibioticmech_inchikeys
    - support-2870-query-chebi_origins
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
  - name: assay_target_scope
    definition: Calls, measurements, target annotations and inferred class have separate
      scopes.
    value: The 22 retained PubChem rows represent eighteen unique AIDs, with paired
      target-presence variants for 1645877, 1645876, 1963824 and 1963823. Four source
      Active calls remain ACTIVE; eighteen Inconclusive calls remain NOT_DETERMINED,
      not inactive. The active thiol-reactivity artifact screen 1845221 has no activity
      class. Generic Potency values remain OTHER, not IC50/EC50; AID 2330 has no numeric
      endpoint. Target accession shape is not protein grounding. AID 720533 describes
      viral binding/entry, so its generated ENZYME_INHIBITOR assertion is unsupported
      by that retained evidence. Cellular TDP1 AID 686978 and STK33 AID 2330 titles
      also do not independently establish direct biochemical inhibition. Preserve
      calls, measurements and target variants while correcting or qualifying class
      inference.
    evidence_ids:
    - support-2870-source
    - support-2870-taxonomy
    - support-2870-curation
    - support-2870-plan
    - support-2870-assay-owner
    - support-2870-activitypolicy
    - support-2870-activityschema
    - support-2870-query-mibig_compounds
    - support-2870-query-chebi_structures
    - support-2870-query-lotus_occurrences
    - support-2870-query-cyanometdb_occurrences
    - support-2870-query-npclassifier
    - support-2870-query-pubchem_bioassay
    - support-2870-query-bindingdb_targets
    - support-2870-query-antibioticmech_inchikeys
    - support-2870-query-chebi_origins
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
- assessment_id: support-2870-classification-assessment
  area: consistency
  topic: Source/model classes and generated activity classification
  summary: NPClassifier retains Alkaloids plus Terpenoids, Tryptophan alkaloids and
    Indole-Diterpenoid alkaloids (Penitrems), is_glycoside:false and date 2026-09-07.
    These chemical-model labels are distinct from the generated bioactivity_summary
    ENZYME_INHIBITOR. The maintained generic inhibition/binding fallback makes an
    overbroad mechanistic assertion for the Lassa binding/entry observation and propagates
    it to the summary; this requires curation. No finding asserts that all retained
    effects are false or that Penitrem A never inhibits an enzyme.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-source
  - support-2870-owner
  - support-2870-motifs
  - support-2870-filingpolicy
  - support-2870-gates
  - support-2870-assay-owner
  - support-2870-activitypolicy
  - support-2870-activityschema
  - support-2870-table-mibig_compounds
  - support-2870-table-lotus_occurrences
  - support-2870-table-npclassifier
  - support-2870-table-pubchem_bioassay
  dimensions:
  - name: classification_applicability
    definition: Chemical model labels and activity mechanism require their own evidence.
    value: NPClassifier retains Alkaloids plus Terpenoids, Tryptophan alkaloids and
      Indole-Diterpenoid alkaloids (Penitrems), is_glycoside:false and date 2026-09-07.
      These chemical-model labels are distinct from the generated bioactivity_summary
      ENZYME_INHIBITOR. The maintained generic inhibition/binding fallback makes an
      overbroad mechanistic assertion for the Lassa binding/entry observation and
      propagates it to the summary; this requires curation. No finding asserts that
      all retained effects are false or that Penitrem A never inhibits an enzyme.
    evidence_ids:
    - support-2870-source
    - support-2870-owner
    - support-2870-motifs
    - support-2870-filingpolicy
    - support-2870-gates
    - support-2870-assay-owner
    - support-2870-activitypolicy
    - support-2870-activityschema
    - support-2870-table-mibig_compounds
    - support-2870-table-lotus_occurrences
    - support-2870-table-npclassifier
    - support-2870-table-pubchem_bioassay
- assessment_id: support-2870-completion-assessment
  area: completeness
  topic: Earned work and unavailable authority
  summary: The complete owner, assigned source payloads, original intake and both
    saved forms were read. The complete owner has no causal_graphs, causal_graph_refs,
    biosynthetic_pathway, molecular_targets or components; no maintained reader applies.
    It retains 22 bioactivity observations and a generated activity summary, which
    are assessed separately. The separate Paxilline reader supplies no authority for
    this owner. One major open classification finding requires maintained-source curation.
    Five local gates pass; full QC, complete OAK and fresh primary/external verification
    are unavailable. Completion is partial and native SEEDED status is unchanged.
  outcome: concern
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  evidence_ids:
  - support-2870-intake
  - support-2870-intakeaccept
  - support-2870-plan
  - support-2870-planaccept
  - support-2870-notes
  - support-2870-gates
  - support-2870-data
  - support-2870-diagaccept
  - support-2870-scope
  - support-2870-assay-owner
  - support-2870-activitypolicy
  - support-2870-activityschema
  dimensions:
  - name: review_completion
    definition: Earned work does not replace unavailable authority or promote native
      status.
    value: The complete owner, assigned source payloads, original intake and both
      saved forms were read. The complete owner has no causal_graphs, causal_graph_refs,
      biosynthetic_pathway, molecular_targets or components; no maintained reader
      applies. It retains 22 bioactivity observations and a generated activity summary,
      which are assessed separately. The separate Paxilline reader supplies no authority
      for this owner. One major open classification finding requires maintained-source
      curation. Five local gates pass; full QC, complete OAK and fresh primary/external
      verification are unavailable. Completion is partial and native SEEDED status
      is unchanged.
    evidence_ids:
    - support-2870-intake
    - support-2870-intakeaccept
    - support-2870-plan
    - support-2870-planaccept
    - support-2870-notes
    - support-2870-gates
    - support-2870-data
    - support-2870-diagaccept
    - support-2870-scope
    - support-2870-assay-owner
    - support-2870-activitypolicy
    - support-2870-activityschema
findings:
- finding_id: support-2870-assay-classification
  issue_key: penitrem-a-generic-inhibition-classification
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Generic assay-title inference overstates enzyme inhibition
  description: AID 720533 is a retained active Lassa-virus binding/entry assay, but
    bioactivities[17].activity_class asserts ENZYME_INHIBITOR without an enzyme endpoint
    or grounded target. The maintained fallback classifies generic inhibition/binding
    wording and propagates active classes into bioactivity_summary, despite its own
    unambiguous-evidence policy. Cellular TDP1 AID 686978 and STK33 AID 2330 likewise
    require evidence-specific class review rather than a title-only direct biochemical
    mechanism. The confirmed defect is the local class inference, not the truth of
    source activity calls or a claim that Penitrem A never inhibits enzymes. Preserve
    all 22 observations, target variants, measurements and source provenance.
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  field_paths:
  - bioactivities[17].activity_class
  - bioactivities[19].activity_class
  - bioactivities[21].activity_class
  - bioactivity_summary
  evidence_ids:
  - support-2870-assay-owner
  - support-2870-activitypolicy
  - support-2870-activityschema
  - support-2870-table-pubchem_bioassay
  - support-2870-query-pubchem_bioassay
  - support-2870-source
  - support-2870-intake
  - support-2870-curation
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  ownership_note: The generated record derives this classification from scripts/seed_from_sources.py;
    correction belongs in the maintained generator and authorized regeneration, not
    a manual edit or blanket assay exclusion.
actions:
- action_id: support-2870-correct-class-inference
  description: Replace generic inhibition/binding-title promotion to ENZYME_INHIBITOR
    with evidence-specific classification in the maintained seeder. Keep valid binding/entry
    and cellular observations, source calls, Potency/OTHER values, absent numeric
    endpoints, target-presence variants and artifact-screen context. Leave activity_class
    unassigned or use an existing evidence-supported enum under policy; do not invent
    BINDING. Recompute the generated summary through the maintained regeneration workflow
    after curator review.
  finding_ids:
  - support-2870-assay-classification
  target_ids:
  - naturalproductmech:mibig-5942c19a89
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Maintained harmonization generator; seeded fields are corrected through
      maintained inputs and validated regeneration.
  ownership_note: The generated record derives this classification from scripts/seed_from_sources.py;
    correction belongs in the maintained generator and authorized regeneration, not
    a manual edit or blanket assay exclusion.
  acceptance_checks:
  - AID 720533 no longer asserts ENZYME_INHIBITOR solely from its viral binding/entry
    title; any retained class has appropriate evidence.
  - AIDs 686978 and 2330 receive explicit evidence-scoped review without treating
    cellular titles alone as direct biochemical inhibition.
  - All 22 source observations and 18 unique AIDs remain attributable; four duplicated-AID
    target variants are not counted as independent assays.
  - Four ACTIVE and eighteen NOT_DETERMINED calls remain intact; the reactive-artifact
    screen is retained with its scope, generic Potency stays OTHER and AID 2330 gains
    no invented endpoint/value.
  - Generated activity summary reflects only justified classes; current schema and
    canonical review checks pass after authorized regeneration.
limitations:
- Normalized identifiers, formula agreement and local parsing do not establish independent
  full graph identity, natural-sample identity, experimental absolute stereochemistry
  or primary biological validation.
- Both canonical SMILES comparisons are true and the saved chirality-aware map covers
  all atoms, but it is one limited substructure comparison. In every case full_graph_identity_established
  remains false. Both forms retain thirteen specified tetrahedral candidates and no
  other potential-stereo entry. The two terminal methylenes cannot carry ordinary
  E/Z assignment. The true source atom-centre flag and canonical agreement do not
  prove natural absolute stereochemistry or validate activity classification.
- Eight undefined-stereochemistry warning lines occur in the original 368-byte stderr.
  They are globally unattributed and are not assigned to any owner or form.
- Primary publications, spectra, sequence/function experiments, live taxonomy, full
  QC and complete OAK remain unavailable. Source grades are not upgraded.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Fresh batch 287 evidence and judgments; batch 286 supplies structural interface
  only.
- No record, native status or history was edited; no source query, molecular parse,
  target invocation or external request occurred in this lane.
- ROOT appends five actual local gate checks and three required unavailable checks.
  No maintained-reader check applies to these five owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-287
```
