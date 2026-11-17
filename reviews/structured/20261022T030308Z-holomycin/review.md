# Scientific review of holomycin

- Review: 20261022T030308Z-holomycin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-22T02:59:33.976734Z
- Finished UTC: 2026-10-22T03:03:08.795086Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Holomycin identity and multiple source-specific native observations are supported. Its unqualified direct RNA-polymerase-inhibitor definition exceeds the inspected evidence: cellular transcription effects are positive, purified-enzyme inhibition is weak and the direct target remains unresolved. The partial NRPS graph remains supported, while several occurrence sources and the complete Yersinia method combination require further verification.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 244, batch 025, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 300 of 3116 current records had campaign coverage and 2816 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 71a28cf520dc96a7107b00d87703ba1e59acc02c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:156451 | data/natural_products/alkaloids/holomycin.yaml | generated | holomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | CHEBI:156451 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | CHEBI:156451 | All3116 corpus records are filed exactly where PATHS.tsv pins them. |
| Corpus reproduction | passed | True | CHEBI:156451 | All3116 records reproduce byte-for-byte from data/raw/. |
| Native deterministic review queue | passed | True | CHEBI:156451 | The canonical review-queue command completed with actual exit0 on the fresh main base; exact output, warnings and skips remain in the pinned transcript. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:156451 | Configured identifier-label gate passed with13449canonical matches,646synonym matches and35configured exceptions. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:156451 | Actual canonical just qc retry002 terminal0. All gates passed: lint;22 governed artifacts; documentation;15 inventory provenance;44 source queue entries;999 tests passed,4 skipped,2 dependency warnings;strict3116 zeroerrors;generated site;3116 byte-identical reproduction;PATHS integrity;corpus report. |
| Complete owner and captured-source scope | passed | True | CHEBI:156451 | Official successful intake and post-intake root reading precede authoring. All seven source sets reconcile. Inline graphs are present in 243, 244, 246 and 248; 246 additionally has sixteen molecular_targets. These are inventories, not independent validation of every biological or affinity claim. |
| Written assay calls and reported endpoint fidelity | passed | True | CHEBI:156451 | All 1 written observations match their exact raw row and current sample/target tuple. Blank values remain blank, AC50/Potency remain OTHER, Inconclusive remains NOT_DETERMINED, and no raw-only assay result is promoted. |
| local | passed | True | CHEBI:156451 | The complete actual owner and seven source sets match the pinned preparation and successful intake. This establishes source fidelity, not the truth of every imported assertion. |
| definition scope | failed | True | CHEBI:156451 | The unqualified direct-RNAP statement exceeds the inspected primary mechanism evidence. |
| yersinia methods | unavailable | True | CHEBI:156451 | The full original article remains required to close applicability of the complete imported Yersinia method combination; positive native evidence is retained. |
| occurrence scope | unavailable | True | CHEBI:156451 | Some written occurrences require unavailable full original bodies or an unresolved exact species bridge; the individual ledger preserves positive evidence without inferring absence. |
| nrps scope | passed | True | CHEBI:156451 | The existing partial pathway/graph and exact reference protein identity are supported. |
| Stored chemical representation and complete source row | passed | True | CHEBI:156451 | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Exact literal chemical authority scope | passed | True | CHEBI:156451 | Every asserted literal is accounted for at its measured representation; default encoding and fixed-H distinctions remain explicit. |
| Original exact compound constitution and depiction | passed | True | CHEBI:156451 | The original closed-disulfide holomycin drawing independently matches the complete achiral owner. Exact authority, committed sibling stated InChI and original deposited sample agree; invalid external default SMILES are preserved separately. Biological target and stock applicability remain independently scoped. |
| Independent experimental stereochemical scope | not_applicable | False | CHEBI:156451 | Achiral exact primary graph; no absolute hand applies. |

## Scientific And Domain Assessments

### Native status and complete audit history

provenance: supported. Targets: CHEBI:156451.

All 4 events retain the exact sequence ['SEEDED_FROM_SOURCES', 'SEEDED_FROM_SOURCES', 'RECORD_CURATED', 'SEEDED_FROM_SOURCES']. Native status is SEEDED. RECORD_CURATED and CURATED_BIOSYNTHESIS_GRAPH events describe prior edits; they are not scientific review passes or a substitute for claim-level assessment.

### Present optional claims

completeness: supported. Targets: CHEBI:156451.

Present optional fields: definition, biosynthetic_pathway, causal_graphs, bioactivities, bioactivity_summary, related_records, discussions. The definition, one pathway step, four-node/four-edge graph, discussion, sibling link, antibacterial summary and one USP30 observation are all present. Biosynthetic and polymerase-mechanism claims are assessed separately; the USP30 assay and summary provenance are assessed here.

### Exact-key computed classification provenance

representation: supported. Targets: CHEBI:156451.

The exact-key NPClassifier projection/version npclassifier.gnps2.org@2026-09-07 reproduces filing, superclass/class and glycoside value false. These computed labels are not independent natural-origin or mechanism evidence. Any accepted new identity requires effective-key reclassification.

### Taxonomic names versus experimental stocks

provenance: supported. Targets: CHEBI:156451.

Streptomyces clavuligerus 1901 includes ATCC 27064; Yersinia ruckeri 29486 and ATCC 29473 strain 527005 remain distinct levels. Photobacterium halotolerans 265726 and P. galatheae 1654360 are separate current species records. S. flavovirens 52258 and S. flavogriseus 67299 remain distinct, as do genus 1883 and named species. These labels do not resolve the source-specific occurrence or stock applicability assessed with primary evidence.

### Literal organism identifier routing

grounding: supported. Targets: CHEBI:156451.

This record's literal organism routes match the retained P225 names and P685 taxon identifiers. No taxonomic match establishes chemical occurrence, stock equivalence or a source-method endpoint.

### Native producer transcriptomic applicability

completeness: not_applicable. Targets: CHEBI:156451.

The native emitted producers are not exact organism/strain matches in the returned 20-organism catalogue. S. albidoflavus J1074 and several S. coelicolor strains are present as expression-resource contexts relevant to separate holomycin occurrence/engineered-host literature. Their catalogue presence neither establishes natural production nor proves a particular introduced strain shares the transcriptome experiment. Unnamed S. albus in the hydroxysporine expression paper must not become J1074 by assumption. No gene-set membership, expression matrix or causal mechanism queried.

### Exact raw and written assay inventory

scope: supported. Targets: CHEBI:156451.

This record has 1 raw rows, 1 written observations and 0 no-data sentinel. There is no retained raw-only assay overflow in this cohort. Inventory equality alone does not establish endpoint interpretation or deposited sample identity.

### bioactivities[0] AID1645860 endpoint and deposited outcome

scope: supported. Targets: CHEBI:156451.

Purified USP30 ubiquitin-rhodamine cleavage screen; the deposited Active call has no emitted potency. Human Q70CQ3 is the source enzyme accession. This screen does not establish selectivity, a clinical mechanism or a polymerase target. No numeric endpoint is emitted; no potency is inferred. Preserve source outcome Active and deposited SID441245207.

### bioactivity_summary and related_records

evidence: supported. Targets: CHEBI:156451.

ANTIBACTERIAL is supplied by the pinned sibling; the USP30 screen is an independent biochemical observation. Neither supplies an unqualified DNA-dependent RNA polymerase mechanism. The definition and sibling identity are assessed separately.

### biosynthesis_origin; producer_organisms

scope: supported. Targets: CHEBI:156451.

Named native holomycin evidence is positive for the three source organisms within their inspected stock scopes. S2753 has an explicit deposited reclassification bridge from historical P. halotolerans to P. galatheae. The conservative S. clavuligerus SOURCE_ASSERTION grade remains faithful even though primary native genetic evidence is now available.

### biosynthetic_gene_clusters[0]

evidence: unknown. Targets: CHEBI:156451.

Native ATCC29473 product and hom6-deletion evidence are positive in the abstract/indexed source. The full original body remains unavailable for the complete imported method combination. Hom12 expression in E. coli is resistance evidence, not proof of whole-cluster holomycin formation. Preserve the positive native result while keeping exact heterologous applicability unresolved.

### biosynthetic_gene_clusters[1]

evidence: supported. Targets: CHEBI:156451.

The inspected native S2753 results support holomycin loss after hlmE deletion. Activity/biofilm complementation is not silently relabeled as exact chemical rescue; remaining full Methods were unavailable. Deposited source naming explicitly bridges the historical species label.

### biosynthetic_gene_clusters[2]

evidence: supported. Targets: CHEBI:156451.

The original native product and genetic experiments support the named locus. Empty imported methods and conservative grades remain source-faithful; adding the newly inspected genetic evidence is optional enrichment rather than mandatory promotion.

### definition

evidence: concern. Targets: CHEBI:156451.

The direct RNA-polymerase-inhibitor definition is stronger than the inspected primary mechanism evidence. Whole-cell RNA-synthesis effects are positive, but purified RNAP inhibition is weak and the direct molecular target remains unresolved.

### biosynthetic_pathway[0]

evidence: supported. Targets: CHEBI:156451.

The step correctly distinguishes native ORF3488 requirement from purified L-Cys activation/tethering and stops before final holomycin formation. Current exact protein identity is independently grounded.

### causal_graphs[0]

evidence: supported. Targets: CHEBI:156451.

All four edges remain at L-Cys activation and enzyme tethering. The product node is an NRPS-bound intermediate, not free holomycin; no complete in-vitro biosynthesis or reaction-order assertion is introduced.

### related_records[0]; bioactivity_summary

evidence: supported. Targets: CHEBI:156451.

The exact pinned sibling is relevant to the antibacterial summary and same-structure linkage. Its mechanism explicitly qualifies weak purified RNAP inhibition and unresolved direct target. Its imported definition is not independent mechanistic proof; deposited sample chemistry and written assay endpoints are assessed separately.

### discussions[0]

completeness: supported. Targets: CHEBI:156451.

The shared-structure question concerns three source concepts. Primary native scopes and current literal graphs are considered separately; no source occurrence is transferred solely because the full Standard key is shared.

### occurrences[0]

evidence: supported. Targets: CHEBI:156451.

PMID32642829 supports the exact NRRL B-24137 source after the reported induction; not an unqualified baseline-production claim.

### occurrences[1]

evidence: unknown. Targets: CHEBI:156451.

PMID863793/1977 exact title is retained but no abstract/full body; genus source assertion remains unclosed at detailed primary scope.

### occurrences[2]

evidence: unknown. Targets: CHEBI:156451.

The literal review is only partly inspected; no exact holomycin/S. albidoflavus bridge is established. Do not infer absence from a partial review.

### occurrences[3]

evidence: supported. Targets: CHEBI:156451.

Review Table 1 names S. coelicolor expression hosts; PMID23147422 abstract independently reports introduced-host production. This is occurrence, not native production.

### occurrences[4]

evidence: supported. Targets: CHEBI:156451.

PMID28627048 identifies isolated holomycin from Streptomyces sp. DT-A37; no transfer of activity from other derivatives.

### occurrences[5]

evidence: supported. Targets: CHEBI:156451.

Original S2753 identification is positive. JMIB deposited comment explicitly links historical P. halotolerans to later P. galatheae; preserve original source naming.

### occurrences[6]

evidence: supported. Targets: CHEBI:156451.

Original abstract/indexed passages identify native ATCC29473 holomycin. Full-body access remains incomplete.

### occurrences[7]

evidence: unknown. Targets: CHEBI:156451.

Exact positive producer is S. flavogriseus NJ-4; no flavovirens name occurs in the complete retained XML text. Unread phylogram labels and external synonym possibilities are not adjudicated; do not yet claim a proved biological absence.

### occurrences[8]

evidence: supported. Targets: CHEBI:156451.

S. flavogriseus NJ-4 purified holomycin is positive; condition-specific yields/other antibiotics stay distinct.

### occurrences[9]

evidence: supported. Targets: CHEBI:156451.

Same exact NJ-4 primary as the LOTUS species row, not an independent publication.

### occurrences[10]

evidence: supported. Targets: CHEBI:156451.

Native-background profiles include holomycin; shunt intermediates and methylated derivatives remain separate.

### occurrences[11]

evidence: unknown. Targets: CHEBI:156451.

PMID23361841 abstract discusses cephamycin regulation without an exact holomycin endpoint; full body is required before accepting or excluding this occurrence.

### occurrences[12]

evidence: supported. Targets: CHEBI:156451.

PMID24323287 is a review with named S. clavuligerus holomycin; not an independent primary production experiment.

### occurrences[13]

evidence: supported. Targets: CHEBI:156451.

PMID23147422 supports native overproducer endpoints and separately a heterologous S. coelicolor result; keep these experimental units distinct.

### occurrences[14]

evidence: supported. Targets: CHEBI:156451.

The native purified product/profile and late enzyme study support occurrence; the HlmI assay is a distinct biochemical endpoint.

### occurrences[15]

evidence: supported. Targets: CHEBI:156451.

Full primary shows native product and genetic perturbation, independently of the partial NRPS enzyme endpoint.

### occurrences[16]

evidence: unknown. Targets: CHEBI:156451.

PMID15819635 abstract does not state exact holomycin occurrence; this is a remaining source-applicability gap, not a confirmed false triple.

### occurrences[17]

evidence: supported. Targets: CHEBI:156451.

PMID26187955 abstract supports the native-species ΔclaR derivative; do not describe an unmodified wild-type readout.

### occurrences[18]

evidence: supported. Targets: CHEBI:156451.

PMID30194098 abstract supports the source-specific oppA2 mutant expression/metabolite context.

### occurrences[19]

evidence: supported. Targets: CHEBI:156451.

PMID22344669 abstract supports NP1/argR-mutant context; preserve the named experimental stocks.

### occurrences[20]

evidence: unknown. Targets: CHEBI:156451.

PMID20889745 is a genome report; its abstract lacks an exact holomycin measurement. A genome/title alone does not independently close occurrence.

### occurrences[21]

evidence: supported. Targets: CHEBI:156451.

PMID12426344 reports holomycin identification in native-species mutants; the claim is not a general unmodified-strain measurement.

### occurrences[22]

evidence: supported. Targets: CHEBI:156451.

Exact clavu7/standard comparison is positive. Tested parent non-detection is not global incapacity, and plasmid-loss causality is not established.

### occurrences[23]

evidence: supported. Targets: CHEBI:156451.

Same PMID21041678 primary as the LOTUS PNAS row; source-provider duplication is not publication independence.

### occurrences[24]

evidence: supported. Targets: CHEBI:156451.

MED PMID468729 identifies MM21801 as holomycin from S. clavuligerus; unrelated CBA identifier collision is excluded.

### Stored representation and source-concept provenance

identity: supported. Targets: CHEBI:156451.

The complete source row BGC0000373:1 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: CHEBI:156451.

Exactly one committed three-star default ChEBI row matches; its current graph is checked separately.

### Exact literal chemical identifier scope

representation: supported. Targets: CHEBI:156451.

Measured exact-literal comparisons: [{"comparison": {"same_charge": true, "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi": true, "same_stereo_removed_standard": true}, "identifier": "npatlas:NPA013565", "scope": "Exact returned representation"}, {"comparison": {"same_charge": true, "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi": true, "same_stereo_removed_standard": true}, "identifier": "pubchem:10262683", "scope": "Exact returned representation"}, {"comparison": {"same_charge": true, "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi": true, "same_stereo_removed_standard": true}, "identifier": "chembl:CHEMBL476226", "scope": "Exact returned representation"}]. Standard identity, fixed-H tautomerism, explicit stereo and coordinate-derived depiction are separate. No more specific authority graph is automatically adopted.

### ChEBI full-key eligibility and serialization

grounding: supported. Targets: CHEBI:156451.

[{"eligible": true, "id": 156451, "literal_default_comparison": null, "literal_default_parse": false, "mol_comparison": {"same_charge": true, "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi": true, "same_stereo_removed_standard": true}, "name": "holomycin", "stars": 3}]. CHEBI156451 is the unique exact three-star committed projection. Official MOL/stated InChI match; literal default SMILES is invalid and is not copied.

### Exact committed sibling structure scope

representation: supported. Targets: CHEBI:156451.

The exact external committed sibling stated InChI/full key agrees; its literal SMILES fails parsing and is preserved without repair. SAME_STRUCTURE is supported at stated-InChI scope, not by copying the invalid string or treating imported definitions as independent experiments.

