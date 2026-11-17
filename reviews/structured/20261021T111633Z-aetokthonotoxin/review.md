# Aetokthonotoxin: validated pathway with citation and provenance wording repairs

- Review: 20261021T111633Z-aetokthonotoxin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T11:04:34.558033Z
- Finished UTC: 2026-10-21T11:16:33.832898Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact parent structure, five native protein cores, seven reactions and complete causal graph agree with primary experiments and current authorities. Two minor repairs concern locus citation placement and CyanoMetDB NMR wording. The source-specific CBT1886 stock designation remains unresolved because the required 2021 supplement was unavailable.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 45, batch 005, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 94 of 3116 current records had campaign coverage and 3022 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:167886 | data/natural_products/alkaloids/aetokthonotoxin.yaml | generated | aetokthonotoxin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | CHEBI:167886 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | CHEBI:167886 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | CHEBI:167886 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | CHEBI:167886 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:167886 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | CHEBI:167886 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Claim-by-claim primary reaction and graph audit | passed | True | CHEBI:167886 | All seven transformations, 13 nodes and 15 edges agree with the 2022 primary chemistry. The native protein-core correspondence independently passed; recombinant construct and accessory-reagent boundaries are retained. |
| Claim-local support for the exact locus enzymatic method | failed | True | CHEBI:167886 | The exact final-product enzymology is correctly cited elsewhere in the owner but not at the MIBiG locus claim, whose inherited 2021 citation establishes only the AetF precursor assay. This is a minor evidence-placement defect, not an unsupported pathway or method. |
| Primary verification of the CyanoMetDB CBT1886 designation | unavailable | True | CHEBI:167886 | The complete accessible 2021 main text supports the native 2011 cyanobacterium and species occurrence, but it does not resolve the literal CBT1886 designation. The required supplement remains inaccessible; no equivalence to Thurmond2011 or rejection of the database assertion is inferred. |
| Full native and published insert sequence identity | passed | True | CHEBI:167886 | All five current reviewed sequences exactly equal independently translated native CDSs and published coding cores; no partial native CDS or unresolved accession crosswalk remains. |
| Existing reaction and molecular grounding | passed | True | CHEBI:167886 | All seven Rhea equations and all existing molecular identifiers resolve consistently, with the neutral/zwitterion L-tryptophan distinction explicitly preserved. |
| Exact parent authority graph and source resolution | passed | True | CHEBI:167886 | Independent parent graphs and official identifiers agree; DOI/method claim placement is evaluated separately. |
| Applicable native expression dataset | not_applicable | False | CHEBI:167886 | No matching organism/strain dataset appears in the complete retained catalogue. |

## Scientific And Domain Assessments

### Exact natural product constitution

identity: supported. Targets: CHEBI:167886.

The original structure and X-ray illustration agree with the owner N1–C2′ linked pentabrominated biindole nitrile. The exact natural product was isolated from native culture and field material; no tetrahedral stereochemistry is missing from the depicted graph. Independent authority and normalized molecular equivalence are documented in the identifier packet.

### Definition, native origin and disease attribution

scope: supported. Targets: CHEBI:167886.

The definition correctly identifies the cyanobacterial toxin and disease association. Pure-compound causality was tested in chickens; the eagle attribution also relies on ecological and chemical evidence. Neither Hydrilla nor birds are treated as biosynthetic producers.

### Three provenance-specific species occurrences

evidence: supported. Targets: CHEBI:167886.

LOTUS and ChEBI species-level occurrences cite the same original study and are supported. The CyanoMetDB row also points to that study; its additional strain wording is separately unresolved. Repetition across retained source provenance is not three independent experiments or a demonstrated duplicate-data defect.

### CBT1886 versus Thurmond2011 source context

evidence: unknown. Targets: CHEBI:167886.

The native 2011 isolate is explicitly toxin-producing in the primary main text, but the relationship of the database label CBT1886 to that stock cannot be established from the inspected material. Keep the source attribution bounded; do not invent an alias, transfer a strain-specific experiment, or withdraw the occurrence on this access gap alone.

### Native producer and locus experimental scope

evidence: concern. Targets: CHEBI:167886.

The stored SOURCE_ASSERTION producer grade and CLUSTER_DEMONSTRATED enzymatic locus grade are consistent with their distinct scopes. The published cores map to MT225528.1 and the 2022 experiments establish exact AETX formation. The locus citation should route to that source while native origin retains the 2021 source; no native genetic or whole-cell heterologous grade upgrade follows.

### Steps 1–2 and graph edges 0–3: AetF

graph: supported. Targets: CHEBI:167886.

AetF sequentially brominates L-tryptophan at positions 5 then 7. The 2021 precursor experiment and 2022 full pathway agree with both substrate/product transitions. Activity is measured with recombinant protein and its cofactors, not inferred solely from annotation.

### Step 3 and graph edges 4–5: AetE

graph: supported. Targets: CHEBI:167886.

PLP-dependent AetE converts 5-bromo-L-tryptophan to 5-bromoindole, and the SI independently detects pyruvate. The chemical node and direction are correct; the Rhea note describes a balanced database reaction rather than claiming all coproducts were independently measured in this particular assay.

### Steps 4–5 and graph edges 6–9: AetA

graph: supported. Targets: CHEBI:167886.

AetA brominates 5-bromoindole at C3 and then C2 to give the exact 2,3,5-tribromoindole monomer. The assay uses SsuE/FAD/NADPH, and tested tryptophan substrates were not accepted. The historical SI accession maps to the current complete native core without substituting the truncated alternate genome annotation.

### Step 6 and graph edges 10–11: AetD

graph: supported. Targets: CHEBI:167886.

AetD converts 5,7-dibromo-L-tryptophan to the exact nitrile; Fe(II) stimulation and independence from AetC are directly shown. Later primary isotope and oxygen experiments support the separately attributed Rhea glycolate/O2 note. Detailed rearrangement intermediates remain proposed and are not asserted by this owner.

### Step 7 and graph edges 12–14: AetB

graph: supported. Targets: CHEBI:167886.

AetB accepts both explicitly named brominated monomers and yields AETX matching a synthetic standard, using ferredoxin, ferredoxin reductase and NADPH. The final N–C bond is clear from the structures. The paper itself calls the reaction biaryl coupling; that source-faithful term is not a confirmed chemical defect in this graph.

### Evidence snippets, accessory proteins and unassigned AetC

representation: supported. Targets: CHEBI:167886.

Both quoted experimental snippets occur in the 2022 original. Five enzyme nodes and eight chemical nodes support 15 edges and seven reactions. The graph omits an unproven AetC catalytic step and does not claim that spinach electron-transfer proteins or expression tags are native cyanobacterial pathway enzymes.

### NMR-used flag rendered as structural confirmation

representation: concern. Targets: CHEBI:167886.

The source nmr_used=yes flag is faithfully present but is rendered as structure confirmed by yes. The wording should state the source-reported NMR use, without claiming an independent confirmation method or reviewer certification.

### Natural-product, alkaloid and tryptophan-derived classifications

consistency: supported. Targets: CHEBI:167886.

Native isolation supports Natural_product. The tryptophan-derived indole structure and pathway are compatible with the source class and the computed Alkaloids classification. Empty NPClassifier class/superclass slots and absent optional activity/target content are not defects. Source version and model provenance remain distinguishable from experimentally established chemistry.

### Native status, curation history and optional expansion

provenance: supported. Targets: CHEBI:167886.

The owner records initial seeding and later pathway/graph curation without claiming that these review artifacts changed its native status. No new mechanism, bioactivity measurement or optional protein addition is required to repair the two narrow defects. The unresolved CBT1886 detail remains a review limitation, not a fabricated negative result.

### Complete native enzyme reference sequences

identity: supported. Targets: CHEBI:167886.

All five exact reviewed proteins are native Thurmond2011 references and equal complete CDS translations from MT225528.1. The historical AetA accession has a verified merge/redirect crosswalk; the alternative truncated genome annotation does not invalidate the stored full protein.

### Native protein identifiers versus recombinant assay preparations

scope: supported. Targets: CHEBI:167886.

Published codon-optimized inserts encode the same five core proteins, but the experiments use recombinant His-tagged preparations and MBP-AetB, with likely cleavage species in the latter sample. Existing enzyme identifiers appropriately identify the native cores; they do not encode exact whole assay constructs or native-culture purification.

### Reaction identifiers, direction and chemical participants

evidence: supported. Targets: CHEBI:167886.

All seven stored Rhea master reactions and their biochemical directions match current reviewed annotations. Cofactors/co-substrates in abbreviated notes are consistent with the full equations. Current reaction annotations do not independently prove which coproducts were measured in the original 2022 study.

### Intermediate stereochemistry, substitution and protonation

identity: supported. Targets: CHEBI:167886.

The intermediate MOLs match the named positional indole substitutions and L-amino-acid stereochemistry. Neutral CHEBI16828 and Rhea CHEBI57912 are related L-tryptophan microspecies, not identical fixed-H graphs; both use the same intended L-tryptophan substrate framework. Brominated tryptophan entries encode zwitterions explicitly. No opposite stereoisomer or wrong positional intermediate was found.

### Current annotation versus historical assay evidence

scope: supported. Targets: CHEBI:167886.

Reviewed status, full sequences and native accession bridges are verified. Later AetD coproduct/mechanism studies and AetF engineered-variant or structural studies remain separate citations and construct contexts; no expanded substrate scope, kinetic result or variant is silently transferred into the existing graph.

### Exact chemical authority and source-concept resolution

identity: supported. Targets: CHEBI:167886.

The official parent graph, MIBiG, owner and Wikidata agree in standardized and fixed-H form. Three-star ChEBI167886 supports exact grounding; source-specific interpretation remains tied to primary evidence.

### Named native strain and species-level occurrences

scope: supported. Targets: CHEBI:167886.

Thurmond2011 is a strain node under the occurrence species. Wikidata maps that species correctly. The unresolved CBT1886 stock bridge is not supplied by these identifiers.

### Curated claims and unchanged native history

provenance: supported. Targets: CHEBI:167886.

Both seed events and both2026-09-28 curation events remain intact, including the later two-substrate correction. Every existing pathway/graph claim is audited in the scientific/protein sections; current SEEDED status is not silently changed.

### Computational classification attribution

provenance: supported. Targets: CHEBI:167886.

Classification is retained as a versioned computational output, not a newly demonstrated biosynthetic reaction.

## Findings

### S045-F-CITATION: Route the exact locus enzymatic claim to the 2022 study

minor / open / confirmed; issue key: mibig-bgc0002643-compound1-claim-reference-routing.

The locus Enzymatic assays claim inherits the 2021 isolation/AetF citation. Exact final-product enzymology was established in 2022 and is already correctly cited by the same owner pathway and graph. The defect is claim-local citation routing, not lack of support for the method, pathway or native species occurrence.

### S045-F-NMR-WORDING: Render the CyanoMetDB flag as reported NMR use

minor / open / confirmed; issue key: cyanometdb-nmr-used-rendered-as-structure-confirmed.

The generated note structure confirmed by yes incorrectly casts a yes/no NMR-use flag as a confirmation method. The current primary paper does use NMR, but that does not make the emitter wording precise or convert the source flag into an independent verification. This is the same shared cause already identified in earlier campaign records.

## Recommended Actions And Acceptance Checks

### S045-A-ROUTE-CITATION

Add a consumed curation/mibig_claim_references.tsv decision for source_id BGC0002643:1 with expected_source_row_sha256 6b6ed3bd66bf39cc49b5da5c9d758c30af79161d20b0f9cb2987a3b6e50af46f, producer_reference PMID:33766860, locus_reference PMID:35142504 and source_reference PMID:35142504, with curator/date/rationale. Preserve the original imported citation in raw provenance. No method REPLACE or grade change is required. The current loader can apply this citation-only correction without a structural overlay.

- The complete source row matches the pinned SHA and a changed chemistry, strain, interval, source method or citation fails closed.
- Producer evidence retains the 2021 native-isolation reference; the locus enzymatic claim cites the 2022 exact pathway study, with explicit curator-routing provenance.
- Enzymatic assays, SOURCE_ASSERTION and CLUSTER_DEMONSTRATED remain unchanged; no native knockout, whole-cell heterologous production, axenic-culture claim or CBT1886 alias is introduced.
- The seven pathway steps, all 13 nodes and 15 edges, molecular structure, source identifiers and raw inventory remain unchanged.
- After implementation, deterministic regeneration, strict target validation and required repository gates pass.

### S045-A-NMR-WORDING

Correct the shared CyanoMetDB emitter to report the literal source fact, for example NMR used according to CyanoMetDB: yes, and retain DATABASE_ASSERTION attribution. Preserve the imported nmr_used flag, DOI, CBT1886 context and taxon; do not use this wording repair to decide the unresolved strain relationship.

