# Azetidomonamide B: retain native support and encode primary E geometry

- Review: 20261021T154343Z-azetidomonamide-b
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T15:23:09.729304Z
- Finished UTC: 2026-10-21T15:43:43.943502Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Primary native-product and locus evidence is supported. The molecular graph omits the independently supported E crotonyl constraint; stereo_complete=true tests tetrahedral centres only. The original Hong ECD/construct supplement remains unavailable, limiting independent review of its details. A guarded structure correction must reconsider exact-key joins without transferring unsupported claims.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 97, batch 010, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 144 of 3116 current records had campaign coverage and 2972 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-269a84b809 | data/natural_products/alkaloids/azetidomonamide-b.yaml | generated | azetidomonamide B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-269a84b809 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-269a84b809 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-269a84b809 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-269a84b809 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-269a84b809 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-269a84b809 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and referenced-component scope | passed | True | naturalproductmech:mibig-269a84b809 | The entire owner and all matching local source rows were read. The resolved view confirms the empty component-reference set; all formal input hashes and fresh intake/strict success receipts agree. |
| Exact native product and locus primary-source support | passed | True | naturalproductmech:mibig-269a84b809 | B has direct native product, insertion-mutant and isolation support in the cited main and official SI. |
| Original Hong construct and ECD supporting-information access | unavailable | True | naturalproductmech:mibig-269a84b809 | Full main is positive; original supplemental construct/ECD details were not recovered. This limits independent verification and is not a negative experimental result. |
| Exact PAO1 accession and interval bridge | passed | True | naturalproductmech:mibig-269a84b809 | Exact source window and all eleven feature boundaries inspected; no unsupported whole-stock or construct equality. |
| Optional later full-main access | unavailable | False | naturalproductmech:mibig-269a84b809 | Official SI is inspected; the full 2022 main was not recovered, so no later enzyme result is silently transferred. |
| Internal exact graph and provenance consistency | passed | True | naturalproductmech:mibig-269a84b809 | SMILES, Standard InChI, key, formula/charge, source concepts and literal current xrefs are consistent at the stored resolution. This check does not independently prove all experimental stereochemistry. |
| Primary E geometry versus stored molecular graph | failed | True | naturalproductmech:mibig-269a84b809 | A potentially stereogenic acyclic crotonyl C=C is unspecified in the stored graph, although primary depiction and trans couplings establish E. The tetrahedral-only stereo_complete calculation does not test this alkene; the confirmed defect is the missing primary-supported graph constraint. |
| Original Hong ECD evidence verification | unavailable | True | naturalproductmech:mibig-269a84b809 | Detailed 4R experimental/computational ECD assessment remains unavailable; this does not weaken the independent confirmed E-geometry discrepancy. |

## Scientific And Domain Assessments

### Native status and retained audit history

provenance: supported. Targets: naturalproductmech:mibig-269a84b809.

The dated seed events and retained SEEDED status document generated provenance. This review adds no native curation event or status promotion.

### Present optional assertions and enrichment limits

completeness: not_applicable. Targets: naturalproductmech:mibig-269a84b809.

The complete owner contains no structured pathway, causal graph, molecular target, bioactivity, clinical status, application, cross-corpus relationship or discussion. Optional enrichment is separate from correcting present claims; compound names and computed classes do not establish a mechanism or activity.

### Computed filing and returned class scope

representation: supported. Targets: naturalproductmech:mibig-269a84b809.

The owner reproduces its exact-key NPClassifier result, including model version npclassifier.gnps2.org@2026-09-07, Alkaloids filing, every superclass/class label (including the empty returned sets where applicable), and false glycoside flag. These remain computed predictions, not experiments proving precursor use, natural origin or stereochemistry. BGC classes retain their separate MIBiG source and biological assessment.

### Matching producer transcriptomic resources

completeness: supported. Targets: naturalproductmech:mibig-269a84b809.

The catalogue contains two P. aeruginosa datasets, making exact PAO1 locus-tag queries appropriate. Their retained query/member-summary outputs and original receipts are assessed in the scientific section. Module membership is expression context and does not establish metabolite production, direct regulator binding, identity of AB16.2 or a recombinant protein construct.

### Literal LOTUS organism-identifier routing

provenance: supported. Targets: naturalproductmech:mibig-269a84b809.

Every literal organism entity in the matching LOTUS rows resolves to its retained taxon and NCBI identifier. The primary-source assessment independently addresses exact compound occurrence, native producer, collection host and experimental strain.

### Natural occurrence and source-specific culture scope

evidence: supported. Targets: naturalproductmech:mibig-269a84b809.

The single Hong species occurrence is supported by B isolation in AB16.2. Independent Patteson isolation directly supports native PAO1 B production under its conditions. No recombinant host is treated as a natural occurrence.

### Exact product, native background and evidence tier

evidence: supported. Targets: naturalproductmech:mibig-269a84b809.

The current Knock-out studies category is supported by native insertion/product experiments, with polarity explicitly unresolved. CLUSTER_DEMONSTRATED and BGC_CHARACTERIZED are compatible at that locus-level scope; they do not claim every encoded protein has a final-product assay.

### Reference locus and source-version meaning

grounding: supported. Targets: naturalproductmech:mibig-269a84b809.

The current MIBiG interval is the exact PAO1 reference window and maps to eleven native features. No complete tagged construct or AB16.2 whole-genome identity is asserted; NRPS is a supported pathway class.

### Bounded additional mechanism and expression evidence

completeness: supported. Targets: naturalproductmech:mibig-269a84b809.

The existing sparse owner has no mandatory optional-mechanism deficit. Later native promoter engineering and expression modules are available context; missing individual enzyme graphs are not findings. Phenotype differences between mutants are not assigned to purified A or B without compound-specific tests.

### Classifier provenance and filing

representation: supported. Targets: naturalproductmech:mibig-269a84b809.

The complete exact-key NPClassifier row reproduces the stored Alkaloids filing and all supplied superclass/class labels; empty finer classifications are preserved. This is model-derived classification, not evidence of biological origin.

### Constitution and 4R identity versus missing E precision

identity: concern. Targets: naturalproductmech:mibig-269a84b809.

All current authority graphs reproduce the less-specified owner and therefore repeat its missing crotonyl geometry. The original Hong drawing and independent Patteson coupling evidence support E. The formula C10H12N2O2, neutral charge and retained 4R centre do not change.

### Ineligible exact authority and migration boundaries

grounding: supported. Targets: naturalproductmech:mibig-269a84b809.

CHEBI:220639 is two-star and carries the same less-specified graph; it is not a repair target or eligible exact grounding. The minted identifier correctly reflects the current source concept. A corrected graph must explicitly re-adjudicate old-key xrefs, occurrence and model-classification joins without asserting equivalence at full stereochemical resolution.

### Reported 4R assignment with inaccessible ECD details

evidence: unknown. Targets: naturalproductmech:mibig-269a84b809.

Hong positively reports 4R, but its original SI is unavailable; Patteson supplies E-geometry evidence without an independent absolute core assignment.

## Findings

### C097-F-E-GEOMETRY: Encode the primary-supported E crotonyl geometry

major / open / confirmed; issue key: azetidomonamide-b-missing-primary-supported-crotonyl-e.

The source-derived graph omits the primary-supported acyclic crotonyl E geometry. Hong Figure 1b and independent Patteson NMR couplings support E; current authority agreement repeats the less-specified source graph. The stored stereo_complete=true flag reflects assigned tetrahedral centres only and is not evidence that alkene geometry was tested or complete.

## Recommended Actions And Acceptance Checks

### C097-A-E-GEOMETRY

Implement and test a primary-derived stereochemical-refinement contract before adding any decision. Guard exact selector BGC0002037:2 version 3, complete original row SHA256 a5658a2f86c6c54360c2f6f043b2aac4d900173ec38f0c01e55d1eed0776b479, old key WNKLVRDIRPADMZ-SSDOTTSWSA-N, old SMILES 'CC=CC(=O)NC1=CC(=O)[C@H]2CCN12', original stereo_complete=true and database_ids=npatlas:NPA032934. The reviewable E/4R representation is C/C=C/C(=O)NC1=CC(=O)[C@H]2CCN12 ; InChI=1S/C10H12N2O2/c1-2-3-10(14)11-9-6-8(13)7-4-5-12(7)9/h2-3,6-7H,4-5H2,1H3,(H,11,14)/b3-2+/t7-/m1/s1 ; WNKLVRDIRPADMZ-TYWZFMJISA-N, formula C10H12N2O2, charge 0. Preserve Hong's reported 4R and its original ECD access limitation; change only the crotonyl geometry, not constitution or ring hand. Confirm a fresh eligible-grounding/collision search before implementation; the currently committed CHEBI projection has no target row and current CHEBI:220639 is ineligible and less specified, so existing REPLACE_WITH_CHEBI is not executable for this candidate. Keep the original MIBiG source row unchanged and source concept identifiable. Re-adjudicate the old-key NPAtlas/Wikidata/PubChem links as less-specified references rather than claiming exact full-graph equivalence. The existing LOTUS triple is old key + NCBITaxon:287 + DOI:10.1002/ANIE.201809981, chemical Q113958881, complete row SHA256 026e6465389f50ee4aa39481c2f98e55097d567f44bed2501973b8bc84537f3b; retain its source provenance and use an explicit reviewed corrected-claim hook if retaining the independently supported named B occurrence at the new key. Do not blindly transfer or silently discard old-key occurrence, classifier, definition or other joins. Current citation/strain consumers reject structure-corrected rows, so compose this refinement with any separately justified biological corrections under original-row pins and transformed-graph verification. Do not edit generated YAML, raw inventories, or create an unconsumed decision placeholder.