### Exact original deposited sample structure

representation: supported. Targets: CHEBI:156451.

The pinned root original-SDF comparison reports full Standard/fixed-H agreement for SID441245207. This is deposited-graph support only; sample purity, original natural isolation and endpoint mechanism remain separately scoped.

### Primary identity and experimental precision

scope: supported. Targets: CHEBI:156451.

The original closed-disulfide holomycin drawing independently matches the complete achiral owner. Exact authority, committed sibling stated InChI and original deposited sample agree; invalid external default SMILES are preserved separately. Biological target and stock applicability remain independently scoped.

## Findings

### S244-F-RNAP-DEFINITION: The definition overstates direct RNA polymerase inhibition

major / open / confirmed; issue key: holomycin-direct-rnap-definition-scope.

The imported definition presents holomycin as a DNA-dependent RNA polymerase inhibitor. The inspected original study supports a whole-cell transcription phenotype but reports weak effects in two purified RNAP assay formats and leaves the direct molecular target unresolved. Preserve the antibacterial/transcription phenotype while qualifying this direct-enzyme assertion.

## Recommended Actions And Acceptance Checks

### S244-ACT-RNAP-DEFINITION

Implement a consumed definition qualification or replacement, guarded by CHEBI:156451, the owner identifier/full key, the exact old definition and the complete source row SHA256 aa6610aa2163fa65a24b58de5f5ca7de2a4f49e314742defee505203150525ba. Retain structural identity and source attribution; describe cellular transcription effects with the direct molecular target unresolved. A curator discussion alone is not a repair because current reseeding reimports the definition. Do not overwrite the raw inventory or substitute an unverified alternative target.

- The exact guarded raw ChEBI row remains unchanged: {"chebi_id":"CHEBI:156451","definition":"A dithiolopyrrolone antibiotic that is 4,5-dihydro[1,2]dithiolo[4,3-b]pyrrole in which the hydrogens at positions 5 and 6 have been replaced by oxo and acetamido groups, respectively. It is an inhibitor of DNA-dependent RNA polymerase, and exhibits antibacterial and antitumour properties.","name":"holomycin","smiles":"CC(=O)Nc1c2sscc-2nc1=O","standard_inchi_key":"HBUNPJGMNVQSBX-UHFFFAOYSA-N","stars":"3"}
- A focused test rejects changed source row, identifier, key or old definition; unrelated ChEBI-derived definitions are unchanged.
- A reseed reproduces the qualified definition and preserves the existing ORF3488 pathway, causal graph, evidence and all independent assay observations.
- Primary PMID11158751 is attached directly to the qualification; weak purified RNAP inhibition and cellular transcription inhibition remain distinct.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R244-OWNER | data/natural_products/alkaloids/holomycin.yaml; Complete actual owner, optional assertions and all history events | supports | Root read the complete post-intake owner: 25 occurrence, 3 producer and 3 locus assertions. Optional fields: definition, biosynthetic_pathway, causal_graphs, bioactivities, bioactivity_summary, related_records, discussions. No external component is present. |
| R244-LOCAL | /private/tmp/npm-review-work/244/local-sources.json; Complete resolved owner and all six officially captured row sets | context_only | All six captured sets and the separately compared seventh PubChem set match exact frozen preparation. Source fidelity does not establish experimental support. |
| R244-PUBCHEM-PREP | data/raw/pubchem_bioassay.tsv; All exact-key raw rows, separately compared with the six officially captured tables | context_only | This target has 1 raw rows and 1 written observations. The cohort has 21 retained assay rows, all written, plus one 245 no-data sentinel. No current-only result or absent endpoint is inferred from this inventory. |
| R244-Q1144013 | https://www.wikidata.org/wiki/Q1144013; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-Q16993573 | https://www.wikidata.org/wiki/Q16993573; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-Q22285363 | https://www.wikidata.org/wiki/Q22285363; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-Q22286833 | https://www.wikidata.org/wiki/Q22286833; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-Q2355919 | https://www.wikidata.org/wiki/Q2355919; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-Q62851309 | https://www.wikidata.org/wiki/Q62851309; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-Q7623381 | https://www.wikidata.org/wiki/Q7623381; Retained 16-entity response; relevant English labels/P225/P685 read, not an audit of unrelated claims | context_only | The literal P225/P685 values match the raw organism source. This identifier routing is not experimental occurrence evidence. |
| R244-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=1883,1886,1901,1902,1911,1931,7787,9606,10116,28576,29486,52258,57139,67299,77133,140106,173560,265726,272129,312885,330879,331992,355589,455632,527005,665115,746128,1654360,1735992,1873369; Relevant TaxId, ScientificName, rank, parent and complete OtherNames fields | context_only | Streptomyces clavuligerus 1901 includes ATCC 27064; Yersinia ruckeri 29486 and ATCC 29473 strain 527005 remain distinct levels. Photobacterium halotolerans 265726 and P. galatheae 1654360 are separate current species records. S. flavovirens 52258 and S. flavogriseus 67299 remain distinct, as do genus 1883 and named species. These labels do not resolve the source-specific occurrence or stock applicability assessed with primary evidence. |
| R244-IMODULON | https://imodulondb.org/api/datasets; Complete 20-organism/28-dataset official catalogue | context_only | The native emitted producers are not exact organism/strain matches in the returned 20-organism catalogue. S. albidoflavus J1074 and several S. coelicolor strains are present as expression-resource contexts relevant to separate holomycin occurrence/engineered-host literature. Their catalogue presence neither establishes natural production nor proves a particular introduced strain shares the transcriptome experiment. Unnamed S. albus in the hydroxysporine expression paper must not become J1074 by assumption. No gene-set membership, expression matrix or causal mechanism queried. |
| R244-IMOD-META-0 | https://imodulondb.org/api/datasets/s_albidoflavus/modulome/meta; Complete dataset metadata, including explicit strains | context_only | S. albidoflavus metadata lists J1074; S. coelicolor metadata lists several named strains. These resources do not identify an unnamed introduced host or establish native production, stock equality, module membership or expression-linked chemistry. |
| R244-IMOD-META-1 | https://imodulondb.org/api/datasets/s_coelicolor/modulome478/meta; Complete dataset metadata, including explicit strains | context_only | S. albidoflavus metadata lists J1074; S. coelicolor metadata lists several named strains. These resources do not identify an unnamed introduced host or establish native production, stock equality, module membership or expression-linked chemistry. |
| R244-ASSAY-PLAN | /private/tmp/npm-review-work/shared-next-batch025/root-authoring/assay-source-plan-v2.json; orders.244.rows: exact written order, full raw-row SHA256, deposited SID/current summary tuple and endpoint scope | context_only | The plan preserves all 21 written observations across 244/246/248. There is no retained raw assay overflow; the separate 245 no-data sentinel is not an observation. |
| R244-ASSAY-ROOT-READ | /private/tmp/npm-review-work/shared-next-batch025/root-assay-source-read-001.json; All 21 exact retained-row joins and notes; 19 descriptions, 18 complete protocols, one high-level description and one metadata-only endpoint | context_only | Root read the original source endpoints and exact sample/target context. AID1347160 was inspected at high-level description scope; AID720532 only at summary metadata scope. Neither scope is presented as a complete protocol read. |
| R244-ASSAY-SUMMARY | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10262683/assaysummary/JSON; Table.Columns/Table.Row: exact current_match tuples in the pinned assay plan | supports | Exact retained source outcomes and reported numeric endpoints agree with current summary tuples. Additional current-only results do not replace retained observations. Summary equality is not molecular-target or purity evidence. |
| R244-AID-1645860 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1645860/description/JSON; Retained aid-descriptions-02.json: PC_AssayContainer[8].assay.descr; name/description/protocol/comment/target fields | supports | Purified USP30 ubiquitin-rhodamine cleavage screen; the deposited Active call has no emitted potency. Human Q70CQ3 is the source enzyme accession. This screen does not establish selectivity, a clinical mechanism or a polymerase target. |
| R244-SAMPLE-GRAPHS | /private/tmp/npm-review-work/shared-next-batch025/root-assay-sample-graph-comparison-001.json; Results for SID441245207,134970445,376241807; Huperzine interpretation qualified by SAMPLE-PRECISION | context_only | The exact deposited holomycin and ilicicolin H sample graphs agree at Standard/fixed-H scope. This does not prove vial purity or natural isolation; the original Huperzine SDF-only diagnostic is qualified by the later atom/bond and coordinate analysis. |
| R244-USP30 | https://rest.uniprot.org/uniprotkb/Q70CQ3.json; Reviewed human USP30 accession, organism, sequence length and catalytic annotation | context_only | Q70CQ3 identifies human USP30, 517 amino acids, consistent with the source biochemical assay target. This database identity is distinct from sample selectivity or clinical mechanism. |
| R244-SIBLING-HOLOMYCIN | https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/holomycin.yaml; Pinned sibling activity_class and qualified mechanism; exact committed source record | context_only | The pinned sibling supplies ANTIBACTERIAL summary support with a qualified transcription mechanism. |
| R244-SEEDER | scripts/seed_from_sources.py; classify_activity lines 160–178; PubChem projection/sorting and summary lines 1310–1378 | context_only | The current consumer accepts an exact AID/title exception before broad patterns, preserves source calls and endpoints, and derives positive summary classes from active written observations and sibling sources. |
| R244-CLASSIFIER-TESTS | tests/test_seed_skeleton.py; Classifier, exact AID1650 counterassay, endpoint and derived-summary tests around lines 985–1054 | context_only | Existing focused tests provide the consumed regression route for a narrow SERCaMP exception and preservation of calls, values, source target context and unrelated classifications. |
| S244-E-LOCAL | /private/tmp/npm-review-work/244/local-sources.json; Complete resolved owner and captured rows; exact seven-set equality checked | context_only | Complete actual owner including any inline graph/pathway, six captured source sets and separately compared seventh PubChem set match the prepared complete reads. |
| S244-E-CONSUMERS | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; LOTUS exclusion, producer/locus emission, method overrides and correction order | context_only | Static inspection covers exact LOTUS exclusions, source method grading and producer/reference qualification order. Exact consumers have their own evidence snapshots. |
| S244-E-SCHEMA | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; ProducerEvidenceBasisEnum and ClusterLinkEvidenceEnum; conf/producer_evidence.tsv and grading.py also read and pinned | context_only | Producer tiers concern evidence in the named organism; cloned-locus experiments are a distinct cluster question. Empty methods and a source assertion do not independently assert native knockout or exact pure-enzyme proof. |
| S244-E-SEARCH | /private/tmp/npm-review-work/244/science-search.json; Exact read scope | context_only | Exact current curated-decision search is retained. Its scope is the curation tree; it does not establish absence of experimental evidence or all possible consumers. |
| S244-E-DEFINITION-CONSUMER | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; CURATOR_OWNED_CARRIED_FIELDS; carry_curator_owned_fields; unique ChEBI definition assignment | context_only | A unique ChEBI definition is imported on seeding; arbitrary edited definitions are not among carried curator fields. Inline graphs and curator-prefixed discussions have distinct preservation rules. |
| S244-E-GRADE-MAP | /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv; Complete method-to-producer/cluster table and native-versus-host rationale | context_only | The source vocabulary separately grades native producer and cluster claims; pure-enzyme evidence and introduced-host expression do not independently establish a native producer. |
| S244-E-GUARDS | /private/tmp/npm-review-work/shared-next-batch025/provisional-science-241-245/source-row-guards.json; All ten future target owner pins and complete raw-row guards | context_only | Exact prepared owners and all seven raw sets, including full parsed rows and SHA256 guards. This is provenance, not independent biology. |
| S244-E-HOLO-CLAV | https://www.ncbi.nlm.nih.gov/nuccore/CM000913.1; ATCC27064 source and SCLAV5271 native CDS within literal 6204480..6222797 window | supports | Deposited-source/locus annotation bridge only; primary experimental applicability is evaluated separately. Read scope: Source/features read; exact named reference protein sequences compared where stated. No cloning-boundary or experimental-plasmid identity inferred. |
| S244-E-HOLO-META | https://www.ebi.ac.uk/europepmc/webservices/rest/search; MED result IDs and their title/abstract fields, not the unrelated CBA result also numbered 468729 | partial | Original abstracts provide claim-specific positive occurrences for several native/mutant stocks. Abstracts without exact holomycin occurrence are access-limited, not negative evidence. Read scope: All 23 MED metadata results read; full-body availability differs by article and is recorded below. PMID863793 has no abstract. |
| S244-E-HOLO-PHOTO | https://www.ncbi.nlm.nih.gov/nuccore/JMIB01000043.1; S2753 source, annotated features and explicit 2015 reclassification comment in literal 78725..91151 window | supports | Deposited-source/locus annotation bridge only; primary experimental applicability is evaluated separately. Read scope: Source/features read; exact named reference protein sequences compared where stated. No cloning-boundary or experimental-plasmid identity inferred. |
| S244-E-HOLO-SIBLING | https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/holomycin.yaml; Pinned committed holomycin sibling: definition, mechanism evidence, class and structure | supports | The antibacterial class and same-structure relationship are relevant; the sibling mechanism explicitly distinguishes cellular transcription effects from weak purified RNAP inhibition and unresolved direct target. Its imported definition is not independent mechanistic proof. Read scope: Complete exact retained sibling owner read, including imported definition and curator mechanism caveat. |
| S244-E-HOLO-YER | https://www.ncbi.nlm.nih.gov/nuccore/ACCC01000028.1; ATCC29473 source and annotated features in literal 3593..21565 window | supports | Deposited-source/locus annotation bridge only; primary experimental applicability is evaluated separately. Read scope: Source/features read; exact named reference protein sequences compared where stated. No cloning-boundary or experimental-plasmid identity inferred. |
| S244-E-HOLO01-005 | DOI:10.1128/AAC.45.2.532-539.2001; original lines approximately 80–450; publisher-provided ResearchGate transcription | supports | The cellular RNA-synthesis phenotype is positive. The two purified-enzyme formats showed weak inhibition; the paper leaves the direct molecular target unresolved. This does not establish a selective direct RNAP mechanism. Read scope: Overlapping retained captures jointly cover the complete scientific body; no original PDF pixels were inspected. Capture time is a tool-response capture, not an invented direct HTTP receipt. |
| S244-E-HOLO01-006 | DOI:10.1128/AAC.45.2.532-539.2001; original lines approximately 400–800; publisher-provided ResearchGate transcription | supports | The cellular RNA-synthesis phenotype is positive. The two purified-enzyme formats showed weak inhibition; the paper leaves the direct molecular target unresolved. This does not establish a selective direct RNAP mechanism. Read scope: Overlapping retained captures jointly cover the complete scientific body; no original PDF pixels were inspected. Capture time is a tool-response capture, not an invented direct HTTP receipt. |
| S244-E-HOLO01-007 | DOI:10.1128/AAC.45.2.532-539.2001; original lines approximately 760–1180, through Discussion; publisher-provided ResearchGate transcription | supports | The cellular RNA-synthesis phenotype is positive. The two purified-enzyme formats showed weak inhibition; the paper leaves the direct molecular target unresolved. This does not establish a selective direct RNAP mechanism. Read scope: Overlapping retained captures jointly cover the complete scientific body; no original PDF pixels were inspected. Capture time is a tool-response capture, not an invented direct HTTP receipt. |
| S244-E-HOLO01-ABSTRACT | PMID:11158751; Original PubMed abstract for the 2001 mode-of-action study | supports | Whole-cell transcription effects and weak purified RNA-polymerase inhibition must be distinguished. Read scope: Complete original abstract read. |
| S244-E-HOLO10-002 | DOI:10.1073/pnas.1014140107; Results and biosynthetic NRPS experiments in the original PNAS full-text capture | supports | Native ORF3488/3489 deletion affects holomycin; purified ORF3488 activates and tethers L-Cys. These are distinct endpoints, and the partial owner graph does not claim complete product reconstitution. Read scope: Combined captures cover the complete scientific body. Original SI routes failed and are not represented as inspected. |
| S244-E-HOLO10-003 | DOI:10.1073/pnas.1014140107; continuation through Methods and references in the original PNAS full-text capture | supports | Native ORF3488/3489 deletion affects holomycin; purified ORF3488 activates and tethers L-Cys. These are distinct endpoints, and the partial owner graph does not claim complete product reconstitution. Read scope: Combined captures cover the complete scientific body. Original SI routes failed and are not represented as inspected. |
| S244-E-HOLO11-HLMI | PMID:21504228; Article PMC3101288 only: complete scientific body and native profile/late oxidase experiments | supports | Native holomycin and HlmI late oxidative chemistry are positive. Reduced production after deletion is not complete absence; no direct RNAP target follows. Read scope: Complete scientific body read, distinct from other articles within the same XML. |
| S244-E-HOLO11-MARINE | PMID:21339958; Original sections 2.1–2.3 and 3.6, S2753 identification and compound characterization | supports | Exact S2753 was then named P. halotolerans and yielded characterized holomycin. Current deposited sequence explicitly records its later reclassification to P. galatheae. Read scope: Targeted scientific sections read, not a complete re-audit of every marine isolate. |
| S244-E-HOLO12-ADAPT | PMID:22470465; Adaptive-study strain Methods, exact holomycin Results and Figure 3/4 captions | supports | ATCC27064-derived clavu7 gives an authentic-standard LC-MS/MS holomycin endpoint. Parent non-detection is limited to tested conditions. The evolved derivative is not unmodified wild type, and plasmid loss alone is not proved causal. Read scope: Targeted original body and independent peer read, no complete figure-pixel audit. |
| S244-E-HOLO12-METHYL | PMID:23097183; Article PMC3573328 only: native profiles and Discussion of self-protection | supports | Holomycin occurs in the compared native backgrounds; methylated shunts and suggested self-protection mechanisms must not be substituted for the named product or a resolved direct target. Read scope: Scientific body read in segments, including the final Discussion in this freeze turn; caption scope preserved. No new independent spectral assignment. |
| S244-E-HOLO13-INDEXED | PMID:23572522; Indexed original PMC3663494/JBC article excerpts; native ATCC29473 and Hom12 resistance passages | partial | Exact native Y. ruckeri holomycin and hom6 deletion are positive. Hom12 expression in E. coli is a resistance experiment and is not itself whole-cluster holomycin production. Imported heterologous-method applicability remains incompletely resolved. Read scope: Search/indexed excerpts only, supported by original abstract. Full scientific body remains unavailable; persistence time is later than the actual inspection. |
| S244-E-HOLO14-REVIEW | DOI:10.1007/s10295-013-1348-5; Original review opening and Table 1, holomycin introduced-host entries; continuation failure retained separately | partial | S. coelicolor introduced-host occurrence is supported at secondary-source scope. The S. albidoflavus triple is not resolved by the inspected portion; no native stock inference is made. Read scope: Partial secondary review only; not a complete absence search across the paper. |
| S244-E-HOLO17-NJ4 | PMID:28740758; Complete retained scientific text; NJ-4 identity and purified holomycin characterization; all XML text-node exact-name search | supports | Positive source organism is S. flavogriseus NJ-4. S. flavovirens is absent from the retained XML text; the asserted flavovirens triple has no established bridge in this inspection. Its applicability remains a targeted question rather than a global absence claim. Read scope: Original body read plus independent complete-text peer. No new phylogram-pixel or external taxonomic-synonym adjudication. |
| S244-E-HOLO21 | PMID:33771780; Original PMC8208159 capture through line 244/Table 3; remaining routes include explicit CAPTCHA failures | partial | S2753 native holomycin loss after hlmE deletion is supported; complementation/activity and biofilm endpoints remain distinguished from exact chemical rescue. Read scope: Partial scientific body plus original abstract; not complete remaining Methods. |
| S244-E-LIMITS | /private/tmp/npm-review-work/shared-next-batch025/bgc-science/source-notes.json; All five record narratives and bounded access limitations | context_only | Source-specific read/access limits remain explicit. Available sources do not establish the unavailable original bodies or experimental allele/construct identities. |
| S244-E-MIBIG0373.5 | https://mibig.secondarymetabolites.org/repository/BGC0000373.5; Exact versioned source, selected compound name/index, source organism/accession and imported evidence methods | context_only | Current versioned annotation matches the retained source concept; its evidence labels are interpreted against the original study, not treated as new independent experiments. |
| S244-E-MIBIG2091.3 | https://mibig.secondarymetabolites.org/repository/BGC0002091.3; Exact versioned source, selected compound name/index, source organism/accession and imported evidence methods | context_only | Current versioned annotation matches the retained source concept; its evidence labels are interpreted against the original study, not treated as new independent experiments. |
| S244-E-MIBIG2412.2 | https://mibig.secondarymetabolites.org/repository/BGC0002412.2; Exact versioned source, selected compound name/index, source organism/accession and imported evidence methods | context_only | Current versioned annotation matches the retained source concept; its evidence labels are interpreted against the original study, not treated as new independent experiments. |
| S244-E-OCC-LEDGER | /private/tmp/npm-review-work/shared-next-batch025/bgc-science/occurrence-ledger.json; Per-record occurrences[0..n], complete raw joins and raw-only Holomycin row | context_only | All31 written occurrence assertions have exact raw joins and source-specific scopes; Holomycin has one additional raw-only row. |
| S244-E-PROTEIN-COMPARE | /private/tmp/npm-review-work/shared-next-batch025/bgc-science/native-protein-comparison-001.json; All nine result rows and exact input pins | supports | Eight A1163 Has references and S. clavuligerus ORF3488 match current UniProt, GenPept, native annotated translation and independently translated genomic CDS. Experimental alleles and functional results are separate. Read scope: Locally computed four-way sequence identity, with independent static peer; no repeated experimental validation. |
| S244-E-ROUTING | /private/tmp/npm-review-work/shared-next-batch025/bgc-science/curator-routing.json; Six exact source/consumer routes and their limitations | context_only | Current consumed correction routes and missing contracts are distinguished. No code change, graph migration or exclusion has been made. |
| S244-E-SEED-TESTS | /private/tmp/npm-record-reviews-20261021/tests/test_seed_skeleton.py; Curator carry, structure-identity guards and producer-strain tests inspected statically | context_only | Existing tests show same-key curator-graph/discussion carry, producer-only strain overlays and composition rejection. A new definition override needs dedicated tests. |
| S244-E-UP-E2PZ83 | https://www.uniprot.org/uniprotkb/E2PZ83; Organism, entry status, sequence, cited function annotations and cross-references for the exact accession | supports | Current exact reference-protein annotation and sequence; experimental allele identity and functional proof are separately scoped. |
| C244-OWNER | data/natural_products/alkaloids/holomycin.yaml; Complete owner and all seven matching source-row sets; no referenced components | supports | The complete owner denotes holomycin under CHEBI:156451. All source selectors, versions and complete row digests are retained in COMPARISON: [{"row_sha256": "fde7b9b561a09c61a248c0e20c2efd0194ecbd32a6deb38450b94b22476edf7e", "selector": "BGC0000373:1", "version": "5"}, {"row_sha256": "193f8de32399c315b744143438adc0649d15eb957764e546d670818db151e5f0", "selector": "BGC0002091:1", "version": "3"}, {"row_sha256": "d51b289d49587ca8c8f2ab0e1ff1b348535c3c5f4fe21cdc6f59c9a82cbcbadf", "selector": "BGC0002412:1", "version": "2"}]. The official intake and prepared owner bytes agree. |
| C244-GRAPH | /private/tmp/npm-review-work/244/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to HBUNPJGMNVQSBX-UHFFFAOYSA-N, formula C7H6N2O2S2, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C244-COMPARISON | /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/retained-graph-comparison.json; Record 244; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner and complete raw rows; current authority responses and primary proof are separate evidence. |
| C244-LOCAL-SEARCH | /private/tmp/npm-review-work/244/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C244-AUTHORITY-COMPARISON | /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/authority-graph-comparison.json; Complete literal Standard/fixed-H, formula, charge and stereo comparison; exact source payload pins retained | supports | Current authority graphs and source-specific serialization differences are independently compared. Database agreement is not primary natural-hand proof. |
| C244-AUTHORITY-DETAIL | /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/source-plan-002.json; Complete literal Standard/fixed-H, formula, charge and stereo comparison; exact source payload pins retained | supports | Current authority graphs and source-specific serialization differences are independently compared. Database agreement is not primary natural-hand proof. |
| C244-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0000373.5/annotations.json; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/BGC0000373.5.json | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-2 | https://mibig.secondarymetabolites.org/repository/BGC0002091.3/annotations.json; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/BGC0002091.3.json | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-3 | https://mibig.secondarymetabolites.org/repository/BGC0002412.2/annotations.json; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/BGC0002412.2.json | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-4 | https://www.npatlas.org/api/v1/compound/NPA013565; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/NPA013565.json | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-5 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10262683/SDF; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/pubchem-10262683.sdf | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-6 | https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL476226.json; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/CHEMBL476226.json | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-7 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/156451/; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/CHEBI156451.json | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-8 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156451/; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/CHEBI156451.mol | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-AUTH-9 | https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/holomycin.yaml; Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/sibling-holomycin.yaml | supports | Exact source representation at its recorded access time; primary identity and natural hand are assessed separately. |
| C244-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=HBUNPJGMNVQSBX-UHFFFAOYSA-N&amp;size=100; Complete bounded key/name response /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase003-public-reads/chebi-key-244.json | supports | HTTP200; exact source response and candidate eligibility preserved. |
| C244-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=holomycin&amp;size=100; Complete bounded key/name response /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase003-public-reads/chebi-name-244.json | supports | HTTP200; exact source response and candidate eligibility preserved. |
| C244-HOLO11-HLMI | PMID:21504228; Article PMC3101288 only: introduction and holomycin/reduced-holomycin characterization paragraph; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/bgc-science/public-003-retry/primary-recovery-a.xml | supports | The closed-disulfide product and reduced dithiol are distinct; direct RNAP target remains qualified. |
| C244-PRIMARY-FIGURE | PMID:21504228; Original Figure1A R=CH3 and Figure1B holomycin1; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase011-public-reads/holomycin2011-fig1.jpg | supports | Complete achiral N-acetyl dithiolopyrrolone graph, distinct from reduced2. |
| C244-SOURCE-LIMITS | /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/source-notes.json; Entry244: observations/limitations, exact source rows, authority/primary pins; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/source-notes.json | supports | Source-specific precision and access limits; not an authority vote. |
| C244-PRIMARY-COMPARISON | /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/primary-mapping-001/holomycin-primary-comparison-001.json; Exact record244: independent source graph, input pins, model and roundtrip; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/primary-mapping-001/holomycin-primary-comparison-001.json | supports | Literal source/model diagnostic with explicit limits; no replacement selected. |
| C244-SAMPLE-COMPARISON | /private/tmp/npm-review-work/shared-next-batch025/root-assay-sample-graph-comparison-001.json; Original deposited SDF results for order244; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/root-assay-sample-graph-comparison-001.json | supports | Pinned root deposited-graph comparison; not purity or experimental endpoint proof. |

