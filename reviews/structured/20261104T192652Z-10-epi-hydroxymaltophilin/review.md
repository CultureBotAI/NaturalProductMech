# Local evidence review: 10-epi-hydroxymaltophilin

- Review: 20261104T192652Z-10-epi-hydroxymaltophilin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-11-04T18:38:45.600460Z
- Finished UTC: 2026-11-04T19:26:52.007844Z
- Reviewer: Codex root with native_checks, bgc_science and review_support peer agents (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

10-epi-hydroxymaltophilin retains exact source/key correspondence with disclosed incomplete stereochemistry. The stored forms differ at two amide/imidic-acid sites; producer, locus and genus occurrence assertions remain source-qualified.

## Scope And Provenance

One complete NaturalProductRecord, including all present scientific claims, history and declared mechanisms; external verification remains unavailable.

Selection: Campaign path order 2439; one of the next ten uncovered paths selected from the 3116-record corpus. Membership uses the canonical validated catalogue plus retained committed campaign bundles.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce6a5498df5be51116bd5e0c119023ee62bb5464.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-b77b372cbd | data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml | generated | 10-epi-hydroxymaltophilin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| strict_ten | passed | True | naturalproductmech:mibig-b77b372cbd | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| strict_full | passed | True | naturalproductmech:mibig-b77b372cbd | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| lockfile | passed | True | naturalproductmech:mibig-b77b372cbd | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| reproduction | passed | True | naturalproductmech:mibig-b77b372cbd | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| queue | passed | True | naturalproductmech:mibig-b77b372cbd | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |
| Full just qc | unavailable | True | naturalproductmech:mibig-b77b372cbd | Not run under the external-request prohibition: the complete recipe includes upstream vendored synchronization. The five executed local checks are recorded separately. |
| Complete OAK identifier/label authority check | unavailable | True | naturalproductmech:mibig-b77b372cbd | Complete offline ontology authority coverage was not established for this run; no ontology retrieval or remote resolution was attempted. Retained taxonomy evidence has only its explicitly stated local scope. |
| Primary literature and current structured database/identifier verification | unavailable | True | naturalproductmech:mibig-b77b372cbd | All external requests are prohibited by the user. Fresh database and identifier verification and complete primary-literature coverage are unavailable. Any retained original literature actually inspected is recorded separately with its historical scope. |

## Scientific And Domain Assessments

### Retained identifier and source correspondence

identity: supported. Targets: naturalproductmech:mibig-b77b372cbd.

10-epi-hydroxymaltophilin retains minted identifier naturalproductmech:mibig-b77b372cbd, full key AKMROGKTWQCRGK-CQBRWIBHSA-N and npatlas:NPA026681. Its MIBiG BGC0002365 v2 compound 5 row exactly retains the stored structure; both diagnostic forms reproduce its StandardInChI/key. The exact-key ChEBI join is empty. This supports the local MINTED/source correspondence, not global identifier absence, fresh cross-reference validity or a fully resolved natural epimer.

### Stored forms, tautomer representation and stereochemistry

representation: supported. Targets: naturalproductmech:mibig-b77b372cbd.

The forms agree on neutral C29H38N2O7, 38 heavy atoms and 42 bonds, but both canonical SMILES comparisons are false and the direct chirality-aware atom map is empty. Complete tables show two C(=O)-NH sites becoming C(OH)=N on InChI reconstruction, supporting a bounded amide/imidic-acid tautomer interpretation. Each form retains 9 specified tetrahedral centers and one unspecified tetrahedral center, plus two specified original double bonds and an unresolved original double bond; a new unspecified imine descriptor depends on representation. Retained stereo_complete false and full_graph_identity_established false remain explicit; no natural tautomer or stereochemical repair is inferred.

### Producer and locus evidence grades

provenance: supported. Targets: naturalproductmech:mibig-b77b372cbd.

MIBiG BGC0002365 v2 is active, with questionable quality and unknown completeness. Streptomyces sp. (NCBITaxon:1931) remains a SOURCE_ASSERTION producer; MN234160.1:1–17258 remains CLUSTER_UNSTATED with no retained locus methods. The LOTUS genus assertion (NCBITaxon:1883) is distinct and supplies no strain identity. Coordinates, the shared BGC and the compound name do not establish demonstrated production or a resolved pathway.

### Citation tier and history scope

evidence: supported. Targets: naturalproductmech:mibig-b77b372cbd.

PMID:31775228 is retained at ENTRY level for the producer/locus assertion; the single LOTUS occurrence cites DOI:10.3390/MD17120663. These identifiers repeat across the six BGC2365 contexts, without establishing independent experiments or a freshly verified relationship between the two citations. An entry citation does not supply compound-specific assay or reaction evidence. Two seeding history events preserve provenance; no primary article was newly accessed.

### Occurrence and assay boundaries

evidence: supported. Targets: naturalproductmech:mibig-b77b372cbd.

One retained LOTUS row records Streptomyces (NCBITaxon:1883), separately from the MIBiG Streptomyces sp. producer assertion. Exact saved PubChem, BindingDB, ChEBI-origin, CyanometDB and AntibioticMech joins are empty; no assay sentinel, measured potency, molecular-target or bioactivity root is present. These bounded absences do not establish inactivity or universal absence. The four selected companions and unselected Xanthobaccin C provide BGC context only; their identity or activity is not transferred.

### Versioned classification applicability

consistency: supported. Targets: naturalproductmech:mibig-b77b372cbd.

NPClassifier npclassifier.gnps2.org@2026-09-07 retains Amino acids and Peptides&#124;Polyketides, Macrolides, Macrocyclic tetramic acids and is_glycoside false. The supplied SMILES has a 16-membered nitrogen-containing ring and a five-membered nitrogen ring bearing two carbonyl carbons, compatible with a broad macrocyclic tetramic-acid interpretation. No ester C-O-C motif or C5O cycle is present: Macrolides is a model grouping, not demonstrated macrolactone chemistry. UNCLASSIFIED filing and source OTHER/PKS classes are separate fields; these labels alone establish no ingestion defect or biosynthetic mechanism.

### Review completion

completeness: unknown. Targets: naturalproductmech:mibig-b77b372cbd.

Complete current owner/history, all assigned source frames and payloads, accepted canonical intake and both accepted saved molecular forms were read. No causal graph, pathway, declared component or molecular-target root applies to this owner, so no maintained reader is required. False fixed-form comparisons, incomplete stereochemistry, unavailable full QC/OAK coverage and absent fresh primary verification keep this review partial. No supported source-edit finding or action is established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| support-2439-owner | /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml; Whole current plaintext and complete curation_history | supports | Complete owner and 2 history events personally read; current source/status retained. |
| support-2439-capture | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/8/owner_document | supports | Whole captured owner preserves present and absent roots. No causal graph, pathway, declared component or molecular-target root applies; no maintained reader is required for this owner. |
| support-2439-grounding-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/8/owner_document/identifier; /records/8/owner_document/label; /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts; /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes | supports | Retained identifier/full key, source structure, source concepts, literal NPAtlas cross-reference and grounding status; no fresh external identity or xref verification. |
| support-2439-origin-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters; /records/8/owner_document/producer_taxon_groups | supports | Source-qualified producer and locus assertions retain ENTRY citations, MN234160.1:1–17258 coordinates and CLUSTER_UNSTATED scope with no locus methods. |
| support-2439-occurrence-activity-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/8/owner_document | supports | One retained Streptomyces genus occurrence; no related-record, bioactivity or molecular-target root. Whole-owner absence is bounded to this capture and does not establish global inactivity. |
| support-2439-classification-owner | /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json; /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification; /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin | supports | UNCLASSIFIED filing, versioned chemical model outputs and source OTHER/PKS BGC assertions are retained as distinct fields. |
| support-2439-direct-contexts | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-target-input-plan-001.json; /records/8/proposed_companion_paths; /records/8/direct_companion_predicates; /records/8/additional_context_roles | context_only | Four selected companions and unselected Xanthobaccin C share the owned BGC; exact one-hop context does not transfer identity, stereo, production, assay or mechanism evidence. |
| support-2439-intake | /private/tmp/npm-review-work/shared-next-batch244/intakes/2439-inspect-001.json; /targets; /source | supports | Actual canonical single-target inspection preserves complete ownership and exact target/context input roles. |
| support-2439-intake-acceptance | /private/tmp/npm-review-work/shared-next-batch244/root-intake-acceptance-001.json; /status; /summary; /intakes/8; /source_plan_acceptance; /verification | supports | ROOT accepts this original canonical intake and the ten current source-aligned input maps. |
| support-2439-intake-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/support-prep/support-current244-last-five-intake-reading-001.json; /personal_reading; /records/3; /coverage | supports | Support personally read the five complete actual intake/ownership documents, factoring exact common inputs: 210 placements across 42 paths. |
| support-2439-inventory-acceptance | /private/tmp/npm-review-work/shared-next-batch244/root-source-inventory-acceptance-001.json; /status; /accepted; /inventory | supports | ROOT accepts the original local source extraction; retained assertions are not fresh primary verification. |
| support-2439-plan | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-target-input-plan-001.json; /records/8/proposed_input_paths; /records/8/proposed_input_count | supports | Actual immutable input plan agrees with this canonical intake. |
| support-2439-plan-acceptance | /private/tmp/npm-review-work/shared-next-batch244/root-source-plan-acceptance-001.json; /status; /plan; /verification | supports | ROOT accepts the composed source plan and exact inventory/notes/input reconciliation. |
| support-2439-source-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/support-prep/support-current244-assigned-source-reading-002.json; /division; /reading; /contexts; /cautions | supports | Support personally read 45 selected frames with 15 positive rows and 190 fields, plus Xanthobaccin C with nine frames, three rows and 38 fields. Complete raw/history carries and other actors remain attributed; no source replay. |
| support-2439-source-notes | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-scope-notes-001.json; /reading; /reading_reconciliation; /cautions; /limitations | context_only | Joint notes retain disjoint source reading, companion limits and Native cache/curation attribution. |
| support-2439-molecular-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/support-prep/support-current244-last-five-molecular-reading-001.json; /reading; /coverage; /records/3; /limits | supports | Support personally read all ten saved last-five forms: 370 atom rows and 410 bonds, with complete strings, stereo/rings/motifs and empty correspondence maps. |
| support-2439-cached-taxonomy | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /cached_taxonomy/whole_stanzas/21; /cached_taxonomy/whole_stanzas/22 | context_only | Retained complete stanzas name NCBITaxon:1883 Streptomyces and NCBITaxon:1931 Streptomyces sp. They are distinct recorded identifiers; cache names/synonyms do not establish strain identity, production or fresh taxonomy. |
| support-2439-taxonomy-reading | /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-cached-taxonomy-reading-001.json; /scope; /taxonomy; /reading_outputs; /limitations | context_only | Native complete 298-stanza and route reading remains attributed; only the two relevant retained stanzas support this owner’s taxon scope. |
| support-2439-curation-scope | /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-implemented-curation-scan-001.json; /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions; /guidance | context_only | Native retained 60 lexical matches across the cohort and found no applicable implemented correction/exclusion. That bounded scan supplies no assay or mechanism result. |
| support-2439-chemistry | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope; /records/8/comparisons; /records/8/atom_correspondence | supports | Eight comparisons are true, including formula/charge/StandardInChI/key. Both canonical SMILES comparisons are false; direct atom correspondence is empty and full-graph identity remains false. |
| support-2439-topology | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json; /records/8/declared_structure; /records/8/smiles; /records/8/inchi; /records/8/comparisons; /records/8/atom_correspondence | supports | The forms agree on neutral C29H38N2O7, 38 heavy atoms and 42 bonds, but both canonical SMILES comparisons are false and the direct chirality-aware atom map is empty. Complete tables show two C(=O)-NH sites becoming C(OH)=N on InChI reconstruction, supporting a bounded amide/imidic-acid tautomer interpretation. Each form retains 9 specified tetrahedral centers and one unspecified tetrahedral center, plus two specified original double bonds and an unresolved original double bond; a new unspecified imine descriptor depends on representation. Retained stereo_complete false and full_graph_identity_established false remain explicit; no natural tautomer or stereochemical repair is inferred. |
| support-2439-diagnostic-acceptance | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/root-diagnostic-acceptance-001.json; /status; /DATA; /execution; /records/8; /global_warning_count; /warning_attribution; /interpretation_boundary | supports | ROOT accepts the original diagnostic and preserves this owner’s two false canonical comparisons and incomplete direct atom match. Six global warnings remain unassigned. |
| support-2439-diagnostic-execution | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-execution-001.json; /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests | supports | Original diagnostic command, source and streams are preserved with exit0, no retry and no external request. |
| support-2439-diagnostic-stderr | /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-original-001.stderr; Whole original stderr (276 bytes) | context_only | Six undefined-stereochemistry warnings are global and unassigned; no owner-specific attribution or empty-stderr claim. |
| support-2439-structure-schema | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; Lines374–430 | context_only | Schema preserves original source SMILES, explicitly limits InChIKey sameness, records unresolved stereochemistry and separates computed classification from source assertions. |
| support-2439-stereo-method | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; Lines150–173 | context_only | Extractor derives stereo_complete from undefined tetrahedral centers found in source SMILES; no experimental or all-double-bond stereochemistry guarantee. |
| support-2439-classification-seeder | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Lines977–1018 | context_only | Seeder retains source structures/flag and versioned NPClassifier values; model predictions are not independently upgraded. |
| support-2439-review-profile | /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md; Whole domain profile and required-check coverage | context_only | Required review dimensions and limits remain applicable; successful local execution does not replace unavailable authority coverage. |
| support-2439-query-mibig_compounds | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/mibig_compounds | supports | Saved mibig_compounds frame: 1 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-source-mibig_compounds-0 | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/mibig_compounds/matches/0 | supports | Retained physical row 2903: BGC0002365 v2, compound 5 10-epi-hydroxymaltophilin; active/questionable/unknown; Streptomyces sp. (NCBITaxon:1931) SOURCE_ASSERTION, locus CLUSTER_UNSTATED, MN234160.1:1–17258 with empty locus methods; PMID:31775228 at ENTRY level. Full structure, xref and BGC class/subclass fields remain distinct in this row. |
| support-2439-physical-mibig_compounds | /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv; Physical TSV lines 2903 | context_only | Every retained field matches its exact physical source row; no source query. |
| support-2439-query-chebi_structures | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/chebi_structures | supports | Saved chebi_structures frame: 0 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-query-lotus_occurrences | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/lotus_occurrences | supports | Saved lotus_occurrences frame: 1 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-source-lotus_occurrences-0 | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/lotus_occurrences/matches/0 | supports | Retained physical row 146: Streptomyces (NCBITaxon:1883), DOI:10.3390/MD17120663; exact-key occurrence assertion, not demonstrated production or independent-study proof. |
| support-2439-physical-lotus_occurrences | /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv; Physical TSV lines 146 | context_only | Every retained field matches its exact physical source row; no source query. |
| support-2439-query-cyanometdb_occurrences | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/cyanometdb_occurrences | supports | Saved cyanometdb_occurrences frame: 0 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-query-npclassifier | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/npclassifier | supports | Saved npclassifier frame: 1 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-source-npclassifier-0 | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/npclassifier/matches/0 | supports | Retained physical row 59: npclassifier.gnps2.org@2026-09-07: Amino acids and Peptides&#124;Polyketides/Macrolides/Macrocyclic tetramic acids; is_glycoside=false. Model classification is not a source or pathway assertion. |
| support-2439-physical-npclassifier | /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv; Physical TSV lines 59 | context_only | Every retained field matches its exact physical source row; no source query. |
| support-2439-query-pubchem_bioassay | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/pubchem_bioassay | supports | Saved pubchem_bioassay frame: 0 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-query-bindingdb_targets | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/bindingdb_targets | supports | Saved bindingdb_targets frame: 0 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-query-antibioticmech_inchikeys | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys | supports | Saved antibioticmech_inchikeys frame: 0 matched placements. Empty results apply only to the exact retained predicate. |
| support-2439-query-chebi_origins | /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json; /contexts/12/source_scope_inventory/joins/chebi_origins | supports | Saved chebi_origins frame: 0 matched placements. Empty results apply only to the exact retained predicate. |
| root-native-strict_ten | /private/tmp/npm-native-checks/batch-244/validate-strict-selected10-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | Closed-schema validation of the ten selected owners and any referenced components reported zero errors. |
| root-native-strict_full | /private/tmp/npm-native-checks/batch-244/validate-all-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | Full closed-schema validation scanned all 3116 owners and reported zero errors. |
| root-native-lockfile | /private/tmp/npm-native-checks/batch-244/verify-corpus-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | PATHS.tsv and filesystem agree on all 3116 records and their pinned filing pathways. |
| root-native-reproduction | /private/tmp/npm-native-checks/batch-244/verify-reproduction-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | All 3116 records reproduce byte-identically from the retained inventories and carried curator content. This does not independently validate curator science. |
| root-native-queue | /private/tmp/npm-native-checks/batch-244/review-queue-001.log; Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json | supports | The full local queue contains 8922 diagnostic rows; selected-target entries were inspected. Queue diagnostics are leads, not scientific sign-off. |

## Limits And Additional Notes

- Retained local evidence only; primary literature, fresh taxonomy, natural identity and external cross-references were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Both canonical SMILES comparisons are false for this owner, direct atom match is empty, and fixed-form graph identity is unproved. Incomplete tetrahedral/double-bond stereochemistry and unassigned global warnings remain explicit.
- Producer, occurrence, locus, model, citation, companion and assay scopes remain separate; no source edit or pharmacological mechanism is inferred.
- The whole selected owner was read, but scientific completion is partial because full QC, complete ontology authority coverage and external source verification were unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main verification and publication are deferred because the user prohibits all external requests.
- Support personally read five selected owners/history,45 selected frames/15rows/190fields and Xanthobaccin C with9frames/3rows/38fields. BGC source and Native cache/curation credit stay separate.
- All ten saved last-five forms were personally read:370 atom rows/410 bonds with complete strings,stereo,rings,motifs and correspondence; no new parse.
- Support operated the once-only admitted canonical intake; actual saved diagnostic and ROOT acceptance are pinned separately. This half has210 intake placements42paths. No maintained reader applies to these five owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state. Proposed actions are not performed edits.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T192652Z-10-epi-hydroxymaltophilin
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Local evidence review: 10-epi-hydroxymaltophilin'
started_at: '2026-11-04T18:38:45.600460Z'
finished_at: '2026-11-04T19:26:52.007844Z'
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
summary: 10-epi-hydroxymaltophilin retains exact source/key correspondence with disclosed
  incomplete stereochemistry. The stored forms differ at two amide/imidic-acid sites;
  producer, locus and genus occurrence assertions remain source-qualified.
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
    role: target
  - path: data/natural_products/unclassified/10-epi-maltophilin.yaml
    sha256: 046fa4ed6b2a5d9119994bde1849ec0b83c3981155b86d393a48dadb9ee8f006
    role: context
  - path: data/natural_products/unclassified/10-epi-xanthobaccin-c.yaml
    sha256: a3bb47cd5f301033a5ba375388e5966dce77323ed82dbcaed63b85b960d4e383
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
  selection: Campaign path order 2439; one of the next ten uncovered paths selected
    from the 3116-record corpus. Membership uses the canonical validated catalogue
    plus retained committed campaign bundles.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-b77b372cbd
targets:
- target_id: naturalproductmech:mibig-b77b372cbd
  path: data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml
  label: 10-epi-hydroxymaltophilin
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
  - naturalproductmech:mibig-b77b372cbd
  command: just validate-strict data/natural_products/terpenoids/yossoside-v.yaml
    data/natural_products/terpenoids/zealexin-a1.yaml data/natural_products/terpenoids/zealexin-b3.yaml
    data/natural_products/terpenoids/zealexin-c2.yaml data/natural_products/terpenoids/zeaxanthin.yaml
    data/natural_products/unclassified/10-epi-3-deoh-hsaf.yaml data/natural_products/unclassified/10-epi-fi-2.yaml
    data/natural_products/unclassified/10-epi-hsaf.yaml data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml
    data/natural_products/unclassified/10-epi-maltophilin.yaml --workers 1 --out /private/tmp/npm-native-checks/batch-244/validate-strict-selected10-001.tsv
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
  - naturalproductmech:mibig-b77b372cbd
  command: just validate-all --workers 1 --out /private/tmp/npm-native-checks/batch-244/validate-all-001.tsv
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
  - naturalproductmech:mibig-b77b372cbd
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
  - naturalproductmech:mibig-b77b372cbd
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
  - naturalproductmech:mibig-b77b372cbd
  command: just review-queue --tsv /private/tmp/npm-native-checks/batch-244/review-queue-001.tsv
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
  - naturalproductmech:mibig-b77b372cbd
  summary: 'Not run under the external-request prohibition: the complete recipe includes
    upstream vendored synchronization. The five executed local checks are recorded
    separately.'
- check_id: root-ontology-authorities
  name: Complete OAK identifier/label authority check
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  summary: Complete offline ontology authority coverage was not established for this
    run; no ontology retrieval or remote resolution was attempted. Retained taxonomy
    evidence has only its explicitly stated local scope.
- check_id: root-primary-and-live-sources
  name: Primary literature and current structured database/identifier verification
  status: unavailable
  required: true
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  summary: All external requests are prohibited by the user. Fresh database and identifier
    verification and complete primary-literature coverage are unavailable. Any retained
    original literature actually inspected is recorded separately with its historical
    scope.
evidence:
- evidence_id: support-2439-owner
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/unclassified/10-epi-hydroxymaltophilin.yaml
  locator: Whole current plaintext and complete curation_history
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Complete owner and 2 history events personally read; current source/status
    retained.
  snapshot_sha256: 40aac5575689675dbe8b183adac018c571d568ed58f532da74761f5b2658707a
- evidence_id: support-2439-capture
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Whole captured owner preserves present and absent roots. No causal graph,
    pathway, declared component or molecular-target root applies; no maintained reader
    is required for this owner.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: support-2439-grounding-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/8/owner_document/identifier; /records/8/owner_document/label;
    /records/8/owner_document/chemical_structure; /records/8/owner_document/source_concepts;
    /records/8/owner_document/xrefs; /records/8/owner_document/grounding_status; /records/8/owner_document/grounding_notes
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Retained identifier/full key, source structure, source concepts, literal
    NPAtlas cross-reference and grounding status; no fresh external identity or xref
    verification.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: support-2439-origin-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/8/owner_document/producer_organisms; /records/8/owner_document/biosynthetic_gene_clusters;
    /records/8/owner_document/producer_taxon_groups
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Source-qualified producer and locus assertions retain ENTRY citations,
    MN234160.1:1–17258 coordinates and CLUSTER_UNSTATED scope with no locus methods.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: support-2439-occurrence-activity-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/8/owner_document
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: One retained Streptomyces genus occurrence; no related-record, bioactivity
    or molecular-target root. Whole-owner absence is bounded to this capture and does
    not establish global inactivity.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: support-2439-classification-owner
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244/owner-capture-DATA-001.json
  locator: /records/8/owner_document/np_pathway; /records/8/owner_document/np_classification;
    /records/8/owner_document/bgc_class; /records/8/owner_document/biosynthesis_origin
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: UNCLASSIFIED filing, versioned chemical model outputs and source OTHER/PKS
    BGC assertions are retained as distinct fields.
  snapshot_sha256: 375822b537b4da0ada786710a3e6325c91f03dd9f67975509fde2d760717c6b6
- evidence_id: support-2439-direct-contexts
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-target-input-plan-001.json
  locator: /records/8/proposed_companion_paths; /records/8/direct_companion_predicates;
    /records/8/additional_context_roles
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Four selected companions and unselected Xanthobaccin C share the owned
    BGC; exact one-hop context does not transfer identity, stereo, production, assay
    or mechanism evidence.
  snapshot_sha256: dccfa62e7ebea5087b254368b8b36da0f0233f06f61fc60a45298ef4983bd85d
- evidence_id: support-2439-intake
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/intakes/2439-inspect-001.json
  locator: /targets; /source
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Actual canonical single-target inspection preserves complete ownership
    and exact target/context input roles.
  snapshot_sha256: 60a940b5614b90dc48d2ad1bca81e924e33a127f4cf9ae26a5cdd38c2c4b361d
- evidence_id: support-2439-intake-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/root-intake-acceptance-001.json
  locator: /status; /summary; /intakes/8; /source_plan_acceptance; /verification
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: ROOT accepts this original canonical intake and the ten current source-aligned
    input maps.
  snapshot_sha256: 69a4e9caf203d1856dab3941056fb7e1f009a566d9d557e0c9beb3e805610f86
- evidence_id: support-2439-intake-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/support-prep/support-current244-last-five-intake-reading-001.json
  locator: /personal_reading; /records/3; /coverage
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Support personally read the five complete actual intake/ownership documents,
    factoring exact common inputs: 210 placements across 42 paths.'
  snapshot_sha256: 7443a2e9792e401a19a5bb7279eddc7046baa3c83598a1d04aeb62b7f0020a3c
- evidence_id: support-2439-inventory-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/root-source-inventory-acceptance-001.json
  locator: /status; /accepted; /inventory
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: ROOT accepts the original local source extraction; retained assertions
    are not fresh primary verification.
  snapshot_sha256: e617a846bce84f0013b375dbf56dc3ef0187ed35542dbd6725a025a3d1bf59bc
- evidence_id: support-2439-plan
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-target-input-plan-001.json
  locator: /records/8/proposed_input_paths; /records/8/proposed_input_count
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Actual immutable input plan agrees with this canonical intake.
  snapshot_sha256: dccfa62e7ebea5087b254368b8b36da0f0233f06f61fc60a45298ef4983bd85d
- evidence_id: support-2439-plan-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/root-source-plan-acceptance-001.json
  locator: /status; /plan; /verification
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: ROOT accepts the composed source plan and exact inventory/notes/input reconciliation.
  snapshot_sha256: 644539ce2aa9af2ccc4419d3516227d61c3e8c05f5fa73d2ac35c5748fbcd9e7
- evidence_id: support-2439-source-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/support-prep/support-current244-assigned-source-reading-002.json
  locator: /division; /reading; /contexts; /cautions
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Support personally read 45 selected frames with 15 positive rows and 190
    fields, plus Xanthobaccin C with nine frames, three rows and 38 fields. Complete
    raw/history carries and other actors remain attributed; no source replay.
  snapshot_sha256: 50682a439fa527c3e25349fac02c6ace8bbd38ba2f8f772f6e423fb8faf47589
- evidence_id: support-2439-source-notes
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-scope-notes-001.json
  locator: /reading; /reading_reconciliation; /cautions; /limitations
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Joint notes retain disjoint source reading, companion limits and Native
    cache/curation attribution.
  snapshot_sha256: d09da1ec6355073c7b1b30869949f4d2602befa1edd7a0df98841b298c80b516
- evidence_id: support-2439-molecular-reading
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/support-prep/support-current244-last-five-molecular-reading-001.json
  locator: /reading; /coverage; /records/3; /limits
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Support personally read all ten saved last-five forms: 370 atom rows and
    410 bonds, with complete strings, stereo/rings/motifs and empty correspondence
    maps.'
  snapshot_sha256: 3fbf3a97fa9c56d563d28e77e09e77e2c8b52b669f960237854fea248721ee44
- evidence_id: support-2439-cached-taxonomy
  kind: authority
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /cached_taxonomy/whole_stanzas/21; /cached_taxonomy/whole_stanzas/22
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Retained complete stanzas name NCBITaxon:1883 Streptomyces and NCBITaxon:1931
    Streptomyces sp. They are distinct recorded identifiers; cache names/synonyms
    do not establish strain identity, production or fresh taxonomy.
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: support-2439-taxonomy-reading
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-cached-taxonomy-reading-001.json
  locator: /scope; /taxonomy; /reading_outputs; /limitations
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Native complete 298-stanza and route reading remains attributed; only the
    two relevant retained stanzas support this owner’s taxon scope.
  snapshot_sha256: 490df5d6fb436d89d8d181011b8ec2a4c8310aac830b3254df0667330b5d4e61
- evidence_id: support-2439-curation-scope
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-implemented-curation-scan-001.json
  locator: /scope; /table_pins; /positive_lexical_matches; /applicable_corrections_or_exclusions;
    /guidance
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Native retained 60 lexical matches across the cohort and found no applicable
    implemented correction/exclusion. That bounded scan supplies no assay or mechanism
    result.
  snapshot_sha256: 2cc4f7732f69d5e3697664af9e42b1d14330dca0c1afd999c028f7a47f33b708
  search_scope: '{"claim": "No applicable correction in the exact saved identity scope;
    not universal absence.", "contexts": 15, "diagnostic_rows": 3329, "diagnostic_tables":
    1, "full_key": "AKMROGKTWQCRGK-CQBRWIBHSA-N", "ignored_files_included": true,
    "implemented_rows": 93, "implemented_tables": 8, "owner": "naturalproductmech:mibig-b77b372cbd",
    "retained_scan": "/private/tmp/npm-review-work/shared-next-batch244-tentative/native-prep/native-current244-implemented-curation-scan-001.json#/scope",
    "tokens": 745}'