- Changed raw source context, row digest, old graph, source version or candidate graph fails closed; no sibling A row changes.
- Output contains E crotonyl geometry and retained 4R, with internally consistent InChI/key and preserved tetrahedral-only completeness semantics; the ECD access limitation remains explicit.
- No false three-star grounding, silent collision, automatic old-key join transfer or claim that less-specified authority graphs are exact corrected stereostructures.
- Biological method/citation/strain repairs compose without bypassing existing guards; exact source provenance and original claims remain auditable.
- Strict target, reproduction, corpus and scientific graph checks pass after implementation; this review performs no regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R097-OWNER | data/natural_products/alkaloids/azetidomonamide-b.yaml; Complete owner, every assertion, inline graph, discussion and history event | supports | Root read the complete azetidomonamide B owner after its individual intake. It contains 1 occurrence, 1 producer and 1 cluster assertions. Referenced components are empty. Present optional fields: none. This scope is based on complete parsed contents, not a filtered search miss. |
| R097-LOCAL-SOURCES | /private/tmp/npm-review-work/097/local-sources.json; Every matching MIBiG, LOTUS, ChEBI, CyanoMetDB and NPClassifier row and complete resolved owner | context_only | Root read every matching source row. The native resolved owner equals the complete parsed raw YAML. Imported assertions and deterministic joins remain distinct from independently inspected primary experiments. |
| R097-IMODULON-DATASETS | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Complete 28-row dataset catalogue; original receipt 010/imodulon-context-receipts.json | context_only | The catalogue was retrieved on 2026-10-21 at 07:21:15 UTC and is reused with that original time. It includes P. aeruginosa precise364/precise411 and S. albidoflavus/S. coelicolor datasets. It has no named Stigmatella, Rhodococcus, Herpetosiphon or S. mirabilis dataset, and no identified NA04227 dataset. Species or genus matching alone does not establish exact stock, gene, locus or metabolite evidence. |
| R097-Q31856 | https://www.wikidata.org/wiki/Special:EntityData/Q31856.json; Exact organism entity, scientific name and P685 NCBI Taxonomy mapping | context_only | Literal entity Q31856 resolves as Pseudomonas aeruginosa, P685 287, matching every associated local LOTUS row. This verifies identifier routing only, not compound occurrence, experimental strain identity or historical taxonomic revisions. |
| S097-E-LOCAL | data/natural_products/alkaloids/azetidomonamide-b.yaml; Complete owner; resolved/components and every matching local source row | supports | Exact B row BGC0002037:2, version 3, raw-row SHA256 a5658a2f86c6c54360c2f6f043b2aac4d900173ec38f0c01e55d1eed0776b479. Producer PAO1 and locus AE004091.2:3729471..3746067 carry Knock-out studies, BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED with PMID 31247735. No inline or referenced mechanism components are present. |
| S097-E-HONG | https://polytechnique.hal.science/hal-02096769/document; Complete scientific main re-read; Figures 1 and 2, isolation, feeding, AzeJ and phenotype paragraphs | supports | The complete scientific main identifies B as compound 2, isolated and structurally characterized from AB16.2, a spontaneous PAO1 derivative selected at 16 mg/L colistin. Both A and B are absent in the PA3327-deficient comparison and after azeJ/PA3335 inactivation; attB::PA3335 complementation restores both at lower abundance. AZC feeding restores B only and suppresses A. Recombinant AzeJ produces the AZC building block, not final A/B; AzeB domain assays measure substrate activation. These native-lineage genetic results support the locus but require the selected-strain context. The main claims 5R A and 4R B by rotation/ECD comparison, whose original detailed SI remains unavailable. |
| S097-E-PATTESON | https://par.nsf.gov/servlets/purl/10162901; Complete main; Figures 1–4 and printed pp. 4955–4958; exact product numbering and polarity qualification | supports | The complete main explicitly identifies azabicyclene 1 as azetidomonamide B; its product 2 is a proline analogue, not A. PAO1 cultures contain B at lower basal levels and more after AHL supplementation. B/C/F/I insertion mutants lose B; D/G/H/J reduce it; E increases it. The authors explicitly cannot exclude insertion polarity. Purified His6-AzeB forms pyridinone intermediates 3/4, not final A or B; 3 has NMR support, 4 HRMS/MS without isolated NMR. No exact A isolation or A-specific genetic endpoint is established by this source. |
| S097-E-PATTESON-SI | https://ndownloader.figshare.com/files/15592466; Official SI S3–S6, S9/Table S2 and Figure S11; original complete-source preparation plus targeted re-read | supports | Official SI S3–S6 specifies PAO1, lacZ insertions in B/C/D/E/F/H/I/J and phoA in G; short-extension PCR verifies the insertion comparison, not whole-stock sequence identity or a nonpolar deletion. Cultures use 6 µM 3-oxo-C12-AHL and 30 µM C4-AHL at 37 °C for 14 h. Native B is purified and NMR-characterized. PAO1 azeB DNA is cloned into pLIC-His for E. coli BL21-Gold(DE3); the isolated enzyme assay stops at intermediates. The G label differs from the main figure, so the explicit Methods are retained. S9/Table S2 B crotonyl couplings 15.3/15.2 Hz support E geometry; the main leaves the ring absolute hand undetermined. |
| S097-E-ERNST-SI | https://ndownloader.figshare.com/files/34875104; Original SI pp. 3–5 and 8, Table S1 p. 35; retained original p. 8 render | supports | Original 2022 SI pp. 3–5, 8 and Table S1 describes PAO1azeind, made by inserting rhaRS/PrhaB 26 bp upstream of PA3327, with PCR/sequencing and azeB RT-qPCR. This is native promoter engineering, separate from AB16.2, insertion-library genotypes and E. coli recombinant-protein hosts. A and B are numbered 3 and 4; original p. 8 gives A crotonyl J 15.3/15.3 Hz and B 15.3/15.4 Hz. The unavailable full main is not used to certify every later enzyme reaction. |
| S097-E-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0002037.3/annotations.json; Complete current annotation; compounds, locus, taxonomy and legacy references | supports | Current version 3 remains active/questionable/completeness unknown. It lists both final compounds under one locus, PAO1 taxon 208964 and both 2019 references. The entry-level ordering does not make the first paper compound-specific proof for A. NRPS classification is compatible with the experimentally studied bimodular AzeB. |
| S097-E-LOCUS | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AE004091.2&amp;seq_start=3729471&amp;seq_stop=3746067&amp;rettype=gbwithparts&amp;retmode=text; Header, source and all 11 CDS feature locations; retained locus-map.json | supports | The exact reference window is 16,597 bp and explicitly PAO1/taxon 208964. It spans PA3326–PA3336; AzeB/PA3327=AAG06715.1, AzeJ/PA3335=AAG06723.1, AzeK/PA3336=AAG06724.1. Hong uses ten genes through PA3335; Patteson includes PA3336. The reference deposit is not an independently sequenced AB16.2 stock, and interval membership does not prove every gene necessary. |
| S097-E-IMODULON | https://imodulondb.org; Structured runner summaries p_aeruginosa/precise364/88 and p_aeruginosa/precise411/59; exact PA3326–PA3336 member rows | context_only | Both components contain the eleven PA locus tags with STRING taxon 208964. precise411/59 additionally contains phzB1/PA4211; its aggregate regulator labels cannot be transferred to the aze genes. These modules supply expression context, not final-product chemistry, AB16.2 stock sequence identity or native necessity. |
| S097-E-ACCESS | https://doi.org/10.1002/anie.201809981; Retained bounded original Hong SI attempts and Ernst full-main attempts | context_only | Hong full main is available, but detailed original SI, ECD parameters and all construct protocols remain unavailable. The 2022 official SI is available, its full main is not. No absence of uninspected experimental results is inferred. |
| S097-E-CONSUMERS | scripts/seed_from_sources.py; Source loading, claim-reference and strain application; full producer_strains.py, claim_references.py and lotus_exclusions.py contracts | supports | The implemented claim-reference and strain tables pin the entire original raw row. Strain qualification changes context only, not taxon or grades. LOTUS exclusions pin the exact key/taxon/DOI and entire triple row. Claim-reference and strain application reject structure_correction_note, requiring tested composition before any chemistry repair. The ignored-inclusive search found no existing matching maintained correction in the searched scope. |
| S097-E-SEARCH | /private/tmp/npm-review-work/097/science-overlay-search.json; Actual rg --no-ignore --hidden search receipt | context_only | Ignored-inclusive exact accession, names and full-key prefixes in all maintained curation tables, scripts and curate consumers; no claim of absence elsewhere. |
| C097-OWNER | /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/azetidomonamide-b.yaml; Complete owner, literal xrefs, definition, source concepts, classification and discussion/history | supports | Owner and resolved packet are identical. Intake chemistry gives WNKLVRDIRPADMZ-SSDOTTSWSA-N, formula C10H12N2O2, charge 0 and centres [[10, 'R']]. The evidence scope here is chemical identity and provenance; biology and causal claims are assessed separately. |
| C097-RAW | /private/tmp/npm-review-work/097/local-sources.json; All matching complete raw MIBiG, ChEBI, LOTUS and classifier rows | supports | All 1 MIBiG rows, 1 LOTUS rows, 0 eligible ChEBI rows and 1 classifier rows were read. Complete parsed row SHA256 values and reproduced source-concept IDs are retained in the per-record comparison. |
| C097-COMPARISON | /private/tmp/npm-review-work/shared-next-batch010/chemistry-first-seven/chemical-comparison.json; azetidomonamide B complete Standard and fixed-H graph comparison | supports | Raw/current BGC0002037.3 compound 2, NPAtlas NPA032934, PubChem 169492153 and two-star CHEBI220639 JSON/MOL all agree at the less-specified key WNKLVRDIRPADMZ-SSDOTTSWSA-N; they assign the ring centre R but leave the acyclic crotonyl double bond unspecified. The missing bond is a potentially stereogenic double bond, not an unconstrained ring bond. |
| C097-AUTH0 | https://mibig.secondarymetabolites.org/repository/BGC0002037.3/annotations.json; current BGC0002037; compounds[1].structure | supports | Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula C10H12N2O2; charge 0; tetrahedral centres [[10, 'R']]. |
| C097-AUTH1 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/WNKLVRDIRPADMZ-SSDOTTSWSA-N/property/InChIKey,InChI,IsomericSMILES,MolecularFormula,Charge/JSON; PubChem 169492153; PropertyTable.Properties[0].SMILES | supports | Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula C10H12N2O2; charge 0; tetrahedral centres [[10, 'R']]. |
| C097-AUTH2 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/220639/; ChEBI JSON CHEBI:220639; default_structure.smiles | supports | Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula C10H12N2O2; charge 0; tetrahedral centres [[10, 'R']]. |
| C097-AUTH3 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/220639/; ChEBI MOL 220639; official MOL | supports | Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula C10H12N2O2; charge 0; tetrahedral centres [[3, 'R']]. |
| C097-GROUNDING-CODE | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; mint_identifier, choose_pathway, grouping and exact-key ChEBI grounding; source_concepts emission | supports | Source-concept identifiers hash source and accession:compound index, not labels or chemical keys. A unique eligible exact-key ChEBI row grounds EXACT; absent eligible rows retain the minted source identifier. Classification is joined by exact key. |
| C097-ELIGIBILITY-CODE | /private/tmp/npm-record-reviews-20261021/scripts/extract_chebi.py; MIN_STARS and extract_compounds status/stars filter | supports | Only the eligible three-star projection enters exact grounding; a currently accessible two-star record is not an asserted eligible authority. |
| C097-WIKIDATA-Q113958881 | https://www.wikidata.org/wiki/Special:EntityData/Q113958881.json; Current P235, P234, P2017 and literal chemical entity identity | supports | Literal LOTUS chemical entity Q113958881 resolves to the stored full key; every retained isomeric SMILES reproduces the same Standard key and fixed-H graph. Canonical stereo-free SMILES is not substituted for the isomeric property. |
| C097-OWNER-COMPARISON | /private/tmp/npm-review-work/097/chemistry-owner-comparison.json; Exact owner/current authority linkage; independently parsed Wikidata and reconstructed source-concept hashes | supports | Recomputed all literal chemical Wikidata isomeric graphs and 1 accession:index source concepts against this owner. Full row pins and ignored-inclusive local search are recorded. |
| C097-PRIMARY | https://polytechnique.hal.science/hal-02096769/document; Hong 2019 complete structural paragraph and original Figure 1b, compound 2 | supports | Hong reports 4R for azetidomonamide B and draws an E crotonyl side chain. The drawing independently transcribes to WNKLVRDIRPADMZ-TYWZFMJISA-N. The owner preserves 4R but omits this acyclic double-bond geometry. Its stereo_complete=true value comes from a tetrahedral-centre-only computation and does not establish alkene geometry. |
| C097-NMR | https://ndownloader.figshare.com/files/15592466; Original SI S5 and S9 Table S2; azabicyclene compound 1 | supports | Patteson compound 1 is azabicyclene/azetidomonamide B, not Hong A compound 1. Its crotonyl olefinic H9/H10 couplings are 15.3 and 15.2 Hz, independently supporting trans/E geometry. The core absolute hand was not assigned in that study, so 4R remains the separate Hong assignment. |
| C097-PRIMARY-GRAPH | /private/tmp/npm-review-work/shared-next-batch010/chemistry-first-seven/primary-transcription.json; azetidomonamide-B-Hong2019 independent atom/bond/wedge transcription | supports | The original graph has the same heavy-atom connectivity, neutral formula and 4R centre as the owner, with the additional E crotonyl bond. This is a stereochemical-resolution difference, not a constitutional isomer, opposite ring hand or tautomer. |
| C097-PIXEL-QA | /private/tmp/npm-review-work/shared-next-batch010/review-support/primary-transcription-qa/independent-primary-transcription-qa.json; Hong B manual CIP, double-bond geometry and original Patteson Table S2 pixels | supports | Independent manual source-pixel QA confirms source C4 R and opposing carbon substituents at the crotonyl bond; original SI coupling values independently corroborate E. |
| C097-ECD-ACCESS | https://onlinelibrary.wiley.com/doi/suppl/10.1002/anie.201809981/supinfo/anie201809981-sup-0001-misc_information.pdf; Original Hong ECD supplementary PDF request | context_only | The original ECD SI remains unavailable. The main positively assigns 4R; original computation details and measured/calculated curves were not inspected. The E-geometry finding does not depend on completing this separate absolute-hand check. |
| C097-CONTRACT | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py; Complete guarded replacement consumer and row_digest | supports | Current actions only REPLACE_WITH_CHEBI or SPLIT_SHARED_WITH_CHEBI and require an exact three-star target row. They withhold old xrefs, retain source history, prevent collisions and do not transfer other exact-key joins. A primary-derived E refinement needs an explicit tested contract extension or a later verified eligible target; ordinary current rows cannot express it. |
| C097-COMPOSITION | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/claim_references.py; load_claim_references and correct_claim_reference; seed_from_sources.py producer-strain application | supports | Citation routing is pinned to the complete original source row and rejects a structure-corrected row. The seeder likewise rejects strain/isolate overlays on such rows. Any scientific method/citation/strain repair must compose through a reviewed tested contract retaining original-row and transformed-graph checks, not by bypassing these guards. |
| C097-REPAIR-SEARCH | /private/tmp/npm-review-work/097/chemistry-repair-search.json; Ignored-inclusive key/selector search and complete committed inventory scans | supports | The original key has one MIBiG owner; the E target key has no current MIBiG or eligible ChEBI row in the committed inventories. Complete original raw and LOTUS row digests, candidate chemistry and search output are preserved. |
| C097-FLAG-SCOPE | /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py; structure_properties lines 165–168; schema ChemicalStructure.stereo_complete lines 392–396 | context_only | The extractor computes stereo_complete by checking Chem.FindMolChiralCenters for undefined tetrahedral centres. It does not call a double-bond geometry check. The schema describes undefined stereocentres; the current boolean is therefore not independent evidence that E/Z is complete. |