## Limits And Additional Notes

- The PubChem audit preserves exact deposited calls and endpoint scope. Across the cohort, 18 complete protocols and one additional high-level biochemical description were read; one pathogen-related assay remains metadata-only. No vial-specific purity, clinical efficacy or direct binding is inferred. Current CID precision and BindingDB molecular-target/graph assessments remain separate.
- Context covers exact owner/history, seven source inventories, literal organism routing and computed classification. Present definitions, graphs, pathways, sibling links and molecular-target claims retain their separate scientific and chemical assessments. Taxonomic agreement does not prove stock equivalence or occurrence. Homoanatoxin-a context is high-level identity and provenance only.
- Several occurrence bodies and the complete Yersinia original remain unavailable; lack of a product name in an abstract is not negative evidence.
- The flavovirens and albidoflavus occurrence bridges remain unresolved; no blanket taxon exclusion is selected.
- The actual assay protocols/classifier assessment is independently supplied by the root assay section; no assay finding is duplicated here.
- Current E2PZ83/native CDS agreement is a reference identity bridge, not a reconstruction of tags or historical plasmids.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
- Deposited graph agreement is not vial purity, direct-target or exact historical-stock proof. External SMILES parse failure is retained, not silently repaired.
- The first fresh QC attempt failed during the public vendored-sync fetch after lint passed. Only the separately recorded complete successful QC retry002 is used as the baseline check; the actual failed001 receipt/log/capture/root observation remain bound.
- Reproduction retains42 withheld ambiguous producer claims,161 merged-taxon rewrites and5 unresolved assay-organism targets.
- 499non-blocking plausibility warnings and4750no-adapter skips remain.
- Four skipped tests and two dependency warnings remain disclosed. Reproduction also reports42 withheld ambiguous-producer claims,161 merged-taxon rewrites and5 unresolved assay-organism rows. Gate success is configured consistency, not scientific validation of every claim.
- Clarification of root review-queue observation: actual session80402 terminal0 and receipt/hash are confirmed. Combined initial log display was truncated; root read its command/output header, displayed samples and final summary, then recovered all12 queue headers in a bounded projection. Root did not read all8928 per-record queue descriptions. No gate outcome changes.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions and no-adapter pairs; a successful command does not convert these into verified scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population was checked; external caches and generated bytecode are not asserted to be independently byte-pinned.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command receipts for this base. Scientific failed or unavailable checks are distinct from bundle validation.
- Scientific conclusions integrate the chemical, biological and provenance assessments; source access and unresolved scopes remain explicit.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
kind: record
repository: CultureBotAI/NaturalProductMech
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
review_id: 20261022T030308Z-holomycin
title: Scientific review of holomycin
started_at: '2026-10-22T02:59:33.976734Z'
finished_at: '2026-10-22T03:03:08.795086Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Holomycin identity and multiple source-specific native observations are
  supported. Its unqualified direct RNA-polymerase-inhibitor definition exceeds the
  inspected evidence: cellular transcription effects are positive, purified-enzyme
  inhibition is weak and the direct target remains unresolved. The partial NRPS graph
  remains supported, while several occurrence sources and the complete Yersinia method
  combination require further verification.'
