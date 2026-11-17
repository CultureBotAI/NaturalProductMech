# 4-hydroxy-2-quinolone: exact DHQ evidence, tautomer identity and assay scope

- Review: 20261021T082323Z-4-hydroxy-2-quinolone
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T08:09:07.691701Z
- Finished UTC: 2026-10-21T08:23:23.505462Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact normalized chemical identity, native PAO1 formation, fungal and bacterial occurrence, and all seven deposited assay calls are supported. One major finding identifies omitted native and reconstituted biosynthetic methods; two minor findings concern the answerable tautomer naming discussion and missing bacterial mutagenicity assay context. The plant occurrence remains unverified because its original paper was inaccessible.

## Scope And Provenance

One complete owner: chemical identity and tautomerism, grounding and xrefs, three occurrence citations, native producer/locus, seven activity results and their target, classification, source concepts, naming discussion and audit history.

Selection: Twentieth initially unreviewed path, tenth in batch 002 from fresh origin/main. Review starts and saves follow path order. The fresh-main authoritative list has 91 valid bundles covering 54 of 3,116 records; ten reviews in pending PR 1000 provide additional campaign coverage. Ignored files were included. This bundle has exactly one target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 10ed28fcdadb3d955c30732ff05b5d0e4adbee3b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:75926 | data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml | generated | 4-hydroxy-2-quinolone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | CHEBI:75926 | The entire target has zero ERROR rows; this does not itself verify scientific claims. |
| Corpus path and filing integrity | passed | True | CHEBI:75926 | All 3,116 record files agree with 3,116 PATHS.tsv rows and their pinned filing pathways. |
| Corpus reproduction | passed | True | CHEBI:75926 | All 3,116 records are byte-identical to the seeder output from committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | CHEBI:75926 | The documented exhaustive queue command produced 8,928 diagnostic rows in 12 queues; deterministic queue output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:75926 | Full configured gate passed using existing CHEBI and GO caches plus the committed taxonomy adapter: 13,434 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,722 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate after environment repair | passed | True | CHEBI:75926 | The full documented just qc recipe passed after installing the pinned linter, allowing the read-only governance fetch, and restoring the required provenance tag. Tests: 999 passed, 4 skipped, 2 warnings. Closed-schema validation: 3,116 records and zero errors. Documentation, provenance, source queue, governed artifacts, generated pages, reproduction, filing integrity and corpus reporting all passed. |
| Seven assay calls, measurements and exact deposited structures | passed | True | CHEBI:75926 | All seven current AID/SID/CID rows and both independent deposited structures agree with the owner. Five inconclusive outcomes remain NOT_DETERMINED; one inactive remains INACTIVE; the one qualitative GENE-TOX positive remains ACTIVE. |
| Assay and protein target scope | passed | True | CHEBI:75926 | Complete official assay descriptions, the exact GENE-TOX row and reviewed UniProt entry were inspected. The target accession is valid; no direct activity or human-toxicology conclusion follows from the inconclusive cellular screen or bacterial mutagenicity row. |
| Supplementary raw qHTS row and titration details | unavailable | False | CHEBI:75926 | Single bounded raw-row requests for AIDs 2685,504332,624287,624296 returned HTTP 504 PUGREST.Timeout. Current exact SID/CID summary values and outcomes plus complete assay descriptions succeeded, so verification of the stored database claims is complete; unreturned raw titration details are not inferred. |
| Normalized substance identity and tautomer representations | passed | True | CHEBI:75926 | The owner, official ChEBI default MOL and PubChem structure share a full Standard InChI/key. Independent fixed-H comparison retains the lactam/lactim distinction; three-star grounding and achiral stereo completeness are supported. |
| Exact native and reconstituted product formation | passed | True | CHEBI:75926 | Full original 2008 text and figures show exact native PAO1 DHQ, pqsA/pqsD dependence, recombinant-cell formation and standard-matched purified-enzyme product. The final ring-closure mechanism remains explicitly proposed. |
| Exact-compound method and native producer grading | failed | True | CHEBI:75926 | The correctly cited original study contains demonstrated methods absent from the source-derived CLUSTER_UNSTATED and SOURCE_ASSERTION grades. A compound-specific maintained correction is needed. |
| Cited fungal exact-compound occurrence | passed | True | CHEBI:75926 | The actual 2013 primary paper explicitly reports exact 4-hydroxyquinolin-2(1H)-one isolated from MM3S-3 rice culture; host-plant tissue is not substituted for the fungal culture. |
| Bacterial occurrence and citation scope | passed | True | CHEBI:75926 | The cited 2011 paper attributes the metabolite to P. aeruginosa and studies recombinant PA14 enzyme; its 2008 reference directly demonstrates native PAO1 occurrence. These distinct scopes are preserved. |
| Exact Haplophyllum occurrence in the cited original | unavailable | True | CHEBI:75926 | The original 2000 body remains inaccessible after bounded free routes. Bibliographic and taxon identity are confirmed, but exact compound, sampled tissue and identification method cannot be certified. |
| Organism identifiers and deposited locus | passed | True | CHEBI:75926 | NCBI/Wikidata identities agree; PAO1 accession AE004091.2 contains pqsA/PA0996 and pqsD/PA0999 within the stored interval. |
| Native expression-context applicability | passed | False | CHEBI:75926 | Previously retrieved PAO1-lineage component membership includes pqsA/pqsD. It is optional regulatory context and is not used as exact-compound formation proof. |

## Scientific And Domain Assessments

### Exact substance, tautomer distinction and ChEBI eligibility

identity: supported. Targets: CHEBI:75926.

All chemical identity fields are internally coherent. ChEBI exact grounding follows the repository full Standard-InChIKey policy. The two names denote tautomers with the same normalized substance key, so a shared key alone must not be described as identical fixed-H graphs. The primary Scheme 1 independently depicts the source enol form.

### Biological origin and experimental versus proposed chemistry

identity: supported. Targets: CHEBI:75926.

Native PAO1 medium contains exact DHQ. Native knockouts, recombinant formation and purified-enzyme product identification support the NATURAL_PRODUCT assertion. The uncertain final cyclization mechanism does not make the observed biological product a synthetic derivative. No detailed causal mechanism is asserted in the owner.

### Native producer and exact-compound locus evidence

evidence: concern. Targets: CHEBI:75926.

The source-derived low grades are faithfully imported, but the record already cites the paper that demonstrates the exact PAO1 pqsA/pqsD requirement and recombinant/purified-enzyme formation. Capture these methods through maintained source-pinned curation. Preserve the distinction between native knockout evidence and heterologous/enzymatic evidence.

### Computed classification and asserted source classes

provenance: supported. Targets: CHEBI:75926.

The model-versioned predictions match the exact-key inventory; the Quinazoline class is not a literal structural adjudication. PKS and Anthranilic acid-derived/Cyclic polyketide reproduce MIBiG. The original precursor and condensation evidence is compatible with the broad anthranilate-derived interpretation. No unsupported manual replacement of model output is proposed.

### Source concepts, history and unresolved naming discussion

provenance: concern. Targets: CHEBI:75926.

Both minted source concepts and four seed events are internally consistent with SEEDED status. The existing name-disagreement question is answerable by tautomer normalization and the independently inspected fixed-H structures; its resolution remains missing.

### All owner claims and optional absent fields

completeness: not_applicable. Targets: CHEBI:75926.

Every source concept, definition, xref, classification, occurrence, assay, producer/locus, discussion and history field is addressed across the root and specialist assessments. The complete resolved owner has no causal graphs, pathway steps, graph references, sibling assertions or clinical claims. Optional annotation expansion is not required by this review.

### Native expression-context applicability

evidence: supported. Targets: CHEBI:75926.

Previously inspected aeruPRECISE364 data provide matching PAO1-lineage pqsA/pqsD component context. Its primary methods include PAO1 and PAO1 delta-mexB. This optional evidence does not change any exact-compound grade or substitute for the primary knockout experiment.

### Haplophyllum bucharicum cited occurrence

evidence: unknown. Targets: CHEBI:75926.

The bibliographic reference is genuine and species-specific, but the original content was unavailable. Exact occurrence, sampled plant part and compound identification remain unknown. No removal or certainty upgrade follows from the bounded access failure.

### Penicillium citrinum exact occurrence

evidence: supported. Targets: CHEBI:75926.

The cited journal paper directly reports the exact known compound from a rice culture of MM3S-3. This supports the species-level occurrence as an isolation report; it is not silently generalized to Ceratonia host tissue or every P. citrinum strain. The current DATABASE_ASSERTION classification remains honest about the imported source.

### Pseudomonas aeruginosa occurrence and citation scope

evidence: supported. Targets: CHEBI:75926.

The cited 2011 paper recognizes the exact species-metabolite relationship, while direct native detection is established by its 2008 primary reference in PAO1. Keep that distinction visible: purified PA14 PqsD kinetics are not a separate native isolation. The import is not contradicted, so no unsupported-triple exclusion is proposed.

### Taxonomic provenance and occurrence/producer separation

evidence: supported. Targets: CHEBI:75926.

All three taxon IDs and Wikidata organism URIs resolve consistently. The occurrence objects retain DATABASE_ASSERTION and do not themselves promote plant or fungal producers. The PAO1 producer/locus and chemical tautomer equivalence are assessed separately in this review.

### Exact structure and assay-result fidelity

evidence: supported. Targets: CHEBI:75926.

Every stored database result is for the exact deposited structure and reproduces the current authoritative outcome and endpoint. Fitted potency values do not override inactive or inconclusive calls. Ungrounded non-UniProt accessions remain transparently recorded; no replacement protein identifiers were guessed.

### Mutant-oriented cell cAMP assay and human GNAS grounding

scope: supported. Targets: CHEBI:75926.

P63092 correctly identifies the human GNAS assay target. AID 624287 is an inconclusive cell-based cAMP HTRF screen directed at gsp activating mutations. The background mentions R201H/R201C but does not establish which mutant construct was tested in the inspected protocol. The current NOT_DETERMINED observation supports neither direct protein action nor wild-type GNAS agonism.

### Bacterial mutagenicity scope behind the TOXIN summary

completeness: concern. Targets: CHEBI:75926.

The sole positive bioactivity is an archived Salmonella Ames result with metabolic activation. The generated record retains a generic mutagenicity title and coarse TOXIN class but omits this available assay context. The classification follows the repository mapping; it should not be interpreted as proven human or systemic toxicity, and the positive should not be deleted merely because it is qualitative.

## Findings

### R020-MISSING-METHODS: The cited primary study demonstrates exact DHQ formation but both grades remain at source level

major / open / confirmed; issue key: bgc0000922-compound2-missing-exact-dhq-methods.

BGC0000922 compound 2 has no imported locus method and remains CLUSTER_UNSTATED with a SOURCE_ASSERTION PAO1 producer. Its existing 2008 citation directly demonstrates native pqsA/pqsD loss, E. coli PqsA/PqsD formation and purified-enzyme formation of authentic-standard-matched DHQ. This materially understates the exact compound evidence; it is not a transferred result from HHQ or PQS.

