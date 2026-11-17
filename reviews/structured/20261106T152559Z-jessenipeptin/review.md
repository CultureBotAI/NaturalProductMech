# Local evidence review: jessenipeptin

- Review: 20261106T152559Z-jessenipeptin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-06T14:21:26.897913Z
- Finished UTC: 2026-11-06T15:25:59.106651Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Jessenipeptin retains a cyclic depsipeptide/lipopeptide topology with twenty specified tetrahedral centers and two Z alkenes. Producer/locus grades and the no-assay-data sentinel remain literal; extensive amide/imidic representation differences do not establish a source defect.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2722; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-6e96262d73 | data/natural_products/unclassified/jessenipeptin.yaml | generated | jessenipeptin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original local two-form molecular diagnostic | passed | True | naturalproductmech:mibig-6e96262d73 | Both stored owner forms parsed in the original twenty-attempt diagnostic and share formula, charge, normalized InChI and declared full key. |
| strict_ten | passed | True | naturalproductmech:mibig-6e96262d73 | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-6e96262d73 | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-6e96262d73 | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-6e96262d73 | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-6e96262d73 | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-6e96262d73 | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-6e96262d73 | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-6e96262d73 | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Exact full-key identity and source-concept boundaries

identity: supported. Targets: naturalproductmech:mibig-6e96262d73.

Jessenipeptin retains full key RCRYELMDBHQIMX-JRGFPVMHSA-N and BGC0001629 compound 1, with source CID145720625. Both accepted forms reproduce that complete key and C91H148N20O24. This supports the selected retained structure mapping without new natural-identity or primary-assay certification.

### Stored molecular forms and stereochemical scope

representation: supported. Targets: naturalproductmech:mibig-6e96262d73.

The stored topology has a 16-membered ester-containing macrocycle, a five-membered N ring and a six-membered aromatic ring, together with a long acyl chain. The ester is C102(=O103)-O101-C100 in the SMILES table; the remaining free primary amine is N123. The reconstructed ester is C90(=O133)-O134-C55 and free amine N91. Ring size is not a residue count or a sequence assignment. Both forms retain twenty specified tetrahedral centers and two Z alkenes. Eighteen added unspecified C=N entries are confined to the reconstructed imidic representation; no new atom-centered source stereo defect follows. Both neutral C91H148N20O24 forms agree in normalized InChI/full key and counts. Carbonyl sites decrease20 to2 and amide sites19 to1; eighteen terminal C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained carbonyls are the proline-associated amide and the ester. Exact canonical graphs differ and the one-way atom map is empty.

### Producer assertion versus locus evidence

provenance: supported. Targets: naturalproductmech:mibig-6e96262d73.

Pseudomonas sp. QS1027 NCBITaxon:2056244 retains BGC_CHARACTERIZED producer evidence. The separate LOTUS Pseudomonas NCBITaxon:286 occurrence is a genus-level assertion and cannot substitute for the strain claim. BGC0001629 version3 is active/questionable/complete and names MT505440.1 with CLUSTER_DEMONSTRATED / Knock-out studies, without locus coordinates. This is retained entry-level evidence, not a newly read molecule-specific knockout result.

### Citation grain and attributed history

evidence: supported. Targets: naturalproductmech:mibig-6e96262d73.

ENTRY DOI:10.1073/pnas.1721790115 is retained for the MIBiG producer/locus assertions; the LOTUS uppercase DOI is the same citation at occurrence grain. Both history events are attributed to seed_from_sources. No primary-paper or knockout data were newly inspected.

### Occurrence and bounded assay/target evidence

evidence: supported. Targets: naturalproductmech:mibig-6e96262d73.

One LOTUS Pseudomonas NCBITaxon:286 occurrence cites the same PNAS DOI. It is not a separate strain identification or independent production experiment. The PubChem row for CID145720625 has a blank AID, literal (no assay data), and blank activity, target and reference fields. It is a no-data sentinel, not an inactive assay, actual AID or applicable exclusion. Other target/activity frames are empty.

### Computed filing and asserted class applicability

consistency: supported. Targets: naturalproductmech:mibig-6e96262d73.

The cyclic ester-containing peptide architecture and long acyl chain provide positive structural support for the predicted Cyclic peptides&#124;Depsipeptides&#124;Lipopeptides classes. Absence of C5O candidate rings is consistent with the retained glycoside=false at this limited scope. NRPS/Type I remains the source assertion; model labels do not prove residue sequence or genetic mechanism. The 2 computed pathway labels are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased classification.

### Local completion and maintained ownership

completeness: unknown. Targets: naturalproductmech:mibig-6e96262d73.