- evidence_id: support-2439-chemistry
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/literal_InChI_layers; /records/8/formula_comparison_scope;
    /records/8/comparisons; /records/8/atom_correspondence
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Eight comparisons are true, including formula/charge/StandardInChI/key.
    Both canonical SMILES comparisons are false; direct atom correspondence is empty
    and full-graph identity remains false.
  snapshot_sha256: c810c4c63bf70013c7fb4bf8700ed8117add6af2d237e661c258fcd2be909ff2
- evidence_id: support-2439-topology
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-DATA-001.json
  locator: /records/8/declared_structure; /records/8/smiles; /records/8/inchi; /records/8/comparisons;
    /records/8/atom_correspondence
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: The forms agree on neutral C29H38N2O7, 38 heavy atoms and 42 bonds, but
    both canonical SMILES comparisons are false and the direct chirality-aware atom
    map is empty. Complete tables show two C(=O)-NH sites becoming C(OH)=N on InChI
    reconstruction, supporting a bounded amide/imidic-acid tautomer interpretation.
    Each form retains 9 specified tetrahedral centers and one unspecified tetrahedral
    center, plus two specified original double bonds and an unresolved original double
    bond; a new unspecified imine descriptor depends on representation. Retained stereo_complete
    false and full_graph_identity_established false remain explicit; no natural tautomer
    or stereochemical repair is inferred.
  snapshot_sha256: c810c4c63bf70013c7fb4bf8700ed8117add6af2d237e661c258fcd2be909ff2