### R020-NAMES: The open naming question can be resolved as a tautomer representation difference

minor / open / confirmed; issue key: chebi75926-tautomer-name-discussion-unresolved.

The current discussion treats the two labels as a possible upstream structure error. Independent reconstruction shows a lactam/lactim tautomer pair with identical Standard InChI but different fixed-H representations. The primary drawing matches the source enol representation. Record that evidence-backed distinction without replacing a coherent owner structure or treating the names as identical fixed-H graphs.

### BIO020-F1: Positive GENE-TOX row omits bacterial assay and metabolic-activation context

minor / open / confirmed; issue key: chebi-75926-genetox-assay-context-omitted.

AID 1259408 SID 363895103 explicitly records a positive Salmonella typhimurium Ames assay with metabolic activation. The owner stores only a generic GENE-TOX mutagenicity title and TOXIN class. Add the inspected assay context so users can distinguish the supported bacterial test from untested human toxicity. The row does not identify an individual tester strain or provide dose-response, and it does not establish that activity requires metabolic activation.

## Recommended Actions And Acceptance Checks

### R020-CAPTURE-METHODS

For naturalproductmech:mibig-41b176c91f / BGC0000922:2, add the demonstrated Knock-out studies, Heterologous expression and Enzymatic assays through the maintained method overlay. Pair the REPLACE row with a claim-reference decision pinned to raw row SHA256 b8c6cb52b474b3b4fb8b35af4103051a086ea612cf1773cd5becde2ec0fa0b21 and retain DOI:10.1074/jbc.m804555200 for producer, locus and source reference. Explain native PAO1 versus recombinant host/His-tagged enzyme scope. Do not rely on expected_* columns alone: the current REPLACE loader does not enforce them. A tested loader extension is the alternative if a paired citation overlay is unsuitable.

- Pin version 5, taxon NCBITaxon:208964, AE004091.2, bounds 1073960..1087095, the full target key and original empty method list through the enforced full-row digest; deliberate source-row drift must fail closed.
- After reseeding only the exact compound gets CLUSTER_DEMONSTRATED and native PAO1 BGC_CHARACTERIZED; preserve the correct original citation, chemistry, occurrences and neighboring compound grades.
- Describe PqsA/PqsD product formation as observed and spontaneous cyclization as proposed; no historical construct sequence or human toxicity claim is inferred.
- Run focused overlay tests, target strict validation, reproduction verification and required repository QC.

### R020-RESOLVE-NAMES

Resolve the existing name-disagreement with curator-owned status, actual resolved_date, resolution_note and evidence. Explain the enol/keto fixed-H distinction and the repository Standard-InChIKey identity policy. Preserve both source labels, the generated prompt and chemical representations.

- The resolution cites the inspected default MOL, full Standard/fixed-H comparison and original primary drawing; no unsupported claim of identical fixed-H structures is introduced.
- The answer survives the documented targeted curation/reseed workflow and required strict/reproduction checks; unrelated fields and source labels remain unchanged.

### BIO020-A1

Preserve exact assay identity, source calls and values; enrich the positive GENE-TOX observation with Salmonella Ames and with-metabolic-activation scope, and disclose that the tester strain, quantitative dose and no-activation comparison are unspecified. Carry this through the effective PubChem inventory/extraction and generated notes, with manifest/source provenance as required. Optionally clarify that P63092 is assay-target metadata for an inconclusive mutant-oriented cellular cAMP screen, not a demonstrated direct compound target.