Whole owner/history, all nine saved query frames (4 positive rows/49 fields) and both complete saved molecular forms were personally read. The 44 actual input hashes and explicit ownership declarations were verified; this does not claim whole-corpus semantic reading. Five required local native commands passed, while full QC/OAK, live authority and independent primary verification remain unavailable. No selected graph/pathway/component or molecular-target root requires a maintained reader for this owner. Corrections belong in maintained inputs, implemented curation tables, extractors or the seeder; no record edit is proposed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bgc-2722-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/jessenipeptin.yaml; Complete plaintext and all curation_history entries | supports | Whole current owner/history was personally read; source assertions and curated mechanism annotations remain attributed. |
| bgc-2722-identity | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/1/owner_document/identifier; /records/1/owner_document/chemical_structure; /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status | supports | Jessenipeptin retains full key RCRYELMDBHQIMX-JRGFPVMHSA-N and BGC0001629 compound 1, with source CID145720625. Both accepted forms reproduce that complete key and C91H148N20O24. This supports the selected retained structure mapping without new natural-identity or primary-assay certification. |
| bgc-2722-history | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/1/owner_document/curation_history | supports | ENTRY DOI:10.1073/pnas.1721790115 is retained for the MIBiG producer/locus assertions; the LOTUS uppercase DOI is the same citation at occurrence grain. Both history events are attributed to seed_from_sources. No primary-paper or knockout data were newly inspected. |
| bgc-2722-provenance | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters | supports | Pseudomonas sp. QS1027 NCBITaxon:2056244 retains BGC_CHARACTERIZED producer evidence. The separate LOTUS Pseudomonas NCBITaxon:286 occurrence is a genus-level assertion and cannot substitute for the strain claim. BGC0001629 version3 is active/questionable/complete and names MT505440.1 with CLUSTER_DEMONSTRATED / Knock-out studies, without locus coordinates. This is retained entry-level evidence, not a newly read molecule-specific knockout result. |
| bgc-2722-classification | /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json; /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway; /records/1/owner_document/bgc_class | supports | The cyclic ester-containing peptide architecture and long acyl chain provide positive structural support for the predicted Cyclic peptides&#124;Depsipeptides&#124;Lipopeptides classes. Absence of C5O candidate rings is consistent with the retained glycoside=false at this limited scope. NRPS/Type I remains the source assertion; model labels do not prove residue sequence or genetic mechanism. The 2 computed pathway labels are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased classification. |
| bgc-2722-roots | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/complete_root_keys; /contexts/4/declared_mechanism_roots_literal; /contexts/4/literal_bioactivities_root | context_only | Whole captured root set has no declared mechanism, component or measured bioactivity/target root. |
| bgc-2722-chemistry | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-DATA-001.json; /records/1/smiles/computed; /records/1/inchi/computed; /records/1/comparisons; /records/1/atom_correspondence; /records/1/literal_InChI_layers | supports | The stored topology has a 16-membered ester-containing macrocycle, a five-membered N ring and a six-membered aromatic ring, together with a long acyl chain. The ester is C102(=O103)-O101-C100 in the SMILES table; the remaining free primary amine is N123. The reconstructed ester is C90(=O133)-O134-C55 and free amine N91. Ring size is not a residue count or a sequence assignment. Both forms retain twenty specified tetrahedral centers and two Z alkenes. Eighteen added unspecified C=N entries are confined to the reconstructed imidic representation; no new atom-centered source stereo defect follows. Both neutral C91H148N20O24 forms agree in normalized InChI/full key and counts. Carbonyl sites decrease20 to2 and amide sites19 to1; eighteen terminal C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained carbonyls are the proline-associated amide and the ester. Exact canonical graphs differ and the one-way atom map is empty. |
| bgc-2722-molecular-reading | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-first-five-molecular-intake-reading-001.json; /records/1; /scope; /warnings_scope | supports | Complete saved atom/bond/ring/stereo/motif and mapping reading is independently attributed here; no new parse or primary source row credit. |
| bgc-2722-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/root-diagnostic-acceptance-001.json; /status; /accepted; /full_graph_identity_established | supports | ROOT accepted the one original twenty-form diagnostic; full graph identity remains false. |
| bgc-2722-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-execution-001.json; /command; /exit_code | supports | Exact original command and zero exit are retained without executing it again. |
| bgc-2722-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-original-001.stderr; Complete original stderr; four nonempty warning lines | context_only | Four omitted-undefined-stereo warnings are preserved globally without assigning them to any owner. |
| bgc-2722-intake | /private/tmp/npm-review-work/shared-next-batch273/intakes-001/2722-inspect-001.json; /targets; /source/inputs | supports | One exact target, 44 current input hashes and explicit maintained ownership declarations. |
| bgc-2722-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch273/root-intake-acceptance-001.json; /status; /accepted; /input_placements; /unique_input_paths | supports | ROOT accepted the ten actual canonical inspections with468 input placements/60 unique paths. |
| bgc-2722-plan | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-target-input-plan-001.json; /records/1 | supports | Current accepted exact input and direct-companion scope; presence alone confers no scientific proof. |
| bgc-2722-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch273/root-current273-source-plan-acceptance-001.json; /status; /accepted | supports | ROOT accepted the original plan after attributed source reading. |
| bgc-2722-gates | /private/tmp/npm-native-checks/batch-273/root-five-gates-acceptance-001.json; /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates; /selected_queue_snapshot | context_only | Five local native commands passed; full QC/OAK remain unavailable and queue entries are leads only. |
| bgc-2722-source-reading | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-assigned-source-reading-001.json; /contexts/4; /totals; /row_attribution | supports | Complete assigned saved dictionaries, physical rows and negative predicates were personally read; final molecular/reader meanings are supplied by the later actual artifacts. |
| bgc-2722-source-notes | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-scope-notes-001.json; /totals; /reading_reconciliation; /cautions | context_only | Disjoint source credit is23 BGC plus24 Support rows and zero Native/ROOT primary rows; this review uses its exact selected subset. |
| bgc-2722-taxonomy | /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-cached-taxonomy-reading-001.json; /scope; /interpretation; /context_interpretations | context_only | Eleven retained stanzas and fifteen exact routes were read, with no forward merge/nonorganism/unmatched route. Generic and strain labels remain separate. |
| bgc-2722-curation | /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json; /scope; /counts; /applied_rows; /interpretation | context_only | Nine substantive tables/3422 rows yield zero lexical candidates and zero applicable exact predicates. Census-only extra tables confer no scientific input credit. |
| bgc-2722-assay-curation | /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json; /assay_scope | context_only | The PubChem row for CID145720625 has a blank AID, literal (no assay data), and blank activity, target and reference fields. It is a no-data sentinel, not an inactive assay, actual AID or applicable exclusion. Other target/activity frames are empty. |
| bgc-2722-stereo-policy | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; lines165-172: FindMolChiralCenters includeUnassigned | context_only | The MIBiG stereo_complete flag tests unassigned atom-centered chirality; reconstructed imidic-double geometry is a separate representation issue. |
| bgc-2722-filing-policy | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; lines295-306: choose_pathway | context_only | The 2 computed pathway labels are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased classification. |
| bgc-2722-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/mibig_compounds | supports | Complete saved mibig_compounds frame: 1 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-row-mibig_compounds-0 | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; physical lines 1952-1952; raw record sha256 8c0bf60c0310f7522e50bf236aa0e6c841f4712cea0714301def37523c37f99d | supports | All 25 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2722-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_structures | context_only | Complete saved chebi_structures frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/lotus_occurrences | supports | Complete saved lotus_occurrences frame: 1 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-row-lotus_occurrences-0 | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; physical lines 7638-7638; raw record sha256 0a68587b4956a77e3298f415c51807d176cbc9d1f46f4f9fbbd5adffc9783e15 | supports | All 6 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2722-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences | context_only | Complete saved cyanometdb_occurrences frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/npclassifier | supports | Complete saved npclassifier frame: 1 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-row-npclassifier-0 | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; physical lines 2086-2086; raw record sha256 a34622731959edc850978ea5724ce797336d9f9b226e5978b7e97274fba42551 | supports | All 7 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2722-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/pubchem_bioassay | supports | Complete saved pubchem_bioassay frame: 1 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-row-pubchem_bioassay-0 | /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv; physical lines 6100-6100; raw record sha256 5e99656fc8f382316654d143285548dda9183924d590518c9a267759485cb755 | supports | All 11 fields of this retained source row were personally read and exactly joined; citation/evidence grain remains literal. |
| bgc-2722-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/bindingdb_targets | context_only | Complete saved bindingdb_targets frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys | context_only | Complete saved antibioticmech_inchikeys frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| bgc-2722-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json; /contexts/4/source_scope_inventory/joins/chebi_origins | context_only | Complete saved chebi_origins frame: 0 positive placements; every returned field and the bounded negative predicate were read. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-273/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-273/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-273/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-273/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-273/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained source rows, grades and history were read; cited primary papers and live identity/taxonomy resources were not newly verified. Full QC and OAK remain unavailable under the no-outbound hold.
- Both neutral C91H148N20O24 forms agree in normalized InChI/full key and counts. Carbonyl sites decrease20 to2 and amide sites19 to1; eighteen terminal C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained carbonyls are the proline-associated amide and the ester. Exact canonical graphs differ and the one-way atom map is empty. Four original omitted-undefined-stereo warnings remain globally unassigned.
- Ring, amide, ester and C5O/bridge predicates provide local topology; they do not assign natural residues, all stereochemical details, enzyme functions or assay activity.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- All current conclusions are scoped to this exact owner and its captured inputs; retained source status remains unchanged.
- No repair, source mutation, external request or new molecular parse was performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261106T152559Z-jessenipeptin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: jessenipeptin'
started_at: '2026-11-06T14:21:26.897913Z'
finished_at: '2026-11-06T15:25:59.106651Z'
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
summary: Jessenipeptin retains a cyclic depsipeptide/lipopeptide topology with twenty
  specified tetrahedral centers and two Z alkenes. Producer/locus grades and the no-assay-data
  sentinel remain literal; extensive amide/imidic representation differences do not
  establish a source defect.
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
  - path: data/natural_products/unclassified/jessenipeptin.yaml
    sha256: 136dc5db69d68f8f5d0395115a9a9d322bfea77d0b25ee709b8164ba6c4825d6
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
  selection: Campaign path order 2722; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-6e96262d73