- evidence_id: support-2439-diagnostic-acceptance
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/root-diagnostic-acceptance-001.json
  locator: /status; /DATA; /execution; /records/8; /global_warning_count; /warning_attribution;
    /interpretation_boundary
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: ROOT accepts the original diagnostic and preserves this owner’s two false
    canonical comparisons and incomplete direct atom match. Six global warnings remain
    unassigned.
  snapshot_sha256: f8bce250d5b3e962bc2964d58ee8b7bc9aaa1df654eedef5972fcd2bb0cf28ca
- evidence_id: support-2439-diagnostic-execution
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-execution-001.json
  locator: /command; /exit_code; /source; /stdout; /stderr; /retries; /external_requests
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: Original diagnostic command, source and streams are preserved with exit0,
    no retry and no external request.
  snapshot_sha256: b2711a19d2e5b81af976c5a9ed111e490efe49be1e8633349337f10e211d3b45
- evidence_id: support-2439-diagnostic-stderr
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch244/chemistry-local/diagnostic-original-001.stderr
  locator: Whole original stderr (276 bytes)
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Six undefined-stereochemistry warnings are global and unassigned; no owner-specific
    attribution or empty-stderr claim.
  snapshot_sha256: 8595cdd5f4839e4016cf6f69ddb46388f44d326afd56b5e877c61adaf8ccd5e8