- The yes, no and blank source cases retain their respective meanings; no output says structure confirmed by yes or structure confirmed by no.
- This target retains the same exact chemical key, occurrence reference, strain context, taxon and source attribution.
- A focused generation check covers all three flag states and confirms that the shared fix does not duplicate or overwrite unrelated occurrence evidence.
- Deterministic regeneration, strict validation and required repository gates pass after implementation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S045-OWNER | data/natural_products/alkaloids/aetokthonotoxin.yaml; Complete 622-line owner and resolved content; all three occurrences, producer/locus, seven steps, 13 nodes, 15 edges, classifications and history | supports | The exact neutral pentabrominated biindole has key JXJDQKCOJBAPQM-UHFFFAOYSA-N. The owner contains three source-specific A. hydrillicola occurrences, native Thurmond2011 producer, source method Enzymatic assays, SOURCE_ASSERTION/CLUSTER_DEMONSTRATED grades, and seven explicitly cited recombinant enzyme reactions. No quantitative bioactivity or molecular target is asserted. |
| S045-RAW | data/raw/mibig_compounds.tsv; Complete BGC0002643:1 version 2 row; canonical complete-row SHA256 6b6ed3bd66bf39cc49b5da5c9d758c30af79161d20b0f9cb2987a3b6e50af46f | supports | The imported row exactly reproduces the owner chemistry, Thurmond2011 taxon, MT225528.1:1..9229 interval, Enzymatic assays method and grades. Both emitted claims inherit PMID:33766860 through COMPOUND_EVIDENCE. Entry quality questionable and completeness unknown are source metadata, not independent experimental conclusions. |
| S045-OCCURRENCE-ROWS | /private/tmp/npm-review-work/045/local-sources.json; All exact-key LOTUS, CyanoMetDB, ChEBI-origin and NPClassifier rows | supports | LOTUS and ChEBI report species-level A. hydrillicola occurrence from the 2021 Science study. CyanoMetDB additionally reports strain CBT1886 and nmr_used=yes. These distinct source assertions are preserved; their shared paper is not three independent isolation experiments. NPClassifier returns Alkaloids and is_glycoside=false, with empty superclass/class results. |
| S045-2021-MAIN | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=8318203&amp;retmode=xml; DOI:10.1126/science.aax9050; PMID:33766860; complete main body and methods summary, especially paragraphs 8, 10, 14, 15, 17 and 19 in retained body extraction | supports | The authors isolated AETX from bromide-supplemented A. hydrillicola cultures and field assemblages, and explicitly confirmed production by the cyanobacterium isolated in 2011 from J. Strom Thurmond Reservoir. The 2011 and 2014 genomes contain the same six-gene locus. Recombinant AetF establishes precursor bromination only in this paper. Pure AETX caused vacuolar lesions in experimentally exposed chickens; bald-eagle causation combines this result with the ecological and chemical evidence. |
| S045-2021-FIGURES | https://pure.mpg.de/rest/items/item_3352301/component/file_3352376/content; Original physical PDF pages 4 and 5, printed pages 3 and 4 of 7; Figures 2, 3 and 4 pixels | supports | Figure 3 shows N1–C2′ linked indoles, bromines at 2,3,5 and 5′,7′, and a 3′ nitrile, agreeing with the owner constitution and C17H6Br5N3 formula. No tetrahedral stereocentres are depicted. Figure 2 localizes toxin to cyanobacterial colonies; Figure 4 shows the cluster and AetF precursor assay. The visual structural comparison is not a new crystallographic refinement or complete spectral reinterpretation. |
| S045-2022-MAIN | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=9004672&amp;retmode=xml; DOI:10.1021/jacs.1c12778; PMID:35142504; full main scientific body paragraphs 1–9 and all main figure captions | supports | The study reconstitutes the exact pathway reactions using purified recombinant proteins: AetF performs two tryptophan brominations; AetE releases 5-bromoindole; AetA forms 3,5-dibromoindole then 2,3,5-tribromoindole; AetD produces the dibromoindole nitrile; AetB couples the exact two monomers to AETX. The final product matches a synthetic standard by chromatography and mass. AetC was not required for the measured reactions. No native knockout, whole-cell heterologous AETX production or single one-pot five-enzyme synthesis is claimed by this audit. |
| S045-2022-SI | https://api.figshare.com/v2/file/download/34030520; Official ja1c12778_si_001.pdf; methods/coding sequences pages 1–13, relevant Table S3 entries page 15, page 16 caption, assay pages 17–20, synthesis pages 21–25; original pixels pages 12, 17–20 and 24 | supports | Codon-optimized inserts were expressed in E. coli BL21(DE3); AetB used a His-MBP fusion and AetE used GroEL/ES. AetB assays used the two exact monomers plus spinach ferredoxin, ferredoxin reductase and NADPH. AetE pyruvate was detected after derivatization. AetD assays distinguish enzyme, AetC and metal conditions and follow amino nitrogen into nitrile. The separately synthesized AETX standard has reported NMR agreement with prior literature. Table S3 uses historical AetA A0A861B8S3. Later spectral pages and every sequence-network row were not exhaustively inspected. |
| S045-2023-AETD | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10654658/fullTextXML; DOI:10.1038/s41467-023-43285-0; PMID:37973794; complete scientific body, methods and figure captions | supports | The structural and biochemical study supports diiron AetD and distinguishes recombinant wild type from site-directed variants. It is not a native organism knockout study. Its proposed mechanistic route does not itself establish the glycolate coproduct; the later 2024 source provides that direct chemical evidence. |
| S045-2024-AETD | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=11611611&amp;retmode=xml; DOI:10.1038/s41557-024-01603-z; PMID:39285206; full main scientific body and Methods, especially Results paragraphs 17–28 and Figures 4–6 captions | supports | Isotope tracing and NMR identify glycolic acid as the two-carbon coproduct of the AetD nitrile-forming reaction; stopped-flow experiments directly probe oxygen-dependent iron chemistry. These results support the later Rhea oxygen/glycolate annotation. The detailed aziridine/nitrone route remains a proposal. Experiments use recombinant AetD, not a new cyanobacterial knockout or transport assay. Supplementary files and original 2024 figure pixels were not independently inspected. |
| S045-SI-CORES | /private/tmp/npm-review-work/045/si2022-coding-cores.json; Independent translation of all six printed codon-optimized coding inserts on SI pages 3–5; terminal stops removed explicitly | supports | The published cores are AetA 596, AetB 485, AetC 174, AetD 239, AetE 468 and AetF 668 residues, with no internal stops. A first parsing attempt spanning a form-feed boundary was corrected before these complete outputs were accepted. The file retains the DNA and amino-acid strings; these cores exclude vector tags and the AetB MBP fusion. |
| S045-CORE-BRIDGE | /private/tmp/npm-review-work/045/protein-reaction/protein-equivalence.json; Independent collaborator comparison, read in full; six native MT225528.1 translations and five complete owner UniProt sequences | supports | All six native deposited translations equal the published SI amino-acid cores. All five owner UniProt proteins match their complete native sequences. Historical AetA A0A861B8S3 is a secondary accession of A0AAP5I1G4. This supports applying the measured core-enzyme chemistry to the stored locus while preserving codon optimization, recombinant tags and assay conditions. It does not establish native knockout or whole-cell expression evidence. |
| S045-2021-SI-ACCESS | /private/tmp/npm-review-work/shared-next-batch005/aetokthonotoxin/2021-si-recovery-notes.json; Preserved exact NCBI instance-path media attempt and official institutional metadata; separate Europe PMC supplementaryFiles response inspected in full | context_only | The linked 2021 supplement was not recovered: the exact NCBI media URL returned HTML with a JavaScript download challenge, and Europe PMC returned a not-open-access XML error rather than an archive. The institutional item lists only the main article. These are access limitations, not evidence that the supplement or strain documentation does not exist. |
| S045-REFERENCE-LOADER | src/naturalproductmech/curate/claim_references.py; Entire load_claim_references and correct_claim_reference implementations; exact required fields and complete-row guard | context_only | The consumed claim-reference table can independently route producer and locus citations using a complete raw-row SHA. It retains raw citation provenance and does not change chemistry, taxa, methods or grades. It rejects structure-corrected rows; no structure correction is proposed here. A method REPLACE overlay is unnecessary for this citation-only repair. |
| S045-CYANO-EMITTER | scripts/seed_from_sources.py; CyanoMetDB occurrence generation, especially lines 1221–1234 and the exact nmr_used=yes source row | context_only | The emitter interpolates the NMR-used flag into structure confirmed by yes. The flag records whether NMR was used, not a confirmation method named yes or an independent reviewer certification. This is the same shared emitter issue already recorded under cyanometdb-nmr-used-rendered-as-structure-confirmed. |
| S045-MAINTAINED-SEARCH | /private/tmp/npm-review-work/045/science-maintained-search.json; Ignored-inclusive maintained correction search | context_only | No existing target-specific correction was found in the searched curation, configuration and curation-consumer paths. This bounded result supports proposing a new exact-source citation row; it does not establish that no external literature exists. |
| P045-OWNER | data/natural_products/alkaloids/aetokthonotoxin.yaml; Full owner: seven pathway steps, thirteen graph nodes and fifteen graph edges | supports | All five existing enzyme identifiers, seven Rhea reaction identifiers and eight pathway chemical identifiers were inventoried before comparison. The graph is explicitly scoped to in vitro branch construction and coupling. It does not assert an AetC reaction or that purified proteins came directly from native cyanobacterial culture. |
| P045-GENBANK | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=MT225528.1&amp;rettype=gb&amp;retmode=text; Header, source, all six complete CDS locations/qualifiers and entire ORIGIN sequence; independently translated | supports | MT225528.1 contains 9,229 bp from A. hydrillicola Thurmond2011, taxon2712845, and six complete plus-strand CDSs. AetA/QNL15171.1 is1..1791; AetB/QNL15172.1 2143..3600; AetD/QNL15174.1 4241..4960; AetE/QNL15175.1 5479..6885; AetF/QNL15176.1 7223..9229. All have codon_start1 and translation table11, without partial markers. The original AetD putative-methyltransferase note is historical annotation, not the current primary biochemical assignment. |
| P045-UNIPROT-AETA | https://rest.uniprot.org/uniprotkb/A0AAP5I1G4.json; Entry type/audit, gene/organism, complete sequence, EMBL cross-references, all comments and references including evidence attribution | supports | A0AAP5I1G4 is reviewed Swiss-Prot aetA from taxon2712845, 596 aa, entry version8, sequence version2. Its MT225528 genomic cross-reference gives QNL15171.1; the full current sequence equals the independently translated native CDS and the published 2022 coding-insert core. AetA lists historical A0A861B8S3 as secondary; its erroneous-initiation caution refers specifically to alternate-genome MDR9893084.1, not complete QNL15171.1. |
| P045-UNIPROT-AETB | https://rest.uniprot.org/uniprotkb/A0A861B5L6.json; Entry type/audit, gene/organism, complete sequence, EMBL cross-references, all comments and references including evidence attribution | supports | A0A861B5L6 is reviewed Swiss-Prot aetB from taxon2712845, 485 aa, entry version20, sequence version1. Its MT225528 genomic cross-reference gives QNL15172.1; the full current sequence equals the independently translated native CDS and the published 2022 coding-insert core. |
| P045-UNIPROT-AETD | https://rest.uniprot.org/uniprotkb/A0A861B387.json; Entry type/audit, gene/organism, complete sequence, EMBL cross-references, all comments and references including evidence attribution | supports | A0A861B387 is reviewed Swiss-Prot aetD from taxon2712845, 239 aa, entry version17, sequence version1. Its MT225528 genomic cross-reference gives QNL15174.1; the full current sequence equals the independently translated native CDS and the published 2022 coding-insert core. Its current functional annotation combines the 2022 nitrile study with later 2023/2024 structural, coproduct and mechanism studies; these are not backdated into the 2022 assay. |
| P045-UNIPROT-AETE | https://rest.uniprot.org/uniprotkb/A0A861BA10.json; Entry type/audit, gene/organism, complete sequence, EMBL cross-references, all comments and references including evidence attribution | supports | A0A861BA10 is reviewed Swiss-Prot aetE from taxon2712845, 468 aa, entry version18, sequence version1. Its MT225528 genomic cross-reference gives QNL15175.1; the full current sequence equals the independently translated native CDS and the published 2022 coding-insert core. |
| P045-UNIPROT-AETF | https://rest.uniprot.org/uniprotkb/A0A861B9Z9.json; Entry type/audit, gene/organism, complete sequence, EMBL cross-references, all comments and references including evidence attribution | supports | A0A861B9Z9 is reviewed Swiss-Prot aetF from taxon2712845, 668 aa, entry version16, sequence version1. Its MT225528 genomic cross-reference gives QNL15176.1; the full current sequence equals the independently translated native CDS and the published 2022 coding-insert core. Later substrate-scope, structural and engineered-variant annotations, including a 1–655 crystallographic construct and 2025 variants, do not redefine the 668-aa native sequence or the 2022 assay construct. |
| P045-AETA-LEGACY | https://rest.uniprot.org/uniprotkb/A0A861B8S3.json; Actual HTTP redirect final URL and complete returned primary/secondary accession fields | supports | The exact historical accession request A0A861B8S3 redirects to A0AAP5I1G4 and returns byte-identical current JSON. Together with the explicit secondary-accession field, this verifies continuity with SI Table S3; it is not an inferred crosswalk from a similar protein name. |
| P045-PROTEIN-COMPARE | /private/tmp/npm-review-work/045/protein-reaction/protein-equivalence.json; All native CDS translations, submitted translations, five current UniProt sequences and six published coding cores | supports | All five owner protein sequences match exactly across the native genomic translation, GenBank qualifier, current UniProt and the full published coding core: AetA596, AetB485, AetD239, AetE468 and AetF668 aa. Context-only AetC174 aa also matches the native/SI comparison. Native and codon-optimized DNA differ as expected; no fusion/tag sequence equivalence is claimed. |
| P045-SI-CONSTRUCTS | https://api.figshare.com/v2/file/download/34030520; DOI10.1021/jacs.1c12778 official SI pp3–5 coding inserts, pp7–10 expression/construct protocols, original p15 Table S3 pixels | supports | The SI supplies E. coli codon-optimized aetA–F inserts in pET28a, His-tagged AetA/C/F/D/E and an MBP-AetB construct expressed in BL21(DE3); its S3 caption describes His-MBP-AetB plus likely cleavage products. The original Table S3 lists AetA A0A861B8S3 and AetF A0A861B9Z9. Coding cores support the native reference bridge while tags, junctions and fusion state remain assay-specific. No complete fusion sequence or cleavage fraction was independently reconstructed. |
| P045-RHEA-82463 | https://www.rhea-db.org/rhea?query=rhea%3A82463&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step1 and corresponding existing graph edges | supports | bromide + L-tryptophan + NADPH + O2 + 2 H(+) = 5-bromo-L-tryptophan + NADP(+) + 2 H2O. The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. This master equation uses CHEBI57912 zwitterion, while the owner precursor is neutral CHEBI16828; their chemically related state distinction is explicitly assessed below. |
| P045-RHEA-82467 | https://www.rhea-db.org/rhea?query=rhea%3A82467&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step2 and corresponding existing graph edges | supports | 5-bromo-L-tryptophan + bromide + NADPH + O2 + 2 H(+) = 5,7-dibromo-L-tryptophan + NADP(+) + 2 H2O. The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. |
| P045-RHEA-82523 | https://www.rhea-db.org/rhea?query=rhea%3A82523&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step3 and corresponding existing graph edges | supports | 5-bromo-L-tryptophan + H2O = 5-bromoindole + pyruvate + NH4(+). The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. |
| P045-RHEA-82527 | https://www.rhea-db.org/rhea?query=rhea%3A82527&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step4 and corresponding existing graph edges | supports | 5-bromoindole + bromide + FADH2 + O2 = 3,5-dibromoindole + FAD + 2 H2O. The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. |
| P045-RHEA-82531 | https://www.rhea-db.org/rhea?query=rhea%3A82531&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step5 and corresponding existing graph edges | supports | 3,5-dibromoindole + bromide + FADH2 + O2 = 2,3,5-tribromoindole + FAD + 2 H2O. The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. |
| P045-RHEA-81787 | https://www.rhea-db.org/rhea?query=rhea%3A81787&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step6 and corresponding existing graph edges | supports | 5,7-dibromo-L-tryptophan + O2 = 5,7-dibromo-indole-3-carbonitrile + glycolate + H2O + H(+). The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. Glycolate belongs to this current database equation; experimental support and publication timing are separately assessed in the primary-source packet. |
| P045-RHEA-82519 | https://www.rhea-db.org/rhea?query=rhea%3A82519&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; Complete one-row TSV; pathway step7 and corresponding existing graph edges | supports | 5,7-dibromo-indole-3-carbonitrile + 2,3,5-tribromoindole + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = aetokthonotoxin + 2 oxidized [2Fe-2S]-[ferredoxin] + 2 H2O. The complete equation exactly matches the current reviewed protein catalytic annotation, which separately provides a left-to-right physiological Rhea variant. The owner stores the valid master reaction ID and abbreviates rather than fully balances its prose. |
| P045-MOL-16828 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/16828/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI16828 MOL resolves L-tryptophan, C11H12N2O2, full key QIVBCDIJIAJPQS-VIFPVBQESA-N. Its official graph has no charged atoms. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-57912 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/57912/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI57912 MOL resolves L-tryptophan zwitterion, C11H12N2O2, full key QIVBCDIJIAJPQS-VIFPVBQESA-N. It is a zwitterion with one positive and one negative atom despite zero net charge. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-232362 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232362/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI232362 MOL resolves 5-bromo-L-tryptophan zwitterion, C11H11BrN2O2, full key KZDNJQUJBMDHJW-VIFPVBQESA-N. It is a zwitterion with one positive and one negative atom despite zero net charge. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-231978 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/231978/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI231978 MOL resolves 5,7-dibromo-L-tryptophan zwitterion, C11H10Br2N2O2, full key UURVQGNSCUCIQS-VIFPVBQESA-N. It is a zwitterion with one positive and one negative atom despite zero net charge. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-231979 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/231979/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI231979 MOL resolves 5,7-dibromo-indole-3-carbonitrile, C9H4Br2N2, full key IVEGXYGMXKFJDG-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-232363 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232363/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI232363 MOL resolves 2,3,5-tribromoindole, C8H4Br3N, full key KUPJVNCDFREPQN-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-232364 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232364/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI232364 MOL resolves 5-bromoindole, C8H6BrN, full key VXWVFZFZYXOBTA-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-232365 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232365/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI232365 MOL resolves 3,5-dibromoindole, C8H5Br2N, full key NGTBILHUFBABDS-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-MOL-167886 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/167886/; Complete official MOL graph; direct chemical comparison including position, charge and stereochemistry | supports | Official CHEBI167886 MOL resolves aetokthonotoxin, C17H6Br5N3, full key JXJDQKCOJBAPQM-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL reconstruction agrees with the separately encoded named positional substitution pattern, full Standard identity and fixed-H form. This verifies a chemical identifier, not an experiment. |
| P045-CHEBI-TRP | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16828/; Exact compound name, formula, charge, default InChI/key and CHEBI57912 relation | supports | CHEBI16828 denotes neutral L-tryptophan, three-star, with a specified S centre. The authority explicitly links its zwitterion CHEBI57912 as a tautomer. The pathway uses this neutral compound identifier without asserting that neutral species predominates in buffered enzyme assays. |
| P045-CHEBI-ZWITTERION | https://www.ebi.ac.uk/chebi/backend/api/public/compound/57912/; Complete compound response, exact molecular form and explicit tautomer relation | supports | CHEBI57912 denotes L-tryptophan zwitterion, three-star, with the same S centre and molecular formula; the authority describes it as the major species at pH7.3 and links CHEBI16828. Rhea82463 uses this species. Equal Standard InChI does not make their fixed-H representations identical. |
| P045-CHEBI-231978 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/231978/; Complete exact intermediate response; name, formula, charge, full InChI/key and ontology form | supports | The exact entry is the named pathway intermediate and has the same formula/full Standard key as its separately inspected official MOL. Current rating is two-star; that does not invalidate its use as a resolvable pathway identifier. The full MOL, rather than the API display SMILES, supplies protonation and indole hydrogen details. |
| P045-CHEBI-231979 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/231979/; Complete exact intermediate response; name, formula, charge, full InChI/key and ontology form | supports | The exact entry is the named pathway intermediate and has the same formula/full Standard key as its separately inspected official MOL. Current rating is two-star; that does not invalidate its use as a resolvable pathway identifier. The full MOL, rather than the API display SMILES, supplies protonation and indole hydrogen details. |
| P045-CHEBI-232362 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/232362/; Complete exact intermediate response; name, formula, charge, full InChI/key and ontology form | supports | The exact entry is the named pathway intermediate and has the same formula/full Standard key as its separately inspected official MOL. Current rating is two-star; that does not invalidate its use as a resolvable pathway identifier. The full MOL, rather than the API display SMILES, supplies protonation and indole hydrogen details. |
| P045-CHEBI-232363 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/232363/; Complete exact intermediate response; name, formula, charge, full InChI/key and ontology form | supports | The exact entry is the named pathway intermediate and has the same formula/full Standard key as its separately inspected official MOL. Current rating is two-star; that does not invalidate its use as a resolvable pathway identifier. The full MOL, rather than the API display SMILES, supplies protonation and indole hydrogen details. |
| P045-CHEBI-232364 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/232364/; Complete exact intermediate response; name, formula, charge, full InChI/key and ontology form | supports | The exact entry is the named pathway intermediate and has the same formula/full Standard key as its separately inspected official MOL. Current rating is two-star; that does not invalidate its use as a resolvable pathway identifier. The full MOL, rather than the API display SMILES, supplies protonation and indole hydrogen details. |
| P045-CHEBI-232365 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/232365/; Complete exact intermediate response; name, formula, charge, full InChI/key and ontology form | supports | The exact entry is the named pathway intermediate and has the same formula/full Standard key as its separately inspected official MOL. Current rating is two-star; that does not invalidate its use as a resolvable pathway identifier. The full MOL, rather than the API display SMILES, supplies protonation and indole hydrogen details. |
| P045-REACTION-COMPARE | /private/tmp/npm-review-work/045/protein-reaction/reaction-chemical-comparison.json; All nine molecular forms and seven existing step/reaction/protein combinations; full graph identifier inventory | supports | Every existing chemical and protein node resolves, and all seven Rhea equations match current UniProt catalytic entries and participant identities. Step1 alone requires the explicit neutral/zwitterion bridge: same Standard InChI and S centre, different fixed-H InChI and internal charge placement. Owner AETX, current MIBiG AETX and official CHEBI167886 MOL agree in full Standard and fixed-H form. No new pathway edge or unasserted side reaction is inferred. |
| R045-OWNER | data/natural_products/alkaloids/aetokthonotoxin.yaml; Entire 622-line owner, all seven steps, 13 nodes, 15 edges and four native history events | supports | The neutral exact parent CHEBI167886 has one MIBiG producer/locus, three source-specific occurrences and a curated biosynthetic pathway/graph. Its curation status remains SEEDED despite later recorded curation events. The review checks those assertions without promoting status or treating history as independent validation. |
| R045-CHEM | /private/tmp/npm-review-work/045/protein-reaction/reaction-chemical-comparison.json; Parent owner/current-MIBiG/official-ChEBI-MOL comparison | supports | All three directly parsed parent graphs agree on full key JXJDQKCOJBAPQM-UHFFFAOYSA-N, fixed-H InChI, neutral C17H6Br5N3 and no tetrahedral stereocentre. The official MOL retains the indole N-H; the API display SMILES is not silently repaired and substituted. |
| R045-WIKI-COMPARE | /private/tmp/npm-review-work/045/identity/wikidata-parent-comparison.json; Independent Wikidata P233 graph comparison | supports | The full Wikidata P233 graph also matches the owner standard and fixed-H identities. Its P234/P235 fields match the stored identity. |
| R045-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/167886/; Retained complete response; stated relevant authority fields | supports | Released CHEBI167886 is three-star, with exact formula/full key, a source-attributed definition and A. hydrillicola taxon1550245/PMID33766860 origin. The definition and origin are audited against primary literature separately; current authority status supports EXACT grounding. |
| R045-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0002643.2/annotations.json; Retained complete response; stated relevant authority fields | supports | Active BGC0002643 version2 retains exact aetokthonotoxin, CyanoMetDB_2448, Thurmond2011 taxon2712845, MT225528.1:1..9229 and Enzymatic assays. Its biosynthesis path explicitly cites DOI10.1021/jacs.1c12778, whereas selected compound evidence includes PMID33766860. Quality questionable/completeness unknown are source flags. Entry-level activity fields are not additional owner activity claims. |
| R045-TAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1550245,2712845&amp;retmode=xml; Both top-level Taxon names, ranks, parent links, aliases and lineage | supports | NCBI1550245 is species Aetokthonos hydrillicola; NCBI2712845 is strain Thurmond2011 directly beneath that species. Cyanobacterial grouping is consistent. Neither taxonomy entry establishes CBT1886 as the same stock; that source-specific occurrence qualifier remains a separate primary-provenance question. |
| R045-WIKI | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q106365096%7CQ67339642&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Both returned entities; labels and P685/P225/P233/P234/P235 identity claims | supports | Organism Q67339642 maps explicitly to NCBI1550245. Chemical Q106365096 carries the exact parent graph, Standard InChI and full key. These links resolve the LOTUS concepts without independently proving culture provenance. |
| R045-RAW | data/raw/chebi_structures.tsv; Complete exact-key source projection and eligible three-star entry | supports | The pinned eligible CHEBI167886 entry and origin resolve the exact owner. The committed CyanoMetDB row is an exact-key Aetokthonotoxin/CBT1886/nmr_used=yes assertion citing the same2021 paper; the xref suffix2448 is inherited from MIBiG, not a second independent experiment. Three occurrence sources converge on one publication rather than three independent biological isolations. |
| R045-CLASS | data/raw/npclassifier.tsv; Complete exact-key classifier row | supports | The owner reproduces the explicitly versioned NPClassifier2026-09-07 pathway/superclass/class assignments. This computational attribution is distinct from source biosynthetic class and experimentally verified mechanism. |
| R045-IMODULON | https://imodulondb.org/; Previously retained complete28-dataset catalogue | context_only | No matching native organism/strain dataset occurs in the complete retained catalogue. No regulatory module is added from a different organism or from unasserted optional expression context. |