targets:
- target_id: naturalproductmech:mibig-6e96262d73
  path: data/natural_products/unclassified/jessenipeptin.yaml
  label: jessenipeptin
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
  ownership_note: This review proposes no record edit. Source corrections belong in
    maintained inventories, implemented curation tables, extractors or the seeder;
    generated pages are not owners.
checks:
- check_id: local-molecular-diagnostic
  name: Original local two-form molecular diagnostic
  command: /private/tmp/npm-record-reviews-20261021/.venv/bin/python -I -S -B /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnose273-001.py
    eef60eba394bf43b8ac3d4ed93ea024d47f231ec4dd051d571c8a865b7b78261 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
    92c35f8754f5db35ac73a3bf2f48f63b286fd6378e915892bbbabdd17fba19f7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  summary: Both stored owner forms parsed in the original twenty-attempt diagnostic
    and share formula, charge, normalized InChI and declared full key.
  scope_note: Both neutral C91H148N20O24 forms agree in normalized InChI/full key
    and counts. Carbonyl sites decrease20 to2 and amide sites19 to1; eighteen terminal
    C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained carbonyls
    are the proline-associated amide and the ester. Exact canonical graphs differ
    and the one-way atom map is empty. Four original omitted-undefined-stereo warnings
    remain globally unassigned. No exact full graph, natural identity or primary biological
    certification follows.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-chemistry
  - bgc-2722-diagnostic-acceptance
  - bgc-2722-diagnostic-execution
  - bgc-2722-diagnostic-stderr
- check_id: root-native-strict_ten
  name: strict_ten
  status: passed
  required: true
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  command: just validate-strict data/natural_products/unclassified/jamaicamide-c.yaml
    data/natural_products/unclassified/jessenipeptin.yaml data/natural_products/unclassified/keanumycin-a.yaml
    data/natural_products/unclassified/keanumycin-b.yaml data/natural_products/unclassified/kedarcidin.yaml
    data/natural_products/unclassified/kirromycin.yaml data/natural_products/unclassified/kitacinnamycin-a.yaml
    data/natural_products/unclassified/kitacinnamycin-b.yaml data/natural_products/unclassified/kitacinnamycin-c.yaml
    data/natural_products/unclassified/kitacinnamycin-d.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-273/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-6e96262d73
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-273/validate-all-001.tsv
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
  - naturalproductmech:mibig-6e96262d73
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
  - naturalproductmech:mibig-6e96262d73
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
  - naturalproductmech:mibig-6e96262d73
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-273/review-queue-001.tsv
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
  - naturalproductmech:mibig-6e96262d73
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: bgc-2722-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/jessenipeptin.yaml
  locator: Complete plaintext and all curation_history entries
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Whole current owner/history was personally read; source assertions and
    curated mechanism annotations remain attributed.
  snapshot_sha256: 136dc5db69d68f8f5d0395115a9a9d322bfea77d0b25ee709b8164ba6c4825d6