- evidence_id: support-2439-structure-schema
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: Lines374–430
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Schema preserves original source SMILES, explicitly limits InChIKey sameness,
    records unresolved stereochemistry and separates computed classification from
    source assertions.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: support-2439-stereo-method
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: Lines150–173
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Extractor derives stereo_complete from undefined tetrahedral centers found
    in source SMILES; no experimental or all-double-bond stereochemistry guarantee.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
- evidence_id: support-2439-classification-seeder
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Lines977–1018
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Seeder retains source structures/flag and versioned NPClassifier values;
    model predictions are not independently upgraded.
  snapshot_sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
- evidence_id: support-2439-review-profile
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/docs/record-review-profile.md
  locator: Whole domain profile and required-check coverage
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Required review dimensions and limits remain applicable; successful local
    execution does not replace unavailable authority coverage.
  snapshot_sha256: 1b4fd54381de5cf93d744f3d8a8f14d831e45ecfe4060d33e7cebe1bda7ef17a
- evidence_id: support-2439-query-mibig_compounds
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/mibig_compounds
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved mibig_compounds frame: 1 matched placements. Empty results apply
    only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/mibig_compounds",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-source-mibig_compounds-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/mibig_compounds/matches/0
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Retained physical row 2903: BGC0002365 v2, compound 5 10-epi-hydroxymaltophilin;
    active/questionable/unknown; Streptomyces sp. (NCBITaxon:1931) SOURCE_ASSERTION,
    locus CLUSTER_UNSTATED, MN234160.1:1–17258 with empty locus methods; PMID:31775228
    at ENTRY level. Full structure, xref and BGC class/subclass fields remain distinct
    in this row.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: support-2439-physical-mibig_compounds
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/mibig_compounds.tsv
  locator: Physical TSV lines 2903
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Every retained field matches its exact physical source row; no source query.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: support-2439-query-chebi_structures
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/chebi_structures
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved chebi_structures frame: 0 matched placements. Empty results apply
    only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/chebi_structures",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-query-lotus_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/lotus_occurrences
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved lotus_occurrences frame: 1 matched placements. Empty results apply
    only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/lotus_occurrences",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-source-lotus_occurrences-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/lotus_occurrences/matches/0
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Retained physical row 146: Streptomyces (NCBITaxon:1883), DOI:10.3390/MD17120663;
    exact-key occurrence assertion, not demonstrated production or independent-study
    proof.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: support-2439-physical-lotus_occurrences
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/lotus_occurrences.tsv
  locator: Physical TSV lines 146
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Every retained field matches its exact physical source row; no source query.
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
- evidence_id: support-2439-query-cyanometdb_occurrences
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/cyanometdb_occurrences
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved cyanometdb_occurrences frame: 0 matched placements. Empty results
    apply only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/cyanometdb_occurrences",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-query-npclassifier
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/npclassifier
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved npclassifier frame: 1 matched placements. Empty results apply only
    to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/npclassifier",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-source-npclassifier-0
  kind: database
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/npclassifier/matches/0
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Retained physical row 59: npclassifier.gnps2.org@2026-09-07: Amino acids
    and Peptides|Polyketides/Macrolides/Macrocyclic tetramic acids; is_glycoside=false.
    Model classification is not a source or pathway assertion.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