## Limits And Additional Notes

- The 2021 main body and original Figures 2–4 were inspected, but its supplementary methods were not recovered. The literal CBT1886 designation, its relationship to Thurmond2011 and detailed culture-purity documentation remain unverified; no strain alias or axenic status is inferred. This required gap makes the scientific review partial.
- The 2022 complete main scientific text and captions were read. SI reading covered coding and assay methods, selected network-table identifiers and synthesis pages 21–25; original assay/synthesis pixels on pages 12, 17–20 and 24 were inspected. Later NMR pages and every sequence-network entry were not exhaustively reanalysed.
- Published codon-optimized coding inserts and complete native amino-acid cores agree, but vector tags, the AetB MBP fusion, host chaperones and accessory reductants remain experimental context. No complete recombinant plasmid or mutant allele reconstruction was performed.
- The 2023 and 2024 AetD main texts were read, including main methods and captions. Their supplementary files and original figure pixels were not independently inspected. Later mechanistic proposals are not upgraded to demonstrated elementary steps, and in-pathway chemistry does not mean an experiment in the native organism.
- Current chemical/taxonomic identifiers, molecular normalization, Rhea equations and full UniProt/native sequence receipts are supplied by the separate authority packet; this packet independently addresses primary scientific applicability. No repository files, saved bundles, campaign state, native status or history were edited.
- This packet verifies existing protein and reaction groundings. It does not independently reproduce enzyme assays or establish unasserted pathway steps, side products or native genetic necessity.
- Published coding cores and native proteins agree exactly; complete His-tag, linker, MBP and cleavage-product sequences were not reconstructed. An AetB fusion preparation with probable cleavage bands is not represented as a homogeneous untagged native protein.
- Current ChEBI API display SMILES omit indole [nH] details in these entries. Exact chemistry was verified from official MOLs and full InChI fields without silently editing the returned strings. Neutral and zwitterionic tryptophan share Standard identity but differ in fixed-H form.
- Current UniProt functional summaries integrate several publication years. Their later mechanistic, kinetic and engineered-variant claims are not experimental evidence for the 2022 citation alone.
- Database graph and taxon resolution do not substitute for the original experiments or establish uninspected historical stock identity.
- The neutral parent graph is the stored representation, not a measurement of solution protonation or tautomer populations.
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
review_id: 20261021T111633Z-aetokthonotoxin
title: 'Aetokthonotoxin: validated pathway with citation and provenance wording repairs'
started_at: '2026-10-21T11:04:34.558033Z'
finished_at: '2026-10-21T11:16:33.832898Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact parent structure, five native protein cores, seven reactions and
  complete causal graph agree with primary experiments and current authorities. Two
  minor repairs concern locus citation placement and CyanoMetDB NMR wording. The source-specific
  CBT1886 stock designation remains unresolved because the required 2021 supplement
  was unavailable.
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
  - path: data/natural_products/alkaloids/aetokthonotoxin.yaml
    sha256: 07ff54c044737bda66d471d372c8f958ff994585d06b7876aed5ea45da160f76
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
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 45, batch 005, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 94 of 3116 current records had campaign coverage and 3022 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:167886
targets:
- target_id: CHEBI:167886
  path: data/natural_products/alkaloids/aetokthonotoxin.yaml
  label: aetokthonotoxin
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
    path: data/natural_products/alkaloids/aetokthonotoxin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - CHEBI:167886
  command: just validate-strict data/natural_products/alkaloids/aetokthonotoxin.yaml
    --out /private/tmp/npm-review-work/045/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T11:04:38.373701Z
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
  scope_note: 'Original read-only batch004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055340+00:00;
    finished 2026-10-21T09:55:22.727768+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-corpus.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-corpus.log. Reused
    for batch005 only after fresh fetch/base/tree equality and all 9,182 tracked file
    bytes and modes were verified against the original batch004 baseline (208,070,649
    bytes). This gate was not rerun for batch005; original times, scope, warnings,
    exceptions and skips are preserved.'
  target_ids:
  - CHEBI:167886
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
  scope_note: 'Original read-only batch004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.055361+00:00;
    finished 2026-10-21T09:56:44.050706+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/verify-reproduction.json;
    transcript: /private/tmp/npm-native-checks/batch-004/verify-reproduction.log.
    Reused for batch005 only after fresh fetch/base/tree equality and all 9,182 tracked
    file bytes and modes were verified against the original batch004 baseline (208,070,649
    bytes). This gate was not rerun for batch005; original times, scope, warnings,
    exceptions and skips are preserved.'
  target_ids:
  - CHEBI:167886
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
  scope_note: 'Original read-only batch004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.057401+00:00;
    finished 2026-10-21T09:54:38.468783+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/review-queue.json;
    transcript: /private/tmp/npm-native-checks/batch-004/review-queue.log. Reused
    for batch005 only after fresh fetch/base/tree equality and all 9,182 tracked file
    bytes and modes were verified against the original batch004 baseline (208,070,649
    bytes). This gate was not rerun for batch005; original times, scope, warnings,
    exceptions and skips are preserved.'
  target_ids:
  - CHEBI:167886
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
  scope_note: 'Original read-only batch004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:20.061733+00:00;
    finished 2026-10-21T09:56:36.296159+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/validate-products.json;
    transcript: /private/tmp/npm-native-checks/batch-004/validate-products.log. Reused
    for batch005 only after fresh fetch/base/tree equality and all 9,182 tracked file
    bytes and modes were verified against the original batch004 baseline (208,070,649
    bytes). This gate was not rerun for batch005; original times, scope, warnings,
    exceptions and skips are preserved.'
  target_ids:
  - CHEBI:167886
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
  scope_note: 'Original read-only batch004 execution on 1c2402097718c138b081e00943de8f04de0541cd
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T09:54:30.560925+00:00;
    finished 2026-10-21T10:04:44.806799+00:00. Exact original receipt: /private/tmp/npm-native-checks/batch-004/qc.json;
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch005
    only after fresh fetch/base/tree equality and all 9,182 tracked file bytes and
    modes were verified against the original batch004 baseline (208,070,649 bytes).
    This gate was not rerun for batch005; original times, scope, warnings, exceptions
    and skips are preserved.'
  target_ids:
  - CHEBI:167886