- evidence_id: bgc-2722-identity
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/1/owner_document/identifier; /records/1/owner_document/chemical_structure;
    /records/1/owner_document/source_concepts; /records/1/owner_document/grounding_status
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Jessenipeptin retains full key RCRYELMDBHQIMX-JRGFPVMHSA-N and BGC0001629
    compound 1, with source CID145720625. Both accepted forms reproduce that complete
    key and C91H148N20O24. This supports the selected retained structure mapping without
    new natural-identity or primary-assay certification.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2722-history
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/1/owner_document/curation_history
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ENTRY DOI:10.1073/pnas.1721790115 is retained for the MIBiG producer/locus
    assertions; the LOTUS uppercase DOI is the same citation at occurrence grain.
    Both history events are attributed to seed_from_sources. No primary-paper or knockout
    data were newly inspected.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2722-provenance
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/1/owner_document/producer_organisms; /records/1/owner_document/biosynthetic_gene_clusters
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Pseudomonas sp. QS1027 NCBITaxon:2056244 retains BGC_CHARACTERIZED producer
    evidence. The separate LOTUS Pseudomonas NCBITaxon:286 occurrence is a genus-level
    assertion and cannot substitute for the strain claim. BGC0001629 version3 is active/questionable/complete
    and names MT505440.1 with CLUSTER_DEMONSTRATED / Knock-out studies, without locus
    coordinates. This is retained entry-level evidence, not a newly read molecule-specific
    knockout result.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2722-classification
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273/owner-capture-DATA-001.json
  locator: /records/1/owner_document/np_classification; /records/1/owner_document/np_pathway;
    /records/1/owner_document/bgc_class
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: The cyclic ester-containing peptide architecture and long acyl chain provide
    positive structural support for the predicted Cyclic peptides|Depsipeptides|Lipopeptides
    classes. Absence of C5O candidate rings is consistent with the retained glycoside=false
    at this limited scope. NRPS/Type I remains the source assertion; model labels
    do not prove residue sequence or genetic mechanism. The 2 computed pathway labels
    are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent
    filing, not biological absence or an erased classification.
  snapshot_sha256: 138df5989225a8efe6a8715fbf4b19cd0e8e5ed6b75ca32a63b51c24ad8fb6c4
- evidence_id: bgc-2722-roots
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/complete_root_keys; /contexts/4/declared_mechanism_roots_literal;
    /contexts/4/literal_bioactivities_root
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Whole captured root set has no declared mechanism, component or measured
    bioactivity/target root.
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: Exact whole current owner root set; no activity or mechanism transfer
    from companion records.
- evidence_id: bgc-2722-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-DATA-001.json
  locator: /records/1/smiles/computed; /records/1/inchi/computed; /records/1/comparisons;
    /records/1/atom_correspondence; /records/1/literal_InChI_layers
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: The stored topology has a 16-membered ester-containing macrocycle, a five-membered
    N ring and a six-membered aromatic ring, together with a long acyl chain. The
    ester is C102(=O103)-O101-C100 in the SMILES table; the remaining free primary
    amine is N123. The reconstructed ester is C90(=O133)-O134-C55 and free amine N91.
    Ring size is not a residue count or a sequence assignment. Both forms retain twenty
    specified tetrahedral centers and two Z alkenes. Eighteen added unspecified C=N
    entries are confined to the reconstructed imidic representation; no new atom-centered
    source stereo defect follows. Both neutral C91H148N20O24 forms agree in normalized
    InChI/full key and counts. Carbonyl sites decrease20 to2 and amide sites19 to1;
    eighteen terminal C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained
    carbonyls are the proline-associated amide and the ester. Exact canonical graphs
    differ and the one-way atom map is empty.
  snapshot_sha256: 0458568ea55f029d20f51b75bae21b1e1be822c1a62c95bf0764118349b3b024
- evidence_id: bgc-2722-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-first-five-molecular-intake-reading-001.json
  locator: /records/1; /scope; /warnings_scope
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Complete saved atom/bond/ring/stereo/motif and mapping reading is independently
    attributed here; no new parse or primary source row credit.
  snapshot_sha256: 8f5b3160d02aef0a71df7a89cc19ec3ef32d0d6542c3c11fb881ae1334ba18c4
- evidence_id: bgc-2722-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /accepted; /full_graph_identity_established
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ROOT accepted the one original twenty-form diagnostic; full graph identity
    remains false.
  snapshot_sha256: 4958a99eeb26cfffbd8c333ef1c3ee720875ff468d51026a3b08590c9cfce39e
- evidence_id: bgc-2722-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Exact original command and zero exit are retained without executing it
    again.
  snapshot_sha256: 19f0309e060cd114e107dee98d301154b18130d166db4b12f2f1fc1ecce48cf6
- evidence_id: bgc-2722-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/chemistry-local/diagnostic-original-001.stderr
  locator: Complete original stderr; four nonempty warning lines
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Four omitted-undefined-stereo warnings are preserved globally without assigning
    them to any owner.
  snapshot_sha256: 1983ffbdc45b00739a943c2031ce64f65d27e1b5c9e3a058936e4d4ec2ddc57a
- evidence_id: bgc-2722-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/intakes-001/2722-inspect-001.json
  locator: /targets; /source/inputs
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: One exact target, 44 current input hashes and explicit maintained ownership
    declarations.
  snapshot_sha256: 01beffb649c479cde58b95ebe4e54e5260a75cf7a9b47fd02ee5723c1a95cc9d