source:
  git_revision: 71a28cf520dc96a7107b00d87703ba1e59acc02c
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 493fa5e0c192f3070ecee080db6b195c57faac048201cdd8f5dd6be47b587aae
    role: context
  - path: CLAUDE.md
    sha256: c783814c18591ea92aaa628fde98e6b0dbf1f59d45d240fe349682eec753e63f
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
  - path: conf/sibling_pins.yaml
    sha256: 39a1d007ee65ba546567e8a34b7a309f75270b872809e1f783fe1fcee55866f2
    role: context
  - path: conf/sources.yaml
    sha256: d5e8ab63eeebb376589a0c9bf6f7eb92f45913b84243de20d820442ec88d5a98
    role: context
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: 4bc422b93002508b0abb86e0fa0afa49aff88745b5b0dd3bcbf351a68725d766
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: f87a4fa580dede966366bece28ccfb6542bdec4a0f810e40cdfc719811407a05
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: b27c2e61e696a285c38bc88c852dbbdc6c06fec8c4584343f2b9146462eea6cf
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
  - path: data/natural_products/alkaloids/esmeraldin.yaml
    sha256: 27e283c4f4c21ba1311b8a6608f1a0a5f8d2f11e40d34f8b15637cc772e84e57
    role: context
  - path: data/natural_products/alkaloids/fervenulin.yaml
    sha256: 5ceec0624f718e3e54cc1699847c92e4314f3c947a78625f250311e53f221213
    role: context
  - path: data/natural_products/alkaloids/fischerindole-l.yaml
    sha256: e1e93f639462795e7f2a50f891e4df0d4039611c82a8b539780d9233ec11d752
    role: context
  - path: data/natural_products/alkaloids/flavichalasine-f.yaml
    sha256: 1ccb330fc29638e721072013846038e3a30e7cef38ed380ea6d2631e5fb6f809
    role: context
  - path: data/natural_products/alkaloids/flavichalasine-g.yaml
    sha256: 9837002422853afb552453b02064bbd27a0746ea1f009bc05253db3669a47bce
    role: context
  - path: data/natural_products/alkaloids/formycin-a.yaml
    sha256: c2910b97207eb4ede16883ea8f16ac519e58e51695472e7bac39b93b4ee00b3c
    role: context
  - path: data/natural_products/alkaloids/fumigaclavine-c.yaml
    sha256: 4fbf243118c5b8fb38bb25a88a702d97f9186c83f8df3853cecc944bd78b7da7
    role: context
  - path: data/natural_products/alkaloids/fumiquinazoline-a.yaml
    sha256: d9892bd99ed9a42be2520cf0d493c8a6df69f525db36c6f6366246d505ddfca6
    role: context
  - path: data/natural_products/alkaloids/fumiquinazoline-c.yaml
    sha256: b38d36d11366b39eba10c1019640f0e9fb9ccfd31a7dd2852441257885fa5ae3
    role: context
  - path: data/natural_products/alkaloids/fumiquinazoline-d.yaml
    sha256: 9056d4978a54375286e1ac8f0c17d316cc1f35ee7276a36ca8ec583bb4f3d3ef
    role: context
  - path: data/natural_products/alkaloids/fusaric-acid.yaml
    sha256: 08df80fe6e2184db09fadf22414f961ec3ed4c183a6bfba817a2899e13d203da
    role: context
  - path: data/natural_products/alkaloids/fusaridione-a.yaml
    sha256: c9739e915f6e22d331a6d25810a333f368adbd56aae03ee698e8fb3db175f690
    role: context
  - path: data/natural_products/alkaloids/fusarin-c.yaml
    sha256: b7393c2db3de8240089e532e542efe58aa43d1c84619df000e4e970c26bdf519
    role: context
  - path: data/natural_products/alkaloids/fusarin-d.yaml
    sha256: 7f5666f829a54a26078dc85792153ad656cc2aef0f6f8db48793fdcb629da106
    role: context
  - path: data/natural_products/alkaloids/fusarochromene.yaml
    sha256: f653a81c04f30502862e365013fef6947eb101c9b2d3594bf2ac1db978709812
    role: context
  - path: data/natural_products/alkaloids/fusatin.yaml
    sha256: cf9c1426d58fa207b0a81ff4af6a4afdaad5b1d68f9cc3d8756e3d790e3e1fa1
    role: context
  - path: data/natural_products/alkaloids/fusatinic-acid.yaml
    sha256: bc1df041b6b93fa1263f79739c48a3c9eb64ad797d01aec1834f5c0e0e22e73d
    role: context
  - path: data/natural_products/alkaloids/gaburedin-d.yaml
    sha256: a1ea0516f1e6c3a2e49ac68af1394148092a2c5327862d0253a3fbebc00ae2ef
    role: context
  - path: data/natural_products/alkaloids/gilvusmycin.yaml
    sha256: 5d76f1088d6338e31c76eaf665034151c33124dc90669c1f8c2c057efa3b8610
    role: context
  - path: data/natural_products/alkaloids/gladiofungin-a.yaml
    sha256: d5f92e508d0fd0febe6312c11c77b32d9fab8a8d15ff9752010bf67eda70e8d7
    role: context
  - path: data/natural_products/alkaloids/gladiofungin-b.yaml
    sha256: 0537d2d991e3555bf5d80eb18d58d901225b65770e4685da1a5ab3aea9a3b931
    role: context
  - path: data/natural_products/alkaloids/glandicoline-a.yaml
    sha256: 661c320e2d349c03e909e5b1b4a3cf9e01680d67f3a4e5890c5b3525ccdc9f19
    role: context
  - path: data/natural_products/alkaloids/glandicoline-b.yaml
    sha256: a0dbffefcec24c9150cfb7a0c374d88f399b072e012edf8eb17e9682f940891a
    role: context
  - path: data/natural_products/alkaloids/gonyautoxin-2.yaml
    sha256: b0c35c96128ccd3b1c00be59cb6fa9ac05aa890afa32696453fb966f7c3e98ba
    role: context
  - path: data/natural_products/alkaloids/griseoluteic-acid.yaml
    sha256: 0dd4033f1be811a42299ab2ff59f7ef982c4ce7d568a58ef75ef13ead0977fd6
    role: context
  - path: data/natural_products/alkaloids/grixazone-a.yaml
    sha256: 3afeef2427dbf63f2c1f33efb8d63262ba2a897f725ac54b4b225aa36e16e316
    role: context
  - path: data/natural_products/alkaloids/guanipiperazine-a.yaml
    sha256: 234f3406f9e6faf5c4c38db04dc8ef91ac859e59538ed0c29879df5ae5ce633b
    role: context
  - path: data/natural_products/alkaloids/guanipiperazine-b.yaml
    sha256: fbe1a98e00e730ecbae027c3eaaf9197e147fca076fe35d97615974defdefa1a
    role: context
  - path: data/natural_products/alkaloids/guanitoxin.yaml
    sha256: 96b4c6ac0c2fc969ae4ac042d4365ea4d73c655a7a6c6f69f8ed4b15f3d47204
    role: context
  - path: data/natural_products/alkaloids/hancockiamide-b.yaml
    sha256: 58b9d5b380eacc91cc1d3aab37d029a47c688385e40dc571ac81f02500765eb2
    role: context
  - path: data/natural_products/alkaloids/hancockiamide-c.yaml
    sha256: f5455801d553581ab6b134955ecb527b48fcdc2aa4e10c86e498aee815ed3335
    role: context
  - path: data/natural_products/alkaloids/hancockiamide-d.yaml
    sha256: 758bf46b4fe8f6572a482e563b64e2899f1d012dcd59d74cb761270fdc8e741f
    role: context
  - path: data/natural_products/alkaloids/hexadehydroastechrome.yaml
    sha256: a065c38b64efa17029b83d2381f84e8973b2f450b3a1b37a194ad0f639c12497
    role: context
  - path: data/natural_products/alkaloids/holomycin.yaml
    sha256: 125f0e310f19582f45f65b82dca90f687fd9463338de592bea14c720e432c3fa
    role: target
  - path: data/natural_products/alkaloids/homoanatoxin-a.yaml
    sha256: 532435867b2dc7742709c97d2e7a857d707bfdce2218e799b7fba96c4f7cd952
    role: context
  - path: data/natural_products/alkaloids/huperzine-a.yaml
    sha256: 5cd4ffb5e2c23fa2cc74b8982cab87d6dc4fe1aaaac89ca759d117fdb364a5a4
    role: context
  - path: data/natural_products/alkaloids/hydroxysporine.yaml
    sha256: 82203ab475b10e5e75bc4742963c5d1eb7ea98aa28ac2ea2c8e961d0d98ac163
    role: context
  - path: data/natural_products/alkaloids/ilicicolin-h.yaml
    sha256: a40244c649b727e078fae647300d2be11f9abd1616d865fe7c3d50e48be62bda
    role: context
  - path: data/natural_products/alkaloids/ilicicolin-j.yaml
    sha256: 83af9c59c72e30686a5bce5d8d725afa9b1475d36aa7609c676fbd6f5d759057
    role: context
  - path: data/natural_products/alkaloids/iminimycin-a.yaml
    sha256: c3d760bfba7f1a604735bf4d3a4ba4d04225870643d0e0dddc5edd172372ec00
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
    sha256: 6873daace2f9e2225ef3d6830e993ac8cf8d01cec66b779fa5829309d77b3eaf
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
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/lotus_exclusions.py
    sha256: 6352cac7c587eab5a56d907c523cc899d02d197009081624bf8649c675ee30f7
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/curate/xref_exclusions.py
    sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
    role: context
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
    role: context
  - path: src/naturalproductmech/graph_components.py
    sha256: 10f08517869f482954fd583fd19d5750ef286a76297c231e6c9a5ba8dc023e17
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: tests/test_lotus_exclusions.py
    sha256: 3e3aa443714202e1bc41f0fb236e6bf69caabd68a16af23b972323f5f846386c
    role: context
  - path: tests/test_seed_skeleton.py
    sha256: 72ec216fb0ed365b09f1cfb64fb06c701c50b5d7c2df409d8dbf613d302803bf
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 244, batch 025, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 300 of 3116 current
    records had campaign coverage and 2816 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:156451
targets:
- target_id: CHEBI:156451
  path: data/natural_products/alkaloids/holomycin.yaml
  label: holomycin
  record_class: NaturalProductRecord
  kind: generated
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: MIBiG source identity, producer and locus
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: LOTUS occurrence triples
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: CyanoMetDB exact-structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/holomycin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - CHEBI:156451
  command: just validate-strict data/natural_products/alkaloids/holomycin.yaml --out
    /private/tmp/npm-review-work/244/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-22T02:59:38.922485Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All3116 corpus records are filed exactly where PATHS.tsv pins them.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=71a28cf520dc96a7107b00d87703ba1e59acc02c
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-025-baseline-verify-corpus-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch025 execution on 71a28cf520dc96a7107b00d87703ba1e59acc02c
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-22T02:47:33.579477Z;
    finished 2026-10-22T02:47:57.474870Z; root observed terminal0 at 2026-10-22T02:48:04.628847Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-025/verify-corpus.json; exact
    transcript: /private/tmp/npm-native-checks/batch-025/verify-corpus.log; input
    proof: /private/tmp/npm-native-checks/batch-025/verify-corpus-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:156451
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All3116 records reproduce byte-for-byte from data/raw/.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=71a28cf520dc96a7107b00d87703ba1e59acc02c
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-025-baseline-verify-reproduction-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch025 execution on 71a28cf520dc96a7107b00d87703ba1e59acc02c
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-22T02:47:33.576606Z;
    finished 2026-10-22T02:48:13.940243Z; root observed terminal0 at 2026-10-22T02:48:29.005331Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-025/verify-reproduction.json;
    exact transcript: /private/tmp/npm-native-checks/batch-025/verify-reproduction.log;
    input proof: /private/tmp/npm-native-checks/batch-025/verify-reproduction-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:156451
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The canonical review-queue command completed with actual exit0 on the fresh
    main base; exact output, warnings and skips remain in the pinned transcript.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=71a28cf520dc96a7107b00d87703ba1e59acc02c
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-025-baseline-review-queue-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just review-queue --tsv /private/tmp/npm-review-queue-batch-025.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch025 execution on 71a28cf520dc96a7107b00d87703ba1e59acc02c
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-22T02:47:33.576310Z;
    finished 2026-10-22T02:47:48.002005Z; root observed terminal0 at 2026-10-22T02:48:04.629532Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-025/review-queue.json; exact
    transcript: /private/tmp/npm-native-checks/batch-025/review-queue.log; input proof:
    /private/tmp/npm-native-checks/batch-025/review-queue-fresh-inputs.json. Dedicated
    pytest basetemp isolates fixture retention; no cleanup was performed. Warnings,
    skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:156451
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: Configured identifier-label gate passed with13449canonical matches,646synonym
    matches and35configured exceptions.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=71a28cf520dc96a7107b00d87703ba1e59acc02c
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-025-baseline-validate-products-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch025 execution on 71a28cf520dc96a7107b00d87703ba1e59acc02c
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-22T02:47:33.580281Z;
    finished 2026-10-22T02:48:13.699538Z; root observed terminal0 at 2026-10-22T02:48:29.005677Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-025/validate-products.json;
    exact transcript: /private/tmp/npm-native-checks/batch-025/validate-products.log;
    input proof: /private/tmp/npm-native-checks/batch-025/validate-products-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:156451
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: 'Actual canonical just qc retry002 terminal0. All gates passed: lint;22
    governed artifacts; documentation;15 inventory provenance;44 source queue entries;999
    tests passed,4 skipped,2 dependency warnings;strict3116 zeroerrors;generated site;3116
    byte-identical reproduction;PATHS integrity;corpus report.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=71a28cf520dc96a7107b00d87703ba1e59acc02c
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-025-baseline-qc-attempt-002
    PYTHONDONTWRITEBYTECODE=1 just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch025 execution on 71a28cf520dc96a7107b00d87703ba1e59acc02c
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-22T02:52:11.932860Z;
    finished 2026-10-22T02:57:35.691390Z; root observed terminal0 at 2026-10-22T02:57:59.838835Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-025/qc-attempt-002.json;
    exact transcript: /private/tmp/npm-native-checks/batch-025/qc-attempt-002.log;
    input proof: /private/tmp/npm-native-checks/batch-025/qc-attempt-002-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:156451
- check_id: R244-FULL-OWNER
  name: Complete owner and captured-source scope
  status: passed
  required: true
  summary: Official successful intake and post-intake root reading precede authoring.
    All seven source sets reconcile. Inline graphs are present in 243, 244, 246 and
    248; 246 additionally has sixteen molecular_targets. These are inventories, not
    independent validation of every biological or affinity claim.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-LOCAL
  - R244-PUBCHEM-PREP
- check_id: R244-ASSAY-FIDELITY
  name: Written assay calls and reported endpoint fidelity
  status: passed
  required: true
  summary: All 1 written observations match their exact raw row and current sample/target
    tuple. Blank values remain blank, AC50/Potency remain OTHER, Inconclusive remains
    NOT_DETERMINED, and no raw-only assay result is promoted.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-PUBCHEM-PREP
  - R244-ASSAY-PLAN
  - R244-ASSAY-SUMMARY
- check_id: S244-C-LOCAL
  name: local
  status: passed
  required: true
  summary: The complete actual owner and seven source sets match the pinned preparation
    and successful intake. This establishes source fidelity, not the truth of every
    imported assertion.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-GUARDS
- check_id: S244-C-DEFINITION-SCOPE
  name: definition scope
  status: failed
  required: true
  summary: The unqualified direct-RNAP statement exceeds the inspected primary mechanism
    evidence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-HOLO01-ABSTRACT
  - S244-E-HOLO01-005
  - S244-E-HOLO01-006
  - S244-E-HOLO01-007
- check_id: S244-C-YERSINIA-METHODS
  name: yersinia methods
  status: unavailable
  required: true
  summary: The full original article remains required to close applicability of the
    complete imported Yersinia method combination; positive native evidence is retained.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-HOLO-META
  - S244-E-HOLO13-INDEXED
  - S244-E-LIMITS
- check_id: S244-C-OCCURRENCE-SCOPE
  name: occurrence scope
  status: unavailable
  required: true
  summary: Some written occurrences require unavailable full original bodies or an
    unresolved exact species bridge; the individual ledger preserves positive evidence
    without inferring absence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-HOLO-META
  - S244-E-HOLO14-REVIEW
  - S244-E-HOLO17-NJ4
  - S244-E-OCC-LEDGER
- check_id: S244-C-NRPS-SCOPE
  name: nrps scope
  status: passed
  required: true
  summary: The existing partial pathway/graph and exact reference protein identity
    are supported.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-HOLO10-002
  - S244-E-HOLO10-003
  - S244-E-PROTEIN-COMPARE
- check_id: C244-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
- check_id: C244-C-LITERAL-SCOPE
  name: Exact literal chemical authority scope
  status: passed
  required: true
  summary: Every asserted literal is accounted for at its measured representation;
    default encoding and fixed-H distinctions remain explicit.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
- check_id: C244-C-PRIMARY-IDENTITY
  name: Original exact compound constitution and depiction
  status: passed
  required: true
  summary: The original closed-disulfide holomycin drawing independently matches the
    complete achiral owner. Exact authority, committed sibling stated InChI and original
    deposited sample agree; invalid external default SMILES are preserved separately.
    Biological target and stock applicability remain independently scoped.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
- check_id: C244-C-ABSOLUTE-SCOPE
  name: Independent experimental stereochemical scope
  status: not_applicable
  required: false
  summary: Achiral exact primary graph; no absolute hand applies.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
evidence:
- evidence_id: R244-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/holomycin.yaml
  locator: Complete actual owner, optional assertions and all history events
  accessed_at: '2026-10-22T03:01:04.125646Z'
  support: supports
  summary: 'Root read the complete post-intake owner: 25 occurrence, 3 producer and
    3 locus assertions. Optional fields: definition, biosynthetic_pathway, causal_graphs,
    bioactivities, bioactivity_summary, related_records, discussions. No external
    component is present.'
  snapshot_sha256: 125f0e310f19582f45f65b82dca90f687fd9463338de592bea14c720e432c3fa
- evidence_id: R244-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/244/local-sources.json
  locator: Complete resolved owner and all six officially captured row sets
  accessed_at: '2026-10-22T03:01:04.125646Z'
  support: context_only
  summary: All six captured sets and the separately compared seventh PubChem set match
    exact frozen preparation. Source fidelity does not establish experimental support.
  snapshot_sha256: 7454333459bad16b076f0a71d30956011ba69163bced4ac2f72ded986e6884c3