- check_id: S045-C-PATHWAY
  name: Claim-by-claim primary reaction and graph audit
  status: passed
  required: true
  summary: All seven transformations, 13 nodes and 15 edges agree with the 2022 primary
    chemistry. The native protein-core correspondence independently passed; recombinant
    construct and accessory-reagent boundaries are retained.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2022-MAIN
  - S045-2022-SI
  - S045-CORE-BRIDGE
- check_id: S045-C-CITATION
  name: Claim-local support for the exact locus enzymatic method
  status: failed
  required: true
  summary: The exact final-product enzymology is correctly cited elsewhere in the
    owner but not at the MIBiG locus claim, whose inherited 2021 citation establishes
    only the AetF precursor assay. This is a minor evidence-placement defect, not
    an unsupported pathway or method.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-RAW
  - S045-2021-MAIN
  - S045-2022-MAIN
  - S045-REFERENCE-LOADER
- check_id: S045-C-STRAIN
  name: Primary verification of the CyanoMetDB CBT1886 designation
  status: unavailable
  required: true
  summary: The complete accessible 2021 main text supports the native 2011 cyanobacterium
    and species occurrence, but it does not resolve the literal CBT1886 designation.
    The required supplement remains inaccessible; no equivalence to Thurmond2011 or
    rejection of the database assertion is inferred.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OCCURRENCE-ROWS
  - S045-2021-MAIN
  - S045-2021-SI-ACCESS
- check_id: P045-C-PROTEINS
  name: Full native and published insert sequence identity
  status: passed
  required: true
  summary: All five current reviewed sequences exactly equal independently translated
    native CDSs and published coding cores; no partial native CDS or unresolved accession
    crosswalk remains.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-PROTEIN-COMPARE
  - P045-GENBANK
  - P045-AETA-LEGACY
  - P045-SI-CONSTRUCTS
  - P045-UNIPROT-AETA
  - P045-UNIPROT-AETB
  - P045-UNIPROT-AETD
  - P045-UNIPROT-AETE
  - P045-UNIPROT-AETF
- check_id: P045-C-REACTIONS
  name: Existing reaction and molecular grounding
  status: passed
  required: true
  summary: All seven Rhea equations and all existing molecular identifiers resolve
    consistently, with the neutral/zwitterion L-tryptophan distinction explicitly
    preserved.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-REACTION-COMPARE
  - P045-CHEBI-TRP
  - P045-CHEBI-ZWITTERION
- check_id: R045-C-PARENT
  name: Exact parent authority graph and source resolution
  status: passed
  required: true
  summary: Independent parent graphs and official identifiers agree; DOI/method claim
    placement is evaluated separately.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - R045-CHEM
  - R045-WIKI-COMPARE
  - R045-CHEBI
  - R045-MIBIG
- check_id: R045-C-IMODULON
  name: Applicable native expression dataset
  status: not_applicable
  required: false
  summary: No matching organism/strain dataset appears in the complete retained catalogue.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - R045-IMODULON
evidence:
- evidence_id: S045-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/aetokthonotoxin.yaml
  locator: Complete 622-line owner and resolved content; all three occurrences, producer/locus,
    seven steps, 13 nodes, 15 edges, classifications and history
  accessed_at: '2026-10-21T11:14:02.949732Z'
  support: supports
  summary: The exact neutral pentabrominated biindole has key JXJDQKCOJBAPQM-UHFFFAOYSA-N.
    The owner contains three source-specific A. hydrillicola occurrences, native Thurmond2011
    producer, source method Enzymatic assays, SOURCE_ASSERTION/CLUSTER_DEMONSTRATED
    grades, and seven explicitly cited recombinant enzyme reactions. No quantitative
    bioactivity or molecular target is asserted.
  snapshot_sha256: 07ff54c044737bda66d471d372c8f958ff994585d06b7876aed5ea45da160f76
- evidence_id: S045-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete BGC0002643:1 version 2 row; canonical complete-row SHA256 6b6ed3bd66bf39cc49b5da5c9d758c30af79161d20b0f9cb2987a3b6e50af46f
  accessed_at: '2026-10-21T11:14:02.949732Z'
  support: supports
  summary: The imported row exactly reproduces the owner chemistry, Thurmond2011 taxon,
    MT225528.1:1..9229 interval, Enzymatic assays method and grades. Both emitted
    claims inherit PMID:33766860 through COMPOUND_EVIDENCE. Entry quality questionable
    and completeness unknown are source metadata, not independent experimental conclusions.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S045-OCCURRENCE-ROWS
  kind: record_content
  reference: /private/tmp/npm-review-work/045/local-sources.json
  locator: All exact-key LOTUS, CyanoMetDB, ChEBI-origin and NPClassifier rows
  accessed_at: '2026-10-21T11:14:02.949732Z'
  support: supports
  summary: LOTUS and ChEBI report species-level A. hydrillicola occurrence from the
    2021 Science study. CyanoMetDB additionally reports strain CBT1886 and nmr_used=yes.
    These distinct source assertions are preserved; their shared paper is not three
    independent isolation experiments. NPClassifier returns Alkaloids and is_glycoside=false,
    with empty superclass/class results.
  snapshot_sha256: 107bc02b2acae02cc0dfb34fd6820a4cbc19bb4042b5f8c28e7ec658b7602bde
- evidence_id: S045-2021-MAIN
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=8318203&retmode=xml
  locator: DOI:10.1126/science.aax9050; PMID:33766860; complete main body and methods
    summary, especially paragraphs 8, 10, 14, 15, 17 and 19 in retained body extraction
  accessed_at: '2026-10-21T10:41:42.370346Z'
  support: supports
  summary: The authors isolated AETX from bromide-supplemented A. hydrillicola cultures
    and field assemblages, and explicitly confirmed production by the cyanobacterium
    isolated in 2011 from J. Strom Thurmond Reservoir. The 2011 and 2014 genomes contain
    the same six-gene locus. Recombinant AetF establishes precursor bromination only
    in this paper. Pure AETX caused vacuolar lesions in experimentally exposed chickens;
    bald-eagle causation combines this result with the ecological and chemical evidence.
  snapshot_sha256: c362dede336f418b9f172d5c28b39e6adde51b66c9b66698c4f50e31e15ae18e
- evidence_id: S045-2021-FIGURES
  kind: primary_source
  reference: https://pure.mpg.de/rest/items/item_3352301/component/file_3352376/content
  locator: Original physical PDF pages 4 and 5, printed pages 3 and 4 of 7; Figures
    2, 3 and 4 pixels
  accessed_at: '2026-10-21T10:42:15.012106Z'
  support: supports
  summary: Figure 3 shows N1–C2′ linked indoles, bromines at 2,3,5 and 5′,7′, and
    a 3′ nitrile, agreeing with the owner constitution and C17H6Br5N3 formula. No
    tetrahedral stereocentres are depicted. Figure 2 localizes toxin to cyanobacterial
    colonies; Figure 4 shows the cluster and AetF precursor assay. The visual structural
    comparison is not a new crystallographic refinement or complete spectral reinterpretation.
  snapshot_sha256: 681157f4bd688f0be61c6473dac515712a85dc5df82af1e66931424989eed514
- evidence_id: S045-2022-MAIN
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=9004672&retmode=xml
  locator: DOI:10.1021/jacs.1c12778; PMID:35142504; full main scientific body paragraphs
    1–9 and all main figure captions
  accessed_at: '2026-10-21T10:41:42.369901Z'
  support: supports
  summary: 'The study reconstitutes the exact pathway reactions using purified recombinant
    proteins: AetF performs two tryptophan brominations; AetE releases 5-bromoindole;
    AetA forms 3,5-dibromoindole then 2,3,5-tribromoindole; AetD produces the dibromoindole
    nitrile; AetB couples the exact two monomers to AETX. The final product matches
    a synthetic standard by chromatography and mass. AetC was not required for the
    measured reactions. No native knockout, whole-cell heterologous AETX production
    or single one-pot five-enzyme synthesis is claimed by this audit.'
  snapshot_sha256: f98bbf0d8fb71320cb315ed1b0e3f2c60528dd3e429f7f71f18ab374739d811e
- evidence_id: S045-2022-SI
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/34030520
  locator: Official ja1c12778_si_001.pdf; methods/coding sequences pages 1–13, relevant
    Table S3 entries page 15, page 16 caption, assay pages 17–20, synthesis pages
    21–25; original pixels pages 12, 17–20 and 24
  accessed_at: '2026-10-21T10:42:15.010657Z'
  support: supports
  summary: Codon-optimized inserts were expressed in E. coli BL21(DE3); AetB used
    a His-MBP fusion and AetE used GroEL/ES. AetB assays used the two exact monomers
    plus spinach ferredoxin, ferredoxin reductase and NADPH. AetE pyruvate was detected
    after derivatization. AetD assays distinguish enzyme, AetC and metal conditions
    and follow amino nitrogen into nitrile. The separately synthesized AETX standard
    has reported NMR agreement with prior literature. Table S3 uses historical AetA
    A0A861B8S3. Later spectral pages and every sequence-network row were not exhaustively
    inspected.
  snapshot_sha256: 6104c9934a6444d1ebb51fd6590ca45a62746994cd3a636e1ddf518e56fa006a
