# 2,3,4,5-Tetrabromopyrrole: strain-specific biosynthetic evidence allocation

- Review: 20261021T072743Z-2-3-4-5-tetrabromopyrrole
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T07:10:08.399174Z
- Finished UTC: 2026-10-21T07:27:43.382066Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact chemical identity, source fusion and the bounded PS5 genetic-production graph are supported. Two confirmed major findings concern separate loci: A757 inherits assays performed with other strains, while PS5 cites an unrelated macrolide review and omits available direct evidence. Maintained, source-pinned corrections should separate those experimental scopes.

## Scope And Provenance

One complete owner and resolved inline mechanism, all five graph nodes/four edges, both source-locus assertions and every remaining field group.

Selection: Ninth unreviewed path in deterministic order from the initial validated list: 91 bundles covered 54 of 3,116 records and 3,062 remained. Ignored bundles were included in coverage counting. This bundle assesses one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-dcee736e16 | data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml | generated | 2,3,4,5-tetrabromopyrrole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema and component validation | passed | True | naturalproductmech:mibig-dcee736e16 | One complete owner with its inline graph validated with zero ERROR rows. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-dcee736e16 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-dcee736e16 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-dcee736e16 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-dcee736e16 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Initial QC attempt before installing the pinned linter | failed | False | naturalproductmech:mibig-dcee736e16 | The first full QC invocation stopped at lint because the isolated copied Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently installed and lint passed on later invocations. |
| QC attempt without network access | failed | False | naturalproductmech:mibig-dcee736e16 | After Ruff installation, QC passed lint and stopped at vendored-sync because sandbox DNS could not reach the pinned public CLAW governance source. Approved network access allowed the next invocation to verify all 22 governed artifacts. |
| QC attempt before restoring the required provenance tag | failed | False | naturalproductmech:mibig-dcee736e16 | QC passed lint, vendored sync, documentation, provenance and source queue, then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a failed archive-content assertion. The tag was subsequently fetched from origin. |
| Targeted verification after restoring the provenance tag | passed | False | naturalproductmech:mibig-dcee736e16 | After restoring the required tag, the exact previously failed gentamicin archive test passed (1 passed). No repository content was edited for this remediation. |
| Diagnosis of the suite skip conditions | passed | False | naturalproductmech:mibig-dcee736e16 | The four observed skip cases were reproduced with pytest skip reasons enabled: the optional sibling AntibioticMech comparison has no sibling checkout in the isolated clone, and three command-frontmatter tests have empty parameter sets. This diagnostic invocation executed no passing tests; it reported four skips. |
| Full repository quality gate after environment repair | passed | True | naturalproductmech:mibig-dcee736e16 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Exact structure and strain-specific primary evidence | passed | True | naturalproductmech:mibig-dcee736e16 | Primary figure confirms exact achiral structure; 2016 text assigns foreign assays separately from A757. Full 2023 PS5 primary text, figure and methods support the bounded native-deletion graph. The cited macrolide review is inspected as an unrelated secondary source. |
| Native protein, other-strain and construct discrimination | passed | True | naturalproductmech:mibig-dcee736e16 | Independent translation and complete sequence comparisons support native PS5 mapping and both named exclusions. |
| Structured expression-source applicability | not_applicable | False | naturalproductmech:mibig-dcee736e16 | Complete returned dataset catalogue contains no Pseudoalteromonas producer dataset. No negative biological inference is made. |

## Scientific And Domain Assessments

### Exact neutral achiral tetrabromopyrrole

identity: supported. Targets: naturalproductmech:mibig-dcee736e16.

The owner matches PubChem CID 4605890 and the primary paper's N-H pyrrole drawing with four carbon-bound bromines. The absence of stereochemical tags is appropriate.

### Chemical equivalence of xref, synonym and two source concepts

identity: supported. Targets: naturalproductmech:mibig-dcee736e16.

Tetrabromopyrrole and 2,3,4,5-tetrabromopyrrole identify the same exact structure here. Both pinned MIBiG source concepts have identical full structures; chemical fusion is supported without conflating their distinct biological claims.

### Minted identity supported by the complete pinned eligible inventory

grounding: supported. Targets: naturalproductmech:mibig-dcee736e16.

No eligible exact match was found in the complete pinned ChEBI inventory, and two current official full-key/name searches explicitly returned no match. Retaining MINTED is supported within those scopes; neither is a universal assertion about every current ChEBI entry.

### Exact native PS5 Bmp2 protein correspondence

grounding: supported. Targets: naturalproductmech:mibig-dcee736e16.

The graph's AKJ75108.1 node and encodes_reference_protein edge are supported by consistent PS5 taxonomy, the precise KR011923.1 CDS coordinates, and independent translation agreement. This establishes reference-locus correspondence; it does not sequence-verify the experimental stock or mutant.

### Other-strain protein and GSH construct correctly excluded

grounding: supported. Targets: naturalproductmech:mibig-dcee736e16.

The 43-residue difference excludes A0A0S2JXW2 as an exact PS5 example; its O-BC30/KCTC 12086 strain equivalence is documented. The GSH extension and conflicting taxonomy justify excluding A0A140UHM3 as the native reference. The historical bounded UniProt-query wording is not expanded into a global absence claim.

### Five-node/four-edge genetic production graph

evidence: supported. Targets: naturalproductmech:mibig-dcee736e16.

The bmp2 deletion, its gene target, loss of detected production and TBP product identity are supported by primary text, figure and methods. The protein edge is explicitly a native-reference mapping and is checked separately against public sequences. The graph correctly avoids direct enzyme catalysis, universal absence, rescue, quantitative yield or pure-compound activity claims.

### Historical evidence-access notes and current independent inspection

provenance: supported. Targets: naturalproductmech:mibig-dcee736e16.

The existing graph records that its original curator inspected extracted main text only. That historical statement is not contradicted by the present review’s successful figure and supplement retrieval. Prior evidence dates and the bounded curation event are preserved; no full-record sign-off is implied.

### Computed classification and source identity merge

provenance: supported. Targets: naturalproductmech:mibig-dcee736e16.

The exact-key NPClassifier inventory supports Alkaloids with empty superclass/class arrays at the recorded model version. Those empty outputs are faithfully preserved. Two source labels describe the same achiral tetrabromopyrrole connectivity; source-specific strain/locus claims remain distinct and are assessed separately.

### Other complete-owner assertions and component boundary

scope: not_applicable. Targets: naturalproductmech:mibig-dcee736e16.

The full resolved owner has no external graph components or other optional pathway, molecular-target, quantitative-assay or clinical assertions. The inline graph is explicitly included in scope; absent optional fields alone are not defects.

### Structured expression-source applicability

scope: not_applicable. Targets: naturalproductmech:mibig-dcee736e16.

No covered organism/dataset in the returned iModulonDB list matches the two producer strains. The primary genetic and biochemical evidence is assessed independently.

### Exact product, source fusion and strain/accession mapping

grounding: supported. Targets: naturalproductmech:mibig-dcee736e16.

Both MIBiG source concepts describe the same achiral exact compound, and native product evidence is reported for both strains. Combining the structure while retaining separate loci/producers is justified. KT808878.1 specifically denotes A757 and KR011923.1 PS5; the two evidence allocations must remain separate. OTHER is consistent with the nonmodular pathway.

### A757 exact-locus assay applicability

evidence: concern. Targets: naturalproductmech:mibig-dcee736e16.

The cited paper supports native A757 TBP detection and a homologous locus, but its direct tests use other organisms. CLUSTER_DEMONSTRATED and both inherited methods overstate this exact accession. Retain the native producer assertion and qualify the locus as homology-based unless additional strain-specific experiments are inspected.

### PS5 primary citation and demonstrated native locus

evidence: concern. Targets: naturalproductmech:mibig-dcee736e16.

The unrelated macrolide review should be replaced at the claim level. PS5 has a demonstrated locus by heterologous expression and native knockout; the latter supports the native producer grade. Current ungraded metadata conflicts with evidence already cited in its own bounded graph.

## Findings

### bgc-a757-methods-misallocated: A757 inherits direct assay methods performed with PS5 and Marinomonas proteins

major / open / confirmed; issue key: mibig-bgc0001463-compound1-strain-specific-link-evidence.

The source-pinned A757 locus KT808878.1 is graded experimentally demonstrated using methods whose cited experiments used PS5 genes or M. mediterranea proteins. A757 production and pathway homology remain supported, but the native A757 proteins are not sequence-identical to PS5. This is a strain-specific evidence-scope error, not a denial of native occurrence or a wrong compound fusion.

### bgc-ps5-reference-and-grade: PS5 producer and locus cite an unrelated review and omit inspected direct evidence

major / open / confirmed; issue key: mibig-bgc0001464-compound1-reference-and-native-link-evidence.