- The GENE-TOX positive retains exact CID 54680871/SID 363895103/AID 1259408 and DATABASE_ASSERTION provenance.
- Notes state Salmonella Ames with metabolic activation without inventing a specific strain, dose or requirement for activation.
- The five NOT_DETERMINED and one INACTIVE qHTS calls and all six Potency values remain intact.
- No direct GNAS agonism, wild-type activity, human toxicity or carcinogenicity is inferred.
- Authorized regeneration, strict validation and reproducibility checks pass after implementing the source-context route.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R020-OWNER | data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml; Entire owner, resolved content, all seven assays, three occurrences, two source concepts and four seed-history events | supports | One achiral neutral compound has three database occurrence assertions, one PAO1 producer and BGC0000922 locus, seven PubChem assays, one assay target and an open naming discussion. The resolved record has no causal graph, graph references, biosynthetic pathway, separate molecular-target list, sibling relation or clinical claim. |
| R020-RAW | data/raw/mibig_compounds.tsv; Entire matching BGC0000922:2 raw row, cross-checked with the complete source-row extraction | supports | The raw version-5 row has exact full key HDHQZCHIXUUSMK-UHFFFAOYSA-N, no locus methods, PAO1 taxon 208964, AE004091.2 bounds 1073960..1087095 and DOI:10.1074/jbc.m804555200. Its canonical row SHA256 is b8c6cb52b474b3b4fb8b35af4103051a086ea612cf1773cd5becde2ec0fa0b21. The output faithfully preserves these source fields. |
| R020-CHEMISTRY | /private/tmp/npm-review-work/020/identity-comparison.json; Independent RDKit reconstruction of owner, current default ChEBI MOL and PubChem graph; Standard and fixed-H InChIs | supports | All three representations have formula C9H7NO2, net charge zero, no stereocentres and identical full Standard InChI/key. The owner is 2,4-quinolinediol; the current ChEBI MOL and PubChem graph are 4-hydroxyquinolin-2(1H)-one. Their fixed-H InChIs differ, documenting tautomeric representation rather than identical fixed-H graphs. stereo_complete:true is appropriate. |
| R020-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/75926/; Complete released three-star entry, default InChI/key, definition, names, CAS and ontology | supports | CHEBI:75926 remains an eligible three-star exact Standard-InChIKey grounding. Its definition and preferred name describe the keto tautomer. The exported aromatic SMILES omits the required pyrrolic H, so that string is not used as the decisive graph; its official default MOL independently resolves the intended structure. |
| R020-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/75926/; Complete default molfile parsed independently | supports | The default MOL encodes the neutral keto tautomer with the owner full Standard InChIKey. It supports the shared substance identity while retaining the fixed-H distinction. |
| R020-PUBCHEM | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54680871/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON; Complete CID 54680871 property response | supports | The sole owner PubChem xref resolves to the same full Standard InChI/key and C9H7NO2. It is chemical identity evidence, not an independent producer or activity experiment. |
| R020-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0000922.5/annotations.json; Complete version-5 entry, compound 2, taxonomy, locus and evidence fields | supports | The current MIBiG entry reproduces the pinned 2,4-Quinolinediol structure, authentic-standard compound citation, PAO1 taxon and locus interval. The locus evidence array is empty; the current database therefore does not itself supply the missing methods. |
| R020-PRIMARY2008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2570881/; DOI:10.1074/jbc.M804555200, PMID:18728009; complete original main body, Experimental Procedures, DHQ Production, Figures 2/3 and discussion | supports | Native PAO1 pqsA deletion and nonpolar pqsD disruption eliminate detectable exact DHQ, whereas pqsB and pqsC mutants retain it. The pqsA deletion was PCR/sequencing verified; the study describes 189-bp residual insertions for the other mutants. PqsA plus PqsD also produces DHQ in E. coli. Purified N-terminal His-tagged PqsA/PqsD form the authentic-standard-matched product from anthranilate/CoA and malonyl-CoA or malonyl-ACP. The proposed spontaneous final ring closure is explicitly uncertain; the paper does not prove that detailed step. |
| R020-SCHEME1 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/bb95/2570881/0701a5dcf469/zbc046085462s001.jpg; Original Scheme 1, directly visually inspected | supports | The original drawing distinguishes DHQ from HHQ and PQS and depicts DHQ in the enol representation used by the MIBiG-derived owner. |
| R020-FIGURE2 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/bb95/2570881/93a6665f25e1/zbc0460854620002.jpg; Original Figure 2 panels A–C, directly visually inspected | supports | Native wild-type and pqsA spent-medium profiles, radiolabeled native mutant lanes and recombinant-cell lanes support the stated DHQ-specific distinctions. Native pqsA/pqsD loss and PqsA-plus-PqsD recombinant formation concern the exact target, not a sibling quinolone. |
| R020-FIGURE3 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/bb95/2570881/6dfb7a8774f5/zbc0460854620003.jpg; Original Figure 3 panels A–D, directly visually inspected with caption | supports | Malonyl-CoA and malonyl-ACP support product formation; malonic acid does not. Product and authentic DHQ coelute at 3.67 minutes and share protonated m/z 162 with the reported fragments. PqsA alone instead forms anthraniloyl-CoA. |
| R020-GENOME | https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AE004091.2&amp;db=nuccore&amp;report=genbank&amp;retmode=text&amp;from=1073960&amp;to=1087095; AE004091.2 exact owner interval; source and complete FEATURES section re-inspected for this target | supports | The interval is explicitly PAO1 taxon 208964 and contains pqsA/PA0996 (AAG04385.1, relative 4503..6056) and pqsD/PA0999 (AAG04388.1, relative 7983..8996). This links the native genes in the 2008 experiment to the stored locus. No historical expression-construct sequence equivalence is claimed. |
| R020-GRADING | conf/producer_evidence.tsv; Complete controlled method table and organism-versus-cluster rules | supports | Knock-out studies grade both the native producer and locus. Enzymatic assays and Heterologous expression grade the locus only. Combining the supported methods yields BGC_CHARACTERIZED for native PAO1 and CLUSTER_DEMONSTRATED for this exact compound. |
| R020-GUARD | src/naturalproductmech/curate/claim_references.py; Complete claim-reference loader and application, reconciled with seed_from_sources.py method loader | context_only | The citation overlay validates the complete raw source-row SHA256. REPLACE method overrides currently ignore expected_* fields, unlike WITHDRAW. A paired exact-row citation overlay retaining the correct DOI can guard this method update; alternatively extend and test the method loader. No structure replacement is needed here. |
| R020-CLASSIFIER | data/raw/npclassifier.tsv; Complete exact-full-key model row | context_only | The stored ALKALOIDS filing and Anthranilic acid alkaloids/Quinazoline alkaloids predictions reproduce the pinned model output. The graph contains one nitrogen; Quinazoline alkaloids is therefore retained only as a computational class prediction, not a validated literal ring identity or biosynthetic experiment. |
| R020-DISCUSSION | scripts/seed_from_sources.py; CURATOR_OWNED_DISCUSSION_FIELDS and preservation by discussion_id | context_only | The existing status, resolved_date, resolution_note and evidence are curator-owned preserved fields. An evidence-backed answer can persist through reseeding while the source labels and generated prompt retain their provenance. |
| R020-imodulon-component85-context | https://imodulondb.org/api/imodulons/p_aeruginosa/precise364/85/genes; Exact component-membership JSON endpoint used by installed runner get_imodulon_genes; verified HTTP200 and matching seven-gene payload; imodulon-component85-source.json plus source-access receipt. Original runner summary and context receipts retained.; previously fetched evidence reused with original timestamp, no new search claimed | context_only | The complete seven-member PAO1-lineage component includes pqsA/PA0996 and pqsD/PA0999 alongside pqsB/C/E and phnAB. This is relevant native expression context only; no exact-DHQ measurement, necessity or catalytic rate follows from component membership. |
| R020-imodulon-dataset-strain-context | https://academic.oup.com/nar/article/50/7/3658/6561658; DOI:10.1093/nar/gkac187; Methods, RNA extraction and Data acquisition; Results, iModulon structure of the transcriptome; dataset link; previously fetched evidence reused with original timestamp, no new search claimed | context_only | The dataset's primary publication explicitly links aeruPRECISE364 to the inspected database dataset. It reports PAO1 and PAO1 delta-mexB expression profiles, comprising 364 quality-filtered samples (83 new and 281 public), mapped to PAO1 genome NC_002516.2. Thus this is relevant PAO1 lineage regulatory context, not a PA14 assay. The runner's dataset catalogue independently labels p_aeruginosa/precise364 as Pseudomonas aeruginosa but supplies no strain field; the strain attribution comes from the primary methods. |
| O020-OWNER | data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml; Entire owner and resolved source rows read; this subtask audits all three occurrence objects | supports | The owner has three LOTUS DATABASE_ASSERTION occurrences: Haplophyllum bucharicum/DOI 10.1007/BF02238348, Pseudomonas aeruginosa/DOI 10.1002/CBIC.201100014 and Penicillium citrinum/DOI 10.1021/NP4001366, all joined by HDHQZCHIXUUSMK-UHFFFAOYSA-N. Their plant, bacterial and fungal taxa must be evaluated separately from the PAO1 producer and enzyme claims. |
| O020-PUBMED | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=18728009,21425231,23713692&amp;retmode=xml; DOI/PMID mappings and complete abstracts of 2008,2011,2013 references | supports | PMID 18728009 maps to DOI 10.1074/jbc.M804555200, PMID 21425231 to DOI 10.1002/cbic.201100014 and PMID 23713692 to DOI 10.1021/np4001366. The 2013 abstract describes an endophytic P. citrinum culture but does not enumerate this known compound; its full article is needed for that exact occurrence. |
| O020-PLANT-REFERENCE | https://api.crossref.org/works/10.1007/BF02238348; Official title, author, journal and pagination for DOI 10.1007/BF02238348 | context_only | The DOI identifies I.A.Bessonova, Components of Haplophyllum bucharicum, Chemistry of Natural Compounds36(2000):323–324. Bibliographic identity is confirmed, but it does not independently establish the exact compound, plant part or isolation method. |
| O020-PLANT-ACCESS | https://api.openalex.org/works/https://doi.org/10.1007/BF02238348; Closed work locations; official article/PDF access responses inspected in primary2000.html and primary2000.pdf | unknown | Only the publisher location was identified. Both purported publisher HTML/PDF responses are 3038-byte Client Challenge HTML, not article text or a PDF. Bounded DOI/title/author searches did not yield a readable original body. Later reviews and citation snippets were used only as discovery leads; the plant occurrence remains unverified. |
| O020-FUNGAL-PRIMARY | https://www.researchgate.net/publication/275582227_Alkaloids_and_Polyketides_from_Penicillium_citrinum_an_Endophyte_Isolated_from_Ceratonia_siliqua; Author-uploaded actual J.Nat.Prod.2013,76:1099–1104 body: Results p1099, Fungal Material and Extraction/Isolation p1103; journal DOI footers verified | supports | The original article explicitly lists 4-hydroxyquinolin-2(1H)-one and reports 1.8 mg isolated from rice cultures of P. citrinum MM3S-3. The endophyte came from a Moroccan Ceratonia siliqua stem; ITS accession JQ901861 is reported. This establishes fungal-culture occurrence, not occurrence in the host plant. The page’s conference wrapper is separate from the uploaded journal article identified by its DOI/page footers. |
| O020-FUNGAL-SI | https://ndownloader.figshare.com/files/4040869; Official Figshare file 4040869, article 2401162; title page and complete 42-page table of contents | context_only | The official supplement matches DOI 10.1021/np4001366 and provides spectra for new compounds 1–6. The target is a known compound, so its occurrence is supported by the explicit main-body isolation statement rather than these other compounds’ spectra. No target spectrum reinterpretation is claimed. |
| O020-BACTERIAL-CITED2011 | https://www.lookchem.com/FreePDFArticle_13283-92-6_20071976.htm; Actual primary ChemBioChem2011,12:850–853 body; p 850 intro, p 851 DHQ kinetic control, p 853 ref 15 and conclusion; public full-text transcription inspected | partial | The authors identify DHQ as a P. aeruginosa metabolite, citing Zhang2008, then study PqsD cloned from PA14 and expressed in E. coli. Their DHQ experiment is a purified-enzyme kinetic control. Native-culture occurrence is contextual attribution, not a new native isolation established by those assays. This supports the substance/species attribution at its stated scope. |
| O020-BACTERIAL-PRIMARY2008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2570881/; PMC2570881: Experimental Procedures; DHQ Production in the pqs Operon Mutants; Figure 2; re-read08:15:11Z | supports | The original Zhang2008 study directly analyzes extracellular DHQ in wild-type PAO1 spent medium by LC-MS, with authentic DHQ standards and radiolabeled anthranilate experiments. It distinguishes DHQ from HHQ/PQS and tests native pqs mutants. This provides direct primary support for P. aeruginosa occurrence, with PAO1 strain scope; recombinant PA14 experiments are not substituted for it. |
| O020-TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1006069,287,5077,208964&amp;retmode=xml; NCBI 1006069,287,5077,208964 names/ranks/lineages | supports | The three occurrence IDs resolve to H. bucharicum, P. aeruginosa and P. citrinum respectively; 208964 is PAO1. Their land-plant, bacterial and fungal groups agree. This validates taxonomic identity, not exact-metabolite detection. |
| O020-WIKIDATA | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q18082667%7CQ31856%7CQ10622902&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Entities Q18082667,Q31856,Q10622902 labels and P225/P685; independently inspected against occurrence taxa | supports | The three provenance entities identify the corresponding plant, bacterium and fungus with matching NCBI taxonomy links. They remain provenance references, not primary isolation proof. |
| BIO020-SUMMARY | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54680871/assaysummary/JSON; /private/tmp/npm-review-work/020/bioactivity/cid54680871-assaysummary.json | supports | All seven owner AIDs are present for CID 54680871: AID 1030 is Inactive at 5.0119uM; AIDs 2147,2685,504332,624287,624296 are Inconclusive at 39.8107,0.206,79.4328,3.9811,8.1995uM respectively; AID 1259408 is Active without a numeric endpoint. Six qHTS rows use SID 24789721; GENE-TOX uses SID 363895103. Values are source Potency endpoints, not evidence that the inactive or inconclusive calls are positive. |
| BIO020-SUBSTANCES | https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/24789721,363895103/JSON; /private/tmp/npm-review-work/020/bioactivity/substances.json | supports | Both deposited substance records standardize to CID 54680871. Independently reconstructed raw atom/bond graphs give C9H7NO2 and full InChIKey HDHQZCHIXUUSMK-UHFFFAOYSA-N, exactly matching this owner. MLSMR SID 24789721 is MLS000716246; GENE-TOX SID 363895103 names 2,4-dihydroxyquinoline. |
| BIO020-DESCRIPTIONS | https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1030,1259408,2147,2685,504332,624287,624296/description/JSON; /private/tmp/npm-review-work/020/bioactivity/seven-assay-descriptions.json | supports | The complete official descriptions distinguish ALDH fluorescence, JMJD2E coupled fluorescence, G9a AlphaScreen, Drosophila S3 lipid imaging, MCF10a DNA-content imaging and GNAS/gsp cell cAMP HTRF. G9a warns of assay interference. AID 624287 concerns activating gsp mutations and a cellular cAMP readout; background names R201H/R201C, but the inspected protocol does not identify the actual mutant construct or cell line. It does not establish direct protein binding or wild-type agonism. |
| BIO020-GENETOX | https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1259408/JSON?sid=363895103; PC_AssaySubmit.data[0], SID 363895103; results tids 1,3,5,6,8,9,10 | supports | The exact deposited row is positive in a Salmonella typhimurium histidine reverse-mutation (Ames) assay with metabolic activation. It specifies one or more of five standard tester strains, not an individual strain. No dose or dose-response is supplied. This archived database assertion is narrower than human toxicity, carcinogenicity or systemic toxin activity; results without activation are not supplied. |
| BIO020-ALDH-ROW | https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1030/JSON?sid=24789721; /private/tmp/npm-review-work/020/bioactivity/aid1030-sid24789721.json | supports | Exact SID 24789721 row retains the depositor Inactive outcome despite fitted Potency 5.0119uM and an Activator phenotype/single-point activity label. The stored INACTIVE call correctly takes precedence over an inference from the number. |
| BIO020-JMJD-ROW | https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/2147/JSON?sid=24789721; /private/tmp/npm-review-work/020/bioactivity/aid2147-sid24789721.json | supports | Exact SID 24789721 row retains the depositor Inconclusive outcome with Potency 39.8107uM and a single-point activity label. Stored NOT_DETERMINED with the original source outcome in notes is faithful. |
| BIO020-UNIPROT | https://rest.uniprot.org/uniprotkb/P63092.json | supports | P63092 is reviewed human GNAS, the G(s) alpha short-isoform entry, with GTPase function and cAMP signaling. It is a legitimate protein grounding for assay target metadata, not a mutant-specific protein accession or evidence that this compound binds or activates it. |
| BIO020-COMPARE | /private/tmp/npm-review-work/020/bioactivity/bioactivity-comparison.json | supports | RDKit 2026.03.5 reconstructs both raw deposited graphs to the exact owner full key. All seven owner calls, numeric values, endpoint names, target accessions and inventory rows agree with the current authoritative summary. |
| BIO020-PIPELINE | scripts/extract_pubchem_bioassay.py; Entire extractor read; scripts/seed_from_sources.py classification and bioactivity construction sections; seven exact data/raw/pubchem_bioassay.tsv rows | supports | The extractor preserves summary outcomes, values, endpoint and target metadata but has no protocol/context columns. The seeder maps non-active/non-inactive outcomes to NOT_DETERMINED and keeps source outcome notes; Potency remains OTHER. Only explicitly ACTIVE rows contribute activity classes; the mutagenicity-title rule assigns TOXIN to this GENE-TOX row. Current source-to-owner reproduction is faithful, while protocol scope is omitted. |

## Limits And Additional Notes