- evidence_id: bgc-2722-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/root-intake-acceptance-001.json
  locator: /status; /accepted; /input_placements; /unique_input_paths
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ROOT accepted the ten actual canonical inspections with468 input placements/60
    unique paths.
  snapshot_sha256: a68ca1cf0788a294ae06506515c973dcebe06ce4d0d280cdbce713be0a0f2278
- evidence_id: bgc-2722-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-target-input-plan-001.json
  locator: /records/1
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Current accepted exact input and direct-companion scope; presence alone
    confers no scientific proof.
  snapshot_sha256: 37a2529c76339bea20b2c862c7a09ce11dd909d4a69623ba4f8914026c771cf4
- evidence_id: bgc-2722-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch273/root-current273-source-plan-acceptance-001.json
  locator: /status; /accepted
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: ROOT accepted the original plan after attributed source reading.
  snapshot_sha256: 678b0919f00212e2f1140491aa5ce980685261662e4f336d19fb01fb46d1ed26
- evidence_id: bgc-2722-gates
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/root-five-gates-acceptance-001.json
  locator: /five_local_commands_passed; /all_native_gates_passed; /unavailable_required_gates;
    /selected_queue_snapshot
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Five local native commands passed; full QC/OAK remain unavailable and queue
    entries are leads only.
  snapshot_sha256: a98bb4066024289ac97d3274aadccfb96d4d4068f9a6168c3ba9e2ff7b39ca6b
- evidence_id: bgc-2722-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-current273-assigned-source-reading-001.json
  locator: /contexts/4; /totals; /row_attribution
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: Complete assigned saved dictionaries, physical rows and negative predicates
    were personally read; final molecular/reader meanings are supplied by the later
    actual artifacts.
  snapshot_sha256: 3b530e67d54edcc3b5a56f3ca7bc7d25e642f8d44e73d5db22b00202a1a0d175
- evidence_id: bgc-2722-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-scope-notes-001.json
  locator: /totals; /reading_reconciliation; /cautions
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Disjoint source credit is23 BGC plus24 Support rows and zero Native/ROOT
    primary rows; this review uses its exact selected subset.
  snapshot_sha256: 7d3af448ee3538d1c078e1f22263097ac13a4d83d3f4192854724c31d6a8eb86
- evidence_id: bgc-2722-taxonomy
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-cached-taxonomy-reading-001.json
  locator: /scope; /interpretation; /context_interpretations
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Eleven retained stanzas and fifteen exact routes were read, with no forward
    merge/nonorganism/unmatched route. Generic and strain labels remain separate.
  snapshot_sha256: 6f4cd7f16a6f8b2e82152f6a274f5b9b139808f8a7845e8912ac4e4538bb7b26
  search_scope: Current cached source labels and exact route predicates only; no fresh
    rank, lineage, strain or OAK result.
- evidence_id: bgc-2722-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json
  locator: /scope; /counts; /applied_rows; /interpretation
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: Nine substantive tables/3422 rows yield zero lexical candidates and zero
    applicable exact predicates. Census-only extra tables confer no scientific input
    credit.
  snapshot_sha256: 61175b3c187b89ef171b28e839d743a6f7e58bddaf5e67dfb64864d62653c966
  search_scope: Current273 bounded identity/source tokens and retained implemented
    predicates; no decision applied.
- evidence_id: bgc-2722-assay-curation
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/native-prep/native-current273-implemented-curation-scan-001.json
  locator: /assay_scope
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: The PubChem row for CID145720625 has a blank AID, literal (no assay data),
    and blank activity, target and reference fields. It is a no-data sentinel, not
    an inactive assay, actual AID or applicable exclusion. Other target/activity frames
    are empty.
  snapshot_sha256: 61175b3c187b89ef171b28e839d743a6f7e58bddaf5e67dfb64864d62653c966
  search_scope: Zero actual AIDs; batch has two blank sentinels, Jessenipeptin and
    Kirromycin. Exact fifteen exclusion decisions cannot transfer without their full
    predicates.
- evidence_id: bgc-2722-stereo-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: 'lines165-172: FindMolChiralCenters includeUnassigned'
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: The MIBiG stereo_complete flag tests unassigned atom-centered chirality;
    reconstructed imidic-double geometry is a separate representation issue.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: bgc-2722-filing-policy
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: 'lines295-306: choose_pathway'
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: The 2 computed pathway labels are retained while choose_pathway files this
    owner UNCLASSIFIED. This is consistent filing, not biological absence or an erased
    classification.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: bgc-2722-query-mibig_compounds
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved mibig_compounds frame: 1 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2722-row-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: physical lines 1952-1952; raw record sha256 8c0bf60c0310f7522e50bf236aa0e6c841f4712cea0714301def37523c37f99d
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 25 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: bgc-2722-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved chebi_structures frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/jessenipeptin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RCRYELMDBHQIMX-JRGFPVMHSA-N",
    "table": "chebi_structures"}'
- evidence_id: bgc-2722-query-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved lotus_occurrences frame: 1 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2722-row-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: physical lines 7638-7638; raw record sha256 0a68587b4956a77e3298f415c51807d176cbc9d1f46f4f9fbbd5adffc9783e15
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 6 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: bgc-2722-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved cyanometdb_occurrences frame: 0 positive placements; every
    returned field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/jessenipeptin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RCRYELMDBHQIMX-JRGFPVMHSA-N",
    "table": "cyanometdb_occurrences"}'