Both PS5 claims cite a rare-actinomycete macrolide review selected from source bioactivity metadata. Correct primary studies support the exact PS5 product and locus, including native deletion evidence already represented in the record graph. Correcting citation routing and source-pinned methods together resolves this claim-support gap and inconsistent grading.

## Recommended Actions And Acceptance Checks

### correct-a757-strain-scope

For BGC0001463:1 version 4 maintain a pinned REPLACE locus override with Homology-based prediction, with DOI:10.1073/pnas.1519695113 scoped to the A757 homologous cluster and native detection. Generate CLUSTER_PREDICTED and retain SOURCE_ASSERTION for the native taxon. Explain the separately assayed PS5 and Marinomonas systems. Preserve source audit metadata and do not relabel those foreign proteins as A757.

- Pair every REPLACE method override with a mibig_claim_references.tsv row pinned by the exact raw source-row SHA256. The current REPLACE loader does not enforce expected_* fields itself; the paired claim-reference loader must fail on source-row drift. If no paired reference row is appropriate, extend the method loader to enforce equivalent pins before relying on them.
- Exact version/accession/taxon/structure and original methods are pinned; only BGC0001463:1 changes.
- A757 producer remains supported; locus wording distinguishes homology from direct assays.
- Run target seed-canary, inspect generated diff, then documented regeneration and strict validation, verify-reproduction, verify-corpus --summary and qc.

### correct-ps5-primary-support

For BGC0001464:1 version 3 add pinned claim references to DOI:10.1073/pnas.1519695113 for heterologous locus sufficiency and DOI:10.1038/s43705-023-00309-6 for native PS5 deletion/production. Replace methods with Heterologous expression and Knock-out studies, yielding CLUSTER_DEMONSTRATED and BGC_CHARACTERIZED. Remove the unrelated review as support for these claims while preserving source provenance. Keep the graph’s bounded native deletion interpretation and distinct native reference protein.