- evidence_id: R244-PUBCHEM-PREP
  kind: record_content
  reference: data/raw/pubchem_bioassay.tsv
  locator: All exact-key raw rows, separately compared with the six officially captured
    tables
  accessed_at: '2026-10-22T03:01:04.125646Z'
  support: context_only
  summary: This target has 1 raw rows and 1 written observations. The cohort has 21
    retained assay rows, all written, plus one 245 no-data sentinel. No current-only
    result or absent endpoint is inferred from this inventory.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: R244-Q1144013
  kind: database
  reference: https://www.wikidata.org/wiki/Q1144013
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-Q16993573
  kind: database
  reference: https://www.wikidata.org/wiki/Q16993573
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-Q22285363
  kind: database
  reference: https://www.wikidata.org/wiki/Q22285363
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-Q22286833
  kind: database
  reference: https://www.wikidata.org/wiki/Q22286833
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-Q2355919
  kind: database
  reference: https://www.wikidata.org/wiki/Q2355919
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-Q62851309
  kind: database
  reference: https://www.wikidata.org/wiki/Q62851309
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-Q7623381
  kind: database
  reference: https://www.wikidata.org/wiki/Q7623381
  locator: Retained 16-entity response; relevant English labels/P225/P685 read, not
    an audit of unrelated claims
  accessed_at: '2026-10-22T00:04:15.065016Z'
  support: context_only
  summary: The literal P225/P685 values match the raw organism source. This identifier
    routing is not experimental occurrence evidence.
  snapshot_sha256: 850b5082dd16e39bd9a6e2f3060451eb8bff15ef25421030264357a8bcc09806
- evidence_id: R244-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=1883,1886,1901,1902,1911,1931,7787,9606,10116,28576,29486,52258,57139,67299,77133,140106,173560,265726,272129,312885,330879,331992,355589,455632,527005,665115,746128,1654360,1735992,1873369
  locator: Relevant TaxId, ScientificName, rank, parent and complete OtherNames fields
  accessed_at: '2026-10-22T00:04:15.203485Z'
  support: context_only
  summary: Streptomyces clavuligerus 1901 includes ATCC 27064; Yersinia ruckeri 29486
    and ATCC 29473 strain 527005 remain distinct levels. Photobacterium halotolerans
    265726 and P. galatheae 1654360 are separate current species records. S. flavovirens
    52258 and S. flavogriseus 67299 remain distinct, as do genus 1883 and named species.
    These labels do not resolve the source-specific occurrence or stock applicability
    assessed with primary evidence.
  snapshot_sha256: f42e674c6568acbf7a468ada3670829376a4258dda4d96a06222eaa9ea405298
- evidence_id: R244-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete 20-organism/28-dataset official catalogue
  accessed_at: '2026-10-22T00:04:15.390206Z'
  support: context_only
  summary: The native emitted producers are not exact organism/strain matches in the
    returned 20-organism catalogue. S. albidoflavus J1074 and several S. coelicolor
    strains are present as expression-resource contexts relevant to separate holomycin
    occurrence/engineered-host literature. Their catalogue presence neither establishes
    natural production nor proves a particular introduced strain shares the transcriptome
    experiment. Unnamed S. albus in the hydroxysporine expression paper must not become
    J1074 by assumption. No gene-set membership, expression matrix or causal mechanism
    queried.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: R244-IMOD-META-0
  kind: database
  reference: https://imodulondb.org/api/datasets/s_albidoflavus/modulome/meta
  locator: Complete dataset metadata, including explicit strains
  accessed_at: '2026-10-22T00:11:49.279280Z'
  support: context_only
  summary: S. albidoflavus metadata lists J1074; S. coelicolor metadata lists several
    named strains. These resources do not identify an unnamed introduced host or establish
    native production, stock equality, module membership or expression-linked chemistry.
  snapshot_sha256: f323caa647fdf0eceed4dedbaebb585c2b64f080021bad4071d3388710d45e25
- evidence_id: R244-IMOD-META-1
  kind: database
  reference: https://imodulondb.org/api/datasets/s_coelicolor/modulome478/meta
  locator: Complete dataset metadata, including explicit strains
  accessed_at: '2026-10-22T00:11:50.456841Z'
  support: context_only
  summary: S. albidoflavus metadata lists J1074; S. coelicolor metadata lists several
    named strains. These resources do not identify an unnamed introduced host or establish
    native production, stock equality, module membership or expression-linked chemistry.
  snapshot_sha256: f18e8899518e1117fbfa5c297276e393f6d07a53c331441eeda42c7e88d54185
- evidence_id: R244-ASSAY-PLAN
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/root-authoring/assay-source-plan-v2.json
  locator: 'orders.244.rows: exact written order, full raw-row SHA256, deposited SID/current
    summary tuple and endpoint scope'
  accessed_at: '2026-10-22T00:32:30.380833Z'
  support: context_only
  summary: The plan preserves all 21 written observations across 244/246/248. There
    is no retained raw assay overflow; the separate 245 no-data sentinel is not an
    observation.
  snapshot_sha256: ecb677d1631231a716512ed42bf90d474c33c6bd103c33b2ba89c0fff3f951b8
- evidence_id: R244-ASSAY-ROOT-READ
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/root-assay-source-read-001.json
  locator: All 21 exact retained-row joins and notes; 19 descriptions, 18 complete
    protocols, one high-level description and one metadata-only endpoint
  accessed_at: '2026-10-22T00:07:13.605629Z'
  support: context_only
  summary: Root read the original source endpoints and exact sample/target context.
    AID1347160 was inspected at high-level description scope; AID720532 only at summary
    metadata scope. Neither scope is presented as a complete protocol read.
  snapshot_sha256: b05e2d9d4b783160f8b1aef57ea0287206bd406784d51baf05a3673784565afb
- evidence_id: R244-ASSAY-SUMMARY
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10262683/assaysummary/JSON
  locator: 'Table.Columns/Table.Row: exact current_match tuples in the pinned assay
    plan'
  accessed_at: '2026-10-22T00:03:55.403389Z'
  support: supports
  summary: Exact retained source outcomes and reported numeric endpoints agree with
    current summary tuples. Additional current-only results do not replace retained
    observations. Summary equality is not molecular-target or purity evidence.
  snapshot_sha256: 7aa56ce27e865d5803d6f42ac42bc64d48f30d747aa1a3b1464a891ace1f64dd
- evidence_id: R244-AID-1645860
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1645860/description/JSON
  locator: 'Retained aid-descriptions-02.json: PC_AssayContainer[8].assay.descr; name/description/protocol/comment/target
    fields'
  accessed_at: '2026-10-22T00:03:56.246771Z'
  support: supports
  summary: Purified USP30 ubiquitin-rhodamine cleavage screen; the deposited Active
    call has no emitted potency. Human Q70CQ3 is the source enzyme accession. This
    screen does not establish selectivity, a clinical mechanism or a polymerase target.
  snapshot_sha256: 1cdfc4b9c468ed3b83416e57f6a40a86a41dc25a70637693b3d9bc6d1d37b047
- evidence_id: R244-SAMPLE-GRAPHS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/root-assay-sample-graph-comparison-001.json
  locator: Results for SID441245207,134970445,376241807; Huperzine interpretation
    qualified by SAMPLE-PRECISION
  accessed_at: '2026-10-22T00:05:31.663976Z'
  support: context_only
  summary: The exact deposited holomycin and ilicicolin H sample graphs agree at Standard/fixed-H
    scope. This does not prove vial purity or natural isolation; the original Huperzine
    SDF-only diagnostic is qualified by the later atom/bond and coordinate analysis.
  snapshot_sha256: 9040eaaffee528439eeceac718e4b9499f4be8281f88f3e0bd3c11647a010224
- evidence_id: R244-USP30
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q70CQ3.json
  locator: Reviewed human USP30 accession, organism, sequence length and catalytic
    annotation
  accessed_at: '2026-10-22T00:03:57.055679Z'
  support: context_only
  summary: Q70CQ3 identifies human USP30, 517 amino acids, consistent with the source
    biochemical assay target. This database identity is distinct from sample selectivity
    or clinical mechanism.
  snapshot_sha256: 3f983098af5dff1a5f35d50a211ef929def29362ea613cf1902561d3f3b72cb2
- evidence_id: R244-SIBLING-HOLOMYCIN
  kind: record_content
  reference: https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/holomycin.yaml
  locator: Pinned sibling activity_class and qualified mechanism; exact committed
    source record
  accessed_at: '2026-10-22T00:03:48.133289Z'
  support: context_only
  summary: The pinned sibling supplies ANTIBACTERIAL summary support with a qualified
    transcription mechanism.
  snapshot_sha256: 4979a76d25ee21ce1535f55be56b0735a0aee386ebeece64e3a436496146ae45
- evidence_id: R244-SEEDER
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: classify_activity lines 160–178; PubChem projection/sorting and summary
    lines 1310–1378
  accessed_at: '2026-10-22T00:32:30.380833Z'
  support: context_only
  summary: The current consumer accepts an exact AID/title exception before broad
    patterns, preserves source calls and endpoints, and derives positive summary classes
    from active written observations and sibling sources.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: R244-CLASSIFIER-TESTS
  kind: record_content
  reference: tests/test_seed_skeleton.py
  locator: Classifier, exact AID1650 counterassay, endpoint and derived-summary tests
    around lines 985–1054
  accessed_at: '2026-10-22T00:32:30.380833Z'
  support: context_only
  summary: Existing focused tests provide the consumed regression route for a narrow
    SERCaMP exception and preservation of calls, values, source target context and
    unrelated classifications.
  snapshot_sha256: 72ec216fb0ed365b09f1cfb64fb06c701c50b5d7c2df409d8dbf613d302803bf
- evidence_id: S244-E-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/244/local-sources.json
  locator: Complete resolved owner and captured rows; exact seven-set equality checked
  accessed_at: '2026-10-22T03:01:59.206235Z'
  support: context_only
  summary: Complete actual owner including any inline graph/pathway, six captured
    source sets and separately compared seventh PubChem set match the prepared complete
    reads.
  snapshot_sha256: 7454333459bad16b076f0a71d30956011ba69163bced4ac2f72ded986e6884c3
- evidence_id: S244-E-CONSUMERS
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: LOTUS exclusion, producer/locus emission, method overrides and correction
    order
  accessed_at: '2026-10-22T03:01:59.206235Z'
  support: context_only
  summary: Static inspection covers exact LOTUS exclusions, source method grading
    and producer/reference qualification order. Exact consumers have their own evidence
    snapshots.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S244-E-SCHEMA
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: ProducerEvidenceBasisEnum and ClusterLinkEvidenceEnum; conf/producer_evidence.tsv
    and grading.py also read and pinned
  accessed_at: '2026-10-22T03:01:59.206235Z'
  support: context_only
  summary: Producer tiers concern evidence in the named organism; cloned-locus experiments
    are a distinct cluster question. Empty methods and a source assertion do not independently
    assert native knockout or exact pure-enzyme proof.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: S244-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/244/science-search.json
  locator: Exact read scope
  accessed_at: '2026-10-22T03:01:59.217349Z'
  support: context_only
  summary: Exact current curated-decision search is retained. Its scope is the curation
    tree; it does not establish absence of experimental evidence or all possible consumers.
  snapshot_sha256: 244ba5f8cd853278c6793ba02efe46dd5e2d98b6a3eb7c2226231e2cb436f2b0
  search_scope: rg --no-ignore --hidden -n -F over curation using exact identifier,
    label, full key and source accessions
- evidence_id: S244-E-DEFINITION-CONSUMER
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: CURATOR_OWNED_CARRIED_FIELDS; carry_curator_owned_fields; unique ChEBI
    definition assignment
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: A unique ChEBI definition is imported on seeding; arbitrary edited definitions
    are not among carried curator fields. Inline graphs and curator-prefixed discussions
    have distinct preservation rules.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S244-E-GRADE-MAP
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/conf/producer_evidence.tsv
  locator: Complete method-to-producer/cluster table and native-versus-host rationale
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: The source vocabulary separately grades native producer and cluster claims;
    pure-enzyme evidence and introduced-host expression do not independently establish
    a native producer.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: S244-E-GUARDS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/provisional-science-241-245/source-row-guards.json
  locator: All ten future target owner pins and complete raw-row guards
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: Exact prepared owners and all seven raw sets, including full parsed rows
    and SHA256 guards. This is provenance, not independent biology.
  snapshot_sha256: 8f1dbcade934cdadc2e5529f13d1f458bc25ac7b5ee57583ed0d945251955474
- evidence_id: S244-E-HOLO-CLAV
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/CM000913.1
  locator: ATCC27064 source and SCLAV5271 native CDS within literal 6204480..6222797
    window
  accessed_at: '2026-10-22T00:08:06.520506Z'
  support: supports
  summary: 'Deposited-source/locus annotation bridge only; primary experimental applicability
    is evaluated separately. Read scope: Source/features read; exact named reference
    protein sequences compared where stated. No cloning-boundary or experimental-plasmid
    identity inferred.'
  snapshot_sha256: 2974b6c205c25d011f9f4ad99d15128457b4ba2342e381f91e18eb56f4b37568
- evidence_id: S244-E-HOLO-META
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: MED result IDs and their title/abstract fields, not the unrelated CBA result
    also numbered 468729
  accessed_at: '2026-10-22T00:03:16.785580Z'
  support: partial
  summary: 'Original abstracts provide claim-specific positive occurrences for several
    native/mutant stocks. Abstracts without exact holomycin occurrence are access-limited,
    not negative evidence. Read scope: All 23 MED metadata results read; full-body
    availability differs by article and is recorded below. PMID863793 has no abstract.'
  snapshot_sha256: c4add1b0c4a656715dd79eeed5f1a8b4059e209c14ce9045ae42b3a931931f80
- evidence_id: S244-E-HOLO-PHOTO
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/JMIB01000043.1
  locator: S2753 source, annotated features and explicit 2015 reclassification comment
    in literal 78725..91151 window
  accessed_at: '2026-10-22T00:08:08.259324Z'
  support: supports
  summary: 'Deposited-source/locus annotation bridge only; primary experimental applicability
    is evaluated separately. Read scope: Source/features read; exact named reference
    protein sequences compared where stated. No cloning-boundary or experimental-plasmid
    identity inferred.'
  snapshot_sha256: 61f52c239792b9e31cb664303752cdd99f9ab87dfbf432da42bca3ab07d69b4a
- evidence_id: S244-E-HOLO-SIBLING
  kind: record_content
  reference: https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/holomycin.yaml
  locator: 'Pinned committed holomycin sibling: definition, mechanism evidence, class
    and structure'
  accessed_at: '2026-10-22T00:03:48.133289Z'
  support: supports
  summary: 'The antibacterial class and same-structure relationship are relevant;
    the sibling mechanism explicitly distinguishes cellular transcription effects
    from weak purified RNAP inhibition and unresolved direct target. Its imported
    definition is not independent mechanistic proof. Read scope: Complete exact retained
    sibling owner read, including imported definition and curator mechanism caveat.'
  snapshot_sha256: 4979a76d25ee21ce1535f55be56b0735a0aee386ebeece64e3a436496146ae45
- evidence_id: S244-E-HOLO-YER
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/ACCC01000028.1
  locator: ATCC29473 source and annotated features in literal 3593..21565 window
  accessed_at: '2026-10-22T00:07:21.998734Z'
  support: supports
  summary: 'Deposited-source/locus annotation bridge only; primary experimental applicability
    is evaluated separately. Read scope: Source/features read; exact named reference
    protein sequences compared where stated. No cloning-boundary or experimental-plasmid
    identity inferred.'
  snapshot_sha256: 09586a4a0a43db20930ac62182fdac1e3394a4161f7bfd77358cb12a0423c437
- evidence_id: S244-E-HOLO01-005
  kind: primary_source
  reference: DOI:10.1128/AAC.45.2.532-539.2001
  locator: original lines approximately 80–450; publisher-provided ResearchGate transcription
  accessed_at: '2026-10-22T00:07:44Z'
  support: supports
  summary: 'The cellular RNA-synthesis phenotype is positive. The two purified-enzyme
    formats showed weak inhibition; the paper leaves the direct molecular target unresolved.
    This does not establish a selective direct RNAP mechanism. Read scope: Overlapping
    retained captures jointly cover the complete scientific body; no original PDF
    pixels were inspected. Capture time is a tool-response capture, not an invented
    direct HTTP receipt.'
  snapshot_sha256: 28467f2534dafcdc0ef8d04ab9c0dbeb068613ab7fbf5639b85eff0da39babfb
