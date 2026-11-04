# Acetoxy-methylpentyl indole: resolvable accession and congener-specific evidence limits

- Review: 20261021T075944Z-3-2-acetoxy-3-oxo-4-methylpentyl-indole
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:52:41.274809Z
- Finished UTC: 2026-10-21T07:59:44.526501Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The shorter acetoxypentyl indole has coherent structure, one declared unassigned centre, source metadata and species/strain boundaries. Its shortened NPAtlas identifier resolves exactly; a stereospecific two-star ChEBI candidate is correctly excluded. Primary patent occurrence is supported with a printed mass inconsistency preserved. No confirmed owner defect was established; exact 1995 citation content and 2014 congener assays remain unverified.

## Scope And Provenance

One complete owner and resolved view, exact chemical identity and congener boundary, all occurrence/producer/locus evidence, taxonomy, source concepts, classification, grounding and history.

Selection: Thirteenth initially unreviewed path, third in batch 002 from fresh origin/main. Starts and saves follow path order. Fresh-main authoritative coverage is 91 valid bundles/54 of 3,116 records; pending PR 1000 adds ten separately validated campaign targets. Ignored files included. This bundle assesses one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-39ca043bc0 | data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml | generated | 3-(2'-acetoxy-3'-oxo-4'-methylpentyl)-indole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-39ca043bc0 | Whole owner validates with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-39ca043bc0 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-39ca043bc0 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-39ca043bc0 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-39ca043bc0 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-39ca043bc0 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Internal chemical structure and stereochemistry consistency | passed | True | naturalproductmech:mibig-39ca043bc0 | SMILES and InChI regenerate the exact stored InChIKey; one unassigned stereocentre agrees with stereo_complete:false. |
| Literal NPAtlas identifier resolution and full identity | passed | True | naturalproductmech:mibig-39ca043bc0 | Stored NPA03248 resolves with HTTP200 to NPA003248, and complete structure matches owner. Canonical spelling request is byte-identical. |
| Current ChEBI full-key and candidate-stereochemistry check | passed | True | naturalproductmech:mibig-39ca043bc0 | Exact full-key query returns no match; CHEBI:200350 is 2-star and stereospecific with a different full InChIKey, so it is not an eligible exact replacement. |
| Exact target in original1995 journal paper | unavailable | True | naturalproductmech:mibig-39ca043bc0 | Full abstract and database mapping inspected; direct compound-level journal content remains unavailable. |
| Exact-congener biosynthetic experiments and stereochemistry | unavailable | True | naturalproductmech:mibig-39ca043bc0 | The family-level primary abstract is readable, but main body and SI were not obtained. Exact product panels, controls and stereochemical evidence remain unknown. |
| Structured expression-source applicability | not_applicable | False | naturalproductmech:mibig-39ca043bc0 | No Xenorhabdus dataset occurs in the returned catalogue; no biological absence conclusion. |

## Scientific And Domain Assessments

### Shorter acetoxypentyl connectivity and declared stereo resolution

identity: supported. Targets: naturalproductmech:mibig-39ca043bc0.

The complete owner structure and official NPAtlas structures agree exactly. One unspecified centre is represented honestly. The longer acetoxyhexyl congener has a different formula/key and two potential stereocentres; its evidence is not transferred to this target.

### Minted status and near stereospecific ChEBI candidate

grounding: supported. Targets: naturalproductmech:mibig-39ca043bc0.

The exact source-concept identifier recomputes. No eligible matching three-star row occurs in the fully parsed pinned inventory. Current CHEBI:200350 is two-star and a different full stereochemical identity, while the complete-key search returns no match. The existing minted rationale is coherent.

### Literal shortened NPAtlas identifier

identity: supported. Targets: naturalproductmech:mibig-39ca043bc0.

Stored NPA03248 resolves directly and returns exact NPA003248, verified by a separate canonical request with identical bytes. The shortened identifier is functional and does not require an invalid-reference finding.

### Exact natural occurrence with primary-source mass discrepancy preserved

evidence: supported. Targets: naturalproductmech:mibig-39ca043bc0.

The primary patent names and isolates exact ID2 from X. bovienii culture broth. This independently corroborates species occurrence and natural origin while retaining unresolved stereochemistry. Its printed mass line conflicts internally and with the computed 273 molecular mass, so that line is not used as identity proof. Source strain A2/ATCC 35271 is not promoted to SS-2004 biosynthetic evidence.

### Exact compound content of the 1995 journal citation

evidence: unknown. Targets: naturalproductmech:mibig-39ca043bc0.

The DOI and PMID resolve, and NPAtlas explicitly maps this structure to the paper. The inspected primary abstract does not identify this individual compound; the independent patent is not the journal full text. Exact citation verification remains incomplete.

### Species occurrence versus SS-2004 source producer

provenance: supported. Targets: naturalproductmech:mibig-39ca043bc0.

NCBI and Wikidata confirm species 40576 and descendant strain 406818. Both are OTHER_BACTERIAL. The same species does not equate A2 and SS-2004; occurrence remains separate from native producer and locus grading.

### Computed classification, asserted PKS class and historical seed events

provenance: supported. Targets: naturalproductmech:mibig-39ca043bc0.

The exact-key classifier output and version match the owner. PKS derives separately from the source locus, not from computational natural-product likeness. Two seed events and SEEDED status do not claim a prior full scientific review; original source concepts are intact.

### Complete owner without separate mechanism/activity assertions

scope: not_applicable. Targets: naturalproductmech:mibig-39ca043bc0.

No optional graph, pathway, quantitative activity, molecular target, clinical or sibling-link assertion occurs in the full resolved owner. The complete returned iModulon catalogue contains no covered Xenorhabdus dataset. Optional expansion is not required, and absent dataset coverage is not negative biological evidence.

### BGC0000189 compound 3 source, strain and locus mapping

evidence: supported. Targets: naturalproductmech:mibig-39ca043bc0.

The exact connectivity, SS-2004 taxon, deposited interval, source method vocabulary and generated two-claim grading agree with the inspected databases. The primary abstract independently corroborates SS-2004 and the reported experimental method categories. Neither heterologous expression nor enzymology alone is used to upgrade native production.

### Exact acetoxypentyl congener in XclA/B/C experiments

evidence: unknown. Targets: naturalproductmech:mibig-39ca043bc0.

The source database assigns demonstrated locus methods to exact compound 3, but the accessible primary abstract summarizes the family. Without the full body/SI, the exact XclA/B/C preparation, target-product experiment, native chromatogram, controls and strain-specific construct details could not be independently adjudicated. No contrary experimental result or confirmed owner defect was found; this remains a primary-access limitation.

### S-selectivity versus the exact one-centre acetoxypentyl target

identity: unknown. Targets: naturalproductmech:mibig-39ca043bc0.

The owner explicitly says stereo_complete:false. This exact pentyl graph has only the 2-prime stereocentre; the two equivalent methyl substituents at 4-prime preclude a second stereocentre. XclA S-selectivity in the primary abstract does not independently establish which exact congeners were stereochemically measured. No R/S repair or stereo_complete:true promotion is warranted from the abstract alone. The original occurrence and identity are assessed separately in this review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R-OWNER | data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml; Complete owner and resolved mechanism view; exact local inventory rows and all history | supports | This is the shorter acetoxypentyl indole, MIBiG compound 3. Its one species occurrence, SS-2004 producer/locus, one NPAtlas cross-reference, classification and two seed events were read. No graph, separate pathway, activity, target, clinical or sibling-link assertion is present. |
| R-CHEMISTRY | /private/tmp/npm-review-work/013/identity/structure-comparison.json; RDKit complete graph, InChI/key, formula and stereocentre comparisons | supports | Owner SMILES and InChI regenerate MNIVLQOKRHODTM-UHFFFAOYSA-N, C16H19NO3 and one unspecified centre at 2-prime. The 4-prime carbon has two equivalent methyl groups and is not stereogenic. stereo_complete:false is correct; it does not assert a racemate. |
| R-NPA-STORED | https://www.npatlas.org/api/v1/compound/NPA03248?include=classifications; Complete official API response to the literal stored accession | supports | The literal NPA03248 request returns HTTP 200 with canonical NPA003248. Its full InChI/key and graph match the owner exactly; origin metadata identify X. bovienii A2 and DOI:10.1021/np50121a016. No invalid-xref finding follows. |
| R-NPA-CANONICAL | https://www.npatlas.org/api/v1/compound/NPA003248?include=classifications; Complete official response to the returned canonical accession | supports | The separately requested NPA003248 response is byte-identical to the successful stored-ID response. Canonical spelling was verified, not assumed. |
| R-CHEBI-CANDIDATE | https://www.ebi.ac.uk/chebi/backend/api/public/compound/200350/; Current two-star compound entry, explicit InChI stereochemical layer and full key | supports | CHEBI:200350 is two-star and specifies the S centre: MNIVLQOKRHODTM-HNNXBMFYSA-N, with /t15-/m0/s1. It is not an exact full-key match to the stereo-unspecified owner and cannot supply its absolute configuration. |
| R-CHEBI-SEARCH | https://www.ebi.ac.uk/chebi/backend/api/public/es_search?term=MNIVLQOKRHODTM-UHFFFAOYSA-N&amp;size=100; Exact full-key official API response body | context_only | The structured response says no compound matches the supplied complete key. This is a bounded current search, not a database-wide independent absence audit. |
| R-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/200350/; Complete official default molfile, RDKit stereochemical comparison | supports | The default molfile independently reproduces the stereospecific CHEBI:200350 full key, distinct from the owner. The shared connectivity prefix does not justify grounding to a stereochemically specified term. |
| E-PUBMED-1995 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=24488732,7561900&amp;retmode=xml; PubmedArticle PMID 7561900; ArticleId DOI and full AbstractText; original source reused after target-specific comparison | partial | PMID:7561900 maps to DOI:10.1021/np50121a016, Li et al. 1995. Its full primary abstract reports indole isolation from X. bovienii A2 but does not name individual structures. The exact target-to-paper mapping is supplied by NPAtlas as database provenance; the journal compound-level body remains uninspected. |
| E-TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=40576,406818&amp;retmode=xml; TaxaSet entries 40576 and 406818, scientific names, ranks, parent and lineage; original source reused after target-specific comparison | supports | NCBITaxon:40576 is species Xenorhabdus bovienii. NCBITaxon:406818 is strain Xenorhabdus bovienii SS-2004, directly parented to 40576. Both belong to Bacteria, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Morganellaceae. OTHER_BACTERIAL is consistent for both; A2 and SS-2004 remain distinct contexts. |
| E-WIKIDATA | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q26307560&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Entity Q26307560 English label and P685 taxon mapping; original source reused after target-specific comparison | supports | Q26307560 resolves to Xenorhabdus bovienii and its P685 statement is 40576, agreeing with the occurrence note and NCBI species identity. The later successful API retrieval supersedes the initial403 attempt. |
| E-GRADE-RULE | docs/HARMONIZATION.md; Producer versus occurrence section and method-to-producer/locus grading table; original source reused after target-specific comparison | supports | Heterologous expression and enzymatic assays map to SOURCE_ASSERTION for the native producer and CLUSTER_DEMONSTRATED for the locus. The owner preserves that separation and cites both imported claims as DATABASE_ASSERTION. This rule explains extraction; it does not establish compound-specific experiments. |
| R-IMODULON-CATALOGUE | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Complete installed kg-microbe-sources datasets response; actual command receipt in010/imodulon-context-receipts.json; original source reused after target-specific comparison | context_only | The complete returned catalogue has 28 dataset keys; none covers Xenorhabdus. No strain-matched structured expression-module query is applicable to this record. This is catalogue coverage only and not evidence against xenocyloin production or gene activity. |
| R-PATENT-ID2 | https://patentimages.storage.googleapis.com/88/ee/a5/deee26bcd7e0de/WO1995003695A1.pdf; Original WO1995003695A1 printed pp 32-34, Examples 10-11; page images visually inspected at 2026-10-21T07:56:13Z | supports | The patent reports extraction of cell-free X. bovienii broth, naming A2 or ATCC 35271, and isolation of pure ID2. It explicitly identifies ID2 as the acetoxy-methyl-oxopentyl indole and reports proton NMR. The original page actually prints M+ 223 alongside a 213 fragment labelled M−60; this internally inconsistent mass line is not an OCR-only error and is not used to verify molecular mass. The named compound, isolation and NMR support occurrence at unresolved stereochemical resolution; no absolute configuration is assigned. |
| R-INVENTORY | data/raw/mibig_compounds.tsv; Exact BGC0000189:3 row; full-key LOTUS/NPClassifier/ChEBI inventories parsed independently of gitignore | supports | Exact source compound 3 retains the stored structure, NPA03248 and entry-level PMID:24488732. The corresponding LOTUS row is species 40576 with DOI:10.1021/NP50121A016 and Q26307560. NPClassifier gives the exact recorded Alkaloids/Tryptophan alkaloids/Simple indole alkaloids, glycoside false. No three-star ChEBI inventory row matches the complete key. The implemented source-concept hash recomputes the owner identifier. |
| xcl-mibig189-compound3 | https://mibig.secondarymetabolites.org/repository/BGC0000189.4/annotations.json; Complete v4 JSON; compounds[2] (one-based compound_index 3), taxonomy, loci and gene annotations; source-access.json | supports | The exact recorded connectivity is compound 3, 3-(2-acetoxy-3-oxo-4-methylpentyl)-indole, C16H19NO3 and key MNIVLQOKRHODTM-UHFFFAOYSA-N. Its SMILES omits stereochemistry. This is the shorter acetylated congener; compound 4 has an extra side-chain carbon, while compounds 1/2 bear hydroxy groups. MIBiG lists SS-2004 taxon 406818, FN667741.1:3771005..3779127, PKS/Type III and Enzymatic assays plus Heterologous expression. The entry-level reference is PMID:24488732; no compound-specific experiment is annotated. The source is active, complete and questionable quality. This existing source was re-compared to record 013; its original retrieval timestamp is retained. The owner faithfully preserves the strain/locus facts and distinguishes SOURCE_ASSERTION producer from CLUSTER_DEMONSTRATED locus. The NPAtlas identifier is assessed separately by the identity reviewer. |
| xcl-pubmed2014-abstract | https://pubmed.ncbi.nlm.nih.gov/24488732/; DOI:10.1002/cbic.201300694, title, author list and complete primary abstract; official PubMed XML retrieved in source-access.json | partial | The primary abstract explicitly identifies the xenocyloin cluster in X. bovienii SS-2004 and reports heterologous expression and in vitro enzyme characterization. It describes XclA as S-selective and XclB/XclC as acylating ketosynthases accepting acetyl-, propionyl- or malonyl-CoA. It also reports preferential native production by the primary bacterial variant. This corroborates strain and method categories at family scope. It does not expose exact acetoxypentyl compound numbering, individual enzyme-substrate/product panels, construct details, controls, or exact-congener absolute-configuration measurements. No exact-congener assay or stereochemical conclusion is inferred from the abstract. The original source-access timestamp is reused; this is not a fresh retrieval. |
| xcl-native-locus-bridge | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FN667741.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text&amp;from=3771005&amp;to=3779127; VERSION, source strain/taxon, full interval CDS annotation; locus.gb | supports | The 8123-bp interval belongs to X. bovienii SS-2004 with taxon 406818. CBJ83019.1/XBJ1_3901 (MIBiG xclA) lies at 3777430..3779127 on the reverse strand, and CBJ83018.1/XBJ1_3900 (MIBiG xclB) lies at 3776409..3777440 on the reverse strand. The interval also includes CBJ83016.1/XBJ1_3898, annotated as a synthase III, but the inspected GenBank annotation alone does not identify it experimentally as XclC. These records establish the strain/accession bridge, not full-locus sufficiency or historical construct sequences. |
| xcl-owner-source-grade | data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml; data/raw/mibig_compounds.tsv; conf/producer_evidence.tsv; Full owner read at 2026-10-21T07:54:41Z, re-read at 07:56:11Z; exact local-sources.json BGC0000189:3 row and chemistry.json | supports | The owner is a stereo-incomplete source-defined structure, not an explicitly racemic material or stereochemically assigned molecule. The exact shorter pentyl graph has one unassigned centre at the acetoxy-bearing 2-prime carbon; 4-prime bears two equivalent methyl groups and is not stereogenic. The method map treats enzymatic and heterologous evidence as support for the cluster only; it does not upgrade native producer evidence to BGC_CHARACTERIZED. The owner applies that distinction correctly. No XclA/B/C graph or protein-reference claim is present in this target. |
| xcl-fulltext-si-unavailable | https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cbic.201300694; Public publisher page identifies SI cbic_201300694_sm_miscellaneous_information.pdf; attempted full, PDF, suppl/supinfo and normal downloadSupplement routes; bgc-access.json | unknown | The publisher abstract and SI filename were visible in indexed primary content. Both Wiley domains returned HTTP 403 for the exact supplement and full text, as did the normal PDF and downloadSupplement routes. The Crossref-listed TDM endpoint returned HTTP 400 requiring a TDM client token; no credentials or paid service were used. The body and SI were therefore not obtained or inspected. Access failure is not evidence that the paper lacks the exact product experiment. |
| xcl-institutional-copy-unavailable | https://pure.mpg.de/rest/items/item_3369009; Public author-linked institutional record, complete JSON; bgc-pure-item.json and bgc-access.json | unknown | The author publication list resolves to MPG.PuRe item 3369009. Its complete public REST record contains the matching article metadata and abstract, without a file/component entry providing the manuscript or supplement. OpenAlex separately listed only closed publisher and PubMed locations. This bounded repository check supplied no additional experimental text; it does not show that no author copy exists elsewhere. |

## Limits And Additional Notes

- The requested 2014 main body and named SI were not accessible through the bounded free public routes. Only the complete primary abstract, bibliographic metadata and database/locus records were inspected. No full-text or SI experiment is represented as read.
- Exact target compound numbering within the 2014 paper, native and heterologous metabolite panels, individual XclA/B/C products and controls, expression constructs, assay conditions and stereochemical derivatization or comparison methods remain unverified.
- The exact structure is MIBiG compound 3, not a hydroxy congener or the longer hexyl congener. Its only potential stereocentre is 2-prime. No congener transfer is used to infer exact target stereochemistry or an experimental claim.
- The source PKS/Type III classification is faithfully generated. The abstract describes unusual acylating ketosynthases but is insufficient to adjudicate a classification repair; no reclassification finding is made.
- Native SS-2004 production is reported at family level in the abstract. The record retains SOURCE_ASSERTION; no native knockout, locus necessity or whole-region sufficiency is inferred.
- The cited 1995 journal exact-compound body remains uninspected. NPAtlas database mapping and independent patent occurrence do not substitute for that citation-level check.
- The primary patent printed p33 reports M+ 223 with a 213 M−60 fragment for ID2. This contradicts itself and the represented formula; the original page image confirms it is not merely an HTML OCR substitution. Its mass line is excluded from independent molecular-mass proof, while exact naming/isolation and reported NMR remain positive evidence.
- The selected ChEBI candidate is S-specified and only two-star. Its stereochemistry is not transferred to an unspecified owner.
- Native source/access receipts for the shared locus, taxon, primary abstracts and dataset catalogue are reused with original timestamps after exact-target comparison. No new full-text/SI access is claimed.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific record or maintained input was edited. This partial observation does not promote SEEDED to REVIEWED.
- The optional canonical NPAtlas spelling is a display-consistency opportunity, not a demonstrated broken xref. No corrective action is proposed solely from successful alias resolution.
- Source-patent mass inconsistency is preserved as a primary-source limitation rather than silently corrected or attributed to the YAML owner.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075944Z-3-2-acetoxy-3-oxo-4-methylpentyl-indole
kind: record
repository: CultureBotAI/NaturalProductMech
title: 'Acetoxy-methylpentyl indole: resolvable accession and congener-specific evidence
  limits'
started_at: '2026-10-21T07:52:41.274809Z'
finished_at: '2026-10-21T07:59:44.526501Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: The shorter acetoxypentyl indole has coherent structure, one declared unassigned
  centre, source metadata and species/strain boundaries. Its shortened NPAtlas identifier
  resolves exactly; a stereospecific two-star ChEBI candidate is correctly excluded.
  Primary patent occurrence is supported with a printed mass inconsistency preserved.
  No confirmed owner defect was established; exact 1995 citation content and 2014
  congener assays remain unverified.
source:
  git_revision: 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b
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
  - path: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml
    sha256: daf800ee8a516270fc5a017ba008cd405efbc16cc0aff79886677617a162faa4
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete owner and resolved view, exact chemical identity and congener
    boundary, all occurrence/producer/locus evidence, taxonomy, source concepts, classification,
    grounding and history.
  selection: Thirteenth initially unreviewed path, third in batch 002 from fresh origin/main.
    Starts and saves follow path order. Fresh-main authoritative coverage is 91 valid
    bundles/54 of 3,116 records; pending PR 1000 adds ten separately validated campaign
    targets. Ignored files included. This bundle assesses one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-39ca043bc0
targets:
- target_id: naturalproductmech:mibig-39ca043bc0
  path: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml
  label: 3-(2'-acetoxy-3'-oxo-4'-methylpentyl)-indole
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
  summary: Whole owner validates with zero ERROR rows.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  command: just validate-strict data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml
    --out /private/tmp/npm-review-work/013/strict.tsv
  exit_code: 0
  scope_note: Actual target check finished 2026-10-21T07:52:43.593811Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808Z; finished 2026-10-21T06:37:52.997020Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-corpus.log. Reused for
    batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703Z; finished 2026-10-21T06:38:35.570687Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-reproduction.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598Z; finished 2026-10-21T06:37:11.018366Z. Exact
    session transcript: /private/tmp/npm-native-checks/review-queue.log. Reused for
    batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212Z; finished 2026-10-21T06:38:54.776253Z. Exact
    session transcript: /private/tmp/npm-native-checks/validate-products.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
- check_id: shared-qc
  name: Full repository quality gate after environment repair
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed after installing the pinned
    linter, allowing the read-only governance fetch, and restoring the required provenance
    tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116
    records and zero errors. Documentation, provenance, source queue, governed artifacts,
    generated pages, reproduction, filing integrity and corpus reporting all passed.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886Z; finished 2026-10-21T06:54:53.950582Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt4.log. Reused for
    batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
- check_id: identity-013-internal-structure
  name: Internal chemical structure and stereochemistry consistency
  status: passed
  required: true
  summary: SMILES and InChI regenerate the exact stored InChIKey; one unassigned stereocentre
    agrees with stereo_complete:false.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  command: .venv/bin/python /private/tmp/npm-review-work/013/check_identity.py
  exit_code: 0
  expected_exit_code: 0
  scope_note: RDKit 2026.03.5; actual check timestamp 2026-10-21T07:54:33.166408Z.
    Warnings about omitted undefined stereo are consistent with this representation.
  evidence_ids:
  - R-CHEMISTRY
- check_id: identity-013-npatlas-resolution
  name: Literal NPAtlas identifier resolution and full identity
  status: passed
  required: true
  summary: Stored NPA03248 resolves with HTTP200 to NPA003248, and complete structure
    matches owner. Canonical spelling request is byte-identical.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  scope_note: Free official API responses and exact receipts retained.
  evidence_ids:
  - R-NPA-STORED
  - R-NPA-CANONICAL
- check_id: identity-013-chebi-candidate
  name: Current ChEBI full-key and candidate-stereochemistry check
  status: passed
  required: true
  summary: Exact full-key query returns no match; CHEBI:200350 is 2-star and stereospecific
    with a different full InChIKey, so it is not an eligible exact replacement.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  scope_note: This check addresses the inspected current search and candidate, not
    an exhaustive independent export of all ChEBI entries.
  evidence_ids:
  - R-CHEBI-CANDIDATE
  - R-CHEBI-MOL
  - R-CHEBI-SEARCH
- check_id: C-CITED-1995
  name: Exact target in original1995 journal paper
  status: unavailable
  required: true
  summary: Full abstract and database mapping inspected; direct compound-level journal
    content remains unavailable.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - E-PUBMED-1995
  - R-NPA-STORED
  - R-PATENT-ID2
- check_id: C-CITED-2014
  name: Exact-congener biosynthetic experiments and stereochemistry
  status: unavailable
  required: true
  summary: The family-level primary abstract is readable, but main body and SI were
    not obtained. Exact product panels, controls and stereochemical evidence remain
    unknown.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - xcl-pubmed2014-abstract
  - xcl-fulltext-si-unavailable
- check_id: C-IMODULON
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: No Xenorhabdus dataset occurs in the returned catalogue; no biological
    absence conclusion.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-IMODULON-CATALOGUE
evidence:
- evidence_id: R-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml
  locator: Complete owner and resolved mechanism view; exact local inventory rows
    and all history
  accessed_at: '2026-10-21T07:59:44.526501Z'
  support: supports
  summary: This is the shorter acetoxypentyl indole, MIBiG compound 3. Its one species
    occurrence, SS-2004 producer/locus, one NPAtlas cross-reference, classification
    and two seed events were read. No graph, separate pathway, activity, target, clinical
    or sibling-link assertion is present.
  snapshot_sha256: daf800ee8a516270fc5a017ba008cd405efbc16cc0aff79886677617a162faa4
- evidence_id: R-CHEMISTRY
  kind: validation
  reference: /private/tmp/npm-review-work/013/identity/structure-comparison.json
  locator: RDKit complete graph, InChI/key, formula and stereocentre comparisons
  accessed_at: '2026-10-21T07:54:33.166408Z'
  support: supports
  summary: Owner SMILES and InChI regenerate MNIVLQOKRHODTM-UHFFFAOYSA-N, C16H19NO3
    and one unspecified centre at 2-prime. The 4-prime carbon has two equivalent methyl
    groups and is not stereogenic. stereo_complete:false is correct; it does not assert
    a racemate.
  snapshot_sha256: 28b27338a66bfc887a74d786650d91bcc0c10042d2a55aa9c44a7c6007ca3783
- evidence_id: R-NPA-STORED
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA03248?include=classifications
  locator: Complete official API response to the literal stored accession
  accessed_at: '2026-10-21T07:53:26.110040Z'
  support: supports
  summary: The literal NPA03248 request returns HTTP 200 with canonical NPA003248.
    Its full InChI/key and graph match the owner exactly; origin metadata identify
    X. bovienii A2 and DOI:10.1021/np50121a016. No invalid-xref finding follows.
  snapshot_sha256: 461dff1d9fe6fccc0cc6f61788136d96ab87480b783c03e3b4513e7dc9a37c25
- evidence_id: R-NPA-CANONICAL
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA003248?include=classifications
  locator: Complete official response to the returned canonical accession
  accessed_at: '2026-10-21T07:53:26.105388Z'
  support: supports
  summary: The separately requested NPA003248 response is byte-identical to the successful
    stored-ID response. Canonical spelling was verified, not assumed.
  snapshot_sha256: 461dff1d9fe6fccc0cc6f61788136d96ab87480b783c03e3b4513e7dc9a37c25
- evidence_id: R-CHEBI-CANDIDATE
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/200350/
  locator: Current two-star compound entry, explicit InChI stereochemical layer and
    full key
  accessed_at: '2026-10-21T07:53:56.194745Z'
  support: supports
  summary: 'CHEBI:200350 is two-star and specifies the S centre: MNIVLQOKRHODTM-HNNXBMFYSA-N,
    with /t15-/m0/s1. It is not an exact full-key match to the stereo-unspecified
    owner and cannot supply its absolute configuration.'
  snapshot_sha256: 41309fed959eeb06e03cf5820e6ebe33d3217b09607ef7cef03e7d95b88145cf
- evidence_id: R-CHEBI-SEARCH
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search?term=MNIVLQOKRHODTM-UHFFFAOYSA-N&size=100
  locator: Exact full-key official API response body
  accessed_at: '2026-10-21T07:53:56.736864Z'
  support: context_only
  summary: The structured response says no compound matches the supplied complete
    key. This is a bounded current search, not a database-wide independent absence
    audit.
  snapshot_sha256: a8ac626e33f3ff5eeb2d428043e71658da343df1122e6eef488b7f4e946e58eb
  search_scope: Complete key MNIVLQOKRHODTM-UHFFFAOYSA-N in the official ChEBI es_search
    endpoint, size100; structured no-match body inspected.
- evidence_id: R-CHEBI-MOL
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/200350/
  locator: Complete official default molfile, RDKit stereochemical comparison
  accessed_at: '2026-10-21T07:53:56.048351Z'
  support: supports
  summary: The default molfile independently reproduces the stereospecific CHEBI:200350
    full key, distinct from the owner. The shared connectivity prefix does not justify
    grounding to a stereochemically specified term.
  snapshot_sha256: 34f6dea68681fd2269023957cfb86469fd341ca873515f002cac3eab0bbc7550
- evidence_id: E-PUBMED-1995
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=24488732,7561900&retmode=xml
  locator: PubmedArticle PMID 7561900; ArticleId DOI and full AbstractText; original
    source reused after target-specific comparison
  accessed_at: '2026-10-21T07:49:07.390045Z'
  support: partial
  summary: PMID:7561900 maps to DOI:10.1021/np50121a016, Li et al. 1995. Its full
    primary abstract reports indole isolation from X. bovienii A2 but does not name
    individual structures. The exact target-to-paper mapping is supplied by NPAtlas
    as database provenance; the journal compound-level body remains uninspected.
  snapshot_sha256: a3ac05ea8d63ac020ceaaa5fd45a1ed0ce1bee13948e096900dc59d63d3eca99
- evidence_id: E-TAXA
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=40576,406818&retmode=xml
  locator: TaxaSet entries 40576 and 406818, scientific names, ranks, parent and lineage;
    original source reused after target-specific comparison
  accessed_at: '2026-10-21T07:49:07.390300Z'
  support: supports
  summary: NCBITaxon:40576 is species Xenorhabdus bovienii. NCBITaxon:406818 is strain
    Xenorhabdus bovienii SS-2004, directly parented to 40576. Both belong to Bacteria,
    Pseudomonadota, Gammaproteobacteria, Enterobacterales, Morganellaceae. OTHER_BACTERIAL
    is consistent for both; A2 and SS-2004 remain distinct contexts.
  snapshot_sha256: e30e7f63a8a598c81d5de79fe275304036a4144e701d74fb74d1bf9ac4ca249b
- evidence_id: E-WIKIDATA
  kind: authority
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q26307560&props=labels%7Cclaims&languages=en&format=json
  locator: Entity Q26307560 English label and P685 taxon mapping; original source
    reused after target-specific comparison
  accessed_at: '2026-10-21T07:50:13.547545Z'
  support: supports
  summary: Q26307560 resolves to Xenorhabdus bovienii and its P685 statement is 40576,
    agreeing with the occurrence note and NCBI species identity. The later successful
    API retrieval supersedes the initial403 attempt.
  snapshot_sha256: 717159983c1676ff6cb57d6b11425bcf6d58074c6a1cc6b732eb85273fa7af29
- evidence_id: E-GRADE-RULE
  kind: record_content
  reference: docs/HARMONIZATION.md
  locator: Producer versus occurrence section and method-to-producer/locus grading
    table; original source reused after target-specific comparison
  accessed_at: '2026-10-21T07:54:32.791480Z'
  support: supports
  summary: Heterologous expression and enzymatic assays map to SOURCE_ASSERTION for
    the native producer and CLUSTER_DEMONSTRATED for the locus. The owner preserves
    that separation and cites both imported claims as DATABASE_ASSERTION. This rule
    explains extraction; it does not establish compound-specific experiments.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: R-IMODULON-CATALOGUE
  kind: search
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Complete installed kg-microbe-sources datasets response; actual command
    receipt in010/imodulon-context-receipts.json; original source reused after target-specific
    comparison
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The complete returned catalogue has 28 dataset keys; none covers Xenorhabdus.
    No strain-matched structured expression-module query is applicable to this record.
    This is catalogue coverage only and not evidence against xenocyloin production
    or gene activity.
  search_scope: All28 dataset rows returned by the installed read-only runner. Original
    command/result reused; no new network query or independent global database export
    is claimed.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: R-PATENT-ID2
  kind: primary_source
  reference: https://patentimages.storage.googleapis.com/88/ee/a5/deee26bcd7e0de/WO1995003695A1.pdf
  locator: Original WO1995003695A1 printed pp 32-34, Examples 10-11; page images visually
    inspected at 2026-10-21T07:56:13Z
  accessed_at: '2026-10-21T07:55:42.903242Z'
  support: supports
  summary: The patent reports extraction of cell-free X. bovienii broth, naming A2
    or ATCC 35271, and isolation of pure ID2. It explicitly identifies ID2 as the
    acetoxy-methyl-oxopentyl indole and reports proton NMR. The original page actually
    prints M+ 223 alongside a 213 fragment labelled M−60; this internally inconsistent
    mass line is not an OCR-only error and is not used to verify molecular mass. The
    named compound, isolation and NMR support occurrence at unresolved stereochemical
    resolution; no absolute configuration is assigned.
  snapshot_sha256: 80a64cb6cbbd141f11962790dc81c37ac9b7a3e52b5320f67c2d5ea78ee44803
- evidence_id: R-INVENTORY
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Exact BGC0000189:3 row; full-key LOTUS/NPClassifier/ChEBI inventories parsed
    independently of gitignore
  accessed_at: '2026-10-21T07:59:44.526501Z'
  support: supports
  summary: Exact source compound 3 retains the stored structure, NPA03248 and entry-level
    PMID:24488732. The corresponding LOTUS row is species 40576 with DOI:10.1021/NP50121A016
    and Q26307560. NPClassifier gives the exact recorded Alkaloids/Tryptophan alkaloids/Simple
    indole alkaloids, glycoside false. No three-star ChEBI inventory row matches the
    complete key. The implemented source-concept hash recomputes the owner identifier.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: xcl-mibig189-compound3
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000189.4/annotations.json
  locator: Complete v4 JSON; compounds[2] (one-based compound_index 3), taxonomy,
    loci and gene annotations; source-access.json
  accessed_at: '2026-10-21T07:49:07Z'
  support: supports
  summary: The exact recorded connectivity is compound 3, 3-(2-acetoxy-3-oxo-4-methylpentyl)-indole,
    C16H19NO3 and key MNIVLQOKRHODTM-UHFFFAOYSA-N. Its SMILES omits stereochemistry.
    This is the shorter acetylated congener; compound 4 has an extra side-chain carbon,
    while compounds 1/2 bear hydroxy groups. MIBiG lists SS-2004 taxon 406818, FN667741.1:3771005..3779127,
    PKS/Type III and Enzymatic assays plus Heterologous expression. The entry-level
    reference is PMID:24488732; no compound-specific experiment is annotated. The
    source is active, complete and questionable quality. This existing source was
    re-compared to record 013; its original retrieval timestamp is retained. The owner
    faithfully preserves the strain/locus facts and distinguishes SOURCE_ASSERTION
    producer from CLUSTER_DEMONSTRATED locus. The NPAtlas identifier is assessed separately
    by the identity reviewer.
- evidence_id: xcl-pubmed2014-abstract
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/24488732/
  locator: DOI:10.1002/cbic.201300694, title, author list and complete primary abstract;
    official PubMed XML retrieved in source-access.json
  accessed_at: '2026-10-21T07:49:07Z'
  support: partial
  summary: The primary abstract explicitly identifies the xenocyloin cluster in X.
    bovienii SS-2004 and reports heterologous expression and in vitro enzyme characterization.
    It describes XclA as S-selective and XclB/XclC as acylating ketosynthases accepting
    acetyl-, propionyl- or malonyl-CoA. It also reports preferential native production
    by the primary bacterial variant. This corroborates strain and method categories
    at family scope. It does not expose exact acetoxypentyl compound numbering, individual
    enzyme-substrate/product panels, construct details, controls, or exact-congener
    absolute-configuration measurements. No exact-congener assay or stereochemical
    conclusion is inferred from the abstract. The original source-access timestamp
    is reused; this is not a fresh retrieval.
- evidence_id: xcl-native-locus-bridge
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=FN667741.1&db=nuccore&report=genbank&retmode=text&from=3771005&to=3779127
  locator: VERSION, source strain/taxon, full interval CDS annotation; locus.gb
  accessed_at: '2026-10-21T07:49:07Z'
  support: supports
  summary: The 8123-bp interval belongs to X. bovienii SS-2004 with taxon 406818.
    CBJ83019.1/XBJ1_3901 (MIBiG xclA) lies at 3777430..3779127 on the reverse strand,
    and CBJ83018.1/XBJ1_3900 (MIBiG xclB) lies at 3776409..3777440 on the reverse
    strand. The interval also includes CBJ83016.1/XBJ1_3898, annotated as a synthase
    III, but the inspected GenBank annotation alone does not identify it experimentally
    as XclC. These records establish the strain/accession bridge, not full-locus sufficiency
    or historical construct sequences.
- evidence_id: xcl-owner-source-grade
  kind: record_content
  reference: data/natural_products/alkaloids/3-2-acetoxy-3-oxo-4-methylpentyl-indole.yaml;
    data/raw/mibig_compounds.tsv; conf/producer_evidence.tsv
  locator: Full owner read at 2026-10-21T07:54:41Z, re-read at 07:56:11Z; exact local-sources.json
    BGC0000189:3 row and chemistry.json
  accessed_at: '2026-10-21T07:54:41Z'
  support: supports
  summary: The owner is a stereo-incomplete source-defined structure, not an explicitly
    racemic material or stereochemically assigned molecule. The exact shorter pentyl
    graph has one unassigned centre at the acetoxy-bearing 2-prime carbon; 4-prime
    bears two equivalent methyl groups and is not stereogenic. The method map treats
    enzymatic and heterologous evidence as support for the cluster only; it does not
    upgrade native producer evidence to BGC_CHARACTERIZED. The owner applies that
    distinction correctly. No XclA/B/C graph or protein-reference claim is present
    in this target.
- evidence_id: xcl-fulltext-si-unavailable
  kind: search
  reference: https://chemistry-europe.onlinelibrary.wiley.com/doi/abs/10.1002/cbic.201300694
  locator: Public publisher page identifies SI cbic_201300694_sm_miscellaneous_information.pdf;
    attempted full, PDF, suppl/supinfo and normal downloadSupplement routes; bgc-access.json
  accessed_at: '2026-10-21T07:52:30Z'
  support: unknown
  summary: The publisher abstract and SI filename were visible in indexed primary
    content. Both Wiley domains returned HTTP 403 for the exact supplement and full
    text, as did the normal PDF and downloadSupplement routes. The Crossref-listed
    TDM endpoint returned HTTP 400 requiring a TDM client token; no credentials or
    paid service were used. The body and SI were therefore not obtained or inspected.
    Access failure is not evidence that the paper lacks the exact product experiment.
  search_scope: Free public sources only. DOI/title/author and exact SI-filename searches,
    publisher chemistry-europe/onlinelibrary routes, Crossref-provided TDM endpoint,
    OpenAlex article locations and the author-linked MPG.PuRe item were checked. No
    broad claim of literature absence. Search snippets were used as leads, not experimental
    proof.
- evidence_id: xcl-institutional-copy-unavailable
  kind: search
  reference: https://pure.mpg.de/rest/items/item_3369009
  locator: Public author-linked institutional record, complete JSON; bgc-pure-item.json
    and bgc-access.json
  accessed_at: '2026-10-21T07:51:28Z'
  support: unknown
  summary: The author publication list resolves to MPG.PuRe item 3369009. Its complete
    public REST record contains the matching article metadata and abstract, without
    a file/component entry providing the manuscript or supplement. OpenAlex separately
    listed only closed publisher and PubMed locations. This bounded repository check
    supplied no additional experimental text; it does not show that no author copy
    exists elsewhere.
  search_scope: Exact author-linked item3369009 and DOI-matched OpenAlex work; no
    recursive institutional-repository absence claim.
assessments:
- assessment_id: R-EXACT-IDENTITY
  area: identity
  topic: Shorter acetoxypentyl connectivity and declared stereo resolution
  outcome: supported
  summary: The complete owner structure and official NPAtlas structures agree exactly.
    One unspecified centre is represented honestly. The longer acetoxyhexyl congener
    has a different formula/key and two potential stereocentres; its evidence is not
    transferred to this target.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-OWNER
  - R-CHEMISTRY
  - R-NPA-STORED
  - R-NPA-CANONICAL
- assessment_id: R-GROUNDING
  area: grounding
  topic: Minted status and near stereospecific ChEBI candidate
  outcome: supported
  summary: The exact source-concept identifier recomputes. No eligible matching three-star
    row occurs in the fully parsed pinned inventory. Current CHEBI:200350 is two-star
    and a different full stereochemical identity, while the complete-key search returns
    no match. The existing minted rationale is coherent.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-INVENTORY
  - R-CHEBI-CANDIDATE
  - R-CHEBI-MOL
  - R-CHEBI-SEARCH
- assessment_id: R-XREF
  area: identity
  topic: Literal shortened NPAtlas identifier
  outcome: supported
  summary: Stored NPA03248 resolves directly and returns exact NPA003248, verified
    by a separate canonical request with identical bytes. The shortened identifier
    is functional and does not require an invalid-reference finding.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-NPA-STORED
  - R-NPA-CANONICAL
  - R-CHEMISTRY
- assessment_id: R-OCCURRENCE-ORIGIN
  area: evidence
  topic: Exact natural occurrence with primary-source mass discrepancy preserved
  outcome: supported
  summary: The primary patent names and isolates exact ID2 from X. bovienii culture
    broth. This independently corroborates species occurrence and natural origin while
    retaining unresolved stereochemistry. Its printed mass line conflicts internally
    and with the computed 273 molecular mass, so that line is not used as identity
    proof. Source strain A2/ATCC 35271 is not promoted to SS-2004 biosynthetic evidence.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-PATENT-ID2
  - R-CHEMISTRY
  - R-INVENTORY
  - R-NPA-STORED
- assessment_id: R-CITED-1995
  area: evidence
  topic: Exact compound content of the 1995 journal citation
  outcome: unknown
  summary: The DOI and PMID resolve, and NPAtlas explicitly maps this structure to
    the paper. The inspected primary abstract does not identify this individual compound;
    the independent patent is not the journal full text. Exact citation verification
    remains incomplete.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - E-PUBMED-1995
  - R-NPA-STORED
  - R-PATENT-ID2
- assessment_id: R-TAXA
  area: provenance
  topic: Species occurrence versus SS-2004 source producer
  outcome: supported
  summary: NCBI and Wikidata confirm species 40576 and descendant strain 406818. Both
    are OTHER_BACTERIAL. The same species does not equate A2 and SS-2004; occurrence
    remains separate from native producer and locus grading.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - E-TAXA
  - E-WIKIDATA
  - R-INVENTORY
  - R-PATENT-ID2
- assessment_id: R-CLASSIFICATION-HISTORY
  area: provenance
  topic: Computed classification, asserted PKS class and historical seed events
  outcome: supported
  summary: The exact-key classifier output and version match the owner. PKS derives
    separately from the source locus, not from computational natural-product likeness.
    Two seed events and SEEDED status do not claim a prior full scientific review;
    original source concepts are intact.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-OWNER
  - R-INVENTORY
  - xcl-mibig189-compound3
- assessment_id: R-OPTIONAL-SCOPE
  area: scope
  topic: Complete owner without separate mechanism/activity assertions
  outcome: not_applicable
  summary: No optional graph, pathway, quantitative activity, molecular target, clinical
    or sibling-link assertion occurs in the full resolved owner. The complete returned
    iModulon catalogue contains no covered Xenorhabdus dataset. Optional expansion
    is not required, and absent dataset coverage is not negative biological evidence.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - R-OWNER
  - R-IMODULON-CATALOGUE
- assessment_id: xcl-source-and-locus-metadata
  area: evidence
  topic: BGC0000189 compound 3 source, strain and locus mapping
  outcome: supported
  summary: The exact connectivity, SS-2004 taxon, deposited interval, source method
    vocabulary and generated two-claim grading agree with the inspected databases.
    The primary abstract independently corroborates SS-2004 and the reported experimental
    method categories. Neither heterologous expression nor enzymology alone is used
    to upgrade native production.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - xcl-mibig189-compound3
  - xcl-native-locus-bridge
  - xcl-owner-source-grade
  - xcl-pubmed2014-abstract
- assessment_id: xcl-exact-product-assay-scope
  area: evidence
  topic: Exact acetoxypentyl congener in XclA/B/C experiments
  outcome: unknown
  summary: The source database assigns demonstrated locus methods to exact compound
    3, but the accessible primary abstract summarizes the family. Without the full
    body/SI, the exact XclA/B/C preparation, target-product experiment, native chromatogram,
    controls and strain-specific construct details could not be independently adjudicated.
    No contrary experimental result or confirmed owner defect was found; this remains
    a primary-access limitation.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - xcl-mibig189-compound3
  - xcl-pubmed2014-abstract
  - xcl-fulltext-si-unavailable
  - xcl-institutional-copy-unavailable
- assessment_id: xcl-stereochemical-scope
  area: identity
  topic: S-selectivity versus the exact one-centre acetoxypentyl target
  outcome: unknown
  summary: The owner explicitly says stereo_complete:false. This exact pentyl graph
    has only the 2-prime stereocentre; the two equivalent methyl substituents at 4-prime
    preclude a second stereocentre. XclA S-selectivity in the primary abstract does
    not independently establish which exact congeners were stereochemically measured.
    No R/S repair or stereo_complete:true promotion is warranted from the abstract
    alone. The original occurrence and identity are assessed separately in this review.
  target_ids:
  - naturalproductmech:mibig-39ca043bc0
  evidence_ids:
  - xcl-owner-source-grade
  - xcl-pubmed2014-abstract
  - xcl-fulltext-si-unavailable
findings: []
actions: []
limitations:
- The requested 2014 main body and named SI were not accessible through the bounded
  free public routes. Only the complete primary abstract, bibliographic metadata and
  database/locus records were inspected. No full-text or SI experiment is represented
  as read.
- Exact target compound numbering within the 2014 paper, native and heterologous metabolite
  panels, individual XclA/B/C products and controls, expression constructs, assay
  conditions and stereochemical derivatization or comparison methods remain unverified.
- The exact structure is MIBiG compound 3, not a hydroxy congener or the longer hexyl
  congener. Its only potential stereocentre is 2-prime. No congener transfer is used
  to infer exact target stereochemistry or an experimental claim.
- The source PKS/Type III classification is faithfully generated. The abstract describes
  unusual acylating ketosynthases but is insufficient to adjudicate a classification
  repair; no reclassification finding is made.
- Native SS-2004 production is reported at family level in the abstract. The record
  retains SOURCE_ASSERTION; no native knockout, locus necessity or whole-region sufficiency
  is inferred.
- The cited 1995 journal exact-compound body remains uninspected. NPAtlas database
  mapping and independent patent occurrence do not substitute for that citation-level
  check.
- The primary patent printed p33 reports M+ 223 with a 213 M−60 fragment for ID2.
  This contradicts itself and the represented formula; the original page image confirms
  it is not merely an HTML OCR substitution. Its mass line is excluded from independent
  molecular-mass proof, while exact naming/isolation and reported NMR remain positive
  evidence.
- The selected ChEBI candidate is S-specified and only two-star. Its stereochemistry
  is not transferred to an unspecified owner.
- Native source/access receipts for the shared locus, taxon, primary abstracts and
  dataset catalogue are reused with original timestamps after exact-target comparison.
  No new full-text/SI access is claimed.
- The configured full identifier-label gate accepts 499 warning-level taxon-label
  mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus;
  its exit 0 is not independent verification of every identifier or of this record's
  scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison
  because the isolated clone has no sibling checkout, and skips three command-frontmatter
  cases because their parameter sets are empty. Pinned-hash and network governance
  checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants.
  They do not establish biological production, stereochemical specificity, evidence
  adequacy or literature-level claim support.
notes:
- No scientific record or maintained input was edited. This partial observation does
  not promote SEEDED to REVIEWED.
- The optional canonical NPAtlas spelling is a display-consistency opportunity, not
  a demonstrated broken xref. No corrective action is proposed solely from successful
  alias resolution.
- Source-patent mass inconsistency is preserved as a primary-source limitation rather
  than silently corrected or attributed to the YAML owner.
tags:
- path-order-campaign
- batch-002
- xenocyloin
- stereo-incomplete
```