- The ChEBI aromatic SMILES export is malformed; its default MOL and full InChI were independently parsed and used for identity verification.
- The 2008 primary full HTML and original figures were available and inspected. Its official PMC XML endpoint supplied only an abstract and the publisher PDF was inaccessible; neither unavailable route is represented as a full-text review.
- The final spontaneous ring-closure step remains the original authors' proposal, with enzyme-assisted closure explicitly not ruled out. The review supports observed product formation without claiming the full mechanism.
- The optional expression-context evidence is reused with original access timestamps. The previously attempted precise411 runner searches failed typed-response parsing and are not interpreted as negative biological evidence.
- The plant 2000 original body remains inaccessible after bounded free primary-source searches. The review must retain this required occurrence-verification limitation even though fungal and bacterial occurrences are positively supported.
- The 2013 publisher body was HTTP 403, but an author-uploaded copy of the actual journal article was read through its public full-text transcription, with DOI and journal pages verified. Its official SI was independently retrieved; that SI covers different numbered compounds.
- The 2011 evidence was read as actual primary-paper text on a public mirror. It reports PA14-derived recombinant enzyme work and cites native-metabolite precedent; the original2008 PAO1 study was inspected separately.
- The source authority for the seven claims is the PubChem depositor record, as represented by DATABASE_ASSERTION. Original GENE-TOX 1977 experimental paper and 1986 panel review were not inspected; quantitative toxicity or human effects are not established.
- Four supplementary raw-row endpoints timed out once; successful current CID/SID summary and complete descriptions verify every stored outcome and value. No missing raw curve or titration result is invented.
- AID 624287 protocol does not specify the exact mutant construct or cell line. R201H/R201C occur in assay background and are not asserted to be the tested constructs.
- The configured full identifier-label gate accepts 499 warning-level taxon-label mismatches, 35 explicit exceptions and 4,722 no-adapter pairs across the corpus; its exit 0 is not independent verification of every identifier or of this record's scientific claims.
- The quality suite skips the optional sibling AntibioticMech checkout comparison because the isolated clone has no sibling checkout, and skips three command-frontmatter cases because their parameter sets are empty. Pinned-hash and network governance checks still ran.
- Shared native gates assess deterministic corpus consistency and configured invariants. They do not establish biological production, stereochemical specificity, evidence adequacy or literature-level claim support.
- No scientific record, source inventory, maintained correction table, native curation status or history was edited. These are review observations and proposed curation actions.
- Shared deterministic baseline gates retain their actual command receipts from the identical tracked scientific base. Target strict validation ran afresh. Scientific failed or unavailable checks are distinct from bundle-schema validation.
- Before extending provenance for the actually inspected PubChem extractor, all original source hashes were asserted unchanged. The source attestation includes exact ChEBI and BioAssay owners.
- The sole positive assay is a qualitative bacterial mutagenicity database assertion. No clinical, human-toxicology, direct GNAS-binding or wild-type agonism claim is made.

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
scientific_review: true
review_id: 20261021T082323Z-4-hydroxy-2-quinolone
title: '4-hydroxy-2-quinolone: exact DHQ evidence, tautomer identity and assay scope'
started_at: '2026-10-21T08:09:07.691701Z'
finished_at: '2026-10-21T08:23:23.505462Z'
completion: partial
verdict: needs_curation
summary: Exact normalized chemical identity, native PAO1 formation, fungal and bacterial
  occurrence, and all seven deposited assay calls are supported. One major finding
  identifies omitted native and reconstituted biosynthetic methods; two minor findings
  concern the answerable tautomer naming discussion and missing bacterial mutagenicity
  assay context. The plant occurrence remains unverified because its original paper
  was inaccessible.
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
  - path: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
    sha256: 49af3c5757759ac6fd8ceb7d1575d873d7070433516778682160a10308db1929
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
  - path: scripts/extract_pubchem_bioassay.py
    sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
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
  description: 'One complete owner: chemical identity and tautomerism, grounding and
    xrefs, three occurrence citations, native producer/locus, seven activity results
    and their target, classification, source concepts, naming discussion and audit
    history.'
  selection: Twentieth initially unreviewed path, tenth in batch 002 from fresh origin/main.
    Review starts and saves follow path order. The fresh-main authoritative list has
    91 valid bundles covering 54 of 3,116 records; ten reviews in pending PR 1000
    provide additional campaign coverage. Ignored files were included. This bundle
    has exactly one target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:75926
targets:
- target_id: CHEBI:75926
  path: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
  label: 4-hydroxy-2-quinolone
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
    path: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Exact ChEBI identity, preferred label and definition
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Seven source-deposited activity assertions
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: Assay source-row extraction and provenance
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The entire target has zero ERROR rows; this does not itself verify scientific
    claims.
  target_ids:
  - CHEBI:75926
  command: just validate-strict data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
    --out /private/tmp/npm-review-work/020/strict.tsv
  exit_code: 0
  scope_note: Actual target command finished 2026-10-21T08:09:13.815407Z
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
    Started 2026-10-21T06:36:36.016808+00:00; finished 2026-10-21T06:37:52.997020+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-corpus.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - CHEBI:75926
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
    Started 2026-10-21T06:36:36.016703+00:00; finished 2026-10-21T06:38:35.570687+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/verify-reproduction.log.
    Reused for batch 002 because the tracked source tree and HEAD remain the exact
    same base commit; this command was not rerun for batch 002. The review author
    must assign the exact target_ids.'
  target_ids:
  - CHEBI:75926
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
    Started 2026-10-21T06:36:36.016598+00:00; finished 2026-10-21T06:37:11.018366+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/review-queue.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - CHEBI:75926
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
    Started 2026-10-21T06:36:56.498212+00:00; finished 2026-10-21T06:38:54.776253+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/validate-products.log.
    Reused for batch 002 because the tracked source tree and HEAD remain the exact
    same base commit; this command was not rerun for batch 002. The review author
    must assign the exact target_ids.'
  target_ids:
  - CHEBI:75926
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
    Started 2026-10-21T06:46:02.058886+00:00; finished 2026-10-21T06:54:53.950582+00:00.
    Exact session transcript: /private/tmp/npm-native-checks/qc-attempt4.log. Reused
    for batch 002 because the tracked source tree and HEAD remain the exact same base
    commit; this command was not rerun for batch 002. The review author must assign
    the exact target_ids.'
  target_ids:
  - CHEBI:75926
- check_id: BIO020-EXACT-ROWS
  name: Seven assay calls, measurements and exact deposited structures
  status: passed
  required: true
  summary: All seven current AID/SID/CID rows and both independent deposited structures
    agree with the owner. Five inconclusive outcomes remain NOT_DETERMINED; one inactive
    remains INACTIVE; the one qualitative GENE-TOX positive remains ACTIVE.
  target_ids:
  - CHEBI:75926
  command: .venv/bin/python /private/tmp/npm-review-work/020/compare_bioactivity.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - BIO020-COMPARE
  - BIO020-SUMMARY
  - BIO020-SUBSTANCES
- check_id: BIO020-ASSAY-SCOPE
  name: Assay and protein target scope
  status: passed
  required: true
  summary: Complete official assay descriptions, the exact GENE-TOX row and reviewed
    UniProt entry were inspected. The target accession is valid; no direct activity
    or human-toxicology conclusion follows from the inconclusive cellular screen or
    bacterial mutagenicity row.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - BIO020-DESCRIPTIONS
  - BIO020-GENETOX
  - BIO020-UNIPROT
- check_id: BIO020-RAW-FOUR
  name: Supplementary raw qHTS row and titration details
  status: unavailable
  required: false
  summary: Single bounded raw-row requests for AIDs 2685,504332,624287,624296 returned
    HTTP 504 PUGREST.Timeout. Current exact SID/CID summary values and outcomes plus
    complete assay descriptions succeeded, so verification of the stored database
    claims is complete; unreturned raw titration details are not inferred.
  target_ids:
  - CHEBI:75926
  scope_note: Optional deeper row-detail access; source-specific failed requests and
    error-body hashes are retained in bioactivity-evidence.json.
- check_id: C-IDENTITY
  name: Normalized substance identity and tautomer representations
  status: passed
  required: true
  summary: The owner, official ChEBI default MOL and PubChem structure share a full
    Standard InChI/key. Independent fixed-H comparison retains the lactam/lactim distinction;
    three-star grounding and achiral stereo completeness are supported.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-CHEMISTRY
  - R020-CHEBI
  - R020-CHEBI-MOL
  - R020-PUBCHEM
- check_id: C-BIOLOGICAL-ORIGIN
  name: Exact native and reconstituted product formation
  status: passed
  required: true
  summary: Full original 2008 text and figures show exact native PAO1 DHQ, pqsA/pqsD
    dependence, recombinant-cell formation and standard-matched purified-enzyme product.
    The final ring-closure mechanism remains explicitly proposed.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-PRIMARY2008
  - R020-SCHEME1
  - R020-FIGURE2
  - R020-FIGURE3
- check_id: C-BGC-GRADING
  name: Exact-compound method and native producer grading
  status: failed
  required: true
  summary: The correctly cited original study contains demonstrated methods absent
    from the source-derived CLUSTER_UNSTATED and SOURCE_ASSERTION grades. A compound-specific
    maintained correction is needed.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-RAW
  - R020-MIBIG
  - R020-PRIMARY2008
  - R020-GRADING
  - R020-GUARD
- check_id: C-FUNGAL-OCCURRENCE
  name: Cited fungal exact-compound occurrence
  status: passed
  required: true
  summary: The actual 2013 primary paper explicitly reports exact 4-hydroxyquinolin-2(1H)-one
    isolated from MM3S-3 rice culture; host-plant tissue is not substituted for the
    fungal culture.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-FUNGAL-PRIMARY
  - O020-FUNGAL-SI
- check_id: C-BACTERIAL-OCCURRENCE
  name: Bacterial occurrence and citation scope
  status: passed
  required: true
  summary: The cited 2011 paper attributes the metabolite to P. aeruginosa and studies
    recombinant PA14 enzyme; its 2008 reference directly demonstrates native PAO1
    occurrence. These distinct scopes are preserved.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-BACTERIAL-CITED2011
  - O020-BACTERIAL-PRIMARY2008
- check_id: C-PLANT-OCCURRENCE
  name: Exact Haplophyllum occurrence in the cited original
  status: unavailable
  required: true
  summary: The original 2000 body remains inaccessible after bounded free routes.
    Bibliographic and taxon identity are confirmed, but exact compound, sampled tissue
    and identification method cannot be certified.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-PLANT-REFERENCE
  - O020-PLANT-ACCESS
  - O020-TAXA
- check_id: C-TAXON-LOCUS
  name: Organism identifiers and deposited locus
  status: passed
  required: true
  summary: NCBI/Wikidata identities agree; PAO1 accession AE004091.2 contains pqsA/PA0996
    and pqsD/PA0999 within the stored interval.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-TAXA
  - O020-WIKIDATA
  - R020-GENOME
- check_id: C-IMODULON
  name: Native expression-context applicability
  status: passed
  required: false
  summary: Previously retrieved PAO1-lineage component membership includes pqsA/pqsD.
    It is optional regulatory context and is not used as exact-compound formation
    proof.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-imodulon-component85-context
  - R020-imodulon-dataset-strain-context