- evidence_id: S244-E-HOLO01-006
  kind: primary_source
  reference: DOI:10.1128/AAC.45.2.532-539.2001
  locator: original lines approximately 400–800; publisher-provided ResearchGate transcription
  accessed_at: '2026-10-22T00:07:44Z'
  support: supports
  summary: 'The cellular RNA-synthesis phenotype is positive. The two purified-enzyme
    formats showed weak inhibition; the paper leaves the direct molecular target unresolved.
    This does not establish a selective direct RNAP mechanism. Read scope: Overlapping
    retained captures jointly cover the complete scientific body; no original PDF
    pixels were inspected. Capture time is a tool-response capture, not an invented
    direct HTTP receipt.'
  snapshot_sha256: 98499cf5c768a5baf970101303e598f9651455cf7e3adc6520dfb0dc374d3800
- evidence_id: S244-E-HOLO01-007
  kind: primary_source
  reference: DOI:10.1128/AAC.45.2.532-539.2001
  locator: original lines approximately 760–1180, through Discussion; publisher-provided
    ResearchGate transcription
  accessed_at: '2026-10-22T00:07:44Z'
  support: supports
  summary: 'The cellular RNA-synthesis phenotype is positive. The two purified-enzyme
    formats showed weak inhibition; the paper leaves the direct molecular target unresolved.
    This does not establish a selective direct RNAP mechanism. Read scope: Overlapping
    retained captures jointly cover the complete scientific body; no original PDF
    pixels were inspected. Capture time is a tool-response capture, not an invented
    direct HTTP receipt.'
  snapshot_sha256: c0e847a90dfb1e70729a341d299d3d949b5247177f226a90b52e4199c1589fbb
- evidence_id: S244-E-HOLO01-ABSTRACT
  kind: primary_source
  reference: PMID:11158751
  locator: Original PubMed abstract for the 2001 mode-of-action study
  accessed_at: '2026-10-22T00:05:46.943975Z'
  support: supports
  summary: 'Whole-cell transcription effects and weak purified RNA-polymerase inhibition
    must be distinguished. Read scope: Complete original abstract read.'
  snapshot_sha256: 1e1a29037bd153954fc39fa1ade821518fdc74d112e7b94f0085a82bac9adb3d
- evidence_id: S244-E-HOLO10-002
  kind: primary_source
  reference: DOI:10.1073/pnas.1014140107
  locator: Results and biosynthetic NRPS experiments in the original PNAS full-text
    capture
  accessed_at: '2026-10-22T00:06:26Z'
  support: supports
  summary: 'Native ORF3488/3489 deletion affects holomycin; purified ORF3488 activates
    and tethers L-Cys. These are distinct endpoints, and the partial owner graph does
    not claim complete product reconstitution. Read scope: Combined captures cover
    the complete scientific body. Original SI routes failed and are not represented
    as inspected.'
  snapshot_sha256: 6ae82643e7da1253cd42afed6ce1de63b928678ed2100fc2e31519ab6c504a8d
- evidence_id: S244-E-HOLO10-003
  kind: primary_source
  reference: DOI:10.1073/pnas.1014140107
  locator: continuation through Methods and references in the original PNAS full-text
    capture
  accessed_at: '2026-10-22T00:06:26Z'
  support: supports
  summary: 'Native ORF3488/3489 deletion affects holomycin; purified ORF3488 activates
    and tethers L-Cys. These are distinct endpoints, and the partial owner graph does
    not claim complete product reconstitution. Read scope: Combined captures cover
    the complete scientific body. Original SI routes failed and are not represented
    as inspected.'
  snapshot_sha256: 57af59817c039d44a889b655f09f05184e8dc1a05bd389bb336b713176765406
- evidence_id: S244-E-HOLO11-HLMI
  kind: primary_source
  reference: PMID:21504228
  locator: 'Article PMC3101288 only: complete scientific body and native profile/late
    oxidase experiments'
  accessed_at: '2026-10-22T00:05:46.691573Z'
  support: supports
  summary: 'Native holomycin and HlmI late oxidative chemistry are positive. Reduced
    production after deletion is not complete absence; no direct RNAP target follows.
    Read scope: Complete scientific body read, distinct from other articles within
    the same XML.'
  snapshot_sha256: aee5bc9b27cff18715db14ca64bf39c4941ca75fe6648947d17f5c9ab5265392
- evidence_id: S244-E-HOLO11-MARINE
  kind: primary_source
  reference: PMID:21339958
  locator: Original sections 2.1–2.3 and 3.6, S2753 identification and compound characterization
  accessed_at: '2026-10-22T00:05:17.037379Z'
  support: supports
  summary: 'Exact S2753 was then named P. halotolerans and yielded characterized holomycin.
    Current deposited sequence explicitly records its later reclassification to P.
    galatheae. Read scope: Targeted scientific sections read, not a complete re-audit
    of every marine isolate.'
  snapshot_sha256: 77e3375695527764c091de942d444cbfbc04e45274c514ed870bbd040ef8ae4e
- evidence_id: S244-E-HOLO12-ADAPT
  kind: primary_source
  reference: PMID:22470465
  locator: Adaptive-study strain Methods, exact holomycin Results and Figure 3/4 captions
  accessed_at: '2026-10-22T00:05:18.614014Z'
  support: supports
  summary: 'ATCC27064-derived clavu7 gives an authentic-standard LC-MS/MS holomycin
    endpoint. Parent non-detection is limited to tested conditions. The evolved derivative
    is not unmodified wild type, and plasmid loss alone is not proved causal. Read
    scope: Targeted original body and independent peer read, no complete figure-pixel
    audit.'
  snapshot_sha256: 8ba52ff46d2be1a08031cccc404f603e20a0deab90a51486e1878ca78552ea80
- evidence_id: S244-E-HOLO12-METHYL
  kind: primary_source
  reference: PMID:23097183
  locator: 'Article PMC3573328 only: native profiles and Discussion of self-protection'
  accessed_at: '2026-10-22T00:05:46.543739Z'
  support: supports
  summary: 'Holomycin occurs in the compared native backgrounds; methylated shunts
    and suggested self-protection mechanisms must not be substituted for the named
    product or a resolved direct target. Read scope: Scientific body read in segments,
    including the final Discussion in this freeze turn; caption scope preserved. No
    new independent spectral assignment.'
  snapshot_sha256: 7846731bcfdc94a0cc899e785ca28fe9879b1aacac4db678ea9d50f5b84bc8b0
- evidence_id: S244-E-HOLO13-INDEXED
  kind: primary_source
  reference: PMID:23572522
  locator: Indexed original PMC3663494/JBC article excerpts; native ATCC29473 and
    Hom12 resistance passages
  accessed_at: '2026-10-22T00:16:15Z'
  support: partial
  summary: 'Exact native Y. ruckeri holomycin and hom6 deletion are positive. Hom12
    expression in E. coli is a resistance experiment and is not itself whole-cluster
    holomycin production. Imported heterologous-method applicability remains incompletely
    resolved. Read scope: Search/indexed excerpts only, supported by original abstract.
    Full scientific body remains unavailable; persistence time is later than the actual
    inspection.'
  snapshot_sha256: ddf762aee1f868105ca4f4ac9fa88bfe90f74b53dc2ce264c41e99af883186ec
- evidence_id: S244-E-HOLO14-REVIEW
  kind: primary_source
  reference: DOI:10.1007/s10295-013-1348-5
  locator: Original review opening and Table 1, holomycin introduced-host entries;
    continuation failure retained separately
  accessed_at: '2026-10-22T00:12:49Z'
  support: partial
  summary: 'S. coelicolor introduced-host occurrence is supported at secondary-source
    scope. The S. albidoflavus triple is not resolved by the inspected portion; no
    native stock inference is made. Read scope: Partial secondary review only; not
    a complete absence search across the paper.'
  snapshot_sha256: 323233745cf4e60a8abb9e17f4ad7bbd57b4bffb3ad56ddfecfed119834f5348
- evidence_id: S244-E-HOLO17-NJ4
  kind: primary_source
  reference: PMID:28740758
  locator: Complete retained scientific text; NJ-4 identity and purified holomycin
    characterization; all XML text-node exact-name search
  accessed_at: '2026-10-22T00:05:16.578351Z'
  support: supports
  summary: 'Positive source organism is S. flavogriseus NJ-4. S. flavovirens is absent
    from the retained XML text; the asserted flavovirens triple has no established
    bridge in this inspection. Its applicability remains a targeted question rather
    than a global absence claim. Read scope: Original body read plus independent complete-text
    peer. No new phylogram-pixel or external taxonomic-synonym adjudication.'
  snapshot_sha256: 530c0b335b5e41afc9f842623589c0edc04dba523087a19c5ae4b6be11c7ae04
- evidence_id: S244-E-HOLO21
  kind: primary_source
  reference: PMID:33771780
  locator: Original PMC8208159 capture through line 244/Table 3; remaining routes
    include explicit CAPTCHA failures
  accessed_at: '2026-10-22T00:06:16Z'
  support: partial
  summary: 'S2753 native holomycin loss after hlmE deletion is supported; complementation/activity
    and biofilm endpoints remain distinguished from exact chemical rescue. Read scope:
    Partial scientific body plus original abstract; not complete remaining Methods.'
  snapshot_sha256: b156aef7d7edcf05fbb41f7e0ec084e42dc8fcb468c6d37bd9be18179cee91ed
- evidence_id: S244-E-LIMITS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/bgc-science/source-notes.json
  locator: All five record narratives and bounded access limitations
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: Source-specific read/access limits remain explicit. Available sources do
    not establish the unavailable original bodies or experimental allele/construct
    identities.
  snapshot_sha256: 4e26918963414b324715407e27811fefaf4ad33a028988620197994fded547ca
- evidence_id: S244-E-MIBIG0373.5
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000373.5
  locator: Exact versioned source, selected compound name/index, source organism/accession
    and imported evidence methods
  accessed_at: '2026-10-22T00:03:25.512709Z'
  support: context_only
  summary: Current versioned annotation matches the retained source concept; its evidence
    labels are interpreted against the original study, not treated as new independent
    experiments.
  snapshot_sha256: 3803185a053d60f32e823cb6f4d2ce58255c68677c888b2f4c0625f536a0c9c8
- evidence_id: S244-E-MIBIG2091.3
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002091.3
  locator: Exact versioned source, selected compound name/index, source organism/accession
    and imported evidence methods
  accessed_at: '2026-10-22T00:03:25.953834Z'
  support: context_only
  summary: Current versioned annotation matches the retained source concept; its evidence
    labels are interpreted against the original study, not treated as new independent
    experiments.
  snapshot_sha256: ca3072551e397bc07ce4fee5f8c230857a6073a92e1bdc88c8793b5507e6025d
- evidence_id: S244-E-MIBIG2412.2
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002412.2
  locator: Exact versioned source, selected compound name/index, source organism/accession
    and imported evidence methods
  accessed_at: '2026-10-22T00:03:26.016562Z'
  support: context_only
  summary: Current versioned annotation matches the retained source concept; its evidence
    labels are interpreted against the original study, not treated as new independent
    experiments.
  snapshot_sha256: 4b05deda813dc1500cfbdc69611a9cd30a003bffd80695e3e2beb05ab46aa201
- evidence_id: S244-E-OCC-LEDGER
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/bgc-science/occurrence-ledger.json
  locator: Per-record occurrences[0..n], complete raw joins and raw-only Holomycin
    row
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: All31 written occurrence assertions have exact raw joins and source-specific
    scopes; Holomycin has one additional raw-only row.
  snapshot_sha256: a198b21d732eb06aae5459e73e3e63864ee31b04fe9f038617884ba6f9735568
- evidence_id: S244-E-PROTEIN-COMPARE
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/bgc-science/native-protein-comparison-001.json
  locator: All nine result rows and exact input pins
  accessed_at: '2026-10-22T00:12:29.860005Z'
  support: supports
  summary: 'Eight A1163 Has references and S. clavuligerus ORF3488 match current UniProt,
    GenPept, native annotated translation and independently translated genomic CDS.
    Experimental alleles and functional results are separate. Read scope: Locally
    computed four-way sequence identity, with independent static peer; no repeated
    experimental validation.'
  snapshot_sha256: 746503278cc0e0d82e22887b40dfdf52d80dcab459cb386f7a48b1a89e560877
- evidence_id: S244-E-ROUTING
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/bgc-science/curator-routing.json
  locator: Six exact source/consumer routes and their limitations
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: Current consumed correction routes and missing contracts are distinguished.
    No code change, graph migration or exclusion has been made.
  snapshot_sha256: c8bc40a499f66e1cb8b2e254928a269c824dd806789560a0e39fed7f523881d6
- evidence_id: S244-E-SEED-TESTS
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/tests/test_seed_skeleton.py
  locator: Curator carry, structure-identity guards and producer-strain tests inspected
    statically
  accessed_at: '2026-10-22T00:23:55.054144Z'
  support: context_only
  summary: Existing tests show same-key curator-graph/discussion carry, producer-only
    strain overlays and composition rejection. A new definition override needs dedicated
    tests.
  snapshot_sha256: 72ec216fb0ed365b09f1cfb64fb06c701c50b5d7c2df409d8dbf613d302803bf
- evidence_id: S244-E-UP-E2PZ83
  kind: database
  reference: https://www.uniprot.org/uniprotkb/E2PZ83
  locator: Organism, entry status, sequence, cited function annotations and cross-references
    for the exact accession
  accessed_at: '2026-10-22T00:05:22.450667Z'
  support: supports
  summary: Current exact reference-protein annotation and sequence; experimental allele
    identity and functional proof are separately scoped.
  snapshot_sha256: 6aebe7fa43d6126179c54fcc0e405f0ecfe14bb5bfcea79b0def251eaaa4327b
- evidence_id: C244-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/holomycin.yaml
  locator: Complete owner and all seven matching source-row sets; no referenced components
  accessed_at: '2026-10-22T03:02:14.975869Z'
  support: supports
  summary: 'The complete owner denotes holomycin under CHEBI:156451. All source selectors,
    versions and complete row digests are retained in COMPARISON: [{"row_sha256":
    "fde7b9b561a09c61a248c0e20c2efd0194ecbd32a6deb38450b94b22476edf7e", "selector":
    "BGC0000373:1", "version": "5"}, {"row_sha256": "193f8de32399c315b744143438adc0649d15eb957764e546d670818db151e5f0",
    "selector": "BGC0002091:1", "version": "3"}, {"row_sha256": "d51b289d49587ca8c8f2ab0e1ff1b348535c3c5f4fe21cdc6f59c9a82cbcbadf",
    "selector": "BGC0002412:1", "version": "2"}]. The official intake and prepared
    owner bytes agree.'
  snapshot_sha256: 125f0e310f19582f45f65b82dca90f687fd9463338de592bea14c720e432c3fa
- evidence_id: C244-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/244/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-22T02:59:36.509798Z'
  support: supports
  summary: The stored SMILES recomputes to HBUNPJGMNVQSBX-UHFFFAOYSA-N, formula C7H6N2O2S2,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: 0842a45d3a5a74cbe93290381cf23792b68cc38dbbbfdb78458d73c492fc8ce8
- evidence_id: C244-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/retained-graph-comparison.json
  locator: Record 244; exact source rows and each graph comparison
  accessed_at: '2026-10-22T00:03:35.761213Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner and complete raw rows; current authority responses and primary
    proof are separate evidence.
  snapshot_sha256: 1bdbd73a6830fda1bff44fe2d224a534863957c6975ec2efe5ec98224f3abc08
- evidence_id: C244-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/244/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-22T03:02:15.373500Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: 911bc801847bf904a89a1c528abe01d9a3023d34526502fb46646d05af940476
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C244-AUTHORITY-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/authority-graph-comparison.json
  locator: Complete literal Standard/fixed-H, formula, charge and stereo comparison;
    exact source payload pins retained
  accessed_at: '2026-10-22T00:09:32.933883Z'
  support: supports
  summary: Current authority graphs and source-specific serialization differences
    are independently compared. Database agreement is not primary natural-hand proof.
  snapshot_sha256: c2ede72eae1251e2e4e9be67e3ae94f1eee48d2e1b4a1663704c46f8d41407c2