- evidence_id: bgc-2722-query-npclassifier
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved npclassifier frame: 1 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2722-row-npclassifier-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: physical lines 2086-2086; raw record sha256 a34622731959edc850978ea5724ce797336d9f9b226e5978b7e97274fba42551
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 7 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: bgc-2722-query-pubchem_bioassay
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: 'Complete saved pubchem_bioassay frame: 1 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
- evidence_id: bgc-2722-row-pubchem_bioassay-0
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/pubchem_bioassay.tsv
  locator: physical lines 6100-6100; raw record sha256 5e99656fc8f382316654d143285548dda9183924d590518c9a267759485cb755
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: supports
  summary: All 11 fields of this retained source row were personally read and exactly
    joined; citation/evidence grain remains literal.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: bgc-2722-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved bindingdb_targets frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/jessenipeptin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RCRYELMDBHQIMX-JRGFPVMHSA-N",
    "table": "bindingdb_targets"}'
- evidence_id: bgc-2722-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved antibioticmech_inchikeys frame: 0 positive placements;
    every returned field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/jessenipeptin.yaml",
    "predicate": "exact complete standard_inchi_key equality", "query": "RCRYELMDBHQIMX-JRGFPVMHSA-N",
    "table": "antibioticmech_inchikeys"}'
- evidence_id: bgc-2722-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch273-tentative/bgc-prep/bgc-conditional273-source-inventory-DATA-001.json
  locator: /contexts/4/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-06T15:08:32.841356Z'
  support: context_only
  summary: 'Complete saved chebi_origins frame: 0 positive placements; every returned
    field and the bounded negative predicate were read.'
  snapshot_sha256: 29636774bbc4a41b6d1ad865639fc2c3feb1e4de60edb6aabf88571ec665654a
  search_scope: '{"matches": 0, "owner": "data/natural_products/unclassified/jessenipeptin.yaml",
    "predicate": "exact chebi_id from exact full-key structure rows", "query": [],
    "table": "chebi_origins"}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:27:07.176543Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 43fcdede3e42b4a8cbfdd8d20ede685766c071c094bfffde0b3540840ec32dd5
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:27:32.867288Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: 680d286e5b6524c522d17e6143f9f5738389cdf8d006a5de216a5266c72fe77f
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:27:53.047300Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:28:27.995571Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-273/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-273/native-current273-five-gates-execution-001.json
  accessed_at: '2026-11-06T14:28:40.232102Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: cd75bfb4b51e32cf7d9e268e520b8869e68b5463e2da44f5b1e2f6c68ee26d09
assessments:
- assessment_id: bgc-2722-identity
  area: identity
  topic: Exact full-key identity and source-concept boundaries
  outcome: supported
  summary: Jessenipeptin retains full key RCRYELMDBHQIMX-JRGFPVMHSA-N and BGC0001629
    compound 1, with source CID145720625. Both accepted forms reproduce that complete
    key and C91H148N20O24. This supports the selected retained structure mapping without
    new natural-identity or primary-assay certification.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-identity
  - bgc-2722-chemistry
  - bgc-2722-query-mibig_compounds
  - bgc-2722-query-chebi_structures
  - bgc-2722-plan
  - bgc-2722-row-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    definition: Exact complete retained key; connectivity blocks alone do not identify
      a congener.
    value: RCRYELMDBHQIMX-JRGFPVMHSA-N
    evidence_ids:
    - bgc-2722-identity
    - bgc-2722-chemistry
    - bgc-2722-query-mibig_compounds
    - bgc-2722-query-chebi_structures
    - bgc-2722-plan
    - bgc-2722-row-mibig_compounds-0
  - name: grounding_scope
    definition: Selected identifier and source concepts, with unresolved naming and
      comparison boundaries.
    value: Jessenipeptin retains full key RCRYELMDBHQIMX-JRGFPVMHSA-N and BGC0001629
      compound 1, with source CID145720625. Both accepted forms reproduce that complete
      key and C91H148N20O24. This supports the selected retained structure mapping
      without new natural-identity or primary-assay certification.
    evidence_ids:
    - bgc-2722-identity
    - bgc-2722-chemistry
    - bgc-2722-query-mibig_compounds
    - bgc-2722-query-chebi_structures
    - bgc-2722-plan
    - bgc-2722-row-mibig_compounds-0
- assessment_id: bgc-2722-representation
  area: representation
  topic: Stored molecular forms and stereochemical scope
  outcome: supported
  summary: The stored topology has a 16-membered ester-containing macrocycle, a five-membered
    N ring and a six-membered aromatic ring, together with a long acyl chain. The
    ester is C102(=O103)-O101-C100 in the SMILES table; the remaining free primary
    amine is N123. The reconstructed ester is C90(=O133)-O134-C55 and free amine N91.
    Ring size is not a residue count or a sequence assignment. Both forms retain twenty
    specified tetrahedral centers and two Z alkenes. Eighteen added unspecified C=N
    entries are confined to the reconstructed imidic representation; no new atom-centered
    source stereo defect follows. Both neutral C91H148N20O24 forms agree in normalized
    InChI/full key and counts. Carbonyl sites decrease20 to2 and amide sites19 to1;
    eighteen terminal C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained
    carbonyls are the proline-associated amide and the ester. Exact canonical graphs
    differ and the one-way atom map is empty.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-identity
  - bgc-2722-chemistry
  - bgc-2722-molecular-reading
  - bgc-2722-diagnostic-acceptance
  - bgc-2722-diagnostic-stderr
  - bgc-2722-stereo-policy
  dimensions:
  - name: stereochemistry_scope
    definition: Specified and unspecified saved stereochemical features, including
      implementation limits of stereo_complete.
    value: Both forms retain twenty specified tetrahedral centers and two Z alkenes.
      Eighteen added unspecified C=N entries are confined to the reconstructed imidic
      representation; no new atom-centered source stereo defect follows.
    evidence_ids:
    - bgc-2722-identity
    - bgc-2722-chemistry
    - bgc-2722-molecular-reading
    - bgc-2722-diagnostic-acceptance
    - bgc-2722-diagnostic-stderr
    - bgc-2722-stereo-policy
  - name: representation_correspondence
    definition: Actual two-form comparisons and limited atom mapping, without full
      graph or natural-identity certification.
    value: Both neutral C91H148N20O24 forms agree in normalized InChI/full key and
      counts. Carbonyl sites decrease20 to2 and amide sites19 to1; eighteen terminal
      C(OH)=N sites appear, each with O degree1/H1 and N H0. The retained carbonyls
      are the proline-associated amide and the ester. Exact canonical graphs differ
      and the one-way atom map is empty.
    evidence_ids:
    - bgc-2722-identity
    - bgc-2722-chemistry
    - bgc-2722-molecular-reading
    - bgc-2722-diagnostic-acceptance
    - bgc-2722-diagnostic-stderr
    - bgc-2722-stereo-policy