- evidence_id: support-2439-physical-npclassifier
  kind: database
  reference: /private/tmp/npm-record-reviews-20261021/data/raw/npclassifier.tsv
  locator: Physical TSV lines 59
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: context_only
  summary: Every retained field matches its exact physical source row; no source query.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: support-2439-query-pubchem_bioassay
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/pubchem_bioassay
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved pubchem_bioassay frame: 0 matched placements. Empty results apply
    only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/pubchem_bioassay",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-query-bindingdb_targets
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/bindingdb_targets
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved bindingdb_targets frame: 0 matched placements. Empty results apply
    only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/bindingdb_targets",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-query-antibioticmech_inchikeys
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved antibioticmech_inchikeys frame: 0 matched placements. Empty results
    apply only to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact complete standard_inchi_key equality", "query":
    "AKMROGKTWQCRGK-CQBRWIBHSA-N", "saved_frame": "/contexts/12/source_scope_inventory/joins/antibioticmech_inchikeys",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: support-2439-query-chebi_origins
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch244-tentative/bgc-prep/bgc-conditional244-source-inventory-DATA-001.json
  locator: /contexts/12/source_scope_inventory/joins/chebi_origins
  accessed_at: '2026-11-04T19:17:16.907697Z'
  support: supports
  summary: 'Saved chebi_origins frame: 0 matched placements. Empty results apply only
    to the exact retained predicate.'
  snapshot_sha256: 792c50ec4933eeabf21db13f9af85dc5b3f9276d4eab615c169de9728554ab30
  search_scope: '{"predicate": "exact chebi_id from exact full-key structure rows",
    "query": [], "saved_frame": "/contexts/12/source_scope_inventory/joins/chebi_origins",
    "scope": "Immutable retained local inventory; no replay, external request or universal
    absence claim."}'