## Limits And Additional Notes

- The review assesses current assertions and concrete evidence gaps. It does not claim exhaustive discovery of every later study or require every optional mechanism for review coverage.
- Original Hong ECD/construct SI remains unavailable despite retained bounded routes; the positive main-body results remain usable at their explicit scope.
- The 2022 full main is unavailable; inspected SI is not a substitute for every main-body enzyme result.
- The PAO1 accession is a reference-sequence bridge, not an independent genome comparison of AB16.2, every insertion stock or a recombinant fusion.
- Chemistry/xref assessments are delivered separately; no optional pathway completion is required by this packet.
- The confirmed defect is omission of supported alkene geometry, not a demonstrated wrong 4R assignment. Original Hong ECD SI is unavailable, and the suggested E/4R graph remains a reviewable source-based correction rather than an adopted corpus change. No claim of global absence of a later exact authority record is made.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35 explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). Skipped tests are not counted as passing tests. Existing ontology caches were used; no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy, or literature-level claim support.
- The five reused gates retain their batch004 execution times and cached ontology results. Reuse establishes unchanged repository inputs; it is not a new remote authority query or new assertion of ontology freshness.
- The ignored-inclusive check enumerates record and saved-review YAML paths, and all tracked files are hashed. Generated Python bytecode and external tool caches are not claimed to have been independently byte-pinned at the prior execution.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification; target strict validation ran afresh. Scientific failed or unavailable checks are distinct from bundle validation.

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
review_id: 20261021T154343Z-azetidomonamide-b
title: 'Azetidomonamide B: retain native support and encode primary E geometry'
started_at: '2026-10-21T15:23:09.729304Z'
finished_at: '2026-10-21T15:43:43.943502Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: Primary native-product and locus evidence is supported. The molecular graph
  omits the independently supported E crotonyl constraint; stereo_complete=true tests
  tetrahedral centres only. The original Hong ECD/construct supplement remains unavailable,
  limiting independent review of its details. A guarded structure correction must
  reconsider exact-key joins without transferring unsupported claims.