- evidence_id: S045-2023-AETD
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10654658/fullTextXML
  locator: DOI:10.1038/s41467-023-43285-0; PMID:37973794; complete scientific body,
    methods and figure captions
  accessed_at: '2026-10-21T10:40:51.444218Z'
  support: supports
  summary: The structural and biochemical study supports diiron AetD and distinguishes
    recombinant wild type from site-directed variants. It is not a native organism
    knockout study. Its proposed mechanistic route does not itself establish the glycolate
    coproduct; the later 2024 source provides that direct chemical evidence.
  snapshot_sha256: e7c6b0699d3833dc97d1659e26aa14695a819cf60cbb98c456aed78ad4584d5a
- evidence_id: S045-2024-AETD
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11611611&retmode=xml
  locator: DOI:10.1038/s41557-024-01603-z; PMID:39285206; full main scientific body
    and Methods, especially Results paragraphs 17–28 and Figures 4–6 captions
  accessed_at: '2026-10-21T11:08:08.982301Z'
  support: supports
  summary: Isotope tracing and NMR identify glycolic acid as the two-carbon coproduct
    of the AetD nitrile-forming reaction; stopped-flow experiments directly probe
    oxygen-dependent iron chemistry. These results support the later Rhea oxygen/glycolate
    annotation. The detailed aziridine/nitrone route remains a proposal. Experiments
    use recombinant AetD, not a new cyanobacterial knockout or transport assay. Supplementary
    files and original 2024 figure pixels were not independently inspected.
  snapshot_sha256: 5601cef15709db9949d91abf7c2f200282d925d52b214d12d5f02556990b34d0
- evidence_id: S045-SI-CORES
  kind: validation
  reference: /private/tmp/npm-review-work/045/si2022-coding-cores.json
  locator: Independent translation of all six printed codon-optimized coding inserts
    on SI pages 3–5; terminal stops removed explicitly
  accessed_at: '2026-10-21T11:14:02.949732Z'
  support: supports
  summary: The published cores are AetA 596, AetB 485, AetC 174, AetD 239, AetE 468
    and AetF 668 residues, with no internal stops. A first parsing attempt spanning
    a form-feed boundary was corrected before these complete outputs were accepted.
    The file retains the DNA and amino-acid strings; these cores exclude vector tags
    and the AetB MBP fusion.
  snapshot_sha256: e2e8acf87adc1fa882a20fcacb73e9226c94f7f491d2dbc0c2c1044574a1e749
- evidence_id: S045-CORE-BRIDGE
  kind: validation
  reference: /private/tmp/npm-review-work/045/protein-reaction/protein-equivalence.json
  locator: Independent collaborator comparison, read in full; six native MT225528.1
    translations and five complete owner UniProt sequences
  accessed_at: '2026-10-21T11:10:00.372991Z'
  support: supports
  summary: All six native deposited translations equal the published SI amino-acid
    cores. All five owner UniProt proteins match their complete native sequences.
    Historical AetA A0A861B8S3 is a secondary accession of A0AAP5I1G4. This supports
    applying the measured core-enzyme chemistry to the stored locus while preserving
    codon optimization, recombinant tags and assay conditions. It does not establish
    native knockout or whole-cell expression evidence.
  snapshot_sha256: 2c16aa366ea6141e9ba550d46678e2be8b561cfdae6952040efca6b8799f4c46
- evidence_id: S045-2021-SI-ACCESS
  kind: search
  reference: /private/tmp/npm-review-work/shared-next-batch005/aetokthonotoxin/2021-si-recovery-notes.json
  locator: Preserved exact NCBI instance-path media attempt and official institutional
    metadata; separate Europe PMC supplementaryFiles response inspected in full
  accessed_at: '2026-10-21T10:50:31.257655Z'
  support: context_only
  summary: 'The linked 2021 supplement was not recovered: the exact NCBI media URL
    returned HTML with a JavaScript download challenge, and Europe PMC returned a
    not-open-access XML error rather than an archive. The institutional item lists
    only the main article. These are access limitations, not evidence that the supplement
    or strain documentation does not exist.'
  snapshot_sha256: e96115bf8c91fa6ba50dbed98a10df0a1e29add7ecfc2ab0f4129b1713a266ae
  search_scope: Bounded prior Science, exact PMC supplement, institutional item and
    Europe PMC supplementaryFiles requests for DOI 10.1126/science.aax9050, with original
    receipts retained. The later Europe PMC note finished at 2026-10-21T10:51:58.650065Z.
    No repeated failed retrieval or exhaustive literature-absence claim.
- evidence_id: S045-REFERENCE-LOADER
  kind: record_content
  reference: src/naturalproductmech/curate/claim_references.py
  locator: Entire load_claim_references and correct_claim_reference implementations;
    exact required fields and complete-row guard
  accessed_at: '2026-10-21T11:14:02.949732Z'
  support: context_only
  summary: The consumed claim-reference table can independently route producer and
    locus citations using a complete raw-row SHA. It retains raw citation provenance
    and does not change chemistry, taxa, methods or grades. It rejects structure-corrected
    rows; no structure correction is proposed here. A method REPLACE overlay is unnecessary
    for this citation-only repair.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: S045-CYANO-EMITTER
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: CyanoMetDB occurrence generation, especially lines 1221–1234 and the exact
    nmr_used=yes source row
  accessed_at: '2026-10-21T11:14:02.949732Z'
  support: context_only
  summary: The emitter interpolates the NMR-used flag into structure confirmed by
    yes. The flag records whether NMR was used, not a confirmation method named yes
    or an independent reviewer certification. This is the same shared emitter issue
    already recorded under cyanometdb-nmr-used-rendered-as-structure-confirmed.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S045-MAINTAINED-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/045/science-maintained-search.json
  locator: Ignored-inclusive maintained correction search
  accessed_at: '2026-10-21T11:14:02.979527Z'
  support: context_only
  summary: No existing target-specific correction was found in the searched curation,
    configuration and curation-consumer paths. This bounded result supports proposing
    a new exact-source citation row; it does not establish that no external literature
    exists.
  snapshot_sha256: 23f17ab100c682b10c58e08260e473a7a2b13601a5980d45fa056122fa773f06
  search_scope: Ignored-inclusive target-specific search of maintained curation/configuration/curation-consumer
    files; no global source absence claim.
- evidence_id: P045-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/aetokthonotoxin.yaml
  locator: 'Full owner: seven pathway steps, thirteen graph nodes and fifteen graph
    edges'
  accessed_at: '2026-10-21T11:12:12.830568Z'
  support: supports
  summary: All five existing enzyme identifiers, seven Rhea reaction identifiers and
    eight pathway chemical identifiers were inventoried before comparison. The graph
    is explicitly scoped to in vitro branch construction and coupling. It does not
    assert an AetC reaction or that purified proteins came directly from native cyanobacterial
    culture.
  snapshot_sha256: 07ff54c044737bda66d471d372c8f958ff994585d06b7876aed5ea45da160f76
- evidence_id: P045-GENBANK
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=MT225528.1&rettype=gb&retmode=text
  locator: Header, source, all six complete CDS locations/qualifiers and entire ORIGIN
    sequence; independently translated
  accessed_at: '2026-10-21T11:07:12.375297Z'
  support: supports
  summary: MT225528.1 contains 9,229 bp from A. hydrillicola Thurmond2011, taxon2712845,
    and six complete plus-strand CDSs. AetA/QNL15171.1 is1..1791; AetB/QNL15172.1
    2143..3600; AetD/QNL15174.1 4241..4960; AetE/QNL15175.1 5479..6885; AetF/QNL15176.1
    7223..9229. All have codon_start1 and translation table11, without partial markers.
    The original AetD putative-methyltransferase note is historical annotation, not
    the current primary biochemical assignment.
  snapshot_sha256: 883564afdbbfecf1c5fd1163056d0ed85ce11c7643828635a0a2acf0fc62423f
- evidence_id: P045-UNIPROT-AETA
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0AAP5I1G4.json
  locator: Entry type/audit, gene/organism, complete sequence, EMBL cross-references,
    all comments and references including evidence attribution
  accessed_at: '2026-10-21T11:07:14.880843Z'
  support: supports
  summary: A0AAP5I1G4 is reviewed Swiss-Prot aetA from taxon2712845, 596 aa, entry
    version8, sequence version2. Its MT225528 genomic cross-reference gives QNL15171.1;
    the full current sequence equals the independently translated native CDS and the
    published 2022 coding-insert core. AetA lists historical A0A861B8S3 as secondary;
    its erroneous-initiation caution refers specifically to alternate-genome MDR9893084.1,
    not complete QNL15171.1.
  snapshot_sha256: 47067376ae8a28fc10033b8410b96bd169a779c7758974fe45a0ea8d651063ce
- evidence_id: P045-UNIPROT-AETB
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A861B5L6.json
  locator: Entry type/audit, gene/organism, complete sequence, EMBL cross-references,
    all comments and references including evidence attribution
  accessed_at: '2026-10-21T11:07:14.435006Z'
  support: supports
  summary: A0A861B5L6 is reviewed Swiss-Prot aetB from taxon2712845, 485 aa, entry
    version20, sequence version1. Its MT225528 genomic cross-reference gives QNL15172.1;
    the full current sequence equals the independently translated native CDS and the
    published 2022 coding-insert core.
  snapshot_sha256: 0bd2fbbe4880bd8709417eb26869ee7f2b9b4bb0c590c2fd48daa47011bcb311
- evidence_id: P045-UNIPROT-AETD
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A861B387.json
  locator: Entry type/audit, gene/organism, complete sequence, EMBL cross-references,
    all comments and references including evidence attribution
  accessed_at: '2026-10-21T11:07:14.129953Z'
  support: supports
  summary: A0A861B387 is reviewed Swiss-Prot aetD from taxon2712845, 239 aa, entry
    version17, sequence version1. Its MT225528 genomic cross-reference gives QNL15174.1;
    the full current sequence equals the independently translated native CDS and the
    published 2022 coding-insert core. Its current functional annotation combines
    the 2022 nitrile study with later 2023/2024 structural, coproduct and mechanism
    studies; these are not backdated into the 2022 assay.
  snapshot_sha256: 17683472b84bd1eb1468c22d2377039660c6911c5e54fce0953221f4c82cc5fb
- evidence_id: P045-UNIPROT-AETE
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A861BA10.json
  locator: Entry type/audit, gene/organism, complete sequence, EMBL cross-references,
    all comments and references including evidence attribution
  accessed_at: '2026-10-21T11:07:14.786639Z'
  support: supports
  summary: A0A861BA10 is reviewed Swiss-Prot aetE from taxon2712845, 468 aa, entry
    version18, sequence version1. Its MT225528 genomic cross-reference gives QNL15175.1;
    the full current sequence equals the independently translated native CDS and the
    published 2022 coding-insert core.
  snapshot_sha256: 03ede04b31b9174fbbb2f919b077b990e094942783e8576d23c55cf1b0037f0c
- evidence_id: P045-UNIPROT-AETF
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A861B9Z9.json
  locator: Entry type/audit, gene/organism, complete sequence, EMBL cross-references,
    all comments and references including evidence attribution
  accessed_at: '2026-10-21T11:07:14.483879Z'
  support: supports
  summary: A0A861B9Z9 is reviewed Swiss-Prot aetF from taxon2712845, 668 aa, entry
    version16, sequence version1. Its MT225528 genomic cross-reference gives QNL15176.1;
    the full current sequence equals the independently translated native CDS and the
    published 2022 coding-insert core. Later substrate-scope, structural and engineered-variant
    annotations, including a 1–655 crystallographic construct and 2025 variants, do
    not redefine the 668-aa native sequence or the 2022 assay construct.
  snapshot_sha256: 825121aa2036565396111b71e9289081c8943300ab22999d3dd594a8d46a108d
- evidence_id: P045-AETA-LEGACY
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A861B8S3.json
  locator: Actual HTTP redirect final URL and complete returned primary/secondary
    accession fields
  accessed_at: '2026-10-21T11:09:37.998131Z'
  support: supports
  summary: The exact historical accession request A0A861B8S3 redirects to A0AAP5I1G4
    and returns byte-identical current JSON. Together with the explicit secondary-accession
    field, this verifies continuity with SI Table S3; it is not an inferred crosswalk
    from a similar protein name.
  snapshot_sha256: 47067376ae8a28fc10033b8410b96bd169a779c7758974fe45a0ea8d651063ce
- evidence_id: P045-PROTEIN-COMPARE
  kind: validation
  reference: /private/tmp/npm-review-work/045/protein-reaction/protein-equivalence.json
  locator: All native CDS translations, submitted translations, five current UniProt
    sequences and six published coding cores
  accessed_at: '2026-10-21T11:10:00.372991Z'
  support: supports
  summary: 'All five owner protein sequences match exactly across the native genomic
    translation, GenBank qualifier, current UniProt and the full published coding
    core: AetA596, AetB485, AetD239, AetE468 and AetF668 aa. Context-only AetC174
    aa also matches the native/SI comparison. Native and codon-optimized DNA differ
    as expected; no fusion/tag sequence equivalence is claimed.'
  snapshot_sha256: 2c16aa366ea6141e9ba550d46678e2be8b561cfdae6952040efca6b8799f4c46
- evidence_id: P045-SI-CONSTRUCTS
  kind: primary_source
  reference: https://api.figshare.com/v2/file/download/34030520
  locator: DOI10.1021/jacs.1c12778 official SI pp3–5 coding inserts, pp7–10 expression/construct
    protocols, original p15 Table S3 pixels
  accessed_at: '2026-10-21T10:42:15.010657Z'
  support: supports
  summary: The SI supplies E. coli codon-optimized aetA–F inserts in pET28a, His-tagged
    AetA/C/F/D/E and an MBP-AetB construct expressed in BL21(DE3); its S3 caption
    describes His-MBP-AetB plus likely cleavage products. The original Table S3 lists
    AetA A0A861B8S3 and AetF A0A861B9Z9. Coding cores support the native reference
    bridge while tags, junctions and fusion state remain assay-specific. No complete
    fusion sequence or cleavage fraction was independently reconstructed.
  snapshot_sha256: 6104c9934a6444d1ebb51fd6590ca45a62746994cd3a636e1ddf518e56fa006a