- assessment_id: bgc-2722-provenance
  area: provenance
  topic: Producer assertion versus locus evidence
  outcome: supported
  summary: Pseudomonas sp. QS1027 NCBITaxon:2056244 retains BGC_CHARACTERIZED producer
    evidence. The separate LOTUS Pseudomonas NCBITaxon:286 occurrence is a genus-level
    assertion and cannot substitute for the strain claim. BGC0001629 version3 is active/questionable/complete
    and names MT505440.1 with CLUSTER_DEMONSTRATED / Knock-out studies, without locus
    coordinates. This is retained entry-level evidence, not a newly read molecule-specific
    knockout result.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-provenance
  - bgc-2722-query-mibig_compounds
  - bgc-2722-taxonomy
  - bgc-2722-curation
  - bgc-2722-row-mibig_compounds-0
  dimensions:
  - name: taxon_scope
    definition: Exact retained taxon labels, IDs and rank/strain limits.
    value: Pseudomonas sp. QS1027 NCBITaxon:2056244 retains BGC_CHARACTERIZED producer
      evidence. The separate LOTUS Pseudomonas NCBITaxon:286 occurrence is a genus-level
      assertion and cannot substitute for the strain claim.
    evidence_ids:
    - bgc-2722-provenance
    - bgc-2722-query-mibig_compounds
    - bgc-2722-taxonomy
    - bgc-2722-curation
    - bgc-2722-row-mibig_compounds-0
  - name: producer_evidence
    definition: Producer evidence grade and its demonstrated or asserted scope.
    value: Pseudomonas sp. QS1027 NCBITaxon:2056244 retains BGC_CHARACTERIZED producer
      evidence. The separate LOTUS Pseudomonas NCBITaxon:286 occurrence is a genus-level
      assertion and cannot substitute for the strain claim.
    evidence_ids:
    - bgc-2722-provenance
    - bgc-2722-query-mibig_compounds
    - bgc-2722-taxonomy
    - bgc-2722-curation
    - bgc-2722-row-mibig_compounds-0
  - name: locus_evidence
    definition: Compound-linked BGC and locus fields with literal evidence grade and
      methods.
    value: BGC0001629 version3 is active/questionable/complete and names MT505440.1
      with CLUSTER_DEMONSTRATED / Knock-out studies, without locus coordinates. This
      is retained entry-level evidence, not a newly read molecule-specific knockout
      result.
    evidence_ids:
    - bgc-2722-provenance
    - bgc-2722-query-mibig_compounds
    - bgc-2722-taxonomy
    - bgc-2722-curation
    - bgc-2722-row-mibig_compounds-0
- assessment_id: bgc-2722-citations
  area: evidence
  topic: Citation grain and attributed history
  outcome: supported
  summary: ENTRY DOI:10.1073/pnas.1721790115 is retained for the MIBiG producer/locus
    assertions; the LOTUS uppercase DOI is the same citation at occurrence grain.
    Both history events are attributed to seed_from_sources. No primary-paper or knockout
    data were newly inspected.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-history
  - bgc-2722-provenance
  - bgc-2722-source-reading
  - bgc-2722-query-mibig_compounds
  - bgc-2722-row-mibig_compounds-0
  dimensions:
  - name: citation_scope
    definition: Citation grain and attributed history, separate from newly read primary
      evidence.
    value: ENTRY DOI:10.1073/pnas.1721790115 is retained for the MIBiG producer/locus
      assertions; the LOTUS uppercase DOI is the same citation at occurrence grain.
      Both history events are attributed to seed_from_sources. No primary-paper or
      knockout data were newly inspected.
    evidence_ids:
    - bgc-2722-history
    - bgc-2722-provenance
    - bgc-2722-source-reading
    - bgc-2722-query-mibig_compounds
    - bgc-2722-row-mibig_compounds-0
- assessment_id: bgc-2722-occurrence_activity
  area: evidence
  topic: Occurrence and bounded assay/target evidence
  outcome: supported
  summary: One LOTUS Pseudomonas NCBITaxon:286 occurrence cites the same PNAS DOI.
    It is not a separate strain identification or independent production experiment.
    The PubChem row for CID145720625 has a blank AID, literal (no assay data), and
    blank activity, target and reference fields. It is a no-data sentinel, not an
    inactive assay, actual AID or applicable exclusion. Other target/activity frames
    are empty.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-roots
  - bgc-2722-query-lotus_occurrences
  - bgc-2722-query-cyanometdb_occurrences
  - bgc-2722-query-pubchem_bioassay
  - bgc-2722-query-bindingdb_targets
  - bgc-2722-query-antibioticmech_inchikeys
  - bgc-2722-assay-curation
  - bgc-2722-row-lotus_occurrences-0
  - bgc-2722-row-pubchem_bioassay-0
  dimensions:
  - name: occurrence_scope
    definition: Exact retained occurrence tuples and limits on production/independence.
    value: One LOTUS Pseudomonas NCBITaxon:286 occurrence cites the same PNAS DOI.
      It is not a separate strain identification or independent production experiment.
    evidence_ids:
    - bgc-2722-roots
    - bgc-2722-query-lotus_occurrences
    - bgc-2722-query-cyanometdb_occurrences
    - bgc-2722-query-pubchem_bioassay
    - bgc-2722-query-bindingdb_targets
    - bgc-2722-query-antibioticmech_inchikeys
    - bgc-2722-assay-curation
    - bgc-2722-row-lotus_occurrences-0
    - bgc-2722-row-pubchem_bioassay-0
  - name: assay_target_scope
    definition: Retained activity/assay/target positives and bounded negative queries.
    value: The PubChem row for CID145720625 has a blank AID, literal (no assay data),
      and blank activity, target and reference fields. It is a no-data sentinel, not
      an inactive assay, actual AID or applicable exclusion. Other target/activity
      frames are empty.
    evidence_ids:
    - bgc-2722-roots
    - bgc-2722-query-lotus_occurrences
    - bgc-2722-query-cyanometdb_occurrences
    - bgc-2722-query-pubchem_bioassay
    - bgc-2722-query-bindingdb_targets
    - bgc-2722-query-antibioticmech_inchikeys
    - bgc-2722-assay-curation
    - bgc-2722-row-lotus_occurrences-0
    - bgc-2722-row-pubchem_bioassay-0