source:
  git_revision: 1c2402097718c138b081e00943de8f04de0541cd
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
  - path: data/natural_products/alkaloids/azetidomonamide-b.yaml
    sha256: c6913bf58487afd9d835fb15af2a5315e873fc7e990b211a5aaef35bd05b6fa0
    role: target
  - path: data/raw/MANIFEST.yaml
    sha256: b81dab34775c79c323f30e05093cfab97fca02556816ef978ed2b24f3a4695a3
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
  - path: src/naturalproductmech/grading.py
    sha256: ece54c4a2c0803f034ac59de51b1006cf79ea8d6b6256d75757d4adb88ea9630
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 97, batch 010, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 144 of 3116 current
    records had campaign coverage and 2972 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-269a84b809
targets:
- target_id: naturalproductmech:mibig-269a84b809
  path: data/natural_products/alkaloids/azetidomonamide-b.yaml
  label: azetidomonamide B
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
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  command: just validate-strict data/natural_products/alkaloids/azetidomonamide-b.yaml
    --out /private/tmp/npm-review-work/097/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T15:23:11.255179Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 current record files agree with PATHS.tsv and their pinned filing
    pathways.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055340+00:00;
    finished 2026-10-21T09:55:22.727768+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-corpus.log. Reused
    for batch010 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch010. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-269a84b809
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 current records passed the documented byte-reproduction gate
    against committed inventories and maintained curation inputs.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055361+00:00;
    finished 2026-10-21T09:56:44.050706+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-reproduction.log.
    Reused for batch010 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch010. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-269a84b809
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The exhaustive review queue produced 8,928 diagnostic rows across 12 queues;
    this deterministic output does not establish scientific review.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just review-queue --tsv /private/tmp/npm-review-queue-batch-004.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.057401+00:00;
    finished 2026-10-21T09:54:38.468783+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-004/review-queue.log. Reused
    for batch010 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch010. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-269a84b809
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'The configured identifier-label gate passed using the existing ontology
    caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions,
    499 warning-only mismatches and 4,744 pairs skipped because their prefixes have
    no adapter.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.061733+00:00;
    finished 2026-10-21T09:56:36.296159+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-004/validate-products.log. Reused
    for batch010 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch010. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-269a84b809
- check_id: shared-qc
  name: Full repository quality gate on the current main baseline
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed on the unchanged main baseline
    during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
    All configured lint, governance, documentation, provenance, source-queue, schema,
    rendering, reproduction, filing-integrity and reporting stages completed successfully.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=1c2402097718c138b081e00943de8f04de0541cd
    just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Original read-only batch-004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:30.560925+00:00;
    finished 2026-10-21T10:04:44.806799+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch010
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch010.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - naturalproductmech:mibig-269a84b809
- check_id: R097-FULL-OWNER
  name: Complete owner and referenced-component scope
  status: passed
  required: true
  summary: The entire owner and all matching local source rows were read. The resolved
    view confirms the empty component-reference set; all formal input hashes and fresh
    intake/strict success receipts agree.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - R097-OWNER
  - R097-LOCAL-SOURCES
- check_id: S097-C-PRIMARY
  name: Exact native product and locus primary-source support
  status: passed
  required: true
  summary: B has direct native product, insertion-mutant and isolation support in
    the cited main and official SI.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-HONG
  - S097-E-PATTESON
  - S097-E-PATTESON-SI
- check_id: S097-C-HONG-SI
  name: Original Hong construct and ECD supporting-information access
  status: unavailable
  required: true
  summary: Full main is positive; original supplemental construct/ECD details were
    not recovered. This limits independent verification and is not a negative experimental
    result.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-ACCESS
  - S097-E-HONG
- check_id: S097-C-LOCUS
  name: Exact PAO1 accession and interval bridge
  status: passed
  required: true
  summary: Exact source window and all eleven feature boundaries inspected; no unsupported
    whole-stock or construct equality.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-LOCUS
  - S097-E-MIBIG
- check_id: S097-C-2022
  name: Optional later full-main access
  status: unavailable
  required: false
  summary: Official SI is inspected; the full 2022 main was not recovered, so no later
    enzyme result is silently transferred.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-ERNST-SI
  - S097-E-ACCESS
- check_id: C097-INTERNAL
  name: Internal exact graph and provenance consistency
  status: passed
  required: true
  summary: SMILES, Standard InChI, key, formula/charge, source concepts and literal
    current xrefs are consistent at the stored resolution. This check does not independently
    prove all experimental stereochemistry.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-OWNER
  - C097-RAW
  - C097-COMPARISON
  - C097-OWNER-COMPARISON
  - C097-AUTH0
  - C097-AUTH1
  - C097-AUTH2
  - C097-AUTH3
- check_id: C097-GEOMETRY
  name: Primary E geometry versus stored molecular graph
  status: failed
  required: true
  summary: A potentially stereogenic acyclic crotonyl C=C is unspecified in the stored
    graph, although primary depiction and trans couplings establish E. The tetrahedral-only
    stereo_complete calculation does not test this alkene; the confirmed defect is
    the missing primary-supported graph constraint.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-OWNER
  - C097-PRIMARY
  - C097-NMR
  - C097-PRIMARY-GRAPH
  - C097-PIXEL-QA
  - C097-FLAG-SCOPE
- check_id: C097-ABSOLUTE-METHOD
  name: Original Hong ECD evidence verification
  status: unavailable
  required: true
  summary: Detailed 4R experimental/computational ECD assessment remains unavailable;
    this does not weaken the independent confirmed E-geometry discrepancy.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-PRIMARY
  - C097-ECD-ACCESS
evidence:
- evidence_id: R097-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/azetidomonamide-b.yaml
  locator: Complete owner, every assertion, inline graph, discussion and history event
  accessed_at: '2026-10-21T15:24:59.730317Z'
  support: supports
  summary: 'Root read the complete azetidomonamide B owner after its individual intake.
    It contains 1 occurrence, 1 producer and 1 cluster assertions. Referenced components
    are empty. Present optional fields: none. This scope is based on complete parsed
    contents, not a filtered search miss.'
  snapshot_sha256: c6913bf58487afd9d835fb15af2a5315e873fc7e990b211a5aaef35bd05b6fa0
- evidence_id: R097-LOCAL-SOURCES
  kind: record_content
  reference: /private/tmp/npm-review-work/097/local-sources.json
  locator: Every matching MIBiG, LOTUS, ChEBI, CyanoMetDB and NPClassifier row and
    complete resolved owner
  accessed_at: '2026-10-21T15:24:59.730317Z'
  support: context_only
  summary: Root read every matching source row. The native resolved owner equals the
    complete parsed raw YAML. Imported assertions and deterministic joins remain distinct
    from independently inspected primary experiments.
  snapshot_sha256: 697f9ac294153def038048c3940ab95823770588199492bb01250e03f2d1400e
- evidence_id: R097-IMODULON-DATASETS
  kind: database
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Complete 28-row dataset catalogue; original receipt 010/imodulon-context-receipts.json
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The catalogue was retrieved on 2026-10-21 at 07:21:15 UTC and is reused
    with that original time. It includes P. aeruginosa precise364/precise411 and S.
    albidoflavus/S. coelicolor datasets. It has no named Stigmatella, Rhodococcus,
    Herpetosiphon or S. mirabilis dataset, and no identified NA04227 dataset. Species
    or genus matching alone does not establish exact stock, gene, locus or metabolite
    evidence.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: R097-Q31856
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q31856.json
  locator: Exact organism entity, scientific name and P685 NCBI Taxonomy mapping
  accessed_at: '2026-10-21T15:06:30.095702Z'
  support: context_only
  summary: Literal entity Q31856 resolves as Pseudomonas aeruginosa, P685 287, matching
    every associated local LOTUS row. This verifies identifier routing only, not compound
    occurrence, experimental strain identity or historical taxonomic revisions.
  snapshot_sha256: b69ab9ff8da6d2c792ff586cfd3ea808c4d65392011b49db7a7b3e8a0ad801dc