evidence:
- evidence_id: R020-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
  locator: Entire owner, resolved content, all seven assays, three occurrences, two
    source concepts and four seed-history events
  accessed_at: '2026-10-21T08:20:52.053920Z'
  support: supports
  summary: One achiral neutral compound has three database occurrence assertions,
    one PAO1 producer and BGC0000922 locus, seven PubChem assays, one assay target
    and an open naming discussion. The resolved record has no causal graph, graph
    references, biosynthetic pathway, separate molecular-target list, sibling relation
    or clinical claim.
  snapshot_sha256: 49af3c5757759ac6fd8ceb7d1575d873d7070433516778682160a10308db1929
- evidence_id: R020-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Entire matching BGC0000922:2 raw row, cross-checked with the complete source-row
    extraction
  accessed_at: '2026-10-21T08:20:52.053920Z'
  support: supports
  summary: The raw version-5 row has exact full key HDHQZCHIXUUSMK-UHFFFAOYSA-N, no
    locus methods, PAO1 taxon 208964, AE004091.2 bounds 1073960..1087095 and DOI:10.1074/jbc.m804555200.
    Its canonical row SHA256 is b8c6cb52b474b3b4fb8b35af4103051a086ea612cf1773cd5becde2ec0fa0b21.
    The output faithfully preserves these source fields.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: R020-CHEMISTRY
  kind: validation
  reference: /private/tmp/npm-review-work/020/identity-comparison.json
  locator: Independent RDKit reconstruction of owner, current default ChEBI MOL and
    PubChem graph; Standard and fixed-H InChIs
  accessed_at: '2026-10-21T08:13:57.748261Z'
  support: supports
  summary: All three representations have formula C9H7NO2, net charge zero, no stereocentres
    and identical full Standard InChI/key. The owner is 2,4-quinolinediol; the current
    ChEBI MOL and PubChem graph are 4-hydroxyquinolin-2(1H)-one. Their fixed-H InChIs
    differ, documenting tautomeric representation rather than identical fixed-H graphs.
    stereo_complete:true is appropriate.
  snapshot_sha256: 91547c01722981e3c3140bc519b2d9650df31d6b0a5713f4519660c90b65f936
- evidence_id: R020-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/75926/
  locator: Complete released three-star entry, default InChI/key, definition, names,
    CAS and ontology
  accessed_at: '2026-10-21T08:11:55.994823Z'
  support: supports
  summary: CHEBI:75926 remains an eligible three-star exact Standard-InChIKey grounding.
    Its definition and preferred name describe the keto tautomer. The exported aromatic
    SMILES omits the required pyrrolic H, so that string is not used as the decisive
    graph; its official default MOL independently resolves the intended structure.
  snapshot_sha256: ed92fa9e8bfb529a65bce3b72ea76087bc085c686179b7706629318c1dee378f
- evidence_id: R020-CHEBI-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/75926/
  locator: Complete default molfile parsed independently
  accessed_at: '2026-10-21T08:11:55.996582Z'
  support: supports
  summary: The default MOL encodes the neutral keto tautomer with the owner full Standard
    InChIKey. It supports the shared substance identity while retaining the fixed-H
    distinction.
  snapshot_sha256: 28b9806160117df4c9cea9fe0d30be1202b191b376fe6e3d0674259d41a68c5d
- evidence_id: R020-PUBCHEM
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54680871/property/InChI,InChIKey,MolecularFormula,IsomericSMILES/JSON
  locator: Complete CID 54680871 property response
  accessed_at: '2026-10-21T08:11:55.996954Z'
  support: supports
  summary: The sole owner PubChem xref resolves to the same full Standard InChI/key
    and C9H7NO2. It is chemical identity evidence, not an independent producer or
    activity experiment.
  snapshot_sha256: 0e8917626d8d6b16b50995bb84e8fc8d8ef1ef4e0a245870fdb859e6cacd98cb
- evidence_id: R020-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000922.5/annotations.json
  locator: Complete version-5 entry, compound 2, taxonomy, locus and evidence fields
  accessed_at: '2026-10-21T08:11:56.795484Z'
  support: supports
  summary: The current MIBiG entry reproduces the pinned 2,4-Quinolinediol structure,
    authentic-standard compound citation, PAO1 taxon and locus interval. The locus
    evidence array is empty; the current database therefore does not itself supply
    the missing methods.
  snapshot_sha256: 4a0a7ba2613b8d00da9d26de516bf58578a727fe9997d6312dcdbd9eb5e078af
- evidence_id: R020-PRIMARY2008
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2570881/
  locator: DOI:10.1074/jbc.M804555200, PMID:18728009; complete original main body,
    Experimental Procedures, DHQ Production, Figures 2/3 and discussion
  accessed_at: '2026-10-21T08:12:51.776840Z'
  support: supports
  summary: Native PAO1 pqsA deletion and nonpolar pqsD disruption eliminate detectable
    exact DHQ, whereas pqsB and pqsC mutants retain it. The pqsA deletion was PCR/sequencing
    verified; the study describes 189-bp residual insertions for the other mutants.
    PqsA plus PqsD also produces DHQ in E. coli. Purified N-terminal His-tagged PqsA/PqsD
    form the authentic-standard-matched product from anthranilate/CoA and malonyl-CoA
    or malonyl-ACP. The proposed spontaneous final ring closure is explicitly uncertain;
    the paper does not prove that detailed step.
  snapshot_sha256: e5fad92f5789b7fb17839c6ffbee765bc6c6f793b4d4cbf0a3a51ce7dd45f082
- evidence_id: R020-SCHEME1
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/bb95/2570881/0701a5dcf469/zbc046085462s001.jpg
  locator: Original Scheme 1, directly visually inspected
  accessed_at: '2026-10-21T08:14:16.417836Z'
  support: supports
  summary: The original drawing distinguishes DHQ from HHQ and PQS and depicts DHQ
    in the enol representation used by the MIBiG-derived owner.
  snapshot_sha256: ad434bd4f66327197377f6c8b2c6ba968360246f1a1b953f75d07c200f19a00a
- evidence_id: R020-FIGURE2
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/bb95/2570881/93a6665f25e1/zbc0460854620002.jpg
  locator: Original Figure 2 panels A–C, directly visually inspected
  accessed_at: '2026-10-21T08:14:16.418254Z'
  support: supports
  summary: Native wild-type and pqsA spent-medium profiles, radiolabeled native mutant
    lanes and recombinant-cell lanes support the stated DHQ-specific distinctions.
    Native pqsA/pqsD loss and PqsA-plus-PqsD recombinant formation concern the exact
    target, not a sibling quinolone.
  snapshot_sha256: 07cbaac9ba67fbf0f57ebc731816621b5a4abf052b6346cfd73a3cfd9a933df7
- evidence_id: R020-FIGURE3
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/bb95/2570881/6dfb7a8774f5/zbc0460854620003.jpg
  locator: Original Figure 3 panels A–D, directly visually inspected with caption
  accessed_at: '2026-10-21T08:14:16.418404Z'
  support: supports
  summary: Malonyl-CoA and malonyl-ACP support product formation; malonic acid does
    not. Product and authentic DHQ coelute at 3.67 minutes and share protonated m/z
    162 with the reported fragments. PqsA alone instead forms anthraniloyl-CoA.
  snapshot_sha256: 15ded1399bee0f69da535fdc4feddabf53033d54c972bb7d5404f8cd4c865cb5
- evidence_id: R020-GENOME
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=AE004091.2&db=nuccore&report=genbank&retmode=text&from=1073960&to=1087095
  locator: AE004091.2 exact owner interval; source and complete FEATURES section re-inspected
    for this target
  accessed_at: '2026-10-21T07:17:15.132327Z'
  support: supports
  summary: The interval is explicitly PAO1 taxon 208964 and contains pqsA/PA0996 (AAG04385.1,
    relative 4503..6056) and pqsD/PA0999 (AAG04388.1, relative 7983..8996). This links
    the native genes in the 2008 experiment to the stored locus. No historical expression-construct
    sequence equivalence is claimed.
  snapshot_sha256: 330511e0ab7b1880d773dcf8f12963ad08388969aac89c63854fdd87c7fe012f
- evidence_id: R020-GRADING
  kind: record_content
  reference: conf/producer_evidence.tsv
  locator: Complete controlled method table and organism-versus-cluster rules
  accessed_at: '2026-10-21T08:20:52.053920Z'
  support: supports
  summary: Knock-out studies grade both the native producer and locus. Enzymatic assays
    and Heterologous expression grade the locus only. Combining the supported methods
    yields BGC_CHARACTERIZED for native PAO1 and CLUSTER_DEMONSTRATED for this exact
    compound.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: R020-GUARD
  kind: record_content
  reference: src/naturalproductmech/curate/claim_references.py
  locator: Complete claim-reference loader and application, reconciled with seed_from_sources.py
    method loader
  accessed_at: '2026-10-21T08:20:52.053920Z'
  support: context_only
  summary: The citation overlay validates the complete raw source-row SHA256. REPLACE
    method overrides currently ignore expected_* fields, unlike WITHDRAW. A paired
    exact-row citation overlay retaining the correct DOI can guard this method update;
    alternatively extend and test the method loader. No structure replacement is needed
    here.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: R020-CLASSIFIER
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Complete exact-full-key model row
  accessed_at: '2026-10-21T08:20:52.053920Z'
  support: context_only
  summary: The stored ALKALOIDS filing and Anthranilic acid alkaloids/Quinazoline
    alkaloids predictions reproduce the pinned model output. The graph contains one
    nitrogen; Quinazoline alkaloids is therefore retained only as a computational
    class prediction, not a validated literal ring identity or biosynthetic experiment.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: R020-DISCUSSION
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: CURATOR_OWNED_DISCUSSION_FIELDS and preservation by discussion_id
  accessed_at: '2026-10-21T08:20:52.053920Z'
  support: context_only
  summary: The existing status, resolved_date, resolution_note and evidence are curator-owned
    preserved fields. An evidence-backed answer can persist through reseeding while
    the source labels and generated prompt retain their provenance.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: R020-imodulon-component85-context
  kind: database
  reference: https://imodulondb.org/api/imodulons/p_aeruginosa/precise364/85/genes
  locator: Exact component-membership JSON endpoint used by installed runner get_imodulon_genes;
    verified HTTP200 and matching seven-gene payload; imodulon-component85-source.json
    plus source-access receipt. Original runner summary and context receipts retained.;
    previously fetched evidence reused with original timestamp, no new search claimed
  accessed_at: '2026-10-21T07:25:32Z'
  support: context_only
  summary: The complete seven-member PAO1-lineage component includes pqsA/PA0996 and
    pqsD/PA0999 alongside pqsB/C/E and phnAB. This is relevant native expression context
    only; no exact-DHQ measurement, necessity or catalytic rate follows from component
    membership.