- evidence_id: root-native-strict_ten
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/validate-strict-selected10-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:43:43.930616Z'
  support: supports
  summary: Closed-schema validation of the ten selected owners and any referenced
    components reported zero errors.
  snapshot_sha256: 7bb4ad4e0fc89a85a446b5527c39990074b4b39615edd9f0921661f38f9d769f
- evidence_id: root-native-strict_full
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/validate-all-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:44:08.281786Z'
  support: supports
  summary: Full closed-schema validation scanned all 3116 owners and reported zero
    errors.
  snapshot_sha256: ddb5ae59e1880322ba67c16aed40fe6d92c5c1fa277fbcc27fd28114ab658231
- evidence_id: root-native-lockfile
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/verify-corpus-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:44:27.128430Z'
  support: supports
  summary: PATHS.tsv and filesystem agree on all 3116 records and their pinned filing
    pathways.
  snapshot_sha256: 254f171c7dff0f1ecbee5f47f75d2b7046143ae7fc499d9a1c08263e1c5125d8
- evidence_id: root-native-reproduction
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/verify-reproduction-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:45:02.008522Z'
  support: supports
  summary: All 3116 records reproduce byte-identically from the retained inventories
    and carried curator content. This does not independently validate curator science.
  snapshot_sha256: cfc38f4e3f434e7f3651975f2cb228e5cda848476b2c53d1636d8746b794237a
- evidence_id: root-native-queue
  kind: validation
  reference: /private/tmp/npm-native-checks/batch-244/review-queue-001.log
  locator: Complete actual command stdout/stderr; command and clocks retained in /private/tmp/npm-native-checks/batch-244/native-current244-five-gates-execution-001.json
  accessed_at: '2026-11-04T18:45:14.089345Z'
  support: supports
  summary: The full local queue contains 8922 diagnostic rows; selected-target entries
    were inspected. Queue diagnostics are leads, not scientific sign-off.
  snapshot_sha256: 8023a9f2ce97c6d100e6a428e98eddc81efb4bc4be6fd5b45fe050798b28612a
assessments:
- area: identity
  topic: Retained identifier and source correspondence
  outcome: supported
  summary: 10-epi-hydroxymaltophilin retains minted identifier naturalproductmech:mibig-b77b372cbd,
    full key AKMROGKTWQCRGK-CQBRWIBHSA-N and npatlas:NPA026681. Its MIBiG BGC0002365
    v2 compound 5 row exactly retains the stored structure; both diagnostic forms
    reproduce its StandardInChI/key. The exact-key ChEBI join is empty. This supports
    the local MINTED/source correspondence, not global identifier absence, fresh cross-reference
    validity or a fully resolved natural epimer.
  assessment_id: support-2439-identity
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-grounding-owner
  - support-2439-chemistry
  - support-2439-direct-contexts
  - support-2439-query-chebi_structures
  - support-2439-source-mibig_compounds-0
  dimensions:
  - name: standard_inchi_key
    value: AKMROGKTWQCRGK-CQBRWIBHSA-N; retained exact full key, not independent natural
      identity.
    definition: Exact full key; no first-block, name or congener substitution.
    evidence_ids:
    - support-2439-grounding-owner
    - support-2439-chemistry
    - support-2439-direct-contexts
    - support-2439-query-chebi_structures
    - support-2439-source-mibig_compounds-0
  - name: grounding_scope
    value: 10-epi-hydroxymaltophilin retains minted identifier naturalproductmech:mibig-b77b372cbd,
      full key AKMROGKTWQCRGK-CQBRWIBHSA-N and npatlas:NPA026681. Its MIBiG BGC0002365
      v2 compound 5 row exactly retains the stored structure; both diagnostic forms
      reproduce its StandardInChI/key. The exact-key ChEBI join is empty. This supports
      the local MINTED/source correspondence, not global identifier absence, fresh
      cross-reference validity or a fully resolved natural epimer.
    definition: Retained grounding fidelity is distinct from fresh natural-identity
      verification.
    evidence_ids:
    - support-2439-grounding-owner
    - support-2439-chemistry
    - support-2439-direct-contexts
    - support-2439-query-chebi_structures
    - support-2439-source-mibig_compounds-0
- area: representation
  topic: Stored forms, tautomer representation and stereochemistry
  outcome: supported
  summary: The forms agree on neutral C29H38N2O7, 38 heavy atoms and 42 bonds, but
    both canonical SMILES comparisons are false and the direct chirality-aware atom
    map is empty. Complete tables show two C(=O)-NH sites becoming C(OH)=N on InChI
    reconstruction, supporting a bounded amide/imidic-acid tautomer interpretation.
    Each form retains 9 specified tetrahedral centers and one unspecified tetrahedral
    center, plus two specified original double bonds and an unresolved original double
    bond; a new unspecified imine descriptor depends on representation. Retained stereo_complete
    false and full_graph_identity_established false remain explicit; no natural tautomer
    or stereochemical repair is inferred.
  assessment_id: support-2439-representation
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-grounding-owner
  - support-2439-chemistry
  - support-2439-topology
  - support-2439-molecular-reading
  - support-2439-diagnostic-acceptance
  - support-2439-structure-schema
  - support-2439-stereo-method
  dimensions:
  - name: stereochemistry_scope
    value: The forms agree on neutral C29H38N2O7, 38 heavy atoms and 42 bonds, but
      both canonical SMILES comparisons are false and the direct chirality-aware atom
      map is empty. Complete tables show two C(=O)-NH sites becoming C(OH)=N on InChI
      reconstruction, supporting a bounded amide/imidic-acid tautomer interpretation.
      Each form retains 9 specified tetrahedral centers and one unspecified tetrahedral
      center, plus two specified original double bonds and an unresolved original
      double bond; a new unspecified imine descriptor depends on representation. Retained
      stereo_complete false and full_graph_identity_established false remain explicit;
      no natural tautomer or stereochemical repair is inferred.
    definition: Saved tetrahedral and double-bond annotations are distinguished from
      experimental natural stereochemistry.
    evidence_ids:
    - support-2439-grounding-owner
    - support-2439-chemistry
    - support-2439-topology
    - support-2439-molecular-reading
    - support-2439-diagnostic-acceptance
    - support-2439-structure-schema
    - support-2439-stereo-method
  - name: representation_correspondence
    value: Eight true comparisons; canonical isomeric/nonisomeric SMILES comparisons
      are false, direct atom map empty and full_graph_identity_established false.
      Two amide/imidic-acid representations share StandardInChI/key without proving
      fixed-form equality or resolving stereochemistry.
    definition: Identifier and atom-match agreement do not establish complete fixed-graph
      or natural-form identity.
    evidence_ids:
    - support-2439-grounding-owner
    - support-2439-chemistry
    - support-2439-topology
    - support-2439-molecular-reading
    - support-2439-diagnostic-acceptance
    - support-2439-structure-schema
    - support-2439-stereo-method