- evidence_id: C244-AUTHORITY-DETAIL
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/source-plan-002.json
  locator: Complete literal Standard/fixed-H, formula, charge and stereo comparison;
    exact source payload pins retained
  accessed_at: '2026-10-22T00:30:08.893968Z'
  support: supports
  summary: Current authority graphs and source-specific serialization differences
    are independently compared. Database agreement is not primary natural-hand proof.
  snapshot_sha256: 8fd13fb10d1d68762b1f21043bd4b43cdcde6db1a234d45af4dd6dd6776fde46
- evidence_id: C244-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000373.5/annotations.json
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/BGC0000373.5.json
  accessed_at: '2026-10-22T00:03:25.512709Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: 3803185a053d60f32e823cb6f4d2ce58255c68677c888b2f4c0625f536a0c9c8
- evidence_id: C244-AUTH-2
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002091.3/annotations.json
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/BGC0002091.3.json
  accessed_at: '2026-10-22T00:03:25.953834Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: ca3072551e397bc07ce4fee5f8c230857a6073a92e1bdc88c8793b5507e6025d
- evidence_id: C244-AUTH-3
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002412.2/annotations.json
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/BGC0002412.2.json
  accessed_at: '2026-10-22T00:03:26.016562Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: 4b05deda813dc1500cfbdc69611a9cd30a003bffd80695e3e2beb05ab46aa201
- evidence_id: C244-AUTH-4
  kind: authority
  reference: https://www.npatlas.org/api/v1/compound/NPA013565
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/NPA013565.json
  accessed_at: '2026-10-22T00:03:47.695580Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: a89f9d39487158ceb454331b54e967c7320d77f9f85362ba4271601e2050a430
- evidence_id: C244-AUTH-5
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10262683/SDF
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/pubchem-10262683.sdf
  accessed_at: '2026-10-22T00:03:28.525045Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: f1bbc23e034a35d23933b793dc4fa352dd75a01764a83e3ce803a32ec97496e0
- evidence_id: C244-AUTH-6
  kind: authority
  reference: https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL476226.json
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/CHEMBL476226.json
  accessed_at: '2026-10-22T00:03:48.501334Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: 22bf855b45d6e02f396cdf8e803fb008b4d2ed345ef558ac7756f0d7ef5dc7e9
- evidence_id: C244-AUTH-7
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/156451/
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/public-reads/CHEBI156451.json
  accessed_at: '2026-10-22T00:03:28.198837Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: f645c8dea8e780f5e92a3f81cfa96ad651fa1e8c0c314c2989dcd2cd2f5027eb
- evidence_id: C244-AUTH-8
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/156451/
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/CHEBI156451.mol
  accessed_at: '2026-10-22T00:03:46.737541Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: 60c5b04e2a0fd7591e36cc893e1b724a6c4b2f503967d44af2cd62a986826aa5
- evidence_id: C244-AUTH-9
  kind: authority
  reference: https://raw.githubusercontent.com/CultureBotAI/AntibioticMech/74f6cc8362498900f2fe2c13d0b6fdb66dd30976/data/antibiotics/antibacterial/holomycin.yaml
  locator: Complete retained payload /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase002-public-reads/sibling-holomycin.yaml
  accessed_at: '2026-10-22T00:03:48.133289Z'
  support: supports
  summary: Exact source representation at its recorded access time; primary identity
    and natural hand are assessed separately.
  snapshot_sha256: 4979a76d25ee21ce1535f55be56b0735a0aee386ebeece64e3a436496146ae45
- evidence_id: C244-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=HBUNPJGMNVQSBX-UHFFFAOYSA-N&size=100
  locator: Complete bounded key/name response /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase003-public-reads/chebi-key-244.json
  accessed_at: '2026-10-22T00:04:11.971444Z'
  support: supports
  summary: HTTP200; exact source response and candidate eligibility preserved.
  snapshot_sha256: 16f2bd39ffa8ed0d25fa2c4070aa2fd586c635851eab000f93af883e14d96aef
  search_scope: Official ChEBI exact literal key/name request, size100; complete returned
    payload. No global absence inference.
- evidence_id: C244-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=holomycin&size=100
  locator: Complete bounded key/name response /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase003-public-reads/chebi-name-244.json
  accessed_at: '2026-10-22T00:04:16.048205Z'
  support: supports
  summary: HTTP200; exact source response and candidate eligibility preserved.
  snapshot_sha256: e44bf840a8da7e754528b23edfccb3443b01311f943ee6ca112fc4209fbf93e1
  search_scope: Official ChEBI exact literal key/name request, size100; complete returned
    payload. No global absence inference.
- evidence_id: C244-HOLO11-HLMI
  kind: primary_source
  reference: PMID:21504228
  locator: 'Article PMC3101288 only: introduction and holomycin/reduced-holomycin
    characterization paragraph; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/bgc-science/public-003-retry/primary-recovery-a.xml'
  accessed_at: '2026-10-22T00:05:46.691573Z'
  support: supports
  summary: The closed-disulfide product and reduced dithiol are distinct; direct RNAP
    target remains qualified.
  snapshot_sha256: aee5bc9b27cff18715db14ca64bf39c4941ca75fe6648947d17f5c9ab5265392
- evidence_id: C244-PRIMARY-FIGURE
  kind: primary_source
  reference: PMID:21504228
  locator: Original Figure1A R=CH3 and Figure1B holomycin1; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/phase011-public-reads/holomycin2011-fig1.jpg
  accessed_at: '2026-10-22T00:23:23.624118Z'
  support: supports
  summary: Complete achiral N-acetyl dithiolopyrrolone graph, distinct from reduced2.
  snapshot_sha256: 6fbac64cf665a5b03cc9377bb1eca430e5033519a4f93ab0b2baf77581fced4a
- evidence_id: C244-SOURCE-LIMITS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/source-notes.json
  locator: 'Entry244: observations/limitations, exact source rows, authority/primary
    pins; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/source-notes.json'
  accessed_at: '2026-10-22T00:26:09.962872Z'
  support: supports
  summary: Source-specific precision and access limits; not an authority vote.
  snapshot_sha256: d794062c51c6c321b1747173ab9705e3b758a2014faf37e39e07e13f55ad13c2
- evidence_id: C244-PRIMARY-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/primary-mapping-001/holomycin-primary-comparison-001.json
  locator: 'Exact record244: independent source graph, input pins, model and roundtrip;
    retained snapshot /private/tmp/npm-review-work/shared-next-batch025/chemistry-prep/primary-mapping-001/holomycin-primary-comparison-001.json'
  accessed_at: '2026-10-22T00:24:08.898837Z'
  support: supports
  summary: Literal source/model diagnostic with explicit limits; no replacement selected.
  snapshot_sha256: e82e2c869cf4c4fa4aab958c326b2c96abbd84762505fa50cedc8ff543f12c54
- evidence_id: C244-SAMPLE-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch025/root-assay-sample-graph-comparison-001.json
  locator: Original deposited SDF results for order244; retained snapshot /private/tmp/npm-review-work/shared-next-batch025/root-assay-sample-graph-comparison-001.json
  accessed_at: '2026-10-22T00:05:31.663976Z'
  support: supports
  summary: Pinned root deposited-graph comparison; not purity or experimental endpoint
    proof.
  snapshot_sha256: 9040eaaffee528439eeceac718e4b9499f4be8281f88f3e0bd3c11647a010224
assessments:
- assessment_id: R244-HISTORY
  area: provenance
  topic: Native status and complete audit history
  outcome: supported
  summary: All 4 events retain the exact sequence ['SEEDED_FROM_SOURCES', 'SEEDED_FROM_SOURCES',
    'RECORD_CURATED', 'SEEDED_FROM_SOURCES']. Native status is SEEDED. RECORD_CURATED
    and CURATED_BIOSYNTHESIS_GRAPH events describe prior edits; they are not scientific
    review passes or a substitute for claim-level assessment.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
- assessment_id: R244-OPTIONAL
  area: completeness
  topic: Present optional claims
  outcome: supported
  summary: 'Present optional fields: definition, biosynthetic_pathway, causal_graphs,
    bioactivities, bioactivity_summary, related_records, discussions. The definition,
    one pathway step, four-node/four-edge graph, discussion, sibling link, antibacterial
    summary and one USP30 observation are all present. Biosynthetic and polymerase-mechanism
    claims are assessed separately; the USP30 assay and summary provenance are assessed
    here.'
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-LOCAL
  - R244-PUBCHEM-PREP
- assessment_id: R244-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The exact-key NPClassifier projection/version npclassifier.gnps2.org@2026-09-07
    reproduces filing, superclass/class and glycoside value false. These computed
    labels are not independent natural-origin or mechanism evidence. Any accepted
    new identity requires effective-key reclassification.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-LOCAL
- assessment_id: R244-TAXON-SCOPE
  area: provenance
  topic: Taxonomic names versus experimental stocks
  outcome: supported
  summary: Streptomyces clavuligerus 1901 includes ATCC 27064; Yersinia ruckeri 29486
    and ATCC 29473 strain 527005 remain distinct levels. Photobacterium halotolerans
    265726 and P. galatheae 1654360 are separate current species records. S. flavovirens
    52258 and S. flavogriseus 67299 remain distinct, as do genus 1883 and named species.
    These labels do not resolve the source-specific occurrence or stock applicability
    assessed with primary evidence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-TAXON-CONTEXT
  - R244-OWNER
  - R244-Q1144013
  - R244-Q16993573
  - R244-Q22285363
  - R244-Q22286833
  - R244-Q2355919
  - R244-Q62851309
  - R244-Q7623381
- assessment_id: R244-ORGANISM-IDS
  area: grounding
  topic: Literal organism identifier routing
  outcome: supported
  summary: This record's literal organism routes match the retained P225 names and
    P685 taxon identifiers. No taxonomic match establishes chemical occurrence, stock
    equivalence or a source-method endpoint.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-Q1144013
  - R244-Q16993573
  - R244-Q22285363
  - R244-Q22286833
  - R244-Q2355919
  - R244-Q62851309
  - R244-Q7623381
  - R244-TAXON-CONTEXT
  - R244-OWNER
- assessment_id: R244-IMODULON-SCOPE
  area: completeness
  topic: Native producer transcriptomic applicability
  outcome: not_applicable
  summary: The native emitted producers are not exact organism/strain matches in the
    returned 20-organism catalogue. S. albidoflavus J1074 and several S. coelicolor
    strains are present as expression-resource contexts relevant to separate holomycin
    occurrence/engineered-host literature. Their catalogue presence neither establishes
    natural production nor proves a particular introduced strain shares the transcriptome
    experiment. Unnamed S. albus in the hydroxysporine expression paper must not become
    J1074 by assumption. No gene-set membership, expression matrix or causal mechanism
    queried.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-IMODULON
  - R244-IMOD-META-0
  - R244-IMOD-META-1
- assessment_id: R244-ASSAY-INVENTORY
  area: scope
  topic: Exact raw and written assay inventory
  outcome: supported
  summary: This record has 1 raw rows, 1 written observations and 0 no-data sentinel.
    There is no retained raw-only assay overflow in this cohort. Inventory equality
    alone does not establish endpoint interpretation or deposited sample identity.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-PUBCHEM-PREP
  - R244-LOCAL
- assessment_id: R244-ASSAY-00
  area: scope
  topic: bioactivities[0] AID1645860 endpoint and deposited outcome
  outcome: supported
  summary: Purified USP30 ubiquitin-rhodamine cleavage screen; the deposited Active
    call has no emitted potency. Human Q70CQ3 is the source enzyme accession. This
    screen does not establish selectivity, a clinical mechanism or a polymerase target.
    No numeric endpoint is emitted; no potency is inferred. Preserve source outcome
    Active and deposited SID441245207.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-LOCAL
  - R244-PUBCHEM-PREP
  - R244-ASSAY-PLAN
  - R244-ASSAY-ROOT-READ
  - R244-ASSAY-SUMMARY
  - R244-AID-1645860
  - R244-USP30
- assessment_id: R244-ASSAY-SUMMARY-SCOPE
  area: evidence
  topic: bioactivity_summary and related_records
  outcome: supported
  summary: ANTIBACTERIAL is supplied by the pinned sibling; the USP30 screen is an
    independent biochemical observation. Neither supplies an unqualified DNA-dependent
    RNA polymerase mechanism. The definition and sibling identity are assessed separately.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - R244-OWNER
  - R244-SIBLING-HOLOMYCIN
  - R244-AID-1645860
  - R244-SEEDER
- assessment_id: S244-A-ORIGIN
  area: scope
  topic: biosynthesis_origin; producer_organisms
  outcome: supported
  summary: Named native holomycin evidence is positive for the three source organisms
    within their inspected stock scopes. S2753 has an explicit deposited reclassification
    bridge from historical P. halotolerans to P. galatheae. The conservative S. clavuligerus
    SOURCE_ASSERTION grade remains faithful even though primary native genetic evidence
    is now available.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO-META
  - S244-E-HOLO13-INDEXED
  - S244-E-HOLO21
  - S244-E-HOLO11-MARINE
  - S244-E-HOLO-PHOTO
  - S244-E-HOLO10-002
  - S244-E-GRADE-MAP
- assessment_id: S244-A-YERSINIA-BGC
  area: evidence
  topic: biosynthetic_gene_clusters[0]
  outcome: unknown
  summary: Native ATCC29473 product and hom6-deletion evidence are positive in the
    abstract/indexed source. The full original body remains unavailable for the complete
    imported method combination. Hom12 expression in E. coli is resistance evidence,
    not proof of whole-cluster holomycin formation. Preserve the positive native result
    while keeping exact heterologous applicability unresolved.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO-META
  - S244-E-HOLO13-INDEXED
  - S244-E-HOLO-YER
  - S244-E-MIBIG2091.3
- assessment_id: S244-A-PHOTO-BGC
  area: evidence
  topic: biosynthetic_gene_clusters[1]
  outcome: supported
  summary: The inspected native S2753 results support holomycin loss after hlmE deletion.
    Activity/biofilm complementation is not silently relabeled as exact chemical rescue;
    remaining full Methods were unavailable. Deposited source naming explicitly bridges
    the historical species label.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO21
  - S244-E-HOLO-META
  - S244-E-HOLO-PHOTO
  - S244-E-MIBIG2412.2
- assessment_id: S244-A-CLAV-BGC
  area: evidence
  topic: biosynthetic_gene_clusters[2]
  outcome: supported
  summary: The original native product and genetic experiments support the named locus.
    Empty imported methods and conservative grades remain source-faithful; adding
    the newly inspected genetic evidence is optional enrichment rather than mandatory
    promotion.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO10-002
  - S244-E-HOLO10-003
  - S244-E-HOLO-CLAV
  - S244-E-MIBIG0373.5
  - S244-E-GRADE-MAP
- assessment_id: S244-A-DEFINITION
  area: evidence
  topic: definition
  outcome: concern
  summary: The direct RNA-polymerase-inhibitor definition is stronger than the inspected
    primary mechanism evidence. Whole-cell RNA-synthesis effects are positive, but
    purified RNAP inhibition is weak and the direct molecular target remains unresolved.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO01-ABSTRACT
  - S244-E-HOLO01-005
  - S244-E-HOLO01-006
  - S244-E-HOLO01-007
- assessment_id: S244-A-NRPS-STEP
  area: evidence
  topic: biosynthetic_pathway[0]
  outcome: supported
  summary: The step correctly distinguishes native ORF3488 requirement from purified
    L-Cys activation/tethering and stops before final holomycin formation. Current
    exact protein identity is independently grounded.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO10-002
  - S244-E-HOLO10-003
  - S244-E-PROTEIN-COMPARE
  - S244-E-UP-E2PZ83
  - S244-E-HOLO-CLAV
- assessment_id: S244-A-NRPS-GRAPH
  area: evidence
  topic: causal_graphs[0]
  outcome: supported
  summary: All four edges remain at L-Cys activation and enzyme tethering. The product
    node is an NRPS-bound intermediate, not free holomycin; no complete in-vitro biosynthesis
    or reaction-order assertion is introduced.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO10-002
  - S244-E-HOLO10-003
  - S244-E-PROTEIN-COMPARE