- evidence_id: R020-imodulon-dataset-strain-context
  kind: primary_source
  reference: https://academic.oup.com/nar/article/50/7/3658/6561658
  locator: DOI:10.1093/nar/gkac187; Methods, RNA extraction and Data acquisition;
    Results, iModulon structure of the transcriptome; dataset link; previously fetched
    evidence reused with original timestamp, no new search claimed
  accessed_at: '2026-10-21T07:21:25Z'
  support: context_only
  summary: The dataset's primary publication explicitly links aeruPRECISE364 to the
    inspected database dataset. It reports PAO1 and PAO1 delta-mexB expression profiles,
    comprising 364 quality-filtered samples (83 new and 281 public), mapped to PAO1
    genome NC_002516.2. Thus this is relevant PAO1 lineage regulatory context, not
    a PA14 assay. The runner's dataset catalogue independently labels p_aeruginosa/precise364
    as Pseudomonas aeruginosa but supplies no strain field; the strain attribution
    comes from the primary methods.
- evidence_id: O020-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
  locator: Entire owner and resolved source rows read; this subtask audits all three
    occurrence objects
  accessed_at: '2026-10-21T08:16:34.063464Z'
  support: supports
  summary: 'The owner has three LOTUS DATABASE_ASSERTION occurrences: Haplophyllum
    bucharicum/DOI 10.1007/BF02238348, Pseudomonas aeruginosa/DOI 10.1002/CBIC.201100014
    and Penicillium citrinum/DOI 10.1021/NP4001366, all joined by HDHQZCHIXUUSMK-UHFFFAOYSA-N.
    Their plant, bacterial and fungal taxa must be evaluated separately from the PAO1
    producer and enzyme claims.'
  snapshot_sha256: 49af3c5757759ac6fd8ceb7d1575d873d7070433516778682160a10308db1929
- evidence_id: O020-PUBMED
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=18728009,21425231,23713692&retmode=xml
  locator: DOI/PMID mappings and complete abstracts of 2008,2011,2013 references
  accessed_at: '2026-10-21T08:11:56.502008Z'
  support: supports
  summary: PMID 18728009 maps to DOI 10.1074/jbc.M804555200, PMID 21425231 to DOI
    10.1002/cbic.201100014 and PMID 23713692 to DOI 10.1021/np4001366. The 2013 abstract
    describes an endophytic P. citrinum culture but does not enumerate this known
    compound; its full article is needed for that exact occurrence.
  snapshot_sha256: 75ce892a3f46197690d6363e6409c627ea26700bbd2ff9259c4498f23a106156
- evidence_id: O020-PLANT-REFERENCE
  kind: authority
  reference: https://api.crossref.org/works/10.1007/BF02238348
  locator: Official title, author, journal and pagination for DOI 10.1007/BF02238348
  accessed_at: '2026-10-21T08:14:22.440004Z'
  support: context_only
  summary: The DOI identifies I.A.Bessonova, Components of Haplophyllum bucharicum,
    Chemistry of Natural Compounds36(2000):323–324. Bibliographic identity is confirmed,
    but it does not independently establish the exact compound, plant part or isolation
    method.
  snapshot_sha256: 1a3f9891a7a02f1573d3a33d9f866be9a83f30eeccfb8fc3f7b2099ff85a343c
- evidence_id: O020-PLANT-ACCESS
  kind: search
  reference: https://api.openalex.org/works/https://doi.org/10.1007/BF02238348
  locator: Closed work locations; official article/PDF access responses inspected
    in primary2000.html and primary2000.pdf
  accessed_at: '2026-10-21T08:14:22.440253Z'
  support: unknown
  summary: Only the publisher location was identified. Both purported publisher HTML/PDF
    responses are 3038-byte Client Challenge HTML, not article text or a PDF. Bounded
    DOI/title/author searches did not yield a readable original body. Later reviews
    and citation snippets were used only as discovery leads; the plant occurrence
    remains unverified.
  snapshot_sha256: 5e87bd4afc4c9db7b1e7d0f29e6aad3a85a55287f1ac0369b8856170c3f111d9
  search_scope: Exact DOI 10.1007/BF02238348; exact Components of Haplophyllum bucharicum
    title with Bessonova,323–324 and PDF; author/species/exact4-hydroxy name queries;
    Crossref/OpenAlex and official Springer article/PDF. No inference of chemical
    absence from access failure.
- evidence_id: O020-FUNGAL-PRIMARY
  kind: primary_source
  reference: https://www.researchgate.net/publication/275582227_Alkaloids_and_Polyketides_from_Penicillium_citrinum_an_Endophyte_Isolated_from_Ceratonia_siliqua
  locator: 'Author-uploaded actual J.Nat.Prod.2013,76:1099–1104 body: Results p1099,
    Fungal Material and Extraction/Isolation p1103; journal DOI footers verified'
  accessed_at: '2026-10-21T08:14:42Z'
  support: supports
  summary: The original article explicitly lists 4-hydroxyquinolin-2(1H)-one and reports
    1.8 mg isolated from rice cultures of P. citrinum MM3S-3. The endophyte came from
    a Moroccan Ceratonia siliqua stem; ITS accession JQ901861 is reported. This establishes
    fungal-culture occurrence, not occurrence in the host plant. The page’s conference
    wrapper is separate from the uploaded journal article identified by its DOI/page
    footers.
  snapshot_sha256: d3a6f054f406ebf555bcd4ec609021d4228961c61306ba7e0ff3a172ad8cd47d
- evidence_id: O020-FUNGAL-SI
  kind: primary_source
  reference: https://ndownloader.figshare.com/files/4040869
  locator: Official Figshare file 4040869, article 2401162; title page and complete
    42-page table of contents
  accessed_at: '2026-10-21T08:14:45.665478Z'
  support: context_only
  summary: The official supplement matches DOI 10.1021/np4001366 and provides spectra
    for new compounds 1–6. The target is a known compound, so its occurrence is supported
    by the explicit main-body isolation statement rather than these other compounds’
    spectra. No target spectrum reinterpretation is claimed.
  snapshot_sha256: fb9ee106d4b40c6bce417bf35185f369379fa25927b5ea4a349ba8344f0086d0
- evidence_id: O020-BACTERIAL-CITED2011
  kind: primary_source
  reference: https://www.lookchem.com/FreePDFArticle_13283-92-6_20071976.htm
  locator: Actual primary ChemBioChem2011,12:850–853 body; p 850 intro, p 851 DHQ
    kinetic control, p 853 ref 15 and conclusion; public full-text transcription inspected
  accessed_at: '2026-10-21T08:14:31Z'
  support: partial
  summary: The authors identify DHQ as a P. aeruginosa metabolite, citing Zhang2008,
    then study PqsD cloned from PA14 and expressed in E. coli. Their DHQ experiment
    is a purified-enzyme kinetic control. Native-culture occurrence is contextual
    attribution, not a new native isolation established by those assays. This supports
    the substance/species attribution at its stated scope.
  snapshot_sha256: f57e32ac4d93d99d404fe6447e20b59ffc7401637630161bb398afdd72fbda91
- evidence_id: O020-BACTERIAL-PRIMARY2008
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2570881/
  locator: 'PMC2570881: Experimental Procedures; DHQ Production in the pqs Operon
    Mutants; Figure 2; re-read08:15:11Z'
  accessed_at: '2026-10-21T08:12:51.776840Z'
  support: supports
  summary: The original Zhang2008 study directly analyzes extracellular DHQ in wild-type
    PAO1 spent medium by LC-MS, with authentic DHQ standards and radiolabeled anthranilate
    experiments. It distinguishes DHQ from HHQ/PQS and tests native pqs mutants. This
    provides direct primary support for P. aeruginosa occurrence, with PAO1 strain
    scope; recombinant PA14 experiments are not substituted for it.
  snapshot_sha256: e5fad92f5789b7fb17839c6ffbee765bc6c6f793b4d4cbf0a3a51ce7dd45f082
- evidence_id: O020-TAXA
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1006069,287,5077,208964&retmode=xml
  locator: NCBI 1006069,287,5077,208964 names/ranks/lineages
  accessed_at: '2026-10-21T08:11:56.527719Z'
  support: supports
  summary: The three occurrence IDs resolve to H. bucharicum, P. aeruginosa and P.
    citrinum respectively; 208964 is PAO1. Their land-plant, bacterial and fungal
    groups agree. This validates taxonomic identity, not exact-metabolite detection.
  snapshot_sha256: 87677863b27c845e59bbb21db5b2b853b1033812ac269f861a3d4c186360dc09
- evidence_id: O020-WIKIDATA
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q18082667%7CQ31856%7CQ10622902&props=labels%7Cclaims&languages=en&format=json
  locator: Entities Q18082667,Q31856,Q10622902 labels and P225/P685; independently
    inspected against occurrence taxa
  accessed_at: '2026-10-21T08:11:56.542683Z'
  support: supports
  summary: The three provenance entities identify the corresponding plant, bacterium
    and fungus with matching NCBI taxonomy links. They remain provenance references,
    not primary isolation proof.
  snapshot_sha256: 9e09ee1114da11574c0b61886948ad24230c17a937fb5e94c8b7ff6c3f7cb61c
- evidence_id: BIO020-SUMMARY
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/54680871/assaysummary/JSON
  locator: /private/tmp/npm-review-work/020/bioactivity/cid54680871-assaysummary.json
  accessed_at: '2026-10-21T08:13:59.882599Z'
  support: supports
  summary: 'All seven owner AIDs are present for CID 54680871: AID 1030 is Inactive
    at 5.0119uM; AIDs 2147,2685,504332,624287,624296 are Inconclusive at 39.8107,0.206,79.4328,3.9811,8.1995uM
    respectively; AID 1259408 is Active without a numeric endpoint. Six qHTS rows
    use SID 24789721; GENE-TOX uses SID 363895103. Values are source Potency endpoints,
    not evidence that the inactive or inconclusive calls are positive.'
  snapshot_sha256: 71aa53608fa3310d90fa81a60b34c93fdb0a390fc6dfd0c168a770556a7e596b
- evidence_id: BIO020-SUBSTANCES
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/24789721,363895103/JSON
  locator: /private/tmp/npm-review-work/020/bioactivity/substances.json
  accessed_at: '2026-10-21T08:14:59.629094Z'
  support: supports
  summary: Both deposited substance records standardize to CID 54680871. Independently
    reconstructed raw atom/bond graphs give C9H7NO2 and full InChIKey HDHQZCHIXUUSMK-UHFFFAOYSA-N,
    exactly matching this owner. MLSMR SID 24789721 is MLS000716246; GENE-TOX SID
    363895103 names 2,4-dihydroxyquinoline.
  snapshot_sha256: 13b67fd152223485d57265335f008aa0c4899ba9095146fa26a6b880b2417be5