- Pair every REPLACE method override with a mibig_claim_references.tsv row pinned by the exact raw source-row SHA256. The current REPLACE loader does not enforce expected_* fields itself; the paired claim-reference loader must fail on source-row drift. If no paired reference row is appropriate, extend the method loader to enforce equivalent pins before relying on them.
- Use BGC0001464:1 source identity and its alias minted identifier when pinning, preserving merged owner naturalproductmech:mibig-dcee736e16.
- Native knockout is limited to tested conditions; no Bmp2-alone catalytic sufficiency or rescue claim is introduced.
- Both producer and locus references resolve to inspected primary PS5 evidence, and the merged structure and separate A757 claim remain intact.
- Run target seed-canary, inspect generated diff, then documented regeneration and strict validation, verify-reproduction, verify-corpus --summary and qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-IDENTITY-LOCAL | data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml; Complete owner; identity, synonym, fused source_concepts and complete inline graph | supports | The owner encodes neutral achiral 2,3,4,5-tetrabromopyrrole, synonymous here with tetrabromopyrrole. The inline graph separately grounds the native PS5 reference Bmp2 to AKJ75108.1 and excludes a differing strain protein and a tagged construct. |
| E-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/4605890/property/InChI,InChIKey,IsomericSMILES,IUPACName/JSON; PropertyTable.Properties[0] | supports | CID 4605890 exactly matches the record SMILES, InChI and full key MIIWISWSCMVZHG-UHFFFAOYSA-N. Its systematic name is 2,3,4,5-tetrabromo-1H-pyrrole. |
| E-SYNONYM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/4605890/synonyms/JSON; InformationList.Information[0].Synonym | supports | The exact CID includes tetrabromopyrrole as a synonym; the short label is not evidence of a different compound. |
| E-CHEMISTRY-IDENTITY | /private/tmp/npm-review-work/009/chemistry.json; RDKit 2026.03.5 result generated 2026-10-21T07:10:09.458812Z; complete result inspected | supports | The SMILES regenerates the exact stored InChI/key, neutral formula C4HBr4N and exact mass 378.684247432. It contains no tetrahedral stereocentre; stereo_complete is appropriate for this achiral aromatic structure. |
| E-SOURCE-FUSION | /private/tmp/npm-review-work/009/local-sources.json; Both complete mibig_compounds rows, BGC0001463 v4 and BGC0001464 v3 | supports | The two pinned MIBiG source concepts have the identical complete SMILES, InChI and key. Their different compound labels resolve to the same PubChem identity. This supports chemical fusion without merging producer or locus evidence. |
| E-PRIMARY-CHEMICAL-FIGURE | https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs43705-023-00309-6/MediaObjects/43705_2023_309_Fig1_HTML.png; DOI 10.1038/s43705-023-00309-6, Figure 1A, visually inspected | supports | The primary figure depicts TBP as a pyrrole N-H ring brominated at all four carbon positions, exactly matching the owner connectivity and substitution pattern. |
| E-GROUNDING-SEARCH | data/raw/chebi_structures.tsv; Complete pinned eligible inventory, full connectivity prefix and compound-name stem | supports | No row matches MIIWISWSCMVZHG or tetrabromopyrrole in the complete pinned eligible ChEBI inventory. |
| E-GROUNDING-POLICY | docs/HARMONIZATION.md; Unambiguous three-star ChEBI default-structure rule | supports | Automatic ChEBI grounding requires an unambiguous matching three-star default structure. |
| E-PS5-NUCLEOTIDE | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KR011923.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; LOCUS, source feature, bmp2 CDS and ORIGIN | supports | KR011923.1 is a 6705-base PS5 pyrrole cluster, taxon 1437473. Its plus-strand bmp2 CDS is 2810..4030, codon_start 1, translation table 11, protein AKJ75108.1. It is a cluster sequence, not a complete genome. |
| E-PS5-PROTEIN | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AKJ75108.1&amp;db=protein&amp;report=genpept&amp;retmode=text; LOCUS, source, CDS coded_by and complete ORIGIN | supports | AKJ75108.1 is a 406-residue conceptual Bmp2 translation from Pseudoalteromonas sp. PS5, taxon 1437473. Its coded_by field is KR011923.1:2810..4030, table 11. |
| E-UNIPROT-OTHER-STRAIN | https://rest.uniprot.org/uniprotkb/A0A0S2JXW2.json; organism, sequence and EMBL cross-reference | supports | A0A0S2JXW2 is an unreviewed 406-residue Pseudoalteromonas phenolica protein, taxon 161398, linked to ALO40986.1 on CP013187. Its complete sequence differs from native PS5 Bmp2. |
| E-UNIPROT-CONSTRUCT | https://rest.uniprot.org/uniprotkb/A0A140UHM3.json; organism, sequence and PDB cross-reference | supports | A0A140UHM3 is an unreviewed 409-residue sequence linked to PDB 5BVA. It carries Streptomyces taxon 1883 and comprises GSH followed by the entire native PS5 sequence. It is not an exact native PS5 reference protein. |
| E-OTHER-STRAIN-REFERENCE | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=ALO40986.1&amp;db=protein&amp;report=genpept&amp;retmode=text; source, CDS and complete protein ORIGIN | supports | The UniProt-linked ALO40986.1 sequence is annotated Pseudoalteromonas phenolica KCTC 12086, taxon 161398, locus PP2015_463 on CP013187.1. It is distinct from the PS5 reference. |
| E-OTHER-STRAIN-ALIAS | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=21460; Culture provenance and equivalent strain numbers; genome CP013187 | supports | The JCM type-strain catalogue explicitly connects O-BC30 to IAM 14989/JCM 21460 and KCTC 12086, and links genome CP013187. This validates the record's O-BC30 wording for the alternative protein. |
| E-PROTEIN-EQUIVALENCE | /private/tmp/npm-review-work/009/protein-equivalence.json; Independent DNA translation and complete sequence comparisons | supports | Translation of the 1221-nt plus-strand CDS, ATG through terminal TAA using table 11, gives 406 residues with no internal stop and exactly matches both GenBank annotation and independently retrieved GenPept ORIGIN. Native SHA256 is 2bc3ab09a447bbca0efcbd70119a5cadd3273bf3b5d9ea97efc2d1a3bcbc7e92. A0A0S2JXW2 differs at exactly 43 positions; A0A140UHM3 equals GSH plus native PS5 Bmp2. |
| E-CHEBI-LIVE-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=MIIWISWSCMVZHG-UHFFFAOYSA-N&amp;size=100; Official documented public es_search endpoint; parsed JSON response with HTTP 404 | context_only | The service explicitly reports no compound matching this query term. This is a bounded search result, not an inaccessible page or universal ontology absence. |
| E-CHEBI-LIVE-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=tetrabromopyrrole&amp;size=100; Official documented public es_search endpoint; parsed JSON response with HTTP 404 | context_only | The service explicitly reports no compound matching this query term. This is a bounded search result, not an inaccessible page or universal ontology absence. |
| R-LOCAL | data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml; Complete owner and resolved read_natural_product view, all five graph nodes/four edges, source rows and seed transform | supports | The record combines two exact-structure MIBiG source concepts, two producer/locus claims, one chemical xref and one curator-owned five-node/four-edge PS5 genetic-production graph. It has no occurrences, separate pathway steps, molecular targets, quantitative assays or clinical assertions. Its open source-fusion discussion and SEEDED status are explicit. Two seed events precede one bounded graph curation event; the seeder carries graph fields across unchanged-structure regeneration. |
| R-GRAPH-PRIMARY | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=10509201&amp;retmode=xml; DOI:10.1038/s43705-023-00309-6; full primary body P3 and Figure 1B/D caption | supports | The study reports an in-frame bmp2 deletion in PS5, with loss of detected TBP production in the mutant under the tested culture conditions. The caption ties the reference cluster to KR011923 and describes three replicate culture extractions. This directly supports the graph’s genetic production context, not Bmp2-alone catalytic sufficiency. |
| R-GRAPH-FIGURE | https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs43705-023-00309-6/MediaObjects/43705_2023_309_Fig1_HTML.png; Figure 1B and 1D; full figure independently viewed in this review | supports | Panel B marks bmp2 within the PS5 cluster. Panel D shows three wild-type production observations and three mutant observations at baseline, agreeing with the limited production-loss edge. The graph does not adopt quantitative concentrations or the separate coral-response panel. |
| R-GRAPH-METHODS | https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs43705-023-00309-6/MediaObjects/43705_2023_309_MOESM1_ESM.docx; Supplement: Generation of bmp2 knockout strain; LC-MS/MS methods; Tables S3 and S5 | supports | Methods describe homologous-recombination deletion construction and Sanger confirmation of the plasmid. Triplicate five-millilitre cultures were extracted for LC-MS/MS using synthetic TBP calibration. Strain NJS602 is the PS5 deletion mutant. These details support the bounded experiment; reference correspondence is not independent sequencing of the final mutant stock. |
| R-IMODULON-COVERAGE | https://imodulondb.org/api/datasets; Installed kg-microbe-sources imodulondb datasets, exit 0; complete returned table inspected | context_only | The complete adapter dataset list contains no Pseudoalteromonas species or PS5/A757 dataset. Pseudomonas datasets are a different genus and are not substituted. No expression-module evidence is used to judge this compound or graph. |
| R-OVERRIDE-GUARD | src/naturalproductmech/curate/claim_references.py; load_claim_references, reconciled with scripts/seed_from_sources.py load_mibig_locus_evidence_overrides | context_only | Claim-reference corrections enforce an exact raw source-row SHA256. Method REPLACE rows currently do not enforce expected_* context fields; WITHDRAW rows do. Proposed REPLACE actions therefore require a paired pinned citation row or an explicit loader extension before relying on source-drift guards. |
| bgc-source1463 | https://mibig.secondarymetabolites.org/repository/BGC0001463.4/annotations.json; complete version 4 entry: compound, taxonomy, locus, evidence and legacy references | partial | Source compound 1 has the exact target structure, taxon 43662, KT808878.1 and methods Enzymatic assays and Heterologous expression. Its compound-level MS/MS reference is DOI:10.1073/pnas.1519695113. Status active and OTHER class are reproduced. The database assertion does not itself establish that each experiment used this strain. |
| bgc-source1464 | https://mibig.secondarymetabolites.org/repository/BGC0001464.3/annotations.json; complete version 3 entry: compound, taxonomy, locus, bioactivity and legacy references | partial | Source compound 1 has the same exact structure, PS5 taxon 1437473 and KR011923.1 but no stated locus methods. Legacy reference PMID:27001835 is relevant primary biosynthesis work. The compound bioactivity list includes DOI:10.1016/j.ijantimicag.2022.106523; automatic selection of that item does not make it evidence for this producer/locus. |
| bgc-a757-deposit | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KT808878.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; source feature, VERSION, bmp1-4 CDS features | supports | The 6707 bp cluster deposit belongs to Pseudoalteromonas piscicida strain A757, taxon 43662. Its Bmp1-4 accessions are AME30284.1 through AME30287.1. This is a cluster sequence, not a complete genome. Species-level wording in the record omits the experimentally named strain but maps to the deposit. |
| bgc-ps5-deposit | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KR011923.1&amp;db=nuccore&amp;report=genbank&amp;retmode=text; source feature, VERSION, bmp1-4 CDS; reused official file ps5-genbank.gb | supports | The 6705 bp deposit is PS5/taxon 1437473; Bmp1-4 are AKJ75107.1 through AKJ75110.1. Reused original access time. On 07:15Z the reviewer compared the complete annotated translations with A757: all four differ; for example Bmp2 is 406 aa in both and differs at 20 aligned positions. Assay applicability cannot be rescued by claiming these are identical proteins. |
| bgc-primary2016-strain-experiments | https://pmc.ncbi.nlm.nih.gov/articles/PMC4833250/; DOI:10.1073/pnas.1519695113; Results, Genetic Basis for the Biosynthesis of 1 and in vitro reconstitution; Fig 2; Database Deposition Information | partial | Primary main text assigns heterologous expression to PS5_bmp1-4 and purified-enzyme reconstitution to Marinomonas mediterranea MMB-1 Bmp1-4. A757 has native extract detection of exact TBP plus a homologous cluster. The deposition statement maps PS5 to KR011923 and A757 to KT808878. Thus the two recorded strains share the product but not the experimental method allocation. |
| bgc-primary2023-native-ps5 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=10509201&amp;retmode=xml; DOI:10.1038/s43705-023-00309-6; main text PS5 bmp2 deletion paragraph and Figure 1B/D; reused graph-primary.xml | supports | Inspected primary text reports native PS5 in-frame bmp2 deletion with complete loss of detected TBP, and Figure 1B names KR011923. This supports native producer and locus necessity under the tested culture/LC-MS/MS conditions. It does not establish Bmp2-alone catalysis, universal production conditions or complementation. Reused original access; applicability checked for this target. |
| bgc-wrong-macrolide-reference | https://purehost.bath.ac.uk/ws/portalfiles/portal/228298369/1_s2.0_S0924857922000139_main.pdf; Published secondary-review identity and full extracted scope; not a primary biosynthesis experiment. author-hosted 49-page review, title, abstract and full extracted text searches for tetrabrom/Pseudoalteromonas/PS5 | refutes | DOI:10.1016/j.ijantimicag.2022.106523 resolves to Macrolides from rare actinomycetes: Structures and bioactivities. Its stated scope is rare-actinomycete macrolides, not a PS5 genetic experiment; full extracted text searches return no tetrabrom, Pseudoalteromonas or PS5 match. This is an irrelevant citation for the two PS5 biosynthetic claims. The conclusion uses inspected scope and text, not title alone. |
| bgc-current-allocation | data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml; data/raw/mibig_compounds.tsv; conf/producer_evidence.tsv; full owner, exact source rows and method-grading table | partial | Owner contains two distinct producer/locus objects merged by the same exact structure. A757 inherits strong locus methods; PS5 inherits no methods and an unrelated bioactivity reference. Existing PS5 causal graph already cites the 2023 native deletion. The grading table maps Homology-based prediction to CLUSTER_PREDICTED and Knock-out studies to BGC_CHARACTERIZED plus CLUSTER_DEMONSTRATED. |

## Limits And Additional Notes