- evidence_id: S097-E-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/azetidomonamide-b.yaml
  locator: Complete owner; resolved/components and every matching local source row
  accessed_at: '2026-10-21T15:29:03.003709Z'
  support: supports
  summary: Exact B row BGC0002037:2, version 3, raw-row SHA256 a5658a2f86c6c54360c2f6f043b2aac4d900173ec38f0c01e55d1eed0776b479.
    Producer PAO1 and locus AE004091.2:3729471..3746067 carry Knock-out studies, BGC_CHARACTERIZED
    and CLUSTER_DEMONSTRATED with PMID 31247735. No inline or referenced mechanism
    components are present.
  snapshot_sha256: c6913bf58487afd9d835fb15af2a5315e873fc7e990b211a5aaef35bd05b6fa0
- evidence_id: S097-E-HONG
  kind: primary_source
  reference: https://polytechnique.hal.science/hal-02096769/document
  locator: Complete scientific main re-read; Figures 1 and 2, isolation, feeding,
    AzeJ and phenotype paragraphs
  accessed_at: '2026-10-21T14:45:41.096540Z'
  support: supports
  summary: The complete scientific main identifies B as compound 2, isolated and structurally
    characterized from AB16.2, a spontaneous PAO1 derivative selected at 16 mg/L colistin.
    Both A and B are absent in the PA3327-deficient comparison and after azeJ/PA3335
    inactivation; attB::PA3335 complementation restores both at lower abundance. AZC
    feeding restores B only and suppresses A. Recombinant AzeJ produces the AZC building
    block, not final A/B; AzeB domain assays measure substrate activation. These native-lineage
    genetic results support the locus but require the selected-strain context. The
    main claims 5R A and 4R B by rotation/ECD comparison, whose original detailed
    SI remains unavailable.
  snapshot_sha256: 0b5119850fd70aa51ffda9c29130d52253ceb4815a06530978fd53031680959e
- evidence_id: S097-E-PATTESON
  kind: primary_source
  reference: https://par.nsf.gov/servlets/purl/10162901
  locator: Complete main; Figures 1–4 and printed pp. 4955–4958; exact product numbering
    and polarity qualification
  accessed_at: '2026-10-21T14:44:57.255817Z'
  support: supports
  summary: The complete main explicitly identifies azabicyclene 1 as azetidomonamide
    B; its product 2 is a proline analogue, not A. PAO1 cultures contain B at lower
    basal levels and more after AHL supplementation. B/C/F/I insertion mutants lose
    B; D/G/H/J reduce it; E increases it. The authors explicitly cannot exclude insertion
    polarity. Purified His6-AzeB forms pyridinone intermediates 3/4, not final A or
    B; 3 has NMR support, 4 HRMS/MS without isolated NMR. No exact A isolation or
    A-specific genetic endpoint is established by this source.
  snapshot_sha256: 6a1a7f30c86108de005666f95442519b9823bb2b721be9ec21dc8a0d94b0b00f
- evidence_id: S097-E-PATTESON-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/15592466
  locator: Official SI S3–S6, S9/Table S2 and Figure S11; original complete-source
    preparation plus targeted re-read
  accessed_at: '2026-10-21T14:46:06.145223Z'
  support: supports
  summary: Official SI S3–S6 specifies PAO1, lacZ insertions in B/C/D/E/F/H/I/J and
    phoA in G; short-extension PCR verifies the insertion comparison, not whole-stock
    sequence identity or a nonpolar deletion. Cultures use 6 µM 3-oxo-C12-AHL and
    30 µM C4-AHL at 37 °C for 14 h. Native B is purified and NMR-characterized. PAO1
    azeB DNA is cloned into pLIC-His for E. coli BL21-Gold(DE3); the isolated enzyme
    assay stops at intermediates. The G label differs from the main figure, so the
    explicit Methods are retained. S9/Table S2 B crotonyl couplings 15.3/15.2 Hz support
    E geometry; the main leaves the ring absolute hand undetermined.
  snapshot_sha256: 42c1afc289be154f2b5cf9f6c496795ab74749b20a2b2b10166d905b6684cec1
- evidence_id: S097-E-ERNST-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/34875104
  locator: Original SI pp. 3–5 and 8, Table S1 p. 35; retained original p. 8 render
  accessed_at: '2026-10-21T14:48:59.968530Z'
  support: supports
  summary: Original 2022 SI pp. 3–5, 8 and Table S1 describes PAO1azeind, made by
    inserting rhaRS/PrhaB 26 bp upstream of PA3327, with PCR/sequencing and azeB RT-qPCR.
    This is native promoter engineering, separate from AB16.2, insertion-library genotypes
    and E. coli recombinant-protein hosts. A and B are numbered 3 and 4; original
    p. 8 gives A crotonyl J 15.3/15.3 Hz and B 15.3/15.4 Hz. The unavailable full
    main is not used to certify every later enzyme reaction.
  snapshot_sha256: abca22f6dccbaebedc5f987b70242859e74fcb6eec0cd1af1f7da01b1906e722
- evidence_id: S097-E-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002037.3/annotations.json
  locator: Complete current annotation; compounds, locus, taxonomy and legacy references
  accessed_at: '2026-10-21T14:57:06.938945Z'
  support: supports
  summary: Current version 3 remains active/questionable/completeness unknown. It
    lists both final compounds under one locus, PAO1 taxon 208964 and both 2019 references.
    The entry-level ordering does not make the first paper compound-specific proof
    for A. NRPS classification is compatible with the experimentally studied bimodular
    AzeB.
  snapshot_sha256: e94d035f8df6d66b82a9fa2c471f91c80511e5cf159c3035686176088df4931b
- evidence_id: S097-E-LOCUS
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AE004091.2&seq_start=3729471&seq_stop=3746067&rettype=gbwithparts&retmode=text
  locator: Header, source and all 11 CDS feature locations; retained locus-map.json
  accessed_at: '2026-10-21T15:05:12.157842Z'
  support: supports
  summary: The exact reference window is 16,597 bp and explicitly PAO1/taxon 208964.
    It spans PA3326–PA3336; AzeB/PA3327=AAG06715.1, AzeJ/PA3335=AAG06723.1, AzeK/PA3336=AAG06724.1.
    Hong uses ten genes through PA3335; Patteson includes PA3336. The reference deposit
    is not an independently sequenced AB16.2 stock, and interval membership does not
    prove every gene necessary.
  snapshot_sha256: 795ff688eb66d07e8b02960a453a42b394d7fd7d16d9912e93b8a6f08e96df80
- evidence_id: S097-E-IMODULON
  kind: database
  reference: https://imodulondb.org
  locator: Structured runner summaries p_aeruginosa/precise364/88 and p_aeruginosa/precise411/59;
    exact PA3326–PA3336 member rows
  accessed_at: '2026-10-21T14:54:44.212639Z'
  support: context_only
  summary: Both components contain the eleven PA locus tags with STRING taxon 208964.
    precise411/59 additionally contains phzB1/PA4211; its aggregate regulator labels
    cannot be transferred to the aze genes. These modules supply expression context,
    not final-product chemistry, AB16.2 stock sequence identity or native necessity.
  snapshot_sha256: 6e74cda69716d7051bc46c500829e62a50d3131de1297a83534f3cf5aa78587e
- evidence_id: S097-E-ACCESS
  kind: search
  reference: https://doi.org/10.1002/anie.201809981
  locator: Retained bounded original Hong SI attempts and Ernst full-main attempts
  accessed_at: '2026-10-21T14:47:45.400165Z'
  support: context_only
  summary: Hong full main is available, but detailed original SI, ECD parameters and
    all construct protocols remain unavailable. The 2022 official SI is available,
    its full main is not. No absence of uninspected experimental results is inferred.
  snapshot_sha256: 3591ba26f522c35f5d9f2dfb71718d7bb97cf6422016f36507372be74acd5a25
  search_scope: Only retained official Wiley SI links/static alternatives and published/author
    2022 full-main routes; no new network requests or global absence claim.
- evidence_id: S097-E-CONSUMERS
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: Source loading, claim-reference and strain application; full producer_strains.py,
    claim_references.py and lotus_exclusions.py contracts
  accessed_at: '2026-10-21T15:29:03.003709Z'
  support: supports
  summary: The implemented claim-reference and strain tables pin the entire original
    raw row. Strain qualification changes context only, not taxon or grades. LOTUS
    exclusions pin the exact key/taxon/DOI and entire triple row. Claim-reference
    and strain application reject structure_correction_note, requiring tested composition
    before any chemistry repair. The ignored-inclusive search found no existing matching
    maintained correction in the searched scope.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S097-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/097/science-overlay-search.json
  locator: Actual rg --no-ignore --hidden search receipt
  accessed_at: '2026-10-21T15:29:03.003709Z'
  support: context_only
  summary: Ignored-inclusive exact accession, names and full-key prefixes in all maintained
    curation tables, scripts and curate consumers; no claim of absence elsewhere.
  snapshot_sha256: e35a611eb203da05cf10bc40093cc0e09013c6ad19949f8ec1e1bb8ae4705e4e
  search_scope: Ignored-inclusive exact accession, names and full-key prefixes in
    all maintained curation tables, scripts and curate consumers; no claim of absence
    elsewhere.