- evidence_id: P045-RHEA-82463
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A82463&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step1 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.317370Z'
  support: supports
  summary: bromide + L-tryptophan + NADPH + O2 + 2 H(+) = 5-bromo-L-tryptophan + NADP(+)
    + 2 H2O. The complete equation exactly matches the current reviewed protein catalytic
    annotation, which separately provides a left-to-right physiological Rhea variant.
    The owner stores the valid master reaction ID and abbreviates rather than fully
    balances its prose. This master equation uses CHEBI57912 zwitterion, while the
    owner precursor is neutral CHEBI16828; their chemically related state distinction
    is explicitly assessed below.
  snapshot_sha256: 111187537f554f3bcc900e5147b73111a696cb50f97017ad33e754ccce5d491d
- evidence_id: P045-RHEA-82467
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A82467&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step2 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.407085Z'
  support: supports
  summary: 5-bromo-L-tryptophan + bromide + NADPH + O2 + 2 H(+) = 5,7-dibromo-L-tryptophan
    + NADP(+) + 2 H2O. The complete equation exactly matches the current reviewed
    protein catalytic annotation, which separately provides a left-to-right physiological
    Rhea variant. The owner stores the valid master reaction ID and abbreviates rather
    than fully balances its prose.
  snapshot_sha256: 11ff85478222a0e234d9e60802b74f549dbb87eef40c69b9e3f6599e48bfdf84
- evidence_id: P045-RHEA-82523
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A82523&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step3 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.638518Z'
  support: supports
  summary: 5-bromo-L-tryptophan + H2O = 5-bromoindole + pyruvate + NH4(+). The complete
    equation exactly matches the current reviewed protein catalytic annotation, which
    separately provides a left-to-right physiological Rhea variant. The owner stores
    the valid master reaction ID and abbreviates rather than fully balances its prose.
  snapshot_sha256: e4833878904aa7ce7564b45b29aa2a850a5b32ca1cd814ce5cb10602c11a4aa0
- evidence_id: P045-RHEA-82527
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A82527&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step4 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.838283Z'
  support: supports
  summary: 5-bromoindole + bromide + FADH2 + O2 = 3,5-dibromoindole + FAD + 2 H2O.
    The complete equation exactly matches the current reviewed protein catalytic annotation,
    which separately provides a left-to-right physiological Rhea variant. The owner
    stores the valid master reaction ID and abbreviates rather than fully balances
    its prose.
  snapshot_sha256: 1165bbad4f22ac3f7e70710114362b14cbe118b950cf79eee39d27dfe0e1358b
- evidence_id: P045-RHEA-82531
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A82531&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step5 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.932028Z'
  support: supports
  summary: 3,5-dibromoindole + bromide + FADH2 + O2 = 2,3,5-tribromoindole + FAD +
    2 H2O. The complete equation exactly matches the current reviewed protein catalytic
    annotation, which separately provides a left-to-right physiological Rhea variant.
    The owner stores the valid master reaction ID and abbreviates rather than fully
    balances its prose.
  snapshot_sha256: 40f47d805c181c7f3c01ad559536ecbe4e6556fafe669e6d9815966c01706290
- evidence_id: P045-RHEA-81787
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A81787&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step6 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.048142Z'
  support: supports
  summary: 5,7-dibromo-L-tryptophan + O2 = 5,7-dibromo-indole-3-carbonitrile + glycolate
    + H2O + H(+). The complete equation exactly matches the current reviewed protein
    catalytic annotation, which separately provides a left-to-right physiological
    Rhea variant. The owner stores the valid master reaction ID and abbreviates rather
    than fully balances its prose. Glycolate belongs to this current database equation;
    experimental support and publication timing are separately assessed in the primary-source
    packet.
  snapshot_sha256: 45d7dbb8aa15b9a4b2fbdbc0c3b8f5c3cc183ab9ee399a435e6f7bfc63c6fa4c
- evidence_id: P045-RHEA-82519
  kind: database
  reference: https://www.rhea-db.org/rhea?query=rhea%3A82519&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: Complete one-row TSV; pathway step7 and corresponding existing graph edges
  accessed_at: '2026-10-21T11:07:15.526129Z'
  support: supports
  summary: 5,7-dibromo-indole-3-carbonitrile + 2,3,5-tribromoindole + 2 reduced [2Fe-2S]-[ferredoxin]
    + O2 + 2 H(+) = aetokthonotoxin + 2 oxidized [2Fe-2S]-[ferredoxin] + 2 H2O. The
    complete equation exactly matches the current reviewed protein catalytic annotation,
    which separately provides a left-to-right physiological Rhea variant. The owner
    stores the valid master reaction ID and abbreviates rather than fully balances
    its prose.
  snapshot_sha256: c0c95df7d0382483e5fb113371fa41f5372930f4762128ed50e8a32462b289de
- evidence_id: P045-MOL-16828
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/16828/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:36.605499Z'
  support: supports
  summary: Official CHEBI16828 MOL resolves L-tryptophan, C11H12N2O2, full key QIVBCDIJIAJPQS-VIFPVBQESA-N.
    Its official graph has no charged atoms. Direct MOL reconstruction agrees with
    the separately encoded named positional substitution pattern, full Standard identity
    and fixed-H form. This verifies a chemical identifier, not an experiment.
  snapshot_sha256: a7c29d96ee48fd4a63ad7a5f2e6b26f3ffbef0a500cbd7568c96aae1b194417e
- evidence_id: P045-MOL-57912
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/57912/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:36.606015Z'
  support: supports
  summary: Official CHEBI57912 MOL resolves L-tryptophan zwitterion, C11H12N2O2, full
    key QIVBCDIJIAJPQS-VIFPVBQESA-N. It is a zwitterion with one positive and one
    negative atom despite zero net charge. Direct MOL reconstruction agrees with the
    separately encoded named positional substitution pattern, full Standard identity
    and fixed-H form. This verifies a chemical identifier, not an experiment.
  snapshot_sha256: 8ed87d527dbc3731e9664773089c01846c9c00a88509302a6765494f9896df4f
- evidence_id: P045-MOL-232362
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232362/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:37.335605Z'
  support: supports
  summary: Official CHEBI232362 MOL resolves 5-bromo-L-tryptophan zwitterion, C11H11BrN2O2,
    full key KZDNJQUJBMDHJW-VIFPVBQESA-N. It is a zwitterion with one positive and
    one negative atom despite zero net charge. Direct MOL reconstruction agrees with
    the separately encoded named positional substitution pattern, full Standard identity
    and fixed-H form. This verifies a chemical identifier, not an experiment.
  snapshot_sha256: dbc13bd383b3f8acb5464341a56d5e87139e51e5a64358127994870237c43049
- evidence_id: P045-MOL-231978
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/231978/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:36.606156Z'
  support: supports
  summary: Official CHEBI231978 MOL resolves 5,7-dibromo-L-tryptophan zwitterion,
    C11H10Br2N2O2, full key UURVQGNSCUCIQS-VIFPVBQESA-N. It is a zwitterion with one
    positive and one negative atom despite zero net charge. Direct MOL reconstruction
    agrees with the separately encoded named positional substitution pattern, full
    Standard identity and fixed-H form. This verifies a chemical identifier, not an
    experiment.
  snapshot_sha256: 2f30fe27a72840df129a667e1cc720668231df6a7ceb310024d9e03e875af770
- evidence_id: P045-MOL-231979
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/231979/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:36.606287Z'
  support: supports
  summary: Official CHEBI231979 MOL resolves 5,7-dibromo-indole-3-carbonitrile, C9H4Br2N2,
    full key IVEGXYGMXKFJDG-UHFFFAOYSA-N. Its official graph has no charged atoms.
    Direct MOL reconstruction agrees with the separately encoded named positional
    substitution pattern, full Standard identity and fixed-H form. This verifies a
    chemical identifier, not an experiment.
  snapshot_sha256: bfd618f520401d5523471ae3632ef12dbe292c6c6ebb46d3899ec74ef0a82b53
- evidence_id: P045-MOL-232363
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232363/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:37.357723Z'
  support: supports
  summary: Official CHEBI232363 MOL resolves 2,3,5-tribromoindole, C8H4Br3N, full
    key KUPJVNCDFREPQN-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct
    MOL reconstruction agrees with the separately encoded named positional substitution
    pattern, full Standard identity and fixed-H form. This verifies a chemical identifier,
    not an experiment.
  snapshot_sha256: 4913235f5ff560bc41d16b0ed75dc25441924f0b82e642d7571630fe0cf5459c
- evidence_id: P045-MOL-232364
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232364/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:37.367153Z'
  support: supports
  summary: Official CHEBI232364 MOL resolves 5-bromoindole, C8H6BrN, full key VXWVFZFZYXOBTA-UHFFFAOYSA-N.
    Its official graph has no charged atoms. Direct MOL reconstruction agrees with
    the separately encoded named positional substitution pattern, full Standard identity
    and fixed-H form. This verifies a chemical identifier, not an experiment.
  snapshot_sha256: dd7b52c08cbfe8cfdcd7595c51dce6ff45fee785cab13115cc94e0f15a0a787f
- evidence_id: P045-MOL-232365
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/232365/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:37.411239Z'
  support: supports
  summary: Official CHEBI232365 MOL resolves 3,5-dibromoindole, C8H5Br2N, full key
    NGTBILHUFBABDS-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL
    reconstruction agrees with the separately encoded named positional substitution
    pattern, full Standard identity and fixed-H form. This verifies a chemical identifier,
    not an experiment.
  snapshot_sha256: a27b58ae15d128a2dcb56877985dd4d0dc16c353b11774c1a46bca6e6d46ccaa
- evidence_id: P045-MOL-167886
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/167886/
  locator: Complete official MOL graph; direct chemical comparison including position,
    charge and stereochemistry
  accessed_at: '2026-10-21T11:09:37.957543Z'
  support: supports
  summary: Official CHEBI167886 MOL resolves aetokthonotoxin, C17H6Br5N3, full key
    JXJDQKCOJBAPQM-UHFFFAOYSA-N. Its official graph has no charged atoms. Direct MOL
    reconstruction agrees with the separately encoded named positional substitution
    pattern, full Standard identity and fixed-H form. This verifies a chemical identifier,
    not an experiment.
  snapshot_sha256: ed59d8d6d6cd7a43e670f2c7ace01d18dcf98fd5276e744e3c0ef761e86f25f2
- evidence_id: P045-CHEBI-TRP
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16828/
  locator: Exact compound name, formula, charge, default InChI/key and CHEBI57912
    relation
  accessed_at: '2026-10-21T11:07:12.912510Z'
  support: supports
  summary: CHEBI16828 denotes neutral L-tryptophan, three-star, with a specified S
    centre. The authority explicitly links its zwitterion CHEBI57912 as a tautomer.
    The pathway uses this neutral compound identifier without asserting that neutral
    species predominates in buffered enzyme assays.
  snapshot_sha256: eb4325e5454737b389b5c29eb32c8c675786ec4042ef61aea9cde988baaec4a9
- evidence_id: P045-CHEBI-ZWITTERION
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/57912/
  locator: Complete compound response, exact molecular form and explicit tautomer
    relation
  accessed_at: '2026-10-21T11:09:37.969052Z'
  support: supports
  summary: CHEBI57912 denotes L-tryptophan zwitterion, three-star, with the same S
    centre and molecular formula; the authority describes it as the major species
    at pH7.3 and links CHEBI16828. Rhea82463 uses this species. Equal Standard InChI
    does not make their fixed-H representations identical.
  snapshot_sha256: 1674f1a123837222ea372e13b92d6252b45fde202203c50cae274cfe812f88cb
- evidence_id: P045-CHEBI-231978
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/231978/
  locator: Complete exact intermediate response; name, formula, charge, full InChI/key
    and ontology form
  accessed_at: '2026-10-21T11:07:13.119476Z'
  support: supports
  summary: The exact entry is the named pathway intermediate and has the same formula/full
    Standard key as its separately inspected official MOL. Current rating is two-star;
    that does not invalidate its use as a resolvable pathway identifier. The full
    MOL, rather than the API display SMILES, supplies protonation and indole hydrogen
    details.
  snapshot_sha256: e98244d80901cfb51aabea84e0ab9bff767ce05be7826ae4d5a225276804acc8
- evidence_id: P045-CHEBI-231979
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/231979/
  locator: Complete exact intermediate response; name, formula, charge, full InChI/key
    and ontology form
  accessed_at: '2026-10-21T11:07:13.450286Z'
  support: supports
  summary: The exact entry is the named pathway intermediate and has the same formula/full
    Standard key as its separately inspected official MOL. Current rating is two-star;
    that does not invalidate its use as a resolvable pathway identifier. The full
    MOL, rather than the API display SMILES, supplies protonation and indole hydrogen
    details.
  snapshot_sha256: 049495b4d77339e455cb6948a3d02c6899a03624cf14d26d2661767baca442c9
- evidence_id: P045-CHEBI-232362
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/232362/
  locator: Complete exact intermediate response; name, formula, charge, full InChI/key
    and ontology form
  accessed_at: '2026-10-21T11:07:13.490883Z'
  support: supports
  summary: The exact entry is the named pathway intermediate and has the same formula/full
    Standard key as its separately inspected official MOL. Current rating is two-star;
    that does not invalidate its use as a resolvable pathway identifier. The full
    MOL, rather than the API display SMILES, supplies protonation and indole hydrogen
    details.
  snapshot_sha256: 45f93ba8b9c5138e583bf8f75c0e3aae8f2be5f4ebfbad5ca63834ad42d92bb5