- The live official ChEBI search returned explicit no-match responses for two bounded queries, exact full key and tetrabromopyrrole. Together with the complete pinned eligible inventory this supports current minted grounding; it is not a universal assertion about every ontology synonym or representation.
- Protein sequence correspondence concerns public reference records. Experimental-stock sequence identity, mutant junctions, catalytic activity and complementation are not established by this comparison.
- The historical bounded UniProt query was not rerun or generalized. Both named alternative entries were directly inspected and compared instead.
- The existing graph is deliberately limited to a genetic production context. This review does not reconstruct deletion junctions from raw sequencing, exclude all off-target changes, infer a rescue experiment, or independently reanalyse chromatographic raw data.
- The original curator’s access notes are historical provenance. Newly inspected figures and supplementary methods support the current review without rewriting those earlier observations.
- PNAS direct PMC pages were challenged and official efetch returned metadata only. The primary main text was inspected through the web index, including the explicit organism assignments and deposit statement; the supporting PDF route returned a browser challenge. No uninspected supporting-table claim is made.
- The 2023 full XML and reference GenBank file were reused with original access timestamps from this record’s root review. The root separately inspected the 2023 figure and supplementary methods; this packet independently uses the main text and caption.
- No universal absence of an A757-specific later experiment is asserted. The confirmed defect is that the existing cited study does not supply the inherited exact-strain assays.
- The two findings concern different source-locus objects: an overgraded A757 experiment allocation and a PS5 citation/evidence routing gap. No identity, source-fusion or inline-graph error is inferred.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific owner, source inventory, component, native status or seed history was edited.
- The PS5 graph is positively supported despite source-level citation and grading defects. The two producer/locus objects retain separate experimental scopes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072743Z-2-3-4-5-tetrabromopyrrole
kind: record
repository: CultureBotAI/NaturalProductMech
title: '2,3,4,5-Tetrabromopyrrole: strain-specific biosynthetic evidence allocation'
started_at: '2026-10-21T07:10:08.399174Z'
finished_at: '2026-10-21T07:27:43.382066Z'
reviewer:
  identity: Codex
  kind: agent
  independence: independent
  independence_basis: This team did not author or modify the selected scientific owner
    or its maintained inputs. Parallel source inspections were reconciled into one
    target review; no independent human sign-off is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Exact chemical identity, source fusion and the bounded PS5 genetic-production
  graph are supported. Two confirmed major findings concern separate loci: A757 inherits
  assays performed with other strains, while PS5 cites an unrelated macrolide review
  and omits available direct evidence. Maintained, source-pinned corrections should
  separate those experimental scopes.'
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
  - path: data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml
    sha256: 44c21d0e976ed13b7e3afe5b2bfaaf4b17ab8a3d33ce7bead36a79226b9b6c6e
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
  description: One complete owner and resolved inline mechanism, all five graph nodes/four
    edges, both source-locus assertions and every remaining field group.
  selection: 'Ninth unreviewed path in deterministic order from the initial validated
    list: 91 bundles covered 54 of 3,116 records and 3,062 remained. Ignored bundles
    were included in coverage counting. This bundle assesses one target.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-dcee736e16
targets:
- target_id: naturalproductmech:mibig-dcee736e16
  path: data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml
  label: 2,3,4,5-tetrabromopyrrole
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
    role: CyanoMetDB exact structure occurrence source
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated owner transform
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml
    role: Curator-owned inline causal graph and curation history carried across seeding
checks:
- check_id: C-STRICT
  name: Closed-schema and component validation
  status: passed
  required: true
  summary: One complete owner with its inline graph validated with zero ERROR rows.
  command: just validate-strict data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml
    --out /private/tmp/npm-review-work/009/strict.tsv
  exit_code: 0
  target_ids:
  - naturalproductmech:mibig-dcee736e16
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned
    filing pathways.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-corpus
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016808Z; finished 2026-10-21T06:37:52.997020Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-corpus.log.'
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3,116 records are byte-identical to the seeder output from committed
    inventories and maintained curation inputs.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just verify-reproduction
    --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016703Z; finished 2026-10-21T06:38:35.570687Z. Exact
    session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.'
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The documented exhaustive queue command produced 8,928 diagnostic rows
    in 12 queues; deterministic queue output does not establish scientific review.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just review-queue
    --tsv /private/tmp/npm-review-queue-initial.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:36.016598Z; finished 2026-10-21T06:37:11.018366Z. Exact
    session transcript: /private/tmp/npm-native-checks/review-queue.log.'
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Full configured gate passed using existing CHEBI and GO caches plus the
    committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35
    documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because
    their prefixes have no adapter.'
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.498212Z; finished 2026-10-21T06:38:54.776253Z. Exact
    session transcript: /private/tmp/npm-native-checks/validate-products.log.'
- check_id: qc-environment-attempt1
  name: Initial QC attempt before installing the pinned linter
  status: failed
  required: false
  summary: The first full QC invocation stopped at lint because the isolated copied
    Python environment lacked Ruff. Exact uv.lock version Ruff 0.16.6 was subsequently
    installed and lint passed on later invocations.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:36:56.497107Z; finished 2026-10-21T06:36:56.918133Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc.log.'
- check_id: qc-network-attempt2
  name: QC attempt without network access
  status: failed
  required: false
  summary: After Ruff installation, QC passed lint and stopped at vendored-sync because
    sandbox DNS could not reach the pinned public CLAW governance source. Approved
    network access allowed the next invocation to verify all 22 governed artifacts.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:37:57.661447Z; finished 2026-10-21T06:37:59.874785Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt2.log.'
- check_id: qc-tag-attempt3
  name: QC attempt before restoring the required provenance tag
  status: failed
  required: false
  summary: 'QC passed lint, vendored sync, documentation, provenance and source queue,
    then stopped at tests: 998 passed, 1 failed, 4 skipped. The sole failure was the
    isolated clone lacking refs/tags/review-base/gentamicin-20261013; it was not a
    failed archive-content assertion. The tag was subsequently fetched from origin.'
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 1
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:38:17.713062Z; finished 2026-10-21T06:45:43.079802Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt3.log.'
- check_id: qc-tag-remediation
  name: Targeted verification after restoring the provenance tag
  status: passed
  required: false
  summary: After restoring the required tag, the exact previously failed gentamicin
    archive test passed (1 passed). No repository content was edited for this remediation.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    tests/test_gentamicin_review_archive.py::test_gentamicin_archive_and_scoped_dispositions
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:45:52.383490Z; finished 2026-10-21T06:45:54.030116Z. Exact
    session transcript: /private/tmp/npm-native-checks/gentamicin-tag-check.log.'
- check_id: qc-skip-diagnosis
  name: Diagnosis of the suite skip conditions
  status: passed
  required: false
  summary: 'The four observed skip cases were reproduced with pytest skip reasons
    enabled: the optional sibling AntibioticMech comparison has no sibling checkout
    in the isolated clone, and three command-frontmatter tests have empty parameter
    sets. This diagnostic invocation executed no passing tests; it reported four skips.'
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just test -q
    -rs tests/test_schema.py::test_shared_mech_modules_are_byte_identical_to_the_fleet
    tests/test_skill_frontmatter.py::test_command_frontmatter_has_no_duplicate_keys
    tests/test_skill_frontmatter.py::test_command_frontmatter_is_valid_yaml tests/test_skill_frontmatter.py::test_command_declares_a_usable_description
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:30.259937Z; finished 2026-10-21T06:46:31.251048Z. Exact
    session transcript: /private/tmp/npm-native-checks/skipped-tests-diagnosis.log.'
- check_id: shared-qc
  name: Full repository quality gate after environment repair
  status: passed
  required: true
  summary: 'The full documented just qc recipe passed after installing the pinned
    linter, allowing the read-only governance fetch, and restoring the required provenance
    tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116
    records and zero errors. Documentation, provenance, source queue, governed artifacts,
    generated pages, reproduction, filing integrity and corpus reporting all passed.'
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Shared read-only baseline over the isolated clone at /private/tmp/npm-record-reviews-20261021.
    Started 2026-10-21T06:46:02.058886Z; finished 2026-10-21T06:54:53.950582Z. Exact
    session transcript: /private/tmp/npm-native-checks/qc-attempt4.log.'
- check_id: C-PRIMARY-SCOPE
  name: Exact structure and strain-specific primary evidence
  status: passed
  required: true
  summary: Primary figure confirms exact achiral structure; 2016 text assigns foreign
    assays separately from A757. Full 2023 PS5 primary text, figure and methods support
    the bounded native-deletion graph. The cited macrolide review is inspected as
    an unrelated secondary source.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-PRIMARY-CHEMICAL-FIGURE
  - bgc-primary2016-strain-experiments
  - R-GRAPH-PRIMARY
  - R-GRAPH-FIGURE
  - R-GRAPH-METHODS
  - bgc-wrong-macrolide-reference
- check_id: C-PROTEIN
  name: Native protein, other-strain and construct discrimination
  status: passed
  required: true
  summary: Independent translation and complete sequence comparisons support native
    PS5 mapping and both named exclusions.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-PROTEIN-EQUIVALENCE
  - E-OTHER-STRAIN-ALIAS
- check_id: C-IMODULON
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: Complete returned dataset catalogue contains no Pseudoalteromonas producer
    dataset. No negative biological inference is made.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - R-IMODULON-COVERAGE
evidence:
- evidence_id: E-IDENTITY-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml
  locator: Complete owner; identity, synonym, fused source_concepts and complete inline
    graph
  accessed_at: '2026-10-21T07:12:47Z'
  support: supports
  summary: The owner encodes neutral achiral 2,3,4,5-tetrabromopyrrole, synonymous
    here with tetrabromopyrrole. The inline graph separately grounds the native PS5
    reference Bmp2 to AKJ75108.1 and excludes a differing strain protein and a tagged
    construct.
  snapshot_sha256: 44c21d0e976ed13b7e3afe5b2bfaaf4b17ab8a3d33ce7bead36a79226b9b6c6e