- assessment_id: S244-A-SIBLING
  area: evidence
  topic: related_records[0]; bioactivity_summary
  outcome: supported
  summary: The exact pinned sibling is relevant to the antibacterial summary and same-structure
    linkage. Its mechanism explicitly qualifies weak purified RNAP inhibition and
    unresolved direct target. Its imported definition is not independent mechanistic
    proof; deposited sample chemistry and written assay endpoints are assessed separately.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO-SIBLING
  - S244-E-HOLO01-005
  - S244-E-HOLO01-006
  - S244-E-HOLO01-007
- assessment_id: S244-A-DISCUSSION
  area: completeness
  topic: discussions[0]
  outcome: supported
  summary: The shared-structure question concerns three source concepts. Primary native
    scopes and current literal graphs are considered separately; no source occurrence
    is transferred solely because the full Standard key is shared.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO-META
  - S244-E-HOLO10-002
  - S244-E-MIBIG0373.5
  - S244-E-MIBIG2091.3
  - S244-E-MIBIG2412.2
- assessment_id: S244-A-OCC0
  area: evidence
  topic: occurrences[0]
  outcome: supported
  summary: PMID32642829 supports the exact NRRL B-24137 source after the reported
    induction; not an unqualified baseline-production claim.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC1
  area: evidence
  topic: occurrences[1]
  outcome: unknown
  summary: PMID863793/1977 exact title is retained but no abstract/full body; genus
    source assertion remains unclosed at detailed primary scope.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC2
  area: evidence
  topic: occurrences[2]
  outcome: unknown
  summary: The literal review is only partly inspected; no exact holomycin/S. albidoflavus
    bridge is established. Do not infer absence from a partial review.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO14-REVIEW
- assessment_id: S244-A-OCC3
  area: evidence
  topic: occurrences[3]
  outcome: supported
  summary: Review Table 1 names S. coelicolor expression hosts; PMID23147422 abstract
    independently reports introduced-host production. This is occurrence, not native
    production.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO14-REVIEW
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC4
  area: evidence
  topic: occurrences[4]
  outcome: supported
  summary: PMID28627048 identifies isolated holomycin from Streptomyces sp. DT-A37;
    no transfer of activity from other derivatives.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC5
  area: evidence
  topic: occurrences[5]
  outcome: supported
  summary: Original S2753 identification is positive. JMIB deposited comment explicitly
    links historical P. halotolerans to later P. galatheae; preserve original source
    naming.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO11-MARINE
  - S244-E-HOLO-PHOTO
- assessment_id: S244-A-OCC6
  area: evidence
  topic: occurrences[6]
  outcome: supported
  summary: Original abstract/indexed passages identify native ATCC29473 holomycin.
    Full-body access remains incomplete.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO13-INDEXED
- assessment_id: S244-A-OCC7
  area: evidence
  topic: occurrences[7]
  outcome: unknown
  summary: Exact positive producer is S. flavogriseus NJ-4; no flavovirens name occurs
    in the complete retained XML text. Unread phylogram labels and external synonym
    possibilities are not adjudicated; do not yet claim a proved biological absence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO17-NJ4
- assessment_id: S244-A-OCC8
  area: evidence
  topic: occurrences[8]
  outcome: supported
  summary: S. flavogriseus NJ-4 purified holomycin is positive; condition-specific
    yields/other antibiotics stay distinct.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO17-NJ4
- assessment_id: S244-A-OCC9
  area: evidence
  topic: occurrences[9]
  outcome: supported
  summary: Same exact NJ-4 primary as the LOTUS species row, not an independent publication.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO17-NJ4
- assessment_id: S244-A-OCC10
  area: evidence
  topic: occurrences[10]
  outcome: supported
  summary: Native-background profiles include holomycin; shunt intermediates and methylated
    derivatives remain separate.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO12-METHYL
- assessment_id: S244-A-OCC11
  area: evidence
  topic: occurrences[11]
  outcome: unknown
  summary: PMID23361841 abstract discusses cephamycin regulation without an exact
    holomycin endpoint; full body is required before accepting or excluding this occurrence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC12
  area: evidence
  topic: occurrences[12]
  outcome: supported
  summary: PMID24323287 is a review with named S. clavuligerus holomycin; not an independent
    primary production experiment.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC13
  area: evidence
  topic: occurrences[13]
  outcome: supported
  summary: PMID23147422 supports native overproducer endpoints and separately a heterologous
    S. coelicolor result; keep these experimental units distinct.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC14
  area: evidence
  topic: occurrences[14]
  outcome: supported
  summary: The native purified product/profile and late enzyme study support occurrence;
    the HlmI assay is a distinct biochemical endpoint.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO11-HLMI
- assessment_id: S244-A-OCC15
  area: evidence
  topic: occurrences[15]
  outcome: supported
  summary: Full primary shows native product and genetic perturbation, independently
    of the partial NRPS enzyme endpoint.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO10-002
- assessment_id: S244-A-OCC16
  area: evidence
  topic: occurrences[16]
  outcome: unknown
  summary: PMID15819635 abstract does not state exact holomycin occurrence; this is
    a remaining source-applicability gap, not a confirmed false triple.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC17
  area: evidence
  topic: occurrences[17]
  outcome: supported
  summary: PMID26187955 abstract supports the native-species ΔclaR derivative; do
    not describe an unmodified wild-type readout.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC18
  area: evidence
  topic: occurrences[18]
  outcome: supported
  summary: PMID30194098 abstract supports the source-specific oppA2 mutant expression/metabolite
    context.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC19
  area: evidence
  topic: occurrences[19]
  outcome: supported
  summary: PMID22344669 abstract supports NP1/argR-mutant context; preserve the named
    experimental stocks.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC20
  area: evidence
  topic: occurrences[20]
  outcome: unknown
  summary: PMID20889745 is a genome report; its abstract lacks an exact holomycin
    measurement. A genome/title alone does not independently close occurrence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC21
  area: evidence
  topic: occurrences[21]
  outcome: supported
  summary: PMID12426344 reports holomycin identification in native-species mutants;
    the claim is not a general unmodified-strain measurement.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: S244-A-OCC22
  area: evidence
  topic: occurrences[22]
  outcome: supported
  summary: Exact clavu7/standard comparison is positive. Tested parent non-detection
    is not global incapacity, and plasmid-loss causality is not established.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO12-ADAPT
- assessment_id: S244-A-OCC23
  area: evidence
  topic: occurrences[23]
  outcome: supported
  summary: Same PMID21041678 primary as the LOTUS PNAS row; source-provider duplication
    is not publication independence.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO10-002
- assessment_id: S244-A-OCC24
  area: evidence
  topic: occurrences[24]
  outcome: supported
  summary: MED PMID468729 identifies MM21801 as holomycin from S. clavuligerus; unrelated
    CBA identifier collision is excluded.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-OCC-LEDGER
  - S244-E-HOLO-META
- assessment_id: C244-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0000373:1 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0000373:1
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C244-OWNER
  - name: complete_raw_row_sha256
    value: fde7b9b561a09c61a248c0e20c2efd0194ecbd32a6deb38450b94b22476edf7e
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C244-OWNER
- assessment_id: C244-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: Exactly one committed three-star default ChEBI row matches; its current
    graph is checked separately.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-OWNER
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-LOCAL-SEARCH
  - C244-CHEBI-SEARCH-1
  - C244-CHEBI-SEARCH-2
- assessment_id: C244-A-XREF
  area: representation
  topic: Exact literal chemical identifier scope
  outcome: supported
  summary: 'Measured exact-literal comparisons: [{"comparison": {"same_charge": true,
    "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi":
    true, "same_stereo_removed_standard": true}, "identifier": "npatlas:NPA013565",
    "scope": "Exact returned representation"}, {"comparison": {"same_charge": true,
    "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi":
    true, "same_stereo_removed_standard": true}, "identifier": "pubchem:10262683",
    "scope": "Exact returned representation"}, {"comparison": {"same_charge": true,
    "same_fixed_h": true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi":
    true, "same_stereo_removed_standard": true}, "identifier": "chembl:CHEMBL476226",
    "scope": "Exact returned representation"}]. Standard identity, fixed-H tautomerism,
    explicit stereo and coordinate-derived depiction are separate. No more specific
    authority graph is automatically adopted.'
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
- assessment_id: C244-A-ELIGIBILITY
  area: grounding
  topic: ChEBI full-key eligibility and serialization
  outcome: supported
  summary: '[{"eligible": true, "id": 156451, "literal_default_comparison": null,
    "literal_default_parse": false, "mol_comparison": {"same_charge": true, "same_fixed_h":
    true, "same_formula": true, "same_full_standard_key": true, "same_standard_inchi":
    true, "same_stereo_removed_standard": true}, "name": "holomycin", "stars": 3}].
    CHEBI156451 is the unique exact three-star committed projection. Official MOL/stated
    InChI match; literal default SMILES is invalid and is not copied.'
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
  - C244-CHEBI-SEARCH-1
  - C244-CHEBI-SEARCH-2
- assessment_id: C244-A-SIBLING
  area: representation
  topic: Exact committed sibling structure scope
  outcome: supported
  summary: The exact external committed sibling stated InChI/full key agrees; its
    literal SMILES fails parsing and is preserved without repair. SAME_STRUCTURE is
    supported at stated-InChI scope, not by copying the invalid string or treating
    imported definitions as independent experiments.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
- assessment_id: C244-A-SAMPLES
  area: representation
  topic: Exact original deposited sample structure
  outcome: supported
  summary: The pinned root original-SDF comparison reports full Standard/fixed-H agreement
    for SID441245207. This is deposited-graph support only; sample purity, original
    natural isolation and endpoint mechanism remain separately scoped.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
- assessment_id: C244-A-PRIMARY-SCOPE
  area: scope
  topic: Primary identity and experimental precision
  outcome: supported
  summary: The original closed-disulfide holomycin drawing independently matches the
    complete achiral owner. Exact authority, committed sibling stated InChI and original
    deposited sample agree; invalid external default SMILES are preserved separately.
    Biological target and stock applicability remain independently scoped.
  target_ids:
  - CHEBI:156451
  evidence_ids:
  - C244-HOLO11-HLMI
  - C244-PRIMARY-FIGURE
  - C244-SOURCE-LIMITS
  - C244-PRIMARY-COMPARISON
  - C244-SAMPLE-COMPARISON
  - C244-OWNER
  - C244-GRAPH
  - C244-COMPARISON
  - C244-AUTHORITY-COMPARISON
  - C244-AUTHORITY-DETAIL
  - C244-AUTH-1
  - C244-AUTH-2
  - C244-AUTH-3
  - C244-AUTH-4
  - C244-AUTH-5
  - C244-AUTH-6
  - C244-AUTH-7
  - C244-AUTH-8
  - C244-AUTH-9
findings:
- finding_id: S244-F-RNAP-DEFINITION
  issue_key: holomycin-direct-rnap-definition-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The definition overstates direct RNA polymerase inhibition
  description: The imported definition presents holomycin as a DNA-dependent RNA polymerase
    inhibitor. The inspected original study supports a whole-cell transcription phenotype
    but reports weak effects in two purified RNAP assay formats and leaves the direct
    molecular target unresolved. Preserve the antibacterial/transcription phenotype
    while qualifying this direct-enzyme assertion.
  target_ids:
  - CHEBI:156451
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - S244-E-LOCAL
  - S244-E-HOLO01-ABSTRACT
  - S244-E-HOLO01-005
  - S244-E-HOLO01-006
  - S244-E-HOLO01-007
  - S244-E-HOLO-SIBLING
  - S244-E-GUARDS
  - S244-E-DEFINITION-CONSUMER
  - S244-E-SEED-TESTS
  - S244-E-ROUTING
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: definition import and future guarded qualification consumer
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_seed_skeleton.py
    role: durability and stale-source regression coverage
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/holomycin.yaml
    role: maintained structural definition and evidence-qualified prose
actions:
- action_id: S244-ACT-RNAP-DEFINITION
  finding_ids:
  - S244-F-RNAP-DEFINITION
  target_ids:
  - CHEBI:156451
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: definition import and future guarded qualification consumer
  - repository: CultureBotAI/NaturalProductMech
    path: tests/test_seed_skeleton.py
    role: durability and stale-source regression coverage
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/holomycin.yaml
    role: maintained structural definition and evidence-qualified prose
  description: Implement a consumed definition qualification or replacement, guarded
    by CHEBI:156451, the owner identifier/full key, the exact old definition and the
    complete source row SHA256 aa6610aa2163fa65a24b58de5f5ca7de2a4f49e314742defee505203150525ba.
    Retain structural identity and source attribution; describe cellular transcription
    effects with the direct molecular target unresolved. A curator discussion alone
    is not a repair because current reseeding reimports the definition. Do not overwrite
    the raw inventory or substitute an unverified alternative target.
  acceptance_checks:
  - 'The exact guarded raw ChEBI row remains unchanged: {"chebi_id":"CHEBI:156451","definition":"A
    dithiolopyrrolone antibiotic that is 4,5-dihydro[1,2]dithiolo[4,3-b]pyrrole in
    which the hydrogens at positions 5 and 6 have been replaced by oxo and acetamido
    groups, respectively. It is an inhibitor of DNA-dependent RNA polymerase, and
    exhibits antibacterial and antitumour properties.","name":"holomycin","smiles":"CC(=O)Nc1c2sscc-2nc1=O","standard_inchi_key":"HBUNPJGMNVQSBX-UHFFFAOYSA-N","stars":"3"}'
  - A focused test rejects changed source row, identifier, key or old definition;
    unrelated ChEBI-derived definitions are unchanged.
  - A reseed reproduces the qualified definition and preserves the existing ORF3488
    pathway, causal graph, evidence and all independent assay observations.
  - Primary PMID11158751 is attached directly to the qualification; weak purified
    RNAP inhibition and cellular transcription inhibition remain distinct.
limitations:
- The PubChem audit preserves exact deposited calls and endpoint scope. Across the
  cohort, 18 complete protocols and one additional high-level biochemical description
  were read; one pathogen-related assay remains metadata-only. No vial-specific purity,
  clinical efficacy or direct binding is inferred. Current CID precision and BindingDB
  molecular-target/graph assessments remain separate.
- Context covers exact owner/history, seven source inventories, literal organism routing
  and computed classification. Present definitions, graphs, pathways, sibling links
  and molecular-target claims retain their separate scientific and chemical assessments.
  Taxonomic agreement does not prove stock equivalence or occurrence. Homoanatoxin-a
  context is high-level identity and provenance only.
- Several occurrence bodies and the complete Yersinia original remain unavailable;
  lack of a product name in an abstract is not negative evidence.
- The flavovirens and albidoflavus occurrence bridges remain unresolved; no blanket
  taxon exclusion is selected.
- The actual assay protocols/classifier assessment is independently supplied by the
  root assay section; no assay finding is duplicated here.
- Current E2PZ83/native CDS agreement is a reference identity bridge, not a reconstruction
  of tags or historical plasmids.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
- Deposited graph agreement is not vial purity, direct-target or exact historical-stock
  proof. External SMILES parse failure is retained, not silently repaired.
- The first fresh QC attempt failed during the public vendored-sync fetch after lint
  passed. Only the separately recorded complete successful QC retry002 is used as
  the baseline check; the actual failed001 receipt/log/capture/root observation remain
  bound.
- Reproduction retains42 withheld ambiguous producer claims,161 merged-taxon rewrites
  and5 unresolved assay-organism targets.
- 499non-blocking plausibility warnings and4750no-adapter skips remain.
- Four skipped tests and two dependency warnings remain disclosed. Reproduction also
  reports42 withheld ambiguous-producer claims,161 merged-taxon rewrites and5 unresolved
  assay-organism rows. Gate success is configured consistency, not scientific validation
  of every claim.
- 'Clarification of root review-queue observation: actual session80402 terminal0 and
  receipt/hash are confirmed. Combined initial log display was truncated; root read
  its command/output header, displayed samples and final summary, then recovered all12
  queue headers in a bounded projection. Root did not read all8928 per-record queue
  descriptions. No gate outcome changes.'
- Native baseline gates establish configured consistency, not independent biological
  production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions
  and no-adapter pairs; a successful command does not convert these into verified
  scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command
  execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population
  was checked; external caches and generated bytecode are not asserted to be independently
  byte-pinned.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command
  receipts for this base. Scientific failed or unavailable checks are distinct from
  bundle validation.
- Scientific conclusions integrate the chemical, biological and provenance assessments;
  source access and unresolved scopes remain explicit.
tags:
- path-order-campaign
- batch-025
```