- assessment_id: bgc-2722-classification
  area: consistency
  topic: Computed filing and asserted class applicability
  outcome: supported
  summary: The cyclic ester-containing peptide architecture and long acyl chain provide
    positive structural support for the predicted Cyclic peptides|Depsipeptides|Lipopeptides
    classes. Absence of C5O candidate rings is consistent with the retained glycoside=false
    at this limited scope. NRPS/Type I remains the source assertion; model labels
    do not prove residue sequence or genetic mechanism. The 2 computed pathway labels
    are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent
    filing, not biological absence or an erased classification.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-classification
  - bgc-2722-chemistry
  - bgc-2722-query-npclassifier
  - bgc-2722-query-mibig_compounds
  - bgc-2722-filing-policy
  - bgc-2722-row-npclassifier-0
  dimensions:
  - name: classification_applicability
    definition: Model and source class claims compared with saved topology and maintained
      filing.
    value: The cyclic ester-containing peptide architecture and long acyl chain provide
      positive structural support for the predicted Cyclic peptides|Depsipeptides|Lipopeptides
      classes. Absence of C5O candidate rings is consistent with the retained glycoside=false
      at this limited scope. NRPS/Type I remains the source assertion; model labels
      do not prove residue sequence or genetic mechanism. The 2 computed pathway labels
      are retained while choose_pathway files this owner UNCLASSIFIED. This is consistent
      filing, not biological absence or an erased classification.
    evidence_ids:
    - bgc-2722-classification
    - bgc-2722-chemistry
    - bgc-2722-query-npclassifier
    - bgc-2722-query-mibig_compounds
    - bgc-2722-filing-policy
    - bgc-2722-row-npclassifier-0
- assessment_id: bgc-2722-completion
  area: completeness
  topic: Local completion and maintained ownership
  outcome: unknown
  summary: Whole owner/history, all nine saved query frames (4 positive rows/49 fields)
    and both complete saved molecular forms were personally read. The 44 actual input
    hashes and explicit ownership declarations were verified; this does not claim
    whole-corpus semantic reading. Five required local native commands passed, while
    full QC/OAK, live authority and independent primary verification remain unavailable.
    No selected graph/pathway/component or molecular-target root requires a maintained
    reader for this owner. Corrections belong in maintained inputs, implemented curation
    tables, extractors or the seeder; no record edit is proposed.
  target_ids:
  - naturalproductmech:mibig-6e96262d73
  evidence_ids:
  - bgc-2722-owner
  - bgc-2722-history
  - bgc-2722-intake
  - bgc-2722-intake-acceptance
  - bgc-2722-plan
  - bgc-2722-plan-acceptance
  - bgc-2722-gates
  - bgc-2722-source-reading
  - bgc-2722-source-notes
  - bgc-2722-molecular-reading
  - bgc-2722-roots
  dimensions:
  - name: review_completion
    definition: Actual semantic reading and input verification, with unavailable checks
      and maintained ownership.
    value: Whole owner/history, all nine saved query frames (4 positive rows/49 fields)
      and both complete saved molecular forms were personally read. The 44 actual
      input hashes and explicit ownership declarations were verified; this does not
      claim whole-corpus semantic reading. Five required local native commands passed,
      while full QC/OAK, live authority and independent primary verification remain
      unavailable. No selected graph/pathway/component or molecular-target root requires
      a maintained reader for this owner. Corrections belong in maintained inputs,
      implemented curation tables, extractors or the seeder; no record edit is proposed.
    evidence_ids:
    - bgc-2722-owner
    - bgc-2722-history
    - bgc-2722-intake
    - bgc-2722-intake-acceptance
    - bgc-2722-plan
    - bgc-2722-plan-acceptance
    - bgc-2722-gates
    - bgc-2722-source-reading
    - bgc-2722-source-notes
    - bgc-2722-molecular-reading
    - bgc-2722-roots
findings: []
actions: []
limitations:
- Retained source rows, grades and history were read; cited primary papers and live
  identity/taxonomy resources were not newly verified. Full QC and OAK remain unavailable
  under the no-outbound hold.
- Both neutral C91H148N20O24 forms agree in normalized InChI/full key and counts.
  Carbonyl sites decrease20 to2 and amide sites19 to1; eighteen terminal C(OH)=N sites
  appear, each with O degree1/H1 and N H0. The retained carbonyls are the proline-associated
  amide and the ester. Exact canonical graphs differ and the one-way atom map is empty.
  Four original omitted-undefined-stereo warnings remain globally unassigned.
- Ring, amide, ester and C5O/bridge predicates provide local topology; they do not
  assign natural residues, all stereochemical details, enzyme functions or assay activity.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- All current conclusions are scoped to this exact owner and its captured inputs;
  retained source status remains unchanged.
- No repair, source mutation, external request or new molecular parse was performed.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-273
```