- evidence_id: E-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/4605890/property/InChI,InChIKey,IsomericSMILES,IUPACName/JSON
  locator: PropertyTable.Properties[0]
  accessed_at: '2026-10-21T07:12:57Z'
  support: supports
  summary: CID 4605890 exactly matches the record SMILES, InChI and full key MIIWISWSCMVZHG-UHFFFAOYSA-N.
    Its systematic name is 2,3,4,5-tetrabromo-1H-pyrrole.
  snapshot_sha256: 48e1b6364fe6c8e85c395fd2c9147b2a53780282fe4ad6d9bb3a5a35427620b7
- evidence_id: E-SYNONYM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/4605890/synonyms/JSON
  locator: InformationList.Information[0].Synonym
  accessed_at: '2026-10-21T07:12:57Z'
  support: supports
  summary: The exact CID includes tetrabromopyrrole as a synonym; the short label
    is not evidence of a different compound.
  snapshot_sha256: d47253e937f99ac80e125ae4315523aac0879e0f4bd292bbbbe86c903fcfbfd5
- evidence_id: E-CHEMISTRY-IDENTITY
  kind: validation
  reference: /private/tmp/npm-review-work/009/chemistry.json
  locator: RDKit 2026.03.5 result generated 2026-10-21T07:10:09.458812Z; complete
    result inspected
  accessed_at: '2026-10-21T07:12:47Z'
  support: supports
  summary: The SMILES regenerates the exact stored InChI/key, neutral formula C4HBr4N
    and exact mass 378.684247432. It contains no tetrahedral stereocentre; stereo_complete
    is appropriate for this achiral aromatic structure.
  snapshot_sha256: e29a2be24841e2f9d9a0a1115362c293836e43e9ac4787eaa21b4a778743084b
- evidence_id: E-SOURCE-FUSION
  kind: record_content
  reference: /private/tmp/npm-review-work/009/local-sources.json
  locator: Both complete mibig_compounds rows, BGC0001463 v4 and BGC0001464 v3
  accessed_at: '2026-10-21T07:14:27Z'
  support: supports
  summary: The two pinned MIBiG source concepts have the identical complete SMILES,
    InChI and key. Their different compound labels resolve to the same PubChem identity.
    This supports chemical fusion without merging producer or locus evidence.
  snapshot_sha256: fffd58e76ab7e3f524143e6732f18adeb2c506c0e408ed226d00f9f789d17065
- evidence_id: E-PRIMARY-CHEMICAL-FIGURE
  kind: primary_source
  reference: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs43705-023-00309-6/MediaObjects/43705_2023_309_Fig1_HTML.png
  locator: DOI 10.1038/s43705-023-00309-6, Figure 1A, visually inspected
  accessed_at: '2026-10-21T07:12:24.478454Z'
  support: supports
  summary: The primary figure depicts TBP as a pyrrole N-H ring brominated at all
    four carbon positions, exactly matching the owner connectivity and substitution
    pattern.
  snapshot_sha256: 1bb793c55fcee74c361a3635fd29e7e7276706f40cacf4f26170b6e63b0fc86c
- evidence_id: E-GROUNDING-SEARCH
  kind: search
  reference: data/raw/chebi_structures.tsv
  locator: Complete pinned eligible inventory, full connectivity prefix and compound-name
    stem
  accessed_at: '2026-10-21T07:12:57Z'
  support: supports
  summary: No row matches MIIWISWSCMVZHG or tetrabromopyrrole in the complete pinned
    eligible ChEBI inventory.
  search_scope: Searched the entire explicitly named inventory with rg --no-ignore
    --hidden for MIIWISWSCMVZHG and tetrabromopyrrole. Ignored files were included;
    no matching row was returned. Live official full-key and exact-name searches were
    later resolved separately; neither source is treated as universal ontology absence.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: E-GROUNDING-POLICY
  kind: authority
  reference: docs/HARMONIZATION.md
  locator: Unambiguous three-star ChEBI default-structure rule
  accessed_at: '2026-10-21T06:45:28Z'
  support: supports
  summary: Automatic ChEBI grounding requires an unambiguous matching three-star default
    structure.
  snapshot_sha256: c372a0f299e50152641500e0f6966e403ed34624a6c4cee58aa955b1ca320a79
- evidence_id: E-PS5-NUCLEOTIDE
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KR011923.1&db=nuccore&report=genbank&retmode=text
  locator: LOCUS, source feature, bmp2 CDS and ORIGIN
  accessed_at: '2026-10-21T07:11:45.171190Z'
  support: supports
  summary: KR011923.1 is a 6705-base PS5 pyrrole cluster, taxon 1437473. Its plus-strand
    bmp2 CDS is 2810..4030, codon_start 1, translation table 11, protein AKJ75108.1.
    It is a cluster sequence, not a complete genome.
  snapshot_sha256: e7174d0e59a821b9f980a8fba7e2454ca14ecde4e11ea2573815560ba49285df
- evidence_id: E-PS5-PROTEIN
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AKJ75108.1&db=protein&report=genpept&retmode=text
  locator: LOCUS, source, CDS coded_by and complete ORIGIN
  accessed_at: '2026-10-21T07:11:45.171327Z'
  support: supports
  summary: AKJ75108.1 is a 406-residue conceptual Bmp2 translation from Pseudoalteromonas
    sp. PS5, taxon 1437473. Its coded_by field is KR011923.1:2810..4030, table 11.
  snapshot_sha256: 2578ec20f0267f43f3e1da74c0ae873fe80d52c06d202c2d275b1b8e0cc0d10e
- evidence_id: E-UNIPROT-OTHER-STRAIN
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A0S2JXW2.json
  locator: organism, sequence and EMBL cross-reference
  accessed_at: '2026-10-21T07:11:45.327909Z'
  support: supports
  summary: A0A0S2JXW2 is an unreviewed 406-residue Pseudoalteromonas phenolica protein,
    taxon 161398, linked to ALO40986.1 on CP013187. Its complete sequence differs
    from native PS5 Bmp2.
  snapshot_sha256: c840dca9f479cb148a44ae59f094586db0709bce92d7c0bd04e127fd3cd3a0cf
- evidence_id: E-UNIPROT-CONSTRUCT
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A140UHM3.json
  locator: organism, sequence and PDB cross-reference
  accessed_at: '2026-10-21T07:11:45.393701Z'
  support: supports
  summary: A0A140UHM3 is an unreviewed 409-residue sequence linked to PDB 5BVA. It
    carries Streptomyces taxon 1883 and comprises GSH followed by the entire native
    PS5 sequence. It is not an exact native PS5 reference protein.
  snapshot_sha256: 583a30dc94b7441389b355a97a4c6f38078bdba208a1c004c6b41d3020fd8e7c
- evidence_id: E-OTHER-STRAIN-REFERENCE
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=ALO40986.1&db=protein&report=genpept&retmode=text
  locator: source, CDS and complete protein ORIGIN
  accessed_at: '2026-10-21T07:13:36Z'
  support: supports
  summary: The UniProt-linked ALO40986.1 sequence is annotated Pseudoalteromonas phenolica
    KCTC 12086, taxon 161398, locus PP2015_463 on CP013187.1. It is distinct from
    the PS5 reference.
  snapshot_sha256: 02893bb372a2433438b6a18d9bb250e57793a656b59e0d3b5b38a9cefcb6e4c4
- evidence_id: E-OTHER-STRAIN-ALIAS
  kind: authority
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=21460
  locator: Culture provenance and equivalent strain numbers; genome CP013187
  accessed_at: '2026-10-21T07:14:01Z'
  support: supports
  summary: The JCM type-strain catalogue explicitly connects O-BC30 to IAM 14989/JCM
    21460 and KCTC 12086, and links genome CP013187. This validates the record's O-BC30
    wording for the alternative protein.
- evidence_id: E-PROTEIN-EQUIVALENCE
  kind: validation
  reference: /private/tmp/npm-review-work/009/protein-equivalence.json
  locator: Independent DNA translation and complete sequence comparisons
  accessed_at: '2026-10-21T07:13:27.188977Z'
  support: supports
  summary: Translation of the 1221-nt plus-strand CDS, ATG through terminal TAA using
    table 11, gives 406 residues with no internal stop and exactly matches both GenBank
    annotation and independently retrieved GenPept ORIGIN. Native SHA256 is 2bc3ab09a447bbca0efcbd70119a5cadd3273bf3b5d9ea97efc2d1a3bcbc7e92.
    A0A0S2JXW2 differs at exactly 43 positions; A0A140UHM3 equals GSH plus native
    PS5 Bmp2.
  snapshot_sha256: 4061188f032d2386680bdabc1dbcf5fce82677a185e62f206fa3d3ddc825294b