- evidence_id: P045-CHEBI-232363
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/232363/
  locator: Complete exact intermediate response; name, formula, charge, full InChI/key
    and ontology form
  accessed_at: '2026-10-21T11:07:13.775735Z'
  support: supports
  summary: The exact entry is the named pathway intermediate and has the same formula/full
    Standard key as its separately inspected official MOL. Current rating is two-star;
    that does not invalidate its use as a resolvable pathway identifier. The full
    MOL, rather than the API display SMILES, supplies protonation and indole hydrogen
    details.
  snapshot_sha256: 4cb87999abbf51fa084b0855ad99628dac54be41771ee2678812cf911a04877e
- evidence_id: P045-CHEBI-232364
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/232364/
  locator: Complete exact intermediate response; name, formula, charge, full InChI/key
    and ontology form
  accessed_at: '2026-10-21T11:07:13.838465Z'
  support: supports
  summary: The exact entry is the named pathway intermediate and has the same formula/full
    Standard key as its separately inspected official MOL. Current rating is two-star;
    that does not invalidate its use as a resolvable pathway identifier. The full
    MOL, rather than the API display SMILES, supplies protonation and indole hydrogen
    details.
  snapshot_sha256: a0f487c5b020637a4e1ba2ff7910d1ddf1a6897e55d42c36470da3cbdee4e64f
- evidence_id: P045-CHEBI-232365
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/232365/
  locator: Complete exact intermediate response; name, formula, charge, full InChI/key
    and ontology form
  accessed_at: '2026-10-21T11:07:14.117587Z'
  support: supports
  summary: The exact entry is the named pathway intermediate and has the same formula/full
    Standard key as its separately inspected official MOL. Current rating is two-star;
    that does not invalidate its use as a resolvable pathway identifier. The full
    MOL, rather than the API display SMILES, supplies protonation and indole hydrogen
    details.
  snapshot_sha256: 5fbe1b52a000b376ca70c032c5a8aaa1b74b08b1554e636262dea8901be3c1c2
- evidence_id: P045-REACTION-COMPARE
  kind: validation
  reference: /private/tmp/npm-review-work/045/protein-reaction/reaction-chemical-comparison.json
  locator: All nine molecular forms and seven existing step/reaction/protein combinations;
    full graph identifier inventory
  accessed_at: '2026-10-21T11:10:37.186542Z'
  support: supports
  summary: 'Every existing chemical and protein node resolves, and all seven Rhea
    equations match current UniProt catalytic entries and participant identities.
    Step1 alone requires the explicit neutral/zwitterion bridge: same Standard InChI
    and S centre, different fixed-H InChI and internal charge placement. Owner AETX,
    current MIBiG AETX and official CHEBI167886 MOL agree in full Standard and fixed-H
    form. No new pathway edge or unasserted side reaction is inferred.'
  snapshot_sha256: 45fd4ee819de262c7c219dd82ad97b5205735a56404231040d6b95486df09e62
- evidence_id: R045-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/aetokthonotoxin.yaml
  locator: Entire 622-line owner, all seven steps, 13 nodes, 15 edges and four native
    history events
  accessed_at: '2026-10-21T11:12:42.919781Z'
  support: supports
  summary: The neutral exact parent CHEBI167886 has one MIBiG producer/locus, three
    source-specific occurrences and a curated biosynthetic pathway/graph. Its curation
    status remains SEEDED despite later recorded curation events. The review checks
    those assertions without promoting status or treating history as independent validation.
  snapshot_sha256: 07ff54c044737bda66d471d372c8f958ff994585d06b7876aed5ea45da160f76
- evidence_id: R045-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/045/protein-reaction/reaction-chemical-comparison.json
  locator: Parent owner/current-MIBiG/official-ChEBI-MOL comparison
  accessed_at: '2026-10-21T11:10:37.186542Z'
  support: supports
  summary: All three directly parsed parent graphs agree on full key JXJDQKCOJBAPQM-UHFFFAOYSA-N,
    fixed-H InChI, neutral C17H6Br5N3 and no tetrahedral stereocentre. The official
    MOL retains the indole N-H; the API display SMILES is not silently repaired and
    substituted.
  snapshot_sha256: 45fd4ee819de262c7c219dd82ad97b5205735a56404231040d6b95486df09e62
- evidence_id: R045-WIKI-COMPARE
  kind: validation
  reference: /private/tmp/npm-review-work/045/identity/wikidata-parent-comparison.json
  locator: Independent Wikidata P233 graph comparison
  accessed_at: '2026-10-21T11:12:43.754709Z'
  support: supports
  summary: The full Wikidata P233 graph also matches the owner standard and fixed-H
    identities. Its P234/P235 fields match the stored identity.
  snapshot_sha256: 61bb898170239dd586b773b734070e54ff4180b56b539b5bd67ca736294e3886
- evidence_id: R045-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/167886/
  locator: Retained complete response; stated relevant authority fields
  accessed_at: '2026-10-21T11:07:13.490741Z'
  support: supports
  summary: Released CHEBI167886 is three-star, with exact formula/full key, a source-attributed
    definition and A. hydrillicola taxon1550245/PMID33766860 origin. The definition
    and origin are audited against primary literature separately; current authority
    status supports EXACT grounding.
  snapshot_sha256: 32fa9306b53c2c3116d46c2269d61c35c5890b6e2252f07ceb020dbf085777d9
- evidence_id: R045-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002643.2/annotations.json
  locator: Retained complete response; stated relevant authority fields
  accessed_at: '2026-10-21T11:07:13.449999Z'
  support: supports
  summary: Active BGC0002643 version2 retains exact aetokthonotoxin, CyanoMetDB_2448,
    Thurmond2011 taxon2712845, MT225528.1:1..9229 and Enzymatic assays. Its biosynthesis
    path explicitly cites DOI10.1021/jacs.1c12778, whereas selected compound evidence
    includes PMID33766860. Quality questionable/completeness unknown are source flags.
    Entry-level activity fields are not additional owner activity claims.
  snapshot_sha256: 3e2fb16ea2d7151891b2e07d71e5ce0284ed50528497df9ab09e3fccaf7dc667
- evidence_id: R045-TAXON
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1550245,2712845&retmode=xml
  locator: Both top-level Taxon names, ranks, parent links, aliases and lineage
  accessed_at: '2026-10-21T11:07:12.737818Z'
  support: supports
  summary: NCBI1550245 is species Aetokthonos hydrillicola; NCBI2712845 is strain
    Thurmond2011 directly beneath that species. Cyanobacterial grouping is consistent.
    Neither taxonomy entry establishes CBT1886 as the same stock; that source-specific
    occurrence qualifier remains a separate primary-provenance question.
  snapshot_sha256: 634d1ce2624b46de2348c088134a0737771850e0ec13e78c2af8f0b649e412af
- evidence_id: R045-WIKI
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q106365096%7CQ67339642&props=labels%7Cclaims&languages=en&format=json
  locator: Both returned entities; labels and P685/P225/P233/P234/P235 identity claims
  accessed_at: '2026-10-21T11:07:12.912422Z'
  support: supports
  summary: Organism Q67339642 maps explicitly to NCBI1550245. Chemical Q106365096
    carries the exact parent graph, Standard InChI and full key. These links resolve
    the LOTUS concepts without independently proving culture provenance.
  snapshot_sha256: 6c17149e01af4ccd1d4e55d0f4af1469d290ec5fc7d33bf730c9df4684e3ed8c
- evidence_id: R045-RAW
  kind: record_content
  reference: data/raw/chebi_structures.tsv
  locator: Complete exact-key source projection and eligible three-star entry
  accessed_at: '2026-10-21T11:12:42.919781Z'
  support: supports
  summary: The pinned eligible CHEBI167886 entry and origin resolve the exact owner.
    The committed CyanoMetDB row is an exact-key Aetokthonotoxin/CBT1886/nmr_used=yes
    assertion citing the same2021 paper; the xref suffix2448 is inherited from MIBiG,
    not a second independent experiment. Three occurrence sources converge on one
    publication rather than three independent biological isolations.
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
- evidence_id: R045-CLASS
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Complete exact-key classifier row
  accessed_at: '2026-10-21T11:12:42.919781Z'
  support: supports
  summary: The owner reproduces the explicitly versioned NPClassifier2026-09-07 pathway/superclass/class
    assignments. This computational attribution is distinct from source biosynthetic
    class and experimentally verified mechanism.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: R045-IMODULON
  kind: database
  reference: https://imodulondb.org/
  locator: Previously retained complete28-dataset catalogue
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: No matching native organism/strain dataset occurs in the complete retained
    catalogue. No regulatory module is added from a different organism or from unasserted
    optional expression context.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
assessments:
- assessment_id: S045-A-IDENTITY
  area: identity
  topic: Exact natural product constitution
  outcome: supported
  summary: The original structure and X-ray illustration agree with the owner N1–C2′
    linked pentabrominated biindole nitrile. The exact natural product was isolated
    from native culture and field material; no tetrahedral stereochemistry is missing
    from the depicted graph. Independent authority and normalized molecular equivalence
    are documented in the identifier packet.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2021-MAIN
  - S045-2021-FIGURES
- assessment_id: S045-A-DEFINITION
  area: scope
  topic: Definition, native origin and disease attribution
  outcome: supported
  summary: The definition correctly identifies the cyanobacterial toxin and disease
    association. Pure-compound causality was tested in chickens; the eagle attribution
    also relies on ecological and chemical evidence. Neither Hydrilla nor birds are
    treated as biosynthetic producers.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2021-MAIN
  - S045-2021-FIGURES
- assessment_id: S045-A-OCCURRENCE
  area: evidence
  topic: Three provenance-specific species occurrences
  outcome: supported
  summary: LOTUS and ChEBI species-level occurrences cite the same original study
    and are supported. The CyanoMetDB row also points to that study; its additional
    strain wording is separately unresolved. Repetition across retained source provenance
    is not three independent experiments or a demonstrated duplicate-data defect.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-OCCURRENCE-ROWS
  - S045-2021-MAIN
- assessment_id: S045-A-CBT
  area: evidence
  topic: CBT1886 versus Thurmond2011 source context
  outcome: unknown
  summary: The native 2011 isolate is explicitly toxin-producing in the primary main
    text, but the relationship of the database label CBT1886 to that stock cannot
    be established from the inspected material. Keep the source attribution bounded;
    do not invent an alias, transfer a strain-specific experiment, or withdraw the
    occurrence on this access gap alone.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OCCURRENCE-ROWS
  - S045-2021-MAIN
  - S045-2021-SI-ACCESS
- assessment_id: S045-A-GRADES
  area: evidence
  topic: Native producer and locus experimental scope
  outcome: concern
  summary: The stored SOURCE_ASSERTION producer grade and CLUSTER_DEMONSTRATED enzymatic
    locus grade are consistent with their distinct scopes. The published cores map
    to MT225528.1 and the 2022 experiments establish exact AETX formation. The locus
    citation should route to that source while native origin retains the 2021 source;
    no native genetic or whole-cell heterologous grade upgrade follows.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-RAW
  - S045-2021-MAIN
  - S045-2022-MAIN
  - S045-2022-SI
  - S045-CORE-BRIDGE
  - S045-REFERENCE-LOADER
- assessment_id: S045-A-AETF
  area: graph
  topic: 'Steps 1–2 and graph edges 0–3: AetF'
  outcome: supported
  summary: AetF sequentially brominates L-tryptophan at positions 5 then 7. The 2021
    precursor experiment and 2022 full pathway agree with both substrate/product transitions.
    Activity is measured with recombinant protein and its cofactors, not inferred
    solely from annotation.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2021-FIGURES
  - S045-2022-MAIN
  - S045-2022-SI
- assessment_id: S045-A-AETE
  area: graph
  topic: 'Step 3 and graph edges 4–5: AetE'
  outcome: supported
  summary: PLP-dependent AetE converts 5-bromo-L-tryptophan to 5-bromoindole, and
    the SI independently detects pyruvate. The chemical node and direction are correct;
    the Rhea note describes a balanced database reaction rather than claiming all
    coproducts were independently measured in this particular assay.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2022-MAIN
  - S045-2022-SI
- assessment_id: S045-A-AETA
  area: graph
  topic: 'Steps 4–5 and graph edges 6–9: AetA'
  outcome: supported
  summary: AetA brominates 5-bromoindole at C3 and then C2 to give the exact 2,3,5-tribromoindole
    monomer. The assay uses SsuE/FAD/NADPH, and tested tryptophan substrates were
    not accepted. The historical SI accession maps to the current complete native
    core without substituting the truncated alternate genome annotation.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2022-MAIN
  - S045-2022-SI
  - S045-CORE-BRIDGE
- assessment_id: S045-A-AETD
  area: graph
  topic: 'Step 6 and graph edges 10–11: AetD'
  outcome: supported
  summary: AetD converts 5,7-dibromo-L-tryptophan to the exact nitrile; Fe(II) stimulation
    and independence from AetC are directly shown. Later primary isotope and oxygen
    experiments support the separately attributed Rhea glycolate/O2 note. Detailed
    rearrangement intermediates remain proposed and are not asserted by this owner.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2022-MAIN
  - S045-2022-SI
  - S045-2023-AETD
  - S045-2024-AETD
- assessment_id: S045-A-AETB
  area: graph
  topic: 'Step 7 and graph edges 12–14: AetB'
  outcome: supported
  summary: AetB accepts both explicitly named brominated monomers and yields AETX
    matching a synthetic standard, using ferredoxin, ferredoxin reductase and NADPH.
    The final N–C bond is clear from the structures. The paper itself calls the reaction
    biaryl coupling; that source-faithful term is not a confirmed chemical defect
    in this graph.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2022-MAIN
  - S045-2022-SI