- evidence_id: BIO020-DESCRIPTIONS
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1030,1259408,2147,2685,504332,624287,624296/description/JSON
  locator: /private/tmp/npm-review-work/020/bioactivity/seven-assay-descriptions.json
  accessed_at: '2026-10-21T08:13:59.301127Z'
  support: supports
  summary: The complete official descriptions distinguish ALDH fluorescence, JMJD2E
    coupled fluorescence, G9a AlphaScreen, Drosophila S3 lipid imaging, MCF10a DNA-content
    imaging and GNAS/gsp cell cAMP HTRF. G9a warns of assay interference. AID 624287
    concerns activating gsp mutations and a cellular cAMP readout; background names
    R201H/R201C, but the inspected protocol does not identify the actual mutant construct
    or cell line. It does not establish direct protein binding or wild-type agonism.
  snapshot_sha256: f6bacbee567165731ff6dda19f1ea70de018a7edc05dcb468fda5d40ae46df77
- evidence_id: BIO020-GENETOX
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1259408/JSON?sid=363895103
  locator: PC_AssaySubmit.data[0], SID 363895103; results tids 1,3,5,6,8,9,10
  accessed_at: '2026-10-21T08:17:33.711399Z'
  support: supports
  summary: The exact deposited row is positive in a Salmonella typhimurium histidine
    reverse-mutation (Ames) assay with metabolic activation. It specifies one or more
    of five standard tester strains, not an individual strain. No dose or dose-response
    is supplied. This archived database assertion is narrower than human toxicity,
    carcinogenicity or systemic toxin activity; results without activation are not
    supplied.
  snapshot_sha256: 1583cf55b7d12b254ff4e5c8994bc4a2471439b8c508e56edc7030a9da8fae41
- evidence_id: BIO020-ALDH-ROW
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1030/JSON?sid=24789721
  locator: /private/tmp/npm-review-work/020/bioactivity/aid1030-sid24789721.json
  accessed_at: '2026-10-21T08:15:18.235111Z'
  support: supports
  summary: Exact SID 24789721 row retains the depositor Inactive outcome despite fitted
    Potency 5.0119uM and an Activator phenotype/single-point activity label. The stored
    INACTIVE call correctly takes precedence over an inference from the number.
  snapshot_sha256: 4257591162d76ec7bb6af91d96a37c04912d8741ca97059eb299522dfcf30cf6
- evidence_id: BIO020-JMJD-ROW
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/2147/JSON?sid=24789721
  locator: /private/tmp/npm-review-work/020/bioactivity/aid2147-sid24789721.json
  accessed_at: '2026-10-21T08:15:37.800571Z'
  support: supports
  summary: Exact SID 24789721 row retains the depositor Inconclusive outcome with
    Potency 39.8107uM and a single-point activity label. Stored NOT_DETERMINED with
    the original source outcome in notes is faithful.
  snapshot_sha256: 611d93df971675f592a39500aba614b5165ca19ffd12ea04101a10750694056a
- evidence_id: BIO020-UNIPROT
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P63092.json
  accessed_at: '2026-10-21T08:11:56.825089Z'
  support: supports
  summary: P63092 is reviewed human GNAS, the G(s) alpha short-isoform entry, with
    GTPase function and cAMP signaling. It is a legitimate protein grounding for assay
    target metadata, not a mutant-specific protein accession or evidence that this
    compound binds or activates it.
  snapshot_sha256: 84206ab2d6036ee098c23efb882224d6882ff4981b3435441fe70465280c2899
- evidence_id: BIO020-COMPARE
  kind: validation
  reference: /private/tmp/npm-review-work/020/bioactivity/bioactivity-comparison.json
  accessed_at: '2026-10-21T08:17:18.049528Z'
  support: supports
  summary: RDKit 2026.03.5 reconstructs both raw deposited graphs to the exact owner
    full key. All seven owner calls, numeric values, endpoint names, target accessions
    and inventory rows agree with the current authoritative summary.
  snapshot_sha256: 0659a82016b8fa474e7a793dc98e6b48632c22bcb5f511bde45fa6551befb607
- evidence_id: BIO020-PIPELINE
  kind: record_content
  reference: scripts/extract_pubchem_bioassay.py
  locator: Entire extractor read; scripts/seed_from_sources.py classification and
    bioactivity construction sections; seven exact data/raw/pubchem_bioassay.tsv rows
  accessed_at: '2026-10-21T08:22:03.536829Z'
  support: supports
  summary: The extractor preserves summary outcomes, values, endpoint and target metadata
    but has no protocol/context columns. The seeder maps non-active/non-inactive outcomes
    to NOT_DETERMINED and keeps source outcome notes; Potency remains OTHER. Only
    explicitly ACTIVE rows contribute activity classes; the mutagenicity-title rule
    assigns TOXIN to this GENE-TOX row. Current source-to-owner reproduction is faithful,
    while protocol scope is omitted.
  snapshot_sha256: 24f9d794e7cf97c420351cb751f8767f7d81a5f22aed01669b2318d6755e7c00
assessments:
- assessment_id: R020-IDENTITY
  area: identity
  topic: Exact substance, tautomer distinction and ChEBI eligibility
  outcome: supported
  summary: All chemical identity fields are internally coherent. ChEBI exact grounding
    follows the repository full Standard-InChIKey policy. The two names denote tautomers
    with the same normalized substance key, so a shared key alone must not be described
    as identical fixed-H graphs. The primary Scheme 1 independently depicts the source
    enol form.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-CHEMISTRY
  - R020-CHEBI
  - R020-CHEBI-MOL
  - R020-PUBCHEM
  - R020-SCHEME1
- assessment_id: R020-ORIGIN
  area: identity
  topic: Biological origin and experimental versus proposed chemistry
  outcome: supported
  summary: Native PAO1 medium contains exact DHQ. Native knockouts, recombinant formation
    and purified-enzyme product identification support the NATURAL_PRODUCT assertion.
    The uncertain final cyclization mechanism does not make the observed biological
    product a synthetic derivative. No detailed causal mechanism is asserted in the
    owner.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-PRIMARY2008
  - R020-FIGURE2
  - R020-FIGURE3
- assessment_id: R020-GRADE
  area: evidence
  topic: Native producer and exact-compound locus evidence
  outcome: concern
  summary: The source-derived low grades are faithfully imported, but the record already
    cites the paper that demonstrates the exact PAO1 pqsA/pqsD requirement and recombinant/purified-enzyme
    formation. Capture these methods through maintained source-pinned curation. Preserve
    the distinction between native knockout evidence and heterologous/enzymatic evidence.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-RAW
  - R020-MIBIG
  - R020-GENOME
  - R020-PRIMARY2008
  - R020-GRADING
- assessment_id: R020-CLASSIFICATION
  area: provenance
  topic: Computed classification and asserted source classes
  outcome: supported
  summary: The model-versioned predictions match the exact-key inventory; the Quinazoline
    class is not a literal structural adjudication. PKS and Anthranilic acid-derived/Cyclic
    polyketide reproduce MIBiG. The original precursor and condensation evidence is
    compatible with the broad anthranilate-derived interpretation. No unsupported
    manual replacement of model output is proposed.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-CLASSIFIER
  - R020-RAW
  - R020-PRIMARY2008
- assessment_id: R020-HISTORY
  area: provenance
  topic: Source concepts, history and unresolved naming discussion
  outcome: concern
  summary: Both minted source concepts and four seed events are internally consistent
    with SEEDED status. The existing name-disagreement question is answerable by tautomer
    normalization and the independently inspected fixed-H structures; its resolution
    remains missing.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-OWNER
  - R020-CHEMISTRY
  - R020-CHEBI
  - R020-DISCUSSION
- assessment_id: R020-COVERAGE
  area: completeness
  topic: All owner claims and optional absent fields
  outcome: not_applicable
  summary: Every source concept, definition, xref, classification, occurrence, assay,
    producer/locus, discussion and history field is addressed across the root and
    specialist assessments. The complete resolved owner has no causal graphs, pathway
    steps, graph references, sibling assertions or clinical claims. Optional annotation
    expansion is not required by this review.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-OWNER
- assessment_id: R020-EXPRESSION
  area: evidence
  topic: Native expression-context applicability
  outcome: supported
  summary: Previously inspected aeruPRECISE364 data provide matching PAO1-lineage
    pqsA/pqsD component context. Its primary methods include PAO1 and PAO1 delta-mexB.
    This optional evidence does not change any exact-compound grade or substitute
    for the primary knockout experiment.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - R020-imodulon-component85-context
  - R020-imodulon-dataset-strain-context
- assessment_id: O020-PLANT
  area: evidence
  topic: Haplophyllum bucharicum cited occurrence
  outcome: unknown
  summary: The bibliographic reference is genuine and species-specific, but the original
    content was unavailable. Exact occurrence, sampled plant part and compound identification
    remain unknown. No removal or certainty upgrade follows from the bounded access
    failure.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-OWNER
  - O020-PLANT-REFERENCE
  - O020-PLANT-ACCESS
  - O020-TAXA
- assessment_id: O020-FUNGAL
  area: evidence
  topic: Penicillium citrinum exact occurrence
  outcome: supported
  summary: The cited journal paper directly reports the exact known compound from
    a rice culture of MM3S-3. This supports the species-level occurrence as an isolation
    report; it is not silently generalized to Ceratonia host tissue or every P. citrinum
    strain. The current DATABASE_ASSERTION classification remains honest about the
    imported source.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-FUNGAL-PRIMARY
  - O020-FUNGAL-SI
  - O020-PUBMED
  - O020-OWNER
  - O020-TAXA
- assessment_id: O020-BACTERIAL
  area: evidence
  topic: Pseudomonas aeruginosa occurrence and citation scope
  outcome: supported
  summary: 'The cited 2011 paper recognizes the exact species-metabolite relationship,
    while direct native detection is established by its 2008 primary reference in
    PAO1. Keep that distinction visible: purified PA14 PqsD kinetics are not a separate
    native isolation. The import is not contradicted, so no unsupported-triple exclusion
    is proposed.'
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-BACTERIAL-CITED2011
  - O020-BACTERIAL-PRIMARY2008
  - O020-PUBMED
  - O020-OWNER
- assessment_id: O020-PROVENANCE
  area: evidence
  topic: Taxonomic provenance and occurrence/producer separation
  outcome: supported
  summary: All three taxon IDs and Wikidata organism URIs resolve consistently. The
    occurrence objects retain DATABASE_ASSERTION and do not themselves promote plant
    or fungal producers. The PAO1 producer/locus and chemical tautomer equivalence
    are assessed separately in this review.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - O020-TAXA
  - O020-WIKIDATA
  - O020-OWNER
- assessment_id: BIO020-FIDELITY
  area: evidence
  topic: Exact structure and assay-result fidelity
  outcome: supported
  summary: Every stored database result is for the exact deposited structure and reproduces
    the current authoritative outcome and endpoint. Fitted potency values do not override
    inactive or inconclusive calls. Ungrounded non-UniProt accessions remain transparently
    recorded; no replacement protein identifiers were guessed.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - BIO020-SUMMARY
  - BIO020-SUBSTANCES
  - BIO020-COMPARE
  - BIO020-ALDH-ROW
  - BIO020-JMJD-ROW