- area: provenance
  topic: Producer and locus evidence grades
  outcome: supported
  summary: MIBiG BGC0002365 v2 is active, with questionable quality and unknown completeness.
    Streptomyces sp. (NCBITaxon:1931) remains a SOURCE_ASSERTION producer; MN234160.1:1–17258
    remains CLUSTER_UNSTATED with no retained locus methods. The LOTUS genus assertion
    (NCBITaxon:1883) is distinct and supplies no strain identity. Coordinates, the
    shared BGC and the compound name do not establish demonstrated production or a
    resolved pathway.
  assessment_id: support-2439-provenance
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-origin-owner
  - support-2439-source-reading
  - support-2439-direct-contexts
  - support-2439-cached-taxonomy
  - support-2439-taxonomy-reading
  - support-2439-curation-scope
  - support-2439-source-mibig_compounds-0
  - support-2439-source-lotus_occurrences-0
  dimensions:
  - name: taxon_scope
    value: MIBiG BGC0002365 v2 is active, with questionable quality and unknown completeness.
      Streptomyces sp. (NCBITaxon:1931) remains a SOURCE_ASSERTION producer; MN234160.1:1–17258
      remains CLUSTER_UNSTATED with no retained locus methods. The LOTUS genus assertion
      (NCBITaxon:1883) is distinct and supplies no strain identity. Coordinates, the
      shared BGC and the compound name do not establish demonstrated production or
      a resolved pathway.
    definition: Producer, occurrence, species, strain and cached synonym scopes remain
      separate.
    evidence_ids:
    - support-2439-origin-owner
    - support-2439-source-reading
    - support-2439-direct-contexts
    - support-2439-cached-taxonomy
    - support-2439-taxonomy-reading
    - support-2439-curation-scope
    - support-2439-source-mibig_compounds-0
    - support-2439-source-lotus_occurrences-0
  - name: producer_evidence
    value: MIBiG BGC0002365 v2 is active, with questionable quality and unknown completeness.
      Streptomyces sp. (NCBITaxon:1931) remains a SOURCE_ASSERTION producer; MN234160.1:1–17258
      remains CLUSTER_UNSTATED with no retained locus methods. The LOTUS genus assertion
      (NCBITaxon:1883) is distinct and supplies no strain identity. Coordinates, the
      shared BGC and the compound name do not establish demonstrated production or
      a resolved pathway.
    definition: Producer grade is preserved independently of locus support and occurrence.
    evidence_ids:
    - support-2439-origin-owner
    - support-2439-source-reading
    - support-2439-direct-contexts
    - support-2439-cached-taxonomy
    - support-2439-taxonomy-reading
    - support-2439-curation-scope
    - support-2439-source-mibig_compounds-0
    - support-2439-source-lotus_occurrences-0
  - name: locus_evidence
    value: MIBiG BGC0002365 v2 is active, with questionable quality and unknown completeness.
      Streptomyces sp. (NCBITaxon:1931) remains a SOURCE_ASSERTION producer; MN234160.1:1–17258
      remains CLUSTER_UNSTATED with no retained locus methods. The LOTUS genus assertion
      (NCBITaxon:1883) is distinct and supplies no strain identity. Coordinates, the
      shared BGC and the compound name do not establish demonstrated production or
      a resolved pathway.
    definition: Retained locus grades and methods do not prove a complete pathway
      or each compound-specific reaction.
    evidence_ids:
    - support-2439-origin-owner
    - support-2439-source-reading
    - support-2439-direct-contexts
    - support-2439-cached-taxonomy
    - support-2439-taxonomy-reading
    - support-2439-curation-scope
    - support-2439-source-mibig_compounds-0
    - support-2439-source-lotus_occurrences-0
- area: evidence
  topic: Citation tier and history scope
  outcome: supported
  summary: PMID:31775228 is retained at ENTRY level for the producer/locus assertion;
    the single LOTUS occurrence cites DOI:10.3390/MD17120663. These identifiers repeat
    across the six BGC2365 contexts, without establishing independent experiments
    or a freshly verified relationship between the two citations. An entry citation
    does not supply compound-specific assay or reaction evidence. Two seeding history
    events preserve provenance; no primary article was newly accessed.
  assessment_id: support-2439-citations
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-owner
  - support-2439-grounding-owner
  - support-2439-origin-owner
  - support-2439-occurrence-activity-owner
  - support-2439-source-reading
  - support-2439-direct-contexts
  - support-2439-source-mibig_compounds-0
  - support-2439-source-lotus_occurrences-0
  - support-2439-source-npclassifier-0
  dimensions:
  - name: citation_scope
    value: PMID:31775228 is retained at ENTRY level for the producer/locus assertion;
      the single LOTUS occurrence cites DOI:10.3390/MD17120663. These identifiers
      repeat across the six BGC2365 contexts, without establishing independent experiments
      or a freshly verified relationship between the two citations. An entry citation
      does not supply compound-specific assay or reaction evidence. Two seeding history
      events preserve provenance; no primary article was newly accessed.
    definition: Historical primary-experiment labels, database provenance and occurrence
      references retain their separate roles; no fresh source access or publication
      independence is inferred.
    evidence_ids:
    - support-2439-owner
    - support-2439-grounding-owner
    - support-2439-origin-owner
    - support-2439-occurrence-activity-owner
    - support-2439-source-reading
    - support-2439-direct-contexts
    - support-2439-source-mibig_compounds-0
    - support-2439-source-lotus_occurrences-0
    - support-2439-source-npclassifier-0