- evidence_id: E-CHEBI-LIVE-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=MIIWISWSCMVZHG-UHFFFAOYSA-N&size=100
  locator: Official documented public es_search endpoint; parsed JSON response with
    HTTP 404
  accessed_at: '2026-10-21T07:21:59.921309Z'
  support: context_only
  summary: The service explicitly reports no compound matching this query term. This
    is a bounded search result, not an inaccessible page or universal ontology absence.
  search_scope: 'Two documented queries only: complete InChIKey and exact tetrabromopyrrole
    name; both returned explicit structured no-match responses.'
  snapshot_sha256: 410f023531e1ada0c1e3215f98fe9c8c7bd25e3b898aaaab697554924fd48f2c
- evidence_id: E-CHEBI-LIVE-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=tetrabromopyrrole&size=100
  locator: Official documented public es_search endpoint; parsed JSON response with
    HTTP 404
  accessed_at: '2026-10-21T07:22:00.646667Z'
  support: context_only
  summary: The service explicitly reports no compound matching this query term. This
    is a bounded search result, not an inaccessible page or universal ontology absence.
  search_scope: 'Two documented queries only: complete InChIKey and exact tetrabromopyrrole
    name; both returned explicit structured no-match responses.'
  snapshot_sha256: 7355988db1c4aa6fdb0d62fd45438ce7ff3378c294cf3c062035d6ee36b792e2
- evidence_id: R-LOCAL
  kind: record_content
  reference: data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml
  locator: Complete owner and resolved read_natural_product view, all five graph nodes/four
    edges, source rows and seed transform
  accessed_at: '2026-10-21T07:14:34.815423Z'
  support: supports
  summary: The record combines two exact-structure MIBiG source concepts, two producer/locus
    claims, one chemical xref and one curator-owned five-node/four-edge PS5 genetic-production
    graph. It has no occurrences, separate pathway steps, molecular targets, quantitative
    assays or clinical assertions. Its open source-fusion discussion and SEEDED status
    are explicit. Two seed events precede one bounded graph curation event; the seeder
    carries graph fields across unchanged-structure regeneration.
  snapshot_sha256: 44c21d0e976ed13b7e3afe5b2bfaaf4b17ab8a3d33ce7bead36a79226b9b6c6e
- evidence_id: R-GRAPH-PRIMARY
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=10509201&retmode=xml
  locator: DOI:10.1038/s43705-023-00309-6; full primary body P3 and Figure 1B/D caption
  accessed_at: '2026-10-21T07:11:45.170660Z'
  support: supports
  summary: The study reports an in-frame bmp2 deletion in PS5, with loss of detected
    TBP production in the mutant under the tested culture conditions. The caption
    ties the reference cluster to KR011923 and describes three replicate culture extractions.
    This directly supports the graph’s genetic production context, not Bmp2-alone
    catalytic sufficiency.
  snapshot_sha256: 9a0ebd0fdbfc520eef4f09e27e86c13b183aa758858b3652677dacfeb68c47b6
- evidence_id: R-GRAPH-FIGURE
  kind: primary_source
  reference: https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs43705-023-00309-6/MediaObjects/43705_2023_309_Fig1_HTML.png
  locator: Figure 1B and 1D; full figure independently viewed in this review
  accessed_at: '2026-10-21T07:14:34.815423Z'
  support: supports
  summary: Panel B marks bmp2 within the PS5 cluster. Panel D shows three wild-type
    production observations and three mutant observations at baseline, agreeing with
    the limited production-loss edge. The graph does not adopt quantitative concentrations
    or the separate coral-response panel.
  snapshot_sha256: 1bb793c55fcee74c361a3635fd29e7e7276706f40cacf4f26170b6e63b0fc86c
- evidence_id: R-GRAPH-METHODS
  kind: primary_source
  reference: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs43705-023-00309-6/MediaObjects/43705_2023_309_MOESM1_ESM.docx
  locator: 'Supplement: Generation of bmp2 knockout strain; LC-MS/MS methods; Tables
    S3 and S5'
  accessed_at: '2026-10-21T07:12:24.479261Z'
  support: supports
  summary: Methods describe homologous-recombination deletion construction and Sanger
    confirmation of the plasmid. Triplicate five-millilitre cultures were extracted
    for LC-MS/MS using synthetic TBP calibration. Strain NJS602 is the PS5 deletion
    mutant. These details support the bounded experiment; reference correspondence
    is not independent sequencing of the final mutant stock.
  snapshot_sha256: 4b61d3d905b91ab7b515871e9cd179b2ba2579c5868e36b402205897545a6e62
- evidence_id: R-IMODULON-COVERAGE
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Installed kg-microbe-sources imodulondb datasets, exit 0; complete returned
    table inspected
  accessed_at: '2026-10-21T07:18:22.510080Z'
  support: context_only
  summary: The complete adapter dataset list contains no Pseudoalteromonas species
    or PS5/A757 dataset. Pseudomonas datasets are a different genus and are not substituted.
    No expression-module evidence is used to judge this compound or graph.
  search_scope: Resolved the installed console runner in the local culturebotai-claw
    environment using ignored-file-inclusive path discovery; ran its datasets command
    with bytecode writes disabled and inspected every returned organism/dataset key.
    This is source coverage only, not absence of a pathway or phenotype.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: R-OVERRIDE-GUARD
  kind: record_content
  reference: src/naturalproductmech/curate/claim_references.py
  locator: load_claim_references, reconciled with scripts/seed_from_sources.py load_mibig_locus_evidence_overrides
  accessed_at: '2026-10-21T07:27:43.327965Z'
  support: context_only
  summary: Claim-reference corrections enforce an exact raw source-row SHA256. Method
    REPLACE rows currently do not enforce expected_* context fields; WITHDRAW rows
    do. Proposed REPLACE actions therefore require a paired pinned citation row or
    an explicit loader extension before relying on source-drift guards.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: bgc-source1463
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001463.4/annotations.json
  locator: 'complete version 4 entry: compound, taxonomy, locus, evidence and legacy
    references'
  accessed_at: '2026-10-21T07:12:20Z'
  support: partial
  summary: Source compound 1 has the exact target structure, taxon 43662, KT808878.1
    and methods Enzymatic assays and Heterologous expression. Its compound-level MS/MS
    reference is DOI:10.1073/pnas.1519695113. Status active and OTHER class are reproduced.
    The database assertion does not itself establish that each experiment used this
    strain.
- evidence_id: bgc-source1464
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001464.3/annotations.json
  locator: 'complete version 3 entry: compound, taxonomy, locus, bioactivity and legacy
    references'
  accessed_at: '2026-10-21T07:12:36Z'
  support: partial
  summary: Source compound 1 has the same exact structure, PS5 taxon 1437473 and KR011923.1
    but no stated locus methods. Legacy reference PMID:27001835 is relevant primary
    biosynthesis work. The compound bioactivity list includes DOI:10.1016/j.ijantimicag.2022.106523;
    automatic selection of that item does not make it evidence for this producer/locus.
- evidence_id: bgc-a757-deposit
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KT808878.1&db=nuccore&report=genbank&retmode=text
  locator: source feature, VERSION, bmp1-4 CDS features
  accessed_at: '2026-10-21T07:12:35Z'
  support: supports
  summary: The 6707 bp cluster deposit belongs to Pseudoalteromonas piscicida strain
    A757, taxon 43662. Its Bmp1-4 accessions are AME30284.1 through AME30287.1. This
    is a cluster sequence, not a complete genome. Species-level wording in the record
    omits the experimentally named strain but maps to the deposit.
- evidence_id: bgc-ps5-deposit
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=KR011923.1&db=nuccore&report=genbank&retmode=text
  locator: source feature, VERSION, bmp1-4 CDS; reused official file ps5-genbank.gb
  accessed_at: '2026-10-21T07:11:45Z'
  support: supports
  summary: 'The 6705 bp deposit is PS5/taxon 1437473; Bmp1-4 are AKJ75107.1 through
    AKJ75110.1. Reused original access time. On 07:15Z the reviewer compared the complete
    annotated translations with A757: all four differ; for example Bmp2 is 406 aa
    in both and differs at 20 aligned positions. Assay applicability cannot be rescued
    by claiming these are identical proteins.'
- evidence_id: bgc-primary2016-strain-experiments
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4833250/
  locator: DOI:10.1073/pnas.1519695113; Results, Genetic Basis for the Biosynthesis
    of 1 and in vitro reconstitution; Fig 2; Database Deposition Information
  accessed_at: '2026-10-21T07:14:58Z'
  support: partial
  summary: Primary main text assigns heterologous expression to PS5_bmp1-4 and purified-enzyme
    reconstitution to Marinomonas mediterranea MMB-1 Bmp1-4. A757 has native extract
    detection of exact TBP plus a homologous cluster. The deposition statement maps
    PS5 to KR011923 and A757 to KT808878. Thus the two recorded strains share the
    product but not the experimental method allocation.