- assessment_id: BIO020-GNAS
  area: scope
  topic: Mutant-oriented cell cAMP assay and human GNAS grounding
  outcome: supported
  summary: P63092 correctly identifies the human GNAS assay target. AID 624287 is
    an inconclusive cell-based cAMP HTRF screen directed at gsp activating mutations.
    The background mentions R201H/R201C but does not establish which mutant construct
    was tested in the inspected protocol. The current NOT_DETERMINED observation supports
    neither direct protein action nor wild-type GNAS agonism.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - BIO020-DESCRIPTIONS
  - BIO020-UNIPROT
  - BIO020-SUMMARY
- assessment_id: BIO020-GENETOX-SCOPE
  area: completeness
  topic: Bacterial mutagenicity scope behind the TOXIN summary
  outcome: concern
  summary: The sole positive bioactivity is an archived Salmonella Ames result with
    metabolic activation. The generated record retains a generic mutagenicity title
    and coarse TOXIN class but omits this available assay context. The classification
    follows the repository mapping; it should not be interpreted as proven human or
    systemic toxicity, and the positive should not be deleted merely because it is
    qualitative.
  target_ids:
  - CHEBI:75926
  evidence_ids:
  - BIO020-GENETOX
  - BIO020-PIPELINE
findings:
- finding_id: R020-MISSING-METHODS
  issue_key: bgc0000922-compound2-missing-exact-dhq-methods
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The cited primary study demonstrates exact DHQ formation but both grades
    remain at source level
  description: BGC0000922 compound 2 has no imported locus method and remains CLUSTER_UNSTATED
    with a SOURCE_ASSERTION PAO1 producer. Its existing 2008 citation directly demonstrates
    native pqsA/pqsD loss, E. coli PqsA/PqsD formation and purified-enzyme formation
    of authentic-standard-matched DHQ. This materially understates the exact compound
    evidence; it is not a transferred result from HHQ or PQS.
  target_ids:
  - CHEBI:75926
  field_paths:
  - producer_organisms[0].evidence_basis
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  evidence_ids:
  - R020-RAW
  - R020-PRIMARY2008
  - R020-FIGURE2
  - R020-FIGURE3
  - R020-GENOME
  - R020-GRADING
  - R020-GUARD
  rule_id: 'review-yaml-record: evidence completeness; conf/producer_evidence.tsv:
    independent organism and locus grading'
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Compound-specific supported method correction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Full raw-row source guard and explicit primary citation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Method override consumption and deterministic generation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Exact raw-row digest enforcement
- finding_id: R020-NAMES
  issue_key: chebi75926-tautomer-name-discussion-unresolved
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: The open naming question can be resolved as a tautomer representation difference
  description: The current discussion treats the two labels as a possible upstream
    structure error. Independent reconstruction shows a lactam/lactim tautomer pair
    with identical Standard InChI but different fixed-H representations. The primary
    drawing matches the source enol representation. Record that evidence-backed distinction
    without replacing a coherent owner structure or treating the names as identical
    fixed-H graphs.
  target_ids:
  - CHEBI:75926
  field_paths:
  - discussions[0]
  evidence_ids:
  - R020-OWNER
  - R020-CHEMISTRY
  - R020-CHEBI-MOL
  - R020-SCHEME1
  - R020-DISCUSSION
  rule_id: 'review-yaml-record: adjudicate concrete open questions; docs/CURATION.md'
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
    role: Curator-owned resolution of name-disagreement
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Preserves curator discussion answer fields
- finding_id: BIO020-F1
  issue_key: chebi-75926-genetox-assay-context-omitted
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Positive GENE-TOX row omits bacterial assay and metabolic-activation context
  description: AID 1259408 SID 363895103 explicitly records a positive Salmonella
    typhimurium Ames assay with metabolic activation. The owner stores only a generic
    GENE-TOX mutagenicity title and TOXIN class. Add the inspected assay context so
    users can distinguish the supported bacterial test from untested human toxicity.
    The row does not identify an individual tester strain or provide dose-response,
    and it does not establish that activity requires metabolic activation.
  target_ids:
  - CHEBI:75926
  field_paths:
  - bioactivities[6]
  - bioactivity_summary
  evidence_ids:
  - BIO020-GENETOX
  - BIO020-PIPELINE
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: Effective extraction of exact assay rows and source protocol context
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Pinned seven exact owner rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Bioactivity notes, outcome mapping and summary class generation
  ownership_note: The omission originates in the summary-only extraction and notes
    generation. Preserve the real positive and its database-assertion evidence while
    adding source-specific context through an effective source/extraction route.
actions:
- action_id: R020-CAPTURE-METHODS
  description: 'For naturalproductmech:mibig-41b176c91f / BGC0000922:2, add the demonstrated
    Knock-out studies, Heterologous expression and Enzymatic assays through the maintained
    method overlay. Pair the REPLACE row with a claim-reference decision pinned to
    raw row SHA256 b8c6cb52b474b3b4fb8b35af4103051a086ea612cf1773cd5becde2ec0fa0b21
    and retain DOI:10.1074/jbc.m804555200 for producer, locus and source reference.
    Explain native PAO1 versus recombinant host/His-tagged enzyme scope. Do not rely
    on expected_* columns alone: the current REPLACE loader does not enforce them.
    A tested loader extension is the alternative if a paired citation overlay is unsuitable.'
  finding_ids:
  - R020-MISSING-METHODS
  target_ids:
  - CHEBI:75926
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Compound-specific supported method correction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Full raw-row source guard and explicit primary citation
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Method override consumption and deterministic generation
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Exact raw-row digest enforcement
  generator: scripts/seed_from_sources.py guarded MIBiG overlays
  acceptance_checks:
  - Pin version 5, taxon NCBITaxon:208964, AE004091.2, bounds 1073960..1087095, the
    full target key and original empty method list through the enforced full-row digest;
    deliberate source-row drift must fail closed.
  - After reseeding only the exact compound gets CLUSTER_DEMONSTRATED and native PAO1
    BGC_CHARACTERIZED; preserve the correct original citation, chemistry, occurrences
    and neighboring compound grades.
  - Describe PqsA/PqsD product formation as observed and spontaneous cyclization as
    proposed; no historical construct sequence or human toxicity claim is inferred.
  - Run focused overlay tests, target strict validation, reproduction verification
    and required repository QC.
- action_id: R020-RESOLVE-NAMES
  description: Resolve the existing name-disagreement with curator-owned status, actual
    resolved_date, resolution_note and evidence. Explain the enol/keto fixed-H distinction
    and the repository Standard-InChIKey identity policy. Preserve both source labels,
    the generated prompt and chemical representations.
  finding_ids:
  - R020-NAMES
  target_ids:
  - CHEBI:75926
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/4-hydroxy-2-quinolone.yaml
    role: Curator-owned resolution of name-disagreement
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Preserves curator discussion answer fields
  generator: scripts/seed_from_sources.py preservation by discussion_id
  acceptance_checks:
  - The resolution cites the inspected default MOL, full Standard/fixed-H comparison
    and original primary drawing; no unsupported claim of identical fixed-H structures
    is introduced.
  - The answer survives the documented targeted curation/reseed workflow and required
    strict/reproduction checks; unrelated fields and source labels remain unchanged.
- action_id: BIO020-A1
  description: Preserve exact assay identity, source calls and values; enrich the
    positive GENE-TOX observation with Salmonella Ames and with-metabolic-activation
    scope, and disclose that the tester strain, quantitative dose and no-activation
    comparison are unspecified. Carry this through the effective PubChem inventory/extraction
    and generated notes, with manifest/source provenance as required. Optionally clarify
    that P63092 is assay-target metadata for an inconclusive mutant-oriented cellular
    cAMP screen, not a demonstrated direct compound target.
  finding_ids:
  - BIO020-F1
  target_ids:
  - CHEBI:75926
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/extract_pubchem_bioassay.py
    role: Effective extraction of exact assay rows and source protocol context
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/pubchem_bioassay.tsv
    role: Pinned seven exact owner rows
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Bioactivity notes, outcome mapping and summary class generation
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The GENE-TOX positive retains exact CID 54680871/SID 363895103/AID 1259408 and
    DATABASE_ASSERTION provenance.
  - Notes state Salmonella Ames with metabolic activation without inventing a specific
    strain, dose or requirement for activation.
  - The five NOT_DETERMINED and one INACTIVE qHTS calls and all six Potency values
    remain intact.
  - No direct GNAS agonism, wild-type activity, human toxicity or carcinogenicity
    is inferred.
  - Authorized regeneration, strict validation and reproducibility checks pass after
    implementing the source-context route.
limitations:
- The ChEBI aromatic SMILES export is malformed; its default MOL and full InChI were
  independently parsed and used for identity verification.
- The 2008 primary full HTML and original figures were available and inspected. Its
  official PMC XML endpoint supplied only an abstract and the publisher PDF was inaccessible;
  neither unavailable route is represented as a full-text review.
- The final spontaneous ring-closure step remains the original authors' proposal,
  with enzyme-assisted closure explicitly not ruled out. The review supports observed
  product formation without claiming the full mechanism.
- The optional expression-context evidence is reused with original access timestamps.
  The previously attempted precise411 runner searches failed typed-response parsing
  and are not interpreted as negative biological evidence.
- The plant 2000 original body remains inaccessible after bounded free primary-source
  searches. The review must retain this required occurrence-verification limitation
  even though fungal and bacterial occurrences are positively supported.
- The 2013 publisher body was HTTP 403, but an author-uploaded copy of the actual
  journal article was read through its public full-text transcription, with DOI and
  journal pages verified. Its official SI was independently retrieved; that SI covers
  different numbered compounds.
- The 2011 evidence was read as actual primary-paper text on a public mirror. It reports
  PA14-derived recombinant enzyme work and cites native-metabolite precedent; the
  original2008 PAO1 study was inspected separately.
- The source authority for the seven claims is the PubChem depositor record, as represented
  by DATABASE_ASSERTION. Original GENE-TOX 1977 experimental paper and 1986 panel
  review were not inspected; quantitative toxicity or human effects are not established.
- Four supplementary raw-row endpoints timed out once; successful current CID/SID
  summary and complete descriptions verify every stored outcome and value. No missing
  raw curve or titration result is invented.
- AID 624287 protocol does not specify the exact mutant construct or cell line. R201H/R201C
  occur in assay background and are not asserted to be the tested constructs.
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
- No scientific record, source inventory, maintained correction table, native curation
  status or history was edited. These are review observations and proposed curation
  actions.
- Shared deterministic baseline gates retain their actual command receipts from the
  identical tracked scientific base. Target strict validation ran afresh. Scientific
  failed or unavailable checks are distinct from bundle-schema validation.
- Before extending provenance for the actually inspected PubChem extractor, all original
  source hashes were asserted unchanged. The source attestation includes exact ChEBI
  and BioAssay owners.
- The sole positive assay is a qualitative bacterial mutagenicity database assertion.
  No clinical, human-toxicology, direct GNAS-binding or wild-type agonism claim is
  made.
tags:
- path-order-campaign
- batch-002
- dhq
- tautomerism
- native-knockout
- assay-scope
```