- area: evidence
  topic: Occurrence and assay boundaries
  outcome: supported
  summary: One retained LOTUS row records Streptomyces (NCBITaxon:1883), separately
    from the MIBiG Streptomyces sp. producer assertion. Exact saved PubChem, BindingDB,
    ChEBI-origin, CyanometDB and AntibioticMech joins are empty; no assay sentinel,
    measured potency, molecular-target or bioactivity root is present. These bounded
    absences do not establish inactivity or universal absence. The four selected companions
    and unselected Xanthobaccin C provide BGC context only; their identity or activity
    is not transferred.
  assessment_id: support-2439-occurrence
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-occurrence-activity-owner
  - support-2439-direct-contexts
  - support-2439-cached-taxonomy
  - support-2439-curation-scope
  - support-2439-query-lotus_occurrences
  - support-2439-query-chebi_origins
  - support-2439-query-cyanometdb_occurrences
  - support-2439-query-pubchem_bioassay
  - support-2439-query-bindingdb_targets
  - support-2439-query-antibioticmech_inchikeys
  - support-2439-source-lotus_occurrences-0
  dimensions:
  - name: occurrence_scope
    value: One retained LOTUS row records Streptomyces (NCBITaxon:1883), separately
      from the MIBiG Streptomyces sp. producer assertion. Exact saved PubChem, BindingDB,
      ChEBI-origin, CyanometDB and AntibioticMech joins are empty; no assay sentinel,
      measured potency, molecular-target or bioactivity root is present. These bounded
      absences do not establish inactivity or universal absence. The four selected
      companions and unselected Xanthobaccin C provide BGC context only; their identity
      or activity is not transferred.
    definition: Occurrence placements do not count independent experiments or demonstrated
      producers.
    evidence_ids:
    - support-2439-occurrence-activity-owner
    - support-2439-direct-contexts
    - support-2439-cached-taxonomy
    - support-2439-curation-scope
    - support-2439-query-lotus_occurrences
    - support-2439-query-chebi_origins
    - support-2439-query-cyanometdb_occurrences
    - support-2439-query-pubchem_bioassay
    - support-2439-query-bindingdb_targets
    - support-2439-query-antibioticmech_inchikeys
    - support-2439-source-lotus_occurrences-0
  - name: assay_target_scope
    value: Exact retained assay/target joins are empty, with no blank-AID sentinel
      or measured assay; no activity, potency or target conclusion follows.
    definition: Empty joins and blank-AID sentinels are not inactivity evidence; biosynthetic
      enzymes are not pharmacological targets.
    evidence_ids:
    - support-2439-occurrence-activity-owner
    - support-2439-direct-contexts
    - support-2439-cached-taxonomy
    - support-2439-curation-scope
    - support-2439-query-lotus_occurrences
    - support-2439-query-chebi_origins
    - support-2439-query-cyanometdb_occurrences
    - support-2439-query-pubchem_bioassay
    - support-2439-query-bindingdb_targets
    - support-2439-query-antibioticmech_inchikeys
    - support-2439-source-lotus_occurrences-0
- area: consistency
  topic: Versioned classification applicability
  outcome: supported
  summary: 'NPClassifier npclassifier.gnps2.org@2026-09-07 retains Amino acids and
    Peptides|Polyketides, Macrolides, Macrocyclic tetramic acids and is_glycoside
    false. The supplied SMILES has a 16-membered nitrogen-containing ring and a five-membered
    nitrogen ring bearing two carbonyl carbons, compatible with a broad macrocyclic
    tetramic-acid interpretation. No ester C-O-C motif or C5O cycle is present: Macrolides
    is a model grouping, not demonstrated macrolactone chemistry. UNCLASSIFIED filing
    and source OTHER/PKS classes are separate fields; these labels alone establish
    no ingestion defect or biosynthetic mechanism.'
  assessment_id: support-2439-classification
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-classification-owner
  - support-2439-chemistry
  - support-2439-topology
  - support-2439-structure-schema
  - support-2439-classification-seeder
  - support-2439-source-mibig_compounds-0
  - support-2439-source-npclassifier-0
  dimensions:
  - name: classification_applicability
    value: 'NPClassifier npclassifier.gnps2.org@2026-09-07 retains Amino acids and
      Peptides|Polyketides, Macrolides, Macrocyclic tetramic acids and is_glycoside
      false. The supplied SMILES has a 16-membered nitrogen-containing ring and a
      five-membered nitrogen ring bearing two carbonyl carbons, compatible with a
      broad macrocyclic tetramic-acid interpretation. No ester C-O-C motif or C5O
      cycle is present: Macrolides is a model grouping, not demonstrated macrolactone
      chemistry. UNCLASSIFIED filing and source OTHER/PKS classes are separate fields;
      these labels alone establish no ingestion defect or biosynthetic mechanism.'
    definition: Versioned model predictions, retained source classes and saved topology
      remain different evidence types.
    evidence_ids:
    - support-2439-classification-owner
    - support-2439-chemistry
    - support-2439-topology
    - support-2439-structure-schema
    - support-2439-classification-seeder
    - support-2439-source-mibig_compounds-0
    - support-2439-source-npclassifier-0
- area: completeness
  topic: Review completion
  outcome: unknown
  summary: Complete current owner/history, all assigned source frames and payloads,
    accepted canonical intake and both accepted saved molecular forms were read. No
    causal graph, pathway, declared component or molecular-target root applies to
    this owner, so no maintained reader is required. False fixed-form comparisons,
    incomplete stereochemistry, unavailable full QC/OAK coverage and absent fresh
    primary verification keep this review partial. No supported source-edit finding
    or action is established.
  assessment_id: support-2439-completion
  target_ids:
  - naturalproductmech:mibig-b77b372cbd
  evidence_ids:
  - support-2439-owner
  - support-2439-capture
  - support-2439-intake
  - support-2439-intake-acceptance
  - support-2439-intake-reading
  - support-2439-inventory-acceptance
  - support-2439-plan
  - support-2439-plan-acceptance
  - support-2439-source-reading
  - support-2439-source-notes
  - support-2439-molecular-reading
  - support-2439-diagnostic-acceptance
  - support-2439-diagnostic-execution
  - support-2439-diagnostic-stderr
  - support-2439-review-profile
  dimensions:
  - name: review_completion
    value: Complete current owner/history, all assigned source frames and payloads,
      accepted canonical intake and both accepted saved molecular forms were read.
      No causal graph, pathway, declared component or molecular-target root applies
      to this owner, so no maintained reader is required. False fixed-form comparisons,
      incomplete stereochemistry, unavailable full QC/OAK coverage and absent fresh
      primary verification keep this review partial. No supported source-edit finding
      or action is established.
    definition: Completion reflects actual access and required-check limits; local
      success is not scientific proof.
    evidence_ids:
    - support-2439-owner
    - support-2439-capture
    - support-2439-intake
    - support-2439-intake-acceptance
    - support-2439-intake-reading
    - support-2439-inventory-acceptance
    - support-2439-plan
    - support-2439-plan-acceptance
    - support-2439-source-reading
    - support-2439-source-notes
    - support-2439-molecular-reading
    - support-2439-diagnostic-acceptance
    - support-2439-diagnostic-execution
    - support-2439-diagnostic-stderr
    - support-2439-review-profile
findings: []
actions: []
limitations:
- Retained local evidence only; primary literature, fresh taxonomy, natural identity
  and external cross-references were not newly verified.
- Full QC and complete OAK authority coverage remain unavailable.
- Both canonical SMILES comparisons are false for this owner, direct atom match is
  empty, and fixed-form graph identity is unproved. Incomplete tetrahedral/double-bond
  stereochemistry and unassigned global warnings remain explicit.
- Producer, occurrence, locus, model, citation, companion and assay scopes remain
  separate; no source edit or pharmacological mechanism is inferred.
- The whole selected owner was read, but scientific completion is partial because
  full QC, complete ontology authority coverage and external source verification were
  unavailable. No native status or history was changed.
- The branch uses cached base ce6a5498df5be51116bd5e0c119023ee62bb5464. Fresh origin/main
  verification and publication are deferred because the user prohibits all external
  requests.
notes:
- Support personally read five selected owners/history,45 selected frames/15rows/190fields
  and Xanthobaccin C with9frames/3rows/38fields. BGC source and Native cache/curation
  credit stay separate.
- All ten saved last-five forms were personally read:370 atom rows/410 bonds with
  complete strings,stereo,rings,motifs and correspondence; no new parse.
- Support operated the once-only admitted canonical intake; actual saved diagnostic
  and ROOT acceptance are pinned separately. This half has210 intake placements42paths.
  No maintained reader applies to these five owners.
- Saved review coverage is distinct from the native SEEDED/REVIEWED curation state.
  Proposed actions are not performed edits.
tags:
- offline
- record-review
- batch-244
```