- evidence_id: C097-OWNER
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/data/natural_products/alkaloids/azetidomonamide-b.yaml
  locator: Complete owner, literal xrefs, definition, source concepts, classification
    and discussion/history
  accessed_at: '2026-10-21T15:32:55.606516Z'
  support: supports
  summary: Owner and resolved packet are identical. Intake chemistry gives WNKLVRDIRPADMZ-SSDOTTSWSA-N,
    formula C10H12N2O2, charge 0 and centres [[10, 'R']]. The evidence scope here
    is chemical identity and provenance; biology and causal claims are assessed separately.
  snapshot_sha256: c6913bf58487afd9d835fb15af2a5315e873fc7e990b211a5aaef35bd05b6fa0
- evidence_id: C097-RAW
  kind: record_content
  reference: /private/tmp/npm-review-work/097/local-sources.json
  locator: All matching complete raw MIBiG, ChEBI, LOTUS and classifier rows
  accessed_at: '2026-10-21T15:32:55.606516Z'
  support: supports
  summary: All 1 MIBiG rows, 1 LOTUS rows, 0 eligible ChEBI rows and 1 classifier
    rows were read. Complete parsed row SHA256 values and reproduced source-concept
    IDs are retained in the per-record comparison.
  snapshot_sha256: 697f9ac294153def038048c3940ab95823770588199492bb01250e03f2d1400e
- evidence_id: C097-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch010/chemistry-first-seven/chemical-comparison.json
  locator: azetidomonamide B complete Standard and fixed-H graph comparison
  accessed_at: '2026-10-21T14:58:36.456215Z'
  support: supports
  summary: Raw/current BGC0002037.3 compound 2, NPAtlas NPA032934, PubChem 169492153
    and two-star CHEBI220639 JSON/MOL all agree at the less-specified key WNKLVRDIRPADMZ-SSDOTTSWSA-N;
    they assign the ring centre R but leave the acyclic crotonyl double bond unspecified.
    The missing bond is a potentially stereogenic double bond, not an unconstrained
    ring bond.
  snapshot_sha256: 68a2e565c0d5e67c8e524396a3d503990757f4924b65437559ab5129ab112710
- evidence_id: C097-AUTH0
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002037.3/annotations.json
  locator: current BGC0002037; compounds[1].structure
  accessed_at: '2026-10-21T14:57:06.938945Z'
  support: supports
  summary: 'Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula
    C10H12N2O2; charge 0; tetrahedral centres [[10, ''R'']].'
  snapshot_sha256: e94d035f8df6d66b82a9fa2c471f91c80511e5cf159c3035686176088df4931b
- evidence_id: C097-AUTH1
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/WNKLVRDIRPADMZ-SSDOTTSWSA-N/property/InChIKey,InChI,IsomericSMILES,MolecularFormula,Charge/JSON
  locator: PubChem 169492153; PropertyTable.Properties[0].SMILES
  accessed_at: '2026-10-21T14:57:06.842931Z'
  support: supports
  summary: 'Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula
    C10H12N2O2; charge 0; tetrahedral centres [[10, ''R'']].'
  snapshot_sha256: 97f1d1dd55b9045199337e6b670d05478a8382e39ffc058705017f710c2a5788
- evidence_id: C097-AUTH2
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/220639/
  locator: ChEBI JSON CHEBI:220639; default_structure.smiles
  accessed_at: '2026-10-21T14:57:58.203508Z'
  support: supports
  summary: 'Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula
    C10H12N2O2; charge 0; tetrahedral centres [[10, ''R'']].'
  snapshot_sha256: 0945b6cd06e96abbda7e533202451e59138d1b762f9381b6781335429fbe1daa
- evidence_id: C097-AUTH3
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/220639/
  locator: ChEBI MOL 220639; official MOL
  accessed_at: '2026-10-21T14:57:58.409843Z'
  support: supports
  summary: 'Valid parsed representation: True. Key WNKLVRDIRPADMZ-SSDOTTSWSA-N; formula
    C10H12N2O2; charge 0; tetrahedral centres [[3, ''R'']].'
  snapshot_sha256: 362b0f7d28fedf35daddb2991c0d80b899962890947a32a3a15e7247c685c7c5
- evidence_id: C097-GROUNDING-CODE
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: mint_identifier, choose_pathway, grouping and exact-key ChEBI grounding;
    source_concepts emission
  accessed_at: '2026-10-21T15:32:55.606516Z'
  support: supports
  summary: Source-concept identifiers hash source and accession:compound index, not
    labels or chemical keys. A unique eligible exact-key ChEBI row grounds EXACT;
    absent eligible rows retain the minted source identifier. Classification is joined
    by exact key.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: C097-ELIGIBILITY-CODE
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_chebi.py
  locator: MIN_STARS and extract_compounds status/stars filter
  accessed_at: '2026-10-21T15:32:55.606516Z'
  support: supports
  summary: Only the eligible three-star projection enters exact grounding; a currently
    accessible two-star record is not an asserted eligible authority.
  snapshot_sha256: 46e1898b88fce16096af34eb9e7c9dea40e4d7c8c157d60d485fa85878088e8f
- evidence_id: C097-WIKIDATA-Q113958881
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q113958881.json
  locator: Current P235, P234, P2017 and literal chemical entity identity
  accessed_at: '2026-10-21T15:27:08.306567Z'
  support: supports
  summary: Literal LOTUS chemical entity Q113958881 resolves to the stored full key;
    every retained isomeric SMILES reproduces the same Standard key and fixed-H graph.
    Canonical stereo-free SMILES is not substituted for the isomeric property.
  snapshot_sha256: d6149f85ca1097d072ca5cf9000340300d9294d28117a469761f629b0f93e0c3
- evidence_id: C097-OWNER-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/097/chemistry-owner-comparison.json
  locator: Exact owner/current authority linkage; independently parsed Wikidata and
    reconstructed source-concept hashes
  accessed_at: '2026-10-21T15:32:57.675261Z'
  support: supports
  summary: Recomputed all literal chemical Wikidata isomeric graphs and 1 accession:index
    source concepts against this owner. Full row pins and ignored-inclusive local
    search are recorded.
  snapshot_sha256: 1469d13b7811c7327e39748e901323c120cc3cb891389043e1f551695ed6d273
- evidence_id: C097-PRIMARY
  kind: primary_source
  reference: https://polytechnique.hal.science/hal-02096769/document
  locator: Hong 2019 complete structural paragraph and original Figure 1b, compound
    2
  accessed_at: '2026-10-21T14:45:41.096540Z'
  support: supports
  summary: Hong reports 4R for azetidomonamide B and draws an E crotonyl side chain.
    The drawing independently transcribes to WNKLVRDIRPADMZ-TYWZFMJISA-N. The owner
    preserves 4R but omits this acyclic double-bond geometry. Its stereo_complete=true
    value comes from a tetrahedral-centre-only computation and does not establish
    alkene geometry.
  snapshot_sha256: 0b5119850fd70aa51ffda9c29130d52253ceb4815a06530978fd53031680959e
- evidence_id: C097-NMR
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/15592466
  locator: Original SI S5 and S9 Table S2; azabicyclene compound 1
  accessed_at: '2026-10-21T14:46:06.145223Z'
  support: supports
  summary: Patteson compound 1 is azabicyclene/azetidomonamide B, not Hong A compound
    1. Its crotonyl olefinic H9/H10 couplings are 15.3 and 15.2 Hz, independently
    supporting trans/E geometry. The core absolute hand was not assigned in that study,
    so 4R remains the separate Hong assignment.
  snapshot_sha256: 42c1afc289be154f2b5cf9f6c496795ab74749b20a2b2b10166d905b6684cec1
- evidence_id: C097-PRIMARY-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch010/chemistry-first-seven/primary-transcription.json
  locator: azetidomonamide-B-Hong2019 independent atom/bond/wedge transcription
  accessed_at: '2026-10-21T15:00:14.209577Z'
  support: supports
  summary: The original graph has the same heavy-atom connectivity, neutral formula
    and 4R centre as the owner, with the additional E crotonyl bond. This is a stereochemical-resolution
    difference, not a constitutional isomer, opposite ring hand or tautomer.
  snapshot_sha256: afc598797396441ba958b0cc1a5c2b756a7379c32e403a286c8e7ccfc12f5cbb