- evidence_id: bgc-primary2023-native-ps5
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=10509201&retmode=xml
  locator: DOI:10.1038/s43705-023-00309-6; main text PS5 bmp2 deletion paragraph and
    Figure 1B/D; reused graph-primary.xml
  accessed_at: '2026-10-21T07:11:45Z'
  support: supports
  summary: Inspected primary text reports native PS5 in-frame bmp2 deletion with complete
    loss of detected TBP, and Figure 1B names KR011923. This supports native producer
    and locus necessity under the tested culture/LC-MS/MS conditions. It does not
    establish Bmp2-alone catalysis, universal production conditions or complementation.
    Reused original access; applicability checked for this target.
- evidence_id: bgc-wrong-macrolide-reference
  kind: database
  reference: https://purehost.bath.ac.uk/ws/portalfiles/portal/228298369/1_s2.0_S0924857922000139_main.pdf
  locator: Published secondary-review identity and full extracted scope; not a primary
    biosynthesis experiment. author-hosted 49-page review, title, abstract and full
    extracted text searches for tetrabrom/Pseudoalteromonas/PS5
  accessed_at: '2026-10-21T07:12:49Z'
  support: refutes
  summary: 'DOI:10.1016/j.ijantimicag.2022.106523 resolves to Macrolides from rare
    actinomycetes: Structures and bioactivities. Its stated scope is rare-actinomycete
    macrolides, not a PS5 genetic experiment; full extracted text searches return
    no tetrabrom, Pseudoalteromonas or PS5 match. This is an irrelevant citation for
    the two PS5 biosynthetic claims. The conclusion uses inspected scope and text,
    not title alone.'
- evidence_id: bgc-current-allocation
  kind: record_content
  reference: data/natural_products/alkaloids/2-3-4-5-tetrabromopyrrole.yaml; data/raw/mibig_compounds.tsv;
    conf/producer_evidence.tsv
  locator: full owner, exact source rows and method-grading table
  accessed_at: '2026-10-21T07:15:19Z'
  support: partial
  summary: Owner contains two distinct producer/locus objects merged by the same exact
    structure. A757 inherits strong locus methods; PS5 inherits no methods and an
    unrelated bioactivity reference. Existing PS5 causal graph already cites the 2023
    native deletion. The grading table maps Homology-based prediction to CLUSTER_PREDICTED
    and Knock-out studies to BGC_CHARACTERIZED plus CLUSTER_DEMONSTRATED.
assessments:
- assessment_id: A-IDENTITY-REPRESENTATION
  area: identity
  topic: Exact neutral achiral tetrabromopyrrole
  outcome: supported
  summary: The owner matches PubChem CID 4605890 and the primary paper's N-H pyrrole
    drawing with four carbon-bound bromines. The absence of stereochemical tags is
    appropriate.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-PUBCHEM
  - E-CHEMISTRY-IDENTITY
  - E-PRIMARY-CHEMICAL-FIGURE
- assessment_id: A-XREF-SYNONYM-FUSION
  area: identity
  topic: Chemical equivalence of xref, synonym and two source concepts
  outcome: supported
  summary: Tetrabromopyrrole and 2,3,4,5-tetrabromopyrrole identify the same exact
    structure here. Both pinned MIBiG source concepts have identical full structures;
    chemical fusion is supported without conflating their distinct biological claims.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-PUBCHEM
  - E-SYNONYM
  - E-SOURCE-FUSION
- assessment_id: A-GROUNDING
  area: grounding
  topic: Minted identity supported by the complete pinned eligible inventory
  outcome: supported
  summary: No eligible exact match was found in the complete pinned ChEBI inventory,
    and two current official full-key/name searches explicitly returned no match.
    Retaining MINTED is supported within those scopes; neither is a universal assertion
    about every current ChEBI entry.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-GROUNDING-SEARCH
  - E-GROUNDING-POLICY
  - E-CHEBI-LIVE-1
  - E-CHEBI-LIVE-2
- assessment_id: A-PROTEIN-REFERENCE
  area: grounding
  topic: Exact native PS5 Bmp2 protein correspondence
  outcome: supported
  summary: The graph's AKJ75108.1 node and encodes_reference_protein edge are supported
    by consistent PS5 taxonomy, the precise KR011923.1 CDS coordinates, and independent
    translation agreement. This establishes reference-locus correspondence; it does
    not sequence-verify the experimental stock or mutant.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-IDENTITY-LOCAL
  - E-PS5-NUCLEOTIDE
  - E-PS5-PROTEIN
  - E-PROTEIN-EQUIVALENCE
- assessment_id: A-PROTEIN-EXCLUSIONS
  area: grounding
  topic: Other-strain protein and GSH construct correctly excluded
  outcome: supported
  summary: The 43-residue difference excludes A0A0S2JXW2 as an exact PS5 example;
    its O-BC30/KCTC 12086 strain equivalence is documented. The GSH extension and
    conflicting taxonomy justify excluding A0A140UHM3 as the native reference. The
    historical bounded UniProt-query wording is not expanded into a global absence
    claim.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - E-UNIPROT-OTHER-STRAIN
  - E-UNIPROT-CONSTRUCT
  - E-OTHER-STRAIN-REFERENCE
  - E-OTHER-STRAIN-ALIAS
  - E-PROTEIN-EQUIVALENCE
- assessment_id: R-GRAPH-SEMANTICS
  area: evidence
  topic: Five-node/four-edge genetic production graph
  outcome: supported
  summary: The bmp2 deletion, its gene target, loss of detected production and TBP
    product identity are supported by primary text, figure and methods. The protein
    edge is explicitly a native-reference mapping and is checked separately against
    public sequences. The graph correctly avoids direct enzyme catalysis, universal
    absence, rescue, quantitative yield or pure-compound activity claims.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - R-LOCAL
  - R-GRAPH-PRIMARY
  - R-GRAPH-FIGURE
  - R-GRAPH-METHODS
  dimensions:
  - name: experimental_scope
    value: PS5 native bmp2 in-frame deletion; LC-MS/MS culture production readout
    definition: Genetic necessity under tested conditions, distinct from an isolated
      protein reaction or direct coral target binding
    evidence_ids:
    - R-GRAPH-PRIMARY
    - R-GRAPH-METHODS
- assessment_id: R-GRAPH-PROVENANCE
  area: provenance
  topic: Historical evidence-access notes and current independent inspection
  outcome: supported
  summary: The existing graph records that its original curator inspected extracted
    main text only. That historical statement is not contradicted by the present review’s
    successful figure and supplement retrieval. Prior evidence dates and the bounded
    curation event are preserved; no full-record sign-off is implied.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - R-LOCAL
  - R-GRAPH-FIGURE
  - R-GRAPH-METHODS
- assessment_id: R-CLASSIFICATION
  area: provenance
  topic: Computed classification and source identity merge
  outcome: supported
  summary: The exact-key NPClassifier inventory supports Alkaloids with empty superclass/class
    arrays at the recorded model version. Those empty outputs are faithfully preserved.
    Two source labels describe the same achiral tetrabromopyrrole connectivity; source-specific
    strain/locus claims remain distinct and are assessed separately.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - R-LOCAL
- assessment_id: R-OPTIONAL
  area: scope
  topic: Other complete-owner assertions and component boundary
  outcome: not_applicable
  summary: The full resolved owner has no external graph components or other optional
    pathway, molecular-target, quantitative-assay or clinical assertions. The inline
    graph is explicitly included in scope; absent optional fields alone are not defects.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - R-LOCAL
- assessment_id: R-IMODULON
  area: scope
  topic: Structured expression-source applicability
  outcome: not_applicable
  summary: No covered organism/dataset in the returned iModulonDB list matches the
    two producer strains. The primary genetic and biochemical evidence is assessed
    independently.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - R-IMODULON-COVERAGE
- assessment_id: bgc-fusion-and-mapping
  area: grounding
  topic: Exact product, source fusion and strain/accession mapping
  outcome: supported
  summary: Both MIBiG source concepts describe the same achiral exact compound, and
    native product evidence is reported for both strains. Combining the structure
    while retaining separate loci/producers is justified. KT808878.1 specifically
    denotes A757 and KR011923.1 PS5; the two evidence allocations must remain separate.
    OTHER is consistent with the nonmodular pathway.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - bgc-source1463
  - bgc-source1464
  - bgc-a757-deposit
  - bgc-ps5-deposit
  - bgc-primary2016-strain-experiments
- assessment_id: bgc-a757-method-scope
  area: evidence
  topic: A757 exact-locus assay applicability
  outcome: concern
  summary: The cited paper supports native A757 TBP detection and a homologous locus,
    but its direct tests use other organisms. CLUSTER_DEMONSTRATED and both inherited
    methods overstate this exact accession. Retain the native producer assertion and
    qualify the locus as homology-based unless additional strain-specific experiments
    are inspected.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - bgc-primary2016-strain-experiments
  - bgc-a757-deposit
  - bgc-ps5-deposit