- assessment_id: S045-A-GRAPH-SCOPE
  area: representation
  topic: Evidence snippets, accessory proteins and unassigned AetC
  outcome: supported
  summary: Both quoted experimental snippets occur in the 2022 original. Five enzyme
    nodes and eight chemical nodes support 15 edges and seven reactions. The graph
    omits an unproven AetC catalytic step and does not claim that spinach electron-transfer
    proteins or expression tags are native cyanobacterial pathway enzymes.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2022-MAIN
  - S045-2022-SI
  - S045-CORE-BRIDGE
- assessment_id: S045-A-NMR-WORDING
  area: representation
  topic: NMR-used flag rendered as structural confirmation
  outcome: concern
  summary: The source nmr_used=yes flag is faithfully present but is rendered as structure
    confirmed by yes. The wording should state the source-reported NMR use, without
    claiming an independent confirmation method or reviewer certification.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-OCCURRENCE-ROWS
  - S045-CYANO-EMITTER
- assessment_id: S045-A-CLASSIFICATION
  area: consistency
  topic: Natural-product, alkaloid and tryptophan-derived classifications
  outcome: supported
  summary: Native isolation supports Natural_product. The tryptophan-derived indole
    structure and pathway are compatible with the source class and the computed Alkaloids
    classification. Empty NPClassifier class/superclass slots and absent optional
    activity/target content are not defects. Source version and model provenance remain
    distinguishable from experimentally established chemistry.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-OCCURRENCE-ROWS
  - S045-2021-MAIN
  - S045-2022-MAIN
- assessment_id: S045-A-HISTORY
  area: provenance
  topic: Native status, curation history and optional expansion
  outcome: supported
  summary: The owner records initial seeding and later pathway/graph curation without
    claiming that these review artifacts changed its native status. No new mechanism,
    bioactivity measurement or optional protein addition is required to repair the
    two narrow defects. The unresolved CBT1886 detail remains a review limitation,
    not a fabricated negative result.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - S045-OWNER
  - S045-2021-SI-ACCESS
- assessment_id: P045-A-PROTEINS
  area: identity
  topic: Complete native enzyme reference sequences
  outcome: supported
  summary: All five exact reviewed proteins are native Thurmond2011 references and
    equal complete CDS translations from MT225528.1. The historical AetA accession
    has a verified merge/redirect crosswalk; the alternative truncated genome annotation
    does not invalidate the stored full protein.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-GENBANK
  - P045-PROTEIN-COMPARE
  - P045-AETA-LEGACY
  - P045-UNIPROT-AETA
  - P045-UNIPROT-AETB
  - P045-UNIPROT-AETD
  - P045-UNIPROT-AETE
  - P045-UNIPROT-AETF
- assessment_id: P045-A-CONSTRUCTS
  area: scope
  topic: Native protein identifiers versus recombinant assay preparations
  outcome: supported
  summary: Published codon-optimized inserts encode the same five core proteins, but
    the experiments use recombinant His-tagged preparations and MBP-AetB, with likely
    cleavage species in the latter sample. Existing enzyme identifiers appropriately
    identify the native cores; they do not encode exact whole assay constructs or
    native-culture purification.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-SI-CONSTRUCTS
  - P045-PROTEIN-COMPARE
  - P045-OWNER
- assessment_id: P045-A-REACTIONS
  area: evidence
  topic: Reaction identifiers, direction and chemical participants
  outcome: supported
  summary: All seven stored Rhea master reactions and their biochemical directions
    match current reviewed annotations. Cofactors/co-substrates in abbreviated notes
    are consistent with the full equations. Current reaction annotations do not independently
    prove which coproducts were measured in the original 2022 study.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-REACTION-COMPARE
  - P045-RHEA-82463
  - P045-RHEA-82467
  - P045-RHEA-82523
  - P045-RHEA-82527
  - P045-RHEA-82531
  - P045-RHEA-81787
  - P045-RHEA-82519
- assessment_id: P045-A-CHEMICAL-FORMS
  area: identity
  topic: Intermediate stereochemistry, substitution and protonation
  outcome: supported
  summary: The intermediate MOLs match the named positional indole substitutions and
    L-amino-acid stereochemistry. Neutral CHEBI16828 and Rhea CHEBI57912 are related
    L-tryptophan microspecies, not identical fixed-H graphs; both use the same intended
    L-tryptophan substrate framework. Brominated tryptophan entries encode zwitterions
    explicitly. No opposite stereoisomer or wrong positional intermediate was found.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-REACTION-COMPARE
  - P045-CHEBI-TRP
  - P045-CHEBI-ZWITTERION
  - P045-MOL-16828
  - P045-MOL-57912
  - P045-MOL-232362
  - P045-MOL-231978
  - P045-MOL-231979
  - P045-MOL-232363
  - P045-MOL-232364
  - P045-MOL-232365
  - P045-MOL-167886
- assessment_id: P045-A-ANNOTATION-SCOPE
  area: scope
  topic: Current annotation versus historical assay evidence
  outcome: supported
  summary: Reviewed status, full sequences and native accession bridges are verified.
    Later AetD coproduct/mechanism studies and AetF engineered-variant or structural
    studies remain separate citations and construct contexts; no expanded substrate
    scope, kinetic result or variant is silently transferred into the existing graph.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - P045-UNIPROT-AETD
  - P045-UNIPROT-AETF
  - P045-OWNER
- assessment_id: R045-IDENTITY
  area: identity
  topic: Exact chemical authority and source-concept resolution
  outcome: supported
  summary: The official parent graph, MIBiG, owner and Wikidata agree in standardized
    and fixed-H form. Three-star ChEBI167886 supports exact grounding; source-specific
    interpretation remains tied to primary evidence.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - R045-CHEM
  - R045-WIKI-COMPARE
  - R045-CHEBI
  - R045-MIBIG
  - R045-WIKI
  - R045-RAW
- assessment_id: R045-TAXON
  area: scope
  topic: Named native strain and species-level occurrences
  outcome: supported
  summary: Thurmond2011 is a strain node under the occurrence species. Wikidata maps
    that species correctly. The unresolved CBT1886 stock bridge is not supplied by
    these identifiers.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - R045-TAXON
  - R045-WIKI
  - R045-MIBIG
- assessment_id: R045-HISTORY
  area: provenance
  topic: Curated claims and unchanged native history
  outcome: supported
  summary: Both seed events and both2026-09-28 curation events remain intact, including
    the later two-substrate correction. Every existing pathway/graph claim is audited
    in the scientific/protein sections; current SEEDED status is not silently changed.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - R045-OWNER
- assessment_id: R045-CLASS
  area: provenance
  topic: Computational classification attribution
  outcome: supported
  summary: Classification is retained as a versioned computational output, not a newly
    demonstrated biosynthetic reaction.
  target_ids:
  - CHEBI:167886
  evidence_ids:
  - R045-CLASS
  - R045-OWNER
findings:
- finding_id: S045-F-CITATION
  issue_key: mibig-bgc0002643-compound1-claim-reference-routing
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Route the exact locus enzymatic claim to the 2022 study
  description: The locus Enzymatic assays claim inherits the 2021 isolation/AetF citation.
    Exact final-product enzymology was established in 2022 and is already correctly
    cited by the same owner pathway and graph. The defect is claim-local citation
    routing, not lack of support for the method, pathway or native species occurrence.
  target_ids:
  - CHEBI:167886
  field_paths:
  - biosynthetic_gene_clusters[0].evidence
  evidence_ids:
  - S045-RAW
  - S045-2021-MAIN
  - S045-2022-MAIN
  - S045-CORE-BRIDGE
  - S045-REFERENCE-LOADER
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Consumed exact-source citation-routing decision
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Complete raw-row guard and provenance-preserving application
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated producer and locus claims
- finding_id: S045-F-NMR-WORDING
  issue_key: cyanometdb-nmr-used-rendered-as-structure-confirmed
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Render the CyanoMetDB flag as reported NMR use
  description: The generated note structure confirmed by yes incorrectly casts a yes/no
    NMR-use flag as a confirmation method. The current primary paper does use NMR,
    but that does not make the emitter wording precise or convert the source flag
    into an independent verification. This is the same shared cause already identified
    in earlier campaign records.
  target_ids:
  - CHEBI:167886
  field_paths:
  - occurrences[1].evidence[0].notes
  evidence_ids:
  - S045-OCCURRENCE-ROWS
  - S045-CYANO-EMITTER
  - S045-2021-MAIN
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Shared CyanoMetDB occurrence-evidence wording
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: Preserved source NMR-used and strain fields
actions:
- action_id: S045-A-ROUTE-CITATION
  description: Add a consumed curation/mibig_claim_references.tsv decision for source_id
    BGC0002643:1 with expected_source_row_sha256 6b6ed3bd66bf39cc49b5da5c9d758c30af79161d20b0f9cb2987a3b6e50af46f,
    producer_reference PMID:33766860, locus_reference PMID:35142504 and source_reference
    PMID:35142504, with curator/date/rationale. Preserve the original imported citation
    in raw provenance. No method REPLACE or grade change is required. The current
    loader can apply this citation-only correction without a structural overlay.
  finding_ids:
  - S045-F-CITATION
  target_ids:
  - CHEBI:167886
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Consumed exact-source citation-routing decision
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Complete raw-row guard and provenance-preserving application
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Generated producer and locus claims
  generator: scripts/seed_from_sources.py and the existing guarded claim-reference
    loader
  acceptance_checks:
  - The complete source row matches the pinned SHA and a changed chemistry, strain,
    interval, source method or citation fails closed.
  - Producer evidence retains the 2021 native-isolation reference; the locus enzymatic
    claim cites the 2022 exact pathway study, with explicit curator-routing provenance.
  - Enzymatic assays, SOURCE_ASSERTION and CLUSTER_DEMONSTRATED remain unchanged;
    no native knockout, whole-cell heterologous production, axenic-culture claim or
    CBT1886 alias is introduced.
  - The seven pathway steps, all 13 nodes and 15 edges, molecular structure, source
    identifiers and raw inventory remain unchanged.
  - After implementation, deterministic regeneration, strict target validation and
    required repository gates pass.
- action_id: S045-A-NMR-WORDING
  description: 'Correct the shared CyanoMetDB emitter to report the literal source
    fact, for example NMR used according to CyanoMetDB: yes, and retain DATABASE_ASSERTION
    attribution. Preserve the imported nmr_used flag, DOI, CBT1886 context and taxon;
    do not use this wording repair to decide the unresolved strain relationship.'
  finding_ids:
  - S045-F-NMR-WORDING
  target_ids:
  - CHEBI:167886
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Shared CyanoMetDB occurrence-evidence wording
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/cyanometdb_occurrences.tsv
    role: Preserved source NMR-used and strain fields
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - The yes, no and blank source cases retain their respective meanings; no output
    says structure confirmed by yes or structure confirmed by no.
  - This target retains the same exact chemical key, occurrence reference, strain
    context, taxon and source attribution.
  - A focused generation check covers all three flag states and confirms that the
    shared fix does not duplicate or overwrite unrelated occurrence evidence.
  - Deterministic regeneration, strict validation and required repository gates pass
    after implementation.
limitations:
- The 2021 main body and original Figures 2–4 were inspected, but its supplementary
  methods were not recovered. The literal CBT1886 designation, its relationship to
  Thurmond2011 and detailed culture-purity documentation remain unverified; no strain
  alias or axenic status is inferred. This required gap makes the scientific review
  partial.
- The 2022 complete main scientific text and captions were read. SI reading covered
  coding and assay methods, selected network-table identifiers and synthesis pages
  21–25; original assay/synthesis pixels on pages 12, 17–20 and 24 were inspected.
  Later NMR pages and every sequence-network entry were not exhaustively reanalysed.
- Published codon-optimized coding inserts and complete native amino-acid cores agree,
  but vector tags, the AetB MBP fusion, host chaperones and accessory reductants remain
  experimental context. No complete recombinant plasmid or mutant allele reconstruction
  was performed.
- The 2023 and 2024 AetD main texts were read, including main methods and captions.
  Their supplementary files and original figure pixels were not independently inspected.
  Later mechanistic proposals are not upgraded to demonstrated elementary steps, and
  in-pathway chemistry does not mean an experiment in the native organism.
- Current chemical/taxonomic identifiers, molecular normalization, Rhea equations
  and full UniProt/native sequence receipts are supplied by the separate authority
  packet; this packet independently addresses primary scientific applicability. No
  repository files, saved bundles, campaign state, native status or history were edited.
- This packet verifies existing protein and reaction groundings. It does not independently
  reproduce enzyme assays or establish unasserted pathway steps, side products or
  native genetic necessity.
- Published coding cores and native proteins agree exactly; complete His-tag, linker,
  MBP and cleavage-product sequences were not reconstructed. An AetB fusion preparation
  with probable cleavage bands is not represented as a homogeneous untagged native
  protein.
- Current ChEBI API display SMILES omit indole [nH] details in these entries. Exact
  chemistry was verified from official MOLs and full InChI fields without silently
  editing the returned strings. Neutral and zwitterionic tryptophan share Standard
  identity but differ in fixed-H form.
- Current UniProt functional summaries integrate several publication years. Their
  later mechanistic, kinetic and engineered-variant claims are not experimental evidence
  for the 2022 citation alone.
- Database graph and taxon resolution do not substitute for the original experiments
  or establish uninspected historical stock identity.
- The neutral parent graph is the stored representation, not a measurement of solution
  protonation or tautomer populations.
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
- batch-005
```