- evidence_id: C097-PIXEL-QA
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch010/review-support/primary-transcription-qa/independent-primary-transcription-qa.json
  locator: Hong B manual CIP, double-bond geometry and original Patteson Table S2
    pixels
  accessed_at: '2026-10-21T15:06:21.544569Z'
  support: supports
  summary: Independent manual source-pixel QA confirms source C4 R and opposing carbon
    substituents at the crotonyl bond; original SI coupling values independently corroborate
    E.
  snapshot_sha256: 4085600b4eaee5674850820fb0a4d3e82ae080270b1177f06699970b709b11f0
- evidence_id: C097-ECD-ACCESS
  kind: search
  reference: https://onlinelibrary.wiley.com/doi/suppl/10.1002/anie.201809981/supinfo/anie201809981-sup-0001-misc_information.pdf
  locator: Original Hong ECD supplementary PDF request
  accessed_at: '2026-10-21T14:47:45.400165Z'
  support: context_only
  summary: The original ECD SI remains unavailable. The main positively assigns 4R;
    original computation details and measured/calculated curves were not inspected.
    The E-geometry finding does not depend on completing this separate absolute-hand
    check.
  snapshot_sha256: 3591ba26f522c35f5d9f2dfb71718d7bb97cf6422016f36507372be74acd5a25
  search_scope: Retained bounded publisher-linked Hong SI request and prior documented
    public attempts; no claim of nonexistence or unsupported opposite hand.
- evidence_id: C097-CONTRACT
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/structure_corrections.py
  locator: Complete guarded replacement consumer and row_digest
  accessed_at: '2026-10-21T15:32:55.606516Z'
  support: supports
  summary: Current actions only REPLACE_WITH_CHEBI or SPLIT_SHARED_WITH_CHEBI and
    require an exact three-star target row. They withhold old xrefs, retain source
    history, prevent collisions and do not transfer other exact-key joins. A primary-derived
    E refinement needs an explicit tested contract extension or a later verified eligible
    target; ordinary current rows cannot express it.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: C097-COMPOSITION
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/curate/claim_references.py
  locator: load_claim_references and correct_claim_reference; seed_from_sources.py
    producer-strain application
  accessed_at: '2026-10-21T15:32:55.606516Z'
  support: supports
  summary: Citation routing is pinned to the complete original source row and rejects
    a structure-corrected row. The seeder likewise rejects strain/isolate overlays
    on such rows. Any scientific method/citation/strain repair must compose through
    a reviewed tested contract retaining original-row and transformed-graph checks,
    not by bypassing these guards.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: C097-REPAIR-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/097/chemistry-repair-search.json
  locator: Ignored-inclusive key/selector search and complete committed inventory
    scans
  accessed_at: '2026-10-21T15:32:57.917857Z'
  support: supports
  summary: The original key has one MIBiG owner; the E target key has no current MIBiG
    or eligible ChEBI row in the committed inventories. Complete original raw and
    LOTUS row digests, candidate chemistry and search output are preserved.
  snapshot_sha256: 1d6666df75128ef9374a4fd9219eddc51c7c21f97242099b933b2f0f6e5ad995
  search_scope: Ignored-inclusive repository source/curation collision and existing-repair
    search; complete exact-key TSV scans. This is not a global current-authority absence
    claim.
- evidence_id: C097-FLAG-SCOPE
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/extract_mibig.py
  locator: structure_properties lines 165–168; schema ChemicalStructure.stereo_complete
    lines 392–396
  accessed_at: '2026-10-21T15:38:34.869298Z'
  support: context_only
  summary: The extractor computes stereo_complete by checking Chem.FindMolChiralCenters
    for undefined tetrahedral centres. It does not call a double-bond geometry check.
    The schema describes undefined stereocentres; the current boolean is therefore
    not independent evidence that E/Z is complete.
  snapshot_sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
assessments:
- assessment_id: R097-HISTORY
  area: provenance
  topic: Native status and retained audit history
  outcome: supported
  summary: The dated seed events and retained SEEDED status document generated provenance.
    This review adds no native curation event or status promotion.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - R097-OWNER
- assessment_id: R097-OPTIONAL
  area: completeness
  topic: Present optional assertions and enrichment limits
  outcome: not_applicable
  summary: The complete owner contains no structured pathway, causal graph, molecular
    target, bioactivity, clinical status, application, cross-corpus relationship or
    discussion. Optional enrichment is separate from correcting present claims; compound
    names and computed classes do not establish a mechanism or activity.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - R097-OWNER
  - R097-LOCAL-SOURCES
- assessment_id: R097-FILING
  area: representation
  topic: Computed filing and returned class scope
  outcome: supported
  summary: The owner reproduces its exact-key NPClassifier result, including model
    version npclassifier.gnps2.org@2026-09-07, Alkaloids filing, every superclass/class
    label (including the empty returned sets where applicable), and false glycoside
    flag. These remain computed predictions, not experiments proving precursor use,
    natural origin or stereochemistry. BGC classes retain their separate MIBiG source
    and biological assessment.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - R097-OWNER
  - R097-LOCAL-SOURCES
- assessment_id: R097-IMODULON-SCOPE
  area: completeness
  topic: Matching producer transcriptomic resources
  outcome: supported
  summary: The catalogue contains two P. aeruginosa datasets, making exact PAO1 locus-tag
    queries appropriate. Their retained query/member-summary outputs and original
    receipts are assessed in the scientific section. Module membership is expression
    context and does not establish metabolite production, direct regulator binding,
    identity of AB16.2 or a recombinant protein construct.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - R097-OWNER
  - R097-IMODULON-DATASETS
- assessment_id: R097-ORGANISM-IDS
  area: provenance
  topic: Literal LOTUS organism-identifier routing
  outcome: supported
  summary: Every literal organism entity in the matching LOTUS rows resolves to its
    retained taxon and NCBI identifier. The primary-source assessment independently
    addresses exact compound occurrence, native producer, collection host and experimental
    strain.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - R097-LOCAL-SOURCES
  - R097-Q31856
- assessment_id: S097-A-ORIGIN
  area: evidence
  topic: Natural occurrence and source-specific culture scope
  outcome: supported
  summary: The single Hong species occurrence is supported by B isolation in AB16.2.
    Independent Patteson isolation directly supports native PAO1 B production under
    its conditions. No recombinant host is treated as a natural occurrence.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-LOCAL
  - S097-E-HONG
  - S097-E-PATTESON
  - S097-E-PATTESON-SI
- assessment_id: S097-A-LOCUS
  area: evidence
  topic: Exact product, native background and evidence tier
  outcome: supported
  summary: The current Knock-out studies category is supported by native insertion/product
    experiments, with polarity explicitly unresolved. CLUSTER_DEMONSTRATED and BGC_CHARACTERIZED
    are compatible at that locus-level scope; they do not claim every encoded protein
    has a final-product assay.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-HONG
  - S097-E-PATTESON
  - S097-E-PATTESON-SI
  - S097-E-LOCUS
  - S097-E-MIBIG
  dimensions:
  - name: experimental_strain
    value: PAO1 wild type and Manoil insertion library; independently AB16.2
    definition: Experimental culture background is distinct from the reference locus
      and recombinant protein-expression host.
    evidence_ids:
    - S097-E-HONG
    - S097-E-PATTESON
    - S097-E-LOCUS
  - name: assay_endpoint
    value: Final native A/B loss and rescue; isolated precursor enzymology
    definition: AzeJ yields AZC and purified AzeB yields intermediates, not a demonstrated
      complete heterologous final-product pathway.
    evidence_ids:
    - S097-E-HONG
    - S097-E-PATTESON-SI
  - name: stereochemical_resolution
    value: Hong claims A 5R / B 4R; original ECD SI inaccessible
    definition: Main-body assignment is retained without an independent ECD recalculation;
      geometry is adjudicated separately.
    evidence_ids:
    - S097-E-HONG
    - S097-E-ACCESS
- assessment_id: S097-A-SEQUENCE
  area: grounding
  topic: Reference locus and source-version meaning
  outcome: supported
  summary: The current MIBiG interval is the exact PAO1 reference window and maps
    to eleven native features. No complete tagged construct or AB16.2 whole-genome
    identity is asserted; NRPS is a supported pathway class.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-LOCUS
  - S097-E-MIBIG
  - S097-E-PATTESON-SI
- assessment_id: S097-A-OPTIONAL
  area: completeness
  topic: Bounded additional mechanism and expression evidence
  outcome: supported
  summary: The existing sparse owner has no mandatory optional-mechanism deficit.
    Later native promoter engineering and expression modules are available context;
    missing individual enzyme graphs are not findings. Phenotype differences between
    mutants are not assigned to purified A or B without compound-specific tests.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - S097-E-HONG
  - S097-E-ERNST-SI
  - S097-E-IMODULON