- assessment_id: bgc-ps5-method-and-reference
  area: evidence
  topic: PS5 primary citation and demonstrated native locus
  outcome: concern
  summary: The unrelated macrolide review should be replaced at the claim level. PS5
    has a demonstrated locus by heterologous expression and native knockout; the latter
    supports the native producer grade. Current ungraded metadata conflicts with evidence
    already cited in its own bounded graph.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  evidence_ids:
  - bgc-primary2016-strain-experiments
  - bgc-primary2023-native-ps5
  - bgc-wrong-macrolide-reference
  - bgc-current-allocation
findings:
- finding_id: bgc-a757-methods-misallocated
  issue_key: mibig-bgc0001463-compound1-strain-specific-link-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: A757 inherits direct assay methods performed with PS5 and Marinomonas proteins
  description: The source-pinned A757 locus KT808878.1 is graded experimentally demonstrated
    using methods whose cited experiments used PS5 genes or M. mediterranea proteins.
    A757 production and pathway homology remain supported, but the native A757 proteins
    are not sequence-identical to PS5. This is a strain-specific evidence-scope error,
    not a denial of native occurrence or a wrong compound fusion.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  field_paths:
  - producer_organisms[0].notes
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].evidence
  evidence_ids:
  - bgc-source1463
  - bgc-a757-deposit
  - bgc-ps5-deposit
  - bgc-primary2016-strain-experiments
  rule_id: 'review-yaml-record Evidence Rules: exact organism and locus; distinguish
    prediction from direct experiments'
  native_severity: 'major: experimentally demonstrated evidence is assigned to a different
    strain/locus'
  normalization_reason: One issue covers both borrowed methods and the resulting locus
    grade; native source assertion is retained.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: pin strain-specific applicability of experimental methods
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: route claim-specific primary references
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: BGC0001463:1 and BGC0001464:1 exact source rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: compound evidence/bioactivity citation selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: reproducible producer and locus evidence grading
- finding_id: bgc-ps5-reference-and-grade
  issue_key: mibig-bgc0001464-compound1-reference-and-native-link-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: PS5 producer and locus cite an unrelated review and omit inspected direct
    evidence
  description: Both PS5 claims cite a rare-actinomycete macrolide review selected
    from source bioactivity metadata. Correct primary studies support the exact PS5
    product and locus, including native deletion evidence already represented in the
    record graph. Correcting citation routing and source-pinned methods together resolves
    this claim-support gap and inconsistent grading.
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  field_paths:
  - producer_organisms[1].evidence
  - producer_organisms[1].evidence_basis
  - producer_organisms[1].notes
  - biosynthetic_gene_clusters[1].evidence
  - biosynthetic_gene_clusters[1].locus_evidence_methods
  - biosynthetic_gene_clusters[1].link_evidence_basis
  evidence_ids:
  - bgc-source1464
  - bgc-primary2016-strain-experiments
  - bgc-primary2023-native-ps5
  - bgc-wrong-macrolide-reference
  - bgc-current-allocation
  rule_id: 'review-yaml-record Evidence Rules: claim-level reference scope and native
    producer evidence'
  native_severity: 'major: an unrelated reference is the sole citation on producer
    and locus claims despite available exact causal evidence'
  normalization_reason: One issue combines wrong reference and missing PS5 evidence
    because one maintained claim-level correction resolves both; no duplicate graph
    finding.
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: pin strain-specific applicability of experimental methods
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: route claim-specific primary references
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: BGC0001463:1 and BGC0001464:1 exact source rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: compound evidence/bioactivity citation selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: reproducible producer and locus evidence grading
actions:
- action_id: correct-a757-strain-scope
  description: For BGC0001463:1 version 4 maintain a pinned REPLACE locus override
    with Homology-based prediction, with DOI:10.1073/pnas.1519695113 scoped to the
    A757 homologous cluster and native detection. Generate CLUSTER_PREDICTED and retain
    SOURCE_ASSERTION for the native taxon. Explain the separately assayed PS5 and
    Marinomonas systems. Preserve source audit metadata and do not relabel those foreign
    proteins as A757.
  finding_ids:
  - bgc-a757-methods-misallocated
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: pin strain-specific applicability of experimental methods
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: route claim-specific primary references
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: BGC0001463:1 and BGC0001464:1 exact source rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: compound evidence/bioactivity citation selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: reproducible producer and locus evidence grading
  generator: scripts/seed_from_sources.py using maintained claim references and locus
    evidence overrides
  acceptance_checks:
  - Pair every REPLACE method override with a mibig_claim_references.tsv row pinned
    by the exact raw source-row SHA256. The current REPLACE loader does not enforce
    expected_* fields itself; the paired claim-reference loader must fail on source-row
    drift. If no paired reference row is appropriate, extend the method loader to
    enforce equivalent pins before relying on them.
  - Exact version/accession/taxon/structure and original methods are pinned; only
    BGC0001463:1 changes.
  - A757 producer remains supported; locus wording distinguishes homology from direct
    assays.
  - Run target seed-canary, inspect generated diff, then documented regeneration and
    strict validation, verify-reproduction, verify-corpus --summary and qc.
- action_id: correct-ps5-primary-support
  description: For BGC0001464:1 version 3 add pinned claim references to DOI:10.1073/pnas.1519695113
    for heterologous locus sufficiency and DOI:10.1038/s43705-023-00309-6 for native
    PS5 deletion/production. Replace methods with Heterologous expression and Knock-out
    studies, yielding CLUSTER_DEMONSTRATED and BGC_CHARACTERIZED. Remove the unrelated
    review as support for these claims while preserving source provenance. Keep the
    graph’s bounded native deletion interpretation and distinct native reference protein.
  finding_ids:
  - bgc-ps5-reference-and-grade
  target_ids:
  - naturalproductmech:mibig-dcee736e16
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: pin strain-specific applicability of experimental methods
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: route claim-specific primary references
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: BGC0001463:1 and BGC0001464:1 exact source rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_mibig.py
    role: compound evidence/bioactivity citation selection
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: reproducible producer and locus evidence grading
  generator: scripts/seed_from_sources.py using maintained claim references and locus
    evidence overrides
  acceptance_checks:
  - Pair every REPLACE method override with a mibig_claim_references.tsv row pinned
    by the exact raw source-row SHA256. The current REPLACE loader does not enforce
    expected_* fields itself; the paired claim-reference loader must fail on source-row
    drift. If no paired reference row is appropriate, extend the method loader to
    enforce equivalent pins before relying on them.
  - Use BGC0001464:1 source identity and its alias minted identifier when pinning,
    preserving merged owner naturalproductmech:mibig-dcee736e16.
  - Native knockout is limited to tested conditions; no Bmp2-alone catalytic sufficiency
    or rescue claim is introduced.
  - Both producer and locus references resolve to inspected primary PS5 evidence,
    and the merged structure and separate A757 claim remain intact.
  - Run target seed-canary, inspect generated diff, then documented regeneration and
    strict validation, verify-reproduction, verify-corpus --summary and qc.
limitations:
- The live official ChEBI search returned explicit no-match responses for two bounded
  queries, exact full key and tetrabromopyrrole. Together with the complete pinned
  eligible inventory this supports current minted grounding; it is not a universal
  assertion about every ontology synonym or representation.
- Protein sequence correspondence concerns public reference records. Experimental-stock
  sequence identity, mutant junctions, catalytic activity and complementation are
  not established by this comparison.
- The historical bounded UniProt query was not rerun or generalized. Both named alternative
  entries were directly inspected and compared instead.
- The existing graph is deliberately limited to a genetic production context. This
  review does not reconstruct deletion junctions from raw sequencing, exclude all
  off-target changes, infer a rescue experiment, or independently reanalyse chromatographic
  raw data.
- The original curator’s access notes are historical provenance. Newly inspected figures
  and supplementary methods support the current review without rewriting those earlier
  observations.
- PNAS direct PMC pages were challenged and official efetch returned metadata only.
  The primary main text was inspected through the web index, including the explicit
  organism assignments and deposit statement; the supporting PDF route returned a
  browser challenge. No uninspected supporting-table claim is made.
- The 2023 full XML and reference GenBank file were reused with original access timestamps
  from this record’s root review. The root separately inspected the 2023 figure and
  supplementary methods; this packet independently uses the main text and caption.
- No universal absence of an A757-specific later experiment is asserted. The confirmed
  defect is that the existing cited study does not supply the inherited exact-strain
  assays.
- 'The two findings concern different source-locus objects: an overgraded A757 experiment
  allocation and a PS5 citation/evidence routing gap. No identity, source-fusion or
  inline-graph error is inferred.'
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
- No scientific owner, source inventory, component, native status or seed history
  was edited.
- The PS5 graph is positively supported despite source-level citation and grading
  defects. The two producer/locus objects retain separate experimental scopes.
tags:
- path-order-campaign
- batch-001
- tetrabromopyrrole
```