- assessment_id: C097-CLASS
  area: representation
  topic: Classifier provenance and filing
  outcome: supported
  summary: The complete exact-key NPClassifier row reproduces the stored Alkaloids
    filing and all supplied superclass/class labels; empty finer classifications are
    preserved. This is model-derived classification, not evidence of biological origin.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-RAW
  - C097-GROUNDING-CODE
- assessment_id: C097-IDENTITY
  area: identity
  topic: Constitution and 4R identity versus missing E precision
  outcome: concern
  summary: All current authority graphs reproduce the less-specified owner and therefore
    repeat its missing crotonyl geometry. The original Hong drawing and independent
    Patteson coupling evidence support E. The formula C10H12N2O2, neutral charge and
    retained 4R centre do not change.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-OWNER
  - C097-PRIMARY
  - C097-NMR
  - C097-PRIMARY-GRAPH
  - C097-PIXEL-QA
  - C097-COMPARISON
- assessment_id: C097-GROUNDING
  area: grounding
  topic: Ineligible exact authority and migration boundaries
  outcome: supported
  summary: CHEBI:220639 is two-star and carries the same less-specified graph; it
    is not a repair target or eligible exact grounding. The minted identifier correctly
    reflects the current source concept. A corrected graph must explicitly re-adjudicate
    old-key xrefs, occurrence and model-classification joins without asserting equivalence
    at full stereochemical resolution.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-RAW
  - C097-GROUNDING-CODE
  - C097-ELIGIBILITY-CODE
  - C097-CONTRACT
  - C097-REPAIR-SEARCH
- assessment_id: C097-ABSOLUTE-LIMIT
  area: evidence
  topic: Reported 4R assignment with inaccessible ECD details
  outcome: unknown
  summary: Hong positively reports 4R, but its original SI is unavailable; Patteson
    supplies E-geometry evidence without an independent absolute core assignment.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  evidence_ids:
  - C097-PRIMARY
  - C097-NMR
  - C097-ECD-ACCESS
findings:
- finding_id: C097-F-E-GEOMETRY
  issue_key: azetidomonamide-b-missing-primary-supported-crotonyl-e
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Encode the primary-supported E crotonyl geometry
  description: The source-derived graph omits the primary-supported acyclic crotonyl
    E geometry. Hong Figure 1b and independent Patteson NMR couplings support E; current
    authority agreement repeats the less-specified source graph. The stored stereo_complete=true
    flag reflects assigned tetrahedral centres only and is not evidence that alkene
    geometry was tested or complete.
  target_ids:
  - naturalproductmech:mibig-269a84b809
  field_paths:
  - chemical_structure.smiles
  - chemical_structure.standard_inchi
  - chemical_structure.standard_inchi_key
  - xrefs
  evidence_ids:
  - C097-OWNER
  - C097-PRIMARY
  - C097-NMR
  - C097-PRIMARY-GRAPH
  - C097-PIXEL-QA
  - C097-CONTRACT
  - C097-REPAIR-SEARCH
  - C097-FLAG-SCOPE
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Implement an explicitly typed source-pinned primary-derived stereochemical
      refinement or use a later verified eligible target
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Add the reviewed decision only after its consumed contract supports this
      repair
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Re-adjudicate exact-key joins, representation metadata and composition with
      scientific corrections
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve the complete original source row unchanged
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserve the original triple and explicitly adjudicate any corrected-key
      assertion
actions:
- action_id: C097-A-E-GEOMETRY
  finding_ids:
  - C097-F-E-GEOMETRY
  target_ids:
  - naturalproductmech:mibig-269a84b809
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Implement an explicitly typed source-pinned primary-derived stereochemical
      refinement or use a later verified eligible target
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Add the reviewed decision only after its consumed contract supports this
      repair
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Re-adjudicate exact-key joins, representation metadata and composition with
      scientific corrections
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Preserve the complete original source row unchanged
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Preserve the original triple and explicitly adjudicate any corrected-key
      assertion
  description: Implement and test a primary-derived stereochemical-refinement contract
    before adding any decision. Guard exact selector BGC0002037:2 version 3, complete
    original row SHA256 a5658a2f86c6c54360c2f6f043b2aac4d900173ec38f0c01e55d1eed0776b479,
    old key WNKLVRDIRPADMZ-SSDOTTSWSA-N, old SMILES 'CC=CC(=O)NC1=CC(=O)[C@H]2CCN12',
    original stereo_complete=true and database_ids=npatlas:NPA032934. The reviewable
    E/4R representation is C/C=C/C(=O)NC1=CC(=O)[C@H]2CCN12 ; InChI=1S/C10H12N2O2/c1-2-3-10(14)11-9-6-8(13)7-4-5-12(7)9/h2-3,6-7H,4-5H2,1H3,(H,11,14)/b3-2+/t7-/m1/s1
    ; WNKLVRDIRPADMZ-TYWZFMJISA-N, formula C10H12N2O2, charge 0. Preserve Hong's reported
    4R and its original ECD access limitation; change only the crotonyl geometry,
    not constitution or ring hand. Confirm a fresh eligible-grounding/collision search
    before implementation; the currently committed CHEBI projection has no target
    row and current CHEBI:220639 is ineligible and less specified, so existing REPLACE_WITH_CHEBI
    is not executable for this candidate. Keep the original MIBiG source row unchanged
    and source concept identifiable. Re-adjudicate the old-key NPAtlas/Wikidata/PubChem
    links as less-specified references rather than claiming exact full-graph equivalence.
    The existing LOTUS triple is old key + NCBITaxon:287 + DOI:10.1002/ANIE.201809981,
    chemical Q113958881, complete row SHA256 026e6465389f50ee4aa39481c2f98e55097d567f44bed2501973b8bc84537f3b;
    retain its source provenance and use an explicit reviewed corrected-claim hook
    if retaining the independently supported named B occurrence at the new key. Do
    not blindly transfer or silently discard old-key occurrence, classifier, definition
    or other joins. Current citation/strain consumers reject structure-corrected rows,
    so compose this refinement with any separately justified biological corrections
    under original-row pins and transformed-graph verification. Do not edit generated
    YAML, raw inventories, or create an unconsumed decision placeholder.
  generator: Reviewed extension of structure-correction and seeder identity/join contracts,
    followed by guarded regeneration.
  acceptance_checks:
  - Changed raw source context, row digest, old graph, source version or candidate
    graph fails closed; no sibling A row changes.
  - Output contains E crotonyl geometry and retained 4R, with internally consistent
    InChI/key and preserved tetrahedral-only completeness semantics; the ECD access
    limitation remains explicit.
  - No false three-star grounding, silent collision, automatic old-key join transfer
    or claim that less-specified authority graphs are exact corrected stereostructures.
  - Biological method/citation/strain repairs compose without bypassing existing guards;
    exact source provenance and original claims remain auditable.
  - Strict target, reproduction, corpus and scientific graph checks pass after implementation;
    this review performs no regeneration.
limitations:
- The review assesses current assertions and concrete evidence gaps. It does not claim
  exhaustive discovery of every later study or require every optional mechanism for
  review coverage.
- Original Hong ECD/construct SI remains unavailable despite retained bounded routes;
  the positive main-body results remain usable at their explicit scope.
- The 2022 full main is unavailable; inspected SI is not a substitute for every main-body
  enzyme result.
- The PAO1 accession is a reference-sequence bridge, not an independent genome comparison
  of AB16.2, every insertion stock or a recombinant fusion.
- Chemistry/xref assessments are delivered separately; no optional pathway completion
  is required by this packet.
- The confirmed defect is omission of supported alkene geometry, not a demonstrated
  wrong 4R assignment. Original Hong ECD SI is unavailable, and the suggested E/4R
  graph remains a reviewable source-based correction rather than an adopted corpus
  change. No claim of global absence of a later exact authority record is made.
- The configured identifier-label gate accepts 499 warning-level mismatches and 35
  explicit exceptions and skips 4,744 no-adapter pairs; exit 0 does not independently
  verify every identifier or scientific claim.
- The quality suite reports 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21).
  Skipped tests are not counted as passing tests. Existing ontology caches were used;
  no multi-gigabyte cache download was required.
- Native gates assess deterministic consistency and configured invariants. They do
  not establish biological production, stereochemical specificity, evidence adequacy,
  or literature-level claim support.
- The five reused gates retain their batch004 execution times and cached ontology
  results. Reuse establishes unchanged repository inputs; it is not a new remote authority
  query or new assertion of ontology freshness.
- The ignored-inclusive check enumerates record and saved-review YAML paths, and all
  tracked files are hashed. Generated Python bytecode and external tool caches are
  not claimed to have been independently byte-pinned at the prior execution.
notes:
- No scientific owner, inventory, curation table, native status or history was edited.
  Actions are proposed work.
- Baseline gates retain their actual original receipts after byte-for-byte input verification;
  target strict validation ran afresh. Scientific failed or unavailable checks are
  distinct from bundle validation.
tags:
- path-order-campaign
- batch-010
```
